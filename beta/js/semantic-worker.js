/**
 * JW Sync — Semantic Search Worker ("Ask Your Library")
 *
 * v3: uses @huggingface/transformers (v3) which adds WebGPU acceleration.
 * On devices that support WebGPU (iOS 17+, Android Chrome 113+) the model
 * runs on the GPU — typically 10-30× faster than WASM on mobile.
 * Falls back to WASM automatically on unsupported browsers.
 *
 * Messages IN:
 *   { type:'load',  model:'en'|'multi' }       → load (or switch) the model
 *   { type:'embed', id, texts:[...] }          → embed a batch of strings
 * Messages OUT:
 *   { type:'modelProgress', file, loaded, total, progress }
 *   { type:'ready', model, device }            ('webgpu' | 'wasm')
 *   { type:'embedded', id, buffer, dim, count } (buffer transferred)
 *   { type:'error', id?, message }
 */

const MODELS = {
  en: 'Xenova/all-MiniLM-L6-v2',
  multi: 'Xenova/paraphrase-multilingual-MiniLM-L12-v2',
};

// v3 package — same jsDelivr CDN, new package name, adds WebGPU
const TRANSFORMERS_URL = 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.0.0';

let lib = null;
let extractor = null;
let currentModel = null;
let activeDevice = 'wasm';

async function ensureLib() {
  if (lib) return lib;
  lib = await import(TRANSFORMERS_URL);
  try { lib.env.allowLocalModels = false; } catch (_) {}
  try { lib.env.useBrowserCache = true; } catch (_) {}
  return lib;
}

self.onmessage = async (e) => {
  const msg = e.data || {};
  try {
    if (msg.type === 'load') {
      const key = MODELS[msg.model] ? msg.model : 'en';
      const repo = MODELS[key];
      const t = await ensureLib();

      if (!extractor || currentModel !== key) {
        const progressCb = (p) => {
          if (p && (p.status === 'progress' || p.status === 'download' || p.status === 'done')) {
            self.postMessage({
              type: 'modelProgress',
              status: p.status,
              file: p.file,
              loaded: p.loaded,
              total: p.total,
              progress: p.progress,
            });
          }
        };

        // Try GPU first. On supported devices this is 10-30× faster than WASM.
        // fp16 → fp32 → WASM fallback chain ensures something always works.
        const hasWebGPU = typeof navigator !== 'undefined' && !!navigator.gpu;
        let loaded = false;

        if (hasWebGPU) {
          for (const dtype of ['fp16', 'fp32']) {
            try {
              extractor = await t.pipeline('feature-extraction', repo, {
                device: 'webgpu',
                dtype,
                progress_callback: progressCb,
              });
              activeDevice = 'webgpu';
              loaded = true;
              break;
            } catch (_) {
              extractor = null;
            }
          }
        }

        if (!loaded) {
          // WASM path — always works, uses quantized int8 model (~23 MB)
          extractor = await t.pipeline('feature-extraction', repo, {
            device: 'wasm',
            dtype: 'q8',
            progress_callback: progressCb,
          });
          activeDevice = 'wasm';
        }

        currentModel = key;
      }

      self.postMessage({ type: 'ready', model: key, device: activeDevice });

    } else if (msg.type === 'embed') {
      if (!extractor) {
        self.postMessage({ type: 'error', id: msg.id, message: 'Model not loaded' });
        return;
      }
      // 600 chars ≈ 150 tokens — within the 256-token model limit, saves tokenisation time
      const texts = (msg.texts || []).map((s) => String(s == null ? '' : s).slice(0, 600));
      const out = await extractor(texts, { pooling: 'mean', normalize: true });
      const data = out.data instanceof Float32Array ? out.data : Float32Array.from(out.data);
      const dim = out.dims[out.dims.length - 1];
      const buf = data.buffer.slice(0);
      self.postMessage(
        { type: 'embedded', id: msg.id, buffer: buf, dim: dim, count: texts.length },
        [buf],
      );
    }
  } catch (err) {
    self.postMessage({ type: 'error', id: msg.id, message: (err && err.message) || String(err) });
  }
};

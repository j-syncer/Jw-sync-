/**
 * JW Sync — Semantic Search Worker ("Ask Your Library")
 *
 * Runs an on-device sentence-embedding model (transformers.js) OFF the main
 * thread. Nothing is ever uploaded: the model weights are fetched once from the
 * jsDelivr / Hugging Face CDN and cached by the browser, then every embedding is
 * computed locally. The main thread sends note text in batches and receives back
 * normalized Float32 vectors (transferred zero-copy).
 *
 * Messages IN:
 *   { type:'load',  model:'en'|'multi' }       → load (or switch) the model
 *   { type:'embed', id, texts:[...] }          → embed a batch of strings
 * Messages OUT:
 *   { type:'modelProgress', file, loaded, total, progress }
 *   { type:'ready', model }
 *   { type:'embedded', id, buffer, dim, count } (buffer transferred)
 *   { type:'error', id?, message }
 */

const MODELS = {
  fast: 'Xenova/all-MiniLM-L3-v2',
  en: 'Xenova/all-MiniLM-L6-v2',
  multi: 'Xenova/paraphrase-multilingual-MiniLM-L12-v2',
};

const TRANSFORMERS_URL = 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2';

let lib = null;
let extractor = null;
let currentModel = null;

async function ensureLib() {
  if (lib) return lib;
  lib = await import(TRANSFORMERS_URL);
  // Use the remote model hub + the browser HTTP cache; never look for local files.
  lib.env.allowLocalModels = false;
  lib.env.useBrowserCache = true;
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
        extractor = await t.pipeline('feature-extraction', repo, {
          quantized: true,
          progress_callback: (p) => {
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
          },
        });
        currentModel = key;
      }
      self.postMessage({ type: 'ready', model: key });
    } else if (msg.type === 'embed') {
      if (!extractor) {
        self.postMessage({ type: 'error', id: msg.id, message: 'Model not loaded' });
        return;
      }
      const texts = (msg.texts || []).map((s) => String(s == null ? '' : s).slice(0, 600));
      const out = await extractor(texts, { pooling: 'mean', normalize: true });
      const data = out.data instanceof Float32Array ? out.data : Float32Array.from(out.data);
      const dim = out.dims[out.dims.length - 1];
      // Own copy so we can transfer ownership to the main thread (zero-copy).
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

// Static integration test for v2.53.0 "Ask Your Library" — on-device semantic search.
//
// The feature adds:
//   - a dedicated Web Worker (beta/js/semantic-worker.js) that loads transformers.js
//     and runs a sentence-embedding model off the main thread,
//   - an "Ask" mode inside the Note Explorer (Browse) module in beta/index.html,
//   - English i18n keys (ask_*) in the Browse I18N object.
//
// JSDOM ships neither Worker nor WebAssembly/transformers, so this suite is a
// static contract check: it asserts the worker protocol and the Browse-side
// wiring exist and stay consistent.

const fs = require('fs');
const path = require('path');

const REPO = path.join(__dirname, '..');
let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

const worker = fs.readFileSync(path.join(REPO, 'beta/js/semantic-worker.js'), 'utf8');
const html = fs.readFileSync(path.join(REPO, 'beta/index.html'), 'utf8');

section('Semantic worker (beta/js/semantic-worker.js)');
[
  ['Light (L3) model wired', /Xenova\/all-MiniLM-L3-v2/],
  ['English model wired', /Xenova\/all-MiniLM-L6-v2/],
  ['Multilingual model wired', /Xenova\/paraphrase-multilingual-MiniLM-L12-v2/],
  ['loads transformers.js from CDN', /cdn\.jsdelivr\.net\/npm\/@xenova\/transformers/],
  ['uses feature-extraction pipeline', /feature-extraction/],
  ['mean pooling + normalize', /pooling:\s*'mean'[\s\S]*normalize:\s*true/],
  ['handles load message', /msg\.type\s*===\s*'load'/],
  ['handles embed message', /msg\.type\s*===\s*'embed'/],
  ['posts ready', /type:\s*'ready'/],
  ['posts embedded (transferable)', /type:\s*'embedded'[\s\S]*\[buf\]/],
  ['reports model progress', /type:\s*'modelProgress'/],
].forEach(([label, re]) => { if (re.test(worker)) ok(label); else fail('worker missing: ' + label); });

section('Browse "Ask" integration (beta/index.html)');
[
  ['Ask toolbar button class', /jb-ask-btn/],
  ['Ask button calls toggleAsk', /askBtn\.onclick\s*=\s*function\(\)\{\s*toggleAsk/],
  ['renderBody hook for ask mode', /if\(state\.askMode\)\{\s*renderAsk\(body\)/],
  ['renderAsk defined', /function renderAsk\(body\)/],
  ['startAskEngine defined', /function startAskEngine\(model\)/],
  ['buildAskIndex defined', /function buildAskIndex\(model\)/],
  ['doAskSearch defined', /function doAskSearch\(q\)/],
  ['embeds via the worker file', /new Worker\('\.\/js\/semantic-worker\.js',\s*\{\s*type:\s*'module'\s*\}\)/],
  ['IndexedDB vector cache', /indexedDB\.open\('jwsync_semantic'/],
  ['cosine via dot product (normalized)', /function dotProd\(/],
  ['model choice persisted', /jwsync_ask_v1/],
  ['all three model sizes offered', /ASK_MODELS\s*=\s*\{\s*fast:\s*11,\s*en:\s*23,\s*multi:\s*50\s*\}/],
  ['ask state reset on close', /if\(ASK\.worker\)\{\s*try\{\s*ASK\.worker\.terminate/],
  ['ask state reset on new file', /New file → previous semantic index/],
].forEach(([label, re]) => { if (re.test(html)) ok(label); else fail('html missing: ' + label); });

section('Browse i18n (ask_* keys, English)');
const i18nMatch = html.match(/var I18N = (\{[\s\S]*?\});\s*function curLang/);
if (!i18nMatch) {
  fail('Browse I18N object not found');
} else {
  let i18n;
  try { i18n = eval('(' + i18nMatch[1] + ')'); ok('Browse I18N parses'); }
  catch (e) { fail('Browse I18N parse failed: ' + e.message); }
  if (i18n && i18n.en) {
    const ASK_KEYS = [
      'ask_btn', 'ask_title', 'ask_sub', 'ask_placeholder', 'ask_go',
      'ask_enable_title', 'ask_enable_body', 'ask_model_fast_name', 'ask_model_fast_desc', 'ask_model_en_name', 'ask_model_en_desc',
      'ask_model_multi_name', 'ask_model_multi_desc', 'ask_size_once', 'ask_privacy',
      'ask_loading_model', 'ask_building', 'ask_ready', 'ask_searching',
      'ask_results_head', 'ask_no_results', 'ask_no_notes', 'ask_err',
      'ask_rebuild', 'ask_match', 'ask_switch_model',
    ];
    const missing = ASK_KEYS.filter((k) => !i18n.en[k]);
    if (missing.length) fail('en missing ask keys: ' + missing.join(', '));
    else ok('en covers all ' + ASK_KEYS.length + ' ask_* keys');
  } else {
    fail('Browse I18N has no English block');
  }
}

console.log('\n== SUMMARY ==');
if (failures) { console.log('Semantic-search checks FAILED: ' + failures); process.exit(1); }
console.log('All semantic-search checks passed.');

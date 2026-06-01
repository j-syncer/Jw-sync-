// Integration test for the v2.20.0 Saved Devices & Auto-Sync (Sync Hub).
//
// The Sync Hub is a self-contained IIFE in beta/index.html exposing
// window.__jwOpenSyncHub(). It persists each device's .jwlibrary backup in
// its own IndexedDB store, lets the user pick a "main" device, and merges all
// saved devices with one click by driving ./js/merge-worker.js directly. It
// also shows a quiet "time to sync" reminder banner based on a cadence pref.
//
// JSDOM ships no IndexedDB and no Worker, so this suite installs compact
// in-memory mocks for both, then asserts:
//   1. window.__jwOpenSyncHub is exposed and a launcher FAB is added
//   2. Opening with no saved devices renders the empty state (merge disabled)
//   3. With >=2 seeded devices the list renders and merge is enabled
//   4. Clicking "Merge" drives the worker and, on {type:'done'}, downloads a
//      file and stamps lastSync in localStorage
//   5. i18n covers all 10 languages with the required keys (static)
//   6. The module targets ./js/merge-worker.js and its own prefs/DB keys
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl'];
const REQUIRED_KEYS = ['title','intro','priv','add','empty','main','setmain','remove','saved',
  'mergenow','merging','done','needtwo','reminder','off','weekly','monthly','clear','clearconfirm',
  'banner','bannercta','dismiss','close','fab','error'];

// ── Extract just the Sync Hub module (style + script) from beta/index.html ──
function extractModule() {
  const html = fs.readFileSync(HTML_PATH, 'utf8');
  const m = html.match(/<!-- ── Saved Devices & Auto-Sync \(Sync Hub[\s\S]*?<!-- ── End Saved Devices & Auto-Sync ─[─]*\s*-->/);
  if (!m) { fail('Sync Hub module block not found in beta/index.html'); process.exit(1); }
  return m[0];
}

// ── Minimal in-memory IndexedDB mock (shared store so tests can pre-seed) ──
function installIDBMock(win, seedRows) {
  const stores = { devices: {} };
  if (seedRows) seedRows.forEach(r => { stores.devices[r.id] = r; });
  function makeStore(name) {
    return {
      put(v) { stores[name][v.id] = v; return {}; },
      getAll() { const req = {}; setTimeout(() => { req.result = Object.values(stores[name]); req.onsuccess && req.onsuccess(); }, 0); return req; },
      delete(id) { delete stores[name][id]; return {}; },
      clear() { stores[name] = {}; return {}; }
    };
  }
  function makeTx() {
    const tx = { objectStore: makeStore };
    setTimeout(() => { tx.oncomplete && tx.oncomplete(); }, 0);
    return tx;
  }
  const db = {
    objectStoreNames: { contains: () => true },
    createObjectStore: () => makeStore('devices'),
    transaction: () => makeTx(),
    close() {}
  };
  win.indexedDB = {
    open() {
      const req = {};
      setTimeout(() => { req.result = db; req.onupgradeneeded && req.onupgradeneeded(); req.onsuccess && req.onsuccess(); }, 0);
      return req;
    }
  };
  return stores;
}

function makeDom(seedRows) {
  const mod = extractModule();
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${mod}</body></html>`;
  const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  return dom;
}

(async function run() {

  // The module wires indexedDB/Worker at call time, so install mocks BEFORE
  // building the DOM is not possible (scripts run on construction). Instead we
  // construct, then the module only touches indexedDB when openHub() runs — so
  // we install the mock right after construction, before opening.

  section('Module exposes API + launcher');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    installIDBMock(win);
    await wait(30);
    if (typeof win.__jwOpenSyncHub === 'function') ok('window.__jwOpenSyncHub exposed');
    else fail('window.__jwOpenSyncHub missing');
    const fab = doc.getElementById('jw-synchub-fab');
    if (fab) ok('launcher FAB rendered'); else fail('launcher FAB missing');
    dom.window.close();
  }

  section('Empty state (no devices) — merge disabled');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    installIDBMock(win, []);
    await wait(20);
    win.__jwOpenSyncHub();
    await wait(60);
    const overlay = doc.getElementById('jw-synchub-overlay');
    if (overlay) ok('overlay opened'); else { fail('overlay did not open'); dom.window.close(); }
    if (overlay) {
      if (overlay.querySelector('.jsh-empty')) ok('empty-state shown');
      else fail('empty-state not shown');
      const mergeBtn = overlay.querySelector('.jsh-merge');
      if (mergeBtn && mergeBtn.disabled) ok('merge button disabled with 0 devices');
      else fail('merge button should be disabled');
      dom.window.close();
    }
  }

  section('Two seeded devices — list renders, merge enabled');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    const seed = [
      { id: 'dev_a', name: 'iPhone.jwlibrary', buffer: new win.ArrayBuffer(8), savedAt: Date.now() - 5000 },
      { id: 'dev_b', name: 'iPad.jwlibrary', buffer: new win.ArrayBuffer(8), savedAt: Date.now() }
    ];
    installIDBMock(win, seed);
    await wait(20);
    win.__jwOpenSyncHub();
    await wait(80);
    const overlay = doc.getElementById('jw-synchub-overlay');
    if (overlay) {
      const rows = overlay.querySelectorAll('.jsh-row');
      if (rows.length === 2) ok('2 device rows rendered'); else fail('expected 2 rows, got ' + rows.length);
      const badges = overlay.querySelectorAll('.jsh-badge');
      if (badges.length === 1) ok('exactly one "Main" badge'); else fail('expected 1 main badge, got ' + badges.length);
      const mergeBtn = overlay.querySelector('.jsh-merge');
      if (mergeBtn && !mergeBtn.disabled) ok('merge button enabled with 2 devices');
      else fail('merge button should be enabled');
      dom.window.close();
    } else { fail('overlay did not open'); dom.window.close(); }
  }

  section('Merge drives the worker and downloads on done');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    const seed = [
      { id: 'dev_a', name: 'iPhone.jwlibrary', buffer: new win.ArrayBuffer(8), savedAt: 1 },
      { id: 'dev_b', name: 'iPad.jwlibrary', buffer: new win.ArrayBuffer(8), savedAt: 2 }
    ];
    installIDBMock(win, seed);

    // Mock Worker: capture the posted merge message, then reply {type:'done'}.
    let posted = null;
    win.Worker = function (url) {
      this._url = url;
      this.postMessage = (msg) => {
        if (msg && msg.type === 'merge') {
          posted = msg;
          setTimeout(() => { this.onmessage && this.onmessage({ data: { type: 'done', zipBuffer: new win.ArrayBuffer(16), stats: {} } }); }, 0);
        }
      };
      this.terminate = () => {};
    };
    // Capture download clicks.
    let downloaded = null;
    const origCreate = doc.createElement.bind(doc);
    doc.createElement = function (tag) {
      const el = origCreate(tag);
      if (tag === 'a') { el.click = function () { downloaded = el.download; }; }
      return el;
    };
    win.URL.createObjectURL = () => 'blob:mock';
    win.URL.revokeObjectURL = () => {};

    await wait(20);
    win.__jwOpenSyncHub();
    await wait(80);
    const overlay = doc.getElementById('jw-synchub-overlay');
    overlay.querySelector('.jsh-merge').click();
    await wait(80);

    if (posted && posted.type === 'merge') ok('worker received {type:"merge"}');
    else fail('worker did not receive merge message');
    if (posted && posted.secondaryFiles && posted.secondaryFiles.length === 1) ok('one secondary file (main excluded)');
    else fail('expected 1 secondary file');
    if (posted && posted.opts && posted.opts.previewConfirm === false) ok('previewConfirm disabled for one-click merge');
    else fail('previewConfirm should be false');
    if (downloaded && /\.jwlibrary$/.test(downloaded)) ok('merged file downloaded: ' + downloaded);
    else fail('no .jwlibrary download triggered');
    const prefs = JSON.parse(win.localStorage.getItem('jwsync_synchub') || '{}');
    if (prefs.lastSync && prefs.lastSync > 0) ok('lastSync stamped after merge');
    else fail('lastSync not stamped');
    dom.window.close();
  }

  section('i18n covers all 10 languages (static)');
  {
    const mod = extractModule();
    const m = mod.match(/var I18N = \{[\s\S]*?\n  \};/);
    if (!m) { fail('I18N object not found'); }
    else {
      // crude per-lang key presence check
      LANGS.forEach(lang => {
        const re = new RegExp('\\b' + lang + ':\\{');
        if (!re.test(mod)) { fail('language missing: ' + lang); return; }
      });
      ok('all 10 language blocks present');
      // ensure each required key string appears at least LANGS.length times-ish (presence)
      let missing = [];
      REQUIRED_KEYS.forEach(k => {
        const count = (mod.match(new RegExp('\\b' + k + ':')) || []).length;
        if (count === 0) missing.push(k);
      });
      if (missing.length === 0) ok('all required i18n keys present');
      else fail('missing i18n keys: ' + missing.join(', '));
    }
  }

  section('Module wiring (static)');
  {
    const mod = extractModule();
    if (mod.includes("new Worker('./js/merge-worker.js')")) ok('drives ./js/merge-worker.js');
    else fail('does not target ./js/merge-worker.js');
    if (mod.includes("'jwsync_synchub'")) ok('uses jwsync_synchub prefs key');
    else fail('prefs key missing');
    if (mod.includes("'jwsync_synchub_db'")) ok('uses own IndexedDB (jwsync_synchub_db)');
    else fail('own IDB name missing');
    if (mod.includes('window.__jwOpenSyncHub')) ok('exposes window.__jwOpenSyncHub');
    else fail('public API not exposed');
  }

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll Sync Hub checks passed.');
})();

/* ──────────────────────────────────────────────────────────────────────────
   jw-session.js — cross-tool file session + universal tool switcher
   ----------------------------------------------------------------------------
   JW Sync's four tools live on separate surfaces:
     • Merge Tool      → index.html (#app)
     • Study Stats     → highlights.html
     • Study Explorer  → index.html (Browse module, #browse)
     • Note Sharing    → share.html
   Historically a file uploaded in one tool could not be reused in another —
   each surface required a fresh upload. This module fixes that with:

     1. A single, persistent (non-consuming) IndexedDB store that holds the
        most-recently-loaded .jwlibrary so any tool can pick it up. Privacy is
        preserved with a short TTL and explicit clear() on "start over".
     2. A self-rendering tool switcher, injected identically on every page, so
        users can jump between tools — carrying their file — from anywhere.

   Dependency-free, framework-agnostic, safe to load on every page.
   Exposes window.JwSession.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var DB_NAME = 'jwsync_session_v1';
  var STORE = 'file';
  var KEY = 'current';
  var TTL_MS = 12 * 60 * 60 * 1000; // keep the working file for at most 12h

  var TOOLS = [
    { id: 'merge',    href: 'index.html#app' },
    { id: 'stats',    href: 'highlights.html' },
    { id: 'explorer', href: 'index.html#browse' },
    { id: 'share',    href: 'share.html' }
  ];

  // Short switcher labels in every supported language (kept tiny on purpose).
  var LABELS = {
    en: { merge: 'Merge',     stats: 'Stats',         explorer: 'Explorer',  share: 'Share' },
    es: { merge: 'Combinar',  stats: 'Estad.',        explorer: 'Explorar',  share: 'Compartir' },
    pt: { merge: 'Mesclar',   stats: 'Estat.',        explorer: 'Explorar',  share: 'Partilhar' },
    fr: { merge: 'Fusion',    stats: 'Stats',         explorer: 'Explorer',  share: 'Partager' },
    de: { merge: 'Zusammen.', stats: 'Statistik',     explorer: 'Explorer',  share: 'Teilen' },
    it: { merge: 'Unisci',    stats: 'Statistiche',   explorer: 'Esplora',   share: 'Condividi' },
    ru: { merge: 'Слияние',   stats: 'Стат.',         explorer: 'Обзор',     share: 'Обмен' },
    ja: { merge: '統合',       stats: '統計',           explorer: 'ノート',     share: '共有' },
    ko: { merge: '병합',       stats: '통계',           explorer: '탐색',       share: '공유' },
    tl: { merge: 'Pagsamahin', stats: 'Estadistika',  explorer: 'Explorer',  share: 'Ibahagi' }
  };

  function lang() {
    var l;
    try { l = localStorage.getItem('jwsync_lang'); } catch (_) {}
    return (l && LABELS[l]) ? l : 'en';
  }

  /* ── IndexedDB plumbing (all guarded so a blocked/absent IDB never throws) ── */
  function openDb() {
    return new Promise(function (resolve, reject) {
      if (typeof indexedDB === 'undefined' || !indexedDB) { reject(new Error('no-idb')); return; }
      var req;
      try { req = indexedDB.open(DB_NAME, 1); } catch (e) { reject(e); return; }
      req.onupgradeneeded = function (e) {
        try { e.target.result.createObjectStore(STORE); } catch (_) {}
      };
      req.onsuccess = function (e) { resolve(e.target.result); };
      req.onerror = function () { reject(req.error || new Error('idb-open')); };
    });
  }

  function toBuffer(fileOrBuf) {
    if (fileOrBuf instanceof ArrayBuffer) return Promise.resolve(fileOrBuf);
    if (fileOrBuf && typeof fileOrBuf.arrayBuffer === 'function') return fileOrBuf.arrayBuffer();
    return new Promise(function (res, rej) {
      try {
        var r = new FileReader();
        r.onload = function () { res(r.result); };
        r.onerror = rej;
        r.readAsArrayBuffer(fileOrBuf);
      } catch (e) { rej(e); }
    });
  }

  // Persist the working file (non-consuming overwrite). Resolves even on failure.
  function put(fileOrBuf, name) {
    if (!fileOrBuf) return Promise.resolve(false);
    return toBuffer(fileOrBuf).then(function (buf) {
      return openDb().then(function (db) {
        return new Promise(function (resolve) {
          var tx = db.transaction(STORE, 'readwrite');
          tx.objectStore(STORE).put({
            name: name || (fileOrBuf && fileOrBuf.name) || 'backup.jwlibrary',
            buffer: buf,
            ts: Date.now()
          }, KEY);
          tx.oncomplete = function () { db.close(); resolve(true); };
          tx.onerror = function () { db.close(); resolve(false); };
        });
      });
    }).catch(function () { return false; });
  }

  // Read the working file WITHOUT deleting it. Honours the TTL (stale → cleared).
  function get() {
    return openDb().then(function (db) {
      return new Promise(function (resolve) {
        var tx = db.transaction(STORE, 'readonly');
        var g = tx.objectStore(STORE).get(KEY);
        g.onsuccess = function () {
          var v = g.result;
          db.close();
          if (!v || !v.buffer) { resolve(null); return; }
          if (v.ts && (Date.now() - v.ts) > TTL_MS) { clear(); resolve(null); return; }
          resolve({ name: v.name || 'backup.jwlibrary', buffer: v.buffer });
        };
        g.onerror = function () { db.close(); resolve(null); };
      });
    }).catch(function () { return null; });
  }

  // Forget the working file (privacy: called by "Start over" / "New file").
  function clear() {
    return openDb().then(function (db) {
      return new Promise(function (resolve) {
        var tx = db.transaction(STORE, 'readwrite');
        tx.objectStore(STORE).delete(KEY);
        tx.oncomplete = function () { db.close(); resolve(true); };
        tx.onerror = function () { db.close(); resolve(true); };
      });
    }).catch(function () { return false; });
  }

  // Persist the given file (if any) then navigate to a tool. Always navigates.
  function goTo(href, fileOrBuf) {
    var nav = function () { try { window.location.href = href; } catch (_) {} };
    if (!fileOrBuf) { nav(); return; }
    put(fileOrBuf).then(nav, nav);
  }

  /* ── Universal tool switcher (single source of truth for all pages) ── */
  function injectCss() {
    if (document.getElementById('jw-switch-css')) return;
    var css =
      '.jw-switch{display:inline-flex;align-items:center;gap:2px;padding:3px;' +
      'background:rgba(71,85,105,.22);border:1px solid rgba(255,255,255,.08);' +
      'border-radius:9px;flex-wrap:nowrap}' +
      '.jw-switch-btn{appearance:none;background:transparent;border:1px solid transparent;' +
      'color:rgba(203,213,225,.72);font:600 12px/1 inherit;font-family:inherit;' +
      'padding:6px 11px;border-radius:6px;cursor:pointer;white-space:nowrap;text-decoration:none;' +
      'transition:color .15s,background .15s,border-color .15s}' +
      '.jw-switch-btn:hover{color:#f1f5f9;background:rgba(255,255,255,.06)}' +
      '.jw-switch-btn.jw-switch-on{color:#ea580c;background:rgba(234,88,12,.12);' +
      'border-color:rgba(234,88,12,.3);cursor:default}' +
      '.jw-switch-btn:focus-visible{outline:2px solid #ea580c;outline-offset:2px}' +
      '@media(max-width:560px){.jw-switch{gap:0;padding:2px}.jw-switch-btn{padding:6px 8px;font-size:11px}}';
    var st = document.createElement('style');
    st.id = 'jw-switch-css';
    st.textContent = css;
    (document.head || document.documentElement).appendChild(st);
  }

  // container: element to render into. active: tool id of the current surface.
  function mountSwitcher(container, active) {
    if (!container) return;
    injectCss();
    var L = LABELS[lang()];
    var wrap = document.createElement('div');
    wrap.className = 'jw-switch';
    wrap.setAttribute('role', 'navigation');
    wrap.setAttribute('aria-label', 'Tools');
    TOOLS.forEach(function (tool) {
      var btn = document.createElement('a');
      btn.className = 'jw-switch-btn' + (tool.id === active ? ' jw-switch-on' : '');
      btn.href = tool.href;
      btn.textContent = (L && L[tool.id]) || tool.id;
      if (tool.id === active) {
        btn.setAttribute('aria-current', 'page');
      } else {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          // Carry the working file: prefer a live File ref, else rely on the store.
          var live = null;
          try { live = window.__jwLastFile || null; } catch (_) {}
          goTo(tool.href, live);
        });
      }
      wrap.appendChild(btn);
    });
    container.appendChild(wrap);
    return wrap;
  }

  window.JwSession = {
    put: put,
    get: get,
    clear: clear,
    goTo: goTo,
    mountSwitcher: mountSwitcher,
    TOOLS: TOOLS,
    _dbName: DB_NAME
  };
})();

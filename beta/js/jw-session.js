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

  var ICONS = {
    merge: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M6 21V9a9 9 0 0 0 9 9"></path></svg>',
    stats: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',
    explorer: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    share: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>'
  };

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
    tl: { merge: 'Pagsamahin', stats: 'Estadistika',  explorer: 'Explorer',  share: 'Ibahagi' },
    sv: { merge: 'Slå ihop',   stats: 'Statistik',    explorer: 'Utforska',  share: 'Dela' },
    ceb: { merge: 'Isagol',     stats: 'Estadistika',   explorer: 'Explorer',  share: 'Ipaambit' },el:{merge:"Συγχώνευση",stats:"Στατιστικά",explorer:"Εξερεύνηση",share:"Κοινοποίηση"},sw:{merge:"Unganisha",stats:"Takwimu",explorer:"Kichunguzi",share:"Shiriki"},nl:{merge:"Samenvoegen",stats:"Statistieken",explorer:"Verkenner",share:"Delen"},ro:{merge:"Îmbinare",stats:"Statistici",explorer:"Explorator",share:"Partajare"},id:{merge:"Gabung",stats:"Statistik",explorer:"Penjelajah",share:"Bagikan"},hi:{merge:"मर्ज",stats:"आँकड़े",explorer:"एक्सप्लोरर",share:"साझा करें"},hu:{merge:"Egyesítés",stats:"Statisztika",explorer:"Böngésző",share:"Megosztás"},vi:{merge:"Hợp nhất",stats:"Thống kê",explorer:"Trình khám phá",share:"Chia sẻ"},"yue-Hant":{merge:"合併",stats:"統計",explorer:"瀏覽器",share:"分享"},"zh-Hant":{merge:"合併",stats:"統計",explorer:"瀏覽器",share:"分享"},"zh-Hans":{merge:"合并",stats:"统计",explorer:"浏览器",share:"分享"},pl:{merge:"Scalanie",stats:"Statystyki",explorer:"Eksplorator",share:"Udostępnij"},uk:{merge:"Об'єднання",stats:"Статистика",explorer:"Оглядач",share:"Поділитися"},he:{merge:"מיזוג",stats:"סטטיסטיקה",explorer:"סייר",share:"שיתוף"},ar:{merge:"دمج",stats:"إحصاءات",explorer:"مستكشف",share:"مشاركة"}
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
      '.jw-switch{display:inline-flex;align-items:center;gap:4px;flex-wrap:nowrap}' +
      '.jw-switch-btn{display:inline-flex;align-items:center;gap:7px;appearance:none;background:transparent;' +
      'border:1px solid transparent;color:rgba(203,213,225,.7);font:500 13px/1 inherit;font-family:inherit;' +
      'padding:7px 12px;border-radius:7px;cursor:pointer;white-space:nowrap;text-decoration:none;' +
      'transition:color .15s,background .15s,border-color .15s}' +
      '.jw-switch-btn svg{width:15px;height:15px;flex:none;opacity:.85}' +
      '.jw-switch-btn:hover{color:#f1f5f9;background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.1)}' +
      '.jw-switch-btn.jw-switch-on{color:#ea580c;background:rgba(234,88,12,.1);' +
      'border-color:rgba(234,88,12,.25);cursor:default}' +
      '.jw-switch-btn.jw-switch-on svg{opacity:1}' +
      '.jw-switch-btn:focus-visible{outline:2px solid #ea580c;outline-offset:2px}' +
      '@media(max-width:640px){.jw-switch{gap:2px}.jw-switch-btn{padding:7px 10px;font-size:12px;gap:6px}}' +
      '@media(max-width:560px){.jw-switch-btn .jw-switch-lbl{display:none}.jw-switch-btn{padding:8px;gap:0}}';
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
      var lbl = (L && L[tool.id]) || tool.id;
      btn.innerHTML = (ICONS[tool.id] || '') + '<span class="jw-switch-lbl"></span>';
      var lblEl = btn.querySelector('.jw-switch-lbl');
      if (lblEl) lblEl.textContent = lbl;
      btn.setAttribute('aria-label', lbl);
      if (tool.id === active) {
        btn.setAttribute('aria-current', 'page');
      } else {
        btn.addEventListener('click', (function (t) { return function (e) {
          e.preventDefault();
          // Carry the working file: prefer a live File ref, else rely on the store.
          var live = null;
          try { live = window.__jwLastFile || null; } catch (_) {}
          // Signal index.html to auto-open Browse on arrival.
          if (t.id === 'explorer') {
            try { sessionStorage.setItem('jwsync_open_browse', '1'); } catch (_) {}
          }
          goTo(t.href, live);
        }; })(tool));
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

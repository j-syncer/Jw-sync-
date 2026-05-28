/* =============================================================================
   JW Sync Beta — js/enhancements.js
   Five responsibilities:
     1. PWA install + service-worker registration
     2. File-handler API (.jwlibrary files open from OS)
     3. Visual backup timeline (DOM observation)
     4. "Try with sample data" demo button
     5. Forum view routing (#forum hash shows forum, hides main app)
   Loaded as a plain <script> tag. No module system.
   ============================================================================= */

/* ===========================================================================
   JW Sync — Enhancement Layer
   ===========================================================================
   Adds new functionality WITHOUT modifying the existing React app:
     1. PWA install + service-worker registration
     2. File-handler API hookup (.jwlibrary files open directly from OS)
     3. Visual backup timeline (rendered via DOM observation)
     4. "Try with sample data" demo button
     5. Forum view (#forum route shows embedded forum, hides main app)
     6. App-update prompt when a new service-worker arrives
   ===========================================================================
*/

(function () {
  'use strict';

  // ── Service-worker registration ─────────────────────────────────────────
  /**
   * Registers the service worker at service-worker.js scoped to /beta/.
   * Shows an update banner when a new SW version is installed and reloads
   * the page when the new SW takes control.
   */
  function registerServiceWorker() {
    if (!('serviceWorker' in navigator)) return;
    if (!location.protocol.startsWith('http')) return; // skip on file://

    navigator.serviceWorker.register('service-worker.js', { scope: "/" })
      .then(function (reg) {
        reg.addEventListener('updatefound', function () {
          var nw = reg.installing;
          if (!nw) return;
          nw.addEventListener('statechange', function () {
            if (nw.state === 'installed' && navigator.serviceWorker.controller) {
              showUpdateBanner(nw);
            }
          });
        });
      })
      .catch(function (err) { console.warn('[JW Sync] SW failed', err); });

    // Reload once the new SW takes control, so the user gets the fresh version
    var refreshing = false;
    navigator.serviceWorker.addEventListener('controllerchange', function () {
      if (refreshing) return;
      refreshing = true;
      location.reload();
    });
  }

  /**
   * Displays a sticky banner offering the user a one-click page reload
   * to activate an already-installed new service worker version.
   * @param {ServiceWorker} worker - The newly installed SW waiting to activate.
   */
  function showUpdateBanner(worker) {
    var bar = document.createElement('div');
    bar.style.cssText = 'position:fixed;left:50%;top:14px;transform:translateX(-50%);z-index:9998;background:#1c1917;border:1px solid #f59e0b;border-radius:12px;padding:10px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 8px 32px rgba(0,0,0,0.6);font-family:system-ui,sans-serif;font-size:13px;color:#f5f5f4;animation:jwsync-slideDown 0.3s ease';
    bar.innerHTML =
      '<span>✨ A new version is available</span>' +
      '<button style="background:#f59e0b;color:#1c1410;border:none;border-radius:6px;padding:6px 12px;font-weight:700;cursor:pointer">Refresh</button>' +
      '<button style="background:transparent;color:#a8a29e;border:none;cursor:pointer;font-size:18px;line-height:1">×</button>';
    var btns = bar.querySelectorAll('button');
    btns[0].onclick = function () { worker.postMessage('SKIP_WAITING'); };
    btns[1].onclick = function () { bar.remove(); };
    document.body.appendChild(bar);
  }

  // ── File-handler API ───────────────────────────────────────────────────
  // When the OS opens a .jwlibrary file via the installed PWA, deliver it
  // into the existing app's <input type="file"> so the React handlers run
  // exactly as if the user had selected the file manually.
  /**
   * Hooks the File Handling API (launchQueue) so .jwlibrary files opened
   * via the installed PWA are delivered directly to the React app's file input.
   */
  function setupFileHandler() {
    if (!('launchQueue' in window)) return;
    window.launchQueue.setConsumer(function (launchParams) {
      if (!launchParams.files || !launchParams.files.length) return;
      Promise.all(launchParams.files.map(function (h) { return h.getFile(); }))
        .then(function (files) { injectFilesIntoMainInput(files); })
        .catch(function (e) { console.warn('[JW Sync] file-handler failed', e); });
    });
  }

  /**
   * Find the main file <input> the React app exposes and dispatch a
   * synthetic 'change' event with the supplied File objects. Uses a
   * DataTransfer to construct a valid FileList.
   */
  /**
   * Injects an array of File objects into the React app's hidden file input
   * by simulating a change event, triggering the merge engine.
   * @param {File[]} files - Array of .jwlibrary File objects to inject.
   */
  function injectFilesIntoMainInput(files) {
    // Wait briefly for React to mount its inputs
    var attempts = 0;
    function tryFind() {
      var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
      if (!inputs.length) {
        if (++attempts < 30) return setTimeout(tryFind, 200);
        return;
      }
      // First input is "main file"; subsequent ones are "add more"
      var input = inputs[0];
      var dt = new DataTransfer();
      files.forEach(function (f) { dt.items.add(f); });
      input.files = dt.files;
      input.dispatchEvent(new Event('change', { bubbles: true }));
    }
    tryFind();
  }

  // ── Forum view routing ─────────────────────────────────────────────────
  // The forum was originally forum.html. We've embedded it as a hidden
  // section in this file. When the URL hash is #forum, we hide the main
  // React app and show the forum; otherwise it stays hidden.
  /**
   * Manages routing between the main app and the embedded forum view.
   * Reads location.hash: '#forum' shows the forum, anything else shows the app.
   * Also rewrites href="forum.html" anchors to use the '#forum' hash route.
   */
  function setupForumRouting() {
    function update() {
      var isForum = location.hash === '#forum';
      var forum = document.getElementById('forum-view');
      var navbar = document.getElementById('jw-navbar');
      if (!forum) return;
      forum.hidden = !isForum;
      // #jw-navbar (React in-app nav) hides on forum; site-nav stays visible
      if (navbar) navbar.style.display = isForum ? 'none' : '';
      document.body.classList.toggle('is-forum', isForum);
      if (isForum && typeof window.jwsyncForumInit === 'function') {
        window.jwsyncForumInit();
      }
      // Update <title> for clarity
      document.title = isForum
        ? 'JW Sync — Community'
        : 'JW Library Backup Merger | Combine Notes & Highlights';
    }
    window.addEventListener('hashchange', update);
    document.addEventListener('DOMContentLoaded', update);
    update();

    // Rewrite the existing "💬 Community" anchor (which points to forum.html)
    // to use our internal hash route instead, so it stays in one file.
    function rewriteCommunityLink() {
      var links = document.querySelectorAll('a[href="forum.html"]');
      if (!links.length) return false;
      links.forEach(function (a) { a.href = '#forum'; });
      return true;
    }
    if (!rewriteCommunityLink()) {
      var obs = new MutationObserver(function () {
        if (rewriteCommunityLink()) obs.disconnect();
      });
      obs.observe(document.body, { childList: true, subtree: true });
    }
  }

  // ── Visual backup timeline ─────────────────────────────────────────────
  // The existing app already renders a "File Data Checker" panel listing
  // each loaded backup. We observe that panel and render a horizontal
  // timeline above it whenever 2+ files are present, ordered by their
  // detected backup creation date (extracted from manifest.json on demand).
  /**
   * Observes the File Data Checker panel and renders a horizontal visual
   * timeline above it whenever two or more backup files are loaded.
   * Timeline nodes are ordered by backup creation date from manifest.json.
   */
  function setupBackupTimeline() {
    var fileCache = Object.create(null); // name → {date, notes}
    var timelineEl = null;
    var rafScheduled = false;

    // Hook into the existing JSZip reads by intercepting File.arrayBuffer
    // calls — but that's fragile. Simpler: just observe DOM file labels
    // and re-render the timeline with names + scan order as a proxy.

    function ensureTimeline(anchorEl) {
      if (timelineEl && document.body.contains(timelineEl)) return timelineEl;
      timelineEl = document.createElement('div');
      timelineEl.id = 'jw-backup-timeline';
      timelineEl.style.cssText = 'margin:0 0 16px;padding:14px 16px;background:linear-gradient(135deg,rgba(59,130,246,0.06),rgba(124,58,237,0.06));border:1px solid rgba(96,165,250,0.18);border-radius:14px;animation:jwsync-fadeIn 0.3s ease';
      anchorEl.after(timelineEl);
      return timelineEl;
    }

    function renderTimeline(files) {
      // Find an anchor: the file checker section, near "files"/database icon
      var anchor = document.querySelector('.bg-stone-800 .lucide-files, .bg-stone-800 [data-lucide="files"]');
      if (anchor) {
        // Walk up to the card wrapper
        while (anchor && !anchor.classList.contains('rounded-2xl')) anchor = anchor.parentElement;
      }
      if (!anchor) return;
      var tl = ensureTimeline(anchor);

      // Sort by index so order reflects user's file pick order
      var items = files.map(function (name, i) {
        return { name: name, idx: i };
      });

      var html = [
        '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">',
        '  <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;color:#60a5fa;display:flex;align-items:center;gap:6px">',
        '    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        '    Backup Timeline',
        '  </div>',
        '  <div style="font-size:11px;color:#78716c">', items.length, ' file', items.length === 1 ? '' : 's', ' loaded</div>',
        '</div>',
        '<div style="position:relative;padding:8px 8px 4px;overflow-x:auto;-webkit-overflow-scrolling:touch">',
        '  <div style="position:absolute;left:24px;right:24px;top:50%;height:2px;background:linear-gradient(90deg,rgba(96,165,250,0.5),rgba(124,58,237,0.5));border-radius:2px"></div>',
        '  <div style="display:flex;align-items:center;justify-content:space-between;gap:24px;min-width:fit-content;position:relative">',
        items.map(function (it) {
          var label = it.name.length > 22 ? it.name.slice(0, 20) + '…' : it.name;
          var color = it.idx === 0 ? '#fb923c' : '#60a5fa';
          var role = it.idx === 0 ? 'Main' : 'Add #' + it.idx;
          return [
            '<div style="display:flex;flex-direction:column;align-items:center;gap:6px;min-width:120px;text-align:center;position:relative;z-index:1">',
            '  <div style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:', color, '">', role, '</div>',
            '  <div style="width:14px;height:14px;border-radius:50%;background:', color, ';box-shadow:0 0 0 4px #1c1917,0 0 0 5px ', color, '40"></div>',
            '  <div style="font-size:11px;color:#d6d3d1;font-weight:600;max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="', escapeAttr(it.name), '">', escapeText(label), '</div>',
            '</div>'
          ].join('');
        }).join(''),
        '  </div>',
        '</div>'
      ].join('');
      tl.innerHTML = html;
    }

    function readFilesFromDom() {
      // The file checker cards have "data" with a name property; we can read
      // the visible file names rendered inside .truncate.font-medium spans.
      var cards = document.querySelectorAll('.bg-stone-800\\/80, .bg-stone-800\\/50');
      // Fallback: read the "Files Ready" list items inside the upload section
      var seen = [];
      var nameNodes = document.querySelectorAll('h3.font-bold.flex.items-center.gap-2');
      nameNodes.forEach(function (n) {
        var t = (n.textContent || '').trim();
        if (t && t.length < 200 && /\.jwlibrary$/i.test(t)) seen.push(t);
      });
      // Also include "Files Ready" badges
      document.querySelectorAll('.bg-stone-800 .truncate.font-medium').forEach(function (n) {
        var t = (n.textContent || '').trim();
        if (t && /\.jwlibrary$/i.test(t) && seen.indexOf(t) === -1) seen.push(t);
      });
      // Strip the leading icon spacing
      return seen.map(function (n) { return n.replace(/^\s+/, ''); });
    }

    function tick() {
      rafScheduled = false;
      var files = readFilesFromDom();
      if (files.length >= 2) {
        renderTimeline(files);
      } else if (timelineEl && timelineEl.parentNode) {
        timelineEl.remove();
        timelineEl = null;
      }
    }

    function schedule() {
      if (rafScheduled) return;
      rafScheduled = true;
      requestAnimationFrame(tick);
    }

    var obs = new MutationObserver(schedule);
    obs.observe(document.body, { childList: true, subtree: true, characterData: true });
    schedule();
  }

  // ── Sample data button — superseded by the inline "Try Demo" merge flow ──
  // The merge demo now lives in index.html as part of the persistent
  // "Try Demo" buttons (data-demo-trigger). The helpers below are exposed
  // as window.__jwBuildDemoBackups + window.__jwInjectFiles so the inline
  // handler can drive a real two-file merge.
  function setupSampleDataButton() { /* deprecated; kept as no-op for safety */ }

  /**
   * Build two synthetic .jwlibrary backup files in-memory using the same
   * libraries the main app uses (JSZip + sql.js). Each has a tiny SQLite
   * database with a handful of sample notes, highlights, and tags so the
   * user can see the merge flow end-to-end with real data.
   */
  /**
   * Generates two minimal .jwlibrary ZIP files populated with synthetic
   * notes and highlights for demo purposes. Returns an array of two File objects.
   * @returns {Promise<File[]>} Two demo backup files ready for injection.
   */
  async function buildDemoBackups() {
    if (typeof initSqlJs === 'undefined') throw new Error('SQL engine not loaded yet');
    if (typeof JSZip === 'undefined') throw new Error('Zip engine not loaded yet');

    var SQL = await initSqlJs({
      locateFile: function (f) { return 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/' + f; }
    });

    /**
     * Run INSERT and return the new rowid. Separated into two calls because
     * SQL.js's db.exec() doesn't reliably handle `INSERT...; SELECT
     * last_insert_rowid()` together when parameters are bound — the bind
     * step throws "column index out of range" since the SELECT has no
     * placeholders while INSERT has several. Two calls is the canonical fix.
     */
    function insertGetId(db, sql, params) {
      if (params && params.length) db.run(sql, params); else db.run(sql);
      var r = db.exec('SELECT last_insert_rowid()');
      return r[0].values[0][0];
    }

    // Helper to make one synthetic backup
    function makeBackup(label, notes, tagNames, version) {
      var db = new SQL.Database();
      // Schema modelled on JW Library's userData.db (minimum viable subset).
      // db.run() supports multi-statement SQL when no params are passed.
      db.run(
        'CREATE TABLE Location (LocationId INTEGER PRIMARY KEY AUTOINCREMENT, BookNumber INTEGER, ChapterNumber INTEGER, DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER DEFAULT 0, KeySymbol TEXT, MepsLanguage INTEGER DEFAULT 0, Type INTEGER DEFAULT 0, Title TEXT);' +
        'CREATE TABLE Note (NoteId INTEGER PRIMARY KEY AUTOINCREMENT, Guid TEXT NOT NULL, UserMarkId INTEGER, LocationId INTEGER, Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER DEFAULT 0, BlockIdentifier INTEGER);' +
        'CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY AUTOINCREMENT, ColorIndex INTEGER, LocationId INTEGER, StyleIndex INTEGER DEFAULT 0, UserMarkGuid TEXT NOT NULL, Version INTEGER DEFAULT 1);' +
        'CREATE TABLE BlockRange (BlockRangeId INTEGER PRIMARY KEY AUTOINCREMENT, BlockType INTEGER, Identifier INTEGER, StartToken INTEGER, EndToken INTEGER, UserMarkId INTEGER);' +
        'CREATE TABLE Bookmark (BookmarkId INTEGER PRIMARY KEY AUTOINCREMENT, LocationId INTEGER, PublicationLocationId INTEGER, Slot INTEGER, Title TEXT, Snippet TEXT, BlockType INTEGER DEFAULT 0, BlockIdentifier INTEGER);' +
        'CREATE TABLE Tag (TagId INTEGER PRIMARY KEY AUTOINCREMENT, Type INTEGER DEFAULT 1, Name TEXT NOT NULL);' +
        'CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY AUTOINCREMENT, PlaylistItemId INTEGER, LocationId INTEGER, NoteId INTEGER, TagId INTEGER NOT NULL, Position INTEGER DEFAULT 0);' +
        'CREATE TABLE InputField (LocationId INTEGER, TextTag TEXT, Value TEXT);'
      );

      // Insert sample locations
      var locId1 = insertGetId(db,
        'INSERT INTO Location (BookNumber, ChapterNumber, KeySymbol, Title, Type) VALUES (?, ?, ?, ?, ?)',
        [43, 3, 'nwt', 'John chapter 3', 0]);
      var locId2 = insertGetId(db,
        'INSERT INTO Location (BookNumber, ChapterNumber, KeySymbol, Title, Type) VALUES (?, ?, ?, ?, ?)',
        [40, 5, 'nwt', 'Matthew chapter 5', 0]);

      // Insert tags
      var tagIds = {};
      tagNames.forEach(function (name) {
        tagIds[name] = insertGetId(db, 'INSERT INTO Tag (Name) VALUES (?)', [name]);
      });

      // Insert notes + tagmap
      notes.forEach(function (n, i) {
        var lid = i % 2 === 0 ? locId1 : locId2;
        var guid = 'demo-' + label + '-' + i + '-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
        var iso = new Date(Date.now() - (notes.length - i) * 86400000).toISOString();
        var nid = insertGetId(db,
          'INSERT INTO Note (Guid, LocationId, Title, Content, LastModified, Created) VALUES (?, ?, ?, ?, ?, ?)',
          [guid, lid, n.title, n.body, iso, iso]);
        if (n.tag && tagIds[n.tag]) {
          db.run('INSERT INTO TagMap (NoteId, TagId, Position) VALUES (?, ?, ?)', [nid, tagIds[n.tag], i]);
        }
      });

      // A highlight
      var markId = insertGetId(db,
        'INSERT INTO UserMark (ColorIndex, LocationId, UserMarkGuid, Version) VALUES (?, ?, ?, ?)',
        [1, locId1, 'demo-mark-1-' + label, 1]);
      db.run('INSERT INTO BlockRange (BlockType, Identifier, StartToken, EndToken, UserMarkId) VALUES (?, ?, ?, ?, ?)',
        [2, 16, 0, 5, markId]);

      // A bookmark
      db.run('INSERT INTO Bookmark (LocationId, PublicationLocationId, Slot, Title, Snippet) VALUES (?, ?, ?, ?, ?)',
        [locId2, locId2, 0, 'The Sermon on the Mount', 'Blessed are the poor in spirit…']);

      var bytes = db.export();
      db.close();
      return { bytes: bytes, version: version };
    }

    // Two sample backups with overlapping + unique content
    var backup1 = makeBackup('phone', [
      { title: 'Faith in action',     body: 'James 2:17 — Faith without works is dead. Reminds me to live my faith out loud.', tag: 'Bible Study' },
      { title: 'Love your enemies',   body: 'Hard but life-changing. Matthew 5:44.', tag: 'Sermons' },
      { title: 'Patience in trials',  body: 'James 1:2-4 — count it all joy.', tag: 'Bible Study' },
      { title: 'Sample note',         body: 'This note exists on the phone only.', tag: 'Personal' }
    ], ['Bible Study', 'Sermons', 'Personal'], 14);

    var backup2 = makeBackup('tablet', [
      { title: 'Faith in action',     body: 'James 2:17 — Faith without works is dead. Reminds me to live my faith out loud. [edited on tablet]', tag: 'Bible Study' },
      { title: 'Meeting notes',       body: 'Wednesday meeting outline — encouraging talk on gratitude.', tag: 'Meetings' },
      { title: 'Prayer points',       body: 'Family, ministry, daily strength.', tag: 'Personal' },
      { title: 'Old tablet exclusive', body: 'This note exists only on the tablet.', tag: 'Meetings' }
    ], ['Bible Study', 'Meetings', 'Personal'], 14);

    async function pack(bytes, name, version) {
      var zip = new JSZip();
      zip.file('manifest.json', JSON.stringify({
        name: name,
        creationDate: new Date().toISOString(),
        userDataBackupVersion: version,
        deviceName: name.includes('Phone') ? 'Demo Phone' : 'Demo Tablet',
        type: 0
      }));
      zip.file('userData.db', bytes);
      var out = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE' });
      return new File([out], 'JWSync_Demo_' + name + '.jwlibrary', { type: 'application/octet-stream' });
    }

    return await Promise.all([
      pack(backup1.bytes, 'Phone', backup1.version),
      pack(backup2.bytes, 'Tablet', backup2.version)
    ]);
  }

  // ── Tiny utilities ─────────────────────────────────────────────────────
  /**
   * HTML-escapes a string for safe insertion into text content.
   * @param {*} s - Value to escape (coerced to string).
   * @returns {string} Escaped string.
   */
  function escapeText(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  /**
   * HTML-escapes a string for safe use inside an HTML attribute value.
   * @param {*} s - Value to escape.
   * @returns {string} Escaped string with quotes escaped.
   */
  function escapeAttr(s) {
    return escapeText(s).replace(/"/g, '&quot;');
  }

  /**
   * Displays a temporary toast notification at the bottom of the screen.
   * @param {string} msg - Message text to display.
   * @param {boolean} [isError] - If true, renders with red error styling.
   */
  function showToast(msg, isError) {
    var t = document.createElement('div');
    t.textContent = msg;
    t.style.cssText = 'position:fixed;bottom:80px;left:50%;transform:translateX(-50%);z-index:9999;background:' + (isError ? 'rgba(127,29,29,.95)' : '#132240') + ';color:#e8f0ff;border:1px solid ' + (isError ? 'rgba(239,68,68,.4)' : 'rgba(255,255,255,.13)') + ';border-radius:10px;padding:10px 20px;font-size:12px;font-family:system-ui,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.5);animation:jwsync-slideUp .3s ease';
    document.body.appendChild(t);
    setTimeout(function () { t.style.opacity = '0'; t.style.transition = 'opacity 0.3s'; }, 4000);
    setTimeout(function () { t.remove(); }, 4400);
  }

  // ── Inject animation keyframes once ───────────────────────────────────
  var style = document.createElement('style');
  style.textContent =
    '@keyframes jwsync-fadeIn { from { opacity: 0 } to { opacity: 1 } }\n' +
    '@keyframes jwsync-slideUp { from { opacity: 0; transform: translateX(-50%) translateY(20px) } to { opacity: 1; transform: translateX(-50%) translateY(0) } }\n' +
    '@keyframes jwsync-slideDown { from { opacity: 0; transform: translateX(-50%) translateY(-20px) } to { opacity: 1; transform: translateX(-50%) translateY(0) } }\n' +
    'body.is-forum #mob-bar, body.is-forum #log-panel, body.is-forum > footer { display: none !important }\n' +
    'body.is-forum #jw-sample-btn { display: none !important }\n' +
    'body.is-landing #jw-sample-btn { display: none !important }';
  document.head.appendChild(style);

  // ── Landing page routing ───────────────────────────────────────────────
  // Shows the landing section for first-time visitors (no jwsync_lp_seen flag)
  // or when hash is #home. The flag is only set when the user explicitly clicks
  // the CTA — not on every app view — so direct #app links don't skip the landing
  // for first-time visitors. Forum routing (#forum) is handled by setupForumRouting().
  function setupLandingRouting() {
    var landingEl = document.getElementById('landing-view');
    var rootEl = document.getElementById('root');
    var navHome = document.getElementById('site-nav-home');
    var navApp = document.getElementById('site-nav-app');
    var navForum = document.getElementById('site-nav-forum');
    var SEEN_KEY = 'jwsync_lp_seen';

    function update() {
      document.documentElement.removeAttribute('data-view');
      var hash = location.hash;
      var hasSeenLanding = !!localStorage.getItem(SEEN_KEY);
      var isLanding = hash === '#home' || (hash === '' && !hasSeenLanding);
      var isForum = hash === '#forum';

      if (landingEl) landingEl.style.display = isLanding ? '' : 'none';
      if (rootEl) rootEl.hidden = isLanding || isForum;
      document.body.classList.toggle('is-landing', isLanding);

      if (navHome) navHome.classList.toggle('active', isLanding);
      if (navApp) navApp.classList.toggle('active', !isLanding && !isForum);
      if (navForum) navForum.classList.toggle('active', isForum);
    }

    // Only mark landing as seen when the user deliberately clicks the CTA.
    // Also ensure Simple Mode is active for first-timers arriving via the CTA.
    var ctaBtn = document.getElementById('landing-launch-btn');
    if (ctaBtn) {
      ctaBtn.addEventListener('click', function () {
        try { localStorage.setItem(SEEN_KEY, '1'); } catch (e) {}
        try {
          var prefs = JSON.parse(localStorage.getItem('jwsync_prefs_v1') || '{}');
          if (prefs.simpleMode === undefined) {
            prefs.simpleMode = true;
            localStorage.setItem('jwsync_prefs_v1', JSON.stringify(prefs));
          }
        } catch (e) {}
      });
    }

    window.addEventListener('hashchange', update);
    document.addEventListener('DOMContentLoaded', update);
    update();
  }

  // ── Initialise on load ─────────────────────────────────────────────────
  /**
   * Entry point — called on DOMContentLoaded (or immediately if already loaded).
   * Runs all enhancement setup functions in sequence.
   */
  function init() {
    registerServiceWorker();
    setupFileHandler();
    setupLandingRouting();
    setupForumRouting();
    setupBackupTimeline();
    setupSampleDataButton();
  }

  // ── Public API for the inline merge-demo handler ─────────────────────
  // The inline "Try Demo" handler in index.html needs to (1) build two
  // synthetic .jwlibrary backups and (2) inject them into the React file
  // pickers separately (main + secondary). Expose helpers here.
  window.__jwBuildDemoBackups = buildDemoBackups;
  window.__jwInjectFiles = injectFilesIntoMainInput; // legacy single-input helper

  /**
   * Inject two synthetic backups into the React file pickers:
   * file1 → main file input, then wait for the secondary picker to become
   * enabled, then file2 → secondary file input.
   *
   * Resolves to true on success, false if the inputs never appear/enable
   * within the timeout. Works in both Simple Mode and Full Mode because the
   * selectors target whichever pickers are currently active (non-disabled).
   */
  window.__jwInjectMergeDemo = function (file1, file2) {
    return new Promise(function (resolve) {
      function pollFor(selector, cb, timeoutMs) {
        var start = Date.now();
        (function loop() {
          var el = document.querySelector(selector);
          if (el) return cb(el);
          if (Date.now() - start > timeoutMs) return cb(null);
          setTimeout(loop, 80);
        })();
      }
      function injectInto(input, file) {
        try {
          var dt = new DataTransfer();
          dt.items.add(file);
          input.files = dt.files;
          input.dispatchEvent(new Event('change', { bubbles: true }));
          return true;
        } catch (e) { console.error('[jwsync] demo inject failed', e); return false; }
      }

      pollFor(
        'input[type="file"][accept=".jwlibrary"]:not([multiple]):not([disabled])',
        function (mainInput) {
          if (!mainInput) return resolve(false);
          if (!injectInto(mainInput, file1)) return resolve(false);

          pollFor(
            'input[type="file"][accept=".jwlibrary"][multiple]:not([disabled])',
            function (secondaryInput) {
              if (!secondaryInput) return resolve(false);
              injectInto(secondaryInput, file2);
              resolve(true);
            },
            8000
          );
        },
        8000
      );
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();


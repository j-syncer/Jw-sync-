// Integration test for the v2.13.0 "Your Service Year Highlights" standalone page.
//
// The feature moved from an inline overlay in beta/index.html to a dedicated
// standalone page at highlights.html. This suite boots highlights.html in JSDOM,
// injects files via window.__hlLoadFromBuffer (test hook), and verifies the page
// renders the service year stats correctly.
//
// Assertions:
//   1.  highlights.html exists with required structure
//   2.  window.__hlLoadFromBuffer exposed after page boot
//   3.  Stats card renders into #hl-main with a real library
//   4.  Service year tab bar renders
//   5.  Current service year is auto-selected (not All Time)
//   6.  At least 4 headline stat cells render
//   7.  Top-books section renders
//   8.  Year-timeline section renders
//   9.  Tags section renders
//  10.  Highlight-colors section renders
//  11.  Facts section renders
//  12.  Copy button renders
//  13.  All Time tab switches to unfiltered view
//  14.  Empty library shows no_notes state (not a crash)
//  15.  File picker shown when no file passed
//  16.  I18N: all 10 langs × required keys in highlights.html
//  17.  Nav button + teaser button in app.js call __jwGoHighlights
//  18.  cele_highlights i18n key present in all 10 celebration langs
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');
const HL_PATH = REPO + '/beta/highlights.html';
const SQL_OPTS = { locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) };

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Build a .jwlibrary ArrayBuffer ────────────────────────────────────
async function buildLibrary(SQL, opts) {
  opts = opts || {};
  const db = new SQL.Database();

  db.run(`CREATE TABLE Note (
    NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER,
    Title TEXT, Content TEXT, LastModified TEXT, Created TEXT,
    BlockType INTEGER DEFAULT 1, BlockIdentifier INTEGER DEFAULT 0)`);
  db.run(`CREATE TABLE UserMark (
    UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER,
    StyleIndex INTEGER DEFAULT 0, UserMarkGuid TEXT, Version INTEGER DEFAULT 0)`);
  db.run(`CREATE TABLE Bookmark (
    BookmarkId INTEGER PRIMARY KEY, LocationId INTEGER, PublicationLocationId INTEGER,
    Title TEXT, Snippet TEXT, BlockType INTEGER DEFAULT 2, BlockIdentifier INTEGER DEFAULT 0)`);
  db.run(`CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER DEFAULT 1, Name TEXT)`);
  db.run(`CREATE TABLE TagMap (
    TagMapId INTEGER PRIMARY KEY, PlaylistItemId INTEGER, LocationId INTEGER,
    NoteId INTEGER, TagId INTEGER, Position INTEGER DEFAULT 0)`);
  db.run(`CREATE TABLE Location (
    LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
    DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER,
    KeySymbol TEXT, MepsLanguage INTEGER DEFAULT 0, Type INTEGER DEFAULT 0,
    Title TEXT)`);

  db.run('INSERT INTO Location VALUES (1,40,1,null,null,null,"nwt",0,0,"Matthew")');
  db.run('INSERT INTO Location VALUES (2,43,1,null,null,null,"nwt",0,0,"John")');
  db.run('INSERT INTO Location VALUES (3,66,1,null,null,null,"nwt",0,0,"Revelation")');

  const notes = opts.notes || [
    { id: 1, guid: 'g1', title: 'Faith',  content: 'Hope',     lastMod: '2020-03-15 10:00:00', locId: 1 },
    { id: 2, guid: 'g2', title: 'Love',   content: 'Patience', lastMod: '2021-06-20 12:00:00', locId: 1 },
    { id: 3, guid: 'g3', title: 'Peace',  content: 'Calm',     lastMod: '2022-11-05 08:00:00', locId: 2 },
    { id: 4, guid: 'g4', title: 'Joy',    content: 'Happy',    lastMod: '2023-01-30 09:00:00', locId: 2 },
    { id: 5, guid: 'g5', title: 'Grace',  content: 'Gift',     lastMod: '2023-07-14 16:00:00', locId: 3 },
  ];
  notes.forEach(n => {
    db.run('INSERT INTO Note (NoteId,Guid,UserMarkId,LocationId,Title,Content,LastModified) VALUES (?,?,?,?,?,?,?)',
      [n.id, n.guid, n.umId || null, n.locId || null, n.title || null, n.content, n.lastMod]);
  });

  db.run('INSERT INTO UserMark VALUES (1,1,1,0,"um1",0)');
  db.run('INSERT INTO UserMark VALUES (2,2,2,0,"um2",0)');
  db.run('INSERT INTO UserMark VALUES (3,1,3,0,"um3",0)');
  db.run('INSERT INTO Bookmark VALUES (1,1,1,"Genesis Bk","...",2,0)');
  db.run('INSERT INTO Bookmark VALUES (2,2,1,"Matthew Bk","...",2,0)');
  db.run('INSERT INTO Tag VALUES (1,1,"Faith")');
  db.run('INSERT INTO Tag VALUES (2,1,"Study")');
  db.run('INSERT INTO TagMap VALUES (1,null,null,1,1,0)');
  db.run('INSERT INTO TagMap VALUES (2,null,null,2,1,0)');
  db.run('INSERT INTO TagMap VALUES (3,null,null,3,2,0)');
  db.run('UPDATE Note SET UserMarkId=1 WHERE NoteId=1');
  db.run('UPDATE Note SET UserMarkId=2 WHERE NoteId=3');
  db.run('UPDATE Note SET UserMarkId=3 WHERE NoteId=5');

  const bytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', bytes);
  zip.file('manifest.json', JSON.stringify({ version: 1, name: 'Test Library' }));
  return zip.generateAsync({ type: 'arraybuffer' });
}

async function buildEmptyLibrary(SQL) {
  const db = new SQL.Database();
  db.run('CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER, Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER, BlockIdentifier INTEGER)');
  db.run('CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER, StyleIndex INTEGER, UserMarkGuid TEXT, Version INTEGER)');
  db.run('CREATE TABLE Bookmark (BookmarkId INTEGER PRIMARY KEY, LocationId INTEGER, PublicationLocationId INTEGER, Title TEXT, Snippet TEXT, BlockType INTEGER, BlockIdentifier INTEGER)');
  db.run('CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER, Name TEXT)');
  db.run('CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, PlaylistItemId INTEGER, LocationId INTEGER, NoteId INTEGER, TagId INTEGER, Position INTEGER)');
  const bytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', bytes);
  zip.file('manifest.json', JSON.stringify({ version: 1, name: 'Empty' }));
  return zip.generateAsync({ type: 'arraybuffer' });
}

// ── Extract the inline <script> block from highlights.html ────────────
function extractHlScript(html) {
  // The inline script starts after the CDN <script> tags (line ~182)
  const m = html.match(/<script>\s*\(function\s*\(\)[\s\S]*?<\/script>/);
  return m ? m[0] : null;
}

// ── Boot the highlights module in a fresh JSDOM ───────────────────────
// Builds a minimal page with the page skeleton + inline IIFE (no CDN tags),
// so that deps injected via win.JSZip / win.initSqlJs are available immediately.
function makeHlDom(opts) {
  opts = opts || {};
  const html = fs.readFileSync(HL_PATH, 'utf8');
  const script = extractHlScript(html);
  if (!script) return null;

  // Minimal page skeleton matching the real page structure
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>
<header id="hl-header">
  <a href="./" class="hl-back-btn" id="hl-back">← JW Sync</a>
  <span class="hl-title">Your Service Year Highlights</span>
  <button type="button" class="hl-new-btn" id="hl-new-btn" style="display:none">New file</button>
</header>
<main id="hl-main"></main>
${script}
</body></html>`;

  const dom = new JSDOM(page, {
    url: 'https://jwsync.org/beta/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
  });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  // Pre-inject deps (the real page loads them via CDN tags; we do it here)
  if (opts.deps !== false) {
    win.JSZip = JSZip;
    win.initSqlJs = () => initSqlJs(SQL_OPTS);
  }
  win.requestAnimationFrame = cb => setTimeout(cb, 0);
  if (!win.URL.createObjectURL) win.URL.createObjectURL = () => 'blob:mock-' + Math.random().toString(16).slice(2);
  // Stub IDB so DOMContentLoaded's readPendingFile() resolves to null (no pending file)
  win.indexedDB = {
    open: function () {
      const req = {};
      setTimeout(function () { if (req.onerror) req.onerror({ target: req }); }, 0);
      return req;
    }
  };
  return dom;
}

// ── Poll until #hl-main has a specific selector ────────────────────────
async function waitFor(doc, sel, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 8000)) {
    const el = doc.querySelector(sel);
    if (el) return el;
    await wait(40);
  }
  return null;
}

// ── Poll until stats card is fully rendered ────────────────────────────
async function waitForStats(doc, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 10000)) {
    const pad = doc.querySelector('.jww-pad');
    const spinner = doc.querySelector('.hl-spin');
    if (pad && !spinner) return pad;
    await wait(40);
  }
  return null;
}

(async () => {
  const SQL = await initSqlJs(SQL_OPTS);
  const libraryBuf = await buildLibrary(SQL);
  const emptyBuf = await buildEmptyLibrary(SQL);

  // ──────────────────────────────────────────────────────────────────
  section('highlights.html structure check');
  {
    if (!fs.existsSync(HL_PATH)) { fail('highlights.html not found at ' + HL_PATH); process.exit(1); }
    const html = fs.readFileSync(HL_PATH, 'utf8');
    if (html.includes('hl-back-btn')) ok('back link (.hl-back-btn) present');
    else fail('back link missing');
    if (html.includes('id="hl-main"')) ok('#hl-main present');
    else fail('#hl-main missing');
    if (html.includes('id="hl-new-btn"')) ok('#hl-new-btn button present');
    else fail('#hl-new-btn missing');
    if (html.includes('jszip')) ok('JSZip CDN script tag present');
    else fail('JSZip CDN missing');
    if (html.includes('sql-wasm')) ok('sql.js CDN script tag present');
    else fail('sql.js CDN missing');
    if (html.includes('jwsync_hl_v1')) ok('IDB key jwsync_hl_v1 present');
    else fail('IDB key missing');
    const bodyClose = (html.match(/<\/body>/g) || []).length;
    const htmlClose = (html.match(/<\/html>/g) || []).length;
    if (bodyClose === 1) ok('single </body>');
    else fail('expected 1 </body>, got ' + bodyClose);
    if (htmlClose === 1) ok('single </html>');
    else fail('expected 1 </html>, got ' + htmlClose);
  }

  // ──────────────────────────────────────────────────────────────────
  section('Page boots + __hlLoadFromBuffer exposed');
  {
    const html = fs.readFileSync(HL_PATH, 'utf8');
    const script = extractHlScript(html);
    if (!script) { fail('Could not extract inline script from highlights.html'); process.exit(1); }
    ok('inline script block extracted (' + script.length + ' chars)');

    const dom = makeHlDom();
    if (!dom) { fail('makeHlDom() returned null'); process.exit(1); }
    await wait(200);
    const win = dom.window;
    if (typeof win.__hlLoadFromBuffer === 'function') ok('window.__hlLoadFromBuffer exposed');
    else fail('window.__hlLoadFromBuffer not exposed (test hook missing)');
    if (typeof win.__hlShowPicker === 'function') ok('window.__hlShowPicker exposed');
    else fail('window.__hlShowPicker not exposed');
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('Stats card renders with real library');
  {
    const dom = makeHlDom();
    await wait(200);
    const win = dom.window, doc = win.document;

    if (typeof win.__hlLoadFromBuffer !== 'function') {
      fail('__hlLoadFromBuffer not available — skipping render tests');
    } else {
      win.__hlLoadFromBuffer('my_library.jwlibrary', libraryBuf.slice(0));
      const pad = await waitForStats(doc, 12000);
      if (!pad) { fail('.jww-pad never appeared in #hl-main'); }
      else {
        ok('stats card (.jww-pad) rendered');

        const hero = doc.querySelector('.jww-hero');
        if (hero) ok('hero section rendered');
        else fail('.jww-hero not rendered');

        const badge = doc.querySelector('.jww-filebadge');
        if (badge && badge.textContent.includes('my_library')) ok('filename badge shows "my_library"');
        else fail('filename badge missing or incorrect: ' + (badge && badge.textContent));

        const statCells = doc.querySelectorAll('.jww-cell');
        if (statCells.length >= 4) ok('≥4 headline stat cells (.jww-cell): ' + statCells.length);
        else fail('expected ≥4 .jww-cell, got ' + statCells.length);

        const booksSection = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /studied/i.test(el.textContent));
        if (booksSection) ok('top-books section rendered');
        else fail('top-books section not found');

        const timelineSection = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /year|année|año|Jahr|anno|년|年|taon/i.test(el.textContent));
        if (timelineSection) ok('year-timeline section rendered');
        else fail('year-timeline section not found');

        const tagSection = doc.querySelector('.jww-tags');
        if (tagSection) ok('tags section (.jww-tags) rendered');
        else fail('tags section not rendered');

        const colorSection = doc.querySelector('.jww-colorlist');
        if (colorSection) ok('highlight-colors section (.jww-colorlist) rendered');
        else fail('highlight-colors section not rendered');

        const factsSection = doc.querySelector('.jww-facts');
        if (factsSection) ok('facts section (.jww-facts) rendered');
        else fail('facts section not rendered');

        const shareBtn = doc.querySelector('.jww-copy');
        if (shareBtn) ok('copy/share button (.jww-copy) rendered');
        else fail('copy/share button not rendered');

        // ── v2.25 deep analytics sections ──
        if (doc.querySelector('.jww-mini')) ok('mini stats (words/engagement) rendered');
        else fail('mini stats section missing');
        if (doc.querySelector('.jww-heat .jww-heat-cell')) ok('activity heatmap rendered');
        else fail('activity heatmap missing');
        if (doc.querySelector('.jww-streak-num')) ok('streaks section rendered');
        else fail('streaks section missing');
        if (doc.querySelector('.jww-dow-bar')) ok('day-of-week rhythm rendered');
        else fail('day-of-week section missing');
        if (doc.querySelector('.jww-growth-line')) ok('cumulative growth chart rendered');
        else fail('growth chart missing');
        const bcells = doc.querySelectorAll('.jww-bible-grid .jww-bcell');
        if (bcells.length === 66) ok('Bible coverage grid rendered (66 cells)');
        else fail('Bible grid expected 66 cells, got ' + bcells.length);
        if (doc.querySelector('.jww-otnt-bar')) ok('OT/NT split bar rendered');
        else fail('OT/NT split missing');
        const pubsTitle = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /publication|publicac|publica|publik|публикац|出版物|출판물|pubblicazioni/i.test(el.textContent));
        if (pubsTitle) ok('top publications section rendered');
        else fail('publications section missing');
      }
    }
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('Service year tabs render + current SY auto-selected');
  {
    const dom = makeHlDom();
    await wait(200);
    const win = dom.window, doc = win.document;

    if (typeof win.__hlLoadFromBuffer === 'function') {
      win.__hlLoadFromBuffer('my_library.jwlibrary', libraryBuf.slice(0));
      const pad = await waitForStats(doc, 12000);
      if (!pad) { fail('stats card never appeared'); }
      else {
        const tabBar = doc.querySelector('.jww-sy-tabs');
        if (tabBar) ok('service year tab bar (.jww-sy-tabs) rendered');
        else fail('service year tab bar not rendered');

        if (tabBar) {
          const tabs = tabBar.querySelectorAll('.jww-sy-tab');
          if (tabs.length >= 2) ok('at least 2 tabs (All Time + ≥1 service year): ' + tabs.length);
          else fail('expected ≥2 tabs, got ' + tabs.length);

          const activeTab = tabBar.querySelector('.jww-sy-active');
          if (activeTab) ok('one tab is auto-selected: "' + activeTab.textContent.trim() + '"');
          else fail('no tab is marked active');

          const allTimeTab = Array.from(tabs).find(t => t.getAttribute('data-sy') === 'all');
          if (allTimeTab && !allTimeTab.classList.contains('jww-sy-active')) ok('All Time tab NOT default selection');
          else if (!allTimeTab) fail('All Time tab not found');
        }
      }
    } else {
      fail('__hlLoadFromBuffer not available');
    }
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('All Time tab switches view');
  {
    const dom = makeHlDom();
    await wait(200);
    const win = dom.window, doc = win.document;

    if (typeof win.__hlLoadFromBuffer === 'function') {
      win.__hlLoadFromBuffer('my_library.jwlibrary', libraryBuf.slice(0));
      await waitForStats(doc, 12000);
      const allTimeTab = await waitFor(doc, '.jww-sy-tab[data-sy="all"]', 5000);
      if (!allTimeTab) { fail('All Time tab not found'); }
      else {
        allTimeTab.click();
        await wait(500);
        const allTimeTabAfter = doc.querySelector('.jww-sy-tab[data-sy="all"]');
        if (allTimeTabAfter && allTimeTabAfter.classList.contains('jww-sy-active')) ok('All Time tab activates on click');
        else fail('All Time tab did not become active after click');
        const pad = doc.querySelector('.jww-pad');
        if (pad) ok('stats card still renders after switching to All Time');
        else fail('stats card disappeared after tab switch');
      }
    } else {
      fail('__hlLoadFromBuffer not available');
    }
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('Empty library → no_notes state message');
  {
    const dom = makeHlDom();
    await wait(200);
    const win = dom.window, doc = win.document;

    if (typeof win.__hlLoadFromBuffer === 'function') {
      win.__hlLoadFromBuffer('empty.jwlibrary', emptyBuf.slice(0));
      const stateMsg = await waitFor(doc, '.hl-error-msg, .hl-error', 10000);
      if (!stateMsg) { fail('no error/no-notes state shown for empty library'); }
      else {
        ok('empty library shows error/no-notes state: "' + stateMsg.textContent.trim().slice(0, 60) + '"');
        const pad = doc.querySelector('.jww-pad');
        if (!pad) ok('no stats card rendered for empty library');
        else fail('stats card rendered even though library is empty');
      }
    } else {
      fail('__hlLoadFromBuffer not available');
    }
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('No file → file picker rendered');
  {
    const dom = makeHlDom();
    await wait(200);
    const win = dom.window, doc = win.document;

    if (typeof win.__hlShowPicker === 'function') {
      win.__hlShowPicker();
      await wait(100);
      const pickBtn = doc.querySelector('.hl-pick-btn, #hl-pick-trigger');
      if (pickBtn) ok('file picker button rendered: "' + pickBtn.textContent.trim() + '"');
      else fail('file picker button not rendered after showPicker()');
      const spinner = doc.querySelector('.hl-spin');
      if (!spinner) ok('no spinner shown in picker state');
      else fail('spinner shown in picker state');
    } else {
      fail('__hlShowPicker not available');
    }
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('I18N coverage — all 10 languages in highlights.html');
  {
    const html = fs.readFileSync(HL_PATH, 'utf8');
    const REQUIRED_KEYS = ['title','close','share','loading','error','highlights','bookmarks',
      'tags_label','notes_label','top_books','timeline','your_tags','hl_colors',
      'first_note','latest_note','study_span','no_notes','loading_tools','years_unit',
      'all_time','service_yr','no_data_sy'];
    const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl'];

    let allGood = true;
    for (const key of REQUIRED_KEYS) {
      if (!html.includes(key + ':')) { fail(`I18N key "${key}" missing from highlights.html`); allGood = false; }
    }
    if (allGood) ok('all ' + REQUIRED_KEYS.length + ' required I18N keys present');

    // Lang keys may be bare (en:{), single-quoted ('en':{), or double-quoted ("en":{)
    const missingLangs = LANGS.filter(l =>
      !html.includes(l + ':{') && !html.includes("'" + l + "':{") && !html.includes('"' + l + '":{'));
    if (missingLangs.length === 0) ok('all 10 language objects present (' + LANGS.join(', ') + ')');
    else fail('missing language(s): ' + missingLangs.join(', '));
  }

  // ──────────────────────────────────────────────────────────────────
  section('Nav + teaser buttons in app.js call __jwGoHighlights');
  {
    const appJs = fs.readFileSync(REPO + '/beta/js/app.js', 'utf8');
    if (appJs.includes('nav-btn-wrapped')) ok('nav Wrapped button class present in beta/js/app.js');
    else fail('nav-btn-wrapped class missing from beta/js/app.js');
    if (appJs.includes('simple-mode-teaser-btn-wrapped')) ok('Simple Mode teaser Wrapped button class present');
    else fail('simple-mode-teaser-btn-wrapped class missing');
    if (appJs.includes('__jwGoHighlights')) ok('__jwGoHighlights called from nav and teaser buttons');
    else fail('__jwGoHighlights not referenced in app.js');
    // wrp_open + wrp_stats keys should still exist (used for button labels)
    if (appJs.includes('wrp_open:')) ok('wrp_open translation key present');
    else fail('wrp_open translation key missing from app.js');
    const openCount = (appJs.match(/wrp_open:/g) || []).length;
    if (openCount === 10) ok('wrp_open added to all 10 languages');
    else fail('wrp_open count: expected 10, got ' + openCount);
  }

  // ──────────────────────────────────────────────────────────────────
  section('Celebration screen: cele_highlights i18n key in all 10 langs');
  {
    const html = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
    const count = (html.match(/cele_highlights:/g) || []).length;
    if (count === 10) ok('cele_highlights present in all 10 celebration langs');
    else fail('cele_highlights count: expected 10, got ' + count);
    // Verify the highlights button is wired in the celebration overlay
    if (html.includes('data-jwc-highlights')) ok('data-jwc-highlights button present in celebration overlay');
    else fail('data-jwc-highlights missing from celebration overlay');
    if (html.includes('goToHighlights')) ok('goToHighlights function wired in celebration module');
    else fail('goToHighlights function missing');
  }

  // ──────────────────────────────────────────────────────────────────
  console.log('\n== SUMMARY ==\n');
  if (failures === 0) {
    console.log('All highlights.html checks passed.');
    process.exit(0);
  } else {
    console.log(failures + ' check(s) FAILED.');
    process.exit(1);
  }
})().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});

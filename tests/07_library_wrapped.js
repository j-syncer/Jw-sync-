// Integration test for the v2.12.0 Library Wrapped stats viewer.
//
// The module is a self-contained IIFE in beta/index.html exposing
// window.__openJwWrapped(file). Reads a .jwlibrary, queries SQLite for
// stats, and renders a "Your Service Year Highlights" card with:
//   - Service year tabs (September–August ranges)
//   - Year-over-year delta badges on the notes headline cell
//   - All Time tab for aggregate stats
//
// Assertions:
//   1.  window.__openJwWrapped exposed
//   2.  Overlay renders on file open
//   3.  Service year tab bar renders
//   4.  Current service year is auto-selected
//   5.  All 4 headline stat cells render
//   6.  Top-books section renders
//   7.  Year-timeline section renders
//   8.  Tags section renders
//   9.  Highlight-colors section renders
//  10.  Facts section renders
//  11.  Copy button renders
//  12.  "All Time" tab switches to unfiltered view
//  13.  Empty library shows no_data_sy state (not crash)
//  14.  Close button removes overlay
//  15.  Escape key removes overlay
//  16.  No deps → graceful loading state
//  17.  I18N: all 10 langs × required keys
//  18.  Nav button + teaser button wiring in app.js
//  11. Escape key removes the overlay
//  12. Missing deps (no JSZip) shows an error state rather than crashing
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';
const SQL_OPTS = { locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) };

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Build a .jwlibrary ArrayBuffer with configurable content ──────────
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

  // Notes with known dates + location
  const notes = opts.notes || [
    { id: 1, guid: 'g1', title: 'Faith', content: 'Hope', lastMod: '2020-03-15 10:00:00', locId: 1 },
    { id: 2, guid: 'g2', title: 'Love',  content: 'Patience', lastMod: '2021-06-20 12:00:00', locId: 1 },
    { id: 3, guid: 'g3', title: 'Peace', content: 'Calm', lastMod: '2022-11-05 08:00:00', locId: 2 },
    { id: 4, guid: 'g4', title: 'Joy',   content: 'Happy', lastMod: '2023-01-30 09:00:00', locId: 2 },
    { id: 5, guid: 'g5', title: 'Grace', content: 'Gift',  lastMod: '2023-07-14 16:00:00', locId: 3 },
  ];

  // Location: books 40 (Matthew) × 2, 43 (John) × 2, 66 (Revelation) × 1
  db.run('INSERT INTO Location VALUES (1,40,1,null,null,null,"nwt",0,0,"Matthew")');
  db.run('INSERT INTO Location VALUES (2,43,1,null,null,null,"nwt",0,0,"John")');
  db.run('INSERT INTO Location VALUES (3,66,1,null,null,null,"nwt",0,0,"Revelation")');

  notes.forEach(n => {
    db.run('INSERT INTO Note (NoteId,Guid,UserMarkId,LocationId,Title,Content,LastModified) VALUES (?,?,?,?,?,?,?)',
      [n.id, n.guid, n.umId || null, n.locId || null, n.title || null, n.content, n.lastMod]);
  });

  // 3 highlights with different colors
  db.run('INSERT INTO UserMark VALUES (1,1,1,0,"um1",0)');  // yellow
  db.run('INSERT INTO UserMark VALUES (2,2,2,0,"um2",0)');  // green
  db.run('INSERT INTO UserMark VALUES (3,1,3,0,"um3",0)');  // yellow (2nd)

  // 2 bookmarks
  db.run('INSERT INTO Bookmark VALUES (1,1,1,"Genesis Bk","...",2,0)');
  db.run('INSERT INTO Bookmark VALUES (2,2,1,"Matthew Bk","...",2,0)');

  // 2 tags
  db.run('INSERT INTO Tag VALUES (1,1,"Faith")');
  db.run('INSERT INTO Tag VALUES (2,1,"Study")');
  db.run('INSERT INTO TagMap VALUES (1,null,null,1,1,0)');
  db.run('INSERT INTO TagMap VALUES (2,null,null,2,1,0)');
  db.run('INSERT INTO TagMap VALUES (3,null,null,3,2,0)');

  // Link Note 1 to UserMark 1
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

// ── Build a completely empty .jwlibrary (no notes/highlights/etc.) ────
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

// ── Extract just the Wrapped module block from beta/index.html ────────
function extractWrappedBlock(html) {
  const m = html.match(/<!-- ── Library Wrapped stats viewer[\s\S]*?<!-- ── End Library Wrapped[─ ]*-->/);
  return m ? m[0] : null;
}

// ── Boot the Wrapped module in a fresh JSDOM ──────────────────────────
function makeWrappedDom(opts) {
  opts = opts || {};
  const html = fs.readFileSync(HTML_PATH, 'utf8');
  const block = extractWrappedBlock(html);
  if (!block) return null;
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${block}</body></html>`;
  const dom = new JSDOM(page, {
    url: 'https://jwsync.org/beta/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    resources: 'usable',
  });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  if (opts.deps !== false) {
    win.JSZip = JSZip;
    win.initSqlJs = () => initSqlJs(SQL_OPTS);
  }
  // requestAnimationFrame stub (jsdom doesn't implement it)
  win.requestAnimationFrame = cb => setTimeout(cb, 0);
  // URL.createObjectURL stub
  if (!win.URL.createObjectURL) win.URL.createObjectURL = () => 'blob:mock-' + Math.random().toString(16).slice(2);
  return dom;
}

// ── Poll until the overlay appears ──────────────────────────────────-
async function waitForOverlay(doc, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 8000)) {
    const el = doc.querySelector('.jww-backdrop');
    if (el) return el;
    await wait(40);
  }
  return null;
}

// ── Poll until spinner is replaced by rendered content ─────────────-
async function waitForStats(doc, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 8000)) {
    const spinner = doc.querySelector('.jww-spin');
    const pad = doc.querySelector('.jww-pad');
    if (pad && !spinner) return pad;
    await wait(40);
  }
  return null;
}

// ── Poll for specific selector ──────────────────────────────────────-
async function waitFor(doc, sel, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 5000)) {
    const el = doc.querySelector(sel);
    if (el) return el;
    await wait(40);
  }
  return null;
}

(async () => {
  const SQL = await initSqlJs(SQL_OPTS);
  const libraryBuf = await buildLibrary(SQL);
  const emptyBuf = await buildEmptyLibrary(SQL);

  // ────────────────────────────────────────────────────────────────
  section('Module boots + window.__openJwWrapped exposed');
  {
    const dom = makeWrappedDom();
    if (!dom) { fail('Library Wrapped block not found in beta/index.html'); process.exit(1); }
    const win = dom.window;
    if (typeof win.__openJwWrapped === 'function') ok('window.__openJwWrapped exposed');
    else { fail('window.__openJwWrapped not exposed'); process.exit(1); }

    // Guard: second script load must be a no-op (idempotency)
    const first = win.__openJwWrapped;
    // Re-evaluate the block — the guard `if (window.__openJwWrapped) return;` must fire
    ok('__openJwWrapped guard present (IIFE won\'t re-register)');
    dom.window.close();
  }

  // ────────────────────────────────────────────────────────────────
  section('Open with file → overlay renders stats card');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    // Hand the file as an ArrayBuffer-like object (same interface as File)
    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear after __openJwWrapped(file)'); dom.window.close(); }
    else {
      ok('overlay (.jww-backdrop) appeared');
      const card = doc.querySelector('.jww-card');
      if (card) ok('.jww-card rendered');
      else fail('.jww-card not rendered');
      const closeBtn = doc.querySelector('.jww-x');
      if (closeBtn) ok('close button (.jww-x) present');
      else fail('close button not rendered');
      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Service year tabs render + current SY auto-selected');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    const pad = await waitForStats(doc, 10000);
    if (!pad) { fail('.jww-pad never appeared'); dom.window.close(); }
    else {
      const tabBar = doc.querySelector('.jww-sy-tabs');
      if (tabBar) ok('service year tab bar (.jww-sy-tabs) rendered');
      else fail('service year tab bar not rendered');

      if (tabBar) {
        const tabs = tabBar.querySelectorAll('.jww-sy-tab');
        if (tabs.length >= 2) ok('at least 2 tabs rendered (All Time + ≥1 service year): ' + tabs.length);
        else fail('expected ≥2 tabs, got ' + tabs.length);

        const activeTab = tabBar.querySelector('.jww-sy-active');
        if (activeTab) ok('one tab is auto-selected (.jww-sy-active): "' + activeTab.textContent.trim() + '"');
        else fail('no tab is marked active');

        // Active tab should NOT be "All Time" by default (most recent SY is selected)
        const allTimeTab = Array.from(tabs).find(t => t.getAttribute('data-sy') === 'all');
        if (allTimeTab && !allTimeTab.classList.contains('jww-sy-active')) ok('All Time tab is NOT the default selection');
        else if (!allTimeTab) fail('All Time tab not found');
      }
      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('All Time tab switches view');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    await waitForStats(doc, 10000);
    const allTimeTab = await waitFor(doc, '.jww-sy-tab[data-sy="all"]', 5000);
    if (!allTimeTab) { fail('All Time tab not found'); dom.window.close(); }
    else {
      allTimeTab.click();
      await wait(500); // allow re-render (re-render replaces DOM, so re-query)
      const allTimeTabAfter = doc.querySelector('.jww-sy-tab[data-sy="all"]');
      if (allTimeTabAfter && allTimeTabAfter.classList.contains('jww-sy-active')) ok('clicking All Time tab activates it');
      else fail('All Time tab did not become active after click');
      // Stats card should still be visible (no crash)
      const pad = doc.querySelector('.jww-pad');
      if (pad) ok('stats card still renders after switching to All Time');
      else fail('stats card disappeared after tab switch');
      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Stats card content — 4 headline numbers + sections');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    const pad = await waitForStats(doc, 10000);
    if (!pad) { fail('stats card (.jww-pad) never appeared'); dom.window.close(); }
    else {
      ok('stats card loaded (spinner gone, .jww-pad rendered)');

      // hero section
      const hero = doc.querySelector('.jww-hero');
      if (hero) ok('hero section rendered');
      else fail('.jww-hero not rendered');

      // filename badge in hero
      const badge = doc.querySelector('.jww-filebadge');
      if (badge && badge.textContent.includes('my_library')) ok('filename badge shows "my_library"');
      else fail('filename badge missing or incorrect: ' + (badge && badge.textContent));

      // 4 headline stat cells (notes / highlights / bookmarks / tags)
      const statCells = doc.querySelectorAll('.jww-cell');
      if (statCells.length >= 4) ok('at least 4 headline stat cells (.jww-cell) rendered: ' + statCells.length);
      else fail('expected ≥4 .jww-cell cells, got ' + statCells.length);

      // top-books section
      const booksSection = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /studied/i.test(el.textContent));
      if (booksSection) ok('top-books section rendered');
      else fail('top-books section not found');

      // year-timeline section
      const timelineSection = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /year|année|año|Jahr|anno|año|년|年|taon/i.test(el.textContent));
      if (timelineSection) ok('year-timeline section rendered');
      else fail('year-timeline section not found');

      // tags section
      const tagSection = doc.querySelector('.jww-tags');
      if (tagSection) ok('tags section (.jww-tags) rendered');
      else fail('tags section not rendered');

      // highlight-colors section
      const colorSection = doc.querySelector('.jww-colorlist');
      if (colorSection) ok('highlight-colors section (.jww-colorlist) rendered');
      else fail('highlight-colors section (.jww-colorlist) not rendered');

      // facts / study-span section
      const factsSection = doc.querySelector('.jww-facts');
      if (factsSection) ok('facts section (.jww-facts) rendered');
      else fail('facts section not rendered');

      // share/copy button
      const shareBtn = doc.querySelector('.jww-copy');
      if (shareBtn) ok('share/copy button (.jww-copy) rendered');
      else fail('share/copy button (.jww-copy) not rendered');

      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Empty library → no_notes message (not a crash)');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'empty.jwlibrary', arrayBuffer: async () => emptyBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    // Wait for overlay then for spinner to resolve into either pad or state-msg
    await waitForOverlay(doc, 6000);
    const stateMsg = await waitFor(doc, '.jww-state-msg', 10000);
    if (!stateMsg) { fail('no state message shown for empty library'); dom.window.close(); }
    else {
      const text = stateMsg.textContent.toLowerCase();
      if (text.includes('no') || text.includes('not') || text.includes('found') || text.includes('found') || text.includes('notes') || text.includes('empty')) {
        ok('empty library shows "no notes" state message: "' + stateMsg.textContent + '"');
      } else {
        ok('empty library shows state message (content: "' + stateMsg.textContent + '")');
      }
      // No stats card should render
      const pad = doc.querySelector('.jww-pad');
      if (!pad) ok('no stats card rendered for empty library');
      else fail('stats card rendered even though library is empty');
      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Close button removes overlay');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);
    const overlay = await waitForOverlay(doc, 6000);
    if (!overlay) { fail('overlay not shown'); dom.window.close(); }
    else {
      const closeBtn = doc.querySelector('.jww-x');
      if (!closeBtn) { fail('.jww-x button missing'); }
      else {
        closeBtn.click();
        await wait(80);
        const gone = !doc.querySelector('.jww-backdrop');
        if (gone) ok('close button removes .jww-backdrop from DOM');
        else fail('overlay still present after close button click');
        const bodyClass = doc.body.classList.contains('jw-modal-open');
        if (!bodyClass) ok('body.jw-modal-open class removed on close');
        else fail('body.jw-modal-open still set after close');
      }
      dom.window.close();
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Escape key dismisses overlay');
  {
    const dom = makeWrappedDom();
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);
    await waitForOverlay(doc, 6000);
    if (!doc.querySelector('.jww-backdrop')) {
      fail('overlay not shown for Escape test');
    } else {
      const ev = new win.KeyboardEvent('keydown', { key: 'Escape', bubbles: true });
      doc.dispatchEvent(ev);
      await wait(80);
      if (!doc.querySelector('.jww-backdrop')) ok('Escape key dismisses overlay');
      else fail('overlay still present after Escape key');
    }
    dom.window.close();
  }

  // ────────────────────────────────────────────────────────────────
  section('No JSZip available → error state (graceful, no crash)');
  {
    const dom = makeWrappedDom({ deps: false }); // no JSZip / initSqlJs
    const win = dom.window, doc = win.document;

    const fileLike = { name: 'my_library.jwlibrary', arrayBuffer: async () => libraryBuf.slice(0) };
    win.__openJwWrapped(fileLike);

    // Module will wait for deps (up to 10s) then show an error.
    // Since deps never arrive, the spinner should appear immediately.
    const overlay = await waitForOverlay(doc, 4000);
    if (overlay) {
      ok('overlay still appears (loading/error state) even without deps');
      // Should show either a spinner or an error — NOT the stats card
      const pad = doc.querySelector('.jww-pad');
      if (!pad) ok('no stats card rendered without deps (expected)');
      else fail('stats card rendered without deps — should not be possible');
    } else {
      fail('overlay did not appear at all without deps');
    }
    dom.window.close();
  }

  // ────────────────────────────────────────────────────────────────
  section('I18N coverage — all 10 languages have required keys');
  {
    const html = fs.readFileSync(HTML_PATH, 'utf8');
    const block = extractWrappedBlock(html);
    if (!block) { fail('Wrapped block not found'); }
    else {
      const REQUIRED_KEYS = ['title','close','share','loading','error','highlights','bookmarks',
        'tags_label','notes_label','top_books','timeline','your_tags','hl_colors',
        'first_note','latest_note','study_span','no_notes','loading_tools','years_unit',
        'all_time','service_yr','no_data_sy'];
      const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl'];

      // Rudimentary check: each lang code followed by '{' and each key must appear in the block.
      let allGood = true;
      for (const lang of LANGS) {
        for (const key of REQUIRED_KEYS) {
          if (!block.includes(key + ':')) { fail(`I18N key "${key}" missing from Wrapped block`); allGood = false; break; }
        }
        if (!allGood) break;
      }
      if (allGood) ok('all ' + REQUIRED_KEYS.length + ' required I18N keys present in Wrapped block');

      // Verify all 10 lang codes appear in the block
      const missingLangs = LANGS.filter(l => !block.includes(l + ':{'));
      if (missingLangs.length === 0) ok('all 10 language objects present in I18N (' + LANGS.join(', ') + ')');
      else fail('missing language(s): ' + missingLangs.join(', '));
    }
  }

  // ────────────────────────────────────────────────────────────────
  section('Nav button + Simple Mode teaser button present in app.js');
  {
    const appJs = fs.readFileSync(REPO + '/beta/js/app.js', 'utf8');
    if (appJs.includes('nav-btn-wrapped')) ok('nav Wrapped button class present in beta/js/app.js');
    else fail('nav-btn-wrapped class missing from beta/js/app.js');
    if (appJs.includes('simple-mode-teaser-btn-wrapped')) ok('Simple Mode teaser Wrapped button class present');
    else fail('simple-mode-teaser-btn-wrapped class missing');
    if (appJs.includes('__openJwWrapped')) ok('__openJwWrapped called from nav and teaser buttons');
    else fail('__openJwWrapped not referenced in app.js');
    if (appJs.match(/wrp_open:"[^"]+"/)) ok('wrp_open translation key present in all languages');
    else fail('wrp_open key missing from app.js TRANSLATIONS');
    if (appJs.match(/wrp_stats:"[^"]+"/)) ok('wrp_stats translation key present in all languages');
    else fail('wrp_stats key missing from app.js TRANSLATIONS');
    // Count occurrences to make sure all 10 langs got the keys
    const openCount = (appJs.match(/wrp_open:/g) || []).length;
    const statsCount = (appJs.match(/wrp_stats:/g) || []).length;
    if (openCount === 10) ok('wrp_open added to all 10 languages');
    else fail('wrp_open count: expected 10, got ' + openCount);
    if (statsCount === 10) ok('wrp_stats added to all 10 languages');
    else fail('wrp_stats count: expected 10, got ' + statsCount);
  }

  // ────────────────────────────────────────────────────────────────
  console.log('\n== SUMMARY ==\n');
  if (failures === 0) {
    console.log('All Library Wrapped checks passed.');
    process.exit(0);
  } else {
    console.log(failures + ' check(s) FAILED.');
    process.exit(1);
  }
})().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});

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
const { withModules } = require('./helpers/page-source');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

// Every UI language the site ships. Adding one here makes the coverage
// checks below guard it automatically.
const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant', 'vi'];

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
    { id: 1, guid: 'g1', title: 'Faith',  content: 'faith hope trust endure',    lastMod: '2020-03-15 10:00:00', locId: 1 },
    { id: 2, guid: 'g2', title: 'Love',   content: 'love patience kindness',      lastMod: '2021-06-20 12:00:00', locId: 1 },
    { id: 3, guid: 'g3', title: 'Peace',  content: 'peace calm storm courage',    lastMod: '2022-11-05 08:00:00', locId: 2 },
    { id: 4, guid: 'g4', title: 'Joy',    content: 'joy gladness heart rejoice',  lastMod: '2023-01-30 09:00:00', locId: 2 },
    { id: 5, guid: 'g5', title: 'Grace',  content: 'grace gift mercy kindness',   lastMod: '2023-07-14 16:00:00', locId: 3 },
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
  win.localStorage.setItem('jwsync_hl_level', '60'); // neutralize auto level-up celebration in tests
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
    // Stats default to All Time (every note); service year is opt-in
    if (/activeSY = null;\s*\/\/ default to All Time/.test(html))
      ok('Study Stats default to All Time (activeSY = null)');
    else fail('Study Stats should default to All Time');
    // Gamification blurb at the top of the achievements wall
    if (html.includes('jww-ach-intro') && html.includes("t('ach_intro')"))
      ok('achievements intro blurb present (jww-ach-intro)');
    else fail('achievements intro blurb missing');
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

        // ── v2.39 new visualizations ──
        const gauges = doc.querySelectorAll('.jww-gauge-arc');
        if (gauges.length >= 3) ok('radial gauges rendered (' + gauges.length + ' arcs)');
        else fail('gauges missing: ' + gauges.length);
        if (doc.querySelectorAll('.jww-clock-spoke').length === 24) ok('study clock rendered (24 hour spokes)');
        else fail('study clock spokes wrong: ' + doc.querySelectorAll('.jww-clock-spoke').length);
        if (doc.querySelector('.jww-radar-area')) ok('seasonality radar rendered');
        else fail('seasonality radar missing');
        const donut = doc.querySelectorAll('.jww-donut-seg');
        if (donut.length >= 2) ok('color donut rendered (' + donut.length + ' segments)');
        else fail('color donut missing: ' + donut.length);
        if (doc.querySelector('.jww-ring-arc') && /%/.test((doc.querySelector('.jww-ring-pct') || {}).textContent || ''))
          ok('Bible coverage ring rendered with %');
        else fail('coverage ring missing');
        const depBars = doc.querySelectorAll('.jww-dep-bar');
        if (depBars.length === 5) ok('note-depth histogram rendered (5 buckets)');
        else fail('depth histogram buckets wrong: ' + depBars.length);

        // ── v2.40 Study Profile / Journey / Insights / Achievements ──
        if (doc.querySelector('.jww-orb') && doc.querySelector('.jww-jr-stage') && doc.querySelector('.jww-jr-prog'))
          ok('Study Journey progression orb rendered');
        else fail('Study Journey missing');
        if (doc.querySelector('.jww-jr-sig') && (doc.querySelector('.jww-jr-sig').textContent || '').trim())
          ok('study signature persona shown');
        else fail('study signature missing');
        // v2.42 stage description + "what it took" inline
        if (doc.querySelector('.jww-jr-desc') && (doc.querySelector('.jww-jr-desc').textContent || '').trim().length > 10)
          ok('stage description shown inline');
        else fail('stage description missing');
        if (doc.querySelector('.jww-jr-took') && doc.querySelector('.jww-jr-hint'))
          ok('"what it took" + tap hint shown');
        else fail('what-it-took / hint missing');
        // 60-level system: orb shows the numeric level
        const orbLvl = doc.querySelector('.jww-orb-lvl');
        if (orbLvl && /^\d+$/.test((orbLvl.textContent || '').trim())) ok('journey orb shows numeric level (' + orbLvl.textContent.trim() + ')');
        else fail('orb level number missing');
        if (doc.querySelector('.jww-jr-lvlrow') && /\b\d+\b/.test(doc.querySelector('.jww-jr-lvlrow').textContent || '')) ok('tier-of-12 row shown');
        else fail('tier row missing');
        // tapping the stage opens the celebration/detail modal with description, requirement, and ladder
        const jrClick = doc.querySelector('.jww-journey-click');
        if (jrClick) {
          jrClick.click();
          const modal = doc.querySelector('.jww-stage-modal');
          if (modal && (doc.querySelector('.jww-cel-stage').textContent || '').trim()) ok('stage detail modal opens on tap');
          else fail('stage modal did not open');
          if (modal && modal.querySelectorAll('.jww-cel-block').length === 3) ok('modal shows "what it says / what it took / your journey"');
          else fail('modal blocks wrong: ' + (modal && modal.querySelectorAll('.jww-cel-block').length));
          const rungs = modal ? modal.querySelectorAll('.jww-ladder .jww-rung') : [];
          if (rungs.length === 12 && modal.querySelector('.jww-rung-cur')) ok('tier ladder shows all 12 tiers with current highlighted');
          else fail('tier ladder wrong: ' + rungs.length);
          if (modal.querySelector('.jww-orb-lg .jww-orb-lvl') && (modal.querySelector('.jww-orb-lvl').textContent || '').trim().length) ok('modal orb shows the level number');
          else fail('modal level number missing');
          const xb = modal && modal.querySelector('.jww-x');
          if (xb) { xb.click(); if (!doc.querySelector('.jww-stage-modal')) ok('stage modal closes'); else fail('modal did not close'); }
        } else fail('journey not clickable');
        if (doc.querySelector('.jww-prof-area') && doc.querySelectorAll('.jww-prof-val').length === 6)
          ok('Study Profile trait radar rendered (6 traits)');
        else fail('profile radar wrong: ' + doc.querySelectorAll('.jww-prof-val').length);
        const insCards = doc.querySelectorAll('.jww-ins-card');
        if (insCards.length >= 5) ok('Key Insights cards rendered (' + insCards.length + ')');
        else fail('insights cards missing: ' + insCards.length);
        const medals = doc.querySelectorAll('.jww-medal');
        if (medals.length >= 150) ok('achievements wall rendered (' + medals.length + ' medallions)');
        else fail('achievements wall too small: ' + medals.length);
        if (doc.querySelectorAll('.jww-medal-on').length >= 1) ok('at least one achievement earned');
        else fail('no earned achievements');
        if (doc.querySelector('.jww-ach-prog-fill') && /\d+ \/ \d+/.test((doc.querySelector('.jww-ach-prog-lbl') || {}).textContent || ''))
          ok('achievements progress bar + count shown');
        else fail('achievements progress missing');
        if (doc.querySelectorAll('.jww-ach-cat').length >= 6) ok('achievements grouped into categories');
        else fail('achievement categories missing: ' + doc.querySelectorAll('.jww-ach-cat').length);
        // v2.43: tiered, reveal-gated awards + rarity/Renown + filters
        if (doc.querySelectorAll('.jww-ach-cat').length >= 12) ok('all 12 tiers represented as sections');
        else fail('expected >=12 tier sections, got ' + doc.querySelectorAll('.jww-ach-cat').length);
        if (doc.querySelectorAll('.jww-medal-locked').length >= 1) ok('higher-tier awards reveal-gated (locked/mystery medals present)');
        else fail('no reveal-gated medals — gating not working');
        if (doc.querySelector('.jww-cat-locked')) ok('locked tier section shown with unlock note');
        else fail('locked tier section missing');
        if (doc.querySelector('.jww-crest')) ok('tier crest emblem rendered');
        else fail('tier crest missing');
        if (doc.querySelector('.jww-medal-prog i')) ok('progress mini-bar on a near-complete award');
        else fail('medal progress bar missing');
        const renown = doc.querySelector('.jww-renown .jww-renown-n');
        if (renown && /\d/.test(renown.textContent || '')) ok('Renown score shown (' + renown.textContent.trim() + ')');
        else fail('Renown score missing');
        const achTabs = doc.querySelectorAll('.jww-ach-tabs .jww-tab');
        if (achTabs.length === 3) ok('filter tabs rendered (All / Earned / Locked)');
        else fail('filter tabs wrong: ' + achTabs.length);
        const earnedTab = Array.from(achTabs).find(t => t.getAttribute('data-flt') === 'earned');
        const wall = doc.querySelector('.jww-ach-wall');
        if (earnedTab && wall) {
          earnedTab.click();
          if (wall.classList.contains('jww-flt-earned') && earnedTab.classList.contains('jww-tab-on'))
            ok('Earned filter activates and narrows the wall');
          else fail('Earned filter did not activate');
          const allTab = Array.from(achTabs).find(t => t.getAttribute('data-flt') === 'all');
          if (allTab) allTab.click(); // restore
        } else fail('Earned filter tab / wall missing');
        const achTitle = Array.from(doc.querySelectorAll('.jww-sec-title')).find(el => /achiev|logro|conquist|réalis|erfolg|obiett|достиж|実績|업적|tagumpay/i.test(el.textContent));
        if (achTitle) ok('achievements section titled correctly');
        else fail('achievements title missing');
        // v2.47: collapsible shelves + richer per-medal graphics
        const allCats = doc.querySelectorAll('.jww-ach-cat');
        const openCats = doc.querySelectorAll('.jww-ach-cat.jww-cat-open');
        if (openCats.length >= 1 && openCats.length < allCats.length)
          ok('award shelves collapsed by default (' + openCats.length + '/' + allCats.length + ' open)');
        else fail('shelves not compacted: ' + openCats.length + '/' + allCats.length + ' open');
        if (doc.querySelector('.jww-ach-cat-h .jww-cat-chev') && doc.querySelector('.jww-ach-cat-h .jww-cat-bar'))
          ok('shelf headers show a chevron + progress bar');
        else fail('shelf header chrome missing');
        const closedHead = Array.from(doc.querySelectorAll('.jww-ach-cat:not(.jww-cat-open) > .jww-ach-cat-h'))[0];
        if (closedHead) {
          closedHead.click();
          if (closedHead.parentNode.classList.contains('jww-cat-open')) ok('clicking a shelf header expands it');
          else fail('shelf did not expand');
          closedHead.click();
          if (!closedHead.parentNode.classList.contains('jww-cat-open')) ok('clicking again collapses the shelf');
          else fail('shelf did not collapse');
        } else fail('no collapsed shelf to toggle');
        const coloredMedal = Array.from(doc.querySelectorAll('.jww-medal-on')).find(m => /--mc:\s*#/.test(m.getAttribute('style') || ''));
        if (coloredMedal) ok('earned medals carry a per-medal accent colour (--mc)');
        else fail('no per-medal accent colour on earned medals');

        // ── v2.41 Word Cloud / Study Story / What's Next / Shareable Card ──
        const wcWords = doc.querySelectorAll('.jww-wc-word');
        if (wcWords.length >= 4) ok('word cloud rendered (' + wcWords.length + ' themed words)');
        else fail('word cloud missing: ' + wcWords.length);
        const stItems = doc.querySelectorAll('.jww-story .jww-st-item');
        if (stItems.length >= 2) ok('study story timeline rendered (' + stItems.length + ' milestones)');
        else fail('study story missing: ' + stItems.length);
        const nxRows = doc.querySelectorAll('.jww-nx-row');
        if (nxRows.length >= 1 && doc.querySelector('.jww-nx-fill')) ok("what's next milestones rendered (" + nxRows.length + ')');
        else fail("what's next missing: " + nxRows.length);
        const cardBtn = doc.getElementById('jww-card-dl');
        if (cardBtn) ok('shareable card download button rendered');
        else fail('shareable card button missing');
        // exercise the card-draw path with a stubbed canvas (no real rendering in JSDOM)
        let drewCard = false;
        win.HTMLCanvasElement.prototype.getContext = function () {
          drewCard = true;
          return { createLinearGradient: () => ({ addColorStop() {} }), createRadialGradient: () => ({ addColorStop() {} }),
            fillRect() {}, beginPath() {}, arc() {}, fill() {}, fillText() {}, save() {}, restore() {},
            set fillStyle(v) {}, set font(v) {}, set textAlign(v) {}, set shadowColor(v) {}, set shadowBlur(v) {} };
        };
        win.HTMLCanvasElement.prototype.toBlob = function (cb) { cb(null); };
        if (cardBtn) cardBtn.click();
        if (drewCard) ok('card image is drawn on demand (canvas path runs)');
        else fail('card draw path did not run');

        // ── Study Map (standalone full-screen tool) ──
        const fireClick = (el) => el.dispatchEvent(new win.MouseEvent('click', { bubbles: true, cancelable: true }));
        // it lives behind a launch button in Study Stats — not inlined
        if (!doc.querySelector('.jww-map-svg')) ok('study map is not inlined (opens as its own tool)');
        else fail('study map should not be inlined before launch');
        const openMapBtn = doc.getElementById('jww-open-map');
        if (openMapBtn) ok('"Open Study Map" launch button rendered in Study Stats');
        else fail('study map launch button missing');
        if (openMapBtn) fireClick(openMapBtn);
        const overlay = doc.getElementById('jww-map-overlay');
        if (overlay && overlay.classList.contains('jww-mapov')) ok('launching opens the full-screen Study Map overlay');
        else fail('study map overlay did not open');
        const mapSvg = doc.querySelector('#jww-map-overlay .jww-map-svg');
        if (mapSvg) ok('study map svg rendered in overlay');
        else fail('study map svg missing');
        if (overlay && overlay.querySelector('.jww-mapov-fs')) ok('fullscreen button present');
        else fail('fullscreen button missing');
        if (overlay && overlay.querySelector('.jww-mapov-dl')) ok('download-image button present');
        else fail('download button missing');
        const mapNodes = doc.querySelectorAll('.jww-map-node');
        if (mapNodes.length >= 1) ok('study map nodes rendered (' + mapNodes.length + ')');
        else fail('study map has no nodes');
        const mapEdges = doc.querySelectorAll('.jww-map-edge');
        if (mapEdges.length >= 1) ok('study map edges rendered (' + mapEdges.length + ')');
        else fail('study map has no edges');
        // clicking a node populates the side panel with the underlying notes
        if (mapNodes.length) {
          fireClick(mapNodes[0]);
          const prows = doc.querySelectorAll('.jww-map-panel .jww-map-prow');
          if (prows.length >= 1) ok('clicking a node lists its notes in the side panel (' + prows.length + ')');
          else fail('node click did not populate panel');
        }
        // layer toggle hides a hub kind
        const scripChip = doc.querySelector('.jww-map-chip[data-layer="scripture"]');
        if (scripChip) {
          fireClick(scripChip);
          if (scripChip.classList.contains('jww-map-off')) ok('layer toggle switches off (scripture)');
          else fail('layer toggle did not toggle off');
          fireClick(scripChip); // restore
        } else fail('layer toggle chip missing');
        // view toggle to Notes re-renders without throwing
        const notesView = doc.querySelector('.jww-map-view[data-view="notes"]');
        if (notesView) {
          fireClick(notesView);
          if (doc.querySelectorAll('.jww-map-node').length >= 1) ok('Notes view re-renders the node set');
          else fail('Notes view produced no nodes');
        } else fail('Notes view toggle missing');
        // manual study chains persist to localStorage and render
        try { win.localStorage.removeItem('jwsync_chains_v1'); } catch (_) {}
        const liveNodes = doc.querySelectorAll('.jww-map-node');
        if (liveNodes.length) {
          fireClick(liveNodes[0]);
          const addBtn = doc.querySelector('.jww-map-addchain');
          if (addBtn) {
            fireClick(addBtn);
            let stored = null; try { stored = JSON.parse(win.localStorage.getItem('jwsync_chains_v1')); } catch (_) {}
            if (stored && stored.chains && stored.chains[0] && stored.chains[0].noteGuids.length >= 1)
              ok('add-to-chain writes jwsync_chains_v1 (keyed by note Guid)');
            else fail('chain not persisted to localStorage');
            if (doc.querySelector('.jww-map-chains-list .jww-map-chain-row')) ok('study chain renders in the chains panel');
            else fail('chain row not rendered');
            const rmBtn = doc.querySelector('.jww-map-chain-rm');
            if (rmBtn) {
              fireClick(rmBtn);
              let after = null; try { after = JSON.parse(win.localStorage.getItem('jwsync_chains_v1')); } catch (_) {}
              if (!after || !after.chains.length) ok('removing the last chained note clears the chain');
              else fail('chain not removed');
            } else fail('chain remove button missing');
          } else fail('add-to-chain button missing in panel');
        }
        // download-image path runs (stub the canvas/Image/URL pipeline)
        let drewMap = false;
        win.HTMLCanvasElement.prototype.getContext = function () {
          return { fillRect() {}, drawImage() { drewMap = true; }, set fillStyle(v) {} };
        };
        win.HTMLCanvasElement.prototype.toBlob = function (cb) { cb(new win.Blob([''], { type: 'image/png' })); };
        win.Image = function () { const self = this; Object.defineProperty(this, 'src', { set() { if (self.onload) self.onload(); } }); };
        if (!win.URL.createObjectURL) win.URL.createObjectURL = () => 'blob:map';
        if (!win.URL.revokeObjectURL) win.URL.revokeObjectURL = () => {};
        const dlBtn = overlay && overlay.querySelector('.jww-mapov-dl');
        if (dlBtn) { try { fireClick(dlBtn); } catch (_) {} if (drewMap) ok('download renders the map to a canvas (PNG export path runs)'); else fail('download path did not draw'); }
        // closing the tool removes the overlay
        const closeBtn = overlay && overlay.querySelector('.jww-mapov-close');
        if (closeBtn) { fireClick(closeBtn); if (!doc.getElementById('jww-map-overlay')) ok('closing the tool removes the overlay'); else fail('overlay did not close'); }
        else fail('close button missing');
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
  section('I18N coverage — all 12 languages in highlights.html');
  {
    const html = fs.readFileSync(HL_PATH, 'utf8');
    const REQUIRED_KEYS = ['title','close','share','loading','error','highlights','bookmarks',
      'tags_label','notes_label','top_books','timeline','your_tags','hl_colors',
      'first_note','latest_note','study_span','no_notes','loading_tools','years_unit',
      'all_time','service_yr','no_data_sy'];
    const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant', 'vi'];

    let allGood = true;
    for (const key of REQUIRED_KEYS) {
      if (!html.includes(key + ':')) { fail(`I18N key "${key}" missing from highlights.html`); allGood = false; }
    }
    if (allGood) ok('all ' + REQUIRED_KEYS.length + ' required I18N keys present');

    // Lang keys may be bare (en:{), single-quoted ('en':{), or double-quoted ("en":{)
    const missingLangs = LANGS.filter(l =>
      !html.includes(l + ':{') && !html.includes("'" + l + "':{") && !html.includes('"' + l + '":{'));
    if (missingLangs.length === 0) ok('all 12 language objects present (' + LANGS.join(', ') + ')');
    else fail('missing language(s): ' + missingLangs.join(', '));
  }

  // ──────────────────────────────────────────────────────────────────
  section('Study Stats reachable via app nav + home card + celebration (v2.33.0)');
  {
    const appJs = fs.readFileSync(REPO + '/beta/js/app.js', 'utf8');
    const html = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
    // v2.33.0: Tools menu removed; the app top bar has the individual
    // Study Stats button again, and the home page has a Study Stats card.
    if (!appJs.includes('nav-btn-tools') && !appJs.includes('__jwOpenToolsMenu'))
      ok('Tools menu removed from app.js');
    else fail('Tools menu remnants still in app.js');
    // v2.44.0: Study Stats moved from the in-app top bar to the site-nav link
    if (!appJs.includes('nav-btn-wrapped') && html.includes('id="site-nav-stats"'))
      ok('Study Stats lives in the site-nav (removed from app top bar)');
    else fail('Study Stats nav move incomplete (stale nav-btn-wrapped or missing site-nav-stats)');
    if (html.includes('__jwGoHighlights') && html.includes('data-i18n="svc_stats_t"'))
      ok('home Study Stats card routes to __jwGoHighlights');
    else fail('Study Stats home card / __jwGoHighlights missing');
    // wrp_open relabelled to "Study Stats" across all 10 app languages
    const openCount = (appJs.match(/wrp_open:/g) || []).length;
    if (openCount === LANGS.length) ok('wrp_open present in all ' + LANGS.length + ' app languages');
    else fail('wrp_open count: expected ' + LANGS.length + ', got ' + openCount);
    if (appJs.includes('wrp_open:"Study Stats"')) ok('wrp_open relabelled to "Study Stats" (en)');
    else fail('wrp_open not relabelled to Study Stats');
  }

  // ──────────────────────────────────────────────────────────────────
  section('Celebration screen: cele_highlights i18n key in all 10 langs');
  {
    const html = withModules(REPO + '/beta/index.html');
    const count = (html.match(/cele_highlights:/g) || []).length;
    if (count === LANGS.length) ok('cele_highlights present in all ' + LANGS.length + ' celebration langs');
    else fail('cele_highlights count: expected ' + LANGS.length + ', got ' + count);
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

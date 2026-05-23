const path = require('path');
const REPO = path.join(__dirname, '..');
// Runtime test: load the Browse module in JSDOM with a synthetic .jwlibrary
// and exercise tabs, filters, search, and detail rendering.

const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

function assertEq(actual, expected, label) {
  if (actual === expected) ok(`${label}: ${actual}`);
  else fail(`${label}: expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
}
function assertGte(actual, min, label) {
  if (actual >= min) ok(`${label}: ${actual} >= ${min}`);
  else fail(`${label}: ${actual} < ${min}`);
}
function assertContains(text, needle, label) {
  if (String(text).includes(needle)) ok(`${label} contains "${needle.slice(0,40)}"`);
  else fail(`${label} missing "${needle.slice(0,40)}": got "${String(text).slice(0,100)}"`);
}

(async () => {
  section('Build synthetic .jwlibrary');
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  const db = new SQL.Database();

  // Mirror the subset of the JW Library schema the Browse module queries.
  db.run(`
    CREATE TABLE Location (
      LocationId INTEGER PRIMARY KEY,
      BookNumber INTEGER,
      ChapterNumber INTEGER,
      DocumentId INTEGER,
      Track INTEGER,
      IssueTagNumber INTEGER,
      KeySymbol TEXT,
      MepsLanguage INTEGER,
      Type INTEGER,
      Title TEXT
    );
    CREATE TABLE UserMark (
      UserMarkId INTEGER PRIMARY KEY,
      ColorIndex INTEGER,
      LocationId INTEGER,
      StyleIndex INTEGER,
      UserMarkGuid TEXT,
      Version INTEGER
    );
    CREATE TABLE Note (
      NoteId INTEGER PRIMARY KEY,
      Guid TEXT,
      UserMarkId INTEGER,
      LocationId INTEGER,
      Title TEXT,
      Content TEXT,
      LastModified TEXT,
      Created TEXT,
      BlockType INTEGER,
      BlockIdentifier INTEGER
    );
    CREATE TABLE Tag (
      TagId INTEGER PRIMARY KEY,
      Type INTEGER,
      Name TEXT
    );
    CREATE TABLE TagMap (
      TagMapId INTEGER PRIMARY KEY,
      PlaylistItemId INTEGER,
      LocationId INTEGER,
      NoteId INTEGER,
      TagId INTEGER,
      Position INTEGER
    );
    CREATE TABLE Bookmark (
      BookmarkId INTEGER PRIMARY KEY,
      LocationId INTEGER,
      PublicationLocationId INTEGER,
      Slot INTEGER,
      Title TEXT,
      Snippet TEXT,
      BlockType INTEGER,
      BlockIdentifier INTEGER
    );
    CREATE TABLE BlockRange (
      BlockRangeId INTEGER PRIMARY KEY,
      BlockType INTEGER,
      Identifier INTEGER,
      StartToken INTEGER,
      EndToken INTEGER,
      UserMarkId INTEGER
    );
  `);

  // Seed locations
  db.run(`INSERT INTO Location (LocationId, BookNumber, ChapterNumber, KeySymbol, Title) VALUES
    (1, 1, 1, 'nwt', NULL),
    (2, 1, 5, 'nwt', NULL),
    (3, 43, 3, 'nwt', NULL),
    (4, NULL, NULL, 'w23', 'The Watchtower—2023 No. 4'),
    (5, NULL, NULL, 'g23', 'Awake!—2023')`);

  // Seed user marks (highlights), various colors
  db.run(`INSERT INTO UserMark (UserMarkId, ColorIndex, LocationId, UserMarkGuid, Version) VALUES
    (1, 1, 1, 'guid-um-1', 1),
    (2, 2, 2, 'guid-um-2', 1),
    (3, 3, 3, 'guid-um-3', 1),
    (4, 5, 4, 'guid-um-4', 1),
    (5, 6, 4, 'guid-um-5', 1)`);

  // Seed notes (some linked to highlights, some standalone)
  db.run(`INSERT INTO Note (NoteId, Guid, UserMarkId, LocationId, Title, Content, LastModified) VALUES
    (10, 'guid-note-10', 1, 1, 'Beginning thoughts', 'In the beginning God created the heaven and the earth.', '2024-01-15 10:00:00'),
    (11, 'guid-note-11', 2, 2, 'Light', 'And God said let there be light.', '2024-02-20 12:00:00'),
    (12, 'guid-note-12', NULL, 3, 'Faith', 'Now faith is the assured expectation of things hoped for.', '2024-03-05 09:00:00'),
    (13, 'guid-note-13', 4, 4, NULL, 'A standalone observation about the article.', '2024-04-10 14:00:00'),
    (14, 'guid-note-14', NULL, 5, 'Awake note', '<p>This is an HTML note with <br/>line breaks and <strong>bold</strong>.</p>', '2024-05-01 08:30:00')`);

  // Seed tags
  db.run(`INSERT INTO Tag (TagId, Type, Name) VALUES
    (100, 1, 'Study'),
    (101, 1, 'Personal'),
    (102, 1, 'Watchtower')`);

  // Tag maps: tag notes and one location (for a bookmark)
  db.run(`INSERT INTO TagMap (TagMapId, NoteId, LocationId, TagId, Position) VALUES
    (1000, 10, NULL, 100, 0),
    (1001, 11, NULL, 100, 0),
    (1002, 11, NULL, 101, 1),
    (1003, 12, NULL, 100, 0),
    (1004, 13, NULL, 102, 0),
    (1005, NULL, 4, 102, 0)`); // tag on location (bookmark tag)

  // Bookmarks
  db.run(`INSERT INTO Bookmark (BookmarkId, LocationId, PublicationLocationId, Slot, Title, Snippet) VALUES
    (200, 1, 1, 0, 'Genesis 1 bookmark', 'In the beginning...'),
    (201, 4, 4, 1, 'WT 2023-04', 'Article on faith'),
    (202, 5, 5, 2, NULL, NULL)`);

  // BlockRanges (some highlights have block ranges)
  db.run(`INSERT INTO BlockRange (BlockRangeId, BlockType, Identifier, StartToken, EndToken, UserMarkId) VALUES
    (300, 2, 5, 0, 10, 1),
    (301, 2, 12, 3, 8, 2)`);

  const dbBytes = db.export();
  db.close();

  // Pack as .jwlibrary (zip with userData.db inside)
  const zip = new JSZip();
  zip.file('userData.db', dbBytes);
  zip.file('manifest.json', JSON.stringify({ version: 1 }));
  const jwlibBytes = await zip.generateAsync({ type: 'arraybuffer' });
  ok(`Built synthetic .jwlibrary (${jwlibBytes.byteLength} bytes)`);

  section('Boot JSDOM with Browse module');
  // Extract Browse module from the live file
  const html = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
  const m = html.match(/<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<!-- ── End Note Explorer ─[─]*\s*-->/);
  if (!m) { fail('Browse block not found in beta/index.html'); process.exit(1); }
  const browseBlock = m[0];

  // Build minimal page that provides what the module expects.
  const pageHtml = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>
    <script>window.__jwsync_lang_default = 'en';</script>
    ${browseBlock}
  </body></html>`;

  const dom = new JSDOM(pageHtml, {
    url: 'https://jwsync.org/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
  });
  const win = dom.window;
  const doc = win.document;

  // Wire up JSZip + initSqlJs onto the window the module expects.
  win.JSZip = JSZip;
  win.initSqlJs = (opts) => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });

  // Polyfill matchMedia (jsdom doesn't ship one)
  win.matchMedia = (q) => ({ matches: false, media: q, addListener(){}, removeListener(){} });

  // Polyfill localStorage already exists in jsdom; set default language
  win.localStorage.setItem('jwsync_lang', 'en');

  if (typeof win.__openJwBrowse !== 'function') {
    fail('window.__openJwBrowse not exposed after script load');
    process.exit(1);
  }
  ok('Browse module booted; __openJwBrowse exposed');

  // Build a File-like for the module
  const fileLike = {
    name: 'test.jwlibrary',
    arrayBuffer: async () => jwlibBytes,
    // JSZip can accept arrayBuffer-able too via loadAsync(file)
  };
  // JSZip.loadAsync accepts File / Blob / ArrayBuffer / Uint8Array — give it the buffer directly.
  const fileForModule = jwlibBytes;

  section('Open Browse modal');
  win.__openJwBrowse(fileForModule);

  // Wait for the async load chain (JSZip + sql.js + queries) to complete
  async function waitFor(predicate, label, timeoutMs = 8000) {
    const start = Date.now();
    while (Date.now() - start < timeoutMs) {
      try { if (predicate()) return true; } catch (_) {}
      await new Promise(r => setTimeout(r, 50));
    }
    fail('timeout waiting for: ' + label);
    return false;
  }

  // Wait until results render (a note row or "no_results" appears)
  await waitFor(() => {
    const list = doc.querySelector('.jb-list');
    return list && (list.querySelector('.jb-note') || list.querySelector('.jb-empty'));
  }, 'Notes list to render');

  const modal = doc.querySelector('.jb-modal');
  if (!modal) { fail('Modal not rendered'); process.exit(1); }
  ok('Modal rendered');

  section('Notes tab — default render');
  let noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 5, 'Notes row count');

  // Tab counts
  const tabs = doc.querySelectorAll('.jb-tab');
  assertEq(tabs.length, 3, 'Tab count');
  const notesTab = doc.querySelector('.jb-tab[data-type="notes"]');
  const hlTab = doc.querySelector('.jb-tab[data-type="highlights"]');
  const bmTab = doc.querySelector('.jb-tab[data-type="bookmarks"]');
  assertEq(notesTab.querySelector('.jb-tab-count').textContent, '5', 'Notes tab count');
  assertEq(hlTab.querySelector('.jb-tab-count').textContent, '5', 'Highlights tab count');
  assertEq(bmTab.querySelector('.jb-tab-count').textContent, '3', 'Bookmarks tab count');

  // Default sort: newest first → first row should be the most recent (Awake note, 2024-05-01)
  const firstNoteTitle = noteRows[0].querySelector('.jb-note-title span:last-child').textContent;
  assertEq(firstNoteTitle, 'Awake note', 'First row (newest) is Awake note');

  // Untitled note should show "Untitled"
  const untitledRow = Array.from(noteRows).find(r => r.textContent.includes('Untitled'));
  if (untitledRow) ok('Untitled note shows "Untitled" fallback');
  else fail('Untitled note fallback missing');

  // Color dots: the green note should show a color dot
  const greenNote = Array.from(noteRows).find(r => r.textContent.includes('Light'));
  if (greenNote && greenNote.querySelector('.jb-note-color')) ok('Highlighted note shows color dot');
  else fail('Color dot not rendered on highlighted note');

  section('Tag filter');
  const tagSel = doc.querySelector('.jb-filter-tag');
  // Options: All + 3 tags
  assertEq(tagSel.options.length, 4, 'Tag dropdown options (All + 3 tags)');
  // Select "Personal" (TagId=101) — only Note 11 ("Light")
  tagSel.value = '101';
  tagSel.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 1, 'tag filter to apply');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 1, 'Tag=Personal: 1 note');
  assertContains(noteRows[0].textContent, 'Light', 'Tag filter result');
  // Reset
  tagSel.value = '';
  tagSel.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 5, 'tag clear');

  section('Publication filter');
  const pubSel = doc.querySelector('.jb-filter-pub');
  assertGte(pubSel.options.length, 5, 'Publication dropdown has at least 5 options (All + 4 distinct pubs)');
  // Filter to LocationId=4 (Watchtower note)
  pubSel.value = '4';
  pubSel.dispatchEvent(new win.Event('change'));
  await waitFor(() => Array.from(doc.querySelectorAll('.jb-list .jb-note')).every(r => r.textContent.includes('Watchtower')), 'pub filter');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 1, 'Pub=WT2023: 1 note');
  pubSel.value = '';
  pubSel.dispatchEvent(new win.Event('change'));

  section('Color filter');
  const colorBtns = doc.querySelectorAll('.jb-color-dot');
  assertEq(colorBtns.length, 7, 'Color dot buttons (1 All + 6 colors)');
  // Click color 2 (green) — should leave only Note 11 ("Light")
  colorBtns[2].click();
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length <= 1, 'color filter');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 1, 'Color=green: 1 note');
  assertContains(noteRows[0].textContent, 'Light', 'Color filter result');
  colorBtns[0].click(); // reset to All
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 5, 'color reset');

  section('Search');
  const searchInp = doc.querySelector('.jb-search input');
  searchInp.value = 'faith';
  searchInp.dispatchEvent(new win.Event('input'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 1, 'search "faith"');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 1, 'Search "faith": 1 result');
  // Search by publication label
  searchInp.value = 'watchtower';
  searchInp.dispatchEvent(new win.Event('input'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 1, 'search "watchtower"');
  // Empty search
  searchInp.value = '';
  searchInp.dispatchEvent(new win.Event('input'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 5, 'search clear');

  section('Detail pane (Notes)');
  // Click the first note
  doc.querySelectorAll('.jb-list .jb-note')[0].click();
  await waitFor(() => doc.querySelector('.jb-detail-title'), 'detail to render');
  const detailTitle = doc.querySelector('.jb-detail-title').textContent;
  assertContains(detailTitle, 'Awake note', 'Detail title');
  // Note 14 has HTML content with <p>...<br/>...<strong>...
  const detailContent = doc.querySelector('.jb-detail-content').textContent;
  assertContains(detailContent, 'HTML note', 'Detail content text extracted');
  assertContains(detailContent, 'line breaks', 'Detail content preserves text');
  // Copy button exists
  if (doc.querySelector('.jb-detail-actions .jb-btn')) ok('Copy button rendered');
  else fail('Copy button missing');

  section('Switch to Highlights tab');
  hlTab.click();
  await waitFor(() => {
    const head = doc.querySelector('.jb-head-count');
    return head && head.textContent.includes('5');
  }, 'highlights tab count');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 5, 'Highlights row count');
  // First highlight should show "Highlight" label
  const firstHl = noteRows[0].textContent;
  assertContains(firstHl, 'Highlight', 'Highlight row label');

  // Click a highlight to see detail (one with a linked note)
  const linkedHl = Array.from(noteRows).find(r => r.textContent.includes('Beginning thoughts') || r.textContent.includes('Light'));
  if (linkedHl) {
    linkedHl.click();
    await waitFor(() => doc.querySelector('.jb-detail-hl-block'), 'highlight detail');
    const hlBlock = doc.querySelector('.jb-detail-hl-block');
    if (hlBlock && hlBlock.textContent.length > 10) ok('Highlight explainer block rendered');
    else fail('Highlight explainer missing');
    // Linked note section
    if (doc.querySelector('.jb-detail').textContent.includes('Linked note')) ok('Linked-note section rendered');
    else fail('Linked-note section missing');
  } else { fail('No linked highlight to test'); }

  section('Switch to Bookmarks tab');
  bmTab.click();
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'bookmarks render');
  noteRows = doc.querySelectorAll('.jb-list .jb-note');
  assertEq(noteRows.length, 3, 'Bookmarks row count');
  // Slot badges present
  const slots = doc.querySelectorAll('.jb-list .jb-bm-slot');
  assertEq(slots.length, 3, 'Slot badges rendered');
  // Bookmark tag (location-tag) — tagged bookmark on LocationId=4
  const tagSel2 = doc.querySelector('.jb-filter-tag');
  tagSel2.value = '102'; // Watchtower tag → bookmark on LocationId=4 should remain
  tagSel2.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 1, 'bookmark tag filter');
  assertEq(doc.querySelectorAll('.jb-list .jb-note').length, 1, 'Bookmark tag filter result');
  tagSel2.value = '';
  tagSel2.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'bookmark tag clear');

  // Click the bookmark with Snippet to render detail
  const bmWithSnippet = Array.from(doc.querySelectorAll('.jb-list .jb-note')).find(r => r.textContent.includes('In the beginning'));
  if (bmWithSnippet) {
    bmWithSnippet.click();
    await waitFor(() => doc.querySelector('.jb-detail-content'), 'bookmark detail');
    assertContains(doc.querySelector('.jb-detail-content').textContent, 'In the beginning', 'Bookmark detail content');
  }

  section('Clear-all');
  doc.querySelector('.jb-clear').click();
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'clear preserves type'); // still bookmarks tab
  assertEq(doc.querySelector('.jb-search input').value, '', 'Search cleared');
  assertEq(doc.querySelector('.jb-filter-tag').value, '', 'Tag filter cleared');
  assertEq(doc.querySelector('.jb-filter-pub').value, '', 'Pub filter cleared');

  section('Close modal');
  doc.querySelector('.jb-head-close').click();
  if (!doc.querySelector('.jb-overlay')) ok('Modal removed from DOM');
  else fail('Modal still in DOM after close');

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll runtime tests passed.'); dom.window.close(); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  dom.window.close();
  process.exit(1);
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

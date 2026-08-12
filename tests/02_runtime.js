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
    CREATE TABLE InputField (
      LocationId INTEGER,
      TextTag TEXT,
      Value TEXT,
      PRIMARY KEY (LocationId, TextTag)
    );
  `);
  // Seed study answers (Input Fields)
  db.run(`INSERT INTO InputField (LocationId, TextTag, Value) VALUES
    (1, 'q1', 'My answer about creation'),
    (1, 'q2', 'A second study answer'),
    (2, 'q1', 'Reflection on light')`);

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

  // Seed notes (some linked to highlights, some standalone).
  // BlockType 2 / BlockIdentifier is how a Bible note records its verse; note
  // 12 carries one directly, note 10 inherits its verse from the BlockRange of
  // the highlight it is attached to, and note 13 sits in a publication, which
  // has paragraphs rather than verses.
  db.run(`INSERT INTO Note (NoteId, Guid, UserMarkId, LocationId, Title, Content, LastModified, BlockType, BlockIdentifier) VALUES
    (10, 'guid-note-10', 1, 1, 'Beginning thoughts', 'In the beginning God created the heaven and the earth.', '2024-01-15 10:00:00', NULL, NULL),
    (11, 'guid-note-11', 2, 2, 'Light', 'And God said let there be light.', '2024-02-20 12:00:00', NULL, NULL),
    (12, 'guid-note-12', NULL, 3, 'Faith', 'Now faith is the assured expectation of things hoped for.', '2024-03-05 09:00:00', 2, 16),
    (13, 'guid-note-13', 4, 4, NULL, 'A standalone observation about the article.', '2024-04-10 14:00:00', NULL, NULL),
    (14, 'guid-note-14', NULL, 5, 'Awake note', '<p>This is an HTML note with <br/>line breaks and <strong>bold</strong>.</p>', '2024-05-01 08:30:00', NULL, NULL)`);

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
  const browseBlock = require('./helpers/browse-source').browseBlock(REPO + '/beta/index.html');
  if (!browseBlock) { fail('Browse module not found for beta/index.html'); process.exit(1); }

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

  // v2.7.0: the Browse module is wrapped in window.__bootBrowse() and no
  // longer auto-runs on script load. The boot loader calls it on demand;
  // for tests, we call it ourselves.
  if (typeof win.__bootBrowse !== 'function') {
    fail('window.__bootBrowse not exposed after script load');
    process.exit(1);
  }
  win.__bootBrowse();
  if (typeof win.__openJwBrowse !== 'function') {
    fail('window.__openJwBrowse not exposed after __bootBrowse() call');
    process.exit(1);
  }
  ok('Browse module booted via __bootBrowse(); __openJwBrowse exposed');

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

  // Tab counts (4 tabs as of v2.27; the Study Answers tab is hidden when empty)
  const tabs = doc.querySelectorAll('.jb-tab');
  assertEq(tabs.length, 4, 'Tab count');
  const notesTab = doc.querySelector('.jb-tab[data-type="notes"]');
  const hlTab = doc.querySelector('.jb-tab[data-type="highlights"]');
  const bmTab = doc.querySelector('.jb-tab[data-type="bookmarks"]');
  const ifTab = doc.querySelector('.jb-tab[data-type="inputfields"]');
  assertEq(notesTab.querySelector('.jb-tab-count').textContent, '5', 'Notes tab count');
  assertEq(hlTab.querySelector('.jb-tab-count').textContent, '5', 'Highlights tab count');
  assertEq(bmTab.querySelector('.jb-tab-count').textContent, '3', 'Bookmarks tab count');
  if (ifTab && ifTab.style.display !== 'none') ok('Study Answers tab visible (has InputField rows)');
  else fail('Study Answers tab should be visible with InputField rows');
  assertEq(ifTab.querySelector('.jb-tab-count').textContent, '3', 'Study Answers tab count');

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

  section('Date-range filter (v2.21.0)');
  // Notes span 2024-01-15 .. 2024-05-01. Two date inputs live in the toolbar.
  const dateInputs = doc.querySelectorAll('.jb-filter-date');
  assertEq(dateInputs.length, 2, 'two date inputs in toolbar');
  const [dFrom, dTo] = dateInputs;
  dFrom.value = '2024-03-01';
  dFrom.dispatchEvent(new win.Event('change'));
  dTo.value = '2024-04-30';
  dTo.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 2, 'date range 03-01..04-30');
  assertEq(doc.querySelectorAll('.jb-list .jb-note').length, 2, 'date range shows 2 notes (Mar+Apr)');
  const extractBtn = doc.querySelector('.jb-extract-btn');
  if (extractBtn && !extractBtn.disabled) ok('extract button enabled when a date is set');
  else fail('extract button should be enabled with a date set');

  // Lower-bound only
  dTo.value = '';
  dTo.dispatchEvent(new win.Event('change'));
  dFrom.value = '2024-05-01';
  dFrom.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 1, 'from 2024-05-01');
  assertEq(doc.querySelectorAll('.jb-list .jb-note').length, 1, 'from 2024-05-01 shows 1 note (May)');

  section('Date extract → pruned .jwlibrary');
  // Extract Jan+Feb (2 notes) into a new backup; capture the generated Blob.
  dFrom.value = '2024-01-01';
  dFrom.dispatchEvent(new win.Event('change'));
  dTo.value = '2024-02-28';
  dTo.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 2, 'date range Jan+Feb');
  let capturedBlob = null;
  const origCOU = win.URL.createObjectURL;
  win.URL.createObjectURL = (b) => { capturedBlob = b; return 'blob:capture'; };
  win.URL.revokeObjectURL = () => {};
  doc.querySelector('.jb-extract-btn').click();
  await waitFor(() => capturedBlob !== null, 'extract to produce a blob');
  win.URL.createObjectURL = origCOU;
  if (capturedBlob) {
    ok('extract produced a .jwlibrary blob');
    const buf = Buffer.from(await capturedBlob.arrayBuffer());
    const ezip = await JSZip.loadAsync(buf);
    const ekey = Object.keys(ezip.files).find(n => /userdata\.db$/i.test(n));
    const ebytes = await ezip.files[ekey].async('uint8array');
    const SQLx = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
    const edb = new SQLx.Database(ebytes);
    const res = edb.exec('SELECT COUNT(*) FROM Note');
    const cnt = res[0].values[0][0];
    assertEq(cnt, 2, 'extracted backup contains only the 2 in-range notes');
    edb.close();
  }

  // Reset date filter so later sections see all 5 notes again.
  dFrom.value = '';
  dFrom.dispatchEvent(new win.Event('change'));
  dTo.value = '';
  dTo.dispatchEvent(new win.Event('change'));
  await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 5, 'date filter cleared');

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
  // v2.17.0: formatted note content rendered (not flattened to text)
  const detailHtml = doc.querySelector('.jb-detail-content').innerHTML;
  if (/<(strong|b)>/i.test(detailHtml)) ok('Note detail renders bold formatting (not plain text)');
  else fail('Note detail lost formatting: ' + detailHtml);

  section('Markdown sharing & export (v2.23.0)');
  // Detail pane should now offer a "Copy as Markdown" action alongside Copy.
  const actionBtns = Array.from(doc.querySelectorAll('.jb-detail-actions .jb-btn'));
  if (actionBtns.length >= 2) ok('Copy + Copy-as-Markdown actions rendered');
  else fail('expected >=2 detail action buttons, got ' + actionBtns.length);
  // Header Export-Markdown button
  const mdExportBtn = doc.querySelector('.jb-md-btn');
  if (mdExportBtn) ok('"Export Markdown" header button present');
  else fail('Export Markdown button missing');
  if (mdExportBtn) {
    let mdBlob = null;
    const origCOU = win.URL.createObjectURL;
    win.URL.createObjectURL = (b) => { mdBlob = b; return 'blob:md'; };
    win.URL.revokeObjectURL = () => {};
    mdExportBtn.click();
    await waitFor(() => mdBlob !== null, 'markdown zip to generate');
    win.URL.createObjectURL = origCOU;
    if (mdBlob) {
      ok('Markdown export produced a .zip blob');
      const zip = await JSZip.loadAsync(Buffer.from(await mdBlob.arrayBuffer()));
      const mdFiles = Object.keys(zip.files).filter(n => /\.md$/.test(n));
      assertEq(mdFiles.length, 5, 'one .md per note (5 total)');
      // The "Awake note" has <strong>bold</strong> → expect **bold** in its markdown
      let foundBold = false, foundFrontmatter = false;
      const mdTexts = [];
      for (const fn of mdFiles) {
        const txt = await zip.files[fn].async('string');
        mdTexts.push(txt);
        if (txt.includes('**bold**')) foundBold = true;
        if (/^---[\s\S]*title:/.test(txt)) foundFrontmatter = true;
      }
      if (foundBold) ok('HTML <strong> converted to Markdown **bold**');
      else fail('bold not converted to Markdown');
      if (foundFrontmatter) ok('Markdown files include YAML frontmatter');
      else fail('no frontmatter in Markdown output');

      // Verse in the front matter. Location stops at the chapter, so this only
      // works if the export reads the note's own BlockIdentifier and the
      // BlockRange of any highlight it is attached to.
      const has = (needle) => mdTexts.some(t => t.includes(needle));
      if (has('publication: John 3:16')) ok('verse from the note itself (John 3:16)');
      else fail('note 12 exported without its verse: ' +
        (mdTexts.find(t => t.includes('John 3')) || '').split('\n').slice(0, 8).join(' | '));
      if (has('book: John') && has('chapter: 3') && has('verse: 16'))
        ok('book / chapter / verse also emitted as discrete fields');
      else fail('discrete book/chapter/verse fields missing from front matter');
      if (has('publication: Genesis 1:5')) ok("verse from the attached highlight's BlockRange (Genesis 1:5)");
      else fail('note 10 exported without the verse its highlight covers');
      // A publication has paragraphs, not verses — it must not grow a verse line.
      const wt = mdTexts.find(t => t.includes('The Watchtower'));
      if (wt && !/\nverse:/.test(wt)) ok('publication note exports with no verse field');
      else fail('a publication note was given a verse');
    }
  }

  section('Rich-text edit mode (Notes)');
  {
    // Find + click the Edit button in the detail actions
    const editBtn = Array.from(doc.querySelectorAll('.jb-detail-actions .jb-btn'))
      .find(b => /edit/i.test(b.textContent));
    if (!editBtn) fail('Edit button not found in note detail');
    else {
      editBtn.click();
      await waitFor(() => doc.querySelector('.jb-edit-rte'), 'rich-text editor to render');
      const rte = doc.querySelector('.jb-edit-rte');
      if (rte) ok('rich-text editor (.jb-edit-rte) rendered');
      else fail('.jb-edit-rte not rendered');
      if (rte && rte.getAttribute('contenteditable') === 'true') ok('editor is contentEditable');
      else fail('editor not contentEditable');
      if (rte && /<(strong|b)>/i.test(rte.innerHTML)) ok('editor preserves <strong>/<b> from the note');
      else fail('editor flattened formatting: ' + (rte && rte.innerHTML));
      const tools = doc.querySelectorAll('.jb-rte-toolbar .jb-rte-btn');
      if (tools.length === 4) ok('toolbar has 4 buttons (B/I/U/bullets)');
      else fail('toolbar buttons: ' + tools.length);
      // Cancel back out so later sections see read view
      const cancelBtn = Array.from(doc.querySelectorAll('.jb-detail-actions .jb-btn'))
        .find(b => /cancel/i.test(b.textContent));
      if (cancelBtn) cancelBtn.click();
      await waitFor(() => doc.querySelector('.jb-detail-content'), 'return to read view');
    }
  }

  section('Bulk select + batch actions + Undo/Redo (v2.26.0)');
  {
    const wait = (ms) => new Promise(r => setTimeout(r, ms));
    // Helper: click Export, capture the generated .jwlibrary blob, open its DB.
    async function exportAndRead() {
      let blob = null;
      const origCOU = win.URL.createObjectURL;
      win.URL.createObjectURL = (b) => { blob = b; return 'blob:exp'; };
      win.URL.revokeObjectURL = () => {};
      doc.querySelector('.jb-export-btn').click();
      await waitFor(() => blob !== null, 'export blob');
      win.URL.createObjectURL = origCOU;
      const zip = await JSZip.loadAsync(Buffer.from(await blob.arrayBuffer()));
      const key = Object.keys(zip.files).find(n => /userdata\.db$/i.test(n));
      const bytes = await zip.files[key].async('uint8array');
      const SQLx = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
      return new SQLx.Database(bytes);
    }
    // Observe the tag filter dropdown (repopulated after every edit/undo).
    const tagInFilter = () => /BulkTag/.test(doc.querySelector('.jb-filter-tag').textContent);

    // Enter select mode
    const selToggle = doc.querySelector('.jb-select-toggle');
    if (selToggle) ok('Select toggle present in toolbar'); else fail('Select toggle missing');
    selToggle.click();
    await waitFor(() => doc.querySelector('.jb-note.jb-selectable'), 'rows become selectable');
    // Select the first two note rows
    const rows = doc.querySelectorAll('.jb-list .jb-note.jb-selectable');
    rows[0].click(); rows[1].click();
    await waitFor(() => doc.querySelectorAll('.jb-check.jb-check-on').length === 2, 'two rows checked');
    ok('two notes selected (checkboxes on)');
    const bar = doc.querySelector('.jb-batch-bar');
    if (bar && bar.style.display !== 'none') ok('batch bar visible with selection');
    else fail('batch bar not visible');

    // Batch add tag "BulkTag" — verify via the tag filter (no export needed)
    Array.from(bar.querySelectorAll('.jb-batch-btn')).find(b => /tag/i.test(b.textContent)).click();
    await waitFor(() => doc.querySelector('.jb-batch-input'), 'tag input appears');
    const tagInput = doc.querySelector('.jb-batch-input');
    tagInput.value = 'BulkTag';
    Array.from(doc.querySelectorAll('.jb-batch-bar .jb-batch-btn')).find(b => /add|agregar|adicionar|ajouter/i.test(b.textContent)).click();
    await waitFor(() => tagInFilter(), 'BulkTag appears after batch add');
    ok('batch tag applied (appears in tag filter)');

    // Undo → tag gone (export disabled at baseline, so verify via filter)
    doc.querySelector('.jb-undo').click();
    await waitFor(() => !tagInFilter(), 'BulkTag gone after Undo');
    ok('Undo removed the batch tag');

    // Redo → tag back
    doc.querySelector('.jb-redo').click();
    await waitFor(() => tagInFilter(), 'BulkTag back after Redo');
    ok('Redo re-applied the batch tag');

    // Batch delete the two selected notes, then Undo to restore (dirty>0 → export works)
    const before = await exportAndRead();
    const noteCountBefore = before.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
    before.close();
    // Re-enter selection (delete clears it); select the same two rows
    const rows2 = doc.querySelectorAll('.jb-list .jb-note.jb-selectable');
    rows2[0].click(); rows2[1].click();
    await waitFor(() => doc.querySelectorAll('.jb-check.jb-check-on').length === 2, 're-select two');
    Array.from(doc.querySelectorAll('.jb-batch-bar .jb-batch-btn')).find(b => /delete|eliminar|excluir|supprimer|löschen/i.test(b.textContent)).click();
    await waitFor(() => /\?|undo/i.test(doc.querySelector('.jb-batch-bar').textContent), 'delete confirm shows');
    Array.from(doc.querySelectorAll('.jb-batch-bar .jb-batch-btn')).find(b => /yes|sí|sim|oui|ja|delete/i.test(b.textContent)).click();
    await wait(80);
    let db = await exportAndRead();
    const noteCountAfter = db.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
    db.close();
    if (noteCountAfter === noteCountBefore - 2) ok('batch delete removed 2 notes (' + noteCountBefore + '→' + noteCountAfter + ')');
    else fail('batch delete expected ' + (noteCountBefore - 2) + ', got ' + noteCountAfter);
    doc.querySelector('.jb-undo').click();
    await wait(80);
    db = await exportAndRead();
    const restored = db.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
    db.close();
    assertEq(restored, noteCountBefore, 'Undo restored the deleted notes');

    // Exit select mode for subsequent sections
    doc.querySelector('.jb-select-toggle').click();
    await wait(40);
    if (!doc.querySelector('.jb-note.jb-selectable')) ok('exited select mode');
    else fail('still in select mode');

    // Undo back to the pristine loaded state so later sections (and the close
    // test, which prompts on unsaved edits) see the original library again.
    let guard = 0;
    while (!doc.querySelector('.jb-undo').disabled && guard++ < 40) {
      doc.querySelector('.jb-undo').click();
      await wait(20);
    }
    await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 5, 'restored to 5 original notes');
    if (doc.querySelector('.jb-export-btn').disabled) ok('clean baseline restored (export disabled)');
    else fail('expected clean baseline after undo-all');
  }

  section('Note sharing — quick share envelope + page entry (v2.28/v2.30)');
  {
    const wait = (ms) => new Promise(r => setTimeout(r, ms));
    // Quick in-context share: select 2 notes → batch Share → envelope built.
    doc.querySelector('.jb-select-toggle').click();
    await waitFor(() => doc.querySelector('.jb-note.jb-selectable'), 'selectable rows');
    const rs = doc.querySelectorAll('.jb-list .jb-note.jb-selectable');
    rs[0].click(); rs[1].click();
    await waitFor(() => doc.querySelectorAll('.jb-check.jb-check-on').length === 2, '2 selected');
    Array.from(doc.querySelectorAll('.jb-batch-bar .jb-batch-btn')).find(b => /share/i.test(b.textContent)).click();
    await waitFor(() => doc.querySelector('.jbs-overlay .jbs-text'), 'share overlay');
    const env = JSON.parse(doc.querySelector('.jbs-overlay .jbs-text').value);
    if (env.app === 'jwsync' && Array.isArray(env.notes) && env.notes.length === 2) ok('quick-share envelope built (2 notes)');
    else fail('share envelope malformed');
    doc.querySelector('.jbs-overlay .jbs-x').click();
    doc.querySelector('.jb-select-toggle').click();
    await wait(30);

    // The header button now routes to the dedicated, explained Share page.
    const headerShare = Array.from(doc.querySelectorAll('.jb-md-btn')).find(b => /share notes|→/i.test(b.textContent) && !/markdown/i.test(b.textContent));
    if (headerShare) ok('header "Share Notes →" button present (opens dedicated page)');
    else fail('header Share-page button missing');
  }

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

  section('Study Answers tab — edit + delete + undo (v2.27.0)');
  {
    const wait = (ms) => new Promise(r => setTimeout(r, ms));
    doc.querySelector('.jb-tab[data-type="inputfields"]').click();
    await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'study answers render');
    ok('Study Answers tab lists 3 answers');
    // Open the first answer and edit its value
    doc.querySelectorAll('.jb-list .jb-note')[0].click();
    await waitFor(() => doc.querySelector('.jb-detail-content'), 'answer detail');
    Array.from(doc.querySelectorAll('.jb-detail-actions .jb-btn')).find(b => /edit/i.test(b.textContent)).click();
    await waitFor(() => doc.querySelector('.jb-edit-textarea'), 'answer edit textarea');
    doc.querySelector('.jb-edit-textarea').value = 'EDITED ANSWER';
    Array.from(doc.querySelectorAll('.jb-detail-actions .jb-btn')).find(b => /save/i.test(b.textContent)).click();
    await waitFor(() => /EDITED ANSWER/.test(doc.querySelector('.jb-detail-content').textContent), 'edit persisted in view');
    ok('study answer edit saved (shown in detail)');
    // Delete an answer → 2 remain; Undo → back to 3
    Array.from(doc.querySelectorAll('.jb-detail-actions button')).find(b => /delete/i.test(b.textContent) && !/confirm/i.test(b.className)).click();
    await waitFor(() => doc.querySelector('.jb-delete-confirm') || /\?/.test(doc.querySelector('.jb-detail-actions').textContent), 'delete confirm');
    Array.from(doc.querySelectorAll('.jb-detail-actions button')).find(b => /yes|sí|sim|oui|ja/i.test(b.textContent)).click();
    await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 2, 'answer deleted (3→2)');
    ok('study answer deleted');
    doc.querySelector('.jb-undo').click();
    await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'undo restored answer');
    ok('Undo restored the deleted answer');
    // Undo back to pristine + return to bookmarks tab for the remaining sections
    let g = 0;
    while (!doc.querySelector('.jb-undo').disabled && g++ < 40) { doc.querySelector('.jb-undo').click(); await wait(20); }
    doc.querySelector('.jb-tab[data-type="bookmarks"]').click();
    await waitFor(() => doc.querySelectorAll('.jb-list .jb-note').length === 3, 'back to bookmarks');
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

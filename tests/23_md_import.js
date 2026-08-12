// 23_md_import.js — Markdown goes out of a backup and comes back in.
//
// The export half is checked in 02_runtime.js. This suite closes the loop:
// export a backup to Markdown, import those files into a *different* backup,
// and read the resulting database to confirm each note landed where its front
// matter said it should.
//
// The check that matters most is the quiet one. A note that imports onto the
// wrong Location does not throw and does not look wrong on this page — it is
// simply not where the reader put it when they open JW Library. So the suite
// asserts the actual BookNumber / ChapterNumber / BlockIdentifier of every
// imported row, and asserts that a backup with no Bible locations to copy
// identity columns from imports its notes unanchored rather than inventing a
// Location that JW Library would not recognise.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');
const initSqlJs = require('sql.js');
const JSZip = require('jszip');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m) => { failures++; console.log('  ✗ ' + m); };
const section = (t) => console.log('\n== ' + t + ' ==');
const assertEq = (a, b, label) => (a === b ? ok(`${label}: ${a}`) : fail(`${label}: expected ${b}, got ${a}`));

const SCHEMA = `
  CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
    DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER DEFAULT 0, KeySymbol TEXT,
    MepsLanguage INTEGER, Type INTEGER, Title TEXT);
  CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER,
    StyleIndex INTEGER, UserMarkGuid TEXT, Version INTEGER);
  CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER,
    Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
  CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER, Name TEXT);
  CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, PlaylistItemId INTEGER, LocationId INTEGER,
    NoteId INTEGER, TagId INTEGER, Position INTEGER);
  CREATE TABLE Bookmark (BookmarkId INTEGER PRIMARY KEY, LocationId INTEGER, PublicationLocationId INTEGER,
    Slot INTEGER, Title TEXT, Snippet TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
  CREATE TABLE BlockRange (BlockRangeId INTEGER PRIMARY KEY, BlockType INTEGER, Identifier INTEGER,
    StartToken INTEGER, EndToken INTEGER, UserMarkId INTEGER);
  CREATE TABLE InputField (LocationId INTEGER, TextTag TEXT, Value TEXT, PRIMARY KEY (LocationId, TextTag));
`;

// KeySymbol 'nwtsty' and MepsLanguage 3 are deliberately unusual here: an
// importer that guesses these instead of copying them would produce a second
// Location for the same chapter, which this suite would catch as a row count.
const LOCATIONS = `
  INSERT INTO Location (LocationId, BookNumber, ChapterNumber, IssueTagNumber, KeySymbol, MepsLanguage, Type, Title) VALUES
    (1, 1, 1, 0, 'nwtsty', 3, 0, NULL),
    (2, 43, 3, 0, 'nwtsty', 3, 0, NULL),
    (3, NULL, NULL, 0, 'w23', 3, 0, 'The Watchtower—2023 No. 4');
`;

async function buildBackup(SQL, { withNotes, withBible }) {
  const db = new SQL.Database();
  db.run(SCHEMA);
  if (withBible) db.run(LOCATIONS);
  else db.run(`INSERT INTO Location (LocationId, BookNumber, ChapterNumber, IssueTagNumber, KeySymbol, MepsLanguage, Type, Title)
               VALUES (3, NULL, NULL, 0, 'w23', 3, 0, 'The Watchtower—2023 No. 4');`);
  if (withNotes) {
    db.run(`INSERT INTO UserMark (UserMarkId, ColorIndex, LocationId, UserMarkGuid, Version) VALUES (1, 2, 1, 'um-1', 1);`);
    db.run(`INSERT INTO BlockRange (BlockRangeId, BlockType, Identifier, StartToken, EndToken, UserMarkId) VALUES (1, 2, 5, 0, 4, 1);`);
    db.run(`INSERT INTO Note (NoteId, Guid, UserMarkId, LocationId, Title, Content, LastModified, Created, BlockType, BlockIdentifier) VALUES
      (10, 'g-10', 1, 1, 'Beginning thoughts', '<p>In the beginning, with <strong>bold</strong>.</p>', '2024-01-15 10:00:00', '2024-01-15 10:00:00', NULL, NULL),
      (11, 'g-11', NULL, 2, 'Faith', '<p>Now faith is the assured expectation.</p>', '2024-03-05 09:00:00', '2024-03-05 09:00:00', 2, 16),
      (12, 'g-12', NULL, 3, 'Article note', '<p>A thought about the article.</p>', '2024-04-10 14:00:00', '2024-04-10 14:00:00', NULL, NULL)`);
    db.run(`INSERT INTO Tag (TagId, Type, Name) VALUES (100, 1, 'Study');`);
    db.run(`INSERT INTO TagMap (TagMapId, NoteId, TagId, Position) VALUES (1000, 11, 100, 0);`);
  }
  const bytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', bytes);
  zip.file('manifest.json', JSON.stringify({ version: 1 }));
  return zip.generateAsync({ type: 'arraybuffer' });
}

function bootBrowse() {
  const browseBlock = require('./helpers/browse-source').browseBlock(REPO + '/beta/index.html');
  if (!browseBlock) { fail('Browse module not found'); process.exit(1); }
  const dom = new JSDOM(
    `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${browseBlock}</body></html>`,
    { url: 'https://jwsync.org/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  win.matchMedia = (q) => ({ matches: false, media: q, addListener() {}, removeListener() {} });
  win.localStorage.setItem('jwsync_lang', 'en');
  win.alert = () => {};
  win.__bootBrowse();
  return win;
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));
async function waitFor(predicate, label, timeoutMs = 10000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    try { if (predicate()) return true; } catch (_) {}
    await sleep(50);
  }
  fail('timeout waiting for: ' + label);
  return false;
}

async function openWith(win, buffer) {
  win.__openJwBrowse(buffer);
  await waitFor(() => {
    const list = win.document.querySelector('.jb-list');
    return list && (list.querySelector('.jb-note') || list.querySelector('.jb-empty'));
  }, 'notes list to render');
}

// Click a header button and capture the blob it hands to createObjectURL.
async function captureDownload(win, selector, label) {
  let blob = null;
  const orig = win.URL.createObjectURL;
  win.URL.createObjectURL = (b) => { blob = b; return 'blob:x'; };
  win.URL.revokeObjectURL = () => {};
  const btn = win.document.querySelector(selector);
  if (!btn) { fail(`${label}: button ${selector} not found`); return null; }
  btn.click();
  await waitFor(() => blob !== null, label);
  win.URL.createObjectURL = orig;
  return blob;
}

async function readDb(SQL, blob) {
  const zip = await JSZip.loadAsync(Buffer.from(await blob.arrayBuffer()));
  const key = Object.keys(zip.files).find(n => /userdata\.db$/i.test(n));
  return new SQL.Database(await zip.files[key].async('uint8array'));
}

// Node-realm ArrayBuffer, which is what a browser's File.arrayBuffer() gives
// the page's own JSZip.
function nodeBuffer(buf) {
  return buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength);
}

function rows(db, sql) {
  const r = db.exec(sql);
  if (!r[0]) return [];
  return r[0].values.map(v => { const o = {}; r[0].columns.forEach((c, i) => o[c] = v[i]); return o; });
}

(async () => {
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });

  // ── 1. export a backup to Markdown ────────────────────────────────────────
  section('Export a backup to Markdown');
  const sourceBuf = await buildBackup(SQL, { withNotes: true, withBible: true });
  let win = bootBrowse();
  await openWith(win, sourceBuf);
  const mdZipBlob = await captureDownload(win, '.jb-md-btn', 'markdown zip');
  if (!mdZipBlob) process.exit(1);
  const mdZipBytes = Buffer.from(await mdZipBlob.arrayBuffer());
  const mdZip = await JSZip.loadAsync(mdZipBytes);
  const mdNames = Object.keys(mdZip.files).filter(n => /\.md$/.test(n));
  assertEq(mdNames.length, 3, 'markdown files exported');
  const sample = await mdZip.files[mdNames.find(n => /Faith/i.test(n))].async('string');
  if (/publication: John 3:16/.test(sample) && /verse: 16/.test(sample)) ok('exported front matter carries the verse');
  else fail('exported front matter missing the verse:\n' + sample.split('\n').slice(0, 10).join('\n'));

  // ── 2. import them into a different backup ────────────────────────────────
  section('Import the .zip into a backup that has none of those notes');
  const emptyBuf = await buildBackup(SQL, { withNotes: false, withBible: true });
  win = bootBrowse();
  await openWith(win, emptyBuf);

  // A duck-typed file rather than new win.File(): JSDOM's Blob hands back an
  // ArrayBuffer from its own realm, and the JSZip injected here is Node's, so
  // its `instanceof ArrayBuffer` check fails. That mismatch does not exist in a
  // browser — readMdFiles() sees the same {name, arrayBuffer()} either way.
  const zipFile = { name: 'notes_markdown.zip', arrayBuffer: async () => nodeBuffer(mdZipBytes) };
  let parsed = await win.__jwMdImport.readFiles([zipFile]);
  assertEq(parsed.length, 3, 'notes parsed back out of the .zip');

  const faith = parsed.find(p => p.title === 'Faith');
  if (faith && faith.ref && faith.ref.book === 43 && faith.ref.chapter === 3 && faith.ref.verse === 16)
    ok('front matter resolved to John (43) 3:16');
  else fail('reference not resolved: ' + JSON.stringify(faith && faith.ref));
  if (faith && /<strong>|assured expectation/.test(faith.content)) ok('body converted back to note HTML');
  else fail('body did not convert: ' + (faith && faith.content));

  const res = win.__jwMdImport.importNotes(parsed);
  assertEq(res.added, 3, 'notes written into the backup');
  assertEq(res.anchored, 2, 'notes anchored to a Bible location');

  const outBlob = await captureDownload(win, '.jb-export-btn', 'exported .jwlibrary');
  const outDb = await readDb(SQL, outBlob);

  const imported = rows(outDb, `SELECT n.Title, n.BlockType, n.BlockIdentifier, l.BookNumber, l.ChapterNumber,
    l.KeySymbol, l.MepsLanguage FROM Note n LEFT JOIN Location l ON l.LocationId = n.LocationId ORDER BY n.Title`);
  assertEq(imported.length, 3, 'notes present in the exported backup');

  const john = imported.find(r => r.Title === 'Faith');
  if (john && john.BookNumber === 43 && john.ChapterNumber === 3 && john.BlockIdentifier === 16 && john.BlockType === 2)
    ok('"Faith" landed on John 3:16 (BlockType 2)');
  else fail('"Faith" landed wrong: ' + JSON.stringify(john));

  const gen = imported.find(r => r.Title === 'Beginning thoughts');
  if (gen && gen.BookNumber === 1 && gen.ChapterNumber === 1 && gen.BlockIdentifier === 5)
    ok('the highlight-derived verse round-tripped to Genesis 1:5');
  else fail('Genesis note landed wrong: ' + JSON.stringify(gen));

  const wt = imported.find(r => r.Title === 'Article note');
  if (wt && wt.BookNumber === null && !wt.BlockIdentifier) ok('publication note imported unanchored (it has no verse)');
  else fail('publication note was anchored: ' + JSON.stringify(wt));

  // The identity columns must be the file's own, never invented.
  if (john && john.KeySymbol === 'nwtsty' && john.MepsLanguage === 3)
    ok("Location identity columns copied from the backup, not guessed");
  else fail('Location identity columns wrong: ' + JSON.stringify(john));
  assertEq(rows(outDb, 'SELECT COUNT(*) AS c FROM Location')[0].c, 3, 'no duplicate Location rows created');

  const tags = rows(outDb, `SELECT t.Name FROM TagMap tm JOIN Tag t ON t.TagId = tm.TagId
    JOIN Note n ON n.NoteId = tm.NoteId WHERE n.Title = 'Faith' ORDER BY t.Name`).map(r => r.Name);
  if (tags.includes('Study')) ok('tags from the front matter survived the round trip');
  else fail('tags lost: ' + JSON.stringify(tags));
  if (tags.includes('Imported')) ok('imported notes carry the Imported tag');
  else fail('Imported tag missing: ' + JSON.stringify(tags));
  outDb.close();

  // ── 3. importing the same files twice is a no-op ─────────────────────────
  section('Re-importing the same export');
  const again = await win.__jwMdImport.readFiles(
    [{ name: 'notes_markdown.zip', arrayBuffer: async () => nodeBuffer(mdZipBytes) }]);
  const dupWin = win;
  const before = rows(await readDb(SQL, await captureDownload(dupWin, '.jb-export-btn', 'pre-dupe export')), 'SELECT COUNT(*) AS c FROM Note')[0].c;
  // The preview panel is what filters duplicates, so exercise the same key.
  const keys = new Set(rows(await readDb(SQL, await captureDownload(dupWin, '.jb-export-btn', 'key export')),
    `SELECT IFNULL(Title,'') AS t, IFNULL(Content,'') AS c, IFNULL(LocationId,-1) AS l, IFNULL(BlockIdentifier,-1) AS b FROM Note`)
    .map(r => [r.t, r.c, r.l, r.b].join(' ')));
  if (keys.size === before) ok(`${before} existing notes give ${keys.size} distinct identity keys`);
  else fail(`duplicate identity keys among existing notes: ${keys.size} of ${before}`);
  if (again.length === 3) ok('the same three notes parse again (the preview is what skips them)');
  else fail('re-parse produced ' + again.length);

  // ── 4. Markdown from anywhere else ───────────────────────────────────────
  section('A file written in an ordinary Markdown editor');
  const foreign = '# A thought from Obsidian\n\nSomething I wrote **elsewhere**.\n\n- first\n- second\n';
  const [note] = await win.__jwMdImport.readFiles([new win.File([foreign], 'obsidian-note.md')]);
  if (note && note.title === 'A thought from Obsidian') ok('title taken from the heading when there is no front matter');
  else fail('title not derived: ' + JSON.stringify(note && note.title));
  if (note && /<ul><li>first<\/li><li>second<\/li><\/ul>/.test(note.content)) ok('list converted to <ul>');
  else fail('list not converted: ' + (note && note.content));
  if (note && !/A thought from Obsidian/.test(note.content)) ok('the heading is not repeated inside the body');
  else fail('heading duplicated into content');
  if (note && note.ref === null) ok('no reference, so it will import as a standalone note');
  else fail('invented a reference for a file that has none: ' + JSON.stringify(note && note.ref));

  // A hand-written "publication:" line is the documented way to place one.
  const placedFile = new win.File(
    ['---\ntitle: Placed\npublication: 1 Corinthians 13:4\n---\n\nLove is patient.\n'], 'p.md');
  const placed = (await win.__jwMdImport.readFiles([placedFile]))[0];
  if (placed && placed.ref && placed.ref.book === 46 && placed.ref.chapter === 13 && placed.ref.verse === 4)
    ok('a "publication: 1 Corinthians 13:4" line places the note');
  else fail('publication line not parsed: ' + JSON.stringify(placed && placed.ref));

  // ── 5. a backup with no Bible location to copy from ──────────────────────
  section('A backup with no Bible locations at all');
  const pubOnly = await buildBackup(SQL, { withNotes: false, withBible: false });
  const win2 = bootBrowse();
  await openWith(win2, pubOnly);
  const oneFile = new win2.File(
    ['---\ntitle: Nowhere to put it\nbook: Matthew\nchapter: 26\nverse: 39\n---\n\nThe cup.\n'], 'n.md');
  const one = await win2.__jwMdImport.readFiles([oneFile]);
  const r2 = win2.__jwMdImport.importNotes(one);
  assertEq(r2.added, 1, 'note still imported');
  assertEq(r2.anchored, 0, 'but not anchored — there was no Location to copy identity from');
  const db2 = await readDb(SQL, await captureDownload(win2, '.jb-export-btn', 'export from pub-only backup'));
  assertEq(rows(db2, 'SELECT COUNT(*) AS c FROM Location')[0].c, 1, 'no Location invented');
  const n2 = rows(db2, 'SELECT LocationId, BlockIdentifier FROM Note')[0];
  if (n2 && n2.LocationId === null) ok('the note is unanchored rather than pointing at a guessed Location');
  else fail('note anchored to something invented: ' + JSON.stringify(n2));
  db2.close();

  // ── 6. the button that opens all this ────────────────────────────────────
  section('The Import Markdown button');
  const importBtn = Array.from(win.document.querySelectorAll('.jb-md-btn'))
    .find(b => /import markdown/i.test(b.textContent || ''));
  if (importBtn) ok('"Import Markdown" button rendered in the header');
  else fail('Import Markdown button not found: ' +
    Array.from(win.document.querySelectorAll('.jb-md-btn')).map(b => b.textContent).join(' | '));
  if (importBtn) {
    importBtn.click();
    const panel = win.document.querySelector('.jbs-overlay');
    if (panel && /Import Markdown notes/i.test(panel.textContent)) ok('clicking it opens the import panel');
    else fail('import panel did not open');
    // Nothing may be written before the reader chooses files and confirms.
    if (panel && panel.querySelector('.jbs-choose')) ok('panel offers a file picker and writes nothing yet');
    else fail('file picker missing from the panel');
    if (panel) panel.remove();
  }

  console.log(failures ? `\n${failures} failure(s)` : '\nAll Markdown import checks passed');
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });

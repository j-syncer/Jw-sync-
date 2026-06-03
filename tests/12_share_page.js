// Integration test for the v2.30.0 standalone Share page (beta/share.html).
//
// The page is a self-contained standalone tool (like highlights.html) with two
// flows: SEND (open a backup → tick notes → create a .jwshare.json) and RECEIVE
// (paste/choose a shared file → preview → adopt into one of your backups). It
// boots in JSDOM with JSZip + sql.js wired onto window, and exposes test hooks
// __shLoadBackup / __shRenderReceive / __shAdopt.
//
// Asserts:
//   1. Home renders the two mode cards
//   2. SEND: a loaded backup lists notes; select-all + create builds a valid
//      jwsync envelope containing the notes
//   3. RECEIVE: pasting an envelope previews the notes read-only
//   4. ADOPT: adopting into a backup produces an updated .jwlibrary with the
//      shared notes added (tagged) — verified by re-opening the exported DB
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');
const SHARE_PATH = REPO + '/beta/share.html';
const SQL_OPTS = { locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) };

let failures = 0;
function ok(m) { console.log('  ✓', m); }
function fail(m) { console.log('  ✗', m); failures++; }
function section(n) { console.log('\n== ' + n + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

async function buildBackup(SQL, notes) {
  const db = new SQL.Database();
  db.run(`CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER, Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER DEFAULT 1, BlockIdentifier INTEGER DEFAULT 0);
    CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER, StyleIndex INTEGER DEFAULT 0, UserMarkGuid TEXT, Version INTEGER DEFAULT 1);
    CREATE TABLE BlockRange (BlockRangeId INTEGER PRIMARY KEY, BlockType INTEGER, Identifier INTEGER, StartToken INTEGER, EndToken INTEGER, UserMarkId INTEGER);
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER, DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER DEFAULT 0, KeySymbol TEXT, MepsLanguage INTEGER DEFAULT 0, Type INTEGER DEFAULT 0, Title TEXT);
    CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER, Name TEXT);
    CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, NoteId INTEGER, LocationId INTEGER, TagId INTEGER, Position INTEGER);
    CREATE UNIQUE INDEX IX_TagMap_TagId_Position ON TagMap (TagId, Position);`);
  db.run(`INSERT INTO Location (LocationId, BookNumber, ChapterNumber, KeySymbol, Title) VALUES (1,1,1,'nwt','Genesis'),(2,null,null,'w23','Watchtower')`);
  (notes || []).forEach(n => {
    let umId = null;
    if (n.hl) {
      db.run('INSERT INTO UserMark (ColorIndex, LocationId, StyleIndex, UserMarkGuid, Version) VALUES (?,?,?,?,1)',
        [n.hl.color || 1, n.loc || 1, 0, 'um' + n.id]);
      umId = db.exec('SELECT last_insert_rowid()')[0].values[0][0];
      db.run('INSERT INTO BlockRange (BlockType, Identifier, StartToken, EndToken, UserMarkId) VALUES (?,?,?,?,?)',
        [n.hl.blockType || 2, n.hl.identifier || 1, n.hl.start || 0, n.hl.end || 5, umId]);
    }
    db.run('INSERT INTO Note (NoteId,Guid,UserMarkId,Title,Content,LastModified,LocationId) VALUES (?,?,?,?,?,?,?)',
      [n.id, 'g' + n.id, umId, n.title, n.content, n.date || '2024-01-01 00:00:00', n.loc || 1]);
  });
  const bytes = db.export(); db.close();
  const zip = new JSZip(); zip.file('userData.db', bytes); zip.file('manifest.json', JSON.stringify({ version: 1, name: 'Test' }));
  return zip.generateAsync({ type: 'nodebuffer' });
}

function bootShare() {
  const html = fs.readFileSync(SHARE_PATH, 'utf8');
  const m = html.match(/<script>\s*\(function\s*\(\)[\s\S]*?<\/script>/);
  if (!m) { fail('share.html inline script not found'); process.exit(1); }
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>
<header id="sh-header"><button id="sh-back" class="sh-back">← JW Sync</button><span id="sh-htitle" class="sh-htitle">Share Notes</span><button id="sh-new" class="sh-new" style="display:none">Start over</button></header>
<main id="sh-main"></main>${m[0]}</body></html>`;
  const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs(SQL_OPTS);
  if (!win.URL.createObjectURL) win.URL.createObjectURL = () => 'blob:mock';
  win.indexedDB = { open: function () { const req = {}; setTimeout(() => { if (req.onerror) req.onerror({ target: req }); }, 0); return req; } };
  return dom;
}

(async function run() {
  const SQL = await initSqlJs(SQL_OPTS);

  section('Home — two mode cards');
  {
    const dom = bootShare(); const doc = dom.window.document;
    await wait(60);
    if (doc.getElementById('sh-go-send') && doc.getElementById('sh-go-recv')) ok('Send + Receive cards render');
    else fail('mode cards missing');
    dom.window.close();
  }

  section('Send — pick a backup, select notes, create file');
  {
    const dom = bootShare(); const win = dom.window, doc = win.document;
    await wait(40);
    const buf = await buildBackup(SQL, [
      { id: 1, title: 'Faith', content: 'Hope and trust', hl: { color: 2, blockType: 2, identifier: 5, start: 0, end: 4 } },
      { id: 2, title: 'Love', content: 'Patience and kindness' },
      { id: 3, title: 'Peace', content: 'Calm in the storm' },
    ]);
    win.__shLoadBackup({ name: 'test.jwlibrary', arrayBuffer: async () => buf });
    async function until(p, l, ms = 8000) { const s = Date.now(); while (Date.now() - s < ms) { try { if (p()) return true; } catch (_) {} await wait(40); } fail('timeout: ' + l); return false; }
    if (await until(() => doc.querySelectorAll('.sh-list .sh-item').length === 3, 'note list'))
      ok('backup loaded — 3 notes listed for selection');
    doc.getElementById('sh-all').click();
    await until(() => /3/.test(doc.getElementById('sh-count').textContent), 'all selected');
    ok('select-all ticks every note');
    const createBtn = doc.getElementById('sh-create');
    if (createBtn && !createBtn.disabled) ok('Create file enabled with a selection'); else fail('create button disabled');
    createBtn.click();
    await until(() => doc.getElementById('sh-json'), 'share result');
    const env = JSON.parse(doc.getElementById('sh-json').value);
    if (env.app === 'jwsync' && env.notes.length === 3) ok('valid envelope built with 3 notes');
    else fail('envelope wrong: ' + JSON.stringify(env).slice(0, 80));
    if (env.notes.some(n => n.title === 'Faith' && /Hope/.test(n.content))) ok('note content carried into envelope');
    else fail('note content missing from envelope');
    if (env.v === 2) ok('envelope bumped to v2');
    else fail('envelope version not 2: ' + env.v);
    const faith = env.notes.find(n => n.title === 'Faith');
    if (faith && faith.loc && Array.isArray(faith.ranges) && faith.ranges.length === 1 && faith.color === 2)
      ok('highlighted note carries loc + ranges + color in envelope');
    else fail('highlight payload missing from envelope: ' + JSON.stringify(faith && { loc: faith.loc, ranges: faith.ranges, color: faith.color }));
    if (faith && faith.ranges[0].startToken === 0 && faith.ranges[0].endToken === 4 && faith.ranges[0].identifier === 5)
      ok('BlockRange span carried (tokens 0-4, identifier 5)');
    else fail('BlockRange span wrong: ' + JSON.stringify(faith && faith.ranges[0]));
    const plain = env.notes.find(n => n.title === 'Love');
    if (plain && !plain.loc && !plain.ranges) ok('non-highlighted note has no highlight payload');
    else fail('plain note unexpectedly carries highlight payload');
    dom.window.close();
  }

  section('Receive — preview shared notes');
  {
    const dom = bootShare(); const win = dom.window, doc = win.document;
    await wait(40);
    win.__shRenderReceive();
    await wait(40);
    const envelope = JSON.stringify({ v: 2, app: 'jwsync', kind: 'notes', notes: [
      { title: 'Shared one', content: 'first shared note', tags: ['Study'], pub: 'Genesis 1', color: 3,
        loc: { BookNumber: 1, ChapterNumber: 1, IssueTagNumber: 0, KeySymbol: 'nwt', MepsLanguage: 0, Type: 0 },
        ranges: [{ blockType: 2, identifier: 5, startToken: 0, endToken: 4 }] },
      { title: 'Shared two', content: 'second shared note', tags: [], pub: 'Watchtower' },
    ] });
    doc.getElementById('sh-paste').value = envelope;
    doc.getElementById('sh-prev').click();
    async function until(p, l, ms = 4000) { const s = Date.now(); while (Date.now() - s < ms) { try { if (p()) return true; } catch (_) {} await wait(40); } fail('timeout: ' + l); return false; }
    await until(() => doc.querySelectorAll('#sh-prevlist .sh-nrow').length === 2, 'preview list');
    ok('shared notes preview (2 items, scrollable list)');
    if (doc.body.classList.contains('sh-wide')) ok('preview widens the window');
    else fail('preview did not widen the window');
    const chips = [...doc.querySelectorAll('.sh-chip')].map(c => c.textContent);
    if (chips.some(c => /All \(2\)/.test(c)) && chips.some(c => /Highlights \(1\)/.test(c)) && chips.some(c => /Notes \(1\)/.test(c)))
      ok('category chips show counts (All / Highlights / Notes)');
    else fail('category chips wrong: ' + chips.join(' | '));
    if (chips.some(c => /Study \(1\)/.test(c))) ok('tag chip rendered');
    else fail('tag chip missing: ' + chips.join(' | '));
    if (doc.querySelectorAll('#sh-prevlist .sh-dot:not(.sh-dot-none)').length === 1) ok('highlighted note shows a colour dot');
    else fail('colour dot count wrong');
    // filter to Highlights only
    [...doc.querySelectorAll('.sh-chip')].find(c => /Highlights/.test(c.textContent)).click();
    await wait(20);
    if (doc.querySelectorAll('#sh-prevlist .sh-nrow').length === 1) ok('filtering by Highlights narrows the list');
    else fail('highlight filter did not narrow: ' + doc.querySelectorAll('#sh-prevlist .sh-nrow').length);
    if (doc.getElementById('sh-addto')) ok('"Add to my backup" action offered');
    else fail('add-to-backup action missing');
    dom.window.close();
  }

  section('Adopt — shared notes added into a backup');
  {
    const dom = bootShare(); const win = dom.window, doc = win.document;
    await wait(40);
    win.__shRenderReceive(); await wait(20);
    const backupBuf = await buildBackup(SQL, [{ id: 1, title: 'Existing', content: 'already here' }]);
    const fileLike = { name: 'mybackup.jwlibrary', arrayBuffer: async () => backupBuf };
    const sharedNotes = [
      { title: 'Gift', content: 'a shared note', tags: ['FromFriend'] },
      { title: 'Grace', content: 'another shared note', tags: [] },
    ];
    // capture the generated updated-backup blob
    let blob = null;
    win.URL.createObjectURL = (b) => { blob = b; return 'blob:upd'; };
    win.URL.revokeObjectURL = () => {};
    win.__shAdopt(fileLike, sharedNotes, 'Gift2026');
    async function until(p, l, ms = 9000) { const s = Date.now(); while (Date.now() - s < ms) { try { if (p()) return true; } catch (_) {} await wait(40); } fail('timeout: ' + l); return false; }
    await until(() => doc.querySelector('.sh-ok'), 'adopt done screen');
    if (/2/.test(doc.querySelector('.sh-ok').textContent)) ok('adopt confirms 2 notes added');
    else fail('adopt count wrong: ' + doc.querySelector('.sh-ok').textContent);
    // the done screen lists the imported notes
    const impRows = doc.querySelectorAll('.sh-panel .sh-prevlist .sh-nrow');
    if (impRows.length === 2) ok('done screen lists the 2 imported notes');
    else fail('imported-notes summary wrong: ' + impRows.length);
    if ([...impRows].some(r => /Gift/.test(r.textContent)) && [...impRows].some(r => /Grace/.test(r.textContent)))
      ok('imported summary shows the note titles');
    else fail('imported summary missing titles');
    const dlu = doc.getElementById('sh-dlu');
    if (dlu) { dlu.click(); await until(() => blob !== null, 'updated backup blob'); }
    else fail('download button missing');
    if (blob) {
      const zip = await JSZip.loadAsync(Buffer.from(await blob.arrayBuffer()));
      const key = Object.keys(zip.files).find(n => /userdata\.db$/i.test(n));
      const edb = new SQL.Database(await zip.files[key].async('uint8array'));
      const cnt = edb.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
      if (cnt === 3) ok('updated backup has original + 2 adopted notes (1→3)');
      else fail('expected 3 notes in updated backup, got ' + cnt);
      const tagged = edb.exec("SELECT COUNT(*) FROM Tag WHERE Name='Gift2026'")[0].values[0][0];
      if (tagged === 1) ok('adopted notes tagged with the custom import tag');
      else fail('custom import tag not created: ' + tagged);
      // both notes must be linked to the import tag — distinct Positions (no UNIQUE(TagId,Position) collision)
      const links = edb.exec("SELECT COUNT(*) FROM TagMap tm JOIN Tag t ON tm.TagId=t.TagId WHERE t.Name='Gift2026'")[0].values[0][0];
      if (links === 2) ok('both adopted notes linked to the import tag (Position collision avoided)');
      else fail('expected 2 import-tag links, got ' + links);
      const orig = edb.exec("SELECT Content FROM Note WHERE Title='Existing'");
      if (orig[0] && orig[0].values[0][0] === 'already here') ok('original note left untouched (non-destructive)');
      else fail('original note was altered');
      edb.close();
    }
    dom.window.close();
  }

  section('Receive — conflict screen lists the clashing notes');
  {
    const dom = bootShare(); const win = dom.window, doc = win.document;
    await wait(40);
    win.__shRenderReceive(); await wait(20);
    // backup already has a highlight on Genesis 1, tokens 0-4
    const backupBuf = await buildBackup(SQL, [
      { id: 1, title: 'My note', content: 'mine', loc: 1, hl: { color: 1, blockType: 2, identifier: 5, start: 0, end: 4 } },
    ]);
    const fileLike = { name: 'mybackup.jwlibrary', arrayBuffer: async () => backupBuf };
    const incoming = [
      { title: 'Clashes', content: 'overlapping', tags: ['Study'], pub: 'Genesis 1', color: 3,
        loc: { BookNumber: 1, ChapterNumber: 1, DocumentId: null, Track: null, IssueTagNumber: 0, KeySymbol: 'nwt', MepsLanguage: 0, Type: 0 },
        ranges: [{ blockType: 2, identifier: 5, startToken: 0, endToken: 4 }] },
      { title: 'NoClash', content: 'elsewhere', tags: [], pub: 'Watchtower' },
    ];
    let blob = null;
    win.URL.createObjectURL = (b) => { blob = b; return 'blob:upd'; };
    win.URL.revokeObjectURL = () => {};
    win.__shAdopt(fileLike, incoming, 'Shared');
    async function until(p, l, ms = 9000) { const s = Date.now(); while (Date.now() - s < ms) { try { if (p()) return true; } catch (_) {} await wait(40); } fail('timeout: ' + l); return false; }
    await until(() => doc.getElementById('sh-ov-note'), 'conflict choice screen');
    const confRows = doc.querySelectorAll('.sh-conflict .sh-nrow');
    if (confRows.length === 1 && /Clashes/.test(confRows[0].textContent))
      ok('conflict screen lists exactly the clashing note');
    else fail('conflict list wrong: ' + confRows.length + ' [' + [...confRows].map(r => r.textContent.slice(0, 12)).join(',') + ']');
    if (doc.getElementById('sh-ov-layer') && doc.getElementById('sh-ov-note')) ok('both conflict options offered');
    else fail('conflict options missing');
    doc.getElementById('sh-ov-note').click();
    await until(() => doc.querySelector('.sh-ok'), 'done after note-only');
    if (/2/.test(doc.querySelector('.sh-ok').textContent)) ok('both notes imported after choosing note-only');
    else fail('post-conflict count wrong: ' + doc.querySelector('.sh-ok').textContent);
    dom.window.close();
  }

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll Share-page checks passed.');
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

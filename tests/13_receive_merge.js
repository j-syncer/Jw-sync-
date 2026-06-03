// Receive shared notes in merge (v2.34.0).
// Loads the self-contained Receive module in JSDOM, builds a real .jwlibrary,
// and verifies envelope parsing + adopting a friend's notes into the buffer.
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

let failures = 0;
const ok = (m) => console.log('  ✓', m);
const fail = (m) => { console.log('  ✗', m); failures++; };
const section = (m) => console.log('\n== ' + m + ' ==');
const wait = (ms) => new Promise(r => setTimeout(r, ms));
const locate = { locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) };

(async function run() {
  section('Build a minimal .jwlibrary');
  const SQL = await initSqlJs(locate);
  const db = new SQL.Database();
  db.run(`
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INT, ChapterNumber INT, KeySymbol TEXT, Title TEXT);
    CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INT, LocationId INT, UserMarkGuid TEXT, Version INT);
    CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INT, LocationId INT, Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INT, BlockIdentifier INT);
    CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INT, Name TEXT);
    CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, NoteId INT, LocationId INT, PlaylistItemId INT, TagId INT, Position INT);
    INSERT INTO Note (Guid,Title,Content,LastModified,Created,BlockType,BlockIdentifier) VALUES ('g1','Existing','<p>hi</p>','2024-01-01 00:00:00','2024-01-01 00:00:00',0,0);
  `);
  const dbBytes = db.export(); db.close();
  const zip = new JSZip(); zip.file('userData.db', Buffer.from(dbBytes));
  const jwlib = await zip.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });
  ok(`built .jwlibrary (${jwlib.byteLength} bytes, 1 existing note)`);

  section('Load the Receive module in JSDOM');
  const html = fs.readFileSync(path.join(__dirname, '../beta/index.html'), 'utf8');
  const m = html.match(/<!-- ── Receive shared notes in merge \(v[\d.]+\)[\s\S]*?<!-- ── End Receive shared notes in merge ─[─]*\s*-->/);
  if (!m) { fail('Receive module block not found'); console.log('\nFAIL'); process.exit(1); }
  const dom = new JSDOM(`<!DOCTYPE html><html><body>${m[0]}</body></html>`, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs(locate);
  await wait(20);
  if (typeof win.__jwParseShareEnvelope === 'function' && typeof win.__jwAdoptSharedIntoBuffer === 'function')
    ok('Receive API exposed (__jwParseShareEnvelope, __jwAdoptSharedIntoBuffer)');
  else { fail('Receive API missing'); console.log('\nFAIL'); process.exit(1); }

  section('Envelope parsing + sanitization');
  const env = JSON.stringify({ v:1, app:'jwsync', kind:'notes', notes:[
    { title:'From Ann', content:'<p>Good <b>point</b></p><script>alert(1)</script>', color:2, tags:['Sermon','Shared'] },
    { title:'Second', content:'<div onclick="x()">plain</div>', tags:[] },
  ]});
  const notes = win.__jwParseShareEnvelope(env);
  if (notes && notes.length === 2) ok('parsed 2 notes from a valid envelope');
  else fail('expected 2 parsed notes, got ' + (notes && notes.length));
  if (notes && !/script|onclick/i.test(notes[0].content + notes[1].content)) ok('dangerous markup stripped on parse');
  else fail('sanitization did not strip script/onclick');
  if (win.__jwParseShareEnvelope('not json') === null && win.__jwParseShareEnvelope('{"app":"other","notes":[]}') === null)
    ok('rejects invalid / foreign envelopes');
  else fail('invalid envelope not rejected');

  section('Adopt notes into the .jwlibrary buffer');
  const res = await win.__jwAdoptSharedIntoBuffer(jwlib, notes, 'Shared');
  if (res && res.added === 2) ok('adopt reported 2 notes added');
  else fail('adopt added count wrong: ' + (res && res.added));
  // reopen the augmented buffer and verify
  const z2 = await JSZip.loadAsync(res.buffer);
  const key = Object.keys(z2.files).find(k => /userdata\.db$/i.test(k));
  const bytes = await z2.file(key).async('uint8array');
  const SQL2 = await initSqlJs(locate);
  const db2 = new SQL2.Database(bytes);
  const cnt = (sql) => { const r = db2.exec(sql); return (r[0] && r[0].values[0]) ? r[0].values[0][0] : 0; };
  if (cnt('SELECT COUNT(*) FROM Note') === 3) ok('Note count is 3 (1 existing + 2 adopted)');
  else fail('Note count wrong: ' + cnt('SELECT COUNT(*) FROM Note'));
  if (cnt("SELECT COUNT(*) FROM Note WHERE Title='From Ann'") === 1) ok('adopted note titles preserved');
  else fail('adopted note title missing');
  if (cnt("SELECT COUNT(*) FROM Tag WHERE Name='Shared' COLLATE NOCASE") === 1) ok('"Shared" provenance tag created once');
  else fail('Shared tag not created exactly once');
  if (cnt("SELECT COUNT(*) FROM Tag WHERE Name='Sermon'") === 1) ok('custom note tag created');
  else fail('custom tag "Sermon" missing');
  // the first adopted note should map to both Shared + Sermon
  const annTags = cnt("SELECT COUNT(*) FROM TagMap tm JOIN Note n ON tm.NoteId=n.NoteId WHERE n.Title='From Ann'");
  if (annTags === 2) ok('TagMap links adopted note to its 2 tags (Shared + Sermon)');
  else fail('TagMap links wrong for adopted note: ' + annTags);
  db2.close();

  section('Static wiring guards');
  if (html.includes('data-jwc-addshared') && html.includes('window.__jwReceivePickAndAdopt'))
    ok('end-of-merge "add shared notes" button wired in celebration');
  else fail('celebration add-shared button/wiring missing');
  if (html.includes('window.__jwReceiveOnCelebration(ov)')) ok('pre-merge auto-adopt hook present in celebration');
  else fail('auto-adopt hook missing');
  if (html.includes("id=\"jwr-panel\"") || html.includes('jwr-panel')) ok('pre-merge attach panel present');
  else fail('pre-merge panel missing');

  section('Phase 2 — non-destructive highlight import (overlapping verse)');
  // Build a .jwlibrary that already has a highlight + note on Genesis 1, tokens 0-4
  async function buildLibWithHighlight() {
    const sql = await initSqlJs(locate);
    const d = new sql.Database();
    d.run(`
      CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INT, ChapterNumber INT, DocumentId INT, Track INT, IssueTagNumber INT DEFAULT 0, KeySymbol TEXT, MepsLanguage INT DEFAULT 0, Type INT DEFAULT 0, Title TEXT);
      CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INT, LocationId INT, StyleIndex INT DEFAULT 0, UserMarkGuid TEXT, Version INT DEFAULT 1);
      CREATE TABLE BlockRange (BlockRangeId INTEGER PRIMARY KEY, BlockType INT, Identifier INT, StartToken INT, EndToken INT, UserMarkId INT);
      CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INT, LocationId INT, Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INT, BlockIdentifier INT);
      CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INT, Name TEXT);
      CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, NoteId INT, LocationId INT, TagId INT, Position INT);
      CREATE UNIQUE INDEX IX_TagMap_TagId_Position ON TagMap (TagId, Position);
      INSERT INTO Location (LocationId,BookNumber,ChapterNumber,DocumentId,Track,IssueTagNumber,KeySymbol,MepsLanguage,Type,Title) VALUES (1,1,1,0,0,0,'nwt',0,0,'Genesis');
      INSERT INTO UserMark (UserMarkId,ColorIndex,LocationId,StyleIndex,UserMarkGuid,Version) VALUES (1,1,1,0,'mine-mark',1);
      INSERT INTO BlockRange (BlockType,Identifier,StartToken,EndToken,UserMarkId) VALUES (2,5,0,4,1);
      INSERT INTO Note (Guid,UserMarkId,LocationId,Title,Content,LastModified,Created,BlockType,BlockIdentifier) VALUES ('mine-note',1,1,'My note','<p>mine</p>','2024-01-01 00:00:00','2024-01-01 00:00:00',2,5);
    `);
    const bytes = d.export(); d.close();
    const z = new JSZip(); z.file('userData.db', Buffer.from(bytes));
    return z.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });
  }
  // An incoming friend's highlight+note on the SAME verse span, different colour (3)
  const friendLoc = { BookNumber: 1, ChapterNumber: 1, DocumentId: 0, Track: 0, IssueTagNumber: 0, KeySymbol: 'nwt', MepsLanguage: 0, Type: 0, Title: 'Genesis' };
  const friendNote = () => ([{ title: 'Friend note', content: '<p>from a friend</p>', tags: ['Study'],
    loc: friendLoc, color: 3, style: 0, ranges: [{ blockType: 2, identifier: 5, startToken: 0, endToken: 4 }] }]);

  async function openDb(buf) {
    const z = await JSZip.loadAsync(buf);
    const k = Object.keys(z.files).find(x => /userdata\.db$/i.test(x));
    const SQLx = await initSqlJs(locate);
    return new SQLx.Database(await z.file(k).async('uint8array'));
  }

  // overlap detected → user chooses "Add as a separate layer"
  {
    const lib = await buildLibWithHighlight();
    let asked = 0;
    const res = await win.__jwAdoptSharedIntoBuffer(lib, friendNote(), { tagLabel: 'FromAnn', onOverlap: (n) => { asked = n; return 'layer'; } });
    if (asked === 1) ok('overlap detected and the user was asked (1 overlapping highlight)');
    else fail('overlap prompt not triggered: ' + asked);
    const db3 = await openDb(res.buffer);
    const c = (s) => { const r = db3.exec(s); return (r[0] && r[0].values[0]) ? r[0].values[0][0] : 0; };
    if (c('SELECT COUNT(*) FROM UserMark') === 2) ok('a second UserMark layer was added (1→2)');
    else fail('UserMark count after layer add: ' + c('SELECT COUNT(*) FROM UserMark'));
    if (c('SELECT ColorIndex FROM UserMark WHERE UserMarkGuid=\'mine-mark\'') === 1) ok("user's original highlight colour untouched (still 1)");
    else fail('original highlight colour changed');
    if (c('SELECT COUNT(*) FROM UserMark WHERE ColorIndex=3') === 1) ok("friend's highlight added in its own colour (3)");
    else fail('friend highlight colour missing');
    if (c('SELECT COUNT(*) FROM BlockRange') === 2) ok('a second BlockRange added for the new layer');
    else fail('BlockRange count wrong: ' + c('SELECT COUNT(*) FROM BlockRange'));
    if (c("SELECT Content FROM Note WHERE Guid='mine-note'") === '<p>mine</p>') ok("user's original note left intact");
    else fail('original note altered');
    if (c('SELECT COUNT(*) FROM Note') === 2) ok('friend note added alongside (1→2)');
    else fail('Note count wrong: ' + c('SELECT COUNT(*) FROM Note'));
    if (c("SELECT COUNT(*) FROM Tag WHERE Name='FromAnn'") === 1) ok('imported note carries the custom import tag');
    else fail('custom tag missing');
    db3.close();
  }

  // overlap detected → user chooses "Import note only"
  {
    const lib = await buildLibWithHighlight();
    const res = await win.__jwAdoptSharedIntoBuffer(lib, friendNote(), { tagLabel: 'FromAnn', onOverlap: () => 'note' });
    const db3 = await openDb(res.buffer);
    const c = (s) => { const r = db3.exec(s); return (r[0] && r[0].values[0]) ? r[0].values[0][0] : 0; };
    if (c('SELECT COUNT(*) FROM UserMark') === 1) ok('note-only: no competing highlight created (stays 1)');
    else fail('note-only added a UserMark: ' + c('SELECT COUNT(*) FROM UserMark'));
    if (c('SELECT COUNT(*) FROM Note') === 2) ok('note-only: friend note still added');
    else fail('note-only Note count wrong: ' + c('SELECT COUNT(*) FROM Note'));
    if (c("SELECT UserMarkId FROM Note WHERE Title='Friend note'") === 1) ok("note-only: friend note linked to user's existing highlight");
    else fail('note-only link wrong: ' + c("SELECT UserMarkId FROM Note WHERE Title='Friend note'"));
    db3.close();
  }

  // no overlap → highlight added without prompting
  {
    const lib = await buildLibWithHighlight();
    const farNote = [{ title: 'Far note', content: '<p>elsewhere</p>', tags: [],
      loc: { BookNumber: 1, ChapterNumber: 1, DocumentId: 0, Track: 0, IssueTagNumber: 0, KeySymbol: 'nwt', MepsLanguage: 0, Type: 0 },
      color: 4, style: 0, ranges: [{ blockType: 2, identifier: 9, startToken: 0, endToken: 3 }] }];
    let asked = 0;
    const res = await win.__jwAdoptSharedIntoBuffer(lib, farNote, { tagLabel: 'FromAnn', onOverlap: () => { asked = 1; return 'note'; } });
    if (asked === 0) ok('non-overlapping highlight added without asking');
    else fail('unexpected overlap prompt for non-overlapping verse');
    const db3 = await openDb(res.buffer);
    const c = (s) => { const r = db3.exec(s); return (r[0] && r[0].values[0]) ? r[0].values[0][0] : 0; };
    if (c('SELECT COUNT(*) FROM UserMark') === 2 && c('SELECT COUNT(*) FROM UserMark WHERE ColorIndex=4') === 1)
      ok('new highlight layer added on the new passage');
    else fail('non-overlap highlight not added correctly');
    db3.close();
  }

  // multiple notes sharing the import tag must all be added (regression: TagMap UNIQUE(TagId,Position))
  {
    const lib = await buildLibWithHighlight();
    const many = [
      { title: 'A', content: '<p>a</p>', tags: ['Study'] },
      { title: 'B', content: '<p>b</p>', tags: ['Study'] },
      { title: 'C', content: '<p>c</p>', tags: [] },
    ];
    const res = await win.__jwAdoptSharedIntoBuffer(lib, many, 'Shared');
    if (res.added === 3) ok('all 3 notes sharing the import tag were added (no Position collision)');
    else fail('expected 3 added, got ' + res.added + ' (TagMap Position collision?)');
    const db3 = await openDb(res.buffer);
    const c = (s) => { const r = db3.exec(s); return (r[0] && r[0].values[0]) ? r[0].values[0][0] : 0; };
    if (c("SELECT COUNT(*) FROM TagMap tm JOIN Tag t ON tm.TagId=t.TagId WHERE t.Name='Shared'") === 3)
      ok('import tag linked to all 3 notes at distinct Positions');
    else fail('import-tag links wrong: ' + c("SELECT COUNT(*) FROM TagMap tm JOIN Tag t ON tm.TagId=t.TagId WHERE t.Name='Shared'"));
    db3.close();
  }

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll receive-merge checks passed.');
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

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
  const m = html.match(/<!-- ── Receive shared notes in merge \(v2\.34\.0\)[\s\S]*?<!-- ── End Receive shared notes in merge ─[─]*\s*-->/);
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

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll receive-merge checks passed.');
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

// 24_backup_manifest.js — does what we hand back actually restore?
//
// Reported on the community page: files that had been through the Library
// Doctor, or edited in the Study Explorer, would not restore into JW Library.
// No error, no confirmation prompt — the app flickered and stayed where it was.
//
// A .jwlibrary carries manifest.json describing the database beside it,
// including userDataBackup.hash, the SHA-256 of userData.db. JW Library checks
// it and silently refuses a file where it does not match. The Explorer was
// shipping a zip with no manifest at all; the Doctor and the receive path kept
// the incoming manifest with its hash still pointing at the old database.
//
// Every one of those files opened perfectly well on our own site — that is the
// whole difficulty. Only the app rejects them, and it does so without saying
// anything. So this suite reads the bytes: for every path that writes a backup,
// it recomputes the SHA-256 of the userData.db in the zip and compares it to
// what the manifest claims.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { JSDOM } = require('jsdom');
const initSqlJs = require('sql.js');
const JSZip = require('jszip');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m) => { failures++; console.log('  ✗ ' + m); };
const section = (t) => console.log('\n== ' + t + ' ==');

const HELPER_SRC = fs.readFileSync(path.join(REPO, 'js/jwlibrary-manifest.js'), 'utf8');

// JSDOM's Blob has no arrayBuffer() in this version, and the export now builds
// its Blob inside the page (application/octet-stream, so iOS saves it as
// .jwlibrary). FileReader is the reader both realms agree on.
function blobBytes(win, blob) {
  if (typeof blob.arrayBuffer === 'function') return blob.arrayBuffer().then(b => Buffer.from(b));
  return new Promise((res, rej) => {
    const r = new win.FileReader();
    r.onload = () => res(Buffer.from(r.result));
    r.onerror = rej;
    r.readAsArrayBuffer(blob);
  });
}

function loadHelper(withSubtle) {
  const scope = withSubtle ? { crypto: require('crypto').webcrypto } : {};
  new Function('self', HELPER_SRC)(scope);
  return scope.__jwFinalizeBackup;
}

// ── 1. the hash itself ──────────────────────────────────────────────────────
(async () => {
  section('SHA-256');
  for (const [label, withSubtle] of [['crypto.subtle', true], ['the pure-JS fallback', false]]) {
    const helper = loadHelper(withSubtle);
    let bad = 0;
    // The sizes that break a hand-written implementation are the padding
    // boundaries: 55/56 (length field spills into a new block) and 63/64/65.
    const sizes = [0, 1, 55, 56, 57, 63, 64, 65, 119, 120, 127, 128, 1000, 65535];
    for (let i = 0; i < 40; i++) sizes.push(Math.floor(Math.random() * 200000));
    for (const n of sizes) {
      const b = crypto.randomBytes(n);
      const mine = await helper.sha256Hex(new Uint8Array(b));
      if (mine !== crypto.createHash('sha256').update(b).digest('hex')) bad++;
    }
    if (!bad) ok(`${label}: ${sizes.length} inputs match Node's sha256`);
    else fail(`${label}: ${bad} of ${sizes.length} inputs hashed wrong`);
  }

  // ── 2. finalizeBackup on a zip ────────────────────────────────────────────
  section('finalizeBackup()');
  const helper = loadHelper(true);
  const dbBytes = new Uint8Array(crypto.randomBytes(4096));

  {
    // A manifest that is already there keeps everything we do not understand.
    const zip = new JSZip();
    zip.file('userData.db', crypto.randomBytes(100));
    zip.file('manifest.json', JSON.stringify({
      name: 'UserdataBackup_2026-08-01', creationDate: '2026-08-01', version: 1,
      type: 0, userDataBackup: {
        lastModifiedDate: '2026-08-01T00:00:00Z', deviceName: 'iPhone',
        databaseName: 'userData.db', hash: 'stale'.repeat(12), schemaVersion: 16,
        someFieldWeHaveNeverHeardOf: 'keep me',
      },
    }));
    await helper(zip, 'userData.db', dbBytes, { nameSuffix: ' (Edited)' });
    const m = JSON.parse(await zip.file('manifest.json').async('string'));
    const expect = crypto.createHash('sha256').update(Buffer.from(dbBytes)).digest('hex');
    if (m.userDataBackup.hash === expect) ok('hash recomputed from the new database');
    else fail(`hash not updated: ${m.userDataBackup.hash}`);
    if (m.userDataBackup.lastModifiedDate !== '2026-08-01T00:00:00Z') ok('lastModifiedDate refreshed');
    else fail('lastModifiedDate left stale');
    if (m.userDataBackup.schemaVersion === 16) ok('schemaVersion preserved, not rewritten');
    else fail('schemaVersion changed to ' + m.userDataBackup.schemaVersion);
    if (m.userDataBackup.someFieldWeHaveNeverHeardOf === 'keep me') ok('unknown manifest fields left alone');
    else fail('an unrecognised manifest field was dropped');
    if (m.userDataBackup.deviceName === 'iPhone') ok('deviceName preserved');
    else fail('deviceName overwritten: ' + m.userDataBackup.deviceName);
    if (m.name === 'UserdataBackup_2026-08-01 (Edited)') ok('name suffixed once');
    else fail('name wrong: ' + m.name);
    // Running twice must not stack the suffix.
    await helper(zip, 'userData.db', dbBytes, { nameSuffix: ' (Edited)' });
    const m2 = JSON.parse(await zip.file('manifest.json').async('string'));
    if (m2.name === 'UserdataBackup_2026-08-01 (Edited)') ok('re-running does not stack the suffix');
    else fail('suffix stacked: ' + m2.name);
  }

  {
    // No manifest at all — what the Explorer used to ship.
    const zip = new JSZip();
    await helper(zip, 'userData.db', dbBytes, {});
    const mf = zip.file('manifest.json');
    if (mf) ok('a manifest is written when the archive has none');
    else { fail('no manifest written'); }
    if (mf) {
      const m = JSON.parse(await mf.async('string'));
      const expect = crypto.createHash('sha256').update(Buffer.from(dbBytes)).digest('hex');
      if (m.userDataBackup && m.userDataBackup.hash === expect) ok('synthesised manifest carries the right hash');
      else fail('synthesised manifest hash wrong');
      // Guessing this is another silently-refused file; absent is honest.
      if (!('schemaVersion' in m.userDataBackup)) ok('schemaVersion is not invented');
      else fail('schemaVersion invented as ' + m.userDataBackup.schemaVersion);
    }
  }

  {
    const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
    const db = new SQL.Database();
    db.run('CREATE TABLE LastModified (LastModified TEXT); INSERT INTO LastModified VALUES ("2020-01-01T00:00:00Z");');
    const touched = helper.touchLastModified(db, '2026-08-12T10:00:00Z');
    const v = db.exec('SELECT LastModified FROM LastModified')[0].values;
    if (touched && v.length === 1 && v[0][0] === '2026-08-12T10:00:00Z') ok('LastModified table updated, still one row');
    else fail('LastModified not updated: ' + JSON.stringify(v));
    const db2 = new SQL.Database();
    db2.run('CREATE TABLE Note (NoteId INTEGER)');
    if (helper.touchLastModified(db2) === false) ok('a backup with no LastModified table is left alone');
    else fail('touchLastModified invented a table');
    db.close(); db2.close();
  }

  // ── 3. every writer goes through it ───────────────────────────────────────
  section('Every path that writes a .jwlibrary uses it');
  // Derived, not listed. This began as four filenames written out by hand; the
  // Conflict Reviewer was missing and shipped a stale hash on every corrected
  // file, and adding it as a fifth row left js/app.js — whose Extract & Share
  // path rewrote manifest.json's name and creationDate but never its hash —
  // just as invisible. A roster of writers only ever protects the writers
  // somebody remembered to add.
  //
  // So: anything under js/ that zips up a userData.db has to finalize it.
  const EXEMPT = {
    // Builds the two synthetic backups for demo mode. They are handed straight
    // back to the site's own loader, never offered for download and never
    // restored into JW Library; the merged result the user *can* download is
    // written by the worker, which does finalize.
    'js/enhancements.js': 'demo fixtures, never restored',
  };
  {
    const jsDir = path.join(REPO, 'js');
    const writers = fs.readdirSync(jsDir).filter((f) => f.endsWith('.js')).filter((f) => {
      const src = fs.readFileSync(path.join(jsDir, f), 'utf8');
      // Match on the word, not on "userData.db" exactly: conflict-review.js
      // names the database only inside the regex /userdata\.db$/i, whose source
      // text carries a backslash before the dot — so a first draft looking for
      // a literal dot skipped one of the two writers that were actually broken.
      return src.includes('generateAsync') && /userdata/i.test(src);
    }).map((f) => 'js/' + f).sort();

    if (writers.length) ok(`found ${writers.length} file(s) that zip a userData.db`);
    else fail('found no .jwlibrary writers at all — this check has stopped looking');

    for (const rel of writers) {
      const src = fs.readFileSync(path.join(REPO, rel), 'utf8');
      if (src.includes('__jwFinalizeBackup')) ok(`${rel} finalizes its output`);
      else if (EXEMPT[rel]) ok(`${rel} exempt — ${EXEMPT[rel]}`);
      else fail(`${rel} writes a backup without refreshing the manifest hash`,
                'JW Library refuses it silently; add __jwFinalizeBackup or an EXEMPT reason');
    }
  }
  const worker = fs.readFileSync(path.join(REPO, 'js/merge-worker.js'), 'utf8');
  if (/importScripts\('jwlibrary-manifest\.js'\)/.test(worker)) ok('the worker imports the helper');
  else fail('the worker references the helper but never imports it');
  for (const rel of ['index.html', 'beta/index.html']) {
    const html = fs.readFileSync(path.join(REPO, rel), 'utf8');
    if (html.includes('js/jwlibrary-manifest.js')) ok(`${rel} loads the helper`);
    else fail(`${rel} does not load js/jwlibrary-manifest.js`);
  }

  // ── 4. the reported bug, end to end ───────────────────────────────────────
  section('Study Explorer: edit a backup and export it');
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  const db = new SQL.Database();
  db.run(`
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
      DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER, KeySymbol TEXT, MepsLanguage INTEGER,
      Type INTEGER, Title TEXT);
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
    CREATE TABLE LastModified (LastModified TEXT);
    INSERT INTO LastModified VALUES ('2020-01-01T00:00:00Z');
    INSERT INTO Location (LocationId, BookNumber, ChapterNumber, IssueTagNumber, KeySymbol, MepsLanguage, Type)
      VALUES (1, 43, 3, 0, 'nwtsty', 0, 0);
    INSERT INTO Note (NoteId, Guid, LocationId, Title, Content, LastModified, Created, BlockType, BlockIdentifier)
      VALUES (1, 'g1', 1, 'A note', '<p>Text</p>', '2024-01-01 00:00:00', '2024-01-01 00:00:00', 2, 16);
  `);
  const dbOut = db.export();
  db.close();

  // A realistic incoming backup: manifest, database, and a media file that must
  // survive the round trip.
  const inZip = new JSZip();
  inZip.file('userData.db', dbOut);
  inZip.file('manifest.json', JSON.stringify({
    name: 'UserdataBackup_2026-08-01_iPhone', creationDate: '2026-08-01', version: 1, type: 0,
    userDataBackup: {
      lastModifiedDate: '2026-08-01T00:00:00Z', deviceName: "purlo's iPhone",
      databaseName: 'userData.db', schemaVersion: 16,
      hash: crypto.createHash('sha256').update(Buffer.from(dbOut)).digest('hex'),
    },
  }, null, 2));
  inZip.file('media/thumb.jpg', crypto.randomBytes(64));
  const inBuf = await inZip.generateAsync({ type: 'arraybuffer' });

  const browseBlock = require('./helpers/browse-source').browseBlock(REPO + '/beta/index.html');
  const dom = new JSDOM(`<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${browseBlock}</body></html>`,
    { url: 'https://jwsync.org/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  win.matchMedia = (q) => ({ matches: false, media: q, addListener() {}, removeListener() {} });
  win.localStorage.setItem('jwsync_lang', 'en');
  win.alert = () => {};
  // The page loads this alongside the module; give the JSDOM window the same.
  new Function('self', HELPER_SRC)(win);
  win.__bootBrowse();
  win.__openJwBrowse(inBuf);

  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const waitFor = async (p, label, ms = 10000) => {
    const t0 = Date.now();
    while (Date.now() - t0 < ms) { try { if (p()) return true; } catch (_) {} await sleep(50); }
    fail('timeout waiting for: ' + label);
    return false;
  };
  await waitFor(() => win.document.querySelector('.jb-list .jb-note'), 'the note to render');

  // Make an edit, the way the reporter did, so the export button turns on.
  const importFile = new win.File(
    ['---\ntitle: Imported note\nbook: John\nchapter: 3\nverse: 16\n---\n\nFrom Markdown.\n'], 'n.md');
  const notes = await win.__jwMdImport.readFiles([importFile]);
  win.__jwMdImport.importNotes(notes);

  let blob = null;
  win.URL.createObjectURL = (b) => { blob = b; return 'blob:x'; };
  win.URL.revokeObjectURL = () => {};
  win.document.querySelector('.jb-export-btn').click();
  await waitFor(() => blob !== null, 'the exported file');

  if (blob && blob.type === 'application/octet-stream') ok('exported as application/octet-stream');
  else fail('wrong blob type: ' + (blob && blob.type));

  const outZip = await JSZip.loadAsync(await blobBytes(win, blob));
  const names = Object.keys(outZip.files);
  if (names.includes('manifest.json')) ok('the exported backup has a manifest.json');
  else fail('exported backup has NO manifest.json — JW Library will refuse it silently');
  if (names.includes('media/thumb.jpg')) ok('other files in the archive survived');
  else fail('media file dropped from the export: ' + names.join(', '));

  const outDbBytes = await outZip.file('userData.db').async('nodebuffer');
  const outManifest = JSON.parse(await outZip.file('manifest.json').async('string'));
  const real = crypto.createHash('sha256').update(outDbBytes).digest('hex');
  if (outManifest.userDataBackup.hash === real) ok('manifest hash matches the exported database');
  else fail(`manifest hash does not match the database it ships with:\n      manifest ${outManifest.userDataBackup.hash}\n      actual   ${real}`);
  if (outManifest.userDataBackup.deviceName === "purlo's iPhone") ok('the original manifest was carried over, not replaced');
  else fail('manifest replaced rather than updated');
  if (outManifest.userDataBackup.schemaVersion === 16) ok('schemaVersion carried over from the original');
  else fail('schemaVersion lost: ' + outManifest.userDataBackup.schemaVersion);

  const outDb = new SQL.Database(new Uint8Array(outDbBytes));
  const lm = outDb.exec('SELECT LastModified FROM LastModified')[0].values;
  if (lm.length === 1 && lm[0][0] !== '2020-01-01T00:00:00Z') ok('LastModified table stamped with the edit');
  else fail('LastModified not updated: ' + JSON.stringify(lm));
  const count = outDb.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
  if (count === 2) ok('the edit itself is in the exported database');
  else fail('expected 2 notes in the export, got ' + count);
  outDb.close();

  console.log(failures ? `\n${failures} failure(s)` : '\nAll backup-manifest checks passed');
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });

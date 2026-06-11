/**
 * 14_backup_doctor.js — Backup Doctor (v2.63.0)
 *
 * Synthesizes an in-memory .jwlibrary with KNOWN health problems, boots the
 * Doctor module in JSDOM, and verifies:
 *   - every check finds exactly the planted issues (and nothing else)
 *   - applyFixes removes them all without touching healthy records
 *   - a re-scan comes back perfectly clean (score 100)
 *   - the UI flow reaches the report state with the right counts
 */
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.resolve(__dirname, '..');
let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

(async function main() {
  section('Build a .jwlibrary with known health problems');
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  const db = new SQL.Database();
  db.run(`
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
      DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER, KeySymbol TEXT, MepsLanguage INTEGER, Type INTEGER, Title TEXT);
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
  `);

  // Locations: 1 + 2 used, 3 unused (leftover)
  db.run("INSERT INTO Location VALUES (1, 1, 1, NULL, NULL, 0, 'nwtsty', 0, 0, NULL)");
  db.run("INSERT INTO Location VALUES (2, 2, 1, NULL, NULL, 0, 'nwtsty', 0, 0, NULL)");
  db.run("INSERT INTO Location VALUES (3, 3, 1, NULL, NULL, 0, 'nwtsty', 0, 0, NULL)");

  // UserMarks: m1 healthy + m2 EXACT duplicate of m1 (no note attached);
  // m3 healthy distinct; m4 same loc/color as m1 but DIFFERENT range (kept).
  db.run("INSERT INTO UserMark VALUES (1, 1, 1, 0, 'g-m1', 1)");
  db.run("INSERT INTO UserMark VALUES (2, 1, 1, 0, 'g-m2', 1)"); // duplicate of m1
  db.run("INSERT INTO UserMark VALUES (3, 2, 2, 0, 'g-m3', 1)");
  db.run("INSERT INTO UserMark VALUES (4, 1, 1, 0, 'g-m4', 1)");
  db.run("INSERT INTO BlockRange VALUES (1, 0, 1, 0, 10, 1)");
  db.run("INSERT INTO BlockRange VALUES (2, 0, 1, 0, 10, 2)");  // identical range → dup
  db.run("INSERT INTO BlockRange VALUES (3, 0, 2, 5, 20, 3)");
  db.run("INSERT INTO BlockRange VALUES (4, 0, 1, 11, 30, 4)"); // different range → keep
  db.run("INSERT INTO BlockRange VALUES (5, 0, 9, 0, 5, 999)"); // ORPHAN fragment

  // Notes: n1 healthy, n2 EXACT duplicate of n1, n3 healthy, n4 EMPTY,
  // n5+n6 SAME text in the SAME chapter (loc 1) but on DIFFERENT verses
  // (BlockIdentifier 3 vs 7) — NOT duplicates, both must survive the clean.
  db.run("INSERT INTO Note VALUES (1, 'g-n1', 1, 1, 'Faith', 'Body about faith', '2026-01-01T00:00:00Z', '2026-01-01T00:00:00Z', NULL, NULL)");
  db.run("INSERT INTO Note VALUES (2, 'g-n2', NULL, 1, 'Faith', 'Body about faith', '2026-01-02T00:00:00Z', '2026-01-02T00:00:00Z', NULL, NULL)");
  db.run("INSERT INTO Note VALUES (3, 'g-n3', 3, 2, 'Hope', 'Body about hope', '2026-01-03T00:00:00Z', '2026-01-03T00:00:00Z', NULL, NULL)");
  db.run("INSERT INTO Note VALUES (4, 'g-n4', NULL, NULL, '', '  ', '2026-01-04T00:00:00Z', '2026-01-04T00:00:00Z', NULL, NULL)");
  db.run("INSERT INTO Note VALUES (5, 'g-n5', NULL, 1, 'Reminder', 'Same words, different verse', '2026-01-05T00:00:00Z', '2026-01-05T00:00:00Z', 2, 3)");
  db.run("INSERT INTO Note VALUES (6, 'g-n6', NULL, 1, 'Reminder', 'Same words, different verse', '2026-01-05T00:00:00Z', '2026-01-05T00:00:00Z', 2, 7)");

  // Tags: Favorites (Type 0, no TagMap — must SURVIVE), used (Type 1), unused (Type 1),
  // Research (Type 1) only on the DOOMED duplicate n2 — must migrate to n1, not vanish
  db.run("INSERT INTO Tag VALUES (1, 0, 'Favorites')");
  db.run("INSERT INTO Tag VALUES (2, 1, 'Sermon')");
  db.run("INSERT INTO Tag VALUES (3, 1, 'OldUnused')");
  db.run("INSERT INTO Tag VALUES (4, 1, 'Research')");
  db.run("INSERT INTO TagMap VALUES (1, NULL, NULL, 1, 2, 1)");      // Sermon → n1
  db.run("INSERT INTO TagMap VALUES (2, NULL, NULL, 999, 2, 2)");    // BROKEN link (note 999)
  db.run("INSERT INTO TagMap VALUES (3, NULL, NULL, 2, 4, 1)");      // Research → n2 (doomed dup)

  // Bookmark keeps Location 2 referenced
  db.run("INSERT INTO Bookmark VALUES (1, 2, 2, 0, 'BM', NULL, NULL, NULL)");

  const dbBytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', dbBytes);
  zip.file('manifest.json', JSON.stringify({ name: 'Test Backup', version: 1 }));
  const jwlibBytes = await zip.generateAsync({ type: 'arraybuffer' });
  ok(`Built sick .jwlibrary (${jwlibBytes.byteLength} bytes)`);

  // Expected: dup_notes=1 (n2), empty_notes=1 (n4), dup_marks=1 (m2),
  //           orph_br=1 (br5), orph_tm=1 (tm2), unused_tags=1 (OldUnused), unused_loc=1 (loc3)
  const EXPECTED = { dup_notes: 1, empty_notes: 1, dup_marks: 1, orph_br: 1, orph_tm: 1, unused_tags: 1, unused_loc: 1 };

  section('Boot the Doctor module in JSDOM');
  const html = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
  const m = html.match(/<!-- ── Backup Doctor \(v[\d.]+\) ─[\s\S]*?<!-- ── End Backup Doctor ─[─]*\s*-->/);
  if (!m) { fail('Backup Doctor block not found in beta/index.html'); process.exit(1); }
  const pageHtml = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${m[0]}</body></html>`;
  const dom = new JSDOM(pageHtml, { url: 'https://jwsync.org/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  win.localStorage.setItem('jwsync_lang', 'en');

  if (typeof win.__openJwDoctor !== 'function') { fail('window.__openJwDoctor not exposed'); process.exit(1); }
  ok('window.__openJwDoctor exposed');
  const internals = win.__jwDoctorInternals;
  if (!internals || typeof internals.runChecks !== 'function' || typeof internals.applyFixes !== 'function') {
    fail('__jwDoctorInternals (runChecks/applyFixes) not exposed'); process.exit(1);
  }
  ok('__jwDoctorInternals exposed');

  section('Checks find exactly the planted issues');
  const sickDb = new SQL.Database(new Uint8Array(dbBytes));
  const report = internals.runChecks(sickDb);
  for (const [k, n] of Object.entries(EXPECTED)) {
    if (report.checks[k] === n) ok(`${k} = ${n}`);
    else fail(`${k}: expected ${n}, got ${report.checks[k]}`);
  }
  if (report.totals.notes === 6 && report.totals.marks === 4 && report.totals.bm === 1 && report.totals.tags === 4)
    ok('totals correct (6 notes / 4 highlights / 1 bookmark / 4 tags)');
  else fail('totals wrong: ' + JSON.stringify(report.totals));
  if (report.issues === 7) ok('7 total issues'); else fail('expected 7 issues, got ' + report.issues);
  if (report.score < 100 && report.score >= 35) ok('score reflects issues (' + report.score + ')');
  else fail('score out of range: ' + report.score);

  section('applyFixes repairs everything, touches nothing healthy');
  const fixed = internals.applyFixes(sickDb);
  for (const [k, n] of Object.entries(EXPECTED)) {
    if (fixed[k] === n) ok(`fixed ${k} = ${n}`);
    else fail(`fixed ${k}: expected ${n}, got ${fixed[k]}`);
  }
  const after = internals.runChecks(sickDb);
  if (after.issues === 0 && after.score === 100) ok('re-scan is perfectly clean (score 100)');
  else fail('re-scan not clean: ' + JSON.stringify(after));
  // Healthy records survived
  const q1 = sickDb.exec("SELECT NoteId FROM Note ORDER BY NoteId")[0].values.flat();
  if (JSON.stringify(q1) === JSON.stringify([1, 3, 5, 6])) ok('healthy notes n1+n3 survived; n2+n4 removed');
  else fail('note survivors wrong: ' + JSON.stringify(q1));
  if (q1.includes(5) && q1.includes(6)) ok('same-text notes on DIFFERENT verses of the same chapter both survived');
  else fail('verse-anchored notes were wrongly deduped: ' + JSON.stringify(q1));
  const tagOnKeeper = sickDb.exec("SELECT NoteId FROM TagMap WHERE TagId=4")[0].values.flat();
  if (JSON.stringify(tagOnKeeper) === JSON.stringify([1])) ok("doomed duplicate's tag (Research) migrated to the kept note");
  else fail('Research tag not migrated to keeper: ' + JSON.stringify(tagOnKeeper));
  const q2 = sickDb.exec("SELECT UserMarkId FROM UserMark ORDER BY UserMarkId")[0].values.flat();
  if (JSON.stringify(q2) === JSON.stringify([1, 3, 4])) ok('healthy marks m1+m3+m4 survived; m2 removed');
  else fail('mark survivors wrong: ' + JSON.stringify(q2));
  const q3 = sickDb.exec("SELECT Name FROM Tag ORDER BY TagId")[0].values.flat();
  if (JSON.stringify(q3) === JSON.stringify(['Favorites', 'Sermon', 'Research'])) ok('Favorites (Type 0) + used tags survived; unused removed');
  else fail('tag survivors wrong: ' + JSON.stringify(q3));
  const q4 = sickDb.exec("SELECT LocationId FROM Location ORDER BY LocationId")[0].values.flat();
  if (JSON.stringify(q4) === JSON.stringify([1, 2])) ok('referenced locations survived; leftover removed');
  else fail('location survivors wrong: ' + JSON.stringify(q4));
  const br = sickDb.exec("SELECT BlockRangeId FROM BlockRange ORDER BY BlockRangeId")[0].values.flat();
  if (JSON.stringify(br) === JSON.stringify([1, 3, 4])) ok('healthy block ranges survived; dup + orphan removed');
  else fail('blockrange survivors wrong: ' + JSON.stringify(br));
  sickDb.close();

  section('Clean backup scores 100 and is left untouched');
  const cleanDb = new SQL.Database(new Uint8Array(dbBytes));
  internals.applyFixes(cleanDb); // first clean
  const before = cleanDb.exec("SELECT COUNT(*) FROM Note")[0].values[0][0];
  const fixed2 = internals.applyFixes(cleanDb); // second pass must be a no-op
  const allZero = Object.values(fixed2).every(n => n === 0);
  const afterCnt = cleanDb.exec("SELECT COUNT(*) FROM Note")[0].values[0][0];
  if (allZero && before === afterCnt) ok('second clean pass is a no-op (idempotent)');
  else fail('clean is not idempotent: ' + JSON.stringify(fixed2));
  cleanDb.close();

  section('Worker-side Library Doctor (opts.doctorCheck, v2.65.0)');
  {
    const workerSrc = fs.readFileSync(REPO + '/beta/js/merge-worker.js', 'utf8');
    const mBlock = workerSrc.match(/\/\/ ═+ Library Doctor[\s\S]*?\/\/ ═+ end Library Doctor/);
    if (mBlock) ok('worker contains the Library Doctor block');
    else fail('worker doctor block missing');
    if (workerSrc.includes('p.doctorCheck') && workerSrc.includes('doctor: doctorReport'))
      ok('worker scans on opts.doctorCheck and ships the report with the impact message');
    else fail('worker doctorCheck gate wiring missing');
    if (/if \(doctorReport && doctorReport\.issues > 0\) \{[\s\S]*?doctorFix\(a\)/.test(workerSrc))
      ok('worker applies fixes only AFTER the user confirms the merge');
    else fail('worker fix-after-confirm wiring missing');
    if (mBlock) {
      // run the worker's headless doctor against the same sick database
      const fns = new Function(mBlock[0] + '\nreturn { doctorScan, doctorFix, dDupNotePairs };')();
      const wDb = new SQL.Database(new Uint8Array(dbBytes));
      const scan = fns.doctorScan(wDb);
      let scanOk = scan.issues === 7;
      for (const [k, n] of Object.entries(EXPECTED)) if (scan.checks[k] !== n) scanOk = false;
      if (scanOk) ok('worker doctorScan finds exactly the 7 planted issues');
      else fail('worker scan wrong: ' + JSON.stringify(scan));
      const fixedN = fns.doctorFix(wDb);
      if (fixedN === 7) ok('worker doctorFix repairs all 7');
      else fail('worker fixed ' + fixedN);
      const rescan = fns.doctorScan(wDb);
      if (rescan.issues === 0) ok('worker re-scan is clean');
      else fail('worker re-scan: ' + JSON.stringify(rescan));
      const wq1 = wDb.exec('SELECT NoteId FROM Note ORDER BY NoteId')[0].values.flat();
      if (JSON.stringify(wq1) === JSON.stringify([1, 3, 5, 6]))
        ok('worker fix keeps verse-anchored same-text notes (n5+n6) intact');
      else fail('worker note survivors wrong: ' + JSON.stringify(wq1));
      const wTag = wDb.exec('SELECT NoteId FROM TagMap WHERE TagId=4')[0].values.flat();
      if (JSON.stringify(wTag) === JSON.stringify([1])) ok('worker fix migrates the doomed duplicate\'s tag');
      else fail('worker tag migration wrong: ' + JSON.stringify(wTag));
      wDb.close();
    }
  }

  section('Merge-page checkbox wiring (one-shot, source check)');
  {
    const appSrc = fs.readFileSync(REPO + '/beta/js/app.js', 'utf8');
    if (appSrc.includes('id:"doctor-merge-cb"') && appSrc.includes('id:"doctor-merge-row"'))
      ok('checkbox rendered under the Create My Merged File button');
    else fail('merge-page checkbox markup missing');
    if (appSrc.includes('defaultChecked:!1')) ok('checkbox defaults to unticked');
    else fail('checkbox default wrong');
    if (appSrc.includes('__doctorOnce=!!__dcb.checked;__dcb.checked=!1'))
      ok('vt() reads the box once and unticks it (one-time use)');
    else fail('one-shot read/reset missing in vt()');
    if (appSrc.includes('doctorCheck:__doctorOnce')) ok('flag forwarded to the worker as opts.doctorCheck');
    else fail('opts.doctorCheck not forwarded');
    if (appSrc.includes('window.__jwImpactPreview(d.counts,d.doctor||null)'))
      ok('doctor report passed through to the impact card');
    else fail('d.doctor passthrough missing');
    if (appSrc.includes('window.__jwDoctorCbLabel')) ok('checkbox label comes from the localised Doctor strings');
    else fail('localised label hook missing');
    const full = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
    if (!full.includes('__jwDoctorSuppressAutoDl') && !full.includes('__jwDoctorArmAfterMerge'))
      ok('superseded watcher/suppression machinery fully removed');
    else fail('old watcher/suppression code still present');
    if (full.includes('window.__jwDoctorT')) ok('doctor exposes __jwDoctorT for the impact card');
    else fail('__jwDoctorT missing');
  }

  section('UI flow reaches the report');
  win.__openJwDoctor(jwlibBytes);
  const doc = win.document;
  if (doc.querySelector('.jbd-overlay .jbd-card')) ok('Doctor overlay opened');
  else fail('overlay missing');
  // scanning shows the ECG + staggered rows, then the report ring renders
  let report2 = null;
  for (let i = 0; i < 50; i++) {
    await sleep(200);
    if (doc.querySelector('.jbd-ring-fg')) { report2 = true; break; }
  }
  if (report2) ok('report state rendered (health ring present)');
  else fail('report never rendered');
  if (report2) {
    const warnChips = doc.querySelectorAll('.jbd-chip-warn');
    if (warnChips.length === 7) ok('7 warning chips shown (one per planted issue)');
    else fail('expected 7 warning chips, got ' + warnChips.length);
    const cleanBtn = doc.querySelector('[data-jbd-clean]');
    if (cleanBtn) ok('Clean & Download button offered');
    else fail('clean button missing');
    const totals = doc.querySelectorAll('.jbd-total strong');
    if (totals.length === 4 && totals[0].textContent === '6') ok('totals strip rendered (6 notes)');
    else fail('totals strip wrong');
  }

  section('Clean & Download produces a valid .jwlibrary');
  // Capture the downloaded blob (type), its raw bytes, and the anchor filename.
  let captured = null, dlName = null, blobBytes = null;
  const RealBlob = win.Blob;
  win.Blob = function (parts, opts) { if (parts && parts[0]) blobBytes = parts[0]; return new RealBlob(parts, opts); };
  win.Blob.prototype = RealBlob.prototype;
  win.URL.createObjectURL = (blob) => { captured = blob; return 'blob:doctor-test'; };
  win.URL.revokeObjectURL = () => {};
  const origCreate = doc.createElement.bind(doc);
  doc.createElement = (tag) => {
    const el = origCreate(tag);
    if (String(tag).toLowerCase() === 'a') {
      Object.defineProperty(el, 'click', { value: function () { dlName = el.getAttribute('download'); }, writable: true });
    }
    return el;
  };
  const cleanBtn = doc.querySelector('[data-jbd-clean]');
  if (cleanBtn) {
    cleanBtn.click();
    let done = false;
    for (let i = 0; i < 50; i++) { await sleep(150); if (doc.querySelector('.jbd-done-t')) { done = true; break; } }
    doc.createElement = origCreate; // restore
    if (done) ok('reached the success ("All fixed!") state');
    else fail('never reached the done state after cleaning');
    if (dlName && /\.jwlibrary$/i.test(dlName) && !/\.zip$/i.test(dlName))
      ok('download filename ends in .jwlibrary (' + dlName + ')');
    else fail('download filename not .jwlibrary: ' + dlName);
    win.Blob = RealBlob; // restore
    if (captured && captured.type === 'application/octet-stream')
      ok('blob MIME is application/octet-stream (saves as .jwlibrary, not .zip)');
    else fail('blob MIME wrong: ' + (captured && captured.type));
    if (blobBytes) {
      const rezip = await JSZip.loadAsync(Buffer.from(new Uint8Array(blobBytes)));
      const dbKey = Object.keys(rezip.files).find(k => /userdata\.db$/i.test(k));
      if (dbKey) ok('exported file is a real ZIP containing userData.db');
      else fail('exported file has no userData.db');
      if (rezip.file('manifest.json')) ok('manifest.json preserved in export');
      else fail('manifest.json missing from export');
      if (dbKey) {
        const outBytes = await rezip.files[dbKey].async('uint8array');
        const outDb = new SQL.Database(outBytes);
        const noteCount = outDb.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
        if (noteCount === 4) ok('exported DB opens and is clean (4 healthy notes)');
        else fail('exported DB note count wrong: ' + noteCount);
        outDb.close();
      }
    }
  } else {
    fail('clean button not available to exercise download');
    doc.createElement = origCreate;
  }

  // close cleanly so JSDOM can tear down
  const closeBtn = doc.querySelector('.jbd-x');
  if (closeBtn) closeBtn.click();
  if (!doc.querySelector('.jbd-overlay')) ok('overlay closes cleanly');
  else fail('overlay did not close');

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll Backup Doctor checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error(e); process.exit(1); });

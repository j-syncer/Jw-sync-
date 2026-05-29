// Integration test for the v2.11.0 Merge Conflict Reviewer.
//
// The reviewer is a self-contained IIFE in beta/index.html exposing
// window.__jwConflictReview({ blobUrl }). It reads the original source
// .jwlibrary files from the page's file inputs, diffs every Note that
// shares a Guid across backups but whose content differs, shows the user a
// side-by-side chooser, and (on "Apply & download") rewrites the merged
// SQLite DB on the main thread and hands back a corrected blob.
//
// This suite boots just that module in JSDOM with real JSZip + sql.js wired
// onto window, fabricates two conflicting backups + a "merged" output, and
// asserts:
//   1. A conflict is detected and the overlay renders side-by-side versions
//   2. Picking the other version + Apply rewrites the merged DB content
//   3. "Keep both" adds the alternate version as a second note
//   4. Identical notes across backups produce NO overlay (resolve null)
//   5. Missing deps (no JSZip / sql.js) short-circuits to null instantly
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

const SQL_OPTS = { locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) };

// ── Build a .jwlibrary ArrayBuffer from a list of note rows ──────────
async function buildBackup(SQL, notes) {
  const db = new SQL.Database();
  db.run(`CREATE TABLE Note (
    NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER,
    Title TEXT, Content TEXT, LastModified TEXT, Created TEXT,
    BlockType INTEGER, BlockIdentifier INTEGER );`);
  notes.forEach((n, i) => {
    db.run('INSERT INTO Note (NoteId, Guid, Title, Content, LastModified) VALUES (?,?,?,?,?)',
      [i + 1, n.guid, n.title || null, n.content, n.lastMod || '2024-01-01 00:00:00']);
  });
  const bytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', bytes);
  zip.file('manifest.json', JSON.stringify({ version: 1, name: 'Test' }));
  return zip.generateAsync({ type: 'arraybuffer' });
}

async function readNotes(SQL, buf) {
  const zip = await JSZip.loadAsync(buf);
  const key = Object.keys(zip.files).find(f => /userdata\.db$/i.test(f));
  const bytes = await zip.file(key).async('uint8array');
  const db = new SQL.Database(bytes);
  const out = {};
  const r = db.exec('SELECT Guid,Title,Content FROM Note');
  if (r.length) r[0].values.forEach(v => { (out[v[0]] = out[v[0]] || []).push({ title: v[1], content: v[2] }); });
  const total = db.exec('SELECT COUNT(*) FROM Note')[0].values[0][0];
  db.close();
  return { byGuid: out, total };
}

// ── Boot the reviewer module in a fresh JSDOM, optionally wiring deps ──
function makeReviewerDom(opts) {
  opts = opts || {};
  const html = fs.readFileSync(HTML_PATH, 'utf8');
  const m = html.match(/<!-- ── Merge Conflict Reviewer \(v2\.11\.0\) ─[\s\S]*?<!-- ── End Merge Conflict Reviewer ─[─]*\s*-->/);
  if (!m) return null;
  const block = m[0];
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${block}</body></html>`;
  const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  if (opts.deps) {
    win.JSZip = JSZip;
    win.initSqlJs = () => initSqlJs(SQL_OPTS);
  }
  // Stub createObjectURL (jsdom doesn't implement it)
  win.URL.createObjectURL = () => 'blob:https://jwsync.org/corrected-' + Math.random().toString(16).slice(2);
  return dom;
}

// Attach a file input whose .files returns File-likes for the given buffers.
function attachInputs(win, files) {
  const doc = win.document;
  const input = doc.createElement('input');
  input.type = 'file';
  input.setAttribute('accept', '.jwlibrary');
  doc.body.appendChild(input);
  const fileLikes = files.map(f => ({ name: f.name, size: f.buffer.byteLength, arrayBuffer: async () => f.buffer }));
  Object.defineProperty(input, 'files', { configurable: true, get() { return fileLikes; } });
  return input;
}

async function waitForOverlay(doc, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 5000)) {
    const el = doc.getElementById('jw-conflict-overlay');
    if (el) return el;
    await wait(40);
  }
  return null;
}

(async () => {
  const SQL = await initSqlJs(SQL_OPTS);

  // Shared fixtures: a note edited differently on two devices (same Guid).
  const G = 'guid-shared-1';
  const phoneNote = { guid: G, title: 'Faith', content: 'Faith is the assured expectation of what is hoped for.', lastMod: '2024-03-01 09:00:00' };
  const tabletNote = { guid: G, title: 'Faith', content: 'Faith is the assured expectation of things hoped for, the evident demonstration of realities.', lastMod: '2024-04-15 18:00:00' };
  const phoneOnly = { guid: 'guid-phone-only', title: 'Hope', content: 'Hope does not lead to disappointment.', lastMod: '2024-02-02 02:00:00' };
  const tabletOnly = { guid: 'guid-tablet-only', title: 'Love', content: 'Love is patient and kind.', lastMod: '2024-02-03 03:00:00' };

  const phoneBuf = await buildBackup(SQL, [phoneNote, phoneOnly]);
  const tabletBuf = await buildBackup(SQL, [tabletNote, tabletOnly]);
  // The worker's merged output kept the phone version of the shared note.
  const mergedBuf = await buildBackup(SQL, [phoneNote, phoneOnly, tabletOnly]);

  // ──────────────────────────────────────────────────────────────────
  section('Conflict detected → side-by-side reviewer overlay appears');
  {
    const dom = makeReviewerDom({ deps: true });
    if (!dom) { fail('Conflict Reviewer block not found in beta/index.html'); process.exit(1); }
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedBuf.slice(0) });
    attachInputs(win, [{ name: 'phone.jwlibrary', buffer: phoneBuf }, { name: 'tablet.jwlibrary', buffer: tabletBuf }]);

    if (typeof win.__jwConflictReview !== 'function') { fail('window.__jwConflictReview not exposed'); process.exit(1); }
    ok('window.__jwConflictReview exposed');

    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged', downloadName: 'merged.jwlibrary' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('reviewer overlay did not appear for a real conflict'); dom.window.close(); }
    else {
      ok('reviewer overlay rendered');
      const conflicts = overlay.querySelectorAll('.jcr-conflict');
      if (conflicts.length === 1) ok('exactly 1 conflict shown (the shared note)');
      else fail('expected 1 conflict, got ' + conflicts.length);
      const vers = overlay.querySelectorAll('.jcr-conflict .jcr-ver');
      if (vers.length === 2) ok('two version cards rendered (phone vs tablet)');
      else fail('expected 2 version cards, got ' + vers.length);
      const current = overlay.querySelector('.jcr-ver-current');
      if (current) ok('the merged choice is badged "' + current.textContent + '"');
      else fail('no "current" badge on the merged choice');
      // A diff highlight should be present on the non-current card
      if (overlay.querySelector('.jcr-ins') || overlay.querySelector('.jcr-del')) ok('word-level diff highlight rendered');
      else fail('no diff highlight rendered on the alternate version');
      const picks = overlay.querySelectorAll('.jcr-ver-pick');
      if (picks.length === 2) ok('each version has a "Keep this" control');
      else fail('expected 2 pick buttons, got ' + picks.length);
      // dismiss (skip) → resolves null
      overlay.querySelector('.jcr-btn-ghost').click();
      const res = await reviewP;
      if (res === null) ok('"Keep merge as-is" resolves null (no rewrite)');
      else fail('skip should resolve null, got ' + JSON.stringify(res));
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  section('Pick the other version + Apply → merged DB is rewritten');
  {
    const dom = makeReviewerDom({ deps: true });
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedBuf.slice(0) });
    attachInputs(win, [{ name: 'phone.jwlibrary', buffer: phoneBuf }, { name: 'tablet.jwlibrary', buffer: tabletBuf }]);

    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      // Find the NON-current version card and click its pick button.
      const cards = Array.from(overlay.querySelectorAll('.jcr-ver'));
      const alt = cards.find(c => !c.querySelector('.jcr-ver-current'));
      alt.querySelector('.jcr-ver-pick').click();
      if (alt.classList.contains('sel')) ok('alternate version becomes selected on click');
      else fail('alternate version did not select');
      overlay.querySelector('.jcr-btn-primary').click();
      const res = await reviewP;
      if (res && res.buffer) {
        ok('Apply resolves with a corrected buffer + blobUrl');
        const { byGuid, total } = await readNotes(SQL, res.buffer);
        const shared = byGuid[G] && byGuid[G][0];
        if (shared && shared.content === tabletNote.content) ok('shared note content now matches the chosen (tablet) version');
        else fail('shared note was not rewritten to the tablet version: ' + (shared && shared.content));
        if (total === 3) ok('note count unchanged (override, not duplicate): ' + total);
        else fail('expected 3 notes after override, got ' + total);
      } else { fail('Apply did not return a corrected buffer: ' + JSON.stringify(res)); }
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  section('"Keep both" → alternate version added as a second note');
  {
    const dom = makeReviewerDom({ deps: true });
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedBuf.slice(0) });
    attachInputs(win, [{ name: 'phone.jwlibrary', buffer: phoneBuf }, { name: 'tablet.jwlibrary', buffer: tabletBuf }]);

    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      const bothBtn = overlay.querySelector('.jcr-both-btn');
      bothBtn.click();
      if (bothBtn.classList.contains('on')) ok('"Keep both" toggles on');
      else fail('"Keep both" did not toggle on');
      overlay.querySelector('.jcr-btn-primary').click();
      const res = await reviewP;
      if (res && res.buffer) {
        const { byGuid, total } = await readNotes(SQL, res.buffer);
        if (total === 4) ok('a second note was added (3 → 4)');
        else fail('expected 4 notes after keep-both, got ' + total);
        // Both phone and tablet content should now exist somewhere
        const allContent = [];
        Object.keys(byGuid).forEach(g => byGuid[g].forEach(n => allContent.push(n.content)));
        if (allContent.includes(phoneNote.content) && allContent.includes(tabletNote.content))
          ok('both the phone and tablet versions are present after keep-both');
        else fail('keep-both did not preserve both versions');
      } else { fail('keep-both Apply did not return a buffer'); }
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  section('No real conflict (identical notes) → no overlay, resolves null');
  {
    const sameA = await buildBackup(SQL, [phoneNote, phoneOnly]);
    const sameB = await buildBackup(SQL, [phoneNote, tabletOnly]); // shared note IDENTICAL
    const mergedSame = await buildBackup(SQL, [phoneNote, phoneOnly, tabletOnly]);
    const dom = makeReviewerDom({ deps: true });
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedSame.slice(0) });
    attachInputs(win, [{ name: 'a.jwlibrary', buffer: sameA }, { name: 'b.jwlibrary', buffer: sameB }]);

    const res = await win.__jwConflictReview({ blobUrl: 'blob:merged' });
    if (res === null) ok('identical shared note → resolves null');
    else fail('expected null for no-conflict, got ' + JSON.stringify(res));
    if (!doc.getElementById('jw-conflict-overlay')) ok('no overlay shown when there are no conflicts');
    else fail('overlay leaked with no conflicts');
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('Missing deps (no JSZip / sql.js) → short-circuits to null');
  {
    const dom = makeReviewerDom({ deps: false });
    const win = dom.window, doc = win.document;
    attachInputs(win, [{ name: 'phone.jwlibrary', buffer: phoneBuf }, { name: 'tablet.jwlibrary', buffer: tabletBuf }]);
    const res = await win.__jwConflictReview({ blobUrl: 'blob:merged' });
    if (res === null) ok('no JSZip/initSqlJs → resolves null (celebration proceeds normally)');
    else fail('expected null when deps missing, got ' + JSON.stringify(res));
    if (!doc.getElementById('jw-conflict-overlay')) ok('no overlay when deps missing');
    else fail('overlay leaked when deps missing');
    dom.window.close();
  }

  // ──────────────────────────────────────────────────────────────────
  section('Single backup (nothing to compare) → resolves null');
  {
    const dom = makeReviewerDom({ deps: true });
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedBuf.slice(0) });
    attachInputs(win, [{ name: 'only.jwlibrary', buffer: phoneBuf }]);
    const res = await win.__jwConflictReview({ blobUrl: 'blob:merged' });
    if (res === null) ok('fewer than 2 source backups → resolves null');
    else fail('expected null for single backup, got ' + JSON.stringify(res));
    dom.window.close();
  }

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll conflict-reviewer checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

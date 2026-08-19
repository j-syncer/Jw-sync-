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
//   6. The v3.44.0 comparison: a line-aligned diff of the two versions,
//      per-line ticks that combine them, and a hand-editable result — each
//      asserted on the Note rows that come back out of the rebuilt file
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const { JSDOM } = require('jsdom');
const { inlineModules } = require('./helpers/page-source');
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
  // A realistic manifest, hash included. A stub without one cannot show that
  // the reviewer refreshed the hash, and a hash left pointing at the database
  // the file used to hold is a file JW Library refuses without saying so.
  zip.file('manifest.json', JSON.stringify({
    name: 'UserdataBackup', creationDate: '2024-01-01', version: 1, type: 0,
    userDataBackup: {
      lastModifiedDate: '2024-01-01T00:00:00Z', deviceName: 'Test', databaseName: 'userData.db',
      hash: sha256Hex(bytes), schemaVersion: '16'
    }
  }));
  return zip.generateAsync({ type: 'arraybuffer' });
}

function sha256Hex(bytes) { return crypto.createHash('sha256').update(Buffer.from(bytes)).digest('hex'); }

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
  const html = inlineModules(fs.readFileSync(HTML_PATH, 'utf8'), HTML_PATH);
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
    // Both index.html files load this; without it the reviewer would be tested
    // on a code path production never takes.
    win.eval(fs.readFileSync(path.join(REPO, 'js/jwlibrary-manifest.js'), 'utf8'));
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
      // dismiss (skip) → resolves null  (target the explicit skip control —
      // the foot also holds a "Suggest best" ghost button as of v2.22)
      overlay.querySelector('[data-jcr-skip].jcr-btn').click();
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
  section('Smart suggestion (v2.22.0) → recommends a version + badge');
  {
    const dom = makeReviewerDom({ deps: true });
    const win = dom.window, doc = win.document;
    win.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedBuf.slice(0) });
    attachInputs(win, [{ name: 'phone.jwlibrary', buffer: phoneBuf }, { name: 'tablet.jwlibrary', buffer: tabletBuf }]);

    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      const suggestBtn = overlay.querySelector('[data-jcr-suggest]');
      if (suggestBtn) ok('"Suggest best" button present');
      else fail('Suggest button missing');
      // Before: no suggestion styling
      if (!overlay.querySelector('.jcr-suggested')) ok('no suggestion highlighted before click');
      else fail('suggestion shown before clicking Suggest');
      suggestBtn.click();
      // After: exactly one card per conflict is highlighted + badged
      const suggested = overlay.querySelectorAll('.jcr-suggested');
      if (suggested.length >= 1) ok('a version is highlighted as suggested after click');
      else fail('no suggested version after clicking Suggest');
      const badge = overlay.querySelector('.jcr-suggestion-badge');
      if (badge && badge.textContent.trim().length > 0) ok('suggestion badge with reason rendered: "' + badge.textContent + '"');
      else fail('no suggestion badge rendered');
      // The suggested card should also be the selected one
      if (overlay.querySelector('.jcr-suggested.sel')) ok('suggested version is auto-selected');
      else fail('suggested version was not selected');
      // Cancel out
      overlay.querySelector('[data-jcr-skip].jcr-btn').click();
      await reviewP;
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

  // ──────────────────────────────────────────────────────────────────
  // v3.44.0 — side-by-side comparison and combining.
  //
  // Picking a whole version is the fast path, but it is still a choice
  // between two things the reader wrote: whichever loses is gone. These
  // sections cover the case the automatic merge cannot resolve at all —
  // each device holds a line worth keeping — and assert on the note rows
  // that actually land in the rebuilt backup, not just the UI state. A
  // combined note that renders correctly but writes the wrong Content is
  // silent data loss, which is the failure this whole screen exists to
  // prevent.
  section('Compare side by side → aligned line diff with per-line ticks');
  const SHARED_LINE = 'Both devices kept this line.';
  const G2 = 'guid-multiline-1';
  const phoneMulti = {
    guid: G2, title: 'Faith',
    content: '<p>' + SHARED_LINE + '</p><p>Faith is the assured expectation.</p><p>Written on the phone.</p>',
    lastMod: '2024-03-01 09:00:00'
  };
  const tabletMulti = {
    guid: G2, title: 'Faith',
    content: '<p>' + SHARED_LINE + '</p><p>Faith is the assured expectation of what is hoped for.</p><p>Written on the tablet.</p>',
    lastMod: '2024-04-15 18:00:00'
  };
  const phoneMultiBuf = await buildBackup(SQL, [phoneMulti]);
  const tabletMultiBuf = await buildBackup(SQL, [tabletMulti]);
  const mergedMultiBuf = await buildBackup(SQL, [phoneMulti]);   // the merge kept the phone side

  function openCompare(overlay) {
    const btn = overlay.querySelector('.jcr-compare-btn');
    if (!btn) return null;
    btn.click();
    return overlay.querySelector('.jcr-compare');
  }
  function bootMulti() {
    const dom = makeReviewerDom({ deps: true });
    dom.window.fetch = () => Promise.resolve({ arrayBuffer: async () => mergedMultiBuf.slice(0) });
    attachInputs(dom.window, [
      { name: 'phone.jwlibrary', buffer: phoneMultiBuf },
      { name: 'tablet.jwlibrary', buffer: tabletMultiBuf }
    ]);
    return dom;
  }

  {
    const dom = bootMulti();
    const win = dom.window, doc = win.document;
    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear for the multi-line conflict'); dom.window.close(); }
    else {
      const btn = overlay.querySelector('.jcr-compare-btn');
      if (btn) ok('"Compare side by side" control present on the conflict');
      else fail('no compare control rendered');
      const pane = openCompare(overlay);
      if (pane && !pane.hidden) ok('comparison pane opens on click');
      else fail('comparison pane did not open');

      const rows = overlay.querySelectorAll('.jcr-drow');
      if (rows.length >= 3) ok('line-aligned diff rendered (' + rows.length + ' rows)');
      else fail('expected at least 3 diff rows, got ' + rows.length);
      if (overlay.querySelector('.jcr-drow-eq')) ok('the line both devices share is shown as unchanged');
      else fail('no unchanged row — the shared line was not aligned');
      const chg = overlay.querySelectorAll('.jcr-drow-chg');
      if (chg.length >= 1) ok('edited lines are paired opposite their replacement (' + chg.length + ')');
      else fail('no changed-line rows: edits were not aligned side by side');
      // Both columns exist on a changed row, each carrying its own word marks.
      if (overlay.querySelector('.jcr-dcut .jcr-del')) ok('removed words marked in the left column');
      else fail('no word-level deletion marked on the left column');
      if (overlay.querySelector('.jcr-dnew .jcr-ins')) ok('added words marked in the right column');
      else fail('no word-level insertion marked on the right column');
      if (overlay.querySelectorAll('.jcr-dtick').length >= 2) ok('every changed line carries its own tick');
      else fail('per-line ticks missing');

      // Opening the comparison must not, by itself, change the outcome:
      // the draft starts as an exact copy of the merge's own choice.
      const ta = overlay.querySelector('.jcr-combine-text');
      if (ta && ta.value.includes('Written on the phone.') && !ta.value.includes('Written on the tablet.'))
        ok('the draft opens reproducing the merge exactly (nothing adopted yet)');
      else fail('draft did not open as the merged version: ' + (ta && JSON.stringify(ta.value)));

      overlay.querySelector('[data-jcr-skip].jcr-btn').click();
      await reviewP;
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  section('Combine both sides → one note carrying work from both devices');
  {
    const dom = bootMulti();
    const win = dom.window, doc = win.document;
    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      openCompare(overlay);
      const acts = Array.from(overlay.querySelectorAll('.jcr-cmp-act'));
      const bothAct = acts[2];           // All from merge / All from other / Keep both sides
      bothAct.click();
      const ta = overlay.querySelector('.jcr-combine-text');
      if (ta.value.includes('Written on the phone.') && ta.value.includes('Written on the tablet.'))
        ok('"Keep both sides" draws both devices’ lines into the draft');
      else fail('combined draft is missing a side: ' + JSON.stringify(ta.value));
      if ((ta.value.match(new RegExp(SHARED_LINE, 'g')) || []).length === 1)
        ok('the line both devices share appears once, not twice');
      else fail('shared line duplicated in the combined draft');

      const useBtn = overlay.querySelector('.jcr-use-combined');
      useBtn.click();
      if (useBtn.classList.contains('on')) ok('"Use this combined text" latches on');
      else fail('use-combined did not latch');
      const badge = overlay.querySelector('.jcr-custom-badge');
      if (badge && !badge.hidden) ok('the conflict is badged as combined');
      else fail('no combined badge on the conflict');
      if (!overlay.querySelector('.jcr-ver.sel')) ok('choosing a whole version is deselected while combining');
      else fail('a version card stayed selected alongside the combined text');

      overlay.querySelector('.jcr-btn-primary').click();
      const res = await reviewP;
      if (res && res.buffer) {
        const { byGuid, total } = await readNotes(SQL, res.buffer);
        const note = byGuid[G2] && byGuid[G2][0];
        if (note && note.content.includes('Written on the phone.') && note.content.includes('Written on the tablet.'))
          ok('the rebuilt backup holds one note with both devices’ lines');
        else fail('combined text did not reach the note row: ' + (note && note.content));
        if (note && !/Written on the phone\.[\s\S]*Written on the phone\./.test(note.content))
          ok('no line was written twice');
        else fail('a line was duplicated in the written note');
        if (note && /<p>/i.test(note.content) && /<br\s*\/?>/i.test(note.content))
          ok('written back as HTML, matching how the note was already stored');
        else fail('combined note lost the note’s storage format: ' + (note && note.content));
        if (total === 1) ok('still one note — combined, not duplicated');
        else fail('expected 1 note after combining, got ' + total);
      } else fail('Apply after combining returned no buffer');
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  section('Hand-edited combined text is written through verbatim');
  {
    const dom = bootMulti();
    const win = dom.window, doc = win.document;
    const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
    const overlay = await waitForOverlay(doc);
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      openCompare(overlay);
      const ta = overlay.querySelector('.jcr-combine-text');
      ta.value = 'A sentence the reader typed themselves.';
      ta.dispatchEvent(new win.Event('input', { bubbles: true }));

      // Ticks no longer overwrite what was typed; rebuilding is asked for.
      const rebuild = overlay.querySelector('.jcr-rebuild');
      if (rebuild && rebuild.hidden) ok('no rebuild prompt until a tick is touched');
      else fail('rebuild control shown too early');
      const tick = overlay.querySelector('.jcr-dtick');
      tick.click();
      if (ta.value === 'A sentence the reader typed themselves.') ok('a tick does not silently discard the typed text');
      else fail('typed text was overwritten by a tick: ' + JSON.stringify(ta.value));
      if (rebuild && !rebuild.hidden) ok('a rebuild control appears instead');
      else fail('no rebuild control offered after a tick');

      overlay.querySelector('.jcr-use-combined').click();
      overlay.querySelector('.jcr-btn-primary').click();
      const res = await reviewP;
      if (res && res.buffer) {
        const { byGuid } = await readNotes(SQL, res.buffer);
        const note = byGuid[G2] && byGuid[G2][0];
        if (note && note.content.includes('A sentence the reader typed themselves.'))
          ok('the reader’s own wording is what lands in the note');
        else fail('hand-edited text did not reach the note: ' + (note && note.content));
        if (note && !note.content.includes('Written on the tablet.'))
          ok('nothing the reader deleted came back');
        else fail('discarded text reappeared in the note');
      } else fail('Apply after a hand edit returned no buffer');
      dom.window.close();
    }
  }

  // ──────────────────────────────────────────────────────────────────
  // The reviewer's script is a shared file — one copy serves both sites —
  // but its stylesheet lives in each index.html. Ship the module without
  // the styles and the comparison renders unstyled on whichever page was
  // missed, which is exactly how the Awards tab went missing from beta.
  section('Comparison CSS is defined on both index.html copies');
  {
    const CLASSES = [
      'jcr-compare-row', 'jcr-compare-btn', 'jcr-compare', 'jcr-cmp-pick-row', 'jcr-cmp-pick',
      'jcr-cmp-heads', 'jcr-cmp-head', 'jcr-cmp-hint', 'jcr-diff', 'jcr-drow', 'jcr-dside',
      'jcr-deq', 'jcr-dcut', 'jcr-dnew', 'jcr-dempty', 'jcr-dtick', 'jcr-dtext',
      'jcr-cmp-actions', 'jcr-cmp-act', 'jcr-rebuild', 'jcr-combine', 'jcr-combine-label',
      'jcr-combine-text', 'jcr-use-combined', 'jcr-custom-badge'
    ];
    ['index.html', 'beta/index.html'].forEach(f => {
      const src = fs.readFileSync(path.join(REPO, f), 'utf8');
      const missing = CLASSES.filter(cls => !src.includes('.' + cls + '{') && !src.includes('.' + cls + ' ') && !src.includes('.' + cls + ':') && !src.includes('.' + cls + ','));
      if (!missing.length) ok('all ' + CLASSES.length + ' comparison classes styled in ' + f);
      else fail(f + ' is missing CSS for: ' + missing.join(', '));
    });
  }

  // ──────────────────────────────────────────────────────────────────
  section('Every language can read the comparison UI');
  {
    const src = fs.readFileSync(path.join(REPO, 'js/conflict-review.js'), 'utf8');
    const NEW_KEYS = ['compare', 'compare_hide', 'cmp_hint', 'all_cur', 'all_alt', 'all_both',
                      'combined', 'use_combined', 'using_combined', 'rebuild', 'custom_badge'];
    const start = src.indexOf('{', src.indexOf('var I18N'));
    let d = 0, end = start;
    for (let i = start; i < src.length; i++) {
      if (src[i] === '{') d++;
      else if (src[i] === '}') { d--; if (d === 0) { end = i + 1; break; } }
    }
    let table = null;
    try { table = eval('(' + src.slice(start, end) + ')'); } catch (e) { fail('I18N table does not evaluate: ' + e.message); }
    if (table) {
      const langs = Object.keys(table);
      const short = langs.filter(l => NEW_KEYS.some(k => !table[l][k]));
      if (!short.length) ok('all ' + NEW_KEYS.length + ' new strings translated in every one of the ' + langs.length + ' languages');
      else fail('untranslated comparison strings in: ' + short.join(', '));
    }
  }

  // ──────────────────────────────────────────────────────────────────
  // Everything above proves the reviewer writes the right rows. This proves
  // JW Library will accept the file it wrote them into. A .jwlibrary whose
  // manifest hash still points at the database the file used to contain is
  // refused *silently* — the app flickers back to the same screen — so a
  // correct merge and a stale hash are indistinguishable from a corrupt
  // file to the person holding it. The reviewer rebuilt the database and
  // re-zipped it on its own for four releases without touching the hash.
  section('The rebuilt .jwlibrary is one JW Library will actually restore');
  {
    for (const [label, resolve] of [
      ['picking the other version', o => {
        const cards = Array.from(o.querySelectorAll('.jcr-ver'));
        cards.find(x => !x.querySelector('.jcr-ver-current')).querySelector('.jcr-ver-pick').click();
      }],
      ['keeping both', o => o.querySelector('.jcr-both-btn').click()],
      ['combining by hand', o => {
        o.querySelector('.jcr-compare-btn').click();
        Array.from(o.querySelectorAll('.jcr-cmp-act'))[2].click();
        o.querySelector('.jcr-use-combined').click();
      }]
    ]) {
      const dom = bootMulti();
      const win = dom.window, doc = win.document;
      const reviewP = win.__jwConflictReview({ blobUrl: 'blob:merged' });
      const overlay = await waitForOverlay(doc);
      if (!overlay) { fail('overlay did not appear (' + label + ')'); dom.window.close(); continue; }
      resolve(overlay);
      overlay.querySelector('.jcr-btn-primary').click();
      const res = await reviewP;
      if (!res || !res.buffer) { fail('no buffer returned when ' + label); dom.window.close(); continue; }

      const zip = await JSZip.loadAsync(res.buffer);
      const dbBytes = await zip.file(Object.keys(zip.files).find(f => /userdata\.db$/i.test(f))).async('uint8array');
      const db = new SQL.Database(dbBytes);
      const integrity = db.exec('PRAGMA integrity_check')[0].values[0][0];
      db.close();
      if (integrity === 'ok') ok('SQLite intact after ' + label);
      else fail('database corrupt after ' + label + ': ' + integrity);

      const mf = zip.file('manifest.json');
      if (!mf) { fail('manifest.json dropped from the file when ' + label); dom.window.close(); continue; }
      const m = JSON.parse(await mf.async('string'));
      const stated = m.userDataBackup && m.userDataBackup.hash;
      if (stated === sha256Hex(dbBytes)) ok('manifest hash describes the rebuilt database after ' + label);
      else fail('stale manifest hash after ' + label + ' — JW Library would refuse this file silently');
      if (m.userDataBackup && m.userDataBackup.schemaVersion === '16')
        ok('schemaVersion carried through untouched after ' + label);
      else fail('schemaVersion lost after ' + label + ': ' + JSON.stringify(m.userDataBackup));
      dom.window.close();
    }
  }

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll conflict-reviewer checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

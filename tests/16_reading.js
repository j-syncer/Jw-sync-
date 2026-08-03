// Test suite for the v2.92.0 Reading Companion (js/reading.js).
//
// The Reading Companion is a shared module (js/reading.js == beta/js/reading.js)
// exposing window.JwReading: a daily Bible reading plan (canonical or
// chronological order, pace presets or custom chapters/day) with a self-healing
// schedule, streaks, milestones, a 66-book progress grid, and — uniquely —
// the user's own notes/highlights from a .jwlibrary shown on today's chapters.
//
// Covered here:
//   1. Plan data: both orders cover exactly 1,189 unique chapters
//   2. Engine: portion sizing, self-healing carry-over, streaks, forecast,
//      milestones, portion labels, jw.org finder links
//   3. I18N: all 12 languages × every UI key
//   4. UI (JSDOM): onboarding → start plan → today rows → check off → done
//      state + streak chip; state survives a remount
//   5. Notes integration: synthetic .jwlibrary → notes render under today's
//      chapters, highlight counts extracted per chapter
//   6. landing-page wiring on both index.html files: script tag, tool card, i18n
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function eq(a, b, label) { if (a === b) ok(label + ' (' + a + ')'); else fail(label + ': expected ' + b + ', got ' + a); }

const LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'ru', 'ja', 'ko', 'tl', 'sv', 'ceb'];
const REQUIRED_KEYS = ['brand', 'tagline', 'choose_plan', 'plan_canon', 'plan_canon_d', 'plan_chrono', 'plan_chrono_d',
  'choose_pace', 'pace_3m', 'pace_6m', 'pace_1y', 'pace_2y', 'pace_custom', 'per_day', 'finish_by', 'start',
  'today', 'read', 'streak_days', 'done_t', 'done_s', 'come_back', 'progress', 'chapters_read', 'forecast',
  'your_notes', 'your_notes_s', 'notes_none', 'notes_hint', 'hl_n', 'change', 'reset', 'reset_c', 'confirm',
  'cancel', 'close', 'ms_t', 'ms_book', 'ms_hebrew', 'ms_greek', 'ms_all', 'card_today', 'card_start',
  'finished_t', 'finished_s'];

function freshWindow() {
  const src = fs.readFileSync(REPO + '/js/reading.js', 'utf8');
  const dom = new JSDOM('<!DOCTYPE html><html><head></head><body><div id="host"></div></body></html>', {
    url: 'https://jwsync.org/beta/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
  });
  const win = dom.window;
  win.localStorage.setItem('jwsync_lang', 'en');
  win.eval(src);
  return { dom, win, doc: win.document };
}

function blankState(extra) {
  return Object.assign({ read: {}, log: {}, cele: {}, plan: 'canonical', days: 365, daysDone: 0 }, extra || {});
}

async function waitFor(predicate, label, timeoutMs = 8000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    try { if (predicate()) return true; } catch (_) {}
    await new Promise(r => setTimeout(r, 50));
  }
  fail('timeout waiting for: ' + label);
  return false;
}

(async () => {
  section('Module loads and exposes API');
  const { win, doc } = freshWindow();
  if (!win.JwReading) { fail('window.JwReading not exposed'); process.exit(1); }
  ok('window.JwReading exposed');
  for (const fn of ['open', 'close', 'mount', 'updateHomeCard']) {
    if (typeof win.JwReading[fn] === 'function') ok('JwReading.' + fn + ' is a function');
    else fail('JwReading.' + fn + ' missing');
  }
  const E = win.JwReading._engine;
  if (!E) { fail('JwReading._engine missing'); process.exit(1); }

  section('Plan data: both orders cover the whole Bible');
  eq(E.TOTAL, 1189, 'TOTAL chapters');
  eq(E.CHAP.reduce((a, b) => a + b, 0), 1189, 'chapter counts sum');
  eq(E.CHAP.length, 66, 'chapter count entries');
  eq(E.BOOKS.length, 66, 'book names');
  eq(E.ABBR.length, 66, 'book abbreviations');
  for (const plan of ['canonical', 'chrono']) {
    const seq = E.seqFor(plan);
    eq(seq.length, 1189, plan + ' sequence length');
    const uniq = new Set(seq.map(x => x[0] + ':' + x[1]));
    eq(uniq.size, 1189, plan + ' sequence unique chapters');
  }
  const canon = E.seqFor('canonical');
  eq(canon[0].join(':'), '1:1', 'canonical starts at Genesis 1');
  eq(canon[1188].join(':'), '66:22', 'canonical ends at Revelation 22');
  const chrono = E.seqFor('chrono');
  eq(chrono[0].join(':'), '1:1', 'chronological starts at Genesis 1');
  eq(chrono[50].join(':'), '18:1', 'chronological reads Job right after Genesis');
  eq(chrono[1188].join(':'), '66:22', 'chronological ends at Revelation 22');
  eq(new Set(E.CHRONO).size, 66, 'chronological order lists every book once');

  section('Engine: portion sizing & self-healing schedule');
  let st = blankState();
  let info = E.todayInfo(st, '2026-01-01');
  eq(info.rows.length, 3, '1-year plan first portion is 3 chapters (floor(1189/365))');
  eq(info.done, false, 'fresh day is not done');
  st = blankState({ days: undefined, perDay: 5 });
  eq(E.todayInfo(st, '2026-01-01').rows.length, 5, 'custom 5/day portion is 5 chapters');

  // Complete a full day → done + streak
  st = blankState();
  let hit = [];
  for (const [b, c] of E.todayInfo(st, '2026-01-01').rows) hit = hit.concat(E.markRead(st, b, c, '2026-01-01'));
  eq(E.todayInfo(st, '2026-01-01').done, true, 'day marked done after completing portion');
  eq(st.streak, 1, 'streak starts at 1');
  eq(st.daysDone, 1, 'daysDone incremented');

  // Next consecutive day → streak grows
  for (const [b, c] of E.todayInfo(st, '2026-01-02').rows) E.markRead(st, b, c, '2026-01-02');
  eq(st.streak, 2, 'streak grows on consecutive day');

  // Skip a day → streak resets to 1
  for (const [b, c] of E.todayInfo(st, '2026-01-04').rows) E.markRead(st, b, c, '2026-01-04');
  eq(st.streak, 1, 'streak resets after a missed day');
  eq(st.longest, 2, 'longest streak retained');

  // Self-healing: reading only part of a portion carries over without piling up
  st = blankState();
  const day1 = E.todayInfo(st, '2026-01-01').rows;
  E.markRead(st, day1[0][0], day1[0][1], '2026-01-01');
  E.markRead(st, day1[1][0], day1[1][1], '2026-01-01');
  eq(E.todayInfo(st, '2026-01-01').done, false, 'partial day is not done');
  const day2 = E.todayInfo(st, '2026-01-02').rows;
  eq(day2.length, 1, 'next day only owes the 1 remaining chapter (no guilt pile)');
  E.markRead(st, day2[0][0], day2[0][1], '2026-01-02');
  eq(E.todayInfo(st, '2026-01-02').done, true, 'catch-up chapter completes the day');

  section('Engine: forecast, labels, links');
  st = blankState();
  eq(E.forecast(st, '2026-01-01'), '2027-01-01', 'fresh 1-year plan forecasts ~365 days out');
  st = blankState({ days: undefined, perDay: 100 });
  eq(E.forecast(st, '2026-01-01'), '2026-01-13', '100/day plan forecasts 12 days out');
  eq(E.portionLabel([[1, 1], [1, 2], [1, 3]]), 'Genesis 1–3', 'portion label within one book');
  eq(E.portionLabel([[1, 50], [2, 1]]), 'Genesis 50 – Exodus 1', 'portion label across books');
  eq(E.portionLabel([[19, 37]]), 'Psalms 37', 'single-chapter label');
  const url = E.chapterUrl(19, 37);
  if (url.includes('jw.org/finder') && url.includes('bible=19037000') && url.includes('pub=nwtsty'))
    ok('chapter link is a jw.org finder deep link (' + url.slice(0, 60) + '…)');
  else fail('bad chapter url: ' + url);
  if (E.chapterUrl(1, 1).includes('bible=01001000')) ok('Genesis 1 zero-padded correctly');
  else fail('Genesis 1 url wrong: ' + E.chapterUrl(1, 1));

  section('Engine: milestones');
  st = blankState();
  let hits = [];
  for (let c = 1; c <= 50; c++) hits = hits.concat(E.markRead(st, 1, c, '2026-01-01'));
  if (hits.includes('b1')) ok('finishing Genesis fires the book milestone');
  else fail('book milestone did not fire: ' + JSON.stringify(hits));
  if (E.markRead(st, 1, 1, '2026-01-02').length === 0) ok('re-marking a read chapter is a no-op');
  else fail('re-marking fired milestones again');
  // Read everything → hebrew + greek + all fire exactly once
  st = blankState();
  let all = [];
  for (const [b, c] of E.seqFor('canonical')) all = all.concat(E.markRead(st, b, c, '2026-01-01'));
  if (all.includes('hebrew') && all.includes('greek') && all.includes('all'))
    ok('hebrew/greek/whole-Bible milestones fire on full read-through');
  else fail('section milestones missing: ' + all.filter(h => !h.startsWith('b')).join(','));
  eq(all.filter(h => h === 'all').length, 1, 'whole-Bible milestone fires once');
  eq(E.todayInfo(st, '2026-02-01').finished, true, 'plan reports finished');

  section('I18N coverage');
  const src = fs.readFileSync(REPO + '/js/reading.js', 'utf8');
  const im = src.match(/var I18N = \{([\s\S]*?)\n {2}\};/);
  if (!im) fail('I18N object not found in js/reading.js');
  else {
    let okAll = true;
    for (const lang of LANGS) {
      const lm = im[1].match(new RegExp('\\b' + lang + ': \\{([\\s\\S]*?)\\}(?:,\\n|\\n|$)'));
      if (!lm) { okAll = false; fail('I18N missing language: ' + lang); continue; }
      const miss = REQUIRED_KEYS.filter(k => !new RegExp('(^|[,{]) ?' + k + ':').test(lm[1]));
      if (miss.length) { okAll = false; fail('I18N ' + lang + ' missing: ' + miss.join(',')); }
    }
    if (okAll) ok('I18N covers all 12 languages × ' + REQUIRED_KEYS.length + ' keys');
  }

  section('UI: onboarding → active plan → done state (JSDOM)');
  const host = doc.getElementById('host');
  win.JwReading.mount(host);
  if (host.querySelector('.jr-opt') && host.querySelectorAll('.jr-pace').length >= 5 && host.querySelector('.jr-start'))
    ok('onboarding renders plan options, pace presets and start button');
  else fail('onboarding did not render');
  if (host.textContent.includes('You would finish around')) ok('live finish-date preview shown');
  else fail('finish-date preview missing');
  host.querySelector('.jr-start').click();
  let rows = host.querySelectorAll('.jr-row');
  eq(rows.length, 3, 'active view shows 3 chapter rows for the default 1-year plan');
  if (host.textContent.includes('Genesis 1')) ok('first portion starts at Genesis 1');
  else fail('Genesis 1 not in first portion');
  const links = host.querySelectorAll('.jr-golink');
  if (links.length === 3 && links[0].href.includes('jw.org/finder')) ok('every chapter row links to jw.org finder');
  else fail('chapter links missing/wrong');
  if (host.querySelector('.jr-books') && host.querySelectorAll('.jr-bk').length === 66)
    ok('66-book progress grid renders');
  else fail('book progress grid missing');
  // Check off all three chapters
  for (let i = 0; i < 3; i++) {
    const cb = host.querySelector('.jr-row:not(.jr-row-done) .jr-cb');
    if (!cb) { fail('checkbox ' + i + ' not found'); break; }
    cb.click();
  }
  if (host.querySelector('.jr-done') && host.textContent.includes("Today's reading is done"))
    ok('done state renders after completing the portion');
  else fail('done state missing after completing portion');
  if (host.textContent.includes('1-day streak')) ok('streak chip shows 1-day streak');
  else fail('streak chip missing');
  const persisted = JSON.parse(win.localStorage.getItem('jwsync_reading_v1'));
  if (persisted && persisted.plan === 'canonical' && Object.keys(persisted.read).length === 3)
    ok('state persisted to localStorage (3 chapters read)');
  else fail('persisted state wrong: ' + win.localStorage.getItem('jwsync_reading_v1'));
  // Remount → straight to active view
  host.innerHTML = '';
  win.JwReading.mount(host);
  if (host.querySelector('.jr-done') && !host.querySelector('.jr-start'))
    ok('remount restores the active plan (no onboarding)');
  else fail('remount did not restore active state');

  section('Notes integration: synthetic .jwlibrary');
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  const db = new SQL.Database();
  db.run(`
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
      DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER, KeySymbol TEXT, MepsLanguage INTEGER, Type INTEGER, Title TEXT);
    CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER,
      StyleIndex INTEGER, UserMarkGuid TEXT, Version INTEGER);
    CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER,
      Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
  `);
  db.run(`INSERT INTO Location (LocationId, BookNumber, ChapterNumber, KeySymbol) VALUES
    (1, 1, 1, 'nwt'), (2, 1, 2, 'nwt'), (3, 43, 3, 'nwt'), (4, NULL, NULL, 'w23')`);
  db.run(`INSERT INTO UserMark (UserMarkId, ColorIndex, LocationId, UserMarkGuid, Version) VALUES
    (1, 2, 1, 'g1', 1), (2, 3, 1, 'g2', 1), (3, 1, 3, 'g3', 1)`);
  db.run(`INSERT INTO Note (NoteId, Guid, UserMarkId, LocationId, Title, Content, Created) VALUES
    (10, 'n10', 1, 1, 'In the beginning', 'A note on creation.', '2024-01-15 10:00:00'),
    (11, 'n11', NULL, 2, 'Second note', 'On Genesis two.', '2024-02-20 12:00:00'),
    (12, 'n12', NULL, 4, 'Article note', 'Not Bible-located.', '2024-03-05 09:00:00')`);
  const lib = win.JwReading._libraryFromDb(db);
  eq(lib.notes.length, 2, 'only Bible-located notes extracted');
  eq(lib.notes[0].b + ':' + lib.notes[0].c, '1:1', 'note keyed by book:chapter');
  eq(lib.hls['1:1'], 2, 'highlight count per chapter (Genesis 1 has 2)');
  eq(lib.hls['43:3'], 1, 'highlight count per chapter (John 3 has 1)');
  const dbBytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', dbBytes);
  zip.file('manifest.json', JSON.stringify({ version: 1 }));
  const jwlibBytes = await zip.generateAsync({ type: 'arraybuffer' });

  // Fresh window: plan active, backup available → notes render under today's rows
  const w2 = freshWindow();
  w2.win.localStorage.setItem('jwsync_reading_v1', JSON.stringify({ plan: 'canonical', days: 365, start: '2026-01-01', daysDone: 0, read: {}, log: {}, cele: {} }));
  w2.win.JSZip = JSZip;
  w2.win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  w2.win.__jwLastFile = jwlibBytes;
  w2.win.JwReading.open();
  if (w2.doc.querySelector('.jr-overlay')) ok('overlay opens');
  else fail('overlay did not open');
  await waitFor(() => w2.doc.querySelector('.jr-note'), 'own notes to render under today\'s chapters');
  const noteCards = w2.doc.querySelectorAll('.jr-note');
  if (noteCards.length === 2 && w2.doc.querySelector('.jr-note-ref').textContent === 'Genesis 1')
    ok('both Genesis notes render with chapter refs');
  else fail('expected 2 note cards for Genesis 1–3 portion, got ' + noteCards.length);
  if (w2.doc.body.textContent.includes('2 highlighted')) ok('highlight badge shows on the chapter row');
  else fail('highlight badge missing');
  w2.win.JwReading.close();
  if (!w2.doc.querySelector('.jr-overlay')) ok('overlay closes');
  else fail('overlay did not close');

  // The card went live on production in v2.98.0, so both landing pages carry it.
  for (const page of ['beta/index.html', 'index.html']) {
    section(page + ' wiring');
    const html = fs.readFileSync(REPO + '/' + page, 'utf8');
    if (html.includes('<script src="js/reading.js"></script>')) ok('reading.js script tag present');
    else fail('reading.js script tag missing');
    if (html.includes('class="svc-card svc-reading"') && html.includes('id="jw-reading-live"'))
      ok('Reading Companion tool card present with live-state hook');
    else fail('tool card / live hook missing');
    if (html.includes('window.JwReading&amp;&amp;window.JwReading.open()')) ok('card opens JwReading');
    else fail('card onclick missing');
    const lm2 = html.match(/window\.__JW_LANDING_I18N = (\{.*?\});\n/s);
    let landing = null;
    try { landing = JSON.parse(lm2[1]); } catch (_) {}
    if (!landing) fail('__JW_LANDING_I18N no longer parses as JSON');
    else {
      const missing = LANGS.filter(l => !landing[l] || !landing[l].svc_reading_t || !landing[l].svc_reading_d ||
        !landing[l].svc_reading_g1 || !landing[l].svc_reading_g2);
      if (missing.length === 0) ok('svc_reading_* present in all 12 landing languages');
      else fail('landing reading keys missing for: ' + missing.join(','));
    }
  }
  if (fs.readFileSync(REPO + '/js/reading.js', 'utf8') === fs.readFileSync(REPO + '/beta/js/reading.js', 'utf8'))
    ok('js/reading.js twins identical');
  else fail('js/reading.js and beta/js/reading.js differ');

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll Reading Companion checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error(e); process.exit(1); });

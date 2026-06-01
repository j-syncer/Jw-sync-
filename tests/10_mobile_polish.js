// Integration test for the v2.24.0 Mobile UX Polish:
//   • Offline indicator banner (self-contained module, online/offline events)
//   • Global haptic helper window.__jwHaptic (navigator.vibrate, guarded)
//   • Browse: horizontal swipe switches tabs (Notes ↔ Highlights ↔ Bookmarks)
//
// JSDOM has no real connectivity or vibrate API, so we drive navigator.onLine
// and dispatch online/offline + touch events manually.
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

const LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl'];

function extractOffline() {
  const html = fs.readFileSync(HTML_PATH, 'utf8');
  const m = html.match(/<!-- ── Offline indicator \+ haptics \(v2\.24\.0\)[\s\S]*?<!-- ── End Offline indicator \+ haptics ─[─]*\s*-->/);
  if (!m) { fail('Offline module block not found'); process.exit(1); }
  return m[0];
}

(async function run() {

  section('Offline banner module');
  {
    const mod = extractOffline();
    const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${mod}</body></html>`;
    const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
    const win = dom.window, doc = win.document;
    win.localStorage.setItem('jwsync_lang', 'en');
    win.requestAnimationFrame = (cb) => setTimeout(cb, 0);

    // haptic helper present + safe without navigator.vibrate
    if (typeof win.__jwHaptic === 'function') ok('window.__jwHaptic exposed');
    else fail('haptic helper missing');
    let threw = false;
    try { win.__jwHaptic(20); } catch (_) { threw = true; }
    if (!threw) ok('haptic is a no-op safe call when vibrate is unavailable');
    else fail('haptic threw without navigator.vibrate');

    // Force offline → banner shows
    Object.defineProperty(win.navigator, 'onLine', { value: false, configurable: true });
    win.dispatchEvent(new win.Event('offline'));
    await wait(30);
    const bar = doc.getElementById('jw-offline-banner');
    if (bar && bar.classList.contains('show')) ok('offline banner shown when navigator.onLine=false');
    else fail('offline banner not shown when offline');
    if (bar && /offline/i.test(bar.textContent)) ok('banner shows an offline message');
    else fail('banner message missing');

    // Back online → banner hides
    Object.defineProperty(win.navigator, 'onLine', { value: true, configurable: true });
    win.dispatchEvent(new win.Event('online'));
    await wait(30);
    if (bar && !bar.classList.contains('show')) ok('banner hidden again when back online');
    else fail('banner did not hide when online');
    dom.window.close();
  }

  section('Offline message localized in all 10 languages (static)');
  {
    const mod = extractOffline();
    const m = mod.match(/var I18N=\{([\s\S]*?)\};/);
    if (!m) { fail('offline I18N not found'); }
    else {
      let missing = LANGS.filter(l => !new RegExp('\\b' + l + ':"').test(mod));
      if (missing.length === 0) ok('all 10 language strings present');
      else fail('missing offline langs: ' + missing.join(','));
    }
  }

  section('Browse swipe switches tabs (v2.24.0)');
  {
    const JSZip = require('jszip');
    const initSqlJs = require('sql.js');
    const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });

    // Minimal .jwlibrary with a couple notes + one bookmark so all tabs exist.
    const db = new SQL.Database();
    db.run(`CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER, Title TEXT, Content TEXT, LastModified TEXT);
            CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER, StyleIndex INTEGER, UserMarkGuid TEXT, Version INTEGER);
            CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER, KeySymbol TEXT, Title TEXT, MepsLanguage INTEGER, Type INTEGER, IssueTagNumber INTEGER, DocumentId INTEGER);
            CREATE TABLE Bookmark (BookmarkId INTEGER PRIMARY KEY, LocationId INTEGER, PublicationLocationId INTEGER, Slot INTEGER, Title TEXT, Snippet TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
            CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER, Name TEXT);
            CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, NoteId INTEGER, LocationId INTEGER, PlaylistItemId INTEGER, TagId INTEGER, Position INTEGER);`);
    db.run(`INSERT INTO Location (LocationId, KeySymbol, Title) VALUES (1,'nwt','Genesis'),(2,'w23','Watchtower');`);
    db.run(`INSERT INTO Note (NoteId, Guid, UserMarkId, LocationId, Title, Content, LastModified) VALUES
      (1,'g1',NULL,1,'Note one','Body one','2024-01-01 00:00:00'),
      (2,'g2',NULL,2,'Note two','Body two','2024-02-01 00:00:00');`);
    db.run(`INSERT INTO Bookmark (BookmarkId, LocationId, PublicationLocationId, Slot, Title, Snippet) VALUES (1,1,1,0,'BM','snip');`);
    const dbBytes = db.export(); db.close();
    const zip = new JSZip(); zip.file('userData.db', dbBytes);
    const jwlibBytes = await zip.generateAsync({ type: 'nodebuffer' });

    const html = fs.readFileSync(HTML_PATH, 'utf8');
    const mm = html.match(/<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<!-- ── End Note Explorer ─[─]*\s*-->/);
    const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${mm[0]}</body></html>`;
    const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
    const win = dom.window, doc = win.document;
    win.JSZip = JSZip;
    win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
    win.matchMedia = (q) => ({ matches: false, media: q, addListener(){}, removeListener(){} });
    win.localStorage.setItem('jwsync_lang', 'en');
    win.__bootBrowse();
    win.__openJwBrowse(jwlibBytes);

    async function waitFor(pred, label, ms = 8000) {
      const start = Date.now();
      while (Date.now() - start < ms) { try { if (pred()) return true; } catch (_) {} await wait(40); }
      fail('timeout: ' + label); return false;
    }
    await waitFor(() => doc.querySelector('.jb-body .jb-list'), 'browse to render');

    function activeTab() { const a = doc.querySelector('.jb-tab.active'); return a && a.dataset.type; }
    if (activeTab() === 'notes') ok('starts on Notes tab');
    else fail('did not start on Notes tab: ' + activeTab());

    // Swipe left on the body → next tab (Highlights)
    const body = doc.querySelector('.jb-body');
    function touch(el, type, x, y) {
      const t = { clientX: x, clientY: y };
      const ev = new win.Event(type, { bubbles: true });
      ev.touches = type === 'touchstart' ? [t] : [];
      ev.changedTouches = [t];
      el.dispatchEvent(ev);
    }
    touch(body, 'touchstart', 250, 100);
    touch(body, 'touchend', 150, 108); // dx = -100 → swipe left → next
    await waitFor(() => activeTab() === 'highlights', 'swipe-left to Highlights');
    if (activeTab() === 'highlights') ok('swipe left → Highlights tab');
    else fail('swipe left did not switch to Highlights: ' + activeTab());

    // Swipe right → back to Notes
    touch(body, 'touchstart', 150, 100);
    touch(body, 'touchend', 260, 95); // dx = +110 → swipe right → prev
    await waitFor(() => activeTab() === 'notes', 'swipe-right to Notes');
    if (activeTab() === 'notes') ok('swipe right → Notes tab');
    else fail('swipe right did not switch back to Notes: ' + activeTab());

    // A mostly-vertical drag must NOT switch tabs
    const before = activeTab();
    touch(body, 'touchstart', 200, 100);
    touch(body, 'touchend', 230, 260); // dx=30, dy=160 → vertical, ignored
    await wait(60);
    if (activeTab() === before) ok('vertical drag does not switch tabs');
    else fail('vertical drag wrongly switched tabs');
    dom.window.close();
  }

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll mobile-polish checks passed.');
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

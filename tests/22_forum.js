// 22_forum.js — does the community forum actually speak the reader's language?
//
// The forum ships from two surfaces: forum.html (standalone) and the #forum
// route embedded in both index.html files. build_forum_i18n.py translated one
// half of each — it put the dictionary in forum.html and the FT() calls in
// js/forum.js — so neither surface worked:
//
//   * on jwsync.org/#forum, window.__forumT did not exist, FT() returned its
//     own argument, and the page rendered the literal strings "cat_feature",
//     "ago_h" and "no_replies" to every reader in every language;
//   * on forum.html, the inline copy of the forum logic was never rewired, so
//     the dynamic half of the page was English in all 25 languages.
//
// Both failures render a perfectly valid page. Nothing throws, `node --check`
// passes, and the twenty-one other suites read these files as text. So this one
// boots the forum in JSDOM against a stubbed Supabase and reads what a visitor
// would actually see.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m) => { failures++; console.log('  ✗ ' + m); };
const section = (t) => console.log('\n== ' + t + ' ==');

const read = (rel) => fs.readFileSync(path.join(REPO, rel), 'utf8');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const FORUM_JS = read('js/forum.js');
const I18N_JS = read('js/forum-i18n.js');
// Falling back to {} on a failed match hid the real problem behind a
// TypeError forty lines later: a dictionary written across several lines does
// not match, and "no languages" is indistinguishable from "no file". Say what
// went wrong instead.
const DICT_MATCH = I18N_JS.match(/window\.__FORUM_I18N=(\{.*\});\s*\n\(function\(\)\{/);
if (!DICT_MATCH) {
  console.log('  ✗ could not read window.__FORUM_I18N from js/forum-i18n.js');
  console.log('      the blob must be one line of JSON ending `};` before the IIFE');
  process.exit(1);
}
const DICT = JSON.parse(DICT_MATCH[1]);
const LANGS = Object.keys(DICT);

// ── 1. every key the runtime asks for exists, in every language ─────────────

section('Dictionary covers what js/forum.js renders');

const used = [...new Set([...FORUM_JS.matchAll(/FT\('([a-z_0-9]+)'/g)].map(m => m[1]))];
if (used.length >= 20) ok(`js/forum.js reads ${used.length} keys through FT()`);
else fail(`expected js/forum.js to read >=20 keys, found ${used.length}`);

const missingEn = used.filter(k => DICT.en[k] === undefined);
if (!missingEn.length) ok('every FT() key is defined in English');
else fail('FT() keys with no English string: ' + missingEn.join(', '));

// Derived from the ?lang= allow-list rather than hard-coded: a literal here
// drifts the moment a language is added, and then the fix is to bump the
// number, which is how a guard quietly stops guarding anything.
const ALLOWED = [...(read('index.html').match(/var V=\[([^\]]*)\]/) || [, ''])[1]
  .matchAll(/'([^']+)'/g)].map(m => m[1]);
if (ALLOWED.length && LANGS.length === ALLOWED.length) {
  ok(`dictionary carries all ${ALLOWED.length} languages the site offers`);
} else {
  const absent = ALLOWED.filter(l => !LANGS.includes(l));
  fail(`dictionary carries ${LANGS.length} languages, the site offers ` +
       `${ALLOWED.length}` + (absent.length ? ' — missing: ' + absent.join(', ') : ''));
}

const enKeys = Object.keys(DICT.en);
const gaps = LANGS.filter(l => enKeys.some(k => DICT[l][k] === undefined));
if (!gaps.length) ok(`every language defines all ${enKeys.length} keys`);
else fail('languages missing keys: ' + gaps.join(', '));

// A translation that is byte-identical to English across the whole table means
// the language was added to the picker but never actually translated.
const untranslated = LANGS.filter(l => l !== 'en' &&
  enKeys.filter(k => typeof DICT[l][k] === 'string').every(k => DICT[l][k] === DICT.en[k]));
if (!untranslated.length) ok('no language is a verbatim copy of English');
else fail('untranslated tables: ' + untranslated.join(', '));

// ── 2. both surfaces load the shared dictionary ────────────────────────────

section('Every surface that loads js/forum.js also loads the dictionary');

for (const rel of ['index.html', 'beta/index.html', 'forum.html']) {
  const html = read(rel);
  const iI18n = html.indexOf('js/forum-i18n.js');
  const iForum = html.indexOf('js/forum.js');
  if (iForum < 0) { fail(`${rel} does not load js/forum.js`); continue; }
  if (iI18n < 0) { fail(`${rel} loads js/forum.js with no dictionary — FT() will render raw keys`); continue; }
  if (iI18n < iForum) ok(`${rel} loads js/forum-i18n.js before js/forum.js`);
  else fail(`${rel} loads the dictionary after js/forum.js`);
}

// The duplicate implementation forum.html used to carry is what drifted out of
// translation in the first place. One copy, or this suite proves nothing.
const forumHtml = read('forum.html');
if (!/const\s+catLabel\s*=/.test(forumHtml)) ok('forum.html has no second copy of the forum logic');
else fail('forum.html carries an inline forum implementation again');
if (!forumHtml.includes('window.__FORUM_I18N=')) ok('forum.html has no second copy of the dictionary');
else fail('forum.html embeds the dictionary again — it will drift from js/forum-i18n.js');

// ── 3. boot each surface and read the page ─────────────────────────────────

// js/forum.js awaits chains like .select().order() and .update().eq(); a
// thenable that is also chainable satisfies both shapes.
function fakeDb(posts, replies) {
  return {
    from(tableName) {
      const rows = tableName === 'posts' ? posts : replies;
      const chain = {
        select: () => chain, eq: () => chain, order: () => chain,
        insert: () => chain, update: () => chain,
        then: (res, rej) => Promise.resolve({ data: rows, error: null }).then(res, rej),
      };
      return chain;
    },
  };
}

const POSTS = [{
  id: 'p1', title: 'Exporting to MD', content: 'Would it be possible to have a verse?',
  author: 'purlo', category: 'feature', votes: 0, solved: false,
  created_at: new Date(Date.now() - 3 * 3600 * 1000).toISOString(),  // "3h ago"
  replies: [{ count: 0 }],
}];

function forumBody() {
  const html = read('forum.html');
  const body = html.slice(html.indexOf('<body>') + 6, html.indexOf('<script src="js/forum-i18n.js"'));
  return body;
}

function embeddedView(rel) {
  const html = read(rel);
  const start = html.indexOf('<div id="forum-view" hidden>');
  const end = html.indexOf('<!-- ── End embedded forum view');
  if (start < 0 || end < 0) return null;
  // hidden would leave offsetParent null; the route un-hides it in the app.
  return html.slice(start, end).replace('<div id="forum-view" hidden>', '<div id="forum-view">');
}

async function boot(markup, lang, hash) {
  const dom = new JSDOM(
    `<!doctype html><html lang="en"><head><meta name="description" content="x"></head><body>${markup}</body></html>`,
    { url: 'https://jwsync.org/forum' + (hash || ''), pretendToBeVisual: true });
  const { window } = dom;
  window.localStorage.setItem('jwsync_lang', lang);
  window.supabase = { createClient: () => fakeDb(POSTS, []) };
  // Both files read these as bare globals; in a Function scope they have to be
  // handed in, or `typeof supabase` resolves against Node's globals and
  // jwsyncForumInit stalls waiting for a CDN script that never loads.
  const run = (src) => new Function('window', 'document', 'navigator', 'localStorage',
    'location', 'history', 'supabase', src)
    (window, window.document, window.navigator, window.localStorage,
     window.location, window.history, window.supabase);
  run(I18N_JS);
  run(FORUM_JS);
  window.__forumApplyI18N();
  await window.jwsyncForumInit();
  await sleep(60);
  return window;
}

// Any key rendered verbatim is the bug this suite exists for.
const KEY_RE = new RegExp('\\b(' + enKeys.filter(k => /^[a-z_0-9]+$/.test(k)).join('|') + ')\\b');

const SURFACES = [
  ['forum.html', forumBody()],
  ['index.html #forum', embeddedView('index.html')],
  ['beta/index.html #forum', embeddedView('beta/index.html')],
];

(async () => {
  for (const [label, markup] of SURFACES) {
    section(label);
    if (!markup) { fail(`${label}: could not locate the forum markup`); continue; }

    let window;
    try {
      window = await boot(markup, 'en');
    } catch (e) {
      fail(`${label}: threw while booting — ${e.message}`);
      continue;
    }

    const list = window.document.getElementById('post-list');
    if (list && list.textContent.includes('Exporting to MD')) ok('renders the post list');
    else { fail(`${label}: post list did not render (${list && list.textContent.trim().slice(0, 80)})`); continue; }

    const text = window.document.getElementById('forum-view')
      ? window.document.getElementById('forum-view').textContent
      : window.document.body.textContent;
    const leaked = text.match(KEY_RE);
    if (!leaked) ok('no untranslated i18n key rendered to the page');
    else fail(`${label}: rendered the raw key "${leaked[1]}" — the dictionary is not reaching FT()`);

    if (/3h ago/.test(text)) ok('relative dates render through the dictionary');
    else fail(`${label}: expected "3h ago" in the post meta`);
    if (/Feature/.test(text)) ok('category badge renders its label');
    else fail(`${label}: category badge did not render`);
    if (/No replies yet/.test(text) || /0 replies/.test(text)) ok('reply count renders');
    else fail(`${label}: reply count did not render`);

    // Spanish — the whole point of the dictionary.
    const es = await boot(markup, 'es');
    const esText = (es.document.getElementById('forum-view') || es.document.body).textContent;
    if (esText.includes(DICT.es.cat_feature)) ok('Spanish category badge translated');
    else fail(`${label}: category badge not translated into Spanish`);
    if (/hace 3\s?h/.test(esText)) ok('Spanish relative date rendered');
    else fail(`${label}: Spanish relative date missing`);
    if (esText.includes('Publicaciones') || esText.includes('publicaciones')) ok('Spanish static markup translated');
    else fail(`${label}: static markup not translated into Spanish (data-i18n tags missing?)`);
  }

  // ── 4. old shared links keep working ─────────────────────────────────────
  section('Legacy #post/<id> deep links');
  const win = await boot(forumBody(), 'en', '#post/p1');
  await sleep(60);
  if (win.location.hash === '#forum/post/p1') ok('rewritten to the canonical #forum/post/<id> route');
  else fail(`legacy hash left as "${win.location.hash}"`);
  const overlay = win.document.getElementById('overlay');
  if (overlay && overlay.classList.contains('open')) ok('opens the thread it points at');
  else fail('legacy deep link did not open the thread');

  console.log(failures ? `\n${failures} failure(s)` : '\nAll forum checks passed');
  process.exit(failures ? 1 : 0);
})();

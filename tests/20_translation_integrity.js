// 20_translation_integrity.js — the shipped words, in every language.
//
// The other suites check that a language is *present*: keys covered, guides
// counted, pages written, clusters reciprocal. None of them reads what the
// strings actually say. That gap is where this codebase's most expensive bugs
// have lived, because they produce fluent, plausible, wrong pages that no
// build, test or page load objects to:
//
//   · a Cyrillic "материал" reached a Cantonese paragraph and reads as an
//     ordinary word at a glance. build_lang_guides.py grew a STRAY guard for
//     it — but that runs only for the five languages generated through it, so
//     the other eighteen were never checked at all.
//   · a translation that silently falls back to English still renders a valid
//     page, so a missing field looks like a working page in the wrong language.
//
// Both checks below run over every language, in the guides and in the UI
// dictionaries. They passed on all 24 languages when written; they exist so
// that stays true.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m, d) => { failures++; console.log('  ✗ ' + m + (d ? '\n      ' + d : '')); };
const section = (t) => console.log('\n== ' + t + ' ==');

// Scripts a language's prose may legitimately contain, beyond Latin — product
// names (JW Library, .jwlibrary, jwsync.org) stay in Latin everywhere, so Latin
// is never flagged.
const BLOCKS = {
  cyrillic: /[Ѐ-ӿ]/, greek: /[Ͱ-Ͽ]/,
  hebrew: /[֐-׿]/, arabic: /[؀-ۿ]/,
  devanagari: /[ऀ-ॿ]/, thai: /[฀-๿]/,
  cjk: /[一-鿿]/, kana: /[぀-ヿ]/, hangul: /[가-힯]/,
};
const ALLOWED = {
  ru: ['cyrillic'], uk: ['cyrillic'], he: ['hebrew'], ar: ['arabic'],
  hi: ['devanagari'], ja: ['cjk', 'kana'], ko: ['hangul', 'cjk'],
  'zh-Hans': ['cjk'], 'zh-Hant': ['cjk'], 'yue-Hant': ['cjk'],
};

// Keys whose value is *meant* to repeat the English word: the awards match a
// literal English word with a SQL LIKE, so translating the quoted word would
// make the stated criterion untrue.
const KEEPS_ENGLISH = /(^|\/)(dk_kw_|ach_kw_)/;

function strayScript(lang, s) {
  const allowed = ALLOWED[lang] || [];
  for (const [name, re] of Object.entries(BLOCKS)) {
    if (allowed.includes(name)) continue;
    const m = s.match(re);
    if (m) return { name, ch: m[0] };
  }
  return null;
}

// ── guides ──────────────────────────────────────────────────────────────────
section('Guide copy: no stray scripts, no English falling through');
{
  // The guide text lives in Python modules; ask Python for it as JSON rather
  // than parsing it here, so this suite cannot drift from what actually ships.
  const dump = execFileSync('python3', ['-c', `
import json, sys
sys.path.insert(0, ${JSON.stringify(path.join(REPO, 'scripts'))})
from build_guides import GUIDES
from guides_i18n import GUIDE_TEXT
def flat(d):
    out = {}
    for f in ("title", "h1", "description"):
        if d.get(f): out[f] = d[f]
    for f in ("intro", "steps", "sections", "faq"):
        for i, it in enumerate(d.get(f, [])):
            if isinstance(it, (tuple, list)):
                out["%s[%d].0" % (f, i)] = it[0]; out["%s[%d].1" % (f, i)] = it[1]
            else:
                out["%s[%d]" % (f, i)] = it
    return out
print(json.dumps({
  "en": {g["slug"]: flat(g) for g in GUIDES},
  "tr": {l: {s: flat(t) for s, t in v.items()} for l, v in GUIDE_TEXT.items()},
}))`], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });

  const { en, tr } = JSON.parse(dump);
  let strays = 0, leaks = 0, langs = 0;
  for (const [lang, guides] of Object.entries(tr)) {
    langs++;
    for (const [slug, fields] of Object.entries(guides)) {
      for (const [label, s] of Object.entries(fields)) {
        if (typeof s !== 'string') continue;
        const bad = strayScript(lang, s);
        if (bad) {
          fail(`${lang}/${slug} ${label}: ${bad.name} ${JSON.stringify(bad.ch)}`,
               JSON.stringify(s.slice(0, 70)));
          strays++;
        }
        // Identical to English and long enough to be prose rather than a
        // product name or a number.
        if (s.length > 25 && en[slug] && en[slug][label] === s) {
          fail(`${lang}/${slug} ${label}: still English`,
               JSON.stringify(s.slice(0, 70)));
          leaks++;
        }
      }
    }
  }
  if (!strays) ok(`no stray scripts in ${langs} languages of guide copy`);
  if (!leaks) ok(`no English left in ${langs} languages of guide copy`);
}

// ── UI dictionaries ─────────────────────────────────────────────────────────
section('UI strings: no stray scripts, no English falling through');
{
  const DIR = path.join(REPO, 'scripts', 'i18n_data');
  const walk = (o, p, out) => {
    if (o && typeof o === 'object') {
      for (const [k, v] of Object.entries(o)) walk(v, p + '/' + k, out);
    } else if (typeof o === 'string') out[p] = o;
    return out;
  };
  const enFiles = fs.readdirSync(DIR).filter(f => f.endsWith('.en.json'));
  let strays = 0, leaks = 0, tables = 0;
  for (const enFile of enFiles) {
    const base = enFile.slice(0, -'.en.json'.length);
    const en = walk(JSON.parse(fs.readFileSync(path.join(DIR, enFile), 'utf8')), '', {});
    for (const f of fs.readdirSync(DIR)) {
      if (!f.startsWith(base + '.') || !f.endsWith('.json') || f === enFile) continue;
      const lang = f.slice(base.length + 1, -'.json'.length);
      if (lang === 'en' || lang.includes('.')) continue;
      tables++;
      const tr = walk(JSON.parse(fs.readFileSync(path.join(DIR, f), 'utf8')), '', {});
      for (const [k, s] of Object.entries(tr)) {
        if (KEEPS_ENGLISH.test(k)) continue;
        const bad = strayScript(lang, s);
        if (bad) {
          fail(`${lang} ${base}${k}: ${bad.name} ${JSON.stringify(bad.ch)}`,
               JSON.stringify(s.slice(0, 60)));
          strays++;
        }
        if (s.length > 25 && en[k] === s) {
          fail(`${lang} ${base}${k}: still English`, JSON.stringify(s.slice(0, 60)));
          leaks++;
        }
      }
    }
  }
  if (!strays) ok(`no stray scripts across ${tables} translated UI tables`);
  if (!leaks) ok(`no English left across ${tables} translated UI tables`);
}

// ── the SEO cluster, on every page rather than just the landing pages ───────
// 19_landing_pages.js checks the landing pages. The guide tree is ~900 more
// pages built by the same code, and nothing looked at them.
section('Every page: self-canonical, reciprocal hreflang');
{
  const SITE = 'https://jwsync.org';
  const skip = new Set(['.git', 'node_modules', 'tests', 'scripts', 'js', 'beta']);
  const pages = [];
  (function walkDir(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (e.isDirectory()) { if (!skip.has(e.name)) walkDir(path.join(dir, e.name)); }
      else if (e.name.endsWith('.html')) pages.push(path.relative(REPO, path.join(dir, e.name)));
    }
  })(REPO);

  const urlOf = (p) => p === 'index.html' ? SITE + '/'
    : p.endsWith('/index.html') ? SITE + '/' + p.slice(0, -'index.html'.length)
    : SITE + '/' + p.slice(0, -'.html'.length);
  const trim = (u) => u.replace(/\/$/, '');

  const info = new Map(), byUrl = new Map();
  for (const p of pages) {
    const html = fs.readFileSync(path.join(REPO, p), 'utf8');
    const head = html.split('</head>')[0];
    const can = head.match(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/);
    const alts = [...head.matchAll(/<link[^>]+hreflang="([^"]+)"[^>]+href="([^"]+)"/g)]
      .map(m => [m[1], m[2]]);
    info.set(p, { can: can && can[1], alts });
    byUrl.set(trim(urlOf(p)), p);
  }

  let badCanon = 0, badRecip = 0, clustered = 0;
  for (const [p, { can, alts }] of info) {
    if (can && trim(can) !== trim(urlOf(p))) {
      fail(`${p}: canonical is ${can}, expected ${urlOf(p)}`); badCanon++;
    }
    if (!alts.length) continue;
    clustered++;
    for (const [h, u] of alts) {
      if (h === 'x-default') continue;
      const other = byUrl.get(trim(u));
      if (!other) { fail(`${p}: hreflang ${h} points at ${u}, which is not built`); badRecip++; continue; }
      const back = info.get(other).alts.some(([, v]) => trim(v) === trim(urlOf(p)));
      if (!back) { fail(`${p}: lists ${other}, which does not list it back`); badRecip++; }
    }
  }
  if (!badCanon) ok(`all ${info.size} pages are self-canonical`);
  if (!badRecip) ok(`all ${clustered} clustered pages have reciprocal hreflang`);
}

section('SUMMARY');
if (failures === 0) { console.log('\nAll translation-integrity checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

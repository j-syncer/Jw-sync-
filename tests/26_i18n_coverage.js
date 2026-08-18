#!/usr/bin/env node
/**
 * 26_i18n_coverage.js — every dictionary carries every language, key for key.
 *
 * `scripts/i18n_check.py` has been able to prove this since it was written.
 * Nothing ran it for more than one language: 18_arabic_rtl.js drove it for
 * `ar`, and that was the whole of its coverage in CI. So the check passed, and
 * meanwhile:
 *
 *   - the 79-key Awards cabinet on Study Stats ("Distinguished Honors", the 26
 *     award names and all 52 criteria lines) was missing from the eleven oldest
 *     languages — es pt fr de it ru ja ko tl sv ceb, between them most of the
 *     site's readers. Every one of those strings fell back to English on a page
 *     that was otherwise fully translated.
 *   - share.html had no `ceb` table at all, so the entire note-sharing page was
 *     English for Cebuano.
 *
 * Neither failed a build, a test or a page load, because the lookup helper ends
 * `: (I18N.en[k] != null ? I18N.en[k] : k)`. A missing key renders as English
 * text, which looks like a translation choice rather than a bug.
 *
 * The language list is read from the shipped `?lang=` allow-list rather than
 * written here. A literal would drift the moment a language is added, and the
 * quickest way back to green would be to bump it — which is how a guard stops
 * guarding anything.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const REPO = path.join(__dirname, '..');

let pass = 0, failCount = 0;
function section(t) { console.log('\n== ' + t + ' =='); }
function ok(n) { pass++; console.log('  ✓ ' + n); }
function fail(n, d) { failCount++; console.log('  ✗ ' + n); if (d) console.log('      ' + d); }

// ── The languages the site actually offers ────────────────────────────────
const idx = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8');
const allow = idx.slice(0, idx.indexOf('</head>')).match(/var V=\[([^\]]*)\]/);
if (!allow) {
  console.log('  ✗ could not read the ?lang= allow-list from index.html');
  process.exit(1);
}
const LANGS = [...allow[1].matchAll(/['"]([A-Za-z-]+)['"]/g)].map((m) => m[1]);

section('Every UI dictionary carries every offered language');
console.log('  (' + LANGS.length + ' languages from the ?lang= allow-list)');

let tablesSeen = 0;
for (const lang of LANGS) {
  let report;
  try {
    report = execFileSync('python3',
      [path.join(REPO, 'scripts', 'i18n_check.py'), lang], { encoding: 'utf8' });
  } catch (e) {
    report = (e.stdout || '') + (e.stderr || '');
  }
  const lines = report.trim().split('\n').filter(Boolean);
  const bad = lines.filter((l) => l.startsWith('FAIL '));
  const good = lines.filter((l) => l.startsWith('OK ')).length;
  if (good === 0) {
    fail(lang + ': i18n_check.py produced no results', report.slice(0, 300));
    continue;
  }
  if (bad.length) {
    for (const b of bad) fail(lang + ': ' + b.slice(5));
    continue;
  }
  if (tablesSeen && good !== tablesSeen) {
    fail(lang + ': sees ' + good + ' dictionaries, other languages see ' + tablesSeen,
      'a language that finds fewer tables is anchored in the wrong place');
    continue;
  }
  tablesSeen = good;
  ok(lang + ': all ' + good + ' dictionaries complete');
}

// ── English is the fallback, so it has to be the superset ─────────────────
// Every lookup ends in I18N.en[k]. A key that exists only in a translation is
// therefore unreachable from English and, more usefully, is a sign the key was
// added to one table by hand instead of through the toolchain.
section('No translation carries a key English lacks');
{
  const script = `
import io, json, os, sys
sys.path.insert(0, os.path.join(${JSON.stringify(REPO)}, 'scripts'))
import i18n_tool as t
langs = json.loads(sys.argv[1])
extra = []
for f in t.FILES:
    p = os.path.join(t.REPO, f)
    if not os.path.exists(p):
        continue
    text = io.open(p, encoding='utf-8').read()
    for n, s in enumerate(t.dict_sites(text)):
        en_src, _ = t.read_lang(text, s, 'en')
        if en_src is None:
            continue
        en = t.js_to_obj(en_src)
        for lang in langs:
            src, _ = t.read_lang(text, s, lang)
            if src is None:
                continue
            for k in t.js_to_obj(src):
                if k not in en:
                    extra.append('%s[%d] %s: %s' % (f, n, lang, k))
print(json.dumps(extra))
`;
  let out;
  try {
    out = execFileSync('python3', ['-c', script, JSON.stringify(LANGS)],
      { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  } catch (e) {
    fail('could not scan for orphan keys', ((e.stderr || '') + '').slice(0, 300));
    out = null;
  }
  if (out !== null) {
    const extra = JSON.parse(out.trim().split('\n').pop());
    if (extra.length) fail(extra.length + ' key(s) exist only in a translation', extra.slice(0, 8).join('; '));
    else ok('English is a superset of every translation');
  }
}

// ── The inline defaults are the English page ──────────────────────────────
// Each `data-i18n="k"` element ships fallback text in the markup. The runtime
// overwrites it from the dictionary — including for English — so a stale
// default still *renders* correctly and looks fine in a browser. But it is what
// the served HTML says, which is what a crawler indexes and what paints before
// the script runs, and the pre-rendered /<lang>/ landing pages are built from
// the dictionary instead. So drift here means every translation shows the new
// copy while English alone serves the old.
//
// That is not hypothetical. When the site's positioning was corrected — from
// "recover a lost phone" to the divergence crux — the dictionary was updated
// and the markup was not, leaving all eleven of the rewritten strings stale in
// English: the hero, the merge card, the share card, the tag manager and the
// semantic-search copy. Twenty-five languages pitched the site correctly and
// the canonical English page did not.
section('data-i18n defaults match the English dictionary');
{
  const PAGES = {
    'index.html': 'index.html.0.en.json',
    'beta/index.html': 'index.html.0.en.json',
    'highlights.html': 'highlights.html.0.en.json',
    'beta/highlights.html': 'highlights.html.0.en.json',
    'share.html': 'share.html.0.en.json',
    'beta/share.html': 'share.html.0.en.json',
    'forum.html': 'forum.html.0.en.json',
  };
  const unescape = (s) => s.replace(/&amp;/g, '&').replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#x27;|&#39;/g, "'");
  for (const [page, dict] of Object.entries(PAGES)) {
    const dp = path.join(REPO, 'scripts', 'i18n_data', dict);
    if (!fs.existsSync(path.join(REPO, page)) || !fs.existsSync(dp)) continue;
    const en = JSON.parse(fs.readFileSync(dp, 'utf8'));
    const html = fs.readFileSync(path.join(REPO, page), 'utf8');
    const drift = [];
    for (const m of html.matchAll(/data-i18n="([A-Za-z0-9_]+)"[^>]*>([^<]*)</g)) {
      const [, key, raw] = m;
      const inline = unescape(raw).trim();
      // An empty default is a deliberate placeholder, not drift.
      if (!inline || !(key in en)) continue;
      if (inline !== String(en[key]).trim()) drift.push(key);
    }
    if (drift.length) {
      fail(page + ': ' + drift.length + ' default(s) stale vs the en dictionary',
        drift.slice(0, 8).join(', '));
    } else {
      ok(page + ': inline defaults match en');
    }
  }
}

// ── Two dictionaries hold the landing copy; they have to agree ────────────
// index.html.0 is the landing table, js_app.js.0 is the React app's. They
// share 18 keys. That would be harmless except for the override order: once
// js/app.js loads it calls applyLandingI18n(lang, TRANSLATIONS) with its own
// table, which becomes `cachedT` and from then on wins for every data-i18n
// element — the landing table only fills keys the app table lacks.
//
// So when the positioning was corrected, updating the landing table (and the
// markup) fixed the served HTML and the first paint, and the app bundle
// silently reverted all six rewritten strings the moment it finished loading
// — in all 26 languages, 156 strings. Whichever store you edit, the other one
// is the one the reader ends up looking at.
section('landing and app dictionaries agree on their shared keys');
{
  const dataDir = path.join(REPO, 'scripts', 'i18n_data');
  const enA = JSON.parse(fs.readFileSync(path.join(dataDir, 'index.html.0.en.json'), 'utf8'));
  const enB = JSON.parse(fs.readFileSync(path.join(dataDir, 'js_app.js.0.en.json'), 'utf8'));
  const shared = Object.keys(enA).filter((k) => k in enB);
  ok(shared.length + ' keys live in both the landing and app tables');
  let drifted = 0;
  for (const lang of LANGS) {
    const pa = path.join(dataDir, 'index.html.0.' + lang + '.json');
    const pb = path.join(dataDir, 'js_app.js.0.' + lang + '.json');
    if (!fs.existsSync(pa) || !fs.existsSync(pb)) continue;
    const a = JSON.parse(fs.readFileSync(pa, 'utf8'));
    const b = JSON.parse(fs.readFileSync(pb, 'utf8'));
    const bad = shared.filter((k) => k in a && k in b
      && String(a[k]).trim() !== String(b[k]).trim());
    if (bad.length) { fail(lang + ': ' + bad.length + ' shared key(s) differ', bad.join(', ')); drifted++; }
  }
  if (!drifted) ok('all ' + LANGS.length + ' languages agree across both tables');
}

// ── Summary ───────────────────────────────────────────────────────────────
section('SUMMARY');
if (failCount) {
  console.log(failCount + ' i18n coverage check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
}
console.log('All ' + pass + ' i18n coverage checks passed.');

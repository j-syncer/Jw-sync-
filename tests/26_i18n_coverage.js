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

// ── Summary ───────────────────────────────────────────────────────────────
section('SUMMARY');
if (failCount) {
  console.log(failCount + ' i18n coverage check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
}
console.log('All ' + pass + ' i18n coverage checks passed.');

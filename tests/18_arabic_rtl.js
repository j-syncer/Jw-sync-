#!/usr/bin/env node
/**
 * 18_arabic_rtl.js — Arabic language + right-to-left layout guard.
 *
 * Arabic is the site's first RTL language, so it exercises code paths the
 * other twelve never touch. This suite covers the four ways it can silently
 * break:
 *
 *   1. A dictionary gains a key in English but not in Arabic, so part of the
 *      UI falls back to English mid-sentence. Every one of the eighteen
 *      language tables is checked key-for-key against `en`.
 *   2. Arabic is translated but not *selectable* — the ?lang= allow-list, the
 *      nav picker or the jw.org wtlocale map is missed. (jw-session.js was
 *      exactly this: translated everywhere else, English in the tool
 *      switcher, because it was not in the extraction list.)
 *   3. `dir="rtl"` is never applied, or applied after first paint, so the page
 *      renders LTR and visibly reflows.
 *   4. rtl.css drifts from the stylesheets it mirrors, or loses the rules that
 *      cannot be derived mechanically.
 *
 * Plus the Arabic guide tree and the SEO invariants that go with it.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const REPO = path.join(__dirname, '..');
const LANG = 'ar';

let pass = 0, failCount = 0;
function section(t) { console.log('\n== ' + t + ' =='); }
function ok(n) { pass++; console.log('  ✓ ' + n); }
function fail(n, d) { failCount++; console.log('  ✗ ' + n); if (d) console.log('      ' + d); }
function read(rel) { return fs.readFileSync(path.join(REPO, rel), 'utf8'); }

// ── 1. Dictionary coverage ────────────────────────────────────────────────
// The dictionaries are JS object literals scattered across the HTML and the
// bundles. scripts/i18n_tool.py already knows how to find and read them, so
// the test drives it rather than re-implementing the search.
section('Every language dictionary carries Arabic');
{
  let report;
  try {
    report = execFileSync('python3', [
      path.join(REPO, 'scripts', 'i18n_check.py'), LANG,
    ], { encoding: 'utf8' });
  } catch (e) {
    report = (e.stdout || '') + (e.stderr || '');
  }
  const lines = report.trim().split('\n').filter(Boolean);
  let tables = 0;
  for (const line of lines) {
    if (line.startsWith('OK ')) { tables++; continue; }
    if (line.startsWith('FAIL ')) fail(line.slice(5));
  }
  if (tables > 0 && !lines.some(l => l.startsWith('FAIL'))) {
    ok(tables + ' dictionaries carry a complete "' + LANG + '" table');
  } else if (tables === 0) {
    fail('i18n_check.py produced no results', report.slice(0, 300));
  }
}

// ── 2. Arabic is selectable ───────────────────────────────────────────────
section('Arabic is wired into the language plumbing');
for (const f of ['index.html', 'beta/index.html']) {
  const c = read(f);
  const head = c.slice(0, c.indexOf('</head>'));
  if (/var V=\[[^\]]*'ar'[^\]]*\]/.test(head)) ok(f + ": ?lang=ar is in the allow-list");
  else fail(f + ': ?lang=ar not accepted (missing from the V allow-list)');
  if (c.includes('<option value="ar">')) ok(f + ': Arabic option in the nav picker');
  else fail(f + ': Arabic missing from the language picker');
}
for (const f of ['js/reading.js', 'beta/js/reading.js']) {
  // Reading Companion deep-links into jw.org; wtlocale=A is Arabic there.
  if (/ar: *'A'/.test(read(f))) ok(f + ': jw.org wtlocale mapped (ar -> A)');
  else fail(f + ': ar missing from WTLOCALE, chapter links would open in English');
}

// ── 3. Direction handling ─────────────────────────────────────────────────
section('dir="rtl" is applied before first paint and on language change');
const DIR_PAGES = ['index.html', 'beta/index.html', 'highlights.html',
  'beta/highlights.html', 'share.html', 'beta/share.html', 'forum.html'];
for (const f of DIR_PAGES) {
  const c = read(f);
  const head = c.slice(0, c.indexOf('</head>'));
  if (head.includes('id="jw-dir-init"')) ok(f + ': direction bootstrap is in <head>');
  else fail(f + ': jw-dir-init missing or below </head> (page would flash LTR)');
  if (head.includes('rtl.css')) ok(f + ': rtl.css linked');
  else fail(f + ': rtl.css not linked');
}
for (const f of ['index.html', 'beta/index.html']) {
  // applyLandingI18n is the single chokepoint every language change flows
  // through — the picker calls it directly, React calls it via the bridge.
  const c = read(f);
  if (c.includes('window.__jwApplyDir(lang)'))
    ok(f + ': language changes re-apply the direction');
  else fail(f + ': runtime language change would not update dir');
}

// ── 4. rtl.css ────────────────────────────────────────────────────────────
section('rtl.css is present, scoped and current');
{
  const rtl = read('rtl.css');
  if (rtl === read('beta/rtl.css')) ok('rtl.css matches its beta twin');
  else fail('rtl.css and beta/rtl.css have drifted');

  const rules = rtl.match(/(^|[}\n])\s*([^{}@\n][^{}]*)\{/g) || [];
  const unscoped = rules
    .map(r => r.replace(/[}\n]/g, '').replace('{', '').trim())
    .filter(s => s && !s.startsWith('/*') && !s.includes('[dir="rtl"]'));
  if (!unscoped.length) ok('every rule is scoped to [dir="rtl"] (' + rules.length + ' rules)');
  else fail(unscoped.length + ' unscoped rule(s) would affect LTR languages',
    unscoped.slice(0, 3).join(' | '));

  // Rules the generator cannot derive from the source CSS.
  const HAND = [
    ['unicode-bidi: plaintext', 'user-written note text keeps its own direction'],
    ['Noto Naskh Arabic', 'an Arabic-capable font stack'],
    ['ol.steps li::before', 'the guide step badges flip side'],
  ];
  for (const [needle, what] of HAND) {
    if (rtl.includes(needle)) ok('hand-written rule kept: ' + what);
    else fail('missing hand-written rule: ' + what + ' (' + needle + ')');
  }

  // Regenerating must be a no-op — otherwise a stylesheet changed after the
  // last build and the mirror is stale.
  const before = rtl;
  execFileSync('python3', [path.join(REPO, 'scripts', 'build_rtl.py')], { encoding: 'utf8' });
  if (read('rtl.css') === before) ok('rtl.css is up to date with the stylesheets it mirrors');
  else fail('rtl.css is stale — run scripts/build_rtl.py and commit the result');

  // A checkmark is not a directional glyph; mirroring its border-width would
  // reverse the tick. Only its position may move.
  if (/\[dir="rtl"\] \.jb-check\.jb-check-on::after\{[^}]*right:4px/.test(rtl)
      && !/\[dir="rtl"\] \.jb-check\.jb-check-on::after\{[^}]*border-width/.test(rtl))
    ok('checkmark glyph moves side but is not mirrored');
  else fail('checkmark handling wrong — the tick would be drawn backwards');
}

// ── 5. Arabic guides ──────────────────────────────────────────────────────
section('Arabic guide tree');
{
  const enFiles = fs.readdirSync(path.join(REPO, 'guides'))
    .filter(f => f.endsWith('.html'));
  const arDir = path.join(REPO, 'guides', LANG);
  if (!fs.existsSync(arDir)) {
    fail('guides/' + LANG + ' does not exist');
  } else {
    const arFiles = fs.readdirSync(arDir).filter(f => f.endsWith('.html'));
    if (arFiles.length === enFiles.length)
      ok('every English guide has an Arabic twin (' + arFiles.length + ' pages)');
    else fail('guide count mismatch: ' + enFiles.length + ' en vs ' + arFiles.length + ' ar',
      enFiles.filter(f => !arFiles.includes(f)).join(', '));

    let bad = 0, checked = 0;
    for (const f of arFiles) {
      const c = fs.readFileSync(path.join(arDir, f), 'utf8');
      checked++;
      if (!c.includes('<html lang="ar" dir="rtl">')) { fail(f + ': wrong <html> attributes'); bad++; continue; }
      if (!/<link rel="canonical" href="https:\/\/jwsync\.org\/guides\/ar\//.test(c)) {
        fail(f + ': canonical does not point at the Arabic URL'); bad++; continue;
      }
      if (!c.includes('hreflang="ar"') || !c.includes('hreflang="x-default"')) {
        fail(f + ': incomplete hreflang cluster'); bad++; continue;
      }
      const m = c.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
      if (!m) { fail(f + ': no JSON-LD'); bad++; continue; }
      let ld;
      try { ld = JSON.parse(m[1]); } catch (e) { fail(f + ': JSON-LD does not parse'); bad++; continue; }
      if (!JSON.stringify(ld).includes('"inLanguage":"ar"')) {
        fail(f + ': JSON-LD still claims inLanguage en'); bad++; continue;
      }
      // Untranslated chrome leaking through would show up as English headings.
      if (c.includes('<h2>Step by step</h2>') || c.includes('<h2>Frequently asked questions</h2>')) {
        fail(f + ': English chrome leaked into the Arabic page'); bad++; continue;
      }
    }
    if (!bad) ok('all ' + checked + ' Arabic guides: lang/dir, canonical, hreflang, JSON-LD, no English chrome');

    // A localized page whose nav or footer links `../../guides/` drops the
    // reader back into English — the link reads "Guías" and lands on the
    // English index. Every translated tree is checked, not just Arabic.
    const trees = fs.readdirSync(path.join(REPO, 'guides'), { withFileTypes: true })
      .filter(d => d.isDirectory()).map(d => d.name);
    let leaked = 0;
    for (const l of trees) {
      for (const f of fs.readdirSync(path.join(REPO, 'guides', l)).filter(x => x.endsWith('.html'))) {
        const c = fs.readFileSync(path.join(REPO, 'guides', l, f), 'utf8');
        const chrome = (c.match(/<nav class="hnav">[\s\S]*?<\/nav>/) || [''])[0]
          + (c.match(/<footer[\s\S]*?<\/footer>/) || [''])[0];
        if (/href="\.\.\/\.\.\/guides\/"/.test(chrome)) { fail(l + '/' + f + ': nav or footer links the English guide index'); leaked++; }
      }
    }
    if (!leaked) ok('localized guide chrome stays inside its own language (' + trees.join(', ') + ')');

    // The English pages must keep their original URLs and canonicals.
    const enGuide = read('guides/backup-jw-library.html');
    if (enGuide.includes('<link rel="canonical" href="https://jwsync.org/guides/backup-jw-library">'))
      ok('English guide URLs and canonicals unchanged');
    else fail('English guide canonical changed — existing rankings would be lost');
  }
}

// ── 6. SEO invariants ─────────────────────────────────────────────────────
section('SEO: Arabic advertised only where it is really served');
{
  const sm = read('sitemap.xml');
  const locs = (sm.match(/<loc>([^<]+)<\/loc>/g) || []).map(s => s.slice(5, -6));

  const arGuides = locs.filter(u => u.includes('/guides/ar/'));
  if (arGuides.length >= 37) ok('sitemap lists the Arabic guides (' + arGuides.length + ')');
  else fail('sitemap is missing Arabic guides (found ' + arGuides.length + ')');

  // The app shell is one document with client-side i18n; ?lang= URLs
  // canonicalise back to it, so they must not be submitted or hreflang'd.
  // 01_static.js guards the general case; this is the Arabic-specific one.
  if (!locs.some(u => u.includes('lang=ar')))
    ok('no ?lang=ar URL submitted (it canonicalises away)');
  else fail('sitemap submits ?lang=ar, which canonicalises back to the shell');

  const idx = read('index.html');
  const head = idx.slice(0, idx.indexOf('</head>'));
  if (head.includes('content="ar_SA"')) ok('og:locale:alternate advertises Arabic');
  else fail('og:locale:alternate ar_SA missing');
  if (/"inLanguage": \[[^\]]*"ar"[^\]]*\]/.test(idx)) ok('JSON-LD inLanguage includes ar');
  else fail('JSON-LD inLanguage does not list ar');

  // Localized <title>/description: present for every language, not just ar.
  const m = idx.match(/__JW_LANDING_I18N *= */);
  const ts = m.index + m[0].length;
  let d = 0, e = ts;
  for (let i = ts; i < idx.length; i++) {
    if (idx[i] === '{') d++;
    else if (idx[i] === '}') { d--; if (d === 0) { e = i + 1; break; } }
  }
  const obj = JSON.parse(idx.slice(ts, e));
  const missing = Object.keys(obj).filter(l => !obj[l].meta_title || !obj[l].meta_desc);
  if (!missing.length) ok('meta_title/meta_desc present for all ' + Object.keys(obj).length + ' languages');
  else fail('meta_title/meta_desc missing for: ' + missing.join(', '));
  if (idx.includes('document.title=mt')) ok('title/description swap on language change');
  else fail('localized title is never applied at runtime');
}

// ── Summary ───────────────────────────────────────────────────────────────
section('SUMMARY');
if (failCount) {
  console.log(failCount + ' Arabic/RTL check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
}
console.log('All ' + pass + ' Arabic/RTL checks passed.');

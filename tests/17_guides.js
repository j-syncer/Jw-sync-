/* =============================================================================
   17_guides.js — static checks for the /guides/ SEO pages (v2.93.0)

   Guards:
   - every guide page listed below exists and is well-formed
     (title, meta description, canonical, robots index, valid JSON-LD)
   - guides/index.html links every guide
   - sitemap.xml lists the guides index and every guide URL
   - both landing pages link to guides/ in the footer
   - internal "related" links only point at guides that exist
   ============================================================================= */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
// Discovered, not listed. A hardcoded roster silently stops covering the next
// guide: the 38th shipped in v3.35.0 and this suite kept passing while checking
// only the original 37 — none of its structure, JSON-LD or index linking was
// ever looked at. The floor guards the opposite failure, an empty directory
// quietly passing everything.
const SLUGS = fs.readdirSync(path.join(ROOT, 'guides'))
  .filter((f) => f.endsWith('.html') && f !== 'index.html')
  .map((f) => f.slice(0, -5))
  .sort();

let failures = 0;
const ok = (cond, label) => {
  if (cond) { console.log('  ✓ ' + label); }
  else { console.error('  ✗ ' + label); failures++; }
};

console.log('== Every language carries every guide ==');
{
  // Neither the file existing nor its title proves anything: build_guides.py
  // writes no page for a language that lacks the translation, and it does not
  // delete the previous one either — so the stale, correctly-titled file stays
  // on disk and every naive check passes. (Confirmed: removing a language's
  // entry drops the build from 975 pages to 974 with nothing else changing.)
  //
  // The English page is rebuilt every time, and its hreflang cluster lists only
  // the languages that really have the guide. That is the one thing a stale
  // file cannot fake, so it is what gets asserted here. This matters because an
  // entry spliced into guides_<lang>.py in the wrong shape lands inside another
  // guide's dict — valid Python, no error — and the language just falls back.
  const LANGS = fs.readdirSync(path.join(ROOT, 'guides'), { withFileTypes: true })
    .filter((d) => d.isDirectory()).map((d) => d.name).sort();
  ok(LANGS.length === 24, `${LANGS.length} translated guide trees (expected 24)`);

  const thin = [];
  for (const slug of SLUGS) {
    const en = fs.readFileSync(path.join(ROOT, 'guides', slug + '.html'), 'utf8');
    const listed = new Set(
      [...en.matchAll(/hreflang="([A-Za-z-]+)"\s+href="https:\/\/jwsync\.org\/guides\/([A-Za-z-]+)\//g)]
        .map((m) => m[2]));
    const absent = LANGS.filter((l) => !listed.has(l));
    if (absent.length) thin.push(`${slug}: ${absent.join(', ')}`);
  }
  ok(thin.length === 0,
     `every guide is advertised in all ${LANGS.length} languages` +
     (thin.length ? ' — not translated: ' + thin.slice(0, 4).join(' | ') : ''));
}

console.log('== Guide pages exist and are well-formed ==');
ok(SLUGS.length >= 38, `found ${SLUGS.length} guide pages (expected at least 38)`);

const pages = {};
for (const slug of SLUGS) {
  const file = path.join(ROOT, 'guides', slug + '.html');
  if (!fs.existsSync(file)) { ok(false, slug + '.html exists'); continue; }
  const c = fs.readFileSync(file, 'utf8');
  pages[slug] = c;
  const checks =
    /<title>[^<]{10,}<\/title>/.test(c) &&
    /<meta name="description" content="[^"]{50,}"/.test(c) &&
    c.includes('<link rel="canonical" href="https://jwsync.org/guides/' + slug + '">') &&
    c.includes('<meta name="robots" content="index, follow">') &&
    !/noindex/i.test(c) &&
    /<h1>[^<]+<\/h1>/.test(c) &&
    c.includes('class="steps"');
  ok(checks, slug + ': title/description/canonical/robots/h1/steps');
  const ld = c.match(/<script type="application\/ld\+json">(.*?)<\/script>/s);
  let ldOk = false;
  try {
    const parsed = JSON.parse(ld[1]);
    const types = parsed['@graph'].map((n) => n['@type']);
    ldOk = types.includes('Article') && types.includes('HowTo') &&
           types.includes('BreadcrumbList');
  } catch (e) { /* ldOk stays false */ }
  ok(ldOk, slug + ': JSON-LD parses with Article + HowTo + BreadcrumbList');
}

console.log('== Guides index ==');
const idxFile = path.join(ROOT, 'guides', 'index.html');
ok(fs.existsSync(idxFile), 'guides/index.html exists');
if (fs.existsSync(idxFile)) {
  const idx = fs.readFileSync(idxFile, 'utf8');
  ok(idx.includes('<link rel="canonical" href="https://jwsync.org/guides/">'),
     'index canonical is /guides/');
  ok(!/noindex/i.test(idx), 'index is indexable');
  let missing = SLUGS.filter((s) => !idx.includes('href="' + s + '"'));
  ok(missing.length === 0, 'index links every guide' +
     (missing.length ? ' (missing: ' + missing.join(', ') + ')' : ''));
}

console.log('== Internal related links resolve ==');
for (const [slug, c] of Object.entries(pages)) {
  const rel = [...c.matchAll(/class="related">([\s\S]*?)<\/ul>/g)]
    .flatMap((m) => [...m[1].matchAll(/href="([^"]+)"/g)].map((x) => x[1]));
  const bad = rel.filter((r) => !SLUGS.includes(r));
  ok(bad.length === 0, slug + ': related links resolve' +
     (bad.length ? ' (bad: ' + bad.join(', ') + ')' : ''));
}

console.log('== Text contrast (WCAG AA, 4.5:1) ==');
{
  const relLum = (hex) => {
    const h = hex.replace('#', '');
    const ch = (s) => {
      const v = parseInt(s, 16) / 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    };
    return 0.2126 * ch(h.slice(0, 2)) + 0.7152 * ch(h.slice(2, 4)) + 0.0722 * ch(h.slice(4, 6));
  };
  const contrast = (a, b) => {
    const la = relLum(a), lb = relLum(b);
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
  };
  const page = pages[SLUGS[0]] || '';
  const v = (name) => {
    const m = page.match(new RegExp('--' + name + ':(#[0-9a-f]{6})', 'i'));
    return m && m[1];
  };
  const bg = v('bg'), muted = v('muted'), soft = v('accent-soft'), strong = v('accent-strong');
  const footer = (page.match(/footer\.site\{[^}]*color:(#[0-9a-f]{6})/i) || [])[1];
  const pairs = [
    ['#ffffff', strong, 'CTA button label on the button'],
    [muted, bg, 'muted body text on the page'],
    [soft, bg, 'links on the page'],
    [footer, bg, 'footer text on the page'],
  ];
  for (const [fg, back, label] of pairs) {
    if (!fg || !back) { ok(false, label + ': colour not found in the generated CSS'); continue; }
    const r = contrast(fg, back);
    ok(r >= 4.5, label + ': ' + r.toFixed(2) + ':1' + (r >= 4.5 ? '' : ' — below AA'));
  }
  // the step numerals sit on a solid fill too, so they need the same shade
  ok(/background:var\(--accent-strong\);color:#fff;font-weight:700;font-size:15px/.test(page),
     'numbered step markers use the AA-contrast accent');
}

console.log('== Sitemap coverage ==');
const sm = fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8');
ok(sm.includes('<loc>https://jwsync.org/guides/</loc>'), 'sitemap lists guides index');
{
  const missing = SLUGS.filter(
    (s) => !sm.includes('<loc>https://jwsync.org/guides/' + s + '</loc>'));
  ok(missing.length === 0, 'sitemap lists every guide' +
     (missing.length ? ' (missing: ' + missing.join(', ') + ')' : ''));
}

console.log('== Landing pages link to guides ==');
// Production sits at / so a relative "guides/" resolves; beta sits at /beta/,
// where a relative link would 404 — it must use the absolute /guides/ path.
ok(fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8').includes('href="guides/"'),
   'index.html links to guides/');
{
  const c = fs.readFileSync(path.join(ROOT, 'beta/index.html'), 'utf8');
  ok(c.includes('href="/guides/"') && !/href="guides\/"/.test(c),
     'beta/index.html links to /guides/ (absolute — /beta/guides/ does not exist)');
}

console.log('\n== SUMMARY ==\n');
if (failures) {
  console.error(failures + ' guide check(s) FAILED');
  process.exit(1);
}
console.log('All guide checks passed.');

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
const SLUGS = [
  'merge-jw-library-backups',
  'sync-jw-library-multiple-devices',
  'transfer-jw-library-notes-new-phone',
  'jw-library-android-to-iphone',
  'backup-jw-library',
  'jw-library-restore-replaced-notes',
  'fix-corrupted-jw-library-backup',
  'edit-jw-library-notes',
  'search-jw-library-notes',
  'jw-library-study-stats',
  'share-jw-library-notes',
  'bible-reading-plan',
];

let failures = 0;
const ok = (cond, label) => {
  if (cond) { console.log('  ✓ ' + label); }
  else { console.error('  ✗ ' + label); failures++; }
};

console.log('== Guide pages exist and are well-formed ==');
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
for (const f of ['index.html', 'beta/index.html']) {
  const c = fs.readFileSync(path.join(ROOT, f), 'utf8');
  ok(c.includes('href="guides/"'), f + ' links to guides/');
}

console.log('\n== SUMMARY ==\n');
if (failures) {
  console.error(failures + ' guide check(s) FAILED');
  process.exit(1);
}
console.log('All guide checks passed.');

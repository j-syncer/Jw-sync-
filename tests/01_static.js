const path = require('path');
const REPO = path.join(__dirname, '..');
// Static checks: parse-ability, anchor presence, i18n completeness, CSS classes used == defined.
const fs = require('fs');

const FILES = [
  REPO + '/beta/index.html',
  REPO + '/index.html',
];

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

const EXPECTED_LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl'];
const REQUIRED_I18N_KEYS = ['brw_open']; // in the main TRANSLATIONS object

const BROWSE_REQUIRED_KEYS = [
  'title','search','no_results','loading','close','no_file','pick_file',
  'count_one','count_many','color_all','no_title','copy','copied','clear',
  'error','pub_all','tag_all','back','detail_empty','sort_newest',
  'sort_oldest','sort_pub','modified','no_content','too_many',
  'tab_notes','tab_highlights','tab_bookmarks','hl_label','hl_no_text',
  'hl_with_note','bm_label','bm_slot','linked_note'
];

for (const path of FILES) {
  section(path);
  const c = fs.readFileSync(path, 'utf8');

  // 1) Main React script parses
  const ti = c.indexOf('TRANSLATIONS=');
  const ss = c.lastIndexOf('<script', ti);
  const so = c.indexOf('>', ss) + 1;
  const se = c.indexOf('</script>', so);
  try {
    new Function(c.slice(so, se));
    ok('main app <script> parses');
  } catch (e) { fail('main app parse failed: ' + e.message); }

  // 2) Browse module parses
  const m = c.match(/<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<\/script>\s*<!-- ── End Note Explorer/);
  if (!m) { fail('Browse block missing'); continue; }
  const sm = m[0].match(/<script>([\s\S]*?)<\/script>/);
  let browseSrc;
  try {
    browseSrc = sm[1];
    new Function(browseSrc);
    ok('Browse module <script> parses (' + browseSrc.length + ' bytes)');
  } catch (e) { fail('Browse parse failed: ' + e.message); continue; }

  // 3) TRANSLATIONS object parses and has all langs + required keys
  let d = 0, e2 = ti + 13;
  for (let i = ti + 13; i < c.length; i++) {
    if (c[i] === '{') d++;
    else if (c[i] === '}') { d--; if (d === 0) { e2 = i + 1; break; } }
  }
  let trans;
  try {
    trans = eval('(' + c.slice(ti + 13, e2) + ')');
    ok('TRANSLATIONS parses');
  } catch (e) { fail('TRANSLATIONS parse failed: ' + e.message); continue; }

  for (const lang of EXPECTED_LANGS) {
    if (!trans[lang]) { fail('missing language: ' + lang); continue; }
    for (const key of REQUIRED_I18N_KEYS) {
      if (!trans[lang][key]) fail(`${lang}.${key} missing`);
    }
  }
  if (Object.keys(trans).length === EXPECTED_LANGS.length) ok('TRANSLATIONS has exactly 10 languages');

  // 4) Browse I18N object parses + every lang has every required key
  const i18nMatch = browseSrc.match(/var I18N = (\{[\s\S]*?\});\s*function curLang/);
  if (!i18nMatch) { fail('Browse I18N object not found'); continue; }
  let browseI18n;
  try {
    browseI18n = eval('(' + i18nMatch[1] + ')');
    ok('Browse I18N parses');
  } catch (e) { fail('Browse I18N parse failed: ' + e.message); continue; }

  for (const lang of EXPECTED_LANGS) {
    if (!browseI18n[lang]) { fail('Browse I18N missing ' + lang); continue; }
    let missing = BROWSE_REQUIRED_KEYS.filter(k => !browseI18n[lang][k]);
    if (missing.length) fail(`${lang} missing keys: ${missing.join(',')}`);
  }
  ok('Browse I18N: 10 langs each cover ' + BROWSE_REQUIRED_KEYS.length + ' keys');

  // 5) Critical CSS classes referenced in module code exist in <style>
  const styleMatch = m[0].match(/<style>([\s\S]*?)<\/style>/);
  if (!styleMatch) { fail('Browse <style> block missing'); continue; }
  const css = styleMatch[1];
  const CRITICAL_CLASSES = [
    'jb-overlay','jb-modal','jb-head','jb-head-close','jb-tabs','jb-tab','jb-tab.active','jb-tab-count',
    'jb-toolbar','jb-search','jb-select','jb-clear','jb-colors','jb-color-dot','jb-body','jb-list','jb-detail',
    'jb-detail-empty','jb-note','jb-note-title','jb-note-color','jb-note-excerpt','jb-note-meta',
    'jb-tag','jb-pub','jb-bm-slot','jb-hl-swatch','jb-detail-title','jb-detail-color','jb-detail-meta',
    'jb-detail-pub','jb-detail-date','jb-detail-tags','jb-detail-content','jb-detail-actions',
    'jb-btn','jb-btn-ghost','jb-empty','jb-loading','jb-spinner','jb-back','jb-detail-hl-block',
    'jb-cta-card','jb-cta-icon','jb-cta-text','jb-cta-head','jb-cta-title','jb-cta-badge','jb-cta-desc','jb-cta-btn'
  ];
  let missingCss = CRITICAL_CLASSES.filter(cls => !css.includes('.' + cls));
  if (missingCss.length) fail('CSS classes missing: ' + missingCss.join(','));
  else ok('All ' + CRITICAL_CLASSES.length + ' critical CSS classes are defined');

  // 6) Browse entry hook exposed
  if (!c.includes('window.__openJwBrowse')) fail('window.__openJwBrowse not exposed');
  else ok('window.__openJwBrowse exposed');
  if (!c.includes('window.__jwLastFile=e')) fail('window.__jwLastFile not set in ja()');
  else ok('window.__jwLastFile assignment present in ja()');

  // 7) Upsell + CTA in markup
  if (!c.includes('Note Explorer ✨')) fail('upsell item missing');
  else ok('Upsell "Note Explorer ✨" present');
  if (!c.includes('jb-cta-card') || !c.includes('jb-cta-btn')) fail('CTA card markup missing');
  else ok('CTA card markup present');

  // 8) Insights modal has the trigger button
  if (!c.includes('jb-browse-open-btn')) fail('Insights trigger button missing');
  else ok('Insights "Browse notes" button present');
}

section('SUMMARY');
if (failures === 0) { console.log('\nAll static checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

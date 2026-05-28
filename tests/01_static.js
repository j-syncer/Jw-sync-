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
const REQUIRED_I18N_KEYS = ['brw_open']; // in the main TRANSLATIONS object (both files)
// Keys that must exist on the beta build (new features land in beta first).
const BETA_ONLY_KEYS = ['cta_try_demo', 'cta_try_demo_nav'];

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

  const isBeta = path.endsWith('beta/index.html') || path.endsWith('beta\\index.html');
  for (const lang of EXPECTED_LANGS) {
    if (!trans[lang]) { fail('missing language: ' + lang); continue; }
    for (const key of REQUIRED_I18N_KEYS) {
      if (!trans[lang][key]) fail(`${lang}.${key} missing`);
    }
    if (isBeta) {
      for (const key of BETA_ONLY_KEYS) {
        if (!trans[lang][key]) fail(`${lang}.${key} missing (beta)`);
      }
    }
  }
  if (Object.keys(trans).length === EXPECTED_LANGS.length) ok('TRANSLATIONS has exactly 10 languages');
  if (isBeta) ok(`Beta: all ${BETA_ONLY_KEYS.length} beta-only key(s) present across ${EXPECTED_LANGS.length} languages`);

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

  // 9) Beta-only: "Try with sample notes" hero CTA + handler
  if (isBeta) {
    if (!c.includes('id="landing-demo-btn"')) fail('landing-demo-btn missing');
    else ok('landing-demo-btn present');
    if (!c.includes('class="cta-row"')) fail('.cta-row wrapper missing');
    else ok('.cta-row wrapper present');
    if (!c.includes('Demo handler')) fail('Demo handler script block missing');
    else ok('Demo handler script block present');
    // v2.8.0: the demo no longer carries an inline DEMO_B64 — it generates two
    // synthetic backups at click time via enhancements.js's buildDemoBackups,
    // then injects them into the React file pickers for a real merge demo.
    if (!c.includes('__jwInjectMergeDemo')) fail('merge-demo injector helper not referenced');
    else ok('merge-demo injector helper referenced (__jwInjectMergeDemo)');
    if (!c.includes('__jwBuildDemoBackups')) fail('demo builder helper not referenced');
    else ok('demo builder helper referenced (__jwBuildDemoBackups)');
    if (!c.includes('jw-demo-banner')) fail('demo guidance banner id missing');
    else ok('demo guidance banner referenced (#jw-demo-banner)');
    if (!c.includes('Try Demo') || !c.includes('merge flow')) fail('merge-flow marker comment missing');
    else ok('merge-flow Demo handler marker present');

    // 9a) Demo trigger surfaces in every place we expect:
    //   - static #site-nav (always-visible)
    //   - React internal nav (next to "Browse notes")
    //   - Simple Mode teaser (next to "Explore Full Mode →")
    if (!c.includes('class="site-nav-link site-nav-demo"')) fail('static nav demo button missing');
    else ok('static #site-nav demo button present');
    if (!c.includes('nav-btn-demo')) fail('React internal nav demo button missing (nav-btn-demo class)');
    else ok('React internal nav demo button present');
    if (!c.includes('simple-mode-teaser-btn-demo')) fail('Simple Mode teaser demo button missing');
    else ok('Simple Mode teaser demo button present');
    if (!c.includes('window.__jwOpenDemo')) fail('window.__jwOpenDemo not exposed');
    else ok('window.__jwOpenDemo exposed for React buttons');
    if (!c.includes('data-demo-trigger')) fail('data-demo-trigger attribute missing');
    else ok('data-demo-trigger attribute present');
    if (!c.includes('MutationObserver')) fail('MutationObserver not wired in demo handler');
    else ok('MutationObserver present (catches React-rendered demo buttons)');

    // 10) Lazy-load infrastructure (v2.7.0)
    //   - CDN script tags must NOT be in <head> (eager loading would defeat the point)
    //   - The main app and Browse module must be wrapped in __bootApp / __bootBrowse
    //   - The boot loader must expose __jwBootApp / __jwBootBrowse
    const CDN_SCRIPTS_IN_HEAD = [
      'cdnjs.cloudflare.com/ajax/libs/react/18.2.0',
      'cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0',
      'cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1',
      'cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0',
      'cdnjs.cloudflare.com/ajax/libs/lucide',
    ];
    const headEnd = c.indexOf('</head>');
    const headSection = c.slice(0, headEnd);
    let eagerCdn = CDN_SCRIPTS_IN_HEAD.filter(u => headSection.includes('<script') && headSection.includes(u) && /<script[^>]*src="[^"]*cdnjs/.test(headSection));
    // Stronger check: look for any <script src="cdnjs..."> in head
    if (/<script[^>]*src="https:\/\/cdnjs\.cloudflare\.com/.test(headSection)) {
      fail('CDN <script src> still present in <head> — lazy-load broken');
    } else {
      ok('no eager CDN <script> tags in <head>');
    }

    if (!c.includes('window.__bootApp')) fail('main app not wrapped in window.__bootApp');
    else ok('main app wrapped in window.__bootApp');
    if (!c.includes('window.__bootBrowse')) fail('Browse module not wrapped in window.__bootBrowse');
    else ok('Browse module wrapped in window.__bootBrowse');
    if (!c.includes('window.__jwBootApp')) fail('window.__jwBootApp not exposed (boot loader missing)');
    else ok('window.__jwBootApp exposed by boot loader');
    if (!c.includes('window.__jwBootBrowse')) fail('window.__jwBootBrowse not exposed (boot loader missing)');
    else ok('window.__jwBootBrowse exposed by boot loader');
    if (!c.includes('Lazy boot loader')) fail('lazy boot loader marker comment missing');
    else ok('lazy boot loader script block present');
    if (!c.includes("rel = 'prefetch'") && !c.includes('rel=\'prefetch\'')) fail('prefetch link logic missing');
    else ok('prefetch logic present (hover / idle)');
    if (!c.includes('jw-demo-loading')) fail('demo loading state CSS class missing');
    else ok('jw-demo-loading state class referenced');

    // 11) v2.8.0 enhancements.js must expose builder + injector for the merge demo
    const enhPath = REPO + '/beta/js/enhancements.js';
    const enh = require('fs').readFileSync(enhPath, 'utf8');
    if (!enh.includes('window.__jwBuildDemoBackups = buildDemoBackups')) fail('enhancements.js does not expose __jwBuildDemoBackups');
    else ok('enhancements.js exposes __jwBuildDemoBackups');
    if (!enh.includes('window.__jwInjectMergeDemo')) fail('enhancements.js does not expose __jwInjectMergeDemo');
    else ok('enhancements.js exposes __jwInjectMergeDemo');
    // The duplicate floating sample-data button must be deprecated (no DOM injection)
    if (/btn\.style\.cssText\s*=\s*['"]position:fixed/.test(enh) && enh.includes('Try with sample data')) {
      fail('the old floating "Try with sample data" button is still active in enhancements.js');
    } else {
      ok('legacy floating sample-data button is deprecated');
    }
    // 12) Banner CSS lives in beta/styles.css
    const cssPath = REPO + '/beta/styles.css';
    const css = require('fs').readFileSync(cssPath, 'utf8');
    if (!css.includes('#jw-demo-banner')) fail('beta/styles.css missing #jw-demo-banner rule');
    else ok('beta/styles.css defines #jw-demo-banner');
    if (!css.includes('.jw-demo-toast')) fail('beta/styles.css missing .jw-demo-toast rule');
    else ok('beta/styles.css defines .jw-demo-toast');
    if (!css.includes('.jw-demo-pulse')) fail('beta/styles.css missing .jw-demo-pulse rule');
    else ok('beta/styles.css defines .jw-demo-pulse');

    // 13) v2.9.0 post-merge celebration + Restore Guide
    if (!c.includes('Post-merge celebration')) fail('post-merge celebration script block missing');
    else ok('post-merge celebration script block present');
    if (!c.includes('jw-celebrate-overlay')) fail('celebration overlay id missing');
    else ok('celebration overlay referenced (#jw-celebrate-overlay)');
    if (!c.includes('jw-restore-overlay')) fail('restore guide overlay id missing');
    else ok('restore guide overlay referenced (#jw-restore-overlay)');
    // Stats query path uses sql.js for the merged db
    if (!c.includes('SELECT COUNT(*) FROM Note')) fail('celebration not querying merged db');
    else ok('celebration queries merged db via sql.js');
    // Translations: all 10 langs must have the celebration keys
    for (const lang of EXPECTED_LANGS) {
      const re = new RegExp(`${lang}:\\s*\\{[^}]*cele_title:`);
      if (!re.test(c)) fail(`celebration i18n missing for ${lang}`);
    }
    ok('celebration i18n present for all 10 languages');
    // Restore guide steps for each platform
    for (const platform of ['ios', 'android', 'other']) {
      const re = new RegExp(`${platform}:\\s*\\[`);
      if (!re.test(c)) fail(`restore guide steps missing for platform: ${platform}`);
    }
    ok('restore guide steps defined for ios / android / other');
    if (!css.includes('#jw-celebrate-overlay')) fail('beta/styles.css missing #jw-celebrate-overlay rule');
    else ok('beta/styles.css defines #jw-celebrate-overlay');
    if (!css.includes('#jw-restore-overlay')) fail('beta/styles.css missing #jw-restore-overlay rule');
    else ok('beta/styles.css defines #jw-restore-overlay');

    // 14) v2.9.1: auto-download + manual download button + donate link
    if (!c.includes('data-jwc-download')) fail('celebration missing Download button (data-jwc-download)');
    else ok('celebration has Download button');
    if (!c.includes('triggerDownload')) fail('celebration missing triggerDownload function (auto-download path)');
    else ok('celebration auto-download path (triggerDownload) present');
    if (!c.includes('autoDownloadedFor')) fail('celebration missing auto-download dedup guard');
    else ok('celebration auto-download one-shot guard present');
    if (!c.includes('paypal.com/paypalme/jwsync')) fail('donate link URL missing');
    else ok('donate link URL present (PayPal)');
    if (!c.includes('data-jwc-donate')) fail('donate link hook missing');
    else ok('donate link has data-jwc-donate hook');
    // Donate prompt/cta strings translated for all 10 langs
    for (const lang of EXPECTED_LANGS) {
      const re = new RegExp(`${lang}:\\s*\\{[^}]*donate_prompt:`);
      if (!re.test(c)) fail(`donate i18n missing for ${lang}`);
    }
    ok('donate i18n present for all 10 languages');
    if (!css.includes('.jwc-donate')) fail('beta/styles.css missing .jwc-donate rule');
    else ok('beta/styles.css defines .jwc-donate');
    if (!css.includes('.jwc-btn-outline')) fail('beta/styles.css missing .jwc-btn-outline (Restore button) rule');
    else ok('beta/styles.css defines .jwc-btn-outline');
    if (!css.includes('.jwc-download-status')) fail('beta/styles.css missing .jwc-download-status banner rule');
    else ok('beta/styles.css defines .jwc-download-status banner');
  }
}

section('SUMMARY');
if (failures === 0) { console.log('\nAll static checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

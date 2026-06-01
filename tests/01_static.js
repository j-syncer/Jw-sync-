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
const BETA_ONLY_KEYS = ['cta_try_demo', 'cta_try_demo_nav', 'cta_howto',
  'err_corrupt', 'err_no_db', 'err_not_sqlite', 'err_oversize', 'warn_oversize'];

const BROWSE_REQUIRED_KEYS = [
  'title','search','no_results','loading','close','no_file','pick_file',
  'count_one','count_many','color_all','no_title','copy','copied','clear',
  'error','pub_all','tag_all','back','detail_empty','sort_newest',
  'sort_oldest','sort_pub','modified','no_content','too_many',
  'tab_notes','tab_highlights','tab_bookmarks','hl_label','hl_no_text',
  'hl_with_note','bm_label','bm_slot','linked_note'
];
// Browse keys that land on the beta build first (new features ship to beta).
const BROWSE_BETA_ONLY_KEYS = [
  'pg_prev','pg_next','pg_status','err_corrupt','err_no_db','err_not_sqlite',
  'rte_bold','rte_italic','rte_underline','rte_bullets','rich_text_note'
];

for (const path of FILES) {
  section(path);
  const c = fs.readFileSync(path, 'utf8');

  // v2.10.0: main app bundle may be extracted to js/app.js (beta) or still
  // inline (production until go-live). Resolve the source either way.
  const isBeta = path.endsWith('beta/index.html') || path.endsWith('beta\\index.html');
  const appJsPath = path.replace(/index\.html$/, 'js/app.js');
  let bundleSrc, bundleSource;
  if (fs.existsSync(appJsPath) && fs.readFileSync(appJsPath, 'utf8').includes('TRANSLATIONS=')) {
    bundleSrc = fs.readFileSync(appJsPath, 'utf8');
    bundleSource = 'external: ' + appJsPath;
  } else {
    const ti0 = c.indexOf('TRANSLATIONS=');
    if (ti0 < 0) { fail('TRANSLATIONS not in HTML nor in ' + appJsPath); continue; }
    const ss = c.lastIndexOf('<script', ti0);
    const so = c.indexOf('>', ss) + 1;
    const se = c.indexOf('</script>', so);
    bundleSrc = c.slice(so, se);
    bundleSource = 'inline <script> in ' + path;
  }

  // 1) Main React bundle parses
  try {
    new Function(bundleSrc);
    ok('main app bundle parses (' + bundleSrc.length + ' bytes, ' + bundleSource + ')');
  } catch (e) { fail('main app parse failed: ' + e.message); }

  // 2) Browse module parses (still inline in both files)
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
  const ti = bundleSrc.indexOf('TRANSLATIONS=');
  let d = 0, e2 = ti + 13;
  for (let i = ti + 13; i < bundleSrc.length; i++) {
    if (bundleSrc[i] === '{') d++;
    else if (bundleSrc[i] === '}') { d--; if (d === 0) { e2 = i + 1; break; } }
  }
  let trans;
  try {
    trans = eval('(' + bundleSrc.slice(ti + 13, e2) + ')');
    ok('TRANSLATIONS parses');
  } catch (e) { fail('TRANSLATIONS parse failed: ' + e.message); continue; }

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

  const browseKeys = isBeta ? BROWSE_REQUIRED_KEYS.concat(BROWSE_BETA_ONLY_KEYS) : BROWSE_REQUIRED_KEYS;
  for (const lang of EXPECTED_LANGS) {
    if (!browseI18n[lang]) { fail('Browse I18N missing ' + lang); continue; }
    let missing = browseKeys.filter(k => !browseI18n[lang][k]);
    if (missing.length) fail(`${lang} missing keys: ${missing.join(',')}`);
  }
  ok('Browse I18N: 10 langs each cover ' + browseKeys.length + ' keys');

  // 4b) All JSON-LD structured-data blocks parse; SEO schema present (beta)
  const ldBlocks = [...c.matchAll(/<script type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/g)];
  let ldOk = true;
  for (const blk of ldBlocks) {
    try { JSON.parse(blk[1]); } catch (e) { fail('JSON-LD block invalid: ' + e.message); ldOk = false; }
  }
  if (ldOk) ok(`all ${ldBlocks.length} JSON-LD block(s) parse`);
  const ldTypes = ldBlocks.map(b => { try { return JSON.parse(b[1])['@type']; } catch { return null; } });
  if (isBeta) {
    if (ldTypes.includes('FAQPage')) ok('FAQPage structured data present'); else fail('FAQPage JSON-LD missing');
    if (ldTypes.includes('HowTo')) ok('HowTo structured data present'); else fail('HowTo JSON-LD missing');
    if (c.includes('class="landing-faq"')) ok('visible FAQ section present'); else fail('visible FAQ section missing');
    if (c.includes('class="landing-howto"')) ok('visible How-to section present'); else fail('visible How-to section missing');
  }

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

  // 6) Browse entry hook exposed (these live in the Browse module inline
  // and in the main app bundle — search both)
  const allSrc = c + '\n' + bundleSrc;
  if (!allSrc.includes('window.__openJwBrowse')) fail('window.__openJwBrowse not exposed');
  else ok('window.__openJwBrowse exposed');
  if (!allSrc.includes('window.__jwLastFile=e')) fail('window.__jwLastFile not set in ja()');
  else ok('window.__jwLastFile assignment present in ja()');

  // Landing language picker must work before the (lazy) app bundle loads:
  // a compact landing i18n set is exposed as a window.TRANSLATIONS fallback.
  if (isBeta) {
    if (!c.includes('window.__JW_LANDING_I18N'))
      fail('landing i18n fallback missing — language switch no-ops on cold landing');
    else ok('landing i18n fallback (window.__JW_LANDING_I18N) present');
    // It must cover all 10 languages with the hero key.
    const lm = c.match(/window\.__JW_LANDING_I18N\s*=\s*(\{[\s\S]*?\});/);
    if (lm) {
      try {
        const li = JSON.parse(lm[1]);
        const ok10 = EXPECTED_LANGS.every(l => li[l] && li[l].hero_title);
        if (ok10) ok('landing i18n covers all 10 languages'); else fail('landing i18n missing a language/hero_title');
      } catch (e) { fail('landing i18n JSON invalid: ' + e.message); }
    } else fail('landing i18n object not parseable');
  }

  // 7) Upsell + CTA in markup
  if (!allSrc.includes('Note Explorer ✨')) fail('upsell item missing');
  else ok('Upsell "Note Explorer ✨" present');
  if (!allSrc.includes('jb-cta-card') || !allSrc.includes('jb-cta-btn')) fail('CTA card markup missing');
  else ok('CTA card markup present');

  // 8) Insights modal has the trigger button
  if (!allSrc.includes('jb-browse-open-btn')) fail('Insights trigger button missing');
  else ok('Insights "Browse notes" button present');

  // Browse open buttons must boot the (lazy) Browse module before opening —
  // otherwise a cold click leaves window.__openJwBrowse undefined and no-ops.
  if (bundleSrc.includes('__openJwBrowse') && !bundleSrc.includes('__jwBootBrowse'))
    fail('Browse buttons call __openJwBrowse without booting Browse first (cold click no-ops)');
  else ok('Browse buttons boot Browse before opening');

  // 8b) Beta-only: Saved Devices & Auto-Sync (Sync Hub, v2.20.0)
  if (isBeta) {
    if (!c.includes('window.__jwOpenSyncHub')) fail('Sync Hub (window.__jwOpenSyncHub) missing');
    else ok('Sync Hub module present');
    if (!c.includes('jsh-fab') || !c.includes('jsh-merge')) fail('Sync Hub markup/CSS missing');
    else ok('Sync Hub launcher + merge controls present');
    if (!c.includes("new Worker('./js/merge-worker.js')")) fail('Sync Hub does not drive merge-worker.js');
    else ok('Sync Hub drives merge-worker.js directly');
  }

  // 8c) Date-Range Extraction in Browse (v2.21.0, beta-only)
  if (isBeta) {
    if (!c.includes('jb-filter-date') || !c.includes('jb-extract-btn')) fail('Browse date-range controls missing');
    else ok('Browse date-range filter + extract controls present');
    if (!c.includes('function extractByDate')) fail('extractByDate() missing');
    else ok('extractByDate() present');
  }

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
    //   - React internal nav (next to "Browse notes")
    //   - Simple Mode teaser (next to "Explore Full Mode →")
    //   - static nav now has the Service Year button instead of Try Demo
    if (!c.includes('class="site-nav-link site-nav-wrapped"')) fail('static nav Service Year button missing');
    else ok('static #site-nav Service Year button present');
    // These render inside the React bundle (now external for beta)
    if (!allSrc.includes('nav-btn-demo')) fail('React internal nav demo button missing (nav-btn-demo class)');
    else ok('React internal nav demo button present');
    if (!allSrc.includes('simple-mode-teaser-btn-demo')) fail('Simple Mode teaser demo button missing');
    else ok('Simple Mode teaser demo button present');
    if (!c.includes('window.__jwOpenDemo')) fail('window.__jwOpenDemo not exposed');
    else ok('window.__jwOpenDemo exposed for React buttons');
    if (!c.includes('data-demo-trigger')) fail('data-demo-trigger attribute missing');
    else ok('data-demo-trigger attribute present');

    // Guided in/out flow (v2.14.0)
    if (!c.includes('EXPORT_GUIDE')) fail('EXPORT_GUIDE object missing (export walkthrough)');
    else ok('EXPORT_GUIDE export-steps object present');
    if (!c.includes('window.__jwOpenGuide')) fail('window.__jwOpenGuide not exposed');
    else ok('window.__jwOpenGuide exposed');
    if (!c.includes('id="landing-howto-btn"')) fail('landing-howto-btn missing');
    else ok('landing "How it works" button present');
    if (!c.includes('data-howto-trigger')) fail('data-howto-trigger attribute missing');
    else ok('data-howto-trigger attribute present');
    if (!c.includes('jwrg-mode')) fail('jwrg-mode IN/OUT toggle markup missing');
    else ok('guide IN/OUT mode toggle (.jwrg-mode) present');

    // Robust error handling + Browse pagination (v2.15.0)
    if (!c.includes('jb-pager')) fail('Browse pager markup/CSS missing (.jb-pager)');
    else ok('Browse pagination (.jb-pager) present');
    if (!c.includes('PAGE_SIZE')) fail('Browse PAGE_SIZE constant missing');
    else ok('Browse PAGE_SIZE windowing present');

    // Pre-merge impact preview (v2.16.0)
    if (!c.includes('window.__jwImpactPreview')) fail('window.__jwImpactPreview module missing');
    else ok('pre-merge impact preview (__jwImpactPreview) present');
    if (!c.includes('jip-card')) fail('impact preview markup/CSS missing (.jip-card)');
    else ok('impact preview modal (.jip-card) present');

    // Rich-text note editing (v2.17.0)
    if (!c.includes('sanitizeNoteHtml')) fail('sanitizeNoteHtml allow-list sanitizer missing');
    else ok('sanitizeNoteHtml sanitizer present');
    if (!c.includes('buildRteEditor')) fail('buildRteEditor (WYSIWYG) missing');
    else ok('rich-text editor (buildRteEditor) present');
    if (!c.includes('jb-edit-rte')) fail('rich-text editor markup/CSS missing (.jb-edit-rte)');
    else ok('rich-text editor (.jb-edit-rte) present');
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

    // v2.10.0: main app bundle is now external (beta only). Verify:
    //   - the inline <script> body that used to hold the bundle is gone
    //   - js/app.js exists and contains the bundle opener + boot wrapper
    //   - the boot loader has loadAppBundle()
    //   - js/app.js is in the prefetch list
    //   - js/app.js is NOT eagerly loaded via <script src> in <head>
    if (c.includes('var Ka=Object.defineProperty')) {
      fail('main app bundle still inline in HTML (extraction did not happen)');
    } else {
      ok('main app bundle NOT inline in beta/index.html (extracted)');
    }
    if (!fs.existsSync(appJsPath)) fail('beta/js/app.js does not exist');
    else {
      const app = fs.readFileSync(appJsPath, 'utf8');
      if (app.includes('window.__bootApp = function()') && app.includes('var Ka=Object.defineProperty')) {
        ok('beta/js/app.js exists, contains the bundle and __bootApp wrapper');
      } else {
        fail('beta/js/app.js missing __bootApp wrapper or bundle opener');
      }
    }
    if (!c.includes('function loadAppBundle()')) fail('boot loader missing loadAppBundle()');
    else ok('boot loader has loadAppBundle()');
    if (!c.includes("'js/app.js'") && !c.includes('"js/app.js"')) fail('boot loader does not reference js/app.js');
    else ok('boot loader references js/app.js');
    if (!c.includes("appLink.href = 'js/app.js'") && !c.includes('appLink.href = "js/app.js"')) {
      fail('js/app.js not in the hover/idle prefetch list');
    } else { ok('js/app.js is in the prefetch list'); }
    if (/<script[^>]*src=["']js\/app\.js["']/.test(c.slice(0, c.indexOf('</head>')))) {
      fail('js/app.js eagerly loaded via <script src> in <head>');
    } else { ok('js/app.js NOT eagerly loaded in <head>'); }
    // The Promise.all chain must include loadAppBundle so the boot waits for it
    if (!/Promise\.all\(\[loadReact\(\), loadStorage\(\), loadAppBundle\(\)\]\)/.test(c)) {
      fail('bootApp Promise.all does not include loadAppBundle()');
    } else { ok('bootApp awaits loadAppBundle alongside React + storage'); }

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

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

const EXPECTED_LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl','sv'];
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
  // Swedish ships to beta first; production gets it on go-live. Until then,
  // only require the 11th language on the beta build.
  const FILE_LANGS = isBeta ? EXPECTED_LANGS : EXPECTED_LANGS.filter(l => l !== 'sv');
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

  for (const lang of FILE_LANGS) {
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
  if (Object.keys(trans).length === FILE_LANGS.length) ok('TRANSLATIONS has exactly ' + FILE_LANGS.length + ' languages');
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
  for (const lang of FILE_LANGS) {
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

  // 8d) Smart Conflict Suggestions (v2.22.0, beta-only)
  if (isBeta) {
    if (!c.includes('data-jcr-suggest') || !c.includes('function suggestFor')) fail('Conflict suggestion engine missing');
    else ok('Conflict "Suggest best" engine present');
    if (!c.includes('jcr-suggestion-badge') || !c.includes('jcr-suggested')) fail('Conflict suggestion styles missing');
    else ok('Conflict suggestion badge/highlight styles present');
  }

  // 8e) Markdown sharing & export (v2.23.0, beta-only)
  if (isBeta) {
    if (!c.includes('function noteToMarkdown') || !c.includes('function exportMarkdown')) fail('Markdown export helpers missing');
    else ok('Markdown export helpers present');
    if (!c.includes('jb-md-btn')) fail('Markdown export button missing');
    else ok('Markdown export button present');
  }

  // 8f) Mobile UX polish (v2.24.0, beta-only): offline banner, haptics, swipe
  if (isBeta) {
    if (!c.includes('jw-offline-banner') || !c.includes('window.__jwHaptic')) fail('Offline banner / haptic helper missing');
    else ok('Offline banner + haptic helper present');
    if (!c.includes('function switchTo') || !c.includes('switchByOffset') || !c.includes('touchstart')) fail('Browse swipe-to-switch missing');
    else ok('Browse swipe-to-switch tabs present');
  }

  // 8g) Bulk manager + Undo/Redo (v2.26.0, beta-only)
  if (isBeta) {
    if (!c.includes('function snapshot') || !c.includes('function doUndo') || !c.includes('function doRedo') || !c.includes('function hydrateFromDb'))
      fail('Undo/redo infrastructure missing');
    else ok('Undo/redo infrastructure present');
    if (!c.includes('function batchDelete') || !c.includes('function batchAddTag') || !c.includes('function batchSetColor'))
      fail('Batch operations missing');
    else ok('Batch operations present');
    if (!c.includes('jb-select-toggle') || !c.includes('jb-batch-bar') || !c.includes('jb-check') || !c.includes('jb-undo'))
      fail('Bulk-manager UI classes missing');
    else ok('Bulk-manager UI (select/batch/checkbox/undo) present');
  }

  // 8h) Study Questions / Input Fields (v2.27.0, beta-only)
  if (isBeta) {
    if (!c.includes('function buildInputFieldRow') || !c.includes('function saveInputField') || !c.includes('function deleteInputField'))
      fail('Input Field (Study Answers) functions missing');
    else ok('Input Field (Study Answers) functions present');
    if (!c.includes("['inputfields',t('tab_inputfields')]") || !c.includes('state.allInputFields'))
      fail('Study Answers tab wiring missing');
    else ok('Study Answers tab wired');
  }

  // 8i) Note sharing (v2.28.0 in-Browse quick share + v2.30.0 dedicated page)
  if (isBeta) {
    if (!c.includes('function openShareExport') || !c.includes('function buildShareEnvelope'))
      fail('Quick-share functions missing');
    else ok('Quick-share functions present');
    if (!c.includes('function __jwGoShare') || !c.includes("href='share.html'"))
      fail('Dedicated Share page handoff missing');
    else ok('Dedicated Share page handoff present');
    if (!c.includes('data-i18n="svc_share_t"'))
      fail('Share service card missing from home page');
    else ok('Share service card present');
  }

  // 8k) Home-page service cards + Tools menu removed (v2.33.0, beta-only)
  if (isBeta) {
    if (c.includes('__jwOpenToolsMenu') || c.includes('site-nav-tools') || allSrc.includes('nav-btn-tools'))
      fail('Tools ▾ menu should be fully removed in v2.33.0');
    else ok('Tools ▾ menu fully removed');
    if (!c.includes('class="svc-grid"') || !c.includes('data-i18n="svc_heading"'))
      fail('Home service section (.svc-grid) missing');
    else ok('Home service section (.svc-grid) present');
    const cards = (c.match(/class="svc-card[ "]/g) || []).length;
    if (cards === 4) ok('Four distinct service cards present');
    else fail('Expected 4 .svc-card, got ' + cards);
    for (const k of ['svc_merge_t', 'svc_explorer_t', 'svc_stats_t', 'svc_share_t'])
      if (!c.includes('data-i18n="' + k + '"')) fail('Service card i18n key missing: ' + k);
    // v2.34.1: whole cards are clickable tiles (no inner buttons / no &#8594; gibberish)
    if (!c.includes('svc-card-btn')) ok('cards are clickable tiles (no inner Open buttons)');
    else fail('svc-card-btn buttons should be gone (clickable tiles)');
    // v2.34.1: landing i18n falls back to __JW_LANDING_I18N so cards translate on
    // language change even after app.js overwrites window.TRANSLATIONS
    if (c.includes('var L=window.__JW_LANDING_I18N'))
      ok('applyLandingI18n falls back to __JW_LANDING_I18N (cards translate on lang change)');
    else fail('applyLandingI18n missing __JW_LANDING_I18N fallback');
    // v2.35.0: per-card colored shimmer + distinct accent classes
    const cssPath = path.replace(/index\.html$/, 'styles.css');
    const cssSrc = fs.existsSync(cssPath) ? fs.readFileSync(cssPath, 'utf8') : '';
    if (['svc-explorer', 'svc-stats', 'svc-share'].every(k => c.includes('class="svc-card ' + k + '"')))
      ok('Distinct accent classes on the three service tiles');
    else fail('Service tile accent classes missing in HTML');
    if (/@keyframes svcShimmer/.test(cssSrc) && /\.svc-card::after/.test(cssSrc))
      ok('Per-card colored shimmer defined in CSS');
    else fail('svcShimmer / .svc-card::after missing from styles.css');
    if (cssSrc.includes('prefers-reduced-motion: reduce) { .svc-card::after'))
      ok('Shimmer respects prefers-reduced-motion');
    else fail('Shimmer missing reduced-motion guard');
    // in-app nav keeps Study Explorer; Study Stats moved to the site-nav (v2.44.0)
    if (allSrc.includes('nav-btn-browse') && !allSrc.includes('nav-btn-wrapped'))
      ok('App top-bar has Study Explorer; Study Stats button moved to site nav');
    else fail('App top-bar nav-btn-browse missing or stale nav-btn-wrapped still present');
  }

  // 8l) Two-level mobile nav (v2.32.0): language picker sits beside the logo,
  //     not inside .site-nav-links (so App/Community/Tools get a full row).
  if (isBeta) {
    if (!/<\/div>\s*<select id="landing-lang-select"/.test(c))
      fail('Language picker not moved out of .site-nav-links (two-level nav)');
    else ok('Two-level nav: language picker is a direct #site-nav child');
  }

  // 8m) Receive shared notes in merge (v2.34.0, beta-only)
  if (isBeta) {
    if (c.includes('window.__jwAdoptSharedIntoBuffer') && c.includes('window.__jwParseShareEnvelope'))
      ok('Receive-in-merge core API present');
    else fail('Receive-in-merge core API missing');
    if (c.includes('data-jwc-addshared') && c.includes('window.__jwReceivePickAndAdopt'))
      ok('End-of-merge "add shared notes" button wired');
    else fail('End-of-merge add-shared button missing');
    if (c.includes('window.__jwReceiveOnCelebration') && c.includes('jwr-panel'))
      ok('Pre-merge attach + auto-adopt hooks present');
    else fail('Pre-merge receive hooks missing');
  }

  // 8j2) Browse tab strip scrolls on overflow (mobile) — v2.30.0
  if (isBeta) {
    if (!/\.jb-tabs\{[^}]*overflow-x:auto/.test(c)) fail('Browse tab strip is not horizontally scrollable (mobile cut-off)');
    else ok('Browse tab strip scrolls horizontally (no cut-off)');
  }

  // 8j) Merge performance dashboard (v2.29.0, beta-only)
  if (isBeta) {
    if (!c.includes('function buildPerfHtml') || !c.includes('jwc-perf') || !c.includes('__jwLastMergeTimings'))
      fail('Merge performance section missing');
    else ok('Merge performance section present');
  }

  // 9) Beta-only: "Try with sample notes" hero CTA + handler
  if (isBeta) {
    if (!c.includes('id="landing-demo-btn"')) fail('landing-demo-btn missing');
    else ok('landing-demo-btn present');
    if (!c.includes('class="cta-row')) fail('.cta-row wrapper missing');
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
    //   - React internal nav (next to the individual service buttons)
    //   - Simple Mode teaser (next to "Explore Full Mode →")
    //   - static nav is lean (services live as home-page cards now)
    if (c.includes('site-nav-tools')) fail('static nav Tools launcher should be removed (v2.33.0)');
    else ok('static #site-nav is lean (no Tools launcher)');
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
    for (const lang of FILE_LANGS) {
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
    for (const lang of FILE_LANGS) {
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
    // v2.44.0: celebration "View Your Stats" button shimmers like the nav link
    if (/\.jwc-btn-highlights\b[\s\S]*?animation:\s*navShimmer/.test(css)
        && css.includes('prefers-reduced-motion: reduce) { .jwc-btn-highlights'))
      ok('Celebration Study Stats button has shimmer (+ reduced-motion guard)');
    else fail('Celebration Study Stats shimmer / reduced-motion guard missing');
  }
}

// ── Cross-tool file session + universal tool switcher (v2.48.0) ──────────
section('Cross-tool session (jw-session.js)');
{
  const sessPath = REPO + '/beta/js/jw-session.js';
  if (!fs.existsSync(sessPath)) fail('beta/js/jw-session.js missing');
  else {
    ok('beta/js/jw-session.js present');
    const js = fs.readFileSync(sessPath, 'utf8');
    // Parse-ability
    try { new (require('vm').Script)(js); ok('jw-session.js parses'); }
    catch (e) { fail('jw-session.js parse error: ' + e.message); }
    // Public API
    for (const api of ['put:', 'get:', 'clear:', 'goTo:', 'mountSwitcher:']) {
      if (js.includes(api)) ok('JwSession exposes ' + api.replace(':', '()'));
      else fail('JwSession missing ' + api);
    }
    // Shared, persistent (non-consuming) store + privacy TTL
    if (js.includes("'jwsync_session_v1'")) ok('shared session DB jwsync_session_v1 present');
    else fail('shared session DB name missing');
    if (/TTL_MS\s*=/.test(js) && js.includes('clear()')) ok('privacy TTL + clear() present');
    else fail('privacy TTL / clear missing');
    // get() must NOT delete (non-consuming, unlike the legacy one-shot inbox)
    const getBody = js.slice(js.indexOf('function get()'), js.indexOf('function clear()'));
    if (getBody && !getBody.includes('.delete(')) ok('get() is non-consuming (no delete in read path)');
    else fail('get() unexpectedly deletes the working file');
    // Switcher covers all four tools
    for (const tool of ['merge', 'stats', 'explorer', 'share']) {
      if (js.includes("id: '" + tool + "'")) ok('switcher includes tool: ' + tool);
      else fail('switcher missing tool: ' + tool);
    }
    // Localised switcher labels for all 10 languages
    for (const lang of EXPECTED_LANGS) {
      const re = new RegExp('\\b' + lang + ':\\s*\\{\\s*merge:');
      if (re.test(js)) ok('switcher labels present for ' + lang);
      else fail('switcher labels missing for ' + lang);
    }
  }

  // All three surfaces load the shared module
  for (const page of ['beta/index.html', 'beta/highlights.html', 'beta/share.html']) {
    const src = fs.readFileSync(REPO + '/' + page, 'utf8');
    if (src.includes('js/jw-session.js')) ok(page + ' loads js/jw-session.js');
    else fail(page + ' does not load js/jw-session.js');
  }

  // index.html: Explorer entry + routing + capture, with localised nav label
  {
    const idx = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
    if (idx.includes('id="site-nav-explorer"') && idx.includes('function __jwGoExplorer'))
      ok('index.html has Explorer nav link + __jwGoExplorer router');
    else fail('index.html Explorer nav/route missing');
    if (idx.includes("Object.defineProperty(window,'__jwLastFile'"))
      ok('index.html mirrors __jwLastFile into the shared session');
    else fail('index.html __jwLastFile capture missing');
    // The Merge upload doesn't set __jwLastFile, so a document-level file
    // capture must persist any .jwlibrary the user picks/drops (v2.48.1 fix).
    if (idx.includes("addEventListener('change'") && idx.includes("addEventListener('drop'") && idx.includes("'.jwlibrary'"))
      ok('index.html captures any uploaded/dropped .jwlibrary into the session');
    else fail('index.html global .jwlibrary capture missing (Merge uploads would not persist)');
    // Legacy hand-off + the tested string contract are preserved
    if (idx.includes('function __jwGoShare') && idx.includes("href='share.html'"))
      ok('legacy __jwGoShare contract preserved');
    else fail('legacy __jwGoShare contract broken');
    let navExpOk = true;
    const lm = idx.match(/window\.__JW_LANDING_I18N\s*=\s*(\{[\s\S]*?\});/);
    try {
      const o = JSON.parse(lm[1]);
      navExpOk = EXPECTED_LANGS.every(l => o[l] && o[l].nav_explorer);
    } catch (e) { navExpOk = false; }
    if (navExpOk) ok('nav_explorer localised for all 10 languages');
    else fail('nav_explorer i18n incomplete');
  }

  // highlights.html + share.html: switcher slot, mount, persist, and privacy-clear
  {
    const hl = fs.readFileSync(REPO + '/beta/highlights.html', 'utf8');
    if (hl.includes('id="hl-switch"') && hl.includes("mountSwitcher(document.getElementById('hl-switch'), 'stats')"))
      ok('highlights.html mounts the switcher (active: stats)');
    else fail('highlights.html switcher mount missing');
    if (hl.includes('window.JwSession.put(buffer') && hl.includes('window.JwSession.clear()'))
      ok('highlights.html persists on load + clears on New file');
    else fail('highlights.html persist/clear wiring missing');
    if (hl.includes('jwsync_hl_v1')) ok('highlights.html keeps legacy one-shot fallback');
    else fail('highlights.html legacy fallback removed');

    const sh = fs.readFileSync(REPO + '/beta/share.html', 'utf8');
    if (sh.includes('id="sh-switch"') && sh.includes("mountSwitcher(document.getElementById('sh-switch'), 'share')"))
      ok('share.html mounts the switcher (active: share)');
    else fail('share.html switcher mount missing');
    if (sh.includes('window.JwSession.put(keepBuf') && sh.includes('window.JwSession.clear()'))
      ok('share.html persists on load + clears on Start over');
    else fail('share.html persist/clear wiring missing');
    if (sh.includes('jwsync_share_v1')) ok('share.html keeps legacy one-shot fallback');
    else fail('share.html legacy fallback removed');
  }
}

section('SUMMARY');
if (failures === 0) { console.log('\nAll static checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

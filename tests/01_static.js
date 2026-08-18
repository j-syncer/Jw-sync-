const path = require('path');
const REPO = path.join(__dirname, '..');
// Static checks: parse-ability, anchor presence, i18n completeness, CSS classes used == defined.
const fs = require('fs');
const { browseJs, browseCss } = require('./helpers/browse-source');
const { withModules } = require('./helpers/page-source');

const FILES = [
  REPO + '/beta/index.html',
  REPO + '/index.html',
];

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

const EXPECTED_LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant', 'vi', 'hu', 'hi', 'id', 'ro', 'nl', 'sw', 'el'];

// A dictionary's language key is written `en:` while the tag is a bare JS
// identifier and `"zh-Hans":` once it is not — a BCP-47 tag with a script
// subtag contains a hyphen and cannot be an unquoted key. Every coverage regex
// below builds its key fragment here, so a new tag *shape* widens the guards
// rather than quietly dropping the language out of each of them.
const KEY = (lang) => '(?:^|[,{\\s])"?' + lang + '"?\\s*:';
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
  'hl_with_note','bm_label','bm_slot','linked_note',
  'change_file',
  'ask_btn','ask_title','ask_sub','ask_placeholder','ask_go',
  'ask_enable_title','ask_enable_body',
  'ask_model_fast_name','ask_model_fast_desc',
  'ask_model_en_name','ask_model_en_desc',
  'ask_model_multi_name','ask_model_multi_desc',
  'ask_size_once','ask_privacy',
  'ask_loading_model','ask_building','ask_ready','ask_searching',
  'ask_results_head','ask_no_results','ask_no_notes','ask_err',
  'ask_rebuild','ask_match','ask_switch_model'
];
// Browse keys that land on the beta build first (new features ship to beta).
const BROWSE_BETA_ONLY_KEYS = [
  'pg_prev','pg_next','pg_status','err_corrupt','err_no_db','err_not_sqlite',
  'rte_bold','rte_italic','rte_underline','rte_bullets','rich_text_note',
  'batch_tagged_ok'
];

for (const path of FILES) {
  section(path);
  const c = fs.readFileSync(path, 'utf8');

  // v2.10.0: main app bundle may be extracted to js/app.js (beta) or still
  // inline (production until go-live). Resolve the source either way.
  const isBeta = path.endsWith('beta/index.html') || path.endsWith('beta\\index.html');
  // Swedish is live on both beta and production.
  const FILE_LANGS = EXPECTED_LANGS;
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

  // 2) Browse module parses. v3.8.0 moved it to js/browse.js on the pages that
  //    lazy-load it; production keeps the inline copy until go-live.
  const browseSrc = browseJs(path);
  if (browseSrc == null) { fail('Browse module not found (inline or js/browse.js)'); continue; }
  try {
    new Function(browseSrc);
    ok('Browse module parses (' + browseSrc.length + ' bytes)');
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

  // Feature-presence checks below search the page *and* every module v3.8.0
  // lifted out of it (js/browse.js, js/doctor.js, …). Structural checks keep
  // using `c` so "must not be inline" assertions stay meaningful.
  const cAll = withModules(path);

  const browseKeys = isBeta ? BROWSE_REQUIRED_KEYS.concat(BROWSE_BETA_ONLY_KEYS) : BROWSE_REQUIRED_KEYS;
  for (const lang of FILE_LANGS) {
    if (!browseI18n[lang]) { fail('Browse I18N missing ' + lang); continue; }
    let missing = browseKeys.filter(k => !browseI18n[lang][k]);
    if (missing.length) fail(`${lang} missing keys: ${missing.join(',')}`);
  }
  ok('Browse I18N: 12 langs each cover ' + browseKeys.length + ' keys');

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
  const css = browseCss(path);
  if (!css) { fail('Browse <style> block missing'); continue; }
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
    // It must cover all 12 languages with the hero key.
    const lm = c.match(/window\.__JW_LANDING_I18N\s*=\s*(\{[\s\S]*?\});/);
    if (lm) {
      try {
        const li = JSON.parse(lm[1]);
        const ok10 = EXPECTED_LANGS.every(l => li[l] && li[l].hero_title);
        if (ok10) ok('landing i18n covers all 12 languages'); else fail('landing i18n missing a language/hero_title');
      } catch (e) { fail('landing i18n JSON invalid: ' + e.message); }
    } else fail('landing i18n object not parseable');
  }

  // 7) Browse CTA in markup
  //
  // There was a third assertion here, that the source still contained the
  // string "Note Explorer ✨". It was the Simple Mode teaser's upsell item, and
  // it had been vacuous since v3.32.0 removed that landing: the string survived
  // only as the smt_note_explorer dictionary value, which no component ever
  // looked up, so the check was reading a translation table and calling it
  // markup. (It also asserted an ✨ in a button, which the design rules forbid.)
  // The live Note Explorer entry points are the CTA card and the Insights
  // trigger button, both checked immediately below.
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
    if (!cAll.includes('window.__jwOpenSyncHub')) fail('Sync Hub (window.__jwOpenSyncHub) missing');
    else ok('Sync Hub module present');
    if (!c.includes('jsh-fab') || !c.includes('jsh-merge')) fail('Sync Hub markup/CSS missing');
    else ok('Sync Hub launcher + merge controls present');
    if (!cAll.includes("new Worker('./js/merge-worker.js')")) fail('Sync Hub does not drive merge-worker.js');
    else ok('Sync Hub drives merge-worker.js directly');
  }

  // 8c) Date-Range Extraction in Browse (v2.21.0, beta-only)
  if (isBeta) {
    if (!c.includes('jb-filter-date') || !c.includes('jb-extract-btn')) fail('Browse date-range controls missing');
    else ok('Browse date-range filter + extract controls present');
    if (!cAll.includes('function extractByDate')) fail('extractByDate() missing');
    else ok('extractByDate() present');
  }

  // 8d) Smart Conflict Suggestions (v2.22.0, beta-only)
  if (isBeta) {
    if (!cAll.includes('data-jcr-suggest') || !cAll.includes('function suggestFor')) fail('Conflict suggestion engine missing');
    else ok('Conflict "Suggest best" engine present');
    if (!c.includes('jcr-suggestion-badge') || !c.includes('jcr-suggested')) fail('Conflict suggestion styles missing');
    else ok('Conflict suggestion badge/highlight styles present');
  }

  // 8e) Markdown sharing & export (v2.23.0, beta-only)
  if (isBeta) {
    if (!cAll.includes('function noteToMarkdown') || !cAll.includes('function exportMarkdown')) fail('Markdown export helpers missing');
    else ok('Markdown export helpers present');
    if (!c.includes('jb-md-btn')) fail('Markdown export button missing');
    else ok('Markdown export button present');
  }

  // 8f) Mobile UX polish (v2.24.0, beta-only): offline banner, haptics, swipe
  if (isBeta) {
    if (!c.includes('jw-offline-banner') || !c.includes('window.__jwHaptic')) fail('Offline banner / haptic helper missing');
    else ok('Offline banner + haptic helper present');
    if (!cAll.includes('function switchTo') || !cAll.includes('switchByOffset') || !cAll.includes('touchstart')) fail('Browse swipe-to-switch missing');
    else ok('Browse swipe-to-switch tabs present');
  }

  // 8g) Bulk manager + Undo/Redo (v2.26.0, beta-only)
  if (isBeta) {
    if (!cAll.includes('function snapshot') || !cAll.includes('function doUndo') || !cAll.includes('function doRedo') || !cAll.includes('function hydrateFromDb'))
      fail('Undo/redo infrastructure missing');
    else ok('Undo/redo infrastructure present');
    if (!cAll.includes('function batchDelete') || !cAll.includes('function batchAddTag') || !cAll.includes('function batchSetColor'))
      fail('Batch operations missing');
    else ok('Batch operations present');
    if (!c.includes('jb-select-toggle') || !c.includes('jb-batch-bar') || !c.includes('jb-check') || !c.includes('jb-undo'))
      fail('Bulk-manager UI classes missing');
    else ok('Bulk-manager UI (select/batch/checkbox/undo) present');
  }

  // 8h) Study Questions / Input Fields (v2.27.0, beta-only)
  if (isBeta) {
    if (!cAll.includes('function buildInputFieldRow') || !cAll.includes('function saveInputField') || !cAll.includes('function deleteInputField'))
      fail('Input Field (Study Answers) functions missing');
    else ok('Input Field (Study Answers) functions present');
    if (!cAll.includes("['inputfields',t('tab_inputfields')]") || !cAll.includes('state.allInputFields'))
      fail('Study Answers tab wiring missing');
    else ok('Study Answers tab wired');
  }

  // 8i) Note sharing (v2.28.0 in-Browse quick share + v2.30.0 dedicated page)
  if (isBeta) {
    if (!cAll.includes('function openShareExport') || !cAll.includes('function buildShareEnvelope'))
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
    const expectedCards = c.includes('svc-reading') ? 6 : 5; // Reading Companion ships beta-first
    if (cards === expectedCards) ok(expectedCards + ' service cards present');
    else fail('Expected ' + expectedCards + ' .svc-card, got ' + cards);
    // Backup Doctor sits 2nd, right after the Merge tool
    if (/svc-card svc-card-merge[\s\S]*?svc-card svc-doctor/.test(c))
      ok('Backup Doctor card placed directly after Merge tool');
    else fail('Backup Doctor card not positioned after Merge tool');
    for (const k of ['svc_merge_t', 'svc_doctor_t', 'svc_explorer_t', 'svc_stats_t', 'svc_share_t'])
      if (!c.includes('data-i18n="' + k + '"')) fail('Service card i18n key missing: ' + k);
    // v2.87.1: Resurface is now an embedded panel (no standalone tool card),
    // mounted inside the merge celebration card via the shared engine.
    if (isBeta) {
      if (cAll.includes('data-jwc-resurface') && cAll.includes('js/resurface.js'))
        ok('Resurface embedded in celebration card (shared engine wired)');
      else fail('Resurface celebration integration missing');
      if (!c.includes('class="svc-card svc-resurface"'))
        ok('Standalone Resurface tool card removed');
      else fail('Standalone Resurface tool card should be gone');
    }
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
    if (!/<\/div>[\s\S]{0,300}<select id="landing-lang-select"/.test(c))
      fail('Language picker not moved out of .site-nav-links (two-level nav)');
    else ok('Two-level nav: language picker is a direct #site-nav child');
  }

  // 8m) Receive shared notes in merge (v2.34.0, beta-only)
  if (isBeta) {
    if (cAll.includes('window.__jwAdoptSharedIntoBuffer') && cAll.includes('window.__jwParseShareEnvelope'))
      ok('Receive-in-merge core API present');
    else fail('Receive-in-merge core API missing');
    if (cAll.includes('data-jwc-addshared') && cAll.includes('window.__jwReceivePickAndAdopt'))
      ok('End-of-merge "add shared notes" button wired');
    else fail('End-of-merge add-shared button missing');
    if (cAll.includes('window.__jwReceiveOnCelebration') && cAll.includes('jwr-panel'))
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
    if (!cAll.includes('function buildPerfHtml') || !cAll.includes('jwc-perf') || !cAll.includes('__jwLastMergeTimings'))
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
    if (!cAll.includes('__jwInjectMergeDemo')) fail('merge-demo injector helper not referenced');
    else ok('merge-demo injector helper referenced (__jwInjectMergeDemo)');
    if (!cAll.includes('__jwBuildDemoBackups')) fail('demo builder helper not referenced');
    else ok('demo builder helper referenced (__jwBuildDemoBackups)');
    if (!cAll.includes('jw-demo-banner')) fail('demo guidance banner id missing');
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
    if (!cAll.includes('window.__jwOpenDemo')) fail('window.__jwOpenDemo not exposed');
    else ok('window.__jwOpenDemo exposed for React buttons');
    if (!c.includes('data-demo-trigger')) fail('data-demo-trigger attribute missing');
    else ok('data-demo-trigger attribute present');

    // Guided in/out flow (v2.14.0)
    if (!cAll.includes('EXPORT_GUIDE')) fail('EXPORT_GUIDE object missing (export walkthrough)');
    else ok('EXPORT_GUIDE export-steps object present');
    if (!cAll.includes('window.__jwOpenGuide')) fail('window.__jwOpenGuide not exposed');
    else ok('window.__jwOpenGuide exposed');
    if (!c.includes('id="landing-howto-btn"')) fail('landing-howto-btn missing');
    else ok('landing "How it works" button present');
    if (!c.includes('data-howto-trigger')) fail('data-howto-trigger attribute missing');
    else ok('data-howto-trigger attribute present');
    if (!cAll.includes('jwrg-mode')) fail('jwrg-mode IN/OUT toggle markup missing');
    else ok('guide IN/OUT mode toggle (.jwrg-mode) present');

    // Robust error handling + Browse pagination (v2.15.0)
    if (!c.includes('jb-pager')) fail('Browse pager markup/CSS missing (.jb-pager)');
    else ok('Browse pagination (.jb-pager) present');
    if (!cAll.includes('PAGE_SIZE')) fail('Browse PAGE_SIZE constant missing');
    else ok('Browse PAGE_SIZE windowing present');

    // Pre-merge impact preview (v2.16.0)
    if (!cAll.includes('window.__jwImpactPreview')) fail('window.__jwImpactPreview module missing');
    else ok('pre-merge impact preview (__jwImpactPreview) present');
    if (!c.includes('jip-card')) fail('impact preview markup/CSS missing (.jip-card)');
    else ok('impact preview modal (.jip-card) present');

    // Rich-text note editing (v2.17.0)
    if (!cAll.includes('sanitizeNoteHtml')) fail('sanitizeNoteHtml allow-list sanitizer missing');
    else ok('sanitizeNoteHtml sanitizer present');
    if (!cAll.includes('buildRteEditor')) fail('buildRteEditor (WYSIWYG) missing');
    else ok('rich-text editor (buildRteEditor) present');
    if (!c.includes('jb-edit-rte')) fail('rich-text editor markup/CSS missing (.jb-edit-rte)');
    else ok('rich-text editor (.jb-edit-rte) present');
    if (!c.includes('MutationObserver')) fail('MutationObserver not wired in demo handler');
    else ok('MutationObserver present (catches React-rendered demo buttons)');

    // 10) Lazy-load infrastructure (v2.7.0)
    //   - CDN script tags must NOT be in <head> (eager loading would defeat the point)
    //   - The main app and Browse module must be wrapped in __bootApp / __bootBrowse
    //   - The boot loader must expose __jwBootApp / __jwBootBrowse
    const headEnd = c.indexOf('</head>');
    const headSection = c.slice(0, headEnd);
    // Any known CDN host, not just cdnjs — the boot loader now pulls Lucide
    // from jsDelivr, and an eager <script src> to *any* of them defeats the
    // lazy load just as thoroughly.
    if (/<script[^>]*src="https:\/\/(cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|unpkg\.com)/.test(headSection)) {
      fail('CDN <script src> still present in <head> — lazy-load broken');
    } else {
      ok('no eager CDN <script> tags in <head>');
    }

    // ── Every CDN URL the boot loader ships must actually exist ────────────
    // Lucide was requested from cdnjs for months and 404'd every single time:
    // cdnjs does not host the library at all, under any path. Nothing caught
    // it because the loader treats icons as decorative and swallows the error.
    // So the URLs are pinned here the same way the jw.org wtlocale codes are
    // pinned in 16_reading.js — each one confirmed with a real request:
    //   curl -sSI <url>   ->   200
    const VERIFIED_CDN = [
      'https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js',
      'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js',
      'https://cdn.jsdelivr.net/npm/lucide@0.292.0/dist/umd/lucide.min.js',
    ];
    const loaderStart = c.indexOf('Lazy boot loader');
    const cdnMap = c.slice(loaderStart, c.indexOf('var loaders', loaderStart));
    const shippedCdn = (cdnMap.match(/'https:\/\/[^']+'/g) || []).map(s => s.slice(1, -1));
    if (!shippedCdn.length) {
      fail('boot loader CDN map not found — cannot verify library URLs');
    } else {
      const unverified = shippedCdn.filter(u => VERIFIED_CDN.indexOf(u) === -1);
      if (unverified.length) {
        fail('boot loader requests unverified CDN URL(s): ' + unverified.join(', ') +
          ' — confirm each returns 200 and add it to VERIFIED_CDN');
      } else {
        ok(`all ${shippedCdn.length} boot-loader CDN URLs are verified-reachable`);
      }
      const missing = VERIFIED_CDN.filter(u => shippedCdn.indexOf(u) === -1);
      if (missing.length) fail('verified CDN URL no longer shipped: ' + missing.join(', '));
    }

    // ── Transient failures must be retried ────────────────────────────────
    // A <script> tag reports a 503 and a 404 identically (bare onerror, no
    // status), so one flaky edge response used to drop the visitor on the
    // fatal-error screen. Cloudflare served exactly that for js/app.js and
    // js/browse.js.
    if (!c.includes('loadWithRetry')) {
      fail('boot loader has no retry — a single transient 503 kills the app');
    } else {
      ok('boot loader retries failed script loads');
      for (const bundle of ['js/app.js', 'js/browse.js']) {
        const re = new RegExp("loadWithRetry\\('" + bundle.replace('.', '\\.') + "'");
        if (!re.test(c)) fail(bundle + ' bundle loader does not go through loadWithRetry');
        else ok(bundle + ' loaded with retry');
      }
      if (!/loadWithRetry\(CDN\[name\]/.test(c)) fail('CDN libraries not loaded with retry');
      else ok('CDN libraries loaded with retry');
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
    if (!cAll.includes('jw-demo-loading')) fail('demo loading state CSS class missing');
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
    if (!c.includes("'js/app.js'") || !c.includes("appLink.rel = 'prefetch'")) {
      fail('js/app.js not in the hover/idle prefetch list');
    } else { ok('js/app.js is in the prefetch list'); }

    // v3.8.0: the Browse module is external and lazy too.
    if (/<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<script>[\s\S]*?<\/script>\s*<!-- ── End Note Explorer/.test(c)) {
      fail('Browse module still inline in HTML (extraction did not happen)');
    } else { ok('Browse module NOT inline in beta/index.html (extracted)'); }
    if (!fs.existsSync(REPO + '/beta/js/browse.js')) fail('beta/js/browse.js does not exist');
    else {
      const b = fs.readFileSync(REPO + '/beta/js/browse.js', 'utf8');
      if (b.includes('window.__bootBrowse = function()')) ok('beta/js/browse.js exists and defines __bootBrowse');
      else fail('beta/js/browse.js missing the __bootBrowse wrapper');
    }
    if (!c.includes('function loadBrowseBundle()')) fail('boot loader missing loadBrowseBundle()');
    else ok('boot loader has loadBrowseBundle()');
    if (/<script[^>]*src=["']js\/browse\.js["']/.test(c)) {
      fail('js/browse.js eagerly loaded via <script src>');
    } else { ok('js/browse.js NOT eagerly loaded'); }
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
    if (!cAll.includes('jw-celebrate-overlay')) fail('celebration overlay id missing');
    else ok('celebration overlay referenced (#jw-celebrate-overlay)');
    if (!cAll.includes('jw-restore-overlay')) fail('restore guide overlay id missing');
    else ok('restore guide overlay referenced (#jw-restore-overlay)');
    // Stats query path uses sql.js for the merged db
    if (!cAll.includes('SELECT COUNT(*) FROM Note')) fail('celebration not querying merged db');
    else ok('celebration queries merged db via sql.js');
    // Translations: all 12 langs must have the celebration keys
    for (const lang of FILE_LANGS) {
      const re = new RegExp(KEY(lang) + '\\s*\\{[^}]*cele_title:');
      if (!re.test(cAll)) fail(`celebration i18n missing for ${lang}`);
    }
    ok('celebration i18n present for all 12 languages');
    // Restore guide steps for each platform
    for (const platform of ['ios', 'android', 'other']) {
      const re = new RegExp(`${platform}:\\s*\\[`);
      if (!re.test(cAll)) fail(`restore guide steps missing for platform: ${platform}`);
    }
    ok('restore guide steps defined for ios / android / other');
    if (!css.includes('#jw-celebrate-overlay')) fail('beta/styles.css missing #jw-celebrate-overlay rule');
    else ok('beta/styles.css defines #jw-celebrate-overlay');
    if (!css.includes('#jw-restore-overlay')) fail('beta/styles.css missing #jw-restore-overlay rule');
    else ok('beta/styles.css defines #jw-restore-overlay');

    // 14) v2.9.1: auto-download + manual download button + donate link
    if (!cAll.includes('data-jwc-download')) fail('celebration missing Download button (data-jwc-download)');
    else ok('celebration has Download button');
    if (!cAll.includes('triggerDownload')) fail('celebration missing triggerDownload function (auto-download path)');
    else ok('celebration auto-download path (triggerDownload) present');
    if (!cAll.includes('autoDownloadedFor')) fail('celebration missing auto-download dedup guard');
    else ok('celebration auto-download one-shot guard present');
    if (!cAll.includes('paypal.com/paypalme/jwsync')) fail('donate link URL missing');
    else ok('donate link URL present (PayPal)');
    if (!cAll.includes('data-jwc-donate')) fail('donate link hook missing');
    else ok('donate link has data-jwc-donate hook');
    // Donate prompt/cta strings translated for all 12 langs
    for (const lang of FILE_LANGS) {
      const re = new RegExp(KEY(lang) + '\\s*\\{[^}]*donate_prompt:');
      if (!re.test(cAll)) fail(`donate i18n missing for ${lang}`);
    }
    ok('donate i18n present for all 12 languages');
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
    // Localised switcher labels for all 12 languages
    for (const lang of EXPECTED_LANGS) {
      const re = new RegExp(KEY(lang) + '\\s*\\{\\s*merge:');
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
    if (navExpOk) ok('nav_explorer localised for all 12 languages');
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

// Merge Wizard + privacy badge (beta first) — markers, hooks, i18n coverage
{
  section('Merge Wizard + privacy badge (beta)');
  const beta = withModules(REPO + '/beta/index.html');
  const blockCount = (beta.match(/<!-- ── Merge Wizard \+ Privacy Badge ─/g) || []).length;
  if (blockCount === 1) ok('Merge Wizard block present exactly once');
  else fail('Merge Wizard block count = ' + blockCount);

  for (const cls of ['jw-priv-badge', 'jw-how-btn', 'jw-wiz-ov', 'jw-wiz-card',
    'jw-wiz-steps', 'jw-wiz-num', 'jw-wiz-start', 'jw-wiz-skip',
    'jw-wiz-tab', 'jw-wiz-tools', 'jw-wiz-tool', 'jw-wiz-tool-open']) {
    if (beta.includes('.' + cls)) ok('wizard CSS class defined: .' + cls);
    else fail('wizard CSS class missing: .' + cls);
  }

  // "Other tools" tab explains the Explorer / Stats+Awards / Share tools
  if (beta.includes('data-jw-tab="merge"') && beta.includes('data-jw-tab="tools"') &&
      beta.includes('data-jw-pane="tools"'))
    ok('wizard has Merging + Other tools tabs');
  else fail('wizard tool tabs missing');
  if (beta.includes("toolHtml('explorer'") && beta.includes("toolHtml('stats'") &&
      beta.includes("toolHtml('share'"))
    ok('Other tools tab covers Explorer, Stats and Share');
  else fail('Other tools tab tool list incomplete');
  if (beta.includes('data-jw-open=') && beta.includes('function openTool'))
    ok('each tool has a working Open action');
  else fail('tool Open dispatch missing');

  if (beta.includes('id="jw-how-btn"') && beta.includes('data-i18n="svc_heading"'))
    ok('"How it works" trigger present above the tool chooser');
  else fail('"How it works" trigger not placed above the tool chooser');
  if (!beta.includes('setTimeout(openWizard'))
    ok('wizard does not auto-open (opens only on click)');
  else fail('wizard still auto-opens on first run');
  if (beta.includes('window.__jwOpenGuide') && beta.includes('data-jw-guide'))
    ok('wizard reuses the existing export/restore guide via __jwOpenGuide');
  else fail('wizard guide hand-off missing');
  if (beta.includes('window.__jwOpenWizard')) ok('wizard reopen hook exposed (__jwOpenWizard)');
  else fail('wizard reopen hook missing');
  if (beta.includes('input[type="file"][accept=".jwlibrary"]:not([multiple])'))
    ok('privacy badge targets the main file picker');
  else fail('privacy badge picker selector missing');

  // i18n: the wizard W object must cover every language with the required keys
  const wm = beta.match(/__jwWizardInit[\s\S]*?var W=\{([\s\S]*?)\n {2}\};/);
  if (!wm) { fail('wizard i18n object (W) not found'); }
  else {
    const WIZ_KEYS = ['close','badge','how','title','sub','s1t','s1d','s1btn',
      's2t','s2d','s3t','s3d','s3btn','start','skip',
      'tab1','tab2','t_intro','exp_d','stat_d','shr_d','open'];
    let wizI18nOk = true;
    for (const lang of EXPECTED_LANGS) {
      const re = new RegExp(KEY(lang) + '\\{([\\s\\S]*?)\\}\\s*(?:,|$)');
      const lm = wm[1].match(re);
      if (!lm) { wizI18nOk = false; fail('wizard i18n missing language: ' + lang); continue; }
      const missing = WIZ_KEYS.filter(k => !new RegExp('(^|[,{])' + k + ':').test(lm[1]));
      if (missing.length) { wizI18nOk = false; fail('wizard i18n ' + lang + ' missing keys: ' + missing.join(',')); }
    }
    if (wizI18nOk) ok('wizard i18n covers all 12 languages × ' + WIZ_KEYS.length + ' keys');
  }
}

// Exactly one canonical per page, pointing where that page should point.
{
  section('Canonical tags are singular and correct');
  const WANT = {
    'index.html': 'https://jwsync.org/',
    // The beta shell canonicalises to itself, not to production: it is a
    // separate noindex document. It briefly carried both and so contradicted
    // itself.
    'beta/index.html': 'https://jwsync.org/beta/',
    'highlights.html': 'https://jwsync.org/highlights',
    'share.html': 'https://jwsync.org/share',
    'forum.html': 'https://jwsync.org/forum',
  };
  for (const [f, want] of Object.entries(WANT)) {
    const c = fs.readFileSync(REPO + '/' + f, 'utf8');
    const all = c.match(/<link rel="canonical" href="([^"]*)">/g) || [];
    if (all.length !== 1) { fail(f + ': ' + all.length + ' canonical tags', all.join(' ')); continue; }
    const href = all[0].match(/href="([^"]*)"/)[1];
    if (href === want) ok(f + ' -> ' + href);
    else fail(f + ': canonical is ' + href + ', expected ' + want);
  }
}

// Generated <head> blocks must be replaced on rebuild, never stacked.
{
  section('SEO marker blocks are singular');
  const PAGES = ['index.html', 'beta/index.html', 'highlights.html',
    'beta/highlights.html', 'share.html', 'beta/share.html', 'forum.html'];
  let bad = 0;
  for (const f of PAGES) {
    const c = fs.readFileSync(REPO + '/' + f, 'utf8');
    for (const name of ['oglocale', 'hreflang']) {
      const opens = (c.match(new RegExp('<!-- SEO:' + name + ' -->', 'g')) || []).length;
      // Only the landing page has per-language twins to point at.
      const want = name === 'hreflang' ? (f === 'index.html' ? 1 : 0) : 1;
      if (opens !== want) { fail(f + ': ' + opens + ' SEO:' + name + ' block(s), expected ' + want); bad++; }
    }
  }
  if (!bad) ok('every page has exactly one og:locale block and no hreflang block');
}

// ── Nothing user-facing may be hardcoded English ─────────────────────────
// Three surfaces shipped English to all thirteen languages for a long time
// because nothing checked them: the navbar (labels + every title= tooltip),
// the in-app language picker (which silently stopped at Swedish, so Cebuano
// users could not switch back to Cebuano), and the whole community forum.
{
  section('No hardcoded English in the app navbar');
  const appJs = fs.readFileSync(REPO + '/js/app.js', 'utf8');
  const navStart = appJs.indexOf('id:"jw-navbar"');
  if (navStart < 0) {
    fail('could not locate the navbar render');
  } else {
    const nav = appJs.slice(navStart, navStart + 4000);
    // Literals that used to sit in the render. Each must now be an s() lookup.
    const FORBIDDEN = [
      '"Advanced options"', '"‹ Simple view"', '"Show advanced tools"',
      '"Back to the simple view"', '"Simple — step', '"Full Mode — all',
      '"Try with sample notes"', '"Open Note Explorer"', '"Community — ',
      '"Open on another device"', '"Switch to Light Mode"', '"Switch to Dark Mode"',
      '⚡ Full"', '✦ Simple"', ' Community"', ' Share"',
    ];
    const found = FORBIDDEN.filter(f => nav.includes(f));
    if (!found.length) ok('navbar renders every label and tooltip through s()');
    else fail(found.length + ' hardcoded English string(s) in the navbar', found.join(' | '));

    // The keys those lookups need, in every language.
    // The mode_* and nav_simple_view/nav_adv_*_title keys used to be listed
    // here. They described a navbar that no longer exists — v3.32.0 removed the
    // mode toggle — and were swept out of every language in v3.35.1.
    const NAV_KEYS = ['nav_adv_options', 'nav_demo_title', 'nav_browse_title',
      'nav_community_title', 'nav_share_btn', 'nav_share_title',
      'theme_to_light', 'theme_to_dark'];
    let missing = [];
    for (const k of NAV_KEYS) {
      const n = (appJs.match(new RegExp('[,{]' + k + ':', 'g')) || []).length;
      if (n !== EXPECTED_LANGS.length) missing.push(k + ' x' + n);
    }
    if (!missing.length)
      ok('all ' + NAV_KEYS.length + ' navbar keys present in ' + EXPECTED_LANGS.length + ' languages');
    else fail('navbar key coverage gaps: ' + missing.join(', '));
  }

  // Two independent ?lang= allow-lists exist: `var V=[…]` at the top of
  // index.html, and `V=[…]` inside the jw-dir-init snippet that every page
  // carries. The plumbing scripts patch the first (it has `var`); the snippet
  // is written by add_rtl_wiring.py. They diverged once — uk and pl reached the
  // first and not the second — which broke ?lang= persistence on the satellite
  // pages, the precise failure the snippet exists to prevent. Assert they agree
  // on every page.
  section('The two ?lang= allow-lists agree on every page');
  {
    const idx = fs.readFileSync(REPO + '/index.html', 'utf8');
    const canonical = (idx.match(/var (V=\[[^\]]*\])/) || [])[1];
    if (!canonical) fail('could not read the ?lang= allow-list from index.html');
    else {
      const PAGES = ['index.html', 'beta/index.html', 'highlights.html',
        'beta/highlights.html', 'share.html', 'beta/share.html', 'forum.html'];
      let bad = 0;
      for (const f of PAGES) {
        const c = fs.readFileSync(REPO + '/' + f, 'utf8');
        const i = c.indexOf('jw-dir-init');
        if (i < 0) { fail(f + ': no jw-dir-init snippet'); bad++; continue; }
        const snip = c.slice(i, c.indexOf('</script>', i));
        const got = (snip.match(/V=\[[^\]]*\]/) || [])[0];
        if (got !== canonical) {
          fail(f + ': dir-bootstrap allow-list differs from index.html', got || '(none)');
          bad++;
        }
      }
      if (!bad) ok('all ' + PAGES.length + ' pages carry the same allow-list as index.html');
    }
  }

  section('In-app language picker lists every language');
  {
    const appJs = fs.readFileSync(REPO + '/js/app.js', 'utf8');
    const m = appJs.match(/NAV_LANGS=\[(.*?)\],TRANSLATIONS=/s);
    if (!m) fail('NAV_LANGS not found — picker may be hand-written again');
    else {
      const codes = [...m[1].matchAll(/\["([A-Za-z-]{2,12})",/g)].map(x => x[1]);
      const missing = EXPECTED_LANGS.filter(l => !codes.includes(l));
      if (!missing.length) ok('picker offers all ' + codes.length + ' languages');
      else fail('picker is missing: ' + missing.join(', '));
      if (appJs.includes('NAV_LANGS.map(')) ok('picker is generated from the list, not hand-written');
      else fail('picker no longer renders from NAV_LANGS');
    }
  }

  // The <select> in the HTML is a *second*, independent picker from NAV_LANGS,
  // and nothing checked it until Romanian shipped listed twice in it. The
  // plumbing script had been run a second time and re-inserted the option,
  // because its idempotency guard asked whether the anchor was still present
  // rather than whether the language already was. Duplicates in a dropdown are
  // visible to every user and no other check looked here.
  section('HTML language picker lists each language exactly once');
  {
    ['index.html', 'beta/index.html'].forEach(rel => {
      const html = fs.readFileSync(path.join(REPO, rel), 'utf8');
      const codes = [...html.matchAll(/<option value="([A-Za-z-]{2,12})">/g)]
        .map(x => x[1]).filter(c => EXPECTED_LANGS.includes(c));
      const dupes = codes.filter((c, i) => codes.indexOf(c) !== i);
      if (dupes.length) {
        fail(rel + ': picker lists twice: ' + [...new Set(dupes)].join(', '));
      } else if (codes.length !== EXPECTED_LANGS.length) {
        const missing = EXPECTED_LANGS.filter(l => !codes.includes(l));
        fail(rel + ': picker is missing: ' + missing.join(', '));
      } else {
        ok(rel + ': ' + codes.length + ' options, no duplicates');
      }
    });
  }

  section('Community forum is translated');
  {
    const forum = fs.readFileSync(REPO + '/forum.html', 'utf8');
    const forumJs = fs.readFileSync(REPO + '/js/forum.js', 'utf8');
    // v3.33.0: the dictionary moved out of forum.html into a shared file. It
    // used to be checked only where it happened to live, which is why nobody
    // noticed that the app's own copy of the forum had no dictionary at all.
    const forumI18n = fs.readFileSync(REPO + '/js/forum-i18n.js', 'utf8');
    const m = forumI18n.match(/window\.__FORUM_I18N=(\{.*\});\s*\n\(function\(\)\{/s);
    if (!m) { fail('__FORUM_I18N dictionary missing from js/forum-i18n.js'); }
    else {
      let dict;
      try { dict = JSON.parse(m[1]); } catch (e) { dict = null; fail('__FORUM_I18N does not parse'); }
      if (dict) {
        const langs = Object.keys(dict);
        const missing = EXPECTED_LANGS.filter(l => !langs.includes(l));
        if (!missing.length) ok('forum dictionary covers all ' + langs.length + ' languages');
        else fail('forum dictionary missing: ' + missing.join(', '));

        const enKeys = Object.keys(dict.en || {});
        const gaps = [];
        for (const l of langs) {
          const miss = enKeys.filter(k => !(k in dict[l]));
          if (miss.length) gaps.push(l + ':' + miss.slice(0, 3).join(','));
        }
        if (!gaps.length) ok('every forum key present in every language (' + enKeys.length + ' keys)');
        else fail('forum key gaps: ' + gaps.join(' | '));

        // Counted strings must carry CLDR plural categories, not a bare string:
        // Arabic needs six forms and Russian four, and "3 ردًا" is wrong.
        for (const l of ['ar', 'ru']) {
          const v = dict[l] && dict[l].n_replies;
          if (v && typeof v === 'object' && v.few && v.other)
            ok(l + ': reply count uses plural categories (few/other present)');
          else fail(l + ': n_replies is not plural-aware — counts 3-10 would be wrong');
        }
      }
    }

    // Markup hooks, on every surface that renders the forum. forum.html was
    // the only one checked before, and the embedded copy inside index.html
    // carried no hooks at all — hardcoded English behind a language picker.
    const SURFACES = [
      ['forum.html', forum],
      ['index.html', fs.readFileSync(REPO + '/index.html', 'utf8')],
      ['beta/index.html', fs.readFileSync(REPO + '/beta/index.html', 'utf8')],
    ];
    for (const [name, src] of SURFACES) {
      const scope = name === 'forum.html' ? src
        : src.slice(src.indexOf('<div id="forum-view"'), src.indexOf('<!-- ── End embedded forum view'));
      const n = (scope.match(/data-i18n[=-]/g) || []).length;
      if (n >= 25) ok(name + ': forum markup carries ' + n + ' i18n hooks');
      else fail(name + ': forum markup has only ' + n + ' i18n hooks (expected >= 25)');
      // Loading js/forum.js without the dictionary is the exact shape of the
      // bug: FT() then renders its own argument, e.g. "cat_feature".
      if (!src.includes('js/forum.js')) continue;
      const iDict = src.indexOf('js/forum-i18n.js'), iJs = src.indexOf('js/forum.js');
      if (iDict >= 0 && iDict < iJs) ok(name + ': loads the dictionary before js/forum.js');
      else fail(name + ': loads js/forum.js without the dictionary ahead of it');
    }
    if (forumI18n.includes('window.__forumT') && forumI18n.includes('window.__forumApplyI18N'))
      ok('shared applier exposes __forumT and __forumApplyI18N');
    else fail('forum i18n applier missing from js/forum-i18n.js');
    if (!/const\s+catLabel\s*=/.test(forum))
      ok('forum.html has no second copy of the forum runtime');
    else fail('forum.html carries an inline forum implementation — it will drift out of translation');

    // Runtime copy must go through FT(), not literals.
    const LEFTOVERS = ["'Please add a title.'", "'Posted! ✓'", "'Already upvoted!'",
      "'No posts yet'", "'Be the first to post!'", "'just now'", "' ago'",
      "'No replies yet", "'Posting…'", '>Try again<', 'Loading replies…',
      '>Copy link', '✓ Solved<', "Couldn't load posts"];
    const stuck = LEFTOVERS.filter(s => forumJs.includes(s));
    if (!stuck.length) ok('forum runtime strings all read from the dictionary');
    else fail(stuck.length + ' hardcoded string(s) left in js/forum.js', stuck.join(' | '));
    if (forumJs.includes('const FT =')) ok('js/forum.js has the FT() lookup helper');
    else fail('FT() helper missing from js/forum.js');
  }
}

// Canonical hygiene — every submitted URL must be its own canonical.
// The original lesson: ?lang= variants serve byte-identical English HTML that
// canonicalises to "/", so submitting them — or pointing hreflang at them —
// made Search Console report the whole set as "Alternate page with proper
// canonical tag", indexing nothing extra.
// That rule is unchanged. What changed is that real per-language documents now
// exist at /<lang>/ (build_landing.py), so hreflang is legitimate again — but
// only ever between distinct paths, never at a query parameter.
{
  section('Canonical hygiene (sitemap + hreflang)');
  const sm = fs.readFileSync(REPO + '/sitemap.xml', 'utf8');
  const locs = (sm.match(/<loc>([^<]+)<\/loc>/g) || [])
    .map(s => s.match(/<loc>([^<]+)<\/loc>/)[1]);

  const paramLocs = locs.filter(u => u.includes('?'));
  if (!paramLocs.length) ok('sitemap.xml submits no parameterised URLs');
  else fail('sitemap.xml submits URLs that canonicalise elsewhere: ' + paramLocs.join(', '));

  // the asset server 307s /foo.html -> /foo, so a .html <loc> submits a redirect
  const htmlLocs = locs.filter(u => u.endsWith('.html'));
  if (!htmlLocs.length) ok('sitemap.xml submits no .html URLs (server redirects those)');
  else fail('sitemap.xml submits redirecting .html URLs: ' + htmlLocs.join(', '));

  if (locs.includes('https://jwsync.org/')) ok('sitemap.xml submits the landing page');
  else fail('sitemap.xml is missing https://jwsync.org/');

  // A noindex page must never be submitted, and a submitted page must never be
  // noindex. Shipping both signals is not a no-op: the sitemap asks Google to
  // index the URL and the meta tag refuses, so the URL lands in Search
  // Console's "Excluded by 'noindex' tag" report — once per ?lang= and .html
  // permutation that the language pickers and guide footers link to. /share
  // and /highlights sat in exactly that state and filled the report between
  // them. Whichever way a page is settled, the two signals must agree.
  {
    const pages = [
      ['index.html', 'https://jwsync.org/'],
      ['highlights.html', 'https://jwsync.org/highlights'],
      ['share.html', 'https://jwsync.org/share'],
      ['forum.html', 'https://jwsync.org/forum'],
      ['guides/index.html', 'https://jwsync.org/guides/'],
      ['guides/backup-jw-library.html', 'https://jwsync.org/guides/backup-jw-library'],
    ];
    for (const [f, url] of pages) {
      const src = fs.readFileSync(REPO + '/' + f, 'utf8');
      const head = src.slice(0, src.indexOf('</head>'));
      const tag = (head.match(/<meta name="robots" content="([^"]*)"/) || [])[1];
      if (tag === undefined) { fail(f + ': no robots meta at all'); continue; }
      const noindex = /noindex/i.test(tag);
      const submitted = locs.includes(url);
      if (noindex && submitted)
        fail(f + ': noindex but submitted in sitemap.xml as ' + url +
             ' — contradictory signals, drop one');
      else if (!noindex && !submitted)
        fail(f + ': indexable but missing from sitemap.xml (' + url + ')');
      else
        ok(f + ': robots "' + tag + '" agrees with sitemap (' +
           (submitted ? 'submitted' : 'withheld') + ')');
    }
  }

  for (const f of ['index.html', 'beta/index.html']) {
    const head = (() => { const c = fs.readFileSync(REPO + '/' + f, 'utf8'); return c.slice(0, c.indexOf('</head>')); })();
    const alts = (head.match(/<link rel="alternate" hreflang="[A-Za-z-]+" href="([^"]*)"/g) || [])
      .map(s => s.match(/href="([^"]*)"/)[1]);
    const param = alts.filter(u => u.includes('?'));
    if (param.length) fail(f + ': hreflang points at parameterised URLs: ' + param.join(', '));
    else ok(f + ': no hreflang points at a canonicalised-away ?lang= URL');
    // beta is noindex and has no per-language twins, so it declares none.
    const wantCluster = f === 'index.html';
    if (wantCluster && alts.length === EXPECTED_LANGS.length + 1)
      ok(f + ': hreflang cluster covers ' + EXPECTED_LANGS.length + ' languages + x-default');
    else if (wantCluster)
      fail(f + ': cluster has ' + alts.length + ' entries, expected ' + (EXPECTED_LANGS.length + 1));
    else if (!alts.length) ok(f + ': declares no hreflang (noindex, no per-language twins)');
    else fail(f + ': ' + alts.length + ' hreflang on a noindex page');
    // ?lang= must still select the UI language, it just must not rewrite canonical
    if (head.includes("localStorage.setItem('jwsync_lang',p)")) ok(f + ': ?lang= still sets the UI language');
    else fail(f + ': ?lang= no longer sets the UI language');
    if (!/can\.href *= *u/.test(head)) ok(f + ': canonical is static, not rewritten by JS');
    else fail(f + ': JS still rewrites the canonical link');
    if (head.includes('og:locale:alternate')) ok(f + ': og:locale:alternate advertises the other locales');
    else fail(f + ': og:locale:alternate missing');
  }
}

// Canonical URLs must not point at a URL the server redirects away from
{
  section('Canonical targets resolve directly');
  for (const f of ['forum.html', 'guides/index.html', 'guides/backup-jw-library.html']) {
    const c = fs.readFileSync(REPO + '/' + f, 'utf8');
    const m = c.match(/<link rel="canonical" href="([^"]+)">/);
    if (!m) { fail(f + ': no canonical'); continue; }
    if (!m[1].endsWith('.html')) ok(f + ': canonical -> ' + m[1]);
    else fail(f + ': canonical points at a redirecting .html URL (' + m[1] + ')');
  }
}

// Merge celebration — Share card (Web Share + branded image, 12 langs)
{
  section('Merge celebration Share card');
  const beta = withModules(REPO + '/beta/index.html');
  if (beta.includes('data-jwc-share')) ok('Share button present in celebration actions');
  else fail('Share button missing from celebration');
  if (beta.includes('function buildMergeCard') && beta.includes('toBlob'))
    ok('branded result image generator present (buildMergeCard)');
  else fail('share image generator missing');
  if (beta.includes('function shareMerge') && beta.includes('navigator.canShare') &&
      beta.includes('navigator.clipboard'))
    ok('shareMerge uses Web Share with download + copy-link fallback');
  else fail('shareMerge / fallbacks missing');
  if (beta.includes('openSharePreview(cached && cached.stats)'))
    ok('Share button wired to the real merge stats (via share preview)');
  else fail('Share button not wired');

  // Share-preview overlay (Instagram/social) — shows the card, then shares
  if (beta.includes('function openSharePreview') &&
      beta.includes('jw-share-overlay') &&
      beta.includes('data-jws-share') &&
      beta.includes('data-jws-save') &&
      beta.includes('data-jws-copy'))
    ok('Share-preview overlay present with share / save / copy actions');
  else fail('Share-preview overlay (openSharePreview) missing or incomplete');
  if (beta.includes('data-jws-share') && beta.includes('shareMerge(stats)'))
    ok('Preview Share button uses the real Web Share flow');
  else fail('Preview Share button not wired to shareMerge');

  const sm = beta.match(/var SHARE_I18N=\{([\s\S]*?)\n {2}\};/);
  if (!sm) fail('SHARE_I18N object not found');
  else {
    const SHARE_KEYS = ['cele_share', 'share_headline', 'share_text',
      'share_preview_title', 'share_preview_body', 'share_save', 'share_copy',
      'share_copied', 'share_saved', 'share_hint'];
    let okAll = true;
    for (const lang of EXPECTED_LANGS) {
      const lm = sm[1].match(new RegExp(KEY(lang) + '\\{([\\s\\S]*?)\\}\\s*(?:,|$)'));
      if (!lm) { okAll = false; fail('SHARE_I18N missing language: ' + lang); continue; }
      const miss = SHARE_KEYS.filter(k => !new RegExp('(^|[,{])' + k + ':').test(lm[1]));
      if (miss.length) { okAll = false; fail('SHARE_I18N ' + lang + ' missing: ' + miss.join(',')); }
    }
    if (okAll) ok('SHARE_I18N covers all 12 languages × ' + SHARE_KEYS.length + ' keys');
  }
}

// Safe Restore confidence layer (celebration + restore guide, 12 langs)
{
  section('Safe Restore confidence layer');
  const beta = withModules(REPO + '/beta/index.html');
  if (beta.includes('function buildSafePanel')) ok('Safe Restore panel builder present');
  else fail('buildSafePanel missing');
  // used in BOTH the celebration and the restore guide (def + 2 call sites)
  if ((beta.match(/buildSafePanel\(\)/g) || []).length >= 3)
    ok('Safe Restore panel shown in celebration and restore guide');
  else fail('Safe Restore panel not wired into both places');
  if (beta.includes("'<div id=\"jwrg-warning\">' + buildSafePanel()"))
    ok('restore guide warning upgraded to the Safe Restore panel');
  else fail('restore guide still uses the old lone warning');

  const sm = beta.match(/var SAFE_I18N=\{([\s\S]*?)\n {2}\};/);
  if (!sm) fail('SAFE_I18N object not found');
  else {
    const SAFE_KEYS = ['safe_title', 'safe_originals', 'safe_master'];
    let okAll = true;
    for (const lang of EXPECTED_LANGS) {
      const lm = sm[1].match(new RegExp(KEY(lang) + '\\{([\\s\\S]*?)\\}\\s*(?:,|$)'));
      if (!lm) { okAll = false; fail('SAFE_I18N missing language: ' + lang); continue; }
      const miss = SAFE_KEYS.filter(k => !new RegExp('(^|[,{])' + k + ':').test(lm[1]));
      if (miss.length) { okAll = false; fail('SAFE_I18N ' + lang + ' missing: ' + miss.join(',')); }
    }
    if (okAll) ok('SAFE_I18N covers all 12 languages × ' + SAFE_KEYS.length + ' keys');
  }
}

// Collapsible tool sections (Extract / Bulk Color / Manage Tags)
{
  section('Collapsible tool sections');
  const beta = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
  if (beta.includes('Collapsible tool sections') && beta.includes('End Collapsible tool sections'))
    ok('collapsible tool-sections block present');
  else fail('collapsible tool-sections block missing');
  // targets the three distinctive merge-tool header icons
  if (["share", "palette", "tags"].every(i => beta.includes("'.lucide-' + n")) ||
      beta.includes("var ICONS = ['share', 'palette', 'tags']"))
    ok('targets share / palette / tags section icons');
  else fail('section icon targeting changed');
  if (beta.includes("data-jwopen") && beta.includes("data-jwtool"))
    ok('uses React-safe data-* attributes for collapse state');
  else fail('collapse state attributes missing');
  if (beta.includes("/jsdom/i.test(navigator.userAgent"))
    ok('observer guarded against JSDOM teardown');
  else fail('JSDOM guard missing (tests may crash on teardown)');
  if (beta.includes("[data-jwtool][data-jwopen=\"0\"] > :not(:first-child)"))
    ok('collapsed CSS hides body, keeps header tab');
  else fail('collapsed-state CSS missing');
}

// Backup Doctor (v2.63.0)
{
  section('Backup Doctor');
  const beta = withModules(REPO + '/beta/index.html');
  if (beta.includes('── Backup Doctor (v') && beta.includes('── End Backup Doctor'))
    ok('Backup Doctor block present');
  else fail('Backup Doctor block missing');
  if (beta.includes('window.__openJwDoctor = openDoctor'))
    ok('window.__openJwDoctor exposed');
  else fail('__openJwDoctor not exposed');
  if (beta.includes('window.__jwDoctorInternals'))
    ok('test internals (runChecks/applyFixes) exposed');
  else fail('__jwDoctorInternals missing');
  if (beta.includes('class="svc-card svc-doctor"') && beta.includes('data-i18n="svc_doctor_t"'))
    ok('Backup Doctor service card present');
  else fail('Backup Doctor service card missing');
  if (beta.includes('<span class="svc-card-new">NEW</span>'))
    ok('Backup Doctor card keeps its NEW badge');
  else fail('Backup Doctor NEW badge missing');
  // DOC_I18N coverage: all 12 languages × the load-bearing keys
  const dm = beta.match(/var DOC_I18N = \{([\s\S]*?)\n {2}\};/);
  if (!dm) fail('DOC_I18N object not found');
  else {
    const DOC_KEYS = ['title', 'sub', 'pick', 'scanning', 'c_dup_notes', 'c_empty_notes', 'c_dup_marks',
      'c_orph_br', 'c_orph_tm', 'c_unused_tags', 'c_unused_loc', 'health', 'v_a', 'v_d',
      'perfect', 'clean', 'done_t', 'safe', 'another', 'err_read', 'err_db'];
    let okAll = true;
    for (const lang of EXPECTED_LANGS) {
      const lm = dm[1].match(new RegExp(KEY(lang) + '\\{([\\s\\S]*?)\\}\\s*(?:,|$)'));
      if (!lm) { okAll = false; fail('DOC_I18N missing language: ' + lang); continue; }
      const miss = DOC_KEYS.filter(k => !new RegExp('(^|[,{])' + k + ':').test(lm[1]));
      if (miss.length) { okAll = false; fail('DOC_I18N ' + lang + ' missing: ' + miss.join(',')); }
    }
    if (okAll) ok('DOC_I18N covers all 12 languages × ' + DOC_KEYS.length + ' keys');
  }
  // landing i18n keys for the CTA card
  const lm2 = beta.match(/window\.__JW_LANDING_I18N = (\{.*?\});\n/s);
  if (!lm2) fail('__JW_LANDING_I18N not found');
  else {
    let landing = null;
    try { landing = JSON.parse(lm2[1]); } catch (_) {}
    if (!landing) fail('__JW_LANDING_I18N no longer parses as JSON');
    else {
      const missing = EXPECTED_LANGS.filter(l => !landing[l] || !landing[l].svc_doctor_t || !landing[l].svc_doctor_d);
      if (missing.length === 0) ok('svc_doctor_t/_d present in all 12 landing languages');
      else fail('landing doctor keys missing for: ' + missing.join(','));
    }
  }
}

// ── One interface: Simple Mode must not come back ────────────────────────
// Removed in v3.32.0. It was meant to be a gentle way in and did the opposite:
// it was bare enough that first-time visitors concluded the site did less than
// it does, and the two-mode toggle was itself the confusing part. What used to
// justify a second mode is now the advanced-settings disclosure below.
//
// These assertions replace the old "Discover panel → Full Mode jump" checks
// rather than deleting them, because a half-removed feature is the real risk
// here: a stray `simpleMode` pref read would silently render an empty page for
// anyone who still has simpleMode:true saved from before the change.
section('Simple Mode is gone, and stays gone');
{
  // The identifiers went in v3.32.0. The strings they used to label did not:
  // 22 keys describing the mode toggle, the "‹ Simple view" back link and the
  // Simple Mode teaser cards stayed in all 25 languages for three releases,
  // and were swept in v3.35.1.
  const DEAD = ['simpleMode', 'simple-mode-teaser', 'mode-seg-ctrl', 'mode-seg-btn',
                '__jwSetFullMode', 'discover-fullmode-btn',
                'smt_', 'mode_simple', 'mode_full', 'nav_simple_view',
                'nav_adv_show_title', 'nav_adv_back_title', 'disc_open_full'];
  for (const rel of ['js/app.js', 'beta/js/app.js', 'styles.css', 'beta/styles.css',
                     'index.html', 'beta/index.html']) {
    const src = fs.readFileSync(REPO + '/' + rel, 'utf8');
    const found = DEAD.filter(t => src.includes(t));
    if (found.length === 0) ok(rel + ': no Simple Mode remnants');
    else fail(rel + ': still references ' + found.join(', '));
  }

  // And the translation store behind them, or `i18n_tool.py inject` would put
  // every one of them straight back into js/app.js on the next language pass.
  const dataDir = path.join(REPO, 'scripts', 'i18n_data');
  const dirty = fs.readdirSync(dataDir).filter(f => f.endsWith('.json')).filter(f => {
    const src = fs.readFileSync(path.join(dataDir, f), 'utf8');
    return DEAD.some(t => src.includes(t));
  });
  if (!dirty.length) ok('scripts/i18n_data: no Simple Mode strings left to re-inject');
  else fail('scripts/i18n_data: dead Simple Mode strings in ' + dirty.join(', '));
}

// ── Advanced settings sit behind a disclosure ────────────────────────────
// The merge panel opens showing only "what to bring over"; Smart Logic, Quick
// Sync, Skip Duplicates, Deep Clean and the conflict radios are one click away.
// The label reuses nav_adv_options, which already exists in every language.
section('Advanced merge settings are deferred');
for (const appRel of ['js/app.js', 'beta/js/app.js']) {
  const src = fs.readFileSync(REPO + '/' + appRel, 'utf8');
  if (/className:"jw-adv-disclosure"/.test(src) && src.includes('s("nav_adv_options")')) {
    ok(appRel + ': disclosure button present, labelled from nav_adv_options');
  } else {
    fail(appRel + ': advanced-settings disclosure missing');
  }
  if (/advOpen&&React\.createElement\("div",\{className:"pt-4 border-t/.test(src)) {
    ok(appRel + ': Smart Logic + conflict block gated on advOpen');
  } else {
    fail(appRel + ': advanced block is not gated on advOpen');
  }
  // The always-visible half must stay visible.
  if (src.includes('s("choose_bring")') && src.includes('s("merge_settings")')) {
    ok(appRel + ': "what to bring over" still renders unconditionally');
  } else {
    fail(appRel + ': the always-visible merge settings went missing');
  }
}
for (const cssRel of ['styles.css', 'beta/styles.css']) {
  const css = fs.readFileSync(REPO + '/' + cssRel, 'utf8');
  if (css.includes('.jw-adv-disclosure')) ok(cssRel + ': .jw-adv-disclosure styled');
  else fail(cssRel + ': .jw-adv-disclosure CSS missing');
}

// ── Accessibility: one main landmark + WCAG AA text contrast ────────────
// Lighthouse flagged jwsync.org for "Document does not have a main landmark"
// and two 4.5:1 contrast failures (the contact button, the footer line).
section('Accessibility — landmark + contrast');

function relLum(hex) {
  const h = hex.replace('#', '');
  const ch = (s) => {
    const v = parseInt(s, 16) / 255;
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  };
  return 0.2126 * ch(h.slice(0, 2)) + 0.7152 * ch(h.slice(2, 4)) + 0.0722 * ch(h.slice(4, 6));
}
function contrast(a, b) {
  const la = relLum(a), lb = relLum(b);
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
}

for (const f of FILES) {
  const name = path.relative(REPO, f);
  const html = fs.readFileSync(f, 'utf8');
  const mains = (html.match(/<main\b/g) || []).length;
  if (html.includes('<main id="site-main"') && mains === 2) {
    // 2 = the page's own landmark + the embedded (hidden) forum view's
    ok(name + ': has a #site-main landmark wrapping the page content');
  } else {
    fail(name + ': expected one #site-main landmark plus the forum view\'s (<main> count: ' + mains + ')');
  }
  // white on the brand orange is 3.6:1 — the contact button uses the darker shade
  if (/mailto:jwsyncsupport@gmail\.com"[^>]*background:#c2410c/.test(html))
    ok(name + ': contact button uses the AA-contrast orange');
  else fail(name + ': contact button is back on a sub-4.5:1 orange');
  if (/<footer class="bg-stone-950[^"]*text-stone-400/.test(html))
    ok(name + ': footer body text is stone-400, not the sub-AA stone-500');
  else fail(name + ': footer text colour regressed below AA');
}
for (const cssRel of ['beta/styles.css', 'styles.css']) {
  const css = fs.readFileSync(REPO + '/' + cssRel, 'utf8');
  if (/body\.is-forum #site-main \{ display: none; \}/.test(css))
    ok(cssRel + ': page landmark hidden while the forum view shows its own');
  else fail(cssRel + ': two <main> landmarks can be visible at once on #forum');
  const badge = css.match(/\.svc-card-new \{[^}]*\}/);
  if (badge && /background: #c2410c/.test(badge[0]))
    ok(cssRel + ': NEW badge uses the AA-contrast orange');
  else fail(cssRel + ': NEW badge back on a sub-4.5:1 orange');
}
// The footer's colours come from the project's own tailwind.css, where the
// "stone" scale is a custom blue ramp — read the real values, don't assume.
const tw = fs.readFileSync(REPO + '/tailwind.css', 'utf8');
function twColor(cls, prop) {
  const m = tw.match(new RegExp('\\.' + cls + '\\{[^}]*' + prop + ':rgb\\((\\d+) (\\d+) (\\d+)'));
  return m && '#' + [m[1], m[2], m[3]].map(n => (+n).toString(16).padStart(2, '0')).join('');
}
const footerBg = twColor('bg-stone-950', 'background-color');
const footerFg = twColor('text-stone-400', 'color');
const footerOld = twColor('text-stone-500', 'color');
if (footerBg && footerFg && footerOld) {
  const now = contrast(footerFg, footerBg), before = contrast(footerOld, footerBg);
  if (now >= 4.5) ok('footer text (stone-400 on stone-950): ' + now.toFixed(2) + ':1');
  else fail('footer text below AA: ' + now.toFixed(2) + ':1');
  if (before < 4.5) ok('the old stone-500 really was below AA (' + before.toFixed(2) + ':1)');
  else fail('stone-500 now passes — this guard is testing the wrong colours');
} else {
  fail('could not read the stone palette out of tailwind.css');
}
[['#ffffff', '#c2410c', 'white on button orange'],
 ['#94a3b8', '#040f22', 'muted body text on page background']].forEach(([fg, bg, label]) => {
  const r = contrast(fg, bg);
  if (r >= 4.5) ok(label + ': ' + r.toFixed(2) + ':1');
  else fail(label + ' below AA: ' + r.toFixed(2) + ':1');
});

// ── Hard-coded language counts ──────────────────────────────────────────────
// "Available in 13 languages" sat in the Schema.org featureList of both shells
// from the release where 13 was true until the release where 22 was, because a
// count written as prose has nothing tying it to the list it counts. Nine
// languages shipped past it and no build, test or page load objected — the same
// silent-wrongness class as the jw.org wtlocale. So: derive it, or don't say it.
section('No stale language counts in shipped copy');
{
  const N = EXPECTED_LANGS.length;
  ['index.html', 'beta/index.html'].forEach(rel => {
    const html = fs.readFileSync(path.join(REPO, rel), 'utf8');
    const hits = [...html.matchAll(/(?:in|all)\s+(\d{1,3})\s+languages/g)];
    if (!hits.length) return ok(rel + ': states no language count');
    const wrong = hits.filter(m => +m[1] !== N);
    if (wrong.length) {
      fail(rel + ': claims ' + wrong.map(m => m[1]).join('/') +
           ' languages, but the site ships ' + N);
    } else {
      ok(rel + ': language count says ' + N + ', matching EXPECTED_LANGS');
    }
  });

  // Guide copy must not carry a count at all. Every translation of the
  // semantic-search guide already dropped the number; English was the last
  // page still naming one, and it named the wrong one.
  const guideSrc = fs.readFileSync(
    path.join(REPO, 'scripts', 'build_guides.py'), 'utf8');
  const inGuides = [...guideSrc.matchAll(/(?:in|all)\s+(\d{1,3})\s+languages/g)];
  if (inGuides.length) {
    fail('scripts/build_guides.py: guide copy hard-codes a language count (' +
         inGuides.map(m => m[1]).join(', ') + ') — say "every language" instead');
  } else {
    ok('guide copy names no language count');
  }
}

// ── The same rot, in the repo's own documentation ───────────────────────────
// The check above was written when README.md had gone stale at 13 languages,
// and README was brought current in the same commit — to 22. It then rotted
// straight back to 22/37 guides/836 pages/19 suites while the site moved to 25
// languages, 38 guides and 25 suites, because the guard was pointed at the
// shipped pages and not at the file describing them. CLAUDE.md drifted the same
// way and matters more: it is the first thing every session reads, and it was
// telling them the suite stopped at 21_app_boot.js while four suites after it
// ran on every push.
//
// Note the regexes here are deliberately broader than the shipped-copy one
// above: README stated its count as "**22 languages**", with no "in"/"all" in
// front, which is exactly why the existing pattern never saw it. That breadth
// is only safe because neither file may now state a count of these things that
// disagrees with the repo — so where a number is genuinely awkward to derive,
// the prose says "every page" instead of naming one.
section('Repo docs state counts that match the repo');
{
  const htmlUnder = dir => {
    let n = 0;
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (e.isDirectory()) n += htmlUnder(path.join(dir, e.name));
      else if (e.name.endsWith('.html')) n++;
    }
    return n;
  };
  const guidesDir = path.join(REPO, 'guides');
  const testsDir = path.join(REPO, 'tests');
  const suiteFiles = fs.readdirSync(testsDir)
    .filter(f => /^\d\d_.+\.js$/.test(f)).sort();

  const FACTS = [
    ['languages', /(\d[\d,]*)\s+languages/g, EXPECTED_LANGS.length],
    ['guides', /(\d[\d,]*)\s+(?:step-by-step\s+|static\s+)?guides/g,
      fs.readdirSync(guidesDir).filter(f => f.endsWith('.html') && f !== 'index.html').length],
    ['guide pages', /(\d[\d,]*)\s+pages/g, htmlUnder(guidesDir)],
    ['test suites', /(\d[\d,]*)\s+suites/g, suiteFiles.length],
    ['sitemap URLs', /(\d[\d,]*)\s+URLs/g,
      (fs.readFileSync(path.join(REPO, 'sitemap.xml'), 'utf8').match(/<loc>/g) || []).length],
  ];

  ['README.md', 'CLAUDE.md'].forEach(rel => {
    const doc = fs.readFileSync(path.join(REPO, rel), 'utf8');
    FACTS.forEach(([label, re, actual]) => {
      const hits = [...doc.matchAll(re)].map(m => +m[1].replace(/,/g, ''));
      if (!hits.length) return;
      const wrong = [...new Set(hits.filter(n => n !== actual))];
      if (wrong.length) {
        fail(rel + ': says ' + wrong.join('/') + ' ' + label +
             ', but the repo has ' + actual + ' — fix the number or stop naming one');
      } else {
        ok(rel + ': ' + label + ' count says ' + actual + ', matching the repo');
      }
    });
  });

  // Counting the suites is not enough on its own: CLAUDE.md's list stopped at
  // 21_app_boot.js for four releases, and a total would have been just as easy
  // to leave alone. Every suite on disk has to be named.
  const claude = fs.readFileSync(path.join(REPO, 'CLAUDE.md'), 'utf8');
  const unlisted = suiteFiles.filter(f => !claude.includes(f));
  if (unlisted.length) {
    fail('CLAUDE.md: suite(s) not documented — ' + unlisted.join(', '));
  } else {
    ok('CLAUDE.md names all ' + suiteFiles.length + ' suites');
  }

  const aliases = Object.keys(
    JSON.parse(fs.readFileSync(path.join(testsDir, 'package.json'), 'utf8')).scripts)
    .filter(k => k.startsWith('test:')).map(k => k.slice(5));
  const unlistedAliases = aliases.filter(a => !claude.includes(':' + a));
  if (unlistedAliases.length) {
    fail('CLAUDE.md: npm alias(es) not documented — ' + unlistedAliases.join(', '));
  } else {
    ok('CLAUDE.md names all ' + aliases.length + ' npm test aliases');
  }

  // Simple Mode went in v3.32.0. The shipped files are already guarded against
  // the identifiers coming back; README kept advertising the feature in prose,
  // which no identifier check can see.
  const readme = fs.readFileSync(path.join(REPO, 'README.md'), 'utf8');
  if (/Simple Mode/i.test(readme)) {
    fail('README.md: still advertises Simple Mode, removed in v3.32.0');
  } else {
    ok('README.md does not advertise Simple Mode');
  }
}

// ── scripts/ holds the toolchain; one-offs live in scripts/archive/ ─────────
// 74 single-use patchers used to sit in the same flat directory as the dozen
// scripts you are meant to run, sorted in among them — add_language.py, which
// you must use to add a language, filed directly beside add_arabic_plumbing.py,
// which must never be run again. CLAUDE.md said so in prose, and prose lost
// three times: add_rtl_wiring.py reverted a first-paint fix, the copy-pasted
// add_*_plumbing.py family shipped two bugs, and patch_navbar_i18n.py would
// restore the keys v3.35.1 swept.
//
// So the split is enforced rather than described. Anything not on this list is
// assumed to be a one-off and belongs in scripts/archive/.
section('scripts/ contains only the maintained toolchain');
{
  const TOOLCHAIN = new Set([
    'build_guides.py', 'build_landing.py', 'build_seo.py', 'build_rtl.py',
    'build_lang_guides.py', 'build_chinese_guides.py',
    'guides_i18n.py', 'i18n_tool.py', 'i18n_check.py',
    'check_guide_lang.py', 'dump_guides.py',
    'add_language.py', 'verify_wtlocale.py',
  ]);
  const scriptsDir = path.join(REPO, 'scripts');
  const strays = fs.readdirSync(scriptsDir)
    .filter(f => f.endsWith('.py'))
    // guides_<lang>.py are copy modules imported by guides_i18n.py, one per
    // language, so they are matched by shape rather than listed.
    .filter(f => !TOOLCHAIN.has(f) && !/^guides_[a-z_]+\.py$/.test(f));
  if (!strays.length) {
    ok('scripts/: only the toolchain, one-offs are in scripts/archive/');
  } else {
    fail('scripts/: ' + strays.join(', ') + ' looks like a one-off — move it to scripts/archive/');
  }
  if (fs.existsSync(path.join(scriptsDir, 'archive', 'README.md'))) {
    ok('scripts/archive/ documents why nothing in it may be re-run');
  } else {
    fail('scripts/archive/README.md missing');
  }
}

section('SUMMARY');
if (failures === 0) { console.log('\nAll static checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

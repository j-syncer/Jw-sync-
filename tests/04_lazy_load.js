// Integration test for the v2.7.0 lazy-load boot loader.
//
// Loads beta/index.html in JSDOM (CDN <script> injections intercepted) and
// asserts the orchestration is correct:
//   1. Returning visitor on empty hash → bootApp runs immediately
//   2. First-time visitor on empty hash → bootApp does NOT run; CDN untouched
//   3. Clicking "Try Demo" while on landing → only Browse + storage scripts load
//   4. Navigating to #app on landing → full app boot (React + ReactDOM + storage)
//   5. Idle prefetch on landing schedules <link rel="prefetch"> hints
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

function readHtml() {
  return fs.readFileSync(HTML_PATH, 'utf8')
    // Drop google tag inline scripts (they reference uninitialised dataLayer in JSDOM)
    .replace(/<script async src="https:\/\/www\.googletagmanager\.com[\s\S]*?<\/script>/, '')
    .replace(/<script>\s*window\.dataLayer[\s\S]*?gtag\('config'[^)]*\);\s*<\/script>/, '')
    // forum.js and enhancements.js are file:// requests we don't want JSDOM to attempt
    .replace(/<script src="js\/forum\.js"><\/script>/, '')
    .replace(/<script src="js\/enhancements\.js"><\/script>/, '');
}

function makeDom({ seeded, url } = {}) {
  const html = readHtml();
  const requested = [];
  const prefetched = [];
  const dom = new JSDOM(html, {
    url: url || 'https://jwsync.org/beta/',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    beforeParse(window) {
      // Make localStorage deterministic and decoupled from JSDOM's default.
      const store = {};
      if (seeded) Object.assign(store, seeded);
      window.Storage.prototype.getItem = function(k) { return Object.prototype.hasOwnProperty.call(store, k) ? store[k] : null; };
      window.Storage.prototype.setItem = function(k, v) { store[k] = String(v); };
      window.Storage.prototype.removeItem = function(k) { delete store[k]; };
      window.Storage.prototype.clear = function() { Object.keys(store).forEach(k => delete store[k]); };
      // Install Node.appendChild intercept BEFORE the boot loader runs so we
      // catch lazy CDN <script src> injections that fire during parse.
      const origAppend = window.Node.prototype.appendChild;
      window.Node.prototype.appendChild = function(node) {
        if (node && node.tagName === 'SCRIPT' && node.src) {
          requested.push(node.src);
          // Fire onload soon so awaiting promises can resolve.
          setTimeout(() => { if (node.onload) node.onload(); }, 0);
          return node;
        }
        if (node && node.tagName === 'LINK' && node.rel === 'prefetch') {
          prefetched.push(node.href);
          return node;
        }
        return origAppend.call(this, node);
      };
    },
  });
  return { dom, requested, prefetched };
}

function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

(async () => {

  section('Returning visitor on empty hash → bootApp immediately');
  {
    const { dom, requested } = makeDom({ seeded: { jwsync_lp_seen: '1' } });
    // Override __bootApp / __bootBrowse with spies BEFORE the boot loader gets a
    // chance to call them. The boot loader's microtask-chain calls __bootApp
    // inside Promise.all().then(), which is queued but not yet run — we can
    // still replace the function reference before then.
    const spy = { bootApp: 0, bootBrowse: 0 };
    const realBootApp = dom.window.__bootApp;
    const realBootBrowse = dom.window.__bootBrowse;
    dom.window.__bootApp = function() { spy.bootApp++; };
    dom.window.__bootBrowse = function() { spy.bootBrowse++; };

    // v2.10.0: __bootApp is now defined by the EXTERNAL js/app.js, so it is
    // NOT present at HTML-parse time. (That's the win — landing visitors
    // don't download the bundle.) The boot loader will set it later when
    // js/app.js arrives. Browse module is still inline, so __bootBrowse IS
    // present at parse time.
    if (typeof realBootApp === 'undefined') ok('main app extracted: __bootApp NOT inline (v2.10.0)');
    else fail('__bootApp was inline at parse time — extraction did not happen');
    if (typeof realBootBrowse === 'function') ok('Browse module wrapped inline: __bootBrowse defined');
    else fail('__bootBrowse not defined after script parse');
    if (typeof dom.window.__jwBootApp === 'function') ok('boot loader exposed __jwBootApp');
    else fail('__jwBootApp not exposed');
    if (typeof dom.window.__jwBootBrowse === 'function') ok('boot loader exposed __jwBootBrowse');
    else fail('__jwBootBrowse not exposed');

    await wait(50);  // let bootApp's promise chain resolve

    const cdn = requested.filter(u => u.includes('cdnjs.cloudflare.com'));
    if (cdn.length >= 4) ok('returning-visitor empty-hash: boot loader triggered ' + cdn.length + ' CDN script loads');
    else fail('returning-visitor empty-hash: only ' + cdn.length + ' CDN scripts (expected ≥4)');
    // v2.10.0: js/app.js is now a same-origin lazy dependency
    const appBundle = requested.filter(u => /js\/app\.js$/.test(u));
    if (appBundle.length >= 1) ok('returning-visitor: js/app.js fetched lazily (' + appBundle.length + 'x)');
    else fail('returning-visitor: js/app.js NOT fetched (' + JSON.stringify(requested) + ')');
    if (spy.bootApp >= 1) ok('__bootApp invoked after CDN scripts loaded');
    else fail('__bootApp not invoked');

    dom.window.close();
  }

  section('First-time visitor on empty hash → no app boot, no CDN, no js/app.js (v2.10.0)');
  {
    const { dom, requested } = makeDom({ seeded: {} });
    const spy = { bootApp: 0 };
    dom.window.__bootApp = function() { spy.bootApp++; };
    await wait(50);

    const cdn = requested.filter(u => u.includes('cdnjs.cloudflare.com'));
    if (cdn.length === 0) ok('first-time landing: NO CDN scripts requested');
    else fail('first-time landing: ' + cdn.length + ' CDN scripts requested unexpectedly');
    // v2.10.0 keystone assertion: bouncer must NOT pay for the app bundle
    const appBundle = requested.filter(u => /js\/app\.js$/.test(u));
    if (appBundle.length === 0) ok('first-time landing: NO js/app.js requested (code-split win)');
    else fail('first-time landing leaked js/app.js: ' + appBundle.length + 'x');
    if (spy.bootApp === 0) ok('__bootApp NOT invoked on landing');
    else fail('__bootApp invoked ' + spy.bootApp + ' times on landing');

    dom.window.close();
  }

  section('Returning visitor + hash #home → no app boot');
  {
    const { dom, requested } = makeDom({
      seeded: { jwsync_lp_seen: '1' },
      url: 'https://jwsync.org/beta/#home',
    });
    const spy = { bootApp: 0 };
    dom.window.__bootApp = function() { spy.bootApp++; };
    await wait(50);
    const cdn = requested.filter(u => u.includes('cdnjs.cloudflare.com'));
    if (cdn.length === 0) ok('#home hash: no CDN scripts requested even for returning visitor');
    else fail('#home hash leaked ' + cdn.length + ' CDN script requests');
    if (spy.bootApp === 0) ok('#home: __bootApp NOT invoked');
    else fail('#home: __bootApp invoked');
    dom.window.close();
  }

  section('Demo click on landing → boots full app for merge demo (v2.8.0)');
  {
    const { dom, requested } = makeDom({ seeded: {} });
    const spy = { bootApp: 0, bootBrowse: 0 };
    dom.window.__bootApp = function() { spy.bootApp++; };
    dom.window.__bootBrowse = function() { spy.bootBrowse++; };
    await wait(50);
    requested.length = 0;

    const btn = dom.window.document.getElementById('landing-demo-btn');
    if (!btn) { fail('landing-demo-btn not in DOM'); dom.window.close(); }
    else {
      ok('landing-demo-btn rendered: "' + btn.textContent.trim() + '"');
      btn.click();

      if (btn.classList.contains('jw-demo-loading')) ok('demo button enters jw-demo-loading state');
      else fail('demo button missing jw-demo-loading after click');

      await wait(120);

      // v2.8.0: demo runs a real merge, so the full app boots (not just Browse).
      const cdn = requested.filter(u => u.includes('cdnjs.cloudflare.com'));
      if (cdn.length >= 4) ok('demo click triggers full app load (' + cdn.length + ' CDN scripts)');
      else fail('demo click did not load full app (got: ' + JSON.stringify(requested) + ')');

      const react = requested.filter(u => /react/.test(u));
      if (react.length >= 2) ok('demo click loads React + ReactDOM (required for merge UI)');
      else fail('demo click missing React (got ' + react.length + ' react scripts)');

      // v2.10.0: demo click also pulls the extracted app bundle
      const appBundle = requested.filter(u => /js\/app\.js$/.test(u));
      if (appBundle.length >= 1) ok('demo click also loads js/app.js (' + appBundle.length + 'x)');
      else fail('demo click missing js/app.js');

      if (spy.bootApp >= 1) ok('__bootApp invoked by demo click (drives the merge UI)');
      else fail('__bootApp NOT invoked by demo click');

      dom.window.close();
    }
  }

  section('hashchange #app on landing → triggers full bootApp');
  {
    const { dom, requested } = makeDom({ seeded: {} });
    const spy = { bootApp: 0 };
    dom.window.__bootApp = function() { spy.bootApp++; };
    await wait(50);
    requested.length = 0;

    dom.window.location.hash = '#app';
    dom.window.dispatchEvent(new dom.window.Event('hashchange'));
    await wait(80);

    const cdn = requested.filter(u => u.includes('cdnjs.cloudflare.com'));
    if (cdn.length >= 4) ok('hashchange #app: full CDN bundle loaded (' + cdn.length + ' scripts)');
    else fail('hashchange #app: only ' + cdn.length + ' CDN scripts (expected ≥4)');
    // v2.10.0: js/app.js is part of the boot
    const appBundle = requested.filter(u => /js\/app\.js$/.test(u));
    if (appBundle.length >= 1) ok('hashchange #app: js/app.js fetched lazily');
    else fail('hashchange #app: js/app.js NOT fetched');
    if (spy.bootApp >= 1) ok('__bootApp invoked after hashchange #app');
    else fail('__bootApp not invoked on #app');

    dom.window.close();
  }

  section('Hover on launch button → prefetch hints injected');
  {
    const { dom, prefetched } = makeDom({ seeded: {} });
    await wait(50);

    const btn = dom.window.document.getElementById('landing-launch-btn');
    if (!btn) { fail('landing-launch-btn not in DOM'); }
    else {
      btn.dispatchEvent(new dom.window.Event('mouseenter'));
      await wait(30);
      const cdn = prefetched.filter(u => u.includes('cdnjs.cloudflare.com'));
      if (cdn.length >= 4) ok('hover prefetch: ' + cdn.length + ' CDN scripts hinted');
      else fail('hover prefetch only emitted ' + cdn.length + ' hints (expected ≥4)');
      // v2.10.0: js/app.js prefetch hint
      const appPrefetch = prefetched.filter(u => /js\/app\.js$/.test(u));
      if (appPrefetch.length >= 1) ok('hover prefetch: js/app.js also hinted');
      else fail('hover prefetch missing js/app.js');
    }
    dom.window.close();
  }

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll lazy-load checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

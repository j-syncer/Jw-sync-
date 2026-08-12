// 21_app_boot.js — does the main app actually mount?
//
// Twenty suites, and not one of them rendered the React app. They read js/app.js
// as *text* — anchors present, classes defined, i18n keys covered — which cannot
// see a ReferenceError. Removing Simple Mode proved the gap the expensive way: a
// single surviving `${be}` inside a useEffect dependency key crashed the app into
// its error boundary on load, and `node --check` plus all twenty suites passed.
//
// So this one boots it for real. It is deliberately shallow — mount, render, poke
// the one control that gates the merge settings — because its job is to catch
// "the page is blank", which is the failure no amount of text-matching can.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m) => { failures++; console.log('  ✗ ' + m); };
const section = (t) => console.log('\n== ' + t + ' ==');

let React, ReactDOM;
try {
  React = require('react');
  ReactDOM = require('react-dom/client');
} catch (e) {
  console.log('  ! react/react-dom not installed — run `npm install` in tests/');
  process.exit(1);
}

function boot(appRel, prefs) {
  const src = fs.readFileSync(path.join(REPO, appRel), 'utf8');
  const dom = new JSDOM('<!doctype html><html><body><div id="root"></div></body></html>',
    { url: 'https://jwsync.org/', pretendToBeVisual: true });
  const { window } = dom;
  const errors = [];
  window.addEventListener('error', e => errors.push(String(e.error || e.message)));

  global.window = window; global.document = window.document;
  global.navigator = window.navigator; global.localStorage = window.localStorage;
  window.requestAnimationFrame = (cb) => setTimeout(cb, 0);
  global.requestAnimationFrame = window.requestAnimationFrame;
  global.cancelAnimationFrame = () => {};
  window.scrollTo = () => {};
  window.matchMedia = window.matchMedia || (() => ({
    matches: false, addListener() {}, removeListener() {},
    addEventListener() {}, removeEventListener() {},
  }));
  window.React = React; global.React = React;
  window.ReactDOM = ReactDOM; global.ReactDOM = ReactDOM;
  window.lucide = { createIcons() {} };
  // Both normally arrive from a CDN; the shell only needs them to exist.
  window.initSqlJs = () => Promise.resolve({ Database: function () { this.exec = () => []; this.close = () => {}; } });
  window.JSZip = function () {};
  if (prefs) window.localStorage.setItem('jwsync_prefs_v1', JSON.stringify(prefs));

  new Function('window', 'document', 'navigator', 'localStorage', 'React', 'ReactDOM', src)
    (window, window.document, window.navigator, window.localStorage, React, ReactDOM);
  if (typeof window.__bootApp !== 'function') throw new Error('__bootApp not exposed');
  window.__bootApp();
  return { window, errors };
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

(async () => {
  for (const appRel of ['js/app.js', 'beta/js/app.js']) {
    // simpleMode:true is what a returning visitor still has saved from before
    // v3.32.0. It must be ignored, not render an empty page.
    section(appRel + ' (with a stale simpleMode pref)');
    let window, errors;
    try {
      ({ window, errors } = boot(appRel, { simpleMode: true }));
      ok('evaluates and boots without throwing');
    } catch (e) {
      fail('threw while booting: ' + e.message);
      continue;
    }
    await sleep(350);

    const body = window.document.body;
    if (body.innerHTML.length > 2000) ok(`rendered a real page (${body.innerHTML.length} chars)`);
    else fail(`rendered almost nothing (${body.innerHTML.length} chars) — blank page`);

    const boundary = body.textContent.toLowerCase();
    if (!/something went wrong|unexpected error/.test(boundary)) ok('no error boundary shown');
    else fail('app fell through to its error boundary');
    if (errors.length === 0) ok('no uncaught window errors');
    else fail('uncaught error(s): ' + errors.slice(0, 2).join(' | '));

    if (!/mode-seg|simple-mode-teaser/.test(body.innerHTML)) ok('no Simple Mode UI rendered');
    else fail('Simple Mode UI still rendered');

    // Merge Settings is a collapsed panel; the disclosure lives inside it.
    const panel = [...window.document.querySelectorAll('button')]
      .find(b => b.textContent.includes('Merge Settings'));
    if (!panel) { fail('Merge Settings panel not found'); continue; }
    panel.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
    await sleep(80);

    const hadAdvanced = body.textContent.includes('Deep Clean');
    const disc = window.document.querySelector('.jw-adv-disclosure');
    if (!disc) { fail('advanced-settings disclosure missing'); continue; }
    ok('advanced-settings disclosure rendered');
    if (!hadAdvanced) ok('advanced settings hidden until asked for');
    else fail('advanced settings visible before the disclosure was opened');

    disc.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
    await sleep(80);
    if (body.textContent.includes('Deep Clean')) ok('disclosure reveals the advanced settings');
    else fail('disclosure did not reveal the advanced settings');
  }

  section('SUMMARY');
  if (failures === 0) { console.log('\nApp boots cleanly.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})();

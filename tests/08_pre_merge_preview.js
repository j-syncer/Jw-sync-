// Integration test for the v2.16.0 Pre-merge Impact Preview.
//
// The preview is a self-contained IIFE in beta/index.html exposing
// window.__jwImpactPreview(counts) -> Promise<boolean>. It renders a modal
// summarising what a merge will add/update/dedupe and resolves true on
// "Merge & Download" or false on Cancel/Escape.
//
// The numbers themselves are produced by beta/js/merge-worker.js, which now
// pauses before packaging (when opts.previewConfirm is set), posts an
// {type:'impact', counts} message, and awaits {type:'confirmMerge'} /
// {type:'cancel'}. This suite asserts:
//   1. The modal renders the supplied counts
//   2. "Merge & Download" resolves true
//   3. Cancel resolves false
//   4. The worker source wires the gate (previewConfirm + impact + confirmMerge)
//   5. app.js sends previewConfirm and handles impact/cancelled
const path = require('path');
const fs = require('fs');
const { JSDOM } = require('jsdom');

const REPO = path.join(__dirname, '..');
const HTML_PATH = REPO + '/beta/index.html';

let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }
function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

function makeDom() {
  const html = fs.readFileSync(HTML_PATH, 'utf8');
  const m = html.match(/<!-- ── Pre-merge Impact Preview \(v2\.16\.0\) ─[\s\S]*?<!-- ── End Pre-merge Impact Preview ─[─]*\s*-->/);
  if (!m) { fail('Pre-merge Impact Preview block not found in beta/index.html'); process.exit(1); }
  const page = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${m[0]}</body></html>`;
  const dom = new JSDOM(page, { url: 'https://jwsync.org/beta/', runScripts: 'dangerously', pretendToBeVisual: true });
  dom.window.localStorage.setItem('jwsync_lang', 'en');
  return dom;
}

async function waitForOverlay(doc, id, ms = 2000) {
  const start = Date.now();
  while (Date.now() - start < ms) {
    const el = doc.getElementById(id);
    if (el) return el;
    await wait(20);
  }
  return null;
}

(async function run() {
  const counts = { Note: 12, UserMark: 7, Bookmark: 3, Tag: 4, Updated: 2, Deduplicated: 5 };

  section('Modal renders supplied counts');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    if (typeof win.__jwImpactPreview !== 'function') { fail('window.__jwImpactPreview not exposed'); process.exit(1); }
    ok('window.__jwImpactPreview exposed');
    const p = win.__jwImpactPreview(counts);
    const overlay = await waitForOverlay(doc, 'jw-impact-overlay');
    if (!overlay) { fail('impact overlay did not render'); dom.window.close(); }
    else {
      ok('impact overlay rendered');
      const rows = overlay.querySelectorAll('.jip-row');
      if (rows.length === 6) ok('6 stat rows rendered');
      else fail('expected 6 stat rows, got ' + rows.length);
      const text = overlay.textContent;
      if (text.includes('+12') && text.includes('+7') && text.includes('+3') && text.includes('+4'))
        ok('added counts (+12 notes, +7 highlights, +3 bookmarks, +4 tags) shown');
      else fail('added counts not rendered correctly: ' + text);
      if (text.includes('2') && text.includes('5')) ok('updated (2) + deduped (5) shown');
      else fail('updated/deduped counts missing');
      // resolve to clean up
      overlay.querySelector('[data-jip-go]').click();
      const res = await p;
      if (res === true) ok('"Merge & Download" resolves true');
      else fail('confirm resolved ' + res);
      dom.window.close();
    }
  }

  section('Cancel resolves false');
  {
    const dom = makeDom();
    const win = dom.window, doc = win.document;
    const p = win.__jwImpactPreview(counts);
    const overlay = await waitForOverlay(doc, 'jw-impact-overlay');
    if (!overlay) { fail('overlay did not render'); dom.window.close(); }
    else {
      overlay.querySelector('.jip-btn-cancel').click();
      const res = await p;
      if (res === false) ok('Cancel resolves false');
      else fail('cancel resolved ' + res);
      if (!doc.getElementById('jw-impact-overlay')) ok('overlay removed after cancel');
      else fail('overlay still present after cancel');
      dom.window.close();
    }
  }

  section('Worker wires the impact gate');
  {
    const w = fs.readFileSync(REPO + '/beta/js/merge-worker.js', 'utf8');
    if (w.includes('previewConfirm')) ok('worker honours opts.previewConfirm');
    else fail('worker previewConfirm gate missing');
    if (w.includes("type: 'impact'")) ok("worker posts {type:'impact'}");
    else fail('worker impact message missing');
    if (w.includes("'confirmMerge'") && w.includes('confirmResolver')) ok('worker awaits confirmMerge');
    else fail('worker confirmMerge handling missing');
  }

  section('app.js drives the preview');
  {
    const a = fs.readFileSync(REPO + '/beta/js/app.js', 'utf8');
    if (a.includes('previewConfirm')) ok('app.js requests previewConfirm');
    else fail('app.js previewConfirm flag missing');
    if (a.includes("d.type==='impact'") && a.includes('__jwImpactPreview')) ok('app.js handles impact -> __jwImpactPreview');
    else fail('app.js impact handling missing');
    if (a.includes("d.type==='cancelled'")) ok('app.js handles cancelled');
    else fail('app.js cancelled handling missing');
  }

  console.log('\n== SUMMARY ==');
  if (failures) { console.log('\nFAIL: ' + failures + ' check(s) failed.'); process.exit(1); }
  console.log('\nAll pre-merge preview checks passed.');
})();

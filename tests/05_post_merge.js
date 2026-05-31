// Integration test for the v2.9.0 post-merge celebration overlay.
//
// Loads beta/index.html in JSDOM (CDN <script> injections intercepted),
// simulates the React download anchor's href becoming a blob: URL — which
// is the signal the merge worker has finished — and asserts:
//   1. The #jw-celebrate-overlay appears
//   2. It contains a title, stats grid (4 cells), and primary/secondary CTAs
//   3. A Demo merge surfaces the "Use my real files" CTA; a real-file merge does not
//   4. Clicking the close button removes the overlay
//   5. Clicking "Restore to JW Library" opens the #jw-restore-overlay
//   6. The restore overlay has 3 platform tabs and step text
//   7. Escape key closes the overlay
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
    .replace(/<script async src="https:\/\/www\.googletagmanager\.com[\s\S]*?<\/script>/, '')
    .replace(/<script>\s*window\.dataLayer[\s\S]*?gtag\('config'[^)]*\);\s*<\/script>/, '')
    .replace(/<script src="js\/forum\.js"><\/script>/, '')
    .replace(/<script src="js\/enhancements\.js"><\/script>/, '');
}

function makeDom() {
  const html = readHtml();
  const dom = new JSDOM(html, {
    url: 'https://jwsync.org/beta/#app',
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    beforeParse(window) {
      // Returning visitor so app boots
      const store = { jwsync_lp_seen: '1' };
      window.Storage.prototype.getItem = function (k) { return Object.prototype.hasOwnProperty.call(store, k) ? store[k] : null; };
      window.Storage.prototype.setItem = function (k, v) { store[k] = String(v); };
      window.Storage.prototype.removeItem = function (k) { delete store[k]; };
      // Intercept dynamically-injected <script src> so JSDOM doesn't fetch CDN
      const orig = window.Node.prototype.appendChild;
      window.Node.prototype.appendChild = function (node) {
        if (node && node.tagName === 'SCRIPT' && node.src) {
          setTimeout(() => { if (node.onload) node.onload(); }, 0);
          return node;
        }
        if (node && node.tagName === 'LINK' && node.rel === 'prefetch') {
          return node;
        }
        return orig.call(this, node);
      };
    },
  });
  // Override boot hooks so the celebration test doesn't blow up trying to
  // mount the real React app without React being defined in the JSDOM realm.
  dom.window.__bootApp = function () {};
  dom.window.__bootBrowse = function () {};
  return dom;
}

function wait(ms) { return new Promise(r => setTimeout(r, ms)); }

function setupFakeFileInput(doc, fileName) {
  // Build an enough-of-an-input element + attach a fake FileList so
  // celebrate's isDemoMerge() can read inputs[0].files[0].name.
  const input = doc.createElement('input');
  input.type = 'file';
  input.setAttribute('accept', '.jwlibrary');
  input.className = 'hidden';
  doc.body.appendChild(input);
  // Define a fake `files` getter that returns a FileList-like object
  Object.defineProperty(input, 'files', {
    configurable: true,
    get() { return [{ name: fileName }]; }
  });
  return input;
}

function simulateMergeComplete(doc) {
  // Insert (or update) a React-style download anchor with a blob: href.
  let a = doc.getElementById('download-btn');
  if (!a) {
    a = doc.createElement('a');
    a.id = 'download-btn';
    a.setAttribute('download', '2026-05-28.jwlibrary');
    a.textContent = '⬇️ Download My Merged Backup';
    a.className = 'simple-download-btn';
    doc.body.appendChild(a);
  }
  // First set to empty, then to a blob URL (mimics React updating state)
  a.setAttribute('href', '');
  // Use setTimeout(0) to let the observer flush an initial empty change first
  return new Promise(r => setTimeout(() => {
    a.setAttribute('href', 'blob:https://jwsync.org/abcdef-test-uuid');
    r(a);
  }, 30));
}

async function waitForOverlay(doc, id, timeoutMs) {
  const start = Date.now();
  while (Date.now() - start < (timeoutMs || 2000)) {
    const el = doc.getElementById(id);
    if (el) return el;
    await wait(40);
  }
  return null;
}

(async () => {

  section('Real-file merge complete → celebration overlay appears');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80); // let init() bind the observer

    setupFakeFileInput(doc, 'MyRealBackup_2024.jwlibrary');
    await simulateMergeComplete(doc);
    const overlay = await waitForOverlay(doc, 'jw-celebrate-overlay');
    if (!overlay) { fail('celebration overlay did not appear'); dom.window.close(); }
    else {
      ok('celebration overlay rendered');

      const title = overlay.querySelector('.jwc-title');
      if (title && title.textContent.trim().length > 0) ok('overlay has a title: "' + title.textContent.trim() + '"');
      else fail('overlay title missing');

      const stats = overlay.querySelectorAll('.jwc-stat');
      if (stats.length === 4) ok('overlay shows 4 stat cells (notes / highlights / bookmarks / tags)');
      else fail('overlay has ' + stats.length + ' stat cells (expected 4)');

      // v2.9.1 button hierarchy: Download (primary) > Restore (outline) > Browse (secondary)
      const downloadBtn = overlay.querySelector('[data-jwc-download]');
      const restoreBtn = overlay.querySelector('[data-jwc-restore]');
      const browseBtn = overlay.querySelector('[data-jwc-browse]');
      if (downloadBtn && downloadBtn.classList.contains('jwc-btn-primary')) ok('Download is the primary CTA');
      else fail('Download primary CTA missing/wrong class');
      if (restoreBtn && restoreBtn.classList.contains('jwc-btn-outline')) ok('Restore CTA present (outline)');
      else fail('Restore outline CTA missing');
      if (browseBtn && browseBtn.classList.contains('jwc-btn-secondary')) ok('Browse CTA present (secondary)');
      else fail('Browse secondary CTA missing');

      // v2.9.1 donate link
      const donateLink = overlay.querySelector('[data-jwc-donate]');
      if (donateLink && /paypal\.com\/paypalme\/jwsync/.test(donateLink.getAttribute('href') || '')) {
        ok('donate link present pointing to PayPal');
      } else { fail('donate link missing or wrong href'); }
      if (donateLink && donateLink.getAttribute('rel') === 'noopener noreferrer') {
        ok('donate link has rel="noopener noreferrer"');
      } else { fail('donate link missing rel="noopener noreferrer"'); }
      if (donateLink && donateLink.getAttribute('target') === '_blank') ok('donate link opens in new tab');
      else fail('donate link missing target="_blank"');

      const demoCta = overlay.querySelector('.jwc-demo-cta');
      if (!demoCta) ok('real-file merge: no demo CTA shown (correct)');
      else fail('real-file merge: demo CTA leaked into overlay');

      dom.window.close();
    }
  }

  section('Demo merge → "Use my real files" CTA appears');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);

    setupFakeFileInput(doc, 'JWSync_Demo_Phone.jwlibrary');
    await simulateMergeComplete(doc);
    const overlay = await waitForOverlay(doc, 'jw-celebrate-overlay');
    if (!overlay) { fail('celebration overlay did not appear'); dom.window.close(); }
    else {
      const demoCta = overlay.querySelector('.jwc-demo-cta');
      if (demoCta) ok('demo merge shows "Use my real files" CTA block');
      else fail('demo merge: demo CTA missing');
      const demoBtn = overlay.querySelector('.jwc-demo-btn');
      if (demoBtn) ok('demo merge: reset button present');
      else fail('demo merge: reset button missing');

      dom.window.close();
    }
  }

  section('Restore button opens guide overlay with 3 platform tabs');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);

    setupFakeFileInput(doc, 'MyRealBackup.jwlibrary');
    await simulateMergeComplete(doc);
    const cele = await waitForOverlay(doc, 'jw-celebrate-overlay');
    if (!cele) { fail('celebration overlay did not appear'); dom.window.close(); }
    else {
      // Restore button is the outline-style CTA in v2.9.1 (Download is primary)
      const restoreBtn = cele.querySelector('[data-jwc-restore]');
      restoreBtn.click();
      const guide = await waitForOverlay(doc, 'jw-restore-overlay');
      if (!guide) { fail('restore guide did not open'); dom.window.close(); }
      else {
        ok('restore guide overlay opened');
        const tabs = guide.querySelectorAll('.jwrg-tab');
        if (tabs.length === 3) ok('restore guide has 3 platform tabs');
        else fail('restore guide has ' + tabs.length + ' tabs (expected 3)');

        const steps = guide.querySelectorAll('#jwrg-steps li');
        if (steps.length >= 4) ok('restore guide shows ' + steps.length + ' steps for the active platform');
        else fail('restore guide steps: only ' + steps.length);

        // Click the Android tab and confirm steps update
        const androidTab = guide.querySelector('.jwrg-tab[data-platform="android"]');
        androidTab.click();
        if (androidTab.classList.contains('active')) ok('Android tab activated on click');
        else fail('Android tab did not activate');

        const newSteps = guide.querySelectorAll('#jwrg-steps li');
        if (newSteps.length >= 4) ok('switching tabs re-renders the steps');
        else fail('switching tabs broke step rendering');

        // Warning visible
        const warning = guide.querySelector('.jwrg-warning');
        if (warning && warning.textContent.length > 20) ok('restore guide shows warning text');
        else fail('restore guide warning missing');

        // IN/OUT mode toggle (v2.14.0 guided in/out flow)
        const modeBtns = guide.querySelectorAll('.jwrg-mode');
        if (modeBtns.length === 2) ok('guide has IN/OUT mode toggle (2 buttons)');
        else fail('guide mode toggle has ' + modeBtns.length + ' buttons (expected 2)');

        const exportModeBtn = guide.querySelector('.jwrg-mode[data-mode="export"]');
        const titleBefore = guide.querySelector('#jwrg-title').textContent;
        exportModeBtn.click();
        if (exportModeBtn.classList.contains('active')) ok('export mode activates on click');
        else fail('export mode did not activate');

        const exportSteps = guide.querySelectorAll('#jwrg-steps li');
        if (exportSteps.length >= 4) ok('export mode renders export steps (' + exportSteps.length + ')');
        else fail('export mode steps: only ' + exportSteps.length);

        const warnAfter = guide.querySelector('#jwrg-warning');
        if (warnAfter && warnAfter.style.display === 'none') ok('restore warning hidden in export mode');
        else fail('restore warning should be hidden in export mode');

        const titleAfter = guide.querySelector('#jwrg-title').textContent;
        if (titleAfter && titleAfter !== titleBefore) ok('guide title changes between modes');
        else fail('guide title did not change between modes');

        dom.window.close();
      }
    }
  }

  section('Landing "How it works" button opens the export guide (cross-module)');
  {
    // Regression: the button binding lives in the Demo-handler module while
    // openRestoreGuide lives in the celebration module — the wiring must go
    // through the global window.__jwOpenGuide, defined in the right scope.
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(120);
    if (typeof dom.window.__jwOpenGuide !== 'function') fail('window.__jwOpenGuide not exposed globally');
    else ok('window.__jwOpenGuide exposed globally');
    const howBtn = doc.getElementById('landing-howto-btn');
    if (!howBtn) { fail('landing-howto-btn not present'); dom.window.close(); }
    else {
      ok('landing-howto-btn present');
      howBtn.click();
      const guide = await waitForOverlay(doc, 'jw-restore-overlay');
      if (!guide) { fail('How it works button did not open the guide overlay'); dom.window.close(); }
      else {
        ok('How it works button opens the guide overlay');
        const em = guide.querySelector('.jwrg-mode[data-mode="export"]');
        if (em && em.classList.contains('active')) ok('guide opens in export mode');
        else fail('guide did not open in export mode');
        const steps = guide.querySelectorAll('#jwrg-steps li');
        if (steps.length >= 4) ok('export steps rendered (' + steps.length + ')');
        else fail('export steps missing: ' + steps.length);
        dom.window.close();
      }
    }
  }

  section('Close button + Escape both dismiss the celebration');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);
    setupFakeFileInput(doc, 'MyRealBackup.jwlibrary');
    await simulateMergeComplete(doc);
    const cele = await waitForOverlay(doc, 'jw-celebrate-overlay');
    if (!cele) { fail('celebration overlay did not appear'); dom.window.close(); }
    else {
      // Click close
      const closeBtn = cele.querySelector('.jwc-close');
      closeBtn.click();
      await wait(40);
      if (!doc.getElementById('jw-celebrate-overlay')) ok('close button dismisses overlay');
      else fail('close button did not remove overlay');

      // Re-trigger with a different blob URL and dismiss via Escape
      const a = doc.getElementById('download-btn');
      a.setAttribute('href', 'blob:https://jwsync.org/another-uuid-zyx');
      const second = await waitForOverlay(doc, 'jw-celebrate-overlay');
      if (!second) fail('new blob URL did not re-trigger overlay');
      else {
        ok('new blob URL re-triggers a fresh overlay');
        // Dispatch Escape
        doc.dispatchEvent(new dom.window.KeyboardEvent('keydown', { key: 'Escape' }));
        await wait(40);
        if (!doc.getElementById('jw-celebrate-overlay')) ok('Escape key dismisses overlay');
        else fail('Escape did not remove overlay');
      }

      dom.window.close();
    }
  }

  section('Same blob URL does NOT re-trigger (idempotency guard)');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);
    setupFakeFileInput(doc, 'MyRealBackup.jwlibrary');
    await simulateMergeComplete(doc);
    const overlay = await waitForOverlay(doc, 'jw-celebrate-overlay');
    if (!overlay) { fail('overlay did not appear'); dom.window.close(); }
    else {
      overlay.querySelector('.jwc-close').click();
      await wait(40);

      // Set the same href again — should NOT re-trigger
      const a = doc.getElementById('download-btn');
      a.setAttribute('href', 'blob:https://jwsync.org/abcdef-test-uuid'); // same as in simulateMergeComplete
      await wait(120);
      const again = doc.getElementById('jw-celebrate-overlay');
      if (!again) ok('same blob URL did not re-fire the celebration');
      else fail('same blob URL incorrectly re-fired (potential duplicate dialogs)');

      dom.window.close();
    }
  }

  section('Auto-download fires when merge completes (v2.9.1)');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);
    setupFakeFileInput(doc, 'MyRealBackup.jwlibrary');

    // Pre-create the download anchor with a click spy
    const a = doc.createElement('a');
    a.id = 'download-btn';
    a.setAttribute('download', 'merged.jwlibrary');
    a.setAttribute('href', '');
    a.textContent = 'Download';
    let clickCount = 0;
    a.addEventListener('click', function (e) { clickCount++; e.preventDefault(); });
    doc.body.appendChild(a);

    // Update href to a blob: URL — should trigger handleMergeComplete →
    // which calls triggerDownload → which clicks the anchor.
    await new Promise(r => setTimeout(() => { a.setAttribute('href', 'blob:https://jwsync.org/auto-download-test'); r(); }, 30));
    await waitForOverlay(doc, 'jw-celebrate-overlay');
    await wait(80);

    if (clickCount >= 1) ok('auto-download programmatically clicked #download-btn (' + clickCount + 'x)');
    else fail('auto-download did NOT click #download-btn');

    // Download status banner should be visible
    const overlay = doc.getElementById('jw-celebrate-overlay');
    const status = overlay && overlay.querySelector('[data-jwc-dl-status]');
    if (status && !status.hidden) ok('download-status banner shown after successful auto-download');
    else fail('download-status banner not shown');

    // Manual re-download via the button increments the click count
    const dlBtn = overlay.querySelector('[data-jwc-download]');
    const before = clickCount;
    dlBtn.click();
    await wait(40);
    if (clickCount > before) ok('manual click on Download button fires anchor click again (' + (clickCount - before) + 'x)');
    else fail('manual Download click did not re-trigger anchor');

    dom.window.close();
  }

  section('Auto-download is one-shot per merge (no duplicate fires)');
  {
    const dom = makeDom();
    const doc = dom.window.document;
    await wait(80);
    setupFakeFileInput(doc, 'MyRealBackup.jwlibrary');

    const a = doc.createElement('a');
    a.id = 'download-btn';
    a.setAttribute('download', 'merged.jwlibrary');
    a.setAttribute('href', '');
    let autoClicks = 0;
    a.addEventListener('click', function (e) { autoClicks++; e.preventDefault(); });
    doc.body.appendChild(a);

    await new Promise(r => setTimeout(() => { a.setAttribute('href', 'blob:https://jwsync.org/oneshot-test'); r(); }, 30));
    await waitForOverlay(doc, 'jw-celebrate-overlay');
    await wait(80);
    const firstRunClicks = autoClicks;

    // Close and re-trigger the SAME blob URL — should NOT fire auto-download again
    doc.getElementById('jw-celebrate-overlay').querySelector('.jwc-close').click();
    await wait(40);
    a.setAttribute('href', 'blob:https://jwsync.org/oneshot-test');
    await wait(120);
    if (autoClicks === firstRunClicks) ok('same blob URL: auto-download did NOT re-fire (one-shot guard works)');
    else fail('same blob URL: auto-download fired ' + (autoClicks - firstRunClicks) + 'x more (expected 0)');

    dom.window.close();
  }

  section('SUMMARY');
  if (failures === 0) { console.log('\nAll post-merge celebration checks passed.'); process.exit(0); }
  console.log('\nFAIL: ' + failures + ' check(s) failed.');
  process.exit(1);
})().catch(e => { console.error('TEST CRASH:', e); process.exit(2); });

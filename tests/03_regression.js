const path = require('path');
const REPO = path.join(__dirname, '..');
// Regression check: confirm features we didn't touch still parse correctly,
// and that the React tree we modified is balanced.

const fs = require('fs');
let failures = 0;
function ok(msg) { console.log('  ✓', msg); }
function fail(msg) { console.log('  ✗', msg); failures++; }
function section(name) { console.log('\n== ' + name + ' =='); }

section('Merge worker untouched and parseable');
const workerSrc = fs.readFileSync(REPO + '/beta/js/merge-worker.js', 'utf8');
try {
  new Function(workerSrc);
  ok('merge-worker.js parses (' + workerSrc.length + ' bytes)');
} catch (e) { fail('merge-worker.js parse failed: ' + e.message); }

const rootWorkerPath = REPO + '/js/merge-worker.js';
if (fs.existsSync(rootWorkerPath)) {
  const rootWorker = fs.readFileSync(rootWorkerPath, 'utf8');
  try { new Function(rootWorker); ok('root js/merge-worker.js parses'); }
  catch (e) { fail('root merge worker parse failed: ' + e.message); }
}

section('Critical merge anchors still present in beta');
// v2.10.0: the main app bundle is now extracted to beta/js/app.js. The merge
// anchors moved with it. Search both the HTML and the app bundle.
const beta = fs.readFileSync(REPO + '/beta/index.html', 'utf8');
const betaAppPath = REPO + '/beta/js/app.js';
const betaApp = fs.existsSync(betaAppPath) ? fs.readFileSync(betaAppPath, 'utf8') : '';
const betaAll = beta + '\n' + betaApp;
const MERGE_ANCHORS = [
  // The async file loader and Insights state setter
  'ja=async e=>{if(!M||!e)return;',
  // The Insights modal close
  'className:"modal-close"',
  // Simple Mode teaser
  'simple-mode-teaser',
  'Explore Full Mode →',
  // Existing features mentioned by the merge engine
  'Preview Merge',
  'Tag Manager',
  // Worker is still wired
  'merge-worker.js',
];
for (const a of MERGE_ANCHORS) {
  const n = betaAll.split(a).length - 1;
  if (n >= 1) ok(`anchor present: "${a.slice(0,40)}" (${n}x)`);
  else fail(`anchor missing: "${a.slice(0,40)}"`);
}

section('HTML structure sanity');
// Strip <script>/<style> blocks before counting close tags, since the app's JS
// builds HTML strings (for print/export) that legitimately contain "</body>".
function stripScriptsAndStyles(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '');
}
for (const path of [REPO + '/beta/index.html', REPO + '/index.html']) {
  const c = fs.readFileSync(path, 'utf8');
  const markup = stripScriptsAndStyles(c);
  const bodyCloseCount = (markup.match(/<\/body>/g) || []).length;
  const htmlCloseCount = (markup.match(/<\/html>/g) || []).length;
  if (bodyCloseCount === 1) ok(`${path}: structural </body> count = 1`);
  else fail(`${path}: structural </body> count = ${bodyCloseCount}`);
  if (htmlCloseCount === 1) ok(`${path}: structural </html> count = 1`);
  else fail(`${path}: structural </html> count = ${htmlCloseCount}`);
  // Note Explorer block appears once
  const browseCount = (c.match(/<!-- ── Note Explorer \(Browse\) ─/g) || []).length;
  if (browseCount === 1) ok(`${path}: Browse block count = 1`);
  else fail(`${path}: Browse block count = ${browseCount}`);
}

section('Service worker cache version');
const sw = fs.readFileSync(REPO + '/service-worker.js', 'utf8');
const verMatch = sw.match(/CACHE_VERSION\s*=\s*'([^']+)'/);
if (verMatch) ok(`CACHE_VERSION = ${verMatch[1]}`);
else fail('CACHE_VERSION not found');

section('SUMMARY');
if (failures === 0) { console.log('\nAll regression checks passed.'); process.exit(0); }
console.log('\nFAIL: ' + failures + ' check(s) failed.');
process.exit(1);

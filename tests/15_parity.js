#!/usr/bin/env node
/**
 * 15_parity.js — beta/production drift guard.
 *
 * Catches the two failure modes that have shipped real bugs:
 *
 *  1. A "go live" session edits the production copy of a shared file without
 *     mirroring beta (the Awards tab was missing from beta/highlights.html for
 *     four days; beta/js/jw-session.js never got the auto-open-Browse flag).
 *  2. A precached page ships without a service-worker CACHE_VERSION bump, so
 *     installed-app (PWA) users keep being served the old cached build (the
 *     Library Doctor freeze fix went out without a bump).
 *
 * index.html / beta/index.html are deliberately NOT compared: beta/index.html
 * is allowed to run ahead of production between go-lives. The satellite pages
 * and the js/ tool layer ship to both sites in lockstep, so they must match.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const cp = require('child_process');

const ROOT = path.join(__dirname, '..');
let pass = 0, failCount = 0;

function ok(name) { pass++; console.log('  ✓ ' + name); }
function fail(name, detail) {
  failCount++;
  console.log('  ✗ ' + name);
  if (detail) console.log('      ' + detail);
}
function read(rel) { return fs.readFileSync(path.join(ROOT, rel), 'utf8'); }

// ── 1. Files that must be byte-identical between production and beta ──────
console.log('== Production/beta pairs must be identical ==');

// Discovered rather than listed: a hardcoded roster is how a new shared file
// escapes this guard. js/forum-i18n.js was added in v3.33.0 and would have had
// to be remembered here; instead every js/*.js with a beta twin is checked, and
// a file with no twin at all is a failure of its own.
// enhancements.js is the one legitimate exception (section 2 below).
const ENHANCEMENTS = 'enhancements.js';
const SHARED_JS = fs.readdirSync(path.join(ROOT, 'js'))
  .filter(function (f) { return /\.js$/.test(f) && f !== ENHANCEMENTS; })
  .sort();

const IDENTICAL_PAIRS = SHARED_JS
  .filter(function (f) { return fs.existsSync(path.join(ROOT, 'beta', 'js', f)); })
  .map(function (f) { return ['js/' + f, 'beta/js/' + f]; })
  .concat([
    ['highlights.html', 'beta/highlights.html'],
    ['share.html', 'beta/share.html'],
    ['styles.css', 'beta/styles.css'],
    ['rtl.css', 'beta/rtl.css'],
  ]);

SHARED_JS.forEach(function (f) {
  if (!fs.existsSync(path.join(ROOT, 'beta', 'js', f))) {
    fail('js/' + f + ' has no beta twin',
      'Every file in js/ ships to both sites. Copy it to beta/js/ in the same commit.');
  }
});

IDENTICAL_PAIRS.forEach(function (pair) {
  if (read(pair[0]) === read(pair[1])) {
    ok(pair[0] + ' == ' + pair[1]);
  } else {
    fail(pair[0] + ' != ' + pair[1],
      'These ship to both sites in lockstep. Apply the change to BOTH copies ' +
      '(or, for intentional beta-first work, mirror it to production when going live).');
  }
});

// ── 2. enhancements.js: only comments + SW registration may differ ────────
console.log('== js/enhancements.js parity (modulo SW registration) ==');

function normalizeEnhancements(src) {
  return src.split('\n')
    .map(function (l) { return l.trim(); })
    // comment-only lines may legitimately differ (path wording)
    .filter(function (l) { return !/^(\/\/|\/\*|\*)/.test(l); })
    // the service-worker registration differs by design: prod registers at
    // scope "/", beta registers ../service-worker.js at scope "/beta/"
    .filter(function (l) { return l.indexOf('service-worker') === -1; })
    .join('\n');
}

(function () {
  const prod = normalizeEnhancements(read('js/enhancements.js'));
  const beta = normalizeEnhancements(read('beta/js/enhancements.js'));
  if (prod === beta) {
    ok('enhancements.js code identical outside comments + SW registration');
  } else {
    const p = prod.split('\n'), b = beta.split('\n');
    let i = 0;
    while (i < p.length && i < b.length && p[i] === b[i]) i++;
    fail('js/enhancements.js has code drift vs beta/js/enhancements.js',
      'First divergence (normalized line ' + (i + 1) + '):\n' +
      '      prod: ' + (p[i] || '<EOF>').slice(0, 120) + '\n' +
      '      beta: ' + (b[i] || '<EOF>').slice(0, 120));
  }
})();

// ── 3. CACHE_VERSION must be bumped whenever a precached page ships ───────
console.log('== Service-worker cache version freshness ==');

const PRECACHED = [
  'index.html', 'beta/index.html',
  'highlights.html', 'beta/highlights.html',
  'share.html', 'beta/share.html',
];

function git(args) {
  return cp.execSync('git ' + args, { cwd: ROOT, stdio: ['ignore', 'pipe', 'ignore'] })
    .toString().trim();
}

(function () {
  try { git('rev-parse --git-dir'); } catch (e) {
    console.log('  (git unavailable — skipping cache-version checks)');
    return;
  }

  // Uncommitted state: page edited but service worker untouched.
  try {
    const dirty = git('diff --name-only HEAD').split('\n').filter(Boolean);
    const dirtyPages = dirty.filter(function (f) { return PRECACHED.indexOf(f) !== -1; });
    if (dirtyPages.length === 0 || dirty.indexOf('service-worker.js') !== -1) {
      ok('working tree: no page change without a service-worker change');
    } else {
      fail('working tree: ' + dirtyPages.join(', ') + ' modified but service-worker.js is not',
        'Bump CACHE_VERSION in service-worker.js before committing, or PWA users keep the old build.');
    }
  } catch (e) {
    fail('working-tree cache check errored', String(e.message || e).slice(0, 200));
  }

  // Committed history: the last commit touching a precached page must be the
  // CACHE_VERSION-bump commit itself, or an ancestor of it.
  //
  // --diff-merges=first-parent matters here. `git log -G` produces no diff for
  // a merge commit by default, so a CACHE_VERSION bump made while resolving a
  // merge is invisible to the plain form — while `log -- <paths>` *does*
  // report that same merge as the last commit touching a page. The two halves
  // then disagree and the check fails on a build that is in fact correct.
  try {
    const hPages = git('log -1 --format=%H -- ' + PRECACHED.join(' '));
    // -s suppresses the patch: --diff-merges turns it back on, which would
    // otherwise land in the captured output alongside %H.
    const hBump = git('log -1 -s --format=%H --diff-merges=first-parent -G"CACHE_VERSION" -- service-worker.js');
    if (!hPages || !hBump) {
      ok('history: nothing to compare yet');
    } else if (hPages === hBump) {
      ok('history: latest page change and CACHE_VERSION bump are in the same commit');
    } else {
      try {
        git('merge-base --is-ancestor ' + hPages + ' ' + hBump);
        ok('history: CACHE_VERSION was bumped after the latest page change');
      } catch (e) {
        fail('history: pages changed in ' + hPages.slice(0, 7) +
          ' but CACHE_VERSION was last bumped in older commit ' + hBump.slice(0, 7),
          'Bump CACHE_VERSION in service-worker.js so PWA users pick up the new build.');
      }
    }
  } catch (e) {
    fail('history cache check errored', String(e.message || e).slice(0, 200));
  }
})();

// ── The two shells must claim the same release ─────────────────────────────
// index.html and beta/index.html are deliberately not byte-identical, so the
// pair check above cannot cover them — which let softwareVersion drift once
// already: a `git checkout index.html` during an unrelated test reverted the
// bump in production while beta kept it, and every existing check still
// passed. The version is in the Schema.org block search engines read, so a
// stale one is wrong in public, not just untidy.
(function shellVersionsAgree() {
  console.log('\n== Landing shells declare the same softwareVersion ==');
  const re = /"softwareVersion": *"([^"]*)"/;
  const got = {};
  for (const f of ['index.html', 'beta/index.html']) {
    const m = re.exec(read(f));
    if (!m) { fail(f + ': no softwareVersion in the JSON-LD block'); return; }
    got[f] = m[1];
  }
  if (got['index.html'] === got['beta/index.html']) {
    ok('both shells declare ' + got['index.html']);
  } else {
    fail('softwareVersion has drifted: index.html says ' + got['index.html'] +
      ', beta/index.html says ' + got['beta/index.html'],
      'Set both to the release you are shipping.');
  }
})();

// ── Summary ────────────────────────────────────────────────────────────────
console.log('\n== SUMMARY ==\n');
if (failCount) {
  console.log(failCount + ' parity check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
} else {
  console.log('All ' + pass + ' parity checks passed.');
}

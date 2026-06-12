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

const IDENTICAL_PAIRS = [
  ['js/app.js', 'beta/js/app.js'],
  ['js/forum.js', 'beta/js/forum.js'],
  ['js/jw-session.js', 'beta/js/jw-session.js'],
  ['js/merge-worker.js', 'beta/js/merge-worker.js'],
  ['js/semantic-worker.js', 'beta/js/semantic-worker.js'],
  ['highlights.html', 'beta/highlights.html'],
  ['share.html', 'beta/share.html'],
  ['styles.css', 'beta/styles.css'],
];

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
  try {
    const hPages = git('log -1 --format=%H -- ' + PRECACHED.join(' '));
    const hBump = git('log -1 --format=%H -G"CACHE_VERSION" -- service-worker.js');
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

// ── Summary ────────────────────────────────────────────────────────────────
console.log('\n== SUMMARY ==\n');
if (failCount) {
  console.log(failCount + ' parity check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
} else {
  console.log('All ' + pass + ' parity checks passed.');
}

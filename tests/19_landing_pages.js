#!/usr/bin/env node
/**
 * 19_landing_pages.js — pre-rendered per-language landing pages.
 *
 * jwsync.org/ is one document with client-side i18n, so ?lang=xx serves
 * byte-identical English HTML and Google indexes nothing extra. /<lang>/ pages
 * exist to be the real, indexable document for each language.
 *
 * That only works if four things hold, and each has a way of quietly breaking:
 *
 *   1. The copy is actually baked into the HTML. If a page ever regressed to
 *      empty elements filled in by JS, it would be back to square one — so the
 *      translated hero text is asserted to be present in the source.
 *   2. Every page is its own canonical and the cluster is reciprocal. A
 *      one-way or self-contradicting cluster is ignored wholesale.
 *   3. No alternate points at a ?lang= URL — the original Search Console
 *      failure. 01_static.js guards the landing shell; this guards the twins.
 *   4. The pages carry real content. A thin page that only funnels to the app
 *      is a doorway page, which is worse than not having it.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const REPO = path.join(__dirname, '..');
const SITE = 'https://jwsync.org';
const LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'ru', 'ja', 'ko', 'tl', 'sv', 'ceb', 'ar', 'he'];
const RTL = new Set(['ar', 'he']);

let pass = 0, failCount = 0;
function section(t) { console.log('\n== ' + t + ' =='); }
function ok(n) { pass++; console.log('  ✓ ' + n); }
function fail(n, d) { failCount++; console.log('  ✗ ' + n); if (d) console.log('      ' + d); }

const url = (l) => (l === 'en' ? SITE + '/' : SITE + '/' + l + '/');
const file = (l) => (l === 'en' ? 'index.html' : l + '/index.html');
const read = (l) => fs.readFileSync(path.join(REPO, file(l)), 'utf8');

// ── 1. The pages exist and declare themselves correctly ───────────────────
section('Every language has a landing document');
{
  let bad = 0;
  for (const l of LANGS) {
    const p = path.join(REPO, file(l));
    if (!fs.existsSync(p)) { fail(l + ': ' + file(l) + ' missing'); bad++; continue; }
    const c = fs.readFileSync(p, 'utf8');
    const tag = (c.match(/<html[^>]*>/) || [''])[0];
    if (!new RegExp('lang="' + l + '"').test(tag)) { fail(l + ': <html lang> is ' + tag); bad++; continue; }
    if (RTL.has(l) && !/dir="rtl"/.test(tag)) { fail(l + ': RTL language without dir="rtl"'); bad++; continue; }
    if (!RTL.has(l) && /dir="rtl"/.test(tag)) { fail(l + ': LTR language marked rtl'); bad++; continue; }
  }
  if (!bad) ok('all ' + LANGS.length + ' pages present with correct lang/dir');
}

// ── 2. Canonicals and a reciprocal cluster ────────────────────────────────
section('hreflang cluster is complete and reciprocal');
{
  let bad = 0;
  for (const l of LANGS) {
    const c = read(l);
    const canon = (c.match(/<link rel="canonical" href="([^"]*)"/) || [])[1];
    if (canon !== url(l)) { fail(l + ': canonical is ' + canon + ', expected ' + url(l)); bad++; }
    const alts = {};
    for (const m of c.matchAll(/hreflang="([a-z-]+)" href="([^"]*)"/g)) alts[m[1]] = m[2];
    for (const o of LANGS) {
      if (alts[o] !== url(o)) { fail(l + ': alternate for ' + o + ' is ' + alts[o]); bad++; }
    }
    if (alts['x-default'] !== url('en')) { fail(l + ': x-default is ' + alts['x-default']); bad++; }
  }
  if (!bad) ok('all ' + LANGS.length + ' pages self-canonical, each linking the full set + x-default');

  // The failure this whole exercise exists to avoid.
  let param = 0;
  for (const l of LANGS) {
    for (const m of read(l).matchAll(/hreflang="[a-z-]+" href="([^"]*)"/g)) {
      if (m[1].includes('?')) param++;
    }
  }
  if (!param) ok('no alternate points at a ?lang= URL');
  else fail(param + ' alternate(s) point at parameterised URLs that canonicalise away');
}

// ── 3. The copy is server-rendered, not filled in by JS ───────────────────
section('Translated copy is baked into the HTML');
{
  // Pull the expected hero text straight from the dictionary the pages build
  // from, so this cannot drift into asserting stale strings.
  const idx = fs.readFileSync(path.join(REPO, 'index.html'), 'utf8');
  const m = idx.match(/__JW_LANDING_I18N *= */);
  const ts = m.index + m[0].length;
  let d = 0, e = ts;
  for (let i = ts; i < idx.length; i++) {
    if (idx[i] === '{') d++;
    else if (idx[i] === '}') { d--; if (d === 0) { e = i + 1; break; } }
  }
  const dict = JSON.parse(idx.slice(ts, e));

  let bad = 0;
  for (const l of LANGS) {
    if (l === 'en') continue;   // "/" is the app shell; it localizes at runtime
    const c = read(l);
    const hero = dict[l].hero_title;
    if (!c.includes(hero)) { fail(l + ': hero text not in the served HTML'); bad++; continue; }
    if (c.includes(dict.en.hero_title)) { fail(l + ': English hero leaked into the page'); bad++; continue; }
    if (!c.includes(dict[l].hero_desc)) { fail(l + ': hero description missing'); bad++; }
  }
  if (!bad) ok('every localized page serves its own translated hero, no English fallback');
}

// ── 4. Real content, not a doorway ────────────────────────────────────────
section('Pages carry substantive content');
{
  // Measured in characters, not words: Japanese and Korean do not delimit
  // words with spaces, so a word count reports Japanese as 73 for the same
  // page that holds 1,510 characters of copy. Characters compare fairly
  // across scripts.
  let worst = null, bad = 0;
  for (const l of LANGS) {
    if (l === 'en') continue;
    const c = read(l);
    const main = c.slice(c.indexOf('<main'), c.indexOf('</main>'));
    const text = main.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    if (!worst || text.length < worst.chars) worst = { l, chars: text.length };
    // Five FAQ pairs, four walkthrough steps, five features, six tools.
    const dt = (main.match(/<dt>/g) || []).length;
    const steps = (main.match(/<li><h3>/g) || []).length;
    if (dt !== 5) { fail(l + ': ' + dt + ' FAQ entries, expected 5'); bad++; }
    if (steps !== 4) { fail(l + ': ' + steps + ' walkthrough steps, expected 4'); bad++; }
  }
  if (worst && worst.chars >= 1200) ok('thinnest page has ' + worst.chars + ' characters (' + worst.l + ')');
  else if (worst) fail('thinnest page has only ' + worst.chars + ' characters (' + worst.l + ') — reads as a doorway page');
  if (!bad) ok('every page has 5 FAQ entries and the 4-step walkthrough');
}

// ── 5. Structured data ────────────────────────────────────────────────────
section('Structured data declares the right language');
{
  let bad = 0;
  for (const l of LANGS) {
    if (l === 'en') continue;
    const c = read(l);
    const m = c.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
    if (!m) { fail(l + ': no JSON-LD'); bad++; continue; }
    let ld;
    try { ld = JSON.parse(m[1]); } catch (e) { fail(l + ': JSON-LD does not parse'); bad++; continue; }
    const s = JSON.stringify(ld);
    if (!s.includes('"inLanguage":"' + l + '"')) { fail(l + ': inLanguage is not ' + l); bad++; continue; }
    const faq = ld['@graph'].find(n => n['@type'] === 'FAQPage');
    if (!faq || faq.mainEntity.length !== 5) { fail(l + ': FAQPage missing or incomplete'); bad++; }
  }
  if (!bad) ok('every page: valid JSON-LD, correct inLanguage, 5-entry FAQPage');
}

// ── 6. Sitemap ────────────────────────────────────────────────────────────
section('Sitemap submits the cluster');
{
  const sm = fs.readFileSync(path.join(REPO, 'sitemap.xml'), 'utf8');
  const locs = [...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
  const missing = LANGS.map(url).filter(u => !locs.includes(u));
  if (!missing.length) ok('all ' + LANGS.length + ' landing URLs submitted');
  else fail('sitemap missing: ' + missing.join(', '));
  const param = locs.filter(u => u.includes('?'));
  if (!param.length) ok('sitemap submits no parameterised URLs');
  else fail('sitemap submits: ' + param.join(', '));
}

// ── Summary ───────────────────────────────────────────────────────────────
section('SUMMARY');
if (failCount) {
  console.log(failCount + ' landing-page check(s) FAILED (' + pass + ' passed).');
  process.exit(1);
}
console.log('All ' + pass + ' landing-page checks passed.');

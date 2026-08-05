'use strict';
/**
 * browse-source.js — locate the Note Explorer (Browse) module.
 *
 * v3.8.0 lifted the module's 185 KB <script> out of the page and into
 * js/browse.js, fetched on demand by bootBrowse(). The <style> block stays in
 * the page. Production keeps the old inline copy until a "go live", so the
 * suites have to handle both shapes — same duality 01_static.js already
 * handles for the main app bundle (inline <script> vs js/app.js).
 *
 * All three helpers take an absolute path to an index.html.
 */
const fs = require('fs');

const OPEN = /<!-- ── Note Explorer \(Browse\) ─/;

/** The Note Explorer <style> block. Always inline in the page. */
function browseCss(pageAbs) {
  const c = fs.readFileSync(pageAbs, 'utf8');
  const m = c.match(/<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<style>([\s\S]*?)<\/style>/);
  return m ? m[1] : '';
}

/**
 * The Browse module source: the inline <script> when the page still carries
 * one, otherwise the sibling js/browse.js the page now loads on demand.
 * Returns null when neither exists.
 */
function browseJs(pageAbs) {
  const c = fs.readFileSync(pageAbs, 'utf8');
  if (!OPEN.test(c)) return null;
  const inline = c.match(
    /<!-- ── Note Explorer \(Browse\) ─[\s\S]*?<script>([\s\S]*?)<\/script>\s*<!-- ── End Note Explorer/);
  if (inline) return inline[1];
  const ext = pageAbs.replace(/index\.html$/, 'js/browse.js');
  if (!fs.existsSync(ext)) return null;
  return fs.readFileSync(ext, 'utf8');
}

/**
 * A <style> + <script> fragment equivalent to the old inline block, for
 * booting the module inside JSDOM.
 */
function browseBlock(pageAbs) {
  const js = browseJs(pageAbs);
  if (js == null) return null;
  return '<style>' + browseCss(pageAbs) + '</style>\n<script>' + js + '<' + '/script>';
}

module.exports = { browseCss, browseJs, browseBlock };

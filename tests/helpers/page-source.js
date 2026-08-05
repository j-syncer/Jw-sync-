'use strict';
/**
 * page-source.js — "everything this page ships".
 *
 * v3.8.0 lifted nine feature modules out of index.html into js/*.js so the HTML
 * document stopped carrying 500 KB of inline script on every page load. The
 * code did not change, only where it lives, so the suites that assert a feature
 * is present need a haystack spanning the page *and* its modules.
 *
 * Production keeps the inline copies until a "go live", at which point the
 * modules simply aren't there and this returns the page unchanged — which is
 * exactly right, because production is still serving them inline.
 *
 * Use this for "feature X is present" checks only. Structural assertions about
 * the HTML itself (script tags, markup, "must NOT be inline") must keep reading
 * the page directly, or they'd pass against the module file.
 */
const fs = require('fs');
const path = require('path');

// Modules extracted from index.html in v3.8.0, in document order.
const EXTRACTED = [
  'browse.js', 'demo.js', 'conflict-review.js', 'impact-preview.js',
  'post-merge.js', 'sync-hub.js', 'receive.js', 'wizard.js', 'doctor.js',
];

/** Source of one extracted module beside `pageAbs`, or '' when still inline. */
function moduleSrc(pageAbs, name) {
  const p = path.join(path.dirname(pageAbs), 'js', name);
  return fs.existsSync(p) ? fs.readFileSync(p, 'utf8') : '';
}

/** The page followed by every extracted module that sits beside it. */
function withModules(pageAbs) {
  let out = fs.readFileSync(pageAbs, 'utf8');
  for (const name of EXTRACTED) {
    const src = moduleSrc(pageAbs, name);
    if (src) out += '\n/* ==== ' + name + ' ==== */\n' + src;
  }
  return out;
}

module.exports = { EXTRACTED, moduleSrc, withModules };

/**
 * Swap the `<script src="js/NAME.js" defer>` tags v3.8.0 introduced back for
 * the module source, so JSDOM (which does not fetch external scripts) sees the
 * same page a browser does. Only touches the extracted modules; lazily fetched
 * bundles like js/browse.js have no tag and stay lazy, which is what the
 * code-splitting assertions check for.
 */
function inlineModules(html, pageAbs) {
  for (const name of EXTRACTED) {
    const tag = new RegExp('<script src="js/' + name.replace('.', '\\.') + '"[^>]*></script>');
    if (!tag.test(html)) continue;
    const src = moduleSrc(pageAbs, name);
    if (!src) continue;
    html = html.replace(tag, '<script>' + src + '<' + '/script>');
  }
  return html;
}

module.exports.inlineModules = inlineModules;

// Light-mode coverage guard, shared by the standalone-page suites.
//
// share.html and highlights.html each ship their own <style> block and their
// own light theme. Both had lightened only their header: the body kept
// #060d1a while cards turned white, so "light mode" read as a rendering
// fault. Nothing failed, because no test looked at colour at all.
//
// This walks every rule in a page's <style> blocks and asks: does it paint
// with a dark-theme token — near-white ink, or one of the page's dark
// surfaces? If so it must have a `body.light` counterpart. Accent surfaces
// (orange buttons, medal discs) are exempt: they carry their own contrast and
// look the same in both themes.

const INK = ['#fff', '#ffffff', '#f8fafc', '#f1f5f9', '#e2e8f0', '#e7eaf3', '#cbd5e1'];
const SURFACE = ['#060d1a', '#0a1224', 'rgba(2,6,20', 'rgba(4,15,34', 'rgba(11,20,36',
  'rgba(15,23,42', 'rgba(255,255,255,'];
const ACCENT = ['#ea580c', '#c2410c', 'rgba(234,88,12', 'rgba(52,211,153', 'rgba(5,150,105',
  'rgba(251,191,36', 'rgba(248,113,113',
  // a page themed through variables paints its accents the same way
  'var(--accent)', 'var(--accent2)'];

// Parse the rules out of a page's <style> blocks. Brace-matched rather than
// line-matched: a rule written across several lines (highlights.html's own
// `body { … }` is one) would otherwise be invisible to the scan.
function rulesIn(html) {
  const out = [];
  let idx = 0;
  for (;;) {
    const s = html.indexOf('<style', idx);
    if (s < 0) break;
    const open = html.indexOf('>', s);
    const e = html.indexOf('</style>', open);
    if (open < 0 || e < 0) break;
    collect(html.slice(open + 1, e).replace(/\/\*[\s\S]*?\*\//g, ''), out);
    idx = e + 8;
  }
  return out;
}

function collect(css, out) {
  let i = 0;
  while (i < css.length) {
    const brace = css.indexOf('{', i);
    if (brace < 0) break;
    const sel = css.slice(i, brace).trim();
    let depth = 1, j = brace + 1;
    while (j < css.length && depth) {
      if (css[j] === '{') depth++;
      else if (css[j] === '}') depth--;
      j++;
    }
    const body = css.slice(brace + 1, j - 1);
    if (sel.startsWith('@')) collect(body, out);          // @media, @supports…
    else if (sel) out.push({ sel, body: body.replace(/\s+/g, ' ').trim() });
    i = j;
  }
}

// An accent surface only carries its own contrast when it is actually painted:
// rgba(234,88,12,.04) is a tint, and white ink on a tint is unreadable once the
// page behind it turns white. Only a solid-enough accent earns the exemption.
function opaqueEnough(value) {
  const m = /rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*([\d.]+)\s*\)/.exec(value);
  return m ? parseFloat(m[1]) >= 0.5 : true;
}

// allow: selectors exempt from needing a light twin, each with a reason
function auditLightMode(html, allow) {
  const skip = new Set(allow || []);
  const rules = rulesIn(html);
  const light = new Set();
  // collect the light rules first — the light block usually sits at the end of
  // the stylesheet, so a single pass would report everything above it
  let paintsPage = false;
  for (const r of rules) {
    if (!r.sel.startsWith('body.light')) continue;
    // a light rule may list several selectors: body.light .a, body.light .b
    for (const part of r.sel.split(',')) {
      const key = part.trim().replace(/^body\.light\s*/, '').trim() || 'body';
      light.add(key);
      // the page itself counts as repainted either by a literal background or
      // by redeclaring the surface variable a variable-driven page paints from
      if (key === 'body' && /background|--bg\s*:/.test(r.body)) paintsPage = true;
    }
  }
  const missing = [];
  let checked = 0;
  for (const { sel, body } of rules) {
    if (sel.startsWith('body.light') || skip.has(sel)) continue;
    const bg = (/background(?:-color)?:\s*([^;]+)/.exec(body) || [])[1] || '';
    const ink = (/(?:^|;)\s*color:\s*([^;]+)/.exec(body) || [])[1] || '';
    if (ACCENT.some(a => bg.includes(a)) && opaqueEnough(bg)) continue;
    if (!(INK.includes(ink.trim()) || SURFACE.some(s => bg.includes(s)))) continue;
    checked++;
    if (!light.has(sel)) missing.push(sel);
  }
  return { checked, missing, paintsPage };
}

// A page themed through custom properties (forum.html, and #forum-view inside
// the app) hides its whole palette behind var(--…), so the literal scan above
// sees almost nothing. This is the other half: every dark custom property
// declared for the theme must be redeclared under body.light, or the light
// theme paints from the dark value.
function luminance(v) {
  let m = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.exec(v.trim());
  let r, g, b;
  if (m) {
    const h = m[1].length === 3 ? m[1].replace(/./g, ch => ch + ch) : m[1];
    r = parseInt(h.slice(0, 2), 16); g = parseInt(h.slice(2, 4), 16); b = parseInt(h.slice(4, 6), 16);
  } else if ((m = /^rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/i.exec(v.trim()))) {
    r = +m[1]; g = +m[2]; b = +m[3];
  } else return null;
  return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
}

// css:  stylesheet text (a page's <style> contents, or a .css file)
// opts.scope: selector the theme's variables are declared on (':root' default)
// opts.only:  restrict to these variable names — styles.css holds two palettes,
//             and the app's own --color-* tokens are themed by rule overrides
//             rather than by redeclaration, so they are not this check's business
function auditThemeVars(css, opts) {
  opts = opts || {};
  const scope = opts.scope;
  const out = [];
  collect(css.replace(/\/\*[\s\S]*?\*\//g, ''), out);
  const declaredIn = sel => {
    const vars = {};
    for (const r of out) {
      if (r.sel !== sel) continue;
      for (const m of r.body.matchAll(/(--[\w-]+)\s*:\s*([^;]+)/g)) vars[m[1]] = m[2].trim();
    }
    return vars;
  };
  const theme = declaredIn(scope || ':root');
  const light = Object.assign({}, declaredIn('body.light'), declaredIn('body.light ' + (scope || '')).valueOf());
  const dark = [], missing = [];
  for (const [name, value] of Object.entries(theme)) {
    const l = luminance(value);
    if (l === null || l > 0.35) continue;   // accents and light inks theme themselves
    if (opts.only && opts.only.indexOf(name) < 0) continue;
    dark.push(name);
    if (!(name in light)) missing.push(name);
  }
  return { dark, missing };
}

module.exports = { auditLightMode, auditThemeVars };

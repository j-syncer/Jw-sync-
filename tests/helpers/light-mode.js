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
  'rgba(251,191,36', 'rgba(248,113,113'];

function rulesIn(html) {
  const out = [];
  let idx = 0;
  for (;;) {
    const s = html.indexOf('<style>', idx);
    if (s < 0) break;
    const e = html.indexOf('</style>', s);
    const css = html.slice(s + 7, e);
    idx = e + 8;
    for (const raw of css.split('\n')) {
      const m = /^([^{@/][^{]*)\{(.*)\}$/.exec(raw.trim());
      if (m) out.push({ sel: m[1].trim(), body: m[2] });
    }
  }
  return out;
}

// allow: selectors exempt from needing a light twin, each with a reason
function auditLightMode(html, allow) {
  const skip = new Set(allow || []);
  const rules = rulesIn(html);
  const light = new Set();
  // collect the light rules first — the light block usually sits at the end of
  // the stylesheet, so a single pass would report everything above it
  for (const r of rules) {
    if (!r.sel.startsWith('body.light')) continue;
    // a light rule may list several selectors: body.light .a, body.light .b
    for (const part of r.sel.split(','))
      light.add(part.trim().replace(/^body\.light\s*/, '').trim() || 'body');
  }
  const missing = [];
  let checked = 0;
  for (const { sel, body } of rules) {
    if (sel.startsWith('body.light') || skip.has(sel)) continue;
    const bg = (/background(?:-color)?:\s*([^;]+)/.exec(body) || [])[1] || '';
    const ink = (/(?:^|;)\s*color:\s*([^;]+)/.exec(body) || [])[1] || '';
    if (ACCENT.some(a => bg.includes(a))) continue;
    if (!(INK.includes(ink.trim()) || SURFACE.some(s => bg.includes(s)))) continue;
    checked++;
    if (!light.has(sel)) missing.push(sel);
  }
  return { checked, missing, paintsPage: light.has('body') };
}

module.exports = { auditLightMode };

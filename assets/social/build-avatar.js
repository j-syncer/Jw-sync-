// Generates the JW Sync Instagram avatar artwork (1080x1080, circle-crop safe).
const fs = require('fs');

const S = 1080, C = S / 2;

// ── palette (matches icon-512.png / og-image.png) ───────────────────────────
const BG = '#17110d';
const AMBER_HI = '#fbbf24';
const AMBER_MID = '#f59e0b';
const ORANGE = '#ea580c';
const SCREEN = '#060d1c';
const HALO = '#0a0705';
const HL = { y: '#facc15', g: '#4ade80', b: '#60a5fa', p: '#f472b6' };

const r2 = (n) => Math.round(n * 100) / 100;

// ── screen content ──────────────────────────────────────────────────────────
// rows: [kind, widthFraction]  kind: 'title' | 'plain' | highlight colour key
function screenRows(rows, sx, sy, sw, sh, pad, lh, gap) {
  let out = '', y = sy + pad;
  for (const [kind, frac] of rows) {
    const w = (sw - pad * 2) * frac;
    if (kind === 'title') {
      out += `<rect x="${r2(sx + pad)}" y="${r2(y)}" width="${r2(w)}" height="${r2(lh * 1.35)}" rx="${r2(lh * 0.55)}" fill="${AMBER_MID}" opacity=".95"/>`;
      y += lh * 1.35 + gap * 1.7;
      continue;
    }
    const isHl = kind !== 'plain';
    out += `<rect x="${r2(sx + pad)}" y="${r2(y)}" width="${r2(w)}" height="${r2(lh)}" rx="${r2(lh / 2)}" fill="${isHl ? HL[kind] : '#cbd5e1'}" opacity="${isHl ? 0.72 : 0.24}"/>`;
    y += lh + gap;
  }
  return out;
}

// ── devices ─────────────────────────────────────────────────────────────────
function phone(cx, cy, rot) {
  const w = 235, h = 430, rx = 34;
  const sw = 203, sh = 378;
  const rows = [
    ['title', 0.66],
    ['plain', 0.96], ['y', 0.86], ['plain', 0.92], ['g', 0.7],
    ['plain', 0.94], ['b', 0.8],
  ];
  return `<g transform="translate(${cx} ${cy}) rotate(${rot})">
    <rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h}" rx="${rx}" fill="url(#body)" stroke="url(#edge)" stroke-width="3.5"/>
    <rect x="${-sw / 2}" y="${-sh / 2 - 7}" width="${sw}" height="${sh}" rx="20" fill="${SCREEN}"/>
    ${screenRows(rows, -sw / 2, -sh / 2 - 7, sw, sh, 21, 13, 19)}
    <rect x="-26" y="${-h / 2 + 14}" width="52" height="8" rx="4" fill="#0b1220" opacity=".85"/>
    <rect x="-44" y="${h / 2 - 24}" width="88" height="7" rx="3.5" fill="#94a3b8" opacity=".35"/>
  </g>`;
}

function tablet(cx, cy, rot) {
  const w = 355, h = 470, rx = 30;
  const sw = 313, sh = 404;
  const rows = [
    ['title', 0.56],
    ['plain', 0.96], ['y', 0.84], ['plain', 0.9], ['g', 0.72],
    ['plain', 0.95], ['b', 0.78], ['p', 0.62],
  ];
  return `<g transform="translate(${cx} ${cy}) rotate(${rot})">
    <rect x="${-w / 2}" y="${-h / 2}" width="${w}" height="${h}" rx="${rx}" fill="url(#body)" stroke="url(#edge)" stroke-width="3.5"/>
    <rect x="${-sw / 2}" y="${-sh / 2 - 5}" width="${sw}" height="${sh}" rx="14" fill="${SCREEN}"/>
    ${screenRows(rows, -sw / 2, -sh / 2 - 5, sw, sh, 28, 15, 20)}
    <circle cx="0" cy="${-h / 2 + 14}" r="5" fill="#0b1220" opacity=".9"/>
  </g>`;
}

// ── centre glyph A: brand "Y" merge swoop (two sources → one) ───────────────
const SWOOP = 'M373 250 C 373 430, 683 430, 683 250';
const STEM = 'M528 380 L 528 490';
const DOTS = [[373, 250, 25], [683, 250, 25], [528, 502, 23]];
// every dark outline is laid down first, so no halo can bite into the amber
const glyphY = `
  <g stroke-linecap="round" fill="none" opacity=".95">
    <path d="${SWOOP}" stroke="${HALO}" stroke-width="49"/>
    <path d="${STEM}" stroke="${HALO}" stroke-width="49"/>
  </g>
  ${DOTS.map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r + 8}" fill="${HALO}" opacity=".95"/>`).join('')}
  <g stroke-linecap="round" fill="none">
    <path d="${SWOOP}" stroke="url(#glyph)" stroke-width="33"/>
    <path d="${STEM}" stroke="url(#glyph)" stroke-width="33"/>
  </g>
  ${DOTS.map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${AMBER_HI}"/>`).join('')}`;

// ── centre glyph B: bidirectional sync arrows ───────────────────────────────
function syncArrows() {
  const cx = 528, cy = 300, r = 80, sw = 27;
  const P = (a) => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)];
  const arc = (a0, a1) => {
    const [x0, y0] = P(a0), [x1, y1] = P(a1);
    return `M ${r2(x0)} ${r2(y0)} A ${r} ${r} 0 0 1 ${r2(x1)} ${r2(y1)}`;
  };
  // arrowhead at angle `a` on the circle, pointing along the clockwise tangent
  const head = (a) => {
    const rad = a * Math.PI / 180;
    const [x, y] = P(a);
    const tx = -Math.sin(rad), ty = Math.cos(rad);   // clockwise tangent
    const nx = Math.cos(rad), ny = Math.sin(rad);    // outward radial
    const L = 44, W = 27;
    return [
      [x + tx * L, y + ty * L],
      [x + nx * W, y + ny * W],
      [x - nx * W, y - ny * W],
    ].map(([a2, b2]) => `${r2(a2)},${r2(b2)}`).join(' ');
  };
  return `
  <g fill="none" stroke-linecap="round">
    <path d="${arc(-165, -25)}" stroke="${HALO}" stroke-width="${sw + 22}" opacity=".95"/>
    <path d="${arc(15, 155)}" stroke="${HALO}" stroke-width="${sw + 22}" opacity=".95"/>
    <path d="${arc(-165, -25)}" stroke="url(#glyph)" stroke-width="${sw}"/>
    <path d="${arc(15, 155)}" stroke="url(#glyph)" stroke-width="${sw}"/>
  </g>
  ${[-25, 155].map(a => `<polygon points="${head(a)}" fill="${AMBER_HI}" stroke="${HALO}" stroke-width="9" stroke-linejoin="round" paint-order="stroke"/>`).join('')}`;
}

// ── page ────────────────────────────────────────────────────────────────────
const defs = `
<defs>
  <radialGradient id="glow" cx="50%" cy="46%" r="72%">
    <stop offset="0%" stop-color="${ORANGE}" stop-opacity=".38"/>
    <stop offset="45%" stop-color="#9a3412" stop-opacity=".20"/>
    <stop offset="100%" stop-color="#7c2d12" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#26364a"/>
    <stop offset="100%" stop-color="#0d1524"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0%" stop-color="#94a3b8" stop-opacity=".6"/>
    <stop offset="100%" stop-color="#94a3b8" stop-opacity=".12"/>
  </linearGradient>
  <!-- userSpaceOnUse: a vertical stem has a zero-width bbox, which makes an
       objectBoundingBox gradient degenerate and the stroke disappear -->
  <linearGradient id="glyph" gradientUnits="userSpaceOnUse" x1="350" y1="240" x2="700" y2="430">
    <stop offset="0%" stop-color="${AMBER_HI}"/>
    <stop offset="55%" stop-color="${AMBER_MID}"/>
    <stop offset="100%" stop-color="${ORANGE}"/>
  </linearGradient>
  <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
    <feGaussianBlur stdDeviation="38"/>
  </filter>
</defs>`;

function stage(id, centre) {
  return `<svg id="${id}" class="stage" width="${S}" height="${S}" viewBox="0 0 ${S} ${S}" xmlns="http://www.w3.org/2000/svg">
  ${defs}
  <rect width="${S}" height="${S}" fill="${BG}"/>
  <rect width="${S}" height="${S}" fill="url(#glow)"/>

  <!-- nudge the whole cluster so its mass sits on the crop circle's centre -->
  <g transform="translate(-25 -12)">
    <!-- contact shadow under the devices -->
    <g filter="url(#soft)" opacity=".6">
      <ellipse cx="330" cy="740" rx="150" ry="180" fill="${HALO}"/>
      <ellipse cx="745" cy="720" rx="200" ry="190" fill="${HALO}"/>
    </g>

    ${phone(330, 660, -7)}
    ${tablet(745, 615, 6)}
    ${centre}
  </g>
</svg>`;
}

const html = `<style>
  html,body{margin:0;padding:0;background:#000}
  .stage{display:block}
  #wrap{display:flex;flex-direction:column}
</style>
<div id="wrap">
  ${stage('a', glyphY)}
  ${stage('b', syncArrows())}
</div>`;

const dir = process.argv[2];
fs.writeFileSync(`${dir}/avatar.html`, html);
console.log('wrote avatar.html');

#!/usr/bin/env python3
"""v2.70.0 — Unified, premium cross-tool navigation (shared files).

The satellite pages (Study Stats, Share) used a text-only "Merge / Stats /
Explorer / Share" pill that looked nothing like the main site nav. This:

1. Redesigns the shared cross-tool switcher (js/jw-session.js → mountSwitcher)
   into an icon + label navigation whose buttons match the main site's
   .site-nav-link exactly (paddings, hover, orange active state) — now with a
   crisp inline icon per tool, full light-mode support, and an icon-only
   collapse on very small screens.
2. Aligns both satellite page headers (highlights.html, share.html) to the
   main nav: same translucent navy background, the "JW Sync" wordmark styled
   like the site logo (white, bold, orange on hover), and the page title
   de-emphasised from competing orange to a quiet slate — so orange lives
   only in the active nav item, exactly like the main site.

All files here are shared (ship to both sites in lockstep); twins kept
identical. Bumps SW CACHE_VERSION (precached pages changed) + softwareVersion.
"""

# ── 1. jw-session.js: ICONS + icon-aware button build + premium CSS ──────────
JS_TOOLS = """  var TOOLS = [
    { id: 'merge',    href: 'index.html#app' },
    { id: 'stats',    href: 'highlights.html' },
    { id: 'explorer', href: 'index.html#browse' },
    { id: 'share',    href: 'share.html' }
  ];"""

JS_ICONS = """  var TOOLS = [
    { id: 'merge',    href: 'index.html#app' },
    { id: 'stats',    href: 'highlights.html' },
    { id: 'explorer', href: 'index.html#browse' },
    { id: 'share',    href: 'share.html' }
  ];

  var ICONS = {
    merge: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M6 21V9a9 9 0 0 0 9 9"></path></svg>',
    stats: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',
    explorer: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
    share: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>'
  };"""

JS_BTN_OLD = """      btn.href = tool.href;
      btn.textContent = (L && L[tool.id]) || tool.id;"""

JS_BTN_NEW = """      btn.href = tool.href;
      var lbl = (L && L[tool.id]) || tool.id;
      btn.innerHTML = (ICONS[tool.id] || '') + '<span class="jw-switch-lbl"></span>';
      var lblEl = btn.querySelector('.jw-switch-lbl');
      if (lblEl) lblEl.textContent = lbl;
      btn.setAttribute('aria-label', lbl);"""

JS_CSS_OLD = """    var css =
      '.jw-switch{display:inline-flex;align-items:center;gap:2px;padding:3px;' +
      'background:rgba(71,85,105,.22);border:1px solid rgba(255,255,255,.08);' +
      'border-radius:9px;flex-wrap:nowrap}' +
      '.jw-switch-btn{appearance:none;background:transparent;border:1px solid transparent;' +
      'color:rgba(203,213,225,.72);font:600 12px/1 inherit;font-family:inherit;' +
      'padding:6px 11px;border-radius:6px;cursor:pointer;white-space:nowrap;text-decoration:none;' +
      'transition:color .15s,background .15s,border-color .15s}' +
      '.jw-switch-btn:hover{color:#f1f5f9;background:rgba(255,255,255,.06)}' +
      '.jw-switch-btn.jw-switch-on{color:#ea580c;background:rgba(234,88,12,.12);' +
      'border-color:rgba(234,88,12,.3);cursor:default}' +
      '.jw-switch-btn:focus-visible{outline:2px solid #ea580c;outline-offset:2px}' +
      '@media(max-width:560px){.jw-switch{gap:0;padding:2px}.jw-switch-btn{padding:6px 8px;font-size:11px}}';"""

JS_CSS_NEW = """    var css =
      '.jw-switch{display:inline-flex;align-items:center;gap:4px;flex-wrap:nowrap}' +
      '.jw-switch-btn{display:inline-flex;align-items:center;gap:7px;appearance:none;background:transparent;' +
      'border:1px solid transparent;color:rgba(203,213,225,.7);font:500 13px/1 inherit;font-family:inherit;' +
      'padding:7px 12px;border-radius:7px;cursor:pointer;white-space:nowrap;text-decoration:none;' +
      'transition:color .15s,background .15s,border-color .15s}' +
      '.jw-switch-btn svg{width:15px;height:15px;flex:none;opacity:.85}' +
      '.jw-switch-btn:hover{color:#f1f5f9;background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.1)}' +
      '.jw-switch-btn.jw-switch-on{color:#ea580c;background:rgba(234,88,12,.1);' +
      'border-color:rgba(234,88,12,.25);cursor:default}' +
      '.jw-switch-btn.jw-switch-on svg{opacity:1}' +
      '.jw-switch-btn:focus-visible{outline:2px solid #ea580c;outline-offset:2px}' +
      '@media(max-width:640px){.jw-switch{gap:2px}.jw-switch-btn{padding:7px 10px;font-size:12px;gap:6px}}' +
      '@media(max-width:560px){.jw-switch-btn .jw-switch-lbl{display:none}.jw-switch-btn{padding:8px;gap:0}}';"""


def patch_js(path):
    c = open(path, encoding='utf-8').read()
    for old, new in [(JS_TOOLS, JS_ICONS), (JS_BTN_OLD, JS_BTN_NEW), (JS_CSS_OLD, JS_CSS_NEW)]:
        assert c.count(old) == 1, '%s: anchor not unique' % path
        c = c.replace(old, new)
    open(path, 'w', encoding='utf-8').write(c)
    print('%s patched' % path)


# ── 2. highlights.html header (spaced CSS) ───────────────────────────────────
HL = [
    ('padding: 0 16px; gap: 12px;\n      background: rgba(8,15,30,.95);',
     'padding: 0 16px; gap: 12px;\n      background: rgba(4,15,34,.92);'),
    ('.hl-back-btn { text-decoration: none; color: rgba(203,213,225,.7); font-size: 14px;\n      flex-shrink: 0; transition: color .15s; cursor: pointer; }',
     '.hl-back-btn { text-decoration: none; color: #f8fafc; font-size: 15px; font-weight: 700; letter-spacing: -.3px;\n      flex-shrink: 0; transition: color .15s; cursor: pointer; }'),
    ('.hl-back-btn:hover { color: #f1f5f9; }',
     '.hl-back-btn:hover { color: #ea580c; }'),
    ('.hl-title { color: #fb923c; font-weight: 600; font-size: 15px; flex-grow: 1; text-align: center;\n      overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }',
     '.hl-title { color: rgba(203,213,225,.55); font-weight: 600; font-size: 14px; flex-grow: 1; text-align: center;\n      overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }'),
]

# ── 3. share.html header (minified CSS) ──────────────────────────────────────
SH = [
    ('background:rgba(8,15,30,.95);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.07)}',
     'background:rgba(4,15,34,.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,.07)}'),
    ('.sh-back{text-decoration:none;color:rgba(203,213,225,.7);font-size:14px;flex-shrink:0;cursor:pointer;background:none;border:none;font-family:inherit;padding:0}',
     '.sh-back{text-decoration:none;color:#f8fafc;font-size:15px;font-weight:700;letter-spacing:-.3px;flex-shrink:0;cursor:pointer;background:none;border:none;font-family:inherit;padding:0}'),
    ('.sh-back:hover{color:#f1f5f9}',
     '.sh-back:hover{color:#ea580c}'),
    ('.sh-htitle{color:#fb923c;font-weight:600;font-size:15px;flex-grow:1;text-align:center;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
     '.sh-htitle{color:rgba(203,213,225,.55);font-weight:600;font-size:14px;flex-grow:1;text-align:center;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}'),
]


def patch_pairs(path, pairs):
    c = open(path, encoding='utf-8').read()
    for old, new in pairs:
        assert c.count(old) == 1, '%s: anchor not unique:\n%s' % (path, old[:80])
        c = c.replace(old, new)
    open(path, 'w', encoding='utf-8').write(c)
    print('%s patched' % path)


patch_js('js/jw-session.js')
patch_js('beta/js/jw-session.js')
patch_pairs('highlights.html', HL)
patch_pairs('beta/highlights.html', HL)
patch_pairs('share.html', SH)
patch_pairs('beta/share.html', SH)

# ── 4. version bumps ─────────────────────────────────────────────────────────
sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v112';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v112';", "const CACHE_VERSION = 'jwsync-v113';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js: CACHE_VERSION -> v113')

for idx in ('beta/index.html', 'index.html'):
    p = open(idx, encoding='utf-8').read()
    assert p.count('"softwareVersion": "2.69.0"') == 1, idx
    p = p.replace('"softwareVersion": "2.69.0"', '"softwareVersion": "2.70.0"')
    open(idx, 'w', encoding='utf-8').write(p)
    print('%s: softwareVersion -> 2.70.0' % idx)
print('done')

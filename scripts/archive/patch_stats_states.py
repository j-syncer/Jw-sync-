#!/usr/bin/env python3
"""v2.71.0 — App-interior aesthetic pass: Study Stats loading + error states.

The Study Stats (highlights.html) loading spinner and error message floated
bare in an empty void, unlike the new welcome card. They now render inside the
same surface card via a small helper (hlCardWrap), so opening a file feels like
the card is working rather than vanishing, and errors get a red alert icon plus
an on-brand recovery button. Shared file → applied to both twins. Bumps SW
CACHE_VERSION (precached page changed) + softwareVersion.
"""

SETMAIN = """    function setMain(html) {
      var m = document.getElementById('hl-main');
      if (m) m.innerHTML = html;
      return m;
    }"""

HELPERS = SETMAIN + """

    function hlCardWrap(inner) {
      return '<div class="hl-pick"><div class="hl-pick-card">' + inner + '</div></div>';
    }
    var HL_ALERT_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>';
    function hlErrorCard(msg) {
      return hlCardWrap('<div class="hl-pick-icon hl-pick-icon-err">' + HL_ALERT_ICON + '</div><div class="hl-error-msg">' + esc(msg) + '</div><button class="hl-error-btn" id="hl-err-retry">' + esc(t('open_file')) + '</button>');
    }"""

SPIN_OLD = """'<div class="hl-loading"><div class="hl-spin"></div><div class="hl-loading-msg">' + esc(msg) + '</div></div>'"""
SPIN_NEW = """hlCardWrap('<div class="hl-spin"></div><div class="hl-loading-msg">' + esc(msg) + '</div>')"""

ERRORS = [
    ("""'<div class="hl-error"><div class="hl-error-msg">' + esc(msg) + '</div><button class="hl-error-btn" id="hl-err-retry">' + esc(t('open_file')) + '</button></div>'""",
     "hlErrorCard(msg)"),
    ("""'<div class="hl-error"><div class="hl-error-msg">' + esc(t('no_notes')) + '</div><button class="hl-error-btn" id="hl-err-retry">' + esc(t('open_file')) + '</button></div>'""",
     "hlErrorCard(t('no_notes'))"),
    ("""'<div class="hl-error"><div class="hl-error-msg">' + esc(t('error')) + '</div><button class="hl-error-btn" id="hl-err-retry">' + esc(t('open_file')) + '</button></div>'""",
     "hlErrorCard(t('error'))"),
]

CSS_BTN_OLD = """    .hl-error-btn { background: transparent; border: 1px solid rgba(248,113,113,.4); color: #f87171;
      border-radius: 8px; padding: 9px 20px; font-size: 14px; cursor: pointer; font-family: inherit; }"""
CSS_BTN_NEW = """    .hl-pick-icon-err { background: rgba(248,113,113,.12); border-color: rgba(248,113,113,.35); color: #f87171; }
    .hl-error-btn { background: #ea580c; color: #fff; border: none;
      border-radius: 8px; padding: 13px 28px; font-size: 15px; font-weight: 600; cursor: pointer; font-family: inherit; margin-top: 4px; transition: background .15s; }
    .hl-error-btn:hover { background: #c2410c; }"""


def patch(path):
    c = open(path, encoding='utf-8').read()
    assert c.count(SETMAIN) == 1, '%s: setMain' % path
    c = c.replace(SETMAIN, HELPERS)
    assert c.count(SPIN_OLD) == 1, '%s: spinner' % path
    c = c.replace(SPIN_OLD, SPIN_NEW)
    for old, new in ERRORS:
        assert c.count(old) == 1, '%s: error site\n%s' % (path, old[:70])
        c = c.replace(old, new)
    assert c.count(CSS_BTN_OLD) == 1, '%s: error-btn css' % path
    c = c.replace(CSS_BTN_OLD, CSS_BTN_NEW)
    open(path, 'w', encoding='utf-8').write(c)
    print('%s patched' % path)


patch('highlights.html')
patch('beta/highlights.html')

sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v113';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v113';", "const CACHE_VERSION = 'jwsync-v114';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js: CACHE_VERSION -> v114')

for idx in ('beta/index.html', 'index.html'):
    p = open(idx, encoding='utf-8').read()
    assert p.count('"softwareVersion": "2.70.0"') == 1, idx
    p = p.replace('"softwareVersion": "2.70.0"', '"softwareVersion": "2.71.0"')
    open(idx, 'w', encoding='utf-8').write(p)
    print('%s: softwareVersion -> 2.71.0' % idx)
print('done')

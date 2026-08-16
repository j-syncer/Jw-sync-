#!/usr/bin/env python3
"""v2.68.1 — Go live: ship hero merge visualization + Home nav link to production.

Copies the v2.67.0 hero visualization (markup + scoped CSS + hero_viz_private
i18n key) and the v2.68.0 Home nav link (+ nav_home i18n key) from
beta/index.html into index.html. The blocks are extracted from the beta file
itself so the two sites can't drift. Bumps softwareVersion + SW CACHE_VERSION.
"""
import json, re

beta = open('beta/index.html', encoding='utf-8').read()
prod = open('index.html', encoding='utf-8').read()

# ── extract the shipped blocks from beta ────────────────────────────────────
css_s = beta.index('<style id="lhv-css">')
css_e = beta.index('</style>', css_s) + len('</style>')
CSS = beta[css_s:css_e]

hero_s = beta.index('<div class="landing-hero landing-hero-split">')
hero_e = beta.index('<div class="svc-section">', hero_s)
HERO = beta[hero_s:hero_e].rstrip() + '\n      '

NAV_LINK = '<a href="#home" id="site-nav-home-link" class="site-nav-link" data-i18n="nav_home">Home</a>'
assert beta.count(NAV_LINK) == 1

def landing_i18n(content):
    m = re.search(r'__JW_LANDING_I18N *= *', content)
    ts = m.end(); d = 0
    for i in range(ts, len(content)):
        if content[i] == '{':
            d += 1
        elif content[i] == '}':
            d -= 1
            if d == 0:
                return ts, i + 1
    raise AssertionError('unbalanced i18n object')

bs, be = landing_i18n(beta)
beta_i18n = json.loads(beta[bs:be])

# ── apply to production ─────────────────────────────────────────────────────
OLD_HERO = '''<div class="landing-hero">
        <h1 data-i18n="hero_title">Merge JW Library backups privately in your browser</h1>
        <p data-i18n="hero_desc">Merge, browse, and edit your JW Library notes, highlights, and bookmarks — entirely in your browser. Your files never leave your device.</p>
      </div>'''
assert prod.count(OLD_HERO) == 1
prod = prod.replace(OLD_HERO + '\n      ', HERO)

LV = '<section id="landing-view" style="display:none">'
assert prod.count(LV) == 1 and prod.count('lhv-css') == 0
prod = prod.replace(LV, CSS + '\n    ' + LV)

NAV_ANCHOR = '<div class="site-nav-links">\n    <a href="#app" id="site-nav-app"'
assert prod.count(NAV_ANCHOR) == 1 and prod.count('site-nav-home-link') == 0
prod = prod.replace(
    NAV_ANCHOR,
    '<div class="site-nav-links">\n    ' + NAV_LINK + '\n    <a href="#app" id="site-nav-app"',
)

ps, pe = landing_i18n(prod)
obj = json.loads(prod[ps:pe])
assert set(obj.keys()) == set(beta_i18n.keys())
for lang in obj:
    for key in ('hero_viz_private', 'nav_home'):
        assert key not in obj[lang]
        obj[lang][key] = beta_i18n[lang][key]
prod = prod[:ps] + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + prod[pe:]

assert prod.count('"softwareVersion": "2.68.0"') == 1
prod = prod.replace('"softwareVersion": "2.68.0"', '"softwareVersion": "2.68.1"')
open('index.html', 'w', encoding='utf-8').write(prod)
print('index.html: hero viz + Home nav link + i18n keys shipped')

b = beta.replace('"softwareVersion": "2.68.0"', '"softwareVersion": "2.68.1"')
assert b != beta
open('beta/index.html', 'w', encoding='utf-8').write(b)
print('beta/index.html: softwareVersion -> 2.68.1')

sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v110';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v110';", "const CACHE_VERSION = 'jwsync-v111';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js: CACHE_VERSION -> v111')
print('done')

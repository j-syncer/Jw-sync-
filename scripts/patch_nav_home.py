#!/usr/bin/env python3
"""v2.68.0 — "Home" nav link (beta).

UX gap: once inside the Merging App (or any tool), the only way back to the
homepage/tool chooser was knowing to click the "JW Sync" logo — so users
couldn't find their way back to the Library Doctor and the other tools.

Adds a visible "Home" link as the first item in the site nav (beta only),
localised in all 12 languages, with active-state wiring in both copies of
js/enhancements.js (lockstep). Bumps softwareVersion + SW CACHE_VERSION.
"""
import json, re

# ─────────────────────────────────────────────────────────────────────────────
# 1. beta/index.html — nav link
# ─────────────────────────────────────────────────────────────────────────────
path = 'beta/index.html'
c = open(path, encoding='utf-8').read()

NAV_ANCHOR = '<div class="site-nav-links">\n    <a href="#app" id="site-nav-app"'
assert c.count(NAV_ANCHOR) == 1, 'nav anchor not unique'
c = c.replace(
    NAV_ANCHOR,
    '<div class="site-nav-links">\n    '
    '<a href="#home" id="site-nav-home-link" class="site-nav-link" data-i18n="nav_home">Home</a>\n    '
    '<a href="#app" id="site-nav-app"',
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. beta/index.html — i18n key nav_home in all 12 languages
# ─────────────────────────────────────────────────────────────────────────────
TR = {
    'en': 'Home', 'es': 'Inicio', 'pt': 'Início', 'fr': 'Accueil',
    'de': 'Startseite', 'it': 'Home', 'ru': 'Главная', 'ja': 'ホーム',
    'ko': '홈', 'tl': 'Home', 'sv': 'Hem', 'ceb': 'Home',
}
m = re.search(r'__JW_LANDING_I18N *= *', c)
ts = m.end(); d = 0; e = None
for i in range(ts, len(c)):
    if c[i] == '{':
        d += 1
    elif c[i] == '}':
        d -= 1
        if d == 0:
            e = i + 1
            break
obj = json.loads(c[ts:e])
assert set(obj.keys()) == set(TR.keys()), 'language set mismatch'
for lang, text in TR.items():
    obj[lang]['nav_home'] = text
c = c[:ts] + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + c[e:]

# ─────────────────────────────────────────────────────────────────────────────
# 3. Version bumps
# ─────────────────────────────────────────────────────────────────────────────
assert c.count('"softwareVersion": "2.67.0"') == 1
c = c.replace('"softwareVersion": "2.67.0"', '"softwareVersion": "2.68.0"')
open(path, 'w', encoding='utf-8').write(c)
print('beta/index.html patched')

p = open('index.html', encoding='utf-8').read()
assert p.count('"softwareVersion": "2.67.0"') == 1
p = p.replace('"softwareVersion": "2.67.0"', '"softwareVersion": "2.68.0"')
open('index.html', 'w', encoding='utf-8').write(p)
print('index.html softwareVersion bumped')

sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v109';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v109';", "const CACHE_VERSION = 'jwsync-v110';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js CACHE_VERSION -> v110')

# ─────────────────────────────────────────────────────────────────────────────
# 4. js/enhancements.js (both copies, lockstep) — active state for the new link
#    Null-guarded, so production (which has no #site-nav-home-link yet) is safe.
# ─────────────────────────────────────────────────────────────────────────────
OLD_DECL = "    var navHome = document.getElementById('site-nav-home');"
NEW_DECL = OLD_DECL + "\n    var navHomeLink = document.getElementById('site-nav-home-link');"
OLD_TOGGLE = "      if (navHome) navHome.classList.toggle('active', isLanding);"
NEW_TOGGLE = OLD_TOGGLE + "\n      if (navHomeLink) navHomeLink.classList.toggle('active', isLanding);"
for jp in ['js/enhancements.js', 'beta/js/enhancements.js']:
    j = open(jp, encoding='utf-8').read()
    assert j.count(OLD_DECL) == 1 and j.count(OLD_TOGGLE) == 1, jp
    j = j.replace(OLD_DECL, NEW_DECL).replace(OLD_TOGGLE, NEW_TOGGLE)
    open(jp, 'w', encoding='utf-8').write(j)
    print(jp, 'patched')
print('done')

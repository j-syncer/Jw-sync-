#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Indonesian (`id`) into the site's language plumbing.

    id   wtlocale IN   serves lang="id"

Probed against the live finder, and this one is a textbook case of why that
step is not optional:

    ID   -> lang="en"    the language's own ISO code, serving English
    I    -> lang="it"    Italian
    INS  -> lang="ins"   Indonesian *Sign* Language, not Indonesian

Only `IN` is right, and it is the code you would reach for last. Note that
`ID` fails the way `PL`, `UK` and `HB` did — silently, with a page that loads
fine and is simply in the wrong language.

Indonesian is LTR and Latin-script, so no direction machinery is involved.
Covers the same four enumeration points as the other plumbing scripts, and is
idempotent.
"""
import io, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE, LABEL, WTLOCALE = "id", "🇮🇩 Bahasa Indonesia", "IN"


def patch(path, pairs):
    p = os.path.join(REPO, path)
    c = io.open(p, encoding="utf-8").read()
    orig = c
    for old, new in pairs:
        if new in c:
            continue
        n = c.count(old)
        if n != 1:
            sys.exit("ABORT %s: anchor %r found %d times" % (path, old[:60], n))
        c = c.replace(old, new, 1)
    if c != orig:
        io.open(p, "w", encoding="utf-8").write(c)
        print("patched", path)
    else:
        print("unchanged", path)


# Anchor on `var V=` — the bare `V=[…]` form also appears in the jw-dir-init
# snippet that add_rtl_wiring.py derives from this list.
LANG_OLD = ("var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb',"
            "'ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant','vi','hu','hi']")
LANG_NEW = LANG_OLD[:-1] + ",'%s']" % CODE
PICK_OLD = '<option value="hi">🇮🇳 हिन्दी</option>'
PICK_NEW = PICK_OLD + '\n      <option value="%s">%s</option>' % (CODE, LABEL)
WT_OLD = "hi: 'HI' }"
WT_NEW = "hi: 'HI', %s: '%s' }" % (CODE, WTLOCALE)
NAV_OLD = '["hi","\\u{1F1EE}\\u{1F1F3} \\u0939\\u093F\\u0928\\u094D\\u0926\\u0940"]]'
NAV_NEW = (NAV_OLD[:-1] +
           ',["id","\\u{1F1EE}\\u{1F1E9} Bahasa Indonesia"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_OLD, LANG_NEW), (PICK_OLD, PICK_NEW)])
for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WT_OLD, WT_NEW)])
for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

# (5) The jw-dir-init <head> bootstrap carries its own copy of the allow-list on
# all seven pages, and 01_static.js asserts the two agree. Earlier plumbing
# scripts left this to a re-run of add_rtl_wiring.py, but that script is older
# than the shipped bootstrap and re-running it reverts a first-paint fix. So do
# it here instead: same substitution, no stale script involved.
BOOT_OLD = LANG_OLD[len("var "):]
BOOT_NEW = LANG_NEW[len("var "):]
for f in ("index.html", "beta/index.html", "highlights.html",
          "beta/highlights.html", "share.html", "beta/share.html", "forum.html"):
    patch(f, [(BOOT_OLD, BOOT_NEW)])
print("\nDone — do NOT re-run add_rtl_wiring.py; step (5) above replaces it.")

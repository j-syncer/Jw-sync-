#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Hindi (`hi`) into the site's language plumbing.

    hi   wtlocale HI   serves lang="hi"

Probed against the live finder. The near-misses are the usual quiet kind:
`H1` serves **Hungarian**, `IN` serves **Indonesian**, and `HIN` falls back to
English. Only `HI` is right.

Hindi is LTR and Devanagari needs no direction machinery. Covers the same four
enumeration points as the other plumbing scripts. Idempotent.
"""
import io, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE, LABEL, WTLOCALE = "hi", "🇮🇳 हिन्दी", "HI"


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
            "'ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant','vi','hu']")
LANG_NEW = LANG_OLD[:-1] + ",'%s']" % CODE
PICK_OLD = '<option value="hu">🇭🇺 Magyar</option>'
PICK_NEW = PICK_OLD + '\n      <option value="%s">%s</option>' % (CODE, LABEL)
WT_OLD = "hu: 'H' }"
WT_NEW = "hu: 'H', %s: '%s' }" % (CODE, WTLOCALE)
NAV_OLD = '["hu","\\u{1F1ED}\\u{1F1FA} Magyar"]]'
NAV_NEW = ('["hu","\\u{1F1ED}\\u{1F1FA} Magyar"],'
           '["hi","\\u{1F1EE}\\u{1F1F3} \\u0939\\u093F\\u0928\\u094D\\u0926\\u0940"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_OLD, LANG_NEW), (PICK_OLD, PICK_NEW)])
for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WT_OLD, WT_NEW)])
for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])
print("\nNow re-run scripts/add_rtl_wiring.py.")

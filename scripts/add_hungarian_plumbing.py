#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Hungarian (`hu`) into the site's language plumbing.

    hu   wtlocale H   serves lang="hu"

Probed against the live finder, as the runbook requires. `HU` — the language's
own ISO code, and the obvious guess — serves English, and `M` serves Romanian.
`HG`, `MA` and `HUN` all fall back to English too. Only `H` is right.

Hungarian is LTR and its code is a plain two-letter identifier, so no direction
machinery and no key quoting are involved.

Covers the same four enumeration points as the other plumbing scripts.
Idempotent: every replacement checks for the marker first.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CODE = "hu"
LABEL = "🇭🇺 Magyar"
WTLOCALE = "H"


def patch(path, pairs, required=True):
    p = os.path.join(REPO, path)
    c = io.open(p, encoding="utf-8").read()
    orig = c
    for old, new in pairs:
        if new in c:
            continue  # already applied
        n = c.count(old)
        if n != 1:
            if required:
                sys.exit("ABORT %s: anchor %r found %d times" % (path, old[:60], n))
            continue
        c = c.replace(old, new, 1)
    if c != orig:
        io.open(p, "w", encoding="utf-8").write(c)
        print("patched", path)
    else:
        print("unchanged", path)


# Anchor on `var V=` — the bare `V=[…]` form also appears in the jw-dir-init
# snippet, which add_rtl_wiring.py derives from this very list, so matching the
# short form would hit both and the count check would (correctly) abort.
LANG_LIST_OLD = ("var V=['en','es','pt','fr','de','it','ru','ja','ko','tl',"
                 "'sv','ceb','ar','he','uk','pl','zh-Hans','zh-Hant',"
                 "'yue-Hant','vi']")
LANG_LIST_NEW = LANG_LIST_OLD[:-1] + ",'%s']" % CODE

PICKER_OLD = '<option value="vi">🇻🇳 Tiếng Việt</option>'
PICKER_NEW = (PICKER_OLD + '\n      <option value="%s">%s</option>' % (CODE, LABEL))

WTLOCALE_OLD = "vi: 'VT' }"
WTLOCALE_NEW = "vi: 'VT', %s: '%s' }" % (CODE, WTLOCALE)

NAV_OLD = '["vi","\\u{1F1FB}\\u{1F1F3} Ti\\u1EBFng Vi\\u1EC7t"]]'
NAV_NEW = ('["vi","\\u{1F1FB}\\u{1F1F3} Ti\\u1EBFng Vi\\u1EC7t"],'
           '["hu","\\u{1F1ED}\\u{1F1FA} Magyar"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

print("\nNow re-run scripts/add_rtl_wiring.py so the dir-bootstrap allow-list "
      "picks up the new code from index.html.")

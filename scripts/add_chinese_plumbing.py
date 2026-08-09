#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire the three Chinese variants into the site's language plumbing.

Chinese is the first language on the site that is not a 2-3 letter lowercase
code, and the first that is not a single variant. jw.org itself splits it three
ways, and we follow that split rather than inventing our own:

    zh-Hans   wtlocale CHS   serves lang="cmn-hans"   Mandarin, Simplified
    zh-Hant   wtlocale CH    serves lang="cmn-hant"   Mandarin, Traditional
    yue-Hant  wtlocale CHC   serves lang="yue-hant"   Cantonese, Traditional

Every one of those wtlocale codes was checked against the live finder, not
inferred — `CHT`, `CAN` and `ZH` all look plausible and all serve English.

The BCP-47 tags are used everywhere, including as dictionary keys, which is
why i18n_tool.py quotes non-identifier keys and the ?lang= regex accepts
[A-Za-z-]{2,12}. See the commit that introduced those.

Covers the same four enumeration points as the other plumbing scripts. All
three variants are LTR, so no direction machinery is involved.

Idempotent: every replacement checks for the marker first.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VARIANTS = [
    ("zh-Hans", "🇨🇳 简体中文", "CHS"),
    ("zh-Hant", "🇹🇼 繁體中文", "CH"),
    ("yue-Hant", "🇭🇰 粵語", "CHC"),
]


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


# Anchor on `var V=` — the bare `V=[…]` form now also appears in the jw-dir-init
# snippet, which add_rtl_wiring.py copies out of this very list. Matching the
# short form would hit both and the count check would (correctly) abort.
LANG_LIST_OLD = ("var V=['en','es','pt','fr','de','it','ru','ja','ko','tl',"
                 "'sv','ceb','ar','he','uk','pl']")
LANG_LIST_NEW = LANG_LIST_OLD[:-1] + ",'zh-Hans','zh-Hant','yue-Hant']"

PICKER_OLD = '<option value="pl">🇵🇱 Polski</option>'
PICKER_NEW = ('<option value="pl">🇵🇱 Polski</option>\n'
              + "\n".join('      <option value="%s">%s</option>' % (c, label)
                          for c, label, _ in VARIANTS))

WTLOCALE_OLD = "uk: 'K', pl: 'P' }"
WTLOCALE_NEW = ("uk: 'K', pl: 'P', "
                + ", ".join("'%s': '%s'" % (c, w) for c, _, w in VARIANTS) + " }")

NAV_OLD = '["pl","\\u{1F1F5}\\u{1F1F1} Polski"]]'
NAV_NEW = ('["pl","\\u{1F1F5}\\u{1F1F1} Polski"],'
           '["zh-Hans","\\u{1F1E8}\\u{1F1F3} \\u7B80\\u4F53\\u4E2D\\u6587"],'
           '["zh-Hant","\\u{1F1F9}\\u{1F1FC} \\u7E41\\u9AD4\\u4E2D\\u6587"],'
           '["yue-Hant","\\u{1F1ED}\\u{1F1F0} \\u7CB5\\u8A9E"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

print("\nNow re-run scripts/add_rtl_wiring.py so the dir-bootstrap allow-list "
      "picks up the new codes from index.html.")

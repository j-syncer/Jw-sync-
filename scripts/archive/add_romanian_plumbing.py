#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Romanian (`ro`) into the site's language plumbing.

    ro   wtlocale M   serves lang="ro"

Probed against the live finder, and the near-misses are the usual quiet kind —
every one of them returns a working page in the wrong language:

    RO   -> lang="en"    the language's own ISO code, serving English
    ROM  -> lang="en"    English again
    R    -> lang="hyw"   Western Armenian
    RU   -> lang="run"   Rundi — not Russian, which is `U`

`M` is the only correct value and there is nothing about it you could guess.

Romanian is LTR and Latin-script (with ă â î ș ț), so no direction machinery is
involved. Covers the same five enumeration points as add_indonesian_plumbing.py,
including the jw-dir-init bootstrap. Idempotent.
"""
import io, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE, LABEL, WTLOCALE = "ro", "🇷🇴 Română", "M"


def patch(path, pairs):
    p = os.path.join(REPO, path)
    c = io.open(p, encoding="utf-8").read()
    orig = c
    for old, new in pairs:
        # Skip on the absence of `old`, not the presence of `new`. The older
        # scripts tested `new in c`, which silently no-ops when `new` happens to
        # be a substring of something already patched — exactly what happens to
        # the bootstrap list once `var V=[…,'ro']` exists on the same page.
        if old not in c:
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
# snippet, which step (5) patches separately.
LANG_OLD = ("var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb',"
            "'ar','he','uk','pl','zh-Hans','zh-Hant','yue-Hant','vi','hu','hi','id']")
LANG_NEW = LANG_OLD[:-1] + ",'%s']" % CODE
PICK_OLD = '<option value="id">🇮🇩 Bahasa Indonesia</option>'
PICK_NEW = PICK_OLD + '\n      <option value="%s">%s</option>' % (CODE, LABEL)
WT_OLD = "id: 'IN' }"
WT_NEW = "id: 'IN', %s: '%s' }" % (CODE, WTLOCALE)
NAV_OLD = '["id","\\u{1F1EE}\\u{1F1E9} Bahasa Indonesia"]]'
NAV_NEW = NAV_OLD[:-1] + ',["ro","\\u{1F1F7}\\u{1F1F4} Rom\\u00e2n\\u0103"]]'

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_OLD, LANG_NEW), (PICK_OLD, PICK_NEW)])
for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WT_OLD, WT_NEW)])
for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

# (5) The jw-dir-init <head> bootstrap carries its own copy of the allow-list on
# all seven pages, and 01_static.js asserts the two agree. Do it here rather
# than by re-running add_rtl_wiring.py, which predates the shipped bootstrap.
# Anchor the bootstrap copy on its leading newline: on index.html the bare
# `V=[…]` form is also a substring of the `var V=[…]` list patched above.
BOOT_OLD = "\n" + LANG_OLD[len("var "):]
BOOT_NEW = "\n" + LANG_NEW[len("var "):]
for f in ("index.html", "beta/index.html", "highlights.html",
          "beta/highlights.html", "share.html", "beta/share.html", "forum.html"):
    patch(f, [(BOOT_OLD, BOOT_NEW)])
print("\nDone — do NOT re-run add_rtl_wiring.py; step (5) above replaces it.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Hebrew ('he') into the site's language plumbing.

The sibling of add_arabic_plumbing.py, covering the three places that
enumerate languages outside the string dictionaries: the ?lang= allow-list,
the nav picker, and the jw.org wtlocale map.

Hebrew needs no new direction code — add_rtl_wiring.py's `R` set was written
as a set precisely so a second RTL language would be free, and already lists
`he`. Only the `V` allow-list inside that snippet has to grow, which is why
this script re-runs the wiring rather than duplicating the bootstrap.

Idempotent: every replacement checks for the marker first.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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


LANG_LIST_OLD = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar']"
LANG_LIST_NEW = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he']"

PICKER_OLD = '<option value="ar">🇸🇦 العربية</option>'
PICKER_NEW = ('<option value="ar">🇸🇦 العربية</option>\n'
              '      <option value="he">🇮🇱 עברית</option>')

# jw.org's own code for Hebrew. Without it the Bible-chapter links that
# reading.js builds would silently open in English for Hebrew readers.
WTLOCALE_OLD = "ceb: 'CV', ar: 'A' }"
WTLOCALE_NEW = "ceb: 'CV', ar: 'A', he: 'HB' }"

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

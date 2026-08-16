#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Arabic ('ar') into the site's language plumbing.

Covers the places that enumerate languages outside the string dictionaries:
the ?lang= allow-list, the nav picker, and the jw.org wtlocale map. Also
installs the direction handling that Arabic needs (see rtl_support.py for the
stylesheet side).

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


LANG_LIST_OLD = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb']"
LANG_LIST_NEW = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar']"

PICKER_OLD = '<option value="ceb">🇵🇭 Cebuano</option>'
PICKER_NEW = ('<option value="ceb">🇵🇭 Cebuano</option>\n'
              '      <option value="ar">🇸🇦 العربية</option>')

WTLOCALE_OLD = "sv: 'Z', ceb: 'CV' }"
WTLOCALE_NEW = "sv: 'Z', ceb: 'CV', ar: 'A' }"

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

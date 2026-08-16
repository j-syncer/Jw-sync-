#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Ukrainian ('uk') into the site's language plumbing.

The sibling of add_arabic_plumbing.py / add_hebrew_plumbing.py, covering the
places that enumerate languages outside the string dictionaries.

Four, not three: the Arabic script predated the in-app picker being extracted
into `NAV_LANGS` in js/app.js, so it only knew about the <select> in
index.html. Hebrew had to be added to NAV_LANGS separately after 01_static.js
caught it; this script covers both pickers.

Ukrainian is left-to-right, so none of the direction machinery is involved.

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


LANG_LIST_OLD = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he']"
LANG_LIST_NEW = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk']"

PICKER_OLD = '<option value="he">🇮🇱 עברית</option>'
PICKER_NEW = ('<option value="he">🇮🇱 עברית</option>\n'
              '      <option value="uk">🇺🇦 Українська</option>')

# jw.org's own code for Ukrainian, checked against the live finder rather than
# assumed: wtlocale=K serves lang="uk", while the plausible-looking "UK" falls
# back to English. A wrong code here fails silently — every Bible-chapter link
# reading.js builds would just open in the wrong language.
WTLOCALE_OLD = "ar: 'A', he: 'HB' }"
WTLOCALE_NEW = "ar: 'A', he: 'HB', uk: 'K' }"

# The in-app picker (js/app.js), which is a separate list from the <select>.
NAV_OLD = '["he","\\u{1F1EE}\\u{1F1F1} \\u05E2\\u05D1\\u05E8\\u05D9\\u05EA"]]'
NAV_NEW = ('["he","\\u{1F1EE}\\u{1F1F1} \\u05E2\\u05D1\\u05E8\\u05D9\\u05EA"],'
           '["uk","\\u{1F1FA}\\u{1F1E6} \\u0423\\u043A\\u0440\\u0430\\u0457\\u043D\\u0441\\u044C\\u043A\\u0430"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

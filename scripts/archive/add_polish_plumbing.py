#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire Polish ('pl') into the site's language plumbing.

Covers the four places that enumerate languages outside the string
dictionaries: the ?lang= allow-list, the <select> in index.html, the in-app
NAV_LANGS picker in js/app.js, and the jw.org wtlocale map.

Polish is left-to-right, so none of the direction machinery is involved.

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


LANG_LIST_OLD = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk']"
LANG_LIST_NEW = "var V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk','pl']"

PICKER_OLD = '<option value="uk">🇺🇦 Українська</option>'
PICKER_NEW = ('<option value="uk">🇺🇦 Українська</option>\n'
              '      <option value="pl">🇵🇱 Polski</option>')

# jw.org's own code for Polish, checked against the live finder: wtlocale=P
# serves lang="pl". Codes are verified rather than inferred here because an
# unrecognised one falls through to English silently — see the note in
# tests/16_reading.js, and the 'HB' mistake that prompted it.
WTLOCALE_OLD = "he: 'Q', uk: 'K' }"
WTLOCALE_NEW = "he: 'Q', uk: 'K', pl: 'P' }"

# The in-app picker (js/app.js), a separate list from the <select>.
NAV_OLD = ('["uk","\\u{1F1FA}\\u{1F1E6} \\u0423\\u043A\\u0440\\u0430\\u0457\\u043D\\u0441\\u044C\\u043A\\u0430"]]')
NAV_NEW = ('["uk","\\u{1F1FA}\\u{1F1E6} \\u0423\\u043A\\u0440\\u0430\\u0457\\u043D\\u0441\\u044C\\u043A\\u0430"],'
           '["pl","\\u{1F1F5}\\u{1F1F1} Polski"]]')

for f in ("index.html", "beta/index.html"):
    patch(f, [(LANG_LIST_OLD, LANG_LIST_NEW), (PICKER_OLD, PICKER_NEW)])

for f in ("js/reading.js", "beta/js/reading.js"):
    patch(f, [(WTLOCALE_OLD, WTLOCALE_NEW)])

for f in ("js/app.js", "beta/js/app.js"):
    patch(f, [(NAV_OLD, NAV_NEW)])

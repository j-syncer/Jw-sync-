#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural check for one language's guide translations.

    python3 scripts/check_guide_lang.py pt

Catches the four ways a translation file goes wrong without anyone noticing:
a missing guide, a field with the wrong number of entries (which would drop a
step or an FAQ answer from the page), an entry that is not a 2-tuple, and a
string left in English. Exits non-zero on any problem.
"""
import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_guides import GUIDES  # noqa: E402
from guides_i18n import GUIDE_TEXT, CHROME  # noqa: E402

CHROME_KEYS = set(CHROME["en"])


def flat(d):
    """(label, string) pairs in a fixed order, so en and xx line up."""
    out = [(f, d.get(f, "")) for f in ("title", "h1", "description")]
    for f in ("intro", "steps", "sections", "faq"):
        for i, it in enumerate(d.get(f, [])):
            if isinstance(it, (tuple, list)):
                out += [("%s[%d].0" % (f, i), it[0]), ("%s[%d].1" % (f, i), it[1])]
            else:
                out.append(("%s[%d]" % (f, i), it))
    return out


def main():
    lang = sys.argv[1]
    if lang not in GUIDE_TEXT:
        print("FAIL %s is not registered in guides_i18n.GUIDE_TEXT" % lang)
        return 1
    txt = GUIDE_TEXT[lang]
    en = {g["slug"]: g for g in GUIDES}
    bad = 0

    missing_chrome = CHROME_KEYS - set(CHROME.get(lang, {}))
    if missing_chrome:
        print("FAIL CHROME[%s] missing: %s" % (lang, ", ".join(sorted(missing_chrome))))
        bad += 1
    if lang in CHROME:
        for grp in CHROME["en"]["groups"]:
            if grp not in CHROME[lang].get("groups", {}):
                print("FAIL CHROME[%s].groups missing %r" % (lang, grp))
                bad += 1

    for slug in en:
        if slug not in txt:
            print("FAIL missing guide: %s" % slug)
            bad += 1
    # A slug appearing as a *field* of another guide is how an entry written in
    # the wrong shape lands: GUIDES_XX["slug"] = {...} modules take an appended
    # dict-literal entry into the previous guide's dict. Valid Python, no error,
    # and that language just falls back to English for the guide that never
    # arrived — so name the cause here, where the language is being checked.
    for slug, g in txt.items():
        if not isinstance(g, dict):
            continue
        nested = [k for k in g if k in en]
        if nested:
            print("FAIL %s contains another guide as a field: %s — the entry was "
                  "written in the wrong shape for this module" % (slug, ", ".join(nested)))
            bad += 1

    for slug in txt:
        if slug not in en:
            print("FAIL unknown slug: %s" % slug)
            bad += 1

    for slug, t in txt.items():
        if slug not in en:
            continue
        e = en[slug]
        for f in ("title", "h1", "description"):
            if not t.get(f):
                print("FAIL %s: empty %s" % (slug, f))
                bad += 1
        for f in ("intro", "steps", "sections", "faq"):
            if len(t.get(f, [])) != len(e.get(f, [])):
                print("FAIL %s: %s has %d entries, English has %d"
                      % (slug, f, len(t.get(f, [])), len(e.get(f, []))))
                bad += 1
        for f in ("steps", "sections", "faq"):
            for i, it in enumerate(t.get(f, [])):
                if not (isinstance(it, (tuple, list)) and len(it) == 2):
                    print("FAIL %s: %s[%d] is not a 2-tuple" % (slug, f, i))
                    bad += 1
        # A string byte-identical to the English one is almost always a line
        # that was pasted and never translated. Short strings can legitimately
        # match (product names, "JW Sync"), so only flag substantial ones.
        for (k, ev), (_, tv) in zip(flat(e), flat(t)):
            if ev.strip() and ev.strip() == tv.strip() and len(ev.strip()) > 25:
                print("FAIL %s %s: still English -- %s" % (slug, k, ev[:60]))
                bad += 1

    print("%s: %d/%d guides, %d problem(s)" % (lang, len(txt), len(en), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

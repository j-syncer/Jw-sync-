#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared machinery for bringing a language's guide copy up to the depth of the
deepened English records (see deepen_guides_en*.py).

The English passes added entries in two positions, and the difference matters:

  * sections / faq were appended, so the outstanding entries are the trailing
    ones — english[field][len(translated):] — and translations append too.
  * intro paragraphs were *prepended* (deepen_guides_en3.add_intro inserts at
    the top, because the new paragraph opens the page). The outstanding entries
    are therefore the *leading* ones, and translations must prepend.

Getting that backwards silently re-translates a paragraph the language already
has while dropping the new one, so the two cases are kept explicit below.

`pending()` returns the outstanding entries per field, so a per-language pass
never has to track which of the four English passes contributed what.
`apply_lang()` writes them back into scripts/guides_<lang>.py in the same
literal style the file already uses.
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))

FIELDS = ("intro", "sections", "faq")


def english():
    import build_guides as B
    return {g["slug"]: g for g in B.GUIDES}


def translated(lang):
    from guides_i18n import GUIDE_TEXT
    return GUIDE_TEXT[lang]


def pending(lang, slugs):
    """{slug: {field: [entries still to translate]}} for one language."""
    en, tr = english(), translated(lang)
    out = {}
    for s in slugs:
        gaps = {}
        for f in FIELDS:
            have = len(tr.get(s, {}).get(f, []))
            want = en[s][f]
            n = len(want) - have
            if n > 0:
                # intro grew at the front, sections/faq at the back
                gaps[f] = want[:n] if f == "intro" else want[have:]
        if gaps:
            out[s] = gaps
    return out


def src_path(lang):
    return os.path.join(REPO, "scripts", "guides_%s.py" % lang)


def _lit(s):
    if '"' in s:
        sys.exit("!! straight double quote in copy: %.60s" % s)
    return '"%s"' % s.replace("\\", "\\\\")


def _record_span(src, slug):
    m = re.search(r'\n "%s": \{\n' % re.escape(slug), src)
    if not m:
        sys.exit("!! record not found: %s" % slug)
    end = src.find("\n },\n", m.start() + 1)
    if end < 0:
        sys.exit("!! record end not found: %s" % slug)
    return m.start(), end


def _append(src, slug, field, entries):
    start, end = _record_span(src, slug)
    rec = src[start:end]
    key = '\n  "%s": [\n' % field
    at = rec.find(key)
    if at < 0:
        sys.exit("!! %s: no %s field" % (slug, field))
    close = rec.find("\n  ],", at)
    if close < 0:
        sys.exit("!! %s: unterminated %s" % (slug, field))
    if field == "intro":
        # prepended, matching how the English pass inserted it
        block = "".join("   %s,\n" % _lit(e) for e in entries)
        rec = rec[:at + len(key)] + block + rec[at + len(key):]
    else:
        block = "".join("   (%s,\n    %s),\n" % (_lit(a), _lit(b)) for a, b in entries)
        rec = rec[:close + 1] + block + rec[close + 1:]
    return src[:start] + rec + src[end:]


def apply_lang(lang, data, sentinel):
    """data: {slug: {field: [entries]}} — already translated into `lang`."""
    p = src_path(lang)
    src = io.open(p, encoding="utf-8").read()
    if sentinel in src:
        sys.exit("%s already deepened — nothing to do" % lang)
    for slug, fields in data.items():
        for field in FIELDS:
            if fields.get(field):
                src = _append(src, slug, field, fields[field])
    io.open(p, "w", encoding="utf-8").write(src)
    print("%s: deepened %d guides" % (lang, len(data)))


def report(lang, slugs):
    """Print what is still outstanding, as a translation worksheet."""
    for slug, gaps in pending(lang, slugs).items():
        print("== %s ==" % slug)
        for f, entries in gaps.items():
            print("  %s: %d" % (f, len(entries)))


if __name__ == "__main__":
    from deepen_guides_en import ADD
    report(sys.argv[1] if len(sys.argv) > 1 else "es", list(ADD))

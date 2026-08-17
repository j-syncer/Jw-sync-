#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
splice_md_write_guide.py — add the Markdown-authoring guide to every language.

The sibling of splice_md_import_guide.py, for the 39th guide. Reads
scripts/i18n_data/guide_md_write/<lang>.json and splices the slug into
scripts/guides_<lang>.py, next to the other guides for that language.

JSON rather than hand-edited Python, per the runbook: a batch is valid JSON or
it is not, a language spliced twice is a no-op rather than a silent winner, and
it reports how many of the 24 languages are present with the missing ones
named, so progress is never guessed at.

Beyond the checks its sibling makes, this one asserts the fenced sample files
survive translation. The guide's whole subject is a file the reader types, and
build_guides.section_body() renders ``` blocks as <pre>; a translation that
drops a fence turns the sample back into run-on prose, which no other check
would notice.

Usage:
  python3 scripts/archive/splice_md_write_guide.py           # splice
  python3 scripts/archive/splice_md_write_guide.py --check   # report only
"""
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "scripts", "i18n_data", "guide_md_write")
SLUG = "write-markdown-notes-for-jw-library"
TOTAL = 39                      # guides per language once this one lands

LANGS = ["es", "pt", "fr", "de", "it", "ru", "ja", "ko", "tl", "sv", "ceb",
         "ar", "he", "uk", "pl", "zh-Hans", "zh-Hant", "yue-Hant", "vi", "hu",
         "hi", "id", "ro", "nl"]

FIELDS = ("title", "h1", "description", "intro", "steps", "sections", "faq")

# Lines inside a fenced sample that are syntax rather than prose: the parser
# matches these field names literally, so a translated key would produce a
# sample that does not work. Matthew 26:39 is in the same position — book names
# are recognised in English only, which the copy itself says.
LITERAL = ("publication:", "title:", "date:", "tags:", "Matthew 26:39")


def module_for(lang):
    return os.path.join(REPO, "scripts",
                        "guides_%s.py" % lang.replace("-", "_").lower())


def py_str(s):
    return json.dumps(s, ensure_ascii=False)


def var_for(lang):
    return "GUIDES_" + lang.replace("-", "_").upper()


def render(entry, lang, style):
    """Two module shapes ship, and mixing them up is silent corruption.

    Some modules build their dict with GUIDES_XX["slug"] = {...} assignments,
    the rest are one dict literal. Appending a `"slug": {...},` entry to an
    assignment-style module drops it *inside the last guide's dict* — valid
    Python, no error. So the shape is detected, never assumed, and the result
    is verified by importing the module afterwards.
    """
    head = (' "%s": {' % SLUG) if style == "literal" \
        else ('%s["%s"] = {' % (var_for(lang), SLUG))
    out = [head]
    for f in ("title", "h1", "description"):
        out.append('  "%s": %s,' % (f, py_str(entry[f])))
    out.append('  "intro": [')
    for p in entry["intro"]:
        out.append("   %s," % py_str(p))
    out.append("  ],")
    for field in ("steps", "sections", "faq"):
        out.append('  "%s": [' % field)
        for pair in entry[field]:
            out.append("   (%s," % py_str(pair[0]))
            out.append("    %s)," % py_str(pair[1]))
        out.append("  ],")
    out.append(" }," if style == "literal" else "}")
    return "\n".join(out) + "\n"


def fences(text):
    return text.count("```")


def samples(text):
    """The text inside the ``` fences, concatenated.

    The literal check has to run here and not over the whole body: the prose
    around a sample *should* localise the book name — "attached to Mateo
    26:39" is right in Spanish — while the sample itself must keep the English
    name the parser actually recognises.
    """
    parts = text.split("```")
    return "\n".join(parts[1::2])


def check(entry, lang, en):
    for f in FIELDS:
        if f not in entry:
            sys.exit("ABORT %s: missing field %r" % (lang, f))
    for f in ("steps", "sections", "faq"):
        if len(entry[f]) != len(en[f]):
            sys.exit("ABORT %s: %s has %d entries, English has %d"
                     % (lang, f, len(entry[f]), len(en[f])))
        for pair in entry[f]:
            if len(pair) != 2:
                sys.exit("ABORT %s: %s entry is not a [heading, body] pair" % (lang, f))
    if len(entry["intro"]) != len(en["intro"]):
        sys.exit("ABORT %s: intro has %d paragraphs, English has %d"
                 % (lang, len(entry["intro"]), len(en["intro"])))
    # Copy left in English is the failure that looks like success.
    if entry["title"] == en["title"] or entry["description"] == en["description"]:
        sys.exit("ABORT %s: title/description still English" % lang)

    # The sample files are the point of this guide. Every fence English opens,
    # the translation must open too, or the example renders as a paragraph.
    for i, ((_, en_body), (_, body)) in enumerate(zip(en["sections"], entry["sections"])):
        if fences(en_body) != fences(body):
            sys.exit("ABORT %s: sections[%d] has %d ``` markers, English has %d"
                     % (lang, i, fences(body), fences(en_body)))
        if fences(body) % 2:
            sys.exit("ABORT %s: sections[%d] has an unclosed ``` fence" % (lang, i))
        en_sample, sample = samples(en_body), samples(body)
        for token in LITERAL:
            if en_sample.count(token) != sample.count(token):
                sys.exit("ABORT %s: the sample in sections[%d] writes %r %d "
                         "time(s), English %d — the parser matches it literally"
                         % (lang, i, token, sample.count(token),
                            en_sample.count(token)))


def english():
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import build_guides
    for g in build_guides.GUIDES:
        if g["slug"] == SLUG:
            return g
    sys.exit("ABORT: the English guide is not in build_guides.GUIDES")


def verify(lang, mod):
    """Import the module and confirm the guide is really in the dict.

    An entry can be written into a file, parse fine and still not be a guide.
    Only the imported dict settles it.
    """
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    import importlib
    m = importlib.import_module(os.path.splitext(os.path.basename(mod))[0])
    importlib.reload(m)
    table = getattr(m, var_for(lang), None)
    if not isinstance(table, dict):
        sys.exit("ABORT %s: %s is not a dict after splicing" % (mod, var_for(lang)))
    if SLUG not in table:
        sys.exit("ABORT %s: the entry was written but is not in %s — wrong shape"
                 % (mod, var_for(lang)))
    if len(table) != TOTAL:
        sys.exit("ABORT %s: %d guides after splicing, expected %d"
                 % (mod, len(table), TOTAL))


def main():
    en = english()
    report_only = "--check" in sys.argv
    have, missing, done = [], [], []
    for lang in LANGS:
        p = os.path.join(DATA, "%s.json" % lang)
        if not os.path.exists(p):
            missing.append(lang)
            continue
        have.append(lang)
        entry = json.load(io.open(p, encoding="utf-8"))
        check(entry, lang, en)
        if report_only:
            continue
        mod = module_for(lang)
        c = io.open(mod, encoding="utf-8").read()
        if ('"%s"' % SLUG) in c:
            done.append(lang)
            continue
        var = var_for(lang)
        if re.search(r"^%s\[" % re.escape(var), c, re.M):
            c = c.rstrip("\n") + "\n\n" + render(entry, lang, "assign")
        elif re.search(r"^%s\s*=\s*\{" % re.escape(var), c, re.M):
            m = list(re.finditer(r"\n\}\s*$", c))
            if not m:
                sys.exit("ABORT %s: cannot find the end of the guide dict" % mod)
            at = m[-1].start()
            c = c[:at] + "\n" + render(entry, lang, "literal") + c[at:]
        else:
            sys.exit("ABORT %s: cannot tell how this module builds its dict" % mod)
        io.open(mod, "w", encoding="utf-8").write(c)
        verify(lang, mod)
        done.append(lang)

    print("%d/%d languages translated" % (len(have), len(LANGS)))
    if missing:
        print("  still missing: %s" % ", ".join(missing))
    if done and not report_only:
        print("  spliced: %s" % ", ".join(done))


if __name__ == "__main__":
    main()

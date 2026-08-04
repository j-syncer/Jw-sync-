#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
i18n_addkeys.py — add new keys to *every* language of one dictionary.

i18n_tool.py adds a whole language; this adds a whole key. Both are needed:
a new string has to land in all thirteen tables at once or the UI falls back
to English for twelve of them — which is exactly how the navbar ended up
hardcoded in the first place.

Input is a JSON file shaped {lang: {key: value, ...}, ...}. Keys already
present in a language are left alone, so re-running is safe.

    python3 scripts/i18n_addkeys.py js/app.js 0 scripts/i18n_data/navbar.json

`0` is the dictionary index as reported by `i18n_tool.py list`. Pass `--all`
instead of a file/index pair's file to apply the same payload to every file
that declares the dictionary (used for the index.html / beta twin).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_tool as t  # noqa: E402


def add(rel, index, payload):
    path = os.path.join(t.REPO, rel)
    text = io.open(path, encoding="utf-8").read()
    sites = t.dict_sites(text)
    if index >= len(sites):
        sys.exit("ABORT %s: no dictionary at index %d (found %d)"
                 % (rel, index, len(sites)))
    site = sites[index]

    # Work language-by-language, back to front, so earlier offsets stay valid.
    langs = sorted(payload)
    edits = []
    for lang in langs:
        src, _ = t.read_lang(text, site, lang)
        if src is None:
            print("  %s: no '%s' table — skipped" % (rel, lang))
            continue
        obj = t.js_to_obj(src)
        new = {k: v for k, v in payload[lang].items() if k not in obj}
        if not new:
            continue
        # Locate this language's object in the file to splice before its '}'.
        table_start, table_end = site["table"]
        table = text[table_start:table_end]
        hits = t.find_dicts(table, lang)
        _, os_, oe_ = hits[0]
        abs_close = table_start + oe_ - 1  # index of the closing brace
        style = t.detect_style(src)
        frag = "," + ",".join(
            "%s:%s" % (json.dumps(k, ensure_ascii=False) if style == "json" else k,
                       json.dumps(v, ensure_ascii=False))
            for k, v in new.items())
        edits.append((abs_close, frag, lang, len(new)))

    for pos, frag, lang, n in sorted(edits, key=lambda e: -e[0]):
        text = text[:pos] + frag + text[pos:]
        print("  %s[%s]: +%d key(s)" % (rel, lang, n))

    if edits:
        io.open(path, "w", encoding="utf-8").write(text)
    return len(edits)


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        return 1
    rel, index, payload_path = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    payload = json.load(io.open(payload_path, encoding="utf-8"))
    add(rel, index, payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())

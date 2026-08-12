#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revise the lead copy (description / intro) of specific guides, per language.

    python3 scripts/revise_guide_copy.py <revisions.json> [--check]

Why this exists: the English guide copy gets edited for *positioning* now and
then — the site is not a phone-recovery tool, and copy that implied it was had
to be rewritten — and when that happens the same paragraphs must change in 24
translated modules. build_lang_guides.py cannot do it: only six languages have
a META entry there, and re-rendering a module would reformat the whole file for
the sake of two paragraphs.

The modules are also not in one format. Two shapes are in the tree:

    GUIDES_ES = { "slug": { "description": "...", ... }, ... }   # 14 languages
    GUIDES_PT["slug"] = { "description": "..." "continued", ... } #  10 languages

and the second style wraps long strings with implicit concatenation across
lines. So this works on the parse tree rather than on the text: ast gives one
Constant node spanning a whole implicitly-concatenated string, and one List
node spanning a whole intro block, whatever the surrounding style. Only those
spans are rewritten, so the rest of every file is left byte-for-byte alone.

Indentation is copied from what each file already does — the inner indent comes
from the existing list elements, the closing bracket from the key's own line —
so a revised module keeps its house style instead of acquiring this script's.

Input JSON is {lang: {slug: {"description": str, "intro": [str, ...]}}}; both
fields are optional. A slug that is missing, or a field that cannot be located,
aborts the whole run before anything is written, because a positioning change
applied to some languages and not others is worse than one applied to none.
"""
import ast
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from build_lang_guides import q  # noqa: E402  the serialiser the modules use


def module_path(lang):
    return os.path.join(HERE, "guides_%s.py" % lang.replace("-", "_").lower())


def line_offsets(raw):
    """Byte offset of the start of each 1-indexed line.

    ast reports col_offset as a UTF-8 *byte* offset, not a character index, so
    every span here is computed and spliced in bytes. Doing it in characters
    silently lands mid-word on any line containing non-ASCII — which is every
    interesting line in twenty of these modules.
    """
    offs, total = [0, 0], 0
    for line in raw.splitlines(True):
        total += len(line)
        offs.append(total)
    return offs


def guide_dicts(tree):
    """slug -> ast.Dict node, across both module shapes in the tree."""
    found = {}
    for node in ast.walk(tree):
        # GUIDES_X = { "slug": {...}, ... }
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id.startswith("GUIDES_"):
                for k, v in zip(node.value.keys, node.value.values):
                    if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                        found[k.value] = v
            # GUIDES_X["slug"] = {...}
            elif (isinstance(tgt, ast.Subscript)
                  and isinstance(tgt.value, ast.Name)
                  and tgt.value.id.startswith("GUIDES_")
                  and isinstance(tgt.slice, ast.Constant)):
                found[tgt.slice.value] = node.value
    return found


def field_node(dict_node, name):
    for k, v in zip(dict_node.keys, dict_node.values):
        if isinstance(k, ast.Constant) and k.value == name:
            return k, v
    return None, None


def span(node, offs):
    return (offs[node.lineno] + node.col_offset,
            offs[node.end_lineno] + node.end_col_offset)


def indent_of_line(raw, offs, lineno):
    line = raw[offs[lineno]:offs[lineno + 1]]
    return len(line) - len(line.lstrip(b" "))


def render_list(items, inner, close):
    body = "".join("%s%s,\n" % (" " * inner, q(p)) for p in items)
    return "[\n%s%s]" % (body, " " * close)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    revisions = json.load(io.open(args[0], encoding="utf-8"))

    total = 0
    for lang, slugs in sorted(revisions.items()):
        path = module_path(lang)
        if not os.path.exists(path):
            sys.exit("ABORT: no module for %r" % lang)
        src = io.open(path, encoding="utf-8").read()
        raw = src.encode("utf-8")
        offs = line_offsets(raw)
        guides = guide_dicts(ast.parse(src))

        edits, touched = [], 0
        for slug, fields in slugs.items():
            gd = guides.get(slug)
            if gd is None:
                sys.exit("ABORT %s: %s is not in this module" % (lang, slug))

            if "description" in fields:
                _, v = field_node(gd, "description")
                if not isinstance(v, ast.Constant):
                    sys.exit("ABORT %s/%s: no description string" % (lang, slug))
                edits.append(span(v, offs)
                             + (q(fields["description"]).encode("utf-8"),))
                touched += 1

            if "intro" in fields:
                k, v = field_node(gd, "intro")
                if not isinstance(v, ast.List):
                    sys.exit("ABORT %s/%s: no intro list" % (lang, slug))
                # Copy this file's own layout rather than imposing one.
                inner = (v.elts[0].col_offset if v.elts
                         else indent_of_line(raw, offs, k.lineno) + 1)
                close = indent_of_line(raw, offs, k.lineno)
                edits.append(span(v, offs)
                             + (render_list(fields["intro"], inner, close).encode("utf-8"),))
                touched += 1

        # Apply back-to-front so earlier spans stay valid.
        for a, b, text in sorted(edits, reverse=True):
            raw = raw[:a] + text + raw[b:]
        src = raw.decode("utf-8")

        # A module that no longer parses, or lost a guide, must never be written.
        after = guide_dicts(ast.parse(src))
        if len(after) != len(guides):
            sys.exit("ABORT %s: guide count changed %d -> %d"
                     % (lang, len(guides), len(after)))

        if not check_only:
            io.open(path, "w", encoding="utf-8").write(src)
        print("  %-9s %d field(s) in %d guide(s)" % (lang, touched, len(slugs)))
        total += touched

    print("\n%s %d field(s) across %d language(s)"
          % ("would revise" if check_only else "revised", total, len(revisions)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
i18n_tool.py — locate every per-language dictionary in the site and
extract / inject a language.

The site keeps its UI strings in ~16 independent object literals scattered
across the HTML files and the js/ bundles. Each one is keyed by language
code (en, es, pt, ...). This tool finds them all by locating the *last*
existing language key ("ceb", or "sv" where ceb is absent) and treating the
object that follows as the template.

  python3 scripts/i18n_tool.py list
  python3 scripts/i18n_tool.py extract en  -> scripts/i18n_data/<site>.<n>.en.json
  python3 scripts/i18n_tool.py inject  ar  <- scripts/i18n_data/<site>.<n>.ar.json

Extraction preserves key order so the injected block reads like its
neighbours. Injection is idempotent: a dictionary that already carries the
language is skipped.
"""
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_data")

# Files that hold language dictionaries. beta/ twins are handled by mirroring
# the root file's edits, so only one side is listed here.
FILES = [
    "index.html",
    "beta/index.html",
    "highlights.html",
    "share.html",
    "js/app.js",
    "js/jw-session.js",
    "js/reading.js",
    "js/resurface.js",
]

# beta/index.html carries the same twelve dictionaries as the root copy with
# identical English source, so both read the same translation files.
DATA_ALIAS = {"beta/index.html": "index.html"}

# The language whose object marks the end of each dictionary. Most carry
# "ceb"; share.html's stops at "sv".
TAIL_LANGS = ["ceb", "sv"]


def _match_brace(s, start):
    """Return the index just past the object literal opening at s[start]=='{'."""
    depth = 0
    i = start
    n = len(s)
    while i < n:
        ch = s[i]
        if ch in "\"'`":
            quote = ch
            i += 1
            while i < n:
                if s[i] == "\\":
                    i += 2
                    continue
                if s[i] == quote:
                    break
                i += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced object literal at %d" % start)


def find_dicts(text, lang):
    """Every `<lang>: { ... }` entry in text, as (key_start, obj_start, obj_end)."""
    out = []
    for m in re.finditer(r"""(?<![A-Za-z0-9_$])(["']?)%s\1\s*:\s*\{""" % lang, text):
        obj_start = text.index("{", m.start())
        try:
            obj_end = _match_brace(text, obj_start)
        except ValueError:
            continue
        out.append((m.start(), obj_start, obj_end))
    return out


def enclosing_table(text, key_start):
    """Byte range of the object literal that holds the language keys."""
    depth = 0
    i = key_start
    while i >= 0:
        ch = text[i]
        if ch == "}":
            depth += 1
        elif ch == "{":
            if depth == 0:
                break
            depth -= 1
        i -= 1
    return i, _match_brace(text, i)


def dict_sites(text):
    """Locate one anchor dictionary per language table in the file.

    A table is the object whose keys are language codes. The anchor is that
    table's last language entry — "ceb" where it exists, otherwise "sv" — and
    a new language is spliced in immediately after it.
    """
    by_table = {}
    for tail in TAIL_LANGS:
        for key_start, obj_start, obj_end in find_dicts(text, tail):
            # Require the object to look like a string table, not arbitrary code.
            body = text[obj_start:obj_end]
            if len(re.findall(r"[{,]\s*[\"']?[A-Za-z_][A-Za-z0-9_]*[\"']?\s*:", body)) < 3:
                continue
            table = enclosing_table(text, key_start)
            # First tail wins: TAIL_LANGS is ordered ceb-before-sv, and ceb is
            # always the later entry where both exist.
            if table in by_table:
                continue
            by_table[table] = {
                "tail": tail,
                "table": table,
                "key_start": key_start,
                "obj_start": obj_start,
                "obj_end": obj_end,
            }
    sites = sorted(by_table.values(), key=lambda s: s["obj_start"])
    # Drop any table nested inside another (a dictionary inside a dictionary).
    kept = []
    for s in sites:
        if any(k["table"][0] < s["table"][0] and s["table"][1] <= k["table"][1] for k in kept):
            continue
        kept.append(s)
    return kept


def read_lang(text, site, lang):
    """The `lang` object belonging to the same table as `site`, as an ordered dict."""
    # Search backwards from the table start for the requested language key at
    # the same nesting depth: simplest reliable way is to scan the whole
    # enclosing table. Find the enclosing '{' of the table.
    depth = 0
    i = site["key_start"]
    while i >= 0:
        ch = text[i]
        if ch == "}":
            depth += 1
        elif ch == "{":
            if depth == 0:
                break
            depth -= 1
        i -= 1
    table_start = i
    table_end = _match_brace(text, table_start)
    table = text[table_start:table_end]
    hits = find_dicts(table, lang)
    if not hits:
        return None, (table_start, table_end)
    _, os_, oe_ = hits[0]
    return table[os_:oe_], (table_start, table_end)


def js_to_obj(src):
    """Evaluate a JS object literal of plain string values into a Python dict."""
    import subprocess
    out = subprocess.run(
        ["node", "-e",
         "const o=(" + src + ");process.stdout.write(JSON.stringify(o))"],
        capture_output=True, text=True)
    if out.returncode != 0:
        raise ValueError(out.stderr.strip()[:400])
    return json.loads(out.stdout)


def obj_to_js(obj, style):
    """Render a Python dict back as a JS object literal.

    `style` mirrors the surrounding code: 'json' quotes keys with " , 'bare'
    leaves keys unquoted and uses double-quoted values.
    """
    parts = []
    for k, v in obj.items():
        key = json.dumps(k, ensure_ascii=False) if style == "json" else k
        parts.append("%s:%s" % (key, json.dumps(v, ensure_ascii=False)))
    return "{" + ",".join(parts) + "}"


def detect_style(src):
    return "json" if re.match(r'\{\s*"', src) else "bare"


def data_name(f, n, lang):
    return "%s.%d.%s.json" % (DATA_ALIAS.get(f, f).replace("/", "_"), n, lang)


def cmd_list():
    for f in FILES:
        text = io.open(os.path.join(REPO, f), encoding="utf-8").read()
        sites = dict_sites(text)
        print("%s: %d dictionaries" % (f, len(sites)))
        for n, s in enumerate(sites):
            en, _ = read_lang(text, s, "en")
            keys = len(js_to_obj(en)) if en else 0
            print("   [%d] tail=%s at %d  en_keys=%d" % (n, s["tail"], s["obj_start"], keys))


def cmd_extract(lang):
    os.makedirs(DATA, exist_ok=True)
    for f in FILES:
        if f in DATA_ALIAS:
            continue  # shares the aliased file's translation data
        text = io.open(os.path.join(REPO, f), encoding="utf-8").read()
        for n, s in enumerate(dict_sites(text)):
            src, _ = read_lang(text, s, lang)
            if src is None:
                print("  %s[%d]: no '%s'" % (f, n, lang))
                continue
            obj = js_to_obj(src)
            name = data_name(f, n, lang)
            with io.open(os.path.join(DATA, name), "w", encoding="utf-8") as fh:
                json.dump(obj, fh, ensure_ascii=False, indent=1)
            print("  wrote %s (%d keys)" % (name, len(obj)))


def cmd_inject(lang):
    total = 0
    for f in FILES:
        path = os.path.join(REPO, f)
        text = io.open(path, encoding="utf-8").read()
        orig = text
        # Work back-to-front so earlier offsets stay valid.
        for n, s in reversed(list(enumerate(dict_sites(text)))):
            name = data_name(f, n, lang)
            src = os.path.join(DATA, name)
            if not os.path.exists(src):
                print("  %s[%d]: no translation file %s — skipped" % (f, n, name))
                continue
            existing, _ = read_lang(text, s, lang)
            if existing is not None:
                print("  %s[%d]: '%s' already present — skipped" % (f, n, lang))
                continue
            obj = json.load(io.open(src, encoding="utf-8"))
            tail_src = text[s["obj_start"]:s["obj_end"]]
            style = detect_style(tail_src)
            key = '"%s"' % lang if style == "json" else lang
            block = ",%s:%s" % (key, obj_to_js(obj, style))
            text = text[:s["obj_end"]] + block + text[s["obj_end"]:]
            total += 1
            print("  %s[%d]: injected %s (%d keys, style=%s)" % (f, n, lang, len(obj), style))
        if text != orig:
            io.open(path, "w", encoding="utf-8").write(text)
    print("injected into %d dictionaries" % total)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        cmd_list()
    elif cmd == "extract":
        cmd_extract(sys.argv[2])
    elif cmd == "inject":
        cmd_inject(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)

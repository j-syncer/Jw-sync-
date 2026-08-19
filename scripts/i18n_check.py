#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
i18n_check.py — verify a language covers every key of every dictionary.

Reuses i18n_tool's dictionary finder so the check can never drift from the
extractor. Prints one line per table:

    OK   index.html[0] 55 keys
    FAIL index.html[3] missing 2 key(s): apply, close

Exit code is non-zero if anything failed, so it works as a standalone check as
well as through tests/18_arabic_rtl.js.

    python3 scripts/i18n_check.py ar
    python3 scripts/i18n_check.py --all            # every offered language
    python3 scripts/i18n_check.py --all --json     # ditto, as JSON

`--all` exists because checking languages one at a time re-reads and re-parses
every dictionary once per language. tests/26_i18n_coverage.js used to invoke
this script 27 times and took 74 seconds, against three to five for every other
suite. One pass shares the file reads, the English tables and — through
i18n_tool.js_to_objs — a single node process per dictionary.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_tool as t  # noqa: E402


def offered_langs():
    """The languages the site actually ships, from the `?lang=` allow-list.

    Read rather than listed, so this cannot fall behind the site the way a
    hard-coded roster does.
    """
    import re
    text = io.open(os.path.join(t.REPO, "index.html"), encoding="utf-8").read()
    head = text[:text.index("</head>")]
    m = re.search(r"var V=\[([^\]]*)\]", head)
    if not m:
        raise SystemExit("could not read the ?lang= allow-list from index.html")
    return re.findall(r"['\"]([A-Za-z-]+)['\"]", m.group(1))


def scan(langs):
    """{lang: {"ok": [labels], "fail": [messages]}} for every dictionary."""
    out = {l: {"ok": [], "fail": []} for l in langs}
    for f in t.FILES:
        path = os.path.join(t.REPO, f)
        if not os.path.exists(path):
            continue
        text = io.open(path, encoding="utf-8").read()
        for n, site in enumerate(t.dict_sites(text)):
            label = "%s[%d]" % (f, n)
            en_src, _ = t.read_lang(text, site, "en")
            if en_src is None:
                for l in langs:
                    out[l]["fail"].append(
                        "%s has no 'en' table to compare against" % label)
                continue
            present, srcs = [], []
            for l in langs:
                src, _ = t.read_lang(text, site, l)
                if src is None:
                    out[l]["fail"].append(
                        "%s has no '%s' table at all" % (label, l))
                else:
                    present.append(l)
                    srcs.append(src)
            # One node process for this dictionary's English plus every
            # language of it, rather than one per language.
            objs = t.js_to_objs([en_src] + srcs)
            en, rest = objs[0], objs[1:]
            for l, got in zip(present, rest):
                missing = [k for k in en if k not in got]
                empty = [k for k in en if k in got and got[k] == ""]
                if missing:
                    out[l]["fail"].append(
                        "%s missing %d key(s): %s"
                        % (label, len(missing), ", ".join(missing[:6])))
                elif empty:
                    out[l]["fail"].append(
                        "%s has %d empty value(s): %s"
                        % (label, len(empty), ", ".join(empty[:6])))
                else:
                    out[l]["ok"].append("%s %d keys" % (label, len(got)))
    return out


def main(lang):
    r = scan([lang])[lang]
    for line in r["ok"]:
        print("OK   %s" % line)
    for line in r["fail"]:
        print("FAIL %s" % line)
    return 1 if r["fail"] else 0


def main_all(as_json):
    langs = offered_langs()
    res = scan(langs)
    if as_json:
        print(json.dumps(res))
    else:
        for l in langs:
            for line in res[l]["ok"]:
                print("OK   %s %s" % (l, line))
            for line in res[l]["fail"]:
                print("FAIL %s %s" % (l, line))
    return 1 if any(res[l]["fail"] for l in langs) else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        sys.exit(main_all("--json" in args))
    sys.exit(main(args[0] if args else "ar"))

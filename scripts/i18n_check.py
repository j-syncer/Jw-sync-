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
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_tool as t  # noqa: E402


def main(lang):
    failed = 0
    for f in t.FILES:
        path = os.path.join(t.REPO, f)
        if not os.path.exists(path):
            continue
        text = io.open(path, encoding="utf-8").read()
        for n, site in enumerate(t.dict_sites(text)):
            label = "%s[%d]" % (f, n)
            en_src, _ = t.read_lang(text, site, "en")
            if en_src is None:
                print("FAIL %s has no 'en' table to compare against" % label)
                failed += 1
                continue
            src, _ = t.read_lang(text, site, lang)
            if src is None:
                print("FAIL %s has no '%s' table at all" % (label, lang))
                failed += 1
                continue
            en = t.js_to_obj(en_src)
            got = t.js_to_obj(src)
            missing = [k for k in en if k not in got]
            empty = [k for k in en if k in got and got[k] == ""]
            if missing:
                print("FAIL %s missing %d key(s): %s"
                      % (label, len(missing), ", ".join(missing[:6])))
                failed += 1
            elif empty:
                print("FAIL %s has %d empty value(s): %s"
                      % (label, len(empty), ", ".join(empty[:6])))
                failed += 1
            else:
                print("OK   %s %d keys" % (label, len(got)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "ar"))

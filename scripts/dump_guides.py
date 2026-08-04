#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print the English source of a slice of guides, ready to translate.

    python3 scripts/dump_guides.py 0 6

Prints guides [start, end) in a compact, line-per-string form so a whole
batch fits in one screen. `slug` and `group` are shown for reference but are
never translated — they are the keys the translated record is filed under.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_guides import GUIDES  # noqa: E402


def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(GUIDES)
    for i, g in enumerate(GUIDES[start:end], start):
        print("=" * 70)
        print("[%d] %s   (group: %s)" % (i, g["slug"], g["group"]))
        print("TITLE: " + g["title"])
        print("H1:    " + g["h1"])
        print("DESC:  " + g["description"])
        for j, p in enumerate(g["intro"]):
            print("INTRO%d: %s" % (j, p))
        for j, (h, b) in enumerate(g["steps"]):
            print("STEP%d.h: %s" % (j, h))
            print("STEP%d.b: %s" % (j, b))
        for j, (h, b) in enumerate(g["sections"]):
            print("SEC%d.h: %s" % (j, h))
            print("SEC%d.b: %s" % (j, b))
        for j, (q, a) in enumerate(g.get("faq", [])):
            print("FAQ%d.q: %s" % (j, q))
            print("FAQ%d.a: %s" % (j, a))


if __name__ == "__main__":
    main()

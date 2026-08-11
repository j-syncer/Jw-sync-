#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check every wtlocale in js/reading.js against the live jw.org finder.

    python3 scripts/verify_wtlocale.py

`tests/16_reading.js` asserts the WTLOCALE map matches a table of values that
were each verified once, by hand, at the moment their language was added. That
catches the map drifting away from the table. It cannot catch the table itself
being wrong, because the authority is a third-party site and the test suite
does not — and should not — reach the network.

This script is the other half: it asks jw.org what each code actually serves.
Run it when adding a language, and occasionally afterwards, because the failure
mode here is silent. An unrecognised code returns a working Bible chapter in
the wrong language, with no error anywhere: `HB` served English to Hebrew
readers for two releases, `VI` serves Russian, `INS` serves Indonesian Sign
Language.

Exit code is 0 only if every language checks out.
"""
import concurrent.futures
import io
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# jw.org answers with the ISO 639-3 individual-language code where we use the
# BCP-47 macrolanguage tag, so zh-Hans comes back as cmn-hans. Same language.
MACROLANGUAGE = {"cmn": "zh"}


def norm(tag):
    parts = tag.lower().split("-")
    parts[0] = MACROLANGUAGE.get(parts[0], parts[0])
    return "-".join(parts)


def check(pair):
    code, wt = pair
    url = "https://www.jw.org/finder?wtlocale=%s&pub=nwtsty&bible=1001000" % wt
    try:
        out = subprocess.run(["curl", "-sL", "--max-time", "40", url],
                             capture_output=True, text=True, timeout=90).stdout
    except Exception as e:
        return code, wt, "unreachable (%s)" % e, False
    m = re.search(r'<html[^>]*\blang="([A-Za-z-]+)"', out)
    if not m:
        return code, wt, "no <html lang>", False
    served = m.group(1)
    return code, wt, served, norm(served) == norm(code)


def main():
    src = io.open(os.path.join(REPO, "js", "reading.js"), encoding="utf-8").read()
    m = re.search(r"var WTLOCALE = \{([^}]*)\}", src)
    if not m:
        sys.exit("ABORT: WTLOCALE map not found in js/reading.js")
    pairs = re.findall(r"'?([A-Za-z-]+)'?:\s*'([A-Za-z0-9]+)'", m.group(1))
    print("Checking %d wtlocale codes against jw.org…\n" % len(pairs))

    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        rows = list(ex.map(check, pairs))

    bad = [r for r in rows if not r[3]]
    for code, wt, served, ok in rows:
        print("  %-9s %-4s -> %-12s %s" % (code, wt, served, "ok" if ok else "WRONG"))
    print()
    if not bad:
        print("All %d serve the right language." % len(rows))
        return 0
    print("%d WRONG — each of these serves a working page in the wrong\n"
          "language, which no test or page load will ever report:" % len(bad))
    for code, wt, served, _ in bad:
        print("  %s: wtlocale %r serves %r" % (code, wt, served))
    return 1


if __name__ == "__main__":
    sys.exit(main())

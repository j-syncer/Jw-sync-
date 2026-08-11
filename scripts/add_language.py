#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wire a new language into every enumeration point, in one parameterised pass.

    python3 scripts/add_language.py --code sw --label "🇰🇪 Kiswahili" --wtlocale SW
    python3 scripts/add_language.py --code fa --label "🇮🇷 فارسی" --wtlocale P --rtl

Replaces the ten hand-copied `add_<language>_plumbing.py` scripts. Those stay in
`scripts/` as historical records of what was actually run; do not re-run them.

WHY THIS EXISTS
---------------
Every language until now got its own copy of a ~70-line script with the
previous language's strings pasted in as anchors. Two things went wrong with
that, both of which this file is shaped to prevent:

1. A bug in the shared `patch()` helper — skipping on the presence of the *new*
   string rather than the absence of the *old* one — survived six languages
   before it silently left both index.html bootstrap lists stale on Romanian.
   Copy-paste propagates bugs and hides them; there is one implementation here.

2. Anchors had to be updated by hand for each new language, so adding one meant
   editing strings that describe the *previous* language. Nothing here is
   hard-coded: every insertion point is derived by reading the current state of
   the file, so this script does not go stale between languages.

THE wtlocale GATE
-----------------
jw.org serves English — or another language entirely — for any code it does not
recognise, with no error. Hebrew shipped as `HB` and served English for two
releases. Since then: `ID` serves English, `RO` serves English, `VI` serves
Russian, `V` serves Slovak, `R` serves Western Armenian, `RU` serves Rundi,
`INS` serves Indonesian Sign Language. Not one of those is guessable.

So the probe is not advice in a runbook, it is a precondition of this script.
`--wtlocale` is verified against the live finder before anything is written, and
a mismatch aborts. `--skip-probe` exists for working offline and says loudly
that the value is unverified.
"""
import argparse
import io
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Both index.html files carry the picker and the allow-list; the satellite pages
# carry only the jw-dir-init bootstrap copy of the allow-list.
INDEX_PAGES = ["index.html", "beta/index.html"]
BOOTSTRAP_PAGES = INDEX_PAGES + [
    "highlights.html", "beta/highlights.html",
    "share.html", "beta/share.html", "forum.html",
]
JS_PAIRS = {
    "reading": ["js/reading.js", "beta/js/reading.js"],
    "app": ["js/app.js", "beta/js/app.js"],
}

changed, skipped = [], []


def read(rel):
    return io.open(os.path.join(REPO, rel), encoding="utf-8").read()


def write(rel, text):
    io.open(os.path.join(REPO, rel), "w", encoding="utf-8").write(text)


SKIP = object()  # sentinel: this file already has the language


def edit(rel, fn, what):
    """Apply fn to a file's text.

    fn returns SKIP if the language is already present, the new text if it
    patched something, or None if its anchor was not found — which is fatal.
    Treating a missing anchor as 'nothing to do' is how the previous scripts
    silently left both index.html bootstrap lists stale."""
    before = read(rel)
    after = fn(before)
    if after is SKIP:
        skipped.append("%s (%s)" % (rel, what))
        return
    if after is None:
        sys.exit("ABORT: no anchor for %s in %s. The file has drifted from "
                 "what this script expects;\n       fix the pattern rather "
                 "than skipping the file." % (what, rel))
    if after == before:
        skipped.append("%s (%s)" % (rel, what))
        return
    write(rel, after)
    changed.append("%s (%s)" % (rel, what))


def sub_once(text, pattern, repl, where, flags=0):
    """Exactly-one-match substitution, or abort. Sloppy anchors are the whole
    reason the old scripts needed hand-checking; make ambiguity fatal.

    `repl` is always a callable taking the match, never a template string: the
    labels being inserted contain `\\u{1F1F7}` escapes, which re.sub would try
    to interpret as backreferences in a template."""
    n = len(re.findall(pattern, text, flags))
    if n == 0:
        return None
    if n != 1:
        sys.exit("ABORT: anchor for %s matched %d times, expected 1" % (where, n))
    return re.sub(pattern, repl, text, count=1, flags=flags)


def js_key(code):
    """A JS object key. A BCP-47 tag with a script subtag contains a hyphen and
    cannot be a bare identifier — 'zh-Hans' must be quoted, en must not be."""
    return "'%s'" % code if not re.match(r"^[A-Za-z_$][\w$]*$", code) else code


def js_escape(label):
    """Escape a label the way the shipped NAV_LANGS entries are escaped, so the
    file stays pure ASCII: astral (flag) codepoints as \\u{...}, other non-ASCII
    as \\uXXXX, ASCII left alone."""
    out = []
    for ch in label:
        cp = ord(ch)
        if cp > 0xFFFF:
            out.append("\\u{%X}" % cp)
        elif cp > 0x7F:
            out.append("\\u%04x" % cp)
        else:
            out.append(ch)
    return "".join(out)


def current_codes():
    """The allow-list in index.html is the source of truth for what ships."""
    m = re.search(r"var V=\[([^\]]*)\]", read("index.html"))
    if not m:
        sys.exit("ABORT: could not find `var V=[…]` in index.html")
    return re.findall(r"'([^']+)'", m.group(1))


# ── the jw.org gate ─────────────────────────────────────────────────────────
# jw.org answers with the ISO 639-3 individual-language code where we use the
# BCP-47 macrolanguage tag, so `zh-Hans` comes back as `cmn-hans`. Both name
# the same language; a strict string compare would abort on a correct value and
# push whoever hit it towards --skip-probe, which is the opposite of the point.
# Keep this map minimal and evidenced — every entry is one we have seen served.
MACROLANGUAGE = {"cmn": "zh"}


def norm_tag(tag):
    parts = tag.lower().split("-")
    parts[0] = MACROLANGUAGE.get(parts[0], parts[0])
    return "-".join(parts)


def probe(code, wtlocale):
    url = ("https://www.jw.org/finder?wtlocale=%s&pub=nwtsty&bible=1001000"
           % wtlocale)
    try:
        html = subprocess.run(["curl", "-sL", "--max-time", "30", url],
                              capture_output=True, text=True, timeout=60).stdout
    except Exception as e:
        sys.exit("ABORT: could not reach jw.org to verify wtlocale (%s).\n"
                 "       Re-run with --skip-probe only if you have verified it "
                 "another way." % e)
    m = re.search(r'<html[^>]*\blang="([A-Za-z-]+)"', html)
    if not m:
        sys.exit("ABORT: jw.org response had no <html lang=…>; cannot verify "
                 "wtlocale %r." % wtlocale)
    served = m.group(1)
    if norm_tag(served) != norm_tag(code):
        sys.exit(
            "ABORT: wtlocale %r serves lang=%r, but you are adding %r.\n"
            "       This is the failure mode the probe exists for: jw.org "
            "returns a working page\n"
            "       in the wrong language rather than an error. Find the real "
            "code before shipping." % (wtlocale, served, code))
    print("  wtlocale %-4s serves lang=%-8s ✓" % (wtlocale, served))


# ── the five enumeration points ─────────────────────────────────────────────
def add_to_allow_list(code, last):
    """`var V=['en',…,'<last>']` in both index.html files."""
    pat = r"(var V=\[(?:[^\]]*)'%s')\]" % re.escape(last)
    rep = lambda m: "%s,'%s']" % (m.group(1), code)
    for page in INDEX_PAGES:
        edit(page, lambda t: sub_once(t, pat, rep, "allow-list"), "allow-list")


def add_to_bootstrap(code, last):
    """The jw-dir-init <head> copy of the same list, on all seven pages.

    Anchored on the leading newline: the bare `V=[…]` form is also a substring
    of `var V=[…]`, which is exactly what made the old scripts no-op here."""
    pat = r"(\nV=\[(?:[^\]]*)'%s')\]" % re.escape(last)
    rep = lambda m: "%s,'%s']" % (m.group(1), code)
    for page in BOOTSTRAP_PAGES:
        edit(page, lambda t: sub_once(t, pat, rep, "bootstrap"),
             "dir-bootstrap allow-list")


def add_to_picker(code, label, last):
    """The nav <select> in both index.html files."""
    pat = r'(<option value="%s">[^<]*</option>)' % re.escape(last)
    rep = lambda m: '%s\n      <option value="%s">%s</option>' % (
        m.group(1), code, label)
    for page in INDEX_PAGES:
        edit(page, lambda t: sub_once(t, pat, rep, "nav picker"), "nav picker")


def add_to_nav_langs(code, label, last):
    """NAV_LANGS in js/app.js — a second, independent picker."""
    pat = r'(\["%s","[^"]*"\])\]' % re.escape(last)
    rep = lambda m: '%s,["%s","%s"]]' % (m.group(1), code, js_escape(label))
    for f in JS_PAIRS["app"]:
        edit(f, lambda t: sub_once(t, pat, rep, "NAV_LANGS"), "NAV_LANGS")


def add_to_wtlocale(code, wtlocale, last):
    """WTLOCALE in js/reading.js — the jw.org deep-link map."""
    pat = r"((?:'%s'|%s): '[^']*')\s*\}" % (re.escape(last), re.escape(last))
    rep = lambda m: "%s, %s: '%s' }" % (m.group(1), js_key(code), wtlocale)
    for f in JS_PAIRS["reading"]:
        edit(f, lambda t: sub_once(t, pat, rep, "WTLOCALE"), "WTLOCALE")


def add_to_rtl_map(code):
    """`R={ar:1,he:1,…}` in the jw-dir-init bootstrap, for an RTL language."""
    pat = r"(R=\{[^}]*)\}"
    for page in BOOTSTRAP_PAGES:
        def fn(t, c=code):
            if re.search(r"R=\{[^}]*\b%s:1" % re.escape(c), t):
                return SKIP
            return sub_once(t, pat, lambda m: "%s,%s:1}" % (m.group(1), c),
                            "RTL map")
        edit(page, fn, "RTL map")


# ── the builders and the test language lists ────────────────────────────────
def add_to_builders(code, name, locale, rtl):
    """The runbook's table of which builder defines which list. Mechanical, and
    hand-editing it is how a language ends up half-registered."""
    def append_to_list(var, value, quote='"'):
        def fn(t):
            if re.search(r"%s = \[[^\]]*%s%s%s" % (var, quote, re.escape(code), quote), t):
                return SKIP
            if not re.search(r"%s = \[" % var, t):
                return SKIP          # this builder does not define that list
            pat = r"(%s = \[[^\]]*%s[\w-]+%s)\]" % (var, quote, quote)
            return sub_once(t, pat,
                            lambda m: "%s, %s%s%s]" % (m.group(1), quote, value, quote),
                            var)
        return fn

    for f in ("scripts/build_guides.py", "scripts/build_landing.py",
              "scripts/build_seo.py"):
        edit(f, append_to_list("LANGS", code), "LANGS")
    if rtl:
        for f in ("scripts/build_guides.py", "scripts/build_landing.py"):
            edit(f, append_to_list("RTL_LANGS", code), "RTL_LANGS")

    def add_map_entry(var, key, value):
        def fn(t):
            if re.search(r'%s = \{.*?"%s":' % (var, re.escape(key)), t, re.S):
                return SKIP
            # DOTALL: these maps span many lines, so `.` must cross newlines.
            pat = r"(%s = \{.*?)\n\}" % var
            return sub_once(t, pat,
                            lambda m: '%s\n    "%s": "%s",\n}' % (m.group(1), key, value),
                            var, flags=re.S)
        return fn

    edit("scripts/build_landing.py", add_map_entry("LANG_NAME", code, name),
         "LANG_NAME")
    for f in ("scripts/build_landing.py", "scripts/build_seo.py"):
        edit(f, add_map_entry("LOCALE", code, locale), "LOCALE")


def add_to_tests(code, last):
    """The suites keep their own language lists, in `'xx', 'yy'` shape."""
    import glob
    pat = r"('%s')\]" % re.escape(last)
    for f in sorted(glob.glob(os.path.join(REPO, "tests", "*.js"))):
        rel = os.path.relpath(f, REPO)
        def fn(t, c=code):
            if re.search(r"'%s'\]" % re.escape(c), t):
                return SKIP
            if not re.search(pat, t):
                return SKIP      # this suite keeps no language list
            return re.sub(pat, lambda m: "%s, '%s']" % (m.group(1), c), t)
        edit(rel, fn, "language list")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--code", required=True, help="BCP-47 tag, e.g. sw or zh-Hans")
    ap.add_argument("--label", required=True, help='picker label, e.g. "🇰🇪 Kiswahili"')
    ap.add_argument("--wtlocale", required=True, help="jw.org locale code — VERIFIED")
    ap.add_argument("--name", help="endonym for LANG_NAME (default: label minus flag)")
    ap.add_argument("--locale", help="OG locale, e.g. sw_KE (default: <code>_<CODE>)")
    ap.add_argument("--rtl", action="store_true", help="right-to-left language")
    ap.add_argument("--skip-probe", action="store_true",
                    help="do not verify wtlocale against jw.org (unverified!)")
    a = ap.parse_args()

    codes = current_codes()
    if a.code in codes:
        sys.exit("ABORT: %r is already in the allow-list." % a.code)
    last = codes[-1]
    name = a.name or a.label.split(" ", 1)[-1].strip()
    locale = a.locale or "%s_%s" % (a.code.split("-")[0],
                                    a.code.split("-")[0].upper())

    print("Adding %s (%s) after %s — wtlocale %s%s"
          % (a.code, name, last, a.wtlocale, ", RTL" if a.rtl else ""))
    if a.skip_probe:
        print("  !! wtlocale NOT verified against jw.org (--skip-probe).")
        print("  !! An unrecognised code serves a working page in the wrong")
        print("  !! language. Verify before this reaches production.")
    else:
        probe(a.code, a.wtlocale)

    add_to_allow_list(a.code, last)
    add_to_picker(a.code, a.label, last)
    add_to_nav_langs(a.code, a.label, last)
    add_to_wtlocale(a.code, a.wtlocale, last)
    add_to_bootstrap(a.code, last)
    if a.rtl:
        add_to_rtl_map(a.code)
    add_to_builders(a.code, name, locale, a.rtl)
    add_to_tests(a.code, last)

    print("\npatched %d:" % len(changed))
    for c in changed:
        print("  " + c)
    if skipped:
        print("already current (%d): %s" % (len(skipped), ", ".join(skipped)))
    print("""
Still to do by hand — this script only does the enumeration points:
  1. UI strings:  i18n_tool.py extract en / write *.%s.json / inject %s
                  plus the offline banner in both index.html and the three
                  scripts/i18n_data/*.json tables i18n_tool cannot see
  2. guides_i18n.py: CHROME[%r] and the GUIDE_TEXT registration
  3. guides:      build_lang_guides.py (add %r to META, STRAY, DIACRITIC)
  4. VERIFIED wtlocale table in tests/16_reading.js
  5. build, bump softwareVersion + CACHE_VERSION, CHANGELOG, CLAUDE.md roster
Do NOT re-run add_rtl_wiring.py; the bootstrap is handled above.""" % (
        a.code, a.code, a.code, a.code))


if __name__ == "__main__":
    main()

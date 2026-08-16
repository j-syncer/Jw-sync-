#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_navbar_i18n.py — replace the hardcoded English in the app navbar.

The navbar rendered eleven strings — button labels and every title= tooltip —
as English literals, so they stayed English in all thirteen languages while
the rest of the UI translated around them. The keys were added to TRANSLATIONS
by i18n_addkeys.py; this rewires the render to read them.

It also rebuilds the in-app language <select>. That list was written out by
hand and had fallen a language behind: it ended at Swedish, so Cebuano users
could never switch back to Cebuano from inside the app. It is now generated
from a single array, which is why it cannot drift again.

Idempotent — each replacement checks it has not already been applied.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The picker is built from one array so a new language is a one-line change.
# Flags are emoji regional-indicator pairs, matching the landing picker.
LANG_OPTIONS_OLD = (
    'React.createElement("option",{value:"en"},"\\u{1F1EC}\\u{1F1E7} English"),'
    'React.createElement("option",{value:"es"},"\\u{1F1EA}\\u{1F1F8} Espa\\xF1ol"),'
    'React.createElement("option",{value:"pt"},"\\u{1F1E7}\\u{1F1F7} Portugu\\xEAs"),'
    'React.createElement("option",{value:"fr"},"\\u{1F1EB}\\u{1F1F7} Fran\\xE7ais"),'
    'React.createElement("option",{value:"de"},"\\u{1F1E9}\\u{1F1EA} Deutsch"),'
    'React.createElement("option",{value:"it"},"\\u{1F1EE}\\u{1F1F9} Italiano"),'
    'React.createElement("option",{value:"ru"},"\\u{1F1F7}\\u{1F1FA} \\u0420\\u0443\\u0441\\u0441\\u043A\\u0438\\u0439"),'
    'React.createElement("option",{value:"ja"},"\\u{1F1EF}\\u{1F1F5} \\u65E5\\u672C\\u8A9E"),'
    'React.createElement("option",{value:"ko"},"\\u{1F1F0}\\u{1F1F7} \\uD55C\\uAD6D\\uC5B4"),'
    'React.createElement("option",{value:"tl"},"\\u{1F1F5}\\u{1F1ED} Filipino"),'
    'React.createElement("option",{value:"sv"},"\\u{1F1F8}\\u{1F1EA} Svenska")'
)
LANG_OPTIONS_NEW = (
    'NAV_LANGS.map(function(L){return React.createElement("option",'
    '{key:L[0],value:L[0]},L[1])})'
)

# Defined next to TRANSLATIONS so the two lists are edited together.
NAV_LANGS_DECL = (
    'NAV_LANGS=[["en","\\u{1F1EC}\\u{1F1E7} English"],'
    '["es","\\u{1F1EA}\\u{1F1F8} Espa\\xF1ol"],'
    '["pt","\\u{1F1E7}\\u{1F1F7} Portugu\\xEAs"],'
    '["fr","\\u{1F1EB}\\u{1F1F7} Fran\\xE7ais"],'
    '["de","\\u{1F1E9}\\u{1F1EA} Deutsch"],'
    '["it","\\u{1F1EE}\\u{1F1F9} Italiano"],'
    '["ru","\\u{1F1F7}\\u{1F1FA} \\u0420\\u0443\\u0441\\u0441\\u043A\\u0438\\u0439"],'
    '["ja","\\u{1F1EF}\\u{1F1F5} \\u65E5\\u672C\\u8A9E"],'
    '["ko","\\u{1F1F0}\\u{1F1F7} \\uD55C\\uAD6D\\uC5B4"],'
    '["tl","\\u{1F1F5}\\u{1F1ED} Filipino"],'
    '["sv","\\u{1F1F8}\\u{1F1EA} Svenska"],'
    '["ceb","\\u{1F1F5}\\u{1F1ED} Cebuano"],'
    '["ar","\\u{1F1F8}\\u{1F1E6} \\u0627\\u0644\\u0639\\u0631\\u0628\\u064A\\u0629"]],'
)

REPLACEMENTS = [
    # Simple/Advanced toggle (beta shell)
    ('title:be?"Show advanced tools":"Back to the simple view"},'
     'be?"Advanced options":"‹ Simple view"',
     'title:be?s("nav_adv_show_title"):s("nav_adv_back_title")},'
     'be?s("nav_adv_options"):s("nav_simple_view")'),
    # Simple / Full segmented control (production shell)
    ('title:"Simple — step-by-step wizard"},"\\u2726 Simple"',
     'title:s("mode_simple_title")},"\\u2726 "+s("mode_simple")'),
    ('title:"Full Mode — all advanced tools"},"\\u26A1 Full"',
     'title:s("mode_full_title")},"\\u26A1 "+s("mode_full")'),
    # Tooltips whose visible labels were already translated. The anchors carry
    # the following render code because the same English now also appears as a
    # value inside TRANSLATIONS — matching on the bare literal would hit both.
    ('title:"Try with sample notes"},s("cta_try_demo_nav")',
     'title:s("nav_demo_title")},s("cta_try_demo_nav")'),
    ('title:"Open Note Explorer"},"📖 "',
     'title:s("nav_browse_title")},"📖 "'),
    # Community button: label and tooltip both hardcoded
    ('title:"Community \\u2014 ask questions, report bugs"},"\\u{1F4AC} Community"',
     'title:s("nav_community_title")},"\\u{1F4AC} "+s("nav_community")'),
    # Cross-device share button
    ('title:"Open on another device"},"\\u25A6 Share"',
     'title:s("nav_share_title")},"\\u25A6 "+s("nav_share_btn")'),
    # Theme toggle
    ('title:Je?"Switch to Light Mode":"Switch to Dark Mode"',
     'title:Je?s("theme_to_light"):s("theme_to_dark")'),
    # Give the tool row a real class so the stylesheet has a hook that does not
    # depend on Tailwind utility names (see .jw-nav-tools in styles.css).
    ('className:"max-w-5xl mx-auto flex items-center gap-2 pb-2.5 overflow-x-auto"',
     'className:"jw-nav-tools max-w-5xl mx-auto flex items-center gap-2 pb-2.5 overflow-x-auto"'),
]


def main():
    path = os.path.join(REPO, "js", "app.js")
    c = io.open(path, encoding="utf-8").read()
    orig = c
    applied = 0

    for old, new in REPLACEMENTS:
        if new in c:
            continue
        if c.count(old) != 1:
            sys.exit("ABORT: anchor found %d times: %s" % (c.count(old), old[:70]))
        c = c.replace(old, new, 1)
        applied += 1

    if "NAV_LANGS" not in c:
        if c.count(LANG_OPTIONS_OLD) != 1:
            sys.exit("ABORT: language <option> run found %d times"
                     % c.count(LANG_OPTIONS_OLD))
        c = c.replace(LANG_OPTIONS_OLD, LANG_OPTIONS_NEW, 1)
        # TRANSLATIONS is one member of a `const A=…,B=…,TRANSLATIONS={…}`
        # chain, so the new array is spliced in as another member of it.
        anchor = "TRANSLATIONS={"
        if c.count(anchor) != 1:
            sys.exit("ABORT: TRANSLATIONS anchor x%d" % c.count(anchor))
        c = c.replace(anchor, NAV_LANGS_DECL + anchor, 1)
        applied += 1

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("js/app.js: %d navbar replacement(s) applied" % applied)
    else:
        print("js/app.js: already patched")


if __name__ == "__main__":
    main()

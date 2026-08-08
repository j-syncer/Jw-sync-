#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_rtl_wiring.py — install the direction bootstrap on every page.

Two things have to happen for Arabic to render correctly:

  1. `<html lang dir>` must be set *before first paint*, or the page renders
     LTR and visibly reflows once the app boots. So the bootstrap is an inline
     <head> script, not part of a bundle.
  2. It must run again whenever the language changes at runtime, because the
     site switches language without a reload.

The snippet exposes `window.__jwApplyDir(lang)` for (2); the callers are
patched below. Idempotent — every insertion checks for its marker first.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MARKER = "jw-dir-init"

# `V` mirrors the ?lang= allow-list in index.html. RTL is a set rather than a
# single check so Hebrew/Farsi/Urdu need no code change if they are ever added.
#
# The snippet also persists a valid ?lang= to localStorage. index.html already
# did this for itself, but the satellite pages did not — so a ?lang=ar deep
# link (the Arabic guides link straight into the tools) rendered Arabic page
# copy while jw-session.js, which reads only localStorage, still drew the tool
# switcher in English.
SNIPPET = """<script id="jw-dir-init">
(function(){var R={ar:1,he:1,fa:1,ur:1},
V=['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he'];
function a(l){var d=document.documentElement;l=l||'en';d.setAttribute('lang',l);d.setAttribute('dir',R[l]?'rtl':'ltr');}
window.__jwRTL=R;window.__jwApplyDir=a;
try{var q=(location.search.match(/[?&]lang=([a-z-]{2,5})/)||[])[1];
if(q&&V.indexOf(q)>=0)localStorage.setItem('jwsync_lang',q);else q=null;
a(q||localStorage.getItem('jwsync_lang')||'en');}catch(e){a('en');}}());
</script>"""

RTL_LINK = '<link rel="stylesheet" href="%srtl.css">'


def edit(path, fn):
    p = os.path.join(REPO, path)
    c = io.open(p, encoding="utf-8").read()
    out = fn(c)
    if out is None:
        print("unchanged", path)
        return
    io.open(p, "w", encoding="utf-8").write(out)
    print("patched", path)


def insert_head(c, css_prefix):
    """Add (or refresh) the bootstrap + rtl.css link just before </head>."""
    if MARKER in c:
        # Replace the existing block so the script stays re-runnable.
        start = c.index('<script id="%s">' % MARKER)
        end = c.index("</script>", start) + len("</script>")
        out = c[:start] + SNIPPET + c[end:]
        return out if out != c else None
    anchor = "</head>"
    if c.count(anchor) != 1:
        sys.exit("ABORT: %d </head> anchors" % c.count(anchor))
    block = SNIPPET + "\n" + (RTL_LINK % css_prefix) + "\n"
    return c.replace(anchor, block + anchor, 1)


# ── 1. The two app shells ────────────────────────────────────────────────
# applyLandingI18n is the single chokepoint every language change flows
# through: the nav picker calls it directly, and the React effect on [d]
# calls it via window.__applyLandingI18n.
I18N_HOOK_OLD = """  function applyLandingI18n(lang,translations){
    if(translations)cachedT=translations;"""
I18N_HOOK_NEW = """  function applyLandingI18n(lang,translations){
    if(translations)cachedT=translations;
    if(lang&&window.__jwApplyDir)window.__jwApplyDir(lang);"""

for f in ("index.html", "beta/index.html"):
    def patch_app(c, f=f):
        prefix = "" if f == "index.html" else ""
        c2 = insert_head(c, prefix)
        c = c2 if c2 is not None else c
        if I18N_HOOK_NEW not in c:
            if c.count(I18N_HOOK_OLD) != 1:
                sys.exit("ABORT %s: applyLandingI18n anchor x%d"
                         % (f, c.count(I18N_HOOK_OLD)))
            c = c.replace(I18N_HOOK_OLD, I18N_HOOK_NEW, 1)
        return c
    edit(f, patch_app)

# ── 2. Satellite pages ───────────────────────────────────────────────────
# highlights.html and share.html read jwsync_lang once at boot and have no
# picker of their own, so the head snippet alone is enough. forum.html has no
# i18n at all yet, but still needs its chrome mirrored.
for f in ("highlights.html", "beta/highlights.html",
          "share.html", "beta/share.html", "forum.html"):
    edit(f, lambda c: insert_head(c, ""))

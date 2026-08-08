#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_seo.py — the site's multilingual SEO layer.

Regenerates, from one language list:

  1. hreflang + x-default clusters in the <head> of every indexable page,
  2. og:locale / og:locale:alternate for the same set,
  3. localized <title> and <meta name="description"> (swapped at runtime, and
     seeded into __JW_LANDING_I18N from the already-translated hero copy so no
     new copy has to be invented per language),
  4. sitemap.xml, including the per-language guide trees.

Everything it writes is wrapped in `<!-- SEO:name -->` … `<!-- /SEO:name -->`
markers, so re-running replaces the previous block instead of stacking. Run it
after adding a language or a page:

    python3 scripts/build_seo.py

Note on scope — where hreflang may point:

Never at a ?lang=xx URL. Those serve byte-identical English HTML that
canonicalises back to "/", so an hreflang cluster over them advertises
alternates Google collapses straight into the canonical — Search Console
reported the whole set as "Alternate page with proper canonical tag" and
indexed nothing extra. 01_static.js still guards against that specifically.

hreflang goes only where the alternates are genuinely separate documents with
their own self-referencing canonicals. Three sets qualify:

  /            <-> /<lang>/          pre-rendered by build_landing.py
  /guides/     <-> /guides/<lang>/   pre-rendered by build_guides.py

The guides emit their own tags; this script emits the landing cluster on "/"
and puts every URL in the sitemap.

Study Stats and Share have no per-language documents, so they still declare
none — they localize at runtime for the reader, which helps nobody's index.
"""
import datetime
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides_i18n import GUIDE_TEXT  # noqa: E402
import build_guides  # noqa: E402
import build_landing  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://jwsync.org"
TODAY = datetime.date.today().isoformat()

LANGS = ["en", "es", "pt", "fr", "de", "it", "ru", "ja", "ko", "tl", "sv", "ceb", "ar", "he"]
LOCALE = {
    "en": "en_US", "es": "es_ES", "pt": "pt_BR", "fr": "fr_FR", "de": "de_DE",
    "it": "it_IT", "ru": "ru_RU", "ja": "ja_JP", "ko": "ko_KR", "tl": "tl_PH",
    "sv": "sv_SE", "ceb": "ceb_PH", "ar": "ar_SA", "he": "he_IL",
}
GUIDE_LANGS = sorted(set(GUIDE_TEXT) | {"en"})

# Pages whose language is selected by the ?lang= query parameter.
QUERY_PAGES = [
    # The asset server 307s /foo.html -> /foo, so canonicals and sitemap
    # entries must use the extensionless form or they submit a redirect.
    ("index.html", SITE + "/", "1.0", "weekly"),
    ("highlights.html", SITE + "/highlights", "0.7", "monthly"),
    ("share.html", SITE + "/share", "0.7", "monthly"),
]
# Pages with no i18n of their own.
STATIC_PAGES = [
    ("forum.html", SITE + "/forum", "0.5", "weekly"),
]


def marker(name, body):
    return "<!-- SEO:%s -->\n%s\n<!-- /SEO:%s -->" % (name, body, name)


def splice(text, name, body, anchor):
    """Insert or replace a marked block, anchoring it after `anchor`."""
    block = marker(name, body)
    pat = re.compile(r"<!-- SEO:%s -->.*?<!-- /SEO:%s -->" % (name, name), re.S)
    if pat.search(text):
        return pat.sub(lambda m: block, text, count=1)
    if text.count(anchor) != 1:
        sys.exit("ABORT: anchor %r appears %d times" % (anchor[:60], text.count(anchor)))
    return text.replace(anchor, anchor + "\n" + block, 1)


def query_url(base, lang):
    if lang == "en":
        return base
    sep = "&" if "?" in base else "?"
    return "%s%slang=%s" % (base, sep, lang)


def hreflang_block(url_for, langs, indent="    "):
    lines = ['<link rel="alternate" hreflang="x-default" href="%s">' % url_for("en")]
    for l in langs:
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (l, url_for(l)))
    return "\n".join(indent + x for x in lines)


def og_locale_block(langs, indent="    "):
    lines = ['<meta property="og:locale" content="%s">' % LOCALE["en"]]
    for l in langs:
        if l != "en":
            lines.append('<meta property="og:locale:alternate" content="%s">' % LOCALE[l])
    return "\n".join(indent + x for x in lines)


# ── 1. <head> tags ────────────────────────────────────────────────────────
def patch_page(rel, canonical, langs, set_canonical=True, hreflang=None):
    """Set the canonical, the hreflang cluster and the og:locale run.

    set_canonical=False leaves an existing canonical alone, for pages that
    legitimately point somewhere other than `canonical`.
    hreflang=<fn(lang)->url> emits a cluster; None emits none. Pass it only
    for pages whose alternates are real separate documents — see the module
    docstring.
    """
    path = os.path.join(REPO, rel)
    c = io.open(path, encoding="utf-8").read()
    orig = c

    canon_tag = '<link rel="canonical" href="%s">' % canonical
    if set_canonical and canon_tag not in c:
        c = re.sub(r'<link rel="canonical" href="[^"]*">', canon_tag, c) \
            if '<link rel="canonical"' in c else \
            c.replace("</head>", canon_tag + "\n</head>", 1)
    if not set_canonical:
        # Anchor the og:locale block on whatever canonical the page already has.
        m = re.search(r'<link rel="canonical" href="[^"]*">', c)
        if m:
            canon_tag = m.group(0)

    # Rebuild the cluster from scratch so a stale one can never survive.
    c = re.sub(r'\n?<!-- SEO:hreflang -->.*?<!-- /SEO:hreflang -->', "", c, flags=re.S)
    c = re.sub(r'\n?\s*<link rel="alternate" hreflang="[a-z-]+"[^>]*>', "", c)
    if hreflang:
        c = c.replace(canon_tag,
                      canon_tag + "\n" + marker("hreflang", hreflang_block(hreflang, langs)),
                      1)

    # Rebuild the og:locale run from scratch: drop every previously generated
    # block and any hand-written tags, then emit exactly one. Stripping the
    # tags but leaving the markers used to hand splice() an empty block to
    # match, so pages with no og:type (highlights, share) grew one more empty
    # marker pair on every run.
    c = re.sub(r'\n?<!-- SEO:oglocale -->.*?<!-- /SEO:oglocale -->', "", c, flags=re.S)
    c = re.sub(r'\n?\s*<meta property="og:locale(?::alternate)?" content="[^"]*">', "", c)
    block = marker("oglocale", og_locale_block(langs))
    og_anchor = '<meta property="og:type"'
    if og_anchor in c:
        line_end = c.index(">", c.index(og_anchor)) + 1
        c = c[:line_end] + "\n" + block + c[line_end:]
    else:
        if c.count(canon_tag) != 1:
            sys.exit("ABORT %s: canonical anchor x%d" % (rel, c.count(canon_tag)))
        c = c.replace(canon_tag, canon_tag + "\n" + block, 1)

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("  head:", rel)
    else:
        print("  head: %s (unchanged)" % rel)


# ── 2. localized <title> / <meta description> ─────────────────────────────
TITLE_HOOK = """    var mt=T.meta_title||TL.meta_title,md=T.meta_desc||TL.meta_desc;
    if(mt)document.title=mt;
    var dm=document.querySelector('meta[name="description"]');
    if(dm&&md)dm.setAttribute('content',md);"""


def patch_landing_meta(rel):
    """Seed meta_title / meta_desc into __JW_LANDING_I18N and swap them at runtime.

    The strings are derived from hero_title / hero_desc, which are already
    translated into all 13 languages and read well as a title tag and a meta
    description — so every language gets localized metadata without new copy
    being written (or machine-translated) per language.
    """
    path = os.path.join(REPO, rel)
    c = io.open(path, encoding="utf-8").read()
    m = re.search(r"__JW_LANDING_I18N *= *", c)
    ts = m.end()
    d = 0
    for i in range(ts, len(c)):
        if c[i] == "{":
            d += 1
        elif c[i] == "}":
            d -= 1
            if d == 0:
                e = i + 1
                break
    obj = json.loads(c[ts:e])
    added = 0
    for lang, t in obj.items():
        if "meta_title" not in t:
            t["meta_title"] = "JW Sync — " + t["hero_title"]
            added += 1
        if "meta_desc" not in t:
            t["meta_desc"] = t["hero_desc"]
    c = c[:ts] + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + c[e:]

    hook_anchor = "    var TL=L[lang]||L['en']||{};"
    if TITLE_HOOK.strip() not in c:
        if c.count(hook_anchor) != 1:
            sys.exit("ABORT %s: title-hook anchor x%d" % (rel, c.count(hook_anchor)))
        c = c.replace(hook_anchor, hook_anchor + "\n" + TITLE_HOOK, 1)

    io.open(path, "w", encoding="utf-8").write(c)
    print("  meta: %s (+%d meta_title keys)" % (rel, added))


# ── 3. JSON-LD inLanguage ─────────────────────────────────────────────────
def patch_jsonld_languages(rel):
    """Keep the Schema.org inLanguage array in step with LANGS.

    It had drifted: "sv" was never added when Swedish shipped, so the array
    listed 11 of the 12 languages the site actually served.
    """
    path = os.path.join(REPO, rel)
    c = io.open(path, encoding="utf-8").read()
    want = '"inLanguage": %s' % json.dumps(LANGS)
    new_c = re.sub(r'"inLanguage": \[[^\]]*\]', lambda m: want, c)
    if new_c != c:
        io.open(path, "w", encoding="utf-8").write(new_c)
        print("  jsonld:", rel)
    else:
        print("  jsonld: %s (unchanged)" % rel)


# ── 4. sitemap ────────────────────────────────────────────────────────────
def url_entry(loc, alts, priority, changefreq, lastmod=TODAY):
    out = ["  <url>", "    <loc>%s</loc>" % loc]
    if alts:
        out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>'
                   % alts["en"])
        for l, href in alts.items():
            out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (l, href))
    out += ["    <lastmod>%s</lastmod>" % lastmod,
            "    <changefreq>%s</changefreq>" % changefreq,
            "    <priority>%s</priority>" % priority,
            "  </url>"]
    return "\n".join(out)


def build_sitemap():
    blocks = []
    # The landing page and its pre-rendered per-language twins form one
    # cluster. Still no ?lang= variants anywhere: those canonicalise back to
    # the page they came from, so submitting them only produces duplicates.
    landing_alts = {l: build_landing.page_url(l) for l in LANGS}
    for l in LANGS:
        blocks.append(url_entry(build_landing.page_url(l), landing_alts, "1.0", "weekly"))
    for _rel, canonical, prio, freq in QUERY_PAGES[1:] + STATIC_PAGES:
        blocks.append(url_entry(canonical, None, prio, freq))

    # Guides: the index plus every slug, once per translated language.
    guide_targets = [None] + [g["slug"] for g in build_guides.GUIDES]
    for slug in guide_targets:
        alts = {l: build_guides.guide_url(slug, l) for l in GUIDE_LANGS}
        prio = "0.8" if slug is None else "0.7"
        for l in GUIDE_LANGS:
            blocks.append(url_entry(build_guides.guide_url(slug, l), alts, prio, "monthly"))

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(blocks) + "\n</urlset>\n")
    io.open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    print("  sitemap.xml: %d urls" % len(blocks))


def main():
    print("head tags:")
    for rel, canonical, _p, _f in QUERY_PAGES:
        # Only the landing page has per-language twins to point at.
        patch_page(rel, canonical, LANGS,
                   hreflang=(build_landing.page_url if rel == "index.html" else None))
        beta = os.path.join("beta", rel)
        if not os.path.exists(os.path.join(REPO, beta)):
            continue
        # The beta shell has its own canonical (https://jwsync.org/beta/) and
        # must keep it — handing it the production URL gave it two conflicting
        # canonical tags. The satellite twins have no canonical of their own
        # and must stay byte-identical to production for 15_parity.js, so they
        # take the production URL, which is also the right signal for a
        # noindex staging copy.
        patch_page(beta, canonical, LANGS,
                   set_canonical=(rel != "index.html"))
    for rel, canonical, _p, _f in STATIC_PAGES:
        patch_page(rel, canonical, ["en"])

    print("localized metadata:")
    for rel in ("index.html", os.path.join("beta", "index.html")):
        patch_landing_meta(rel)

    print("json-ld languages:")
    for rel in ("index.html", os.path.join("beta", "index.html")):
        patch_jsonld_languages(rel)

    print("sitemap:")
    build_sitemap()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_landing.py — pre-rendered landing pages, one per language.

Why this exists
---------------
jwsync.org/ is a single 700 KB document with client-side i18n. A ?lang=xx URL
serves byte-identical English HTML that canonicalises back to "/", so Google
collapses the whole set and indexes nothing extra — Search Console reported it
as "Alternate page with proper canonical tag", which is why the hreflang
cluster over those URLs was removed and 01_static.js guards against it.

The only real fix is documents that genuinely differ. This generates one at
/<lang>/ for each non-English language: the copy is baked into the HTML, the
canonical points at itself, and the hreflang cluster links the set together.
English keeps "/" — its URL and its rankings are untouched.

These are not doorway pages. Each carries the hero, five feature cards, six
tool cards, the four-step walkthrough and five FAQ entries — the same
substance as the app's own landing view, and more text than the guide pages
that already index fine. Every string is pulled from copy that is already
translated and reviewed:

  __JW_LANDING_I18N  (index.html)  hero, features, tool cards
  TRANSLATIONS       (js/app.js)   walkthrough steps, FAQ, privacy badge
  landing_chrome.json              five section headings + the attribution

so no page invents wording for a language nobody has read.

Run from the repo root:  python3 scripts/build_landing.py
"""
import html
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_data")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n_tool as t  # noqa: E402

SITE = "https://jwsync.org"
LANGS = ["en", "es", "pt", "fr", "de", "it", "ru", "ja", "ko", "tl", "sv", "ceb", "ar", "he"]
RTL_LANGS = {"ar", "he"}
# Derived, not hand-listed: a language gets a /guides/<lang>/ link the moment
# its translations land in guides_i18n.GUIDE_TEXT, and never before — so this
# can neither lag behind a new language nor link at a tree that is not built.
from guides_i18n import GUIDE_TEXT  # noqa: E402
GUIDE_LANGS = set(GUIDE_TEXT) | {"en"}

LANG_NAME = {
    "en": "English", "es": "Español", "pt": "Português", "fr": "Français",
    "de": "Deutsch", "it": "Italiano", "ru": "Русский", "ja": "日本語",
    "ko": "한국어", "tl": "Filipino", "sv": "Svenska", "ceb": "Cebuano",
    "ar": "العربية", "he": "עברית",
}
LOCALE = {
    "en": "en_US", "es": "es_ES", "pt": "pt_BR", "fr": "fr_FR", "de": "de_DE",
    "it": "it_IT", "ru": "ru_RU", "ja": "ja_JP", "ko": "ko_KR", "tl": "tl_PH",
    "sv": "sv_SE", "ceb": "ceb_PH", "ar": "ar_SA", "he": "he_IL",
}

TOOLS = [
    ("merge", "", "/"),
    ("explorer", "", "/"),
    ("stats", "", "/highlights"),
    ("share", "", "/share"),
    ("doctor", "", "/"),
    ("reading", "", "/"),
]
FEATURES = ["local", "tags", "date", "browse", "review"]


def esc(s):
    return html.escape(str(s), quote=True)


# ── Source dictionaries ───────────────────────────────────────────────────
def load_landing():
    c = io.open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
    m = re.search(r"__JW_LANDING_I18N *= *", c)
    ts = m.end()
    d = 0
    for i in range(ts, len(c)):
        if c[i] == "{":
            d += 1
        elif c[i] == "}":
            d -= 1
            if d == 0:
                return json.loads(c[ts:i + 1])
    raise ValueError("__JW_LANDING_I18N not found")


def load_app():
    a = io.open(os.path.join(REPO, "js", "app.js"), encoding="utf-8").read()
    site = t.dict_sites(a)[0]
    return {l: t.js_to_obj(t.read_lang(a, site, l)[0]) for l in LANGS}


CSS = """
:root{--bg:#040f22;--card:rgba(15,28,52,.6);--line:rgba(71,85,105,.35);--txt:#e2e8f0;
--muted:#94a3b8;--accent:#ea580c;--accent-strong:#c2410c;--accent-soft:#fb923c;
--green:#22c55e}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);
font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
-webkit-font-smoothing:antialiased}
a{color:var(--accent-soft);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:900px;margin:0 auto;padding:0 20px}
header.site{border-bottom:1px solid var(--line);padding:14px 0}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;
flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;color:var(--txt);font-weight:700;font-size:17px}
.brand:hover{text-decoration:none}
.brand .dot{width:26px;height:26px;border-radius:7px;background:var(--accent);
display:inline-flex;align-items:center;justify-content:center;color:#fff;font-size:13px;
font-weight:800}
.hnav{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.hnav a{color:var(--muted);font-size:14px}
.lp-lang{background:transparent;border:1px solid var(--line);color:var(--muted);
font-size:13px;padding:4px 8px;border-radius:8px;font-family:inherit;max-width:160px}
.lp-lang:hover{border-color:var(--accent)}
.hero{padding:54px 0 12px}
h1{font-size:38px;line-height:1.18;margin:0 0 14px;letter-spacing:-.015em}
.lede{color:var(--muted);font-size:17px;margin:0 0 26px;max-width:660px}
.cta-row{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.btn{display:inline-block;background:var(--accent-strong);color:#fff;font-weight:600;
font-size:15.5px;padding:12px 26px;border-radius:10px;box-shadow:0 1px 5px rgba(0,0,0,.35)}
.btn:hover{text-decoration:none;filter:brightness(1.07)}
.btn-ghost{background:transparent;border:1px solid var(--line);color:var(--txt);font-weight:600;
font-size:15px;padding:11px 22px;border-radius:10px;display:inline-block}
.btn-ghost:hover{text-decoration:none;border-color:var(--accent)}
.privacy{display:inline-flex;align-items:center;gap:8px;margin:24px 0 0;padding:6px 12px;
border-radius:9px;font-size:12.5px;font-weight:600;color:#6ee7a8;
background:rgba(16,30,23,.7);border:1px solid rgba(52,211,153,.16)}
.privacy .dot{width:6px;height:6px;border-radius:50%;background:var(--green)}
h2{font-size:23px;margin:52px 0 14px;letter-spacing:-.01em}
.grid{display:grid;grid-template-columns:1fr;gap:14px;margin:0;padding:0;list-style:none}
@media(min-width:700px){.grid{grid-template-columns:1fr 1fr}}
.grid li{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:18px 20px}
.grid strong{display:block;font-size:16px;margin-bottom:5px}
.grid span{color:var(--muted);font-size:14.5px;display:block}
.tags{margin:11px 0 0;padding:0;list-style:none;display:flex;gap:7px;flex-wrap:wrap}
.tags li{background:rgba(234,88,12,.1);border:1px solid rgba(234,88,12,.25);color:var(--accent-soft);
font-size:12px;padding:3px 9px;border-radius:20px}
ol.steps{counter-reset:s;list-style:none;margin:0;padding:0}
ol.steps li{counter-increment:s;position:relative;padding:0 0 22px 54px}
ol.steps li::before{content:counter(s);position:absolute;left:0;top:1px;width:33px;height:33px;
border-radius:50%;background:var(--accent-strong);color:#fff;font-weight:700;font-size:15px;
display:flex;align-items:center;justify-content:center}
ol.steps h3{margin:0 0 5px;font-size:16.5px}
ol.steps p{margin:0;color:var(--muted);font-size:15px}
.faq dt{font-weight:600;margin:20px 0 5px;font-size:16px}
.faq dd{margin:0;color:var(--muted);font-size:15px}
.cta-card{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;
padding:22px 24px;margin:38px 0 0}
.cta-card strong{display:block;font-size:17px;margin-bottom:5px}
.cta-card span{color:var(--muted);font-size:14.5px}
.lp-guides{margin:44px 0 0}
.lp-guides h2{margin:0 0 14px}
.lp-gcards{display:grid;grid-template-columns:1fr;gap:12px;margin:0 0 22px;padding:0;list-style:none}
@media(min-width:640px){.lp-gcards{grid-template-columns:1fr 1fr}}
.lp-gcards a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px 18px;color:var(--txt);height:100%}
.lp-gcards a:hover{text-decoration:none;border-color:var(--accent)}
.lp-gcards strong{display:block;font-size:15.5px;margin-bottom:4px}
.lp-gcards span{color:var(--muted);font-size:13.5px;line-height:1.55;display:block}
footer.site{border-top:1px solid var(--line);margin-top:58px;padding:26px 0 44px;
color:#8b99ad;font-size:12.5px}
footer.site p{margin:0 0 10px}
""".strip()

RTL_CSS = """<style>
body{direction:rtl}
ol.steps li{padding:0 54px 22px 0}
ol.steps li::before{left:auto;right:0}
.lp-lang{max-width:170px}
</style>"""


def page_url(lang):
    return SITE + "/" if lang == "en" else "%s/%s/" % (SITE, lang)


def guides_url(lang):
    """Guides live at /guides/<lang>/ only where that language is translated;
    everyone else is sent to the English tree rather than a 404."""
    if lang == "en" or lang not in GUIDE_LANGS:
        return "/guides/"
    return "/guides/%s/" % lang


def alternates():
    out = ['<link rel="alternate" hreflang="x-default" href="%s">' % page_url("en")]
    for l in LANGS:
        out.append('<link rel="alternate" hreflang="%s" href="%s">' % (l, page_url(l)))
    return "\n".join(out)


def lang_picker(lang):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (page_url(l), " selected" if l == lang else "", esc(LANG_NAME[l]))
        for l in LANGS)
    return ('<select class="lp-lang" aria-label="%s" onchange="location.href=this.value">%s</select>'
            % (esc(LANG_NAME[lang]), opts))


_VERSION_RE = re.compile(r'"softwareVersion"\s*:\s*"([0-9.]+)"')


def app_version():
    """Read softwareVersion off the English page so the two can never diverge."""
    c = io.open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
    m = _VERSION_RE.search(c)
    if not m:
        sys.exit("build_landing: no softwareVersion in index.html")
    return m.group(1)


# Guides worth a direct link from the landing page. Slugs are English keys and
# are the same in every language; GUIDE_TEXT supplies the localized wording.
POPULAR_GUIDES = [
    "merge-jw-library-backups",
    "transfer-jw-library-notes-new-phone",
    "backup-jw-library",
    "jw-library-android-to-iphone",
    "sync-jw-library-multiple-devices",
    "jw-library-notes-missing-after-update",
    "recover-jw-library-notes-lost-phone",
    "fix-corrupted-jw-library-backup",
    "export-jw-library-notes",
    "share-jw-library-notes",
    "organize-jw-library-tags",
    "jw-library-windows-pc",
]


def popular_guides(lang, C):
    """A grid of guide links, so the landing page is not a dead end.

    Before this the page linked five URLs and not one guide: all 37 sat behind
    a single hub link, two clicks from the only page in the cluster with
    external links pointing at it. Titles come from that language's own
    GUIDE_TEXT, so the anchor text matches the guide it points at.
    """
    txt = GUIDE_TEXT.get(lang)
    if not txt:
        return ""
    items = []
    for slug in POPULAR_GUIDES:
        g = txt.get(slug)
        if not g:
            sys.exit("build_landing: %s missing guide %r" % (lang, slug))
        items.append('<li><a href="/guides/%s/%s"><strong>%s</strong>'
                     '<span>%s</span></a></li>'
                     % (lang, slug, esc(g["title"]), esc(g["description"])))
    return ('<section class="lp-guides"><h2>%s</h2><ul class="lp-gcards">%s</ul></section>'
            % (esc(C["lp_popular"]), "".join(items)))


def jsonld(lang, L, A):
    return {
        "@context": "https://schema.org",
        "@graph": [
            # Must stay the same @type, and carry the same trust properties, as
            # the English node in index.html. Google consolidates an entity
            # across a hreflang cluster; when "/" declared WebApplication and
            # every /<lang>/ declared a barer SoftwareApplication, the cluster
            # described two different things and the localized nodes were the
            # weaker of the two.
            {
                "@type": "WebApplication",
                "name": "JW Sync",
                "applicationCategory": "UtilityApplication",
                "operatingSystem": "Web Browser",
                "browserRequirements": "Requires modern web browser with JavaScript enabled",
                "url": page_url(lang),
                "inLanguage": lang,
                "description": L["hero_desc"],
                "isAccessibleForFree": True,
                "softwareVersion": app_version(),
                "image": SITE + "/og-image.png",
                "screenshot": SITE + "/og-image.png",
                "downloadUrl": page_url(lang),
                "author": {"@type": "Organization", "name": "JW Sync", "url": SITE + "/"},
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            {
                "@type": "FAQPage",
                "inLanguage": lang,
                "mainEntity": [
                    {"@type": "Question", "name": A["faq_q%d" % i],
                     "acceptedAnswer": {"@type": "Answer", "text": A["faq_a%d" % i]}}
                    for i in range(1, 6)
                ],
            },
        ],
    }


def build(lang, landing, app, chrome):
    L, A, C = landing[lang], app[lang], chrome[lang]
    url = page_url(lang)
    d = ' dir="rtl"' if lang in RTL_LANGS else ""
    app_href = "/" if lang == "en" else "/?lang=%s" % lang
    # highlights/share/forum read ?lang=, so a localized landing page has to
    # carry its language across instead of dropping the reader into English.
    # Internal links only — never hreflang or sitemap (see 01_static.js).
    q = "" if lang == "en" else "?lang=%s" % lang
    p = []
    p.append(f"""<!DOCTYPE html>
<html lang="{lang}"{d}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(L["meta_title"])}</title>
<meta name="description" content="{esc(L["meta_desc"])}">
<link rel="canonical" href="{url}">
{alternates()}
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#040f22">
<link rel="icon" href="/favicon.ico">
<meta property="og:site_name" content="JW Sync">
<meta property="og:type" content="website">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:title" content="{esc(L["meta_title"])}">
<meta property="og:description" content="{esc(L["meta_desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(jsonld(lang, L, A), ensure_ascii=False)}</script>
<style>{CSS}</style>
{RTL_CSS if lang in RTL_LANGS else ""}
</head>
<body>""")

    # header
    p.append('<header class="site"><div class="wrap">'
             f'<a class="brand" href="{app_href}"><span class="dot">JW</span>JW Sync</a>'
             '<nav class="hnav">'
             f'<a href="{app_href}">{esc(L["nav_home"])}</a>'
             f'<a href="{guides_url(lang)}">{esc(L["nav_guides"])}</a>'
             f'<a href="/highlights{q}">{esc(L["nav_stats"])}</a>'
             f'<a href="/share{q}">{esc(L["nav_sharing"])}</a>'
             f'<a href="/forum{q}">{esc(L["nav_community"])}</a>'
             f'{lang_picker(lang)}'
             '</nav></div></header>')

    p.append('<main class="wrap">')
    # hero
    p.append('<section class="hero">')
    p.append(f'<h1>{esc(L["hero_title"])}</h1>')
    p.append(f'<p class="lede">{esc(L["hero_desc"])}</p>')
    p.append('<div class="cta-row">'
             f'<a class="btn" href="{app_href}">{esc(L["cta_launch"])}</a>'
             f'<a class="btn-ghost" href="{app_href}">{esc(L["cta_try_demo"])}</a>'
             '</div>')
    p.append(f'<div class="privacy"><span class="dot"></span>{esc(A["privacy_badge"])}</div>')
    p.append('</section>')

    # features
    p.append(f'<h2>{esc(C["lp_features"])}</h2><ul class="grid">')
    for f in FEATURES:
        p.append(f'<li><strong>{esc(L["feat_%s_title" % f])}</strong>'
                 f'<span>{esc(L["feat_%s_desc" % f])}</span></li>')
    p.append("</ul>")

    # tools
    p.append(f'<h2>{esc(L["svc_heading"])}</h2><ul class="grid">')
    for key, _icon, href in TOOLS:
        href = href + q if href in ("/highlights", "/share") else href
        p.append(f'<li><strong>{esc(L["svc_%s_t" % key])}</strong>'
                 f'<span>{esc(L["svc_%s_d" % key])}</span>'
                 f'<ul class="tags"><li>{esc(L["svc_%s_g1" % key])}</li>'
                 f'<li>{esc(L["svc_%s_g2" % key])}</li></ul></li>')
    p.append("</ul>")

    # walkthrough
    p.append(f'<h2>{esc(C["lp_how"])}</h2><ol class="steps">')
    for i in range(1, 5):
        p.append(f'<li><h3>{esc(A["guide_step%d_title" % i])}</h3>'
                 f'<p>{esc(A["guide_step%d_body" % i])}</p></li>')
    p.append("</ol>")

    # faq
    p.append(f'<h2>{esc(C["lp_faq"])}</h2><dl class="faq">')
    for i in range(1, 6):
        p.append(f'<dt>{esc(A["faq_q%d" % i])}</dt><dd>{esc(A["faq_a%d" % i])}</dd>')
    p.append("</dl>")

    # guides
    p.append(popular_guides(lang, C))
    p.append(f'<a class="cta-card" href="{guides_url(lang)}">'
             f'<strong>{esc(C["lp_guides"])}</strong>'
             f'<span>{esc(C["lp_guides_d"])}</span></a>')
    p.append("</main>")

    p.append('<footer class="site"><div class="wrap">'
             f'<p>{esc(L["footer_tagline"])}</p>'
             f'<p>{esc(C["lp_disclaimer"])}</p>'
             '</div></footer>')
    p.append("</body>\n</html>\n")
    return "".join(p)


def main():
    landing = load_landing()
    app = load_app()
    chrome = json.load(io.open(os.path.join(DATA, "landing_chrome.json"), encoding="utf-8"))

    written = 0
    for lang in LANGS:
        if lang == "en":
            continue  # English stays at "/" — the existing app shell
        out = os.path.join(REPO, lang)
        os.makedirs(out, exist_ok=True)
        page = build(lang, landing, app, chrome)
        json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                             page, re.S).group(1))  # sanity: JSON-LD parses
        io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
        written += 1
    print("wrote %d localized landing pages (/%s/)"
          % (written, "/, /".join(l for l in LANGS if l != "en")))


if __name__ == "__main__":
    main()

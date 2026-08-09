# Adding a language

Everything below is regenerated from data — there is no step that requires
hand-editing a 690 KB HTML file.

## 1. UI strings

The site keeps its UI strings in ~30 object literals scattered across the HTML
files and the `js/` bundles. `i18n_tool.py` finds them all:

```bash
python3 scripts/i18n_tool.py list            # what it found
python3 scripts/i18n_tool.py extract en      # -> scripts/i18n_data/*.en.json
# translate each *.en.json to *.<lang>.json, same keys, same order
python3 scripts/i18n_tool.py inject <lang>   # splice them back in
python3 scripts/i18n_check.py <lang>         # every key covered?
```

Injection is idempotent — a table that already has the language is skipped.
Mirror `js/*` and the satellite pages to `beta/` afterwards; `15_parity.js`
enforces it.

`i18n_tool.py` finds `lang: { … }` objects only. Two string tables are flat
`lang: "string"` maps and are therefore invisible to it — patch them by hand:
the offline banner in both `index.html` files, and the `*.json` data files in
`i18n_data/` (`landing_chrome`, `navbar`, `forum`). Arabic was missing from the
offline banner for months because nothing looked.

## 2. Plumbing

There are **four** places outside the dictionaries that enumerate languages:
the `?lang=` allow-list, the nav `<select>`, `NAV_LANGS` in `js/app.js` (a
second, independent picker), and `reading.js`'s jw.org `wtlocale` map. Add the
new code to `V` in `add_rtl_wiring.py`'s snippet too.

Copy the newest plumbing script — `add_polish_plumbing.py` — not
`add_arabic_plumbing.py`, which predates `NAV_LANGS` and only covers three of
the four.

⚠️ Verify the `wtlocale` code against the live jw.org finder before using it.
jw.org serves English for any code it does not recognise, so a wrong value
fails completely silently. Hebrew shipped as `HB` (not a real code; the correct
one is `Q`) and served English for two releases.

## 3. Direction

Right-to-left languages go in the `R` set in `add_rtl_wiring.py`, then:

```bash
python3 scripts/add_rtl_wiring.py   # <head> bootstrap on every page
python3 scripts/build_rtl.py        # regenerate rtl.css
```

`build_rtl.py` mirrors every direction-sensitive rule in every stylesheet the
site ships. Re-run it after touching any CSS — `18_arabic_rtl.js` fails if
`rtl.css` is stale.

## 4. Guides

Add a `CHROME` entry in `guides_i18n.py` and a per-slug dict in a
`guides_<lang>.py` module, then:

```bash
python3 scripts/build_guides.py
```

English stays at `/guides/<slug>`; other languages go to
`/guides/<lang>/<slug>`, so existing URLs and rankings are untouched. A
language only enters the hreflang cluster once it appears in `GUIDE_TEXT` —
half-finished languages are never advertised.

## 5. SEO

```bash
python3 scripts/build_seo.py
```

Regenerates canonicals, `og:locale`, JSON-LD `inLanguage`, the localized
`<title>`/description seeds, and `sitemap.xml` from one `LANGS` list.

Note: the app shell deliberately has **no** `hreflang`. It is one document
with client-side i18n, so `?lang=xx` serves the same HTML canonicalising back
to `/`; alternates over those URLs index nothing. See the docstring in
`build_seo.py` and the canonical-hygiene section of `01_static.js`.

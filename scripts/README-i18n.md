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

## 2. Plumbing

`add_arabic_plumbing.py` shows the three places outside the dictionaries that
enumerate languages: the `?lang=` allow-list, the nav `<select>`, and
`reading.js`'s jw.org `wtlocale` map. Add the new code to `V` in
`add_rtl_wiring.py`'s snippet too.

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

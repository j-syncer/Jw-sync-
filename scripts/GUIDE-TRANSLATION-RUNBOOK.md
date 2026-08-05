# Guide translation runbook

Translating the 37 static guides into one more language. One language per
pass; each pass ends with a push to `main`.

**Status:** en ✅ · ar ✅ · es ✅ · pt ✅ · fr ✅ · de ✅ · it ✅ · ru ✅ · ja ✅ ·
ko ⬜ · tl ⬜ · sv ⬜ · ceb ⬜

## The pass

1. **Dump the English source** in batches of 6–7 guides so the working set
   stays small:
   ```bash
   python3 scripts/dump_guides.py 0 6        # indices are half-open
   ```
2. **Write `scripts/guides_<lang>.py`** defining `GUIDES_<LANG>`, appending one
   batch at a time. Structure must mirror the English record exactly:
   - keys: `title`, `h1`, `description`, `intro`, `steps`, `sections`, `faq`
   - `intro` is a list of strings; `steps`/`sections`/`faq` are lists of
     **2-tuples**
   - same number of entries per field as English (the checker enforces this)
   - `slug` and `group` are NOT translated — they stay English keys
3. **Add `CHROME["<lang>"]`** to `scripts/guides_i18n.py` (all 25 keys plus the
   5-entry `groups` map), and register the module:
   ```python
   from guides_<lang> import GUIDES_<LANG>
   GUIDE_TEXT = {..., "<lang>": GUIDES_<LANG>}
   ```
4. **Check structure and leakage:**
   ```bash
   python3 scripts/check_guide_lang.py <lang>
   ```
5. **Build:**
   ```bash
   python3 scripts/build_guides.py && python3 scripts/build_landing.py \
     && python3 scripts/build_seo.py && python3 scripts/build_rtl.py
   ```
   `build_landing.py` derives the `/guides/<lang>/` link from
   `GUIDE_TEXT`, so the landing page rewires itself. A language that is not
   in `GUIDE_TEXT` is never linked or put in the sitemap — half-finished work
   is invisible to readers and to Google.
6. **Test:** `cd tests && npm test` (must exit 0).
7. **Ship:** bump `softwareVersion` in `index.html` + `beta/index.html`, bump
   `CACHE_VERSION` in `service-worker.js`, add a `CHANGELOG.md` entry, commit,
   `git push -u origin main`.

## Notes

- Minor version bump per language (3.1.0 = es, 3.2.0 = pt, …).
- English guide URLs and canonicals must never change — they already rank.
- Terminology is per-language and should stay consistent across all 37 guides;
  the glossary each language settled on is at the top of its
  `scripts/guides_<lang>.py`.

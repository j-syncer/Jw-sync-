# JW Sync — Claude Instructions

## ⚠️ Read This First — Default Behaviour

**Every change goes to `beta/index.html` and is committed + pushed to the `main` git branch.**
Do this automatically for any request. No need to ask, no feature branches.

| Trigger | Action |
|---------|--------|
| Any normal request | Edit `beta/index.html` → commit → `git push origin main` |
| "go live" / "push to production" / "ship it" | Copy the same changes into `index.html` → commit → `git push origin main` |

**Never touch `index.html` unless the user explicitly says "go live" or "push to production".**

| File | Live URL | Edit when |
|------|----------|-----------|
| `beta/index.html` | jwsync.org/beta | Every change, by default |
| `index.html` | jwsync.org | Only on explicit "go live" |

### ⚠️ Shared files ship to BOTH sites in lockstep
The satellite pages and the tool-layer scripts are NOT beta-first — they must
stay identical between the two sites. **Any edit to one copy must be applied to
the other copy in the same commit:**
`highlights.html`, `share.html`, `styles.css`, and everything in `js/`
(each has a twin under `beta/`). `js/enhancements.js` is the one exception:
its service-worker registration line legitimately differs (scope `/` vs
`/beta/`). Test suite `15_parity.js` fails the build if the copies drift —
this rule exists because the Awards tab once shipped to production only and
was missing from beta for days.

### Git rules
- Branch is **always `main`** — never create feature branches unless explicitly asked
- Always `git push origin main` after every commit
- Never ask the user about branching; it never needs to come up

### Changelog rule
**Every time a user-facing feature is added or changed, update `CHANGELOG.md`** with:
- A new `## [x.y.z] — YYYY-MM-DD` section at the top (bump the minor version for new features, patch for fixes)
- Bullet points describing what changed from the user's perspective
- Also update: `softwareVersion` in the Schema.org JSON-LD block in both `beta/index.html` and `index.html`, and the feature cards / hero copy on the landing page if the feature warrants it.

---

## ⚠️ Tests — when the user says "run tests" / "run the tests"

The test suite lives in `tests/`. **Always run it as a single command** (no need to ask which suite):

```bash
cd tests && npm install --silent 2>/dev/null; npm test
```

- `npm install` is idempotent — skip the wait if `tests/node_modules` already exists, but it's safe to run every time.
- `npm test` chains all 19 suites (`01_static.js` … `19_landing_pages.js`) and exits non-zero on the first failure.
- Individual suites are available too: `npm run test:static`, `:runtime`, `:regression`, `:lazy`, `:post-merge`, `:conflict`, `:wrapped`, `:preview`, `:sync`, `:mobile`, `:semantic`, `:share`, `:receive`, `:doctor`, `:parity`, `:reading`, `:guides`, `:arabic`, `:landing`.

**Run the tests proactively before pushing any feature that touches `beta/index.html`, `index.html`, the Browse module, or `service-worker.js`.** If a suite fails, fix it before committing — do not push a broken build.

Suite coverage:
- **01_static.js** — both index.html files parse, TRANSLATIONS object is well-formed across every language in `EXPECTED_LANGS`, Browse i18n covers every required key, every CSS class referenced is defined, all hook/marker strings present, canonical/hreflang hygiene.
- **02_runtime.js** — synthesises a `.jwlibrary` in-memory (zipped SQLite with the JW Library schema), boots the Browse module in JSDOM, drives every UI affordance (tab switching, color/tag/publication filters, search, sort, detail panes for notes/highlights/bookmarks, copy-to-clipboard, clear-all, close).
- **03_regression.js** — merge worker still parses, every critical merge anchor is intact, HTML structure clean (one structural `</body>`/`</html>` outside scripts), cache version is set.
- **04_lazy_load.js** — lazy-loading / code-splitting of the heavy modules.
- **05_post_merge.js** — post-merge flows (celebration screen, downloads, hand-offs).
- **06_conflict_review.js** — merge conflict review UI.
- **07_library_wrapped.js** — Study Stats page (highlights.html) end-to-end.
- **08_pre_merge_preview.js** — pre-merge preview card.
- **09_scheduled_sync.js** — sync reminder scheduling.
- **10_mobile_polish.js** — mobile-specific affordances.
- **11_semantic_search.js** — semantic worker + Browse "Ask" integration.
- **12_share_page.js** — share.html note-sharing page.
- **13_receive_merge.js** — receive/adopt shared notes into a backup.
- **14_backup_doctor.js** — Library Doctor scan/fix, standalone and inside the merge engine.
- **15_parity.js** — beta/production drift guard: shared-file pairs identical, `enhancements.js` differs only by SW registration, and `CACHE_VERSION` bumped whenever a precached page changes (checks both working tree and git history).
- **16_reading.js** — Reading Companion: plan data (1,189 chapters both orders), engine (portions, self-healing carry-over, streaks, forecast, milestones), i18n coverage, JSDOM UI, notes integration — **and the jw.org wtlocale table** (see the language runbook below).
- **17_guides.js** — the 37 static guides in every language: structure, canonicals, cross-links.
- **18_arabic_rtl.js** — RTL guard: dictionary coverage, `?lang=` allow-list, nav picker, wtlocale presence, `dir="rtl"` applied before first paint, `rtl.css` not stale.
- **19_landing_pages.js** — the pre-rendered `/<lang>/` landing pages: they exist with correct `lang`/`dir`, are self-canonical with a reciprocal hreflang cluster, serve real translated copy (not JS-filled), carry substantive content, and are in the sitemap.

If you add a new user-facing feature, extend the relevant suite to cover it.

### ⚠️ When a guard fails on a new language, fix the guard — don't narrow it

Three languages in a row each exposed a check that had been quietly *shrunk to
keep passing* instead of repaired, so the thing it was supposed to protect went
unprotected for months:

| Guard | How it had been narrowed | Real fix |
|-------|--------------------------|----------|
| `i18n_check.py` coverage | `i18n_tool.FILES` still described the pre-v3.8.0 layout, so it checked **8 of 20** tables | list every file holding a dictionary |
| `16_reading.js` i18n | regex assumed pretty-printed `en: {`, so it could not see the compact blocks `i18n_tool.py` splices in — Arabic was dropped from its language list rather than the regex fixed | brace-match instead of pattern-match |
| `10_mobile_polish.js` offline | language list left at 12 because the offline banner had no Arabic | add the missing translations |
| `19_landing_pages.js` copy | compared raw dictionary text to HTML the builder escapes; broke on Ukrainian's apostrophe (`Об'єднуйте` ships as `Об&#x27;єднуйте`) | compare against the escaped form |
| various `LANGS` lists | drifted to 12 or 13 while the site had more | keep at the full set |

The tell is always the same: a check fails on a correct page, and the quickest
way to green is to make the check ask for less. Resist it — that is how Arabic
ended up unverified in four places. **A guard that fails on a new language is
usually right that something is wrong; it is just wrong about what.**

Chinese made the same point in a new shape. A language key is written `en:`
while the tag is a bare JS identifier and `"zh-Hans":` once it is not — a
BCP-47 tag with a script subtag contains a hyphen and cannot be an unquoted
key — and `\b` never matches before a quote. Nine regexes across five suites
therefore reported perfectly good pages as missing the language:

| Guard | What it could not see |
|-------|-----------------------|
| `01_static.js` ×7 | `'\\b' + lang + ':'` — celebration, donate, switcher, wizard, SHARE_I18N, SAFE_I18N, DOC_I18N |
| `09`, `10` | the same shape inline |
| `19_landing_pages.js` | `hreflang="[a-z-]+"` cannot match a title-case script subtag |

The fix in `01_static.js` is one `KEY(lang)` helper every coverage regex now
builds its key fragment from, so the *next* tag shape widens the guards once
instead of dropping a language out of each of them.

---

## Codebase Overview

- **React SPA, no build system** — edit the HTML and `js/*.js` files directly with
  Python string replacements. Files are large; use Python `str.replace()` for all
  edits, never the Edit tool.
- `styles.css` / `beta/styles.css` exist but the HTML files also have embedded `<style>` blocks

### ⚠️ Where the JavaScript lives (changed in v3.8.0)

`beta/index.html` used to carry ~550 KB of inline `<script>`. That inline weight
was the cause of a 4.7 s First Contentful Paint: the bytes rode in the HTML
document at the browser's highest priority and starved the render-blocking CSS.
Nine modules now live in `js/` instead. **Do not move feature code back inline.**

| File | Loaded | Entry point |
|------|--------|-------------|
| `js/app.js` | lazily, by `bootApp()` | `window.__bootApp()` |
| `js/browse.js` | lazily, by `bootBrowse()` | `window.__bootBrowse()` → `__openJwBrowse` |
| `js/demo.js` | `<script defer>` | `window.__jwOpenDemo` |
| `js/conflict-review.js` | `<script defer>` | `window.__jwConflictReview` |
| `js/impact-preview.js` | `<script defer>` | `window.__jwImpactPreview` |
| `js/post-merge.js` | `<script defer>` | `window.__jwOpenGuide` |
| `js/sync-hub.js` | `<script defer>` | `window.__jwOpenSyncHub` |
| `js/receive.js` | `<script defer>` | `window.__jwReceive*` |
| `js/wizard.js` | `<script defer>` | `window.__jwOpenWizard` |
| `js/doctor.js` | `<script defer>` | `window.__openJwDoctor` |

The HTML keeps each module's `<!-- ── Name ── -->` marker comments and its
`<style>` block — several suites still locate features by those markers.

When a test needs to search "everything this page ships", use the helpers rather
than reading the HTML directly:

- `tests/helpers/page-source.js` — `withModules(page)` for feature-presence
  checks, `inlineModules(html, page)` to give JSDOM the page a browser sees
- `tests/helpers/browse-source.js` — `browseJs` / `browseCss` / `browseBlock`

Structural assertions ("must NOT be inline", script-tag shape) must keep reading
the page itself, or they will pass against the module file.
- `loadPrefs()` / `savePrefs({key:val})` — localStorage persistence via key `jwsync_prefs_v1`
- Language preference stored separately via key `jwsync_lang`

---

## Key Variables (minified names)

| Variable | Meaning |
|----------|---------|
| `be` | Simple Mode state (bool) — `true` = Simple Mode |
| `na` | Setter for Simple Mode (`useState` setter) |
| `d` | Current language code (e.g. `"en"`, `"tl"`) |
| `m` | Setter for language |
| `TRANSLATIONS` | Object keyed by lang code, each containing ~100 UI string keys |

---

## Design Principles (always apply)

- **Single accent color** — orange (`#ea580c`) is the brand color. Blue (`#1d4ed8`) is used only for the Full Mode toggle indicator. Never introduce a third competing accent.
- **No animated gradients** — static borders and backgrounds only.
- **No emojis in functional UI** — no ✨ ⚡ in buttons or banners. Emoji only acceptable in content (e.g. flag icons in language picker).
- **Flat solid buttons** — solid `#ea580c` for primary actions, not gradients. Drop-shadows minimal (`0 1px 5px` max).
- **Cool dark backgrounds** — cool navy/slate (`rgba(4,15,34,.7)`), not warm brown.
- **Quiet utility controls** — muted (`rgba(71,85,105,.35)` slate) so they don't compete with content.
- **Professional CTA copy** — "Explore Full Mode →" not "⚡ It's Free — Switch Now".

---

## Features Built (permanent reference)

### Languages (22 total)
`en` `es` `pt` `fr` `de` `it` `ru` `ja` `ko` `tl` `sv` `ceb` `ar` `he` `uk` `pl`
`zh-Hans` `zh-Hant` `yue-Hant` `vi` `hu` `hi`

RTL: `ar`, `he`. Everything else is LTR.

Chinese is three languages here, matching jw.org's own split rather than
inventing one: Mandarin Simplified (`zh-Hans`), Mandarin Traditional
(`zh-Hant`), Cantonese Traditional (`yue-Hant`). Cantonese is a different
language in its grammar and function words (嘅 唔 係 喺 咗 啲 佢 冇 畀), not
Mandarin in Traditional characters — a converter cannot produce it.

---

## 🌍 Adding a language — the runbook

**Do not hand-edit the HTML.** Everything is generated. The old brace-balancing
recipe that used to live here is obsolete: `scripts/i18n_tool.py` finds and
splices every dictionary, and the builders regenerate the pages.

Reference implementations, newest first — copy the most recent one:
`add_polish_plumbing.py`, `add_ukrainian_plumbing.py`, `add_hebrew_plumbing.py`.

### Step 0 — verify the jw.org locale code FIRST

⚠️ **The quietest bug in the codebase.** `js/reading.js` has a `WTLOCALE` map
that turns a language into jw.org's own code for Bible-chapter deep links.
jw.org serves **English for any code it does not recognise** — no error, no
warning, the feature just silently works in the wrong language.

Hebrew shipped as `HB` (the obvious-looking abbreviation, not a real code) and
served English to Hebrew readers for two releases before anyone noticed. Never
infer this value. Check it:

```bash
curl -sL "https://www.jw.org/finder?wtlocale=<CODE>&pub=nwtsty&bible=1001000" \
  | grep -o '<html[^>]*lang="[a-z-]*"'
```

The code is **not** the ISO code, and near-misses fail silently: `PL`, `UK` and
`HB` all serve English. Verified values, asserted on every run by the
`VERIFIED` table in `tests/16_reading.js`:

```
en E    es S    pt T    fr F    de X    it I    ru U    ja J
ko KO   tl TG   sv Z    ceb CV  ar A    he Q    uk K    pl P
zh-Hans CHS     zh-Hant CH      yue-Hant CHC     vi VT     hu H
```

Vietnamese is the sharpest illustration of why this step exists: `VI` — the
language's own ISO code, and the first thing anyone would try — serves
**Russian**, and `V` serves **Slovak**. Not English, not an error: a Bible
chapter in a different language entirely.

If jw.org splits a language into variants, split it the same way rather than
picking one — the codes above are three separate entries because jw.org serves
three separate sites, and `CHT`, `CAN` and `ZH` all look plausible and all
serve English.

Add a row there for each new language, or the map can drift back out of step
with the picker without anything objecting.

### Step 1 — plumbing (4 places, all outside the dictionaries)

Copy the newest `add_*_plumbing.py`, change the anchors, run it. It patches:

1. the `?lang=` allow-list `var V=[…]` in both index.html files
2. the nav `<option>` picker in both index.html files
3. **`NAV_LANGS` in `js/app.js`** — a *second, independent* picker
4. `WTLOCALE` in `js/reading.js`

Anchor on `var V=` for (1), not the bare list: `add_rtl_wiring.py` derives its
own copy of the allow-list out of index.html, so the short form now matches
twice. If the code is a BCP-47 tag with a hyphen it must be **quoted** wherever
it is a JS object key — `i18n_tool.py` does this for you, and `add_chinese_
plumbing.py` is the reference for the four enumeration points.

> `add_arabic_plumbing.py` only knew about (1), (2) and (4) — it predates
> `NAV_LANGS` being extracted out of the HTML — which is why Hebrew needed a
> separate patch after `01_static.js` caught it. Always do both pickers.

Then add the code to the builders. They do **not** all define the same
variables — add it to the ones each file actually has:

| | `LANGS` | `RTL_LANGS` | `LANG_NAME` | `LOCALE` |
|---|---|---|---|---|
| `build_guides.py`  | ✅ | ✅ | — | — |
| `build_landing.py` | ✅ | ✅ | ✅ | ✅ |
| `build_seo.py`     | ✅ | — | — | ✅ |

(`RTL_LANGS` only matters for a right-to-left language.)

### Step 2 — UI strings (~1,100 keys, 20 tables)

```bash
python3 scripts/i18n_tool.py extract en   # -> scripts/i18n_data/*.en.json
# write scripts/i18n_data/<file>.<lang>.json for each, same keys, same order
python3 scripts/i18n_tool.py inject <lang>
python3 scripts/i18n_check.py <lang>      # must exit 0
```

Two tables `i18n_tool.py` cannot see, because they are flat `lang:"string"`
maps rather than `lang:{…}` objects — patch them by hand:

- the **offline banner** inside the `<!-- ── Offline indicator + haptics ── -->`
  block in both index.html files (Arabic was missing from it for months
  because nothing looked)
- `scripts/i18n_data/landing_chrome.json`, `navbar.json`, `forum.json`

**Keep `dk_kw_*` keyword words in English** (highlights.html). Those awards
match a literal English word with a SQL `LIKE`; translating the quoted word
would make the stated criterion untrue.

### Step 3 — the 37 guides (~122k characters, ~85% of the total work)

Write `scripts/guides_<lang>.py` defining `GUIDES_<LANG>`, add `CHROME["<lang>"]`
(27 keys incl. the 5-entry `groups` map) to `guides_i18n.py`, register it in
`GUIDE_TEXT`, then `python3 scripts/check_guide_lang.py <lang>` (must be
`37/37, 0 problems`). Dump the English source in batches with
`python3 scripts/dump_guides.py <start> <end>` and append batch by batch —
building the module in one pass is unwieldy.

**Prefer the JSON-batch route.** `scripts/build_lang_guides.py` is the general
form — pass it a language and a batch directory. (`build_chinese_guides.py` is
the Chinese-only variant, which additionally derives zh-Hant by conversion.)
It reads one JSON file per batch (`{lang: {slug: {...}}}`) and generates the
`.py` module,
which is strictly better than appending to a Python file by hand: the batch is
valid JSON or it is not, a slug translated twice aborts instead of silently
winning, and re-running is idempotent. It also reports `n/37 translated` with
the missing slugs named, so progress is never guessed at, and it writes an
empty stub on the first run so registering the language in `guides_i18n.py`
before generating the module does not deadlock the import.

Add the language to `META` there, plus `STRAY` (scripts its copy must never
contain) and, for a Latin-script language with obligatory diacritics,
`DIACRITIC` — a long Vietnamese paragraph with no tone marks at all is
stripped or untranslated text, not a stylistic choice.

#### If you are tempted to machine-convert one language into another

Only two of the site's languages are close enough for that to be a real
option, and even there OpenCC alone was not safe. `s2twp` made two mistakes on
this copy that no test, build or page load would have caught:

| Simplified | s2twp gave | Should be | Why it matters |
|---|---|---|---|
| 项目 | 專案 | 項目 | "project" vs "item" — every guide means item |
| 合并 | 合並 *sometimes* | 合併 | its segmenter occasionally swallowed the 并; the site's most important verb came out two ways on one page |

So `build_chinese_guides.py` hides the load-bearing vocabulary behind
placeholders (`TERMS`) and lets the converter see only ordinary prose, then
fails the build on any known-wrong form (`BANNED`). Note what is *not* banned:
`文件` must become `檔案` when it means "file", but `s2twp` also turns `文档`
into `文件`, which is the correct Traditional name for the Documents folder —
banning the string would fail the build on a correct page. **A conversion that
is wrong is worse than one that is missing**, because nothing downstream
objects to fluent, plausible, incorrect text.

The same script also rejects stray scripts (Cyrillic, Hebrew, Arabic, Thai,
Hangul, kana) in Chinese copy. That guard exists because a Cyrillic
`материал` reached a Cantonese paragraph and reads as a plausible word at a
glance. Any language whose copy should be written in one script deserves the
equivalent check.

### Step 4 — build, test, ship

```bash
python3 scripts/build_guides.py && python3 scripts/build_landing.py \
  && python3 scripts/build_seo.py && python3 scripts/build_rtl.py
```
Then mirror `js/*` + `highlights.html` + `share.html` to `beta/` (but
`git checkout beta/js/enhancements.js` — it legitimately differs), add the code
to the `LANGS`/`EXPECTED_LANGS`/`RTL` lists in `tests/*.js` **and to the
`VERIFIED` wtlocale table in `16_reading.js`**, bump `softwareVersion` in both
index.html files and `CACHE_VERSION` in `service-worker.js`, add a `CHANGELOG.md`
entry, run the full suite to exit 0.

### Cost, and the cheap option

UI strings ≈ 30k characters; the guides ≈ 122k. So a language is **~85% guides**,
which means **you can ship a language's UI without its guides** and the SEO layer
handles it correctly on its own. Useful for testing demand before committing to
the guide translation.

There are **two** hreflang clusters and they are gated differently — this is
what makes the split safe:

- the **landing** cluster (`/` ↔ `/<lang>/`) is driven by `LANGS`, so a UI-only
  language does get its `/<lang>/` page, its alternates and its sitemap entry;
- the **guides** cluster (`/guides/` ↔ `/guides/<lang>/`) is driven by
  `GUIDE_LANGS`, which is derived from `guides_i18n.GUIDE_TEXT`
  (`build_seo.py`, `build_landing.py`).

So a language absent from `GUIDE_TEXT` is fully advertised as a landing page and
not advertised at all as a guide tree. Its landing page still shows the "Guides
and how-tos" link, but `guides_url()` points it at the English `/guides/` rather
than a `/guides/<lang>/` that does not exist — a deliberate fallback, not a 404.
Nothing has to be remembered or switched off by hand.

### Simple Mode
- Default ON for first-time visitors; restores saved pref via `loadPrefs().simpleMode`
- State init: `useState(()=>{const p=loadPrefs();return p.simpleMode!==void 0?p.simpleMode:!0})`
- Segmented pill toggle in nav bar — CSS classes: `.mode-seg-ctrl`, `.mode-seg-btn`, `.mode-seg-on`, `.mode-seg-full`
- Static teaser banner at top of Simple Mode — CSS classes: `.simple-mode-teaser`, `.simple-mode-teaser-inner`
- All mode changes call `savePrefs({simpleMode: bool})`

### Merge Pipeline — Web Worker (`beta/js/merge-worker.js`)
All SQLite query execution, ZIP decompression, and ZIP recompression run in a dedicated Web Worker off the UI thread. The main thread transfers `ArrayBuffer`s to the worker via Transferable Objects (zero-copy) and receives the merged `.jwlibrary` buffer back the same way. The main thread's `vt()` function is now a thin dispatcher; result assembly (Blob URL, IDB save) stays on the main thread.
- Worker file: `beta/js/merge-worker.js`
- Cancel: main thread posts `{type:'cancel'}` → worker checks `cancelled` flag every 250 rows

### Tag Suggestion Merge Toggle
The "Merge →" button in the Suggested Merges panel is a persistent toggle:
- **Idle:** Orange "Merge →"
- **Active:** Emerald green "✓ Applied" (bold) — persists until clicked again
- Clicking again resets action to `"keep"` (toggle off / undo)

### Note Explorer (Browse) — v2.4.0 full edit mode
In-browser library manager for any `.jwlibrary` file — three tabs (Notes / Highlights / Bookmarks) with search, color filter, tag filter, publication filter, detail pane, **and full editing**.

- **Self-contained `<script>` + `<style>` block** injected just before `</body>` (markers: `<!-- ── Note Explorer (Browse) ──...`). Does NOT touch React state — all CSS classes are `.jb-*` to avoid collisions.
- **Entry points:**
  - Standalone CTA card on the Simple Mode landing (`.jb-cta-card`, "Browse Your Notes")
  - Orange button in the Insights modal header (`.jb-browse-open-btn`, label key `brw_open`)
  - Public function: `window.__openJwBrowse(file)` — pass a `File`/`Blob`/`ArrayBuffer` or `undefined` (will prompt for one)
- **File hand-off:** the main app's `ja()` function (the file loader that powers Insights) sets `window.__jwLastFile = e` so Browse can reuse the same upload.
- **i18n:** Browse has its **own** `I18N` object inside `js/browse.js` (141 keys × every language). Only `brw_open` lives in the main `TRANSLATIONS` (because the trigger button renders inside React). `i18n_tool.py` handles it like any other table.
- **Data:** Reads AND WRITES `Note`, `UserMark`, `Bookmark`, `Tag`, `TagMap`, `Location` on the main thread via sql.js — do NOT extend `merge-worker.js` (it's write-optimised).
- Capped at 2000 displayed rows with a "narrow your search" hint.
- **DB stays open** after load (`state.db`); `state.dirty` tracks change count; `state.editingId` tracks which item is in edit mode.
- **Edit mode** (all three tabs): click Edit in the detail pane → in-place form; Save writes SQL UPDATE; Cancel restores read view.
  - Notes: edit title + content (textarea, plain text → `plainTextToNoteHtml()` on save), add/remove tags, change highlight colour (if note has a UserMarkId)
  - Highlights: change colour, edit linked note title + content
  - Bookmarks: edit title
- **Delete**: inline confirm box (no `window.confirm`) → cascade-deletes TagMap rows for notes
- **Export**: `state.db.export()` → JSZip → download `edited_<filename>.jwlibrary`
- **Unsaved guard**: `closeOverlay()` calls `window.confirm()` if `state.dirty > 0`
- **New CSS classes** (all `.jb-*`): `.jb-edit-panel`, `.jb-edit-field`, `.jb-edit-label`, `.jb-edit-input`, `.jb-edit-textarea`, `.jb-tag-editor`, `.jb-tag-rm`, `.jb-tag-rm-x`, `.jb-tag-add-row`, `.jb-tag-add-input`, `.jb-tag-add-btn`, `.jb-color-picker-row`, `.jb-cp-dot`, `.jb-btn-danger`, `.jb-btn-danger-solid`, `.jb-delete-confirm`, `.jb-export-btn`, `.jb-dirty-badge`, `.jb-format-note`
- **Key helper functions**: `plainTextToNoteHtml(text)`, `saveNote()`, `deleteNote()`, `addTagToNote()`, `removeTagFromNote()`, `changeNoteColor()`, `changeHighlightColor()`, `deleteHighlight()`, `saveHighlightNote()`, `deleteBookmark()`, `saveBookmark()`, `exportDb()`, `markDirty()`, `updateDirtyBadge()`, `buildEditNote()`, `buildEditHighlight()`, `buildEditBookmark()`, `buildColorPicker()`, `buildTagEditor()`, `buildInlineDeleteConfirm()`

---

## 📖 Weekly Watchtower Study Annotation (personal `.jwlibrary` workflow)

**Trigger:** the user uploads a `.jwlibrary` backup and says "study and annotate today's/this week's Watchtower" (any phrasing). This is a **file deliverable**, not a website change — nothing in the repo is edited, no commit needed. Do the whole thing without asking questions.

### Step 1 — Identify the article
- Week's schedule: `https://wol.jw.org/en/wol/meetings/r1/lp-e/<year>/<ISO week number>` → gives the study article title + link `https://wol.jw.org/en/wol/d/r1/lp-e/<DocumentId>`.
- WebFetch's summarizer may refuse to reproduce article text — instead `curl` the article URL and parse the raw HTML yourself.
- Study paragraphs are `<p id="pN" data-pid="N">`; questions are `class="qu"`; each question is followed by a `gen-field` div containing `<textarea id="ttNN">` (this id is the `InputField.TextTag` for the answer).

### Step 2 — Open the backup
`.jwlibrary` = ZIP containing `userData.db` (SQLite, schemaVersion 16), `manifest.json`, media files. Work on an extracted copy. Check what the user already has on the article's Location(s) — never duplicate or disturb their own notes/highlights.

### Step 3 — Add three kinds of annotations
All anchored to the article's Location row with `KeySymbol='w'`, `DocumentId=<id>`, `IssueTagNumber=<yyyymm00>`, **`MepsLanguage=0`, Type 0** (create if missing).

**a) Gem notes** (~15–22 per article):
- `Note` rows: `BlockType=1`, `BlockIdentifier = data-pid` of the paragraph (**NOT** the printed paragraph number), `Guid=uuid4`, `UserMarkId=NULL`, timestamps `YYYY-MM-DDTHH:MM:SSZ`.
- Style: titles like `Greek gem: …` / `Hebrew gem: …` / `Gem: …` / `Modern parallel: …`; body 1–3 sentences, insightful and concise. Cover the theme text, most study paragraphs, opening/closing songs, and any box. Doctrinally consistent with JW understanding (e.g. holy spirit = God's active force).

**b) Key-point highlights** (all paragraphs the user hasn't marked; key phrases only, never whole paragraphs):
- `UserMark(UserMarkId, ColorIndex, LocationId, StyleIndex=0, UserMarkGuid=uuid4, Version=1)` + `BlockRange(BlockRangeId, BlockType=1, Identifier=data-pid, StartToken, EndToken, UserMarkId)`.
- Color scheme: **1 yellow** = direct answer to the printed question · **2 green** = principles/scriptures/holy-spirit statements · **3 blue** = illustrations, definitions, tools · **4 pink** = heart statements / key definitions · **5 orange** = action commands · **6 purple** = warnings.
- **Token numbering (critical):** strip zero-width chars (`​ ⁠ ﻿ ­`); split paragraph text on whitespace; within each chunk, a token is a maximal run matching `[A-Za-zÀ-ɏ’':\-\d]+`, and every other character is its own token. So `Jehovah’s`, `well-trained`, `6:5`, `3:1-7`, `607` are each ONE token; `.` `,` `“` `”` `(` `)` `—` are each their own token; `B.C.E.` is six. The printed paragraph number (`2 `, `3 `…) is **not** a token. Tokens are 0-indexed; `StartToken`/`EndToken` are inclusive.
- **Always validate the tokenizer first** against the user's existing highlights in the same backup (reproduce their `BlockRange` ranges as sensible phrases) before inserting anything.

**c) Study-question answers:**
- `InputField(LocationId, TextTag, Value)` — one row per question textarea (`tt44`, `tt48`… from the HTML, plus the "How Would You Answer?" review box, e.g. `tt25/tt30/tt35`).
- ⚠️ InputField rows attach to a **separate Location row with `MepsLanguage=NULL`** (same DocumentId/KeySymbol/IssueTagNumber, Type 0) — create it if missing. Notes/marks use the `MepsLanguage=0` row.
- Answers: 1–3 sentences, drawn from the paragraph, woven with the gems, cite scriptures.

### Step 4 — Repackage & deliver
1. Update the `LastModified` table (single row) to the same timestamp.
2. Sanity: `pragma integrity_check` = ok; `pragma foreign_key_check` count unchanged vs the pristine DB (the device's own backups already contain ~300 benign violations — do not "fix" them).
3. Recompute `manifest.json → userDataBackup.hash` = SHA-256 hex of the new `userData.db`; update `lastModifiedDate`.
4. Re-zip the same file list (deflate), name it `UserdataBackup_<YYYYMMDD>_Watchtower_Annotated.jwlibrary`, verify it round-trips, and send it to the user (import via JW Library → Personal Study → Backup and restore).

### Reference — first run (July 13-19, 2026, doc 2026401)
Delivered 22 notes, 43 highlights, 19 answers. Earlier articles annotated the same way: docs 2026367, 2026368 (notes + answers, `tt` tags stepping by 4). Existing user habits: colors 2/3/6 for their own marks; their highlights confirmed the tokenizer (e.g. pid 7 tokens 22-28 = "We are created with a special gift").

---

## Gotchas & Tips

- **Python replacements only** — files are too large for Edit tool; use `open().read()` → `str.replace()` → `write()`
- **Always verify anchors first** — check `content.count(anchor) == 1` before replacing
- **A stale `scripts/*.py` will happily undo a later fix.** `add_rtl_wiring.py` carried its own copy of the `<head>` bootstrap. Re-running it overwrote the shipped one and silently reverted a first-paint fix (rtl.css had been made lazy so it stopped blocking render for the 14 LTR languages). Before re-running any patch script, diff what it *writes* against what is actually in the file — the script is not necessarily the newer of the two.
- **Bugs that produce no error are the expensive ones.** Two hit this codebase: the jw.org wtlocale falling back to English, and a language table that no tooling could see. Neither failed a test, a build, or a page load. When a field is "an opaque code someone else's system interprets", verify it against that system rather than reasoning about it.
- **Service worker** precaches `index.html`, `highlights.html`, and `share.html`. Bump `CACHE_VERSION` in `service-worker.js` (currently `jwsync-vN` — check the file) any time you ship a change to any of those pages (or their beta twins) so PWA users pick it up. Test suite `15_parity.js` fails if you forget.
- **One-off Python patch scripts** from past sessions live in `scripts/` — they are historical records, not part of any build; don't re-run them.
- **Mobile language picker** — on Android, the `<select>` renders as a native radio list. That IS the language selector; no separate component
- **TRANSLATIONS validation** — verify after any language insertion:
  ```bash
  node -e "
  const c=require('fs').readFileSync('beta/index.html','utf8');
  const m=c.match(/__JW_LANDING_I18N *= */);   // TRANSLATIONS is an alias of this
  const ts=m.index+m[0].length;
  let d=0,e=ts;
  for(let i=ts;i<c.length;i++){if(c[i]==='{')d++;else if(c[i]==='}'){d--;if(d===0){e=i+1;break;}}}
  const r=JSON.parse(c.slice(ts,e));           // strict JSON — parse, don't eval
  console.log(Object.keys(r));
  "
  ```

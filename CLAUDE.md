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
- `npm test` chains all three suites (`01_static.js && 02_runtime.js && 03_regression.js`) and exits non-zero on the first failure.
- Individual suites are available too: `npm run test:static`, `:runtime`, `:regression`.

**Run the tests proactively before pushing any feature that touches `beta/index.html`, `index.html`, the Browse module, or `service-worker.js`.** If a suite fails, fix it before committing — do not push a broken build.

Suite coverage (~80 assertions):
- **01_static.js** — both index.html files parse, TRANSLATIONS object is well-formed across all 10 languages, Browse i18n covers every required key, every CSS class referenced is defined, all hook/marker strings present.
- **02_runtime.js** — synthesises a `.jwlibrary` in-memory (zipped SQLite with the JW Library schema), boots the Browse module in JSDOM, drives every UI affordance (tab switching, color/tag/publication filters, search, sort, detail panes for notes/highlights/bookmarks, copy-to-clipboard, clear-all, close).
- **03_regression.js** — merge worker still parses, every critical merge anchor is intact, HTML structure clean (one structural `</body>`/`</html>` outside scripts), cache version is set.

If you add a new user-facing feature, extend the relevant suite to cover it.

---

## Codebase Overview

- **Single-file React SPA** — all JS is minified and embedded directly in the HTML files
- **No build system** — edit the HTML files directly with Python string replacements
- Files are ~440KB+; use Python `str.replace()` for all edits, never the Edit tool
- `styles.css` / `beta/styles.css` exist but the HTML files also have embedded `<style>` blocks
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

### Languages (10 total)
`en` `es` `pt` `fr` `de` `it` `ru` `ja` `ko` `tl`

**Adding a language — critical gotcha:** The `TRANSLATIONS` object ends with `}},stripHTML=`. Insert a new language BETWEEN those two closing braces:
```python
content.replace('}},stripHTML=', '}' + new_lang_block + '},stripHTML=', 1)
# new_lang_block starts with ,xx:{...} and ends with }
```

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
- **i18n:** Browse has its **own** `I18N` object inside the module (~55 keys × 10 languages). Only `brw_open` lives in the main `TRANSLATIONS` (because the trigger button renders inside React).
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

## Gotchas & Tips

- **Python replacements only** — files are too large for Edit tool; use `open().read()` → `str.replace()` → `write()`
- **Always verify anchors first** — check `content.count(anchor) == 1` before replacing
- **Service worker** caches `index.html`. Bump `CACHE_VERSION` in `service-worker.js` (currently `jwsync-vN` — check the file) any time you ship a meaningful change to either index.html so PWA users pick it up
- **Mobile language picker** — on Android, the `<select>` renders as a native radio list. That IS the language selector; no separate component
- **TRANSLATIONS validation** — verify after any language insertion:
  ```bash
  node -e "
  const c=require('fs').readFileSync('beta/index.html','utf8');
  const ts=c.indexOf('TRANSLATIONS=')+13;
  let d=0,e=ts;
  for(let i=ts;i<c.length;i++){if(c[i]==='{')d++;else if(c[i]==='}'){d--;if(d===0){e=i+1;break;}}}
  const r=eval('('+c.slice(ts,e)+')');
  console.log(Object.keys(r));
  "
  ```

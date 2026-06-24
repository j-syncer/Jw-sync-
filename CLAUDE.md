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
- `npm test` chains all 15 suites (`01_static.js` … `15_parity.js`) and exits non-zero on the first failure.
- Individual suites are available too: `npm run test:static`, `:runtime`, `:regression`, `:lazy`, `:post-merge`, `:conflict`, `:wrapped`, `:preview`, `:sync`, `:mobile`, `:semantic`, `:share`, `:receive`, `:doctor`, `:parity`.

**Run the tests proactively before pushing any feature that touches `beta/index.html`, `index.html`, the Browse module, or `service-worker.js`.** If a suite fails, fix it before committing — do not push a broken build.

Suite coverage:
- **01_static.js** — both index.html files parse, TRANSLATIONS object is well-formed across all 12 languages, Browse i18n covers every required key, every CSS class referenced is defined, all hook/marker strings present.
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

### Languages (12 total)
`en` `es` `pt` `fr` `de` `it` `ru` `ja` `ko` `tl` `sv` `ceb`

**Adding a language:** the app's `TRANSLATIONS` is an alias —
`TRANSLATIONS = window.__JW_LANDING_I18N;` — and `__JW_LANDING_I18N` is defined
as one big **strict-JSON** object (one per index.html, near the top of a script
block). The old `}},stripHTML=` anchor no longer exists. Safest method: locate
the object by brace-balancing from the `__JW_LANDING_I18N = ` anchor, then
round-trip it through `json`:
```python
import json, re
c = open('beta/index.html', encoding='utf-8').read()
m = re.search(r'__JW_LANDING_I18N *= *', c)
ts = m.end(); d = 0
for i in range(ts, len(c)):
    if c[i] == '{': d += 1
    elif c[i] == '}':
        d -= 1
        if d == 0: e = i + 1; break
obj = json.loads(c[ts:e])
obj['xx'] = {...}  # same ~100 keys as obj['en']
c = c[:ts] + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + c[e:]
open('beta/index.html', 'w', encoding='utf-8').write(c)
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
- **i18n:** Browse has its **own** `I18N` object inside the module (~55 keys × all 12 languages). Only `brw_open` lives in the main `TRANSLATIONS` (because the trigger button renders inside React).
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

---

## JW Library Backup Editing

The user sometimes asks to edit their `.jwlibrary` backup file — e.g. to pre-fill study article answer boxes, add highlights, and add notes so the article appears fully studied. This section documents the complete workflow.

### What a .jwlibrary file is

A `.jwlibrary` file is a **ZIP archive** containing:
- `userData.db` — SQLite database with all user data
- `manifest.json` and image assets

Extract with Python's `zipfile` module, edit the SQLite DB, then repackage.

### Relevant database tables

| Table | Purpose |
|-------|---------|
| `Location` | Links content to a document. One row per article per context (see Two-Location rule below) |
| `UserMark` | One row per highlight — stores ColorIndex and LocationId |
| `BlockRange` | Token range for a highlight — `Identifier` = paragraph PID, `StartToken`/`EndToken` = word indices (0-based) |
| `Note` | Freeform notes — `BlockIdentifier` = paragraph PID |
| `InputField` | Study question answers — `TextTag` = the textarea's HTML id, `Value` = answer text |

### ⚠️ CRITICAL: The Two-Location Rule

JW Library uses **two separate Location rows** for the same article:

| LocationId | MepsLanguage | Used for |
|------------|-------------|---------|
| Primary (e.g. 19732) | `0` (integer) | `UserMark`, `BlockRange`, `Note` |
| Secondary (e.g. 19738) | `NULL` | `InputField` only |

**InputField entries placed at the MepsLanguage=0 location will silently fail to appear in the app.** Always create a second Location with `MepsLanguage=NULL` for InputField entries. The two LocationIds are usually consecutive (original + 1 beyond the max existing ID).

Check the pattern from any other article in the DB:
```python
c.execute("SELECT LocationId, MepsLanguage FROM Location WHERE DocumentId=? ORDER BY LocationId", (doc_id,))
```

### ⚠️ CRITICAL: TextTag IDs are NOT data-pid values

The `TextTag` column in `InputField` matches the **`id` attribute of the `<textarea>` element** inside each answer box in the JW.org HTML — it does NOT match the `data-pid` of the surrounding `<div class="gen-field">`.

The `data-pid` and the textarea `id` are completely different numbers. Always extract TextTag IDs from the HTML:

```python
import re
html = open('article.html', encoding='utf-8').read()
# Each result is (textarea_id, containing_gen_field_pid)
for m in re.finditer(r'<textarea id="(tt\d+)"', html):
    tag_id = m.group(1)
    before = html[:m.start()]
    pids = re.findall(r'class="gen-field"[^>]*data-pid="(\d+)"', before)
    print(f'TextTag={tag_id}, gen-field pid={pids[-1] if pids else "?"}')
```

### ColorIndex values

| Value | Color |
|-------|-------|
| 1 | Yellow |
| 2 | Green |
| 3 | Blue |
| 4 | Red |
| 5 | Orange |
| 6 | Purple |

### Token range calculation

`BlockRange.StartToken` and `EndToken` are 0-based word indices (split on whitespace) within the paragraph text. Use this helper:

```python
def tok_range(text, phrase):
    tokens = text.split()
    offsets = []
    pos = 0
    for t in tokens:
        idx = text.find(t, pos)
        offsets.append((idx, idx + len(t)))
        pos = idx + len(t)
    p_start = text.find(phrase)
    if p_start == -1:
        raise ValueError(f"Phrase not found: {repr(phrase)}")
    p_end = p_start + len(phrase)
    s = e = None
    for i, (ts, te) in enumerate(offsets):
        if s is None and te > p_start: s = i
        if ts < p_end: e = i
    return s, e
```

Watch out for Unicode vs ASCII quotes in phrases — the paragraph text may use straight quotes while a copied phrase has curly quotes. Strip or normalize when needed.

### Full workflow

```python
import sqlite3, uuid, zipfile, os

ARCHIVE = "path/to/original.jwlibrary"
OUT     = "path/to/output.jwlibrary"

# 1. Extract fresh copy of DB
with zipfile.ZipFile(ARCHIVE, 'r') as z:
    z.extractall("work_dir/")
DB = "work_dir/userData.db"

# 2. Find the article's existing Location (MepsLanguage=0)
conn = sqlite3.connect(DB)
c = conn.cursor()
row = c.execute("SELECT LocationId FROM Location WHERE DocumentId=? AND MepsLanguage=0", (doc_id,)).fetchone()
LOC_UM = row[0]  # for UserMark / Note / BlockRange

# 3. Create InputField location (MepsLanguage=NULL)
max_loc = c.execute("SELECT MAX(LocationId) FROM Location").fetchone()[0]
LOC_IF = max_loc + 1
c.execute("""INSERT INTO Location
             (LocationId,BookNumber,ChapterNumber,DocumentId,Track,
              IssueTagNumber,KeySymbol,MepsLanguage,Type,Title,Specialty,Edition)
             VALUES (?,NULL,NULL,?,NULL,?,'w',NULL,0,'',NULL,NULL)""",
          (LOC_IF, doc_id, issue_tag))  # issue_tag e.g. 20260400 for April 2026

# 4. Insert highlights
um_id = c.execute("SELECT MAX(UserMarkId) FROM UserMark").fetchone()[0] + 1
br_id = c.execute("SELECT MAX(BlockRangeId) FROM BlockRange").fetchone()[0] + 1
for pid, color, phrase in HIGHLIGHTS:
    s, e = tok_range(PARA[pid], phrase)
    c.execute("INSERT INTO UserMark (UserMarkId,ColorIndex,LocationId,StyleIndex,UserMarkGuid,Version) VALUES (?,?,?,?,?,?)",
              (um_id, color, LOC_UM, 0, str(uuid.uuid4()), 1))
    c.execute("INSERT INTO BlockRange (BlockRangeId,BlockType,Identifier,StartToken,EndToken,UserMarkId) VALUES (?,?,?,?,?,?)",
              (br_id, 1, pid, s, e, um_id))
    um_id += 1; br_id += 1

# 5. Insert InputField answers (at LOC_IF, NOT LOC_UM)
for tag, value in INPUT_FIELDS:
    c.execute("INSERT INTO InputField (LocationId,TextTag,Value) VALUES (?,?,?)",
              (LOC_IF, tag, value))

# 6. Insert notes
n_id = c.execute("SELECT MAX(NoteId) FROM Note").fetchone()[0] + 1
TS = "2026-06-24T12:00:00+00:00"
for pid, title, content in NOTES:
    c.execute("""INSERT INTO Note (NoteId,Guid,UserMarkId,LocationId,Title,Content,
                                   LastModified,Created,BlockType,BlockIdentifier)
                 VALUES (?,?,NULL,?,?,?,?,?,1,?)""",
              (n_id, str(uuid.uuid4()), LOC_UM, title, content, TS, TS, pid))
    n_id += 1

c.execute("UPDATE LastModified SET LastModified=?", (TS,))
conn.commit(); conn.close()

# 7. Repackage
with zipfile.ZipFile(ARCHIVE, 'r') as zin:
    names = zin.namelist()
with zipfile.ZipFile(OUT, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name in names:
        if name == 'userData.db':
            zout.write(DB, 'userData.db')
        else:
            with zipfile.ZipFile(ARCHIVE, 'r') as zin:
                zout.writestr(name, zin.read(name))
```

### How to get the article HTML and TextTags

Fetch the article from JW.org using curl (the proxy handles HTTPS):

```bash
curl -sL "https://www.jw.org/en/library/magazines/watchtower-study-YYYYMM/article-name/" \
  -o article.html
```

Or use the `finder` URL with `docid`:
```bash
curl -sL "https://www.jw.org/finder?srcid=jwlshare&wtlocale=E&prefer=lang&docid=XXXXXXX" \
  -o article.html
```

Then extract all TextTags and paragraph PIDs with:
```python
import re
html = open('article.html', encoding='utf-8').read()
# All answer box TextTags
print(re.findall(r'<textarea id="(tt\d+)"', html))
# All gen-field (answer box) PIDs
print(re.findall(r'class="gen-field"[^>]*data-pid="(\d+)"', html))
# All paragraph PIDs
print(re.findall(r'data-pid="(\d+)"', html))
```

### IssueTagNumber format

For Watchtower study articles: `YYYYMM00` where MM is the **month of the magazine** (not the week), zero-padded, with `00` appended. Example: April 2026 issue → `20260400`. Find this in the existing Location row for any other article from the same issue:
```python
c.execute("SELECT IssueTagNumber FROM Location WHERE KeySymbol='w' AND MepsLanguage=0 LIMIT 5").fetchall()
```

### Preserving the user's existing data

Always start from a **fresh extract of the original backup** — never re-run scripts on an already-modified DB. The user's original highlights are already in the DB at their LocationIds; adding new rows does not disturb them. Use `MAX(UserMarkId)+1`, `MAX(BlockRangeId)+1`, `MAX(NoteId)+1` for all new IDs.

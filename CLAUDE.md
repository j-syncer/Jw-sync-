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
- Answers: **short and plain — 1–2 sentences**, the direct answer to the printed question with its scripture. No personas here. This box is the answer the user could read out at the meeting; the personality lives in the persona notes (see below).

**d) Persona comments — coloured highlight + attached note:**
Each commenter's remark is a `Note` **attached to a `UserMark` in that persona's own colour**, not text in the answer box. Tapping the highlight in JW Library opens the comment.
- Colour is the persona's identity and never changes: **Rosa = 4 pink · James = 3 blue · Dave = 5 orange · Tala = 6 purple · Naomi = 2 green.** (Yellow 1 stays free for a plain key-point mark.)
- Build each one as: `UserMark(ColorIndex=<persona colour>, LocationId=<MepsLanguage=0 row>, StyleIndex=0, UserMarkGuid=uuid4, Version=1)` + `BlockRange(BlockType=1, Identifier=data-pid, StartToken, EndToken)` + `Note(UserMarkId=<that mark>, LocationId=<same>, BlockType=1, BlockIdentifier=data-pid, Title='<persona name>', Content='<the comment>')`.
- **Title is just the persona's first name** — that is what shows in the note list.
- Anchor the highlight on the phrase the comment is actually about, in the paragraph that question covers. Keep it to a phrase, never a whole paragraph.
- **Never overlap a highlight the user already has, or one you just placed.** Read the existing `BlockRange` rows for the Location first, keep a running occupied-set per pid, and if a chosen phrase collides, move to another phrase. The user's own marks are never modified or deleted.
- Comments are **short — 1–2 sentences, ~25 words.** Cut anything that restates the paragraph.
- Add one unattached note titled `Colour key: who is speaking` on the first paragraph, listing which colour is which persona.

#### The five commenters (permanent cast — use on every article)

Personas are fixed across weeks so the user gets to know them. They speak in the attached colour notes, never in the answer box.

| # | Persona | Who they are | Voice | Answers questions about… |
|---|---------|--------------|-------|--------------------------|
| 1 | **Rosa** | Sister, joyful and quirky, warm-hearted | Bright and personal, homey illustrations (kitchen, grandkids, service group), often ends on encouragement. Exclamation-friendly, never sappy | Application, gratitude, encouraging one another, hospitality, joy under trial |
| 2 | **James** | Brother, serious and dignified | Measured and unhurried. Original-language words, historical/cultural background, cross-references, the "why beneath the why". Never jokes | Doctrine, prophecy, Bible context, motive, deeper reasons behind a command |
| 3 | **Dave** | Brother, the quick wit — the one who gets the laugh | **Genuinely funny, and the funniest thing in the article.** Two sentences at most: set up an honest admission about himself, then turn it so the point lands *through* the joke rather than after it. Best device is catching himself in a double standard ("when I do it, it's concern; when it's done to me, it's gossip"). Undersell the punch line — no exclamation marks, no winking. Humour is always on himself or on ordinary human nature — **never** on Jehovah, the scriptures, the organization, or another person | Human weakness, procrastination, pride, double standards, "easier said than done" questions, practical illustrations |
| 4 | **Tala** | Young sister, ~16, candid | Short, honest, unpolished. Will admit a struggle before applying the point. School, phones, friends, feeling different from peers | Peer pressure, doubts, standing firm, youth, social media, prayer |
| 5 | **Naomi** | Veteran sister, decades in the truth | Calm and unhurried; usually one brief experience from years past ("I remember a sister who…"), then the lesson. Historical perspective on the organization | Endurance, loyalty, field service, waiting on Jehovah, past hardship, changes over the years |

**Suggested alternates** (swap in if the user asks for variety): *Elena*, newly baptized, gives the plain first-principles answer that cuts through — or *Kofi*, an elder, answers from the shepherding side.

**Assignment rules**
- Match persona to question, not the reverse. Nobody answers every question; a persona who has nothing distinctive to add stays quiet.
- **1–3 personas per question.** Roughly 40% of questions get one, 45% get two, 15% get three. Never four, never all five.
- Per-article budget, scaled to the question count: **Rosa ≈ half the questions, James ≈ half** (they are the anchors) · **Dave max 4** and never on consecutive questions · **Tala 3–5** · **Naomi 3–5**.
- When two share a question they must contribute **different content** — one keys off the direct answer, the other adds an angle. No restating.
- Rosa and Dave are both light, but distinct: Rosa is *warm*, Dave is *funny*. If a Dave line could have been Rosa's, rewrite one of them.
- No persona may open two comments in the same article with the same word or construction.
- Every comment, whatever the voice, still has to be true to the printed question and doctrinally consistent with JW understanding. Humour and personality never come at the cost of accuracy.

**Not persona-voiced:** the review / "How Would You Answer?" boxes (a clean 1–2 sentence summary) and the gem notes in (a) — those stay in the study-note voice with no highlight attached.

### Step 4 — Repackage & deliver
1. Update the `LastModified` table (single row) to the same timestamp.
2. Sanity: `pragma integrity_check` = ok; `pragma foreign_key_check` count unchanged vs the pristine DB (the device's own backups already contain ~300 benign violations — do not "fix" them).
3. Recompute `manifest.json → userDataBackup.hash` = SHA-256 hex of the new `userData.db`; update `lastModifiedDate`.
4. Re-zip the same file list (deflate), name it `UserdataBackup_<YYYYMMDD>_Watchtower_Annotated.jwlibrary`, verify it round-trips, and send it to the user (import via JW Library → Personal Study → Backup and restore).

### Reference — past runs
- **doc 2026401** (July 13-19, 2026), first run: 22 notes, 43 highlights, 19 answers. Earlier articles annotated the same way: docs 2026367, 2026368 (notes + answers, `tt` tags stepping by 4).
- **doc 2026403** (July 27-Aug 2): personas introduced, still written inside `InputField.Value` — superseded by the coloured-note scheme below.
- **doc 2026404** (Aug 3-9), first run of the coloured persona notes: 16 short answers, 23 persona notes on their own coloured marks, 12 gem notes + colour key. The user already had 13 highlights of their own on pids 23-26 (colors 2/3/4/6) — all routed around, none touched.

Existing user habits: they mark in colors 2/3/4/6; their own highlights are the tokenizer check every week (reproduce their `BlockRange` ranges as sensible phrases before inserting anything).

### Gotcha — drop caps
The first word of the article's opening paragraph is set in caps in the HTML (`HAVE you ever…`, `SOME of Jehovah's servants…`). Match the case exactly when locating an anchor phrase, or the token lookup fails.

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

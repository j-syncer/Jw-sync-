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

---

## Gotchas & Tips

- **Python replacements only** — files are too large for Edit tool; use `open().read()` → `str.replace()` → `write()`
- **Always verify anchors first** — check `content.count(anchor) == 1` before replacing
- **Service worker** caches `index.html` (key: `jwsync-v3`). Bump `CACHE_VERSION` in `service-worker.js` if users report stale cache after a production push
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

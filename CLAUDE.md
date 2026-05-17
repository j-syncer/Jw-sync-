# JW Sync — Claude Instructions

## Development Workflow

1. **All changes → `beta/index.html` first** (live at jwsync.org/beta)
2. Commit + push to `main` so beta updates immediately
3. User reviews at jwsync.org/beta
4. User says "push to main" → apply same changes to `index.html` → push
5. **Never touch `index.html` (production) unless user explicitly approves**

| File | URL |
|------|-----|
| `beta/index.html` | jwsync.org/beta — staging |
| `index.html` | jwsync.org — production |

---

## Codebase Overview

- **Single-file React SPA** — all JS is minified and embedded directly in the HTML files
- **No build system** — edit the HTML files directly with Python string replacements
- Files are ~440KB+; use Python `str.replace()` for all edits, not text editor tools
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

## What Was Built (this session)

### 1. Tagalog (Filipino) Language — `tl`
- Added `tl` translation block (~94 keys) to `TRANSLATIONS` in both HTML files
- Added `🇵🇭 Filipino` option to the `<select>` language picker in the nav
- Updated `inLanguage` schema.org array and "9 languages" → "10 languages" everywhere
- **Critical gotcha:** The `TRANSLATIONS` object ends with `}},stripHTML=` where the first `}` closes the last language object and the second `}` closes `TRANSLATIONS`. When inserting a new language, you must insert BETWEEN those two braces — not before both. Wrong insertion makes the new language nest inside the previous one instead of being a top-level sibling.

  **Correct pattern:**
  ```python
  content.replace('}},stripHTML=', '}' + tl_block + '},stripHTML=', 1)
  # tl_block starts with: ,tl:{...} and ends with }
  ```

### 2. Simple Mode Redesign
- **Default:** Simple Mode on first visit; restores saved preference via `loadPrefs().simpleMode`
  - State init changed from `useState(!1)` → `useState(()=>{const p=loadPrefs();return p.simpleMode!==void 0?p.simpleMode:!0})`
- **Segmented pill toggle** in nav bar (replaces old single button):
  - CSS classes: `.mode-seg-ctrl`, `.mode-seg-btn`, `.mode-seg-on`, `.mode-seg-full`
  - Orange gradient when Simple active, purple when Full active
- **Animated teaser banner** at top of Simple Mode (replaces old "Switch Back to Full Version" button):
  - CSS classes: `.simple-mode-teaser`, `.simple-mode-teaser-inner`, `.simple-mode-teaser-text`, `.simple-mode-teaser-btn`
  - Animated border cycles orange→purple via `@keyframes teaserGlow`
  - Text: *"✨ Unlock **Tag Management**, advanced merging, bulk tools & more"*
  - CTA button: *"⚡ It's Free — Switch Now"*
- All mode changes call `savePrefs({simpleMode: bool})` to persist

---

## Gotchas & Tips

- **Python replacements only** — files are too large for Edit tool; use `open().read()` → `str.replace()` → `write()`
- **Always verify anchors first** — check `content.count(anchor) == 1` before replacing
- **Service worker** caches `index.html` (key: `jwsync-v3`). Comment says bump `CACHE_VERSION` in `service-worker.js` when shipping a new version if users report stale cache
- **Mobile language picker** — on Android, the `<select>` element renders as a native radio list. That IS the language selector we update, not a separate component
- **TRANSLATIONS validation** — use Node.js to verify after any language insertion:
  ```bash
  node -e "
  const c=require('fs').readFileSync('index.html','utf8');
  const ts=c.indexOf('TRANSLATIONS=')+13;
  let d=0,e=ts;
  for(let i=ts;i<c.length;i++){if(c[i]==='{')d++;else if(c[i]==='}'){d--;if(d===0){e=i+1;break;}}}
  const r=eval('('+c.slice(ts,e)+')');
  console.log(Object.keys(r));
  "
  ```
- **Branch for Tagalog work:** `claude/add-tagalog-language-H3H6D` (merged to main, done)

---

## Languages Supported (10 total)
`en` `es` `pt` `fr` `de` `it` `ru` `ja` `ko` `tl`

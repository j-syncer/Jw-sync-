# JW Sync — Claude Instructions

## Development Workflow

**Default: every change goes to beta only.**

| Term | What it means |
|------|---------------|
| "update beta" / any normal request | Edit `beta/index.html`, commit, push to the `main` git branch → live at jwsync.org/beta |
| "push to production" / "go live" / "ship it" | Copy the same changes into `index.html`, commit, push → live at jwsync.org |

Steps:
1. **All changes → `beta/index.html` first**, always, unless told otherwise
2. Commit + push to the `main` git branch → jwsync.org/beta updates immediately
3. User reviews at jwsync.org/beta
4. User says **"push to production"** → apply the same changes to `index.html` → commit + push
5. **Never touch `index.html` unless the user explicitly says "push to production"**

The git branch is always `main` — that detail never needs to come up in conversation.

| File | URL | When to edit |
|------|-----|--------------|
| `beta/index.html` | jwsync.org/beta | Every change, by default |
| `index.html` | jwsync.org | Only after "push to production" |

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
  - Simple active: flat solid `#ea580c` (orange). Full active: flat solid `#1d4ed8` (blue). No gradients.
- **Static teaser banner** at top of Simple Mode:
  - CSS classes: `.simple-mode-teaser`, `.simple-mode-teaser-inner`, `.simple-mode-teaser-text`, `.simple-mode-teaser-btn`
  - Static orange-tinted card (`rgba(234,88,12,.05)` bg, `rgba(234,88,12,.2)` border). No animation.
  - Text: *"Unlock **Tag Management**, advanced merging, bulk tools & more"*
  - CTA button: *"Explore Full Mode →"* — flat orange `#ea580c`, no emojis
  - `.simple-mode-teaser-icon` is `display:none` (emoji icon hidden)
- All mode changes call `savePrefs({simpleMode: bool})` to persist

### 3. Professional UI Redesign
**Design principles (approved, apply to all future work):**
- **Single accent color** — orange (`#ea580c`) is the brand color. Blue (`#1d4ed8`) is used only for the Full Mode toggle indicator. Never introduce a third competing accent.
- **No animated gradients** — `teaserGlow` and similar cycling animations are removed. Static borders and backgrounds only.
- **No emojis in functional UI** — no ✨ ⚡ in buttons or banners. Emoji only acceptable in content (e.g. flag icons in language picker).
- **Flat solid buttons** — use solid `#ea580c` for primary actions, not gradients. Drop-shadows kept minimal (`0 1px 5px` max).
- **Cool dark backgrounds** — use cool navy/slate (`rgba(4,15,34,.7)`) not warm brown (`#1c1410`). The Tailwind stone palette is already cool navy (`stone-900 = #040f22`).
- **Quiet utility controls** — the peek button (`.fn-peek-btn`) and similar inline helpers should be muted (`rgba(71,85,105,.35)` slate) so they don't compete with content.
- **Professional CTA copy** — "Explore Full Mode →" not "⚡ It's Free — Switch Now".

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

# Changelog

All notable changes to JW Sync are recorded here.

---

## [2.5.0] — 2026-05-23

### Added
- **Full language coverage** — every visible string throughout the site now changes when you switch language (10 languages: EN, ES, PT, FR, DE, IT, RU, JA, KO, TL)
- **Language picker on the landing page** — a language selector is now present in the top nav, so first-time visitors can choose their language before entering the app
- Landing page hero subtitle, nav links ("App", "Community"), feature card names and descriptions all now respond to language selection
- Simple Mode teaser cards (Note Explorer, Study Insights, Tag Management, Extract & Share, Compare & Review), the "Explore Full Mode" button, and the "Browse Your Notes" CTA card all translate correctly
- App main heading ("Merge Your JW Library Backups"), subtitle, discover cards ("What else can JW Sync do?" section), and download title all translate
- Two-way sync: changing language in the app updates the landing page; changing it on the landing page updates the React app when you enter it

---

## [2.4.2] — 2026-05-23

### Changed
- **Dark mode design refinement**: resolved "box-in-a-box" visual layering across all full-mode cards — hard `border border-stone-700` outlines removed from main cards, replaced with subtle `shadow-lg` elevation
- Removed rainbow top-border accents (pink, amber, blue, emerald strips) from utility section cards; all cards now share a consistent borderless elevated style
- Card section headers no longer use a separate high-contrast background; they now use a minimal separator line (`border-white/7`) to divide from body
- Inner drop-zone bordered boxes removed — content area is now visually flat inside the card
- "Ideas" tip boxes redesigned from opaque background boxes into quiet inline text lists with a barely-visible top separator
- Navigation utility buttons (Activity Log, Changelog, How to Use, Share, Community) visually demoted to 11 px muted ghost buttons, leaving the Simple/Full mode toggle as the clear primary control
- A subtle divider line now separates the mode toggle pill from the secondary nav buttons, reinforcing the hierarchy
- FAQ / How-to-Use modal tip cards toned down from stone-bordered boxes to lightly tinted panels; purple accent replaced with neutral stone

---

## [2.4.1] — 2026-05-23

### Fixed
- **Full landing page translation**: the hero heading, subtitle, CTA button, all four feature cards, and the footer tagline now translate into all 10 supported languages (English, Spanish, Portuguese, French, German, Italian, Russian, Japanese, Korean, Tagalog). These strings were previously hardcoded English regardless of the selected language.

---

## [2.4.0] — 2026-05-23

### Added
- **Note Explorer — Edit Mode**: the Browse module is now a full note manager, not just a viewer.
  - Edit note title and content inline (textarea; plain text round-trips back to JW Library `<p>/<br />` HTML on save)
  - Add tags from existing library or create new ones via autocomplete; remove tags with one click
  - Change highlight colour for notes that have an attached highlight
  - Edit linked note title and content directly from the Highlights tab
  - Change highlight colour from the Highlights tab detail pane
  - Edit bookmark titles from the Bookmarks tab
  - Delete notes, highlights, or bookmarks — cascade-safe with inline confirmation (no browser popup)
  - **Export .jwlibrary** — "Export .jwlibrary" button in the modal header downloads the modified backup; sql.js database kept alive after load so edits accumulate before export
  - Live "N edits" badge in the header; export button disabled until first change
  - Unsaved-changes guard: prompts before closing if there are unexported edits
  - Keyboard shortcuts: Ctrl/Cmd+Enter saves, Escape cancels, Tab moves title→content
  - All new UI strings translated into all 10 supported languages

### Changed
- Landing page hero copy updated to reflect Browse & Edit capability
- Schema.org `featureList` expanded with "Browse, search, and edit notes in your browser" and "Export edited backups as .jwlibrary"
- `softwareVersion` bumped to `2.4.0`
- Service worker cache bumped to `jwsync-v13`

---

## [2.3.0] — 2025 (approx.)

### Added
- **Note Explorer (Browse)**: self-contained in-browser library viewer
  - Three tabs: Notes, Highlights, Bookmarks
  - Full-text search, color filter, tag filter, publication filter, sort (newest / oldest / by publication)
  - Detail pane with full note content, tags, metadata, copy-to-clipboard
  - Capped at 2 000 displayed rows with "narrow your search" hint
  - Accessible via "Browse Your Notes" CTA on the Simple Mode landing and "Browse notes →" button in the Insights modal
  - Public API: `window.__openJwBrowse(file)`
  - Own `I18N` object (~34 keys × 10 languages)

---

## [2.2.0] — 2025 (approx.)

### Added
- **Merge Web Worker**: all SQLite execution, ZIP decompression, and ZIP recompression run off the UI thread via a dedicated Web Worker (`beta/js/merge-worker.js`)
  - Main thread transfers `ArrayBuffer`s via Transferable Objects (zero-copy)
  - Cancel support: main thread posts `{type:'cancel'}`; worker checks `cancelled` flag every 250 rows

---

## [2.1.0] — 2025 (approx.)

### Added
- **Simple Mode** (default ON for first-time visitors)
  - Segmented pill toggle in nav bar
  - Static teaser banner with "Explore Full Mode →" CTA
  - Preference persisted via `loadPrefs().simpleMode`
- **Tag Suggestion Merge Toggle**: the "Merge →" button in Suggested Merges is a persistent toggle — orange "Merge →" idle, emerald "✓ Applied" when active; clicking again resets to "keep"

---

## [2.0.0] — 2025 (approx.)

### Added
- **Insights**: statistics dashboard modal — study span, activity-over-time chart, most-annotated Bible books, computed entirely in the browser
- **Bulk Colour Changer**: remap highlight colours (6-colour JWL system) before or after merge
- **Tag Manager**: rename, merge-duplicate, and filter tags before committing a merge
- **Import Tag**: stamp all notes imported from a secondary file with a chosen tag

### Changed
- Conflict strategy selector: "base" (keep existing) vs "newest" (replace by `LastModified`)
- Smart dedup toggle: strip HTML and compare note content to catch identical notes with different GUIDs
- Deep clean toggle: remove orphaned TagMap entries post-merge

---

## [1.x] — 2024–2025

### Foundation
- Multi-file merge engine: combine notes, highlights, bookmarks, tags, and input fields from up to N `.jwlibrary` backup files
- Pre-merge deduplication by file hash (SHA-1)
- 10-language UI: English, Spanish, Portuguese, French, German, Italian, Russian, Japanese, Korean, Tagalog
- PWA: offline support, service worker caching, `.jwlibrary` file association via File Handler API
- Sample data demo for first-time visitors
- Community forum (Supabase backend, hash-routed `#forum`)
- Note export: TXT, CSV, HTML, PDF
- Merge report download (`JWSync_Report_YYYY-MM-DD.txt`)

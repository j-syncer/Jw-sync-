# Changelog

All notable changes to JW Sync are recorded here.

---

## [2.9.1] — 2026-05-28

### Added
- **Auto-download on merge complete.** When the celebration dialog opens, the merged `.jwlibrary` file now downloads automatically (one-shot per merge, deduped by blob URL). If the browser blocks the programmatic click (some popup-blocker setups do), the new **Download merged backup** button right at the top of the dialog completes the download with one tap.
- **Re-download button** as the primary CTA — the user no longer has to scroll past the celebration to find the original React download link. A green "Your file is downloading…" confirmation banner appears once auto-download succeeds, and the button label switches to "Download again" so it's clear what a second click does.
- **Donate link** in the celebration footer ("Found JW Sync useful? Support development →") pointing to `paypal.me/jwsync`. Subtle, opt-in, opens in a new tab. Translated in all 10 languages.

### Changed
- Button hierarchy in the celebration: **Download** (primary, filled orange) → **Restore to JW Library** (outline, also brand-coloured) → **Browse the merged result** (secondary, neutral outline). The previous layout buried the download.
- `tests/05_post_merge.js`: 2 new scenarios verify the auto-download programmatically clicks `#download-btn` on merge complete + that it's correctly one-shot per merge.

### Bumped
- `softwareVersion` 2.9.0 → 2.9.1.
- Service worker cache `jwsync-v22` → `jwsync-v23`.

---

## [2.9.0] — 2026-05-28

### Added
- **Post-merge celebration overlay.** When the merge worker finishes and the download anchor's `href` becomes a `blob:` URL, JW Sync now opens a polished full-screen dialog announcing the result. The overlay reads the merged `.jwlibrary` back via sql.js + JSZip (entirely client-side, no server) and shows live counts of notes, highlights, bookmarks, and tags in the merged file — so the user can see at a glance what they just gained.
- **"Restore to JW Library" guide.** Primary CTA on the celebration opens a second dialog with platform-aware step-by-step instructions (iPhone / iPad, Android, Other / Desktop tabs — pre-selected based on `userAgent`) for actually getting the merged file back into JW Library on a real device. Includes a safety warning that restoring replaces the current library.
- **"Browse the merged result" CTA** pipes the merged buffer into the existing Note Explorer so users can immediately verify the merge worked without re-uploading.
- **Demo conversion ramp.** When the user just ran the v2.8.0 sample merge demo, the celebration surfaces an additional "That was a demo · Use my real files →" CTA that clears the file pickers and scrolls back to the upload area — turning the demo into a direct path to first real use.
- Escape key dismisses the overlay; same-blob-URL deduplication prevents duplicate dialogs; new-merge triggers a fresh dialog.
- All overlay short strings (titles, buttons, stat labels, warnings) translated into all 10 supported languages. Long platform-specific step text stays in English for now.
- New `tests/05_post_merge.js` JSDOM suite (18 scenarios) covers overlay rendering, demo CTA gating, restore guide tab switching, Escape/close interactions, and the idempotency guard.

### Bumped
- `softwareVersion` 2.8.0 → 2.9.0.
- Service worker cache `jwsync-v21` → `jwsync-v22`.

---

## [2.8.0] — 2026-05-28

### Changed
- **"Try Demo" now actually demonstrates the merge.** Previously the demo opened Note Explorer with a single sample library — useful, but it showed the secondary feature, not the headline value prop. Clicking any "Try Demo" button (landing hero, top nav, React-rendered nav, Simple-Mode teaser) now boots the app, generates two synthetic `.jwlibrary` backups end-to-end via sql.js + JSZip, injects them into the React file pickers (main + secondary), shows a guidance banner explaining the next step, and pulses the **Preview Merge** button so the user can see the entire merge → preview → confirm → download arc without uploading anything.
- The legacy floating purple "Try with sample data" button (Full-Mode only, first-time-visitor only) is deprecated; its `buildDemoBackups` + `injectFilesIntoMainInput` helpers now power the unified merge demo, so there's a single discoverable path instead of two competing ones.
- Demo banner is i18n-aware — translated into all 10 supported languages. Localised toast on failure too.
- If the user already has real files staged, the demo asks for confirmation before overwriting them (no silent data loss).

### Added
- New CSS: `#jw-demo-banner` guidance overlay, `.jw-demo-toast` success/error notification, `.jw-demo-pulse` highlight animation that briefly draws attention to the "Preview Merge" button after the demo loads.
- `enhancements.js` now exposes `window.__jwBuildDemoBackups()` and `window.__jwInjectMergeDemo(file1, file2)` so the inline demo handler can drive a real merge without duplicating the builder code.

### Removed
- The inline base64 demo payload (`DEMO_B64`, ~3.5 KB) is gone — the merge demo generates its backups at runtime via sql.js + JSZip, which were already needed for the merge UI itself.

### Bumped
- `softwareVersion` 2.7.0 → 2.8.0.
- Service worker cache `jwsync-v20` → `jwsync-v21`.

---

## [2.7.0] — 2026-05-27

### Changed
- **Lazy-loaded heavy bundles for faster first paint.** The landing page no longer downloads React, ReactDOM, JSZip, sql.js, or Lucide upfront — those CDN scripts (~400 KB transferred) are now fetched only when the user navigates to the app, clicks "Try Demo", or hovers a CTA button. Returning visitors who go straight to the app still see the same "Preparing your workspace…" splash; the perceived difference is on landing, where the page becomes interactive almost immediately.
- The inline main React app is now wrapped in `window.__bootApp()` and only executes when needed; the Browse module is wrapped in `window.__bootBrowse()` and runs the first time the demo CTA or the in-app Browse button is used.
- A small inline boot loader (~3 KB) orchestrates lazy loading: it decides whether to boot the app based on URL hash + first-visit flag, listens on `hashchange`, prefetches CDN scripts on hover/focus of "Launch App" / "Try Demo" / site-nav "App", and queues an idle prefetch ~2.5 s after a landing visit so the first click stays snappy.
- The "Try Demo" buttons now show a `jw-demo-loading` spinner state while the Browse module + storage CDNs download on the first click.
- Connection-aware: skips prefetch entirely if `navigator.connection.saveData` is set.

### Added
- New `tests/04_lazy_load.js` JSDOM integration suite (6 scenarios) verifies that landing visits do NOT trigger CDN loads, demo clicks only load Browse + storage (not React), and `#app` navigation triggers the full bundle.

### Bumped
- `softwareVersion` 2.6.1 → 2.7.0.
- Service worker cache `jwsync-v19` → `jwsync-v20`.

---

## [2.6.1] — 2026-05-27

### Added
- **"Try Demo" button on every screen.** The sample-notes demo previously only appeared on the landing page (which shows once per visitor). It now also lives in the persistent top nav and in the React-rendered app nav alongside the existing "Browse notes" button, plus a secondary "Try with sample notes" button next to "Explore Full Mode →" inside the Simple Mode teaser. Returning visitors can always reach the demo.
- New `cta_try_demo_nav` i18n key (short label for nav buttons) translated to all 10 languages.

### Changed
- Demo handler upgraded: exposes `window.__jwOpenDemo()` and binds any element carrying `data-demo-trigger` (including dynamically-mounted React buttons, via MutationObserver). The decoded `.jwlibrary` buffer is cached after first click and cloned per call so the consumer can transfer it freely.
- `softwareVersion` bumped to `2.6.1`.
- Service worker cache bumped to `jwsync-v19`.

---

## [2.6.0] — 2026-05-27

### Added
- **"Try with sample notes" CTA** on the landing page hero — a secondary button alongside "Launch App →" that opens Note Explorer pre-loaded with a small demo library. Visitors can search, filter, tag, recolour, and even export the demo data without uploading a personal `.jwlibrary` file. The demo contains 10 notes, 7 highlights, 3 bookmarks, and 4 tags across 8 publications (Bible references, Watchtower, Awake!, and a study brochure).
- New `cta_try_demo` i18n key with translations for all 10 supported languages (EN, ES, PT, FR, DE, IT, RU, JA, KO, TL).

### Changed
- `softwareVersion` bumped to `2.6.0` (Schema.org JSON-LD in `beta/index.html`).
- Service worker cache bumped to `jwsync-v18`.

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

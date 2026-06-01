# Changelog

All notable changes to JW Sync are recorded here.

---

## [2.25.0] — 2026-06-01

### Added
- **A whole analytics dashboard in "Your Service Year Highlights."** The Wrapped page now goes deep on your study habits — all computed privately in your browser:
  - **Activity heatmap** — a GitHub-style calendar of your note-taking over the last six months.
  - **Streaks** — your longest and most-recent runs of consecutive days with a note.
  - **Study rhythm** — which days of the week you study most.
  - **Growth over time** — an animated chart of your notes accumulating month by month.
  - **Bible coverage** — how many of the 66 books you've annotated, a book-by-book grid, and your Hebrew-vs-Greek-Scriptures split.
  - **Top publications** — your most-annotated publications beyond the Bible.
  - **Words written**, your **longest note**, and what share of your **highlights carry a written note**.
- All new sections are animated, responsive, and fully localized in all 10 languages.

---

## [2.24.0] — 2026-06-01

### Added
- **Mobile polish.**
  - **Offline indicator** — a quiet banner now appears when you lose connection, reassuring you that merging still works and your notes stay on your device. It disappears automatically when you're back online.
  - **Swipe between tabs** in the Note Explorer — swipe left/right to move between Notes, Highlights, and Bookmarks on touch devices.
  - **Haptic feedback** — a subtle vibration on key actions (merging, exporting, switching tabs) on supported devices.

---

## [2.23.0] — 2026-06-01

### Added
- **Share & export notes as Markdown.** In the Note Explorer:
  - Each note's detail pane now has a **"Copy as Markdown"** button — paste a clean, formatted version straight into Obsidian, Notion, Apple Notes, or any Markdown editor (bold, italics and lists preserved).
  - A new **"Export Markdown"** button downloads the notes you're currently viewing as a `.zip` of individual `.md` files, each with YAML frontmatter (title, date, tags, publication). Combine with the date filter or a tag filter to export, say, just one tag's notes as a study guide.

---

## [2.22.0] — 2026-06-01

### Added
- **Smart suggestions in the Merge Conflict Reviewer.** When notes were edited differently on more than one device, a new **"Suggest best"** button now recommends a version for every conflict at once — highlighting it in green with a short reason ("Most recent edit", "Most detailed", or "Has content"). You can accept the suggestions as-is (just click Download) or override any of them. No more reading every conflict from scratch.

---

## [2.21.0] — 2026-06-01

### Added
- **Date-range extraction in the Note Explorer.** The Browse tool now has **From / To date filters** so you can narrow your notes and highlights to any time window — e.g. "everything up to my baptism" or "just this year's notes."
- **One-click "Extract date range".** With a date set, download a brand-new `.jwlibrary` containing **only the notes in that window** — the in-browser way to pull out content from a point in time, exactly as promised on the home page. Your working library is never altered; the extract is a fresh copy.

---

## [2.20.0] — 2026-06-01

### Added
- **Saved Devices & Auto-Sync.** Save each device's `.jwlibrary` backup once, then re-merge them all with a single click — no more re-uploading the same files every time you sync. A new **Sync** button (bottom-right) opens a panel where you can:
  - Add a backup from each device and keep them in one place
  - Choose which device is the "main" base for the merge
  - Merge every saved device instantly and download the unified file
  - Set a gentle **weekly or monthly reminder** to re-sync, with a quiet prompt when it's time
- **Everything stays private.** Saved backups live only in your browser (IndexedDB) and are never uploaded.

---

## [2.19.3] — 2026-05-31

### Fixed
- **Changing the language now updates the home page immediately.** On the first-time landing page (before the main app loads), switching the language picker did nothing because the translations weren't available yet. The landing page now carries its own compact translation set, so the hero, buttons, feature cards, and nav switch language instantly.

---

## [2.19.2] — 2026-05-31

### Fixed
- **Language picker now stays visible on mobile.** On the first-time landing page, the nav language selector could be pushed off the right edge (and clipped) on narrow screens — especially in longer-worded languages. The picker is now pinned and the other nav links give way instead.

---

## [2.19.1] — 2026-05-31

### Fixed
- **"Browse notes" button now works from a cold start.** The button opened the Note Explorer only if the (lazy-loaded) Browse module had already been booted by another action; clicking it from Simple or Full mode without that did nothing. It now boots the Browse module on demand before opening.

---

## [2.19.0] — 2026-05-31

### Added
- **Localized FAQ and How-to** — the homepage FAQ and "How to merge" sections (and their FAQPage/HowTo structured data) are now translated into all 10 languages. Visiting `?lang=es`, `?lang=ja`, etc. — or switching language — shows the content, and the rich-result schema, in that language.

---

## [2.18.0] — 2026-05-31

### Added
- **Homepage FAQ and "How to merge" sections** — clear, on-brand answers (privacy, multi-device merging, .jwlibrary basics, iPhone/Android support) and a 5-step how-to, giving real content for both visitors and search engines.
- **Richer search results** — added `FAQPage` and `HowTo` structured data (plus image/screenshot/author on the app schema) so Google can show rich results.
- **Language URLs** — visiting `?lang=es` (any of the 10 languages) now loads the site in that language, with a self-referencing canonical.

### Changed
- Tightened the meta description and fixed the heading hierarchy for cleaner on-page SEO.

---

## [2.17.2] — 2026-05-31

### Changed
- **"First time? How it works" button now shimmers** with a subtle animated sheen and orange glow so new visitors notice it. Respects `prefers-reduced-motion`.

---

## [2.17.1] — 2026-05-31

### Fixed
- **"First time? How it works" button now opens the guide.** The landing button was wired to a function in a different script scope, so clicking it did nothing. It now correctly opens the export walkthrough.

---

## [2.17.0] — 2026-05-31

### Added
- **Rich-text note editing in the Note Explorer** — editing a note no longer flattens it to plain text. A lightweight built-in editor lets you apply **bold, italic, underline, and bullet lists**, and your note's existing formatting is now preserved when you open it, edit it, and save it. Formatted notes also display with their formatting in the detail pane (and in the linked note shown for a highlight).

### Changed
- Note content is sanitized to JW Library's safe HTML subset on save, so edits round-trip cleanly back into the app.

---

## [2.16.0] — 2026-05-31

### Added
- **Pre-merge impact preview** — before your merged backup is packaged and downloaded, JW Sync now shows a clear summary of exactly what the merge will do: how many **notes, highlights, bookmarks, and tags** will be added, how many notes will be **updated** (newer version wins), and how many **duplicates** were skipped. Confirm with **Merge & Download**, or **Cancel** to back out — nothing is downloaded until you approve. Available in all 10 languages.

---

## [2.15.0] — 2026-05-31

### Added
- **Friendly, specific file errors** — instead of a raw "Error processing file" message, JW Sync now explains exactly what went wrong when a backup can't be read, in all 10 languages:
  - the file isn't a readable `.jwlibrary` (corrupted or wrong type),
  - it's missing its notes database (`userData.db`) — with a prompt to re-export from JW Library,
  - the database couldn't be opened (damaged file).
  - These apply both to the merge pipeline and the Note Explorer (Browse) loader.
- **Large-file heads-up** — merging very large backups now shows a non-blocking notice that it may take longer.

### Changed
- **Note Explorer no longer caps at 2,000 rows** — large libraries are now fully browsable with simple **pagination** (200 per page, Prev / Next), so no notes are hidden behind a "narrow your search" message.

---

## [2.14.0] — 2026-05-31

### Added
- **Guided "How it works" walkthrough** — a new platform-aware (iPhone/iPad, Android, Desktop) step-by-step guide that covers the whole round trip:
  - **Export from JW Library** (new): how to create a `.jwlibrary` backup on each device and gather every device's file in one place, ready to merge.
  - **Restore the merged file**: the existing restore guide is now part of the same modal, with an IN/OUT toggle to switch direction.
  - **"First time? How it works"** button on the landing page hero opens the guide straight to the export steps — so newcomers immediately learn where to get their backup files.
  - Reachable after a merge from the celebration overlay's existing **Restore** button, and programmatically via `window.__jwOpenGuide('export' | 'restore')`.

---

## [2.13.0] — 2026-05-29

### Added
- **`highlights.html` standalone page** — "Your Service Year Highlights" is now a dedicated page (`jwsync.org/beta/highlights.html` and `jwsync.org/highlights.html`) rather than an overlay. Clicking the button from the homepage or inside the app navigates there directly.
  - **← JW Sync back button** in the page header returns the user to the app.
  - **"New file" button** in the header lets the user swap to a different `.jwlibrary` file without leaving the page.
  - **Eager CDN loading**: JSZip and sql.js load immediately when the page is visited — no 10-second wait or "loading" failures.
  - **File passing via IndexedDB**: when the user already has a file loaded in the main app, it is written to IDB (`jwsync_hl_v1 / pending / next`) before navigation so the highlights page auto-analyzes it on arrival. If no file is available, the page shows a file picker immediately.
- **Celebration screen "View Highlights" button** — after a successful merge and download, the celebration overlay now includes a "View Highlights →" button. Clicking it passes the merged `.jwlibrary` buffer to IDB and navigates to `highlights.html` so the user can see their service year stats for the freshly-merged file.
- **`cele_highlights` i18n key** added to all 10 languages in the celebration module (e.g. `en`: "View Highlights →").

### Changed
- **Inline Library Wrapped overlay removed** from `beta/index.html` and `index.html`. All stats functionality lives in `highlights.html` now.
- **Nav buttons updated**: the "Your Service Year Highlights" button in the React nav bar and the Simple Mode teaser now navigate to `highlights.html` (via `__jwGoHighlights()` which handles IDB hand-off) instead of opening an overlay.
- **Static nav button onclick** updated to call `__jwGoHighlights()`.
- **Service worker** bumped to `jwsync-v27`; `highlights.html` added to the precache SHELL so it works offline.

### Tests
- `07_library_wrapped.js` fully rewritten for the standalone-page architecture: extracts the inline script from `highlights.html`, boots it in JSDOM with pre-injected deps, and verifies rendering, service year tabs, All Time switching, empty-library state, file picker, I18N (all 10 langs × 22 keys), nav button wiring, and celebration `cele_highlights` i18n.

---

## [2.12.1] — 2026-05-29

### Changed
- **"Your Service Year Highlights"** — the Library Wrapped feature is now focused on JW service years (September 1 – August 31). The modal is titled "Your Service Year Highlights" and opens to the current service year by default.
  - **Service year tab bar** at the top of the card: shows all service years that have note data (e.g. "2025–26", "2024–25"…), plus an "All Time" tab. Tabs are horizontally scrollable on mobile.
  - **Year-over-year delta badge** on the Notes headline cell: shows "↑ +12" in green or "↓ −5" in red compared to the previous service year, so you can see whether your study pace is growing.
  - **"All Time" tab** aggregates stats across all service years — same view as the original feature.
  - Highlights, bookmarks, and tag counts are always shown all-time (those tables have no date field), with a small "all time" sub-label when a specific service year is selected.
- **Nav button renamed**: the "Library Stats" button in the React nav bar is now labelled "Service Year", and the Simple Mode teaser button says "Year Highlights". Translated into all 10 languages.
- **Removed**: the redundant "Try Demo" button from the top nav bar — Try Demo is already accessible in the mode-controls row and on the landing page. The top-nav slot is now occupied by the shimmering "Service Year" button.
- **Shimmer effect**: both the static-nav "Service Year" button and the React-nav "Service Year" button have a sweeping light animation to draw the eye. Orange accent, no animated gradient — a subtle sweep on a solid background.

### Bumped
- No version bump to `softwareVersion` (UI-only change; version stays 2.12.0 internally).

### Tests
- `07_library_wrapped.js` extended with 7 new assertions: service year tab bar renders, current SY is auto-selected (not All Time), All Time tab can be clicked and activates, all 3 new I18N keys (`all_time`, `service_yr`, `no_data_sy`) verified across all 10 languages.
- `01_static.js` updated: removed assertion for old `.site-nav-demo` button; now asserts `.site-nav-wrapped` is present.

---

## [2.12.0] — 2026-05-29

### Added
- **Library Wrapped** — a Spotify-Wrapped-style stats card for your JW Library backup. Open it via the new "📊 Library Stats" button in the nav bar or the "Your Stats" button in the Simple Mode teaser. It reads your `.jwlibrary` file locally (nothing leaves your device) and shows:
  - **4 headline numbers** — total notes, highlights, bookmarks, and tags, each counting up in an animated easeOut reveal.
  - **Most Studied Books** — a horizontal bar chart of up to 8 Bible books ranked by note count, with full book names.
  - **Activity by Year** — a vertical bar chart showing how many notes you wrote each year, so you can see your study history at a glance.
  - **Your Tags** — all your custom tags with their note counts as badges.
  - **Highlight Colors** — a segmented color bar showing the breakdown of your 6 highlight colors.
  - **Study span facts** — first note date, latest note date, total years of study, and your single most-active month.
  - **Copy stats** button — copies a clean plain-text summary to the clipboard for sharing.
- New "📊" nav button ("Library Stats") and "Your Stats" Simple Mode teaser button — both wired to `window.__openJwWrapped(window.__jwLastFile)`. Translated into all 10 languages.

### Why
- The merge and browse features answer *what* is in your library. Wrapped answers *how much* — a rewarding, visual snapshot of years of personal Bible study in one beautiful card.

### Notes
- Fully internationalised (19 keys × 10 languages, self-contained `I18N` object inside the module).
- Self-contained `<style>` + `<script>` IIFE block; all CSS prefixed `.jww-*` to avoid collisions. Z-index 10070 (above Browse at 10050, above Conflict Reviewer at 10060).
- Loads sql.js and JSZip on demand from CDN; gracefully falls back to a file-picker prompt if `window.__jwLastFile` is not set.
- No CDN scripts fetched until the user opens Wrapped.

### Bumped
- `softwareVersion` 2.11.0 → 2.12.0 (both beta and production).
- Service worker cache `jwsync-v25` → `jwsync-v26`.

### Tests
- New suite `07_library_wrapped.js` (28 assertions): boots the module in JSDOM with real JSZip + sql.js, fabricates a `.jwlibrary` with notes/highlights/bookmarks/tags across multiple Bible books and years, and verifies overlay rendering, all 4 headline stat cells, top-books bar chart, year timeline, tags section, color bar, facts section, copy button, close button, Escape key, empty-library "no notes" message, graceful no-crash when deps are absent, I18N coverage (19 keys × 10 langs), and nav/teaser button wiring in `app.js`. Wired into `npm test`.

---

## [2.11.0] — 2026-05-29

### Added
- **Merge Conflict Reviewer** — the headline feature. When the same note was edited differently on more than one device, JW Sync no longer silently picks a winner behind your back. After a merge (and before the file downloads), a review screen now shows every conflicting note **side by side**, with a word-level diff highlighting exactly what changed between versions. For each conflict you can:
  - **Keep this** — pick whichever version wins (the version currently in the merge is badged "In your merge").
  - **Keep both** — add the other version as a separate note so nothing is lost.
  - **Keep merge as-is** — accept the automatic choice and continue.
  Your picks are written straight into the merged backup on your device (still 100% local, no uploads), and the corrected file is what downloads. If there are no conflicts, nothing changes — you go straight to the celebration + download as before.
- New landing feature card: **"Review before you download"**, translated into all 10 languages.

### Why
- The merge used to be a black box: you couldn't see what happened to a note you'd edited on two devices. The reviewer turns JW Sync from "trust me" into "see for yourself" — full transparency over your own notes.

### Notes
- Fully internationalised (reviewer UI ships its own ~17-key string table across all 10 languages).
- Self-contained module injected before the celebration block; reads/writes `Note` on the main thread via sql.js (the merge worker is untouched).

### Bumped
- `softwareVersion` 2.10.0 → 2.11.0 (beta).
- Service worker cache `jwsync-v24` → `jwsync-v25`.

### Tests
- New suite `06_conflict_review.js` (~20 assertions): boots the reviewer in JSDOM with real JSZip + sql.js, fabricates two conflicting backups + a merged output, and verifies conflict detection, side-by-side rendering with diff highlights, "Keep this" override (DB rewritten, note count unchanged), "Keep both" (alternate added as a second note), and every short-circuit path (identical notes, missing deps, single backup all resolve to null with no overlay). Wired into `npm test`.

## [2.10.0] — 2026-05-28

### Changed
- **Main React app bundle extracted to `beta/js/app.js`** (code splitting). Previously, the entire ~241 KB minified app was inlined inside `beta/index.html` and downloaded by every visitor — including bouncers who never clicked anything past the hero. v2.10.0 moves the bundle to its own file and treats it as one more lazy dependency the boot loader fetches alongside React + sql.js + JSZip. **`beta/index.html` shrinks from 397 KB to 158 KB** (a 60% drop).
- The boot loader's `bootApp()` now does `Promise.all([loadReact(), loadStorage(), loadAppBundle()])`. `loadAppBundle()` injects `<script src="js/app.js">` on demand and resolves on `onload`.
- Hover/idle prefetch (`prefetchAll`) adds a `<link rel="prefetch" as="script" href="js/app.js">` hint alongside the CDN scripts, so a visitor hovering "Launch App" pre-warms the app bundle.
- **First-time landing visitors do NOT download `js/app.js`** — the win this commit is named after. Verified by a new `04_lazy_load.js` scenario.

### Bumped
- `softwareVersion` 2.9.1 → 2.10.0.
- Service worker cache `jwsync-v23` → `jwsync-v24`. (Same-origin scripts go through `staleWhileRevalidate`, so `js/app.js` gets its own cache entry separate from `index.html`. HTML copy tweaks no longer invalidate the JS bundle, and JS updates no longer re-download the HTML.)

### Tests
- `01_static.js` — new `bundleSrc` resolution: read TRANSLATIONS + parse the main bundle from `beta/js/app.js` when it exists, fall back to the inline `<script>` block otherwise (so production, which hasn't been mirrored yet, still passes). Added 7 new assertions for the extraction (bundle not inline in HTML, `js/app.js` exists with `__bootApp` wrapper, boot loader has `loadAppBundle`, `js/app.js` in prefetch list and NOT in `<head>`, `Promise.all` chain awaits it).
- `03_regression.js` — merge anchors (`ja=async e=>`, `className:"modal-close"`, `Preview Merge`, etc.) now searched across both `beta/index.html` and `beta/js/app.js`.
- `04_lazy_load.js` — 4 new assertions covering the lazy-load chain for `js/app.js`: fetched on returning-visitor boot, NOT fetched on first-time landing, fetched on demo click, fetched on `#app` hashchange, and prefetched on hover.

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

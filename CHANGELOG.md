# Changelog

All notable changes to JW Sync are recorded here.

---

## [2.99.0] — 2026-08-04

### Added: Arabic — the site's first right-to-left language

JW Sync now speaks Arabic, and the whole interface flips to read right-to-left
when you pick it. Choose **العربية** from the language menu, or open any page
with `?lang=ar`.

- **Every screen is translated** — the landing page, the merge app, Study
  Explorer, Study Stats, Note Sharing, Library Doctor, Reading Companion,
  Resurface, the conflict reviewer, the merge celebration and the tool
  switcher. 1,027 strings across all 30 dictionaries.
- **Real right-to-left layout**, not just Arabic text in a left-to-right page.
  Navigation, cards, step lists, toolbars, modals and the Explorer's list and
  detail panes all mirror. The direction is set before the page paints, so
  there is no flash of the wrong layout.
- **Mixed-language notes read correctly.** If your interface is Arabic but a
  note is written in English, that note keeps its own direction — no more full
  stops jumping to the wrong end of the line.
- **Bible chapter links** open in Arabic on jw.org.
- **All 37 guides are available in Arabic** at `jwsync.org/guides/ar/`, with a
  language switcher on every guide page. The English guides keep their
  existing URLs.

### Added: multilingual SEO

- **Localized page title and description in all 13 languages.** Previously
  every language shared the English title and meta description; each language
  now gets its own, so search results and shared links read in your language.
- **The Arabic guides are properly indexable** — each one is a real page with
  its own canonical URL, `hreflang` alternates linking it to its English twin,
  and Arabic structured data. All 114 guide URLs are in the sitemap.
- **Fixed:** the Schema.org `inLanguage` list had never been updated when
  Swedish shipped, so it advertised 11 of the 12 languages the site served. It
  is now generated from a single language list along with everything else.
- **Fixed:** `sitemap.xml` submitted `highlights.html` and `share.html`, which
  the server redirects; those pages also had no canonical URL of their own.
  Both now use their extensionless URLs.
- **Fixed:** opening a tool with `?lang=` deep link (as the Arabic guides do)
  left parts of the page in English, because only the landing page remembered
  the choice. Every page now does.

---

## [2.98.1] — 2026-08-02

### Fixed: the accessibility issues PageSpeed Insights reported

Lighthouse flagged three things on jwsync.org; all three are fixed.

- **No main landmark.** The landing content, the merge app and the contact card
  now sit inside a single `<main>`, so screen-reader users get a "skip to main
  content" target. The embedded Community view has its own `<main>`, so the
  page's landmark is hidden while that view is open — a document must expose
  exactly one.
- **Contact button contrast.** White on the brand orange is 3.6:1, below the
  4.5:1 minimum for text under 19px. The support-email button now uses a
  slightly deeper shade of the same orange: 5.2:1.
- **Footer contrast.** The footer's links line was 4.1:1 against the near-black
  footer; its text is now one step lighter, at 7.8:1.

The same white-on-orange problem appeared in two more places, so those are
fixed too: the "NEW" badge on the tool cards, and the buttons and numbered
step markers on the guide pages. The guide footer, at 4.0:1, was lightened to
6.6:1.

Tests now compute the actual WCAG contrast ratios for these colour pairs, so a
future palette change can't quietly drop them back below AA.

## [2.98.0] — 2026-08-02

### Go live: Reading Companion card and Library Doctor auto-mode

Two features that had been sitting in beta are now on jwsync.org.

- **Reading Companion** now has its own card on the landing page, carrying the
  NEW badge (moved off Library Doctor, which has been live for a while), with
  its description and tags in all 12 languages. `js/reading.js` was already
  shipping to both sites, so only the landing-page wiring was missing.
- **Library Doctor auto-mode** — the code path that lets the Doctor be opened
  in "scan, clean and hand back one download" mode, plus its Download-your-file
  and cleaned-backup-ready strings in all 12 languages.

Also fixed while promoting:

- Production had the merge-tool redesign `<style>` and its companion script
  **twice** — a duplicated block left by an earlier go-live, which meant two
  elements sharing each id and two MutationObservers stripping emoji from the
  same nodes. Production now carries one copy, as beta always did.
- `index.html` and `beta/index.html` now differ only by the five things that
  should differ between them: title, canonical, robots, the BETA banner and
  the guides link.

## [2.97.1] — 2026-08-02

### Fixed: Guides link 404'd on the beta site

The Guides links in the beta site's nav bar and footer were relative, so from
`/beta/` they pointed at `/beta/guides/`, which does not exist — the guides are
a single set served from `/guides/`. Both links are now absolute. Production
was unaffected.

## [2.97.0] — 2026-08-02

### Added: tag filter in the Share page's note picker

Picking the notes to share used to mean searching and ticking. Sharing is
usually organised around a tag, though — an event, a subject, the person you
study with — so the picker now filters by tag directly.

- A tag dropdown above the note list shows every tag in the backup with the
  number of notes carrying it. Choose one and the list narrows to those notes;
  **Select all** then ticks exactly that set, so sharing a tag is two clicks.
- Each note in the list shows the tags it carries, so you can see what you are
  about to send.
- The search box now matches tag names as well as titles, note text and
  publication, and it combines with the tag filter to narrow further.
- An empty result now says so instead of showing a blank list.
- The tag filter is hidden for backups that have no tags, and it survives
  select-all and search re-renders.

The sharing guides were updated to describe the one-click flow, including the
convention-notes guide, which had described a tag filter before one existed.

## [2.96.0] — 2026-08-02

### Added: 12 scenario guides in the Guides & How-tos section

The guides section grows from 25 to 37 pages. Where the existing guides explain
a feature, these explain a situation — the moment someone actually reaches for
the tool — which is also how people search for it.

Two new sections on `/guides/`:

- **Sharing scenarios** — share only the notes under one tag; share study notes
  with someone you study the Bible with; send the week's meeting notes to the
  family; open notes somebody shared with you; swap research with a study group;
  hand off the research behind a talk or assignment.
- **Everyday scenarios** — prepare for the meeting using notes you already
  wrote; print your notes; clear out duplicate and empty notes with Library
  Doctor; back up before a factory reset or repair; help a family member move
  their notes.

Also added under **Fixing problems**: what to do when notes are missing after an
app update, reinstall or restore — including the mistake that makes it
unrecoverable.

- Each page carries Article + HowTo + BreadcrumbList + FAQPage structured data,
  a unique title and meta description, steps, FAQs and related-guide links.
- The 12 new URLs are in `sitemap.xml`, and existing guides now link to the new
  ones, so the whole section is better connected internally.
- Corrected a step in the convention-notes guide that described selecting notes
  by tag filter on the share page; selection there is by search and ticking.

## [2.95.1] — 2026-07-28

### Fixed: Search Console "Alternate page with proper canonical tag"

Google reported the site's 12 language URLs as unindexed because every one of
them was a duplicate that pointed back at the homepage. The landing page is a
single document that translates itself in the browser, so `?lang=es` and friends
send Google byte-identical English HTML — submitting them as separate pages could
never index anything extra, it only produced the warning.

- `sitemap.xml` now submits the homepage once instead of 13 near-identical
  copies, and points at `/forum` rather than the `/forum.html` URL the server
  redirects away from.
- Removed the `hreflang` alternates and the script that rewrote the canonical
  link to the `?lang=` URL — two signals that contradicted the page's own
  canonical tag.
- Language links still work exactly as before: `?lang=es` continues to open the
  site in Spanish and remember the choice.
- `forum.html` now declares its canonical as `/forum`.

## [2.95.0] — 2026-07-21

### Added: 13 more guides in the Guides & How-tos section

Expanded jwsync.org/guides/ from 12 to 25 pages, adding a use-case guide for
every remaining feature and the long-tail JW Library searches people make:

- Getting started: what a .jwlibrary file is and how to open it, using JW
  Library backups on a Windows PC.
- Fixing problems: recovering notes after a lost/broken/reset phone, handling
  merge conflicts when the same note was edited on two devices.
- Power tools: exporting notes to text/Markdown, organizing & cleaning up tags,
  managing & recolouring highlights, viewing fill-in Study Answers, extracting
  notes by date range, the Study Map knowledge graph, reviewing old notes with
  Resurface, study streaks/levels/achievements, and sharing convention/assembly
  notes.

Each page carries step-by-step instructions, FAQs, and Article + HowTo +
BreadcrumbList (+FAQPage) structured data, and is listed in sitemap.xml. Pages
are generated by scripts/build_guides.py; test suite 17_guides.js covers all 25.

## [2.94.0] — 2026-07-21

### Added
- The **"What else can JW Sync do?"** panel shown after a merge (Simple Mode)
  now has an **Explore Full Mode →** button, so you can jump straight to the
  advanced tools it describes instead of hunting for the mode switch.
  Translated in all 12 languages.

## [2.93.2] — 2026-07-21

### Changed
- On the post-download celebration window, the "support development" donation
  link now sits directly above the **Download again** button, and is a little
  larger with a subtle shimmer so it's easier to notice.

## [2.93.1] — 2026-07-13

### Changed
- Added a **Guides** tab to the homepage navigation bar (next to Community),
  linking to the new Guides & How-tos section — translated in all 12 languages.

## [2.93.0] — 2026-07-13

### New: Guides & How-tos section (jwsync.org/guides/)

Twelve static, search-indexable guide pages covering every JW Sync tool and the
most common JW Library backup questions:

- Getting started: merge backups from two devices, keep multiple devices in
  sync, transfer notes to a new phone, move Android ↔ iPhone, back up properly.
- Fixing problems: restore replaced your notes (merge instead), fix a corrupted
  backup with Library Doctor.
- Power tools: Study Explorer (view/edit notes), Ask Your Library (semantic
  search), Study Stats, note sharing, Reading Companion.

Each page has step-by-step instructions, FAQs, Article/HowTo/FAQ structured
data, and is listed in sitemap.xml. New footer links (Guides · Community ·
Study Stats) on the landing page. Pages are generated by
`scripts/build_guides.py`; new test suite `17_guides.js` guards them.

## [2.92.1] — 2026-07-13

### Fixed
- **Google can find jwsync.org again.** The production homepage had been
  shipping a `noindex, nofollow` robots meta tag since v2.72.0 (introduced
  accidentally during a head-section restructure), which told search engines
  to drop the site from their index entirely. The tag is now `index, follow`.
  The beta site (`/beta`) intentionally keeps `noindex` so it never competes
  with the main site in search results.
- Refreshed `sitemap.xml` last-modified dates to prompt a recrawl.

## Feature highlights — recent updates

A themed summary of what's been added over the last few weeks, since the
version-by-version notes below don't always capture the full picture. Everything
runs in your browser — your files are never uploaded.

### 📊 Study Stats
- A dedicated Study Stats page: headline totals (notes, highlights, bookmarks,
  tags), Service-Year and All-Time views, and year-over-year growth.
- Private analytics: activity heatmap, longest/current streaks, weekly rhythm,
  growth over time, and busiest hours and months.
- Bible coverage across all 66 books, with a Hebrew/Greek-Scriptures split.
- Visualizations: study gauges, a 24-hour study clock, seasonality radar,
  highlight colour wheel, Bible-progress ring, note-depth histogram, word cloud.
- A six-trait Study Profile (Consistency, Diligence, Depth, Breadth, Reflection,
  Steadiness) and a "Study Signature" persona (e.g. Reflective Writer, Night Owl,
  Morning/Afternoon/Evening Studier, Midnight Oil).
- Your Study Story timeline, a "What's Next" forecast, and a Shareable Card.

### 🏆 Achievements & Study Journey
- Study Journey: 60 levels across 12 named tiers (Seed → … → Evergreen) with a
  colour-shifting orb and level-up celebrations; lifetime-based.
- ~200 awards with rarity (Common → Legendary) and "Appreciation" points.
- Content-aware, themed medals (e.g. Prayer Warrior, Truth Seeker, Kingdom
  Ambassador, Hopeful Heart, Wisdom Keeper) in distinct shapes.
- Distinguished Honors cabinet, clickable medal popups with progress.

### 🕸️ Study Map
- A private, interactive knowledge graph linking notes by shared scripture,
  shared tags, and similar wording.
- Topics ↔ Notes views, hover-to-spotlight, drag, a strength slider, manual
  "study chains", full-screen mode, and image (PNG) export.

### 🔎 Study Explorer
- Ask Your Library: on-device, offline-capable semantic search (find notes by
  meaning, not keywords), with WebGPU acceleration and a choice of models.
- Rich-text note editing (bold/italic/underline/lists) with formatting preserved.
- Bulk editing (retag, recolour, delete) with full Undo/Redo.
- Study Answers tab (view/edit JW Library fill-in answers).
- Date-range extraction to a fresh backup; Markdown copy/export; pagination for
  large libraries.

### 🤝 Note Sharing
- Send/receive specific notes as a small file (no server, no account).
- Shared highlights travel with their notes; your own notes are never overwritten
  (you choose how clashes are added); imported notes are tagged for easy finding.
- A dedicated, step-by-step Share page.

### 🔀 Merging
- Pre-merge impact preview before anything downloads.
- Merge Conflict Reviewer with side-by-side word-level diff and "Suggest best".
- Saved Devices & Auto-Sync with weekly/monthly reminders.
- Safe Restore reassurance, a share-your-result card, merge-performance
  breakdown, and clearer file-error messages.

### 🧭 Onboarding & workspace
- Platform-aware "How it works" guide (export → merge → restore).
- Redesigned home page with the four tools as cards.
- One shared workspace — load a file once and it follows you between tools
  (kept only in your browser, auto-cleared, wiped on "Start over").
- Built-in sample notes to try without uploading.

### 🌍 Languages
- Added Swedish and Cebuano — the entire app (not just the home page) is now
  translated into 12 languages.
- Localized FAQ/How-to and per-language URLs.

### ✨ Design, accessibility & performance
- A visual refresh (softer hero, calmer card hovers, cleaner section styling).
- Accessibility & mobile polish: higher-contrast text, larger touch targets,
  offline indicator, swipe-between-tabs, haptic feedback.
- Faster first load (lazy-loading/code-splitting) and improved SEO across all
  12 languages.

---

## [2.92.0] — 2026-07-13

### New tool: Reading Companion — a daily Bible reading plan with your notes beside you (beta)

A brand-new daily habit, built around something no generic reading tracker can
do: because JW Sync reads your own `.jwlibrary`, **today's reading shows the
notes and highlights you yourself made on those exact chapters** — "you
highlighted four verses in Psalm 37 two years ago." Reading the Bible through
the lens of your own study history, 100% on your device.

- **Pick an order and a pace.** Read in Bible order or in approximate
  chronological order; finish in 3 months, 6 months, 1 year, 2 years, or set
  your own chapters-per-day pace — with a live "you would finish around…"
  preview.
- **Today's reading, every day.** Each chapter is one tap away — links open
  directly in JW Library (or Watchtower ONLINE LIBRARY) in your language.
  Check chapters off as you read.
- **Streaks without guilt.** Completing a day grows your streak; missing a day
  just moves your forecast finish date. No overdue pile, ever.
- **Your notes on today's chapters.** If you've loaded a backup in any JW Sync
  tool, your own notes and highlight counts appear right under today's portion.
- **Progress you can see.** A 66-book progress grid, chapters-read bar, and an
  on-pace-to-finish forecast.
- **Milestones.** Finish a book, the Hebrew-Aramaic Scriptures, the Christian
  Greek Scriptures — and eventually the whole Bible.
- Fully private (everything in your browser), fully translated in all 12
  languages. Find it on the home page: **Reading Companion**.

## [2.91.1] — 2026-07-11

Performance release driven by Core Web Vitals field data (Cloudflare Web Analytics):
interaction responsiveness (INP) and load-time tail (LCP) improvements.

- **Faster Browse search** — typing in the Note Explorer search box no longer
  re-parses every note's HTML on each pass; searchable text is now cached per
  row (was up to ~770 ms of main-thread blocking on large libraries).
- **Smoother file loading** — the backup scanner now yields to the browser
  before opening the database, so the "file loaded" state paints immediately
  and the next tap on the second drop zone isn't delayed (was up to ~700 ms).
- **Snappier "Launch App"** — the hero CTA and "Try with sample notes" buttons
  now pre-fetch the app bundle on hover/touch, like the other launch buttons.
- **Faster first paint** — Google Analytics now loads after the page finishes
  loading instead of competing with it; below-the-fold landing sections
  (how-to, FAQ) skip rendering until scrolled into view.
- **Less layout shift** — icon placeholders are sized before the icon library
  swaps them in, so the app view no longer shifts when icons appear.

## [2.91.0] — 2026-07-07

### Community navigation overhaul
- Opening a post now gets its own address (`#forum/post/…`), so the browser or
  phone back button closes the post and returns you to the post list instead of
  kicking you out of the Community area entirely.
- Fixed a bug where leaving a post via the browser back button froze scrolling
  on the rest of the app until the page was reloaded.
- Fixed the "← Back to community" button being hidden behind the navigation bar
  on phones — the post view is now full-screen on small displays.
- The "← Back to community" button now stays pinned to the top while you scroll
  a long post, so the way back is always one tap away.
- Previous / next links under each post let you move between posts without
  returning to the list first.
- New "Copy link" button on every post — share a direct link that opens that
  exact post.
- The standalone community page (forum.html) got the same back-button and
  sticky-back-button fixes.

## [2.90.0] — 2026-07-04

### Library Doctor: review duplicates before anything is deleted

Library Doctor now shows you exactly what it found **before** it cleans. After
the health scan, tap **Review changes** to open a clear list:

- **Every duplicate note laid out** — its title and a preview of the text, with
  a **1 kept** / **N to remove** badge so you can see which copy stays and which
  goes.
- **A tick box on each item.** Uncheck any individual duplicate — or any other
  cleanup category (empty notes, duplicate highlights, orphaned data, unused
  tags and leftover locations) — and it's left completely untouched.
- **Nothing is deleted until you confirm.** As always, your original file is
  never changed; fixes go into a fresh copy you download.

This comes straight from a community request — thank you Lukas! Fully translated
in all 12 languages.

## [2.89.0] — 2026-07-04

### Share your merge to Instagram & social media

The post-merge celebration now has a proper **Share** experience. Tap **Share**
and you get a preview of a clean, branded card showing your combined totals —
notes, highlights, bookmarks and tags — ready to post:

- **See it before you share.** A preview of the square (1080×1080) card appears
  right in the celebration, so you know exactly what your friends will see.
- **One tap to share.** On a phone, tap **Share** and pick Instagram (Stories or
  feed), WhatsApp, or anywhere else — the image comes along automatically.
- **Save image** downloads the card so you can post it manually — handy on a
  computer, where you save it and upload to Instagram.
- **Copy caption** copies a friendly, ready-to-paste caption that invites others
  to try JW Sync.
- Encouraging, on-brand copy and full translations in all 12 languages.

It's an easy way to celebrate combining your library — and to help friends
discover a free, private way to sync their own JW Library notes.

## [2.88.0] — 2026-06-23

### The home page now shows what's *inside* each tool

The "Choose a tool" cards on the home page used to hint at only the surface of
each tool. Now every card carries a short row of tags naming the powerful
features tucked inside — so you can see at a glance what JW Sync can really do
before you dive in:

- **Merge Tool** — Conflict reviewer · Auto-sync
- **Library Doctor** — Find duplicates · 1-tap fix
- **Study Stats** — Achievements · Study Map
- **Study Explorer** — Ask your library · Bulk edit
- **Note Share & Receive** — No account · Highlights too

These were always there; they were just hard to discover. The tags are fully
translated into all 12 languages.

## [2.87.1] — 2026-06-23

### Resurface is now woven into the moments you're already in

Based on feedback, Resurface is no longer a separate tool you have to open.
Instead, the daily review now appears right where you already are:

- **On the merge celebration screen.** After you combine your backups, a small
  "Resurface" panel invites you to revisit a note you wrote on this day before
  you move on.
- **On the Study Stats page.** Your daily review sits at the top of your stats,
  so checking your progress and revisiting a past note happen in one place.
- The standalone home-page tool card and full-screen view have been removed —
  Resurface is now a gentle add-on, not its own destination.
- Your review streak and spaced-repetition schedule carry over unchanged and
  are shared across both spots.

## [2.87.0] — 2026-06-22

### 🌅 New tool: Resurface — your daily study review (beta)

A brand-new reason to come back every day. Resurface gently brings your own
past notes back to you — privately, entirely on your device.

- **On this day.** Notes you wrote on today's date in years gone by float to
  the top — rediscover an insight you'd long forgotten.
- **A daily review deck.** Each day Resurface hands you a small set of notes to
  revisit, using light spaced repetition so older and rarely-seen notes resurface
  over time. Read each one, tap **Mark reviewed**, and move on.
- **Build a streak.** Finishing the day's deck grows your review streak, with
  your best streak and total notes reviewed shown when you're done.
- **Remember this library (optional).** Tick "Remember this library on this
  device" and your daily review is ready the moment you open it next time —
  stored privately in your browser (IndexedDB), never uploaded.
- Opens from the new **Resurface** card on the home page, reuses the file you've
  already loaded in another tool, and is fully translated in all 12 languages.

## [2.86.1] — 2026-06-21

### A more premium look for the merge tool
- The merge tool's panels and secondary buttons moved from a flat gray-slate to
  a cool blue-slate with a subtle marble-like depth — two soft static blooms give
  the cards a polished, premium feel without competing with the brand orange.

## [2.86.0] — 2026-06-21

### The polish reaches the merge tool itself
- The merge tool's cards now rise gracefully into view as you scroll — the same
  one-shot entrance as the landing page, now where you actually spend your time
  on a phone. Reduced-motion users are unaffected.
- The merge panel's warm orange glow was retuned for phones to bloom top and
  bottom (the sideways glow was being clipped by the screen edges), so the
  signature aurora is finally visible on mobile.

## [2.85.1] — 2026-06-21

### Scroll reveals now read clearly on phones
- The entrance animation travels further and adds a subtle lift-and-scale, with
  a longer stagger, so the effect is obvious on a narrow single-column layout —
  not just on wide desktop rows. Still one-shot and reduced-motion-safe.

## [2.85.0] — 2026-06-21

### The landing page now comes alive as you scroll
- Sections gracefully rise into place the first time they enter view — the
  hero, the tool cards, the feature grid, the how-to steps, and the FAQ each
  fade and lift, with cards in a row staggering one after another.
- It plays once per section (no looping, no distraction) and is completely
  turned off for anyone who prefers reduced motion.

## [2.84.1] — 2026-06-21

### The merge tool now glows too
- The main merge panel now carries the same warm orange "aurora" bleed as the
  landing hero — a soft halo of brand color radiating from behind the card,
  intensifying gently on hover. Beta dark mode only; production untouched.

## [2.84.0] — 2026-06-21

### A more beautiful landing hero
- The headline is now a true display title — larger, tighter, and weighted, with
  graceful balanced line-wrapping so it never breaks awkwardly.
- A soft, static orange "aurora" now glows behind the hero, giving the page
  warmth and depth against the cool navy backdrop (no animation, no flicker).
- A subtle orange accent underline sits beneath the headline, and the supporting
  text was refined for cleaner rhythm and readability — in both dark and light.

## [2.83.0] — 2026-06-20

### Merge tool redesign now live
- The redesigned merge experience — single "Advanced options" control instead of the Simple/Full switch, refined glass surfaces, tactile shimmering buttons, and per-feature metallic accents — is now live on the main site, not just the beta preview.

## [2.82.3] — 2026-06-19

### Shimmering "Create My Merged Backup" button (beta)
- The advanced-view "Create My Merged Backup" button now shimmers with the same gold sheen and pulse as the main merge button, and shows a calm metallic slate (instead of dead gray) when disabled. Honors reduced-motion preferences.

## [2.82.2] — 2026-06-19

### Shimmering download button (beta)
- The post-merge "Download" button now shimmers with an emerald sheen and gentle pulse, matching the main merge button so the whole flow feels cohesive. Honors reduced-motion preferences.

## [2.82.1] — 2026-06-19

### Shimmering main merge button (beta)
- The big "Merge My Files Now!" button now shimmers with a warm gold sheen and a gentle energy pulse when it's ready to use. When it's disabled it's a calm metallic slate instead of dead gray. Honors reduced-motion preferences.

## [2.82.0] — 2026-06-19

### Shimmering advanced-feature bubbles (beta)
- Each minimized advanced tool now has its own distinct metallic, shimmering accent: Extract & Share (emerald), Bulk Color Changer (sapphire), Manage Tags (amethyst), and Merge Settings (gold). The sheen drifts slowly and speeds up on hover. Honors reduced-motion preferences.

## [2.81.3] — 2026-06-19

### Finer detail + polish on the merge tool (beta)
- Added a detail pass for a more professional finish: refined hairline panels, text fields with a clear focus glow, premium stat tiles with embossed numbers, a crafted glow on card-header icons, slim custom scrollbars, on-brand text selection, and crisper text rendering.

## [2.81.2] — 2026-06-19

### Sleeker, more refined merge tool (beta)
- Retuned the merge tool toward a calmer, more premium "Apple-like" finish: neutral graphite surfaces, fine hairline highlights and large soft shadows instead of heavy bevels, with the accent color used more sparingly.
- The "100% private" badge is now a compact, embossed pill instead of a big empty box on mobile.

## [2.81.1] — 2026-06-19

### Deeper, more tactile merge tool (beta)
- Pushed the merge tool's new look further: cards now have crisp beveled edges with a bright top highlight and layered shadows so they feel like real raised panels, inner sections sit recessed inside them, and every button (orange and gray) has a glossy, pressable 3D cap.

## [2.81.0] — 2026-06-19

### A more beautiful merge tool (beta)
- Big visual refresh of the merge screen: flat panels are now elevated glass cards with depth, a soft ambient glow sits behind the page, and the buttons have a real tactile feel — they lift on hover and press down when clicked.
- Drop zones look like inviting drop targets, and the floating "files ready" bar is now a glassy, glowing action bar.

## [2.80.0] — 2026-06-19

### Merge tool — simpler by default (beta)
- Removed the confusing Simple/Full mode switch on the beta site. The merge tool now opens in the clean step-by-step flow by default, with a single quiet "Advanced options" button that reveals the full toolset when you want it — and tucks it away when you don't.
- First step toward a calmer, more beautiful merge experience; more polish to follow.

## [2.79.1] — 2026-06-17

### Removed
- Removed the experimental printable Study Guide (PDF) from the beta build. It didn't print reliably across devices, so it has been pulled while we reconsider the approach. No other features are affected.

## [2.76.2] — 2026-06-17

### Home page spacing
- Evened out the vertical rhythm of the landing page: the hero now has more breathing room above the tool grid, and the gap before the "Everything you need" section matches the spacing used between the other sections.

## [2.76.1] — 2026-06-17

### Accessibility
- Improved the contrast of the footer privacy tagline and the legal-notice disclosure links so they meet WCAG AA in both dark and light themes. (The main landing copy already passed; these footer items were the exceptions.)

## [2.76.0] — 2026-06-17

### Community page brought in line with the rest of the site
- The Community/forum view now uses the same Inter typeface as the rest of JW Sync instead of a different font, for one consistent look.
- Replaced the blue accents and the book emoji logo with the orange brand colour and a clean chat icon.
- Voting, reaction, and hover highlights now use the brand orange instead of blue.

## [2.75.0] — 2026-06-17

### Home page polish
- The hero now leads with a clear primary call-to-action — **Launch App →** — alongside a quiet "Try with sample notes" option, so you can start without scrolling.
- Unified the home page around the single orange brand accent: the tool cards and the "Study Stats" / "Study Explorer" navigation links no longer use competing cyan, violet, or amber colours.
- Calmer, more focused motion: removed the always-on shimmer and glow loops from the navigation and buttons. Hover feedback is kept.
- Harmonized the "Everything you need" feature cards with the tool cards above them — matching icon sizes, type scale, and hover lift for one cohesive look.

## [2.73.0] — 2026-06-13

### Changed (beta preview)
- **The merge tool is cleaner and more professional on jwsync.org/beta.** The
  redundant second header (a duplicate logo + language picker that sat right
  under the site nav) is gone, and the toolbar no longer repeats Study Explorer
  and Community (they already live in the site nav) — so there's a single nav
  and one tidy toolbar. Emojis were removed from the tool's buttons (including
  the main "Merge My Files Now!" button), and the app's warm-grey surfaces now
  use the brand's cool navy. Works in dark and light themes and on mobile.
  Production is unchanged until this goes live.

## [2.72.0] — 2026-06-13

### Changed (beta preview)
- **The Community forum is now on-brand on jwsync.org/beta.** It previously
  used a blue accent and a multi-colour gradient logo with emoji buttons. On
  beta it now uses the orange brand colour, a flat orange logo, and clean line
  icons on the New Post button and the Questions / Bugs / Features / General
  filters (the category dropdown drops its emojis too). Production is unchanged
  until this goes live.

## [2.71.0] — 2026-06-13

### Changed
- **Study Stats loading and error screens now match the welcome card.** While
  your file is being read, the spinner and "Analyzing your library…" message
  now sit inside the same card, so opening a file feels like the card is
  working rather than the page going blank. If a file can't be read, you get a
  clean card with a red alert icon, the message, and an orange "Open File"
  button to try again — consistent with the rest of the site.

## [2.70.0] — 2026-06-13

### Changed
- **Unified, more professional navigation across the tools.** The Study Stats
  and Share pages now share one polished top bar that matches the main site:
  a "JW Sync" wordmark logo, and a cross-tool navigation where each item
  (Merge, Stats, Explorer, Share) now carries a crisp icon alongside its
  label, with the active tool highlighted in the brand orange — the same
  treatment as the main menu. The page title is no longer a competing orange,
  so orange now signals only "where you are". On phones the navigation
  collapses neatly to icons so nothing crowds or overflows.

## [2.69.0] — 2026-06-13

### Changed
- **Study Stats now opens with a polished welcome card** instead of a bare
  title and button. It matches the rest of the site: a stats icon, a clear
  prompt, the Open File button, and a privacy line ("Your file is read on
  your device — nothing is uploaded"). You can now also **drag a .jwlibrary
  file straight onto the card** to open it, with a highlight as you drag over.
  Works in dark and light themes and is translated in all 12 languages.

## [2.68.1] — 2026-06-13

### Shipped to production
- The hero merge visualization (v2.67.0) and the "Home" navigation link
  (v2.68.0) are now live on jwsync.org, not just /beta.

## [2.68.0] — 2026-06-12

### Added
- **"Home" link in the site navigation (beta):** once inside the Merging App
  there was no visible way back to the homepage — you had to know to click the
  "JW Sync" logo to find the other tools (Library Doctor, Study Stats, …).
  A "Home" link now sits first in the nav on every view, highlighted when
  you're on the homepage, and translated in all 12 languages.

## [2.67.0] — 2026-06-12

### Added
- **Hero merge visualization (beta):** the landing page now *shows* the product
  at first glance — a split hero with two `.jwlibrary` backup files (phone +
  tablet) flowing into a single merged library card, drawn with
  highlight-coloured note lines and a "Never leaves your device" privacy badge.
  Pure HTML/CSS (no images, ~3 KB), theme-aware (dark + light), localised in
  all 12 languages, side-by-side on desktop and stacked on mobile.

## [2.66.0] — 2026-06-12

### Added (beta)
- **The Awards tab is now on the beta site's Study Stats page too** — the
  Stats / Awards two-tab layout, themed medals, and the Distinguished Honors
  cabinet had been live on jwsync.org since June 8 but never reached
  jwsync.org/beta. Both sites now show the identical Stats page.

### Internal
- New automated drift guard (test suite 15): the shared pages and scripts that
  ship to both sites must stay in sync, and the offline cache version must be
  bumped whenever a cached page changes — the two mistakes behind the missing
  Awards tab and the stale freeze fix can no longer slip through unnoticed.
- One-off build scripts moved out of the repository root into `scripts/`.

## [2.65.3] — 2026-06-12

### Fixed (live)
- **Library Doctor could freeze during the duplicate-highlights check** on
  large libraries. The check now uses a linear scan instead of a quadratic
  SQL self-join, so it finishes in seconds even with tens of thousands of
  highlights. (Shipped earlier; this release bumps the offline cache so
  installed-app users actually receive it.)
- **Jumping to Study Explorer from another tool now auto-opens Browse on the
  beta site too** — the hand-off flag was only being set on production.
- **Returning visitors on the production site no longer see the landing page
  on every visit.** Once you've clicked "Launch" the site takes you straight
  to the app, matching the beta site and the documented behaviour.

## [2.65.2] — 2026-06-11

### Fixed (live)
- **"View Your Stats" on the celebration screen showed an older file.** The
  stats page prefers the shared working file (the cross-tool session), but the
  celebration only handed the merged result to an older one-shot mailbox — so
  you'd see stats for whatever file was loaded before the merge. The button now
  makes the just-merged file the shared working file, so the stats you see are
  for the exact file you just downloaded (and the other tools follow it too).

## [2.65.1] — 2026-06-11

### Fixed (live)
- **The "Ready to merge" card could overflow the screen on mobile** with no
  way to scroll — especially with a long Library Doctor findings list — cutting
  off the Merge & Download button. The card now caps itself to the screen
  height and scrolls smoothly inside.

## [2.65.0] — 2026-06-11

### Library Doctor moved into the merge itself (live)
- The opt-in now lives where it belongs: a small checkbox directly under
  **Create My Merged File** on the merge page — "Health-check & clean the
  merged file before downloading (Library Doctor)".
- It's **one-time use**: always unticked by default, and unticks itself the
  moment a merge starts. No remembered setting.
- When ticked, the Doctor runs **silently inside the merge engine** — no
  pop-up, no second screen. Its findings appear as a "Library Doctor" group
  right on the **Ready to merge** card, alongside the merge numbers, with a
  note that they'll be fixed automatically.
- Confirming the merge applies the fixes before the file is packaged, so the
  single download you already get is the final, healthy backup. Cancelling
  changes nothing, as always.
- The previous version's two-step flow (Doctor pop-up after the merge,
  download suppression) is gone — one card, one confirm, one file.

## [2.64.1] — 2026-06-11

### Library Doctor merge opt-in — one download instead of two (beta)
- When the health-check box is ticked, the merged file no longer downloads
  by itself. Instead the Doctor opens on it, **cleans it automatically**,
  and then shows a single **Download your file** button — so you only ever
  save one file: the final, healthy backup.
- If the merge is already in perfect health, the Doctor says so and the same
  single button downloads the merged file as-is.
- If anything goes wrong on the way (the file can't be handed over), the
  normal merged-file download happens exactly as before — you can never end
  up without your file. The celebration screen also keeps its manual
  "Download merged backup" button as a backup.
- Checkbox label updated to match: "Health-check & clean the merged file
  before downloading".

## [2.64.0] — 2026-06-11

### Library Doctor — health-check your merge as part of the flow (beta)
- The "Ready to merge" window now has an opt-in checkbox: **"Also
  health-check the merged file (Library Doctor)"**. Tick it, and as soon as
  your merged backup is ready the Library Doctor opens automatically with
  that exact file loaded — scan it, and if anything fixable turns up, one
  click downloads the healthy copy too.
- Your choice is remembered for next time. The merge itself is completely
  unaffected either way — the Doctor only ever reads the finished file.
- Localised in all 12 languages.

## [2.63.3] — 2026-06-11

### Library Doctor — safer duplicate-note detection (live)
- Notes are now only treated as duplicates when their anchor matches too —
  identical text on **different verses or paragraphs of the same chapter** is
  never removed anymore.
- When a true duplicate is removed, the kept copy is now the one linked to a
  highlight (if any), and any tags that were only on the removed copy are
  moved onto the kept note instead of being lost.

## [2.58.2] — 2026-06-09

### More visual polish — editorial touches (live)

- **Refined "Choose a tool" eyebrow** — soft hairlines now flank the label for a cleaner, more editorial look.
- **Section accents** — each major section heading gets a small orange underline accent, giving the page clearer rhythm and structure.
- The full beauty pass (hero glow, calmer card hovers, feature-card hovers, and these touches) is now **live on jwsync.org**.

---

## [2.58.1] — 2026-06-09

### Visual polish — a more beautiful landing (live)

- **Hero depth**: a soft, static glow now sits behind the headline, giving the page a warmer focal point without any animated gradients.
- **Calmer, classier tool cards**: the constant background shimmer is gone — instead each "Choose a tool" card plays a single, elegant accent sweep with a gentle lift *on hover*.
- **Cohesive feature cards**: the feature tiles now respond on hover (subtle orange border + lift), matching the rest of the page.

---

## [2.58.0] — 2026-06-09

### Safe Restore — confidence at the most important step (live)

Restoring is the one step that *replaces* what's on your device, so JW Sync now makes it reassuring and clear with a beautiful **Safe Restore** panel — shown both on the merge celebration screen and inside the restore guide:

- **✓ Your originals are safe** — JW Sync never changes your original backups; the merged file is brand-new.
- **⚠ Restoring replaces** the notes currently in JW Library on this device.
- **★ Keep the combined file** as your master backup.

Localised across all 12 languages, with the brand's calm navy/emerald/amber styling.

---

## [2.57.0] — 2026-06-09

### Share your merge result + completed multilingual SEO (live)

- **Share card on the merge celebration**: after a successful merge, a new **Share** button generates a clean, branded result image (your notes / highlights / bookmarks / tags totals) and shares it via the device's native share sheet — with automatic **download + copy-link fallback** where Web Share isn't available. Localised in all 12 languages.
- **Multilingual SEO completed in production**: production was missing `hreflang` for Swedish and Cebuano and had no `og:locale:alternate` tags — both are now in place, so all 12 languages are fully discoverable.
- Shipped to **jwsync.org** (not just /beta).

---

## [2.56.2] — 2026-06-09

### Multilingual SEO — discoverable in all 12 languages (beta)

- Added **`hreflang`** alternate tags (all 12 languages + `x-default`) and **`og:locale:alternate`** tags to the page head, so search engines and social platforms know about every language version of the site.
- **Rebuilt `sitemap.xml`** to include all 12 languages — previously it was missing Swedish and Cebuano — with a complete reciprocal hreflang set per URL and a fresh `lastmod`.
- This lets the fully-translated site rank in the other 11 languages instead of only English. No visible UI change.

---

## [2.56.1] — 2026-06-09

### Shipped to production

All of the How-it-works improvements (v2.55.0–v2.56.0) are now live on jwsync.org, not just /beta:

- **"How it works" card** with its two tabs — **Merging** (3-step guide) and **Other tools** (Study Explorer, Study Stats & Awards, Note Share & Receive, each with an Open shortcut).
- **"How it works" button** sits above "Choose a tool"; the card opens only when clicked (no auto-popup).
- **Privacy badge** above the file picker. All localised across 12 languages.

---

## [2.63.2] — 2026-06-10

### Renamed: Backup Doctor → Library Doctor

- The health-check tool is now called **Library Doctor** (localised in all 12 languages). Same one-tap checkup and private, one-click cleanup — just a clearer name.

---

## [2.63.0] — 2026-06-10

### 🩺 New tool: Backup Doctor (beta)

A free, private health check for any `.jwlibrary` backup — and a one-click repair.

- **Seven health checks**: duplicate notes, empty notes, duplicate highlights, stray highlight fragments, broken tag links, unused tags, and leftover location records.
- **Beautiful scan**: an animated ECG pulse while each check runs, then an animated health-score ring (0–100) with a verdict — Excellent, Good, Fair, or Needs care.
- **One-click "Clean & Download"**: removes everything fixable, compacts the database, and downloads a fresh `healthy_….jwlibrary` — your original file is never touched. Shows how much smaller the cleaned backup is.
- **Smart & safe**: keeps the oldest copy of any duplicate, never deletes highlights that have notes attached, never touches the special Favorites tag, and only removes location records nothing else references.
- New **Backup Doctor** banner on the home page, under "Choose a tool". Fully localised in all 12 languages.

---

## [2.62.0] — 2026-06-10

### Tidier merge tool: collapsible advanced sections (beta)

- **Extract & Share**, **Bulk Color Changer**, and **Manage Tags** now collapse into three compact tabs in the merge tool. They're tucked away by default, so the page is shorter and you can scroll straight to the merge button.
- Tap any tab to expand the full tool; tap again to collapse it. A chevron shows the state.
- Your merge flow is unchanged — these are optional power tools, now out of the way until you want them.

---

## [2.61.0] — 2026-06-10

### Juicy merge celebration: particles, rings & checkmarks (beta)

- The merge celebration now feels truly rewarding: floating particles drift upward, animated rings fill as each stat counts up, and emerald checkmarks bounce in as each total completes.

---

## [2.60.0] — 2026-06-10

### Elegant modal entrance animations (beta)

- All modals (celebration, restore guide, conflict review) now open with a smooth, staggered entrance — the backdrop blurs in, then the title, content, and buttons reveal in sequence with premium easing.

---

## [2.59.0] — 2026-06-10

### Celebration screen polish: animated stats counter (beta)

- **Stats count-up animation**: The merge celebration now animates the stats numbers (notes, highlights, bookmarks, tags) counting up from 0 to their final values—adding visual polish and engagement to the post-merge moment.
- **Visual dividers**: A subtle gradient line now separates the stats grid from the Safe Restore panel, improving visual hierarchy.

---

## [2.56.0] — 2026-06-09

### "How it works" — now covers every tool (beta)

- The How-it-works card has **two tabs**: **Merging** (the original 3-step guide) and a new **Other tools** tab.
- **Other tools** explains what each tool does and how to use it — **Study Explorer** (search, edit, tag, Ask Your Library), **Study Stats** (totals, streaks, trends, plus the **Awards** medals tab), and **Note Share & Receive** — each with an **Open** shortcut that takes you straight there.
- Tool names match the "Choose a tool" cards, fully localised across all 12 languages.

---

## [2.55.1] — 2026-06-09

### Merge Wizard — quieter, on-demand (beta)

- The **"How it works"** button now lives at the top of the landing, right above **"Choose a tool"**, so it's easy to find before you start.
- The wizard **no longer pops up on its own** for first-time visitors — it opens only when you tap "How it works". The privacy badge stays put above the file picker as a quiet reassurance.

---

## [2.55.0] — 2026-06-08

### First-run Merge Wizard + point-of-action privacy badge (beta)

- **Merge Wizard**: First-time visitors now see a friendly 3-step guide — Export your backups → Add & merge → Restore — that ties the existing platform-aware export and restore guides directly into the flow. The "Export" and "Restore" steps open the matching step-by-step guide for your device. Shown once, then dismissed for good.
- **"How it works" link**: Returning users can reopen the wizard any time from the link in the privacy badge.
- **Privacy badge at the file picker**: A subtle "100% private — your files never leave this device" badge now sits right above the main file picker, reassuring you exactly where it matters most that nothing is ever uploaded.
- Both are fully localised across all 12 languages.

---

## [2.54.0] — 2026-06-08

### Cebuano language added (12th language)

- **Cebuano (Bisaya)**: Full translation added across the entire app — landing page, merge flow, Study Explorer, Ask Your Library, celebration screen, Study Stats, awards, and all tool UIs
- All 12 languages now live: English, Spanish, Portuguese, French, German, Italian, Russian, Japanese, Korean, Filipino, Swedish, Cebuano

---

## [2.53.5] — 2026-06-08

### Shipped to production — Study Stats Awards tab + Ask tag fix

All features are now live on jwsync.org:

- **Study Stats — Awards tab**: Stats and Awards are split into two tabs at the top of the page. The Awards tab has an animated shimmer effect. Clicking Stats hides the Awards content and vice versa.
- **Distinguished Honors cabinet**: Always shows your top 3 rarest earned medals directly below the achievements intro — falls back to top 3 by rarity if no ultra-rare medals are earned yet.
- **Merge celebration teaser**: After downloading your merged file, the celebration screen now shows your 3 most-rare earned medals and a shimmering "Explore Your Awards →" link.
- **Donation prompt moved**: "Found JW Sync useful?" now appears right after the download confirmation banner, above the action buttons.
- **Bug fix — Ask Your Library tag assignment**: Tags were not being applied when using "Select All" in Ask mode if the user had previously been on the Highlights or Bookmarks tab. Fixed so "Select All" always uses the visible Ask results.
- **Bug fix**: Restored the "tagged ✓" green confirmation banner in the batch bar after bulk-tagging notes.

---

## [2.53.4] — 2026-06-08

### Fixed — Ask Your Library tag assignment (beta)

- **Bug fix**: When selecting notes in Ask Your Library and adding a tag via the batch bar, the tag was not being applied if the user had previously been on the Highlights or Bookmarks tab. The "Select All" button was picking up the wrong item list (the previous tab's filtered results instead of the Ask results). Fixed so "Select All" in Ask mode always selects the visible Ask results.
- Also restored the "tagged ✓" confirmation banner in the batch bar after applying a tag (it was accidentally placed outside its function).

---

## [2.53.3] — 2026-06-06

### Shipped to production — Ask Your Library + Study Explorer improvements

All features from v2.53.0–v2.53.2 are now live on jwsync.org (not just /beta):

- **Ask Your Library** semantic search is live in the main Study Explorer
- **WebGPU acceleration** on Android Chrome 113+ / iOS 17+ — up to 10–30× faster indexing
- **Study Explorer** nav button renamed and updated with a teal shimmer animation
- **Explorer nav button** click now correctly boots the module before opening it
- **Progress bar**, ETA countdown, and search-while-indexing are all in production

---

## [2.53.2] — 2026-06-06

### Improved — Ask Your Library: faster model, larger batches

- Upgraded to **transformers.js v3** with **WebGPU acceleration** — up to 10–30× faster on modern Android and iOS devices. Falls back to optimised WASM (quantized int8) on older browsers.
- Batch size increased to 64 notes per pass for fewer worker round-trips.
- Note text truncated to 600 characters before embedding (well within model limits) to cut tokenisation time.
- Error recovery: if a model fails to load, the picker reappears so you can choose again without refreshing.

---

## [2.53.1] — 2026-06-06

### Improved — Ask Your Library: search while indexing, faster first-time build

- **Search immediately.** Instead of waiting for all notes to be indexed, you can now type a question and get results as soon as the first batch of notes is ready. Results update automatically as more notes are added to the index.
- **Faster indexing.** Batch size doubled (24 → 48 notes per pass), reducing the number of worker round-trips by half and cutting total first-time index time significantly.
- **Clear expectations.** A "First-time only — saved to your device, instant next time" message now appears during the initial build so you know subsequent opens will be immediate.

---

## [2.53.0] — 2026-06-06

### Added — Ask Your Library: private, on-device semantic search (beta)

The Study Explorer can now search your notes **by meaning, not just keywords**. Ask a question in plain language and find related notes even when they use completely different words — all computed in your browser, with nothing uploaded.

- **Natural-language search.** Tap the new **Ask** button in the Study Explorer toolbar and type something like *"notes about staying loyal under pressure"* — you get back your most related notes, ranked with a **% match**, even if they never use those exact words.
- **100% private and offline-capable.** A small language model runs entirely on your device. It downloads **once**, is cached for reuse (including offline), and your notes never leave your browser.
- **Choose your model.** On first use you pick between a smaller **English** model (~23 MB) or a **Multilingual** model (~50 MB) that understands 50+ languages — ideal if you write notes in more than one language. You can switch models or rebuild the index anytime.
- **Fast re-use.** Note embeddings are cached locally (IndexedDB), so re-opening Ask is instant and only new or edited notes are re-read.
- Click any result to open it in the normal detail view, where you can read and edit it as usual.

## [2.52.0] — 2026-06-06

### Added — Study Achievements: keyword awards, shaped medals & clickable popups (production)

Shipping the full Study Achievements upgrade to production (`highlights.html`):

- **27 content-aware keyword achievements.** JW Sync now reads your note text and awards medals for writing about love, faith, hope, prayer, prophecy, wisdom, grace, kingdom, peace, joy, truth and covenant — each keyword has 2–4 tiers from Common to Legendary.
- **Shaped medal discs.** Keyword medals are rendered in seven distinct shapes — heart, shield, star, diamond, crown, scroll and teardrop — giving each spiritual theme its own visual identity.
- **Appreciation badges.** Every earned medal with rarity ≥ 1 shows a small "+N" chip indicating its Appreciation point value.
- **Distinguished Honors cabinet.** A special showcase at the bottom of the Achievements wall displays all your rare (rarity ≥ 2) earned medals in a golden highlight strip.
- **Clickable medal popups.** Tap any medal — in the main wall or the cabinet — to open a popup showing its name, what it means, how to earn it, and its Appreciation value. Locked medals show a progress bar.
- **Description keys for all named achievements.** Every achievement with a `dk` key now has a human-readable English description in the popup.

## [2.50.2] — 2026-06-05

### Changed — Accessibility & mobile polish (beta)
- **More readable muted text.** Lightened the lowest-contrast helper text so it now meets WCAG AA contrast (dark and light themes) — labels, captions and hints are easier to read.
- **Bigger touch targets.** On touch devices, the nav links, language picker and primary buttons are now at least 44px tall, making them easier to tap accurately.

## [2.50.1] — 2026-06-05

### Changed — "Renown" renamed to "Appreciation" (beta)
The points earned from rarer awards are now called **Appreciation** instead of "Renown" — a humbler word that reflects gratitude for the insight gained, rather than personal fame. Updated in the achievements header and the awards explainer across all 11 languages.

## [2.50.0] — 2026-06-05

### Changed — Study Stats now open on All-Time, plus an awards explainer (beta)
- **Defaults to All Time.** Study Stats now open showing **every note across your whole library** instead of just the latest service year. You can still tap any **Service Year** tab to focus on a single year.
- **Awards explainer.** A short blurb at the top of the Achievements wall explains how the gamified part works — earn awards by adding notes, highlighting verses, exploring more Bible books and keeping streaks; rarer awards grant more **Renown**; tap a tier to open it and use the filters to see what's left to unlock. Translated into all 11 languages.

## [2.49.0] — 2026-06-05

### Added — Swedish (Svenska) — the whole site is now translated (beta)
JW Sync is now available in **Swedish** — its 11th language. Every surface is translated, not just the landing page:
- The **Merge tool**, **Study Explorer**, **Study Stats** (including achievements, the Study Map, and your study journey), **Note Sharing**, the post-merge celebration, the Sync Hub, and all dialogs and messages.
- Pick **🇸🇪 Svenska** from the language selector (top of the page) — your choice is remembered, and the new tool switcher is translated too.

## [2.48.1] — 2026-06-05

### Fixed — Cross-tool workspace (beta)
- **Your merge file now actually follows you.** Previously, a backup uploaded in the **Merge** tool wasn't being remembered, so opening **Study Stats** still asked you to upload again. Any `.jwlibrary` you pick or drag in is now saved to the shared workspace, so it carries over to every tool.
- **Fixed the cramped nav on phones.** The **Merging App** and **Study Stats** links were running together. The tool links now wrap onto a tidy, evenly-spaced second row on narrow screens instead of colliding.

## [2.48.0] — 2026-06-05

### Added — Your file follows you between tools (beta)
The four tools — **Merge**, **Study Stats**, **Study Explorer**, and **Note Sharing** — used to feel like separate apps: open one, and you had to upload your backup again. Now they share one workspace:
- **Universal tool switcher.** Every page shows a compact **Merge · Stats · Explorer · Share** switcher (with the current tool highlighted), so you can jump straight to any tool from anywhere — no more going back to the home page.
- **No re-uploading.** Load your `.jwlibrary` once and it follows you between tools automatically. Check your Study Stats, hop to the Explorer to edit a note, then to Note Sharing — all on the same file.
- **Still 100% private.** The working file is kept only in your own browser (IndexedDB), never uploaded. It is automatically forgotten after 12 hours, and **"New file" / "Start over" clears it immediately.**
- The switcher is fully translated into all 10 languages.

## [2.47.1] — 2026-06-05

### Changed — Visual consistency pass (beta)
A first round of polish to make the interface feel more cohesive:
- **Consistent button hovers.** Every primary (orange) button now *darkens* on hover instead of a few buttons lightening — the action buttons in Browse, the note-explorer CTA, and the import dialog now match the main "Merge" and service-card buttons.
- **Keyboard focus ring on the main call-to-action.** The primary CTA button now shows a visible focus outline for keyboard and screen-reader users, matching the secondary buttons.
- **Reusable button foundation.** Added a shared, design-token-based button system (`.btn` with primary/secondary/ghost/danger variants) so future buttons stay consistent automatically. Existing buttons are unchanged in appearance.

## [2.47.0] — 2026-06-05

### Changed — Achievements are now tidy, collapsible shelves with richer medals (beta)
The ~200-award wall no longer dumps everything on screen at once:
- **Collapsible shelves.** Each tier is a tappable shelf that **starts collapsed** (only the tier you're currently working on is open), so you can browse calmly and **expand** the ones you want. Headers show a chevron, a tier progress bar, and an earned/total count.
- **Smart filtering.** Choosing **Earned** or **Locked** automatically opens every shelf so you can see all matches at once; **All** returns to the tidy collapsed view.
- **Richer, more colourful medals.** Earned awards now have **higher-quality, more nuanced medallions** — a glossy gem face, a metallic rim, and a **per-award accent colour keyed to its category** (notes, scriptures, streaks, colours, etc.), so the wall reads as a vibrant, varied collection. Legendary awards get a slowly rotating shine.

## [2.46.1] — 2026-06-05

### Fixed — Study Map fullscreen now expands just the map (beta)
The **Fullscreen** button in the Study Map tool now blows up **only the graph canvas** edge-to-edge, instead of the whole window with its header and side panels — a cleaner, distraction-free view of your connections. Esc returns you to the tool.

## [2.46.0] — 2026-06-05

### Changed — Study Map is now a standalone full-screen tool (beta)
The Study Map graduated from an inline chart into its own dedicated tool:
- **Launch button.** Study Stats now shows an **“Open Study Map”** button instead of embedding the graph — tap it to open the map as a focused, full-screen workspace.
- **Go full-screen.** A **Fullscreen** button expands the map edge-to-edge for exploring large libraries (Esc or Close returns you to your stats).
- **Download an image.** Export the current map (with all your connections and study chains) as a **PNG** to save or share.
- Everything from before — Topics ↔ Notes views, layer toggles, the strength slider, drag, hover-to-spotlight, the click-through side panel, and manual study chains — now lives inside the tool, with more room to breathe.
- New controls fully translated across all 10 languages.

## [2.45.0] — 2026-06-05

### Added — Study Map: an interactive knowledge graph of your notes (beta)
The Study Stats page now includes a **Study Map** — a private, in-browser graph that reveals how years of your notes connect to each other. Nothing leaves your device.
- **See the connections you never tagged.** The map links your notes by **shared scripture** (notes on the same passage), **shared tags**, and **similar wording** (overlapping key terms) — all computed on your device, with no AI service and no upload.
- **Topics ↔ Notes view.** Switch live between a clustered **Topics** view (themes, tags, and scriptures as hubs sized by how many notes touch them) and a **Notes** view of individual notes — pick whichever reads best for your library.
- **Click to read.** Tap any point to open a side panel listing the notes behind it, with snippets and dates.
- **Manual study chains.** Hand-link related notes into named **study chains** — saved privately on your device (keyed to each note, never written into your backup) and drawn as distinct threads on the map.
- **Explore controls.** Toggle each connection layer on/off, drag nodes around, hover to spotlight a note's neighbors, and use the strength slider to focus on the strongest links.
- Fully translated across all 10 languages.

## [2.44.0] — 2026-06-04

### Added — Achievements Gallery: ~200 awards across 12 tiers (beta)
The Study Stats achievements wall grew from a flat set of medals into a deep, gorgeous collection that matches the 60-level / 12-tier journey:
- **~200 awards**, organized under the **same 12 tiers** as your Study Journey, each tier shown in **its own color**.
- **Reveal-gating:** awards above your current tier appear as locked **“???”** mysteries with a “Reach _[tier]_ to unlock _N_ more” hint — they light up the moment you climb into that tier.
- **Rarity + Renown:** every award has a rarity (Common → Legendary) and is worth Renown points; your total **Renown score** is shown at the top as a second long-term goal.
- **Tier crests** (a capstone emblem for each tier) and **“Tier Mastered”** bonuses for completing a whole tier.
- **Secret awards** stay hidden until you earn them.
- **Filter tabs** (All / Earned / Locked) and **progress mini-bars** on awards you’re close to earning.
- Earned medals glow in their tier’s color; legendary awards shimmer.

All new labels localized across 10 languages.

---

## [2.43.0] — 2026-06-03

### Changed — Study Journey: 60 levels across 12 tiers (beta)
A much longer, more addictive climb for people who've been studying for years:
- **60 levels** (up from 6 stages), grouped into **12 named tiers** — Seed, Sprout, Sapling, Young Tree, Tree, Blossom, Grove, Orchard, Garden, Vineyard, Forest, and Evergreen.
- **Your level shows right in the orb,** and the orb's color **shifts smoothly as you climb** — every level looks a little different from the last.
- **Early levels come fast** (a handful of notes gets you moving), while the summit — **Level 60, Evergreen** — takes a true lifetime of study, so there's always a higher level to reach for.
- **Each tier has its own description** (what it says about you) and a level-up / new-tier **confetti celebration**, with a 12-tier ladder showing exactly where you are and what's ahead.
- Your level is **lifetime-based**, so it only ever climbs.

All localized across 10 languages.

---

## [2.42.0] — 2026-06-03

### Added — Study Journey: stages explained + level-up celebrations (beta)
- **Each stage now means something.** Your Study Journey shows a short description of *what this stage says about you* and *what it took* to reach it, right on the card.
- **Tap your stage** to open a beautiful detail view: a big glossy orb, your signature persona, the full meaning, the requirement you met, and **a ladder of all six stages** (Seed → Sprout → Sapling → Tree → Grove → Orchard) showing where you are and what's ahead.
- **Level-up celebration.** When you reach a new stage, it's celebrated with a confetti burst and the detail view, so a promotion actually feels like a moment.
- **Your stage is now lifetime-based** (total notes), so it stays consistent no matter which service year you're viewing.

All localized across 10 languages.

---

## [2.41.0] — 2026-06-03

### Added — Study Stats: four more showpieces (beta)
- **Word Cloud** — analyzes the actual text of your notes (on-device) and shows the words you write most as a gorgeous sized, colored cloud — revealing *what* you study, not just how much.
- **Your Study Story** — an animated milestone timeline: your first note, each growth stage you reached, your longest-streak start, your busiest day, and your latest note — in order.
- **What's Next** — a motivating panel with a pace forecast ("~N weeks to your next stage") and progress bars toward your closest upcoming milestones.
- **Shareable Card** — generate a beautiful image of your stats (your stage, signature, and headline numbers) to download or share, drawn on-device.

All localized across 10 languages.

---

## [2.40.0] — 2026-06-03

### Added — Study Stats "character sheet" (beta)
A rich, personal layer on the Study Stats page — a sense of progression and identity, with no game-y language:
- **Study Journey** — a glossy progression orb (Seed → Sprout → Sapling → Tree → Grove → Orchard) with a progress ring showing how far you are to the next stage, plus your **study signature** persona (e.g. "The Reflective Writer") drawn from your strongest trait.
- **Study Profile** — a six-point trait radar scoring your **Consistency, Diligence, Depth, Breadth, Reflection,** and **Steadiness** from 0–100.
- **Key Insights** — at-a-glance cards on *when* you study (busiest day, time of day, cadence — "every ~N days", busiest single day) and *how* (what share of highlights get a note, signature color, top tag, books explored, words written).
- **Achievements wall** — **66** unlockable milestones as glossy medallions across ten categories (Notes, Highlights, Writing, Streaks, Coverage, Colors, Tags, Bookmarks, Rhythm, Dedication), with earned/locked states and an "X / N earned" progress bar. Includes coverage feats like the Four Gospels, the Torah, and the whole Hebrew/Greek Scriptures.

All localized across 10 languages.

---

## [2.39.0] — 2026-06-03

### Added — Study Stats (beta)
Eight new colorful visualizations on the Study Stats page:
- **Study Gauges** — radial arc gauges for Consistency (active weeks), Depth (notes on highlights), Pace (notes per study day), and Weekend share.
- **Study Clock** — a 24-hour radial chart showing what time of day you study, with your busiest hour called out.
- **Seasonality radar** — a 12-month polar chart of which months you study most.
- **Highlight Color Wheel** — your highlight colors as a donut with your signature color in the center.
- **Bible Progress ring** — a circular gauge of how many of the 66 books you've touched, with Hebrew/Greek-Scripture arcs.
- **Note Depth histogram** — the spread of your note lengths from one-liners to essays, with your average words per note.
- **Achievements** — unlockable milestone badges (100 / 1,000 notes, Four Gospels, whole Bible, all colors, 30-day streak, 500 highlights, 10k words).

All localized across 10 languages.

---

## [2.38.0] — 2026-06-03

### Added
- **The Merge tool's "receive notes" step now has the same rich experience as the Share page.** When you attach a friend's share file before merging, a **Preview** link lets you open a full, categorized view of the notes.
- **Categorized preview in the Merge tool.** The preview opens in a roomy window with filter chips — **All**, **Highlights**, **Notes**, and one per **tag** (each with a count) — and a scrollable list showing each note's publication, a colour dot for highlights, and its tags.
- **The conflict prompt now shows which notes clash.** When some incoming highlights land on verses you've already highlighted, the choice dialog lists those specific notes before you pick "Add as a separate layer" or "Import note only".
- **An import summary after merging.** Once shared notes are added, a summary lists every note that was added, with a Download button for the updated file.

---

## [2.37.0] — 2026-06-03

### Added
- **A much richer preview when you receive shared notes.** After you load a share file and tap Preview, the page now scrolls straight to the notes and opens up wider to fit them. The notes are shown in a clean, scrollable list with their publication, a colour dot for highlights, and their tags.
- **Browse hundreds of notes by category.** Filter chips at the top let you jump between **All**, **Highlights**, and **Notes**, plus a chip for each **tag** — each showing how many there are — so a big share file is easy to skim before importing.
- **See exactly what clashes.** When some incoming highlights land on verses you've already highlighted, the choice screen now **lists those specific notes** so you can see what's affected before you pick "Add as a separate layer" or "Import note only".
- **See exactly what was added.** After importing, the confirmation screen now **lists every note that was added to your backup**, with the same colour dots and tags.

---

## [2.36.1] — 2026-06-03

### Fixed
- **"0 notes added to your backup" when receiving a friend's notes.** Imported notes were actually being written, but a tagging clash (every note's tag was filed in the same slot) made the import silently fail its count — and could drop the tags. Imported notes are now filed correctly, so all of them are added and tagged, and the count is accurate. Affected the Share page and the Merge tool's receive step.

---

## [2.36.0] — 2026-06-03

### Added
- **You're now in control when you receive someone's notes.** When you add a friend's `.jwshare.json`, you can set your own **tag for the imported notes** (defaults to "Shared") so every received note is easy to find later. A clear reminder shows that imported notes are **added as new notes — your own notes are never replaced.**
- **Shared highlights now travel with their notes.** When you send notes, any highlight on them (its colour and exact verse span) is included in the share file. When the other person receives them, the highlight is recreated **on the right passage in your friend's colour.**
- **Nothing of yours is ever overwritten.** If a friend's highlight lands on a verse you've **already highlighted** (even with your own note), JW Sync asks how you'd like to add it:
  - **Add as a separate layer** — the friend's highlight is added in its own colour alongside yours, and a second note is created. Your highlight and note stay exactly as they were.
  - **Import note only** — just the friend's note is added (linked to your existing highlight), with no competing colour.
- Highlights on **new** passages are added automatically without asking.

---

## [2.35.0] — 2026-06-03

### Changed
- **The home tool tiles now have a gentle, colored shimmer** — each with its own accent (Merge Tool orange, Study Explorer blue, Study Stats green, Note Share & Receive violet) and matching icon and hover glow. The shimmers are staggered so they sweep one after another, and they automatically turn off if you have "reduce motion" enabled.

---

## [2.34.1] — 2026-06-03

### Fixed
- **Home service cards now translate when you change the language.** They were stuck in English because the cards' text wasn't being looked up correctly after the app loaded — fixed so all four cards follow the selected language in all 10 languages.
- **Removed the odd "Open &#8594;" text** on the cards. Each card is now a single tidy clickable tile showing the **tool's name** (Merge Tool, Study Explorer, Study Stats, Note Share & Receive) — no stray symbols.
- **Tidier, unified layout.** The four tools now sit together in one clean sequence right under the heading (the separate "Launch App" button is folded into the Merge Tool tile), with "Try with sample notes" and "First time? How it works" as compact secondary actions beneath.

---

## [2.34.0] — 2026-06-03

### Added
- **Receive a friend's shared notes right inside the Merge Tool.** If someone sent you a `.jwshare.json`, you can now:
  - **Attach it before merging** — a "Got notes from a friend?" panel appears on the merge screen; the shared notes are folded into your merged backup automatically when the merge finishes.
  - **Add them after merging** — the post-merge screen has a new **"Add notes a friend shared"** button that drops them into your freshly-merged file and gives you the updated download.
- Adopted notes are tagged **"Shared"** (plus any tags the sender included) so you can always find what came from a friend. Everything stays on your device — nothing is uploaded.

---

## [2.33.0] — 2026-06-03

### Changed
- **The home page now presents JW Sync's tools as four distinct services**, each in its own clean card with an icon, a one-line description, and an Open button:
  - **Merge Tool** — combine JW Library backups from all your devices.
  - **Study Explorer** — *(renamed from "Note Explorer")* search, edit, tag and organise every note in a backup.
  - **Study Stats** — *(renamed from "Your Service Year Highlights")* your study streaks, totals and trends.
  - **Note Share & Receive** — send notes to a friend, or add notes they sent you (its own page).
- **Retired the "Tools ▾" menu.** The services are now front-and-centre on the home page instead of tucked inside a dropdown. Inside the app, the Study Explorer and Study Stats buttons return to the top bar as individual buttons.
- These are label/placement changes — the underlying tools (and the service-year date logic behind Study Stats) work exactly as before.

---

## [2.32.0] — 2026-06-02

### Fixed
- **The top navigation no longer scrunches up on phones.** Previously "App", "Community", and "Tools" were squeezed together and truncated (e.g. "A…", "Com…") with the language picker crowding them. The nav now uses a tidy **two-level layout on small screens** — the logo and language picker share the top line, and **App · Community · ✦ Tools** get their own full-width row with complete, readable labels and the Tools launcher clearly set apart.

---

## [2.31.0] — 2026-06-02

### Changed
- **The extra services now feel like extra services.** Browse, Service Year Highlights, and Share Notes used to sit in the nav next to ordinary links. They're now gathered under one distinct, accented **Tools** button (in both the app top bar and the home-page nav) that opens a tidy menu — each service with its own icon and a one-line description. It reads as a little suite of bonus tools, clearly set apart from the everyday controls, and (unlike before) the launcher stays visible on phones.

---

## [2.30.0] — 2026-06-02

### Added
- **Share Notes now has its own dedicated page** (like Your Service Year Highlights), reachable from a prominent **Share notes** button on the home page and a **Share Notes** link in the top nav. It walks you through everything step by step:
  - **Send:** open one of your backups, **tick the notes you want** to share (with search and select-all), then create a small file to send — by email, chat, or AirDrop. Clear instructions explain exactly what to do.
  - **Receive:** paste shared text or open the file someone sent, **preview the notes**, then add them into one of your backups and download the updated copy to restore in JW Library.
- Everything stays on your device — nothing is uploaded.

### Fixed
- **The Note Explorer tab strip no longer cuts off on phones.** With the new Study Answers tab, the tabs now scroll sideways (and shrink on small screens) so every tab is reachable in portrait — no need to rotate to landscape.

---

## [2.29.0] — 2026-06-02

### Added
- **Merge performance breakdown.** The completion screen now includes a collapsible **Merge performance** panel showing total time and how long each stage took (prepare / merge / package) as a quick coloured bar. For very large libraries it adds a tip on how to merge faster (combine fewer files at once or use date-range extraction). Purely informational — it doesn't change how merges work.

---

## [2.28.0] — 2026-06-02

### Added
- **Share notes with others — no server, no account.** In the Note Explorer, select notes and tap **Share** to produce a small file (or copyable text) you hand over yourself. Nothing is uploaded.
- **Receive & adopt shared notes.** A new **Receive** button lets you paste shared text or open a `.jwshare.json` file someone sent, **preview the notes read-only**, and **adopt them into your library** — added as new notes tagged "Shared" and covered by Undo. Perfect for households and study groups.

---

## [2.27.0] — 2026-06-02

### Added
- **Study Answers are no longer invisible.** JW Library's fill-in study answers (Input Fields) have always been carried through a merge, but you could never see them. The Note Explorer now has a **Study Answers** tab (shown only when your backup contains them) where you can search, **edit**, and **delete** your answers — each change covered by the same Undo/Redo safety net.
- **Pre-merge preview now counts study answers**, so you can see how many will be added before you commit a merge.

---

## [2.26.0] — 2026-06-02

### Added
- **Bulk editing in the Note Explorer.** Tap **Select** to enter selection mode, tick multiple notes, highlights, or bookmarks, then act on them all at once:
  - **Set a highlight color**, **add a tag**, or **delete** the whole selection in one step.
  - **Select all** / **none** for the current filtered view.
- **Undo / Redo.** Every edit — single or bulk — can now be reversed with the **Undo** and **Redo** buttons (or Ctrl/⌘-Z and ⇧-Z) before you export. Made a mistake retagging or deleted the wrong notes? Step right back. Nothing is final until you download the file.

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

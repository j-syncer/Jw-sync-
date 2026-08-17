# JW Sync

**Merge JW Library backups from multiple devices — privately, in your browser.**

🌐 [jwsync.org](https://jwsync.org) &nbsp;·&nbsp; 📖 [Guides](https://jwsync.org/guides/) &nbsp;·&nbsp; 📊 [Study Stats](https://jwsync.org/highlights) &nbsp;·&nbsp; 💬 [Community Forum](https://jwsync.org/forum)

---

## What is JW Sync?

If you use JW Library on more than one device — a phone, a tablet, a laptop — your notes, highlights, bookmarks, and tags end up split across separate backup files. JW Library can back up and restore, but it cannot merge: restoring one backup **replaces** everything on the device, wiping out the other device's work.

JW Sync fills that gap. It reads two or more `.jwlibrary` backups and combines their notes, highlights, bookmarks and tags into one new backup file.

**Everything happens inside your browser. Your files are never uploaded to any server.**

---

## Features

**Merging**

- **Merge** notes, highlights, bookmarks and tags from any number of `.jwlibrary` backups
- **Pre-merge preview** — see exactly what will change before anything is written
- **Conflict Reviewer** — when the same note was edited on two devices, compare both versions with a word-level diff and choose
- **Duplicate detection** — items are matched by their GUID, so re-merging the same files never doubles anything up
- **Tag manager** — search, rename and organise tags across merged files
- **Bulk colour changer** — update highlight colours across the whole library

**Working with a backup**

- **Note Explorer** — open any backup to search, filter and fully edit notes, highlights and bookmarks, then export an updated `.jwlibrary`
- **Ask** — semantic search across your own notes
- **Library Doctor** — scan a backup for structural problems and repair the ones that stop it restoring
- **Study Stats** — a visual summary of your library: notes, highlights, tags, reading streaks, awards and a Study Map of where you have been reading
- **Share & receive notes** — send a selection of notes to someone else and adopt them into their own library
- **Note export** — TXT, CSV, HTML, PDF or Markdown
- **Markdown import** — write notes in any editor and bring them back into a backup, anchored to the verse the front matter names
- **Reading Companion** — build and track a Bible reading plan

**The app itself**

- **25 languages** — English, Spanish, Portuguese, French, German, Italian, Russian, Japanese, Korean, Filipino (Tagalog), Swedish, Cebuano, Arabic, Hebrew, Ukrainian, Polish, Mandarin (Simplified and Traditional), Cantonese, Vietnamese, Hungarian, Hindi, Indonesian, Romanian and Dutch — with full right-to-left support for Arabic and Hebrew
- **Works offline** — installs as a Progressive Web App
- **Opens files from your device** — tap a `.jwlibrary` file and JW Sync opens it directly

---

## Guides

Alongside the app there is a library of **39 step-by-step guides, translated into all 25 languages** — 1,000 pages in total, covering the questions people actually arrive with:

| | |
|---|---|
| [Merge backups from two devices](https://jwsync.org/guides/merge-jw-library-backups) | [Transfer notes to a new phone](https://jwsync.org/guides/transfer-jw-library-notes-new-phone) |
| [Back up JW Library properly](https://jwsync.org/guides/backup-jw-library) | [Move from Android to iPhone](https://jwsync.org/guides/jw-library-android-to-iphone) |
| [Keep several devices in sync](https://jwsync.org/guides/sync-jw-library-multiple-devices) | [Notes missing after an update](https://jwsync.org/guides/jw-library-notes-missing-after-update) |
| [Recover notes from a lost phone](https://jwsync.org/guides/recover-jw-library-notes-lost-phone) | [Repair a corrupted backup](https://jwsync.org/guides/fix-corrupted-jw-library-backup) |
| [Export your notes](https://jwsync.org/guides/export-jw-library-notes) | [Open a .jwlibrary file](https://jwsync.org/guides/open-jwlibrary-file) |

**Browse all guides:** [English](https://jwsync.org/guides/) · [Español](https://jwsync.org/guides/es/) · [Português](https://jwsync.org/guides/pt/) · [Français](https://jwsync.org/guides/fr/) · [Deutsch](https://jwsync.org/guides/de/) · [Italiano](https://jwsync.org/guides/it/) · [Русский](https://jwsync.org/guides/ru/) · [日本語](https://jwsync.org/guides/ja/) · [한국어](https://jwsync.org/guides/ko/) · [Filipino](https://jwsync.org/guides/tl/) · [Svenska](https://jwsync.org/guides/sv/) · [Cebuano](https://jwsync.org/guides/ceb/) · [العربية](https://jwsync.org/guides/ar/) · [עברית](https://jwsync.org/guides/he/) · [Українська](https://jwsync.org/guides/uk/) · [Polski](https://jwsync.org/guides/pl/) · [简体中文](https://jwsync.org/guides/zh-Hans/) · [繁體中文](https://jwsync.org/guides/zh-Hant/) · [粵語](https://jwsync.org/guides/yue-Hant/) · [Tiếng Việt](https://jwsync.org/guides/vi/) · [Magyar](https://jwsync.org/guides/hu/) · [हिन्दी](https://jwsync.org/guides/hi/) · [Bahasa Indonesia](https://jwsync.org/guides/id/) · [Română](https://jwsync.org/guides/ro/) · [Nederlands](https://jwsync.org/guides/nl/)

---

## Privacy

JW Sync processes everything locally using two well-known open-source libraries:

- [SQL.js](https://sql-js.github.io/sql.js/) — SQLite compiled to WebAssembly, runs entirely in your browser
- [JSZip](https://stuk.github.io/jszip/) — reads and writes ZIP files (the `.jwlibrary` format) in memory

**Nothing is sent to a server. No account is required.**

You don't have to take our word for it — the full source is in this repository, so you or anyone you trust can verify exactly what the app does.

---

## The `.jwlibrary` format

Worth knowing, because it explains why this tool can exist at all. A `.jwlibrary` backup is an ordinary **ZIP archive** containing:

- `userData.db` — a **SQLite** database holding every note, highlight, bookmark and tag. Notes live in `Note`, highlights in `UserMark` + `BlockRange`, bookmarks in `Bookmark`, tags in `Tag` + `TagMap`.
- `manifest.json` — describes the backup, including a SHA-256 hash of `userData.db` that JW Library uses to confirm the file has not been altered.

Nothing about it is proprietary or encrypted. That is why the merge can happen client-side: it is a standard archive around a standard database, both of which run in the browser via WebAssembly.

It also explains the two things people get caught by — a restore replaces the device's whole database rather than merging into it, and editing the database by hand without recomputing the manifest hash produces a file JW Library will refuse to restore.

---

## How to use

1. Visit **[jwsync.org](https://jwsync.org)**
2. On each device: JW Library → **Personal Study** → three-dot menu → **Backup and Restore** → **Create a backup**
3. Load the backups into JW Sync
4. Review the pre-merge preview, and resolve anything the Conflict Reviewer flags
5. Download the merged `.jwlibrary` file
6. On each device: **Backup and Restore** → **Restore**, and pick the merged file

Detailed walkthrough: [How to merge JW Library backups from two devices](https://jwsync.org/guides/merge-jw-library-backups).

---

## Installing as an app

JW Sync works as a Progressive Web App — install it for fast offline access:

- **iPhone/iPad**: Share button in Safari → *Add to Home Screen*
- **Android**: browser menu → *Install app* or *Add to Home Screen*
- **Desktop (Chrome/Edge)**: the install icon in the address bar

Once installed it works fully offline, and `.jwlibrary` files can be opened straight from your file manager.

---

## Code structure

No build step for the app itself — the HTML and `js/*.js` files are edited directly and served as-is.

```
/
├── index.html              Production landing page + app shell
├── beta/index.html         Beta shell (noindex) — beta-first changes land here
├── js/                     Feature modules, loaded lazily or deferred
├── guides/                 39 guides × 25 languages (1000 pages)
├── <lang>/                 Pre-rendered landing page per language
├── highlights.html         Study Stats
├── share.html              Share notes
├── forum.html              Community forum
├── service-worker.js       Offline support and asset caching (PWA)
├── scripts/                Generators + one-off patch scripts
├── tests/                  25 suites, plain Node — no framework
└── sitemap.xml             1,027 URLs with a full hreflang cluster
```

The heavy feature code lives in `js/` rather than inline, because ~550 KB of inline `<script>` was the cause of a 4.7 s First Contentful Paint — the bytes rode in the HTML at the browser's highest priority and starved the render-blocking CSS.

| Module | Role |
|---|---|
| `app.js` | React core — merge engine, landing view, i18n |
| `browse.js` | Note Explorer (read + full edit) |
| `merge-worker.js` | SQLite queries and ZIP work, off the main thread |
| `semantic-worker.js` | Embeddings for the **Ask** search |
| `doctor.js` | Library Doctor scan + repair |
| `conflict-review.js` | Side-by-side conflict resolution |
| `impact-preview.js` · `post-merge.js` | Pre-merge preview, post-merge guidance |
| `receive.js` · `sync-hub.js` · `reading.js` · `resurface.js` | Sharing, scheduling, reading plan, resurfacing |

### Generated content

The guides, per-language landing pages, sitemap and RTL stylesheet are **generated** — edit the generators, not the output:

```bash
python3 scripts/build_guides.py    # guides/, every language that has them
python3 scripts/build_landing.py   # <lang>/index.html
python3 scripts/build_seo.py       # sitemap.xml, head tags
python3 scripts/build_rtl.py       # rtl.css
```

Guide copy lives in `scripts/guides_<lang>.py`; `scripts/check_guide_lang.py <lang>` verifies a translation is structurally complete and free of English leakage.

### Tests

```bash
cd tests && npm install && npm test
```

25 suites covering static structure, a JSDOM run of the full Browse UI against a synthesised `.jwlibrary`, a JSDOM boot of the React app itself, merge regressions, Markdown import round-trips, `.jwlibrary` manifest integrity, the guide tree, translation integrity in every language, Arabic/RTL, landing pages, the forum, and a production/beta parity guard.

---

## Tech stack

| Library | Purpose |
|---|---|
| [React 18.2](https://react.dev) | UI components |
| [SQL.js 1.8.0](https://sql-js.github.io/sql.js/) | SQLite in the browser (WebAssembly) |
| [JSZip 3.10.1](https://stuk.github.io/jszip/) | Reading and writing `.jwlibrary` files |
| [Tailwind CSS](https://tailwindcss.com) | Styling (shipped as a local stylesheet) |
| [Lucide](https://lucide.dev) | Icons |
| [Supabase](https://supabase.com) | Community forum backend |

Design is deliberately restrained: a cool navy background (`#040f22`), a single orange accent (`#ea580c`), flat solid buttons, and no animated gradients.

---

## Contributing

Contributions are warmly welcome — a bug report, a translation correction, a feature idea or a pull request.

**Found a bug?** [Open an issue](https://github.com/j-syncer/Jw-sync-/issues) or post in the [community forum](https://jwsync.org/forum).

**Want to contribute code?** `js/enhancements.js` is the cleanest entry point — well-structured vanilla JavaScript handling PWA features, file handling and UI additions. Run the test suite before opening a PR.

**Translations?** The app and the full guide library ship in 25 languages. If you spot an error, or want to add a language, open an issue — `scripts/GUIDE-TRANSLATION-RUNBOOK.md` documents exactly how a language pass works.

All contributions, no matter how small, are appreciated.

---

## Roadmap

- [x] Web Worker for SQL.js (move heavy database work off the main thread)
- [x] Modular rebuild — feature code split out of `index.html` into `js/`
- [x] Full guide library in all supported languages
- [ ] JSDoc documentation on all modules
- [ ] More export formats

---

## Acknowledgements

Thank you to everyone in the community who has tested the app, reported bugs, shared feedback and suggested improvements. This project exists because of you.

---

*JW Sync is an independent project. It is not affiliated with, endorsed by, or connected to the Watch Tower Bible and Tract Society of Pennsylvania. "JW Library" is a trademark of the Watch Tower Bible and Tract Society of Pennsylvania.*

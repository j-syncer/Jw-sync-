# JW Sync

**Merge JW Library backups from multiple devices — privately, in your browser.**

🌐 [jwsync.org](https://jwsync.org) &nbsp;·&nbsp; 💬 [Community Forum](https://jwsync.org/#forum)

---

## What is JW Sync?

If you use JW Library on more than one device — a phone, a tablet, a laptop — your notes, highlights, bookmarks, and tags can end up split across separate backup files. JW Sync merges them back into one.

**Everything happens inside your browser. Your files are never uploaded to any server.**

---

## Features

- **Merge** notes, highlights, bookmarks, and tags from multiple `.jwlibrary` backups
- **Pre-merge preview** — see exactly what will change before committing
- **Duplicate finder** — detect and resolve conflicting or identical notes
- **Tag manager** — search, rename, and organise tags across merged files
- **Bulk colour changer** — update highlight colours across your whole library
- **Side-by-side comparison** — compare two backup files before merging
- **Note export** — save notes as TXT, CSV, HTML, or PDF
- **Statistics** — see a summary of your merged library
- **Activity log** — a full record of every merge operation
- **Simple Mode** — a clean, minimal interface for everyday use
- **9 languages** — English, Spanish, Portuguese, French, German, Italian, Russian, Japanese, Korean
- **Works offline** — installs as a Progressive Web App (PWA)
- **Opens files from your device** — tap a `.jwlibrary` file and JW Sync opens it directly
- **Community forum** — ask questions and share feedback without leaving the app

---

## Privacy

JW Sync processes everything locally using two well-known open-source libraries:

- [SQL.js](https://sql-js.github.io/sql.js/) — SQLite compiled to WebAssembly, runs entirely in your browser
- [JSZip](https://stuk.github.io/jszip/) — reads and writes ZIP files (the `.jwlibrary` format) in memory

**Nothing is sent to a server. No account is required. No analytics are collected.**

You don't have to take our word for it — the full source code is in this repository so you or anyone you trust can verify exactly what the app does.

---

## How to use

1. Visit **[jwsync.org](https://jwsync.org)**
2. Tap **Select Main File** and choose your primary backup (the one you want to keep as the base)
3. Tap **Select File(s) to Add** and choose one or more backups to merge in
4. Review the pre-merge preview
5. Tap **Merge**
6. Download the merged `.jwlibrary` file
7. Open JW Library → Backup & Restore → Restore from backup

---

## Installing as an app

JW Sync works as a Progressive Web App — you can install it on your phone or computer for fast offline access:

- **iPhone/iPad**: tap the Share button in Safari → *Add to Home Screen*
- **Android**: tap the browser menu → *Install app* or *Add to Home Screen*
- **Desktop (Chrome/Edge)**: look for the install icon in the address bar

Once installed, the app works fully offline and `.jwlibrary` files can be opened directly from your file manager.

---

## Code structure

```
/
├── index.html              Main app — compiled React core + all enhancements
├── service-worker.js       Offline support and asset caching (PWA)
├── sitemap.xml             Search engine index
├── robots.txt              Crawler instructions
└── og-image.png            Social media preview image (1200×630)
```

The `index.html` is assembled from several source layers by a build script:

| Layer | Description |
|---|---|
| Core merge engine | React app using SQL.js and JSZip |
| Enhancement layer | PWA, file handlers, visual timeline, sample data demo |
| Community forum | Embedded forum view, Supabase backend, lazy-loaded |
| Design theme | Inter font, zinc-dark palette, amber accent |
| Mobile layer | iOS zoom fix, touch targets, safe-area insets |

> **Note for developers:** The codebase is currently transitioning toward a fully modular structure with separate source files, an esbuild pipeline, and JSDoc documentation. Contributions to that effort are very welcome — see [Contributing](#contributing) below.

---

## Tech stack

| Library | Purpose |
|---|---|
| [React 18](https://react.dev) | UI components |
| [Tailwind CSS](https://tailwindcss.com) | Styling |
| [SQL.js 1.8.0](https://sql-js.github.io/sql.js/) | SQLite in the browser |
| [JSZip 3.10.1](https://stuk.github.io/jszip/) | Reading and writing `.jwlibrary` files |
| [Lucide](https://lucide.dev) | Icons |
| [Supabase](https://supabase.com) | Community forum backend |

---

## Contributing

Contributions are warmly welcome — whether that's a bug report, a translation correction, a feature idea, or a pull request.

**Found a bug?** [Open an issue](https://github.com/j-syncer/Jw-sync-/issues) or post in the [community forum](https://jwsync.org/#forum).

**Want to contribute code?** The enhancement layer (`jwsync-enhancements.js` in the build source) is the cleanest entry point — it's well-structured vanilla JavaScript that handles PWA features, file handling, and UI additions. Start there.

**Translations?** The app already supports 9 languages. If you spot an error in any translation or want to add a new language, open an issue and we can work through it together.

All contributions, no matter how small, are appreciated.

---

## Roadmap

- [ ] Modular rebuild — separate JS/CSS source files with esbuild pipeline
- [ ] JSDoc documentation on all functions
- [ ] Web Worker for SQL.js (move heavy database work off the main thread)
- [ ] More export formats

---

## Acknowledgements

Thank you to everyone in the community who has tested the app, reported bugs, shared feedback, and suggested improvements. This project exists because of you.

---

*JW Sync is an independent project. It is not affiliated with, endorsed by, or connected to the Watch Tower Bible and Tract Society of Pennsylvania.*

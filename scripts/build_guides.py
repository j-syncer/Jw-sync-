#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the static SEO guide pages under /guides/ (v2.93.0).

Run from the repo root:  python3 scripts/build_guides.py
Regenerates guides/*.html and guides/index.html from the GUIDES data below.
Each page is fully static, self-contained (inline CSS, no JS), indexable,
and carries Article + HowTo + BreadcrumbList structured data.
"""
import html
import json
import os
import re

SITE = "https://jwsync.org"
TODAY = "2026-07-13"

# ── Guide content ─────────────────────────────────────────────────────────
# order here = order on guides/index.html
GUIDES = [
 {
  "slug": "merge-jw-library-backups",
  "group": "Getting started",
  "title": "How to Merge JW Library Backups from Two Devices",
  "h1": "How to merge JW Library backups from two devices",
  "description": "Combine the notes, highlights, bookmarks and tags from two or more JW Library backups into one .jwlibrary file — free, private, in your browser.",
  "intro": [
   "If you study on more than one device — a phone at the hall, a tablet at home — each device ends up with its own notes and highlights. JW Library's built-in Backup and Restore can't combine them: restoring one backup replaces everything on the device, wiping out the other device's work.",
   "JW Sync solves this. It reads two (or more) .jwlibrary backup files and merges the notes, highlights, bookmarks and tags from all of them into one new backup file. The merge runs entirely in your browser — your files are never uploaded to any server, so your personal study notes stay private.",
  ],
  "steps": [
   ("Create a backup on each device", "In JW Library, open Personal Study, tap the three-dot menu, choose Backup and Restore, then Create a backup. Do this on every device. Each one produces a .jwlibrary file."),
   ("Open JW Sync", "Go to jwsync.org in any browser — on your phone, tablet or computer. Nothing to install."),
   ("Load both backup files", "Drop in (or pick) the .jwlibrary files. JW Sync reads them locally on your device."),
   ("Review the pre-merge preview", "Before anything is written, a preview shows exactly what will be combined. If the same note was edited differently on each device, the Conflict Reviewer shows both versions side by side with a word-level diff so you choose which to keep — or let “Suggest best” pick for you."),
   ("Download the merged file and restore it", "Download the merged .jwlibrary file, then restore it on each device via Backup and Restore → Restore. Both devices now carry the complete, combined library."),
  ],
  "sections": [
   ("What gets merged?",
    "Notes, highlights, bookmarks, tags and their connections. Duplicates are detected automatically, so restoring the merged file never doubles anything up. Backups from Android, iPhone, iPad and the Windows app all use the same format and merge together freely."),
   ("Is it safe?",
    "The merge never modifies your original files — it produces a brand-new backup, so your originals remain untouched as a fallback. And because everything runs client-side in the browser, no data leaves your device."),
  ],
  "faq": [
   ("Can I merge more than two backups?", "Yes — load as many .jwlibrary files as you have devices. They are all combined into a single merged backup."),
   ("Will merging create duplicate notes?", "No. Identical notes, highlights and bookmarks are detected and kept once. Genuinely different versions of the same note are surfaced in the Conflict Reviewer for you to decide."),
   ("Does it work between Android and iPhone?", "Yes. The .jwlibrary format is identical across Android, iOS, iPadOS and Windows, so backups from different platforms merge without any conversion."),
  ],
  "related": ["sync-jw-library-multiple-devices", "transfer-jw-library-notes-new-phone", "jw-library-restore-replaced-notes"],
 },
 {
  "slug": "sync-jw-library-multiple-devices",
  "group": "Getting started",
  "title": "How to Sync JW Library Between Multiple Devices",
  "h1": "How to keep JW Library in sync between multiple devices",
  "description": "JW Library has no built-in sync between devices. Here's a simple, private routine to keep notes, highlights and bookmarks identical on your phone, tablet and computer.",
  "intro": [
   "JW Library doesn't sync personal study data between devices — there's no account that carries your notes from your phone to your tablet. The official mechanism is Backup and Restore, and a restore replaces the device's data outright. So how do you keep two or three devices identical without losing anything?",
   "The answer is a short merge-and-restore routine. Done weekly or monthly, it takes about two minutes and keeps every device carrying your complete library.",
  ],
  "steps": [
   ("Back up every device", "On each device: Personal Study → three-dot menu → Backup and Restore → Create a backup. You get one .jwlibrary file per device."),
   ("Merge the backups at jwsync.org", "Load all the files. JW Sync combines the notes, highlights, bookmarks and tags from every device into one merged .jwlibrary file — locally in your browser, nothing uploaded."),
   ("Restore the merged file on every device", "Backup and Restore → Restore, pick the merged file. Every device is now identical and complete."),
   ("Let JW Sync remind you", "Turn on a sync reminder (weekly or monthly) in JW Sync and it will nudge you when it's time to repeat the routine. It also remembers your saved devices, so each round is faster."),
  ],
  "sections": [
   ("Why not just restore the newest backup?",
    "Because “newest” only reflects one device. If you took meeting notes on the phone and study notes on the tablet the same week, each backup has content the other lacks. Restoring either one over the other loses half your work. Merging first is what makes the routine safe."),
   ("How often should I sync?",
    "Match it to how you study. Two active devices used daily: weekly is comfortable. A tablet that only comes out for meetings: monthly is plenty. The cost of waiting longer is only that the merge has more to combine — nothing is ever lost between rounds."),
  ],
  "faq": [
   ("Does JW Sync run in the background?", "No — it's a web page, not an installed service. Nothing scans your devices. You run the routine when you choose; the optional reminder is just a notification."),
   ("Can I sync three or more devices?", "Yes. Back up each one, load all the files, merge once, restore the merged file everywhere."),
  ],
  "related": ["merge-jw-library-backups", "backup-jw-library", "transfer-jw-library-notes-new-phone"],
 },
 {
  "slug": "transfer-jw-library-notes-new-phone",
  "group": "Getting started",
  "title": "How to Transfer JW Library Notes to a New Phone",
  "h1": "How to transfer JW Library notes to a new phone",
  "description": "Step-by-step: move all your JW Library notes, highlights, bookmarks and tags to a new phone with a .jwlibrary backup — and how to merge if you already made notes on the new phone.",
  "intro": [
   "Phone-transfer tools move your apps and photos, but they do not reliably move JW Library's personal study data. The dependable way to bring your notes, highlights, bookmarks and tags to a new phone is JW Library's own backup file — it takes a few minutes and works across platforms.",
  ],
  "steps": [
   ("Create a backup on the old phone", "Open JW Library → Personal Study → three-dot menu → Backup and Restore → Create a backup. This saves a .jwlibrary file containing all your study data."),
   ("Move the file to the new phone", "Email it to yourself, or use Google Drive, iCloud, AirDrop or a USB cable. The file is small — usually a few megabytes."),
   ("Restore on the new phone", "Install JW Library, then Personal Study → Backup and Restore → Restore, and choose the .jwlibrary file. All notes, highlights, bookmarks and tags appear."),
  ],
  "sections": [
   ("Already made notes on the new phone? Merge instead of overwriting",
    "Restoring replaces whatever is on the device. If you've been using the new phone for a while and it has its own notes, don't restore over them — back up the new phone too, then merge the old and new backups into one file at jwsync.org (free, in your browser, nothing uploaded) and restore the merged file. You keep both sets of notes."),
   ("A common iPhone gotcha",
    "If the backup file arrives on an iPhone renamed to .zip, rename it back to .jwlibrary before restoring — the content is fine; only the extension changed in transit."),
  ],
  "faq": [
   ("Will this move my downloaded publications too?", "The backup carries your personal study data — notes, highlights, bookmarks, tags and playlists. Publications simply re-download on the new phone."),
   ("Does it matter if the phones run different Android versions?", "No. The .jwlibrary format is the same everywhere, including across Android versions and between Android and iPhone."),
  ],
  "related": ["jw-library-android-to-iphone", "merge-jw-library-backups", "backup-jw-library"],
 },
 {
  "slug": "jw-library-android-to-iphone",
  "group": "Getting started",
  "title": "Move JW Library from Android to iPhone (Keep All Notes)",
  "h1": "Moving JW Library from Android to iPhone or iPad — keeping every note",
  "description": "The .jwlibrary backup format is identical on Android and iOS. How to move your notes, highlights and bookmarks across platforms — and merge if both devices have notes.",
  "intro": [
   "Switching platforms is the moment people fear losing years of study notes — Android-to-iPhone transfer apps skip JW Library's data entirely. The good news: JW Library's backup format is identical on Android, iPhone, iPad and Windows, so a cross-platform move is just a backup, a file transfer and a restore.",
  ],
  "steps": [
   ("Back up on the Android phone", "JW Library → Personal Study → three-dot menu → Backup and Restore → Create a backup. Save the .jwlibrary file."),
   ("Send the file to the iPhone or iPad", "Email, Google Drive, iCloud Drive — anything that moves a file. If iOS renames it to .zip on the way, rename it back to .jwlibrary."),
   ("Restore on the new device", "Install JW Library, sign in, then Backup and Restore → Restore and pick the file. Notes, highlights, bookmarks, tags and playlists all arrive."),
  ],
  "sections": [
   ("If the iPhone already has notes on it",
    "Restore replaces the device's data. When the new device already carries its own notes, back it up too and merge both backups into one file first at jwsync.org — the merge combines both libraries in your browser without uploading anything — then restore the merged file. Nothing is lost from either side."),
   ("The same steps work in every direction",
    "iPhone to Android, Android to Android, adding an iPad as a second study device, or moving to the Windows app — the backup file is the common language between all of them."),
  ],
  "faq": [
   ("Do I need a computer to do this?", "No. The whole move can be done phone-to-phone with email or a cloud drive."),
   ("Will my highlight colours survive the move?", "Yes — highlights keep their colours, notes keep their tags, and bookmarks keep their places."),
  ],
  "related": ["transfer-jw-library-notes-new-phone", "merge-jw-library-backups", "backup-jw-library"],
 },
 {
  "slug": "backup-jw-library",
  "group": "Getting started",
  "title": "How to Back Up JW Library the Right Way",
  "h1": "How to back up JW Library the right way",
  "description": "A 30-second backup routine that protects years of JW Library study notes, highlights and bookmarks — and the common mistake that catches people out.",
  "intro": [
   "A proper JW Library backup takes half a minute and protects years of accumulated study. Most data loss stories start the same way: no recent .jwlibrary file existed when a phone was lost, reset or replaced.",
  ],
  "steps": [
   ("Create the backup", "Open JW Library → Personal Study → three-dot menu → Backup and Restore → Create a backup. It produces a .jwlibrary file containing every note, highlight, bookmark and tag."),
   ("Store it somewhere off the phone", "Email it to yourself, or save it to Google Drive, iCloud or OneDrive. A backup that only lives on the phone disappears with the phone."),
   ("Repeat on a schedule", "Monthly is a good default; before any phone change, reset or OS update is essential. Keep older copies — the files are small, and an old backup has saved many people."),
  ],
  "sections": [
   ("The common mistake: trusting the phone's own cloud backup",
    "A whole-phone backup (Google One, iCloud device backup) often restores an old copy of JW Library's data — or none at all. The .jwlibrary file is the only backup you fully control and can carry between platforms. Treat the phone backup as a bonus, not the plan."),
   ("Ended up with two different backups?",
    "It happens: one backup from the phone, an older one from a tablet, each with unique notes. You never have to choose between them — merge them into one complete file at jwsync.org, free and private, right in the browser."),
  ],
  "faq": [
   ("How big is a backup file?", "Usually a few megabytes even for very large libraries — email-attachment small."),
   ("Does creating a backup change anything on my phone?", "No. It only writes the file; your library is untouched."),
  ],
  "related": ["jw-library-restore-replaced-notes", "merge-jw-library-backups", "fix-corrupted-jw-library-backup"],
 },
 {
  "slug": "jw-library-restore-replaced-notes",
  "group": "Fixing problems",
  "title": "JW Library Restore Replaced Your Notes? How to Get Them Back",
  "h1": "Restore replaced your notes? Here's how to combine both backups",
  "description": "JW Library's restore is a full swap, not a merge — notes made after the backup date seem gone. If you still have both backup files, nothing is lost. Here's the fix.",
  "intro": [
   "It's a horrible moment: you restore a backup onto a device that already had notes, and the restore replaces everything — the notes you made since that backup seem gone. This happens because JW Library's Backup and Restore is a full swap, not a merge.",
   "The key fact: if the newer work still exists in any backup file, nothing is actually lost. The fix is to merge the two backups instead of choosing between them.",
  ],
  "steps": [
   ("Stop — don't restore again", "Every restore replaces the device's current data. Pause before anything else disappears."),
   ("Back up the device as it is right now", "Personal Study → Backup and Restore → Create a backup. This preserves the current state, whatever it contains."),
   ("Find the backup with the missing notes", "The .jwlibrary file you restored from, or an earlier one — check your email, Drive, iCloud and downloads folder."),
   ("Merge both files at jwsync.org", "Load both backups. JW Sync combines all notes, highlights, bookmarks and tags from both into one new file — in your browser, nothing uploaded. Conflicting versions of the same note are shown side by side for you to pick."),
   ("Restore the merged file", "Backup and Restore → Restore with the merged .jwlibrary. Both sets of notes are back on the device."),
  ],
  "sections": [
   ("What if there's no backup of the newer notes?",
    "If the only copy of the newer notes was on the device and a restore already overwrote them, JW Library itself offers no undo. This is why step 2 above — backing up the current state before doing anything — matters so much whenever data looks wrong. Going forward, the merge-first routine makes the problem structurally impossible."),
  ],
  "faq": [
   ("Will the merge duplicate the notes both backups share?", "No — identical items are detected and kept once. Only genuinely different versions of the same note are flagged for review."),
   ("Can this fix a backup that won't restore at all?", "That's usually file damage rather than an overwrite — see the guide to fixing a corrupted backup below."),
  ],
  "related": ["fix-corrupted-jw-library-backup", "merge-jw-library-backups", "backup-jw-library"],
 },
 {
  "slug": "fix-corrupted-jw-library-backup",
  "group": "Fixing problems",
  "title": "Fix a Corrupted JW Library Backup That Won't Restore",
  "h1": "Fixing a corrupted JW Library backup with Library Doctor",
  "description": "JW Library refuses to restore your .jwlibrary file? Library Doctor scans the backup in your browser, repairs common problems, and produces a clean copy that restores.",
  "intro": [
   "Sometimes JW Library refuses a backup file — the restore fails, errors out, or the file won't open. Common causes: an interrupted download, a cloud drive that mangled the file, an extension changed in transit, or internal inconsistencies that accumulated over years of use.",
   "JW Sync includes Library Doctor, a checker that scans a .jwlibrary file and repairs the common problems — entirely in your browser, without the file ever leaving your device.",
  ],
  "steps": [
   ("Open JW Sync and load the problem file", "Go to jwsync.org and load the .jwlibrary file that won't restore. (If the file arrived renamed to .zip, rename it back to .jwlibrary first — that alone fixes many cases.)"),
   ("Run the Library Doctor scan", "The Doctor examines the backup's internal structure and lists what it finds — from harmless quirks to real damage — in plain language."),
   ("Apply the fixes", "One tap repairs what's repairable. The Doctor never edits your original file; it produces a cleaned copy, so the original stays untouched as a fallback."),
   ("Download and restore the repaired file", "Restore the cleaned .jwlibrary via Backup and Restore → Restore in JW Library."),
  ],
  "sections": [
   ("The Doctor also runs during every merge",
    "The same checks run automatically inside the merge engine, so a merged backup is always delivered clean — even when one of the input files had problems you never knew about."),
   ("When a file is beyond repair",
    "If the file was truncated badly enough that the data simply isn't in it, no tool can invent it back. The Doctor will say so honestly rather than produce a doubtful file — and that's the cue to hunt for an earlier copy in email, Drive or iCloud, which is also why keeping older backups is worth it."),
  ],
  "faq": [
   ("Is my data uploaded for the scan?", "No. The scan, the fixes and the export all run locally in the browser."),
   ("Can it recover notes deleted inside JW Library?", "No — it repairs file structure. Notes deleted in the app before the backup was made aren't in the file to recover."),
  ],
  "related": ["jw-library-restore-replaced-notes", "backup-jw-library", "merge-jw-library-backups"],
 },
 {
  "slug": "edit-jw-library-notes",
  "group": "Power tools",
  "title": "View and Edit JW Library Notes in Your Browser",
  "h1": "View, search and edit your JW Library notes — Study Explorer",
  "description": "Open any .jwlibrary backup in your browser to browse, search, edit, retag, recolour and bulk-clean your JW Library notes, highlights and bookmarks. Nothing uploaded.",
  "intro": [
   "JW Library is built for taking notes, not for managing thousands of them. Study Explorer opens any .jwlibrary backup right in your browser and turns it into a searchable, editable library manager — notes, highlights and bookmarks in one place, with nothing uploaded anywhere.",
  ],
  "steps": [
   ("Load a backup", "Create a backup in JW Library (Personal Study → Backup and Restore → Create a backup), then open jwsync.org and load the file into Study Explorer."),
   ("Browse and search everything", "Three tabs — Notes, Highlights, Bookmarks — with full-text search plus colour, tag and publication filters. A Study Answers tab shows your fill-in answers from publications too."),
   ("Edit in place", "Open any note to edit its title and content with rich-text formatting (bold, italic, underline, lists), change its highlight colour, and add or remove tags. Bookmarks and highlight colours are editable the same way."),
   ("Clean up in bulk", "Select many notes at once to retag, recolour or delete together — with full undo/redo, so a slip is never fatal. You can also extract a date range of notes into a fresh backup, or copy notes out as Markdown."),
   ("Export your edited library", "Download the edited .jwlibrary and restore it in JW Library. Your changes are now on the device."),
  ],
  "sections": [
   ("Why edit in a browser instead of the app?",
    "Scale. Renaming a tag across 300 notes, recolouring every yellow highlight in one publication, or deleting years of stale bookmarks is minutes of work here and hours of tapping in the app. The exported file is a standard backup that JW Library restores like any other."),
  ],
  "faq": [
   ("Does editing touch my original backup?", "No — edits are made to an in-browser copy and saved into a new exported file. The original stays as it was."),
   ("Is there a limit to library size?", "Very large libraries are paginated so browsing stays fast; search and filters work across everything."),
  ],
  "related": ["search-jw-library-notes", "share-jw-library-notes", "jw-library-study-stats"],
 },
 {
  "slug": "search-jw-library-notes",
  "group": "Power tools",
  "title": "Search JW Library Notes by Meaning — Ask Your Library",
  "h1": "Ask Your Library: search your JW Library notes by meaning",
  "description": "Semantic search for your JW Library notes: find that half-remembered note by describing it, even when you can't recall its exact words. On-device, offline-capable, private.",
  "intro": [
   "Everyone with years of notes knows the problem: you remember writing about enduring trials with joy, but the note doesn't contain the word “endurance”, so keyword search finds nothing. Ask Your Library searches by meaning instead — describe the thought, and it surfaces the notes closest to it, however they're worded.",
   "It runs entirely on your device: the language model is downloaded once into the browser and works offline afterwards, with WebGPU acceleration where available. Your notes are never sent anywhere.",
  ],
  "steps": [
   ("Load a backup into Study Explorer", "At jwsync.org, load your .jwlibrary file and open the Ask tab."),
   ("Let the model prepare once", "On first use the on-device model downloads and indexes your notes. This happens once; afterwards it works instantly, even offline."),
   ("Ask in your own words", "Type what you remember — “that note about being patient with new ones in service”, “encouragement for discouraged pioneers” — and the closest notes appear, ranked by meaning."),
  ],
  "sections": [
   ("How it differs from normal search",
    "Keyword search matches letters; semantic search matches ideas. A query about “anxiety” also finds notes written using “worry”, “cares of life” or a scripture citation on the theme. Both kinds of search are available in Study Explorer — they complement each other."),
   ("Private by design",
    "This is not a cloud AI service. The model runs inside your browser tab, the index lives on your device, and closing the tab is the end of it. Nothing about your notes ever leaves your machine."),
  ],
  "faq": [
   ("Does it need a powerful device?", "A modern phone or laptop handles it well; on devices with WebGPU it's fastest. There's a choice of model sizes to match your hardware."),
   ("Does it work in my language?", "Yes — search works across the languages your notes are written in, and the interface is translated into all 12 languages JW Sync supports."),
  ],
  "related": ["edit-jw-library-notes", "jw-library-study-stats", "merge-jw-library-backups"],
 },
 {
  "slug": "jw-library-study-stats",
  "group": "Power tools",
  "title": "See Your JW Library Study Stats: Streaks, Heatmaps & Awards",
  "h1": "Your JW Library study stats: streaks, heatmaps, coverage and awards",
  "description": "Turn a JW Library backup into private study analytics — totals, activity heatmap, streaks, Bible coverage across 66 books, a study personality profile and ~200 awards.",
  "intro": [
   "Your backup file quietly records years of study history — when you take notes, what you highlight, which books you've covered. The Study Stats page reads a .jwlibrary backup and turns that history into a private dashboard, computed entirely in your browser.",
  ],
  "steps": [
   ("Create a backup", "In JW Library: Personal Study → Backup and Restore → Create a backup."),
   ("Open the Study Stats page", "Go to jwsync.org/highlights.html and load the file."),
   ("Explore your study story", "Headline totals, Service-Year and All-Time views, year-over-year growth — then the fun parts below."),
  ],
  "sections": [
   ("What you'll see",
    "An activity heatmap with your longest and current streaks; weekly rhythm, busiest hours and months; Bible coverage across all 66 books with a Hebrew/Greek Scriptures split; a highlight colour wheel, note-depth histogram and word cloud; a 24-hour study clock and seasonality radar."),
   ("Profile, journey and awards",
    "A six-trait Study Profile (Consistency, Diligence, Depth, Breadth, Reflection, Steadiness) with a “Study Signature” persona; a Study Journey of 60 levels across 12 named tiers; and around 200 awards from Common to Legendary, including content-aware medals. A Shareable Card sums up your year without exposing a single note."),
   ("A daily reason to come back",
    "The Resurface panel shows notes you wrote on this day in past years and builds a gentle spaced-repetition review — a little, often, is how study sticks."),
  ],
  "faq": [
   ("Is any of this uploaded?", "No. The backup is parsed in your browser; the statistics never leave your device."),
   ("Do stats update automatically?", "They reflect the backup you load — create a fresh backup to see fresh stats."),
  ],
  "related": ["bible-reading-plan", "edit-jw-library-notes", "merge-jw-library-backups"],
 },
 {
  "slug": "share-jw-library-notes",
  "group": "Power tools",
  "title": "How to Share JW Library Notes with a Friend",
  "h1": "How to share JW Library notes with a friend — without a server",
  "description": "Send selected JW Library notes (and their highlights) to a friend as a small file — no server, no account. The receiver merges them in without overwriting their own notes.",
  "intro": [
   "JW Library has no way to give another person a copy of specific notes. Sending your whole backup would work — but it hands over everything, and restoring it would wipe the receiver's own library. JW Sync's note sharing solves both problems: pick exactly which notes to share, and the receiver adds them without losing anything.",
  ],
  "steps": [
   ("Pick the notes to share", "On the Share page at jwsync.org/share.html, load your backup and select the notes — a handful from one talk, everything under a tag, whatever you choose. Highlights attached to those notes travel along."),
   ("Send the share file", "JW Sync produces a small file containing only the selected notes. Send it by any channel you like — messaging app, email, AirDrop. There is no server and no account; the file is the whole exchange."),
   ("The receiver merges it in", "Your friend opens the same page, loads the share file together with their own backup, and gets a new backup with your notes added. Their own notes are never overwritten — if a shared note clashes with one of theirs, they choose how it's added — and imported notes arrive tagged, so they're easy to find, review or remove later."),
  ],
  "sections": [
   ("Good uses",
    "Passing on research to a study partner, sharing meeting notes with someone who was away, giving a new publisher a starter set of notes on a publication, or moving a specific project's notes to a family member — all without exposing the rest of either library."),
  ],
  "faq": [
   ("Does the receiver need JW Sync installed?", "Nothing is installed on either side — it's a web page. The receiver just needs the share file and their own backup."),
   ("Can I unshare or expire a shared file?", "The file is an ordinary file you sent — there's no server copy to expire. Share only what you'd share in any message."),
  ],
  "related": ["edit-jw-library-notes", "merge-jw-library-backups", "backup-jw-library"],
 },
 {
  "slug": "bible-reading-plan",
  "group": "Power tools",
  "title": "A Daily Bible Reading Plan with Your Own Notes Beside It",
  "h1": "Reading Companion: a Bible reading plan with your own notes beside it",
  "description": "A private daily Bible reading schedule that shows the notes and highlights you made on today's chapters. Pick your pace, keep a streak, watch the 66-book grid fill in.",
  "intro": [
   "Plenty of apps offer a Bible reading schedule. Reading Companion does something none of them can: because it reads your own .jwlibrary backup, today's reading arrives with the notes and highlights you yourself made on those exact chapters — “you highlighted four verses in Psalm 37 two years ago.” Reading through the lens of your own study history, entirely on your device.",
  ],
  "steps": [
   ("Choose an order and a pace", "Read in Bible order or approximate chronological order; finish in 3 months, 6 months, 1 year, 2 years, or set your own chapters-per-day pace — with a live “you'd finish around…” preview."),
   ("Read today's portion", "Each chapter is one tap away, opening directly in JW Library or Watchtower ONLINE LIBRARY in your language. Check chapters off as you go."),
   ("Bring your notes along (optional)", "Load a backup in any JW Sync tool and your own notes and highlight counts appear right under today's chapters."),
   ("Watch the progress build", "A 66-book grid fills in as you read, with a chapters-read bar, an on-pace forecast, and milestones for finishing each book, the Hebrew-Aramaic Scriptures, the Greek Scriptures — and the whole Bible."),
  ],
  "sections": [
   ("Streaks without guilt",
    "Completing a day grows your streak; missing a day simply moves the forecast finish date. There is no overdue pile — the plan bends to your life instead of scolding you."),
  ],
  "faq": [
   ("Do I need to load a backup to use it?", "No — the plan, streaks and progress work on their own. The backup only adds your personal notes to each day's reading."),
   ("Is my reading progress private?", "Yes. Progress lives in your browser on your device — there's no account and nothing is uploaded."),
  ],
  "related": ["jw-library-study-stats", "search-jw-library-notes", "backup-jw-library"],
 },
]

GROUPS = ["Getting started", "Fixing problems", "Power tools"]

# ── Template ──────────────────────────────────────────────────────────────
CSS = """
:root{--bg:#040f22;--card:rgba(15,28,52,.6);--line:rgba(71,85,105,.35);--txt:#e2e8f0;
--muted:#94a3b8;--accent:#ea580c;--accent-soft:#fb923c}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);
font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
-webkit-font-smoothing:antialiased}
a{color:var(--accent-soft);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.site{border-bottom:1px solid var(--line);padding:14px 0}
header.site .wrap{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:10px;color:var(--txt);font-weight:700;font-size:17px}
.brand:hover{text-decoration:none}
.brand .dot{width:26px;height:26px;border-radius:7px;background:var(--accent);display:inline-flex;
align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:800}
.hnav a{color:var(--muted);font-size:14px;margin-left:18px}
.crumbs{font-size:13px;color:var(--muted);margin:26px 0 6px}
.crumbs a{color:var(--muted)}
h1{font-size:30px;line-height:1.25;margin:8px 0 6px;letter-spacing:-.01em}
.lede{color:var(--muted);font-size:15px;margin:0 0 26px}
h2{font-size:21px;margin:38px 0 10px;letter-spacing:-.01em}
p{margin:0 0 16px}
ol.steps{counter-reset:s;list-style:none;margin:0 0 8px;padding:0}
ol.steps li{counter-increment:s;position:relative;padding:0 0 20px 52px}
ol.steps li::before{content:counter(s);position:absolute;left:0;top:2px;width:32px;height:32px;
border-radius:50%;background:var(--accent);color:#fff;font-weight:700;font-size:15px;
display:flex;align-items:center;justify-content:center}
ol.steps h3{margin:0 0 4px;font-size:16.5px}
ol.steps p{margin:0;color:var(--muted);font-size:15px}
.cta{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;
padding:20px 22px;margin:34px 0}
.cta strong{display:block;font-size:17px;margin-bottom:4px}
.cta span{color:var(--muted);font-size:14.5px}
.cta .btn{display:inline-block;margin-top:14px;background:var(--accent);color:#fff;font-weight:600;
font-size:15px;padding:10px 22px;border-radius:9px;box-shadow:0 1px 5px rgba(0,0,0,.35)}
.cta .btn:hover{text-decoration:none;filter:brightness(1.07)}
.faq dt{font-weight:600;margin:18px 0 4px}
.faq dd{margin:0;color:var(--muted);font-size:15px}
.related{margin:8px 0 0;padding:0;list-style:none}
.related li{margin:0 0 8px}
footer.site{border-top:1px solid var(--line);margin-top:56px;padding:26px 0 40px;
color:#64748b;font-size:12.5px}
footer.site p{margin:0 0 10px}
.gcards{display:grid;grid-template-columns:1fr;gap:12px;margin:14px 0 0;padding:0;list-style:none}
@media(min-width:640px){.gcards{grid-template-columns:1fr 1fr}}
.gcards a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px 18px;color:var(--txt);height:100%}
.gcards a:hover{text-decoration:none;border-color:var(--accent)}
.gcards strong{display:block;font-size:15.5px;margin-bottom:4px}
.gcards span{color:var(--muted);font-size:13.5px;line-height:1.55;display:block}
""".strip()

FOOTER = (
 '<footer class="site"><div class="wrap">'
 '<p><a href="{root}">JW Sync</a> · <a href="{root}guides/">All guides</a> · '
 '<a href="{root}forum.html">Community</a> · <a href="{root}highlights.html">Study Stats</a></p>'
 '<p>JW Sync processes all data locally — your files never leave your device. '
 'Free to use; no account, no uploads.</p>'
 '<p>“JW Library” is the property of the Watch Tower Bible and Tract Society of Pennsylvania. '
 'JW Sync is an independent utility and is not affiliated with or endorsed by it.</p>'
 '</div></footer>'
)

def esc(s):
    return html.escape(s, quote=True)

def head(title, description, canonical, jsonld):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#040f22">
<link rel="icon" href="/favicon.ico">
<meta property="og:site_name" content="JW Sync">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>"""

def site_header(root):
    return (f'<header class="site"><div class="wrap">'
            f'<a class="brand" href="{root}"><span class="dot">JW</span>JW Sync</a>'
            f'<nav class="hnav"><a href="{root}guides/">Guides</a>'
            f'<a href="{root}forum.html">Community</a>'
            f'<a href="{root}">Open the app</a></nav>'
            f'</div></header>')

def guide_jsonld(g, canonical):
    graph = [
        {
            "@type": "Article",
            "headline": g["title"],
            "description": g["description"],
            "inLanguage": "en",
            "datePublished": TODAY,
            "dateModified": TODAY,
            "mainEntityOfPage": canonical,
            "image": f"{SITE}/og-image.png",
            "author": {"@type": "Organization", "name": "JW Sync", "url": SITE},
            "publisher": {"@type": "Organization", "name": "JW Sync", "url": SITE},
        },
        {
            "@type": "HowTo",
            "name": g["title"],
            "description": g["description"],
            "inLanguage": "en",
            "totalTime": "PT5M",
            "tool": [{"@type": "HowToTool", "name": "JW Sync (jwsync.org)"}],
            "step": [
                {"@type": "HowToStep", "position": i + 1, "name": name, "text": text}
                for i, (name, text) in enumerate(g["steps"])
            ],
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "JW Sync", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides/"},
                {"@type": "ListItem", "position": 3, "name": g["title"], "item": canonical},
            ],
        },
    ]
    if g.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in g["faq"]
            ],
        })
    return {"@context": "https://schema.org", "@graph": graph}

def build_guide(g):
    canonical = f"{SITE}/guides/{g['slug']}"
    root = "../"
    by_slug = {x["slug"]: x for x in GUIDES}
    parts = [head(g["title"] + " | JW Sync Guides", g["description"], canonical,
                  guide_jsonld(g, canonical))]
    parts.append(site_header(root))
    parts.append('<main class="wrap">')
    parts.append(f'<nav class="crumbs"><a href="{root}">JW Sync</a> › '
                 f'<a href="./">Guides</a> › {esc(g["group"])}</nav>')
    parts.append(f"<h1>{esc(g['h1'])}</h1>")
    parts.append(f'<p class="lede">{esc(g["description"])}</p>')
    for p in g["intro"]:
        parts.append(f"<p>{esc(p)}</p>")
    parts.append("<h2>Step by step</h2><ol class=\"steps\">")
    for name, text in g["steps"]:
        parts.append(f"<li><h3>{esc(name)}</h3><p>{esc(text)}</p></li>")
    parts.append("</ol>")
    parts.append('<div class="cta"><strong>Do it now — free, in your browser</strong>'
                 '<span>JW Sync merges, edits and analyses .jwlibrary backups entirely on your '
                 'device. No account, no uploads, nothing installed.</span>'
                 f'<a class="btn" href="{root}">Open JW Sync →</a></div>')
    for h2, body in g["sections"]:
        parts.append(f"<h2>{esc(h2)}</h2><p>{esc(body)}</p>")
    if g.get("faq"):
        parts.append('<h2>Frequently asked questions</h2><dl class="faq">')
        for q, a in g["faq"]:
            parts.append(f"<dt>{esc(q)}</dt><dd>{esc(a)}</dd>")
        parts.append("</dl>")
    parts.append('<h2>Related guides</h2><ul class="related">')
    for slug in g["related"]:
        r = by_slug[slug]
        parts.append(f'<li><a href="{slug}">{esc(r["title"])}</a></li>')
    parts.append("</ul></main>")
    parts.append(FOOTER.format(root=root))
    parts.append("</body>\n</html>\n")
    return "".join(parts)

def build_index():
    canonical = f"{SITE}/guides/"
    root = "../"
    title = "JW Library Backup, Sync & Notes Guides | JW Sync"
    description = ("Practical guides for JW Library backups: merge backups from two devices, "
                   "transfer notes to a new phone, move Android to iPhone, fix a backup that "
                   "won't restore, edit and search your notes, and more.")
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": title,
                "description": description,
                "url": canonical,
                "inLanguage": "en",
                "isPartOf": {"@type": "WebSite", "name": "JW Sync", "url": SITE},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "JW Sync", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2, "name": "Guides", "item": canonical},
                ],
            },
        ],
    }
    parts = [head(title, description, canonical, jsonld)]
    parts.append(site_header(root))
    parts.append('<main class="wrap">')
    parts.append(f'<nav class="crumbs"><a href="{root}">JW Sync</a> › Guides</nav>')
    parts.append("<h1>Guides &amp; how-tos</h1>")
    parts.append('<p class="lede">Everything about JW Library backups, in plain steps: merging '
                 'devices, moving to a new phone, rescuing notes, and getting more out of the '
                 'library you already have. Every tool mentioned runs free in your browser — '
                 'your files are never uploaded.</p>')
    for group in GROUPS:
        parts.append(f"<h2>{esc(group)}</h2><ul class=\"gcards\">")
        for g in GUIDES:
            if g["group"] != group:
                continue
            parts.append(f'<li><a href="{g["slug"]}"><strong>{esc(g["title"])}</strong>'
                         f'<span>{esc(g["description"])}</span></a></li>')
        parts.append("</ul>")
    parts.append('<div class="cta"><strong>Skip the reading — just open the tool</strong>'
                 '<span>Merging two backups takes about a minute and the app walks you through '
                 'it.</span>'
                 f'<a class="btn" href="{root}">Open JW Sync →</a></div>')
    parts.append("</main>")
    parts.append(FOOTER.format(root=root))
    parts.append("</body>\n</html>\n")
    return "".join(parts)

def main():
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(repo, "guides")
    os.makedirs(outdir, exist_ok=True)
    for g in GUIDES:
        path = os.path.join(outdir, g["slug"] + ".html")
        html_out = build_guide(g)
        json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                             html_out, re.S).group(1))  # sanity: JSON-LD parses
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote", os.path.relpath(path, repo))
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index())
    print("wrote guides/index.html")
    print(f"{len(GUIDES)} guides + index")

if __name__ == "__main__":
    main()

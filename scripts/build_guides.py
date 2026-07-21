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
 {
  "slug": "open-jwlibrary-file",
  "group": "Getting started",
  "title": "What Is a .jwlibrary File and How Do You Open It?",
  "h1": "What is a .jwlibrary file — and how to open one on any device",
  "description": "A .jwlibrary file is your JW Library backup: a single file holding every note, highlight, bookmark and tag. Here's what's inside it and how to open and read it.",
  "intro": [
   "When you back up JW Library you get a file ending in .jwlibrary. It's a single, portable package that contains everything from your personal study — notes, highlights, bookmarks, tags and playlists — in a compact database. It is not a document you open in Word or a PDF reader; it's designed to be restored back into JW Library.",
   "But you don't have to restore it just to look inside. JW Sync opens a .jwlibrary file directly in your browser so you can read, search and edit its contents without touching your phone.",
  ],
  "steps": [
   ("Get a .jwlibrary file", "It's created in JW Library: Personal Study → three-dot menu → Backup and Restore → Create a backup. That's the file we're talking about."),
   ("Open it in JW Sync", "Go to jwsync.org and load the file into Study Explorer. It opens instantly, on your device — nothing is uploaded."),
   ("Read and work with it", "Browse notes, highlights and bookmarks; search across everything; edit, retag or export. When you're done you can restore the file (or an edited copy) back into JW Library."),
  ],
  "sections": [
   ("What's actually inside the file",
    "Technically a .jwlibrary file is a zipped SQLite database plus a manifest. That's why renaming it to .zip sometimes happens by accident in transit — and why renaming it back to .jwlibrary fixes it. You never need to know any of that to use it, but it explains why the file is small, self-contained and identical across Android, iPhone, iPad and Windows."),
   ("Opening it on a computer",
    "The same jwsync.org page works on a laptop or desktop browser — handy for reading years of notes on a big screen, or doing bulk clean-up that would be tedious on a phone. There's nothing to install."),
  ],
  "faq": [
   ("Can I open a .jwlibrary file in Excel or Notepad?", "Not usefully — it's a database, not a spreadsheet or text file. Open it in JW Sync to read it, or export your notes to Markdown/text from Study Explorer."),
   ("Is it safe to open my backup in the browser?", "Yes. JW Sync reads the file locally in your browser tab; nothing is sent to a server, and your original file is never modified."),
  ],
  "related": ["backup-jw-library", "edit-jw-library-notes", "export-jw-library-notes"],
 },
 {
  "slug": "jw-library-windows-pc",
  "group": "Getting started",
  "title": "Back Up and Merge JW Library on a Windows PC",
  "h1": "Using JW Library backups on a Windows PC",
  "description": "How to back up JW Library on Windows, and how to merge a PC backup with your phone and tablet so notes, highlights and bookmarks stay together on every device.",
  "intro": [
   "JW Library runs on Windows as well as phones and tablets, and it makes the same .jwlibrary backup file. That means your PC can be part of the same study library as your phone — as long as you merge the backups rather than restoring one over another.",
  ],
  "steps": [
   ("Back up on Windows", "In the JW Library Windows app, open the menu, go to Backup and Restore, and create a backup. Save the .jwlibrary file somewhere easy to find."),
   ("Back up your phone and tablet too", "On each device: Personal Study → three-dot menu → Backup and Restore → Create a backup."),
   ("Merge them at jwsync.org", "Open jwsync.org in any browser on the PC and load all the backup files. JW Sync combines the notes, highlights, bookmarks and tags from every device into one merged .jwlibrary file — locally, nothing uploaded."),
   ("Restore the merged file everywhere", "Restore the merged file in the Windows app and on each mobile device. Now the PC, phone and tablet all carry the complete library."),
  ],
  "sections": [
   ("Why the PC is the easiest place to do this",
    "A desktop browser makes loading several files, reviewing the merge preview and saving the result far quicker than tapping on a phone. Many people keep their master merge routine on the computer and just restore the merged file back to their mobile devices."),
  ],
  "faq": [
   ("Does the Windows backup work with iPhone and Android backups?", "Yes — the .jwlibrary format is identical on every platform, so a Windows backup merges freely with phone and tablet backups."),
   ("Do I need to install anything on the PC?", "No. JW Sync is a web page; it runs in Edge, Chrome or Firefox with nothing to install."),
  ],
  "related": ["merge-jw-library-backups", "sync-jw-library-multiple-devices", "open-jwlibrary-file"],
 },
 {
  "slug": "recover-jw-library-notes-lost-phone",
  "group": "Fixing problems",
  "title": "How to Recover JW Library Notes After a Lost or Broken Phone",
  "h1": "Recovering JW Library notes from a lost, broken or reset phone",
  "description": "Lost your phone or had it reset with JW Library notes on it? What you can recover depends on your backups. Here's exactly how to get your notes back — and what to do next time.",
  "intro": [
   "Losing a phone is stressful enough without fearing you've lost years of study notes with it. Whether you can recover them comes down to one question: does a .jwlibrary backup exist anywhere outside that phone?",
   "This guide walks through finding any backup you may have — even ones you forgot you made — and turning it back into a full JW Library on your new device.",
  ],
  "steps": [
   ("Search every place a backup might be", "Check your email (search for “jwlibrary” or “backup”), Google Drive, iCloud Drive, OneDrive, Dropbox and your computer's Downloads folder. Backups are small files that are easy to forget you saved."),
   ("Check your other devices", "If you ever used JW Library on a tablet or PC, it has its own study data — create a backup from it right now to preserve whatever it holds."),
   ("Restore what you find on the new phone", "Install JW Library on the new device, then Backup and Restore → Restore, and load the .jwlibrary file. Your notes, highlights and bookmarks return."),
   ("Merge if you find more than one backup", "Different devices or dates may each hold unique notes. Don't pick just one — load them all at jwsync.org, merge them into a single complete file, and restore that. Nothing is left behind."),
  ],
  "sections": [
   ("If no backup exists anywhere",
    "Be honest with yourself early: if the only copy of your notes lived on the lost phone and you never exported a backup, JW Library keeps no cloud copy to restore from. That's painful — and it's exactly why the habit below matters so much."),
   ("Never be here again",
    "Set a monthly backup reminder and store each .jwlibrary file off the phone (email it to yourself is enough). JW Sync can even remind you and merge your devices on a schedule. A file that lives in your inbox survives any phone."),
  ],
  "faq": [
   ("Can JW Sync recover notes from a phone I no longer have?", "No tool can — recovery depends on a backup file existing somewhere. JW Sync's job is to read, repair and merge the backups you do have."),
   ("My backup is old — is it still worth restoring?", "Absolutely. An old backup with most of your notes beats starting from nothing, and you can merge it with anything newer you find later."),
  ],
  "related": ["backup-jw-library", "merge-jw-library-backups", "fix-corrupted-jw-library-backup"],
 },
 {
  "slug": "handle-merge-conflicts",
  "group": "Fixing problems",
  "title": "Same Note Edited on Two Devices? Handling Merge Conflicts",
  "h1": "Handling merge conflicts: the same note edited on two devices",
  "description": "When you edit the same JW Library note differently on two devices, merging has to choose a winner. The Conflict Reviewer shows both versions side by side so you decide — nothing is lost.",
  "intro": [
   "Most of merging is effortless — notes unique to each device simply combine. The one case that needs a decision is a genuine conflict: the same note, edited differently on two devices, so the two backups disagree about what it should say. JW Sync never guesses silently; it hands the choice to you.",
  ],
  "steps": [
   ("Load both backups", "At jwsync.org, load the .jwlibrary files from both devices. JW Sync compares them as it merges."),
   ("Open the Conflict Reviewer", "If any notes conflict, the reviewer lists them. Everything that didn't conflict is already merged — this step is only for the genuine clashes."),
   ("Compare side by side", "Each conflict shows both versions with a word-level diff highlighting exactly what differs. “Suggest best” can pick the fuller version for you, or you choose the one to keep — per note."),
   ("Finish and restore", "Once every conflict is resolved, download the merged file and restore it. Both devices now agree, with your chosen version of each note."),
  ],
  "sections": [
   ("Why this beats just keeping the newest",
    "“Newest wins” quietly deletes edits you may have wanted. Maybe the older version had a paragraph you removed by accident on the other device. Seeing both, word for word, means you never lose text without knowing it — which is the whole point of merging instead of overwriting."),
   ("How conflicts happen in the first place",
    "Usually from editing offline on two devices between merges, or restoring an old backup and then adding to it. Merging on a regular schedule keeps the number of conflicts small and the differences fresh in your memory."),
  ],
  "faq": [
   ("Will I have to review hundreds of conflicts?", "Rarely. Only notes edited differently on both sides conflict; new notes, and notes changed on just one device, merge automatically. Most merges have a handful of conflicts or none."),
   ("Can I change my mind after choosing?", "Yes — nothing is written to a device until you restore the merged file, and your original backups are never modified, so you can redo the merge."),
  ],
  "related": ["merge-jw-library-backups", "sync-jw-library-multiple-devices", "jw-library-restore-replaced-notes"],
 },
 {
  "slug": "export-jw-library-notes",
  "group": "Power tools",
  "title": "How to Export JW Library Notes to Text or Markdown",
  "h1": "Exporting your JW Library notes to text, Markdown or a fresh backup",
  "description": "Get your JW Library notes out of the app: copy or export them as Markdown/plain text for use anywhere, or extract a selection into a new .jwlibrary backup. All in your browser.",
  "intro": [
   "Your study notes shouldn't be trapped inside one app. Sometimes you want them as plain text — to paste into a talk outline, a document, or your own notes app — and sometimes you want a clean backup containing just a subset. Study Explorer does both, reading your backup entirely in the browser.",
  ],
  "steps": [
   ("Load your backup", "Create a backup in JW Library (Personal Study → Backup and Restore → Create a backup), then open jwsync.org and load it into Study Explorer."),
   ("Find the notes you want", "Use search plus colour, tag and publication filters to narrow to exactly the notes you're after — one publication, one tag, one topic."),
   ("Copy or export as Markdown/text", "Copy notes out as Markdown or plain text to paste anywhere. Formatting (bold, italic, lists) is preserved so structured notes stay structured."),
   ("Or extract to a fresh backup", "Prefer a file? Export a selection or date range into a new .jwlibrary backup — useful for archiving a project or handing a specific set of notes to another device."),
  ],
  "sections": [
   ("Why export at all",
    "Notes are more useful when they can travel: into a document for a part on the meeting, into a personal wiki, into a printout for someone who doesn't use the app. Markdown keeps the structure while staying readable as plain text anywhere."),
  ],
  "faq": [
   ("Does exporting change my JW Library notes?", "No. Export reads a copy of your backup in the browser; your original file and your app are untouched."),
   ("Can I export everything at once?", "Yes — clear the filters to select your whole library, or narrow down first to export just part of it."),
  ],
  "related": ["edit-jw-library-notes", "extract-jw-library-notes-by-date", "open-jwlibrary-file"],
 },
 {
  "slug": "organize-jw-library-tags",
  "group": "Power tools",
  "title": "How to Organize and Clean Up JW Library Tags",
  "h1": "Organizing your JW Library tags: rename, merge and clean up in bulk",
  "description": "Tags multiply over years of study. Rename a tag across every note, merge duplicates, and remove ones you no longer use — in bulk, in your browser, with full undo.",
  "intro": [
   "Tags are how you find notes later — but after a few years they sprawl. You end up with “Ministry”, “ministry” and “Field service” meaning the same thing, tags you made once and never reused, and inconsistent naming that makes filtering unreliable. JW Library gives you no way to fix this at scale. Study Explorer does.",
  ],
  "steps": [
   ("Load your backup into Study Explorer", "At jwsync.org, load your .jwlibrary file. Filter by tag to see every tag and how many notes carry it."),
   ("Rename a tag across all its notes", "Retag in bulk: rename a tag once and every note using it updates — no more editing notes one by one to fix a spelling."),
   ("Merge duplicates", "Retag notes from a duplicate tag onto the canonical one, then drop the empty duplicate. “Ministry” and “ministry” become one clean tag."),
   ("Remove tags you no longer use", "Select and delete stale tags in bulk. Everything is undoable, so an over-eager clean-up is never permanent."),
   ("Export the tidied library", "Download the edited .jwlibrary and restore it in JW Library. Your tags are consistent everywhere."),
  ],
  "sections": [
   ("A tag system that actually helps",
    "Once tags are consistent, filtering becomes trustworthy — one tap shows every note on a theme, across every publication. It's the difference between tags as clutter and tags as a real index of your study."),
  ],
  "faq": [
   ("Will bulk retagging touch the note text?", "No — it only changes which tags are attached. Your note titles and content stay exactly as written."),
   ("Is there an undo if I make a mistake?", "Yes. Study Explorer has full undo/redo, and your original backup is never modified — the changes go into an exported copy."),
  ],
  "related": ["edit-jw-library-notes", "manage-jw-library-highlights", "search-jw-library-notes"],
 },
 {
  "slug": "manage-jw-library-highlights",
  "group": "Power tools",
  "title": "How to Manage and Recolour JW Library Highlights",
  "h1": "Managing your JW Library highlights: recolour and organize in bulk",
  "description": "Bring order to years of JW Library highlights: change colours in bulk, give your colour code a consistent meaning, and browse every highlight in one place. In your browser.",
  "intro": [
   "Highlight colours only help if they mean something consistent. Over time most people's highlights drift — yellow meant one thing in 2019 and something else now, and there's no way in JW Library to see them all together or fix them at scale. Study Explorer gathers every highlight into one view and lets you recolour in bulk.",
  ],
  "steps": [
   ("Load your backup", "At jwsync.org, open your .jwlibrary file in Study Explorer and switch to the Highlights tab."),
   ("Browse and filter your highlights", "See every highlight in one list, filter by colour or publication, and search the highlighted text and any linked notes."),
   ("Recolour in bulk", "Select many highlights and change their colour together — for example, unify everything you meant as “key scripture” to one colour across your whole library."),
   ("Edit linked notes too", "Where a highlight has a note attached, edit that note's title and content right here as well."),
   ("Export and restore", "Download the edited .jwlibrary and restore it in JW Library so your consistent colour code is on every device."),
  ],
  "sections": [
   ("Decide what your colours mean",
    "A simple scheme — one colour for main points, one for scriptures to memorise, one for questions to research — turns highlights into a study tool instead of decoration. Recolouring in bulk lets you apply that scheme retroactively to years of reading."),
  ],
  "faq": [
   ("Can I see highlights that have no note attached?", "Yes — the Highlights tab shows all of them, with or without a linked note."),
   ("Does recolouring affect the underlying text?", "No, it only changes the highlight colour; the publication text and your notes are untouched."),
  ],
  "related": ["organize-jw-library-tags", "edit-jw-library-notes", "jw-library-study-stats"],
 },
 {
  "slug": "jw-library-study-answers",
  "group": "Power tools",
  "title": "View and Edit Your JW Library Fill-in Study Answers",
  "h1": "Finding your JW Library study answers (fill-in answers) in one place",
  "description": "Your typed answers to study-article and workbook questions are hidden in your backup. Study Explorer's Study Answers tab lets you read, search and edit them all at once.",
  "intro": [
   "As you study, you type answers into the fill-in boxes of study articles, the Watchtower, and meeting workbooks. They're saved in your backup — but JW Library only shows each one buried in its own publication. There's no single place to review everything you've written. Study Explorer's Study Answers tab is that place.",
  ],
  "steps": [
   ("Load your backup into Study Explorer", "At jwsync.org, load your .jwlibrary file and open the Study Answers tab."),
   ("Read all your answers together", "Every fill-in answer you've typed appears in one searchable list, so you can review a whole study article's worth of your own thinking at a glance."),
   ("Search and edit", "Find an answer by its text, then edit and polish it in place — helpful when reviewing before a meeting or tidying up rushed wording."),
   ("Export or restore", "Restore the edited file to carry your changes back to JW Library, or copy answers out as text for a talk or personal record."),
  ],
  "sections": [
   ("Why this is useful before meetings",
    "Reviewing your prepared answers in one continuous list — rather than scrolling each paragraph in the app — is a faster way to refresh what you planned to say, and to spot answers you left blank."),
  ],
  "faq": [
   ("Are these the same as my personal notes?", "No — fill-in answers are the responses you typed into a publication's answer boxes. Study Explorer shows them on their own tab, separate from freeform notes."),
   ("Is anything uploaded to read my answers?", "No. Like everything in JW Sync, your backup is read locally in the browser and never sent anywhere."),
  ],
  "related": ["edit-jw-library-notes", "export-jw-library-notes", "search-jw-library-notes"],
 },
 {
  "slug": "extract-jw-library-notes-by-date",
  "group": "Power tools",
  "title": "Extract JW Library Notes from a Date Range into a New Backup",
  "h1": "Extracting a date range of JW Library notes into a fresh backup",
  "description": "Pull just the notes from a specific period — a service year, a convention, a study project — into their own clean .jwlibrary backup. Entirely in your browser.",
  "intro": [
   "Sometimes you want a slice of your library, not all of it: this year's notes for a review, everything from a convention, or a single project's research to pass to someone. Study Explorer can extract notes from a date range into a brand-new .jwlibrary backup, leaving your main library untouched.",
  ],
  "steps": [
   ("Load your backup", "At jwsync.org, open your .jwlibrary file in Study Explorer."),
   ("Set the date range", "Choose the start and end dates for the notes you want — a service year, a month, a specific event's dates."),
   ("Extract to a new backup", "Export the matching notes into a fresh .jwlibrary file. It contains only that period's notes, highlights and their tags."),
   ("Use the extracted file", "Restore it into JW Library for a focused review, archive it, or share it with someone who only needs that slice."),
  ],
  "sections": [
   ("Good reasons to extract by date",
    "A yearly archive of your study; a clean file of convention notes to keep separate; handing a study partner only the notes from a project you worked on together; or trimming a huge library into manageable, dated pieces — all without disturbing your main backup."),
  ],
  "faq": [
   ("Does extracting remove those notes from my library?", "No. It copies the matching notes into a new file; your original backup keeps everything."),
   ("What date does it use — when I wrote or last edited the note?", "It uses the note's own timestamps in the backup, so the range reflects when the notes were created or modified."),
  ],
  "related": ["export-jw-library-notes", "share-jw-library-notes", "edit-jw-library-notes"],
 },
 {
  "slug": "connect-jw-library-notes-study-map",
  "group": "Power tools",
  "title": "See How Your JW Library Notes Connect — Study Map",
  "h1": "Study Map: a private knowledge graph of your JW Library notes",
  "description": "Study Map turns your JW Library notes into an interactive web, linking them by shared scriptures, shared tags and similar wording — so you can see the themes running through your study.",
  "intro": [
   "Years of notes hold connections you've never seen: the same scripture cited across a dozen entries, a theme you keep returning to, ideas that echo each other in different publications. Study Map draws those links as an interactive graph, so the shape of your own study becomes visible.",
  ],
  "steps": [
   ("Open the Study Stats page and load a backup", "Go to jwsync.org/highlights.html and load your .jwlibrary file. Study Map reads it in your browser."),
   ("Open Study Map", "Launch the map to see your notes as connected points, linked by shared scriptures, shared tags and similar wording."),
   ("Explore the connections", "Switch between Topics and Notes views, hover to spotlight a note's links, drag things around, and use the strength slider to show only the closest connections. Full-screen mode gives you room to roam."),
   ("Build and save study chains", "Draw your own manual “study chains” between related notes to capture a line of reasoning, and export the map as a PNG image to keep or share."),
  ],
  "sections": [
   ("What the map reveals",
    "Clusters show the themes you study most; a scripture linked to many notes shows a verse you keep coming back to; an isolated note might be a thread worth developing. It's a way to study your study — and to prepare talks by following the connections you've already made."),
  ],
  "faq": [
   ("Do I need a lot of notes for the map to be useful?", "A modest library already shows connections; the richer your notes, the more the map reveals. Very small libraries will show a hint to add more notes first."),
   ("Is the map private?", "Entirely. It's built in your browser from your backup and never uploaded; even the PNG export is generated on your device."),
  ],
  "related": ["jw-library-study-stats", "search-jw-library-notes", "review-old-jw-library-notes"],
 },
 {
  "slug": "review-old-jw-library-notes",
  "group": "Power tools",
  "title": "How to Review Your Old JW Library Notes (So They Stick)",
  "h1": "Reviewing old JW Library notes with Resurface — a little, often",
  "description": "Notes you never revisit are notes you forget. Resurface shows what you wrote on this day in past years and builds a gentle spaced-repetition review, so past study keeps working for you.",
  "intro": [
   "Most study notes are written once and never seen again. That's a quiet waste — the insight was worth capturing, then it sank to the bottom of the library. Resurface brings your own past notes back to the surface, a few at a time, so revisiting them becomes a small daily habit instead of a someday project.",
  ],
  "steps": [
   ("Open the Study Stats page and load a backup", "Go to jwsync.org/highlights.html and load your .jwlibrary file. Resurface reads your notes locally."),
   ("See “On this day”", "Resurface surfaces notes you wrote on this date in previous years — “written two years ago today” — reconnecting you with past study at the moment it's most meaningful."),
   ("Do a short daily review", "It presents a handful of notes to revisit and mark as reviewed. A little, often, is how study sticks — and a streak grows as you keep the habit."),
   ("Come back tomorrow", "Spaced repetition schedules notes to reappear over time, so the ones worth remembering keep coming back until they're yours."),
  ],
  "sections": [
   ("Why spaced repetition works",
    "Reviewing something just as you're about to forget it is far more effective than cramming. By spreading a few notes across many days, Resurface turns your existing library into an ongoing, low-effort review that steadily deepens what you've studied."),
  ],
  "faq": [
   ("Where does my review progress get saved?", "In your browser on your device — there's no account and nothing is uploaded. The streak and schedule are yours alone."),
   ("Do I need new notes for this?", "No — Resurface works with the notes you've already written. The older your library, the more rewarding the “on this day” moments."),
  ],
  "related": ["jw-library-study-stats", "connect-jw-library-notes-study-map", "jw-library-achievements-streaks"],
 },
 {
  "slug": "jw-library-achievements-streaks",
  "group": "Power tools",
  "title": "JW Library Study Streaks, Levels and Achievements",
  "h1": "Turn your JW Library study into streaks, levels and awards",
  "description": "See your study streaks, climb 60 levels across 12 tiers on your Study Journey, and unlock around 200 achievements — all read privately from your own JW Library backup.",
  "intro": [
   "Consistency is the hard part of personal study, and progress you can't see is easy to let slide. The Study Stats page turns your backup's history into something you can watch grow: streaks, levels and awards that reflect the study you've genuinely done — no goals imposed, just your own record made visible.",
  ],
  "steps": [
   ("Open the Study Stats page", "Go to jwsync.org/highlights.html and load your .jwlibrary backup. Everything is computed in your browser."),
   ("Check your streaks", "See your longest and current study streaks, your weekly rhythm, and your busiest hours and months — the pulse of your study habit."),
   ("Climb your Study Journey", "Progress through 60 levels across 12 named tiers (Seed all the way to Evergreen), with a colour-shifting orb and level-up celebrations, based on your lifetime study."),
   ("Collect achievements", "Unlock around 200 awards spanning Common to Legendary rarity, including content-aware, themed medals; open any medal to see your progress toward the next one."),
  ],
  "sections": [
   ("Motivation without pressure",
    "These aren't targets someone else set — they're a mirror of what you've already done. Seeing a streak you don't want to break, or a level almost reached, is a gentle nudge to keep the good habit going. And a Shareable Card sums up your year without exposing a single private note."),
  ],
  "faq": [
   ("Do streaks and awards update on their own?", "They reflect the backup you load, so create a fresh backup to see your latest progress. Nothing runs in the background."),
   ("Is any of this shared or uploaded?", "No. It's all computed locally from your backup; only the summary card is something you can choose to share, and it contains no note text."),
  ],
  "related": ["jw-library-study-stats", "review-old-jw-library-notes", "bible-reading-plan"],
 },
 {
  "slug": "share-convention-assembly-notes",
  "group": "Power tools",
  "title": "How to Share Convention and Assembly Notes from JW Library",
  "h1": "Sharing your convention, assembly and meeting notes",
  "description": "Pass your convention, assembly or meeting notes to family and friends as a small file — without handing over your whole library or overwriting theirs. A practical use of note sharing.",
  "intro": [
   "You took careful notes through a convention; a friend who missed a session would love them; family members want the points for their own review. Sending your entire backup is overkill and would wipe out the receiver's own notes if restored. Note sharing lets you pass along exactly the notes you want — and lets the receiver keep everything they already have.",
  ],
  "steps": [
   ("Load your backup on the Share page", "Go to jwsync.org/share.html and load your .jwlibrary file."),
   ("Select just the convention notes", "Pick the notes to share — filter by the tag you used for the event, or by date, and select that set. Highlights attached to those notes come along."),
   ("Send the small share file", "JW Sync makes a small file containing only those notes. Send it however you like — messaging app, email, AirDrop. No server, no account."),
   ("Family and friends merge it in", "Each person opens the same page, loads your file with their own backup, and gets a new backup with your notes added. Their own notes are never overwritten, and your imported notes arrive tagged so they're easy to find."),
  ],
  "sections": [
   ("A tag makes this effortless",
    "If you tag your notes during the event (say, “2026 Convention”), selecting them afterward is one filter click. It's worth starting a fresh tag at the beginning of any convention, assembly or special meeting for exactly this reason."),
  ],
  "faq": [
   ("Can I share with several people at once?", "Yes — the share file is just a file. Send it to as many people as you like; each merges it into their own library independently."),
   ("Will my whole library be exposed?", "No. Only the notes you select are in the file; the rest of your library stays private."),
  ],
  "related": ["share-jw-library-notes", "extract-jw-library-notes-by-date", "organize-jw-library-tags"],
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

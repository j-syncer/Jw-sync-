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
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides_i18n import CHROME, GUIDE_TEXT  # noqa: E402

SITE = "https://jwsync.org"
TODAY = "2026-07-13"

# English lives at /guides/<slug>; every other language at /guides/<lang>/<slug>,
# so the existing URLs — and their rankings — are untouched.
LANGS = ["en", "es", "pt", "fr", "de", "it", "ru", "ja", "ko", "tl", "sv", "ceb", "ar"]
RTL_LANGS = {"ar"}

# Languages that actually have translated guide copy. A language listed in
# LANGS but absent here keeps pointing at the English guides, and is left out
# of the hreflang cluster — announcing an alternate that does not exist is
# worse for SEO than announcing none.
TRANSLATED = sorted(set(GUIDE_TEXT) | {"en"})

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
   ("What is actually inside a .jwlibrary file",
    "A .jwlibrary backup is a ZIP archive. Rename a copy to .zip and open it and you will find userData.db — a SQLite database holding every note, highlight, bookmark and tag you have ever made — alongside a small manifest.json describing the backup. Your notes live in a Note table, your highlights in UserMark and BlockRange, your bookmarks in Bookmark, and your tags in Tag and TagMap. Understanding that the backup is a complete database, not a set of loose files, explains everything else on this page: it is why a restore is all-or-nothing, and why two backups can be combined at all."),
   ("Why JW Library's own Restore cannot merge",
    "When you restore, JW Library does not read your backup and add the missing items to what is already on the device. It replaces the device's database with the one from the file. That is a deliberate, safe design — it guarantees the device ends up in a known state — but it means restoring your tablet's backup onto your phone discards everything the phone had that the tablet did not. There is no setting to change this, which is exactly the gap a merge fills: it produces a single file that already contains both devices' work, so whichever device you restore it to ends up complete."),
   ("How duplicates are detected",
    "Every note, highlight and bookmark carries a GUID — a unique identifier assigned when you create it and preserved in every backup thereafter. When the same item appears in two backups, both copies carry the same GUID, so it is recognised as one item and kept once. This is why merging the same pair of files twice does not double anything up, and why you can safely re-merge every week. Where the GUIDs match but the text differs — the same note edited on both devices — the item cannot be resolved automatically, so it is surfaced in the Conflict Reviewer with a word-level diff for you to choose."),
   ("What is not in the backup",
    "A backup carries your personal study data only. Downloaded publications, Bible translations, videos and audio are not included, which is why backup files are small — usually a few megabytes even for a library built over years. After restoring on a new device you may need to download the publications you read regularly again. Nothing you wrote is affected by that; notes are anchored to publications by reference, so they reattach as soon as the publication is present."),
   ("If the merge reports 0 notes added",
    "This is almost always correct rather than a fault. It means every note in the second file already existed in the first — common when you have merged recently, or when one device is simply behind the other. Check the pre-merge preview: it lists what each file contributes before anything is written. If you expected new items and see none, confirm you backed the device up after the study session you are looking for, since a backup only ever contains what existed at the moment it was created."),
  ],
  "faq": [
   ("Can I merge more than two backups?", "Yes — load as many .jwlibrary files as you have devices. They are all combined into a single merged backup."),
   ("Will merging create duplicate notes?", "No. Identical notes, highlights and bookmarks are detected and kept once. Genuinely different versions of the same note are surfaced in the Conflict Reviewer for you to decide."),
   ("Does it work between Android and iPhone?", "Yes. The .jwlibrary format is identical across Android, iOS, iPadOS and Windows, so backups from different platforms merge without any conversion."),
   ("Do I need to merge in a particular order?",
    "No. The merge is order-independent — the same set of files produces the same result whichever one you load first. The only thing order affects is which file is treated as the base for the preview's summary."),
   ("What happens to tags that exist on only one device?",
    "They are carried across intact, along with the links between tags and the notes they mark. If both devices have a tag with the same name, it is treated as one tag and the notes from both are attached to it."),
   ("How large is the merged file?",
    "About the size of the two originals combined, minus the duplicates — typically still only a few megabytes. Backups contain no publication media, so even a heavily annotated library stays small enough to email."),
   ("Can I undo a restore?",
    "Not from inside JW Library, which is why keeping your original backups matters. The merge never modifies the files you load, so your pre-merge backups remain exactly as they were and can be restored if you want to go back."),
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
   "Most people who study on two devices discover the problem the same way: notes written on the tablet are not on the phone, and restoring one device's backup onto the other would wipe whatever that device had. JW Library offers no sync, and its Restore is deliberately all-or-nothing, so keeping devices aligned takes a routine rather than a setting.",
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
   ("Why there is no true sync",
    "JW Library has no account that carries personal study data between devices. Notes, highlights and bookmarks live in a database on each device and stay there. The only official mechanism for moving them is Backup and Restore, and a restore replaces the target device's data outright rather than combining it. So two devices used independently diverge permanently unless something merges them — which is the whole point of the routine below."),
   ("Keeping one master file",
    "The routine works best if you treat one merged file as the current master. Each cycle, back up every device, merge those backups together, and restore the result everywhere. The merged file then becomes the master for the next cycle. Keeping the dated masters in cloud storage gives you both a sync mechanism and a running archive — if you delete something by accident, an earlier master still contains it."),
   ("What happens if you skip a device for a while",
    "Nothing is lost. A device left out of several cycles simply carries older data; when you finally include it, its notes merge in alongside everything else and duplicate items are matched by GUID rather than duplicated. The only situation needing a decision is the same note edited on two devices since they were last merged, and that is surfaced in the Conflict Reviewer with both versions shown side by side."),
   ("How often is often enough",
    "Match it to how much work you would mind redoing. Weekly suits people who study on two devices most days; monthly is plenty if one device is occasional. The important thing is doing it before anything irreversible — a phone upgrade, a reset, a repair — because that is when a divergence becomes a loss."),
   ("Phone, tablet and the Windows app together",
    "The routine does not care how many devices are involved or what they run. Back up each, merge them all in one pass, restore the merged file everywhere. A Windows machine used for preparation and a phone used at meetings combine exactly as two phones would, because every platform writes the same backup format."),
   ("Reducing conflicts before they happen",
    "Conflicts only arise when the same note is edited on two devices between merges. In practice that is rare, and it becomes rarer if you write on one device at a time — reading anywhere, but doing the typing where you usually type. Merging more often also shrinks the window in which a divergence can occur, which is a better fix than trying to remember which device holds the newest version."),
   ("Where the routine pays off",
    "The value of keeping devices merged is not the tidiness — it is that every device becomes a full backup of your study library. Lose or break any one of them and the others still carry everything, which turns the worst case from years of lost notes into an inconvenience. That is a stronger position than any single-device backup habit can give you."),
  ],
  "faq": [
   ("Does JW Sync run in the background?", "No — it's a web page, not an installed service. Nothing scans your devices. You run the routine when you choose; the optional reminder is just a notification."),
   ("Can I sync three or more devices?", "Yes. Back up each one, load all the files, merge once, restore the merged file everywhere."),
   ("What if I edited the same note on two devices?",
    "Both versions are kept until you choose. The Conflict Reviewer shows them side by side with a word-level diff, or you can let it suggest the fuller version."),
   ("Does the order I restore in matter?",
    "No. Once the merged file is created, restoring it on each device puts every device into the same complete state, in whatever order suits you."),
   ("Can I sync three or more devices?",
    "Yes. Back up each one and load them all into the same merge — there is no limit tied to device count."),
   ("Can this be automated?",
    "Not fully, because JW Library has no sync API and the restore step happens in the app. The manual routine takes about two minutes once you are used to it."),
   ("Do I need to merge if I only read on the second device?",
    "If you never annotate on it, you only need to restore onto it periodically so it carries your current notes."),
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
   "Getting a new phone is the single most common moment people lose years of JW Library notes — not because the transfer is difficult, but because it has to be done deliberately before the old device is wiped. Personal study data does not ride along with a normal phone-to-phone transfer, and JW Library keeps no copy of it in any account.",
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
   ("Do this before the old phone is wiped or traded in",
    "The backup has to be created while the old phone still works and still has JW Library installed. Once the device is reset, traded in or handed on, the notes are gone with it — JW Library keeps no cloud copy of personal study data, and a phone-level backup such as Google One or an iCloud device backup usually restores an older snapshot of the app's data, or none at all. Create the .jwlibrary file first, get it somewhere safe, and confirm you can see it before you wipe anything."),
   ("Getting the file off the old phone",
    "On Android the file is written to your chosen folder — typically Downloads or Documents — and you can move it with any file manager, email it to yourself, or drop it into cloud storage. On iPhone the share sheet appears as soon as the backup is created: save it to Files, AirDrop it to the new phone, or send it to yourself. The transfer method does not matter and cannot corrupt the file; a .jwlibrary is a single archive that either arrives intact or does not arrive at all."),
   ("Why a phone-to-phone transfer app is not enough",
    "Tools such as Smart Switch, Move to iOS or an iCloud restore copy apps and system data, but app-private databases are frequently skipped, restored partially, or restored from an older point in time. People regularly discover the gap weeks later, once the old phone is gone. Treat the .jwlibrary file as the authoritative copy and the phone transfer as a convenience — if the transfer happens to bring your notes across, restoring your own backup on top costs nothing."),
   ("Check the transfer actually worked",
    "After restoring on the new phone, open two or three publications you have annotated recently and confirm the notes, highlight colours and bookmarks are all present. A quicker check is to open the backup file itself in your browser before you wipe the old device — you can see every note, highlight and bookmark it contains, so you know what should appear. Only wipe the old phone once the new one is verified."),
   ("Moving to a tablet or computer at the same time",
    "The same file works everywhere. If you are setting up a new phone and a tablet together, restore the identical .jwlibrary file on both and they start out matching. From that point they will drift apart again as you study on each, so it is worth deciding now whether you will keep them merged periodically or treat one as the device that matters."),
   ("If the new phone already has notes on it",
    "This happens when you use the new device for a week before getting round to the transfer. A straight restore would replace that work with the old phone's data. Back the new phone up first, merge that file with the old phone's backup, and restore the merged result — both sets of notes end up in one library instead of one overwriting the other."),
   ("What to do once the new phone is working",
    "Verify before you dispose of anything. Open a few publications you annotated recently on the new phone and confirm the notes, colours and bookmarks are all there, then wipe or trade in the old device — in that order, never the reverse. Once you are settled, put a backup somewhere off the phone, because the situation that brought you to this page will come round again with the next upgrade."),
  ],
  "faq": [
   ("Will this move my downloaded publications too?", "The backup carries your personal study data — notes, highlights, bookmarks, tags and playlists. Publications simply re-download on the new phone."),
   ("Does it matter if the phones run different Android versions?", "No. The .jwlibrary format is the same everywhere, including across Android versions and between Android and iPhone."),
   ("Can I move my notes if the old phone is already gone?",
    "Only if a .jwlibrary backup exists somewhere — in Files, Downloads, an email to yourself or cloud storage. Without one there is nothing to restore from, because personal study data is stored only on the device."),
   ("Do both phones need the same JW Library version?",
    "They do not need to match exactly, but update the new phone to the current version before restoring. A backup made by a newer version can use a newer database schema than an older app understands."),
   ("Will I have to download my publications again?",
    "Usually yes — publication media is not part of the backup. Your notes reattach to each publication as soon as it is downloaded, so nothing you wrote is lost in the meantime."),
   ("How long does the whole thing take?",
    "A few minutes. Creating the backup takes seconds, moving the file depends on your method, and the restore is quick. Re-downloading publications afterwards takes longest and can happen in the background."),
   ("Can I do this without Wi-Fi?",
    "The transfer itself yes, over AirDrop or a cable. Re-downloading publications on the new device needs a connection."),
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
   "Switching between Android and iPhone sounds like the hard case, and it is the easy one. JW Library writes the same backup format on every platform it runs on, so moving a study library from Android to iOS is the same operation as moving it between two Android phones — no conversion, no export format to choose, nothing lost in translation.",
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
   ("Why the format is identical on both platforms",
    "JW Library uses the same backup format everywhere it runs — Android, iOS, iPadOS and Windows. A .jwlibrary file is a ZIP containing a SQLite database with the same tables and the same schema regardless of which device wrote it. There is no conversion step, no export-to-import dance, and nothing platform-specific inside the file. An Android backup restores onto an iPhone exactly as an iPhone backup would."),
   ("The only part that really differs",
    "Not the file — just getting hold of it. On Android the backup is saved to a folder you choose and can be moved with any file manager. On iPhone it goes through the share sheet into Files, AirDrop, or whatever you pick. The friction people hit moving between platforms is always this handling step, never compatibility. Email, cloud storage or AirDrop all work; the archive arrives intact or not at all."),
   ("Highlight colours, tags and study answers",
    "All of it survives. Highlight colours are stored as a numeric index — yellow, green, blue, pink, orange and purple — and render the same on every platform. Tags and the links between tags and notes come across, as do the answers typed into study-question fields. What you see on the iPhone after restoring is what you had on the Android device."),
   ("If iOS will not let you choose the file",
    "Save the file into the Files app first, then pick it from there rather than from a mail attachment or a chat app preview. Some apps hand iOS a temporary preview copy rather than the real file, and JW Library cannot open that. If the file arrived as an attachment, tap it, choose Save to Files, and restore from Files."),
   ("Set the iPhone up before restoring",
    "Install JW Library from the App Store and update it to the current version before you restore anything. A backup written by a newer version of the app can use a database schema an older version does not understand, and the restore will simply be refused. Signing in to anything is not required — personal study data lives in the file you are restoring, not in an account."),
   ("If you have already started studying on the iPhone",
    "Back the iPhone up first. Restoring the Android file straight over the top would replace whatever you have written since switching. Merging the two backups produces one file containing both, which you then restore — the Android history and the new iPhone notes end up in the same library."),
   ("Keeping both phones going afterwards",
    "Some people keep the old Android device as a second reader rather than retiring it. That works, but the two will diverge as soon as you annotate on both, because there is no sync between them. If you intend to use both, plan on merging their backups periodically rather than assuming they stay aligned."),
   ("After the move",
    "Give the iPhone time to re-download the publications you use most, then check a handful of annotated ones to confirm everything arrived — notes, highlight colours, bookmarks and tags. Keep the Android backup file even after the switch is complete: it is a dated snapshot of your library, and it costs nothing to keep."),
  ],
  "faq": [
   ("Do I need a computer to do this?", "No. The whole move can be done phone-to-phone with email or a cloud drive."),
   ("Will my highlight colours survive the move?", "Yes — highlights keep their colours, notes keep their tags, and bookmarks keep their places."),
   ("Do I need a computer for this?",
    "No. AirDrop, email or any cloud storage app moves the file directly between the two phones."),
   ("Does it work the other way — iPhone to Android?",
    "Yes, identically. The same steps work in every direction, including to and from the Windows app."),
   ("Will the iPhone need the same publications downloaded?",
    "Yes, since publication media is not part of a backup. Notes reattach to each publication once it is downloaded."),
   ("Do I need to keep the Android phone afterwards?",
    "No, once you have verified the notes are present on the iPhone. Check a few annotated publications before wiping or trading in the old device."),
   ("Does the transfer work for study-question answers?",
    "Yes. Typed answers are part of personal study data and come across with everything else."),
   ("Is there any risk of losing notes in the move?",
    "Not if you keep the Android backup. The restore writes to the iPhone and never alters the file it reads, so the original stays intact as a fallback. Keep it until you have confirmed the iPhone has everything, and ideally afterwards too — it is a dated snapshot of your library."),
   ("What if the Android phone will not create a backup?",
    "Check available storage first, since the app needs room to write the file. If the app itself is failing, updating it or restarting the device usually resolves it. The data remains intact while you troubleshoot."),
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
   "Everything you have marked in JW Library — every note, every highlight, every bookmark and tag — exists in exactly one place: the device in your hand. There is no account holding a copy and no automatic cloud sync. A backup is the only thing standing between a study library built over years and a lost, reset or upgraded phone.",
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
   ("What the file contains, and what it does not",
    "The backup holds your personal study data: notes, highlights and their colours, bookmarks, tags, and the answers you have typed into study-question fields. It does not hold the publications themselves — no Bibles, magazines, books, videos or audio. That is why a backup of years of study is usually only a few megabytes, and why restoring on a new device leaves you re-downloading publications while every note you wrote is already back in place."),
   ("How many backups to keep",
    "Keep more than one. The failure that costs people their notes is rarely a lost file — it is a good backup overwritten by a bad one, or a restore performed on the wrong device. Because the files are small, there is no reason to delete old ones: keep them dated in a folder in cloud storage. A backup from six months ago is not worthless even after you have newer ones, because anything you deleted by accident since then still exists inside it."),
   ("Where to store them",
    "Anywhere that is not only the device itself. A folder in Drive, iCloud, Dropbox or OneDrive covers the case that matters most — the device being lost, stolen, reset or damaged. Emailing the file to yourself works too and has the useful side effect of date-stamping it. The file contains your own study notes, so treat it with the same care you would any personal document."),
   ("Verifying a backup before you rely on it",
    "A backup you have never opened is an assumption, not a safety net. You can open a .jwlibrary file in your browser and see exactly which notes, highlights and bookmarks it contains — a thirty-second check that turns an assumption into a fact. This matters most immediately before something irreversible: a factory reset, a trade-in, a repair, or a major OS upgrade."),
   ("The moments worth backing up before",
    "Any point where the device changes hands or state: an OS upgrade, a factory reset, a repair or screen replacement, a trade-in, or handing a device on to someone else. Add to that the end of anything you would hate to redo — a convention, an assembly, a stretch of preparation for a talk. Backups are cheap and quick, so the useful habit is tying them to events rather than to a calendar."),
   ("A phone backup is not a JW Library backup",
    "Google One, an iCloud device backup or a manufacturer transfer tool operate at the device level and treat app-private data inconsistently. People routinely find that a full phone restore brought back their apps and settings but not their study notes, or brought back a version from weeks earlier. The .jwlibrary file is the only copy whose contents you control and can verify, so treat the phone-level backup as a bonus rather than the plan."),
   ("Turning it into a habit that survives",
    "The routine that actually holds is the one attached to something you already do: back up when you finish preparing for the week, or on the same day you do any other regular admin. Save to the same folder every time so the files accumulate in one place, and leave the old ones there. A folder of dated backups going back years is the most robust form this can take, and it takes seconds a week to maintain."),
  ],
  "faq": [
   ("How big is a backup file?", "Usually a few megabytes even for very large libraries — email-attachment small."),
   ("Does creating a backup change anything on my phone?", "No. It only writes the file; your library is untouched."),
   ("Does the backup include my downloaded publications?",
    "No. Only personal study data. Publications are re-downloaded on the new device, and your notes reattach to them automatically."),
   ("Can I open a backup to check what is in it?",
    "Yes. You can open a .jwlibrary file in your browser and browse every note, highlight and bookmark it holds, without installing anything and without the file leaving your device."),
   ("Do backups expire?",
    "No. A .jwlibrary file stays restorable indefinitely. Restore into a current version of JW Library rather than an old one, since the app reads older backup formats but not newer ones."),
   ("Should I back up before every meeting?",
    "No need. Tie backups to events that could cost you data — updates, repairs, new devices — plus a regular rhythm that matches how much study you would mind repeating."),
   ("Is it worth keeping backups from years ago?",
    "Yes. They are small, and anything you deleted by accident since then still exists inside them."),
  ],
  "related": ["backup-jw-library-before-phone-repair", "jw-library-restore-replaced-notes", "merge-jw-library-backups", "fix-corrupted-jw-library-backup"],
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
   "A backup that will not restore is not necessarily a backup that has lost your notes. Most files people describe as corrupted are structurally sound and rejected for a fixable reason, or damaged in transfer in a way that a fresh copy resolves. It is worth working through the causes before writing off the file.",
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
   ("What corrupted usually means",
    "In practice it is rarely damaged data. The common causes are a file that was truncated in transfer — cut short by a failed upload or a chat app that compressed it — or an archive that is intact but contains internal inconsistencies the app rejects. Because a .jwlibrary file is a ZIP wrapping a SQLite database, either layer can be the problem, and they need different fixes. A truncated file cannot be repaired and has to be re-obtained; an inconsistent database usually can be."),
   ("What a scan actually checks",
    "A scan verifies that the archive opens, that userData.db is a readable SQLite database that passes an integrity check, that the schema matches what JW Library expects, and that the manifest agrees with the database it describes — including the hash the app uses to confirm the file has not been altered. A mismatch between the manifest and the database is one of the most common reasons a technically fine backup is refused on restore, and it is straightforwardly repairable."),
   ("Orphaned rows are usually harmless",
    "A scan of a real backup will often report rows that reference something no longer present — a highlight pointing at a publication location that has moved, for instance. JW Library's own backups routinely contain hundreds of these and restore without complaint. They are a normal consequence of publications being updated over time, not evidence of damage, and clearing them is not necessary to make a file work."),
   ("Rescuing notes from a file that will not restore",
    "Even when a backup cannot be repaired well enough for JW Library to accept it, the notes inside are often still readable. Opening the file in your browser lets you see and copy the note text directly, which turns an unusable file into recovered study material. If you have a second, older backup that does restore, the readable content from the damaged one can be brought together with it rather than retyped."),
   ("When the restore fails with no clear error",
    "JW Library often refuses a file without explaining why. The most frequent causes are a manifest whose hash no longer matches the database it describes, a file truncated in transfer, or a backup written by a newer version of the app than the one you are restoring into. The first is repairable, the second needs the file fetching again from its original source, and the third is solved by updating the app before restoring."),
   ("Avoiding it next time",
    "Most damage happens in transit. Move backups as files rather than through anything that may recompress them, and prefer cloud storage, AirDrop or a cable to chat apps. After transferring, confirm the file size matches the original — a file noticeably smaller than the one you sent was truncated, and no repair will bring back bytes that never arrived."),
   ("If nothing works",
    "A file that cannot be repaired can still be readable, and reading it is often enough — the note text can be recovered directly even when JW Library refuses the file. Combine that with any older backup that does restore and you usually end up with most of your library intact. Before concluding a file is beyond use, open it and see what is actually inside it."),
  ],
  "faq": [
   ("Is my data uploaded for the scan?", "No. The scan, the fixes and the export all run locally in the browser."),
   ("Can it recover notes deleted inside JW Library?", "No — it repairs file structure. Notes deleted in the app before the backup was made aren't in the file to recover."),
   ("Will repairing the file lose any notes?",
    "Repairs work on a copy and address structural problems rather than content. Your original file is never modified, so it remains available if you want to start again."),
   ("Why did my backup get corrupted?",
    "Most often the file was altered in transit — sent through an app that compressed or truncated it, or an upload that did not finish. Transferring the file again from the original source usually resolves it."),
   ("Can a scan recover notes I deleted inside JW Library?",
    "No. Once deleted in the app and a new backup taken, the note is gone from that file. An older backup made before the deletion will still contain it."),
   ("Can I tell from the file size whether it is truncated?",
    "Often yes. Compare it against the original if you still have it; a significant shortfall means the transfer did not complete."),
   ("Is a backup that opens in the browser guaranteed to restore?",
    "Not guaranteed, but it is a strong sign the archive and database are sound, which rules out the most common failures."),
  ],
  "related": ["clean-up-duplicate-jw-library-notes", "jw-library-notes-missing-after-update", "backup-jw-library", "merge-jw-library-backups"],
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
   ("Pick the notes to share", "On the Share page at jwsync.org/share.html, load your backup and select the notes — a handful from one talk, or everything under a tag in one click with the picker's tag filter. Highlights attached to those notes travel along."),
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
  "related": ["share-jw-library-notes-by-tag", "receive-shared-jw-library-notes", "share-notes-with-bible-student", "share-notes-with-study-group"],
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
   "A .jwlibrary file looks opaque, and it is not. It is an ordinary ZIP archive around an ordinary SQLite database, which means you can read your own backup — see exactly which notes, highlights and bookmarks it holds — without JW Library and without installing anything at all.",
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
   ("What the file actually is",
    "A .jwlibrary file is a ZIP archive with a different extension. Inside it are userData.db — a SQLite database holding your notes, highlights, bookmarks and tags — and manifest.json, a small file describing the backup, including a hash of the database that JW Library uses to confirm the file has not been altered. Nothing about it is proprietary or encrypted; it is a standard archive around a standard database."),
   ("Opening it without JW Library",
    "You do not need the app, or any software, to read your own backup. Opening the file in your browser shows every note, highlight and bookmark it contains, with search and filtering, and the file never leaves your device — it is read locally rather than uploaded. This is the fastest way to confirm a backup contains what you think it does before a reset, a trade-in, or a restore onto a new phone."),
   ("Looking inside manually",
    "If you are curious, copy the file, rename the copy to .zip and open it with any archive tool. You will see userData.db and manifest.json. Opening the database needs a SQLite viewer, and the tables are named for what they hold — Note, UserMark, Bookmark, Tag. Always work on a copy: editing the database by hand without updating the manifest hash produces a file JW Library will refuse to restore."),
   ("Editing safely",
    "Notes can be corrected, retagged, recoloured or deleted outside the app, and the result exported as a new .jwlibrary file you restore normally. The rule that keeps this safe is to keep the original: edit a copy, restore the edited file, and if anything is not as you expected, the untouched original is still there to fall back on."),
   ("Reading a backup on a phone",
    "You do not need a computer. Opening the file in a mobile browser works the same way, which is useful when the backup is already on the phone and you want to confirm its contents before restoring or before wiping the device. The file is read locally, so this works with no connection beyond loading the page itself."),
   ("Why the manifest hash matters",
    "manifest.json records a hash of userData.db. JW Library uses it to confirm the database has not been altered since the backup was written, so a file whose database has been edited without the hash being recalculated is refused on restore. This is the single most common reason a hand-edited backup stops working, and the reason editing through a tool that rewrites the manifest is safer than editing the database directly."),
   ("What this is good for",
    "Being able to read a backup changes what a backup is worth. You can confirm a file contains what you think before wiping a phone, check whether an old file is worth restoring, find a note you know you wrote without hunting through the app, or recover text from a file JW Library will not accept. None of it requires trusting the file to anyone — it is read on your own device."),
  ],
  "faq": [
   ("Can I open a .jwlibrary file in Excel or Notepad?", "Not usefully — it's a database, not a spreadsheet or text file. Open it in JW Sync to read it, or export your notes to Markdown/text from Study Explorer."),
   ("Is it safe to open my backup in the browser?", "Yes. JW Sync reads the file locally in your browser tab; nothing is sent to a server, and your original file is never modified."),
   ("Can I just rename it to .zip?",
    "Yes, on a copy. Renaming does not alter the contents, and it lets any archive tool show you what is inside."),
   ("Will opening the file change it?",
    "No. Reading a backup — in the browser or an archive tool — leaves it byte-for-byte unchanged. Only saving or exporting produces a new file."),
   ("Do I need to be online?",
    "Only to load the page. The file itself is read on your device, not uploaded, so your notes never travel over the network."),
   ("Can I open a backup someone else sent me?",
    "Yes, the format is not tied to a device or account. Whether you should restore it is a separate question, since restoring replaces your own library."),
   ("Do I need to install anything to look inside?",
    "No. A browser is enough to read the notes; only manual inspection of the database itself needs a SQLite viewer."),
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
   "When a phone is lost, stolen or damaged beyond use, whether your JW Library notes survive comes down to one question: does a .jwlibrary backup exist anywhere outside that device? If it does, everything in it comes back. This page covers how to find one, how to restore it onto any replacement device, and what to do when the only backup you have is old.",
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
   ("Where a backup may already exist",
    "Before concluding there is none, check everywhere a file might have been saved: the Downloads and Documents folders of any computer you have connected the phone to, your email sent items, chat apps you may have sent the file through, and every cloud storage account you use. People often created a backup once, months ago, and forgot — and a months-old backup still contains the great majority of a study library."),
   ("Restoring onto a different phone or platform",
    "The replacement device does not need to match the lost one. A backup from an Android phone restores onto an iPhone and vice versa, because the format is identical across Android, iOS, iPadOS and Windows. Install JW Library on the new device, update it to the current version, then restore through Personal Study → Backup and Restore."),
   ("If all you have is an old or partial backup",
    "Restore it anyway. Recovering most of your notes is not a consolation prize — it is the outcome. If you later find a second, different backup, the two can be merged into one file that contains everything from both, so restoring the older one now does not prevent you from adding to it later."),
   ("What cannot be recovered",
    "If no backup exists in any form, personal study data cannot be retrieved. It is stored only in the app's private storage on the device, and neither JW Library nor a phone-level cloud backup reliably preserves it. This is worth knowing plainly, because it is the reason the routine on this site exists at all."),
   ("Check before the device is wiped remotely",
    "If the phone is lost rather than destroyed, and you are considering a remote erase, look for existing backups first — the erase is irreversible and removes the last chance of anyone creating one. If the device is merely misplaced and still reachable, creating a backup remotely is not possible, but the data remains intact as long as the phone is not wiped or reset."),
   ("Making sure this cannot happen twice",
    "The reason a lost phone costs people years of study is that the only copy was on the phone. Once you have restored onto a replacement, put a backup somewhere off the device the same day, and repeat it on a rhythm you will actually keep. The files are small enough that keeping every one of them indefinitely costs nothing."),
   ("If there is genuinely no backup",
    "Then the honest answer is that the notes cannot be retrieved, and it is better to hear that than to keep searching. What you can do is make the loss the last one: install JW Library on the replacement, and before you have rebuilt anything worth losing, create a backup and put it somewhere off the device. From that point the same event costs you nothing."),
  ],
  "faq": [
   ("Can JW Sync recover notes from a phone I no longer have?", "No tool can — recovery depends on a backup file existing somewhere. JW Sync's job is to read, repair and merge the backups you do have."),
   ("My backup is old — is it still worth restoring?", "Absolutely. An old backup with most of your notes beats starting from nothing, and you can merge it with anything newer you find later."),
   ("Does JW Library keep a cloud copy of my notes?",
    "No. Personal study data stays on the device unless you create a backup file yourself."),
   ("Can notes be recovered from a phone with a broken screen?",
    "Sometimes — if the phone still powers on and can be controlled, or a repair shop can drive the display, JW Library can still create a backup. The data is intact as long as the storage is."),
   ("Will an old backup still restore into the current app?",
    "Yes. JW Library reads older backup formats. Update the app first and restore into the current version."),
   ("I found two old backups — which should I use?",
    "Neither alone. Merge them: the result contains everything from both, including anything present in the older file that had been deleted by the time of the newer one."),
   ("Can I check what is in a backup before restoring it?",
    "Yes. Open the file in your browser and browse its notes, highlights and bookmarks first, so you know what you are restoring."),
  ],
  "related": ["jw-library-notes-missing-after-update", "backup-jw-library-before-phone-repair", "merge-jw-library-backups", "fix-corrupted-jw-library-backup"],
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
   "Notes written in JW Library are easy to read inside the app and awkward to use anywhere else — in a document, in a talk outline, on paper, or in the hands of someone who does not use the app. Exporting solves that, and the main decision is not how to export but how much: a filtered export is almost always more useful than everything at once.",
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
   ("Choosing a format",
    "Plain text is the most portable and pastes cleanly into any document or email. Formatted output preserves the structure of longer notes and suits printing or sharing. If you want the notes back inside JW Library later — on another device, or for someone else's library — keep the .jwlibrary file itself rather than a text export, since only that preserves the links between notes, highlights, tags and the exact place in the publication they are anchored to."),
   ("Exporting only part of your library",
    "A full export of years of study is rarely what you want. Narrowing first — to a tag, a publication, a highlight colour, or a date range — produces something you can actually use, such as every note tagged for a talk, or everything written during one convention. The same filters that narrow the view narrow the export, so what you see is what you get."),
   ("What travels with the text, and what does not",
    "An export carries your words. It does not carry the anchors that tie a note to a specific paragraph of a specific publication, because those references only mean something inside JW Library. This is the practical reason to keep backups as well as exports: an export is for reading, printing and sharing outside the app, while a .jwlibrary file is what puts the notes back into a library with their context intact."),
   ("Pulling together everything for one talk or assignment",
    "This is the most common reason to export. Filter to the tag, publication or date range the material sits under, check the result, and export just that. What you get is a single document containing the relevant notes and the passages you highlighted, in the order they appear, rather than an unmanageable dump of your whole library."),
   ("Sharing notes with someone else",
    "There are two different things people mean by sharing. If the other person wants to read your notes, a text export is right — it opens anywhere and needs no special software. If they want the notes inside their own JW Library, anchored to the same paragraphs and carrying their tags and colours, then a .jwlibrary file is what you want instead, because a text export cannot put anything back into the app."),
   ("Keeping an archive you can still read later",
    "Exports are also worth making for their own sake. A plain-text copy of your study notes will still open in thirty years on software nobody has written yet, which is not something any app-specific format can promise. Keeping both — the .jwlibrary for restoring and a text export for reading — costs almost nothing and covers both futures."),
   ("Export or backup — which you need",
    "The two answer different questions. An export is for using your notes outside JW Library: reading, printing, quoting, sending to someone. A .jwlibrary backup is for putting them back into JW Library, on this device or another, with every anchor, tag and colour intact. Neither substitutes for the other, and there is no reason not to keep both."),
  ],
  "faq": [
   ("Does exporting change my JW Library notes?", "No. Export reads a copy of your backup in the browser; your original file and your app are untouched."),
   ("Can I export everything at once?", "Yes — clear the filters to select your whole library, or narrow down first to export just part of it."),
   ("Can I get my notes into Word or Google Docs?",
    "Yes — export as text and paste it in. The text arrives with its structure intact and can be styled from there."),
   ("Do highlights export as well as notes?",
    "Yes, including the highlighted passage and its colour, so a printed copy shows what you marked as well as what you wrote."),
   ("Can I export everything at once?",
    "Yes, though a filtered export is usually more useful. Everything can be exported in one pass when you want a complete copy."),
   ("Can I export the answers I typed into study questions?",
    "Yes. Typed study answers are part of your personal study data and can be exported along with notes and highlights."),
   ("Will an export include which publication each note belongs to?",
    "Yes, the export identifies where each note came from, even though the underlying anchor only functions inside JW Library."),
   ("Does exporting change anything in my library?",
    "No. An export reads your data and writes a separate file; nothing in JW Library is altered, moved or removed by it."),
   ("Can I export from a backup rather than the app?",
    "Yes. A .jwlibrary file can be opened directly and its notes exported, which is useful when the notes you want are in an old backup rather than on your current device."),
  ],
  "related": ["print-jw-library-notes", "share-talk-preparation-notes", "extract-jw-library-notes-by-date", "open-jwlibrary-file"],
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
   ("Consistent tags make sharing a two-click job",
    "The note picker on the Share page has its own tag filter, so a clean tag is also the fastest way to send someone a set of notes: choose the tag, hit Select all, create the file. Sloppy tags cost you twice — once when you look for notes, and again when you try to share them."),
  ],
  "faq": [
   ("Will bulk retagging touch the note text?", "No — it only changes which tags are attached. Your note titles and content stay exactly as written."),
   ("Is there an undo if I make a mistake?", "Yes. Study Explorer has full undo/redo, and your original backup is never modified — the changes go into an exported copy."),
  ],
  "related": ["share-jw-library-notes-by-tag", "edit-jw-library-notes", "manage-jw-library-highlights", "search-jw-library-notes"],
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
  "related": ["weekly-meeting-preparation-jw-library-notes", "edit-jw-library-notes", "export-jw-library-notes", "search-jw-library-notes"],
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
   ("Select just the convention notes", "Pick the event's tag from the tag filter in the note picker and hit Select all — the list is already exactly the notes you tagged. Highlights attached to those notes come along."),
   ("Send the small share file", "JW Sync makes a small file containing only those notes. Send it however you like — messaging app, email, AirDrop. No server, no account."),
   ("Family and friends merge it in", "Each person opens the same page, loads your file with their own backup, and gets a new backup with your notes added. Their own notes are never overwritten, and your imported notes arrive tagged so they're easy to find."),
  ],
  "sections": [
   ("A tag makes this effortless",
    "If you tag your notes during the event (say, “2026 Convention”), selecting them afterward is one filter click and a Select all. It's worth starting a fresh tag at the beginning of any convention, assembly or special meeting for exactly this reason."),
  ],
  "faq": [
   ("Can I share with several people at once?", "Yes — the share file is just a file. Send it to as many people as you like; each merges it into their own library independently."),
   ("Will my whole library be exposed?", "No. Only the notes you select are in the file; the rest of your library stays private."),
  ],
  "related": ["share-jw-library-notes", "receive-shared-jw-library-notes", "share-meeting-notes-with-family", "organize-jw-library-tags"],
 },

 # ── Scenario guides (v2.96.0) ────────────────────────────────────────────
 {
  "slug": "share-jw-library-notes-by-tag",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Share Only the JW Library Notes Under One Tag",
  "h1": "Sharing just the notes carrying one tag",
  "description": "Send one topic, one project or one student's worth of notes instead of your whole library — and your tags travel with them, so they arrive organised on the other side.",
  "intro": [
   "A tag is usually the natural unit of sharing. You tagged everything you gathered on a subject, everything from one event, or everything you go over with one person — and that set, not your whole library, is what the other person actually wants.",
   "JW Sync's note sharing works note by note, so a tag is simply the list you tick. The notes keep their tags on the way out, which means the person receiving them can filter for exactly the same set inside their own library afterwards.",
  ],
  "steps": [
   ("Make sure the notes carry the tag", "Tag them in JW Library as you go, or open your backup in Study Explorer at jwsync.org and use the tag editor to add a tag to notes in bulk. Consistent tagging now is what makes sharing a one-minute job later."),
   ("Open the Share page and load your backup", "Go to jwsync.org/share.html, choose Send notes and load your .jwlibrary file. It's read in your browser and never leaves your device."),
   ("Pick the tag from the filter, then Select all", "The note picker has a tag filter listing every tag in your backup with the number of notes under it. Choose your tag and the list narrows to exactly those notes; Select all ticks the lot. That's the whole selection — two clicks."),
   ("Create the file and send it", "JW Sync builds a small share file containing only the notes you ticked. Send it by chat, email or AirDrop — there is no server involved and no account on either side."),
   ("They add it to their own backup", "The other person opens the same page, chooses Receive, previews the notes, and adds them to their backup. Your tags arrive with the notes, plus a label tag for the import, so the whole set is one filter away for them too."),
  ],
  "sections": [
   ("Why share a tag rather than a backup",
    "Handing over a full .jwlibrary backup gives away everything you have ever written, and restoring it would erase the other person's own notes. Sharing a tagged selection is the opposite on both counts: they see only what you chose, and they lose nothing of their own."),
   ("Narrowing further, or sharing across tags",
    "The tag filter and the search box work together: pick a tag, then type a word to reduce it further, and Select all still ticks only what's in front of you. Searching also matches tag names, so a keyword shared by several tags gathers them in one pass. Each note in the list shows the tags it carries, so you can see what you're sending before you send it."),
   ("Tags to keep for sharing",
    "It is worth keeping a few tags that exist purely to be shared — an event name, a subject you research for others, the person you study with. When the moment comes to send something, there is no hunting: the set is already assembled."),
  ],
  "faq": [
   ("Do my tags go across to the other person?", "Yes. Shared notes carry their tags, and the import is labelled with a tag of its own, so the receiver can find, review or remove the whole batch later."),
   ("What if a note has several tags?", "It appears under each of them in the filter, and all of its tags travel with it. Filtering by one tag never strips the others."),
   ("Does sharing remove the notes from my library?", "No. Sharing copies notes into a small file; your backup and your app are untouched."),
   ("Can I send the same tag to several people?", "Yes — the share file is an ordinary file. Send it to as many people as you like, and each adds it to their own library independently."),
  ],
  "related": ["share-jw-library-notes", "organize-jw-library-tags", "receive-shared-jw-library-notes"],
 },
 {
  "slug": "share-notes-with-bible-student",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Share JW Library Notes with a Bible Student",
  "h1": "Sharing study notes with someone you study the Bible with",
  "description": "Send the notes for a lesson — scriptures, illustrations, the points you prepared — straight into the other person's own JW Library, without touching anything they have written themselves.",
  "intro": [
   "When you prepare a study, most of the work ends up in your own notes: the extra scriptures, the illustration that made a point land, the answer to the question they asked last week. Reading it out is one thing; leaving them with a copy they can reread all week is another.",
   "Note sharing puts your prepared notes into their library as real JW Library notes, attached to the same paragraphs and verses — not as a screenshot or a message they will scroll past.",
  ],
  "steps": [
   ("Prepare the lesson's notes in JW Library", "Write the notes as you normally would, on the paragraphs and scriptures the lesson covers. Give them a tag — the person's name, or the publication — so the set is easy to select later."),
   ("Open the Share page and load your backup", "Create a backup (Personal Study → Backup and Restore → Create a backup), then open jwsync.org/share.html, choose Send notes and load the file. It never leaves your device."),
   ("Tick the notes for this lesson", "Filter the picker by the tag you used and hit Select all, or search and tick them one by one. Create the share file — everything else in your library stays where it is."),
   ("Send it and walk them through receiving", "They need a backup of their own first — Personal Study → Backup and Restore → Create a backup. Then they open jwsync.org/share.html, choose Receive, load your file and their backup, and download the updated backup."),
   ("They restore it in JW Library", "Backup and Restore → Restore, choose the updated file, and your notes appear in their library alongside their own — tagged, so they know which ones came from you."),
  ],
  "sections": [
   ("Their notes are never overwritten",
    "This is the important difference from sending a backup. A restore replaces a device's whole library; receiving shared notes adds to it. Anything they have written themselves — including on the very same paragraphs — stays exactly as it was."),
   ("A weekly rhythm that takes two minutes",
    "Once both of you have done it a first time, the routine is short: prepare, tick, send, restore. Many find it easiest to send the notes right after preparing, so the student has them before the study rather than after."),
  ],
  "faq": [
   ("Does the student need an account or an app installed?", "No account anywhere, and nothing to install beyond JW Library itself — the sharing page is an ordinary web page."),
   ("What if the student has never made a backup?", "They make one first, in JW Library under Personal Study → Backup and Restore. Even an empty-looking library works; the backup is what the shared notes are added to."),
   ("Can I take the notes back later?", "The file is yours to send or not send. Once someone has it, it is theirs, exactly like any message — so share what you would be comfortable sharing in writing."),
  ],
  "related": ["share-jw-library-notes-by-tag", "receive-shared-jw-library-notes", "share-jw-library-notes"],
 },
 {
  "slug": "share-meeting-notes-with-family",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Share Meeting Notes with Your Family or Household",
  "h1": "Sharing this week's meeting notes with the family",
  "description": "Someone was sick, working or away — send them the week's notes as a small file they can add to their own JW Library, without either of you losing anything.",
  "intro": [
   "In most households everyone takes their own notes on their own device, and someone always misses a meeting. Reading your notes out over dinner works once; putting them in the other person's library is what lets them use the material later, in the place they will actually look for it.",
   "Because sharing is note-by-note rather than backup-by-backup, several people can swap notes freely without anyone's library being overwritten.",
  ],
  "steps": [
   ("Back up the device you took notes on", "JW Library → Personal Study → Backup and Restore → Create a backup."),
   ("Select the week's notes", "At jwsync.org/share.html choose Send notes, load your backup, and tick this week's notes — searching by the publication brings them together quickly, and if you tag the week's notes the tag filter gathers them in one click."),
   ("Send it in the family chat", "Create the share file and send it however the household already talks — messaging app, email, AirDrop. It is a small file with only the notes you ticked in it."),
   ("Each person adds it to their own backup", "They open the same page, choose Receive, load your file with a backup of their own, download the updated backup and restore it in JW Library."),
  ],
  "sections": [
   ("Everyone's library stays their own",
    "Nobody's notes are replaced, and nobody has to hand over their whole library to take part. Imported notes arrive under a tag, so each person can see at a glance which notes came from someone else and delete the batch later if they would rather not keep it."),
   ("Family worship: gather instead of scatter",
    "The same tool works in the other direction. If everyone takes notes during family worship, one person can collect the others' share files into a single backup and end up with the household's combined notes on the same material."),
  ],
  "faq": [
   ("Can children's devices take part?", "Any device that can run JW Library and open a web page can. The steps are identical on a phone, tablet or computer."),
   ("Do we need to be on the same platform?", "No. Android, iPhone, iPad and the Windows app all use the same backup format, so notes cross between them without conversion."),
  ],
  "related": ["receive-shared-jw-library-notes", "share-convention-assembly-notes", "sync-jw-library-multiple-devices"],
 },
 {
  "slug": "receive-shared-jw-library-notes",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Someone Sent Me JW Library Notes — How Do I Open Them?",
  "h1": "Adding notes someone shared with you into your own JW Library",
  "description": "You were sent a shared-notes file or a block of shared text. Here's how to preview it and add it to your own JW Library backup without losing a single note of your own.",
  "intro": [
   "Shared JW Library notes arrive as a small file (ending in .jwshare.json) or as a block of text pasted into a message. JW Library itself can't open either one — but you don't need it to. The receiving side of JW Sync reads the shared notes, shows you what's in them, and writes them into a backup of yours.",
   "The whole exchange happens on your device. There's no account, nothing is uploaded, and your own notes are added to, never replaced.",
  ],
  "steps": [
   ("Make a backup of your own library first", "In JW Library: Personal Study → Backup and Restore → Create a backup. This is the file the shared notes will be added to, so it should be current."),
   ("Open the Share page and choose Receive", "Go to jwsync.org/share.html and pick Receive notes."),
   ("Load what you were sent", "Choose the .jwshare.json file, or paste the shared text straight into the box if it came through as a message. Either way you get a read-only preview of every note before anything is written."),
   ("Add them to your backup", "Load your own backup, choose the tag the imported notes should carry, and add them. JW Sync builds an updated backup file for you to download."),
   ("Restore the updated backup in JW Library", "Personal Study → Backup and Restore → Restore, choose the updated file. The shared notes are now in your library, sitting on the right paragraphs and verses."),
  ],
  "sections": [
   ("Nothing of yours is replaced",
    "Shared notes are added as new notes. Even where a shared note lands on a paragraph you have already written on, both survive — yours untouched, theirs alongside it. The one thing to keep in mind is the ordinary rule of restoring: restore the updated backup, not an older one."),
   ("Changed your mind later?",
    "Every imported note carries the tag you chose when you added it. Open your backup in Study Explorer, filter by that tag, and you can review or delete the whole batch in one pass."),
  ],
  "faq": [
   ("The file arrived renamed to .txt or opened as text — is it broken?", "No. Messaging apps often do that. Copy the text and paste it into the Receive box; it works exactly the same."),
   ("Do I need the sender's whole backup?", "No. The share file contains only the notes they chose to send — nothing else from their library."),
   ("Is anything uploaded when I preview the notes?", "No. Reading the shared file, previewing it and writing the updated backup all happen in your browser on your device."),
  ],
  "related": ["share-jw-library-notes", "share-jw-library-notes-by-tag", "backup-jw-library"],
 },
 {
  "slug": "share-notes-with-study-group",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Share Research Notes with a Study Group",
  "h1": "Sharing research with a group — and collecting theirs back",
  "description": "One file, many people: send a set of research notes to everyone studying the same subject, and gather what they send back into a single, combined set of your own.",
  "intro": [
   "When several people are digging into the same subject, the research usually ends up scattered — one person found the cross-references, another the historical background, a third the illustrations. Reading each other's screenshots is not the same as having the material in your own library, on the same verses, searchable next year.",
   "Because a share file is just a file, one export serves the whole group, and the same mechanism carries their work back to you.",
  ],
  "steps": [
   ("Tag your research as you gather it", "Give the subject a tag in JW Library so the set stays together. In Study Explorer you can add a tag to notes in bulk if you didn't tag them at the time."),
   ("Create one share file for the group", "At jwsync.org/share.html choose Send notes, load your backup, pick the subject's tag from the tag filter, hit Select all and create the file."),
   ("Post it once", "Send the same file to everyone — a group chat, an email to several people, whatever the group already uses. There's no per-person setup and no server copy."),
   ("Ask for theirs in return", "Each person can do exactly the same from their side. Add each file you receive to your backup in turn, giving each import its own tag — the sender's name works well — so you can always tell whose research is whose."),
  ],
  "sections": [
   ("One combined set, still attributable",
    "After a few rounds you have the group's whole research on the subject in your own library, on the right paragraphs and verses, with each contribution tagged by source. Search finds all of it at once; the tags let you separate it again whenever you want to."),
   ("Nobody has to expose their library",
    "Everyone shares only the notes they tick. The rest of each person's library — private study, personal reminders, everything else — never enters the file."),
  ],
  "faq": [
   ("Is there a limit on how many notes I can share at once?", "Practically, no. Notes are small; a large set still produces a file you can send in a message."),
   ("What if two people send me the same note?", "You'll see it twice, each under its sender's tag. Study Explorer's search makes near-duplicates easy to spot and delete."),
   ("Can someone receive without sending anything back?", "Yes. Receiving and sending are independent — nobody is obliged to share to be able to add what they were given."),
  ],
  "related": ["share-jw-library-notes-by-tag", "receive-shared-jw-library-notes", "search-jw-library-notes"],
 },
 {
  "slug": "share-talk-preparation-notes",
  "group": "Sharing scenarios",
  "date": "2026-08-02",
  "title": "Hand Off the Research Behind a Talk or Assignment",
  "h1": "Passing on your talk and assignment research",
  "description": "You did the digging for a talk, a part or an assignment. Here's how to hand the research to whoever needs it next — as real notes in their library, or as plain text for a document.",
  "intro": [
   "Preparation is rarely used only once. The scriptures you chased down, the background you read, the way you finally decided to frame a point — someone covering the same material later would rather start from that than from a blank page.",
   "JW Sync gives you two ways to pass it on, and they suit different people: as notes that land in the other person's JW Library, or as plain text they can paste into a document.",
  ],
  "steps": [
   ("Pull the research together under one tag", "As you prepare, tag the notes with the theme or the assignment. If they're already written and untagged, open your backup in Study Explorer and tag them in bulk in a couple of minutes."),
   ("Decide which form suits the other person", "Someone who studies in JW Library wants notes in their library. Someone building a document wants text. You can do both from the same set."),
   ("To send notes: use the Share page", "At jwsync.org/share.html choose Send notes, load your backup, filter by the tag you used and hit Select all, then create the file. They add it to their own backup and restore it — their own notes are untouched."),
   ("To send text: export from Study Explorer", "Filter to the same set and copy or export it as Markdown or plain text. Formatting survives, so a structured outline stays structured when it's pasted into a document."),
  ],
  "sections": [
   ("Keep a copy for yourself, in a form you'll find again",
    "The same export is worth keeping for your own use. A tag plus a date range makes the whole preparation retrievable years later, which is exactly when you'll want it — and Study Explorer's date extraction turns any window of time into its own file."),
  ],
  "faq": [
   ("Will the scriptures stay linked to the right verses?", "Yes — shared notes keep the paragraph and verse they were attached to, so they land in the right place in the other person's library."),
   ("Can I share notes that have highlights on them?", "Yes. Highlights attached to the notes you share travel with them."),
  ],
  "related": ["export-jw-library-notes", "share-jw-library-notes", "extract-jw-library-notes-by-date"],
 },
 {
  "slug": "weekly-meeting-preparation-jw-library-notes",
  "group": "Everyday scenarios",
  "date": "2026-08-02",
  "title": "Prepare for the Meeting Using Notes You Already Wrote",
  "h1": "Weekly preparation with the notes you already have",
  "description": "You've studied this material before. Here's a short weekly routine that surfaces your old notes, highlights and fill-in answers on the same publication before you prepare again.",
  "intro": [
   "Most people prepare each week from a blank page, even though they've written on the same subject — sometimes the same scripture — several times before. That earlier thinking is sitting in your library; the only problem is that nothing brings it back to you at the right moment.",
   "A five-minute routine at the start of preparation fixes that, and it uses nothing but the backup you already have.",
  ],
  "steps": [
   ("Load a current backup in Study Explorer", "Create a backup in JW Library, then open it at jwsync.org. Everything is read in your browser."),
   ("Search the subject before you start", "Search for the theme scripture, the subject or the publication. Whatever you wrote on it in past years comes up together, across every publication it appears in."),
   ("Check your fill-in answers", "The Study Answers view collects the answers you typed into study questions, so previous rounds through the same material are there to build on rather than repeat."),
   ("Add what's missing, then put it back", "Notes can be edited or added right there — title, text, tags, highlight colour. Export the edited backup and restore it in JW Library, and your preparation is in the app for the meeting."),
  ],
  "sections": [
   ("Why the old notes matter",
    "Reviewing what you concluded last time turns preparation into something cumulative. You stop rediscovering the same points and start building on them — and the notes you add this week become next round's starting point."),
   ("A gentler version: let the notes come to you",
    "If a weekly search feels like work, Resurface on the Study Stats page brings a few old notes back on its own each day, including ones you wrote on this date in past years. Same benefit, no routine to remember."),
  ],
  "faq": [
   ("Does editing in the browser change my library directly?", "No. You export an updated backup and restore it in JW Library — the app is only ever changed by a restore you perform yourself."),
   ("Is my backup uploaded when I search it?", "No. The file is read locally in your browser; nothing is sent anywhere."),
  ],
  "related": ["jw-library-study-answers", "search-jw-library-notes", "review-old-jw-library-notes"],
 },
 {
  "slug": "print-jw-library-notes",
  "group": "Everyday scenarios",
  "date": "2026-08-02",
  "title": "How to Print Your JW Library Notes",
  "h1": "Getting your JW Library notes onto paper",
  "description": "JW Library has no print button. Export your notes as text or Markdown, paste them into any document, and print — a study journal, a set of notes for someone without the app, or an archive.",
  "intro": [
   "There's no way to print from JW Library, and screenshots of a phone screen make poor reading. But the notes are yours, and getting them into a printable document is straightforward once you can read the backup file.",
   "Study Explorer reads a .jwlibrary backup in your browser and lets you copy or export any selection of notes as plain text or Markdown — which every word processor, notes app and printer already understands.",
  ],
  "steps": [
   ("Create a backup and open it", "JW Library → Personal Study → Backup and Restore → Create a backup, then load the file at jwsync.org."),
   ("Narrow down to what you want on paper", "Filter by publication, tag, highlight colour or date range, or search for a subject. Printing everything is possible, but a filtered set usually makes a far more useful document."),
   ("Copy or export as text or Markdown", "Take the selection out as Markdown or plain text. Bold, italics and lists survive, so structured notes stay structured on the page."),
   ("Paste into a document and print", "Any word processor or notes app will do. Set the headings and margins you want, then print or save as PDF."),
  ],
  "sections": [
   ("Making a study journal",
    "A date range is the natural unit for a printed journal — a year of notes, or the period covering one publication. Extracting by date gives you a clean chronological set to print or bind, which is a satisfying thing to have off-screen."),
   ("Printing for someone who doesn't use the app",
    "Not everyone studies from a device. A printed set of notes on the current material is genuinely useful for someone who prefers paper, and it takes the same two minutes as any other export."),
  ],
  "faq": [
   ("Can I print my highlights too?", "The highlights view lists the passages you've marked, and that list copies out as text alongside your notes."),
   ("Does exporting change anything in JW Library?", "No. Exporting reads a copy of your backup; your original file and the app are untouched."),
  ],
  "related": ["export-jw-library-notes", "extract-jw-library-notes-by-date", "search-jw-library-notes"],
 },
 {
  "slug": "clean-up-duplicate-jw-library-notes",
  "group": "Everyday scenarios",
  "date": "2026-08-02",
  "title": "Clean Up Duplicate and Empty JW Library Notes",
  "h1": "Clearing out duplicate notes, empty notes and clutter",
  "description": "Restored a backup twice, or imported the same notes again? Library Doctor scans your .jwlibrary file in the browser, finds duplicates and empty notes, and produces a clean copy.",
  "intro": [
   "Libraries collect clutter. Restoring a backup onto a device that already had some of the same notes, importing a shared set twice, or years of half-written notes that never got finished — each leaves something behind, and JW Library gives you no way to sweep it up in bulk.",
   "Library Doctor is a free health check for a .jwlibrary file. It scans the backup in your browser, tells you in plain language what it found, and fixes what's fixable in one tap.",
  ],
  "steps": [
   ("Back up first — as always", "JW Library → Personal Study → Backup and Restore → Create a backup. Keep this file; it's your fallback."),
   ("Run the health check", "Open jwsync.org, load the backup and start Library Doctor. It examines the file's contents and structure without sending it anywhere."),
   ("Read what it found", "Duplicates, empty notes and other clutter are listed plainly, with counts, so you can see the scale of the problem before you change anything."),
   ("Fix and download the clean copy", "One tap applies the repairs and produces a new, cleaned .jwlibrary file. Your original is never modified."),
   ("Restore the clean file", "Backup and Restore → Restore, and pick the cleaned file. Your library is the same, minus the clutter."),
  ],
  "sections": [
   ("How duplicates happen in the first place",
    "Almost always through a restore. If you restore a backup onto a device that already carried some of the same material — or restore the same file twice through different routes — the app has no way to know it has seen those notes before."),
   ("Merging is the way to avoid them",
    "This is exactly why merging two backups is safer than restoring one over another: the merge detects material that already exists and keeps it once. The same checks run inside every merge, so a merged backup comes out clean even if the files going in weren't."),
  ],
  "faq": [
   ("Will it delete notes I actually want?", "It removes exact duplicates and empty notes — material with nothing in it to lose. And because it writes a new file instead of editing yours, the original is always there to fall back on."),
   ("Can it recover notes I deleted in the app?", "No. If a note was deleted in JW Library before the backup was made, it isn't in the file to recover — an older backup is the place to look."),
  ],
  "related": ["fix-corrupted-jw-library-backup", "merge-jw-library-backups", "organize-jw-library-tags"],
 },
 {
  "slug": "backup-jw-library-before-phone-repair",
  "group": "Everyday scenarios",
  "date": "2026-08-02",
  "title": "Back Up JW Library Before a Factory Reset or Repair",
  "h1": "Before a factory reset, a repair or selling the phone",
  "description": "A reset wipes JW Library's notes with everything else, and phone-transfer tools don't carry them. Make a backup, verify it actually opens, then reset with nothing at risk.",
  "intro": [
   "Reset the phone, send it in for repair, or hand it on to someone else, and JW Library's personal study data goes with it. Photos and apps come back from a cloud backup; years of notes, highlights and bookmarks generally do not, because phone-transfer tools skip the app's private data.",
   "The fix takes five minutes, and the step people miss is the one that matters most: checking that the backup file is genuinely readable before the device is wiped.",
  ],
  "steps": [
   ("Create the backup", "JW Library → Personal Study → Backup and Restore → Create a backup. You get a .jwlibrary file — usually only a few megabytes."),
   ("Get it off the device", "Email it to yourself, or put it in Drive, iCloud or a computer folder. A backup that only exists on the phone you're about to wipe isn't a backup."),
   ("Verify it opens before you wipe anything", "Load the file at jwsync.org and look at it — the notes, highlights and bookmarks should all be there, and the health check will flag anything wrong with the file. This is the whole point of the exercise: finding out the file is unreadable afterwards is too late."),
   ("Reset, then restore", "After the reset or repair, install JW Library, sign in, then Backup and Restore → Restore and choose your file."),
   ("Used a loaner phone in between? Merge, don't overwrite", "If you took notes on a temporary device, back that one up too and merge both files at jwsync.org before restoring — otherwise restoring the old backup erases whatever you wrote while you waited."),
  ],
  "sections": [
   ("Why verification is worth the extra minute",
    "Interrupted transfers, cloud drives that mangle files and extensions renamed in transit all produce backups that look fine in a folder and fail at restore. Opening the file first turns a silent problem into one you can still fix, while the original device still has the data."),
   ("Keep the file after the restore",
    "Don't delete it once the new device is working. Old backups are the only way back from a note deleted by accident months later, and they cost nothing to keep."),
  ],
  "faq": [
   ("Will my downloaded publications come back?", "The backup carries your personal study data — notes, highlights, bookmarks, tags and playlists. Publications simply re-download afterwards."),
   ("Does the file work if I switch to a different phone brand or platform?", "Yes. The .jwlibrary format is the same on Android, iPhone, iPad and Windows."),
  ],
  "related": ["backup-jw-library", "recover-jw-library-notes-lost-phone", "transfer-jw-library-notes-new-phone"],
 },
 {
  "slug": "jw-library-notes-missing-after-update",
  "group": "Fixing problems",
  "date": "2026-08-02",
  "title": "JW Library Notes Missing After an Update or Reinstall",
  "h1": "Notes gone after an app update, reinstall or restore",
  "description": "Your notes vanished after updating, reinstalling or signing in again. What to do first, what not to do, and how to get them back without losing anything you've written since.",
  "intro": [
   "Opening JW Library after an update to find your notes gone is alarming, and in the great majority of cases they are recoverable. What matters is what you do in the next few minutes — specifically, not doing the one thing that turns a recoverable situation into a permanent loss.",
   "It's an unpleasant moment: JW Library opens, and the notes aren't there. Before anything else, one piece of advice — don't rush. Most of what makes this situation unrecoverable is done in the first ten minutes, by overwriting the very backup that still contains the missing notes.",
   "Work through the steps below in order. The goal is to end up with one file containing both the old notes and anything you've written since.",
  ],
  "steps": [
   ("Don't overwrite your backups yet", "Resist creating a fresh backup on top of an old one, and don't restore anything blindly. An older backup file is the most likely place your notes still exist."),
   ("Hunt for the newest backup you have", "Check email attachments, Google Drive, iCloud Drive, your computer's downloads folder and any other device you have restored to. Backups are small, so people often have more copies than they remember."),
   ("Look inside the file before restoring it", "Load the candidate at jwsync.org and see what's actually in it — how many notes, from which publications, up to what date. That tells you whether it's the right file to use, before you commit to a restore."),
   ("Back up the current device too", "Even if it looks empty, back it up. If you've written anything since the notes disappeared, this file is the only copy of it."),
   ("Merge the two, then restore", "Merge the old backup with the current one at jwsync.org. The result contains the recovered notes and everything written since, with duplicates kept once. Restore that merged file — never the old backup on its own."),
  ],
  "sections": [
   ("Why restoring the old backup on its own is the wrong move",
    "A restore replaces the device's library outright. If you restore an old backup directly, you get the missing notes back and lose everything written after that backup was made. Merging first is what makes the recovery lossless."),
   ("If the backup itself won't restore",
    "A file that errors out during restore isn't necessarily lost. Run the health check on it — damage from interrupted downloads, cloud sync or a renamed extension is often repairable, and a cleaned copy will restore normally."),
   ("First: do not create a new backup yet",
    "If notes have vanished, resist the reflex to back up immediately. A backup captures the current state, and if the current state is the empty one you risk overwriting the good file you already had. Find out what backups exist first — in Downloads, Files, email, or cloud storage — and only then decide what to do. Nothing on the device is improved by a fresh backup taken in a panic."),
   ("Why an update can appear to lose notes",
    "The usual cause is not deletion. An update can leave the app pointing at a fresh, empty database while the old one is still on disk; a reinstall — including one performed automatically by a store update that failed midway — starts the app from scratch; and on shared or multi-profile devices the app can end up running under a different profile than before. In each case the notes are not gone so much as not currently loaded, which is also why a restore from backup usually brings everything back cleanly."),
   ("Recovering an old backup without discarding new work",
    "If you have studied since the backup was made, a plain restore trades one loss for another: it brings the old notes back and removes anything newer. The way around it is to back up the current state to a separate file, merge that with the older backup so both sets of notes exist in one file, and restore the merged result. You end up with the recovered notes and the recent ones together rather than choosing between them."),
   ("If the app reinstalled itself",
    "A reinstall clears app-private storage, so anything not in a backup is unrecoverable — there is no cloud copy to fall back on. Check every place a .jwlibrary file might have been saved before concluding there is none, including your email sent folder and any cloud storage you have ever saved to. Once you find one, restore it, and thereafter keep backups outside the device."),
   ("Once everything is back",
    "When your notes are restored, take one more backup and store it off the device — the episode you have just been through is the argument for it. If you had to merge an old backup with the current state to get here, keep both source files as well: they are dated snapshots, and having more of them is what made the recovery possible in the first place."),
  ],
  "faq": [
   ("Are the notes still on the device somewhere?", "Not in a form you can get at from outside the app. Recovery realistically means an earlier backup file — which is why keeping old ones matters so much."),
   ("Does signing in again bring notes back?", "No. Personal study data isn't held in an account; it lives on the device and travels only through backup files."),
   ("What if the only backup I have is months old?", "Merge it with a backup of the device as it is now. You'll recover everything the old file has, and keep everything the device still has, without choosing between them."),
   ("Are my notes really gone?",
    "Not necessarily. If a backup exists anywhere, everything in it is fully recoverable. What is unrecoverable is only work done after the most recent backup was taken."),
   ("Can I combine an old backup with what is on the device now?",
    "Yes — back up the current state first, then merge that file with the older one and restore the result. Both sets of notes end up in the same library."),
   ("Will restoring an old backup delete my recent notes?",
    "On its own, yes, because a restore replaces the device's data. Merge the current backup with the old one first and restore the merged file instead."),
   ("Should I reinstall the app to fix it?",
    "No — reinstalling clears app-private storage and removes any chance of recovering what is still on the device. Look for an existing backup first, and treat reinstalling as a last resort after you have one."),
  ],
  "related": ["jw-library-restore-replaced-notes", "recover-jw-library-notes-lost-phone", "fix-corrupted-jw-library-backup"],
 },
 {
  "slug": "help-family-member-move-jw-library-notes",
  "group": "Everyday scenarios",
  "date": "2026-08-02",
  "title": "Help a Family Member Move Their JW Library Notes",
  "h1": "Helping someone else move or rescue their JW Library notes",
  "description": "You're the one who gets asked to fix the phone. Here's the shortest reliable path to move a relative's JW Library notes to a new device — including how to do it without reading their notes.",
  "intro": [
   "Sooner or later someone hands you their phone and a new one beside it. JW Library's notes are the part that won't move on its own, and they're often the part that matters most — years of study that no transfer tool will carry across.",
   "The process is the same as doing it for yourself, with one extra consideration worth thinking about first: whose device the work happens on.",
  ],
  "steps": [
   ("Talk them through making a backup on the old device", "JW Library → Personal Study → the three-dot menu → Backup and Restore → Create a backup. It saves a .jwlibrary file. If you're not with them, this part they can do over the phone."),
   ("Get the file where you need it", "Have them email it to themselves, or share it to you. It's small enough to send through any messaging app."),
   ("Check the file opens", "Load it at jwsync.org and confirm the notes are there. Doing this before the old device is wiped or handed on is what turns a bad surprise into a non-event."),
   ("Merge if the new device already has notes", "If they've been using the new phone for a while, back that one up too and merge both files — otherwise restoring the old backup deletes everything they've written on the new device."),
   ("Walk them through the restore", "On the new device: Backup and Restore → Restore, choose the file. Notes, highlights, bookmarks and tags all appear."),
  ],
  "sections": [
   ("Doing it without reading their notes",
    "Personal study notes are personal. If you'd rather not see them — or they'd rather you didn't — do the whole thing on their device: it's a web page, so you can open jwsync.org on their phone or tablet, load their files there and never have the backup on your own machine. Nothing is uploaded either way, but this way the file never leaves their hands."),
   ("Leave them with a backup they can find",
    "Before you give the phone back, make sure the backup file is somewhere they'll be able to find again — their own email or cloud drive, not just your downloads folder. Next time, they may not need you at all."),
  ],
  "faq": [
   ("Can I do this remotely?", "Yes. If they can create a backup and send you the file, everything else works at a distance — and the restore is a few taps you can talk them through."),
   ("They have an Android and the new one is an iPhone. Does that matter?", "No. The backup format is identical across Android, iPhone, iPad and Windows."),
   ("What if they never made a backup and the old phone is gone?", "Then there's nothing to recover from — the data lived on that device. It's worth setting up a habit of regular backups on the new phone straight away."),
  ],
  "related": ["transfer-jw-library-notes-new-phone", "backup-jw-library-before-phone-repair", "jw-library-android-to-iphone"],
 },
]

GROUPS = ["Getting started", "Sharing scenarios", "Everyday scenarios",
          "Fixing problems", "Power tools"]

# ── Template ──────────────────────────────────────────────────────────────
CSS = """
:root{--bg:#040f22;--card:rgba(15,28,52,.6);--line:rgba(71,85,105,.35);--txt:#e2e8f0;
--muted:#94a3b8;--accent:#ea580c;--accent-strong:#c2410c;--accent-soft:#fb923c}
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
border-radius:50%;background:var(--accent-strong);color:#fff;font-weight:700;font-size:15px;
display:flex;align-items:center;justify-content:center}
ol.steps h3{margin:0 0 4px;font-size:16.5px}
ol.steps p{margin:0;color:var(--muted);font-size:15px}
.cta{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;
padding:20px 22px;margin:34px 0}
.cta strong{display:block;font-size:17px;margin-bottom:4px}
.cta span{color:var(--muted);font-size:14.5px}
.cta .btn{display:inline-block;margin-top:14px;background:var(--accent-strong);color:#fff;font-weight:600;
font-size:15px;padding:10px 22px;border-radius:9px;box-shadow:0 1px 5px rgba(0,0,0,.35)}
.cta .btn:hover{text-decoration:none;filter:brightness(1.07)}
.faq dt{font-weight:600;margin:18px 0 4px}
.faq dd{margin:0;color:var(--muted);font-size:15px}
.related{margin:8px 0 0;padding:0;list-style:none}
.related li{margin:0 0 8px}
footer.site{border-top:1px solid var(--line);margin-top:56px;padding:26px 0 40px;
color:#8b99ad;font-size:12.5px}
footer.site p{margin:0 0 10px}
.gcards{display:grid;grid-template-columns:1fr;gap:12px;margin:14px 0 0;padding:0;list-style:none}
@media(min-width:640px){.gcards{grid-template-columns:1fr 1fr}}
.gcards a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px 18px;color:var(--txt);height:100%}
.gcards a:hover{text-decoration:none;border-color:var(--accent)}
.gcards strong{display:block;font-size:15.5px;margin-bottom:4px}
.gcards span{color:var(--muted);font-size:13.5px;line-height:1.55;display:block}
.glang{background:transparent;border:1px solid var(--line);color:var(--muted);
font-size:13px;padding:4px 8px;border-radius:8px;margin-left:14px;font-family:inherit;
max-width:150px}
.glang:hover{border-color:var(--accent)}
.glangs{border-top:1px solid var(--line);margin-top:30px;padding-top:18px}
.glangs b{display:block;font-size:13px;color:var(--muted);font-weight:600;margin-bottom:8px}
.glangs a{display:inline-block;color:#8b99ad;font-size:12.5px;margin:0 14px 6px 0}
.glangs a:hover{color:var(--accent)}
.glangs a[aria-current]{color:var(--txt);font-weight:600}
""".strip()

# The guides are self-contained static pages with no external stylesheet, so
# they carry their own small RTL block rather than linking the site's rtl.css.
RTL_CSS = """<style>
body{direction:rtl}
.hnav a{margin-left:0;margin-right:18px}
ol.steps li{padding:0 52px 20px 0}
ol.steps li::before{left:auto;right:0}
.glang{margin-left:0;margin-right:14px}
code,.lede code{unicode-bidi:isolate}
</style>"""

def footer(root, lang, slug=None):
    t = CHROME[lang]
    # The app and the two satellite pages all read ?lang=, so a localized guide
    # must carry its language across. Linking them bare sent a Spanish reader to
    # an English page and pointed every localized guide's outbound links at the
    # English URLs. (Internal links only — ?lang= must never appear in hreflang
    # or the sitemap; see the canonical-hygiene block in tests/01_static.js.)
    q = "" if lang == "en" else "?lang=" + lang
    return (
        '<footer class="site"><div class="wrap">'
        '%s'
        '<p><a href="%s">JW Sync</a> · <a href="%s">%s</a> · '
        '<a href="%sforum.html%s">%s</a> · <a href="%shighlights.html%s">%s</a></p>'
        '<p>%s</p><p>%s</p>'
        '</div></footer>'
    ) % (lang_links(slug, lang),
         root + q, guides_index_href(root, lang), esc(t["footer_all_guides"]),
         root, q, esc(t["footer_community"]), root, q, esc(t["footer_stats"]),
         esc(t["footer_privacy"]), esc(t["footer_disclaimer"]))

def esc(s):
    return html.escape(s, quote=True)

def guides_index_href(root, lang):
    """Relative href of *this language's* guide index.

    A localized page linking `root + "guides/"` would send the reader back
    to the English tree — the nav and footer must stay inside the language.
    """
    return root + "guides/" + ("" if lang == "en" else lang + "/")


def guide_url(slug, lang):
    """Canonical URL of a guide (or of the index when slug is None)."""
    base = SITE + "/guides/" + ("" if lang == "en" else lang + "/")
    return base + (slug if slug else "")


def alternates(slug):
    """hreflang cluster for one guide across every translated language."""
    out = ['<link rel="alternate" hreflang="x-default" href="%s">' % guide_url(slug, "en")]
    for l in TRANSLATED:
        out.append('<link rel="alternate" hreflang="%s" href="%s">' % (l, guide_url(slug, l)))
    return "\n".join(out)


def lang_links(slug, lang):
    """The same set as lang_picker, as links a crawler can actually follow.

    lang_picker is a <select onchange>: fine for readers, invisible to Google,
    which does not treat <option value> as a link. Without this the thirteen
    translations of a guide were asserted by hreflang and reachable by zero
    internal links, so nothing pointed at a translation but the <head>.
    """
    out = []
    for l in TRANSLATED:
        cur = ' aria-current="page"' if l == lang else ""
        out.append('<a href="%s" hreflang="%s" lang="%s"%s>%s</a>'
                   % (guide_url(slug, l), l, l, cur, CHROME[l]["lang_name"]))
    return ('<nav class="glangs"><b>%s</b>%s</nav>'
            % (esc(CHROME[lang]["lang_other"]), "".join(out)))


def lang_picker(slug, lang, root):
    """A plain <select> that navigates — no JS bundle on these static pages."""
    opts = []
    for l in TRANSLATED:
        sel = " selected" if l == lang else ""
        opts.append('<option value="%s"%s>%s</option>'
                    % (guide_url(slug, l), sel, CHROME[l]["lang_name"]))
    return ('<select class="glang" aria-label="%s" '
            'onchange="location.href=this.value">%s</select>'
            % (esc(CHROME[lang]["lang_label"]), "".join(opts)))


def head(title, description, canonical, jsonld, lang="en", slug=None):
    d = ' dir="rtl"' if lang in RTL_LANGS else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}"{d}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
{alternates(slug)}
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
<meta property="og:locale" content="{CHROME[lang]["og_locale"]}">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<style>{CSS}</style>
{RTL_CSS if lang in RTL_LANGS else ""}
</head>
<body>"""

def site_header(root, lang, slug):
    t = CHROME[lang]
    app = root + ("" if lang == "en" else "?lang=" + lang)
    return (f'<header class="site"><div class="wrap">'
            f'<a class="brand" href="{app}"><span class="dot">JW</span>JW Sync</a>'
            f'<nav class="hnav"><a href="{guides_index_href(root, lang)}">'
            f'{esc(t["nav_guides"])}</a>'
            f'<a href="{root}forum.html">{esc(t["nav_community"])}</a>'
            f'<a href="{app}">{esc(t["nav_open_app"])}</a>'
            f'{lang_picker(slug, lang, root)}</nav>'
            f'</div></header>')

def localize(g, lang):
    """Merge the language's copy over the English guide record.

    Untranslated fields fall back to English, so a partially translated
    language still produces a valid page rather than a KeyError.
    """
    if lang == "en":
        return g
    tr = GUIDE_TEXT.get(lang, {}).get(g["slug"], {})
    out = dict(g)
    out.update(tr)
    return out


def guide_jsonld(g, canonical, lang="en"):
    published = g.get("date", TODAY)
    graph = [
        {
            "@type": "Article",
            "headline": g["title"],
            "description": g["description"],
            "inLanguage": lang,
            "datePublished": published,
            "dateModified": published,
            "mainEntityOfPage": canonical,
            "image": f"{SITE}/og-image.png",
            "author": {"@type": "Organization", "name": "JW Sync", "url": SITE},
            "publisher": {"@type": "Organization", "name": "JW Sync", "url": SITE},
        },
        {
            "@type": "HowTo",
            "name": g["title"],
            "description": g["description"],
            "inLanguage": lang,
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
                {"@type": "ListItem", "position": 2,
                 "name": CHROME[lang]["crumb_guides"], "item": guide_url(None, lang)},
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

def build_guide(g_en, lang="en"):
    g = localize(g_en, lang)
    t = CHROME[lang]
    slug = g_en["slug"]
    canonical = guide_url(slug, lang)
    # /guides/<slug> is one level below the root; /guides/<lang>/<slug> is two.
    root = "../" if lang == "en" else "../../"
    parts = [head(g["title"] + " | " + t["site_guides"], g["description"], canonical,
                  guide_jsonld(g, canonical, lang), lang, slug)]
    parts.append(site_header(root, lang, slug))
    parts.append('<main class="wrap">')
    parts.append(f'<nav class="crumbs"><a href="{root}">JW Sync</a> › '
                 f'<a href="./">{esc(t["crumb_guides"])}</a> › '
                 f'{esc(t["groups"][g_en["group"]])}</nav>')
    parts.append(f"<h1>{esc(g['h1'])}</h1>")
    parts.append(f'<p class="lede">{esc(g["description"])}</p>')
    for p in g["intro"]:
        parts.append(f"<p>{esc(p)}</p>")
    parts.append(f'<h2>{esc(t["h_steps"])}</h2><ol class="steps">')
    for name, text in g["steps"]:
        parts.append(f"<li><h3>{esc(name)}</h3><p>{esc(text)}</p></li>")
    parts.append("</ol>")
    app = root + ("" if lang == "en" else "?lang=" + lang)
    parts.append(f'<div class="cta"><strong>{esc(t["cta_title"])}</strong>'
                 f'<span>{esc(t["cta_body"])}</span>'
                 f'<a class="btn" href="{app}">{esc(t["cta_btn"])}</a></div>')
    for h2, body in g["sections"]:
        parts.append(f"<h2>{esc(h2)}</h2><p>{esc(body)}</p>")
    if g.get("faq"):
        parts.append(f'<h2>{esc(t["h_faq"])}</h2><dl class="faq">')
        for q, a in g["faq"]:
            parts.append(f"<dt>{esc(q)}</dt><dd>{esc(a)}</dd>")
        parts.append("</dl>")
    parts.append(f'<h2>{esc(t["h_related"])}</h2><ul class="related">')
    by_slug = {x["slug"]: x for x in GUIDES}
    for rel in g_en["related"]:
        r = localize(by_slug[rel], lang)
        parts.append(f'<li><a href="{rel}">{esc(r["title"])}</a></li>')
    parts.append("</ul></main>")
    parts.append(footer(root, lang, g_en["slug"]))
    parts.append("</body>\n</html>\n")
    return "".join(parts)

def build_index(lang="en"):
    t = CHROME[lang]
    canonical = guide_url(None, lang)
    root = "../" if lang == "en" else "../../"
    title = t["index_title"]
    description = t["index_desc"]
    jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": title,
                "description": description,
                "url": canonical,
                "inLanguage": lang,
                "isPartOf": {"@type": "WebSite", "name": "JW Sync", "url": SITE},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "JW Sync", "item": SITE + "/"},
                    {"@type": "ListItem", "position": 2,
                     "name": t["crumb_guides"], "item": canonical},
                ],
            },
        ],
    }
    parts = [head(title, description, canonical, jsonld, lang, None)]
    parts.append(site_header(root, lang, None))
    parts.append('<main class="wrap">')
    parts.append(f'<nav class="crumbs"><a href="{root}">JW Sync</a> › '
                 f'{esc(t["crumb_guides"])}</nav>')
    parts.append(f'<h1>{esc(t["index_h1"])}</h1>')
    parts.append(f'<p class="lede">{esc(t["index_lede"])}</p>')
    for group in GROUPS:
        parts.append(f'<h2>{esc(t["groups"][group])}</h2><ul class="gcards">')
        for g_en in GUIDES:
            if g_en["group"] != group:
                continue
            g = localize(g_en, lang)
            parts.append(f'<li><a href="{g_en["slug"]}"><strong>{esc(g["title"])}</strong>'
                         f'<span>{esc(g["description"])}</span></a></li>')
        parts.append("</ul>")
    app = root + ("" if lang == "en" else "?lang=" + lang)
    parts.append(f'<div class="cta"><strong>{esc(t["index_cta_title"])}</strong>'
                 f'<span>{esc(t["index_cta_body"])}</span>'
                 f'<a class="btn" href="{app}">{esc(t["cta_btn"])}</a></div>')
    parts.append("</main>")
    parts.append(footer(root, lang))
    parts.append("</body>\n</html>\n")
    return "".join(parts)


def main():
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    written = 0
    for lang in TRANSLATED:
        outdir = os.path.join(repo, "guides") if lang == "en" \
            else os.path.join(repo, "guides", lang)
        os.makedirs(outdir, exist_ok=True)
        for g in GUIDES:
            html_out = build_guide(g, lang)
            # sanity: the JSON-LD block must still parse after templating
            json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                                 html_out, re.S).group(1))
            with open(os.path.join(outdir, g["slug"] + ".html"), "w", encoding="utf-8") as f:
                f.write(html_out)
            written += 1
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_index(lang))
        written += 1
        print("wrote guides/%s%d pages"
              % ("" if lang == "en" else lang + "/", len(GUIDES) + 1))
    print("%d guides x %d languages (+index) = %d pages"
          % (len(GUIDES), len(TRANSLATED), written))


if __name__ == "__main__":
    main()

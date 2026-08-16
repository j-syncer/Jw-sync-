#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deepen the ten highest-intent English guides.

They ran 270–460 words of body copy (median across all 37 was 530 rendered
words, 31 of 37 under 600). That is thin for the queries they target — "how to
transfer JW Library notes to a new phone" is answered by pages several times
longer, and Google's helpful-content systems reward first-hand specifics.

Every addition here is material the site can write and a generic listicle
cannot: what is actually inside a .jwlibrary file, why Restore replaces instead
of merging, how duplicate detection keys off the note GUID, which failure modes
look like data loss and are not.

Only the English records change. localize() replaces whole fields, so each
translation keeps its own (shorter) copy — no English leaks into a localized
page. Translations are brought up to the same depth in per-language passes.

Run from the repo root:  python3 scripts/deepen_guides_en.py
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "scripts", "build_guides.py")

# slug -> {"sections": [(title, body), ...], "faq": [(q, a), ...]}
ADD = {
 "merge-jw-library-backups": {
  "sections": [
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
   ("Do I need to merge in a particular order?",
    "No. The merge is order-independent — the same set of files produces the same result whichever one you load first. The only thing order affects is which file is treated as the base for the preview's summary."),
   ("What happens to tags that exist on only one device?",
    "They are carried across intact, along with the links between tags and the notes they mark. If both devices have a tag with the same name, it is treated as one tag and the notes from both are attached to it."),
   ("How large is the merged file?",
    "About the size of the two originals combined, minus the duplicates — typically still only a few megabytes. Backups contain no publication media, so even a heavily annotated library stays small enough to email."),
   ("Can I undo a restore?",
    "Not from inside JW Library, which is why keeping your original backups matters. The merge never modifies the files you load, so your pre-merge backups remain exactly as they were and can be restored if you want to go back."),
  ],
 },
 "transfer-jw-library-notes-new-phone": {
  "sections": [
   ("Do this before the old phone is wiped or traded in",
    "The backup has to be created while the old phone still works and still has JW Library installed. Once the device is reset, traded in or handed on, the notes are gone with it — JW Library keeps no cloud copy of personal study data, and a phone-level backup such as Google One or an iCloud device backup usually restores an older snapshot of the app's data, or none at all. Create the .jwlibrary file first, get it somewhere safe, and confirm you can see it before you wipe anything."),
   ("Getting the file off the old phone",
    "On Android the file is written to your chosen folder — typically Downloads or Documents — and you can move it with any file manager, email it to yourself, or drop it into cloud storage. On iPhone the share sheet appears as soon as the backup is created: save it to Files, AirDrop it to the new phone, or send it to yourself. The transfer method does not matter and cannot corrupt the file; a .jwlibrary is a single archive that either arrives intact or does not arrive at all."),
   ("Why a phone-to-phone transfer app is not enough",
    "Tools such as Smart Switch, Move to iOS or an iCloud restore copy apps and system data, but app-private databases are frequently skipped, restored partially, or restored from an older point in time. People regularly discover the gap weeks later, once the old phone is gone. Treat the .jwlibrary file as the authoritative copy and the phone transfer as a convenience — if the transfer happens to bring your notes across, restoring your own backup on top costs nothing."),
   ("Check the transfer actually worked",
    "After restoring on the new phone, open two or three publications you have annotated recently and confirm the notes, highlight colours and bookmarks are all present. A quicker check is to open the backup file itself in your browser before you wipe the old device — you can see every note, highlight and bookmark it contains, so you know what should appear. Only wipe the old phone once the new one is verified."),
  ],
  "faq": [
   ("Can I move my notes if the old phone is already gone?",
    "Only if a .jwlibrary backup exists somewhere — in Files, Downloads, an email to yourself or cloud storage. Without one there is nothing to restore from, because personal study data is stored only on the device."),
   ("Do both phones need the same JW Library version?",
    "They do not need to match exactly, but update the new phone to the current version before restoring. A backup made by a newer version can use a newer database schema than an older app understands."),
   ("Will I have to download my publications again?",
    "Usually yes — publication media is not part of the backup. Your notes reattach to each publication as soon as it is downloaded, so nothing you wrote is lost in the meantime."),
  ],
 },
 "backup-jw-library": {
  "sections": [
   ("What the file contains, and what it does not",
    "The backup holds your personal study data: notes, highlights and their colours, bookmarks, tags, and the answers you have typed into study-question fields. It does not hold the publications themselves — no Bibles, magazines, books, videos or audio. That is why a backup of years of study is usually only a few megabytes, and why restoring on a new device leaves you re-downloading publications while every note you wrote is already back in place."),
   ("How many backups to keep",
    "Keep more than one. The failure that costs people their notes is rarely a lost file — it is a good backup overwritten by a bad one, or a restore performed on the wrong device. Because the files are small, there is no reason to delete old ones: keep them dated in a folder in cloud storage. A backup from six months ago is not worthless even after you have newer ones, because anything you deleted by accident since then still exists inside it."),
   ("Where to store them",
    "Anywhere that is not only the device itself. A folder in Drive, iCloud, Dropbox or OneDrive covers the case that matters most — the device being lost, stolen, reset or damaged. Emailing the file to yourself works too and has the useful side effect of date-stamping it. The file contains your own study notes, so treat it with the same care you would any personal document."),
   ("Verifying a backup before you rely on it",
    "A backup you have never opened is an assumption, not a safety net. You can open a .jwlibrary file in your browser and see exactly which notes, highlights and bookmarks it contains — a thirty-second check that turns an assumption into a fact. This matters most immediately before something irreversible: a factory reset, a trade-in, a repair, or a major OS upgrade."),
  ],
  "faq": [
   ("Does the backup include my downloaded publications?",
    "No. Only personal study data. Publications are re-downloaded on the new device, and your notes reattach to them automatically."),
   ("Can I open a backup to check what is in it?",
    "Yes. You can open a .jwlibrary file in your browser and browse every note, highlight and bookmark it holds, without installing anything and without the file leaving your device."),
   ("Do backups expire?",
    "No. A .jwlibrary file stays restorable indefinitely. Restore into a current version of JW Library rather than an old one, since the app reads older backup formats but not newer ones."),
  ],
 },
 "jw-library-android-to-iphone": {
  "sections": [
   ("Why the format is identical on both platforms",
    "JW Library uses the same backup format everywhere it runs — Android, iOS, iPadOS and Windows. A .jwlibrary file is a ZIP containing a SQLite database with the same tables and the same schema regardless of which device wrote it. There is no conversion step, no export-to-import dance, and nothing platform-specific inside the file. An Android backup restores onto an iPhone exactly as an iPhone backup would."),
   ("The only part that really differs",
    "Not the file — just getting hold of it. On Android the backup is saved to a folder you choose and can be moved with any file manager. On iPhone it goes through the share sheet into Files, AirDrop, or whatever you pick. The friction people hit moving between platforms is always this handling step, never compatibility. Email, cloud storage or AirDrop all work; the archive arrives intact or not at all."),
   ("Highlight colours, tags and study answers",
    "All of it survives. Highlight colours are stored as a numeric index — yellow, green, blue, pink, orange and purple — and render the same on every platform. Tags and the links between tags and notes come across, as do the answers typed into study-question fields. What you see on the iPhone after restoring is what you had on the Android device."),
   ("If iOS will not let you choose the file",
    "Save the file into the Files app first, then pick it from there rather than from a mail attachment or a chat app preview. Some apps hand iOS a temporary preview copy rather than the real file, and JW Library cannot open that. If the file arrived as an attachment, tap it, choose Save to Files, and restore from Files."),
  ],
  "faq": [
   ("Do I need a computer for this?",
    "No. AirDrop, email or any cloud storage app moves the file directly between the two phones."),
   ("Does it work the other way — iPhone to Android?",
    "Yes, identically. The same steps work in every direction, including to and from the Windows app."),
   ("Will the iPhone need the same publications downloaded?",
    "Yes, since publication media is not part of a backup. Notes reattach to each publication once it is downloaded."),
  ],
 },
 "sync-jw-library-multiple-devices": {
  "sections": [
   ("Why there is no true sync",
    "JW Library has no account that carries personal study data between devices. Notes, highlights and bookmarks live in a database on each device and stay there. The only official mechanism for moving them is Backup and Restore, and a restore replaces the target device's data outright rather than combining it. So two devices used independently diverge permanently unless something merges them — which is the whole point of the routine below."),
   ("Keeping one master file",
    "The routine works best if you treat one merged file as the current master. Each cycle, back up every device, merge those backups together, and restore the result everywhere. The merged file then becomes the master for the next cycle. Keeping the dated masters in cloud storage gives you both a sync mechanism and a running archive — if you delete something by accident, an earlier master still contains it."),
   ("What happens if you skip a device for a while",
    "Nothing is lost. A device left out of several cycles simply carries older data; when you finally include it, its notes merge in alongside everything else and duplicate items are matched by GUID rather than duplicated. The only situation needing a decision is the same note edited on two devices since they were last merged, and that is surfaced in the Conflict Reviewer with both versions shown side by side."),
   ("How often is often enough",
    "Match it to how much work you would mind redoing. Weekly suits people who study on two devices most days; monthly is plenty if one device is occasional. The important thing is doing it before anything irreversible — a phone upgrade, a reset, a repair — because that is when a divergence becomes a loss."),
  ],
  "faq": [
   ("What if I edited the same note on two devices?",
    "Both versions are kept until you choose. The Conflict Reviewer shows them side by side with a word-level diff, or you can let it suggest the fuller version."),
   ("Does the order I restore in matter?",
    "No. Once the merged file is created, restoring it on each device puts every device into the same complete state, in whatever order suits you."),
   ("Can I sync three or more devices?",
    "Yes. Back up each one and load them all into the same merge — there is no limit tied to device count."),
  ],
 },
 "jw-library-notes-missing-after-update": {
  "sections": [
   ("First: do not create a new backup yet",
    "If notes have vanished, resist the reflex to back up immediately. A backup captures the current state, and if the current state is the empty one you risk overwriting the good file you already had. Find out what backups exist first — in Downloads, Files, email, or cloud storage — and only then decide what to do. Nothing on the device is improved by a fresh backup taken in a panic."),
   ("Why an update can appear to lose notes",
    "The usual cause is not deletion. An update can leave the app pointing at a fresh, empty database while the old one is still on disk; a reinstall — including one performed automatically by a store update that failed midway — starts the app from scratch; and on shared or multi-profile devices the app can end up running under a different profile than before. In each case the notes are not gone so much as not currently loaded, which is also why a restore from backup usually brings everything back cleanly."),
   ("Recovering an old backup without discarding new work",
    "If you have studied since the backup was made, a plain restore trades one loss for another: it brings the old notes back and removes anything newer. The way around it is to back up the current state to a separate file, merge that with the older backup so both sets of notes exist in one file, and restore the merged result. You end up with the recovered notes and the recent ones together rather than choosing between them."),
   ("If the app reinstalled itself",
    "A reinstall clears app-private storage, so anything not in a backup is unrecoverable — there is no cloud copy to fall back on. Check every place a .jwlibrary file might have been saved before concluding there is none, including your email sent folder and any cloud storage you have ever saved to. Once you find one, restore it, and thereafter keep backups outside the device."),
  ],
  "faq": [
   ("Are my notes really gone?",
    "Not necessarily. If a backup exists anywhere, everything in it is fully recoverable. What is unrecoverable is only work done after the most recent backup was taken."),
   ("Can I combine an old backup with what is on the device now?",
    "Yes — back up the current state first, then merge that file with the older one and restore the result. Both sets of notes end up in the same library."),
   ("Will restoring an old backup delete my recent notes?",
    "On its own, yes, because a restore replaces the device's data. Merge the current backup with the old one first and restore the merged file instead."),
  ],
 },
 "recover-jw-library-notes-lost-phone": {
  "sections": [
   ("Where a backup may already exist",
    "Before concluding there is none, check everywhere a file might have been saved: the Downloads and Documents folders of any computer you have connected the phone to, your email sent items, chat apps you may have sent the file through, and every cloud storage account you use. People often created a backup once, months ago, and forgot — and a months-old backup still contains the great majority of a study library."),
   ("Restoring onto a different phone or platform",
    "The replacement device does not need to match the lost one. A backup from an Android phone restores onto an iPhone and vice versa, because the format is identical across Android, iOS, iPadOS and Windows. Install JW Library on the new device, update it to the current version, then restore through Personal Study → Backup and Restore."),
   ("If all you have is an old or partial backup",
    "Restore it anyway. Recovering most of your notes is not a consolation prize — it is the outcome. If you later find a second, different backup, the two can be merged into one file that contains everything from both, so restoring the older one now does not prevent you from adding to it later."),
   ("What cannot be recovered",
    "If no backup exists in any form, personal study data cannot be retrieved. It is stored only in the app's private storage on the device, and neither JW Library nor a phone-level cloud backup reliably preserves it. This is worth knowing plainly, because it is the reason the routine on this site exists at all."),
  ],
  "faq": [
   ("Does JW Library keep a cloud copy of my notes?",
    "No. Personal study data stays on the device unless you create a backup file yourself."),
   ("Can notes be recovered from a phone with a broken screen?",
    "Sometimes — if the phone still powers on and can be controlled, or a repair shop can drive the display, JW Library can still create a backup. The data is intact as long as the storage is."),
   ("Will an old backup still restore into the current app?",
    "Yes. JW Library reads older backup formats. Update the app first and restore into the current version."),
  ],
 },
 "fix-corrupted-jw-library-backup": {
  "sections": [
   ("What corrupted usually means",
    "In practice it is rarely damaged data. The common causes are a file that was truncated in transfer — cut short by a failed upload or a chat app that compressed it — or an archive that is intact but contains internal inconsistencies the app rejects. Because a .jwlibrary file is a ZIP wrapping a SQLite database, either layer can be the problem, and they need different fixes. A truncated file cannot be repaired and has to be re-obtained; an inconsistent database usually can be."),
   ("What a scan actually checks",
    "A scan verifies that the archive opens, that userData.db is a readable SQLite database that passes an integrity check, that the schema matches what JW Library expects, and that the manifest agrees with the database it describes — including the hash the app uses to confirm the file has not been altered. A mismatch between the manifest and the database is one of the most common reasons a technically fine backup is refused on restore, and it is straightforwardly repairable."),
   ("Orphaned rows are usually harmless",
    "A scan of a real backup will often report rows that reference something no longer present — a highlight pointing at a publication location that has moved, for instance. JW Library's own backups routinely contain hundreds of these and restore without complaint. They are a normal consequence of publications being updated over time, not evidence of damage, and clearing them is not necessary to make a file work."),
   ("Rescuing notes from a file that will not restore",
    "Even when a backup cannot be repaired well enough for JW Library to accept it, the notes inside are often still readable. Opening the file in your browser lets you see and copy the note text directly, which turns an unusable file into recovered study material. If you have a second, older backup that does restore, the readable content from the damaged one can be brought together with it rather than retyped."),
  ],
  "faq": [
   ("Will repairing the file lose any notes?",
    "Repairs work on a copy and address structural problems rather than content. Your original file is never modified, so it remains available if you want to start again."),
   ("Why did my backup get corrupted?",
    "Most often the file was altered in transit — sent through an app that compressed or truncated it, or an upload that did not finish. Transferring the file again from the original source usually resolves it."),
   ("Can a scan recover notes I deleted inside JW Library?",
    "No. Once deleted in the app and a new backup taken, the note is gone from that file. An older backup made before the deletion will still contain it."),
  ],
 },
 "export-jw-library-notes": {
  "sections": [
   ("Choosing a format",
    "Plain text is the most portable and pastes cleanly into any document or email. Formatted output preserves the structure of longer notes and suits printing or sharing. If you want the notes back inside JW Library later — on another device, or for someone else's library — keep the .jwlibrary file itself rather than a text export, since only that preserves the links between notes, highlights, tags and the exact place in the publication they are anchored to."),
   ("Exporting only part of your library",
    "A full export of years of study is rarely what you want. Narrowing first — to a tag, a publication, a highlight colour, or a date range — produces something you can actually use, such as every note tagged for a talk, or everything written during one convention. The same filters that narrow the view narrow the export, so what you see is what you get."),
   ("What travels with the text, and what does not",
    "An export carries your words. It does not carry the anchors that tie a note to a specific paragraph of a specific publication, because those references only mean something inside JW Library. This is the practical reason to keep backups as well as exports: an export is for reading, printing and sharing outside the app, while a .jwlibrary file is what puts the notes back into a library with their context intact."),
  ],
  "faq": [
   ("Can I get my notes into Word or Google Docs?",
    "Yes — export as text and paste it in. The text arrives with its structure intact and can be styled from there."),
   ("Do highlights export as well as notes?",
    "Yes, including the highlighted passage and its colour, so a printed copy shows what you marked as well as what you wrote."),
   ("Can I export everything at once?",
    "Yes, though a filtered export is usually more useful. Everything can be exported in one pass when you want a complete copy."),
  ],
 },
 "open-jwlibrary-file": {
  "sections": [
   ("What the file actually is",
    "A .jwlibrary file is a ZIP archive with a different extension. Inside it are userData.db — a SQLite database holding your notes, highlights, bookmarks and tags — and manifest.json, a small file describing the backup, including a hash of the database that JW Library uses to confirm the file has not been altered. Nothing about it is proprietary or encrypted; it is a standard archive around a standard database."),
   ("Opening it without JW Library",
    "You do not need the app, or any software, to read your own backup. Opening the file in your browser shows every note, highlight and bookmark it contains, with search and filtering, and the file never leaves your device — it is read locally rather than uploaded. This is the fastest way to confirm a backup contains what you think it does before a reset, a trade-in, or a restore onto a new phone."),
   ("Looking inside manually",
    "If you are curious, copy the file, rename the copy to .zip and open it with any archive tool. You will see userData.db and manifest.json. Opening the database needs a SQLite viewer, and the tables are named for what they hold — Note, UserMark, Bookmark, Tag. Always work on a copy: editing the database by hand without updating the manifest hash produces a file JW Library will refuse to restore."),
   ("Editing safely",
    "Notes can be corrected, retagged, recoloured or deleted outside the app, and the result exported as a new .jwlibrary file you restore normally. The rule that keeps this safe is to keep the original: edit a copy, restore the edited file, and if anything is not as you expected, the untouched original is still there to fall back on."),
  ],
  "faq": [
   ("Can I just rename it to .zip?",
    "Yes, on a copy. Renaming does not alter the contents, and it lets any archive tool show you what is inside."),
   ("Will opening the file change it?",
    "No. Reading a backup — in the browser or an archive tool — leaves it byte-for-byte unchanged. Only saving or exporting produces a new file."),
   ("Do I need to be online?",
    "Only to load the page. The file itself is read on your device, not uploaded, so your notes never travel over the network."),
  ],
 },
}


def find_record(src, slug):
    """Half-open span of one guide's dict literal in the GUIDES list."""
    m = re.search(r'\n \{\n  "slug": "%s",\n' % re.escape(slug), src)
    if not m:
        sys.exit("!! record not found: %s" % slug)
    end = src.find("\n },\n", m.start() + 1)
    if end < 0:
        sys.exit("!! record end not found: %s" % slug)
    return m.start(), end


def insert(src, slug, field, entries):
    """Append tuples to `field` of one guide, before its closing bracket."""
    start, end = find_record(src, slug)
    rec = src[start:end]
    key = '\n  "%s": [\n' % field
    at = rec.find(key)
    if at < 0:
        sys.exit("!! %s: no %s field" % (slug, field))
    close = rec.find("\n  ],", at)
    if close < 0:
        sys.exit("!! %s: unterminated %s" % (slug, field))
    block = "".join(
        '   (%s,\n    %s),\n' % (pylit(a), pylit(b)) for a, b in entries)
    rec = rec[:close + 1] + block + rec[close + 1:]
    return src[:start] + rec + src[end:]


def pylit(s):
    """Double-quoted Python literal; copy uses curly quotes, so " is rare."""
    if '"' in s:
        sys.exit("!! straight double quote in copy: %.60s" % s)
    return '"%s"' % s.replace("\\", "\\\\")


def main():
    src = io.open(SRC, encoding="utf-8").read()
    if "What is actually inside a .jwlibrary file" in src:
        sys.exit("already deepened — nothing to do")
    for slug, add in ADD.items():
        for field in ("sections", "faq"):
            if add.get(field):
                src = insert(src, slug, field, add[field])
    io.open(SRC, "w", encoding="utf-8").write(src)
    print("deepened %d guides" % len(ADD))


if __name__ == "__main__":
    main()

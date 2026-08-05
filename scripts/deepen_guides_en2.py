#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Second deepening pass: bring the remaining top guides to the 1,200+ word band.

Pass one (deepen_guides_en.py) lifted the ten guides from 440–800 rendered
words to 777–1,289. This pass covers the eight that still landed short of the
target, adding the situational material readers actually arrive with — moving
to a tablet as well as a phone, what to do on the new device *before*
restoring, sharing notes with someone else, why a restore fails with no error.

Reuses the insertion helpers from pass one so the two stay consistent.

Run from the repo root:  python3 scripts/deepen_guides_en2.py
"""
import io
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_guides_en import SRC, insert  # noqa: E402

ADD = {
 "transfer-jw-library-notes-new-phone": {
  "sections": [
   ("Moving to a tablet or computer at the same time",
    "The same file works everywhere. If you are setting up a new phone and a tablet together, restore the identical .jwlibrary file on both and they start out matching. From that point they will drift apart again as you study on each, so it is worth deciding now whether you will keep them merged periodically or treat one as the device that matters."),
   ("If the new phone already has notes on it",
    "This happens when you use the new device for a week before getting round to the transfer. A straight restore would replace that work with the old phone's data. Back the new phone up first, merge that file with the old phone's backup, and restore the merged result — both sets of notes end up in one library instead of one overwriting the other."),
  ],
  "faq": [
   ("How long does the whole thing take?",
    "A few minutes. Creating the backup takes seconds, moving the file depends on your method, and the restore is quick. Re-downloading publications afterwards takes longest and can happen in the background."),
   ("Can I do this without Wi-Fi?",
    "The transfer itself yes, over AirDrop or a cable. Re-downloading publications on the new device needs a connection."),
  ],
 },
 "backup-jw-library": {
  "sections": [
   ("The moments worth backing up before",
    "Any point where the device changes hands or state: an OS upgrade, a factory reset, a repair or screen replacement, a trade-in, or handing a device on to someone else. Add to that the end of anything you would hate to redo — a convention, an assembly, a stretch of preparation for a talk. Backups are cheap and quick, so the useful habit is tying them to events rather than to a calendar."),
   ("A phone backup is not a JW Library backup",
    "Google One, an iCloud device backup or a manufacturer transfer tool operate at the device level and treat app-private data inconsistently. People routinely find that a full phone restore brought back their apps and settings but not their study notes, or brought back a version from weeks earlier. The .jwlibrary file is the only copy whose contents you control and can verify, so treat the phone-level backup as a bonus rather than the plan."),
  ],
  "faq": [
   ("Should I back up before every meeting?",
    "No need. Tie backups to events that could cost you data — updates, repairs, new devices — plus a regular rhythm that matches how much study you would mind repeating."),
   ("Is it worth keeping backups from years ago?",
    "Yes. They are small, and anything you deleted by accident since then still exists inside them."),
  ],
 },
 "jw-library-android-to-iphone": {
  "sections": [
   ("Set the iPhone up before restoring",
    "Install JW Library from the App Store and update it to the current version before you restore anything. A backup written by a newer version of the app can use a database schema an older version does not understand, and the restore will simply be refused. Signing in to anything is not required — personal study data lives in the file you are restoring, not in an account."),
   ("If you have already started studying on the iPhone",
    "Back the iPhone up first. Restoring the Android file straight over the top would replace whatever you have written since switching. Merging the two backups produces one file containing both, which you then restore — the Android history and the new iPhone notes end up in the same library."),
   ("Keeping both phones going afterwards",
    "Some people keep the old Android device as a second reader rather than retiring it. That works, but the two will diverge as soon as you annotate on both, because there is no sync between them. If you intend to use both, plan on merging their backups periodically rather than assuming they stay aligned."),
  ],
  "faq": [
   ("Do I need to keep the Android phone afterwards?",
    "No, once you have verified the notes are present on the iPhone. Check a few annotated publications before wiping or trading in the old device."),
   ("Does the transfer work for study-question answers?",
    "Yes. Typed answers are part of personal study data and come across with everything else."),
  ],
 },
 "sync-jw-library-multiple-devices": {
  "sections": [
   ("Phone, tablet and the Windows app together",
    "The routine does not care how many devices are involved or what they run. Back up each, merge them all in one pass, restore the merged file everywhere. A Windows machine used for preparation and a phone used at meetings combine exactly as two phones would, because every platform writes the same backup format."),
   ("Reducing conflicts before they happen",
    "Conflicts only arise when the same note is edited on two devices between merges. In practice that is rare, and it becomes rarer if you write on one device at a time — reading anywhere, but doing the typing where you usually type. Merging more often also shrinks the window in which a divergence can occur, which is a better fix than trying to remember which device holds the newest version."),
  ],
  "faq": [
   ("Can this be automated?",
    "Not fully, because JW Library has no sync API and the restore step happens in the app. The manual routine takes about two minutes once you are used to it."),
   ("Do I need to merge if I only read on the second device?",
    "If you never annotate on it, you only need to restore onto it periodically so it carries your current notes."),
  ],
 },
 "recover-jw-library-notes-lost-phone": {
  "sections": [
   ("Check before the device is wiped remotely",
    "If the phone is lost rather than destroyed, and you are considering a remote erase, look for existing backups first — the erase is irreversible and removes the last chance of anyone creating one. If the device is merely misplaced and still reachable, creating a backup remotely is not possible, but the data remains intact as long as the phone is not wiped or reset."),
   ("Making sure this cannot happen twice",
    "The reason a lost phone costs people years of study is that the only copy was on the phone. Once you have restored onto a replacement, put a backup somewhere off the device the same day, and repeat it on a rhythm you will actually keep. The files are small enough that keeping every one of them indefinitely costs nothing."),
  ],
  "faq": [
   ("I found two old backups — which should I use?",
    "Neither alone. Merge them: the result contains everything from both, including anything present in the older file that had been deleted by the time of the newer one."),
   ("Can I check what is in a backup before restoring it?",
    "Yes. Open the file in your browser and browse its notes, highlights and bookmarks first, so you know what you are restoring."),
  ],
 },
 "fix-corrupted-jw-library-backup": {
  "sections": [
   ("When the restore fails with no clear error",
    "JW Library often refuses a file without explaining why. The most frequent causes are a manifest whose hash no longer matches the database it describes, a file truncated in transfer, or a backup written by a newer version of the app than the one you are restoring into. The first is repairable, the second needs the file fetching again from its original source, and the third is solved by updating the app before restoring."),
   ("Avoiding it next time",
    "Most damage happens in transit. Move backups as files rather than through anything that may recompress them, and prefer cloud storage, AirDrop or a cable to chat apps. After transferring, confirm the file size matches the original — a file noticeably smaller than the one you sent was truncated, and no repair will bring back bytes that never arrived."),
  ],
  "faq": [
   ("Can I tell from the file size whether it is truncated?",
    "Often yes. Compare it against the original if you still have it; a significant shortfall means the transfer did not complete."),
   ("Is a backup that opens in the browser guaranteed to restore?",
    "Not guaranteed, but it is a strong sign the archive and database are sound, which rules out the most common failures."),
  ],
 },
 "export-jw-library-notes": {
  "sections": [
   ("Pulling together everything for one talk or assignment",
    "This is the most common reason to export. Filter to the tag, publication or date range the material sits under, check the result, and export just that. What you get is a single document containing the relevant notes and the passages you highlighted, in the order they appear, rather than an unmanageable dump of your whole library."),
   ("Sharing notes with someone else",
    "There are two different things people mean by sharing. If the other person wants to read your notes, a text export is right — it opens anywhere and needs no special software. If they want the notes inside their own JW Library, anchored to the same paragraphs and carrying their tags and colours, then a .jwlibrary file is what you want instead, because a text export cannot put anything back into the app."),
   ("Keeping an archive you can still read later",
    "Exports are also worth making for their own sake. A plain-text copy of your study notes will still open in thirty years on software nobody has written yet, which is not something any app-specific format can promise. Keeping both — the .jwlibrary for restoring and a text export for reading — costs almost nothing and covers both futures."),
  ],
  "faq": [
   ("Can I export the answers I typed into study questions?",
    "Yes. Typed study answers are part of your personal study data and can be exported along with notes and highlights."),
   ("Will an export include which publication each note belongs to?",
    "Yes, the export identifies where each note came from, even though the underlying anchor only functions inside JW Library."),
  ],
 },
 "open-jwlibrary-file": {
  "sections": [
   ("Reading a backup on a phone",
    "You do not need a computer. Opening the file in a mobile browser works the same way, which is useful when the backup is already on the phone and you want to confirm its contents before restoring or before wiping the device. The file is read locally, so this works with no connection beyond loading the page itself."),
   ("Why the manifest hash matters",
    "manifest.json records a hash of userData.db. JW Library uses it to confirm the database has not been altered since the backup was written, so a file whose database has been edited without the hash being recalculated is refused on restore. This is the single most common reason a hand-edited backup stops working, and the reason editing through a tool that rewrites the manifest is safer than editing the database directly."),
  ],
  "faq": [
   ("Can I open a backup someone else sent me?",
    "Yes, the format is not tied to a device or account. Whether you should restore it is a separate question, since restoring replaces your own library."),
   ("Do I need to install anything to look inside?",
    "No. A browser is enough to read the notes; only manual inspection of the database itself needs a SQLite viewer."),
  ],
 },
}


def main():
    src = io.open(SRC, encoding="utf-8").read()
    if "The moments worth backing up before" in src:
        sys.exit("pass two already applied — nothing to do")
    for slug, add in ADD.items():
        for field in ("sections", "faq"):
            if add.get(field):
                src = insert(src, slug, field, add[field])
    io.open(SRC, "w", encoding="utf-8").write(src)
    print("second pass: deepened %d guides" % len(ADD))


if __name__ == "__main__":
    main()

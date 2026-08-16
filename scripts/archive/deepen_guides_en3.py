#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Third deepening pass: clear 1,200 rendered words on the last nine guides.

Passes one and two brought the set to 1,045–1,289. This adds, per guide, one
opening paragraph and one closing section — the two positions that carry the
most weight, since the intro is the first thing both a reader and a crawler
see, and the closing section is where "so what do I do now" belongs.

Run from the repo root:  python3 scripts/deepen_guides_en3.py
"""
import io
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_guides_en import SRC, insert, find_record, pylit  # noqa: E402

INTRO = {
 "transfer-jw-library-notes-new-phone":
    "Getting a new phone is the single most common moment people lose years of JW Library notes — not because the transfer is difficult, but because it has to be done deliberately before the old device is wiped. Personal study data does not ride along with a normal phone-to-phone transfer, and JW Library keeps no copy of it in any account.",
 "backup-jw-library":
    "Everything you have marked in JW Library — every note, every highlight, every bookmark and tag — exists in exactly one place: the device in your hand. There is no account holding a copy and no automatic cloud sync. A backup is the only thing standing between a study library built over years and a lost, reset or upgraded phone.",
 "jw-library-android-to-iphone":
    "Switching between Android and iPhone sounds like the hard case, and it is the easy one. JW Library writes the same backup format on every platform it runs on, so moving a study library from Android to iOS is the same operation as moving it between two Android phones — no conversion, no export format to choose, nothing lost in translation.",
 "sync-jw-library-multiple-devices":
    "Most people who study on two devices discover the problem the same way: notes written on the tablet are not on the phone, and restoring one device's backup onto the other would wipe whatever that device had. JW Library offers no sync, and its Restore is deliberately all-or-nothing, so keeping devices aligned takes a routine rather than a setting.",
 "jw-library-notes-missing-after-update":
    "Opening JW Library after an update to find your notes gone is alarming, and in the great majority of cases they are recoverable. What matters is what you do in the next few minutes — specifically, not doing the one thing that turns a recoverable situation into a permanent loss.",
 "recover-jw-library-notes-lost-phone":
    "When a phone is lost, stolen or damaged beyond use, whether your JW Library notes survive comes down to one question: does a .jwlibrary backup exist anywhere outside that device? If it does, everything in it comes back. This page covers how to find one, how to restore it onto any replacement device, and what to do when the only backup you have is old.",
 "fix-corrupted-jw-library-backup":
    "A backup that will not restore is not necessarily a backup that has lost your notes. Most files people describe as corrupted are structurally sound and rejected for a fixable reason, or damaged in transfer in a way that a fresh copy resolves. It is worth working through the causes before writing off the file.",
 "export-jw-library-notes":
    "Notes written in JW Library are easy to read inside the app and awkward to use anywhere else — in a document, in a talk outline, on paper, or in the hands of someone who does not use the app. Exporting solves that, and the main decision is not how to export but how much: a filtered export is almost always more useful than everything at once.",
 "open-jwlibrary-file":
    "A .jwlibrary file looks opaque, and it is not. It is an ordinary ZIP archive around an ordinary SQLite database, which means you can read your own backup — see exactly which notes, highlights and bookmarks it holds — without JW Library and without installing anything at all.",
}

SECTION = {
 "transfer-jw-library-notes-new-phone":
   ("What to do once the new phone is working",
    "Verify before you dispose of anything. Open a few publications you annotated recently on the new phone and confirm the notes, colours and bookmarks are all there, then wipe or trade in the old device — in that order, never the reverse. Once you are settled, put a backup somewhere off the phone, because the situation that brought you to this page will come round again with the next upgrade."),
 "backup-jw-library":
   ("Turning it into a habit that survives",
    "The routine that actually holds is the one attached to something you already do: back up when you finish preparing for the week, or on the same day you do any other regular admin. Save to the same folder every time so the files accumulate in one place, and leave the old ones there. A folder of dated backups going back years is the most robust form this can take, and it takes seconds a week to maintain."),
 "jw-library-android-to-iphone":
   ("After the move",
    "Give the iPhone time to re-download the publications you use most, then check a handful of annotated ones to confirm everything arrived — notes, highlight colours, bookmarks and tags. Keep the Android backup file even after the switch is complete: it is a dated snapshot of your library, and it costs nothing to keep."),
 "sync-jw-library-multiple-devices":
   ("Where the routine pays off",
    "The value of keeping devices merged is not the tidiness — it is that every device becomes a full backup of your study library. Lose or break any one of them and the others still carry everything, which turns the worst case from years of lost notes into an inconvenience. That is a stronger position than any single-device backup habit can give you."),
 "jw-library-notes-missing-after-update":
   ("Once everything is back",
    "When your notes are restored, take one more backup and store it off the device — the episode you have just been through is the argument for it. If you had to merge an old backup with the current state to get here, keep both source files as well: they are dated snapshots, and having more of them is what made the recovery possible in the first place."),
 "recover-jw-library-notes-lost-phone":
   ("If there is genuinely no backup",
    "Then the honest answer is that the notes cannot be retrieved, and it is better to hear that than to keep searching. What you can do is make the loss the last one: install JW Library on the replacement, and before you have rebuilt anything worth losing, create a backup and put it somewhere off the device. From that point the same event costs you nothing."),
 "fix-corrupted-jw-library-backup":
   ("If nothing works",
    "A file that cannot be repaired can still be readable, and reading it is often enough — the note text can be recovered directly even when JW Library refuses the file. Combine that with any older backup that does restore and you usually end up with most of your library intact. Before concluding a file is beyond use, open it and see what is actually inside it."),
 "export-jw-library-notes":
   ("Export or backup — which you need",
    "The two answer different questions. An export is for using your notes outside JW Library: reading, printing, quoting, sending to someone. A .jwlibrary backup is for putting them back into JW Library, on this device or another, with every anchor, tag and colour intact. Neither substitutes for the other, and there is no reason not to keep both."),
 "open-jwlibrary-file":
   ("What this is good for",
    "Being able to read a backup changes what a backup is worth. You can confirm a file contains what you think before wiping a phone, check whether an old file is worth restoring, find a note you know you wrote without hunting through the app, or recover text from a file JW Library will not accept. None of it requires trusting the file to anyone — it is read on your own device."),
}


def add_intro(src, slug, text):
    start, end = find_record(src, slug)
    rec = src[start:end]
    key = '\n  "intro": [\n'
    at = rec.find(key)
    if at < 0:
        sys.exit("!! %s: no intro" % slug)
    rec = rec[:at + len(key)] + "   %s,\n" % pylit(text) + rec[at + len(key):]
    return src[:start] + rec + src[end:]


def main():
    src = io.open(SRC, encoding="utf-8").read()
    if "Turning it into a habit that survives" in src:
        sys.exit("pass three already applied — nothing to do")
    for slug, text in INTRO.items():
        src = add_intro(src, slug, text)
    for slug, sec in SECTION.items():
        src = insert(src, slug, "sections", [sec])
    io.open(SRC, "w", encoding="utf-8").write(src)
    print("third pass: deepened %d guides" % len(INTRO))


if __name__ == "__main__":
    main()

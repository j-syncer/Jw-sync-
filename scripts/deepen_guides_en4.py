#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fourth pass: the last three guides sat at 1,177–1,196, just under the 1,200
target. One more FAQ entry each clears it.

Run from the repo root:  python3 scripts/deepen_guides_en4.py
"""
import io
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_guides_en import SRC, insert  # noqa: E402

ADD = {
 "jw-library-android-to-iphone": [
  ("Is there any risk of losing notes in the move?",
   "Not if you keep the Android backup. The restore writes to the iPhone and never alters the file it reads, so the original stays intact as a fallback. Keep it until you have confirmed the iPhone has everything, and ideally afterwards too — it is a dated snapshot of your library."),
  ("What if the Android phone will not create a backup?",
   "Check available storage first, since the app needs room to write the file. If the app itself is failing, updating it or restarting the device usually resolves it. The data remains intact while you troubleshoot."),
 ],
 "jw-library-notes-missing-after-update": [
  ("Should I reinstall the app to fix it?",
   "No — reinstalling clears app-private storage and removes any chance of recovering what is still on the device. Look for an existing backup first, and treat reinstalling as a last resort after you have one."),
 ],
 "export-jw-library-notes": [
  ("Does exporting change anything in my library?",
   "No. An export reads your data and writes a separate file; nothing in JW Library is altered, moved or removed by it."),
  ("Can I export from a backup rather than the app?",
   "Yes. A .jwlibrary file can be opened directly and its notes exported, which is useful when the notes you want are in an old backup rather than on your current device."),
 ],
}


def main():
    src = io.open(SRC, encoding="utf-8").read()
    if "Should I reinstall the app to fix it?" in src:
        sys.exit("pass four already applied — nothing to do")
    for slug, faq in ADD.items():
        src = insert(src, slug, "faq", faq)
    io.open(SRC, "w", encoding="utf-8").write(src)
    print("fourth pass: %d guides" % len(ADD))


if __name__ == "__main__":
    main()

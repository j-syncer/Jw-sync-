#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_md_import_guide_en.py — the English guide for importing Markdown.

Adds a 38th guide to build_guides.GUIDES. The translations live in
add_md_import_guide_i18n.py, which splices the same slug into each
scripts/guides_<lang>.py.

Everything this page promises about what the parser accepts is enforced by
tests/25_md_tolerance.js — each row there is a sentence here. If the two ever
disagree, the guide is lying, which is worse than the guide being missing.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "scripts", "build_guides.py")

GUIDE = '''
 {
  "slug": "import-markdown-notes-jw-library",
  "group": "Power tools",
  "title": "How to Import Markdown Notes into JW Library",
  "h1": "How to import Markdown notes into JW Library",
  "description": "Turn .md files from Obsidian, Notion or any Markdown editor into real JW Library notes, placed on the right verse — free, private, in your browser.",
  "intro": [
   "JW Library has no way to bring text in. You can write notes inside the app, but a note written anywhere else — in Obsidian, in Notion, in a plain text file on your computer — has no route into your library at all. People retype them, or give up and keep two sets of study notes that never meet.",
   "JW Sync closes that gap. Load a backup in the Study Explorer, press Import Markdown, and your .md files become real notes inside it: title, date and tags intact, and — when the file says which scripture it belongs to — attached to that verse, exactly as if you had written the note in the app while reading it.",
   "It works in both directions. Notes exported from this site carry their book, chapter and verse, so they go back to precisely where they came from. Notes written anywhere else usually carry nothing of the sort, so this page explains the one or two lines that place them — and what happens when a file does not have them.",
  ],
  "steps": [
   ("Create a backup in JW Library", "Open JW Library, go to Personal Study, tap the three-dot menu, choose Backup and Restore, then Create a backup. That gives you a .jwlibrary file — the library your notes will be added to."),
   ("Open the Study Explorer", "Go to jwsync.org, open the Study Explorer, and load that .jwlibrary file. Everything happens inside your browser; the file is never uploaded."),
   ("Press Import Markdown", "The button sits next to Export Markdown. Choose as many .md files as you like, or a .zip of them — including the .zip this site produces when you export."),
   ("Read the summary before anything is written", "You are told how many notes will land on a verse, how many will be added as standalone notes, and how many are already in your backup and will be skipped. Anything the site had to interpret is listed one line at a time, with a tick box, so you decide rather than discover later."),
   ("Export and restore", "Press Export .jwlibrary, then restore that file in JW Library through Backup and Restore → Restore. Your imported notes are now part of your library on that device."),
  ],
  "sections": [
   ("The shortest file that works",
    "A Markdown file needs nothing at all to be imported — a file containing only text becomes a note, taking its title from the first heading or, failing that, from the filename. Everything beyond that is about telling the site where the note belongs. A complete file looks like this:\\n\\n---\\ntitle: The cup he prayed about\\ntags: [study, gethsemane]\\npublication: Matthew 26:39\\n---\\n\\nHis prayer shows submission, not reluctance.\\n\\nThe block between the two lines of dashes is called front matter. The lines below it are the note itself."),
   ("The fields it reads",
    "Only five things are read, and each has several accepted spellings so you do not have to remember an exact one. **title** (or name, heading) becomes the note's title. **tags** (or tag, keywords, categories, labels, topics) become real JW Library tags, created if they do not exist yet. **date** (or created, modified) sets the note's date; anything containing YYYY-MM-DD is understood. **publication** (or pub, reference, ref, scripture, citation, source, passage) is where you write the verse. **book**, **chapter** and **verse** (or ch, v, vs, verses) do the same job in separate fields. Any other field you keep for your own purposes — author, status, whatever your editor adds — is ignored rather than treated as an error."),
   ("Three ways to point a note at a verse",
    "Write the reference on one line: `publication: Matthew 26:39`. Or split it up: `book: Matthew`, `chapter: 26`, `verse: 39`. Or use both — that is what this site's own export does, so the file reads well to a human and parses exactly for a machine. All three produce the same result, so use whichever suits the editor you write in."),
   ("How forgiving the reference can be",
    "Book names are matched generously. Full names work, and so do the abbreviations people actually type: Matt, Matt., Mt, 1 Cor, 1Cor, I Corinthians, Second Timothy, Psalm as well as Psalms, Song of Songs as well as Song of Solomon. The separator between chapter and verse can be a colon, a full stop or the word v — `John 3:16`, `John 3.16` and `1 Cor 13 v4` are all read the same way. Spaces are optional throughout, so `1Cor13:4` is fine.\\n\\nThe front matter itself is just as forgiving. Keys may be capitalised. The space after the colon may be missing. Extra spaces and tabs are ignored, as are quotes around values and a trailing # comment. Windows line endings are fine. You may even leave out the --- fences entirely and simply begin the file with the fields, as long as the very first line is one of the recognised names — that rule exists so a note that opens with an ordinary sentence containing a colon does not lose its first paragraph."),
   ("Tags, however you write them",
    "All of these produce the same two tags: `tags: [study, greek]`, `tags: study, greek`, `tags: study; greek`, `tags: #study #greek`, or a list on its own lines beneath `tags:` with each entry starting with a dash. Tags that already exist in your library are reused rather than duplicated, so an imported note joins the same tag you already filter by."),
   ("What happens when something is unclear",
    "Nothing uncertain is decided for you. If a book name is close to a real one but not exact — `Mathew`, `Ecclesiates` — the note is not placed automatically. It appears in the summary on its own line saying what the site made of it: “read as Matthew 26:39”, with a tick box. Untick it and it is left out; leave it ticked and it goes where the line says.\\n\\nIf the book cannot be recognised at all, the line says so and the note is added as a standalone note instead — never forced onto a guess. A numbered book keeps its number, so `1 Jonh` can only ever be corrected to 1 John, never to 2 John."),
   ("What it deliberately will not do",
    "A verse range anchors the note to its first verse: `Matthew 26:39-41` places the note at verse 39, because a JW Library note attaches to one point in the text rather than to a span. A reference with a chapter but no verse — `Matthew 26` — attaches the note to that chapter. A file naming a publication rather than a scripture — `The Watchtower—2023 No. 4` — is imported as an ordinary standalone note without any question being asked, since that is what this site's own export writes for notes taken in an article."),
   ("Formatting that survives the trip",
    "Paragraphs, line breaks, **bold**, *italics* and bulleted lists come through as real formatting in JW Library. A heading at the top of the file is used as the note's title rather than repeated inside it. Anything Markdown can express that JW Library notes cannot — tables, images, links, code blocks — is reduced to its text, so nothing is lost from the words even when the layout cannot be carried over."),
   ("Where the notes actually end up, and why that is safe",
    "To attach a note to a verse, JW Library needs internal identifiers for that chapter that are particular to your library. JW Sync never invents them. It reuses the location your own backup already has for that chapter, or copies those identifiers from another scripture location in the same file. If a backup contains no Bible notes or highlights at all, there is nothing to copy from, so the notes are added as standalone notes rather than attached to something the app might not recognise. That is a deliberate choice: a note that quietly lands in the wrong place is worse than one that arrives plainly unattached."),
   ("Importing the same files twice",
    "A note is treated as already present when its title, its text and its place all match something in the backup, so re-importing the same export does not double anything up. The summary tells you how many were skipped for that reason before you commit. Everything an import adds is one step of Undo, and imported notes are tagged Imported so you can find, filter or delete them as a group afterwards."),
  ],
  "faq": [
   ("Do I have to use the --- lines?",
    "No. They make the file unambiguous, and every Markdown editor understands them, but you can also just start the file with the fields — `title: …` on the first line — or skip the front matter entirely and let the note take its title from the first heading."),
   ("What if I misspell a book name?",
    "The site will usually work out what you meant, but it will not act on that alone. The note appears in the summary saying how it was read, with a tick box, so you confirm before anything is written."),
   ("Can I import a whole folder from Obsidian?",
    "Select as many .md files as you like in one go, or zip the folder and choose the .zip. Files inside the archive are read the same way as loose ones."),
   ("Will importing overwrite the notes I already have?",
    "No. Importing only adds. Your existing notes, highlights, bookmarks and tags are untouched, and the file you loaded is never modified — you download a new .jwlibrary at the end."),
   ("Are my notes uploaded anywhere?",
    "No. The whole thing runs in your browser, like everything else on this site. Your backup and your Markdown files never leave your device."),
   ("Which languages can I write the reference in?",
    "Book names are recognised in English at present, which is also what the export writes. If you write your notes in another language, use the `book`, `chapter` and `verse` fields with the English book name, or simply import the notes unattached and place them by hand later."),
   ("Can I get my notes back out again?",
    "Yes — Export Markdown in the same screen writes every note to a .md file with the same fields, so notes can travel out of JW Library and back in without losing where they belong."),
  ],
  "related": ["export-jw-library-notes", "edit-jw-library-notes", "merge-jw-library-backups"],
 },
'''

ANCHOR = '''
 {
  "slug": "export-jw-library-notes",'''


def main():
    c = io.open(BUILD, encoding="utf-8").read()
    if "import-markdown-notes-jw-library" in c:
        print("build_guides.py: already added")
        return
    if c.count(ANCHOR) != 1:
        sys.exit("ABORT build_guides.py: export guide anchor x%d" % c.count(ANCHOR))
    c = c.replace(ANCHOR, GUIDE.rstrip("\n") + ANCHOR, 1)
    io.open(BUILD, "w", encoding="utf-8").write(c)
    print("build_guides.py: import-markdown-notes-jw-library added")


if __name__ == "__main__":
    main()

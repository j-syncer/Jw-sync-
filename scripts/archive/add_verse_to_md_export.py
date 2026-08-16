#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_verse_to_md_export.py — put the verse in the Markdown front matter.

Asked for on the community forum: notes exported to Markdown carry
"publication: Matthew 26", never "publication: Matthew 26:14".

pubLabel() builds that line out of Location.BookNumber and
Location.ChapterNumber, and a Bible Location carries nothing finer than the
chapter — so the verse looked absent. It is not: it sits on the note itself
(BlockType 2, BlockIdentifier = the verse), and for a note attached to a
highlight it sits on the highlight's BlockRange rows, which span a range when
the highlight spans several verses. hydrateFromDb simply never selected those
columns.

So this adds them to the query, adds pubRef()/verseRange() beside pubLabel(),
and points the front matter at pubRef(). The Explorer's own labels keep using
pubLabel(): the list reads better grouped by chapter, and the export is where
the precision was asked for.

Notes in publications keep the publication name — a Watchtower paragraph has
no verse — and a note placed on a chapter rather than a verse keeps
"Matthew 26".

Idempotent; mirrors js/ to beta/js/ as 15_parity.js requires.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUERY_OLD = (
    '        "SELECT n.NoteId, n.LocationId, n.UserMarkId, n.Title, n.Content, n.LastModified, n.Guid, " +\n'
    '        "l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol, " +\n'
    '        "u.ColorIndex " +\n'
    '        "FROM Note n " +\n'
)
QUERY_NEW = (
    '        "SELECT n.NoteId, n.LocationId, n.UserMarkId, n.Title, n.Content, n.LastModified, n.Guid, " +\n'
    '        "n.BlockType, n.BlockIdentifier, " +\n'
    '        "l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol, " +\n'
    '        "u.ColorIndex, br.BrFirst, br.BrLast " +\n'
    '        "FROM Note n " +\n'
)

# The verse range comes from the highlight's BlockRange rows. Grouped once and
# joined rather than run as a correlated subquery per note: a large library has
# thousands of each.
JOIN_OLD = (
    '        "LEFT JOIN UserMark u ON n.UserMarkId = u.UserMarkId " +\n'
    '        "ORDER BY n.LastModified DESC"'
)
JOIN_NEW = (
    '        "LEFT JOIN UserMark u ON n.UserMarkId = u.UserMarkId " +\n'
    '        // A highlight can span several verses, so the note anchored to it\n'
    '        // covers the range its BlockRange rows describe. Grouped once and\n'
    '        // joined rather than run as a correlated subquery per note: a large\n'
    '        // library has thousands of each.\n'
    '        "LEFT JOIN (SELECT UserMarkId, MIN(Identifier) AS BrFirst, MAX(Identifier) AS BrLast " +\n'
    '        "           FROM BlockRange GROUP BY UserMarkId) br ON br.UserMarkId = n.UserMarkId " +\n'
    '        "ORDER BY n.LastModified DESC"'
)

HELPER_ANCHOR = """  function fmtDate(s){"""

HELPER = """  // The verse a Bible note sits on. A Bible Location stops at the chapter, so
  // pubLabel() can only ever say "Matthew 26"; the verse is on the note
  // (BlockType 2, BlockIdentifier) or on the BlockRange rows of the highlight
  // it is attached to, which span a range when the highlight does.
  function verseRange(row){
    if(!row) return null;
    var bn = row.BookNumber;
    // Publications are numbered by paragraph, not by verse.
    if(!(bn >= 1 && bn <= 66) || !row.ChapterNumber) return null;
    var lo = null, hi = null;
    if(row.BlockIdentifier != null && row.BlockIdentifier >= 1){ lo = hi = row.BlockIdentifier; }
    if(row.BrFirst != null && row.BrFirst >= 1){
      lo = (lo == null) ? row.BrFirst : Math.min(lo, row.BrFirst);
      hi = (hi == null) ? row.BrLast  : Math.max(hi, row.BrLast);
    }
    if(lo == null) return null;              // a note on the chapter as a whole
    return (hi != null && hi > lo) ? (lo + '-' + hi) : ('' + lo);
  }
  // pubLabel() with the verse appended where there is one. The Explorer's own
  // labels stay at chapter level — grouping a list by "Matthew 26" reads
  // better than by 30 separate verses — so this is used by the export.
  function pubRef(row){
    var base = pubLabel(row);
    if(!base) return '';
    var v = verseRange(row);
    return v ? (base + ':' + v) : base;
  }
"""

FM_OLD = """    var pub=pubLabel(n); if(pub) fm+='publication: '+pub.replace(/\\n/g,' ')+'\\n';
    fm+='---\\n\\n';"""

FM_NEW = """    var pub=pubRef(n); if(pub) fm+='publication: '+pub.replace(/\\n/g,' ')+'\\n';
    // Discrete fields as well as the readable line: Markdown editors query
    // front matter, and an importer reading these back can place the note
    // exactly where it came from.
    var bn=n.BookNumber;
    if(bn>=1&&bn<=66){
      fm+='book: '+(BIBLE[bn-1]||('Book '+bn))+'\\n';
      if(n.ChapterNumber) fm+='chapter: '+n.ChapterNumber+'\\n';
      var vr=verseRange(n); if(vr) fm+='verse: '+vr+'\\n';
    }
    fm+='---\\n\\n';"""


def patch(path):
    c = io.open(path, encoding="utf-8").read()
    orig = c

    if "br.BrFirst" not in c:
        if c.count(QUERY_OLD) != 1:
            sys.exit("ABORT %s: note query anchor x%d" % (path, c.count(QUERY_OLD)))
        c = c.replace(QUERY_OLD, QUERY_NEW, 1)
        if c.count(JOIN_OLD) != 1:
            sys.exit("ABORT %s: note join anchor x%d" % (path, c.count(JOIN_OLD)))
        c = c.replace(JOIN_OLD, JOIN_NEW, 1)

    if "function pubRef(" not in c:
        if c.count(HELPER_ANCHOR) != 1:
            sys.exit("ABORT %s: fmtDate anchor x%d" % (path, c.count(HELPER_ANCHOR)))
        c = c.replace(HELPER_ANCHOR, HELPER + HELPER_ANCHOR, 1)

    if "var pub=pubRef(n)" not in c:
        if c.count(FM_OLD) != 1:
            sys.exit("ABORT %s: front matter anchor x%d" % (path, c.count(FM_OLD)))
        c = c.replace(FM_OLD, FM_NEW, 1)

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("%s: verse wired into the Markdown export" % os.path.relpath(path, REPO))
    else:
        print("%s: already patched" % os.path.relpath(path, REPO))
    return c


if __name__ == "__main__":
    src = patch(os.path.join(REPO, "js", "browse.js"))
    # Shared tool-layer file: both sites ship the same copy.
    io.open(os.path.join(REPO, "beta", "js", "browse.js"), "w", encoding="utf-8").write(src)
    print("beta/js/browse.js: mirrored")

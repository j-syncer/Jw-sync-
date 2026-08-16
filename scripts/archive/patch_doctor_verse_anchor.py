# -*- coding: utf-8 -*-
"""Library Doctor (v2.63.3) — duplicate-note safety fix.

A note's duplicate criteria now include its anchor (BlockType +
BlockIdentifier) so identical text on DIFFERENT verses/paragraphs of the
same chapter is never treated as a duplicate. The kept copy prefers the
one linked to a highlight (UserMarkId), and tag assignments on the
removed copy are migrated to the kept copy instead of being dropped.
"""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

# 1) Shared duplicate-note pair finder, inserted before the Health checks block
OLD1 = "  // ── Health checks ─"
must(c.count(OLD1) == 1, 'health-checks anchor not unique: %d' % c.count(OLD1))

HELPER = r"""  // Two notes are duplicates only when BOTH the text AND the anchor match:
  // same Title, Content, Location, BlockType and BlockIdentifier. Identical
  // text on a different verse/paragraph of the same chapter is NOT a
  // duplicate. The kept copy prefers the one linked to a highlight.
  function dupNotePairs(db){
    if(!hasTable(db,'Note')) return [];
    var bt=hasCol(db,'Note','BlockType')?'IFNULL(BlockType,-1)':'-1',
        bi=hasCol(db,'Note','BlockIdentifier')?'IFNULL(BlockIdentifier,-1)':'-1',
        btN=hasCol(db,'Note','BlockType')?'IFNULL(n.BlockType,-1)':'-1',
        biN=hasCol(db,'Note','BlockIdentifier')?'IFNULL(n.BlockIdentifier,-1)':'-1',
        keep=hasCol(db,'Note','UserMarkId')
          ? 'COALESCE(MIN(CASE WHEN UserMarkId IS NOT NULL THEN NoteId END),MIN(NoteId))'
          : 'MIN(NoteId)';
    return q(db,
      "SELECT n.NoteId AS dup, g.keepId AS keep FROM Note n JOIN ("+
      " SELECT IFNULL(Title,'') AS t, IFNULL(Content,'') AS c, IFNULL(LocationId,-1) AS l, "+bt+" AS bt, "+bi+" AS bi, "+keep+" AS keepId"+
      " FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'')"+
      " GROUP BY t, c, l, bt, bi HAVING COUNT(*)>1) g"+
      " ON IFNULL(n.Title,'')=g.t AND IFNULL(n.Content,'')=g.c AND IFNULL(n.LocationId,-1)=g.l AND "+btN+"=g.bt AND "+biN+"=g.bi"+
      " WHERE n.NoteId<>g.keepId");
  }

"""
c = c.replace(OLD1, HELPER + OLD1, 1)

# 2) dup_notes detection delegates to the pair finder
OLD2 = """      case 'dup_notes':
        if(!hasTable(db,'Note')) return [];
        return col1(db,
          "SELECT NoteId FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'') AND NoteId NOT IN ("+
          " SELECT MIN(NoteId) FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'')"+
          " GROUP BY IFNULL(Title,''), IFNULL(Content,''), IFNULL(LocationId,-1))");"""
must(c.count(OLD2) == 1, 'dup_notes case not unique: %d' % c.count(OLD2))
NEW2 = """      case 'dup_notes':
        return dupNotePairs(db).map(function(r){ return r.dup; });"""
c = c.replace(OLD2, NEW2, 1)

# 3) applyFixes: migrate the removed copy's tags to the kept copy first
OLD3 = "    var dn=idsFor(db,'dup_notes');   delNotes(db,dn); fixed.dup_notes=dn.length;"
must(c.count(OLD3) == 1, 'applyFixes dup_notes line not unique: %d' % c.count(OLD3))
NEW3 = """    var pairs=dupNotePairs(db);
    if(hasTable(db,'TagMap')) pairs.forEach(function(p){
      // keep tag assignments: move the removed copy's tags onto the kept copy
      db.run('UPDATE TagMap SET NoteId='+p.keep+' WHERE NoteId='+p.dup+
             ' AND TagId IS NOT NULL AND TagId NOT IN (SELECT TagId FROM TagMap WHERE NoteId='+p.keep+' AND TagId IS NOT NULL)');
    });
    var dn=pairs.map(function(p){ return p.dup; }); delNotes(db,dn); fixed.dup_notes=dn.length;"""
c = c.replace(OLD3, NEW3, 1)

# 4) version bump
OLD4 = '"softwareVersion": "2.63.2"'
must(c.count(OLD4) == 1, 'softwareVersion anchor not unique: %d' % c.count(OLD4))
c = c.replace(OLD4, '"softwareVersion": "2.63.3"', 1)

io.open(f, 'w', encoding='utf-8').write(c)
print('OK: beta/index.html patched')

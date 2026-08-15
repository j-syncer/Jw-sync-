#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harden_md_import.py — make the Markdown importer forgiving, and make it ask.

The first cut of the importer read exactly the front matter this site writes.
That is fine for a round trip and no use at all for a file someone typed: a
missing space, "Mathew", "Matt 26:39", tags on their own lines, or no `---`
fences and the whole reference is dropped on the floor without a word — which
is the same class of failure as a silently refused backup, just at the other
end of the pipe.

Two changes:

  1. The parser now reads what people actually write. Keys are matched
     case-insensitively with aliases (pub/ref/reference/scripture for
     publication, v/vs/verses for verse, and so on), YAML block lists are
     understood, front matter without fences is recognised when it looks like
     front matter, and book names are matched through an abbreviation table and
     then — only if that fails — by edit distance, so "Mathew" and "Ecclesiates"
     resolve.

  2. Nothing uncertain happens quietly. A reference that had to be guessed, or
     one naming a book we cannot recognise, is listed in the preview with what
     we made of it and a tick box. The reader confirms or drops it before a
     single row is written.

The rule behind both: be liberal about what a file may look like, and never be
liberal about where a note ends up. Anything we are not sure of is a question,
not an assumption.

Idempotent; mirrors js/ to beta/js/ as 15_parity.js requires.
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def match_brace(s, i):
    depth = 0
    while i < len(s):
        ch = s[i]
        if ch in "\"'":
            q = ch
            i += 1
            while i < len(s):
                if s[i] == "\\":
                    i += 2
                    continue
                if s[i] == q:
                    break
                i += 1
        elif ch == "/" and s[i + 1:i + 2] == "/":
            while i < len(s) and s[i] != "\n":
                i += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def replace_fn(src, name, new_text):
    """Replace `function <name>(...){...}` wholesale.

    Brace-counting is no use here — these bodies are full of regex literals
    carrying {3,} and apostrophes inside character classes, which no naive
    scanner tells apart from code. The module is uniformly two-space indented,
    so the function ends at the first line that is exactly "  }".
    """
    m = re.search(r"\n  function " + re.escape(name) + r"\s*\(", src)
    if not m:
        sys.exit("ABORT: function %s not found" % name)
    end = src.find("\n  }\n", m.end())
    if end < 0:
        sys.exit("ABORT: no closing line for %s" % name)
    return src[:m.start() + 1] + new_text + src[end + len("\n  }\n"):]


# ── the parser ──────────────────────────────────────────────────────────────

PARSE_FRONT_MATTER = r'''  // Front matter as people actually write it. The fences may be missing, the
  // keys may be capitalised or spelled a little differently, the space after
  // the colon may not be there, and a list may be inline or on its own lines.
  // None of that is a reason to lose someone's note.
  function parseFrontMatter(text){
    var s=String(text||'').replace(/^﻿/,'').replace(/\r\n/g,'\n');
    var lines, rest;
    var fenced=/^\s*\n?(-{3,}|_{3,})[ \t]*\n([\s\S]*?)\n[ \t]*(-{3,}|\.{3}|_{3,})[ \t]*(\n|$)/.exec(s);
    if(fenced){
      lines=fenced[2].split('\n');
      rest=s.slice(fenced[0].length);
    } else {
      // No fences. Treat leading "key: value" lines as front matter, but only
      // while they keep looking like one — a note that opens with a sentence
      // containing a colon must not lose its first paragraph.
      var all=s.split('\n'), take=0, first=true;
      for(var i=0;i<all.length;i++){
        var ln=all[i];
        if(!ln.trim()){ if(take) break; else continue; }
        var col=ln.indexOf(':');
        if(col<1) break;
        // The first line has to be a field we recognise. Without that rule an
        // ordinary opening sentence containing a colon — "A sentence: with a
        // colon" — gets swallowed as front matter and the note loses it.
        if(first){
          if(!canonKey(ln.slice(0,col))) break;
          first=false;
        } else if(!/^[ \t]*[A-Za-z][A-Za-z0-9 _-]{0,24}:[ \t]*\S?/.test(ln)) break;
        take=i+1;
      }
      if(!take) return { meta:{}, body:s };
      lines=all.slice(0,take);
      rest=all.slice(take).join('\n');
    }
    var meta={}, pendingKey=null, pendingList=null;
    function store(k,v){ if(k && meta[k]===undefined) meta[k]=v; }
    for(var j=0;j<lines.length;j++){
      var line=lines[j];
      var item=/^[ \t]*-[ \t]+(.*)$/.exec(line);
      if(item && pendingKey){                     // a YAML block list under a key
        (pendingList=pendingList||[]).push(unquote(item[1]));
        store(pendingKey, pendingList);
        meta[pendingKey]=pendingList;
        continue;
      }
      var c=line.indexOf(':');
      if(c<1){ continue; }
      var rawKey=line.slice(0,c), val=line.slice(c+1).trim();
      var key=canonKey(rawKey);
      if(!key) continue;
      pendingKey=null; pendingList=null;
      if(val===''){ pendingKey=key; continue; }   // value may follow as a list
      store(key, unquote(val));
    }
    return { meta:meta, body:rest };
  }
'''

CANON_KEY = r'''  // "Publication", " pub ", "Bible reference" and "scripture" all mean the same
  // thing to someone writing a note; only one of them means anything to us.
  var KEY_ALIASES={
    title:'title', name:'title', heading:'title', subject:'title',
    tags:'tags', tag:'tags', keywords:'tags', keyword:'tags', categories:'tags',
    category:'tags', labels:'tags', label:'tags', topics:'tags', topic:'tags',
    date:'date', created:'date', modified:'date', lastmodified:'date', day:'date',
    publication:'publication', pub:'publication', publications:'publication',
    reference:'publication', ref:'publication', bibleref:'publication',
    biblereference:'publication', scripture:'publication', citation:'publication',
    source:'publication', passage:'publication', versereference:'publication',
    book:'book', biblebook:'book', bookname:'book',
    chapter:'chapter', chap:'chapter', ch:'chapter',
    verse:'verse', verses:'verse', v:'verse', vs:'verse', vv:'verse'
  };
  function canonKey(raw){
    var k=String(raw||'').toLowerCase().replace(/[^a-z0-9]/g,'');
    return KEY_ALIASES[k]||null;
  }
  function unquote(v){
    var s=String(v==null?'':v).trim();
    // A trailing "# ..." is a YAML comment — unless the value is a hashtag
    // list, which is how plenty of people write tags.
    if(s.charAt(0)!=='#') s=s.replace(/\s+#.*$/,'');
    if(/^\[[\s\S]*\]$/.test(s)) return splitList(s.slice(1,-1));
    var q=/^(["'])([\s\S]*)\1$/.exec(s);
    return q?q[2]:s;
  }
  function splitList(s){
    var raw=String(s||'').trim();
    if(!raw) return [];
    // "#study #greek" is a tag list too, but only when there are no commas.
    var parts=(raw.indexOf('#')>=0 && raw.indexOf(',')<0 && raw.indexOf(';')<0)
      ? raw.split('#') : raw.split(/[,;]/);
    return parts.map(function(p){
      return String(p).trim().replace(/^(["'#])|(["'])$/g,'').trim();
    }).filter(Boolean);
  }
  function asList(v){
    if(Array.isArray(v)) return v.filter(Boolean);
    if(v==null||v==='') return [];
    return splitList(String(v));
  }
'''

BOOKS = r'''  // Abbreviations people actually type. Everything is compared after
  // normalisation (lower case, punctuation dropped, "1st"/"I"/"first" folded to
  // "1"), so one entry covers "1 Cor.", "1Cor", "I Corinthians" and so on.
  var BOOK_ABBR={
    'gen':1,'ge':1,'gn':1, 'ex':2,'exo':2,'exod':2, 'lev':3,'le':3,'lv':3,
    'num':4,'nu':4,'nm':4, 'deut':5,'de':5,'dt':5, 'josh':6,'jos':6,
    'judg':7,'jdg':7,'jg':7, 'ruth':8,'ru':8, '1sam':9,'1sa':9,'1sm':9,
    '2sam':10,'2sa':10,'2sm':10, '1kings':11,'1ki':11,'1kg':11,'1kgs':11,
    '2kings':12,'2ki':12,'2kg':12,'2kgs':12, '1chron':13,'1ch':13,'1chr':13,
    '2chron':14,'2ch':14,'2chr':14, 'ezra':15,'ezr':15, 'neh':16,'ne':16,
    'esth':17,'est':17,'es':17, 'job':18,'jb':18, 'ps':19,'psa':19,'psalm':19,
    'psalms':19,'pss':19, 'prov':20,'pr':20,'prv':20, 'eccl':21,'ec':21,'ecc':21,
    'song':22,'sos':22,'songofsongs':22,'canticles':22,'ca':22,
    'isa':23,'is':23, 'jer':24,'je':24, 'lam':25,'la':25, 'ezek':26,'eze':26,'ezk':26,
    'dan':27,'da':27,'dn':27, 'hos':28,'ho':28, 'joel':29,'joe':29,'jl':29,
    'amos':30,'am':30, 'obad':31,'ob':31, 'jonah':32,'jon':32, 'mic':33,'mi':33,
    'nah':34,'na':34, 'hab':35,'hb':35, 'zeph':36,'zep':36,'zp':36,
    'hag':37,'hg':37, 'zech':38,'zec':38,'zc':38, 'mal':39,'ml':39,
    'matt':40,'mt':40,'mat':40, 'mark':41,'mk':41,'mr':41, 'luke':42,'lk':42,'lu':42,
    'john':43,'jn':43,'joh':43, 'acts':44,'ac':44, 'rom':45,'ro':45,'rm':45,
    '1cor':46,'1co':46, '2cor':47,'2co':47, 'gal':48,'ga':48, 'eph':49,'ep':49,
    'phil':50,'php':50,'pp':50, 'col':51,'cl':51, '1thess':52,'1th':52,
    '2thess':53,'2th':53, '1tim':54,'1ti':54,'1tm':54, '2tim':55,'2ti':55,'2tm':55,
    'titus':56,'tit':56,'ti':56, 'philem':57,'phm':57,'pm':57, 'heb':58,'hb2':58,
    'jas':59,'jam':59,'jm':59, '1pet':60,'1pe':60,'1pt':60, '2pet':61,'2pe':61,'2pt':61,
    '1john':62,'1jn':62,'1jo':62, '2john':63,'2jn':63,'2jo':63, '3john':64,'3jn':64,'3jo':64,
    'jude':65,'jud':65, 'rev':66,'re':66,'rv':66,'revelations':66,'apocalypse':66
  };
  var BOOK_LOOKUP=null;
  function normBook(s){
    return String(s||'')
      .toLowerCase()
      .replace(/[’']/g,'')
      .replace(/^\s*(first|1st|i)\s+/,'1 ')
      .replace(/^\s*(second|2nd|ii)\s+/,'2 ')
      .replace(/^\s*(third|3rd|iii)\s+/,'3 ')
      .replace(/[^a-z0-9]/g,'');
  }
  function bookLookup(){
    if(BOOK_LOOKUP) return BOOK_LOOKUP;
    BOOK_LOOKUP={};
    BIBLE.forEach(function(b,i){ BOOK_LOOKUP[normBook(b)]=i+1; });
    Object.keys(BOOK_ABBR).forEach(function(k){
      if(BOOK_LOOKUP[normBook(k)]===undefined) BOOK_LOOKUP[normBook(k)]=BOOK_ABBR[k];
    });
    return BOOK_LOOKUP;
  }
  function editDistance(a,b){
    var m=a.length, n=b.length, prev=[], cur=[], i, j;
    if(Math.abs(m-n)>2) return 3;                 // we only care about <=2
    for(j=0;j<=n;j++) prev[j]=j;
    for(i=1;i<=m;i++){
      cur[0]=i;
      for(j=1;j<=n;j++){
        cur[j]=Math.min(prev[j]+1, cur[j-1]+1, prev[j-1]+(a.charAt(i-1)===b.charAt(j-1)?0:1));
      }
      for(j=0;j<=n;j++) prev[j]=cur[j];
    }
    return prev[n];
  }
  /**
   * @returns {number|{book:number,guessed:true}|0}
   * A near-miss resolves, but it comes back flagged so the reader is asked
   * before it is used. Silently correcting someone's spelling is how a note
   * ends up in a book they never opened.
   */
  function bookNumberFromName(name){
    var key=normBook(name);
    if(!key) return 0;
    var table=bookLookup();
    if(table[key]!==undefined) return table[key];
    // Numbered books must keep their number: "1 John" is never "2 John".
    var lead=/^([123])/.exec(key), best=0, bestD=3, ties=0;
    Object.keys(table).forEach(function(cand){
      var candLead=/^([123])/.exec(cand);
      if((lead?lead[1]:'')!==(candLead?candLead[1]:'')) return;
      if(Math.abs(cand.length-key.length)>2) return;
      if(key.length<4 || cand.length<4) return;   // "ge" vs "je" is not a typo
      var d=editDistance(key,cand);
      if(d<bestD){ bestD=d; best=table[cand]; ties=1; }
      else if(d===bestD && table[cand]!==best){ ties++; }
    });
    if(best && bestD<=2 && ties===1) return { book:best, guessed:true };
    return 0;
  }
'''

PARSE_REFERENCE = r'''  /**
   * Work out which verse a note belongs to, from discrete fields or from a
   * free-text line like "Matt. 26:39-41", "1 Cor 13 v4" or "John 3.16".
   * @returns null | {book, chapter, verse, guessed, label, raw}
   */
  function parseReference(meta){
    var book=meta.book, chapter=meta.chapter, verse=meta.verse, guessed=false;
    var raw=(meta.publication!=null?String(meta.publication):'').trim();
    if(book==null || book==='' || chapter==null || chapter===''){
      if(raw){
        // Book name, then chapter, then an optional verse after : . , or "v".
        var m=/^\s*((?:[123]\s*)?[A-Za-z][A-Za-z.'’\s]*?)\s*(\d{1,3})\s*(?:[:.,]|\s+vv?\.?\s*|\s+verse[s]?\s*)\s*(\d{1,3})/.exec(raw);
        if(!m) m=/^\s*((?:[123]\s*)?[A-Za-z][A-Za-z.'’\s]*?)\s*(\d{1,3})\s*$/.exec(raw);
        if(m){
          if(book==null||book==='') book=m[1];
          if(chapter==null||chapter==='') chapter=m[2];
          if((verse==null||verse==='') && m[3]) verse=m[3];
        } else {
          // It does not have the shape of a scripture reference at all, so it
          // is a publication name — "The Watchtower—2023 No. 4" is exactly what
          // this site writes for a note in an article. Those are ordinary
          // notes, not something to question the reader about.
          return null;
        }
      }
    }
    if(book==null||book==='') return null;        // a publication note, not a verse
    var hit=bookNumberFromName(book), bn=0;
    if(typeof hit==='object' && hit){ bn=hit.book; guessed=true; }
    else bn=hit||0;
    var label=String(raw||(book+(chapter?' '+chapter:'')+(verse?':'+verse:''))).trim();
    if(!bn) return { book:0, chapter:0, verse:null, guessed:false, unknown:true,
                     raw:label, label:label };
    var ch=parseInt(String(chapter).replace(/[^0-9]/g,''),10);
    if(!(ch>=1)) return { book:bn, chapter:0, verse:null, guessed:guessed, unknown:true,
                          raw:label, label:label };
    var vs=null, vm=/(\d{1,3})/.exec(String(verse==null?'':verse));
    if(vm) vs=parseInt(vm[1],10);
    if(!(vs>=1)) vs=null;
    return { book:bn, chapter:ch, verse:vs, guessed:guessed, unknown:false, raw:label,
             label:(BIBLE[bn-1]||('Book '+bn))+' '+ch+(vs?(':'+vs):'') };
  }
'''

MD_FILE_TO_NOTE = r'''  function mdFileToNote(name, text){
    var fm=parseFrontMatter(text);
    var meta=fm.meta||{};
    var title=(typeof meta.title==='string'&&meta.title.trim())?meta.title.trim():'';
    if(!title){
      var h=/^#{1,6}\s+(.+)$/m.exec(fm.body||'');
      title=h?h[1].trim():String(name||'').replace(/\.(md|markdown|txt)$/i,'')
        .replace(/^\d+[-_ ]/,'').replace(/[-_]+/g,' ').trim();
    }
    var date=null;
    var dm=/(\d{4})-(\d{2})-(\d{2})/.exec(String(meta.date==null?'':meta.date));
    if(dm) date=dm[0]+' 00:00:00';
    return { title:title, content:sanitizeNoteHtml(mdBodyToNoteHtml(fm.body,title)),
             tags:asList(meta.tags), date:date, ref:parseReference(meta), file:name };
  }
'''


def patch_browse():
    path = os.path.join(REPO, "js", "browse.js")
    c = io.open(path, encoding="utf-8").read()
    orig = c

    # Order matters: the replacements go first, while the old definitions are
    # still the only ones in the file. Inserting the new helpers first would
    # put a second bookNumberFromName *above* the old one, and the deletion
    # below would take out the new one.
    if "KEY_ALIASES" not in c:
        c = replace_fn(c, "parseFrontMatter", PARSE_FRONT_MATTER)
        c = replace_fn(c, "bookNumberFromName", "")   # superseded by the one in BOOKS
        c = replace_fn(c, "parseReference", PARSE_REFERENCE)
        c = replace_fn(c, "mdFileToNote", MD_FILE_TO_NOTE)
        c = c.replace("  var BIBLE_BY_NAME=null;\n", "")

        anchor = "  // ---------- Markdown import ----------"
        if c.count(anchor) != 1:
            sys.exit("ABORT browse.js: import section anchor x%d" % c.count(anchor))
        c = c.replace(anchor, anchor + "\n" + CANON_KEY + BOOKS, 1)

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("js/browse.js: parser hardened")
    else:
        print("js/browse.js: already patched")
    return c


if __name__ == "__main__":
    src = patch_browse()
    io.open(os.path.join(REPO, "beta", "js", "browse.js"), "w", encoding="utf-8").write(src)
    print("beta/js/browse.js: mirrored")

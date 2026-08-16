#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_md_import_review.py — ask before placing anything we had to interpret.

The parser now resolves "Mathew 26:39" and "Matt. 26:39" and a file with no
fences at all. That is only half of being foolproof: the other half is never
acting on a reading we are not sure of. A note that lands on the wrong verse
looks completely fine on this site — the mistake only shows up later, in the
app, on a verse the reader never opened.

So the preview now separates what it is sure about from what it is not:

  * confident references are counted;
  * a reference that resolved only by edit distance ("Mathew" → Matthew), and
    one naming a book we cannot recognise at all, are listed one per line with
    what we made of them and a tick box;
  * unticked rows are not imported; a ticked unrecognised one comes in as a
    standalone note rather than being forced onto a guess.

Two safety bugs fixed at the same time:

  * the preview called resolveBibleLocationId(), which *creates* a Location row
    when the backup has none for that chapter — so merely looking at a file
    wrote to the database. Preview is now strictly read-only.
  * a reference with book 0 (unrecognised) was passed to the same function,
    which would have looked up, and could have created, a Location with
    BookNumber 0. Anchoring now requires a real book and chapter.

Idempotent; mirrors js/ to beta/js/ as 15_parity.js requires.
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BROWSE = os.path.join(REPO, "js", "browse.js")

KEYS = ["mdi_check", "mdi_read_as", "mdi_no_book", "mdi_untick"]

STRINGS = {
"en": ["Check these before importing", "read as {ref}",
 "book not recognised — will be added as a standalone note",
 "Untick anything you would rather leave out."],
"es": ["Revisa esto antes de importar", "se ha leído como {ref}",
 "libro no reconocido — se añadirá como nota suelta",
 "Desmarca lo que prefieras dejar fuera."],
"pt": ["Confira isto antes de importar", "lido como {ref}",
 "livro não reconhecido — será adicionado como nota avulsa",
 "Desmarque o que preferir deixar de fora."],
"fr": ["Vérifiez ceci avant d'importer", "lu comme {ref}",
 "livre non reconnu — sera ajouté comme note libre",
 "Décochez ce que vous préférez laisser de côté."],
"de": ["Bitte vor dem Import prüfen", "gelesen als {ref}",
 "Buch nicht erkannt — wird als freie Notiz hinzugefügt",
 "Hake ab, was nicht mitkommen soll."],
"it": ["Controlla prima di importare", "letto come {ref}",
 "libro non riconosciuto — sarà aggiunto come nota libera",
 "Deseleziona ciò che preferisci lasciare fuori."],
"ru": ["Проверьте это перед импортом", "прочитано как {ref}",
 "книга не распознана — будет добавлено как отдельная заметка",
 "Снимите отметку с того, что не нужно импортировать."],
"ja": ["読み込む前に確認してください", "{ref} と解釈しました",
 "書名を判別できません — 単独のノートとして追加されます",
 "取り込みたくないものはチェックを外してください。"],
"ko": ["가져오기 전에 확인하세요", "{ref} (으)로 읽었습니다",
 "책 이름을 알아보지 못했습니다 — 독립 노트로 추가됩니다",
 "가져오지 않을 항목은 체크를 해제하세요."],
"tl": ["Suriin ito bago mag-import", "binasa bilang {ref}",
 "hindi nakilala ang aklat — idadagdag bilang malayang tala",
 "Alisan ng tsek ang ayaw mong isama."],
"sv": ["Kontrollera detta före import", "tolkat som {ref}",
 "boken känns inte igen — läggs till som fristående anteckning",
 "Avmarkera det du hellre vill utelämna."],
"ceb": ["Susiha kini una mag-import", "gibasa isip {ref}",
 "wala mailhi ang libro — idugang isip nagbarog nga nota",
 "Tangtangi ang tsek sa dili nimo gusto iapil."],
"nl": ["Controleer dit vóór het importeren", "gelezen als {ref}",
 "boek niet herkend — wordt als losse notitie toegevoegd",
 "Vink uit wat je liever weglaat."],
"ro": ["Verifică înainte de import", "citit ca {ref}",
 "cartea nu a fost recunoscută — va fi adăugată ca notiță de sine stătătoare",
 "Debifează ce preferi să lași deoparte."],
"id": ["Periksa ini sebelum mengimpor", "dibaca sebagai {ref}",
 "kitab tidak dikenali — akan ditambahkan sebagai catatan lepas",
 "Hapus centang pada yang tidak ingin diimpor."],
"hi": ["आयात करने से पहले इन्हें जाँचें", "{ref} के रूप में पढ़ा गया",
 "पुस्तक पहचानी नहीं गई — अलग नोट के रूप में जुड़ेगा",
 "जो नहीं चाहिए उसका निशान हटा दें।"],
"hu": ["Ellenőrizd ezeket importálás előtt", "így értelmeztük: {ref}",
 "a könyv nem ismerhető fel — önálló jegyzetként kerül be",
 "Vedd ki a pipát arról, amit inkább kihagynál."],
"vi": ["Hãy kiểm tra trước khi nhập", "được đọc là {ref}",
 "không nhận ra tên sách — sẽ được thêm dưới dạng ghi chú rời",
 "Bỏ chọn những mục bạn không muốn nhập."],
"yue-Hant": ["匯入之前請檢查", "讀作 {ref}",
 "認唔到書卷 — 會加做獨立筆記",
 "唔想要嘅就撳走個剔。"],
"zh-Hant": ["匯入前請先確認", "讀作 {ref}",
 "無法辨識書卷 — 將以獨立筆記加入",
 "不想匯入的請取消勾選。"],
"zh-Hans": ["导入前请先确认", "读作 {ref}",
 "无法识别书卷 — 将以独立笔记加入",
 "不想导入的请取消勾选。"],
"pl": ["Sprawdź to przed importem", "odczytano jako {ref}",
 "nie rozpoznano księgi — zostanie dodana jako notatka samodzielna",
 "Odznacz to, czego wolisz nie importować."],
"uk": ["Перевірте це перед імпортом", "прочитано як {ref}",
 "книгу не розпізнано — буде додано як окрему нотатку",
 "Зніміть позначку з того, чого не треба імпортувати."],
"he": ["בדקו את אלה לפני הייבוא", "נקרא כ-{ref}",
 "הספר לא זוהה — יתווסף כהערה עצמאית",
 "הסירו את הסימון ממה שעדיף להשאיר בחוץ."],
"ar": ["راجع هذه قبل الاستيراد", "قُرئت على أنها {ref}",
 "السفر غير معروف — ستُضاف كملاحظة مستقلة",
 "أزل العلامة عمّا لا تريد استيراده."],
}


def js_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


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
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def add_strings(c):
    if "mdi_check:" in c:
        print("  strings: already present")
        return c
    m = re.search(r"\bI18N\s*=\s*\{", c)
    start = m.end() - 1
    end = match_brace(c, start)
    body = c[start + 1:end]
    out, pos, seen = [], 0, []
    while pos < len(body):
        km = re.compile(r'[\s,]*("?[\w-]+"?)\s*:\s*\{').match(body, pos)
        if not km:
            break
        lang = km.group(1).strip('"')
        s = body.index("{", km.end() - 1)
        e = match_brace(body, s)
        if lang not in STRINGS:
            sys.exit("ABORT: no translations for %r" % lang)
        add = ",".join(k + ":" + js_str(v) for k, v in zip(KEYS, STRINGS[lang]))
        out.append(body[pos:e])
        out.append("," + add + "}")
        seen.append(lang)
        pos = e + 1
    out.append(body[pos:])
    missing = set(STRINGS) - set(seen)
    if missing:
        sys.exit("ABORT: languages not found: %s" % ", ".join(sorted(missing)))
    print("  strings: %d keys x %d languages" % (len(KEYS), len(seen)))
    return c[:start + 1] + "".join(out) + c[end:]


# ── read-only lookup + a guard on unrecognised books ────────────────────────

RESOLVE_OLD = """  function resolveBibleLocationId(bookNumber, chapter, cache){
    var key=bookNumber+':'+chapter;
    if(cache && key in cache) return cache[key];
    var id=null;
    try{"""
RESOLVE_NEW = """  function resolveBibleLocationId(bookNumber, chapter, cache, create){
    if(!(bookNumber>=1&&bookNumber<=66)||!(chapter>=1)) return null;
    var key=bookNumber+':'+chapter+(create?'!':'');
    if(cache && key in cache) return cache[key];
    var id=null;
    try{"""

CREATE_OLD = """      if(hit.length){ id=hit[0].LocationId; }
      else {"""
CREATE_NEW = """      if(hit.length){ id=hit[0].LocationId; }
      // Preview must never write. It asks whether a chapter *could* be
      // anchored; only the import itself creates the row.
      else if(!create){ id=hasBibleTemplate()?0:null; }
      else {"""

TEMPLATE_HELPER = """  // Does this backup contain any Bible location we could copy the identity
  // columns from? Without one, a verse reference cannot be honoured at all.
  var BIBLE_TEMPLATE=null;
  function hasBibleTemplate(){
    if(BIBLE_TEMPLATE!==null) return BIBLE_TEMPLATE;
    try{
      var r=rowsFromExec(state.db,'SELECT LocationId FROM Location WHERE BookNumber IS NOT NULL'+
        ' AND ChapterNumber IS NOT NULL LIMIT 1');
      BIBLE_TEMPLATE=!!r.length;
    }catch(e){ BIBLE_TEMPLATE=false; }
    return BIBLE_TEMPLATE;
  }
"""

IMPORT_OLD = """          var locId=it.ref?resolveBibleLocationId(it.ref.book,it.ref.chapter,cache):null;"""
IMPORT_NEW = """          // Anchor only on a reference we actually resolved. Anything the
          // reader was asked about arrives here already decided.
          var ref=it.ref;
          var locId=(ref && !ref.unknown && ref.book>=1 && ref.chapter>=1)
            ? resolveBibleLocationId(ref.book, ref.chapter, cache, true) : null;"""

IMPORT_VERSE_OLD = """          var verse=(locId&&it.ref&&it.ref.verse)?it.ref.verse:null;"""
IMPORT_VERSE_NEW = """          var verse=(locId&&ref&&ref.verse)?ref.verse:null;"""

# ── the preview ─────────────────────────────────────────────────────────────

PREVIEW_OLD_START = "    function preview(notes, fileCount){"
PREVIEW_NEW = r'''    function preview(notes, fileCount){
      result.innerHTML='';
      var have=existingNoteKeys(), cache={}, fresh=[], review=[], dupes=0, willAnchor=0;
      notes.forEach(function(it){
        if(!it || (!it.title && !it.content)) return;
        var ref=it.ref;
        var anchorable = ref && !ref.unknown && ref.book>=1 && ref.chapter>=1;
        // Read-only: this asks whether the chapter is already in the backup,
        // and never creates a row to answer.
        var locId = anchorable ? resolveBibleLocationId(ref.book, ref.chapter, cache, false) : null;
        var verse = (anchorable && ref.verse) ? ref.verse : null;
        var key=[String(it.title||''),String(it.content||''),
                 (locId==null?-1:locId),(verse==null?-1:verse)].join('\u0000');
        if(have[key]){ dupes++; return; }
        if(ref && (ref.unknown || ref.guessed)){ review.push(it); return; }
        if(anchorable) willAnchor++;
        fresh.push(it);
      });
      if(!fresh.length && !review.length && !dupes){
        result.innerHTML='<div class="jbs-err">'+htmlEscape(t('mdi_none'))+'</div>'; return;
      }
      var box=document.createElement('div'); box.className='jbs-list';
      function line(txt){ var d=document.createElement('div'); d.className='jbs-list-hdr'; d.textContent=txt; box.appendChild(d); }
      line(t('mdi_found',{n:fresh.length+review.length+dupes, f:fileCount}));
      if(willAnchor) line(t('mdi_anchored',{n:willAnchor}));
      if(fresh.length-willAnchor>0) line(t('mdi_plain',{n:fresh.length-willAnchor}));
      if(dupes) line(t('mdi_dupes',{n:dupes}));
      result.appendChild(box);

      // Anything we had to interpret is a question, not a decision. One row
      // each, ticked by default, saying exactly what we made of it.
      var boxes=[];
      if(review.length){
        var rv=document.createElement('div'); rv.className='jbs-list';
        var hdr=document.createElement('div'); hdr.className='jbs-list-hdr';
        hdr.textContent=t('mdi_check')+' · '+t('mdi_untick');
        rv.appendChild(hdr);
        review.forEach(function(it){
          var row=document.createElement('label'); row.className='jbs-item';
          row.style.cssText='display:flex;gap:8px;align-items:flex-start;cursor:pointer';
          var cb=document.createElement('input'); cb.type='checkbox'; cb.checked=true;
          cb.style.marginTop='3px';
          var txt=document.createElement('div'); txt.style.flex='1';
          var ti=document.createElement('div'); ti.className='jbs-item-title';
          ti.textContent=(it.title&&String(it.title).trim())||it.file||t('no_title');
          var sub=document.createElement('div'); sub.className='jbs-item-sub';
          sub.textContent=it.ref.unknown ? t('mdi_no_book') : t('mdi_read_as',{ref:it.ref.label});
          txt.appendChild(ti); txt.appendChild(sub);
          row.appendChild(cb); row.appendChild(txt);
          rv.appendChild(row);
          boxes.push({cb:cb, it:it});
        });
        result.appendChild(rv);
      }

      var go=document.createElement('button'); go.type='button'; go.className='jb-btn'; go.style.marginTop='10px';
      go.textContent=t('mdi_go');
      go.onclick=function(){
        go.disabled=true;
        var chosen=fresh.slice();
        boxes.forEach(function(b){
          if(!b.cb.checked) return;                     // left out on purpose
          if(b.it.ref && b.it.ref.unknown) b.it.ref=null; // in, but not onto a guess
          chosen.push(b.it);
        });
        if(!chosen.length){ jbsClose(ov); return; }
        var res=importMdNotes(chosen);
        jbsClose(ov);
        window.alert(t('mdi_done',{n:res.added}));
      };
      result.appendChild(go);
    }
'''


def patch(path):
    c = io.open(path, encoding="utf-8").read()
    orig = c
    c = add_strings(c)

    if "function hasBibleTemplate(" not in c:
        anchor = "  function resolveBibleLocationId("
        if c.count(anchor) != 1:
            sys.exit("ABORT: resolveBibleLocationId anchor x%d" % c.count(anchor))
        c = c.replace(anchor, TEMPLATE_HELPER + anchor, 1)

    for old, new, label in ((RESOLVE_OLD, RESOLVE_NEW, "resolve signature"),
                            (CREATE_OLD, CREATE_NEW, "create guard"),
                            (IMPORT_OLD, IMPORT_NEW, "import anchor guard"),
                            (IMPORT_VERSE_OLD, IMPORT_VERSE_NEW, "import verse")):
        if new in c:
            continue
        if c.count(old) != 1:
            sys.exit("ABORT: %s anchor x%d" % (label, c.count(old)))
        c = c.replace(old, new, 1)

    if "mdi_check" not in c.split("var I18N")[-1].split("function t(")[0] or "boxes.push(" not in c:
        i = c.find(PREVIEW_OLD_START)
        if i < 0:
            sys.exit("ABORT: preview() not found")
        end = c.find("\n    }\n", i)
        if end < 0:
            sys.exit("ABORT: preview() has no closing line")
        c = c[:i] + PREVIEW_NEW.rstrip("\n") + c[end + len("\n    }"):]

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("js/browse.js: preview asks about anything interpreted")
    else:
        print("js/browse.js: already patched")
    return c


if __name__ == "__main__":
    src = patch(BROWSE)
    io.open(os.path.join(REPO, "beta", "js", "browse.js"), "w", encoding="utf-8").write(src)
    print("beta/js/browse.js: mirrored")

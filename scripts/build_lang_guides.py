#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate scripts/guides_<lang>.py from translated JSON batches.

The general form of scripts/build_chinese_guides.py, minus the script
conversion that only Chinese needs. Use this for any new language: write one
JSON file per batch under a scratch directory, shaped

    { "<lang>": { "<slug>": {title, h1, description, intro[], steps[][2],
                             sections[][2], faq[][2]} } }

and run this. It is strictly better than appending to a Python module by hand:

  - a batch is valid JSON or it is not, so a broken batch fails loudly;
  - a slug translated twice aborts instead of one copy silently winning;
  - re-running is idempotent, so a batch can be corrected and replayed;
  - progress is reported as n/37 with the missing slugs named, never guessed.

Two guards run over every batch, both from real mistakes:

  STRAY   characters from a script the language does not use. A Cyrillic
          "материал" once reached a Cantonese paragraph and reads as a
          plausible word at a glance — nothing downstream objects to fluent,
          plausible, wrong text.
  DIACRITIC  for languages whose orthography is Latin-plus-diacritics, a
          paragraph with none at all is a strong sign of stripped or
          untranslated copy. Vietnamese without its tone marks is a different
          set of words, not a stylistic variant.

Usage:  python3 scripts/build_lang_guides.py <lang> <batch-dir>
"""
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Scripts each language must NOT contain. Latin-script languages reject every
# non-Latin block we have shipped copy in; add a row when adding a language.
_NON_LATIN = "[Ѐ-ӿ֐-ۿ฀-๿가-힯぀-ヿ一-鿿]"
STRAY = {
    "vi": re.compile(_NON_LATIN),
    "hu": re.compile(_NON_LATIN),
    # Hindi is Devanagari, so the Latin-script class is the wrong
    # guard: allow Devanagari + ASCII product names, reject the rest.
    "hi": re.compile("[Ѐ-ӿ֐-ۿ฀-๿가-힯぀-ヿ一-鿿]"),
    # Indonesian is Latin-script with no obligatory diacritics, so it gets
    # the stray-script guard but no DIACRITIC entry — an unaccented
    # Indonesian paragraph is simply correct Indonesian.
    "id": re.compile(_NON_LATIN + "|[ऀ-ॿ]"),
    # Romanian is Latin-script; ă â î ș ț are all in Latin Extended-A/B.
    "ro": re.compile(_NON_LATIN + "|[ऀ-ॿ]"),
    # Dutch is Latin-script. Its only non-ASCII letters are the diaeresis
    # (geüpload, coördinatie) and borrowed acutes, all Latin-1 — so like
    # Indonesian it gets the stray-script guard and no DIACRITIC entry.
    "nl": re.compile(_NON_LATIN + "|[ऀ-ॿ]"),
    # Kiswahili is Latin-script with no diacritics at all, so like
    # Indonesian it gets the stray-script guard and no DIACRITIC entry.
    "sw": re.compile(_NON_LATIN + "|[ऀ-ॿ]"),
    # Greek is Greek-script, so — like Hindi — the Latin-script class is the
    # wrong guard. Allow Greek and ASCII product names, reject the rest.
    # Note Cyrillic is in the reject set on purpose: а е о р с х у and their
    # capitals are visually identical to Greek/Latin letters, so a stray one
    # reads as an ordinary word and nothing downstream objects.
    "el": re.compile("[Ѐ-ӿ֐-ۿ฀-๿가-힯぀-ヿ一-鿿ऀ-ॿ]"),
}

# Languages written in Latin script with obligatory diacritics, and the
# fraction of paragraphs that must carry at least one.
DIACRITIC = {
    "vi": re.compile("[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợ"
                     "ùúủũụưừứửữựỳýỷỹỵđ]", re.I),
    # Hungarian: á é í ó ö ő ú ü ű. Its long/short vowel pairs are contrastive
    # (kerek/kérek, tor/tör/tőr), so unaccented copy is not a stylistic choice
    # either — it is a different set of words, or ASCII-mangled text.
    "hu": re.compile("[áéíóöőúüű]", re.I),
    # Hindi has no Latin diacritics; the equivalent "is this really the
    # language" check is that the prose is in Devanagari at all.
    "hi": re.compile("[ऀ-ॿ]"),
    # Same for Greek: prose with no Greek letters in it is transliterated,
    # untranslated or stripped — never a stylistic choice.
    "el": re.compile("[Ͱ-Ͽ]"),
}

META = {
    "el": {
        "name": "Greek",
        "upper": "EL",
        "glossary": """Glossary settled on for all 39 guides:

  backup              αντίγραφο ασφαλείας
  to merge / merge    συγχωνεύω / συγχώνευση
  notes               σημειώσεις
  highlights          επισημάνσεις
  bookmarks           σελιδοδείκτες
  tags                ετικέτες
  device              συσκευή
  file                αρχείο
  browser             πρόγραμμα περιήγησης
  to restore          κάνω επαναφορά / επαναφορά
  to back up          δημιουργώ αντίγραφο ασφαλείας
  Personal Study      Προσωπική Μελέτη
  Backup and Restore  Αντίγραφο ασφαλείας και επαναφορά
  database            βάση δεδομένων
  publication         έντυπο
  verse               εδάφιο
  Hebrew Scriptures   Εβραϊκές Γραφές
  Greek Scriptures    Ελληνικές Γραφές
  service year        υπηρεσιακό έτος

  "JW Library", "JW Sync", ".jwlibrary" and jwsync.org stay in Latin.
""",
    },
    "ro": {
        "name": "Romanian",
        "upper": "RO",
        "glossary": """Glossary settled on for all 37 guides:

  backup              copie de rezervă
  to merge / merge    a îmbina / îmbinare
  notes               notițe
  highlights          evidențieri
  bookmarks           semne de carte
  tags                etichete
  device              dispozitiv
  file                fișier
  browser             browser
  to restore          a restaura
  to back up          a face o copie de rezervă
  Personal Study      Studiu personal
  Backup and Restore  Copiere de rezervă și restaurare
  database            bază de date
  Conflict Reviewer   verificatorul de conflicte
  duplicate           duplicat
  publication         publicație
  meeting             întrunire
  convention          congres
  talk                cuvântare
  Hebrew Scriptures   Scripturile ebraice
  Greek Scriptures    Scripturile grecești

JW Library, .jwlibrary, JW Sync and jwsync.org are never translated.""",
    },
    "sw": {
        "name": "Swahili",
        "upper": "SW",
        "glossary": """Glossary settled on for all 39 guides:

  backup              nakala rudufu
  to merge / merge    kuunganisha / muunganisho
  notes               madokezo (sing. dokezo)
  highlights          viangazio (sing. kiangazio)
  bookmarks           alamisho
  tags                lebo
  device              kifaa (pl. vifaa)
  file                faili (pl. mafaili)
  browser             kivinjari
  to restore          kurejesha
  to back up          kutengeneza nakala rudufu
  Personal Study      Funzo la Kibinafsi
  Backup and Restore  Nakala Rudufu na Kurejesha
  database            hifadhidata
  Conflict Reviewer   kikagua migongano
  duplicate           nakala iliyojirudia
  publication         chapisho (pl. machapisho)
  meeting             mkutano
  convention          kusanyiko
  talk                hotuba
  Hebrew Scriptures   Maandiko ya Kiebrania
  Greek Scriptures    Maandiko ya Kigiriki

JW Library, .jwlibrary, JW Sync and jwsync.org are never translated.""",
    },
    "nl": {
        "name": "Dutch",
        "upper": "NL",
        "glossary": """Glossary settled on for all 37 guides:

  backup              back-up
  to merge / merge    samenvoegen / samenvoeging
  notes               aantekeningen
  highlights          markeringen
  bookmarks           bladwijzers
  tags                labels
  device              apparaat
  file                bestand
  browser             browser
  to restore          terugzetten
  to back up          een back-up maken
  Personal Study      Persoonlijke studie
  Backup and Restore  Back-up maken en terugzetten
  database            database
  Conflict Reviewer   conflictcontrole
  duplicate           dubbele
  publication         publicatie
  meeting             vergadering
  convention          congres
  talk                lezing
  Hebrew Scriptures   Hebreeuwse Geschriften
  Greek Scriptures    Griekse Geschriften

JW Library, .jwlibrary, JW Sync and jwsync.org are never translated.""",
    },
    "id": {
        "name": "Indonesian",
        "upper": "ID",
        "glossary": """Glossary settled on for all 37 guides:

  backup              cadangan
  to merge / merge    menggabungkan / gabungan
  notes               catatan
  highlights          sorotan
  bookmarks           penanda
  tags                label
  device              perangkat
  file                berkas
  browser             peramban
  to restore          memulihkan
  to back up          mencadangkan
  publication         publikasi
  study               pelajaran

JW Library, .jwlibrary, JW Sync and jwsync.org are never translated.""",
    },
    "vi": {
        "name": "Vietnamese",
        "upper": "VI",
        "glossary": """Glossary settled on for all 37 guides:

  backup              bản sao lưu
  to merge / merge    hợp nhất
  notes               ghi chú
  highlights          phần tô màu
  bookmarks           dấu trang
  tags                thẻ
  device              thiết bị
  to restore          khôi phục
  Personal Study      Học hỏi cá nhân
  Backup and Restore  Sao lưu và khôi phục
  browser             trình duyệt
  database            cơ sở dữ liệu
  Conflict Reviewer   trình xem lại xung đột
  duplicate           bản trùng lặp
  publication         ấn phẩm
  meeting             buổi nhóm họp
  convention          hội nghị
  talk                bài giảng
  Hebrew Scriptures   phần Kinh Thánh tiếng Hê-bơ-rơ
  Greek Scriptures    phần Kinh Thánh tiếng Hy Lạp""",
    },
    "hu": {
        "name": "Hungarian",
        "upper": "HU",
        "glossary": """Glossary settled on for all 37 guides:

  backup              biztonsági mentés
  to merge / merge    egyesíteni / egyesítés
  notes               jegyzetek
  highlights          kiemelések
  bookmarks           könyvjelzők
  tags                címkék
  device              eszköz
  to restore          visszaállítani
  Personal Study      Személyes tanulmányozás
  Backup and Restore  Biztonsági mentés és visszaállítás
  browser             böngésző
  database            adatbázis
  Conflict Reviewer   ütközésáttekintő
  duplicate           duplikátum
  publication         kiadvány
  meeting             összejövetel
  convention          kongresszus
  talk                előadás
  Hebrew Scriptures   Héber Iratok
  Greek Scriptures    Görög Iratok""",
    },
    "hi": {
        "name": "Hindi",
        "upper": "HI",
        "glossary": """Glossary settled on for the guides:

  backup              बैकअप
  to merge / merge    मर्ज करना / मर्ज
  notes               नोट
  highlights          हाइलाइट
  bookmarks           बुकमार्क
  tags                टैग
  device              डिवाइस
  to restore          रीस्टोर करना
  Personal Study      निजी अध्ययन
  Backup and Restore  बैकअप और रीस्टोर
  browser             ब्राउज़र
  database            डेटाबेस
  Conflict Reviewer   टकराव जाँच
  duplicate           डुप्लिकेट
  publication         प्रकाशन
  meeting             सभा
  convention          अधिवेशन
  talk                भाषण
  Hebrew Scriptures   इब्रानी शास्त्र
  Greek Scriptures    यूनानी शास्त्र""",
    },
}

HEADER = '''# -*- coding: utf-8 -*-
"""%(name)s copy for the static guide pages, keyed by slug.

Field names mirror build_guides.GUIDES. Anything left out falls back to
English. `group` and `related` are deliberately not translated — the first is
looked up through CHROME["%(code)s"]["groups"], the second is a list of slugs.

Product names stay in Latin script (JW Library, JW Sync, .jwlibrary, Google
Drive, iCloud), matching how they appear in the file system and in the app.

%(glossary)s

Generated by scripts/build_lang_guides.py — edit the JSON batches, not this.
"""

GUIDES_%(upper)s = '''


def q(s):
    """A Python string literal that keeps non-ASCII readable in the source."""
    return json.dumps(s, ensure_ascii=False)


def render(guides, order):
    out = ["{\n"]
    for slug in order:
        g = guides[slug]
        out.append("\n %s: {\n" % q(slug))
        for f in ("title", "h1", "description"):
            out.append("  %s: %s,\n" % (q(f), q(g[f])))
        out.append("  \"intro\": [\n")
        for p in g["intro"]:
            out.append("   %s,\n" % q(p))
        out.append("  ],\n")
        for field in ("steps", "sections", "faq"):
            out.append("  \"%s\": [\n" % field)
            for a, b in g[field]:
                out.append("   (%s, %s),\n" % (q(a), q(b)))
            out.append("  ],\n")
        out.append(" },\n")
    out.append("}\n")
    return "".join(out)


def check(lang, slug, g):
    blob = json.dumps(g, ensure_ascii=False)
    stray = STRAY.get(lang)
    if stray:
        m = stray.search(blob)
        if m:
            sys.exit("ABORT %s/%s: stray %r (U+%04X) — wrong script for this "
                     "language" % (lang, slug, m.group(0), ord(m.group(0))))
    dia = DIACRITIC.get(lang)
    if dia:
        # Long prose only: a heading like "Android" legitimately has none.
        prose = [p for p in g["intro"]] + [b for _, b in g["sections"]]
        bare = [p for p in prose if len(p) > 60 and not dia.search(p)]
        if bare:
            sys.exit("ABORT %s/%s: %d paragraph(s) with no diacritics at all — "
                     "likely stripped or untranslated:\n  %s"
                     % (lang, slug, len(bare), bare[0][:90]))


def m_upper(lang):
    return META[lang]["upper"]


def main():
    lang, batch_dir = sys.argv[1], sys.argv[2]
    if lang not in META:
        sys.exit("ABORT: add %r to META (and STRAY/DIACRITIC if it needs them)"
                 % lang)
    sys.path.insert(0, HERE)
    # guides_i18n.py registers guides_<lang>.py, and build_guides imports
    # guides_i18n — so on the very first run the module this script is about to
    # write is already being imported. Drop an empty stub in first rather than
    # asking the operator to register the language only after generating it,
    # which is an ordering nobody remembers on the next language.
    fname = "guides_%s.py" % lang.replace("-", "_").lower()
    fpath = os.path.join(HERE, fname)
    if not os.path.exists(fpath):
        io.open(fpath, "w", encoding="utf-8").write(
            "# -*- coding: utf-8 -*-\n# stub — replaced on the first successful"
            " run of build_lang_guides.py\nGUIDES_%s = {}\n" % m_upper(lang))
        print("created stub scripts/%s" % fname)
    import build_guides
    order = [g["slug"] for g in build_guides.GUIDES]

    data = {}
    for p in sorted(glob.glob(os.path.join(batch_dir, "b*.json"))):
        batch = json.load(io.open(p, encoding="utf-8"))
        for slug, g in batch.get(lang, {}).items():
            if slug in data:
                sys.exit("ABORT: %s translated twice for %s" % (slug, lang))
            check(lang, slug, g)
            data[slug] = g

    extra = [s for s in data if s not in order]
    if extra:
        sys.exit("ABORT %s: unknown slug(s) %s" % (lang, extra))
    missing = [s for s in order if s not in data]
    print("%-9s %2d/%d translated%s"
          % (lang, len(data), len(order),
             "" if not missing else "  missing: " + ", ".join(missing)))

    have = [s for s in order if s in data]
    m = META[lang]
    body = HEADER % {"name": m["name"], "code": lang,
                     "glossary": m["glossary"], "upper": m["upper"]}
    body += render(data, have)
    io.open(fpath, "w", encoding="utf-8").write(body)
    print("wrote scripts/%s (%d guides)" % (fname, len(have)))


if __name__ == "__main__":
    main()

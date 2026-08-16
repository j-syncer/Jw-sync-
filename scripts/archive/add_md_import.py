#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_md_import.py — read Markdown files back into a .jwlibrary.

Asked for on the community forum, alongside the verse in the export: "I would
like to import my notes from MD format to JW library app."

The write half already existed. adoptNotes() in js/browse.js inserts notes into
the open database with undo, tag creation and a dirty badge; it just always
inserted them unanchored. So this adds the reading half —

  * parseFrontMatter / mdBodyToNoteHtml, the inverse of exportMarkdown();
  * parseReference, which turns "book: Matthew / chapter: 26 / verse: 39" (or a
    "publication: Matthew 26:39" line) into a book number, chapter and verse;
  * resolveBibleLocationId, which finds the Location the backup already has for
    that chapter, or clones the identity columns off an existing Bible Location
    when it does not have one;
  * a preview panel that says what will land on a verse and what will not,
    before anything is written.

Both directions the forum asked about are covered by the same path: files
exported from this page carry book/chapter/verse and go back to the verse they
came from; files written in an ordinary Markdown editor have no such header and
arrive as standalone notes, keeping their title, date and tags. Adding a
"publication: Matthew 26:14" line to any file places it.

⚠️ The one thing this must never do is invent Location identity columns.
KeySymbol, MepsLanguage, Type and IssueTagNumber are values JW Library
interprets; a plausible-looking guess produces a Location the app does not tie
to the chapter, and nothing errors — the note simply is not where the reader
put it. So resolveBibleLocationId copies them off a row the backup already has,
and imports the note unanchored if there is no such row.

Idempotent; mirrors js/ to beta/js/ as 15_parity.js requires.
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BROWSE = os.path.join(REPO, "js", "browse.js")

# ── 1. UI strings, in all 25 languages ──────────────────────────────────────

KEYS = ["md_import", "mdi_title", "mdi_intro", "mdi_choose", "mdi_found",
        "mdi_anchored", "mdi_plain", "mdi_dupes", "mdi_go", "mdi_none",
        "mdi_err", "mdi_done", "mdi_tag"]

STRINGS = {
"en": ["Import Markdown", "Import Markdown notes",
 "Add .md files — or the .zip this page exports — as notes in this backup. A note whose header names a book, chapter and verse lands on that verse; the rest arrive as standalone notes.",
 "Choose .md files or a .zip", "{n} note(s) in {f} file(s)",
 "{n} will land on their verse", "{n} will be added as standalone notes",
 "{n} already in this backup — skipped", "Add to backup",
 "No notes found in those files.", "Those files could not be read.",
 "{n} note(s) added — use Export .jwlibrary to save them.", "Imported"],
"es": ["Importar Markdown", "Importar notas de Markdown",
 "Añade archivos .md — o el .zip que exporta esta página — como notas en esta copia de seguridad. Una nota cuyo encabezado indique libro, capítulo y versículo irá a ese versículo; las demás se añaden como notas sueltas.",
 "Elegir archivos .md o un .zip", "{n} nota(s) en {f} archivo(s)",
 "{n} irán a su versículo", "{n} se añadirán como notas sueltas",
 "{n} ya están en esta copia — omitidas", "Añadir a la copia",
 "No se encontraron notas en esos archivos.", "No se pudieron leer esos archivos.",
 "{n} nota(s) añadida(s) — usa Exportar .jwlibrary para guardarlas.", "Importado"],
"pt": ["Importar Markdown", "Importar notas de Markdown",
 "Adicione arquivos .md — ou o .zip que esta página exporta — como notas neste backup. Uma nota cujo cabeçalho traga livro, capítulo e versículo vai para esse versículo; as demais entram como notas avulsas.",
 "Escolher arquivos .md ou um .zip", "{n} nota(s) em {f} arquivo(s)",
 "{n} vão para o seu versículo", "{n} serão adicionadas como notas avulsas",
 "{n} já estão neste backup — ignoradas", "Adicionar ao backup",
 "Nenhuma nota encontrada nesses arquivos.", "Não foi possível ler esses arquivos.",
 "{n} nota(s) adicionada(s) — use Exportar .jwlibrary para salvar.", "Importado"],
"fr": ["Importer du Markdown", "Importer des notes Markdown",
 "Ajoutez des fichiers .md — ou le .zip exporté par cette page — comme notes dans cette sauvegarde. Une note dont l'en-tête indique le livre, le chapitre et le verset se place sur ce verset ; les autres arrivent comme notes libres.",
 "Choisir des fichiers .md ou un .zip", "{n} note(s) dans {f} fichier(s)",
 "{n} iront sur leur verset", "{n} seront ajoutées comme notes libres",
 "{n} déjà dans cette sauvegarde — ignorées", "Ajouter à la sauvegarde",
 "Aucune note trouvée dans ces fichiers.", "Ces fichiers n'ont pas pu être lus.",
 "{n} note(s) ajoutée(s) — utilisez Exporter .jwlibrary pour les enregistrer.", "Importé"],
"de": ["Markdown importieren", "Markdown-Notizen importieren",
 "Füge .md-Dateien — oder das .zip, das diese Seite exportiert — als Notizen zu dieser Sicherung hinzu. Eine Notiz, deren Kopfdaten Buch, Kapitel und Vers nennen, landet auf diesem Vers; die übrigen kommen als freie Notizen an.",
 "-md-Dateien oder ein .zip wählen", "{n} Notiz(en) in {f} Datei(en)",
 "{n} landen auf ihrem Vers", "{n} werden als freie Notizen hinzugefügt",
 "{n} bereits in dieser Sicherung — übersprungen", "Zur Sicherung hinzufügen",
 "In diesen Dateien wurden keine Notizen gefunden.", "Diese Dateien konnten nicht gelesen werden.",
 "{n} Notiz(en) hinzugefügt — zum Speichern .jwlibrary exportieren.", "Importiert"],
"it": ["Importa Markdown", "Importa note Markdown",
 "Aggiungi file .md — o lo .zip che questa pagina esporta — come note in questo backup. Una nota la cui intestazione indica libro, capitolo e versetto finisce su quel versetto; le altre arrivano come note libere.",
 "Scegli file .md o uno .zip", "{n} nota/e in {f} file",
 "{n} andranno sul loro versetto", "{n} saranno aggiunte come note libere",
 "{n} già presenti in questo backup — ignorate", "Aggiungi al backup",
 "Nessuna nota trovata in quei file.", "Non è stato possibile leggere quei file.",
 "{n} nota/e aggiunta/e — usa Esporta .jwlibrary per salvarle.", "Importato"],
"ru": ["Импорт Markdown", "Импорт заметок из Markdown",
 "Добавьте файлы .md — или .zip, который экспортирует эта страница — как заметки в эту резервную копию. Заметка, в заголовке которой указаны книга, глава и стих, встанет на этот стих; остальные добавятся как отдельные заметки.",
 "Выбрать файлы .md или .zip", "{n} заметок в {f} файлах",
 "{n} встанут на свой стих", "{n} добавятся как отдельные заметки",
 "{n} уже есть в этой копии — пропущены", "Добавить в копию",
 "В этих файлах заметок не найдено.", "Не удалось прочитать эти файлы.",
 "Добавлено заметок: {n} — нажмите «Экспорт .jwlibrary», чтобы сохранить.", "Импортировано"],
"ja": ["Markdown を読み込み", "Markdown ノートの読み込み",
 ".md ファイル（またはこのページが書き出す .zip）を、このバックアップのノートとして追加します。冒頭に書名・章・節があるノートはその節に付き、それ以外は単独のノートとして追加されます。",
 ".md ファイルか .zip を選ぶ", "{f} 個のファイルに {n} 件のノート",
 "{n} 件は該当の節に付きます", "{n} 件は単独のノートとして追加されます",
 "{n} 件はこのバックアップに既にあります（スキップ）", "バックアップに追加",
 "これらのファイルにノートは見つかりませんでした。", "これらのファイルを読み込めませんでした。",
 "{n} 件のノートを追加しました。「.jwlibrary を書き出し」で保存してください。", "読み込み済み"],
"ko": ["Markdown 가져오기", "Markdown 노트 가져오기",
 ".md 파일 또는 이 페이지가 내보낸 .zip을 이 백업의 노트로 추가합니다. 머리말에 책·장·절이 적힌 노트는 해당 절에 붙고, 나머지는 독립 노트로 추가됩니다.",
 ".md 파일 또는 .zip 선택", "파일 {f}개에 노트 {n}개",
 "{n}개는 해당 절에 붙습니다", "{n}개는 독립 노트로 추가됩니다",
 "{n}개는 이미 이 백업에 있습니다 — 건너뜀", "백업에 추가",
 "해당 파일에서 노트를 찾지 못했습니다.", "해당 파일을 읽을 수 없습니다.",
 "노트 {n}개를 추가했습니다 — '.jwlibrary 내보내기'로 저장하세요.", "가져옴"],
"tl": ["Mag-import ng Markdown", "Mag-import ng mga talang Markdown",
 "Magdagdag ng mga .md file — o ang .zip na ini-export ng pahinang ito — bilang mga tala sa backup na ito. Ang talang may aklat, kabanata at talata sa itaas ay dadapo sa talatang iyon; ang iba ay idadagdag bilang malayang tala.",
 "Pumili ng mga .md file o isang .zip", "{n} tala sa {f} file",
 "{n} ang dadapo sa kanilang talata", "{n} ang idadagdag bilang malayang tala",
 "{n} ang nasa backup na — nilaktawan", "Idagdag sa backup",
 "Walang talang nakita sa mga file na iyon.", "Hindi mabasa ang mga file na iyon.",
 "{n} talang naidagdag — gamitin ang I-export ang .jwlibrary para i-save.", "Na-import"],
"sv": ["Importera Markdown", "Importera Markdown-anteckningar",
 "Lägg till .md-filer — eller den .zip som den här sidan exporterar — som anteckningar i den här säkerhetskopian. En anteckning vars huvud anger bok, kapitel och vers hamnar på den versen; övriga läggs till som fristående anteckningar.",
 "Välj .md-filer eller en .zip", "{n} anteckning(ar) i {f} fil(er)",
 "{n} hamnar på sin vers", "{n} läggs till som fristående anteckningar",
 "{n} finns redan i säkerhetskopian — hoppades över", "Lägg till i säkerhetskopian",
 "Inga anteckningar hittades i de filerna.", "Filerna kunde inte läsas.",
 "{n} anteckning(ar) tillagda — använd Exportera .jwlibrary för att spara.", "Importerad"],
"ceb": ["I-import ang Markdown", "Pag-import ug mga nota gikan sa Markdown",
 "Idugang ang mga .md nga file — o ang .zip nga gi-export niini nga panid — isip mga nota niini nga backup. Ang notang adunay libro, kapitulo ug bersikulo sa ibabaw motugpa sa maong bersikulo; ang uban idugang isip nagbarog nga nota.",
 "Pagpili ug mga .md file o usa ka .zip", "{n} ka nota sa {f} ka file",
 "{n} ang motugpa sa ilang bersikulo", "{n} ang idugang isip nagbarog nga nota",
 "{n} anaa na niini nga backup — gilaktawan", "Idugang sa backup",
 "Walay nota nga nakit-an niadtong mga file.", "Dili mabasa kadtong mga file.",
 "{n} ka nota ang nadugang — gamita ang Export .jwlibrary aron matipigan.", "Gi-import"],
"nl": ["Markdown importeren", "Markdown-notities importeren",
 "Voeg .md-bestanden — of de .zip die deze pagina exporteert — toe als notities in deze back-up. Een notitie met boek, hoofdstuk en vers in de kop komt op dat vers terecht; de rest wordt als losse notitie toegevoegd.",
 "Kies .md-bestanden of een .zip", "{n} notitie(s) in {f} bestand(en)",
 "{n} komen op hun vers terecht", "{n} worden als losse notities toegevoegd",
 "{n} staan al in deze back-up — overgeslagen", "Aan back-up toevoegen",
 "Geen notities gevonden in die bestanden.", "Die bestanden konden niet worden gelezen.",
 "{n} notitie(s) toegevoegd — gebruik .jwlibrary exporteren om ze op te slaan.", "Geïmporteerd"],
"ro": ["Importă Markdown", "Importă notițe Markdown",
 "Adaugă fișiere .md — sau arhiva .zip exportată de această pagină — ca notițe în această copie de rezervă. O notiță al cărei antet indică cartea, capitolul și versetul ajunge pe acel verset; restul sunt adăugate ca notițe de sine stătătoare.",
 "Alege fișiere .md sau un .zip", "{n} notiț(e) în {f} fișier(e)",
 "{n} vor ajunge pe versetul lor", "{n} vor fi adăugate ca notițe de sine stătătoare",
 "{n} sunt deja în această copie — omise", "Adaugă în copie",
 "Nu s-au găsit notițe în acele fișiere.", "Acele fișiere nu au putut fi citite.",
 "{n} notiț(e) adăugate — folosește Exportă .jwlibrary pentru a le salva.", "Importat"],
"id": ["Impor Markdown", "Impor catatan Markdown",
 "Tambahkan berkas .md — atau .zip yang diekspor halaman ini — sebagai catatan di cadangan ini. Catatan yang bagian atasnya menyebut kitab, pasal, dan ayat akan mendarat di ayat itu; sisanya ditambahkan sebagai catatan lepas.",
 "Pilih berkas .md atau .zip", "{n} catatan dalam {f} berkas",
 "{n} akan mendarat di ayatnya", "{n} akan ditambahkan sebagai catatan lepas",
 "{n} sudah ada di cadangan ini — dilewati", "Tambahkan ke cadangan",
 "Tidak ada catatan yang ditemukan di berkas itu.", "Berkas itu tidak dapat dibaca.",
 "{n} catatan ditambahkan — gunakan Ekspor .jwlibrary untuk menyimpannya.", "Diimpor"],
"hi": ["Markdown आयात करें", "Markdown नोट आयात करें",
 ".md फ़ाइलें — या इस पेज से निर्यात की गई .zip — इस बैकअप में नोट के रूप में जोड़ें। जिस नोट के शीर्ष में पुस्तक, अध्याय और आयत लिखी हो, वह उसी आयत पर लगेगा; बाकी अलग नोट के रूप में जुड़ेंगे।",
 ".md फ़ाइलें या .zip चुनें", "{f} फ़ाइलों में {n} नोट",
 "{n} अपनी आयत पर लगेंगे", "{n} अलग नोट के रूप में जुड़ेंगे",
 "{n} पहले से इस बैकअप में हैं — छोड़े गए", "बैकअप में जोड़ें",
 "उन फ़ाइलों में कोई नोट नहीं मिला।", "वे फ़ाइलें पढ़ी नहीं जा सकीं।",
 "{n} नोट जोड़े गए — सहेजने के लिए .jwlibrary निर्यात करें।", "आयातित"],
"hu": ["Markdown importálása", "Markdown-jegyzetek importálása",
 "Adj hozzá .md fájlokat — vagy az oldal által exportált .zip fájlt — jegyzetként ehhez a biztonsági mentéshez. Az a jegyzet, amelynek fejlécében szerepel a könyv, a fejezet és a vers, arra a versre kerül; a többi önálló jegyzetként kerül be.",
 "Válassz .md fájlokat vagy egy .zip-et", "{n} jegyzet {f} fájlban",
 "{n} a saját versére kerül", "{n} önálló jegyzetként kerül be",
 "{n} már szerepel a mentésben — kihagyva", "Hozzáadás a mentéshez",
 "Nem található jegyzet ezekben a fájlokban.", "Ezeket a fájlokat nem sikerült beolvasni.",
 "{n} jegyzet hozzáadva — mentéshez exportáld a .jwlibrary fájlt.", "Importálva"],
"vi": ["Nhập Markdown", "Nhập ghi chú Markdown",
 "Thêm các tệp .md — hoặc tệp .zip mà trang này xuất ra — làm ghi chú trong bản sao lưu này. Ghi chú có ghi sách, chương và câu ở đầu tệp sẽ nằm đúng câu đó; số còn lại được thêm dưới dạng ghi chú rời.",
 "Chọn tệp .md hoặc .zip", "{n} ghi chú trong {f} tệp",
 "{n} sẽ nằm đúng câu của mình", "{n} sẽ được thêm dưới dạng ghi chú rời",
 "{n} đã có trong bản sao lưu — bỏ qua", "Thêm vào bản sao lưu",
 "Không tìm thấy ghi chú nào trong các tệp đó.", "Không đọc được các tệp đó.",
 "Đã thêm {n} ghi chú — dùng Xuất .jwlibrary để lưu lại.", "Đã nhập"],
"yue-Hant": ["匯入 Markdown", "匯入 Markdown 筆記",
 "將 .md 檔案（或者呢版匯出嘅 .zip）加入呢個備份做筆記。開頭寫咗書卷、章同節嘅筆記會落喺嗰節，其餘會加做獨立筆記。",
 "揀 .md 檔案或者 .zip", "{f} 個檔案入面有 {n} 條筆記",
 "{n} 條會落喺自己嗰節", "{n} 條會加做獨立筆記",
 "{n} 條呢個備份已經有——略過", "加入備份",
 "嗰啲檔案搵唔到筆記。", "讀唔到嗰啲檔案。",
 "已加入 {n} 條筆記——用「匯出 .jwlibrary」儲存。", "已匯入"],
"zh-Hant": ["匯入 Markdown", "匯入 Markdown 筆記",
 "將 .md 檔案（或本頁匯出的 .zip）加入這個備份作為筆記。開頭註明書卷、章與節的筆記會落在該節；其餘則以獨立筆記加入。",
 "選擇 .md 檔案或 .zip", "{f} 個檔案中有 {n} 則筆記",
 "{n} 則會落在所屬的節", "{n} 則會以獨立筆記加入",
 "{n} 則已在這個備份中 — 略過", "加入備份",
 "那些檔案中找不到筆記。", "無法讀取那些檔案。",
 "已加入 {n} 則筆記 — 請用「匯出 .jwlibrary」儲存。", "已匯入"],
"zh-Hans": ["导入 Markdown", "导入 Markdown 笔记",
 "将 .md 文件（或本页导出的 .zip）作为笔记加入这个备份。开头注明书卷、章和节的笔记会落在该节；其余以独立笔记加入。",
 "选择 .md 文件或 .zip", "{f} 个文件中有 {n} 条笔记",
 "{n} 条会落在所属的节", "{n} 条将以独立笔记加入",
 "{n} 条已在这个备份中 — 已跳过", "加入备份",
 "这些文件中没有找到笔记。", "无法读取这些文件。",
 "已加入 {n} 条笔记 — 请用“导出 .jwlibrary”保存。", "已导入"],
"pl": ["Importuj Markdown", "Importuj notatki z Markdown",
 "Dodaj pliki .md — albo archiwum .zip, które eksportuje ta strona — jako notatki do tej kopii zapasowej. Notatka z księgą, rozdziałem i wersetem w nagłówku trafi na ten werset; pozostałe zostaną dodane jako notatki samodzielne.",
 "Wybierz pliki .md lub .zip", "{n} notatek w {f} plikach",
 "{n} trafi na swój werset", "{n} zostanie dodanych jako notatki samodzielne",
 "{n} jest już w tej kopii — pominięto", "Dodaj do kopii",
 "W tych plikach nie znaleziono notatek.", "Nie udało się odczytać tych plików.",
 "Dodano notatki: {n} — użyj Eksportuj .jwlibrary, aby je zapisać.", "Zaimportowano"],
"uk": ["Імпорт Markdown", "Імпорт нотаток з Markdown",
 "Додайте файли .md — або .zip, який експортує ця сторінка — як нотатки до цієї резервної копії. Нотатка, у заголовку якої вказано книгу, розділ і вірш, стане на цей вірш; решта додасться як окремі нотатки.",
 "Виберіть файли .md або .zip", "{n} нотаток у {f} файлах",
 "{n} стануть на свій вірш", "{n} додадуться як окремі нотатки",
 "{n} уже є в цій копії — пропущено", "Додати до копії",
 "У цих файлах нотаток не знайдено.", "Не вдалося прочитати ці файли.",
 "Додано нотаток: {n} — натисніть «Експорт .jwlibrary», щоб зберегти.", "Імпортовано"],
"he": ["ייבוא Markdown", "ייבוא הערות מ-Markdown",
 "הוסיפו קובצי .md — או את קובץ ה-.zip שהדף הזה מייצא — כהערות בגיבוי הזה. הערה שמצוינים בראשה ספר, פרק ופסוק תיכנס לאותו פסוק; השאר יתווספו כהערות עצמאיות.",
 "בחרו קובצי .md או .zip", "{n} הערות ב-{f} קבצים",
 "{n} ייכנסו לפסוק שלהן", "{n} יתווספו כהערות עצמאיות",
 "{n} כבר בגיבוי הזה — דולגו", "הוספה לגיבוי",
 "לא נמצאו הערות בקבצים האלה.", "לא ניתן לקרוא את הקבצים האלה.",
 "נוספו {n} הערות — השתמשו בייצוא .jwlibrary כדי לשמור.", "מיובא"],
"ar": ["استيراد Markdown", "استيراد ملاحظات Markdown",
 "أضف ملفات .md — أو ملف .zip الذي تصدّره هذه الصفحة — كملاحظات في هذه النسخة الاحتياطية. الملاحظة التي يذكر رأسها السفر والأصحاح والآية تستقر على تلك الآية، والبقية تُضاف كملاحظات مستقلة.",
 "اختر ملفات .md أو ملف .zip", "{n} ملاحظة في {f} ملف",
 "{n} ستستقر على آيتها", "{n} ستُضاف كملاحظات مستقلة",
 "{n} موجودة أصلاً في هذه النسخة — تم تخطيها", "أضف إلى النسخة الاحتياطية",
 "لم يُعثر على ملاحظات في تلك الملفات.", "تعذّرت قراءة تلك الملفات.",
 "تمت إضافة {n} ملاحظة — استخدم تصدير .jwlibrary للحفظ.", "مستورد"],
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
    if "mdi_title:" in c:
        print("  strings: already present")
        return c
    m = re.search(r"\bI18N\s*=\s*\{", c)
    if not m:
        sys.exit("ABORT browse.js: no I18N object")
    start = m.end() - 1
    end = match_brace(c, start)
    body = c[start + 1:end]

    # Walk the language tables and splice the new keys into each one.
    out = []
    pos = 0
    seen = []
    while pos < len(body):
        km = re.compile(r'[\s,]*("?[\w-]+"?)\s*:\s*\{').match(body, pos)
        if not km:
            break
        lang = km.group(1).strip('"')
        s = body.index("{", km.end() - 1)
        e = match_brace(body, s)
        if lang not in STRINGS:
            sys.exit("ABORT browse.js: no translations written for %r" % lang)
        add = ",".join(k + ":" + js_str(v) for k, v in zip(KEYS, STRINGS[lang]))
        out.append(body[pos:e])
        out.append("," + add + "}")
        seen.append(lang)
        pos = e + 1
    out.append(body[pos:])
    missing = set(STRINGS) - set(seen)
    if missing:
        sys.exit("ABORT browse.js: languages not found in I18N: %s" % ", ".join(sorted(missing)))
    print("  strings: %d keys x %d languages" % (len(KEYS), len(seen)))
    return c[:start + 1] + "".join(out) + c[end:]


# ── 2. the importer ─────────────────────────────────────────────────────────

CODE_ANCHOR = "  // ---------- edit UI helpers ----------"

CODE = r'''  // ---------- Markdown import ----------
  // The inverse of exportMarkdown(). Files this page wrote carry book, chapter
  // and verse in their front matter and go back to the verse they came from;
  // files written in any other editor have no such header and arrive as
  // standalone notes, keeping their title, date and tags.
  function parseFrontMatter(text){
    var s=String(text||'').replace(/^﻿/,'').replace(/\r\n/g,'\n');
    var m=/^---\n([\s\S]*?)\n---\n?/.exec(s);
    if(!m) return { meta:{}, body:s };
    var meta={};
    m[1].split('\n').forEach(function(line){
      var i=line.indexOf(':'); if(i<1) return;
      var k=line.slice(0,i).trim(), v=line.slice(i+1).trim();
      if(!k) return;
      if(/^\[[\s\S]*\]$/.test(v)){
        meta[k]=v.slice(1,-1).split(',').map(function(x){ return x.trim().replace(/^["']|["']$/g,''); }).filter(Boolean);
      } else {
        meta[k]=v.replace(/^["']|["']$/g,'');
      }
    });
    return { meta:meta, body:s.slice(m[0].length) };
  }
  function mdInline(s){
    return htmlEscape(s)
      .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
      .replace(/(^|[^*])\*([^*\n]+)\*/g,'$1<em>$2</em>');
  }
  function mdBodyToNoteHtml(md, title){
    var text=String(md||'').replace(/\r\n/g,'\n').trim();
    // exportMarkdown() repeats the title as an <h1> above the body; importing
    // it as content would give every note its own title twice.
    var h=/^#\s+(.+)\n?/.exec(text);
    if(h && (!title || h[1].trim()===String(title).trim())) text=text.slice(h[0].length).replace(/^\n+/,'');
    var out=[];
    text.split(/\n{2,}/).forEach(function(block){
      block=block.trim(); if(!block) return;
      var lines=block.split('\n');
      if(lines.length && lines.every(function(l){ return /^\s*[-*+]\s+/.test(l); })){
        out.push('<ul>'+lines.map(function(l){ return '<li>'+mdInline(l.replace(/^\s*[-*+]\s+/,''))+'</li>'; }).join('')+'</ul>');
        return;
      }
      out.push('<p>'+lines.map(function(l){ return mdInline(l.replace(/^#{1,6}\s+/,'')); }).join('<br />')+'</p>');
    });
    return out.join('');
  }
  var BIBLE_BY_NAME=null;
  function bookNumberFromName(name){
    if(!BIBLE_BY_NAME){ BIBLE_BY_NAME={}; BIBLE.forEach(function(b,i){ BIBLE_BY_NAME[b.toLowerCase()]=i+1; }); }
    return BIBLE_BY_NAME[String(name||'').trim().toLowerCase().replace(/\s+/g,' ')]||0;
  }
  // Discrete book/chapter/verse fields if they are there, otherwise the
  // readable "publication: Matthew 26:14" line, which is what older exports
  // and hand-written files have.
  function parseReference(meta){
    var book=meta.book, chapter=meta.chapter, verse=meta.verse;
    if(!book && meta.publication){
      var m=/^(.+?)\s+(\d+)(?::(\d+))?/.exec(String(meta.publication).trim());
      if(m){ book=m[1]; chapter=m[2]; if(verse==null) verse=m[3]; }
    }
    var bn=bookNumberFromName(book);
    if(!bn) return null;
    var ch=parseInt(chapter,10); if(!(ch>=1)) return null;
    var vs=null, vm=/^(\d+)/.exec(String(verse==null?'':verse));
    if(vm) vs=parseInt(vm[1],10);
    return { book:bn, chapter:ch, verse:(vs>=1?vs:null) };
  }
  // ⚠️ Never invent the columns that identify a Location. KeySymbol,
  // MepsLanguage, Type and IssueTagNumber are values JW Library interprets, and
  // a plausible guess yields a row the app does not tie to the chapter —
  // silently, with the note simply not where the reader put it. So reuse the
  // Location the backup already has for this chapter, or clone those columns
  // off another Bible location in the same file. With neither, the note goes in
  // unanchored, which is honest and reversible.
  function resolveBibleLocationId(bookNumber, chapter, cache){
    var key=bookNumber+':'+chapter;
    if(cache && key in cache) return cache[key];
    var id=null;
    try{
      var hit=rowsFromExec(state.db,'SELECT LocationId FROM Location WHERE BookNumber='+(bookNumber|0)+
        ' AND ChapterNumber='+(chapter|0)+' ORDER BY LocationId LIMIT 1');
      if(hit.length){ id=hit[0].LocationId; }
      else {
        var tpl=rowsFromExec(state.db,'SELECT * FROM Location WHERE BookNumber IS NOT NULL'+
          ' AND ChapterNumber IS NOT NULL ORDER BY LocationId LIMIT 1');
        if(tpl.length){
          var t0=tpl[0], cols=[], vals=[];
          Object.keys(t0).forEach(function(c){
            if(c==='LocationId'||c==='Title') return;
            cols.push(c);
            vals.push(c==='BookNumber'?bookNumber:(c==='ChapterNumber'?chapter:t0[c]));
          });
          state.db.run('INSERT INTO Location ('+cols.map(function(c){return '"'+c+'"';}).join(',')+
            ') VALUES ('+cols.map(function(){return '?';}).join(',')+')', vals);
          id=rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id;
        }
      }
    }catch(e){ console.error('[jb] md location',e); id=null; }
    if(cache) cache[key]=id;
    return id;
  }
  // Same notion of "already there" the Library Doctor uses: title, content and
  // where it sits. Re-importing the same export twice should be a no-op.
  function existingNoteKeys(){
    var set={};
    (state.allNotes||[]).forEach(function(n){
      set[[String(n.Title||''),String(n.Content||''),
        (n.LocationId==null?-1:n.LocationId),
        (n.BlockIdentifier==null?-1:n.BlockIdentifier)].join('\u0000')]=1;
    });
    return set;
  }
  function mdFileToNote(name, text){
    var fm=parseFrontMatter(text);
    var meta=fm.meta||{};
    var title=(typeof meta.title==='string'&&meta.title.trim())?meta.title.trim():'';
    if(!title){
      var h=/^#\s+(.+)$/m.exec(fm.body||'');
      title=h?h[1].trim():String(name||'').replace(/\.md$/i,'').replace(/^\d+-/,'').replace(/-/g,' ');
    }
    var tags=Array.isArray(meta.tags)?meta.tags:(meta.tags?[meta.tags]:[]);
    var date=null;
    if(typeof meta.date==='string' && /^\d{4}-\d{2}-\d{2}/.test(meta.date)) date=meta.date.slice(0,10)+' 00:00:00';
    return { title:title, content:sanitizeNoteHtml(mdBodyToNoteHtml(fm.body,title)),
             tags:tags, date:date, ref:parseReference(meta), file:name };
  }
  // Accepts the .zip exportMarkdown() produces as well as loose .md files.
  function readMdFiles(files){
    // Read to an ArrayBuffer / text first rather than handing the File straight
    // to JSZip and FileReader: it is the same work, and it keeps this readable
    // by anything with a Blob rather than only by a browser's own File.
    function bytes(f){ return (typeof f.arrayBuffer==='function') ? f.arrayBuffer() : Promise.resolve(f); }
    function text(f){
      if(typeof f.text==='function') return f.text();
      return new Promise(function(res){
        var rd=new FileReader();
        rd.onload=function(){ res(String(rd.result||'')); };
        rd.onerror=function(){ res(''); };
        rd.readAsText(f);
      });
    }
    var jobs=Array.prototype.slice.call(files||[]).map(function(f){
      if(/\.zip$/i.test(f.name||'')){
        if(!window.JSZip) return Promise.resolve([]);
        return bytes(f).then(function(buf){ return window.JSZip.loadAsync(buf); }).then(function(zip){
          var names=Object.keys(zip.files).filter(function(n){ return /\.md$/i.test(n) && !zip.files[n].dir; });
          return Promise.all(names.map(function(n){
            return zip.files[n].async('string').then(function(txt){ return mdFileToNote(n.split('/').pop(), txt); });
          }));
        }).catch(function(e){ console.error('[jb] md zip',e); return []; });
      }
      return text(f).then(function(txt){ return txt ? [mdFileToNote(f.name, txt)] : []; });
    });
    return Promise.all(jobs).then(function(lists){
      return lists.reduce(function(a,b){ return a.concat(b); },[]);
    });
  }
  function importMdNotes(items){
    if(!state.db||!items||!items.length) return {added:0,anchored:0};
    snapshot(); state._inBatch=true;
    var added=0, anchored=0, now=nowTimestamp(), cache={};
    try{
      var label=t('mdi_tag');
      function tagId(name){
        var s=String(name).replace(/'/g,"''");
        var r=rowsFromExec(state.db,"SELECT TagId FROM Tag WHERE Name='"+s+"' COLLATE NOCASE");
        if(r.length) return r[0].TagId;
        state.db.run('INSERT INTO Tag (Name, Type) VALUES (?,1)',[name]);
        return rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id;
      }
      items.forEach(function(it){
        try{
          var locId=it.ref?resolveBibleLocationId(it.ref.book,it.ref.chapter,cache):null;
          var verse=(locId&&it.ref&&it.ref.verse)?it.ref.verse:null;
          var stamp=it.date||now;
          var cols=['Guid','Title','Content','LastModified','Created','BlockType','BlockIdentifier'];
          var vals=[jbUuid(), it.title||'', it.content||'', stamp, stamp, verse?2:0, verse?verse:0];
          if(locId){ cols.push('LocationId'); vals.push(locId); }
          state.db.run('INSERT INTO Note ('+cols.join(',')+') VALUES ('+cols.map(function(){return '?';}).join(',')+')', vals);
          var noteId=rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id;
          var names=[label].concat(Array.isArray(it.tags)?it.tags:[]), seen={};
          names.forEach(function(tn){
            tn=String(tn||'').trim(); if(!tn||seen[tn.toLowerCase()]) return; seen[tn.toLowerCase()]=1;
            try{ state.db.run('INSERT INTO TagMap (TagId, NoteId, Position) VALUES (?,?,0)',[tagId(tn),noteId]); }catch(_){ }
          });
          added++; if(locId) anchored++;
        }catch(e){ console.error('[jb] md import note',e); }
      });
    }catch(e){ console.error('[jb] md import',e); }
    finally{ state._inBatch=false; }
    afterBatch(false);
    return { added:added, anchored:anchored };
  }
  window.__jwMdImport={ parse:mdFileToNote, toHtml:mdBodyToNoteHtml, ref:parseReference,
    readFiles:readMdFiles, importNotes:importMdNotes, open:openMdImport }; // for tests

  function openMdImport(){
    if(!state.db) return;
    var ov=document.createElement('div'); ov.className='jbs-overlay';
    ov.innerHTML='<div class="jbs-card"><div class="jbs-head"><h3>'+htmlEscape(t('mdi_title'))+
      '</h3><button class="jbs-x" type="button" aria-label="'+htmlEscape(t('close'))+'">&times;</button></div>'+
      '<p class="jbs-intro">'+htmlEscape(t('mdi_intro'))+'</p>'+
      '<div class="jbs-actions"><button type="button" class="jb-btn jbs-choose">'+htmlEscape(t('mdi_choose'))+'</button></div>'+
      '<div class="jbs-result"></div></div>';
    document.body.appendChild(ov);
    var result=ov.querySelector('.jbs-result');
    ov.querySelector('.jbs-x').onclick=function(){ jbsClose(ov); };
    ov.addEventListener('mousedown',function(e){ if(e.target===ov) jbsClose(ov); });
    ov.querySelector('.jbs-choose').onclick=function(){
      var fi=document.createElement('input'); fi.type='file'; fi.multiple=true;
      fi.accept='.md,.markdown,.zip,text/markdown';
      fi.onchange=function(){
        var files=fi.files; if(!files||!files.length) return;
        result.innerHTML='<div class="jbs-list-hdr">'+htmlEscape(t('loading'))+'</div>';
        readMdFiles(files).then(function(notes){ preview(notes, files.length); })
          .catch(function(e){ console.error('[jb] md read',e); result.innerHTML='<div class="jbs-err">'+htmlEscape(t('mdi_err'))+'</div>'; });
      };
      fi.click();
    };
    function preview(notes, fileCount){
      result.innerHTML='';
      var have=existingNoteKeys(), cache={}, fresh=[], dupes=0, willAnchor=0;
      notes.forEach(function(it){
        if(!it || (!it.title && !it.content)) return;
        // Resolving here would create Locations before the user has agreed to
        // anything, so only count what an existing Location can already take.
        var locId=it.ref?resolveBibleLocationId(it.ref.book,it.ref.chapter,cache):null;
        var verse=(locId&&it.ref&&it.ref.verse)?it.ref.verse:null;
        var key=[String(it.title||''),String(it.content||''),(locId==null?-1:locId),(verse==null?-1:verse)].join('\u0000');
        if(have[key]){ dupes++; return; }
        if(it.ref) willAnchor++;
        fresh.push(it);
      });
      if(!fresh.length && !dupes){ result.innerHTML='<div class="jbs-err">'+htmlEscape(t('mdi_none'))+'</div>'; return; }
      var box=document.createElement('div'); box.className='jbs-list';
      function line(txt){ var d=document.createElement('div'); d.className='jbs-list-hdr'; d.textContent=txt; box.appendChild(d); }
      line(t('mdi_found',{n:fresh.length+dupes, f:fileCount}));
      if(willAnchor) line(t('mdi_anchored',{n:willAnchor}));
      if(fresh.length-willAnchor>0) line(t('mdi_plain',{n:fresh.length-willAnchor}));
      if(dupes) line(t('mdi_dupes',{n:dupes}));
      result.appendChild(box);
      if(!fresh.length) return;
      var go=document.createElement('button'); go.type='button'; go.className='jb-btn'; go.style.marginTop='10px';
      go.textContent=t('mdi_go');
      go.onclick=function(){
        go.disabled=true;
        var res=importMdNotes(fresh);
        jbsClose(ov);
        window.alert(t('mdi_done',{n:res.added}));
      };
      result.appendChild(go);
    }
  }

'''

BTN_OLD = """    var recvBtn=document.createElement('button'); recvBtn.type='button'; recvBtn.className='jb-md-btn'; recvBtn.textContent=t('open_share'); recvBtn.title=t('open_share'); recvBtn.onclick=function(){ if(window.__jwGoShare) window.__jwGoShare(); };"""

BTN_NEW = """    var mdiBtn=document.createElement('button'); mdiBtn.className='jb-md-btn'; mdiBtn.type='button';
    mdiBtn.title=t('mdi_title');
    mdiBtn.innerHTML='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><polyline points="9 13 12 16 15 13"/><line x1="12" y1="16" x2="12" y2="10"/></svg>'+htmlEscape(t('md_import'));
    mdiBtn.onclick=openMdImport;
    head.appendChild(mdiBtn);
""" + BTN_OLD


def patch(path):
    c = io.open(path, encoding="utf-8").read()
    orig = c

    c = add_strings(c)

    if "function openMdImport(" not in c:
        if c.count(CODE_ANCHOR) != 1:
            sys.exit("ABORT browse.js: edit-helpers anchor x%d" % c.count(CODE_ANCHOR))
        c = c.replace(CODE_ANCHOR, CODE + CODE_ANCHOR, 1)
        print("  importer installed")

    if "mdiBtn" not in c:
        if c.count(BTN_OLD) != 1:
            sys.exit("ABORT browse.js: header button anchor x%d" % c.count(BTN_OLD))
        c = c.replace(BTN_OLD, BTN_NEW, 1)
        print("  header button added")

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("js/browse.js: Markdown import installed")
    else:
        print("js/browse.js: already patched")
    return c


if __name__ == "__main__":
    src = patch(BROWSE)
    io.open(os.path.join(REPO, "beta", "js", "browse.js"), "w", encoding="utf-8").write(src)
    print("beta/js/browse.js: mirrored")

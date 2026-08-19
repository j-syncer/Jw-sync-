/* ──────────────────────────────────────────────────────────────────────────
   conflict-review.js — Merge conflict review UI (window.__jwConflictReview).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var SQLJS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';

  var I18N = {
    en: { title:"Review your merge", subtitle:"{n} notes were edited differently across your backups. Choose which version to keep — or keep both.", current:"In your merge", keep_this:"Keep this", kept:"✓ Kept", keep_both:"Keep both", keep_both_on:"✓ Keeping both", keep_both_hint:"Adds the other version as a separate note", modified:"Edited", apply:"Apply & download", applying:"Applying…", skip:"Keep merge as-is", close:"Close", untitled:"(untitled note)", empty:"(empty)", more:"+{n} more conflicts will keep the merge's automatic choice.", merged_label:"Merged result" , suggest:"Suggest best",suggested:"Suggested",sg_content:"Has content",sg_newer:"Most recent edit",sg_longer:"Most detailed" ,compare:"Compare side by side",compare_hide:"Hide comparison",cmp_hint:"Pick the lines you want from each version, then edit the result below if you need to.",all_cur:"All from the merge",all_alt:"All from the other version",all_both:"Keep both sides",combined:"Combined note",use_combined:"Use this combined text",using_combined:"✓ Using combined text",rebuild:"Rebuild from selection",custom_badge:"Combined"},
    es: { title:"Revisa tu fusión", subtitle:"{n} notas se editaron de forma diferente en tus copias. Elige qué versión conservar — o conserva ambas.", current:"En tu fusión", keep_this:"Conservar esta", kept:"✓ Conservada", keep_both:"Conservar ambas", keep_both_on:"✓ Conservando ambas", keep_both_hint:"Añade la otra versión como una nota aparte", modified:"Editada", apply:"Aplicar y descargar", applying:"Aplicando…", skip:"Dejar la fusión como está", close:"Cerrar", untitled:"(nota sin título)", empty:"(vacío)", more:"+{n} conflictos más mantendrán la elección automática de la fusión.", merged_label:"Resultado de la fusión" , suggest:"Sugerir la mejor",suggested:"Sugerida",sg_content:"Tiene contenido",sg_newer:"Edición más reciente",sg_longer:"Más detallada" ,compare:"Comparar lado a lado",compare_hide:"Ocultar comparación",cmp_hint:"Elige las líneas que quieras de cada versión y luego edita el resultado si lo necesitas.",all_cur:"Todo de la fusión",all_alt:"Todo de la otra versión",all_both:"Conservar ambos lados",combined:"Nota combinada",use_combined:"Usar este texto combinado",using_combined:"✓ Usando el texto combinado",rebuild:"Rehacer desde la selección",custom_badge:"Combinada"},
    pt: { title:"Revise sua mesclagem", subtitle:"{n} notas foram editadas de forma diferente nos seus backups. Escolha qual versão manter — ou mantenha ambas.", current:"Na sua mesclagem", keep_this:"Manter esta", kept:"✓ Mantida", keep_both:"Manter ambas", keep_both_on:"✓ Mantendo ambas", keep_both_hint:"Adiciona a outra versão como uma nota separada", modified:"Editada", apply:"Aplicar e baixar", applying:"Aplicando…", skip:"Manter a mesclagem como está", close:"Fechar", untitled:"(nota sem título)", empty:"(vazio)", more:"+{n} conflitos manterão a escolha automática da mesclagem.", merged_label:"Resultado da mesclagem" , suggest:"Sugerir a melhor",suggested:"Sugerida",sg_content:"Tem conteúdo",sg_newer:"Edição mais recente",sg_longer:"Mais detalhada" ,compare:"Comparar lado a lado",compare_hide:"Ocultar comparação",cmp_hint:"Escolha as linhas que quiser de cada versão e depois edite o resultado se precisar.",all_cur:"Tudo da mesclagem",all_alt:"Tudo da outra versão",all_both:"Manter os dois lados",combined:"Nota combinada",use_combined:"Usar este texto combinado",using_combined:"✓ Usando o texto combinado",rebuild:"Refazer a partir da seleção",custom_badge:"Combinada"},
    fr: { title:"Vérifiez votre fusion", subtitle:"{n} notes ont été modifiées différemment dans vos sauvegardes. Choisissez la version à conserver — ou gardez les deux.", current:"Dans votre fusion", keep_this:"Garder celle-ci", kept:"✓ Conservée", keep_both:"Garder les deux", keep_both_on:"✓ Les deux conservées", keep_both_hint:"Ajoute l'autre version comme note distincte", modified:"Modifiée", apply:"Appliquer et télécharger", applying:"Application…", skip:"Laisser la fusion telle quelle", close:"Fermer", untitled:"(note sans titre)", empty:"(vide)", more:"+{n} autres conflits conserveront le choix automatique de la fusion.", merged_label:"Résultat de la fusion" , suggest:"Suggérer la meilleure",suggested:"Suggérée",sg_content:"Contient du texte",sg_newer:"Édition la plus récente",sg_longer:"La plus détaillée" ,compare:"Comparer côte à côte",compare_hide:"Masquer la comparaison",cmp_hint:"Choisissez les lignes que vous voulez dans chaque version, puis modifiez le résultat si besoin.",all_cur:"Tout de la fusion",all_alt:"Tout de l'autre version",all_both:"Garder les deux côtés",combined:"Note combinée",use_combined:"Utiliser ce texte combiné",using_combined:"✓ Texte combiné utilisé",rebuild:"Reconstruire depuis la sélection",custom_badge:"Combinée"},
    de: { title:"Prüfe deine Zusammenführung", subtitle:"{n} Notizen wurden in deinen Backups unterschiedlich bearbeitet. Wähle, welche Version bleibt — oder behalte beide.", current:"In deiner Zusammenführung", keep_this:"Diese behalten", kept:"✓ Behalten", keep_both:"Beide behalten", keep_both_on:"✓ Beide behalten", keep_both_hint:"Fügt die andere Version als separate Notiz hinzu", modified:"Bearbeitet", apply:"Anwenden & herunterladen", applying:"Wird angewendet…", skip:"Zusammenführung unverändert lassen", close:"Schließen", untitled:"(Notiz ohne Titel)", empty:"(leer)", more:"+{n} weitere Konflikte behalten die automatische Auswahl der Zusammenführung.", merged_label:"Ergebnis der Zusammenführung" , suggest:"Beste vorschlagen",suggested:"Vorschlag",sg_content:"Hat Inhalt",sg_newer:"Neueste Änderung",sg_longer:"Am ausführlichsten" ,compare:"Nebeneinander vergleichen",compare_hide:"Vergleich ausblenden",cmp_hint:"Wähle aus jeder Version die Zeilen, die du behalten willst, und bearbeite das Ergebnis bei Bedarf.",all_cur:"Alles aus der Zusammenführung",all_alt:"Alles aus der anderen Version",all_both:"Beide Seiten behalten",combined:"Kombinierte Notiz",use_combined:"Diesen kombinierten Text verwenden",using_combined:"✓ Kombinierter Text wird verwendet",rebuild:"Aus Auswahl neu aufbauen",custom_badge:"Kombiniert"},
    it: { title:"Controlla la tua unione", subtitle:"{n} note sono state modificate in modo diverso nei tuoi backup. Scegli quale versione mantenere — o tienile entrambe.", current:"Nella tua unione", keep_this:"Tieni questa", kept:"✓ Mantenuta", keep_both:"Tieni entrambe", keep_both_on:"✓ Entrambe mantenute", keep_both_hint:"Aggiunge l'altra versione come nota separata", modified:"Modificata", apply:"Applica e scarica", applying:"Applicazione…", skip:"Lascia l'unione com'è", close:"Chiudi", untitled:"(nota senza titolo)", empty:"(vuoto)", more:"+{n} altri conflitti manterranno la scelta automatica dell'unione.", merged_label:"Risultato dell'unione" , suggest:"Suggerisci la migliore",suggested:"Suggerita",sg_content:"Ha contenuto",sg_newer:"Modifica più recente",sg_longer:"Più dettagliata" ,compare:"Confronta affiancate",compare_hide:"Nascondi il confronto",cmp_hint:"Scegli le righe che vuoi da ciascuna versione, poi modifica il risultato se serve.",all_cur:"Tutto dall'unione",all_alt:"Tutto dall'altra versione",all_both:"Tieni entrambi i lati",combined:"Nota combinata",use_combined:"Usa questo testo combinato",using_combined:"✓ Testo combinato in uso",rebuild:"Ricostruisci dalla selezione",custom_badge:"Combinata"},
    ru: { title:"Проверьте объединение", subtitle:"{n} заметок были изменены по-разному в ваших копиях. Выберите, какую версию оставить — или оставьте обе.", current:"В объединении", keep_this:"Оставить эту", kept:"✓ Оставлено", keep_both:"Оставить обе", keep_both_on:"✓ Обе оставлены", keep_both_hint:"Добавит другую версию как отдельную заметку", modified:"Изменено", apply:"Применить и скачать", applying:"Применение…", skip:"Оставить как есть", close:"Закрыть", untitled:"(заметка без названия)", empty:"(пусто)", more:"+{n} других конфликтов сохранят автоматический выбор объединения.", merged_label:"Результат объединения" , suggest:"Предложить лучшее",suggested:"Рекомендуется",sg_content:"Есть содержимое",sg_newer:"Последнее изменение",sg_longer:"Наиболее подробная" ,compare:"Сравнить рядом",compare_hide:"Скрыть сравнение",cmp_hint:"Выберите нужные строки из каждой версии, а затем при необходимости отредактируйте результат.",all_cur:"Всё из объединения",all_alt:"Всё из другой версии",all_both:"Оставить обе стороны",combined:"Объединённая заметка",use_combined:"Использовать этот объединённый текст",using_combined:"✓ Используется объединённый текст",rebuild:"Собрать заново по выбору",custom_badge:"Объединено"},
    ja: { title:"マージを確認", subtitle:"{n} 件のメモがバックアップ間で異なる形で編集されています。残すバージョンを選ぶか、両方を残せます。", current:"マージ結果", keep_this:"これを残す", kept:"✓ 残しました", keep_both:"両方残す", keep_both_on:"✓ 両方を残す", keep_both_hint:"もう一方を別のメモとして追加します", modified:"編集", apply:"適用してダウンロード", applying:"適用中…", skip:"マージのままにする", close:"閉じる", untitled:"(無題のメモ)", empty:"(空)", more:"他 +{n} 件の競合はマージの自動選択を維持します。", merged_label:"マージ結果" , suggest:"おすすめを提案",suggested:"おすすめ",sg_content:"内容あり",sg_newer:"最新の編集",sg_longer:"最も詳しい" ,compare:"左右に並べて比較",compare_hide:"比較を隠す",cmp_hint:"各バージョンから残したい行を選び、必要なら結果を編集してください。",all_cur:"マージ結果からすべて",all_alt:"もう一方からすべて",all_both:"両方を残す",combined:"組み合わせたメモ",use_combined:"この組み合わせた文章を使う",using_combined:"✓ 組み合わせた文章を使用中",rebuild:"選択から作り直す",custom_badge:"組み合わせ"},
    ko: { title:"병합 검토", subtitle:"{n}개의 메모가 백업마다 다르게 편집되었습니다. 어떤 버전을 남길지 선택하거나 둘 다 보관하세요.", current:"병합 결과", keep_this:"이것 남기기", kept:"✓ 남김", keep_both:"둘 다 남기기", keep_both_on:"✓ 둘 다 보관", keep_both_hint:"다른 버전을 별도의 메모로 추가합니다", modified:"편집됨", apply:"적용 후 다운로드", applying:"적용 중…", skip:"병합 그대로 두기", close:"닫기", untitled:"(제목 없는 메모)", empty:"(비어 있음)", more:"+{n}개의 추가 충돌은 병합의 자동 선택을 유지합니다.", merged_label:"병합 결과" , suggest:"최적 추천",suggested:"추천",sg_content:"내용 있음",sg_newer:"가장 최근 편집",sg_longer:"가장 상세함" ,compare:"나란히 비교",compare_hide:"비교 숨기기",cmp_hint:"각 버전에서 남길 줄을 고른 다음, 필요하면 결과를 편집하세요.",all_cur:"병합 결과에서 전부",all_alt:"다른 버전에서 전부",all_both:"양쪽 다 남기기",combined:"합친 메모",use_combined:"이 합친 내용 사용",using_combined:"✓ 합친 내용 사용 중",rebuild:"선택한 대로 다시 만들기",custom_badge:"합침"},
    tl: { title:"Suriin ang merge", subtitle:"{n} na tala ang iba't iba ang pagkaka-edit sa iyong mga backup. Piliin kung aling bersyon ang itatago — o itago ang pareho.", current:"Sa iyong merge", keep_this:"Itago ito", kept:"✓ Itinago", keep_both:"Itago pareho", keep_both_on:"✓ Itinatago pareho", keep_both_hint:"Idaragdag ang isa pang bersyon bilang hiwalay na tala", modified:"In-edit", apply:"Ilapat at i-download", applying:"Inilalapat…", skip:"Iwan ang merge", close:"Isara", untitled:"(talang walang pamagat)", empty:"(walang laman)", more:"+{n} pang conflicts ang magpapanatili ng awtomatikong pili ng merge.", merged_label:"Resulta ng merge" , suggest:"Imungkahi ang pinakamahusay",suggested:"Iminumungkahi",sg_content:"May nilalaman",sg_newer:"Pinakabagong edit",sg_longer:"Pinakadetalyado" ,compare:"Ihambing nang magkatabi",compare_hide:"Itago ang paghahambing",cmp_hint:"Piliin ang mga linyang gusto mo mula sa bawat bersyon, tapos i-edit ang resulta kung kailangan.",all_cur:"Lahat mula sa merge",all_alt:"Lahat mula sa isang bersyon",all_both:"Panatilihin pareho",combined:"Pinagsamang tala",use_combined:"Gamitin ang pinagsamang teksto",using_combined:"✓ Ginagamit ang pinagsamang teksto",rebuild:"Gawing muli mula sa pinili",custom_badge:"Pinagsama"}
  ,sv:{title:"Granska din sammanslagning",subtitle:"{n} anteckningar redigerades olika i dina säkerhetskopior. Välj vilken version du vill behålla — eller behåll båda.",current:"I din sammanslagning",keep_this:"Behåll denna",kept:"✓ Behållen",keep_both:"Behåll båda",keep_both_on:"✓ Behåller båda",keep_both_hint:"Lägger till den andra versionen som en separat anteckning",modified:"Ändrad",apply:"Tillämpa och ladda ner",applying:"Tillämpar…",skip:"Behåll sammanslagningen som den är",close:"Stäng",untitled:"(namnlös anteckning)",empty:"(tom)",more:"+{n} fler konflikter behåller sammanslagningens automatiska val.",merged_label:"Sammanslaget resultat",suggest:"Föreslå bästa",suggested:"Föreslagen",sg_content:"Har innehåll",sg_newer:"Senaste ändringen",sg_longer:"Mest detaljerad",compare:"Jämför sida vid sida",compare_hide:"Dölj jämförelsen",cmp_hint:"Välj de rader du vill ha från varje version och redigera sedan resultatet om du behöver.",all_cur:"Allt från sammanslagningen",all_alt:"Allt från den andra versionen",all_both:"Behåll båda sidorna",combined:"Sammansatt anteckning",use_combined:"Använd den här sammansatta texten",using_combined:"✓ Använder sammansatt text",rebuild:"Bygg om från valet",custom_badge:"Sammansatt"},ceb:{title:"Susihon ang merge",subtitle:"{n} ka nota ang lain-laing gibag-o sa imong mga backup. Pilia kon unsang bersyon ang tipigan — o tipigan ang pareho.",current:"Sa imong merge",keep_this:"Tipigan kini",kept:"✓ Gitipig",keep_both:"Tipigan pareho",keep_both_on:"✓ Gitipig pareho",keep_both_hint:"Idugang ang laing bersyon isip lain-laing nota",modified:"Gibag-o",apply:"Ilapat ug i-download",applying:"Giilapat…",skip:"Biyaan ang merge",close:"Isira",untitled:"(nota nga walay titulo)",empty:"(wala)",more:"+{n} pa nga conflicts ang mogamit sa awtomatikong pagpili sa merge.",merged_label:"Resulta sa merge",suggest:"Imungkahi ang labing maayo",suggested:"Girekomenda",sg_content:"May sulod",sg_newer:"Pinakabag-o nga pag-edit",sg_longer:"Pinaka-detalyado",compare:"Itandi nga magtapad",compare_hide:"Itago ang pagtandi",cmp_hint:"Pilia ang mga linya nga gusto nimo gikan sa matag bersyon, dayon usba ang resulta kon kinahanglan.",all_cur:"Tanan gikan sa merge",all_alt:"Tanan gikan sa laing bersyon",all_both:"Tipigan ang duha ka kilid",combined:"Gihiusang nota",use_combined:"Gamita kining gihiusang teksto",using_combined:"✓ Gigamit ang gihiusang teksto",rebuild:"Himoa pag-usab gikan sa gipili",custom_badge:"Gihiusa"},el:{title:"Έλεγχος της συγχώνευσής σας",subtitle:"{n} σημειώσεις επεξεργάστηκαν διαφορετικά στα αντίγραφα ασφαλείας σας. Επιλέξτε ποια εκδοχή θα κρατήσετε — ή κρατήστε και τις δύο.",current:"Στη συγχώνευσή σας",keep_this:"Κράτησε αυτή",kept:"✓ Κρατήθηκε",keep_both:"Κράτησε και τις δύο",keep_both_on:"✓ Κρατούνται και οι δύο",keep_both_hint:"Προσθέτει την άλλη εκδοχή ως ξεχωριστή σημείωση",modified:"Επεξεργάστηκε",apply:"Εφαρμογή και λήψη",applying:"Εφαρμογή…",skip:"Διατήρηση της συγχώνευσης ως έχει",close:"Κλείσιμο",untitled:"(σημείωση χωρίς τίτλο)",empty:"(κενή)",more:"+{n} ακόμη διενέξεις θα κρατήσουν την αυτόματη επιλογή της συγχώνευσης.",merged_label:"Συγχωνευμένο αποτέλεσμα",suggest:"Πρότεινε την καλύτερη",suggested:"Προτεινόμενη",sg_content:"Έχει περιεχόμενο",sg_newer:"Πιο πρόσφατη επεξεργασία",sg_longer:"Πιο αναλυτική",compare:"Σύγκριση δίπλα-δίπλα",compare_hide:"Απόκρυψη σύγκρισης",cmp_hint:"Διάλεξε τις γραμμές που θέλεις από κάθε εκδοχή και μετά επεξεργάσου το αποτέλεσμα αν χρειάζεται.",all_cur:"Όλα από τη συγχώνευση",all_alt:"Όλα από την άλλη εκδοχή",all_both:"Κράτησε και τις δύο πλευρές",combined:"Συνδυασμένη σημείωση",use_combined:"Χρήση αυτού του συνδυασμένου κειμένου",using_combined:"✓ Χρησιμοποιείται το συνδυασμένο κείμενο",rebuild:"Ξαναφτιάξ' το από την επιλογή",custom_badge:"Συνδυασμένη"},sw:{title:"Kagua muunganisho wako",subtitle:"Madokezo {n} yalihaririwa kwa njia tofauti kwenye nakala zako rudufu. Chagua toleo la kuhifadhi — au uhifadhi yote mawili.",current:"Katika muunganisho wako",keep_this:"Hifadhi hili",kept:"✓ Limehifadhiwa",keep_both:"Hifadhi yote mawili",keep_both_on:"✓ Yanahifadhiwa yote",keep_both_hint:"Huongeza toleo lingine kama dokezo tofauti",modified:"Limehaririwa",apply:"Tekeleza na upakue",applying:"Inatekeleza…",skip:"Acha muunganisho kama ulivyo",close:"Funga",untitled:"(dokezo lisilo na kichwa)",empty:"(tupu)",more:"+Migongano mingine {n} itahifadhi chaguo la kiotomatiki la muunganisho.",merged_label:"Matokeo yaliyounganishwa",suggest:"Pendekeza bora",suggested:"Limependekezwa",sg_content:"Lina maudhui",sg_newer:"Hariri ya karibuni zaidi",sg_longer:"Lenye maelezo zaidi",compare:"Linganisha ubavu kwa ubavu",compare_hide:"Ficha ulinganisho",cmp_hint:"Chagua mistari unayotaka kutoka kila toleo, kisha hariri matokeo ukihitaji.",all_cur:"Yote kutoka kwa muunganisho",all_alt:"Yote kutoka toleo lingine",all_both:"Hifadhi pande zote mbili",combined:"Dokezo lililounganishwa",use_combined:"Tumia maandishi haya yaliyounganishwa",using_combined:"✓ Yanatumika maandishi yaliyounganishwa",rebuild:"Jenga upya kutoka kwa uliyochagua",custom_badge:"Limeunganishwa"},nl:{title:"Je samenvoeging bekijken",subtitle:"{n} aantekeningen zijn in je back-ups verschillend bewerkt. Kies welke versie je wilt houden — of houd ze allebei.",current:"In je samenvoeging",keep_this:"Deze houden",kept:"✓ Gehouden",keep_both:"Allebei houden",keep_both_on:"✓ Allebei houden",keep_both_hint:"Voegt de andere versie toe als aparte aantekening",modified:"Bewerkt",apply:"Toepassen en downloaden",applying:"Bezig met toepassen…",skip:"Samenvoeging laten zoals ze is",close:"Sluiten",untitled:"(aantekening zonder titel)",empty:"(leeg)",more:"Bij nog {n} conflicten wordt de automatische keuze van de samenvoeging aangehouden.",merged_label:"Samengevoegd resultaat",suggest:"Beste voorstellen",suggested:"Voorgesteld",sg_content:"Heeft inhoud",sg_newer:"Meest recente bewerking",sg_longer:"Meest uitgebreid",compare:"Naast elkaar vergelijken",compare_hide:"Vergelijking verbergen",cmp_hint:"Kies uit elke versie de regels die je wilt en pas het resultaat daarna aan als dat nodig is.",all_cur:"Alles uit de samenvoeging",all_alt:"Alles uit de andere versie",all_both:"Beide kanten houden",combined:"Gecombineerde aantekening",use_combined:"Deze gecombineerde tekst gebruiken",using_combined:"✓ Gecombineerde tekst wordt gebruikt",rebuild:"Opnieuw opbouwen uit selectie",custom_badge:"Gecombineerd"},ro:{title:"Verifică îmbinarea",subtitle:"{n} notițe au fost modificate diferit în copiile tale de rezervă. Alege ce versiune păstrezi — sau păstrează-le pe amândouă.",current:"În îmbinarea ta",keep_this:"Păstreaz-o pe aceasta",kept:"✓ Păstrată",keep_both:"Păstrează-le pe amândouă",keep_both_on:"✓ Le păstrez pe amândouă",keep_both_hint:"Adaugă cealaltă versiune ca notiță separată",modified:"Modificată",apply:"Aplică și descarcă",applying:"Se aplică…",skip:"Lasă îmbinarea așa cum e",close:"Închide",untitled:"(notiță fără titlu)",empty:"(gol)",more:"Încă {n} conflicte vor păstra alegerea automată a îmbinării.",merged_label:"Rezultatul îmbinării",suggest:"Sugerează cea mai bună",suggested:"Sugerată",sg_content:"Are conținut",sg_newer:"Cea mai recentă modificare",sg_longer:"Cea mai detaliată",compare:"Compară una lângă alta",compare_hide:"Ascunde comparația",cmp_hint:"Alege rândurile pe care le vrei din fiecare versiune, apoi modifică rezultatul dacă e nevoie.",all_cur:"Tot din îmbinare",all_alt:"Tot din cealaltă versiune",all_both:"Păstrează ambele părți",combined:"Notiță combinată",use_combined:"Folosește acest text combinat",using_combined:"✓ Se folosește textul combinat",rebuild:"Reconstruiește din selecție",custom_badge:"Combinată"},id:{title:"Tinjau penggabungan Anda",subtitle:"{n} catatan diubah secara berbeda di antara cadangan Anda. Pilih versi mana yang ingin disimpan — atau simpan keduanya.",current:"Dalam gabungan Anda",keep_this:"Simpan yang ini",kept:"✓ Disimpan",keep_both:"Simpan keduanya",keep_both_on:"✓ Menyimpan keduanya",keep_both_hint:"Menambahkan versi satunya sebagai catatan terpisah",modified:"Diubah",apply:"Terapkan & unduh",applying:"Menerapkan…",skip:"Biarkan gabungan apa adanya",close:"Tutup",untitled:"(catatan tanpa judul)",empty:"(kosong)",more:"+{n} konflik lainnya akan mengikuti pilihan otomatis dari penggabungan.",merged_label:"Hasil gabungan",suggest:"Sarankan yang terbaik",suggested:"Disarankan",sg_content:"Ada isinya",sg_newer:"Perubahan terbaru",sg_longer:"Paling rinci",compare:"Bandingkan berdampingan",compare_hide:"Sembunyikan perbandingan",cmp_hint:"Pilih baris yang Anda inginkan dari tiap versi, lalu ubah hasilnya jika perlu.",all_cur:"Semua dari gabungan",all_alt:"Semua dari versi satunya",all_both:"Simpan kedua sisi",combined:"Catatan gabungan",use_combined:"Pakai teks gabungan ini",using_combined:"✓ Memakai teks gabungan",rebuild:"Susun ulang dari pilihan",custom_badge:"Gabungan"},hi:{title:"अपना मर्ज जाँचें",subtitle:"{n} नोट आपके बैकअप में अलग-अलग तरह से बदले गए थे। चुनें कि कौन-सा वर्शन रखना है — या दोनों रखें।",current:"आपके मर्ज में",keep_this:"यह रखें",kept:"✓ रखा गया",keep_both:"दोनों रखें",keep_both_on:"✓ दोनों रखे जा रहे हैं",keep_both_hint:"दूसरा वर्शन अलग नोट के रूप में जोड़ता है",modified:"बदला गया",apply:"लागू करें और डाउनलोड करें",applying:"लागू किया जा रहा है…",skip:"मर्ज को जैसा है वैसा रहने दें",close:"बंद करें",untitled:"(बिना शीर्षक का नोट)",empty:"(खाली)",more:"+{n} और टकरावों में मर्ज का अपने आप किया गया चुनाव लागू रहेगा।",merged_label:"मर्ज का नतीजा",suggest:"बेहतर सुझाएँ",suggested:"सुझाया गया",sg_content:"इसमें सामग्री है",sg_newer:"सबसे हाल का बदलाव",sg_longer:"सबसे विस्तृत",compare:"आमने-सामने तुलना करें",compare_hide:"तुलना छिपाएँ",cmp_hint:"हर वर्शन से वे पंक्तियाँ चुनें जो आप रखना चाहते हैं, फिर ज़रूरत हो तो नतीजा बदल लें।",all_cur:"मर्ज से सब कुछ",all_alt:"दूसरे वर्शन से सब कुछ",all_both:"दोनों तरफ़ के रखें",combined:"मिलाया हुआ नोट",use_combined:"यही मिलाया हुआ टेक्स्ट इस्तेमाल करें",using_combined:"✓ मिलाया हुआ टेक्स्ट इस्तेमाल हो रहा है",rebuild:"चुनाव से दोबारा बनाएँ",custom_badge:"मिलाया हुआ"},hu:{title:"Nézd át az egyesítést",subtitle:"{n} jegyzetet eltérően szerkesztettél a mentéseidben. Válaszd ki, melyik verziót tartod meg — vagy tartsd meg mindkettőt.",current:"Az egyesítésben",keep_this:"Ezt tartom meg",kept:"✓ Megtartva",keep_both:"Mindkettő megtartása",keep_both_on:"✓ Mindkettő megmarad",keep_both_hint:"A másik verziót külön jegyzetként adja hozzá",modified:"Szerkesztve",apply:"Alkalmaz és letölt",applying:"Alkalmazás…",skip:"Marad az egyesítés úgy, ahogy van",close:"Bezárás",untitled:"(cím nélküli jegyzet)",empty:"(üres)",more:"+{n} további ütközésnél az egyesítés automatikus választása marad érvényben.",merged_label:"Egyesített eredmény",suggest:"Javasold a jobbat",suggested:"Javasolt",sg_content:"Van benne tartalom",sg_newer:"Legutóbbi szerkesztés",sg_longer:"Legrészletesebb",compare:"Összehasonlítás egymás mellett",compare_hide:"Összehasonlítás elrejtése",cmp_hint:"Válaszd ki mindkét változatból a megtartandó sorokat, majd szükség esetén szerkeszd az eredményt.",all_cur:"Minden az egyesítésből",all_alt:"Minden a másik változatból",all_both:"Mindkét oldal megtartása",combined:"Összevont jegyzet",use_combined:"Ezt az összevont szöveget használom",using_combined:"✓ Az összevont szöveg van használatban",rebuild:"Újraépítés a kijelölésből",custom_badge:"Összevont"},vi:{title:"Xem lại lần hợp nhất của bạn",subtitle:"{n} ghi chú được sửa khác nhau giữa các bản sao lưu. Hãy chọn phiên bản muốn giữ — hoặc giữ cả hai.",current:"Trong bản hợp nhất",keep_this:"Giữ bản này",kept:"✓ Đã giữ",keep_both:"Giữ cả hai",keep_both_on:"✓ Đang giữ cả hai",keep_both_hint:"Thêm phiên bản kia thành một ghi chú riêng",modified:"Đã sửa",apply:"Áp dụng & tải về",applying:"Đang áp dụng…",skip:"Giữ nguyên bản hợp nhất",close:"Đóng",untitled:"(ghi chú không tiêu đề)",empty:"(trống)",more:"+{n} xung đột nữa sẽ theo lựa chọn tự động của bản hợp nhất.",merged_label:"Kết quả hợp nhất",suggest:"Gợi ý bản tốt nhất",suggested:"Được gợi ý",sg_content:"Có nội dung",sg_newer:"Sửa gần đây nhất",sg_longer:"Chi tiết nhất",compare:"So sánh cạnh nhau",compare_hide:"Ẩn phần so sánh",cmp_hint:"Chọn những dòng bạn muốn giữ từ mỗi phiên bản, rồi sửa lại kết quả nếu cần.",all_cur:"Lấy hết từ bản hợp nhất",all_alt:"Lấy hết từ phiên bản kia",all_both:"Giữ cả hai bên",combined:"Ghi chú đã kết hợp",use_combined:"Dùng đoạn văn bản đã kết hợp này",using_combined:"✓ Đang dùng văn bản đã kết hợp",rebuild:"Dựng lại theo lựa chọn",custom_badge:"Đã kết hợp"},"yue-Hant":{title:"檢查今次合併",subtitle:"有 {n} 條筆記喺唔同備份入面改成咗唔同內容。請揀保留邊個版本——或者兩個都保留。",current:"喺你嘅合併結果入面",keep_this:"保留呢條",kept:"✓ 已保留",keep_both:"兩個都保留",keep_both_on:"✓ 兩個都保留",keep_both_hint:"會將另一個版本加做獨立嘅筆記",modified:"已修改",apply:"套用並下載",applying:"套用緊……",skip:"維持合併結果唔變",close:"閂咗佢",untitled:"（冇標題嘅筆記）",empty:"（空白）",more:"另外仲有 {n} 處衝突會用合併時嘅自動選擇。",merged_label:"合併結果",suggest:"建議較好嗰個",suggested:"已建議",sg_content:"有內容",sg_newer:"最近改過",sg_longer:"內容最詳細",compare:"左右並排比較",compare_hide:"收埋比較",cmp_hint:"喺兩個版本入面揀你想要嘅行，之後有需要就自己改下個結果。",all_cur:"合併結果全部要",all_alt:"另一個版本全部要",all_both:"兩邊都保留",combined:"合埋嘅筆記",use_combined:"用呢段合埋嘅文字",using_combined:"✓ 用緊合埋嘅文字",rebuild:"照所揀嘅重新砌過",custom_badge:"已合埋"},"zh-Hant":{title:"檢查這次合併",subtitle:"有 {n} 條筆記在不同備份中被改成了不同內容。請選擇保留哪個版本——或者兩個都保留。",current:"在你的合併結果中",keep_this:"保留這條",kept:"✓ 已保留",keep_both:"兩個都保留",keep_both_on:"✓ 兩個都保留",keep_both_hint:"會把另一個版本新增為獨立的筆記",modified:"已修改",apply:"應用並下載",applying:"正在應用……",skip:"保持合併結果不變",close:"關閉",untitled:"（無標題筆記）",empty:"（空）",more:"另有 {n} 處衝突將採用合併時的自動選擇。",merged_label:"合併結果",suggest:"推薦較佳版本",suggested:"已推薦",sg_content:"有內容",sg_newer:"最近修改",sg_longer:"內容最詳細",compare:"並排比較",compare_hide:"隱藏比較",cmp_hint:"從兩個版本中挑出你要保留的行，然後視需要修改結果。",all_cur:"全部取自合併結果",all_alt:"全部取自另一個版本",all_both:"兩邊都保留",combined:"合併後的筆記",use_combined:"使用這段合併後的文字",using_combined:"✓ 正在使用合併後的文字",rebuild:"依所選重新產生",custom_badge:"已合併"},"zh-Hans":{title:"检查这次合并",subtitle:"有 {n} 条笔记在不同备份中被改成了不同内容。请选择保留哪个版本——或者两个都保留。",current:"在你的合并结果中",keep_this:"保留这条",kept:"✓ 已保留",keep_both:"两个都保留",keep_both_on:"✓ 两个都保留",keep_both_hint:"会把另一个版本添加为独立的笔记",modified:"已修改",apply:"应用并下载",applying:"正在应用……",skip:"保持合并结果不变",close:"关闭",untitled:"（无标题笔记）",empty:"（空）",more:"另有 {n} 处冲突将采用合并时的自动选择。",merged_label:"合并结果",suggest:"推荐较佳版本",suggested:"已推荐",sg_content:"有内容",sg_newer:"最近修改",sg_longer:"内容最详细",compare:"并排比较",compare_hide:"隐藏比较",cmp_hint:"从两个版本中挑出你要保留的行，然后按需要修改结果。",all_cur:"全部取自合并结果",all_alt:"全部取自另一个版本",all_both:"两边都保留",combined:"合并后的笔记",use_combined:"使用这段合并后的文字",using_combined:"✓ 正在使用合并后的文字",rebuild:"按所选重新生成",custom_badge:"已合并"},pl:{title:"Sprawdź scalanie",subtitle:"{n} notatek zostało zmienionych inaczej w różnych kopiach zapasowych. Wybierz, którą wersję zachować — albo zachowaj obie.",current:"W Twoim scaleniu",keep_this:"Zachowaj tę",kept:"✓ Zachowano",keep_both:"Zachowaj obie",keep_both_on:"✓ Zachowujemy obie",keep_both_hint:"Dodaje drugą wersję jako osobną notatkę",modified:"Zmieniono",apply:"Zastosuj i pobierz",applying:"Stosowanie…",skip:"Zostaw scalanie bez zmian",close:"Zamknij",untitled:"(notatka bez tytułu)",empty:"(puste)",more:"Kolejne +{n} konfliktów zachowa automatyczny wybór scalania.",merged_label:"Wynik scalania",suggest:"Zaproponuj najlepszą",suggested:"Zaproponowano",sg_content:"Ma treść",sg_newer:"Najnowsza zmiana",sg_longer:"Najbardziej szczegółowa",compare:"Porównaj obok siebie",compare_hide:"Ukryj porównanie",cmp_hint:"Wybierz z każdej wersji wiersze, które chcesz zachować, a potem w razie potrzeby popraw wynik.",all_cur:"Wszystko ze scalenia",all_alt:"Wszystko z drugiej wersji",all_both:"Zachowaj obie strony",combined:"Połączona notatka",use_combined:"Użyj tego połączonego tekstu",using_combined:"✓ Używam połączonego tekstu",rebuild:"Zbuduj na nowo z zaznaczenia",custom_badge:"Połączona"},uk:{title:"Перевірте об'єднання",subtitle:"{n} нотаток були відредаговані по-різному в різних резервних копіях. Виберіть, яку версію залишити, — або залиште обидві.",current:"У вашому об'єднанні",keep_this:"Залишити цю",kept:"✓ Залишено",keep_both:"Залишити обидві",keep_both_on:"✓ Залишаємо обидві",keep_both_hint:"Додає другу версію як окрему нотатку",modified:"Відредаговано",apply:"Застосувати і завантажити",applying:"Застосовуємо…",skip:"Залишити об'єднання як є",close:"Закрити",untitled:"(нотатка без назви)",empty:"(порожньо)",more:"Ще +{n} конфліктів збережуть автоматичний вибір об'єднання.",merged_label:"Об'єднаний результат",suggest:"Запропонувати найкращу",suggested:"Запропоновано",sg_content:"Має вміст",sg_newer:"Найновіша редакція",sg_longer:"Найдетальніша",compare:"Порівняти поруч",compare_hide:"Сховати порівняння",cmp_hint:"Виберіть рядки, які хочете залишити з кожної версії, а потім за потреби відредагуйте результат.",all_cur:"Усе з об'єднання",all_alt:"Усе з іншої версії",all_both:"Залишити обидві сторони",combined:"Об'єднана нотатка",use_combined:"Використати цей об'єднаний текст",using_combined:"✓ Використовується об'єднаний текст",rebuild:"Зібрати заново з вибраного",custom_badge:"Об'єднано"},he:{title:"בדקו את המיזוג",subtitle:"{n} הערות נערכו בצורה שונה בין הגיבויים שלכם. בחרו איזו גרסה לשמור — או שמרו את שתיהן.",current:"במיזוג שלכם",keep_this:"שמור את זו",kept:"✓ נשמרה",keep_both:"שמור את שתיהן",keep_both_on:"✓ שומר את שתיהן",keep_both_hint:"מוסיף את הגרסה השנייה כהערה נפרדת",modified:"נערכה",apply:"החלה והורדה",applying:"מחיל…",skip:"השאר את המיזוג כפי שהוא",close:"סגירה",untitled:"(הערה ללא כותרת)",empty:"(ריק)",more:"+{n} התנגשויות נוספות ישמרו על הבחירה האוטומטית של המיזוג.",merged_label:"התוצאה הממוזגת",suggest:"הצע את הטובה ביותר",suggested:"מוצע",sg_content:"יש בה תוכן",sg_newer:"העריכה האחרונה",sg_longer:"המפורטת ביותר",compare:"השוואה זו מול זו",compare_hide:"הסתרת ההשוואה",cmp_hint:"בחרו מכל גרסה את השורות שאתם רוצים, ואז ערכו את התוצאה אם צריך.",all_cur:"הכול מהמיזוג",all_alt:"הכול מהגרסה השנייה",all_both:"שמור את שני הצדדים",combined:"הערה משולבת",use_combined:"השתמש בטקסט המשולב הזה",using_combined:"✓ הטקסט המשולב בשימוש",rebuild:"בנייה מחדש לפי הבחירה",custom_badge:"משולבת"},ar:{title:"راجِع عملية الدمج",subtitle:"جرى تعديل {n} ملاحظة بصور مختلفة بين نسخك الاحتياطية. اختر النسخة التي تريد الاحتفاظ بها — أو احتفظ بالاثنتين.",current:"في ملف الدمج",keep_this:"احتفظ بهذه",kept:"✓ تم الاحتفاظ",keep_both:"احتفظ بالاثنتين",keep_both_on:"✓ الاحتفاظ بالاثنتين",keep_both_hint:"يضيف النسخة الأخرى كملاحظة مستقلة",modified:"مُعدَّلة",apply:"تطبيق وتنزيل",applying:"جارٍ التطبيق…",skip:"أبقِ الدمج كما هو",close:"إغلاق",untitled:"(ملاحظة بلا عنوان)",empty:"(فارغة)",more:"+{n} تعارض إضافي سيبقى على الاختيار التلقائي للدمج.",merged_label:"نتيجة الدمج",suggest:"اقترح الأفضل",suggested:"مُقترَحة",sg_content:"تحتوي على محتوى",sg_newer:"أحدث تعديل",sg_longer:"الأكثر تفصيلًا",compare:"مقارنة جنبًا إلى جنب",compare_hide:"إخفاء المقارنة",cmp_hint:"اختر الأسطر التي تريدها من كل نسخة، ثم عدِّل النتيجة إن احتجت.",all_cur:"كل شيء من ملف الدمج",all_alt:"كل شيء من النسخة الأخرى",all_both:"احتفظ بالجانبين",combined:"ملاحظة مدمجة",use_combined:"استخدم هذا النص المدمج",using_combined:"✓ يُستخدم النص المدمج",rebuild:"أعِد البناء من الاختيار",custom_badge:"مدمجة"}};
  function curLang() { try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; } }
  function t(k) { var l = curLang(); return (I18N[l] && I18N[l][k]) || I18N.en[k] || k; }
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function stripHtml(s) { return String(s || '').replace(/<[^>]*>?/gm, ' ').replace(/\s+/g, ' ').trim(); }
  function clip(s) { s = String(s || ''); return s.length > 1400 ? s.slice(0, 1400) + '…' : s; }
  function fmtDate(s) {
    if (!s) return '';
    var d = new Date(s);
    if (isNaN(d.getTime())) return String(s);
    try { return d.toLocaleString(undefined, { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }); }
    catch (_) { return d.toISOString().slice(0, 16).replace('T', ' '); }
  }

  // ── Lightweight word-level diff (LCS) ──────────────────────────────
  function lcsDiff(o, n) {
    var m = o.length, k = n.length;
    var dp = []; for (var i = 0; i <= m; i++) dp.push(new Array(k + 1).fill(0));
    for (var a = m - 1; a >= 0; a--) for (var b = k - 1; b >= 0; b--)
      dp[a][b] = (o[a] === n[b]) ? dp[a + 1][b + 1] + 1 : Math.max(dp[a + 1][b], dp[a][b + 1]);
    var out = [], x = 0, y = 0;
    while (x < m && y < k) {
      if (o[x] === n[y]) { out.push({ t: 'eq', s: n[y] }); x++; y++; }
      else if (dp[x + 1][y] >= dp[x][y + 1]) { out.push({ t: 'del', s: o[x] }); x++; }
      else { out.push({ t: 'add', s: n[y] }); y++; }
    }
    while (x < m) out.push({ t: 'del', s: o[x++] });
    while (y < k) out.push({ t: 'add', s: n[y++] });
    return out;
  }
  function diffHtml(curPlain, altPlain) {
    var a = clip(curPlain).split(/(\s+)/), b = clip(altPlain).split(/(\s+)/);
    if (a.length > 600) a = a.slice(0, 600);
    if (b.length > 600) b = b.slice(0, 600);
    return lcsDiff(a, b).map(function (p) {
      if (p.t === 'eq') return esc(p.s);
      if (p.t === 'add') return '<span class="jcr-ins">' + esc(p.s) + '</span>';
      return '<span class="jcr-del">' + esc(p.s) + '</span>';
    }).join('');
  }

  // ── Line-aligned comparison + combine (v3.44.0) ────────────────────
  // The card diff above answers "what changed". These answer "which parts of
  // each version do I want", which is the question the automatic merge had to
  // guess at: notes are compared line by line the way a code review shows a
  // patch, so a paragraph added on the phone and a sentence fixed on the
  // tablet can both survive into one note instead of one erasing the other.
  var ENT = { '&nbsp;': ' ', '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&apos;': "'" };
  function unent(s) {
    return String(s == null ? '' : s).replace(/&nbsp;|&amp;|&lt;|&gt;|&quot;|&#39;|&apos;/g, function (m) { return ENT[m]; });
  }
  // stripHtml() flattens a note to one line — right for comparing identity,
  // wrong for a line-by-line view. This keeps the paragraph breaks.
  function toPlainText(html) {
    var s = String(html == null ? '' : html)
      .replace(/<\s*br\s*\/?\s*>/gi, '\n')
      .replace(/<\/\s*(?:p|div|li|h[1-6]|tr|blockquote)\s*>/gi, '\n')
      .replace(/<[^>]*>/g, '');
    s = unent(s).replace(/\r\n?/g, '\n');
    s = s.split('\n').map(function (l) { return l.replace(/[ \t ]+/g, ' ').trim(); }).join('\n');
    return s.replace(/\n{3,}/g, '\n\n').replace(/^\n+|\n+$/g, '');
  }
  function toPlainLines(html) { var s = toPlainText(html); return s ? s.split('\n') : []; }
  function isHtmlNote(s) { return /<(?:p|br|b|i|u|em|strong|ul|ol|li|div)\b/i.test(String(s == null ? '' : s)); }
  // Write the combined text back in the shape the note was already stored in.
  // Wrapping a plain-text note in <p> tags would render as literal markup in
  // JW Library, and stripping tags off an HTML one would lose its formatting.
  function textToContent(text, sample) {
    text = String(text == null ? '' : text);
    if (!isHtmlNote(sample)) return text;
    return text.split(/\n{2,}/).map(function (p) {
      p = p.trim();
      return p ? '<p>' + esc(p).replace(/\n/g, '<br />') + '</p>' : '';
    }).filter(Boolean).join('');
  }
  // Word-level diff of one changed line, split across the two columns: the
  // left keeps its removed words, the right shows what replaced them.
  function wordPair(l, r) {
    var a = String(l == null ? '' : l).split(/(\s+)/), b = String(r == null ? '' : r).split(/(\s+)/);
    if (a.length > 240 || b.length > 240) return { l: esc(l), r: esc(r) };
    var lh = '', rh = '';
    lcsDiff(a, b).forEach(function (p) {
      if (p.t === 'eq') { lh += esc(p.s); rh += esc(p.s); }
      else if (p.t === 'del') lh += '<span class="jcr-del">' + esc(p.s) + '</span>';
      else rh += '<span class="jcr-ins">' + esc(p.s) + '</span>';
    });
    return { l: lh, r: rh };
  }
  // Turn a flat line diff into aligned rows. Consecutive removals and
  // additions are paired up so an edited line sits opposite its replacement
  // rather than scrolling past it.
  function alignLines(la, lb) {
    var ops = lcsDiff(la, lb), rows = [], i = 0;
    while (i < ops.length) {
      if (ops[i].t === 'eq') { rows.push({ t: 'eq', l: ops[i].s, r: ops[i].s }); i++; continue; }
      var dels = [], adds = [];
      while (i < ops.length && ops[i].t !== 'eq') { (ops[i].t === 'del' ? dels : adds).push(ops[i].s); i++; }
      var n = Math.max(dels.length, adds.length);
      for (var k = 0; k < n; k++) {
        if (k < dels.length && k < adds.length) rows.push({ t: 'chg', l: dels[k], r: adds[k] });
        else if (k < dels.length) rows.push({ t: 'del', l: dels[k], r: null });
        else rows.push({ t: 'add', l: null, r: adds[k] });
      }
    }
    return rows;
  }
  // Ticks start out reproducing the merge exactly, so opening the comparison
  // never changes the outcome on its own.
  function defaultInc(rows) {
    return rows.map(function (row) { return { l: row.l != null, r: false }; });
  }
  function combineText(rows, inc) {
    var out = [];
    rows.forEach(function (row, i) {
      var st = inc[i] || {};
      if (row.t === 'eq') { out.push(row.l); return; }
      if (row.l != null && st.l) out.push(row.l);
      if (row.r != null && st.r) out.push(row.r);
    });
    return out.join('\n').replace(/\n{3,}/g, '\n\n').replace(/^\n+|\n+$/g, '');
  }

  // ── Source-file + DB helpers (all main-thread sql.js) ──────────────
  function readFileBuf(file) {
    if (!file) return Promise.reject(new Error('no file'));
    if (typeof file.arrayBuffer === 'function') return file.arrayBuffer();
    return new Promise(function (res, rej) {
      var r = new FileReader();
      r.onload = function () { res(r.result); };
      r.onerror = function () { rej(new Error('read failed')); };
      r.readAsArrayBuffer(file);
    });
  }
  function collectSourceFiles() {
    var out = [], seen = {};
    var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
    for (var i = 0; i < inputs.length; i++) {
      var fl = inputs[i].files; if (!fl) continue;
      for (var j = 0; j < fl.length; j++) {
        var f = fl[j]; if (!f) continue;
        var key = (f.name || '') + '::' + (f.size || 0);
        if (seen[key]) continue; seen[key] = 1; out.push(f);
      }
    }
    try {
      if (window.__jwLastFile) {
        var lf = window.__jwLastFile, k = (lf.name || '') + '::' + (lf.size || 0);
        if (!seen[k]) { seen[k] = 1; out.push(lf); }
      }
    } catch (_) {}
    return out;
  }
  function openDbFromBuffer(SQL, buf) {
    return window.JSZip.loadAsync(buf).then(function (zip) {
      var key = Object.keys(zip.files).find(function (f) { return /userdata\.db$/i.test(f); });
      if (!key) return null;
      return zip.file(key).async('uint8array').then(function (bytes) { return new SQL.Database(bytes); });
    });
  }
  function queryNotes(db) {
    var map = {};
    try {
      var r = db.exec('SELECT Guid,Title,Content,LastModified FROM Note');
      if (r.length && r[0].values) r[0].values.forEach(function (v) {
        if (v[0] == null) return;
        map[v[0]] = { title: v[1] || '', content: v[2] || '', lastMod: v[3] || '' };
      });
    } catch (_) {}
    return map;
  }

  // ── Detection: which notes were edited differently across backups ──
  function detect(opts) {
    if (typeof window.JSZip !== 'function' || typeof window.initSqlJs !== 'function') return Promise.resolve(null);
    var sources = collectSourceFiles();
    if (sources.length < 2) return Promise.resolve(null);
    var SQL;
    return window.initSqlJs({ locateFile: function (f) { return SQLJS_URL + f; } })
      .then(function (s) {
        SQL = s;
        return sources.reduce(function (chain, file, idx) {
          return chain.then(function (acc) {
            return readFileBuf(file)
              .then(function (buf) { return openDbFromBuffer(SQL, buf); })
              .then(function (db) {
                if (db) { acc.push({ name: file.name || ('Backup ' + (idx + 1)), notes: queryNotes(db) }); db.close(); }
                return acc;
              })
              .catch(function () { return acc; });
          });
        }, Promise.resolve([]));
      })
      .then(function (perFile) {
        if (perFile.length < 2) return null;
        return fetch(opts.blobUrl).then(function (r) { return r.arrayBuffer(); }).then(function (mergedBuf) {
          return openDbFromBuffer(SQL, mergedBuf).then(function (mdb) {
            if (!mdb) return null;
            var mergedNotes = queryNotes(mdb); mdb.close();

            var byGuid = {};
            perFile.forEach(function (pf) {
              Object.keys(pf.notes).forEach(function (guid) {
                var note = pf.notes[guid];
                (byGuid[guid] = byGuid[guid] || []).push({
                  file: pf.name, title: note.title, content: note.content,
                  key: stripHtml(note.content).toLowerCase(), lastMod: note.lastMod
                });
              });
            });

            var conflicts = [];
            Object.keys(byGuid).forEach(function (guid) {
              var list = byGuid[guid];
              if (list.length < 2) return;
              var variants = {};
              list.forEach(function (it) {
                if (!variants[it.key]) variants[it.key] = { key: it.key, content: it.content, title: it.title, plain: stripHtml(it.content), lastMod: it.lastMod, files: [it.file] };
                else { variants[it.key].files.push(it.file); if (String(it.lastMod) > String(variants[it.key].lastMod)) variants[it.key].lastMod = it.lastMod; }
              });
              var keys = Object.keys(variants);
              if (keys.length < 2) return; // identical everywhere → no conflict
              var varr = keys.map(function (k) { return variants[k]; });
              var mn = mergedNotes[guid];
              var curKey = mn ? stripHtml(mn.content).toLowerCase() : null;
              var curIdx = -1;
              for (var x = 0; x < varr.length; x++) { if (curKey != null && varr[x].key === curKey) { curIdx = x; break; } }
              if (curIdx === -1 && mn) {
                varr.unshift({ key: curKey, content: mn.content, title: mn.title, plain: stripHtml(mn.content), lastMod: mn.lastMod, files: [t('merged_label')], synthetic: true });
                curIdx = 0;
              }
              if (curIdx === -1) curIdx = 0;
              conflicts.push({ guid: guid, title: (mn && mn.title) || varr[curIdx].title || '', variants: varr, current: curIdx });
            });

            if (!conflicts.length) return null;
            // Stable order: most-recently-edited conflicts first
            conflicts.sort(function (p, q) {
              var pm = p.variants.reduce(function (a, v) { return String(v.lastMod) > a ? String(v.lastMod) : a; }, '');
              var qm = q.variants.reduce(function (a, v) { return String(v.lastMod) > a ? String(v.lastMod) : a; }, '');
              return qm < pm ? -1 : (qm > pm ? 1 : 0);
            });
            return { conflicts: conflicts, mergedBuf: mergedBuf, SQL: SQL };
          });
        });
      })
      .catch(function () { return null; });
  }

  // ── Apply overrides to the merged DB on the main thread ────────────
  function insertDup(db, cols, vals, variant) {
    var ic = [], iv = [];
    var ng = (window.crypto && crypto.randomUUID) ? crypto.randomUUID().toUpperCase() : ('JWSYNC-' + Date.now() + '-' + Math.random().toString(16).slice(2));
    for (var i = 0; i < cols.length; i++) {
      var c = cols[i]; if (c === 'NoteId') continue;
      var v = vals[i];
      if (c === 'Guid') v = ng;
      else if (c === 'Title') v = variant.title;
      else if (c === 'Content') v = variant.content;
      else if (c === 'LastModified') v = variant.lastMod || new Date().toISOString();
      ic.push('"' + c + '"'); iv.push(v);
    }
    db.run('INSERT INTO Note (' + ic.join(',') + ') VALUES (' + ic.map(function () { return '?'; }).join(',') + ')', iv);
  }
  function applyResolutions(ctx, resolutions) {
    var changed = false;
    return openDbFromBuffer(ctx.SQL, ctx.mergedBuf.slice(0)).then(function (db) {
      if (!db) return null;
      ctx.conflicts.forEach(function (cf, i) {
        var res = resolutions[i]; if (!res) return;
        if (res.choice === 'both') {
          var others = cf.variants.filter(function (_, idx) { return idx !== cf.current; });
          if (!others.length) return;
          try {
            var st = db.prepare('SELECT * FROM Note WHERE Guid = :g');
            st.bind({ ':g': cf.guid });
            var cols = null, vals = null;
            if (st.step()) { cols = st.getColumnNames(); vals = st.get(); }
            st.free();
            if (cols && vals) others.forEach(function (v) { try { insertDup(db, cols, vals, v); changed = true; } catch (_) {} });
          } catch (_) {}
        } else if (res.choice === 'custom') {
          // A combined note is a new edit, not one of the two originals, so it
          // is written back in whatever shape the note was already stored in.
          var txt = String(res.text == null ? '' : res.text);
          if (!txt.trim()) return;
          var base = cf.variants[cf.current] || cf.variants[0];
          try { db.run('UPDATE Note SET Content = ?, LastModified = ? WHERE Guid = ?', [textToContent(txt, base && base.content), new Date().toISOString(), cf.guid]); changed = true; } catch (_) {}
        } else if (typeof res.choice === 'number' && res.choice !== cf.current) {
          var v = cf.variants[res.choice]; if (!v) return;
          try { db.run('UPDATE Note SET Title = ?, Content = ?, LastModified = ? WHERE Guid = ?', [v.title, v.content, v.lastMod || new Date().toISOString(), cf.guid]); changed = true; } catch (_) {}
        }
      });
      if (!changed) { try { db.close(); } catch (_) {} return null; }
      if (window.__jwFinalizeBackup) window.__jwFinalizeBackup.touchLastModified(db);
      var out = db.export();
      try { db.close(); } catch (_) {}
      return window.JSZip.loadAsync(ctx.mergedBuf.slice(0)).then(function (zip) {
        var key = Object.keys(zip.files).find(function (f) { return /userdata\.db$/i.test(f); });
        // manifest.json has to describe the database we just wrote, not the one
        // the merge produced — see js/jwlibrary-manifest.js. Leave its hash
        // pointing at the old database and JW Library refuses the corrected
        // file *silently*, which looks exactly like the reviewer corrupting it.
        var ready = window.__jwFinalizeBackup
          ? window.__jwFinalizeBackup(zip, key, out)
          : Promise.resolve(zip.file(key, out));
        return ready.then(function () { return zip.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' }); });
      }).then(function (arr) {
        var url = URL.createObjectURL(new Blob([arr], { type: 'application/octet-stream' }));
        return { blobUrl: url, buffer: arr };
      });
    }).catch(function () { return null; });
  }

  // ── Public entry: called by the celebration before it shows ────────
  window.__jwConflictReview = function (opts) {
    opts = opts || {};
    return new Promise(function (resolve) {
      var settled = false, overlay = null;
      var refreshers = [], suggestions = {};
      function done(v) { if (settled) return; settled = true; cleanup(); resolve(v); }
      function cleanup() {
        if (overlay) { overlay.remove(); overlay = null; }
        document.body.classList.remove('jw-modal-open');
        document.removeEventListener('keydown', onKey);
      }
      function onKey(e) { if (e.key === 'Escape') done(null); }

      detect(opts).then(function (ctx) {
        if (!ctx) { done(null); return; }
        render(ctx);
      }).catch(function () { done(null); });

      function render(ctx) {
        var MAX = 100;
        var resolutions = ctx.conflicts.map(function (cf) { return { choice: cf.current }; });
        var shown = ctx.conflicts.slice(0, MAX);
        refreshers.length = 0; suggestions = {};

        var warnIcon = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 2 19a1 1 0 0 0 .87 1.5h18.26A1 1 0 0 0 22 19L12 2z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
        var dlIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';

        var html =
          '<div class="jcr-backdrop" data-jcr-skip></div>' +
          '<div class="jcr-card" role="dialog" aria-modal="true" aria-labelledby="jcr-title">' +
            '<button class="jcr-close" type="button" data-jcr-skip aria-label="' + esc(t('close')) + '">×</button>' +
            '<div class="jcr-head">' +
              '<div class="jcr-icon">' + warnIcon + '</div>' +
              '<div><h2 id="jcr-title" class="jcr-title">' + esc(t('title')) + '</h2>' +
              '<p class="jcr-subtitle">' + esc(t('subtitle').replace('{n}', ctx.conflicts.length)) + '</p></div>' +
            '</div>' +
            '<div class="jcr-body" id="jcr-body"></div>' +
            (ctx.conflicts.length > MAX ? '<div class="jcr-more">' + esc(t('more').replace('{n}', ctx.conflicts.length - MAX)) + '</div>' : '') +
            '<div class="jcr-foot">' +
              '<button class="jcr-btn jcr-btn-ghost jcr-btn-suggest" type="button" data-jcr-suggest>' + esc(t('suggest')) + '</button>' +
              '<button class="jcr-btn jcr-btn-ghost" type="button" data-jcr-skip>' + esc(t('skip')) + '</button>' +
              '<button class="jcr-btn jcr-btn-primary" type="button" data-jcr-apply>' + dlIcon + '<span>' + esc(t('apply')) + '</span></button>' +
            '</div>' +
          '</div>';

        overlay = document.createElement('div');
        overlay.id = 'jw-conflict-overlay';
        overlay.innerHTML = html;
        document.body.appendChild(overlay);
        document.body.classList.add('jw-modal-open');

        var body = overlay.querySelector('#jcr-body');
        shown.forEach(function (cf, ci) { body.appendChild(buildConflict(cf, ci, resolutions)); });

        overlay.querySelectorAll('[data-jcr-skip]').forEach(function (el) {
          el.addEventListener('click', function () { done(null); });
        });
        var applyBtn = overlay.querySelector('[data-jcr-apply]');
        applyBtn.addEventListener('click', function () {
          applyBtn.disabled = true;
          var span = applyBtn.querySelector('span'); if (span) span.textContent = t('applying');
          applyResolutions(ctx, resolutions).then(function (r) { done(r); }).catch(function () { done(null); });
        });
        var suggestBtn = overlay.querySelector('[data-jcr-suggest]');
        if (suggestBtn) suggestBtn.addEventListener('click', function () {
          shown.forEach(function (cf, ci) { var s = suggestFor(cf); suggestions[ci] = s; if (s.reason) resolutions[ci] = { choice: s.vi }; });
          refreshers.forEach(function (fn) { fn(); });
        });
        document.addEventListener('keydown', onKey);
      }

      function suggestFor(cf) {
        var vs = cf.variants, nonEmpty = [];
        vs.forEach(function (v, i) { if (v.plain && v.plain.trim().length > 0) nonEmpty.push(i); });
        if (nonEmpty.length === 0) return { vi: cf.current, reason: null };
        if (nonEmpty.length === 1) return { vi: nonEmpty[0], reason: 'sg_content' };
        var withDate = nonEmpty.filter(function (i) { return vs[i].lastMod; });
        if (withDate.length === nonEmpty.length) {
          var sorted = withDate.slice().sort(function (a2, b2) { return new Date(vs[b2].lastMod) - new Date(vs[a2].lastMod); });
          if (new Date(vs[sorted[0]].lastMod).getTime() !== new Date(vs[sorted[1]].lastMod).getTime())
            return { vi: sorted[0], reason: 'sg_newer' };
        }
        var longest = nonEmpty.slice().sort(function (a2, b2) { return vs[b2].plain.length - vs[a2].plain.length; })[0];
        return { vi: longest, reason: 'sg_longer' };
      }

      function buildConflict(cf, ci, resolutions) {
        var wrap = document.createElement('div');
        wrap.className = 'jcr-conflict';
        var title = cf.title ? stripHtml(cf.title) : t('untitled');

        var head = document.createElement('div');
        head.className = 'jcr-conflict-head';
        head.innerHTML = '<span class="jcr-conflict-n">' + (ci + 1) + '</span><span class="jcr-conflict-title">' + esc(title) + '</span>';
        var customBadge = document.createElement('span');
        customBadge.className = 'jcr-custom-badge';
        customBadge.textContent = t('custom_badge');
        customBadge.hidden = true;
        head.appendChild(customBadge);
        wrap.appendChild(head);

        var vers = document.createElement('div');
        vers.className = 'jcr-versions';
        var current = cf.variants[cf.current];
        cf.variants.forEach(function (v, vi) {
          var isCur = vi === cf.current;
          var card = document.createElement('div');
          card.className = 'jcr-ver' + (resolutions[ci].choice === vi ? ' sel' : '');
          card.setAttribute('data-vi', vi);
          var contentHtml = isCur ? esc(clip(v.plain)) : diffHtml(current.plain, v.plain);
          if (!contentHtml) contentHtml = '<span class="jcr-empty">' + esc(t('empty')) + '</span>';
          card.innerHTML =
            '<div class="jcr-ver-head">' +
              '<span class="jcr-ver-from">' + esc(v.files.join(', ')) + '</span>' +
              (isCur ? '<span class="jcr-ver-current">' + esc(t('current')) + '</span>' : '') +
            '</div>' +
            (v.lastMod ? '<div class="jcr-ver-date">' + esc(t('modified')) + ' ' + esc(fmtDate(v.lastMod)) + '</div>' : '') +
            '<div class="jcr-ver-body">' + contentHtml + '</div>' +
            '<button class="jcr-ver-pick" type="button">' + esc(resolutions[ci].choice === vi ? t('kept') : t('keep_this')) + '</button>';
          card.querySelector('.jcr-ver-pick').addEventListener('click', function () { resolutions[ci] = { choice: vi }; refresh(); });
          vers.appendChild(card);
        });
        wrap.appendChild(vers);

        var bothRow = document.createElement('div');
        bothRow.className = 'jcr-both-row';
        var bothBtn = document.createElement('button');
        bothBtn.type = 'button';
        bothBtn.className = 'jcr-both-btn' + (resolutions[ci].choice === 'both' ? ' on' : '');
        bothBtn.textContent = resolutions[ci].choice === 'both' ? t('keep_both_on') : t('keep_both');
        bothBtn.addEventListener('click', function () {
          resolutions[ci] = (resolutions[ci].choice === 'both') ? { choice: cf.current } : { choice: 'both' };
          refresh();
        });
        bothRow.appendChild(bothBtn);
        var hint = document.createElement('span');
        hint.className = 'jcr-both-hint';
        hint.textContent = t('keep_both_hint');
        bothRow.appendChild(hint);
        wrap.appendChild(bothRow);

        // ── Side-by-side comparison + combine ────────────────────────
        // Choosing a whole version is the fast path; this is the one for a
        // note where each device holds something worth keeping.
        var otherIdx = -1;
        for (var oi = 0; oi < cf.variants.length; oi++) { if (oi !== cf.current) { otherIdx = oi; break; } }
        var cmpRefresh = null;
        if (otherIdx !== -1) {
          var cmpRow = document.createElement('div');
          cmpRow.className = 'jcr-compare-row';
          var cmpBtn = document.createElement('button');
          cmpBtn.type = 'button';
          cmpBtn.className = 'jcr-compare-btn';
          cmpBtn.textContent = t('compare');
          cmpBtn.setAttribute('aria-expanded', 'false');
          cmpRow.appendChild(cmpBtn);
          wrap.appendChild(cmpRow);

          var cmpWrap = document.createElement('div');
          cmpWrap.className = 'jcr-compare';
          cmpWrap.hidden = true;
          wrap.appendChild(cmpWrap);

          cmpBtn.addEventListener('click', function () {
            var open = cmpWrap.hidden;
            cmpWrap.hidden = !open;
            cmpBtn.classList.toggle('on', open);
            cmpBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
            cmpBtn.textContent = open ? t('compare_hide') : t('compare');
            if (open && !cmpWrap.firstChild) renderCompare();
          });

          var st = { rows: [], inc: [], edited: false };
          var ta = null, useBtn = null, rebuildBtn = null;

          cmpRefresh = function () {
            if (!useBtn) return;
            var on = resolutions[ci].choice === 'custom';
            useBtn.classList.toggle('on', on);
            useBtn.textContent = on ? t('using_combined') : t('use_combined');
            useBtn.disabled = !on && !(ta && ta.value.trim());
          };

          function renderCompare() {
            var cur = cf.variants[cf.current], oth = cf.variants[otherIdx];
            cmpWrap.innerHTML = '';

            if (cf.variants.length > 2) {
              var pickRow = document.createElement('div');
              pickRow.className = 'jcr-cmp-pick-row';
              cf.variants.forEach(function (v, vi) {
                if (vi === cf.current) return;
                var pb = document.createElement('button');
                pb.type = 'button';
                pb.className = 'jcr-cmp-pick' + (vi === otherIdx ? ' on' : '');
                pb.textContent = v.files.join(', ');
                pb.addEventListener('click', function () { otherIdx = vi; renderCompare(); });
                pickRow.appendChild(pb);
              });
              cmpWrap.appendChild(pickRow);
            }

            var heads = document.createElement('div');
            heads.className = 'jcr-cmp-heads';
            heads.innerHTML = '<span class="jcr-cmp-head">' + esc(t('current')) + '</span>' +
                              '<span class="jcr-cmp-head">' + esc(oth.files.join(', ')) + '</span>';
            cmpWrap.appendChild(heads);

            var hint = document.createElement('p');
            hint.className = 'jcr-cmp-hint';
            hint.textContent = t('cmp_hint');
            cmpWrap.appendChild(hint);

            var la = toPlainLines(cur.content), lb = toPlainLines(oth.content);
            if (la.length > 300) la = la.slice(0, 300);
            if (lb.length > 300) lb = lb.slice(0, 300);
            st.rows = alignLines(la, lb);
            st.inc = defaultInc(st.rows);
            st.edited = false;

            var painters = [];
            function buildSide(side, row, ri, pair) {
              var el = document.createElement('div');
              var text = side === 'l' ? row.l : row.r;
              if (text == null) { el.className = 'jcr-dside jcr-dempty'; return el; }
              el.className = 'jcr-dside ' + (row.t === 'eq' ? 'jcr-deq' : (side === 'l' ? 'jcr-dcut' : 'jcr-dnew'));
              var html = pair ? (side === 'l' ? pair.l : pair.r) : esc(text);
              if (!html) html = '&nbsp;';
              if (row.t === 'eq') { el.innerHTML = '<span class="jcr-dtext">' + html + '</span>'; return el; }
              var tick = document.createElement('button');
              tick.type = 'button';
              tick.className = 'jcr-dtick';
              var txt = document.createElement('span');
              txt.className = 'jcr-dtext';
              txt.innerHTML = html;
              el.appendChild(tick);
              el.appendChild(txt);
              function paint() {
                var on = !!st.inc[ri][side];
                tick.setAttribute('aria-pressed', on ? 'true' : 'false');
                tick.textContent = on ? '✓' : '+';
                el.classList.toggle('on', on);
              }
              tick.addEventListener('click', function () { st.inc[ri][side] = !st.inc[ri][side]; paint(); syncDraft(); });
              painters.push(paint);
              paint();
              return el;
            }

            var diff = document.createElement('div');
            diff.className = 'jcr-diff';
            st.rows.forEach(function (row, ri) {
              var el = document.createElement('div');
              el.className = 'jcr-drow jcr-drow-' + row.t;
              var pair = row.t === 'chg' ? wordPair(row.l, row.r) : null;
              el.appendChild(buildSide('l', row, ri, pair));
              el.appendChild(buildSide('r', row, ri, pair));
              diff.appendChild(el);
            });
            cmpWrap.appendChild(diff);

            function setAll(l, r) {
              st.inc = st.rows.map(function (row) {
                return { l: row.l != null && l, r: row.r != null && r };
              });
              painters.forEach(function (fn) { fn(); });
              st.edited = false;
              if (rebuildBtn) rebuildBtn.hidden = true;
              syncDraft();
            }
            var acts = document.createElement('div');
            acts.className = 'jcr-cmp-actions';
            [['all_cur', 1, 0], ['all_alt', 0, 1], ['all_both', 1, 1]].forEach(function (spec) {
              var b = document.createElement('button');
              b.type = 'button';
              b.className = 'jcr-cmp-act';
              b.textContent = t(spec[0]);
              b.addEventListener('click', function () { setAll(!!spec[1], !!spec[2]); });
              acts.appendChild(b);
            });
            rebuildBtn = document.createElement('button');
            rebuildBtn.type = 'button';
            rebuildBtn.className = 'jcr-cmp-act jcr-rebuild';
            rebuildBtn.textContent = t('rebuild');
            rebuildBtn.hidden = true;
            rebuildBtn.addEventListener('click', function () { st.edited = false; rebuildBtn.hidden = true; syncDraft(); });
            acts.appendChild(rebuildBtn);
            cmpWrap.appendChild(acts);

            var combine = document.createElement('div');
            combine.className = 'jcr-combine';
            var lab = document.createElement('label');
            lab.className = 'jcr-combine-label';
            lab.textContent = t('combined');
            var taId = 'jcr-combine-' + ci;
            lab.setAttribute('for', taId);
            ta = document.createElement('textarea');
            ta.className = 'jcr-combine-text';
            ta.id = taId;
            ta.spellcheck = false;
            combine.appendChild(lab);
            combine.appendChild(ta);
            useBtn = document.createElement('button');
            useBtn.type = 'button';
            useBtn.className = 'jcr-use-combined';
            useBtn.textContent = t('use_combined');
            combine.appendChild(useBtn);
            cmpWrap.appendChild(combine);

            // Typing wins over the ticks: rebuilding from them would throw the
            // edit away, so the rebuild becomes something you ask for.
            ta.addEventListener('input', function () {
              st.edited = true;
              if (resolutions[ci].choice === 'custom') resolutions[ci].text = ta.value;
              cmpRefresh();
            });
            useBtn.addEventListener('click', function () {
              if (resolutions[ci].choice === 'custom') resolutions[ci] = { choice: cf.current };
              else if (ta.value.trim()) resolutions[ci] = { choice: 'custom', text: ta.value };
              refresh();
            });

            syncDraft();
          }

          function syncDraft() {
            if (st.edited) { if (rebuildBtn) rebuildBtn.hidden = false; return; }
            ta.value = combineText(st.rows, st.inc);
            if (resolutions[ci].choice === 'custom') resolutions[ci].text = ta.value;
            cmpRefresh();
          }
        }

        function refresh() {

          var sg = suggestions[ci];
          vers.querySelectorAll('.jcr-ver').forEach(function (card) {
            var vi = parseInt(card.getAttribute('data-vi'), 10);
            var sel = resolutions[ci].choice === vi;
            card.classList.toggle('sel', sel);
            var isSug = !!(sg && sg.reason && sg.vi === vi);
            card.classList.toggle('jcr-suggested', isSug);
            var badge = card.querySelector('.jcr-suggestion-badge');
            if (isSug) {
              if (!badge) { badge = document.createElement('span'); badge.className = 'jcr-suggestion-badge'; card.querySelector('.jcr-ver-head').appendChild(badge); }
              badge.textContent = t('suggested') + ' \u00b7 ' + t(sg.reason);
            } else if (badge) { badge.remove(); }
            card.querySelector('.jcr-ver-pick').textContent = sel ? t('kept') : t('keep_this');
          });
          var isBoth = resolutions[ci].choice === 'both';
          bothBtn.classList.toggle('on', isBoth);
          bothBtn.textContent = isBoth ? t('keep_both_on') : t('keep_both');
          customBadge.hidden = resolutions[ci].choice !== 'custom';
          if (cmpRefresh) cmpRefresh();
        }
        refreshers.push(refresh);

        return wrap;
      }
    });
  };
})();

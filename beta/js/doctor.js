/* ──────────────────────────────────────────────────────────────────────────
   doctor.js — Library Doctor — private health check for a backup (window.__openJwDoctor).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';
  var DOC_I18N = {
  en:{title:"Library Doctor",sub:"A private health check for your backup",priv:"100% private — your file never leaves this device.",pick:"Choose a .jwlibrary file",use_last:"Check {name}",scanning:"Examining your backup…",c_dup_notes:"Duplicate notes",c_empty_notes:"Empty notes",c_dup_marks:"Duplicate highlights",c_orph_br:"Stray highlight fragments",c_orph_tm:"Broken tag links",c_unused_tags:"Unused tags",c_unused_loc:"Leftover location records",l_notes:"notes",l_marks:"highlights",l_bm:"bookmarks",l_tags:"tags",health:"Health score",v_a:"Excellent",v_b:"Good",v_c:"Fair",v_d:"Needs care",issues_one:"1 fixable issue found",issues_many:"{n} fixable issues found",perfect:"Perfect health — nothing to fix!",clean:"Clean & Download",cleaning:"Cleaning…",done_t:"All fixed!",done_d:"Your cleaned backup is downloading.",smaller:"smaller",safe:"Your original file is never changed — fixes go into a new copy.",another:"Check another file",close:"Close",err_read:"Could not read this backup — it may be corrupted or the wrong type of file.",err_db:"This backup is missing its notes database (userData.db).",download:"Download your file",done_ready:"Your cleaned backup is ready to download.",will_fix:"These will be fixed automatically in your merged file.",review:"Review changes",rv_t:"Review before cleaning",rv_d:"Nothing is deleted until you tap Clean. Uncheck anything you'd like to keep.",rv_dups_h:"Duplicate notes",rv_other_h:"Other cleanup",rv_kept:"1 kept",rv_remove_n:"{n} to remove",rv_notitle:"(untitled note)",rv_none:"Select at least one item to clean.",back:"Back"},
  es:{title:"Doctor de Biblioteca",sub:"Un chequeo privado para tu copia de seguridad",priv:"100% privado — tu archivo nunca sale de este dispositivo.",pick:"Elegir archivo .jwlibrary",use_last:"Revisar {name}",scanning:"Examinando tu copia…",c_dup_notes:"Notas duplicadas",c_empty_notes:"Notas vacías",c_dup_marks:"Subrayados duplicados",c_orph_br:"Fragmentos de subrayado sueltos",c_orph_tm:"Enlaces de etiqueta rotos",c_unused_tags:"Etiquetas sin usar",c_unused_loc:"Registros de ubicación sobrantes",l_notes:"notas",l_marks:"subrayados",l_bm:"marcadores",l_tags:"etiquetas",health:"Puntuación de salud",v_a:"Excelente",v_b:"Buena",v_c:"Regular",v_d:"Necesita atención",issues_one:"1 problema corregible encontrado",issues_many:"{n} problemas corregibles encontrados",perfect:"¡Salud perfecta — nada que corregir!",clean:"Limpiar y Descargar",cleaning:"Limpiando…",done_t:"¡Todo corregido!",done_d:"Tu copia limpia se está descargando.",smaller:"más pequeña",safe:"Tu archivo original nunca se modifica — las correcciones van a una copia nueva.",another:"Revisar otro archivo",close:"Cerrar",err_read:"No se pudo leer esta copia — puede estar dañada o ser un tipo de archivo incorrecto.",err_db:"A esta copia le falta su base de datos de notas (userData.db).",download:"Descargar tu archivo",done_ready:"Tu copia limpia está lista para descargar.",will_fix:"Se corregirán automáticamente en tu archivo combinado.",review:"Revisar cambios",rv_t:"Revisa antes de limpiar",rv_d:"No se elimina nada hasta que toques Limpiar. Desmarca lo que quieras conservar.",rv_dups_h:"Notas duplicadas",rv_other_h:"Otra limpieza",rv_kept:"1 conservada",rv_remove_n:"{n} a eliminar",rv_notitle:"(nota sin título)",rv_none:"Selecciona al menos un elemento para limpiar.",back:"Atrás"},
  pt:{title:"Doutor da Biblioteca",sub:"Um exame privado para o seu backup",priv:"100% privado — seu arquivo nunca sai deste dispositivo.",pick:"Escolher arquivo .jwlibrary",use_last:"Examinar {name}",scanning:"Examinando seu backup…",c_dup_notes:"Notas duplicadas",c_empty_notes:"Notas vazias",c_dup_marks:"Destaques duplicados",c_orph_br:"Fragmentos de destaque soltos",c_orph_tm:"Vínculos de etiqueta quebrados",c_unused_tags:"Etiquetas sem uso",c_unused_loc:"Registros de local restantes",l_notes:"notas",l_marks:"destaques",l_bm:"marcadores",l_tags:"etiquetas",health:"Pontuação de saúde",v_a:"Excelente",v_b:"Boa",v_c:"Razoável",v_d:"Precisa de cuidado",issues_one:"1 problema corrigível encontrado",issues_many:"{n} problemas corrigíveis encontrados",perfect:"Saúde perfeita — nada para corrigir!",clean:"Limpar e Baixar",cleaning:"Limpando…",done_t:"Tudo corrigido!",done_d:"Seu backup limpo está sendo baixado.",smaller:"menor",safe:"Seu arquivo original nunca é alterado — as correções vão para uma nova cópia.",another:"Examinar outro arquivo",close:"Fechar",err_read:"Não foi possível ler este backup — pode estar corrompido ou ser o tipo errado de arquivo.",err_db:"Este backup está sem o banco de dados de notas (userData.db).",download:"Baixar seu arquivo",done_ready:"Seu backup limpo está pronto para baixar.",will_fix:"Serão corrigidos automaticamente no seu arquivo mesclado.",review:"Revisar alterações",rv_t:"Revise antes de limpar",rv_d:"Nada é excluído até você tocar em Limpar. Desmarque o que quiser manter.",rv_dups_h:"Notas duplicadas",rv_other_h:"Outra limpeza",rv_kept:"1 mantida",rv_remove_n:"{n} a remover",rv_notitle:"(nota sem título)",rv_none:"Selecione pelo menos um item para limpar.",back:"Voltar"},
  fr:{title:"Docteur de Bibliothèque",sub:"Un bilan de santé privé pour votre sauvegarde",priv:"100 % privé — votre fichier ne quitte jamais cet appareil.",pick:"Choisir un fichier .jwlibrary",use_last:"Examiner {name}",scanning:"Examen de votre sauvegarde…",c_dup_notes:"Notes en double",c_empty_notes:"Notes vides",c_dup_marks:"Surlignages en double",c_orph_br:"Fragments de surlignage orphelins",c_orph_tm:"Liens d'étiquette cassés",c_unused_tags:"Étiquettes inutilisées",c_unused_loc:"Entrées de lieu superflues",l_notes:"notes",l_marks:"surlignages",l_bm:"signets",l_tags:"étiquettes",health:"Score de santé",v_a:"Excellent",v_b:"Bon",v_c:"Moyen",v_d:"À soigner",issues_one:"1 problème corrigeable trouvé",issues_many:"{n} problèmes corrigeables trouvés",perfect:"Santé parfaite — rien à corriger !",clean:"Nettoyer et Télécharger",cleaning:"Nettoyage…",done_t:"Tout est réparé !",done_d:"Votre sauvegarde nettoyée se télécharge.",smaller:"plus légère",safe:"Votre fichier d'origine n'est jamais modifié — les corrections vont dans une nouvelle copie.",another:"Examiner un autre fichier",close:"Fermer",err_read:"Impossible de lire cette sauvegarde — elle est peut-être corrompue ou du mauvais type.",err_db:"Cette sauvegarde n'a pas sa base de données de notes (userData.db).",download:"Télécharger votre fichier",done_ready:"Votre sauvegarde nettoyée est prête à télécharger.",will_fix:"Ils seront corrigés automatiquement dans votre fichier fusionné.",review:"Vérifier les changements",rv_t:"Vérifiez avant de nettoyer",rv_d:"Rien n'est supprimé tant que vous n'appuyez pas sur Nettoyer. Décochez ce que vous voulez garder.",rv_dups_h:"Notes en double",rv_other_h:"Autre nettoyage",rv_kept:"1 conservée",rv_remove_n:"{n} à supprimer",rv_notitle:"(note sans titre)",rv_none:"Sélectionnez au moins un élément à nettoyer.",back:"Retour"},
  de:{title:"Bibliothek-Doktor",sub:"Ein privater Gesundheitscheck für deine Sicherung",priv:"100 % privat — deine Datei verlässt dieses Gerät nie.",pick:".jwlibrary-Datei wählen",use_last:"{name} prüfen",scanning:"Deine Sicherung wird untersucht…",c_dup_notes:"Doppelte Notizen",c_empty_notes:"Leere Notizen",c_dup_marks:"Doppelte Markierungen",c_orph_br:"Verwaiste Markierungsfragmente",c_orph_tm:"Defekte Tag-Verknüpfungen",c_unused_tags:"Unbenutzte Tags",c_unused_loc:"Übrige Ortseinträge",l_notes:"Notizen",l_marks:"Markierungen",l_bm:"Lesezeichen",l_tags:"Tags",health:"Gesundheitswert",v_a:"Ausgezeichnet",v_b:"Gut",v_c:"Mittel",v_d:"Braucht Pflege",issues_one:"1 behebbares Problem gefunden",issues_many:"{n} behebbare Probleme gefunden",perfect:"Perfekte Gesundheit — nichts zu beheben!",clean:"Bereinigen & Herunterladen",cleaning:"Bereinige…",done_t:"Alles behoben!",done_d:"Deine bereinigte Sicherung wird heruntergeladen.",smaller:"kleiner",safe:"Deine Originaldatei wird nie verändert — Korrekturen kommen in eine neue Kopie.",another:"Weitere Datei prüfen",close:"Schließen",err_read:"Diese Sicherung konnte nicht gelesen werden — sie ist evtl. beschädigt oder der falsche Dateityp.",err_db:"Dieser Sicherung fehlt ihre Notizdatenbank (userData.db).",download:"Deine Datei herunterladen",done_ready:"Deine bereinigte Sicherung ist bereit zum Download.",will_fix:"Diese werden in deiner zusammengeführten Datei automatisch behoben.",review:"Änderungen prüfen",rv_t:"Vor dem Bereinigen prüfen",rv_d:"Es wird nichts gelöscht, bis du auf Bereinigen tippst. Entferne den Haken bei allem, was du behalten möchtest.",rv_dups_h:"Doppelte Notizen",rv_other_h:"Weitere Bereinigung",rv_kept:"1 behalten",rv_remove_n:"{n} entfernen",rv_notitle:"(Notiz ohne Titel)",rv_none:"Wähle mindestens ein Element zum Bereinigen aus.",back:"Zurück"},
  it:{title:"Dottore della Biblioteca",sub:"Un controllo privato per il tuo backup",priv:"100% privato — il tuo file non lascia mai questo dispositivo.",pick:"Scegli file .jwlibrary",use_last:"Esamina {name}",scanning:"Esame del tuo backup…",c_dup_notes:"Note duplicate",c_empty_notes:"Note vuote",c_dup_marks:"Evidenziazioni duplicate",c_orph_br:"Frammenti di evidenziazione orfani",c_orph_tm:"Collegamenti di etichetta rotti",c_unused_tags:"Etichette inutilizzate",c_unused_loc:"Record di posizione residui",l_notes:"note",l_marks:"evidenziazioni",l_bm:"segnalibri",l_tags:"etichette",health:"Punteggio di salute",v_a:"Eccellente",v_b:"Buono",v_c:"Discreto",v_d:"Da curare",issues_one:"1 problema risolvibile trovato",issues_many:"{n} problemi risolvibili trovati",perfect:"Salute perfetta — niente da correggere!",clean:"Pulisci e Scarica",cleaning:"Pulizia…",done_t:"Tutto sistemato!",done_d:"Il tuo backup pulito è in download.",smaller:"più leggero",safe:"Il file originale non viene mai modificato — le correzioni vanno in una nuova copia.",another:"Esamina un altro file",close:"Chiudi",err_read:"Impossibile leggere questo backup — potrebbe essere danneggiato o del tipo sbagliato.",err_db:"A questo backup manca il database delle note (userData.db).",download:"Scarica il tuo file",done_ready:"Il tuo backup pulito è pronto da scaricare.",will_fix:"Saranno corretti automaticamente nel file unito.",review:"Rivedi le modifiche",rv_t:"Controlla prima di pulire",rv_d:"Nulla viene eliminato finché non tocchi Pulisci. Deseleziona ciò che vuoi conservare.",rv_dups_h:"Note duplicate",rv_other_h:"Altra pulizia",rv_kept:"1 conservata",rv_remove_n:"{n} da rimuovere",rv_notitle:"(nota senza titolo)",rv_none:"Seleziona almeno un elemento da pulire.",back:"Indietro"},
  ru:{title:"Доктор библиотеки",sub:"Приватная проверка здоровья вашей копии",priv:"100% приватно — файл никогда не покидает это устройство.",pick:"Выбрать файл .jwlibrary",use_last:"Проверить {name}",scanning:"Осматриваем вашу копию…",c_dup_notes:"Дубликаты заметок",c_empty_notes:"Пустые заметки",c_dup_marks:"Дубликаты выделений",c_orph_br:"Осиротевшие фрагменты выделений",c_orph_tm:"Битые связи тегов",c_unused_tags:"Неиспользуемые теги",c_unused_loc:"Лишние записи мест",l_notes:"заметки",l_marks:"выделения",l_bm:"закладки",l_tags:"теги",health:"Оценка здоровья",v_a:"Отлично",v_b:"Хорошо",v_c:"Средне",v_d:"Требует внимания",issues_one:"Найдена 1 исправимая проблема",issues_many:"Найдено исправимых проблем: {n}",perfect:"Идеальное здоровье — исправлять нечего!",clean:"Очистить и скачать",cleaning:"Очистка…",done_t:"Всё исправлено!",done_d:"Ваша очищенная копия скачивается.",smaller:"меньше",safe:"Исходный файл не изменяется — исправления попадают в новую копию.",another:"Проверить другой файл",close:"Закрыть",err_read:"Не удалось прочитать эту копию — возможно, она повреждена или неверного типа.",err_db:"В этой копии нет базы данных заметок (userData.db).",download:"Скачать ваш файл",done_ready:"Ваша очищенная копия готова к скачиванию.",will_fix:"Они будут автоматически исправлены в объединённом файле.",review:"Просмотреть изменения",rv_t:"Проверьте перед очисткой",rv_d:"Ничего не удаляется, пока вы не нажмёте «Очистить». Снимите отметку с того, что хотите сохранить.",rv_dups_h:"Повторяющиеся заметки",rv_other_h:"Прочая очистка",rv_kept:"1 останется",rv_remove_n:"удалить: {n}",rv_notitle:"(заметка без заголовка)",rv_none:"Выберите хотя бы один элемент для очистки.",back:"Назад"},
  ja:{title:"ライブラリードクター",sub:"バックアップのプライベート健康診断",priv:"100%プライベート — ファイルがこの端末から出ることはありません。",pick:".jwlibraryファイルを選択",use_last:"{name} を診断",scanning:"バックアップを検査中…",c_dup_notes:"重複したメモ",c_empty_notes:"空のメモ",c_dup_marks:"重複したハイライト",c_orph_br:"孤立したハイライト断片",c_orph_tm:"壊れたタグリンク",c_unused_tags:"未使用のタグ",c_unused_loc:"残された場所レコード",l_notes:"メモ",l_marks:"ハイライト",l_bm:"ブックマーク",l_tags:"タグ",health:"健康スコア",v_a:"非常に良好",v_b:"良好",v_c:"普通",v_d:"要ケア",issues_one:"修復可能な問題が1件見つかりました",issues_many:"修復可能な問題が{n}件見つかりました",perfect:"完璧な状態 — 修復は不要です！",clean:"クリーンアップしてダウンロード",cleaning:"クリーンアップ中…",done_t:"すべて修復しました！",done_d:"クリーンなバックアップをダウンロード中です。",smaller:"削減",safe:"元のファイルは変更されません — 修復は新しいコピーに適用されます。",another:"別のファイルを診断",close:"閉じる",err_read:"このバックアップを読み込めませんでした — 破損しているか、ファイル形式が違う可能性があります。",err_db:"このバックアップにはメモのデータベース（userData.db）がありません。",download:"ファイルをダウンロード",done_ready:"クリーンなバックアップの準備ができました。",will_fix:"結合ファイルでは自動的に修復されます。",review:"変更を確認",rv_t:"クリーンアップ前に確認",rv_d:"「クリーン」をタップするまで何も削除されません。残したいものはチェックを外してください。",rv_dups_h:"重複したノート",rv_other_h:"その他の整理",rv_kept:"1件を保持",rv_remove_n:"{n}件を削除",rv_notitle:"(タイトルなしのノート)",rv_none:"整理する項目を1つ以上選んでください。",back:"戻る"},
  ko:{title:"라이브러리 닥터",sub:"백업을 위한 프라이빗 건강 검진",priv:"100% 프라이빗 — 파일은 이 기기를 절대 벗어나지 않습니다.",pick:".jwlibrary 파일 선택",use_last:"{name} 검진하기",scanning:"백업을 검사하는 중…",c_dup_notes:"중복된 메모",c_empty_notes:"빈 메모",c_dup_marks:"중복된 하이라이트",c_orph_br:"고아 하이라이트 조각",c_orph_tm:"끊어진 태그 연결",c_unused_tags:"사용하지 않는 태그",c_unused_loc:"남은 위치 기록",l_notes:"메모",l_marks:"하이라이트",l_bm:"북마크",l_tags:"태그",health:"건강 점수",v_a:"최상",v_b:"양호",v_c:"보통",v_d:"관리 필요",issues_one:"수정 가능한 문제 1건 발견",issues_many:"수정 가능한 문제 {n}건 발견",perfect:"완벽한 상태 — 고칠 것이 없습니다!",clean:"정리 후 다운로드",cleaning:"정리 중…",done_t:"모두 수정했습니다!",done_d:"정리된 백업이 다운로드되고 있습니다.",smaller:"감소",safe:"원본 파일은 절대 변경되지 않습니다 — 수정 사항은 새 복사본에 적용됩니다.",another:"다른 파일 검진",close:"닫기",err_read:"이 백업을 읽을 수 없습니다 — 손상되었거나 잘못된 파일 형식일 수 있습니다.",err_db:"이 백업에는 메모 데이터베이스(userData.db)가 없습니다.",download:"파일 다운로드",done_ready:"정리된 백업이 준비되었습니다.",will_fix:"병합된 파일에서 자동으로 수정됩니다.",review:"변경 검토",rv_t:"정리 전에 검토하기",rv_d:"정리를 누르기 전까지는 아무것도 삭제되지 않습니다. 남기고 싶은 항목은 선택을 해제하세요.",rv_dups_h:"중복 노트",rv_other_h:"기타 정리",rv_kept:"1개 유지",rv_remove_n:"{n}개 삭제",rv_notitle:"(제목 없는 노트)",rv_none:"정리할 항목을 하나 이상 선택하세요.",back:"뒤로"},
  tl:{title:"Library Doctor",sub:"Pribadong health check para sa iyong backup",priv:"100% pribado — hindi kailanman aalis ang iyong file sa device na ito.",pick:"Pumili ng .jwlibrary file",use_last:"Suriin ang {name}",scanning:"Sinusuri ang iyong backup…",c_dup_notes:"Mga duplicate na tala",c_empty_notes:"Mga walang lamang tala",c_dup_marks:"Mga duplicate na highlight",c_orph_br:"Mga ulilang piraso ng highlight",c_orph_tm:"Mga sirang tag link",c_unused_tags:"Mga hindi ginagamit na tag",c_unused_loc:"Mga natirang tala ng lokasyon",l_notes:"mga tala",l_marks:"mga highlight",l_bm:"mga bookmark",l_tags:"mga tag",health:"Health score",v_a:"Napakahusay",v_b:"Mabuti",v_c:"Katamtaman",v_d:"Kailangan ng pag-aalaga",issues_one:"1 maaayos na problema ang natagpuan",issues_many:"{n} maaayos na problema ang natagpuan",perfect:"Perpektong kalusugan — walang dapat ayusin!",clean:"Linisin at I-download",cleaning:"Naglilinis…",done_t:"Naayos na lahat!",done_d:"Dina-download na ang iyong malinis na backup.",smaller:"mas maliit",safe:"Hindi kailanman binabago ang orihinal mong file — ang mga pag-aayos ay napupunta sa bagong kopya.",another:"Suriin ang ibang file",close:"Isara",err_read:"Hindi mabasa ang backup na ito — maaaring sira o maling uri ng file.",err_db:"Walang notes database (userData.db) ang backup na ito.",download:"I-download ang iyong file",done_ready:"Handa nang i-download ang malinis mong backup.",will_fix:"Awtomatikong aayusin ang mga ito sa iyong pinagsamang file.",review:"Suriin ang mga pagbabago",rv_t:"Suriin bago maglinis",rv_d:"Walang buburahin hangga't hindi mo pinindot ang Linisin. Alisin sa check ang gusto mong itago.",rv_dups_h:"Dobleng mga tala",rv_other_h:"Iba pang paglilinis",rv_kept:"1 itatago",rv_remove_n:"{n} aalisin",rv_notitle:"(walang pamagat na tala)",rv_none:"Pumili ng kahit isang item na lilinisin.",back:"Bumalik"},
  sv:{title:"Biblioteksdoktorn",sub:"En privat hälsokontroll för din säkerhetskopia",priv:"100 % privat — din fil lämnar aldrig den här enheten.",pick:"Välj .jwlibrary-fil",use_last:"Undersök {name}",scanning:"Undersöker din säkerhetskopia…",c_dup_notes:"Dubblerade anteckningar",c_empty_notes:"Tomma anteckningar",c_dup_marks:"Dubblerade överstrykningar",c_orph_br:"Övergivna överstrykningsfragment",c_orph_tm:"Trasiga tagglänkar",c_unused_tags:"Oanvända taggar",c_unused_loc:"Kvarblivna platsposter",l_notes:"anteckningar",l_marks:"överstrykningar",l_bm:"bokmärken",l_tags:"taggar",health:"Hälsopoäng",v_a:"Utmärkt",v_b:"Bra",v_c:"Okej",v_d:"Behöver omsorg",issues_one:"1 åtgärdbart problem hittades",issues_many:"{n} åtgärdbara problem hittades",perfect:"Perfekt hälsa — inget att åtgärda!",clean:"Rensa och ladda ner",cleaning:"Rensar…",done_t:"Allt åtgärdat!",done_d:"Din rensade säkerhetskopia laddas ner.",smaller:"mindre",safe:"Din originalfil ändras aldrig — åtgärderna hamnar i en ny kopia.",another:"Undersök en annan fil",close:"Stäng",err_read:"Kunde inte läsa den här säkerhetskopian — den kan vara skadad eller fel filtyp.",err_db:"Den här säkerhetskopian saknar sin anteckningsdatabas (userData.db).",download:"Ladda ner din fil",done_ready:"Din rensade säkerhetskopia är redo att laddas ner.",will_fix:"Dessa åtgärdas automatiskt i din sammanslagna fil.",review:"Granska ändringar",rv_t:"Granska innan du rensar",rv_d:"Inget raderas förrän du trycker på Rensa. Avmarkera det du vill behålla.",rv_dups_h:"Dubbletter av anteckningar",rv_other_h:"Övrig rensning",rv_kept:"1 behålls",rv_remove_n:"{n} tas bort",rv_notitle:"(anteckning utan titel)",rv_none:"Välj minst ett objekt att rensa.",back:"Tillbaka"},
  ceb:{title:"Library Doctor",sub:"Pribadong health check para sa imong backup",priv:"100% pribado — dili gayud mogawas ang imong file niini nga device.",pick:"Pilia ang .jwlibrary file",use_last:"Susiha ang {name}",scanning:"Gisusi ang imong backup…",c_dup_notes:"Mga duplicate nga nota",c_empty_notes:"Mga walay sulod nga nota",c_dup_marks:"Mga duplicate nga highlight",c_orph_br:"Mga nabiyaan nga piraso sa highlight",c_orph_tm:"Mga naputol nga tag link",c_unused_tags:"Mga wala magamit nga tag",c_unused_loc:"Mga nahibilin nga rekord sa lokasyon",l_notes:"mga nota",l_marks:"mga highlight",l_bm:"mga bookmark",l_tags:"mga tag",health:"Health score",v_a:"Maayo kaayo",v_b:"Maayo",v_c:"Igo-igo",v_d:"Nagkinahanglan ug pag-atiman",issues_one:"1 ka maayos nga problema ang nakit-an",issues_many:"{n} ka maayos nga problema ang nakit-an",perfect:"Hingpit nga kahimsog — walay angay ayohon!",clean:"Limpyohi ug I-download",cleaning:"Naglimpyo…",done_t:"Naayo na ang tanan!",done_d:"Gi-download na ang imong limpyo nga backup.",smaller:"mas gamay",safe:"Dili gayud usbon ang imong orihinal nga file — ang mga pag-ayo moadto sa bag-ong kopya.",another:"Susiha ang laing file",close:"Sirado",err_read:"Dili mabasa kini nga backup — tingali nadaot o sayop nga klase sa file.",err_db:"Wala kini backup sa notes database (userData.db).",download:"I-download ang imong file",done_ready:"Andam na ang limpyo nimong backup nga i-download.",will_fix:"Awtomatikong ayohon kini sa imong gisagol nga file.",review:"Susiha ang mga kausaban",rv_t:"Susiha una sa dili pa manglimpyo",rv_d:"Walay mapapas hangtod nga imong i-tap ang Limpyo. Kuhaa ang check sa gusto nimong tipigan.",rv_dups_h:"Doble nga mga nota",rv_other_h:"Uban pang paglimpyo",rv_kept:"1 tipigan",rv_remove_n:"{n} tangtangon",rv_notitle:"(nota nga walay ulohan)",rv_none:"Pagpili ug labing menos usa ka butang nga limpyohan.",back:"Balik"},he:{title:"רופא הספרייה",sub:"בדיקת תקינות פרטית לגיבוי שלכם",priv:"‏100% פרטי — הקובץ שלכם לעולם לא עוזב את המכשיר הזה.",pick:"בחרו קובץ ‎.jwlibrary",use_last:"בדיקת {name}",scanning:"בודק את הגיבוי שלכם…",c_dup_notes:"הערות כפולות",c_empty_notes:"הערות ריקות",c_dup_marks:"הדגשות כפולות",c_orph_br:"שברי הדגשה יתומים",c_orph_tm:"קישורי תוויות שבורים",c_unused_tags:"תוויות שאינן בשימוש",c_unused_loc:"רשומות מיקום שנותרו",l_notes:"הערות",l_marks:"הדגשות",l_bm:"סימניות",l_tags:"תוויות",health:"ציון תקינות",v_a:"מצוין",v_b:"טוב",v_c:"סביר",v_d:"דורש טיפול",issues_one:"נמצאה בעיה אחת שניתן לתקן",issues_many:"נמצאו {n} בעיות שניתן לתקן",perfect:"תקינות מושלמת — אין מה לתקן!",clean:"ניקוי והורדה",cleaning:"מנקה…",done_t:"הכול תוקן!",done_d:"הגיבוי המנוקה שלכם יורד.",smaller:"קטן יותר",safe:"הקובץ המקורי שלכם לעולם לא משתנה — התיקונים נכנסים לעותק חדש.",another:"בדיקת קובץ אחר",close:"סגירה",err_read:"לא הצלחנו לקרוא את הגיבוי הזה — ייתכן שהוא פגום או שזה סוג קובץ שגוי.",err_db:"בגיבוי הזה חסר מסד הנתונים של ההערות (userData.db).",download:"הורדת הקובץ שלכם",done_ready:"הגיבוי המנוקה שלכם מוכן להורדה.",will_fix:"אלה יתוקנו אוטומטית בקובץ הממוזג שלכם.",review:"סקירת השינויים",rv_t:"סקירה לפני הניקוי",rv_d:"שום דבר לא נמחק עד שתקישו על ניקוי. בטלו את הסימון של כל מה שתרצו לשמור.",rv_dups_h:"הערות כפולות",rv_other_h:"ניקוי נוסף",rv_kept:"אחת נשמרת",rv_remove_n:"{n} להסרה",rv_notitle:"(הערה ללא כותרת)",rv_none:"בחרו לפחות פריט אחד לניקוי.",back:"חזרה"},ar:{title:"طبيب المكتبة",sub:"فحص صحي خاص لنسختك الاحتياطية",priv:"خصوصية 100% — ملفك لا يغادر هذا الجهاز أبدًا.",pick:"اختر ملف ‎.jwlibrary‎",use_last:"افحص {name}",scanning:"جارٍ فحص نسختك الاحتياطية…",c_dup_notes:"ملاحظات مكرّرة",c_empty_notes:"ملاحظات فارغة",c_dup_marks:"تظليلات مكرّرة",c_orph_br:"أجزاء تظليل شاردة",c_orph_tm:"روابط وسوم معطوبة",c_unused_tags:"وسوم غير مستخدمة",c_unused_loc:"سجلات مواضع متبقّية",l_notes:"ملاحظة",l_marks:"تظليل",l_bm:"علامة مرجعية",l_tags:"وسم",health:"درجة السلامة",v_a:"ممتازة",v_b:"جيدة",v_c:"مقبولة",v_d:"تحتاج عناية",issues_one:"عُثر على مشكلة واحدة قابلة للإصلاح",issues_many:"عُثر على {n} مشكلة قابلة للإصلاح",perfect:"سلامة تامة — لا شيء لإصلاحه!",clean:"نظّف ونزّل",cleaning:"جارٍ التنظيف…",done_t:"تم إصلاح كل شيء!",done_d:"جارٍ تنزيل نسختك الاحتياطية بعد التنظيف.",smaller:"أصغر",safe:"ملفك الأصلي لا يتغيّر أبدًا — تُطبَّق الإصلاحات على نسخة جديدة.",another:"افحص ملفًا آخر",close:"إغلاق",err_read:"تعذّرت قراءة هذه النسخة الاحتياطية — قد تكون تالفة أو من نوع ملفات غير صحيح.",err_db:"تفتقر هذه النسخة الاحتياطية إلى قاعدة بيانات الملاحظات (userData.db).",download:"نزّل ملفك",done_ready:"نسختك الاحتياطية بعد التنظيف جاهزة للتنزيل.",will_fix:"ستُصلَح هذه تلقائيًا في ملفك المدمج.",review:"راجِع التغييرات",rv_t:"راجِع قبل التنظيف",rv_d:"لا يُحذف شيء حتى تضغط تنظيف. أزِل التحديد عن أي عنصر تريد الاحتفاظ به.",rv_dups_h:"ملاحظات مكرّرة",rv_other_h:"تنظيف آخر",rv_kept:"1 محفوظة",rv_remove_n:"{n} للإزالة",rv_notitle:"(ملاحظة بلا عنوان)",rv_none:"اختر عنصرًا واحدًا على الأقل للتنظيف.",back:"رجوع"}
  };
  function lang(){ try{ return localStorage.getItem('jwsync_lang')||'en'; }catch(_){ return 'en'; } }
  function t(k){ var l=lang(); return (DOC_I18N[l]&&DOC_I18N[l][k])||DOC_I18N.en[k]||k; }
  function esc(s){ return String(s==null?'':s).replace(/[&<>"']/g,function(ch){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]; }); }
  function fmtSize(b){ if(!b&&b!==0) return ''; if(b>=1048576) return (b/1048576).toFixed(1)+' MB'; if(b>=1024) return Math.round(b/1024)+' KB'; return b+' B'; }

  var SQLJS_CDN='https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';
  function ensureDeps(){
    var boot = (typeof window.__jwBootBrowse==='function') ? window.__jwBootBrowse().catch(function(){}) : Promise.resolve();
    return boot.then(function(){
      if(window.JSZip && window.initSqlJs) return;
      function load(src){ return new Promise(function(res,rej){ var s=document.createElement('script'); s.src=src; s.async=true; s.crossOrigin='anonymous'; s.onload=res; s.onerror=rej; document.head.appendChild(s); }); }
      var p=[];
      if(!window.JSZip) p.push(load('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'));
      if(!window.initSqlJs) p.push(load(SQLJS_CDN+'sql-wasm.js'));
      return Promise.all(p);
    });
  }

  // ── SQL helpers ─────────────────────────────────────────────────────
  function q(db,sql){ var out=[],st=db.prepare(sql); try{ while(st.step()) out.push(st.getAsObject()); } finally { st.free(); } return out; }
  function qv(db,sql){ var r=q(db,sql); if(!r.length) return 0; var k=Object.keys(r[0])[0]; return r[0][k]||0; }
  function col1(db,sql){ var st=db.prepare(sql),out=[]; try{ while(st.step()) out.push(st.get()[0]); } finally { st.free(); } return out; }
  function hasTable(db,n){ return qv(db,"SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='"+n+"'")>0; }
  function hasCol(db,tbl,cname){ try{ return q(db,'PRAGMA table_info('+tbl+')').some(function(r){ return r.name===cname; }); }catch(_){ return false; } }

  // Two notes are duplicates only when BOTH the text AND the anchor match:
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

  // ── Health checks ───────────────────────────────────────────────────
  var CHECKS=['dup_notes','empty_notes','dup_marks','orph_br','orph_tm','unused_tags','unused_loc'];
  var WEIGHTS={dup_notes:1.2,empty_notes:.4,dup_marks:.8,orph_br:.15,orph_tm:.15,unused_tags:.3,unused_loc:.02};

  function idsFor(db,key){
    switch(key){
      case 'dup_notes':
        return dupNotePairs(db).map(function(r){ return r.dup; });
      case 'empty_notes':
        if(!hasTable(db,'Note')) return [];
        return col1(db,"SELECT NoteId FROM Note WHERE TRIM(IFNULL(Title,''))='' AND TRIM(IFNULL(Content,''))=''");
      case 'dup_marks':{
        if(!hasTable(db,'UserMark')||!hasTable(db,'BlockRange')) return [];
        // O(n) JS grouping replaces the O(n²) SQL self-join.
        // Fetch ALL single-blockrange marks so note-linked ones can still serve
        // as the 'keep' reference; only return non-note-linked marks as duplicates.
        var _rows=q(db,
          "SELECT um.UserMarkId,IFNULL(um.LocationId,-1) AS loc,IFNULL(um.ColorIndex,-1) AS col,"+
          "IFNULL(br.BlockType,-1) AS bt,IFNULL(br.Identifier,-1) AS bid,"+
          "IFNULL(br.StartToken,-1) AS st,IFNULL(br.EndToken,-1) AS et"+
          " FROM UserMark um JOIN BlockRange br ON br.UserMarkId=um.UserMarkId"+
          " WHERE (SELECT COUNT(*) FROM BlockRange b2 WHERE b2.UserMarkId=um.UserMarkId)=1"+
          " ORDER BY um.UserMarkId");
        var _noteMarkSet={};
        col1(db,"SELECT IFNULL(UserMarkId,-1) FROM Note WHERE UserMarkId IS NOT NULL")
          .forEach(function(id){ _noteMarkSet[id]=true; });
        var _grp={};
        _rows.forEach(function(r){
          var k=r.loc+'|'+r.col+'|'+r.bt+'|'+r.bid+'|'+r.st+'|'+r.et;
          if(!_grp[k]) _grp[k]=[];
          _grp[k].push(r.UserMarkId);
        });
        var _dups=[];
        Object.keys(_grp).forEach(function(k){
          var ids=_grp[k]; // ascending by UserMarkId (ORDER BY ensures this)
          if(ids.length>1){
            for(var j=1;j<ids.length;j++){
              if(!_noteMarkSet[ids[j]]) _dups.push(ids[j]);
            }
          }
        });
        return _dups;
      }
      case 'orph_br':
        if(!hasTable(db,'BlockRange')||!hasTable(db,'UserMark')) return [];
        return col1(db,"SELECT BlockRangeId FROM BlockRange WHERE UserMarkId NOT IN (SELECT UserMarkId FROM UserMark)");
      case 'orph_tm':
        if(!hasTable(db,'TagMap')||!hasTable(db,'Note')) return [];
        return col1(db,"SELECT TagMapId FROM TagMap WHERE NoteId IS NOT NULL AND NoteId NOT IN (SELECT NoteId FROM Note)");
      case 'unused_tags':
        if(!hasTable(db,'Tag')) return [];
        var typeFilter = hasCol(db,'Tag','Type') ? "IFNULL(Type,1)=1 AND " : "";
        var tmRef = hasTable(db,'TagMap') ? " AND TagId NOT IN (SELECT DISTINCT TagId FROM TagMap WHERE TagId IS NOT NULL)" : "";
        return col1(db,"SELECT TagId FROM Tag WHERE "+typeFilter+"1=1"+tmRef);
      case 'unused_loc':
        if(!hasTable(db,'Location')) return [];
        var refs=[];
        [['Note','LocationId'],['UserMark','LocationId'],['Bookmark','LocationId'],['Bookmark','PublicationLocationId'],
         ['TagMap','LocationId'],['InputField','LocationId'],['PlaylistItemLocationMap','LocationId'],['PlaylistMedia','LocationId']
        ].forEach(function(tc){ if(hasTable(db,tc[0])&&hasCol(db,tc[0],tc[1])) refs.push('SELECT '+tc[1]+' FROM '+tc[0]+' WHERE '+tc[1]+' IS NOT NULL'); });
        if(!refs.length) return [];
        return col1(db,'SELECT LocationId FROM Location WHERE LocationId NOT IN ('+refs.join(' UNION ')+')');
      default: return [];
    }
  }

  function runChecks(db){
    var res={checks:{},totals:{},score:100,issues:0};
    res.totals.notes = hasTable(db,'Note')?qv(db,'SELECT COUNT(*) FROM Note'):0;
    res.totals.marks = hasTable(db,'UserMark')?qv(db,'SELECT COUNT(*) FROM UserMark'):0;
    res.totals.bm    = hasTable(db,'Bookmark')?qv(db,'SELECT COUNT(*) FROM Bookmark'):0;
    res.totals.tags  = hasTable(db,'Tag')?qv(db,'SELECT COUNT(*) FROM Tag'):0;
    var pen=0;
    CHECKS.forEach(function(k){
      var n=0; try{ n=idsFor(db,k).length; }catch(_){ n=0; }
      res.checks[k]=n; res.issues+=n; pen+=n*WEIGHTS[k];
    });
    res.score = res.issues===0 ? 100 : Math.max(35, Math.min(99, Math.round(100-pen)));
    return res;
  }

  function delNotes(db, ids){
    if(!ids.length) return;
    var list=ids.join(',');
    if(hasTable(db,'TagMap')) db.run('DELETE FROM TagMap WHERE NoteId IN ('+list+')');
    db.run('DELETE FROM Note WHERE NoteId IN ('+list+')');
  }
  function delMarks(db, ids){
    if(!ids.length) return;
    var list=ids.join(',');
    if(hasTable(db,'BlockRange')) db.run('DELETE FROM BlockRange WHERE UserMarkId IN ('+list+')');
    db.run('DELETE FROM UserMark WHERE UserMarkId IN ('+list+')');
  }
  // preview: strip tags/whitespace from note text for the review list
  function preview(s){
    var txt=String(s==null?'':s).replace(/<[^>]*>/g,' ').replace(/\s+/g,' ').trim();
    return txt.length>150 ? txt.slice(0,150)+'…' : txt;
  }
  // Group duplicate notes by the copy that will be KEPT, attaching that note's
  // title + content so the review screen can show exactly what is about to be
  // removed. Returns [{keep, dups:[ids], count, title, content}].
  function dupNoteGroups(db){
    var pairs=dupNotePairs(db);
    if(!pairs.length) return [];
    var byKeep={};
    pairs.forEach(function(p){ (byKeep[p.keep]=byKeep[p.keep]||[]).push(p.dup); });
    var ids={};
    Object.keys(byKeep).forEach(function(k){ ids[k]=1; byKeep[k].forEach(function(d){ ids[d]=1; }); });
    var idList=Object.keys(ids);
    if(!idList.length) return [];
    var meta={};
    try{
      q(db,"SELECT NoteId,IFNULL(Title,'') AS Title,IFNULL(Content,'') AS Content FROM Note WHERE NoteId IN ("+idList.join(',')+")")
        .forEach(function(r){ meta[r.NoteId]={title:r.Title,content:r.Content}; });
    }catch(_){}
    return Object.keys(byKeep).map(function(keep){
      var mrec=meta[keep]||{title:'',content:''};
      var dups=byKeep[keep].map(Number);
      return { keep:Number(keep), dups:dups, count:dups.length+1, title:mrec.title, content:mrec.content };
    });
  }
  // sel (optional): { skip:{checkKey:true}, excludeDup:{dupNoteId:true} }
  // With no argument every issue is fixed (unchanged behaviour). The review
  // screen passes a selection so users can keep specific duplicates/categories.
  function applyFixes(db, sel){
    sel=sel||{};
    var skip=sel.skip||{};
    var excludeDup=sel.excludeDup||null;
    var fixed={};
    var pairs=dupNotePairs(db);
    if(excludeDup) pairs=pairs.filter(function(p){ return !excludeDup[p.dup]; });
    if(hasTable(db,'TagMap')) pairs.forEach(function(p){
      // keep tag assignments: move the removed copy's tags onto the kept copy
      db.run('UPDATE TagMap SET NoteId='+p.keep+' WHERE NoteId='+p.dup+
             ' AND TagId IS NOT NULL AND TagId NOT IN (SELECT TagId FROM TagMap WHERE NoteId='+p.keep+' AND TagId IS NOT NULL)');
    });
    var dn=pairs.map(function(p){ return p.dup; }); delNotes(db,dn); fixed.dup_notes=dn.length;
    var en=skip.empty_notes?[]:idsFor(db,'empty_notes'); delNotes(db,en); fixed.empty_notes=en.length;
    var dm=skip.dup_marks?[]:idsFor(db,'dup_marks');   delMarks(db,dm); fixed.dup_marks=dm.length;
    var ob=skip.orph_br?[]:idsFor(db,'orph_br');     if(ob.length) db.run('DELETE FROM BlockRange WHERE BlockRangeId IN ('+ob.join(',')+')'); fixed.orph_br=ob.length;
    var ot=skip.orph_tm?[]:idsFor(db,'orph_tm');     if(ot.length) db.run('DELETE FROM TagMap WHERE TagMapId IN ('+ot.join(',')+')'); fixed.orph_tm=ot.length;
    var ut=skip.unused_tags?[]:idsFor(db,'unused_tags'); if(ut.length) db.run('DELETE FROM Tag WHERE TagId IN ('+ut.join(',')+')'); fixed.unused_tags=ut.length;
    var ul=skip.unused_loc?[]:idsFor(db,'unused_loc');  if(ul.length) db.run('DELETE FROM Location WHERE LocationId IN ('+ul.join(',')+')'); fixed.unused_loc=ul.length;
    try{ db.run('VACUUM'); }catch(_){}
    return fixed;
  }

  // ── File loading ────────────────────────────────────────────────────
  function loadDb(file){
    var name=(file&&file.name)||'backup.jwlibrary';
    var size=(file&&(file.size||file.byteLength))||0;
    var zipRef=null;
    return ensureDeps()
      .then(function(){ return window.JSZip.loadAsync(file).catch(function(){ throw {code:'read'}; }); })
      .then(function(zip){
        zipRef=zip;
        var dbKey=Object.keys(zip.files).find(function(k){ return /userdata\.db$/i.test(k); });
        if(!dbKey) throw {code:'db'};
        return zip.files[dbKey].async('uint8array').then(function(bytes){ return {bytes:bytes,dbKey:dbKey}; });
      })
      .then(function(r){
        return window.initSqlJs({locateFile:function(fn){ return SQLJS_CDN+fn; }}).then(function(SQL){
          var db;
          try{ db=new SQL.Database(r.bytes); qv(db,'SELECT COUNT(*) FROM sqlite_master'); }
          catch(_){ throw {code:'read'}; }
          return {db:db, zip:zipRef, dbKey:r.dbKey, name:name, size:size};
        });
      });
  }

  function dlBlob(blob){
    try{
      var base=((cur&&cur.name)||'backup.jwlibrary').replace(/\.jwlibrary$/i,'');
      var url=URL.createObjectURL(blob);
      var a=document.createElement('a');
      a.href=url; a.download='healthy_'+base+'.jwlibrary';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function(){ URL.revokeObjectURL(url); },4000);
    }catch(_){}
  }

  function exportCleaned(st){
    var bytes=st.db.export();
    st.zip.file(st.dbKey, bytes);
    var mf=st.zip.file('manifest.json');
    var p = mf ? mf.async('string').then(function(s){
      try{
        var raw=JSON.parse(s);
        raw.creationDate=new Date().toISOString();
        raw.name=(raw.name||'Backup')+' (Cleaned)';
        st.zip.file('manifest.json', JSON.stringify(raw,null,2));
      }catch(_){}
    }) : Promise.resolve();
    return p.then(function(){
      // Generate a raw buffer and wrap it in an application/octet-stream Blob
      // (NOT JSZip's default application/zip) so browsers — iOS Safari in
      // particular — save it as .jwlibrary, exactly like the merge tool does.
      return st.zip.generateAsync({type:'arraybuffer',compression:'DEFLATE',compressionOptions:{level:6}});
    }).then(function(buf){
      var blob=new Blob([buf],{type:'application/octet-stream'});
      if(!autoMode) dlBlob(blob); // auto mode: the Done screen offers the button
      return blob;
    });
  }

  // ── UI ──────────────────────────────────────────────────────────────
  var ICON_HEART='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></svg>';
  var ICON_CHECK='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>';
  var ICON_SHIELD='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>';
  var ICON_DL='<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="3" x2="12" y2="15"/></svg>';
  var ICON_BROOM='<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m13 11 9-9"/><path d="M14.6 12.6c.8.8.9 2 .2 2.8l-1.4 1.4a8 8 0 0 1-11.2 0 8 8 0 0 1 0-11.2l1.4-1.4c.8-.7 2-.6 2.8.2Z"/></svg>';

  var cur=null; // {overlay, db, zip, dbKey, name, size, report}
  var autoMode=false; // opened from the merge flow: auto-clean, single download

  function closeDoctor(){
    if(!cur) return;
    try{ if(cur.db) cur.db.close(); }catch(_){}
    if(cur.overlay) cur.overlay.remove();
    document.removeEventListener('keydown', onKey);
    cur=null;
  }
  function onKey(e){ if(e.key==='Escape') closeDoctor(); }

  function shell(){
    var ov=document.createElement('div');
    ov.className='jbd-overlay';
    ov.innerHTML=
      '<div class="jbd-backdrop" data-jbd-close></div>'+
      '<div class="jbd-card" role="dialog" aria-modal="true" aria-labelledby="jbd-title">'+
        '<button class="jbd-x" type="button" data-jbd-close aria-label="'+esc(t('close'))+'">×</button>'+
        '<div class="jbd-head">'+
          '<div class="jbd-head-ic">'+ICON_HEART+'</div>'+
          '<div><h2 class="jbd-title" id="jbd-title">'+esc(t('title'))+'</h2>'+
          '<p class="jbd-sub">'+esc(t('sub'))+'</p></div>'+
        '</div>'+
        '<div class="jbd-body"></div>'+
      '</div>';
    document.body.appendChild(ov);
    ov.querySelectorAll('[data-jbd-close]').forEach(function(el){
      el.addEventListener('click', closeDoctor);
    });
    document.addEventListener('keydown', onKey);
    return ov;
  }
  function body(){ return cur && cur.overlay.querySelector('.jbd-body'); }

  function renderPick(){
    var last=window.__jwLastFile;
    var b=body();
    b.innerHTML=
      '<button class="jbd-pick-btn" type="button" data-jbd-pick>'+ICON_HEART+' <span>'+esc(t('pick'))+'</span></button>'+
      (last&&last.name ? '<button class="jbd-use-last" type="button" data-jbd-last>'+esc(t('use_last').replace('{name}', last.name))+'</button>' : '')+
      '<div class="jbd-priv"><span class="jbd-priv-dot"></span><span>'+esc(t('priv'))+'</span></div>';
    var pick=b.querySelector('[data-jbd-pick]');
    pick.addEventListener('click', function(){
      var inp=document.createElement('input');
      inp.type='file'; inp.accept='.jwlibrary';
      inp.addEventListener('change', function(){ if(inp.files&&inp.files[0]) startScan(inp.files[0]); });
      inp.click();
    });
    var lastBtn=b.querySelector('[data-jbd-last]');
    if(lastBtn) lastBtn.addEventListener('click', function(){ startScan(window.__jwLastFile); });
  }

  function renderError(code){
    var b=body();
    b.innerHTML=
      '<div class="jbd-err">'+esc(t(code==='db'?'err_db':'err_read'))+'</div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';
    b.querySelector('[data-jbd-again]').addEventListener('click', renderPick);
  }

  function startScan(file){
    var b=body();
    var rows=CHECKS.map(function(k){
      return '<div class="jbd-row" data-jbd-row="'+k+'">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-row-state"></span>'+
      '</div>';
    }).join('');
    b.innerHTML=
      '<div class="jbd-ecg-wrap"><svg class="jbd-ecg" viewBox="0 0 560 74" preserveAspectRatio="none">'+
        '<path d="M0,40 L120,40 L138,40 L146,16 L154,58 L162,30 L170,40 L300,40 L318,40 L326,16 L334,58 L342,30 L350,40 L560,40"/>'+
      '</svg></div>'+
      '<p class="jbd-scan-file">'+esc(t('scanning'))+' · '+esc((file&&file.name)||'backup.jwlibrary')+'</p>'+
      '<div class="jbd-rows">'+rows+'</div>';
    loadDb(file).then(function(st){
      cur.db=st.db; cur.zip=st.zip; cur.dbKey=st.dbKey; cur.name=st.name; cur.size=st.size;
      // progressive reveal: one check at a time
      var report={checks:{},totals:{},score:100,issues:0};
      report.totals.notes = hasTable(st.db,'Note')?qv(st.db,'SELECT COUNT(*) FROM Note'):0;
      report.totals.marks = hasTable(st.db,'UserMark')?qv(st.db,'SELECT COUNT(*) FROM UserMark'):0;
      report.totals.bm    = hasTable(st.db,'Bookmark')?qv(st.db,'SELECT COUNT(*) FROM Bookmark'):0;
      report.totals.tags  = hasTable(st.db,'Tag')?qv(st.db,'SELECT COUNT(*) FROM Tag'):0;
      var pen=0, i=0;
      function step(){
        if(!cur) return;
        if(i>=CHECKS.length){
          report.score = report.issues===0 ? 100 : Math.max(35, Math.min(99, Math.round(100-pen)));
          cur.report=report;
          setTimeout(function(){ if(cur) renderReport(); }, 420);
          return;
        }
        var k=CHECKS[i++];
        var row=b.querySelector('[data-jbd-row="'+k+'"]');
        if(row){ row.classList.add('jbd-on'); var stEl=row.querySelector('.jbd-row-state'); stEl.innerHTML='<span class="jbd-row-spin"></span>'; }
        setTimeout(function(){
          if(!cur) return;
          var n=0; try{ n=idsFor(cur.db,k).length; }catch(_){ n=0; }
          report.checks[k]=n; report.issues+=n; pen+=n*WEIGHTS[k];
          if(row){
            var stEl=row.querySelector('.jbd-row-state');
            stEl.innerHTML = n===0
              ? '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+'</span>'
              : '<span class="jbd-chip jbd-chip-warn">'+n+'</span>';
          }
          setTimeout(step, 140);
        }, 170);
      }
      step();
    }).catch(function(e){ if(cur) renderError(e&&e.code); });
  }

  function tier(score){ return score>=97?'a':score>=85?'b':score>=65?'c':'d'; }

  // Shared clean routine: applies fixes (optionally a review selection),
  // exports the cleaned copy, then shows the Done screen.
  function doClean(btnEl, sel){
    if(btnEl){ btnEl.disabled=true; btnEl.innerHTML='<span class="jbd-row-spin" style="border-top-color:#fff"></span> <span>'+esc(t('cleaning'))+'</span>'; }
    setTimeout(function(){
      if(!cur) return;
      try{
        var fixed=applyFixes(cur.db, sel||{});
        exportCleaned(cur).then(function(blob){ if(cur) renderDone(fixed, blob||null); }).catch(function(){ if(cur) renderDone(fixed, null); });
      }catch(_){ renderError('read'); }
    }, 60);
  }

  // Review screen: lists the actual duplicate notes (title + preview) plus the
  // other cleanup categories, each with a checkbox. Nothing is deleted until
  // the user confirms; unchecking an item leaves it untouched.
  function renderReview(){
    var r=cur.report, b=body();
    var groups=[]; try{ groups=dupNoteGroups(cur.db); }catch(_){ groups=[]; }
    var otherKeys=CHECKS.filter(function(k){ return k!=='dup_notes' && (r.checks[k]||0)>0; });
    var dupHtml=groups.map(function(g,idx){
      var ttl=g.title&&g.title.trim() ? esc(g.title.trim()) : '<em class="jbd-rv-untitled">'+esc(t('rv_notitle'))+'</em>';
      var prev=preview(g.content);
      return '<label class="jbd-rv-item">'+
          '<input type="checkbox" class="jbd-rv-cb" data-jbd-dupgrp="'+idx+'" checked>'+
          '<span class="jbd-rv-main">'+
            '<span class="jbd-rv-title">'+ttl+'</span>'+
            (prev?'<span class="jbd-rv-prev">'+esc(prev)+'</span>':'')+
            '<span class="jbd-rv-badges">'+
              '<span class="jbd-rv-badge jbd-rv-keep">'+esc(t('rv_kept'))+'</span>'+
              '<span class="jbd-rv-badge jbd-rv-rm">'+esc(t('rv_remove_n').replace('{n}', g.dups.length))+'</span>'+
            '</span>'+
          '</span>'+
        '</label>';
    }).join('');
    var otherHtml=otherKeys.map(function(k){
      return '<label class="jbd-rv-other">'+
          '<input type="checkbox" class="jbd-rv-cb" data-jbd-cat="'+k+'" checked>'+
          '<span class="jbd-rv-other-label">'+esc(t('c_'+k))+'</span>'+
          '<span class="jbd-chip jbd-chip-warn">'+(r.checks[k]||0)+'</span>'+
        '</label>';
    }).join('');
    b.innerHTML=
      '<div class="jbd-rv-head">'+
        '<h3 class="jbd-rv-h">'+esc(t('rv_t'))+'</h3>'+
        '<p class="jbd-rv-d">'+esc(t('rv_d'))+'</p>'+
      '</div>'+
      (groups.length ? '<div class="jbd-rv-sec">'+esc(t('rv_dups_h'))+'</div><div class="jbd-rv-list">'+dupHtml+'</div>' : '')+
      (otherKeys.length ? '<div class="jbd-rv-sec">'+esc(t('rv_other_h'))+'</div><div class="jbd-rv-list">'+otherHtml+'</div>' : '')+
      '<p class="jbd-rv-warn" data-jbd-warn hidden>'+esc(t('rv_none'))+'</p>'+
      '<button class="jbd-clean-btn" type="button" data-jbd-confirm>'+ICON_BROOM+' <span>'+esc(t('clean'))+'</span></button>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-back>'+esc(t('back'))+'</button>'+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>';
    b.querySelector('[data-jbd-back]').addEventListener('click', renderReport);
    var confirmBtn=b.querySelector('[data-jbd-confirm]');
    confirmBtn.addEventListener('click', function(){
      var excludeDup={}, anyDup=false;
      b.querySelectorAll('[data-jbd-dupgrp]').forEach(function(cb){
        var g=groups[+cb.getAttribute('data-jbd-dupgrp')];
        if(cb.checked){ anyDup=true; }
        else if(g){ g.dups.forEach(function(id){ excludeDup[id]=true; }); }
      });
      var skip={}, anyOther=false;
      b.querySelectorAll('[data-jbd-cat]').forEach(function(cb){
        if(cb.checked) anyOther=true; else skip[cb.getAttribute('data-jbd-cat')]=true;
      });
      if(!anyDup && !anyOther){ var w=b.querySelector('[data-jbd-warn]'); if(w) w.hidden=false; return; }
      doClean(confirmBtn, {excludeDup:excludeDup, skip:skip});
    });
  }

  function renderReport(){
    var r=cur.report, b=body();
    var C=326.7, tr=tier(r.score);
    var rows=CHECKS.map(function(k){
      var n=r.checks[k]||0;
      return '<div class="jbd-row jbd-on" data-jbd-row="'+k+'">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-row-state">'+(n===0
          ? '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+'</span>'
          : '<span class="jbd-chip jbd-chip-warn">'+n+'</span>')+'</span>'+
      '</div>';
    }).join('');
    b.innerHTML=
      '<div class="jbd-ring-wrap">'+
        '<svg class="jbd-ring" viewBox="0 0 120 120">'+
          '<circle class="jbd-ring-bg" cx="60" cy="60" r="52"/>'+
          '<circle class="jbd-ring-fg jbd-tier-'+tr+'" cx="60" cy="60" r="52" stroke-dasharray="'+C+'" stroke-dashoffset="'+C+'"/>'+
        '</svg>'+
        '<div class="jbd-ring-num"><strong>0</strong><span>'+esc(t('health'))+'</span></div>'+
      '</div>'+
      '<div class="jbd-verdict"><span class="jbd-verdict-pill jbd-verdict-'+tr+'">'+esc(t('v_'+tr))+'</span></div>'+
      '<div class="jbd-totals">'+
        '<div class="jbd-total"><strong>'+r.totals.notes+'</strong><span>'+esc(t('l_notes'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.marks+'</strong><span>'+esc(t('l_marks'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.bm+'</strong><span>'+esc(t('l_bm'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.tags+'</strong><span>'+esc(t('l_tags'))+'</span></div>'+
      '</div>'+
      (r.issues>0
        ? '<p class="jbd-issues-line">'+esc((r.issues===1?t('issues_one'):t('issues_many')).replace('{n}', r.issues))+'</p>'
        : '<div class="jbd-perfect">'+ICON_CHECK+' '+esc(t('perfect'))+'</div>')+
      '<div class="jbd-rows">'+rows+'</div>'+
      (r.issues>0
        ? (autoMode
            ? '<button class="jbd-clean-btn" type="button" data-jbd-clean>'+ICON_BROOM+' <span>'+esc(t('clean'))+'</span></button>'
            : '<button class="jbd-clean-btn" type="button" data-jbd-review>'+ICON_BROOM+' <span>'+esc(t('review'))+'</span></button>')
        : (autoMode ? '<button class="jbd-clean-btn" type="button" data-jbd-dlmerged>'+ICON_DL+' <span>'+esc(t('download'))+'</span></button>' : ''))+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';

    // animate ring + score count-up
    var fg=b.querySelector('.jbd-ring-fg'), num=b.querySelector('.jbd-ring-num strong');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){
      if(fg) fg.style.strokeDashoffset=(C*(1-r.score/100)).toFixed(1);
    }); });
    var elapsed=0, dur=1100;
    var iv=setInterval(function(){
      elapsed+=16;
      var p=Math.min(elapsed/dur,1), ease=1-Math.pow(1-p,4);
      if(num) num.textContent=Math.round(r.score*ease);
      if(p>=1) clearInterval(iv);
    },16);

    var cleanBtn=b.querySelector('[data-jbd-clean]');
    if(cleanBtn) cleanBtn.addEventListener('click', function(){ doClean(cleanBtn); });
    var reviewBtn=b.querySelector('[data-jbd-review]');
    if(reviewBtn) reviewBtn.addEventListener('click', renderReview);
    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
    if(autoMode){
      if(r.issues>0){
        // start the clean by itself after the score has a moment to show
        setTimeout(function(){
          if(!cur||!cur.report) return;
          var btn=cur.overlay.querySelector('[data-jbd-clean]');
          if(btn&&!btn.disabled) btn.click();
        },1100);
      } else {
        var dlm=b.querySelector('[data-jbd-dlmerged]');
        if(dlm) dlm.addEventListener('click', function(){
          var a=document.getElementById('download-btn');
          if(a) a.click();
        });
      }
    }
  }

  function renderDone(fixed, blob){
    var b=body();
    var newSize=blob?blob.size:0;
    var fixedRows=CHECKS.filter(function(k){ return fixed[k]>0; }).map(function(k){
      return '<div class="jbd-row jbd-on jbd-row-fixed">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+' '+fixed[k]+'</span>'+
      '</div>';
    }).join('');
    var sizeRow='';
    if(cur.size>0 && newSize>0 && newSize<cur.size){
      var pct=Math.round((1-newSize/cur.size)*100);
      sizeRow='<div class="jbd-size-row"><span>'+fmtSize(cur.size)+'</span><span class="jbd-size-arrow">→</span><span>'+fmtSize(newSize)+'</span>'+
        (pct>=1?'<span class="jbd-size-pct">↓ '+pct+'% '+esc(t('smaller'))+'</span>':'')+'</div>';
    }
    b.innerHTML=
      '<div class="jbd-done-ic"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>'+
      '<h3 class="jbd-done-t">'+esc(t('done_t'))+'</h3>'+
      '<p class="jbd-done-d">'+esc(t(autoMode&&blob?'done_ready':'done_d'))+'</p>'+
      sizeRow+
      '<div class="jbd-rows">'+fixedRows+'</div>'+
      (autoMode&&blob ? '<button class="jbd-clean-btn" type="button" data-jbd-dl>'+ICON_DL+' <span>'+esc(t('download'))+'</span></button>' : '')+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';
    var dlBtn=b.querySelector('[data-jbd-dl]');
    if(dlBtn) dlBtn.addEventListener('click', function(){ dlBlob(blob); });
    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function openDoctor(file, opts){
    closeDoctor();
    autoMode=!!(opts&&opts.auto);
    cur={overlay:shell(), db:null, zip:null, dbKey:null, name:null, size:0, report:null};
    if(file) startScan(file); else renderPick();
  }

  window.__openJwDoctor = openDoctor;
  // Localised Doctor strings for other modules (the pre-merge impact card
  // renders the worker's doctor report with these).
  window.__jwDoctorT = function(k){ return t(k); };
  window.__jwDoctorInternals = { runChecks:runChecks, applyFixes:applyFixes, idsFor:idsFor, dupNoteGroups:dupNoteGroups };
})();

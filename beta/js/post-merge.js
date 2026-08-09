/* ──────────────────────────────────────────────────────────────────────────
   post-merge.js — Post-merge celebration screen + Restore Guide (window.__jwOpenGuide).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var DONATE_URL = 'https://www.paypal.com/paypalme/jwsync';

  // Localised UI strings. Long restore-guide step text stays in English for
  // now (translation effort is bigger than the dialogue itself).
  var I18N = {
    en: { close: 'Close', cele_title: 'Merge complete', cele_subtitle: 'You combined your backups into a single unified file.', stat_notes: 'notes', stat_highlights: 'highlights', stat_bookmarks: 'bookmarks', stat_tags: 'tags', cele_download: 'Download merged backup', cele_redownload: 'Download again', cele_downloading: 'Your file is downloading…', cele_browse: 'Browse the merged result', cele_restore: 'Restore to JW Library', cele_demo_title: 'That was a demo with sample data', cele_demo_body: 'Ready to try with your own JW Library backups?', cele_demo_cta: 'Use my real files', donate_prompt: 'Found JW Sync useful?', donate_cta: 'Support development', guide_title: 'How to restore to JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Other / Desktop', guide_warning: 'Restoring replaces the notes currently in JW Library. Keep this merged backup as your master copy.', guide_done: 'Got it', guide_export_title: 'How to export from JW Library', guide_mode_export: 'Export backups', guide_mode_restore: 'Restore merged file', cele_highlights: 'View Your Stats', cele_addshared: 'Add notes a friend shared' , perf_title: 'Merge performance', perf_prepare: 'Prepare', perf_merge: 'Merge', perf_package: 'Package', perf_tip_large: 'Large library — for faster merges, combine fewer files at once or use date-range extraction.',cele_top_medals:'Your top medals',cele_awards_btn:'Explore Your Awards →' },
    es: { close: 'Cerrar', cele_title: '¡Fusión completa!', cele_subtitle: 'Combinaste tus copias en un solo archivo unificado.', stat_notes: 'notas', stat_highlights: 'resaltados', stat_bookmarks: 'marcadores', stat_tags: 'etiquetas', cele_download: 'Descargar copia fusionada', cele_redownload: 'Descargar de nuevo', cele_downloading: 'Tu archivo se está descargando…', cele_browse: 'Explorar el resultado', cele_restore: 'Restaurar en JW Library', cele_demo_title: 'Eso fue una demo con datos de muestra', cele_demo_body: '¿Listo para probar con tus propias copias de JW Library?', cele_demo_cta: 'Usar mis archivos reales', donate_prompt: '¿Te resulta útil JW Sync?', donate_cta: 'Apoyar el desarrollo', guide_title: 'Cómo restaurar en JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Otro / Escritorio', guide_warning: 'Al restaurar se reemplazan las notas actuales en JW Library. Guarda esta copia como tu archivo maestro.', guide_done: 'Entendido', guide_export_title: 'Cómo exportar desde JW Library', guide_mode_export: 'Exportar copias', guide_mode_restore: 'Restaurar archivo', cele_highlights: 'Ver tus estadísticas', cele_addshared: 'Añadir notas de un amigo' , perf_title: 'Rendimiento de la fusión', perf_prepare: 'Preparar', perf_merge: 'Fusionar', perf_package: 'Empaquetar', perf_tip_large: 'Biblioteca grande: para fusiones más rápidas, combina menos archivos a la vez o usa la extracción por fecha.',cele_top_medals:'Tus mejores medallas',cele_awards_btn:'Explorar premios →' },
    pt: { close: 'Fechar', cele_title: 'Mesclagem concluída!', cele_subtitle: 'Você combinou seus backups em um único arquivo unificado.', stat_notes: 'notas', stat_highlights: 'destaques', stat_bookmarks: 'marcadores', stat_tags: 'etiquetas', cele_download: 'Baixar backup mesclado', cele_redownload: 'Baixar novamente', cele_downloading: 'Seu arquivo está sendo baixado…', cele_browse: 'Explorar o resultado', cele_restore: 'Restaurar no JW Library', cele_demo_title: 'Isso foi uma demo com dados de exemplo', cele_demo_body: 'Pronto para experimentar com seus próprios backups do JW Library?', cele_demo_cta: 'Usar meus arquivos reais', donate_prompt: 'JW Sync foi útil pra você?', donate_cta: 'Apoiar o desenvolvimento', guide_title: 'Como restaurar no JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Outro / Desktop', guide_warning: 'A restauração substitui as notas atuais no JW Library. Guarde esse backup mesclado como sua cópia mestre.', guide_done: 'Entendi', guide_export_title: 'Como exportar do JW Library', guide_mode_export: 'Exportar backups', guide_mode_restore: 'Restaurar arquivo', cele_highlights: 'Ver estatísticas', cele_addshared: 'Adicionar notas de um amigo' , perf_title: 'Desempenho da mesclagem', perf_prepare: 'Preparar', perf_merge: 'Mesclar', perf_package: 'Empacotar', perf_tip_large: 'Biblioteca grande: para mesclagens mais rápidas, combine menos arquivos por vez ou use a extração por data.',cele_top_medals:'Suas melhores medalhas',cele_awards_btn:'Explorar prêmios →' },
    fr: { close: 'Fermer', cele_title: 'Fusion terminée !', cele_subtitle: 'Vous avez combiné vos sauvegardes en un seul fichier unifié.', stat_notes: 'notes', stat_highlights: 'surlignages', stat_bookmarks: 'signets', stat_tags: 'étiquettes', cele_download: 'Télécharger la sauvegarde fusionnée', cele_redownload: 'Télécharger à nouveau', cele_downloading: 'Votre fichier est en cours de téléchargement…', cele_browse: 'Explorer le résultat', cele_restore: 'Restaurer dans JW Library', cele_demo_title: 'C’était une démo avec des données d’exemple', cele_demo_body: 'Prêt à essayer avec vos propres sauvegardes JW Library ?', cele_demo_cta: 'Utiliser mes vrais fichiers', donate_prompt: 'JW Sync vous est utile ?', donate_cta: 'Soutenir le développement', guide_title: 'Comment restaurer dans JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Autre / Bureau', guide_warning: 'La restauration remplace les notes actuelles dans JW Library. Gardez cette sauvegarde fusionnée comme copie maîtresse.', guide_done: 'Compris', guide_export_title: 'Comment exporter depuis JW Library', guide_mode_export: 'Exporter les sauvegardes', guide_mode_restore: 'Restaurer le fichier', cele_highlights: 'Voir vos stats', cele_addshared: 'Ajouter des notes d’un ami' , perf_title: 'Performance de la fusion', perf_prepare: 'Préparer', perf_merge: 'Fusionner', perf_package: 'Empaqueter', perf_tip_large: 'Grande bibliothèque : pour des fusions plus rapides, combinez moins de fichiers à la fois ou utilisez l’extraction par date.',cele_top_medals:'Vos meilleures médailles',cele_awards_btn:'Explorer vos récompenses →' },
    de: { close: 'Schließen', cele_title: 'Zusammenführung abgeschlossen!', cele_subtitle: 'Du hast deine Backups in einer einzigen Datei vereint.', stat_notes: 'Notizen', stat_highlights: 'Hervorhebungen', stat_bookmarks: 'Lesezeichen', stat_tags: 'Etiketten', cele_download: 'Zusammengeführtes Backup herunterladen', cele_redownload: 'Erneut herunterladen', cele_downloading: 'Deine Datei wird heruntergeladen…', cele_browse: 'Ergebnis durchsuchen', cele_restore: 'In JW Library wiederherstellen', cele_demo_title: 'Das war eine Demo mit Beispieldaten', cele_demo_body: 'Bereit, es mit deinen eigenen JW Library-Backups zu versuchen?', cele_demo_cta: 'Meine echten Dateien verwenden', donate_prompt: 'Findest du JW Sync nützlich?', donate_cta: 'Entwicklung unterstützen', guide_title: 'So stellst du in JW Library wieder her', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Andere / Desktop', guide_warning: 'Eine Wiederherstellung ersetzt die aktuellen Notizen in JW Library. Bewahre dieses zusammengeführte Backup als Master-Kopie auf.', guide_done: 'Verstanden', guide_export_title: 'So exportierst du aus JW Library', guide_mode_export: 'Backups exportieren', guide_mode_restore: 'Datei wiederherstellen', cele_highlights: 'Statistiken ansehen', cele_addshared: 'Notizen eines Freundes hinzufügen' , perf_title: 'Zusammenführungs-Leistung', perf_prepare: 'Vorbereiten', perf_merge: 'Zusammenführen', perf_package: 'Verpacken', perf_tip_large: 'Große Bibliothek — für schnellere Zusammenführungen weniger Dateien auf einmal kombinieren oder die Datumsbereich-Extraktion nutzen.',cele_top_medals:'Deine besten Medaillen',cele_awards_btn:'Auszeichnungen erkunden →' },
    it: { close: 'Chiudi', cele_title: 'Fusione completata!', cele_subtitle: 'Hai combinato i tuoi backup in un singolo file unificato.', stat_notes: 'note', stat_highlights: 'evidenziazioni', stat_bookmarks: 'segnalibri', stat_tags: 'etichette', cele_download: 'Scarica backup unificato', cele_redownload: 'Scarica di nuovo', cele_downloading: 'Il tuo file si sta scaricando…', cele_browse: 'Esplora il risultato', cele_restore: 'Ripristina in JW Library', cele_demo_title: 'Era una demo con dati di esempio', cele_demo_body: 'Pronto a provarla con i tuoi backup di JW Library?', cele_demo_cta: 'Usa i miei file reali', donate_prompt: 'Trovi utile JW Sync?', donate_cta: 'Sostieni lo sviluppo', guide_title: 'Come ripristinare in JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Altro / Desktop', guide_warning: 'Il ripristino sostituisce le note correnti in JW Library. Conserva questo backup unificato come copia principale.', guide_done: 'Ho capito', guide_export_title: 'Come esportare da JW Library', guide_mode_export: 'Esporta backup', guide_mode_restore: 'Ripristina file', cele_highlights: 'Vedi le statistiche', cele_addshared: 'Aggiungi note di un amico' , perf_title: 'Prestazioni dell’unione', perf_prepare: 'Preparare', perf_merge: 'Unire', perf_package: 'Pacchettizzare', perf_tip_large: 'Biblioteca grande: per unioni più veloci, combina meno file alla volta o usa l’estrazione per data.',cele_top_medals:'Le tue migliori medaglie',cele_awards_btn:'Esplora i premi →' },
    ru: { close: 'Закрыть', cele_title: 'Объединение завершено!', cele_subtitle: 'Вы объединили резервные копии в один файл.', stat_notes: 'заметок', stat_highlights: 'выделений', stat_bookmarks: 'закладок', stat_tags: 'тегов', cele_download: 'Скачать объединённую копию', cele_redownload: 'Скачать ещё раз', cele_downloading: 'Ваш файл загружается…', cele_browse: 'Просмотреть результат', cele_restore: 'Восстановить в JW Library', cele_demo_title: 'Это была демо с примерами', cele_demo_body: 'Готовы попробовать со своими резервными копиями JW Library?', cele_demo_cta: 'Использовать свои файлы', donate_prompt: 'JW Sync оказался полезен?', donate_cta: 'Поддержать разработку', guide_title: 'Как восстановить в JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Другое / Десктоп', guide_warning: 'Восстановление заменит текущие заметки в JW Library. Сохраните этот объединённый файл как мастер-копию.', guide_done: 'Понятно', guide_export_title: 'Как экспортировать из JW Library', guide_mode_export: 'Экспорт копий', guide_mode_restore: 'Восстановить файл', cele_highlights: 'Посмотреть статистику', cele_addshared: 'Добавить заметки друга' , perf_title: 'Производительность объединения', perf_prepare: 'Подготовка', perf_merge: 'Объединение', perf_package: 'Упаковка', perf_tip_large: 'Большая библиотека — для ускорения объединяйте меньше файлов за раз или используйте извлечение по дате.',cele_top_medals:'Ваши лучшие медали',cele_awards_btn:'Смотреть награды →' },
    ja: { close: '閉じる', cele_title: 'マージが完了しました', cele_subtitle: '複数のバックアップを1つの統合ファイルにまとめました。', stat_notes: 'ノート', stat_highlights: 'ハイライト', stat_bookmarks: 'ブックマーク', stat_tags: 'タグ', cele_download: '統合バックアップをダウンロード', cele_redownload: 'もう一度ダウンロード', cele_downloading: 'ファイルをダウンロードしています…', cele_browse: 'マージ結果を閲覧', cele_restore: 'JW Library に復元', cele_demo_title: 'これはサンプルデータを使ったデモでした', cele_demo_body: '実際の JW Library バックアップで試してみますか？', cele_demo_cta: '自分のファイルを使う', donate_prompt: 'JW Sync は役に立ちましたか？', donate_cta: '開発を応援する', guide_title: 'JW Library への復元方法', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'その他 / デスクトップ', guide_warning: '復元すると JW Library の現在のノートが置き換わります。このマージ済みバックアップをマスターコピーとして保管してください。', guide_done: 'わかった', guide_export_title: 'JW Library からの書き出し方法', guide_mode_export: 'バックアップを書き出す', guide_mode_restore: '統合ファイルを復元', cele_highlights: '統計を見る', cele_addshared: '友達のノートを追加' , perf_title: 'マージのパフォーマンス', perf_prepare: '準備', perf_merge: 'マージ', perf_package: 'パッケージ', perf_tip_large: '大きなライブラリです。より速くマージするには、一度に結合するファイルを減らすか、日付範囲の抽出を使ってください。',cele_top_medals:'トップメダル',cele_awards_btn:'実績を見る →' },
    ko: { close: '닫기', cele_title: '병합 완료!', cele_subtitle: '백업을 하나의 통합 파일로 합쳤습니다.', stat_notes: '노트', stat_highlights: '하이라이트', stat_bookmarks: '북마크', stat_tags: '태그', cele_download: '병합 백업 다운로드', cele_redownload: '다시 다운로드', cele_downloading: '파일을 다운로드하는 중입니다…', cele_browse: '병합된 결과 탐색', cele_restore: 'JW Library에 복원', cele_demo_title: '샘플 데이터로 진행한 데모였습니다', cele_demo_body: '실제 JW Library 백업으로 시도할 준비가 되셨나요?', cele_demo_cta: '내 실제 파일 사용', donate_prompt: 'JW Sync가 유용했나요?', donate_cta: '개발 지원하기', guide_title: 'JW Library에 복원하는 방법', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: '기타 / 데스크톱', guide_warning: '복원하면 JW Library의 현재 노트가 대체됩니다. 이 병합된 백업을 마스터 사본으로 보관하세요.', guide_done: '확인', guide_export_title: 'JW Library에서 내보내는 방법', guide_mode_export: '백업 내보내기', guide_mode_restore: '병합 파일 복원', cele_highlights: '통계 보기', cele_addshared: '친구의 노트 추가' , perf_title: '병합 성능', perf_prepare: '준비', perf_merge: '병합', perf_package: '패키지', perf_tip_large: '큰 라이브러리입니다. 더 빠른 병합을 위해 한 번에 더 적은 파일을 결합하거나 날짜 범위 추출을 사용하세요.',cele_top_medals:'최고 메달',cele_awards_btn:'수상 보기 →' },
    tl: { close: 'Isara', cele_title: 'Tapos ang merge!', cele_subtitle: 'Pinagsama mo ang iyong mga backup sa isang pinag-isang file.', stat_notes: 'mga tala', stat_highlights: 'mga highlight', stat_bookmarks: 'mga bookmark', stat_tags: 'mga tag', cele_download: 'I-download ang merged backup', cele_redownload: 'I-download muli', cele_downloading: 'Dina-download na ang iyong file…', cele_browse: 'Tingnan ang merged na resulta', cele_restore: 'I-restore sa JW Library', cele_demo_title: 'Iyon ay isang demo gamit ang sample data', cele_demo_body: 'Handa nang subukan gamit ang sarili mong JW Library backup?', cele_demo_cta: 'Gamitin ang aking mga file', donate_prompt: 'Nakatulong sa iyo ang JW Sync?', donate_cta: 'Suportahan ang pag-develop', guide_title: 'Paano i-restore sa JW Library', guide_tab_ios: 'iPhone / iPad', guide_tab_android: 'Android', guide_tab_other: 'Iba / Desktop', guide_warning: 'Papalitan ng restore ang kasalukuyang mga tala sa JW Library. Panatilihin ang merged backup na ito bilang master copy.', guide_done: 'Sige', guide_export_title: 'Paano mag-export mula sa JW Library', guide_mode_export: 'Mag-export ng backup', guide_mode_restore: 'I-restore ang file', cele_highlights: 'Tingnan ang stats', cele_addshared: 'Magdagdag ng tala ng kaibigan' , perf_title: 'Performance ng merge', perf_prepare: 'Ihanda', perf_merge: 'Pagsamahin', perf_package: 'I-package', perf_tip_large: 'Malaking library — para sa mas mabilis na merge, magsama ng mas kaunting file o gamitin ang date-range extraction.',cele_top_medals:'Iyong nangungunang mga medalya',cele_awards_btn:'I-explore ang mga gantimpala →' }
  ,sv:{close:"Stäng",cele_title:"Sammanslagning klar",cele_subtitle:"Du kombinerade dina säkerhetskopior till en enda enhetlig fil.",stat_notes:"anteckningar",stat_highlights:"överstrykningar",stat_bookmarks:"bokmärken",stat_tags:"taggar",cele_download:"Ladda ner sammanslagen säkerhetskopia",cele_redownload:"Ladda ner igen",cele_downloading:"Din fil laddas ner…",cele_browse:"Bläddra i det sammanslagna resultatet",cele_restore:"Återställ till JW Library",cele_demo_title:"Det var en demo med exempeldata",cele_demo_body:"Redo att testa med dina egna JW Library-säkerhetskopior?",cele_demo_cta:"Använd mina riktiga filer",donate_prompt:"Tycker du att JW Sync är användbar?",donate_cta:"Stöd utvecklingen",guide_title:"Så återställer du till JW Library",guide_tab_ios:"iPhone / iPad",guide_tab_android:"Android",guide_tab_other:"Övrigt / Dator",guide_warning:"Återställning ersätter anteckningarna som finns i JW Library just nu. Behåll den här sammanslagna säkerhetskopian som din originalkopia.",guide_done:"Uppfattat",guide_export_title:"Så exporterar du från JW Library",guide_mode_export:"Exportera säkerhetskopior",guide_mode_restore:"Återställ sammanslagen fil",cele_highlights:"Visa din statistik",cele_addshared:"Lägg till anteckningar en vän delat",perf_title:"Sammanslagningens prestanda",perf_prepare:"Förbered",perf_merge:"Slå ihop",perf_package:"Paketera",perf_tip_large:"Stort bibliotek — för snabbare sammanslagningar, kombinera färre filer åt gången eller använd extrahering per datumintervall.",cele_top_medals:"Dina bästa medaljer",cele_awards_btn:"Utforska utmärkelserna →"},ceb:{close:'Isira',cele_title:'Natapos ang merge!',cele_subtitle:'Gisagol mo ang imong mga backup ngadto sa usa ka pinag-isang file.',stat_notes:'mga nota',stat_highlights:'mga highlight',stat_bookmarks:'mga bookmark',stat_tags:'mga tag',cele_download:'I-download ang gisagol nga backup',cele_redownload:'I-download pag-usab',cele_downloading:'Gi-download na ang imong file…',cele_browse:'Tan-awon ang resulta sa merge',cele_restore:'I-restore sa JW Library',cele_demo_title:'Usa ka demo gamit ang sample data ang nahitabo',cele_demo_body:'Andam na nga sulayin gamit ang imong kaugalingong mga backup sa JW Library?',cele_demo_cta:'Gamita ang akong mga file',donate_prompt:'Nakatabang ba kanimo ang JW Sync?',donate_cta:'Suportahan ang pag-develop',guide_title:'Unsaon pag-restore sa JW Library',guide_tab_ios:'iPhone / iPad',guide_tab_android:'Android',guide_tab_other:'Uban / Desktop',guide_warning:'Mapulihan sa restore ang kasamtangan nga mga nota sa JW Library. Tipigan kining gisagol nga backup isip imong master copy.',guide_done:'Nasabtan',guide_export_title:'Unsaon pag-export gikan sa JW Library',guide_mode_export:'Mag-export ug backup',guide_mode_restore:'I-restore ang file',cele_highlights:'Tan-awa ang mga Stats',cele_addshared:'Idugang ang mga nota sa higala',perf_title:'Performance sa merge',perf_prepare:'Andam-anama',perf_merge:'Isagol',perf_package:'I-package',perf_tip_large:'Dako nga librarya — para sa mas paspas nga merge, magsagol ug mas gamay nga mga file sa usa ka higayon o gamiton ang date-range extraction.',cele_top_medals:'Imong pinakataas nga mga medalya',cele_awards_btn:'I-explore ang mga ganti →'},uk:{close:"Закрити",cele_title:"Об'єднання завершено",cele_subtitle:"Ви поєднали свої резервні копії в один спільний файл.",stat_notes:"нотаток",stat_highlights:"виділень",stat_bookmarks:"закладок",stat_tags:"тегів",cele_download:"Завантажити об'єднану копію",cele_redownload:"Завантажити ще раз",cele_downloading:"Ваш файл завантажується…",cele_browse:"Переглянути об'єднаний результат",cele_restore:"Відновити в JW Library",cele_demo_title:"Це була демонстрація зі зразковими даними",cele_demo_body:"Готові спробувати з власними резервними копіями JW Library?",cele_demo_cta:"Використати мої справжні файли",donate_prompt:"JW Sync став вам у пригоді?",donate_cta:"Підтримати розробку",guide_title:"Як відновити в JW Library",guide_tab_ios:"iPhone / iPad",guide_tab_android:"Android",guide_tab_other:"Інше / Комп'ютер",guide_warning:"Відновлення замінює нотатки, які зараз є в JW Library. Зберігайте цю об'єднану копію як основну.",guide_done:"Зрозуміло",guide_export_title:"Як експортувати з JW Library",guide_mode_export:"Експорт резервних копій",guide_mode_restore:"Відновлення об'єднаного файлу",cele_highlights:"Переглянути статистику",cele_addshared:"Додати нотатки, якими поділився друг",perf_title:"Продуктивність об'єднання",perf_prepare:"Підготовка",perf_merge:"Об'єднання",perf_package:"Пакування",perf_tip_large:"Велика бібліотека — щоб об'єднувати швидше, поєднуйте менше файлів за раз або використовуйте вибірку за діапазоном дат.",cele_top_medals:"Ваші найкращі медалі",cele_awards_btn:"Переглянути свої нагороди →"},he:{close:"סגירה",cele_title:"המיזוג הושלם",cele_subtitle:"איחדתם את הגיבויים שלכם לקובץ אחד מאוחד.",stat_notes:"הערות",stat_highlights:"הדגשות",stat_bookmarks:"סימניות",stat_tags:"תוויות",cele_download:"הורדת הגיבוי הממוזג",cele_redownload:"הורדה שוב",cele_downloading:"הקובץ שלכם יורד…",cele_browse:"עיון בתוצאה הממוזגת",cele_restore:"שחזור אל JW Library",cele_demo_title:"זו הייתה הדגמה עם נתוני דוגמה",cele_demo_body:"מוכנים לנסות עם הגיבויים האמיתיים שלכם מ-JW Library?",cele_demo_cta:"להשתמש בקבצים האמיתיים שלי",donate_prompt:"JW Sync היה מועיל לכם?",donate_cta:"תמכו בפיתוח",guide_title:"איך לשחזר אל JW Library",guide_tab_ios:"iPhone / iPad",guide_tab_android:"אנדרואיד",guide_tab_other:"אחר / מחשב",guide_warning:"השחזור מחליף את ההערות שנמצאות כעת ב-JW Library. שמרו את הגיבוי הממוזג הזה כעותק הראשי שלכם.",guide_done:"הבנתי",guide_export_title:"איך לייצא מ-JW Library",guide_mode_export:"ייצוא גיבויים",guide_mode_restore:"שחזור הקובץ הממוזג",cele_highlights:"צפייה בסטטיסטיקה שלכם",cele_addshared:"הוספת הערות שחבר שיתף",perf_title:"ביצועי המיזוג",perf_prepare:"הכנה",perf_merge:"מיזוג",perf_package:"אריזה",perf_tip_large:"ספרייה גדולה — למיזוג מהיר יותר, אחדו פחות קבצים בבת אחת או השתמשו בחילוץ לפי טווח תאריכים.",cele_top_medals:"המדליות המובילות שלכם",cele_awards_btn:"גלו את ההישגים שלכם →"},ar:{close:"إغلاق",cele_title:"اكتمل الدمج",cele_subtitle:"دمجت نسخك الاحتياطية في ملف واحد موحّد.",stat_notes:"ملاحظة",stat_highlights:"تظليل",stat_bookmarks:"علامة مرجعية",stat_tags:"وسم",cele_download:"نزّل النسخة الاحتياطية المدمجة",cele_redownload:"نزّل مرة أخرى",cele_downloading:"جارٍ تنزيل ملفك…",cele_browse:"تصفّح النتيجة المدمجة",cele_restore:"استعادة إلى JW Library",cele_demo_title:"كان ذلك عرضًا تجريبيًا ببيانات نموذجية",cele_demo_body:"هل أنت مستعد لتجربته بنسخك الاحتياطية الحقيقية من JW Library؟",cele_demo_cta:"استخدم ملفاتي الحقيقية",donate_prompt:"هل وجدت JW Sync مفيدًا؟",donate_cta:"ادعم التطوير",guide_title:"كيفية الاستعادة إلى JW Library",guide_tab_ios:"iPhone / iPad",guide_tab_android:"أندرويد",guide_tab_other:"أخرى / حاسوب",guide_warning:"الاستعادة تستبدل الملاحظات الموجودة حاليًا في JW Library. احتفظ بهذه النسخة المدمجة بوصفها نسختك الرئيسية.",guide_done:"فهمت",guide_export_title:"كيفية التصدير من JW Library",guide_mode_export:"تصدير النسخ الاحتياطية",guide_mode_restore:"استعادة الملف المدمج",cele_highlights:"اعرض إحصاءاتك",cele_addshared:"أضف ملاحظات شاركها صديق",perf_title:"أداء الدمج",perf_prepare:"التحضير",perf_merge:"الدمج",perf_package:"التغليف",perf_tip_large:"مكتبة كبيرة — لدمج أسرع، اجمع ملفات أقل في المرة الواحدة أو استخدم الاستخراج حسب نطاق التاريخ.",cele_top_medals:"أفضل أوسمتك",cele_awards_btn:"استكشف أوسمتك ←"}};
  var SHARE_I18N={
   en:{cele_share:'Share',share_headline:'Library merged!',share_preview_title:'Share your progress',share_preview_body:'Post this card to your story — and help a friend discover a free, private way to combine their JW Library notes.',share_save:'Save image',share_copy:'Copy caption',share_copied:'Caption copied — paste it with your post!',share_saved:'Image saved! Add it to your Instagram story or post.',share_hint:'On a phone, tap Share and pick Instagram. On a computer, save the image, then upload it to Instagram.',share_text:'I just merged my JW Library notes with JW Sync — a free, private tool that combines your notes, highlights and bookmarks from all your devices. https://jwsync.org'},
   es:{cele_share:'Compartir',share_headline:'¡Biblioteca combinada!',share_preview_title:'Comparte tu avance',share_preview_body:'Publica esta tarjeta en tu historia y ayuda a un amigo a descubrir una forma gratuita y privada de combinar sus notas de JW Library.',share_save:'Guardar imagen',share_copy:'Copiar texto',share_copied:'¡Texto copiado! Pégalo con tu publicación.',share_saved:'¡Imagen guardada! Añádela a tu historia o publicación de Instagram.',share_hint:'En el teléfono, toca Compartir y elige Instagram. En la computadora, guarda la imagen y súbela a Instagram.',share_text:'Acabo de combinar mis notas de JW Library con JW Sync, una herramienta gratuita y privada que une tus notas, subrayados y marcadores de todos tus dispositivos. https://jwsync.org'},
   pt:{cele_share:'Compartilhar',share_headline:'Biblioteca combinada!',share_preview_title:'Compartilhe seu progresso',share_preview_body:'Publique este cartão no seu story e ajude um amigo a descobrir um jeito gratuito e privado de combinar as notas do JW Library.',share_save:'Salvar imagem',share_copy:'Copiar legenda',share_copied:'Legenda copiada — cole com sua publicação!',share_saved:'Imagem salva! Adicione ao seu story ou post do Instagram.',share_hint:'No celular, toque em Compartilhar e escolha Instagram. No computador, salve a imagem e envie para o Instagram.',share_text:'Acabei de combinar minhas notas do JW Library com o JW Sync — uma ferramenta gratuita e privada que une suas notas, destaques e marcadores de todos os seus dispositivos. https://jwsync.org'},
   fr:{cele_share:'Partager',share_headline:'Bibliothèque fusionnée !',share_preview_title:'Partagez votre progression',share_preview_body:'Publiez cette carte dans votre story et aidez un ami à découvrir une façon gratuite et privée de combiner ses notes JW Library.',share_save:'Enregistrer l’image',share_copy:'Copier le texte',share_copied:'Texte copié — collez-le avec votre publication !',share_saved:'Image enregistrée ! Ajoutez-la à votre story ou publication Instagram.',share_hint:'Sur téléphone, touchez Partager et choisissez Instagram. Sur ordinateur, enregistrez l’image puis importez-la dans Instagram.',share_text:'Je viens de fusionner mes notes JW Library avec JW Sync — un outil gratuit et privé qui réunit vos notes, surlignages et signets de tous vos appareils. https://jwsync.org'},
   de:{cele_share:'Teilen',share_headline:'Bibliothek zusammengeführt!',share_preview_title:'Teile deinen Fortschritt',share_preview_body:'Poste diese Karte in deiner Story und hilf einem Freund, eine kostenlose, private Möglichkeit zu entdecken, seine JW Library-Notizen zusammenzuführen.',share_save:'Bild speichern',share_copy:'Text kopieren',share_copied:'Text kopiert — füge ihn zu deinem Beitrag hinzu!',share_saved:'Bild gespeichert! Füge es deiner Instagram-Story oder deinem Beitrag hinzu.',share_hint:'Tippe am Handy auf Teilen und wähle Instagram. Am Computer speichere das Bild und lade es bei Instagram hoch.',share_text:'Ich habe gerade meine JW Library-Notizen mit JW Sync zusammengeführt — ein kostenloses, privates Tool, das deine Notizen, Markierungen und Lesezeichen von allen Geräten vereint. https://jwsync.org'},
   it:{cele_share:'Condividi',share_headline:'Biblioteca unita!',share_preview_title:'Condividi i tuoi progressi',share_preview_body:'Pubblica questa card nella tua storia e aiuta un amico a scoprire un modo gratuito e privato di combinare le note di JW Library.',share_save:'Salva immagine',share_copy:'Copia testo',share_copied:'Testo copiato — incollalo con il tuo post!',share_saved:'Immagine salvata! Aggiungila alla tua storia o al tuo post di Instagram.',share_hint:'Su telefono, tocca Condividi e scegli Instagram. Su computer, salva l’immagine e caricala su Instagram.',share_text:'Ho appena unito le mie note di JW Library con JW Sync — uno strumento gratuito e privato che riunisce note, evidenziazioni e segnalibri da tutti i tuoi dispositivi. https://jwsync.org'},
   ru:{cele_share:'Поделиться',share_headline:'Библиотека объединена!',share_preview_title:'Поделитесь достижением',share_preview_body:'Опубликуйте эту карточку в истории и помогите другу узнать о бесплатном и приватном способе объединять заметки JW Library.',share_save:'Сохранить изображение',share_copy:'Копировать текст',share_copied:'Текст скопирован — вставьте его к публикации!',share_saved:'Изображение сохранено! Добавьте его в историю или пост Instagram.',share_hint:'На телефоне нажмите «Поделиться» и выберите Instagram. На компьютере сохраните изображение и загрузите его в Instagram.',share_text:'Я объединил свои заметки JW Library с помощью JW Sync — бесплатного и приватного инструмента, который собирает заметки, выделения и закладки со всех устройств. https://jwsync.org'},
   ja:{cele_share:'共有',share_headline:'ライブラリを統合しました！',share_preview_title:'成果をシェアしよう',share_preview_body:'このカードをストーリーに投稿して、JW Library のノートを無料でプライベートにまとめられることを友達に教えてあげましょう。',share_save:'画像を保存',share_copy:'キャプションをコピー',share_copied:'キャプションをコピーしました。投稿に貼り付けてください！',share_saved:'画像を保存しました！Instagram のストーリーや投稿に追加してください。',share_hint:'スマホでは「シェア」をタップして Instagram を選びます。パソコンでは画像を保存して Instagram にアップロードしてください。',share_text:'JW Syncで JW Library のノートを統合しました。すべての端末のノート・ハイライト・しおりを一つにまとめる無料＆プライベートなツールです。https://jwsync.org'},
   ko:{cele_share:'공유',share_headline:'라이브러리 병합 완료!',share_preview_title:'성과를 공유하세요',share_preview_body:'이 카드를 스토리에 올리고, 친구에게 JW Library 노트를 무료로 비공개로 합치는 방법을 알려 주세요.',share_save:'이미지 저장',share_copy:'캡션 복사',share_copied:'캡션이 복사되었습니다 — 게시물에 붙여넣으세요!',share_saved:'이미지가 저장되었습니다! 인스타그램 스토리나 게시물에 추가하세요.',share_hint:'휴대폰에서는 공유를 누르고 Instagram을 선택하세요. 컴퓨터에서는 이미지를 저장한 뒤 Instagram에 업로드하세요.',share_text:'JW Sync로 JW Library 노트를 병합했어요 — 모든 기기의 노트, 강조, 책갈피를 하나로 합쳐 주는 무료 비공개 도구입니다. https://jwsync.org'},
   tl:{cele_share:'Ibahagi',share_headline:'Pinagsama ang library!',share_preview_title:'Ibahagi ang iyong tagumpay',share_preview_body:'I-post ang card na ito sa iyong story at tulungan ang isang kaibigan na matuklasan ang libre at pribadong paraan para pagsamahin ang kanilang JW Library notes.',share_save:'I-save ang larawan',share_copy:'Kopyahin ang caption',share_copied:'Nakopya ang caption — i-paste ito sa iyong post!',share_saved:'Na-save ang larawan! Idagdag ito sa iyong Instagram story o post.',share_hint:'Sa telepono, i-tap ang Share at piliin ang Instagram. Sa computer, i-save ang larawan at i-upload ito sa Instagram.',share_text:'Kakapagsama ko lang ng aking JW Library notes gamit ang JW Sync — isang libre at pribadong tool na pinagsasama ang iyong mga tala, highlight at bookmark mula sa lahat ng device. https://jwsync.org'},
   sv:{cele_share:'Dela',share_headline:'Biblioteket sammanfogat!',share_preview_title:'Dela din framgång',share_preview_body:'Lägg upp det här kortet i din story och hjälp en vän att upptäcka ett gratis och privat sätt att slå ihop sina JW Library-anteckningar.',share_save:'Spara bild',share_copy:'Kopiera text',share_copied:'Texten kopierad — klistra in den med ditt inlägg!',share_saved:'Bilden sparad! Lägg till den i din Instagram-story eller ditt inlägg.',share_hint:'På mobilen trycker du på Dela och väljer Instagram. På datorn sparar du bilden och laddar upp den till Instagram.',share_text:'Jag sammanfogade just mina JW Library-anteckningar med JW Sync — ett gratis och privat verktyg som samlar dina anteckningar, markeringar och bokmärken från alla enheter. https://jwsync.org'},
   ceb:{cele_share:'Ipaambit',share_headline:'Nahiusa ang library!',share_preview_title:'Ipaambit ang imong kalampusan',share_preview_body:'I-post kini nga card sa imong story ug tabangi ang usa ka higala nga makakita sa libre ug pribado nga paagi sa paghiusa sa ilang JW Library notes.',share_save:'I-save ang hulagway',share_copy:'Kopyaha ang caption',share_copied:'Nakopya ang caption — i-paste kini sa imong post!',share_saved:'Na-save ang hulagway! Idugang kini sa imong Instagram story o post.',share_hint:'Sa telepono, i-tap ang Share ug pilia ang Instagram. Sa kompyuter, i-save ang hulagway ug i-upload kini sa Instagram.',share_text:'Bag-o lang nako gihiusa ang akong JW Library notes gamit ang JW Sync — usa ka libre ug pribado nga tool nga naghiusa sa imong mga nota, highlight ug bookmark gikan sa tanan nimong device. https://jwsync.org'},uk:{cele_share:"Поділитися",share_headline:"Бібліотеку об'єднано!",share_preview_title:"Поділіться своїм поступом",share_preview_body:"Опублікуйте цю картку в історії — і допоможіть другові дізнатися про безкоштовний і приватний спосіб поєднати свої нотатки з JW Library.",share_save:"Зберегти зображення",share_copy:"Копіювати підпис",share_copied:"Підпис скопійовано — вставте його у свою публікацію!",share_saved:"Зображення збережено! Додайте його в історію або допис в Instagram.",share_hint:"На телефоні натисніть «Поділитися» і виберіть Instagram. На комп'ютері збережіть зображення, а тоді завантажте його в Instagram.",share_text:"Я щойно об'єднав свої нотатки з JW Library за допомогою JW Sync — безкоштовного і приватного інструмента, який поєднує нотатки, виділення та закладки з усіх ваших пристроїв. https://jwsync.org"},he:{cele_share:"שיתוף",share_headline:"הספרייה מוזגה!",share_preview_title:"שתפו את ההתקדמות שלכם",share_preview_body:"פרסמו את הכרטיס הזה בסטורי — ועזרו לחבר לגלות דרך חינמית ופרטית לאחד את ההערות שלו מ-JW Library.",share_save:"שמירת התמונה",share_copy:"העתקת הכיתוב",share_copied:"הכיתוב הועתק — הדביקו אותו בפרסום!",share_saved:"התמונה נשמרה! הוסיפו אותה לסטורי או לפוסט באינסטגרם.",share_hint:"בטלפון, הקישו על שיתוף ובחרו באינסטגרם. במחשב, שמרו את התמונה ואז העלו אותה לאינסטגרם.",share_text:"בדיוק מיזגתי את ההערות שלי מ-JW Library עם JW Sync — כלי חינמי ופרטי שמאחד הערות, הדגשות וסימניות מכל המכשירים שלכם. https://jwsync.org"},ar:{cele_share:"مشاركة",share_headline:"تم دمج المكتبة!",share_preview_title:"شارِك تقدّمك",share_preview_body:"انشر هذه البطاقة في قصتك — وساعد صديقًا على اكتشاف طريقة مجانية وخاصة لدمج ملاحظات JW Library.",share_save:"حفظ الصورة",share_copy:"نسخ التعليق",share_copied:"تم نسخ التعليق — الصقه مع منشورك!",share_saved:"تم حفظ الصورة! أضفها إلى قصتك أو منشورك على إنستغرام.",share_hint:"على الهاتف، اضغط مشاركة واختر إنستغرام. على الحاسوب، احفظ الصورة ثم ارفعها إلى إنستغرام.",share_text:"دمجت للتو ملاحظات JW Library باستخدام JW Sync — أداة مجانية وخاصة تجمع ملاحظاتك وتظليلاتك وعلاماتك المرجعية من كل أجهزتك. https://jwsync.org"}
  };
  function ts(k){var l;try{l=lang();}catch(_){l='en';}return (SHARE_I18N[l]&&SHARE_I18N[l][k])||SHARE_I18N.en[k]||k;}
  var SAFE_I18N={
   en:{safe_title:'Restore safely',safe_originals:'Your original backups are safe — JW Sync never changes them. This is a brand-new combined file.',safe_master:'Keep this combined file as your master backup.'},
   es:{safe_title:'Restaura con seguridad',safe_originals:'Tus copias originales están a salvo: JW Sync nunca las modifica. Este es un archivo combinado totalmente nuevo.',safe_master:'Guarda este archivo combinado como tu copia maestra.'},
   pt:{safe_title:'Restaure com segurança',safe_originals:'Seus backups originais estão seguros — o JW Sync nunca os altera. Este é um arquivo combinado totalmente novo.',safe_master:'Guarde este arquivo combinado como sua cópia mestra.'},
   fr:{safe_title:'Restaurer en toute sécurité',safe_originals:'Vos sauvegardes d’origine sont intactes — JW Sync ne les modifie jamais. Ceci est un nouveau fichier combiné.',safe_master:'Conservez ce fichier combiné comme copie maîtresse.'},
   de:{safe_title:'Sicher wiederherstellen',safe_originals:'Deine ursprünglichen Sicherungen sind sicher — JW Sync ändert sie nie. Dies ist eine brandneue kombinierte Datei.',safe_master:'Bewahre diese kombinierte Datei als deine Hauptsicherung auf.'},
   it:{safe_title:'Ripristina in sicurezza',safe_originals:'I tuoi backup originali sono al sicuro: JW Sync non li modifica mai. Questo è un nuovo file combinato.',safe_master:'Conserva questo file combinato come copia principale.'},
   ru:{safe_title:'Безопасное восстановление',safe_originals:'Ваши исходные копии в безопасности — JW Sync их не меняет. Это совершенно новый объединённый файл.',safe_master:'Сохраните этот объединённый файл как основную копию.'},
   ja:{safe_title:'安全に復元',safe_originals:'元のバックアップは安全です。JW Syncが変更することはありません。これは新しく統合されたファイルです。',safe_master:'この統合ファイルをマスターバックアップとして保管してください。'},
   ko:{safe_title:'안전하게 복원',safe_originals:'원본 백업은 안전합니다 — JW Sync는 절대 변경하지 않습니다. 이것은 완전히 새로운 통합 파일입니다.',safe_master:'이 통합 파일을 마스터 백업으로 보관하세요.'},
   tl:{safe_title:'Mag-restore nang ligtas',safe_originals:'Ligtas ang iyong orihinal na mga backup — hindi ito kailanman binabago ng JW Sync. Ito ay isang bagong pinagsamang file.',safe_master:'Itago ang pinagsamang file na ito bilang iyong master backup.'},
   sv:{safe_title:'Återställ tryggt',safe_originals:'Dina ursprungliga säkerhetskopior är trygga — JW Sync ändrar dem aldrig. Detta är en helt ny sammanslagen fil.',safe_master:'Spara den här sammanslagna filen som din huvudkopia.'},
   ceb:{safe_title:'Pag-restore nga luwas',safe_originals:'Luwas ang imong orihinal nga mga backup — dili kini usbon sa JW Sync. Kini usa ka bag-ong gihiusa nga file.',safe_master:'Tipigi kini nga gihiusa nga file isip imong master backup.'},uk:{safe_title:"Безпечне відновлення",safe_originals:"Ваші початкові резервні копії в безпеці — JW Sync ніколи їх не змінює. Це цілком новий об'єднаний файл.",safe_master:"Зберігайте цей об'єднаний файл як свою основну резервну копію."},he:{safe_title:"שחזור בבטחה",safe_originals:"הגיבויים המקוריים שלכם בטוחים — JW Sync לעולם לא משנה אותם. זהו קובץ מאוחד חדש לגמרי.",safe_master:"שמרו את הקובץ המאוחד הזה כגיבוי הראשי שלכם."},ar:{safe_title:"استعادة آمنة",safe_originals:"نسخك الاحتياطية الأصلية في أمان — JW Sync لا يغيّرها أبدًا. هذا ملف مدمج جديد تمامًا.",safe_master:"احتفظ بهذا الملف المدمج بوصفه نسختك الاحتياطية الرئيسية."}
  };
  function sg(k){var l;try{l=lang();}catch(_){l='en';}return (SAFE_I18N[l]&&SAFE_I18N[l][k])||SAFE_I18N.en[k]||k;}
  function safeRow(color,bg,icon,text){return '<div style="display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:10px;background:'+bg+'">'+'<span style="flex:0 0 auto;color:'+color+';line-height:0;margin-top:2px">'+icon+'</span>'+'<span style="flex:1 1 auto;font:500 13px/1.5 inherit;color:#cbd5e1">'+esc(text)+'</span></div>';}
  function buildSafePanel(){var ck='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>';
    var wn='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
    var st='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>';
    var sh='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>';
    return '<div style="width:100%;box-sizing:border-box;text-align:left;margin:16px 0 2px;padding:16px;border-radius:14px;background:rgba(4,15,34,.6);border:1px solid rgba(71,85,105,.4)">'+'<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;color:#34d399;font:700 13px/1.2 inherit">'+sh+'<span>'+esc(sg('safe_title'))+'</span></div>'+'<div style="display:flex;flex-direction:column;gap:8px">'+safeRow('#34d399','rgba(16,185,129,.08)',ck,sg('safe_originals'))+safeRow('#fbbf24','rgba(245,158,11,.09)',wn,t('guide_warning'))+safeRow('#fb923c','rgba(234,88,12,.09)',st,sg('safe_master'))+'</div></div>';}
  function lang() { try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; } }
  function t(k) { var l = lang(); return (I18N[l] && I18N[l][k]) || I18N.en[k] || k; }
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

  var GUIDE = {
    ios: [
      'Your merged backup file is downloaded — usually to your Downloads folder or wherever your browser saves files.',
      'If you’re on a desktop, transfer the file to your iPhone or iPad (AirDrop, iCloud Drive, email, or any cloud service works).',
      'On your iPhone or iPad, open the Files app and locate the .jwlibrary file.',
      'Tap the file. iOS may ask which app to open it with — choose <strong>JW Library</strong>.',
      'JW Library will prompt you to confirm restoring the backup. Confirm.',
      'Done — your merged notes are now in JW Library.'
    ],
    android: [
      'Your merged backup file is downloaded — usually to your Downloads folder.',
      'If you’re on a desktop, transfer the .jwlibrary file to your Android device (Google Drive, email, USB, or any cloud service).',
      'On your Android device, open your file manager and find the file.',
      'Tap the file. Android may ask which app should open it — choose <strong>JW Library</strong>.',
      'JW Library will ask to confirm the restore. Confirm.',
      'Done — your merged notes are now in JW Library.'
    ],
    other: [
      'Your merged backup file is on your computer.',
      'To use it, transfer it to a device running JW Library — an iPhone, iPad, or Android phone/tablet.',
      'Use cloud storage (iCloud, Google Drive, Dropbox), AirDrop, or USB to move the file across.',
      'On your phone or tablet, tap the file and choose <strong>JW Library</strong> to open it.',
      'Confirm the restore in JW Library.',
      'Done — your merged notes are now in JW Library.'
    ]
  };

  var EXPORT_GUIDE = {
    ios: [
      'Open JW Library on your iPhone or iPad.',
      'Tap the menu (☰), then open <strong>Settings</strong> → <strong>Backup &amp; Restore</strong>.',
      'Tap <strong>Create Backup</strong> — JW Library saves a .jwlibrary file and offers to share it.',
      'Share the file somewhere this computer can reach it — AirDrop, iCloud Drive, Google Drive, or email it to yourself.',
      'Repeat on every device whose notes you want to combine, so each one’s .jwlibrary file is gathered in one place.',
      'Back here, add your main backup as the first file and the others as additional files, then merge.'
    ],
    android: [
      'Open JW Library on your Android phone or tablet.',
      'Tap the menu (☰), then open <strong>Settings</strong> → <strong>Backup &amp; Restore</strong>.',
      'Tap <strong>Create Backup</strong> and choose where to save the .jwlibrary file.',
      'Move the file to this computer — Google Drive, email, USB, or any cloud service works.',
      'Repeat on every device you want to combine, gathering each .jwlibrary file in one place.',
      'Back here, add your main backup as the first file and the others as additional files, then merge.'
    ],
    other: [
      'Backups are created inside the JW Library app on a phone or tablet — not on desktop.',
      'On each device: open JW Library → menu (☰) → <strong>Settings</strong> → <strong>Backup &amp; Restore</strong> → <strong>Create Backup</strong>.',
      'Send each .jwlibrary file to this computer using cloud storage, AirDrop, email, or USB.',
      'Gather every device’s backup file in one place — for example your Downloads folder.',
      'Back here, add your main backup as the first file and the others as additional files, then merge.'
    ]
  };

  // ── State ──────────────────────────────────────────────────────────
  var lastSeenBlob = '';
  var autoDownloadedFor = null;
  var cached = null;

  function detectPlatform() {
    var ua = (navigator.userAgent || '');
    if (/iPad|iPhone|iPod/i.test(ua)) return 'ios';
    if (/Android/i.test(ua)) return 'android';
    return 'other';
  }
  function isDemoMerge() {
    var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
    for (var i = 0; i < inputs.length; i++) {
      var fl = inputs[i].files;
      if (fl && fl.length) {
        for (var j = 0; j < fl.length; j++) {
          if (fl[j].name.indexOf('JWSync_Demo_') === 0) return true;
        }
      }
    }
    return false;
  }
  function fireAnalytics(ev) {
    try { if (typeof gtag === 'function') gtag('event', ev, { event_category: 'engagement' }); } catch (_) {}
  }
  function readDownloadName() {
    var a = document.querySelector('a#download-btn[download]');
    return (a && a.getAttribute('download')) || 'merged.jwlibrary';
  }

  // ── Trigger the download (click the existing React-rendered anchor) ──
  function triggerDownload(opts) {
    var dl = document.getElementById('download-btn');
    if (!dl) return false;
    var href = dl.getAttribute('href') || '';
    if (href.indexOf('blob:') !== 0) return false;
    try {
      dl.click();
      fireAnalytics(opts && opts.auto ? 'merge_auto_download' : 'merge_manual_download');
      return true;
    } catch (e) {
      console.warn('[jwsync] download click blocked:', e);
      return false;
    }
  }

  window.__jwUpdateMergedCache = function (buf) {
    try {
      cached = cached || {};
      cached.buffer = buf;
      if (cached.blobUrl) { try { URL.revokeObjectURL(cached.blobUrl); } catch (_) {} }
      cached.blobUrl = URL.createObjectURL(new Blob([buf], { type: 'application/octet-stream' }));
    } catch (_) {}
  };

  function fetchStats(blobUrl) {
    if (typeof window.JSZip !== 'function' || typeof window.initSqlJs !== 'function') {
      return Promise.resolve(null);
    }
    return fetch(blobUrl)
      .then(function (r) { return r.arrayBuffer(); })
      .then(function (buf) {
        cached = cached || {};
        cached.buffer = buf;
        return window.JSZip.loadAsync(buf);
      })
      .then(function (zip) {
        var name = Object.keys(zip.files).find(function (f) { return /userdata\.db$/i.test(f); });
        if (!name) throw new Error('userData.db not in zip');
        return zip.file(name).async('uint8array');
      })
      .then(function (dbBytes) {
        return window.initSqlJs({
          locateFile: function (f) { return 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/' + f; }
        }).then(function (SQL) {
          var db = new SQL.Database(dbBytes);
          function count(sql) {
            try {
              var r = db.exec(sql);
              return (r[0] && r[0].values && r[0].values[0]) ? r[0].values[0][0] : 0;
            } catch (_) { return 0; }
          }
          var s = {
            notes: count('SELECT COUNT(*) FROM Note'),
            highlights: count('SELECT COUNT(*) FROM UserMark'),
            bookmarks: count('SELECT COUNT(*) FROM Bookmark'),
            tags: count('SELECT COUNT(*) FROM Tag')
          };
          db.close();
          return s;
        });
      })
      .catch(function (e) { console.warn('[jwsync] stats query failed:', e); return null; });
  }

  // ── Render the celebration overlay ─────────────────────────────────
  // ── Awards teaser ──
  function ensureAwardsCss() {
    if (document.getElementById('jwc-awards-css')) return;
    var s = document.createElement('style'); s.id = 'jwc-awards-css';
    s.textContent = '@keyframes jwca{0%{background-position:-200% center}100%{background-position:200% center}}'
      + '.jwc-awards-link{background:linear-gradient(90deg,#f59e0b,#c084fc,#ec4899,#fbbf24,#c084fc,#f59e0b)!important;background-size:300% auto!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;background-clip:text!important;animation:jwca 3s linear infinite!important}';
    document.head.appendChild(s);
  }
  function celebTopMedals(stats) {
    var n=+(stats&&stats.notes)||0, h=+(stats&&stats.highlights)||0, b=+(stats&&stats.bookmarks)||0, tg=+(stats&&stats.tags)||0;
    var all=[
      [n,5000,'✍️',4,'5k '+t('stat_notes')],[n,2500,'✍️',3,'2,500 '+t('stat_notes')],
      [n,1000,'✍️',3,'1k '+t('stat_notes')],[n,500,'✍️',2,'500 '+t('stat_notes')],
      [n,250,'✍️',2,'250 '+t('stat_notes')],[n,100,'✍️',1,'100 '+t('stat_notes')],
      [n,10,'✍️',0,'10 '+t('stat_notes')],[n,1,'✍️',0,t('stat_notes')],
      [h,1000,'✨',3,'1k '+t('stat_highlights')],[h,500,'✨',2,'500 '+t('stat_highlights')],
      [h,100,'✨',1,'100 '+t('stat_highlights')],[h,1,'✨',0,t('stat_highlights')],
      [b,500,'🔖',2,'500 '+t('stat_bookmarks')],[b,100,'🔖',1,'100 '+t('stat_bookmarks')],
      [b,1,'🔖',0,t('stat_bookmarks')],
      [tg,50,'🏷',2,'50 '+t('stat_tags')],[tg,10,'🏷',1,'10 '+t('stat_tags')],[tg,1,'🏷',0,t('stat_tags')],
    ];
    var earned=all.filter(function(a){return a[0]>=a[1];});
    earned.sort(function(a,b){return(b[3]-a[3])||(b[1]-a[1]);});
    return earned.slice(0,3);
  }
  function showAwardsTeaser(ov, stats) {
    var box=ov&&ov.querySelector('[data-jwc-awards]');
    if(!box||box._shown) return;
    var medals=celebTopMedals(stats||{});
    if(!medals.length) return;
    ensureAwardsCss();
    var rarBg=['rgba(148,163,184,.12)','rgba(96,165,250,.15)','rgba(251,191,36,.15)','rgba(192,132,252,.2)','rgba(234,88,12,.15)'];
    var rarBd=['#94a3b8','#60a5fa','#fbbf24','#c084fc','#ea580c'];
    var chips=medals.map(function(m){
      var r=Math.min(4,m[3]);
      return '<div style="display:flex;flex-direction:column;align-items:center;gap:5px">'
        +'<div style="width:46px;height:46px;border-radius:50%;background:'+rarBg[r]+';border:2px solid '+rarBd[r]+';display:flex;align-items:center;justify-content:center;font-size:20px">'+m[2]+'</div>'
        +'<div style="font-size:10px;color:'+rarBd[r]+';font-weight:700;white-space:nowrap;max-width:68px;overflow:hidden;text-overflow:ellipsis">'+esc(m[4])+'</div>'
        +'</div>';
    }).join('');
    box.innerHTML='<div style="font-size:11px;font-weight:700;color:#64748b;letter-spacing:.07em;text-transform:uppercase;margin-bottom:11px">'+esc(t('cele_top_medals'))+'</div>'
      +'<div style="display:flex;justify-content:center;gap:14px;margin-bottom:14px">'+chips+'</div>'
      +'<a href="highlights.html" class="jwc-awards-link" style="display:inline-flex;align-items:center;gap:6px;padding:9px 22px;border-radius:8px;font-size:13.5px;font-weight:700;text-decoration:none;border:1px solid rgba(245,158,11,.3);background:rgba(0,0,0,0)">'+esc(t('cele_awards_btn'))+'</a>';
    box.hidden=false; box._shown=true;
  }
  function buildPerfHtml() {
    var T = null; try { T = window.__jwLastMergeTimings; } catch (_) {}
    if (!T || !T.total) return '';
    function ms(v) { v = Math.max(0, +v || 0); return v >= 1000 ? (Math.round(v / 100) / 10) + 's' : Math.round(v) + 'ms'; }
    var total = T.total || 1;
    var segs = [['prepare', t('perf_prepare'), '#60a5fa'], ['merge', t('perf_merge'), '#ea580c'], ['package', t('perf_package'), '#34d399']];
    var bar = '', legend = '';
    segs.forEach(function (s) {
      var v = +T[s[0]] || 0, pct = Math.max(0, Math.min(100, v / total * 100));
      if (pct > 0.4) bar += '<span style="width:' + pct.toFixed(1) + '%;background:' + s[2] + '"></span>';
      legend += '<span style="display:inline-flex;align-items:center;gap:5px;margin-right:12px;font-size:11.5px;color:#94a3b8"><i style="width:9px;height:9px;border-radius:2px;background:' + s[2] + ';display:inline-block"></i>' + esc(s[1]) + ' ' + ms(v) + '</span>';
    });
    var tip = ((T.rows || 0) > 10000 || total > 60000) ? '<div style="margin-top:8px;font-size:12px;color:#fbbf24">' + esc(t('perf_tip_large')) + '</div>' : '';
    return '<details class="jwc-perf" style="margin:4px 0 10px;text-align:left;border:1px solid rgba(71,85,105,.3);border-radius:10px;padding:10px 12px;background:rgba(255,255,255,.02)">' +
      '<summary style="cursor:pointer;font-size:12.5px;font-weight:700;color:#cbd5e1">' + esc(t('perf_title')) + ' · ' + ms(total) + '</summary>' +
      '<div style="display:flex;height:10px;border-radius:6px;overflow:hidden;background:rgba(148,163,184,.12);margin:10px 0 8px">' + bar + '</div>' +
      '<div>' + legend + '</div>' + tip + '</details>';
  }

  function shWrap(ctx,text,cx,y,maxW,lh){var words=String(text||'').split(' '),line='',yy=y;for(var n=0;n<words.length;n++){var tt=line+words[n]+' ';if(ctx.measureText(tt).width>maxW&&n>0){ctx.fillText(line.replace(/ $/,''),cx,yy);line=words[n]+' ';yy+=lh;}else{line=tt;}}ctx.fillText(line.replace(/ $/,''),cx,yy);}
  function buildMergeCard(stats){try{var s=stats||{},W=1080,H=1080,cv=document.createElement('canvas');cv.width=W;cv.height=H;var ctx;try{ctx=cv.getContext('2d');}catch(_){return null;}if(!ctx)return null;var loc;try{loc=lang();}catch(_){loc='en';}
    ctx.fillStyle='#0b1426';ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(234,88,12,.5)';ctx.lineWidth=8;ctx.strokeRect(30,30,W-60,H-60);
    ctx.textAlign='center';
    ctx.fillStyle='#fb923c';ctx.font='700 40px Inter,Arial,sans-serif';ctx.fillText('J W   S Y N C',W/2,132);
    ctx.beginPath();ctx.arc(W/2,300,84,0,Math.PI*2);ctx.fillStyle='#ea580c';ctx.fill();
    ctx.strokeStyle='#fff';ctx.lineWidth=14;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();ctx.moveTo(W/2-38,300);ctx.lineTo(W/2-8,334);ctx.lineTo(W/2+46,262);ctx.stroke();
    ctx.fillStyle='#f8fafc';ctx.font='800 62px Inter,Arial,sans-serif';ctx.fillText(ts('share_headline'),W/2,468);
    ctx.fillStyle='#94a3b8';ctx.font='400 30px Inter,Arial,sans-serif';shWrap(ctx,t('cele_subtitle'),W/2,528,W-240,40);
    var items=[[s.notes,'stat_notes'],[s.highlights,'stat_highlights'],[s.bookmarks,'stat_bookmarks'],[s.tags,'stat_tags']],gx=[W/2-210,W/2+210],gy=[722,902];
    for(var i=0;i<4;i++){var x=gx[i%2],y=gy[i>1?1:0],v=items[i][0];if(v==null||v==='\u2013')v=0;v=Number(v)||0;
      ctx.fillStyle='#fb923c';ctx.font='800 74px Inter,Arial,sans-serif';ctx.fillText(v.toLocaleString(loc),x,y);
      ctx.fillStyle='#cbd5e1';ctx.font='600 26px Inter,Arial,sans-serif';ctx.fillText(String(t(items[i][1])).toUpperCase(),x,y+46);}
    ctx.fillStyle='#64748b';ctx.font='600 30px Inter,Arial,sans-serif';ctx.fillText('jwsync.org',W/2,H-74);
    return cv;}catch(_){return null;}}
  function shareMerge(stats){var url='https://jwsync.org',text=ts('share_text');
    function dl(b){try{var u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='jwsync.png';document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u);},3000);}catch(_){}try{if(navigator.clipboard)navigator.clipboard.writeText(url);}catch(_){}}
    function linkShare(){try{if(navigator.share){navigator.share({title:'JW Sync',text:text,url:url}).catch(function(){});return true;}}catch(_){}return false;}
    var cv=buildMergeCard(stats);
    try{if(cv&&cv.toBlob){cv.toBlob(function(b){if(b){try{if(navigator.canShare&&typeof File==='function'){var fl=new File([b],'jwsync.png',{type:'image/png'});if(navigator.canShare({files:[fl]})){navigator.share({files:[fl],text:text}).catch(function(){dl(b);});return;}}}catch(_){}if(!linkShare())dl(b);}else{linkShare();}},'image/png');}else{linkShare();}}catch(_){linkShare();}}
  // ── Share-preview overlay: shows the branded card + easy Instagram/social share ──
  var JW_IG_SVG = '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.5" y2="6.5"/></svg>';
  function jwsToast(ov, msg) { var el = ov && ov.querySelector('[data-jws-toast]'); if (!el) return; el.textContent = msg; el.hidden = false; }
  function saveCardImage(cv) {
    try {
      if (cv && cv.toBlob) {
        cv.toBlob(function (b) {
          if (!b) return;
          try {
            var u = URL.createObjectURL(b), a = document.createElement('a');
            a.href = u; a.download = 'jwsync-merge.png';
            document.body.appendChild(a); a.click(); a.remove();
            setTimeout(function () { URL.revokeObjectURL(u); }, 3000);
          } catch (_) {}
        }, 'image/png');
      }
    } catch (_) {}
  }
  function shareEsc(e) { if (e.key === 'Escape') { e.stopImmediatePropagation(); closeSharePreview(); } }
  function closeSharePreview() {
    var ov = document.getElementById('jw-share-overlay');
    if (ov) ov.remove();
    document.removeEventListener('keydown', shareEsc, true);
  }
  function openSharePreview(stats) {
    fireAnalytics('post_merge_share_open');
    closeSharePreview();
    var cv = buildMergeCard(stats);
    var dataUrl = '';
    try { dataUrl = cv && cv.toDataURL ? cv.toDataURL('image/png') : ''; } catch (_) { dataUrl = ''; }
    var preview = dataUrl
      ? '<img src="' + dataUrl + '" alt="' + esc(ts('share_headline')) + '" style="display:block;width:100%;max-width:300px;margin:4px auto 2px;border-radius:16px;border:1px solid rgba(234,88,12,.35);box-shadow:0 14px 44px rgba(0,0,0,.5)">'
      : '';
    var saveIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';
    var copyIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';
    var html =
      '<div data-jws-close style="position:absolute;inset:0;background:rgba(4,15,34,.86)"></div>' +
      '<div class="jwc-card" role="dialog" aria-modal="true" aria-labelledby="jws-title" style="max-width:400px">' +
        '<button class="jwc-close" type="button" data-jws-close aria-label="' + esc(t('close')) + '">&times;</button>' +
        '<div class="jwc-icon" aria-hidden="true" style="background:linear-gradient(135deg,#ea580c,#f97316);box-shadow:0 8px 24px rgba(234,88,12,.45)">' +
          JW_IG_SVG.replace('width="17" height="17"', 'width="26" height="26"') +
        '</div>' +
        '<h2 id="jws-title" class="jwc-title">' + esc(ts('share_preview_title')) + '</h2>' +
        '<p class="jwc-subtitle">' + esc(ts('share_preview_body')) + '</p>' +
        preview +
        '<div class="jwc-actions" style="margin-top:16px">' +
          '<button class="jwc-btn jwc-btn-primary" type="button" data-jws-share>' + JW_IG_SVG + '<span>' + esc(ts('cele_share')) + '</span></button>' +
          '<button class="jwc-btn jwc-btn-outline" type="button" data-jws-save>' + saveIcon + '<span>' + esc(ts('share_save')) + '</span></button>' +
          '<button class="jwc-btn jwc-btn-secondary" type="button" data-jws-copy>' + copyIcon + '<span>' + esc(ts('share_copy')) + '</span></button>' +
        '</div>' +
        '<div data-jws-toast hidden style="margin:14px 0 2px;padding:10px 12px;border-radius:10px;background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.32);color:#86efac;font-size:12.5px;font-weight:600;text-align:center"></div>' +
        '<p style="margin:12px 0 0;font-size:11.5px;color:rgba(148,163,184,.8);line-height:1.55;text-align:center">' + esc(ts('share_hint')) + '</p>' +
      '</div>';
    var ov = document.createElement('div');
    ov.id = 'jw-share-overlay';
    ov.style.cssText = 'position:fixed;inset:0;z-index:9500;display:flex;align-items:center;justify-content:center;padding:16px;font-family:inherit';
    ov.innerHTML = html;
    document.body.appendChild(ov);
    ov.querySelectorAll('[data-jws-close]').forEach(function (el) { el.addEventListener('click', closeSharePreview); });
    var sBtn = ov.querySelector('[data-jws-share]');
    if (sBtn) sBtn.addEventListener('click', function () { fireAnalytics('post_merge_share_do'); shareMerge(stats); });
    var vBtn = ov.querySelector('[data-jws-save]');
    if (vBtn) vBtn.addEventListener('click', function () { fireAnalytics('post_merge_share_save'); saveCardImage(buildMergeCard(stats)); jwsToast(ov, ts('share_saved')); });
    var cBtn = ov.querySelector('[data-jws-copy]');
    if (cBtn) cBtn.addEventListener('click', function () {
      fireAnalytics('post_merge_share_copy');
      var txt = ts('share_text');
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(txt).then(function () { jwsToast(ov, ts('share_copied')); }).catch(function () { jwsToast(ov, ts('share_copied')); });
        } else { jwsToast(ov, ts('share_copied')); }
      } catch (_) { jwsToast(ov, ts('share_copied')); }
    });
    document.addEventListener('keydown', shareEsc, true);
  }

  function renderCelebration(opts) {
    closeCelebration(true);
    var stats = opts.stats || { notes: '–', highlights: '–', bookmarks: '–', tags: '–' };
    var demo = !!opts.demoMode;
    var didAutoDl = !!opts.autoDownloaded;

    var downloadIcon =
      '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>' +
      '</svg>';

    var html =
      '<div class="jwc-backdrop" data-jwc-close></div>' +
      '<div class="jwc-particles" aria-hidden="true"></div>' +
      '<div class="jwc-card" role="dialog" aria-modal="true" aria-labelledby="jwc-title">' +
        '<button class="jwc-close" type="button" data-jwc-close aria-label="' + esc(t('close')) + '">×</button>' +
        '<div class="jwc-icon" aria-hidden="true">' +
          '<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' +
        '</div>' +
        '<h2 id="jwc-title" class="jwc-title">' + esc(t('cele_title')) + '</h2>' +
        '<p class="jwc-subtitle">' + esc(t('cele_subtitle')) + '</p>' +
        '<div class="jwc-stats">' +
          '<div class="jwc-stat" data-jwc-stat-type="notes" data-jwc-stat-val="' + (stats.notes || '0') + '"><div class="jwc-stat-ring"></div><strong>0</strong><svg class="jwc-stat-check" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>' + esc(t('stat_notes')) + '</span></div>' +
          '<div class="jwc-stat" data-jwc-stat-type="highlights" data-jwc-stat-val="' + (stats.highlights || '0') + '"><div class="jwc-stat-ring"></div><strong>0</strong><svg class="jwc-stat-check" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>' + esc(t('stat_highlights')) + '</span></div>' +
          '<div class="jwc-stat" data-jwc-stat-type="bookmarks" data-jwc-stat-val="' + (stats.bookmarks || '0') + '"><div class="jwc-stat-ring"></div><strong>0</strong><svg class="jwc-stat-check" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>' + esc(t('stat_bookmarks')) + '</span></div>' +
          '<div class="jwc-stat" data-jwc-stat-type="tags" data-jwc-stat-val="' + (stats.tags || '0') + '"><div class="jwc-stat-ring"></div><strong>0</strong><svg class="jwc-stat-check" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#34d399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg><span>' + esc(t('stat_tags')) + '</span></div>' +
        '</div>' +
        buildSafePanel() +
        buildPerfHtml() +
        // Download status banner — informs the user the download started
        '<div class="jwc-download-status" data-jwc-dl-status hidden>' +
          '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>' +
          '<span>' + esc(t('cele_downloading')) + '</span>' +
        '</div>' +
        '<div data-jwc-awards style="margin:16px 0 2px;padding:16px;background:rgba(245,158,11,.06);border:1px solid rgba(245,158,11,.18);border-radius:14px;text-align:center" hidden></div>' +
        '<div class="jwc-donate">' +
          '<a href="' + DONATE_URL + '" target="_blank" rel="noopener noreferrer" data-jwc-donate>' +
            '<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true">' +
              '<path d="M12 21s-7-4.35-7-10.5a4.5 4.5 0 0 1 7-3.72A4.5 4.5 0 0 1 19 10.5C19 16.65 12 21 12 21z"/>' +
            '</svg>' +
            '<span><strong>' + esc(t('donate_prompt')) + '</strong> ' + esc(t('donate_cta')) + ' →</span>' +
          '</a>' +
        '</div>' +
        '<div class="jwc-actions">' +
          '<button class="jwc-btn jwc-btn-primary" type="button" data-jwc-download>' +
            downloadIcon + '<span data-jwc-dl-label>' + esc(t('cele_download')) + '</span>' +
          '</button>' +
          '<button class="jwc-btn jwc-btn-outline" type="button" data-jwc-share><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg> ' + esc(ts('cele_share')) + '</button>' +
          '<button class="jwc-btn jwc-btn-outline" type="button" data-jwc-restore>' + esc(t('cele_restore')) + ' →</button>' +
          '<button class="jwc-btn jwc-btn-secondary" type="button" data-jwc-browse>' + esc(t('cele_browse')) + '</button>' +
          '<button class="jwc-btn jwc-btn-highlights" type="button" data-jwc-highlights>' + esc(t('cele_highlights')) + ' →</button>' +
          '<button class="jwc-btn jwc-btn-outline" type="button" data-jwc-addshared>' + esc(t('cele_addshared')) + '</button>' +
        '</div>' +
        '<div data-jwc-resurface></div>' +
        (demo ?
          '<div class="jwc-demo-cta">' +
            '<strong>' + esc(t('cele_demo_title')) + '</strong>' +
            '<span>' + esc(t('cele_demo_body')) + '</span>' +
            '<button class="jwc-demo-btn" type="button" data-jwc-real>' + esc(t('cele_demo_cta')) + ' →</button>' +
          '</div>' : '') +
      '</div>';

    var ov = document.createElement('div');
    ov.id = 'jw-celebrate-overlay';
    ov.innerHTML = html;
    document.body.appendChild(ov);
    document.body.classList.add('jw-modal-open');
    try { if (window.__jwReceiveOnCelebration) window.__jwReceiveOnCelebration(ov); } catch (_) {}
    try {
      var __rsEl = ov.querySelector('[data-jwc-resurface]');
      if (__rsEl && window.JwResurface && cached && cached.buffer) {
        window.JwResurface.notesFromBuffer(cached.buffer.slice(0)).then(function (notes) {
          if (notes && notes.length) window.JwResurface.mount(__rsEl, { notes: notes });
        }).catch(function () {});
      }
    } catch (_) {}

    // Generate floating particles
    var particlesContainer = ov.querySelector('.jwc-particles');
    if (particlesContainer) {
      for (var i = 0; i < 12; i++) {
        var p = document.createElement('div');
        p.className = 'jwc-particle';
        var delay = Math.random() * 300;
        var duration = 2500 + Math.random() * 1500;
        var tx = (Math.random() - 0.5) * 300;
        var ty = -300 - Math.random() * 100;
        p.style.left = Math.random() * 100 + '%';
        p.style.top = Math.random() * 100 + '%';
        p.style.setProperty('--tx', tx + 'px');
        p.style.setProperty('--ty', ty + 'px');
        p.style.animation = 'float-particle ' + duration + 'ms ease-out ' + delay + 'ms forwards';
        particlesContainer.appendChild(p);
      }
    }

    // Reflect auto-download status if it succeeded
    if (didAutoDl) {
      var status = ov.querySelector('[data-jwc-dl-status]');
      if (status) status.hidden = false;
      var label = ov.querySelector('[data-jwc-dl-label]');
      if (label) label.textContent = t('cele_redownload');
      showAwardsTeaser(ov, stats);
    }

    // Wire interactions
    ov.querySelectorAll('[data-jwc-close]').forEach(function (el) {
      el.addEventListener('click', function () { closeCelebration(); });
    });
    var dlBtn = ov.querySelector('[data-jwc-download]');
    if (dlBtn) dlBtn.addEventListener('click', function () {
      triggerDownload({ auto: false });
      var status = ov.querySelector('[data-jwc-dl-status]');
      if (status) status.hidden = false;
      var label = ov.querySelector('[data-jwc-dl-label]');
      if (label) label.textContent = t('cele_redownload');
      showAwardsTeaser(ov, cached && cached.stats);
    });
    var rBtn = ov.querySelector('[data-jwc-restore]');
    if (rBtn) rBtn.addEventListener('click', function () { fireAnalytics('post_merge_restore'); openRestoreGuide(); });
    var shBtn = ov.querySelector('[data-jwc-share]');
    if (shBtn) shBtn.addEventListener('click', function () { fireAnalytics('post_merge_share'); openSharePreview(cached && cached.stats); });
    var bBtn = ov.querySelector('[data-jwc-browse]');
    if (bBtn) bBtn.addEventListener('click', function () { fireAnalytics('post_merge_browse'); browseMerged(); });
    var hlBtn = ov.querySelector('[data-jwc-highlights]');
    if (hlBtn) hlBtn.addEventListener('click', function () { fireAnalytics('post_merge_highlights'); goToHighlights(); });
    var asBtn = ov.querySelector('[data-jwc-addshared]');
    if (asBtn) asBtn.addEventListener('click', function () { fireAnalytics('post_merge_addshared'); if (window.__jwReceivePickAndAdopt) window.__jwReceivePickAndAdopt(); });
    var realBtn = ov.querySelector('[data-jwc-real]');
    if (realBtn) realBtn.addEventListener('click', function () { fireAnalytics('post_merge_use_real'); resetForRealFiles(); });
    var donateLink = ov.querySelector('[data-jwc-donate]');
    if (donateLink) donateLink.addEventListener('click', function () { fireAnalytics('post_merge_donate_click'); });

    // Focus the primary (download) button
    if (dlBtn) setTimeout(function () { try { dlBtn.focus(); } catch (_) {} }, 50);
    // Animate stats counting up with completion rings + checkmarks
    setTimeout(function() {
      var statEls = ov.querySelectorAll('[data-jwc-stat-val]');
      var index = 0;
      statEls.forEach(function(el, idx) {
        var target = parseInt(el.getAttribute('data-jwc-stat-val')) || 0;
        if (target === 0) { el.classList.add('jwc-stat-zero'); return; }
        var strong = el.querySelector('strong');
        var ring = el.querySelector('.jwc-stat-ring');
        var check = el.querySelector('.jwc-stat-check');
        if (!strong || !ring || !check) return;
        var delayOffset = idx * 180;
        setTimeout(function() {
          var start = 0, elapsed = 0, duration = 650;
          ring.classList.add('jwc-ring-animate');
          var frame = setInterval(function() {
            elapsed += 16;
            var progress = Math.min(elapsed / duration, 1);
            var easeOutQuart = 1 - Math.pow(1 - progress, 4);
            var current = Math.floor(start + (target - start) * easeOutQuart);
            strong.textContent = current;
            ring.style.setProperty('--ring-progress', progress);
            if (progress >= 1) {
              clearInterval(frame);
              check.classList.add('jwc-check-visible');
            }
          }, 16);
        }, delayOffset);
      });
    }, 120);
    document.addEventListener('keydown', escListener);
  }
  function escListener(e) {
    if (e.key === 'Escape') closeCelebration();
  }
  function closeCelebration(silent) {
    var ov = document.getElementById('jw-celebrate-overlay');
    if (ov) ov.remove();
    var rg = document.getElementById('jw-restore-overlay');
    if (rg) rg.remove();
    document.body.classList.remove('jw-modal-open');
    document.removeEventListener('keydown', escListener);
    if (!silent) fireAnalytics('post_merge_close');
  }

  function goToHighlights() {
    var blobUrl = cached && cached.blobUrl;
    var name = (cached && cached.name) || 'merged.jwlibrary';
    var href = 'highlights.html';
    var nav = function () { window.location.href = href; };
    if (!blobUrl) { nav(); return; }
    function legacyHandoff(buf) {
      var req = indexedDB.open('jwsync_hl_v1', 1);
      req.onupgradeneeded = function(e) { e.target.result.createObjectStore('pending'); };
      req.onsuccess = function(e) {
        var db = e.target.result;
        var tx = db.transaction('pending', 'readwrite');
        tx.objectStore('pending').put({ name: name, buffer: buf }, 'next');
        tx.oncomplete = function() { db.close(); nav(); };
        tx.onerror = function() { db.close(); nav(); };
      };
      req.onerror = nav;
    }
    fetch(blobUrl)
      .then(function(r) { return r.arrayBuffer(); })
      .then(function(buf) {
        // Make the just-merged file the shared working file: the Stats page
        // prefers the cross-tool session over the one-shot inbox, so without
        // this it would open whatever older file the session still held.
        if (window.JwSession && window.JwSession.put) {
          window.JwSession.put(buf, name).then(function (okPut) {
            if (okPut) nav(); else legacyHandoff(buf);
          }, function () { legacyHandoff(buf); });
        } else {
          legacyHandoff(buf);
        }
      })
      .catch(nav);
  }

  function browseMerged() {
    var buf = cached && cached.buffer;
    if (!buf) return;
    var bootP = (typeof window.__jwBootBrowse === 'function') ? window.__jwBootBrowse() : Promise.resolve();
    bootP.then(function () {
      if (typeof window.__openJwBrowse === 'function') {
        window.__openJwBrowse(buf.slice(0));
      }
    });
  }

  function openRestoreGuide(mode) {
    mode = (mode === 'export') ? 'export' : 'restore';
    var current = detectPlatform();
    var titleKey = mode === 'export' ? 'guide_export_title' : 'guide_title';
    var html =
      '<div class="jwrg-backdrop" data-jwrg-close></div>' +
      '<div class="jwrg-card" role="dialog" aria-modal="true" aria-labelledby="jwrg-title">' +
        '<button class="jwrg-close" type="button" data-jwrg-close aria-label="' + esc(t('close')) + '">×</button>' +
        '<h2 id="jwrg-title" class="jwrg-title">' + esc(t(titleKey)) + '</h2>' +
        '<div class="jwrg-modes" role="tablist">' +
          '<button data-mode="export" type="button" class="jwrg-mode' + (mode === 'export' ? ' active' : '') + '">' + esc(t('guide_mode_export')) + '</button>' +
          '<button data-mode="restore" type="button" class="jwrg-mode' + (mode === 'restore' ? ' active' : '') + '">' + esc(t('guide_mode_restore')) + '</button>' +
        '</div>' +
        '<div class="jwrg-tabs" role="tablist">' +
          '<button data-platform="ios" class="jwrg-tab' + (current === 'ios' ? ' active' : '') + '" role="tab">' + esc(t('guide_tab_ios')) + '</button>' +
          '<button data-platform="android" class="jwrg-tab' + (current === 'android' ? ' active' : '') + '" role="tab">' + esc(t('guide_tab_android')) + '</button>' +
          '<button data-platform="other" class="jwrg-tab' + (current === 'other' ? ' active' : '') + '" role="tab">' + esc(t('guide_tab_other')) + '</button>' +
        '</div>' +
        '<ol class="jwrg-steps" id="jwrg-steps"></ol>' +
        '<div id="jwrg-warning">' + buildSafePanel() + '</div>' +
        '<div class="jwrg-actions">' +
          '<button class="jwrg-done" type="button" data-jwrg-close>' + esc(t('guide_done')) + '</button>' +
        '</div>' +
      '</div>';

    var ov = document.createElement('div');
    ov.id = 'jw-restore-overlay';
    ov.innerHTML = html;
    document.body.appendChild(ov);

    var curPlatform = current;
    function renderSteps(platform) {
      curPlatform = platform;
      var ol = ov.querySelector('#jwrg-steps');
      var src = mode === 'export' ? EXPORT_GUIDE : GUIDE;
      var steps = src[platform] || src.other;
      ol.innerHTML = steps.map(function (s) { return '<li>' + s + '</li>'; }).join('');
    }
    function applyMode() {
      var titleEl = ov.querySelector('#jwrg-title');
      if (titleEl) titleEl.textContent = t(mode === 'export' ? 'guide_export_title' : 'guide_title');
      var warn = ov.querySelector('#jwrg-warning');
      if (warn) warn.style.display = mode === 'export' ? 'none' : '';
      ov.querySelectorAll('.jwrg-mode').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-mode') === mode);
      });
      renderSteps(curPlatform);
    }
    applyMode();

    ov.querySelectorAll('.jwrg-mode').forEach(function (btn) {
      btn.addEventListener('click', function () {
        mode = btn.getAttribute('data-mode') === 'export' ? 'export' : 'restore';
        applyMode();
      });
    });

    ov.querySelectorAll('.jwrg-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        ov.querySelectorAll('.jwrg-tab').forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        renderSteps(tab.getAttribute('data-platform'));
      });
    });
    ov.querySelectorAll('[data-jwrg-close]').forEach(function (el) {
      el.addEventListener('click', function () { ov.remove(); });
    });
  }

  window.__jwOpenGuide = function (mode) { openRestoreGuide(mode === 'restore' ? 'restore' : 'export'); };

  function resetForRealFiles() {
    var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
    for (var i = 0; i < inputs.length; i++) {
      try {
        inputs[i].value = '';
        inputs[i].dispatchEvent(new Event('change', { bubbles: true }));
      } catch (_) {}
    }
    closeCelebration(true);
    setTimeout(function () {
      var main = document.querySelector('input[type="file"][accept=".jwlibrary"]:not([multiple])');
      var node = main && (main.closest('[class*="step"]') || main.parentElement);
      if (node && node.scrollIntoView) {
        try { node.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (_) {}
      }
    }, 120);
  }

  function checkAnchor(node) {
    if (!node || node.tagName !== 'A') return;
    if (node.getAttribute && node.getAttribute('download') === null) return;
    var href = node.getAttribute && node.getAttribute('href') || '';
    if (href.indexOf('blob:') !== 0) return;
    if (href === lastSeenBlob) return;
    lastSeenBlob = href;
    handleMergeComplete(href);
  }
  function handleMergeComplete(blobUrl) {
    var demoMode = isDemoMerge();
    fireAnalytics(demoMode ? 'merge_complete_demo' : 'merge_complete_real');
    cached = { stats: null, buffer: null, demoMode: demoMode, name: readDownloadName(), blobUrl: blobUrl };

    // v2.11.0 — Conflict Reviewer: if any notes were edited differently
    // across the source backups, let the user review/override which version
    // wins BEFORE the file downloads. Resolves instantly (to null) when the
    // reviewer is absent, deps are missing, or there are no conflicts.
    var reviewP = (typeof window.__jwConflictReview === 'function')
      ? window.__jwConflictReview({ blobUrl: blobUrl, downloadName: cached.name }).catch(function () { return null; })
      : Promise.resolve(null);

    reviewP.then(function (res) {
      var finalUrl = (res && res.blobUrl) ? res.blobUrl : blobUrl;
      if (res && res.blobUrl && res.blobUrl !== blobUrl) {
        // User overrode one or more conflicts → swap the corrected file in.
        var dl = document.getElementById('download-btn');
        if (dl) dl.setAttribute('href', finalUrl);
        lastSeenBlob = finalUrl;      // stop the observer re-firing on our own swap
        cached.blobUrl = finalUrl;
        fireAnalytics('merge_conflicts_resolved');
      }
      proceedToCelebration(finalUrl, demoMode);
    });
  }

  function proceedToCelebration(blobUrl, demoMode) {
    // Try to auto-trigger the file download once per merge. Some browsers
    // block programmatic downloads not initiated by a user gesture; the
    // overlay always renders a manual Download button as the primary CTA
    // so the user can complete the download with one click if the auto
    // attempt was blocked.
    var didAutoDl = false;
    if (autoDownloadedFor !== blobUrl) {
      autoDownloadedFor = blobUrl;
      didAutoDl = triggerDownload({ auto: true });
    }

    renderCelebration({ stats: null, demoMode: demoMode, autoDownloaded: didAutoDl });
    fetchStats(blobUrl).then(function (stats) {
      if (!stats) return;
      cached.stats = stats;
      var ov = document.getElementById('jw-celebrate-overlay');
      if (!ov) return;
      if (didAutoDl) showAwardsTeaser(ov, stats);
      var statsEls = ov.querySelectorAll('.jwc-stat strong');
      if (statsEls.length >= 4) {
        statsEls[0].textContent = String(stats.notes);
        statsEls[1].textContent = String(stats.highlights);
        statsEls[2].textContent = String(stats.bookmarks);
        statsEls[3].textContent = String(stats.tags);
      }
    });
  }

  function init() {
    var existing = document.querySelectorAll('a#download-btn[download]');
    for (var i = 0; i < existing.length; i++) {
      var href = existing[i].getAttribute('href') || '';
      if (href.indexOf('blob:') === 0) { checkAnchor(existing[i]); break; }
    }
    var obs = new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        var m = muts[i];
        if (m.type === 'attributes' && m.target) checkAnchor(m.target);
        for (var j = 0; j < (m.addedNodes ? m.addedNodes.length : 0); j++) {
          var n = m.addedNodes[j];
          if (n.nodeType !== 1) continue;
          if (n.tagName === 'A') checkAnchor(n);
          else if (n.querySelectorAll) {
            n.querySelectorAll('a[download]').forEach(checkAnchor);
          }
        }
      }
    });
    obs.observe(document.body, {
      attributes: true,
      attributeFilter: ['href'],
      subtree: true,
      childList: true
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

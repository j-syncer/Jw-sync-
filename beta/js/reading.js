/*!
 * JW Sync — Reading Companion (shared)
 * A daily Bible reading plan that lives entirely on-device: pick an order
 * (canonical or chronological) and a pace, get a "Today's reading" portion
 * every day with one-tap links to each chapter, keep a streak, and — because
 * JW Sync can read the user's own .jwlibrary — see your own past notes and
 * highlights on today's chapters while you read.
 *
 * Public API (window.JwReading):
 *   open()            -> full-screen overlay with the companion
 *   mount(container)  -> renders the companion inline into a host element
 *   updateHomeCard()  -> refreshes the landing tool card with live plan state
 *   _engine           -> pure plan/schedule functions (used by the test suite)
 *
 * All state lives in localStorage key jwsync_reading_v1. No uploads, ever.
 */
(function () {
  'use strict';
  if (window.JwReading) return;

  // ── i18n (12 languages) ───────────────────────────────────────────────
  var I18N = {
    en: { brand: 'Reading Companion', tagline: 'Read the Bible on a daily plan — with your own study notes beside you.', choose_plan: 'Reading order', plan_canon: 'In Bible order', plan_canon_d: 'Genesis through Revelation, straight through.', plan_chrono: 'Chronological', plan_chrono_d: 'Books arranged in the approximate order events happened.', choose_pace: 'Pace', pace_3m: '3 months', pace_6m: '6 months', pace_1y: '1 year', pace_2y: '2 years', pace_custom: 'Custom', per_day: '{n} chapters a day', finish_by: 'You would finish around {d}', start: 'Start my reading plan', today: "Today's reading", read: 'Read', streak_days: '{n}-day streak', done_t: "Today's reading is done", done_s: 'A little every day — that is how the whole Bible gets read.', come_back: 'Come back tomorrow for the next portion.', progress: 'Your progress', chapters_read: '{a} of {b} chapters read', forecast: 'On pace to finish around {d}', your_notes: "Your notes on today's chapters", your_notes_s: 'From your own library — written the last time you studied here.', notes_none: 'No notes on these chapters yet. Today is a good day to write the first one.', notes_hint: 'Load a .jwlibrary backup in any JW Sync tool and your own notes will appear here.', hl_n: '{n} highlighted', change: 'Change plan', reset: 'Start over', reset_c: 'Reset your reading plan? Your reading progress will be erased.', confirm: 'Yes, reset', cancel: 'Cancel', close: 'Close', ms_t: 'Milestone reached', ms_book: 'You finished {b}', ms_hebrew: 'Hebrew-Aramaic Scriptures complete', ms_greek: 'Christian Greek Scriptures complete', ms_all: 'You have read the whole Bible', card_today: 'Today: {r}', card_start: 'Start today', finished_t: 'You read the whole Bible', finished_s: 'Every one of the 1,189 chapters. Start a new plan any time.' },
    es: { brand: 'Compañero de lectura', tagline: 'Lee la Biblia con un plan diario, con tus propias notas de estudio al lado.', choose_plan: 'Orden de lectura', plan_canon: 'En orden bíblico', plan_canon_d: 'De Génesis a Apocalipsis, de corrido.', plan_chrono: 'Cronológico', plan_chrono_d: 'Los libros en el orden aproximado en que ocurrieron los hechos.', choose_pace: 'Ritmo', pace_3m: '3 meses', pace_6m: '6 meses', pace_1y: '1 año', pace_2y: '2 años', pace_custom: 'Personalizado', per_day: '{n} capítulos al día', finish_by: 'Terminarías alrededor del {d}', start: 'Comenzar mi plan de lectura', today: 'Lectura de hoy', read: 'Leer', streak_days: 'Racha de {n} días', done_t: 'La lectura de hoy está completa', done_s: 'Un poco cada día: así se termina de leer toda la Biblia.', come_back: 'Vuelve mañana para la siguiente porción.', progress: 'Tu progreso', chapters_read: '{a} de {b} capítulos leídos', forecast: 'A este ritmo terminarás alrededor del {d}', your_notes: 'Tus notas sobre los capítulos de hoy', your_notes_s: 'De tu propia biblioteca, escritas la última vez que estudiaste aquí.', notes_none: 'Aún no hay notas sobre estos capítulos. Hoy es un buen día para escribir la primera.', notes_hint: 'Carga una copia .jwlibrary en cualquier herramienta de JW Sync y tus notas aparecerán aquí.', hl_n: '{n} resaltados', change: 'Cambiar plan', reset: 'Empezar de nuevo', reset_c: '¿Restablecer tu plan de lectura? Tu progreso se borrará.', confirm: 'Sí, restablecer', cancel: 'Cancelar', close: 'Cerrar', ms_t: 'Meta alcanzada', ms_book: 'Terminaste {b}', ms_hebrew: 'Escrituras Hebreoarameas completas', ms_greek: 'Escrituras Griegas Cristianas completas', ms_all: 'Has leído toda la Biblia', card_today: 'Hoy: {r}', card_start: 'Empieza hoy', finished_t: 'Leíste toda la Biblia', finished_s: 'Los 1,189 capítulos completos. Puedes empezar un nuevo plan cuando quieras.' },
    pt: { brand: 'Companheiro de leitura', tagline: 'Leia a Bíblia com um plano diário — com suas próprias notas de estudo ao lado.', choose_plan: 'Ordem de leitura', plan_canon: 'Na ordem bíblica', plan_canon_d: 'De Gênesis a Apocalipse, direto.', plan_chrono: 'Cronológica', plan_chrono_d: 'Os livros na ordem aproximada em que os fatos aconteceram.', choose_pace: 'Ritmo', pace_3m: '3 meses', pace_6m: '6 meses', pace_1y: '1 ano', pace_2y: '2 anos', pace_custom: 'Personalizado', per_day: '{n} capítulos por dia', finish_by: 'Você terminaria por volta de {d}', start: 'Começar meu plano de leitura', today: 'Leitura de hoje', read: 'Ler', streak_days: 'Sequência de {n} dias', done_t: 'A leitura de hoje está completa', done_s: 'Um pouco por dia — é assim que se lê a Bíblia inteira.', come_back: 'Volte amanhã para a próxima parte.', progress: 'Seu progresso', chapters_read: '{a} de {b} capítulos lidos', forecast: 'Nesse ritmo você termina por volta de {d}', your_notes: 'Suas notas sobre os capítulos de hoje', your_notes_s: 'Da sua própria biblioteca, escritas na última vez que você estudou aqui.', notes_none: 'Ainda não há notas nesses capítulos. Hoje é um bom dia para escrever a primeira.', notes_hint: 'Carregue um backup .jwlibrary em qualquer ferramenta do JW Sync e suas notas aparecerão aqui.', hl_n: '{n} destaques', change: 'Mudar plano', reset: 'Recomeçar', reset_c: 'Redefinir seu plano de leitura? Seu progresso será apagado.', confirm: 'Sim, redefinir', cancel: 'Cancelar', close: 'Fechar', ms_t: 'Marco alcançado', ms_book: 'Você terminou {b}', ms_hebrew: 'Escrituras Hebraico-Aramaicas completas', ms_greek: 'Escrituras Gregas Cristãs completas', ms_all: 'Você leu a Bíblia inteira', card_today: 'Hoje: {r}', card_start: 'Comece hoje', finished_t: 'Você leu a Bíblia inteira', finished_s: 'Todos os 1.189 capítulos. Comece um novo plano quando quiser.' },
    fr: { brand: 'Compagnon de lecture', tagline: 'Lisez la Bible avec un programme quotidien — avec vos propres notes d’étude à côté.', choose_plan: 'Ordre de lecture', plan_canon: 'Dans l’ordre biblique', plan_canon_d: 'De la Genèse à la Révélation, d’une traite.', plan_chrono: 'Chronologique', plan_chrono_d: 'Les livres dans l’ordre approximatif des événements.', choose_pace: 'Rythme', pace_3m: '3 mois', pace_6m: '6 mois', pace_1y: '1 an', pace_2y: '2 ans', pace_custom: 'Personnalisé', per_day: '{n} chapitres par jour', finish_by: 'Vous termineriez vers le {d}', start: 'Commencer mon programme', today: 'Lecture du jour', read: 'Lire', streak_days: 'Série de {n} jours', done_t: 'La lecture du jour est terminée', done_s: 'Un peu chaque jour : c’est ainsi qu’on lit toute la Bible.', come_back: 'Revenez demain pour la suite.', progress: 'Votre progression', chapters_read: '{a} chapitres lus sur {b}', forecast: 'À ce rythme, vous terminerez vers le {d}', your_notes: 'Vos notes sur les chapitres du jour', your_notes_s: 'Tirées de votre propre bibliothèque, écrites lors de votre dernière étude ici.', notes_none: 'Pas encore de notes sur ces chapitres. C’est le bon jour pour écrire la première.', notes_hint: 'Chargez une sauvegarde .jwlibrary dans un outil JW Sync et vos notes apparaîtront ici.', hl_n: '{n} surlignés', change: 'Changer de programme', reset: 'Recommencer', reset_c: 'Réinitialiser votre programme de lecture ? Votre progression sera effacée.', confirm: 'Oui, réinitialiser', cancel: 'Annuler', close: 'Fermer', ms_t: 'Étape franchie', ms_book: 'Vous avez terminé {b}', ms_hebrew: 'Écritures hébraïques et araméennes terminées', ms_greek: 'Écritures grecques chrétiennes terminées', ms_all: 'Vous avez lu toute la Bible', card_today: 'Aujourd’hui : {r}', card_start: 'Commencez aujourd’hui', finished_t: 'Vous avez lu toute la Bible', finished_s: 'Les 1 189 chapitres, tous lus. Commencez un nouveau programme quand vous voulez.' },
    de: { brand: 'Lesebegleiter', tagline: 'Lies die Bibel nach einem Tagesplan — mit deinen eigenen Studiennotizen daneben.', choose_plan: 'Lesereihenfolge', plan_canon: 'In biblischer Reihenfolge', plan_canon_d: 'Von 1. Mose bis Offenbarung, der Reihe nach.', plan_chrono: 'Chronologisch', plan_chrono_d: 'Die Bücher ungefähr in der Reihenfolge der Ereignisse.', choose_pace: 'Tempo', pace_3m: '3 Monate', pace_6m: '6 Monate', pace_1y: '1 Jahr', pace_2y: '2 Jahre', pace_custom: 'Eigenes', per_day: '{n} Kapitel pro Tag', finish_by: 'Du wärst ungefähr am {d} fertig', start: 'Leseplan starten', today: 'Heutige Lesung', read: 'Lesen', streak_days: '{n}-Tage-Serie', done_t: 'Die heutige Lesung ist geschafft', done_s: 'Jeden Tag ein wenig — so liest man die ganze Bibel.', come_back: 'Komm morgen für den nächsten Abschnitt wieder.', progress: 'Dein Fortschritt', chapters_read: '{a} von {b} Kapiteln gelesen', forecast: 'In diesem Tempo bist du ungefähr am {d} fertig', your_notes: 'Deine Notizen zu den heutigen Kapiteln', your_notes_s: 'Aus deiner eigenen Bibliothek — geschrieben, als du hier zuletzt studiert hast.', notes_none: 'Noch keine Notizen zu diesen Kapiteln. Heute ist ein guter Tag für die erste.', notes_hint: 'Lade in einem JW-Sync-Tool eine .jwlibrary-Sicherung, dann erscheinen deine Notizen hier.', hl_n: '{n} Markierungen', change: 'Plan ändern', reset: 'Neu anfangen', reset_c: 'Leseplan zurücksetzen? Dein Fortschritt wird gelöscht.', confirm: 'Ja, zurücksetzen', cancel: 'Abbrechen', close: 'Schließen', ms_t: 'Meilenstein erreicht', ms_book: 'Du hast {b} abgeschlossen', ms_hebrew: 'Hebräisch-aramäische Schriften abgeschlossen', ms_greek: 'Christlich-griechische Schriften abgeschlossen', ms_all: 'Du hast die ganze Bibel gelesen', card_today: 'Heute: {r}', card_start: 'Fang heute an', finished_t: 'Du hast die ganze Bibel gelesen', finished_s: 'Alle 1.189 Kapitel. Starte jederzeit einen neuen Plan.' },
    it: { brand: 'Compagno di lettura', tagline: 'Leggi la Bibbia con un piano quotidiano — con le tue note di studio accanto.', choose_plan: 'Ordine di lettura', plan_canon: 'In ordine biblico', plan_canon_d: 'Da Genesi a Rivelazione, di seguito.', plan_chrono: 'Cronologico', plan_chrono_d: 'I libri nell’ordine approssimativo degli avvenimenti.', choose_pace: 'Ritmo', pace_3m: '3 mesi', pace_6m: '6 mesi', pace_1y: '1 anno', pace_2y: '2 anni', pace_custom: 'Personalizzato', per_day: '{n} capitoli al giorno', finish_by: 'Finiresti intorno al {d}', start: 'Inizia il mio piano di lettura', today: 'Lettura di oggi', read: 'Leggi', streak_days: 'Serie di {n} giorni', done_t: 'La lettura di oggi è completa', done_s: 'Un po’ ogni giorno: è così che si legge tutta la Bibbia.', come_back: 'Torna domani per la prossima parte.', progress: 'I tuoi progressi', chapters_read: '{a} capitoli letti su {b}', forecast: 'A questo ritmo finirai intorno al {d}', your_notes: 'Le tue note sui capitoli di oggi', your_notes_s: 'Dalla tua biblioteca, scritte l’ultima volta che hai studiato qui.', notes_none: 'Ancora nessuna nota su questi capitoli. Oggi è un buon giorno per scrivere la prima.', notes_hint: 'Carica un backup .jwlibrary in un qualsiasi strumento di JW Sync e le tue note appariranno qui.', hl_n: '{n} evidenziazioni', change: 'Cambia piano', reset: 'Ricomincia', reset_c: 'Azzerare il piano di lettura? I tuoi progressi saranno cancellati.', confirm: 'Sì, azzera', cancel: 'Annulla', close: 'Chiudi', ms_t: 'Traguardo raggiunto', ms_book: 'Hai finito {b}', ms_hebrew: 'Scritture Ebraico-Aramaiche completate', ms_greek: 'Scritture Greche Cristiane completate', ms_all: 'Hai letto tutta la Bibbia', card_today: 'Oggi: {r}', card_start: 'Inizia oggi', finished_t: 'Hai letto tutta la Bibbia', finished_s: 'Tutti i 1.189 capitoli. Inizia un nuovo piano quando vuoi.' },
    ru: { brand: 'Спутник чтения', tagline: 'Читайте Библию по ежедневному плану — рядом с вашими собственными заметками.', choose_plan: 'Порядок чтения', plan_canon: 'По порядку книг', plan_canon_d: 'От Бытия до Откровения, подряд.', plan_chrono: 'Хронологический', plan_chrono_d: 'Книги в примерном порядке событий.', choose_pace: 'Темп', pace_3m: '3 месяца', pace_6m: '6 месяцев', pace_1y: '1 год', pace_2y: '2 года', pace_custom: 'Свой темп', per_day: '{n} глав в день', finish_by: 'Вы закончите примерно {d}', start: 'Начать план чтения', today: 'Чтение на сегодня', read: 'Читать', streak_days: 'Серия {n} дней', done_t: 'Чтение на сегодня выполнено', done_s: 'Понемногу каждый день — так прочитывается вся Библия.', come_back: 'Возвращайтесь завтра за следующей частью.', progress: 'Ваш прогресс', chapters_read: 'Прочитано глав: {a} из {b}', forecast: 'В таком темпе вы закончите примерно {d}', your_notes: 'Ваши заметки к сегодняшним главам', your_notes_s: 'Из вашей собственной библиотеки — написаны, когда вы изучали эти места раньше.', notes_none: 'К этим главам пока нет заметок. Сегодня хороший день, чтобы написать первую.', notes_hint: 'Загрузите резервную копию .jwlibrary в любом инструменте JW Sync, и ваши заметки появятся здесь.', hl_n: 'Выделений: {n}', change: 'Сменить план', reset: 'Начать заново', reset_c: 'Сбросить план чтения? Ваш прогресс будет удалён.', confirm: 'Да, сбросить', cancel: 'Отмена', close: 'Закрыть', ms_t: 'Веха достигнута', ms_book: 'Вы прочитали {b}', ms_hebrew: 'Еврейско-арамейские Писания прочитаны', ms_greek: 'Христианские Греческие Писания прочитаны', ms_all: 'Вы прочитали всю Библию', card_today: 'Сегодня: {r}', card_start: 'Начните сегодня', finished_t: 'Вы прочитали всю Библию', finished_s: 'Все 1 189 глав. Начните новый план в любое время.' },
    ja: { brand: '通読コンパニオン', tagline: '毎日の計画に沿って聖書を通読。自分の研究ノートをすぐ隣に。', choose_plan: '読む順序', plan_canon: '聖書の順', plan_canon_d: '創世記から啓示の書まで順番に。', plan_chrono: '年代順', plan_chrono_d: '出来事が起きたおおよその順序で。', choose_pace: 'ペース', pace_3m: '3か月', pace_6m: '6か月', pace_1y: '1年', pace_2y: '2年', pace_custom: 'カスタム', per_day: '1日{n}章', finish_by: '{d}ごろに読み終わる予定です', start: '通読計画を始める', today: '今日の通読', read: '読む', streak_days: '{n}日連続', done_t: '今日の通読は完了です', done_s: '毎日少しずつ。それが聖書全巻を読み通す方法です。', come_back: 'また明日、次の範囲をどうぞ。', progress: '進み具合', chapters_read: '{b}章中{a}章を読了', forecast: 'このペースなら{d}ごろに完了します', your_notes: '今日の章についてのあなたのノート', your_notes_s: 'あなた自身のライブラリーから。前回ここを研究したときに書いたものです。', notes_none: 'この章のノートはまだありません。今日が最初の1つを書く良い日です。', notes_hint: 'JW Syncのいずれかのツールで.jwlibraryバックアップを読み込むと、ここにノートが表示されます。', hl_n: 'ハイライト{n}件', change: '計画を変更', reset: '最初からやり直す', reset_c: '通読計画をリセットしますか？ 進み具合は消去されます。', confirm: 'はい、リセット', cancel: 'キャンセル', close: '閉じる', ms_t: '節目に到達', ms_book: '{b}を読み終えました', ms_hebrew: 'ヘブライ語・アラム語聖書を読了', ms_greek: 'クリスチャン・ギリシャ語聖書を読了', ms_all: '聖書全巻を読み終えました', card_today: '今日: {r}', card_start: '今日から始める', finished_t: '聖書全巻を読み終えました', finished_s: '全1,189章を読了。いつでも新しい計画を始められます。' },
    ko: { brand: '통독 도우미', tagline: '매일의 계획에 따라 성경을 읽으세요. 나의 연구 노트를 바로 옆에 두고서.', choose_plan: '읽는 순서', plan_canon: '성경 순서대로', plan_canon_d: '창세기부터 계시록까지 차례대로.', plan_chrono: '연대순', plan_chrono_d: '사건이 일어난 대략적인 순서대로.', choose_pace: '속도', pace_3m: '3개월', pace_6m: '6개월', pace_1y: '1년', pace_2y: '2년', pace_custom: '직접 설정', per_day: '하루 {n}장', finish_by: '{d}쯤 마치게 됩니다', start: '통독 계획 시작', today: '오늘의 통독', read: '읽기', streak_days: '{n}일 연속', done_t: '오늘의 통독을 마쳤습니다', done_s: '매일 조금씩. 그것이 성경 전체를 읽는 방법입니다.', come_back: '내일 다음 부분으로 다시 오세요.', progress: '나의 진도', chapters_read: '{b}장 중 {a}장 읽음', forecast: '이 속도라면 {d}쯤 마칩니다', your_notes: '오늘 읽을 장에 대한 나의 노트', your_notes_s: '나의 라이브러리에서 가져왔습니다. 지난번 이 부분을 연구할 때 쓴 것입니다.', notes_none: '이 장들에는 아직 노트가 없습니다. 오늘이 첫 노트를 쓰기 좋은 날입니다.', notes_hint: 'JW Sync의 어느 도구에서든 .jwlibrary 백업을 불러오면 나의 노트가 여기에 표시됩니다.', hl_n: '하이라이트 {n}개', change: '계획 변경', reset: '처음부터 다시', reset_c: '통독 계획을 초기화할까요? 진도가 지워집니다.', confirm: '예, 초기화', cancel: '취소', close: '닫기', ms_t: '이정표 달성', ms_book: '{b}을(를) 다 읽었습니다', ms_hebrew: '히브리어·아람어 성경 완독', ms_greek: '그리스도인 그리스어 성경 완독', ms_all: '성경 전체를 다 읽었습니다', card_today: '오늘: {r}', card_start: '오늘 시작하세요', finished_t: '성경 전체를 다 읽었습니다', finished_s: '1,189장 전부입니다. 언제든 새 계획을 시작하세요.' },
    tl: { brand: 'Kasama sa Pagbabasa', tagline: 'Basahin ang Bibliya ayon sa pang-araw-araw na plano — kasama ang sarili mong mga nota sa pag-aaral.', choose_plan: 'Ayos ng pagbabasa', plan_canon: 'Ayon sa pagkakasunod sa Bibliya', plan_canon_d: 'Mula Genesis hanggang Apocalipsis, tuloy-tuloy.', plan_chrono: 'Ayon sa panahon', plan_chrono_d: 'Ang mga aklat sa tinatayang pagkakasunod ng mga pangyayari.', choose_pace: 'Bilis', pace_3m: '3 buwan', pace_6m: '6 na buwan', pace_1y: '1 taon', pace_2y: '2 taon', pace_custom: 'Sariling bilis', per_day: '{n} kabanata bawat araw', finish_by: 'Matatapos ka bandang {d}', start: 'Simulan ang plano ko sa pagbabasa', today: 'Babasahin ngayon', read: 'Basahin', streak_days: '{n}-araw na sunod-sunod', done_t: 'Tapos na ang babasahin ngayon', done_s: 'Kaunti bawat araw — ganiyan nababasa ang buong Bibliya.', come_back: 'Bumalik bukas para sa susunod na bahagi.', progress: 'Ang progreso mo', chapters_read: '{a} sa {b} kabanata ang nabasa', forecast: 'Sa bilis na ito, matatapos ka bandang {d}', your_notes: 'Ang mga nota mo sa mga kabanata ngayon', your_notes_s: 'Mula sa sarili mong library — isinulat noong huli kang nag-aral dito.', notes_none: 'Wala pang nota sa mga kabanatang ito. Magandang araw ngayon para isulat ang una.', notes_hint: 'Mag-load ng .jwlibrary backup sa alinmang tool ng JW Sync at lalabas dito ang mga nota mo.', hl_n: '{n} naka-highlight', change: 'Palitan ang plano', reset: 'Magsimula ulit', reset_c: 'I-reset ang plano sa pagbabasa? Mabubura ang progreso mo.', confirm: 'Oo, i-reset', cancel: 'Kanselahin', close: 'Isara', ms_t: 'Naabot ang palatandaan', ms_book: 'Natapos mo ang {b}', ms_hebrew: 'Tapos na ang Hebreo-Aramaikong Kasulatan', ms_greek: 'Tapos na ang Kristiyanong Griegong Kasulatan', ms_all: 'Nabasa mo na ang buong Bibliya', card_today: 'Ngayon: {r}', card_start: 'Magsimula ngayon', finished_t: 'Nabasa mo ang buong Bibliya', finished_s: 'Lahat ng 1,189 kabanata. Magsimula ng bagong plano anumang oras.' },
    sv: { brand: 'Läskompanjon', tagline: 'Läs Bibeln enligt en daglig plan — med dina egna studieanteckningar bredvid.', choose_plan: 'Läsordning', plan_canon: 'I biblisk ordning', plan_canon_d: 'Från Första Moseboken till Uppenbarelseboken, rakt igenom.', plan_chrono: 'Kronologisk', plan_chrono_d: 'Böckerna i ungefär den ordning händelserna inträffade.', choose_pace: 'Takt', pace_3m: '3 månader', pace_6m: '6 månader', pace_1y: '1 år', pace_2y: '2 år', pace_custom: 'Egen takt', per_day: '{n} kapitel om dagen', finish_by: 'Du skulle bli klar omkring {d}', start: 'Starta min läsplan', today: 'Dagens läsning', read: 'Läs', streak_days: '{n} dagar i rad', done_t: 'Dagens läsning är klar', done_s: 'Lite varje dag — så läser man hela Bibeln.', come_back: 'Kom tillbaka i morgon för nästa del.', progress: 'Dina framsteg', chapters_read: '{a} av {b} kapitel lästa', forecast: 'I den här takten är du klar omkring {d}', your_notes: 'Dina anteckningar om dagens kapitel', your_notes_s: 'Från ditt eget bibliotek — skrivna senast du studerade här.', notes_none: 'Inga anteckningar om de här kapitlen än. I dag är en bra dag att skriva den första.', notes_hint: 'Läs in en .jwlibrary-säkerhetskopia i något JW Sync-verktyg så visas dina anteckningar här.', hl_n: '{n} markeringar', change: 'Byt plan', reset: 'Börja om', reset_c: 'Nollställa din läsplan? Dina framsteg raderas.', confirm: 'Ja, nollställ', cancel: 'Avbryt', close: 'Stäng', ms_t: 'Milstolpe nådd', ms_book: 'Du har läst klart {b}', ms_hebrew: 'De hebreisk-arameiska skrifterna klara', ms_greek: 'De kristna grekiska skrifterna klara', ms_all: 'Du har läst hela Bibeln', card_today: 'I dag: {r}', card_start: 'Börja i dag', finished_t: 'Du har läst hela Bibeln', finished_s: 'Alla 1 189 kapitel. Starta en ny plan när du vill.' },
    ceb: { brand: 'Kauban sa Pagbasa', tagline: 'Basaha ang Bibliya sumala sa adlaw-adlaw nga plano — uban ang imong kaugalingong mga nota sa pagtuon.', choose_plan: 'Han-ay sa pagbasa', plan_canon: 'Sumala sa han-ay sa Bibliya', plan_canon_d: 'Gikan sa Genesis hangtod sa Pinadayag, sunodsunod.', plan_chrono: 'Sumala sa panahon', plan_chrono_d: 'Ang mga basahon sa gibanabana nga han-ay sa mga panghitabo.', choose_pace: 'Kapaspason', pace_3m: '3 ka bulan', pace_6m: '6 ka bulan', pace_1y: '1 ka tuig', pace_2y: '2 ka tuig', pace_custom: 'Kaugalingong kapaspason', per_day: '{n} ka kapitulo kada adlaw', finish_by: 'Mahuman ka mga {d}', start: 'Sugdan ang akong plano sa pagbasa', today: 'Basahon karong adlawa', read: 'Basaha', streak_days: '{n} ka adlaw nga sunod-sunod', done_t: 'Nahuman na ang basahon karong adlawa', done_s: 'Gamay kada adlaw — mao kana ang paagi nga mabasa ang tibuok Bibliya.', come_back: 'Balik ugma para sa sunod nga bahin.', progress: 'Imong pag-uswag', chapters_read: '{a} sa {b} ka kapitulo ang nabasa', forecast: 'Niini nga kapaspason, mahuman ka mga {d}', your_notes: 'Imong mga nota sa mga kapitulo karong adlawa', your_notes_s: 'Gikan sa imong kaugalingong library — gisulat sa kataposang higayon nga nagtuon ka dinhi.', notes_none: 'Wala pay nota niining mga kapituloha. Maayong adlaw karon para isulat ang una.', notes_hint: 'I-load ang .jwlibrary backup sa bisan unsang tool sa JW Sync ug makita dinhi ang imong mga nota.', hl_n: '{n} gi-highlight', change: 'Usba ang plano', reset: 'Sugod pag-usab', reset_c: 'I-reset ang plano sa pagbasa? Mawala ang imong pag-uswag.', confirm: 'Oo, i-reset', cancel: 'Kanselaha', close: 'Sirhi', ms_t: 'Naabot ang timaan', ms_book: 'Nahuman nimo ang {b}', ms_hebrew: 'Nahuman ang Hebreohanon-Aramaiko nga Kasulatan', ms_greek: 'Nahuman ang Kristohanong Gregong Kasulatan', ms_all: 'Nabasa na nimo ang tibuok Bibliya', card_today: 'Karon: {r}', card_start: 'Sugdi karon', finished_t: 'Nabasa nimo ang tibuok Bibliya', finished_s: 'Ang tanang 1,189 ka kapitulo. Sugdi ang bag-ong plano bisan kanus-a.' },sw:{brand:"Mwandani wa Kusoma",tagline:"Soma Biblia kwa ratiba ya kila siku — pamoja na madokezo yako mwenyewe ya funzo kando yako.",choose_plan:"Mpangilio wa kusoma",plan_canon:"Kwa mpangilio wa Biblia",plan_canon_d:"Kutoka Mwanzo hadi Ufunuo, moja kwa moja.",plan_chrono:"Kwa mpangilio wa matukio",plan_chrono_d:"Vitabu vimepangwa takriban kwa mpangilio ambao matukio yalitokea.",choose_pace:"Kasi",pace_3m:"Miezi 3",pace_6m:"Miezi 6",pace_1y:"Mwaka 1",pace_2y:"Miaka 2",pace_custom:"Yako mwenyewe",per_day:"Sura {n} kwa siku",finish_by:"Ungemaliza karibu na {d}",start:"Anza ratiba yangu ya kusoma",today:"Usomaji wa leo",read:"Soma",streak_days:"Mfululizo wa siku {n}",done_t:"Usomaji wa leo umekamilika",done_s:"Kidogo kila siku — ndivyo Biblia nzima inavyosomwa.",come_back:"Rudi kesho kwa fungu linalofuata.",progress:"Maendeleo yako",chapters_read:"Sura {a} kati ya {b} zimesomwa",forecast:"Kwa kasi hii utamaliza karibu na {d}",your_notes:"Madokezo yako kuhusu sura za leo",your_notes_s:"Kutoka maktaba yako mwenyewe — yaliyoandikwa mara ya mwisho ulipojifunza hapa.",notes_none:"Bado hakuna madokezo kwenye sura hizi. Leo ni siku nzuri ya kuandika la kwanza.",notes_hint:"Pakia nakala rudufu ya .jwlibrary kwenye kifaa chochote cha JW Sync na madokezo yako mwenyewe yataonekana hapa.",hl_n:"{n} vimeangaziwa",change:"Badilisha ratiba",reset:"Anza upya",reset_c:"Uweke upya ratiba yako ya kusoma? Maendeleo yako ya usomaji yatafutwa.",confirm:"Ndiyo, weka upya",cancel:"Ghairi",close:"Funga",ms_t:"Umefikia hatua muhimu",ms_book:"Umemaliza {b}",ms_hebrew:"Maandiko ya Kiebrania na Kiaramu yamekamilika",ms_greek:"Maandiko ya Kigiriki ya Kikristo yamekamilika",ms_all:"Umeisoma Biblia nzima",card_today:"Leo: {r}",card_start:"Anza leo",finished_t:"Umeisoma Biblia nzima",finished_s:"Kila moja ya sura 1,189. Anza ratiba mpya wakati wowote."},nl:{brand:"Leesmaatje",tagline:"Lees de Bijbel volgens een dagelijks plan — met je eigen studieaantekeningen ernaast.",choose_plan:"Leesvolgorde",plan_canon:"In Bijbelvolgorde",plan_canon_d:"Van Genesis tot Openbaring, achter elkaar door.",plan_chrono:"Chronologisch",plan_chrono_d:"Boeken gerangschikt in ongeveer de volgorde waarin de gebeurtenissen plaatsvonden.",choose_pace:"Tempo",pace_3m:"3 maanden",pace_6m:"6 maanden",pace_1y:"1 jaar",pace_2y:"2 jaar",pace_custom:"Zelf instellen",per_day:"{n} hoofdstukken per dag",finish_by:"Je zou rond {d} klaar zijn",start:"Start mijn leesplan",today:"Lezen van vandaag",read:"Lezen",streak_days:"Reeks van {n} dagen",done_t:"Het lezen van vandaag is klaar",done_s:"Elke dag een beetje — zo lees je de hele Bijbel uit.",come_back:"Kom morgen terug voor het volgende deel.",progress:"Je voortgang",chapters_read:"{a} van {b} hoofdstukken gelezen",forecast:"In dit tempo klaar rond {d}",your_notes:"Je aantekeningen bij de hoofdstukken van vandaag",your_notes_s:"Uit je eigen bibliotheek — geschreven toen je hier voor het laatst studeerde.",notes_none:"Nog geen aantekeningen bij deze hoofdstukken. Vandaag is een goede dag om de eerste te schrijven.",notes_hint:"Laad een .jwlibrary-back-up in een van de JW Sync-tools en je eigen aantekeningen verschijnen hier.",hl_n:"{n} gemarkeerd",change:"Plan wijzigen",reset:"Opnieuw beginnen",reset_c:"Je leesplan opnieuw instellen? Je leesvoortgang wordt gewist.",confirm:"Ja, opnieuw instellen",cancel:"Annuleren",close:"Sluiten",ms_t:"Mijlpaal bereikt",ms_book:"Je hebt {b} uitgelezen",ms_hebrew:"Hebreeuws-Aramese Geschriften voltooid",ms_greek:"Christelijke Griekse Geschriften voltooid",ms_all:"Je hebt de hele Bijbel gelezen",card_today:"Vandaag: {r}",card_start:"Begin vandaag",finished_t:"Je hebt de hele Bijbel gelezen",finished_s:"Alle 1.189 hoofdstukken. Je kunt altijd een nieuw plan beginnen."},ro:{brand:"Însoțitorul de lectură",tagline:"Citește Biblia după un plan zilnic — cu propriile tale notițe de studiu alături.",choose_plan:"Ordinea lecturii",plan_canon:"În ordinea Bibliei",plan_canon_d:"De la Geneza la Revelația, în ordine.",plan_chrono:"Cronologic",plan_chrono_d:"Cărțile aranjate aproximativ în ordinea în care s-au petrecut evenimentele.",choose_pace:"Ritm",pace_3m:"3 luni",pace_6m:"6 luni",pace_1y:"1 an",pace_2y:"2 ani",pace_custom:"Personalizat",per_day:"{n} capitole pe zi",finish_by:"Ai termina pe la {d}",start:"Începe planul meu de lectură",today:"Lectura de azi",read:"Citește",streak_days:"Serie de {n} zile",done_t:"Lectura de azi e gata",done_s:"Câte puțin în fiecare zi — așa se citește Biblia în întregime.",come_back:"Revino mâine pentru porția următoare.",progress:"Progresul tău",chapters_read:"{a} din {b} capitole citite",forecast:"În ritmul acesta termini pe la {d}",your_notes:"Notițele tale la capitolele de azi",your_notes_s:"Din propria ta bibliotecă — scrise ultima dată când ai studiat aici.",notes_none:"Încă nicio notiță la aceste capitole. Azi e o zi bună s-o scrii pe prima.",notes_hint:"Încarcă o copie de rezervă .jwlibrary în oricare instrument JW Sync și notițele tale vor apărea aici.",hl_n:"{n} evidențiate",change:"Schimbă planul",reset:"Ia-o de la capăt",reset_c:"Resetezi planul de lectură? Progresul tău va fi șters.",confirm:"Da, resetează",cancel:"Anulează",close:"Închide",ms_t:"Prag atins",ms_book:"Ai terminat {b}",ms_hebrew:"Scripturile ebraico-aramaice, complete",ms_greek:"Scripturile grecești creștine, complete",ms_all:"Ai citit Biblia în întregime",card_today:"Azi: {r}",card_start:"Începe azi",finished_t:"Ai citit Biblia în întregime",finished_s:"Toate cele 1.189 de capitole. Poți începe oricând un plan nou."},id:{brand:"Teman Pembacaan",tagline:"Bacalah Alkitab dengan jadwal harian — ditemani catatan pelajaran Anda sendiri.",choose_plan:"Urutan pembacaan",plan_canon:"Sesuai urutan Alkitab",plan_canon_d:"Dari Kejadian sampai Penyingkapan, berurutan.",plan_chrono:"Kronologis",plan_chrono_d:"Buku-buku disusun kira-kira sesuai urutan terjadinya peristiwa.",choose_pace:"Kecepatan",pace_3m:"3 bulan",pace_6m:"6 bulan",pace_1y:"1 tahun",pace_2y:"2 tahun",pace_custom:"Sesuai keinginan",per_day:"{n} pasal sehari",finish_by:"Anda akan selesai sekitar {d}",start:"Mulai jadwal pembacaan saya",today:"Bacaan hari ini",read:"Baca",streak_days:"Rentetan {n} hari",done_t:"Bacaan hari ini selesai",done_s:"Sedikit setiap hari — begitulah seluruh Alkitab akhirnya terbaca.",come_back:"Kembalilah besok untuk bagian berikutnya.",progress:"Kemajuan Anda",chapters_read:"{a} dari {b} pasal terbaca",forecast:"Dengan kecepatan ini, selesai sekitar {d}",your_notes:"Catatan Anda pada pasal hari ini",your_notes_s:"Dari perpustakaan Anda sendiri — ditulis saat terakhir kali Anda mempelajarinya.",notes_none:"Belum ada catatan pada pasal-pasal ini. Hari ini waktu yang tepat untuk menulis yang pertama.",notes_hint:"Muat cadangan .jwlibrary di alat JW Sync mana pun, dan catatan Anda sendiri akan muncul di sini.",hl_n:"{n} disorot",change:"Ubah jadwal",reset:"Mulai dari awal",reset_c:"Atur ulang jadwal pembacaan Anda? Kemajuan pembacaan Anda akan terhapus.",confirm:"Ya, atur ulang",cancel:"Batal",close:"Tutup",ms_t:"Tonggak tercapai",ms_book:"Anda menyelesaikan {b}",ms_hebrew:"Kitab-Kitab Ibrani-Aram selesai",ms_greek:"Kitab-Kitab Yunani Kristen selesai",ms_all:"Anda telah membaca seluruh Alkitab",card_today:"Hari ini: {r}",card_start:"Mulai hari ini",finished_t:"Anda telah membaca seluruh Alkitab",finished_s:"Seluruh 1.189 pasalnya. Anda bisa memulai jadwal baru kapan saja."},hi:{brand:"पठन साथी",tagline:"रोज़ाना योजना से बाइबल पढ़ें — अपने ही अध्ययन नोटों के साथ।",choose_plan:"पढ़ने का क्रम",plan_canon:"बाइबल के क्रम में",plan_canon_d:"उत्पत्ति से प्रकाशितवाक्य तक, सीधे क्रम में।",plan_chrono:"कालक्रम के अनुसार",plan_chrono_d:"किताबें लगभग उसी क्रम में जिसमें घटनाएँ हुईं।",choose_pace:"रफ़्तार",pace_3m:"3 महीने",pace_6m:"6 महीने",pace_1y:"1 साल",pace_2y:"2 साल",pace_custom:"अपनी पसंद",per_day:"रोज़ {n} अध्याय",finish_by:"आप लगभग {d} तक पूरा करेंगे",start:"मेरी पठन योजना शुरू करें",today:"आज का पाठ",read:"पढ़ें",streak_days:"{n} दिन की लड़ी",done_t:"आज का पाठ पूरा हुआ",done_s:"रोज़ थोड़ा-थोड़ा — इसी तरह पूरी बाइबल पढ़ी जाती है।",come_back:"अगले हिस्से के लिए कल फिर आइए।",progress:"आपकी प्रगति",chapters_read:"{b} में से {a} अध्याय पढ़े",forecast:"इसी रफ़्तार से लगभग {d} तक पूरा होगा",your_notes:"आज के अध्यायों पर आपके नोट",your_notes_s:"आपकी अपनी लाइब्रेरी से — जब आपने पिछली बार यहाँ अध्ययन किया था।",notes_none:"इन अध्यायों पर अभी कोई नोट नहीं है। पहला नोट लिखने के लिए आज अच्छा दिन है।",notes_hint:"किसी भी JW Sync टूल में .jwlibrary बैकअप लोड करें और आपके अपने नोट यहाँ दिखेंगे।",hl_n:"{n} हाइलाइट",change:"योजना बदलें",reset:"फिर से शुरू करें",reset_c:"अपनी पठन योजना रीसेट करें? आपकी पढ़ाई की प्रगति मिट जाएगी।",confirm:"हाँ, रीसेट करें",cancel:"रद्द करें",close:"बंद करें",ms_t:"मील का पत्थर पूरा",ms_book:"आपने {b} पूरी की",ms_hebrew:"इब्रानी-अरामी शास्त्र पूरा",ms_greek:"मसीही यूनानी शास्त्र पूरा",ms_all:"आपने पूरी बाइबल पढ़ ली",card_today:"आज: {r}",card_start:"आज ही शुरू करें",finished_t:"आपने पूरी बाइबल पढ़ ली",finished_s:"पूरे 1,189 अध्याय। आप कभी भी नई योजना शुरू कर सकते हैं।"},hu:{brand:"Olvasótárs",tagline:"Olvasd a Bibliát napi terv szerint — a saját tanulmányozási jegyzeteiddel magad mellett.",choose_plan:"Olvasási sorrend",plan_canon:"Bibliai sorrendben",plan_canon_d:"Az 1Mózestől a Jelenésekig, végig egyhuzamban.",plan_chrono:"Időrendben",plan_chrono_d:"A könyvek nagyjából az események megtörténtének sorrendjében.",choose_pace:"Tempó",pace_3m:"3 hónap",pace_6m:"6 hónap",pace_1y:"1 év",pace_2y:"2 év",pace_custom:"Egyéni",per_day:"napi {n} fejezet",finish_by:"Nagyjából ekkorra végeznél: {d}",start:"Olvasási tervem indítása",today:"A mai olvasmány",read:"Olvasás",streak_days:"{n} napos sorozat",done_t:"A mai olvasmány kész",done_s:"Minden nap egy keveset — így lehet elolvasni az egész Bibliát.",come_back:"Gyere vissza holnap a következő részért.",progress:"A haladásod",chapters_read:"{a} / {b} fejezet elolvasva",forecast:"Ezzel a tempóval nagyjából ekkorra végzel: {d}",your_notes:"A jegyzeteid a mai fejezetekhez",your_notes_s:"A saját könyvtáradból — akkor írtad, amikor utoljára itt tanulmányoztál.",notes_none:"Ezekhez a fejezetekhez még nincs jegyzeted. A mai nap jó alkalom megírni az elsőt.",notes_hint:"Tölts be egy .jwlibrary mentést bármelyik JW Sync eszközben, és itt megjelennek a saját jegyzeteid.",hl_n:"{n} kiemelés",change:"Terv módosítása",reset:"Kezdés elölről",reset_c:"Visszaállítod az olvasási tervedet? Az olvasási haladásod törlődik.",confirm:"Igen, visszaállítom",cancel:"Mégse",close:"Bezárás",ms_t:"Mérföldkő elérve",ms_book:"Befejezted ezt: {b}",ms_hebrew:"A Héber–arámi Iratok kész",ms_greek:"A Keresztény Görög Iratok kész",ms_all:"Elolvastad az egész Bibliát",card_today:"Ma: {r}",card_start:"Kezdd el ma",finished_t:"Elolvastad az egész Bibliát",finished_s:"Mind az 1189 fejezetet. Bármikor indíthatsz új tervet."},vi:{brand:"Bạn đồng hành đọc Kinh Thánh",tagline:"Đọc Kinh Thánh theo lịch hằng ngày — với chính ghi chú học hỏi của bạn bên cạnh.",choose_plan:"Thứ tự đọc",plan_canon:"Theo thứ tự Kinh Thánh",plan_canon_d:"Từ Sáng thế đến Khải huyền, đọc thẳng một mạch.",plan_chrono:"Theo dòng thời gian",plan_chrono_d:"Các sách được sắp gần đúng theo thứ tự các biến cố đã xảy ra.",choose_pace:"Nhịp đọc",pace_3m:"3 tháng",pace_6m:"6 tháng",pace_1y:"1 năm",pace_2y:"2 năm",pace_custom:"Tùy chỉnh",per_day:"{n} chương mỗi ngày",finish_by:"Bạn sẽ đọc xong khoảng {d}",start:"Bắt đầu lịch đọc của tôi",today:"Phần đọc hôm nay",read:"Đọc",streak_days:"Chuỗi {n} ngày",done_t:"Đã đọc xong phần hôm nay",done_s:"Mỗi ngày một ít — đó là cách người ta đọc trọn bộ Kinh Thánh.",come_back:"Ngày mai quay lại để đọc phần tiếp theo.",progress:"Tiến độ của bạn",chapters_read:"Đã đọc {a} trong {b} chương",forecast:"Với nhịp này, bạn sẽ xong khoảng {d}",your_notes:"Ghi chú của bạn về các chương hôm nay",your_notes_s:"Từ thư viện của chính bạn — viết trong lần bạn học hỏi phần này gần nhất.",notes_none:"Chưa có ghi chú nào cho các chương này. Hôm nay là ngày tốt để viết ghi chú đầu tiên.",notes_hint:"Hãy tải một bản sao lưu .jwlibrary trong bất kỳ công cụ JW Sync nào, ghi chú của bạn sẽ hiện ra ở đây.",hl_n:"{n} phần đã tô màu",change:"Đổi lịch",reset:"Bắt đầu lại",reset_c:"Đặt lại lịch đọc của bạn? Tiến độ đọc sẽ bị xóa.",confirm:"Vâng, đặt lại",cancel:"Hủy",close:"Đóng",ms_t:"Đã đạt cột mốc",ms_book:"Bạn đã đọc xong {b}",ms_hebrew:"Hoàn tất phần Kinh Thánh tiếng Hê-bơ-rơ và A-ram",ms_greek:"Hoàn tất phần Kinh Thánh tiếng Hy Lạp",ms_all:"Bạn đã đọc trọn bộ Kinh Thánh",card_today:"Hôm nay: {r}",card_start:"Bắt đầu hôm nay",finished_t:"Bạn đã đọc trọn bộ Kinh Thánh",finished_s:"Đủ cả 1.189 chương. Bạn có thể bắt đầu một lịch đọc mới bất cứ lúc nào."},"yue-Hant":{brand:"讀經夥伴",tagline:"按每日計劃讀聖經——你自己嘅筆記就喺隔籬。",choose_plan:"閱讀次序",plan_canon:"按聖經書卷次序",plan_canon_d:"由創世記讀到啟示錄，一路讀落去。",plan_chrono:"按時間次序",plan_chrono_d:"書卷大致按事件發生嘅先後排。",choose_pace:"進度",pace_3m:"3 個月",pace_6m:"6 個月",pace_1y:"1 年",pace_2y:"2 年",pace_custom:"自訂",per_day:"每日 {n} 章",finish_by:"預計 {d} 左右讀完",start:"開始我嘅讀經計劃",today:"今日嘅進度",read:"閱讀",streak_days:"連續 {n} 日",done_t:"今日嘅閱讀做完喇",done_s:"每日讀少少——成本聖經就係咁讀完嘅。",come_back:"聽日再返嚟讀下一段。",progress:"你嘅進度",chapters_read:"已讀 {a} / {b} 章",forecast:"照呢個進度，預計 {d} 左右讀完",your_notes:"你喺今日章節上嘅筆記",your_notes_s:"嚟自你自己嘅書庫——上次研究呢度嗰陣寫嘅。",notes_none:"呢啲章節仲未有筆記。今日啱啱好可以寫低第一條。",notes_hint:"喺任何 JW Sync 工具入面載入 .jwlibrary 備份，你嘅筆記就會喺呢度顯示。",hl_n:"{n} 處標註",change:"更改計劃",reset:"由頭開始",reset_c:"要重設讀經計劃？你嘅閱讀進度會清走。",confirm:"係，重設",cancel:"取消",close:"閂咗佢",ms_t:"達成里程碑",ms_book:"你讀完咗{b}",ms_hebrew:"希伯來語同阿拉米語經卷讀完喇",ms_greek:"希臘語經卷讀完喇",ms_all:"你讀完咗成本聖經",card_today:"今日：{r}",card_start:"今日開始",finished_t:"你讀完咗成本聖經",finished_s:"全部 1189 章。幾時想開始新計劃都得。"},"zh-Hant":{brand:"讀經伴侶",tagline:"按每日計劃讀聖經——你自己的筆記就在旁邊。",choose_plan:"閱讀順序",plan_canon:"按聖經書卷順序",plan_canon_d:"從創世記到啟示錄，依次讀下去。",plan_chrono:"按時間順序",plan_chrono_d:"書卷大致按事件發生的先後排列。",choose_pace:"進度",pace_3m:"3 個月",pace_6m:"6 個月",pace_1y:"1 年",pace_2y:"2 年",pace_custom:"自定義",per_day:"每天 {n} 章",finish_by:"預計在 {d} 前後讀完",start:"開始我的讀經計劃",today:"今天的進度",read:"閱讀",streak_days:"連續 {n} 天",done_t:"今天的閱讀已完成",done_s:"每天讀一點——整本聖經就是這樣讀完的。",come_back:"明天再來讀下一段。",progress:"你的進度",chapters_read:"已讀 {a} / {b} 章",forecast:"照這個進度，預計在 {d} 前後讀完",your_notes:"你在今天章節上的筆記",your_notes_s:"來自你自己的書庫——上次研讀這裡時寫的。",notes_none:"這些章節還沒有筆記。今天正適合寫下第一條。",notes_hint:"在任意 JW Sync 工具中載入 .jwlibrary 備份，你的筆記就會顯示在這裡。",hl_n:"{n} 處標註",change:"更改計劃",reset:"重新開始",reset_c:"要重置讀經計劃嗎？你的閱讀進度將被清除。",confirm:"是的，重置",cancel:"取消",close:"關閉",ms_t:"達成里程碑",ms_book:"你讀完了{b}",ms_hebrew:"希伯來語和阿拉米語經卷已讀完",ms_greek:"希臘語經卷已讀完",ms_all:"你讀完了整本聖經",card_today:"今天：{r}",card_start:"今天開始",finished_t:"你讀完了整本聖經",finished_s:"全部 1189 章。隨時可以開始新的計劃。"},"zh-Hans":{brand:"读经伴侣",tagline:"按每日计划读圣经——你自己的笔记就在旁边。",choose_plan:"阅读顺序",plan_canon:"按圣经书卷顺序",plan_canon_d:"从创世记到启示录，依次读下去。",plan_chrono:"按时间顺序",plan_chrono_d:"书卷大致按事件发生的先后排列。",choose_pace:"进度",pace_3m:"3 个月",pace_6m:"6 个月",pace_1y:"1 年",pace_2y:"2 年",pace_custom:"自定义",per_day:"每天 {n} 章",finish_by:"预计在 {d} 前后读完",start:"开始我的读经计划",today:"今天的进度",read:"阅读",streak_days:"连续 {n} 天",done_t:"今天的阅读已完成",done_s:"每天读一点——整本圣经就是这样读完的。",come_back:"明天再来读下一段。",progress:"你的进度",chapters_read:"已读 {a} / {b} 章",forecast:"照这个进度，预计在 {d} 前后读完",your_notes:"你在今天章节上的笔记",your_notes_s:"来自你自己的书库——上次研读这里时写的。",notes_none:"这些章节还没有笔记。今天正适合写下第一条。",notes_hint:"在任意 JW Sync 工具中加载 .jwlibrary 备份，你的笔记就会显示在这里。",hl_n:"{n} 处标注",change:"更改计划",reset:"重新开始",reset_c:"要重置读经计划吗？你的阅读进度将被清除。",confirm:"是的，重置",cancel:"取消",close:"关闭",ms_t:"达成里程碑",ms_book:"你读完了{b}",ms_hebrew:"希伯来语和阿拉米语经卷已读完",ms_greek:"希腊语经卷已读完",ms_all:"你读完了整本圣经",card_today:"今天：{r}",card_start:"今天开始",finished_t:"你读完了整本圣经",finished_s:"全部 1189 章。随时可以开始新的计划。"},pl:{brand:"Towarzysz czytania",tagline:"Czytaj Biblię według dziennego planu — z własnymi notatkami obok.",choose_plan:"Kolejność czytania",plan_canon:"W kolejności ksiąg Biblii",plan_canon_d:"Od Rodzaju do Objawienia, po kolei.",plan_chrono:"Chronologicznie",plan_chrono_d:"Księgi ułożone mniej więcej w kolejności opisanych wydarzeń.",choose_pace:"Tempo",pace_3m:"3 miesiące",pace_6m:"6 miesięcy",pace_1y:"1 rok",pace_2y:"2 lata",pace_custom:"Własne",per_day:"{n} rozdziałów dziennie",finish_by:"Skończysz mniej więcej {d}",start:"Rozpocznij mój plan czytania",today:"Dzisiejsze czytanie",read:"Czytaj",streak_days:"Passa: {n} dni",done_t:"Dzisiejsze czytanie ukończone",done_s:"Po trochu każdego dnia — tak przeczytasz całą Biblię.",come_back:"Wróć jutro po kolejną porcję.",progress:"Twój postęp",chapters_read:"Przeczytano {a} z {b} rozdziałów",forecast:"W tym tempie skończysz mniej więcej {d}",your_notes:"Twoje notatki do dzisiejszych rozdziałów",your_notes_s:"Z Twojej własnej biblioteki — napisane, gdy ostatnio je studiowałeś.",notes_none:"Do tych rozdziałów nie ma jeszcze notatek. Dziś dobry dzień, żeby napisać pierwszą.",notes_hint:"Wczytaj kopię zapasową .jwlibrary w dowolnym narzędziu JW Sync, a Twoje notatki pojawią się tutaj.",hl_n:"{n} wyróżnionych",change:"Zmień plan",reset:"Zacznij od nowa",reset_c:"Zresetować Twój plan czytania? Postęp w czytaniu zostanie usunięty.",confirm:"Tak, resetuj",cancel:"Anuluj",close:"Zamknij",ms_t:"Osiągnięto etap",ms_book:"Ukończyłeś księgę {b}",ms_hebrew:"Pisma Hebrajsko-Aramejskie przeczytane",ms_greek:"Chrześcijańskie Pisma Greckie przeczytane",ms_all:"Przeczytałeś całą Biblię",card_today:"Dziś: {r}",card_start:"Zacznij dzisiaj",finished_t:"Przeczytałeś całą Biblię",finished_s:"Wszystkie 1189 rozdziałów. Nowy plan możesz zacząć w każdej chwili."},uk:{brand:"Супутник читання",tagline:"Читайте Біблію за щоденним планом — з власними нотатками поруч.",choose_plan:"Порядок читання",plan_canon:"У порядку книг Біблії",plan_canon_d:"Від Буття до Об'явлення, поспіль.",plan_chrono:"Хронологічний",plan_chrono_d:"Книги розташовані приблизно в порядку описаних подій.",choose_pace:"Темп",pace_3m:"3 місяці",pace_6m:"6 місяців",pace_1y:"1 рік",pace_2y:"2 роки",pace_custom:"Власний",per_day:"{n} розділів на день",finish_by:"Ви завершите приблизно {d}",start:"Почати мій план читання",today:"Сьогоднішнє читання",read:"Читати",streak_days:"Серія: {n} днів",done_t:"Сьогоднішнє читання виконано",done_s:"Потроху щодня — саме так прочитується вся Біблія.",come_back:"Повертайтеся завтра по наступну частину.",progress:"Ваш поступ",chapters_read:"Прочитано розділів: {a} з {b}",forecast:"За таким темпом ви завершите приблизно {d}",your_notes:"Ваші нотатки до сьогоднішніх розділів",your_notes_s:"З вашої власної бібліотеки — написані, коли ви востаннє вивчали ці уривки.",notes_none:"До цих розділів ще немає нотаток. Сьогодні гарний день, щоб написати першу.",notes_hint:"Завантажте резервну копію .jwlibrary у будь-якому інструменті JW Sync, і ваші нотатки з'являться тут.",hl_n:"{n} виділено",change:"Змінити план",reset:"Почати спочатку",reset_c:"Скинути ваш план читання? Поступ у читанні буде стерто.",confirm:"Так, скинути",cancel:"Скасувати",close:"Закрити",ms_t:"Досягнуто віху",ms_book:"Ви завершили {b}",ms_hebrew:"Єврейсько-арамейські Писання прочитано",ms_greek:"Християнські Грецькі Писання прочитано",ms_all:"Ви прочитали всю Біблію",card_today:"Сьогодні: {r}",card_start:"Почати сьогодні",finished_t:"Ви прочитали всю Біблію",finished_s:"Усі 1 189 розділів. Новий план можна почати будь-коли."},he:{brand:"מלווה הקריאה",tagline:"קראו את המקרא לפי תוכנית יומית — עם הערות הלימוד שלכם לצידכם.",choose_plan:"סדר הקריאה",plan_canon:"לפי סדר המקרא",plan_canon_d:"מבראשית ועד ההתגלות, ברצף.",plan_chrono:"כרונולוגי",plan_chrono_d:"הספרים מסודרים לפי הסדר המשוער שבו התרחשו האירועים.",choose_pace:"קצב",pace_3m:"3 חודשים",pace_6m:"6 חודשים",pace_1y:"שנה",pace_2y:"שנתיים",pace_custom:"מותאם אישית",per_day:"{n} פרקים ביום",finish_by:"תסיימו בסביבות {d}",start:"התחילו את תוכנית הקריאה שלי",today:"הקריאה של היום",read:"קריאה",streak_days:"רצף של {n} ימים",done_t:"הקריאה של היום הושלמה",done_s:"מעט בכל יום — כך קוראים את כל המקרא.",come_back:"חזרו מחר למנה הבאה.",progress:"ההתקדמות שלכם",chapters_read:"{a} מתוך {b} פרקים נקראו",forecast:"בקצב הזה תסיימו בסביבות {d}",your_notes:"ההערות שלכם על פרקי היום",your_notes_s:"מהספרייה שלכם — נכתבו בפעם האחרונה שלמדתם כאן.",notes_none:"אין עדיין הערות על הפרקים האלה. היום הוא יום טוב לכתוב את הראשונה.",notes_hint:"טענו גיבוי ‎.jwlibrary בכל כלי של JW Sync וההערות שלכם יופיעו כאן.",hl_n:"{n} מודגשות",change:"שינוי התוכנית",reset:"התחלה מחדש",reset_c:"לאפס את תוכנית הקריאה שלכם? התקדמות הקריאה שלכם תימחק.",confirm:"כן, אפס",cancel:"ביטול",close:"סגירה",ms_t:"אבן דרך הושגה",ms_book:"סיימתם את {b}",ms_hebrew:"כתבי־הקודש העבריים־ארמיים הושלמו",ms_greek:"כתבי־הקודש היווניים המשיחיים הושלמו",ms_all:"קראתם את כל המקרא",card_today:"היום: {r}",card_start:"התחילו היום",finished_t:"קראתם את כל המקרא",finished_s:"כל אחד מ-1,189 הפרקים. אפשר להתחיל תוכנית חדשה בכל עת."},ar:{brand:"رفيق القراءة",tagline:"اقرأ الكتاب المقدس وفق خطة يومية — وملاحظات درسك بجانبك.",choose_plan:"ترتيب القراءة",plan_canon:"بترتيب الكتاب المقدس",plan_canon_d:"من التكوين إلى الرؤيا، على التوالي.",plan_chrono:"حسب التسلسل الزمني",plan_chrono_d:"الأسفار مرتّبة وفق الترتيب التقريبي لوقوع الأحداث.",choose_pace:"الوتيرة",pace_3m:"3 أشهر",pace_6m:"6 أشهر",pace_1y:"سنة واحدة",pace_2y:"سنتان",pace_custom:"مخصّصة",per_day:"{n} إصحاحات يوميًا",finish_by:"ستنتهي تقريبًا في {d}",start:"ابدأ خطة قراءتي",today:"قراءة اليوم",read:"اقرأ",streak_days:"سلسلة {n} أيام",done_t:"أنجزت قراءة اليوم",done_s:"قليل كل يوم — هكذا يُقرأ الكتاب المقدس كله.",come_back:"عُد غدًا للجزء التالي.",progress:"تقدّمك",chapters_read:"قرأت {a} من {b} إصحاحًا",forecast:"بهذه الوتيرة ستنتهي تقريبًا في {d}",your_notes:"ملاحظاتك على إصحاحات اليوم",your_notes_s:"من مكتبتك الخاصة — كتبتها آخر مرة درست فيها هنا.",notes_none:"لا توجد ملاحظات على هذه الإصحاحات بعد. اليوم فرصة طيبة لكتابة أولها.",notes_hint:"حمّل نسخة احتياطية ‎.jwlibrary‎ في أي أداة من JW Sync لتظهر ملاحظاتك هنا.",hl_n:"{n} مظلَّلة",change:"غيّر الخطة",reset:"ابدأ من جديد",reset_c:"هل تريد إعادة ضبط خطة قراءتك؟ سيُمحى تقدّمك في القراءة.",confirm:"نعم، أعِد الضبط",cancel:"إلغاء",close:"إغلاق",ms_t:"بلغت محطة",ms_book:"أنهيت {b}",ms_hebrew:"أنهيت الأسفار العبرانية الأرامية",ms_greek:"أنهيت الأسفار اليونانية المسيحية",ms_all:"قرأت الكتاب المقدس كله",card_today:"اليوم: {r}",card_start:"ابدأ اليوم",finished_t:"قرأت الكتاب المقدس كله",finished_s:"كل إصحاح من الإصحاحات الـ1189. ابدأ خطة جديدة متى شئت."}
  };
  function lang() { try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; } }
  function t(k) { var L = I18N[lang()] || I18N.en; return (L && L[k] != null) ? L[k] : (I18N.en[k] != null ? I18N.en[k] : k); }
  function tf(k, repl) { var s = t(k); Object.keys(repl || {}).forEach(function (key) { s = s.replace('{' + key + '}', repl[key]); }); return s; }

  // ── Bible data ────────────────────────────────────────────────────────
  var BOOKS = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"];
  var ABBR = ["Ge","Ex","Le","Nu","De","Jos","Jg","Ru","1Sa","2Sa","1Ki","2Ki","1Ch","2Ch","Ezr","Ne","Es","Job","Ps","Pr","Ec","Ca","Isa","Jer","La","Eze","Da","Ho","Joe","Am","Ob","Jon","Mic","Na","Hab","Zep","Hag","Zec","Mal","Mt","Mr","Lu","Joh","Ac","Ro","1Co","2Co","Ga","Eph","Php","Col","1Th","2Th","1Ti","2Ti","Tit","Phm","Heb","Jas","1Pe","2Pe","1Jo","2Jo","3Jo","Jude","Re"];
  var CHAP = [50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,10,42,150,31,12,8,66,52,5,48,12,14,3,9,1,4,7,3,3,3,2,14,4,28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,5,1,1,1,22];
  var TOTAL = 1189;
  // Approximate chronological ordering of whole books (a widely used
  // book-level chronological plan; events, not composition, drive the order).
  var CHRONO = [1,18,2,3,4,5,6,7,8,9,10,19,20,21,22,11,12,13,14,31,29,32,30,28,33,23,34,36,35,24,25,26,27,15,37,38,17,16,39,41,40,42,44,59,48,52,53,46,47,45,49,50,51,57,54,56,60,58,55,61,65,43,62,63,64,66];
  var HLC = { 1: '#fde68a', 2: '#bbf7d0', 3: '#bfdbfe', 4: '#fbcfe8', 5: '#fed7aa', 6: '#e9d5ff' };
  var SQL_BASE = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';
  var SKEY = 'jwsync_reading_v1';
  var WTLOCALE = { en: 'E', es: 'S', pt: 'T', fr: 'F', de: 'X', it: 'I', ru: 'U', ja: 'J', ko: 'KO', tl: 'TG', sv: 'Z', ceb: 'CV', ar: 'A', he: 'Q', uk: 'K', pl: 'P', 'zh-Hans': 'CHS', 'zh-Hant': 'CH', 'yue-Hant': 'CHC', vi: 'VT', hu: 'H', hi: 'HI', id: 'IN', ro: 'M', nl: 'O', sw: 'SW' };

  function pad2(n) { return n < 10 ? '0' + n : '' + n; }
  function pad3(n) { return n < 10 ? '00' + n : (n < 100 ? '0' + n : '' + n); }
  // jw.org finder deep link: opens the chapter in JW Library when installed,
  // otherwise in Watchtower ONLINE LIBRARY in the browser.
  function chapterUrl(b, c) {
    return 'https://www.jw.org/finder?wtlocale=' + (WTLOCALE[lang()] || 'E') + '&pub=nwtsty&bible=' + pad2(b) + pad3(c) + '000';
  }

  // ── date helpers (local, injectable "today" for tests) ────────────────
  function dpad(n) { return n < 10 ? '0' + n : '' + n; }
  function dstr(d) { return d.getFullYear() + '-' + dpad(d.getMonth() + 1) + '-' + dpad(d.getDate()); }
  function today() { return dstr(new Date()); }
  function addDays(ds, n) { var d = new Date(ds + 'T00:00:00'); d.setDate(d.getDate() + n); return dstr(d); }
  function fmtDate(ds) {
    try { return new Date(ds + 'T00:00:00').toLocaleDateString(lang(), { year: 'numeric', month: 'long', day: 'numeric' }); }
    catch (_) { return ds; }
  }

  // ── persistent state ──────────────────────────────────────────────────
  function store() {
    var s = {};
    try { s = JSON.parse(localStorage.getItem(SKEY)) || {}; } catch (_) { s = {}; }
    s.read = s.read || {}; s.log = s.log || {}; s.cele = s.cele || {};
    return s;
  }
  function save(s) { try { localStorage.setItem(SKEY, JSON.stringify(s)); } catch (_) {} }

  // ── plan engine (pure — everything takes state + a date string) ───────
  function seqFor(plan) {
    var order = plan === 'chrono' ? CHRONO : null, seq = [], i, b, c;
    for (i = 0; i < 66; i++) {
      b = order ? order[i] : i + 1;
      for (c = 1; c <= CHAP[b - 1]; c++) seq.push([b, c]);
    }
    return seq;
  }
  function rateFor(s) { return s.perDay ? s.perDay : TOTAL / (s.days || 365); }
  function readCount(s) { return Object.keys(s.read).length; }
  function remainingSeq(s) {
    return seqFor(s.plan).filter(function (x) { return !s.read[x[0] + ':' + x[1]]; });
  }
  // Today's portion. Self-healing: the portion is always the next unread
  // chapters; missed days only move the forecast, they never pile up.
  function todayInfo(s, td) {
    var rem = remainingSeq(s);
    if (!rem.length) return { finished: true, done: true, rows: [] };
    if (s.doneDate === td) return { done: true, rows: [] };
    var k = s.daysDone || 0;
    var target = Math.floor((k + 1) * rateFor(s) + 1e-9);
    var size = Math.max(1, target - readCount(s));
    return { done: false, rows: rem.slice(0, Math.min(size, rem.length)) };
  }
  function forecast(s, td) {
    var remN = remainingSeq(s).length;
    if (!remN) return td;
    return addDays(td, Math.max(1, Math.ceil(remN / rateFor(s))));
  }
  function bookDone(s, b) {
    for (var c = 1; c <= CHAP[b - 1]; c++) if (!s.read[b + ':' + c]) return false;
    return true;
  }
  function rangeDone(s, from, to) {
    for (var b = from; b <= to; b++) if (!bookDone(s, b)) return false;
    return true;
  }
  // Marks a chapter read; returns list of freshly-hit milestone keys.
  function markRead(s, b, c, td) {
    var key = b + ':' + c;
    if (s.read[key]) return [];
    s.read[key] = 1;
    s.log[td] = (s.log[td] || 0) + 1;
    var info = todayInfo(s, td);
    if (info.done || info.finished || !info.rows.length || readCount(s) >= Math.floor(((s.daysDone || 0) + 1) * rateFor(s) + 1e-9)) {
      if (s.doneDate !== td) {
        s.doneDate = td;
        s.daysDone = (s.daysDone || 0) + 1;
        if (s.streakDate !== td) {
          s.streak = (s.streakDate === addDays(td, -1)) ? ((s.streak || 0) + 1) : 1;
          s.streakDate = td;
          s.longest = Math.max(s.longest || 0, s.streak);
        }
      }
    }
    var hit = [];
    if (bookDone(s, b) && !s.cele['b' + b]) { s.cele['b' + b] = td; hit.push('b' + b); }
    if (rangeDone(s, 1, 39) && !s.cele.hebrew) { s.cele.hebrew = td; hit.push('hebrew'); }
    if (rangeDone(s, 40, 66) && !s.cele.greek) { s.cele.greek = td; hit.push('greek'); }
    if (readCount(s) >= TOTAL && !s.cele.all) { s.cele.all = td; hit.push('all'); }
    return hit;
  }
  function portionLabel(rows) {
    if (!rows.length) return '';
    var f = rows[0], l = rows[rows.length - 1];
    if (f[0] === l[0]) {
      var nm = BOOKS[f[0] - 1];
      return f[1] === l[1] ? nm + ' ' + f[1] : nm + ' ' + f[1] + '–' + l[1];
    }
    return BOOKS[f[0] - 1] + ' ' + f[1] + ' – ' + BOOKS[l[0] - 1] + ' ' + l[1];
  }

  // ── library extraction (notes + highlights keyed by book:chapter) ─────
  var LIB = { loaded: false, notes: [], hls: {} };
  function execRows(db, sql) {
    try {
      var r = db.exec(sql); if (!r[0]) return [];
      var cols = r[0].columns;
      return r[0].values.map(function (v) { var o = {}; for (var i = 0; i < cols.length; i++) o[cols[i]] = v[i]; return o; });
    } catch (_) { return []; }
  }
  function htmlToText(html) {
    if (!html) return '';
    var s = String(html).replace(/<\s*(br|\/p|\/div|\/li|\/h[1-6])[^>]*>/gi, '\n').replace(/<\s*li[^>]*>/gi, '• ').replace(/<[^>]+>/g, '');
    var ta = document.createElement('textarea'); ta.innerHTML = s; s = ta.value;
    return s.replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
  }
  function libraryFromDb(db) {
    var out = { notes: [], hls: {} };
    if (!db) return out;
    execRows(db,
      "SELECT n.Title, n.Content, n.Created, l.BookNumber b, l.ChapterNumber c, u.ColorIndex col " +
      "FROM Note n JOIN Location l ON n.LocationId=l.LocationId " +
      "LEFT JOIN UserMark u ON n.UserMarkId=u.UserMarkId " +
      "WHERE l.BookNumber IS NOT NULL AND l.ChapterNumber IS NOT NULL"
    ).forEach(function (r) {
      var text = htmlToText(r.Content || ''), title = (r.Title || '').trim();
      if (!text && !title) return;
      out.notes.push({ b: r.b, c: r.c, title: title, text: text, created: r.Created || '', color: r.col || 0 });
    });
    execRows(db,
      "SELECT l.BookNumber b, l.ChapterNumber c, COUNT(*) n FROM UserMark u " +
      "JOIN Location l ON u.LocationId=l.LocationId " +
      "WHERE l.BookNumber IS NOT NULL AND l.ChapterNumber IS NOT NULL GROUP BY l.BookNumber, l.ChapterNumber"
    ).forEach(function (r) { out.hls[r.b + ':' + r.c] = r.n; });
    return out;
  }
  function libraryFromBuffer(buf) {
    if (!window.JSZip || !window.initSqlJs || !buf) return Promise.resolve(null);
    return new window.JSZip().loadAsync(buf).then(function (zip) {
      var nm = Object.keys(zip.files).find(function (n) { return /userdata\.db$/i.test(n); });
      if (!nm) throw new Error('no db');
      return zip.files[nm].async('uint8array');
    }).then(function (bytes) {
      return window.initSqlJs({ locateFile: function (f) { return SQL_BASE + f; } }).then(function (SQL) {
        var db = new SQL.Database(bytes); var lib = libraryFromDb(db); try { db.close(); } catch (_) {} return lib;
      });
    }).catch(function () { return null; });
  }
  function loadLibrary() {
    if (LIB.loaded) return Promise.resolve(LIB);
    var direct = null;
    try { direct = window.__jwLastFile || null; } catch (_) {}
    var src = direct ? Promise.resolve(direct) :
      (window.JwSession && window.JwSession.get ? window.JwSession.get().then(function (rec) { return rec && rec.buffer; }).catch(function () { return null; }) : Promise.resolve(null));
    return src.then(function (fileOrBuf) {
      if (!fileOrBuf) return LIB;
      // File/Blob expose .arrayBuffer(); anything else (ArrayBuffer/Uint8Array,
      // possibly from another realm) goes to JSZip as-is — it accepts both.
      var toBuf = (fileOrBuf && typeof fileOrBuf.arrayBuffer === 'function') ?
        fileOrBuf.arrayBuffer() : Promise.resolve(fileOrBuf);
      return toBuf.then(libraryFromBuffer).then(function (lib) {
        if (lib) { LIB.notes = lib.notes; LIB.hls = lib.hls; LIB.loaded = true; }
        return LIB;
      });
    }).catch(function () { return LIB; });
  }

  // ── styles ────────────────────────────────────────────────────────────
  function injectStyle() {
    if (document.getElementById('jw-reading-style')) return;
    var css = '' +
      '.jr-overlay{position:fixed;inset:0;z-index:2147483000;background:rgba(2,8,20,.92);overflow-y:auto;-webkit-overflow-scrolling:touch;font-family:Inter,system-ui,sans-serif}' +
      '.jr-wrap{max-width:680px;margin:0 auto;padding:18px 16px 60px}' +
      '.jr-head{display:flex;align-items:center;gap:10px;margin-bottom:14px;position:sticky;top:0;background:rgba(2,8,20,.96);padding:12px 0;z-index:2}' +
      '.jr-ttl{display:flex;align-items:center;gap:8px;font-weight:800;font-size:17px;color:#fdba74}' +
      '.jr-ttl svg{width:20px;height:20px;color:#fb923c}' +
      '.jr-x{margin-left:auto;background:rgba(71,85,105,.35);border:0;color:#e2e8f0;font-size:13px;font-weight:700;padding:8px 14px;border-radius:9px;cursor:pointer;font-family:inherit}' +
      '.jr-x:hover{background:rgba(71,85,105,.5)}' +
      '.jr-tagline{font-size:13.5px;color:#94a3b8;line-height:1.55;margin:0 0 18px}' +
      '.jr-sec{background:rgba(15,28,52,.55);border:1px solid rgba(234,88,12,.28);border-radius:14px;padding:16px;margin-bottom:14px}' +
      '.jr-sec-t{font-size:11px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#fdba74;margin:0 0 10px}' +
      '.jr-opt-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}' +
      '.jr-opt{background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.16);border-radius:11px;padding:12px;cursor:pointer;text-align:left;font-family:inherit;color:inherit}' +
      '.jr-opt.jr-on{border-color:#ea580c;background:rgba(234,88,12,.12)}' +
      '.jr-opt-t{font-size:14px;font-weight:700;color:#f1f5f9}' +
      '.jr-opt-d{font-size:12px;color:#94a3b8;line-height:1.45;margin-top:3px}' +
      '.jr-pace-row{display:flex;flex-wrap:wrap;gap:8px}' +
      '.jr-pace{background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.16);border-radius:999px;padding:8px 15px;font-size:13px;font-weight:700;color:#e2e8f0;cursor:pointer;font-family:inherit}' +
      '.jr-pace.jr-on{border-color:#ea580c;background:rgba(234,88,12,.14);color:#fdba74}' +
      '.jr-custom{display:flex;align-items:center;gap:8px;margin-top:10px;font-size:13px;color:#94a3b8}' +
      '.jr-custom input{width:64px;background:rgba(4,12,28,.6);border:1px solid rgba(148,163,184,.25);border-radius:8px;color:#f1f5f9;font-size:14px;font-weight:700;padding:7px 9px;font-family:inherit;text-align:center}' +
      '.jr-finish-note{font-size:13px;color:#fdba74;font-weight:600;margin-top:12px}' +
      '.jr-start{display:block;width:100%;background:#ea580c;color:#fff;border:0;padding:13px;border-radius:11px;font-size:15px;font-weight:800;cursor:pointer;font-family:inherit;margin-top:4px;box-shadow:0 1px 5px rgba(0,0,0,.35)}' +
      '.jr-start:hover{background:#c2410c}' +
      '.jr-stats{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}' +
      '.jr-chip{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:800;color:#fdba74;background:rgba(234,88,12,.14);border:1px solid rgba(234,88,12,.3);padding:6px 12px;border-radius:999px}' +
      '.jr-chip svg{width:13px;height:13px}' +
      '.jr-chip-mut{color:#cbd5e1;background:rgba(71,85,105,.25);border-color:rgba(148,163,184,.18)}' +
      '.jr-row{display:flex;align-items:center;gap:11px;background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.16);border-radius:11px;padding:11px 13px;margin-bottom:8px}' +
      '.jr-row-done{opacity:.55}' +
      '.jr-cb{width:26px;height:26px;border-radius:8px;border:2px solid rgba(148,163,184,.4);background:transparent;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;color:transparent;padding:0}' +
      '.jr-cb svg{width:15px;height:15px}' +
      '.jr-cb.jr-ck{background:#ea580c;border-color:#ea580c;color:#fff}' +
      '.jr-ref{font-size:14.5px;font-weight:700;color:#f1f5f9;flex:1}' +
      '.jr-hlmeta{font-size:11.5px;color:#94a3b8;font-weight:600}' +
      '.jr-golink{display:flex;align-items:center;gap:5px;color:#fdba74;font-size:12.5px;font-weight:700;text-decoration:none;background:rgba(234,88,12,.12);border:1px solid rgba(234,88,12,.28);padding:6px 11px;border-radius:8px;flex-shrink:0}' +
      '.jr-golink:hover{background:rgba(234,88,12,.2)}' +
      '.jr-golink svg{width:12px;height:12px}' +
      '.jr-done{text-align:center;padding:10px 4px 4px}' +
      '.jr-done svg{width:34px;height:34px;color:#fb923c;margin-bottom:6px}' +
      '.jr-done-t{font-size:15px;font-weight:800;color:#f1f5f9}' +
      '.jr-done-s{font-size:12.5px;color:#94a3b8;line-height:1.5;margin-top:4px;max-width:380px;margin-left:auto;margin-right:auto}' +
      '.jr-done-cb{font-size:12.5px;color:#fdba74;font-weight:600;margin-top:8px}' +
      '.jr-ms{display:flex;align-items:center;gap:10px;background:rgba(234,88,12,.14);border:1px solid rgba(234,88,12,.4);border-radius:11px;padding:12px 14px;margin-bottom:10px}' +
      '.jr-ms svg{width:22px;height:22px;color:#fb923c;flex-shrink:0}' +
      '.jr-ms-t{font-size:11px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:#fdba74}' +
      '.jr-ms-b{font-size:14px;font-weight:700;color:#f1f5f9;margin-top:1px}' +
      '.jr-bar-wrap{height:8px;background:rgba(71,85,105,.3);border-radius:999px;overflow:hidden;margin:10px 0 6px}' +
      '.jr-bar{height:100%;background:#ea580c;border-radius:999px;transition:width .3s}' +
      '.jr-prog-meta{display:flex;justify-content:space-between;font-size:12px;color:#94a3b8;font-weight:600}' +
      '.jr-forecast{font-size:12.5px;color:#fdba74;font-weight:600;margin-top:8px}' +
      '.jr-books{display:grid;grid-template-columns:repeat(auto-fill,minmax(64px,1fr));gap:6px;margin-top:12px}' +
      '.jr-bk{background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.14);border-radius:8px;padding:6px 7px}' +
      '.jr-bk-n{font-size:10.5px;font-weight:700;color:#cbd5e1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '.jr-bk-bar{height:4px;background:rgba(71,85,105,.35);border-radius:999px;margin-top:5px;overflow:hidden}' +
      '.jr-bk-fill{height:100%;background:#ea580c;border-radius:999px}' +
      '.jr-bk-done .jr-bk-n{color:#fdba74}' +
      '.jr-bk-done{border-color:rgba(234,88,12,.4)}' +
      '.jr-note{background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.16);border-radius:11px;padding:12px 13px;margin-bottom:8px}' +
      '.jr-note-meta{display:flex;align-items:center;gap:7px;font-size:12px;color:#94a3b8;margin-bottom:5px}' +
      '.jr-note-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}' +
      '.jr-note-ref{font-weight:700;color:#cbd5e1}' +
      '.jr-note-t{font-size:13.5px;font-weight:700;color:#f1f5f9;margin-bottom:3px}' +
      '.jr-note-x{font-size:12.5px;line-height:1.55;color:#dbe3ef;white-space:pre-wrap;word-break:break-word;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}' +
      '.jr-sub{font-size:12px;color:#94a3b8;line-height:1.5;margin:-4px 0 10px}' +
      '.jr-empty{font-size:12.5px;color:#94a3b8;line-height:1.55}' +
      '.jr-util-row{display:flex;gap:8px;justify-content:flex-end;margin-top:4px}' +
      '.jr-util{background:rgba(71,85,105,.3);border:0;color:#cbd5e1;font-size:12px;font-weight:700;padding:8px 13px;border-radius:8px;cursor:pointer;font-family:inherit}' +
      '.jr-util:hover{background:rgba(71,85,105,.45)}' +
      '.jr-util-danger{color:#fca5a5}' +
      '.jr-confirm{background:rgba(127,29,29,.25);border:1px solid rgba(248,113,113,.35);border-radius:11px;padding:12px 14px;margin-top:10px}' +
      '.jr-confirm p{font-size:13px;color:#fecaca;margin:0 0 10px;line-height:1.5}' +
      '.jr-confirm-row{display:flex;gap:8px;justify-content:flex-end}' +
      '.jr-confirm-yes{background:#dc2626;color:#fff;border:0;font-size:12.5px;font-weight:700;padding:8px 13px;border-radius:8px;cursor:pointer;font-family:inherit}' +
      'body.light .jr-overlay{background:rgba(248,250,252,.97)}' +
      'body.light .jr-head{background:rgba(248,250,252,.97)}' +
      'body.light .jr-sec{background:#fff7ed;border-color:rgba(234,88,12,.25)}' +
      'body.light .jr-opt,body.light .jr-row,body.light .jr-bk,body.light .jr-note,body.light .jr-pace{background:#fff;border-color:rgba(15,23,42,.1)}' +
      'body.light .jr-opt-t,body.light .jr-ref,body.light .jr-note-t,body.light .jr-done-t,body.light .jr-ms-b{color:#0f172a}' +
      'body.light .jr-note-x{color:#1e293b}' +
      'body.light .jr-pace{color:#334155}' +
      'body.light .jr-bk-n{color:#475569}' +
      'body.light .jr-x,body.light .jr-util{background:rgba(71,85,105,.12);color:#334155}';
    var st = document.createElement('style'); st.id = 'jw-reading-style'; st.textContent = css;
    document.head.appendChild(st);
  }

  var BOOK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>';
  var FLAME_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 .5-2 .5-2S6 9 6 13a6 6 0 0 0 12 0c0-5-6-11-6-11z"/></svg>';
  var CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
  var CHECK_RING_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>';
  var EXT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>';
  var TROPHY_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>';

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }

  // ── UI ────────────────────────────────────────────────────────────────
  function renderOnboarding(M) {
    var c = M.container; c.innerHTML = '';
    M.draft = M.draft || { plan: 'canonical', days: 365, perDay: 0 };
    c.appendChild(el('p', 'jr-tagline', t('tagline')));

    var secPlan = el('div', 'jr-sec');
    secPlan.appendChild(el('div', 'jr-sec-t', t('choose_plan')));
    var row = el('div', 'jr-opt-row');
    [['canonical', 'plan_canon', 'plan_canon_d'], ['chrono', 'plan_chrono', 'plan_chrono_d']].forEach(function (p) {
      var o = el('button', 'jr-opt' + (M.draft.plan === p[0] ? ' jr-on' : '')); o.type = 'button';
      o.appendChild(el('div', 'jr-opt-t', t(p[1])));
      o.appendChild(el('div', 'jr-opt-d', t(p[2])));
      o.onclick = function () { M.draft.plan = p[0]; renderOnboarding(M); };
      row.appendChild(o);
    });
    secPlan.appendChild(row);
    c.appendChild(secPlan);

    var secPace = el('div', 'jr-sec');
    secPace.appendChild(el('div', 'jr-sec-t', t('choose_pace')));
    var pr = el('div', 'jr-pace-row');
    [[91, 'pace_3m'], [182, 'pace_6m'], [365, 'pace_1y'], [730, 'pace_2y']].forEach(function (p) {
      var b = el('button', 'jr-pace' + (!M.draft.perDay && M.draft.days === p[0] ? ' jr-on' : ''), t(p[1])); b.type = 'button';
      b.onclick = function () { M.draft.days = p[0]; M.draft.perDay = 0; renderOnboarding(M); };
      pr.appendChild(b);
    });
    var cust = el('button', 'jr-pace' + (M.draft.perDay ? ' jr-on' : ''), t('pace_custom')); cust.type = 'button';
    cust.onclick = function () { M.draft.perDay = M.draft.perDay || 3; renderOnboarding(M); };
    pr.appendChild(cust);
    secPace.appendChild(pr);
    if (M.draft.perDay) {
      var cr = el('div', 'jr-custom');
      var inp = document.createElement('input'); inp.type = 'number'; inp.min = '1'; inp.max = '99'; inp.value = M.draft.perDay;
      var perDayLbl = el('span', null, tf('per_day', { n: M.draft.perDay }));
      inp.oninput = function () { var v = parseInt(inp.value, 10); if (v >= 1 && v <= 99) { M.draft.perDay = v; perDayLbl.textContent = tf('per_day', { n: v }); note.textContent = finishNote(); } };
      cr.appendChild(inp);
      cr.appendChild(perDayLbl);
      secPace.appendChild(cr);
    }
    function finishNote() {
      var rate = M.draft.perDay ? M.draft.perDay : TOTAL / M.draft.days;
      return tf('finish_by', { d: fmtDate(addDays(today(), Math.ceil(TOTAL / rate))) });
    }
    var note = el('div', 'jr-finish-note', finishNote());
    secPace.appendChild(note);
    c.appendChild(secPace);

    var start = el('button', 'jr-start', t('start')); start.type = 'button';
    start.onclick = function () {
      var s = store();
      s.plan = M.draft.plan;
      if (M.draft.perDay) { s.perDay = M.draft.perDay; delete s.days; } else { s.days = M.draft.days; delete s.perDay; }
      s.start = today(); s.daysDone = s.daysDone || 0;
      save(s);
      renderActive(M);
      updateHomeCard();
    };
    c.appendChild(start);
  }

  function statChips(s) {
    var wrap = el('div', 'jr-stats');
    if (s.streak > 0) {
      var chip = el('div', 'jr-chip'); chip.innerHTML = FLAME_SVG;
      chip.appendChild(el('span', null, tf('streak_days', { n: s.streak })));
      wrap.appendChild(chip);
    }
    var pct = Math.floor(readCount(s) / TOTAL * 100);
    wrap.appendChild(el('div', 'jr-chip jr-chip-mut', pct + '%'));
    return wrap;
  }

  function renderActive(M) {
    var c = M.container; c.innerHTML = '';
    var s = store(), td = today();
    var info = todayInfo(s, td);

    c.appendChild(statChips(s));

    // milestone banners (freshly hit, dismissed on next render)
    (M.justHit || []).forEach(function (key) {
      var ms = el('div', 'jr-ms'); ms.innerHTML = TROPHY_SVG;
      var col = el('div');
      col.appendChild(el('div', 'jr-ms-t', t('ms_t')));
      var label = key === 'hebrew' ? t('ms_hebrew') : key === 'greek' ? t('ms_greek') : key === 'all' ? t('ms_all') :
        tf('ms_book', { b: BOOKS[parseInt(key.slice(1), 10) - 1] });
      col.appendChild(el('div', 'jr-ms-b', label));
      ms.appendChild(col);
      c.appendChild(ms);
    });
    M.justHit = [];

    var sec = el('div', 'jr-sec');
    sec.appendChild(el('div', 'jr-sec-t', t('today')));
    if (info.finished) {
      var fin = el('div', 'jr-done');
      var ic = document.createElement('div'); ic.innerHTML = TROPHY_SVG; fin.appendChild(ic.firstChild);
      fin.appendChild(el('div', 'jr-done-t', t('finished_t')));
      fin.appendChild(el('div', 'jr-done-s', t('finished_s')));
      sec.appendChild(fin);
    } else if (info.done) {
      var dn = el('div', 'jr-done');
      var ic2 = document.createElement('div'); ic2.innerHTML = CHECK_RING_SVG; dn.appendChild(ic2.firstChild);
      dn.appendChild(el('div', 'jr-done-t', t('done_t')));
      dn.appendChild(el('div', 'jr-done-s', t('done_s')));
      dn.appendChild(el('div', 'jr-done-cb', t('come_back')));
      sec.appendChild(dn);
    } else {
      info.rows.forEach(function (rc) {
        var b = rc[0], ch = rc[1], key = b + ':' + ch;
        var row = el('div', 'jr-row' + (s.read[key] ? ' jr-row-done' : ''));
        var cb = el('button', 'jr-cb' + (s.read[key] ? ' jr-ck' : '')); cb.type = 'button'; cb.innerHTML = CHECK_SVG;
        cb.setAttribute('aria-label', BOOKS[b - 1] + ' ' + ch);
        cb.onclick = function () {
          var st = store();
          M.justHit = markRead(st, b, ch, today());
          save(st);
          if (window.__jwHaptic) { try { window.__jwHaptic(12); } catch (_) {} }
          renderActive(M);
          updateHomeCard();
        };
        row.appendChild(cb);
        row.appendChild(el('div', 'jr-ref', BOOKS[b - 1] + ' ' + ch));
        var hn = LIB.hls[key];
        if (hn) row.appendChild(el('span', 'jr-hlmeta', tf('hl_n', { n: hn })));
        var a = el('a', 'jr-golink'); a.href = chapterUrl(b, ch); a.target = '_blank'; a.rel = 'noopener';
        a.appendChild(el('span', null, t('read'))); a.insertAdjacentHTML('beforeend', EXT_SVG);
        row.appendChild(a);
        sec.appendChild(row);
      });
    }
    c.appendChild(sec);

    // Your notes on today's chapters
    var noteSec = el('div', 'jr-sec');
    noteSec.appendChild(el('div', 'jr-sec-t', t('your_notes')));
    noteSec.appendChild(el('p', 'jr-sub', t('your_notes_s')));
    var host = el('div'); host.setAttribute('data-jr-notes', '1');
    noteSec.appendChild(host);
    c.appendChild(noteSec);
    fillNotes(M, host, info.rows);

    // Progress
    var prog = el('div', 'jr-sec');
    prog.appendChild(el('div', 'jr-sec-t', t('progress')));
    var read = readCount(s);
    var barW = el('div', 'jr-bar-wrap'); var bar = el('div', 'jr-bar'); bar.style.width = (read / TOTAL * 100).toFixed(1) + '%';
    barW.appendChild(bar); prog.appendChild(barW);
    var meta = el('div', 'jr-prog-meta');
    meta.appendChild(el('span', null, tf('chapters_read', { a: read, b: TOTAL })));
    meta.appendChild(el('span', null, Math.floor(read / TOTAL * 100) + '%'));
    prog.appendChild(meta);
    if (!info.finished) prog.appendChild(el('div', 'jr-forecast', tf('forecast', { d: fmtDate(forecast(s, td)) })));
    var grid = el('div', 'jr-books');
    for (var i = 0; i < 66; i++) {
      var got = 0;
      for (var ch2 = 1; ch2 <= CHAP[i]; ch2++) if (s.read[(i + 1) + ':' + ch2]) got++;
      var bk = el('div', 'jr-bk' + (got === CHAP[i] ? ' jr-bk-done' : ''));
      bk.title = BOOKS[i] + ' — ' + got + '/' + CHAP[i];
      bk.appendChild(el('div', 'jr-bk-n', ABBR[i]));
      var bb = el('div', 'jr-bk-bar'); var bf = el('div', 'jr-bk-fill'); bf.style.width = (got / CHAP[i] * 100) + '%';
      bb.appendChild(bf); bk.appendChild(bb);
      grid.appendChild(bk);
    }
    prog.appendChild(grid);
    c.appendChild(prog);

    // utilities
    var util = el('div', 'jr-util-row');
    var chg = el('button', 'jr-util', t('change')); chg.type = 'button';
    chg.onclick = function () { M.draft = { plan: s.plan || 'canonical', days: s.days || 365, perDay: s.perDay || 0 }; renderOnboarding(M); };
    util.appendChild(chg);
    var rst = el('button', 'jr-util jr-util-danger', t('reset')); rst.type = 'button';
    rst.onclick = function () {
      if (c.querySelector('.jr-confirm')) return;
      var box = el('div', 'jr-confirm');
      box.appendChild(el('p', null, t('reset_c')));
      var cr = el('div', 'jr-confirm-row');
      var no = el('button', 'jr-util', t('cancel')); no.type = 'button'; no.onclick = function () { box.remove(); };
      var yes = el('button', 'jr-confirm-yes', t('confirm')); yes.type = 'button';
      yes.onclick = function () { try { localStorage.removeItem(SKEY); } catch (_) {} renderOnboarding(M); updateHomeCard(); };
      cr.appendChild(no); cr.appendChild(yes); box.appendChild(cr);
      c.appendChild(box);
    };
    util.appendChild(rst);
    c.appendChild(util);
  }

  function fillNotes(M, host, rows) {
    function paint() {
      host.innerHTML = '';
      if (!LIB.loaded) { host.appendChild(el('p', 'jr-empty', t('notes_hint'))); return; }
      var keys = {};
      (rows || []).forEach(function (rc) { keys[rc[0] + ':' + rc[1]] = 1; });
      var hits = LIB.notes.filter(function (n) { return keys[n.b + ':' + n.c]; }).slice(0, 12);
      if (!hits.length) { host.appendChild(el('p', 'jr-empty', t('notes_none'))); return; }
      hits.forEach(function (n) {
        var card = el('div', 'jr-note');
        var meta = el('div', 'jr-note-meta');
        if (n.color && HLC[n.color]) { var dot = el('span', 'jr-note-dot'); dot.style.background = HLC[n.color]; meta.appendChild(dot); }
        meta.appendChild(el('span', 'jr-note-ref', BOOKS[n.b - 1] + ' ' + n.c));
        card.appendChild(meta);
        if (n.title) card.appendChild(el('div', 'jr-note-t', n.title));
        if (n.text) card.appendChild(el('div', 'jr-note-x', n.text));
        host.appendChild(card);
      });
    }
    paint();
    // First load: once the library arrives, repaint the whole active view so
    // the per-chapter highlight badges show up too (guarded: only while the
    // active view is still on screen).
    if (!LIB.loaded) loadLibrary().then(function () {
      if (LIB.loaded && host.isConnected && store().plan) renderActive(M);
    });
  }

  function mount(container) {
    if (!container) return null;
    injectStyle();
    var M = { container: container, justHit: [] };
    var s = store();
    if (s.plan) renderActive(M); else renderOnboarding(M);
    return M;
  }

  // ── overlay ───────────────────────────────────────────────────────────
  var overlay = null;
  function close() {
    if (!overlay) return;
    overlay.remove(); overlay = null;
    try { document.body.style.overflow = ''; } catch (_) {}
    document.removeEventListener('keydown', onKey);
    updateHomeCard();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }
  function open() {
    if (overlay) return;
    injectStyle();
    overlay = el('div', 'jr-overlay');
    overlay.setAttribute('role', 'dialog'); overlay.setAttribute('aria-modal', 'true');
    var wrap = el('div', 'jr-wrap');
    var head = el('div', 'jr-head');
    var ttl = el('div', 'jr-ttl'); ttl.innerHTML = BOOK_SVG; ttl.appendChild(el('span', null, t('brand')));
    head.appendChild(ttl);
    var x = el('button', 'jr-x', t('close')); x.type = 'button'; x.onclick = close;
    head.appendChild(x);
    wrap.appendChild(head);
    var body = el('div');
    wrap.appendChild(body);
    overlay.appendChild(wrap);
    document.body.appendChild(overlay);
    try { document.body.style.overflow = 'hidden'; } catch (_) {}
    document.addEventListener('keydown', onKey);
    mount(body);
  }

  // ── landing tool card live state ──────────────────────────────────────
  function updateHomeCard() {
    var live = document.getElementById('jw-reading-live');
    if (!live) return;
    var tags = live.querySelectorAll('.svc-tag');
    if (tags.length < 2) return;
    var s = store();
    if (!s.plan) return; // keep the translated default tags
    var info = todayInfo(s, today());
    if (info.finished) { tags[0].textContent = t('finished_t'); }
    else if (info.done) { tags[0].textContent = t('done_t'); }
    else { tags[0].textContent = tf('card_today', { r: portionLabel(info.rows) }); }
    tags[1].textContent = (s.streak > 0) ? tf('streak_days', { n: s.streak }) : (Math.floor(readCount(s) / TOTAL * 100) + '%');
  }

  window.JwReading = {
    open: open,
    close: close,
    mount: mount,
    updateHomeCard: updateHomeCard,
    _libraryFromDb: libraryFromDb,
    _engine: {
      BOOKS: BOOKS, ABBR: ABBR, CHAP: CHAP, TOTAL: TOTAL, CHRONO: CHRONO,
      seqFor: seqFor, rateFor: rateFor, readCount: readCount, remainingSeq: remainingSeq,
      todayInfo: todayInfo, forecast: forecast, markRead: markRead, bookDone: bookDone,
      portionLabel: portionLabel, addDays: addDays, chapterUrl: chapterUrl,
      store: store, save: save, SKEY: SKEY
    }
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', updateHomeCard);
  else updateHomeCard();
})();

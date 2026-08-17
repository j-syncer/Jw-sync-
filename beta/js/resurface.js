/*!
 * JW Sync — Resurface engine (shared)
 * A small, embeddable "daily review" of the user's own past notes.
 * Mounts an inline panel into a host element (the merge celebration card and
 * the Study Stats page). No overlay, no standalone tool. All on-device.
 *
 * Public API (window.JwResurface):
 *   mount(container, { notes })  -> renders the inline review panel
 *   notesFromDb(sqlJsDb)         -> normalized note array (synchronous)
 *   notesFromBuffer(arrayBuffer) -> Promise<note array>  (uses JSZip + sql.js)
 *
 * Review state (streak + spaced repetition) lives in localStorage key
 * jwsync_resurface_v1 and is shared across both surfaces.
 */
(function () {
  'use strict';
  if (window.JwResurface) return;

  // ── i18n (12 languages) ───────────────────────────────────────────────
  var I18N = {
    en: { brand: 'Resurface', on_this_day: 'On this day', w_years: 'Written {n} years ago', w_year: 'Written a year ago', w_months: 'Written {n} months ago', w_month: 'Written last month', w_recent: 'Written recently', count_sep: 'of', reflect: 'Mark reviewed', next: 'Next', done_title: "You're all caught up", done_sub: "You've reviewed today's notes. A little, often, is how study sticks.", come_back: 'Come back tomorrow for more.', streak_days: '{n}-day streak' },
    es: { brand: 'Recuperar', on_this_day: 'Tal día como hoy', w_years: 'Escrita hace {n} años', w_year: 'Escrita hace un año', w_months: 'Escrita hace {n} meses', w_month: 'Escrita el mes pasado', w_recent: 'Escrita hace poco', count_sep: 'de', reflect: 'Marcar como repasada', next: 'Siguiente', done_title: 'Estás al día', done_sub: 'Has repasado las notas de hoy. Un poco cada día es lo que hace que el estudio perdure.', come_back: 'Vuelve mañana para más.', streak_days: 'Racha de {n} días' },
    pt: { brand: 'Reviver', on_this_day: 'Neste dia', w_years: 'Escrita há {n} anos', w_year: 'Escrita há um ano', w_months: 'Escrita há {n} meses', w_month: 'Escrita no mês passado', w_recent: 'Escrita recentemente', count_sep: 'de', reflect: 'Marcar como revisada', next: 'Próxima', done_title: 'Você está em dia', done_sub: 'Você revisou as notas de hoje. Um pouco, com frequência, é o que fixa o estudo.', come_back: 'Volte amanhã para mais.', streak_days: 'Sequência de {n} dias' },
    fr: { brand: 'Resurgir', on_this_day: 'Ce jour-là', w_years: 'Écrite il y a {n} ans', w_year: 'Écrite il y a un an', w_months: 'Écrite il y a {n} mois', w_month: 'Écrite le mois dernier', w_recent: 'Écrite récemment', count_sep: 'sur', reflect: 'Marquer comme revue', next: 'Suivante', done_title: 'Vous êtes à jour', done_sub: "Vous avez revu les notes du jour. Un peu, souvent : c'est ainsi que l'étude s'ancre.", come_back: 'Revenez demain pour la suite.', streak_days: 'Série de {n} jours' },
    de: { brand: 'Rückblick', on_this_day: 'An diesem Tag', w_years: 'Vor {n} Jahren geschrieben', w_year: 'Vor einem Jahr geschrieben', w_months: 'Vor {n} Monaten geschrieben', w_month: 'Letzten Monat geschrieben', w_recent: 'Kürzlich geschrieben', count_sep: 'von', reflect: 'Als wiederholt markieren', next: 'Weiter', done_title: 'Du bist auf dem neuesten Stand', done_sub: 'Du hast die heutigen Notizen wiederholt. Wenig, aber regelmäßig — so bleibt das Studium haften.', come_back: 'Komm morgen für mehr wieder.', streak_days: '{n}-Tage-Serie' },
    it: { brand: 'Riscopri', on_this_day: 'In questo giorno', w_years: 'Scritta {n} anni fa', w_year: 'Scritta un anno fa', w_months: 'Scritta {n} mesi fa', w_month: 'Scritta il mese scorso', w_recent: 'Scritta di recente', count_sep: 'di', reflect: 'Segna come ripassata', next: 'Avanti', done_title: 'Sei in pari', done_sub: 'Hai ripassato le note di oggi. Poco e spesso: così lo studio resta.', come_back: 'Torna domani per altre.', streak_days: 'Serie di {n} giorni' },
    ru: { brand: 'Вспомнить', on_this_day: 'В этот день', w_years: 'Написано {n} лет назад', w_year: 'Написано год назад', w_months: 'Написано {n} месяцев назад', w_month: 'Написано в прошлом месяце', w_recent: 'Написано недавно', count_sep: 'из', reflect: 'Отметить просмотренным', next: 'Далее', done_title: 'Вы всё просмотрели', done_sub: 'Вы просмотрели сегодняшние заметки. Понемногу, но регулярно — так изучение закрепляется.', come_back: 'Возвращайтесь завтра за новым.', streak_days: 'Серия {n} дней' },
    ja: { brand: 'リサーフェス', on_this_day: 'この日に', w_years: '{n}年前に作成', w_year: '1年前に作成', w_months: '{n}か月前に作成', w_month: '先月作成', w_recent: '最近作成', count_sep: '/', reflect: '確認済みにする', next: '次へ', done_title: '今日の分は完了です', done_sub: '今日のノートを振り返りました。少しずつ続けることで研究が身につきます。', come_back: 'また明日来てください。', streak_days: '{n}日連続' },
    ko: { brand: '되살리기', on_this_day: '오늘 이날', w_years: '{n}년 전 작성', w_year: '1년 전 작성', w_months: '{n}개월 전 작성', w_month: '지난달 작성', w_recent: '최근 작성', count_sep: '/', reflect: '복습 완료로 표시', next: '다음', done_title: '오늘 분량을 마쳤습니다', done_sub: '오늘의 노트를 복습했습니다. 조금씩 꾸준히 하는 것이 연구를 오래 남게 합니다.', come_back: '내일 다시 오세요.', streak_days: '{n}일 연속' },
    tl: { brand: 'Balikan', on_this_day: 'Sa araw na ito', w_years: 'Isinulat {n} taon na ang nakalipas', w_year: 'Isinulat isang taon na ang nakalipas', w_months: 'Isinulat {n} buwan na ang nakalipas', w_month: 'Isinulat noong nakaraang buwan', w_recent: 'Kamakailang isinulat', count_sep: 'sa', reflect: 'Markahan bilang nasuri', next: 'Susunod', done_title: 'Nakahabol ka na', done_sub: 'Nasuri mo na ang mga tala ngayong araw. Kaunti pero madalas — ganito tumatagal ang pag-aaral.', come_back: 'Bumalik bukas para sa iba pa.', streak_days: '{n}-araw na sunod-sunod' },
    sv: { brand: 'Återblick', on_this_day: 'På denna dag', w_years: 'Skriven för {n} år sedan', w_year: 'Skriven för ett år sedan', w_months: 'Skriven för {n} månader sedan', w_month: 'Skriven förra månaden', w_recent: 'Skriven nyligen', count_sep: 'av', reflect: 'Markera som repeterad', next: 'Nästa', done_title: 'Du är ikapp', done_sub: 'Du har repeterat dagens anteckningar. Lite men ofta — så fastnar studierna.', come_back: 'Kom tillbaka i morgon för mer.', streak_days: '{n} dagar i rad' },
    ceb: { brand: 'Balikan', on_this_day: 'Niini nga adlaw', w_years: 'Gisulat {n} ka tuig na ang milabay', w_year: 'Gisulat usa ka tuig na ang milabay', w_months: 'Gisulat {n} ka bulan na ang milabay', w_month: 'Gisulat niadtong miaging bulan', w_recent: 'Bag-o lang gisulat', count_sep: 'sa', reflect: 'Markahi nga nasusi', next: 'Sunod', done_title: 'Naapsan na nimo', done_sub: 'Nasusi na nimo ang mga nota karong adlawa. Gamay apan kanunay — mao kini ang paagi nga magpabilin ang pagtuon.', come_back: 'Balik ugma para sa dugang.', streak_days: '{n} ka adlaw nga sunod-sunod' },sw:{brand:"Kumbusho",on_this_day:"Siku kama ya leo",w_years:"Liliandikwa miaka {n} iliyopita",w_year:"Liliandikwa mwaka mmoja uliopita",w_months:"Liliandikwa miezi {n} iliyopita",w_month:"Liliandikwa mwezi uliopita",w_recent:"Liliandikwa hivi karibuni",count_sep:"kati ya",reflect:"Weka alama kuwa umepitia",next:"Ifuatayo",done_title:"Umemaliza yote",done_sub:"Umepitia madokezo ya leo. Kidogo, mara kwa mara, ndiyo njia ya funzo kubaki akilini.",come_back:"Rudi kesho kwa mengine zaidi.",streak_days:"Mfululizo wa siku {n}"},nl:{brand:"Weer in beeld",on_this_day:"Op deze dag",w_years:"{n} jaar geleden geschreven",w_year:"Een jaar geleden geschreven",w_months:"{n} maanden geleden geschreven",w_month:"Vorige maand geschreven",w_recent:"Onlangs geschreven",count_sep:"van",reflect:"Markeren als bekeken",next:"Volgende",done_title:"Je bent helemaal bij",done_sub:"Je hebt de aantekeningen van vandaag bekeken. Een beetje, maar vaak — zo blijft studie hangen.",come_back:"Kom morgen terug voor meer.",streak_days:"Reeks van {n} dagen"},ro:{brand:"Readuse în față",on_this_day:"În această zi",w_years:"Scrisă acum {n} ani",w_year:"Scrisă acum un an",w_months:"Scrisă acum {n} luni",w_month:"Scrisă luna trecută",w_recent:"Scrisă recent",count_sep:"din",reflect:"Marchează ca recitită",next:"Următoarea",done_title:"Ai terminat tot",done_sub:"Ai recitit notițele de azi. Câte puțin, dar des — așa rămâne studiul cu tine.",come_back:"Revino mâine pentru altele.",streak_days:"Serie de {n} zile"},id:{brand:"Munculkan Lagi",on_this_day:"Pada hari ini",w_years:"Ditulis {n} tahun lalu",w_year:"Ditulis setahun lalu",w_months:"Ditulis {n} bulan lalu",w_month:"Ditulis bulan lalu",w_recent:"Baru saja ditulis",count_sep:"dari",reflect:"Tandai sudah ditinjau",next:"Berikutnya",done_title:"Semua sudah selesai",done_sub:"Anda sudah meninjau catatan hari ini. Sedikit demi sedikit, tapi rutin — begitulah pelajaran melekat.",come_back:"Kembalilah besok untuk lebih banyak lagi.",streak_days:"Rentetan {n} hari"},hi:{brand:"फिर से देखें",on_this_day:"आज के दिन",w_years:"{n} साल पहले लिखा",w_year:"एक साल पहले लिखा",w_months:"{n} महीने पहले लिखा",w_month:"पिछले महीने लिखा",w_recent:"हाल ही में लिखा",count_sep:"/",reflect:"देखा हुआ चिह्नित करें",next:"आगे",done_title:"आपने सब देख लिया",done_sub:"आपने आज के नोट देख लिए। थोड़ा-थोड़ा, बार-बार — इसी तरह अध्ययन याद रहता है।",come_back:"कल फिर आइए।",streak_days:"{n} दिन की लड़ी"},hu:{brand:"Felidézés",on_this_day:"A mai napon",w_years:"{n} éve írtad",w_year:"Egy éve írtad",w_months:"{n} hónapja írtad",w_month:"Múlt hónapban írtad",w_recent:"Nemrég írtad",count_sep:"/",reflect:"Átnézettnek jelöl",next:"Tovább",done_title:"Mindent átnéztél",done_sub:"Átnézted a mai jegyzeteket. Keveset, de gyakran — így marad meg a tanulmányozás.",come_back:"Gyere vissza holnap még többért.",streak_days:"{n} napos sorozat"},vi:{brand:"Ôn lại",on_this_day:"Ngày này năm xưa",w_years:"Viết cách đây {n} năm",w_year:"Viết cách đây một năm",w_months:"Viết cách đây {n} tháng",w_month:"Viết tháng trước",w_recent:"Mới viết gần đây",count_sep:"trong",reflect:"Đánh dấu đã ôn",next:"Tiếp",done_title:"Bạn đã ôn xong hết rồi",done_sub:"Bạn đã ôn lại các ghi chú hôm nay. Ít một, nhưng đều đặn — đó là cách việc học hỏi đọng lại.",come_back:"Ngày mai quay lại để ôn tiếp nhé.",streak_days:"Chuỗi {n} ngày"},"yue-Hant":{brand:"重溫",on_this_day:"今日呢一日",w_years:"{n} 年前寫嘅",w_year:"一年前寫嘅",w_months:"{n} 個月前寫嘅",w_month:"上個月寫嘅",w_recent:"最近先寫嘅",count_sep:"/",reflect:"標記為已重溫",next:"下一條",done_title:"今日嘅重溫做完喇",done_sub:"你已經重溫咗今日嘅筆記。每次少少、經常做，學到嘅嘢先至記得住。",come_back:"聽日再返嚟睇多啲。",streak_days:"連續 {n} 日"},"zh-Hant":{brand:"回顧",on_this_day:"歷史上的今天",w_years:"寫於 {n} 年前",w_year:"寫於一年前",w_months:"寫於 {n} 個月前",w_month:"寫於上個月",w_recent:"最近寫的",count_sep:"/",reflect:"標記為已回顧",next:"下一條",done_title:"今天的回顧已完成",done_sub:"你已回顧完今天的筆記。少量而經常，學到的才留得住。",come_back:"明天再來看更多。",streak_days:"連續 {n} 天"},"zh-Hans":{brand:"回顾",on_this_day:"历史上的今天",w_years:"写于 {n} 年前",w_year:"写于一年前",w_months:"写于 {n} 个月前",w_month:"写于上个月",w_recent:"最近写的",count_sep:"/",reflect:"标记为已回顾",next:"下一条",done_title:"今天的回顾已完成",done_sub:"你已回顾完今天的笔记。少量而经常，学到的才留得住。",come_back:"明天再来看更多。",streak_days:"连续 {n} 天"},pl:{brand:"Przypomnienie",on_this_day:"Tego dnia",w_years:"Napisano {n} lat temu",w_year:"Napisano rok temu",w_months:"Napisano {n} miesięcy temu",w_month:"Napisano w zeszłym miesiącu",w_recent:"Napisano niedawno",count_sep:"z",reflect:"Oznacz jako przejrzane",next:"Dalej",done_title:"Wszystko przejrzane",done_sub:"Przejrzałeś dzisiejsze notatki. Po trochu, ale regularnie — tak wiedza zostaje na dłużej.",come_back:"Wróć jutro po kolejne.",streak_days:"Passa: {n} dni"},uk:{brand:"Пригадати",on_this_day:"Цього дня",w_years:"Написано {n} років тому",w_year:"Написано рік тому",w_months:"Написано {n} місяців тому",w_month:"Написано минулого місяця",w_recent:"Написано нещодавно",count_sep:"з",reflect:"Позначити як переглянуте",next:"Далі",done_title:"Ви все переглянули",done_sub:"Ви переглянули сьогоднішні нотатки. Потроху, але регулярно — саме так знання залишаються.",come_back:"Повертайтеся завтра по нові.",streak_days:"Серія: {n} днів"},he:{brand:"ריענון",on_this_day:"ביום הזה",w_years:"נכתבה לפני {n} שנים",w_year:"נכתבה לפני שנה",w_months:"נכתבה לפני {n} חודשים",w_month:"נכתבה בחודש שעבר",w_recent:"נכתבה לאחרונה",count_sep:"מתוך",reflect:"סימון כנצפה",next:"הבא",done_title:"סיימתם להיום",done_sub:"עברתם על ההערות של היום. קצת, לעיתים קרובות — כך הלימוד נשאר.",come_back:"חזרו מחר להמשך.",streak_days:"רצף של {n} ימים"},ar:{brand:"استعادة",on_this_day:"في مثل هذا اليوم",w_years:"كُتبت قبل {n} سنوات",w_year:"كُتبت قبل سنة",w_months:"كُتبت قبل {n} أشهر",w_month:"كُتبت الشهر الماضي",w_recent:"كُتبت مؤخرًا",count_sep:"من",reflect:"علّمها كمُراجَعة",next:"التالي",done_title:"أنهيت كل شيء",done_sub:"راجعت ملاحظات اليوم. القليل المتكرّر هو ما يجعل الدرس يرسخ.",come_back:"عُد غدًا للمزيد.",streak_days:"سلسلة {n} أيام"}
  };
  function lang() { try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; } }
  function t(k) { var L = I18N[lang()] || I18N.en; return (L && L[k] != null) ? L[k] : (I18N.en[k] != null ? I18N.en[k] : k); }

  var BIBLE = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"];
  var HLC = { 1: '#fde68a', 2: '#bbf7d0', 3: '#bfdbfe', 4: '#fbcfe8', 5: '#fed7aa', 6: '#e9d5ff' };
  var SQL_BASE = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';
  var IV = [1, 3, 7, 16, 35, 75, 150];
  var SKEY = 'jwsync_resurface_v1';
  var TARGET = 3;

  // ── persistent review state ───────────────────────────────────────────
  function store() { var s = {}; try { s = JSON.parse(localStorage.getItem(SKEY)) || {}; } catch (_) { s = {}; } s.sched = s.sched || {}; s.seen = s.seen || {}; return s; }
  function save(s) { try { localStorage.setItem(SKEY, JSON.stringify(s)); } catch (_) {} }

  // ── date helpers (local) ──────────────────────────────────────────────
  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function dstr(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
  function today() { return dstr(new Date()); }
  function addDays(ds, n) { var d = new Date(ds + 'T00:00:00'); d.setDate(d.getDate() + n); return dstr(d); }
  function parseDate(s) { if (!s) return null; var d = new Date(String(s).replace(' ', 'T')); return isNaN(d.getTime()) ? null : d; }
  function hash(s) { var h = 0; for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; } return h >>> 0; }

  function htmlToText(html) {
    if (!html) return '';
    var s = String(html).replace(/<\s*(br|\/p|\/div|\/li|\/h[1-6])[^>]*>/gi, '\n').replace(/<\s*li[^>]*>/gi, '• ').replace(/<[^>]+>/g, '');
    var ta = document.createElement('textarea'); ta.innerHTML = s; s = ta.value;
    return s.replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
  }
  function refLabel(r) { var bn = r.BookNumber, ch = r.ChapterNumber; if (bn && bn >= 1 && bn <= 66) { var nm = BIBLE[bn - 1] || ('Book ' + bn); return ch ? (nm + ' ' + ch) : nm; } return r.LocTitle || r.KeySymbol || ''; }
  function otdYears(created) { var d = parseDate(created); if (!d) return 0; var now = new Date(); if (d.getMonth() === now.getMonth() && d.getDate() === now.getDate() && d.getFullYear() < now.getFullYear()) return now.getFullYear() - d.getFullYear(); return 0; }
  function agoLabel(created) {
    var d = parseDate(created); if (!d) return '';
    var now = new Date();
    var months = (now.getFullYear() - d.getFullYear()) * 12 + (now.getMonth() - d.getMonth());
    if (now.getDate() < d.getDate()) months--;
    if (months < 1) return t('w_recent');
    if (months < 12) return months === 1 ? t('w_month') : t('w_months').replace('{n}', months);
    var y = Math.floor(months / 12);
    return y === 1 ? t('w_year') : t('w_years').replace('{n}', y);
  }

  // ── data extraction ───────────────────────────────────────────────────
  function execRows(db, sql) { try { var r = db.exec(sql); if (!r[0]) return []; var cols = r[0].columns; return r[0].values.map(function (v) { var o = {}; for (var i = 0; i < cols.length; i++) o[cols[i]] = v[i]; return o; }); } catch (_) { return []; } }
  function notesFromDb(db) {
    if (!db) return [];
    var raw = execRows(db,
      "SELECT n.Guid, n.Title, n.Content, n.Created, n.LastModified, n.UserMarkId, " +
      "l.BookNumber, l.ChapterNumber, l.KeySymbol, l.Title AS LocTitle, u.ColorIndex " +
      "FROM Note n LEFT JOIN Location l ON n.LocationId=l.LocationId " +
      "LEFT JOIN UserMark u ON n.UserMarkId=u.UserMarkId");
    return raw.map(function (r) {
      var created = r.Created || r.LastModified || '';
      return { guid: r.Guid || ('x' + Math.random()), title: (r.Title || '').trim(), text: htmlToText(r.Content || ''), created: created, ref: refLabel(r), color: r.ColorIndex || 0, otdYears: otdYears(created) };
    }).filter(function (n) { return (n.text && n.text.length) || (n.title && n.title.length); });
  }
  function notesFromBuffer(buf) {
    if (!window.JSZip || !window.initSqlJs || !buf) return Promise.resolve([]);
    return new window.JSZip().loadAsync(buf).then(function (zip) {
      var nm = Object.keys(zip.files).find(function (n) { return /userdata\.db$/i.test(n); });
      if (!nm) throw new Error('no db');
      return zip.files[nm].async('uint8array');
    }).then(function (bytes) {
      return window.initSqlJs({ locateFile: function (f) { return SQL_BASE + f; } }).then(function (SQL) {
        var db = new SQL.Database(bytes); var ns = notesFromDb(db); try { db.close(); } catch (_) {} return ns;
      });
    }).catch(function () { return []; });
  }

  // ── spaced repetition + streak ────────────────────────────────────────
  function scheduleNext(st, n) {
    var s = st.sched[n.guid] || { reps: 0 };
    var i = Math.min(s.reps || 0, IV.length - 1);
    s.due = addDays(today(), IV[i]);
    s.reps = (s.reps || 0) + 1;
    st.sched[n.guid] = s;
  }
  function maybeStreak(st) {
    var td = today();
    if ((st.dayDone || 0) >= (st.dayTarget || 0) && st.streakDate !== td) {
      var y = addDays(td, -1);
      st.streak = (st.streakDate === y) ? ((st.streak || 0) + 1) : 1;
      st.streakDate = td;
      st.longest = Math.max(st.longest || 0, st.streak);
    }
  }

  // ── deck building ─────────────────────────────────────────────────────
  function buildDeck(M) {
    var st = store(), td = today();
    if (st.dayDate !== td) { st.dayDate = td; st.dayDone = 0; st.dayTarget = 0; st.dayBuilt = false; }
    function seenToday(n) { return st.seen[n.guid] === td; }
    var pool = M.notes.filter(function (n) { return !seenToday(n); });
    var otd = pool.filter(function (n) { return n.otdYears > 0; }).sort(function (a, b) { return b.otdYears - a.otdYears; });
    var due = pool.filter(function (n) { var s = st.sched[n.guid]; return n.otdYears <= 0 && s && s.due && s.due <= td; });
    var chosen = [], ids = {};
    function push(n) { if (!ids[n.guid]) { ids[n.guid] = 1; chosen.push(n); } }
    otd.slice(0, TARGET).forEach(push);
    due.forEach(push);
    if (chosen.length < TARGET) {
      var rest = pool.filter(function (n) { return !ids[n.guid]; });
      rest.sort(function (a, b) { var sa = st.seen[a.guid] || '', sb = st.seen[b.guid] || ''; if (sa !== sb) return sa < sb ? -1 : 1; return hash(a.guid + td) - hash(b.guid + td); });
      for (var i = 0; i < rest.length && chosen.length < TARGET; i++) push(rest[i]);
    }
    M.deck = chosen;
    if (!st.dayBuilt) { st.dayTarget = chosen.length; st.dayBuilt = true; save(st); }
  }

  // ── styles (injected once) ────────────────────────────────────────────
  function injectStyle() {
    if (document.getElementById('jw-resurface-style')) return;
    var css = '' +
      '.rsp-panel{font-family:Inter,system-ui,sans-serif;background:rgba(15,28,52,.55);border:1px solid rgba(234,88,12,.28);border-radius:14px;padding:14px 16px 16px;margin:14px 0;text-align:left}' +
      '.rsp-top{display:flex;align-items:center;gap:8px;margin-bottom:10px}' +
      '.rsp-ttl{display:flex;align-items:center;gap:7px;font-weight:800;font-size:14px;color:#fdba74;letter-spacing:.2px}' +
      '.rsp-ttl svg{width:17px;height:17px;color:#fb923c}' +
      '.rsp-streak{margin-left:auto;display:flex;align-items:center;gap:5px;font-weight:800;font-size:12px;color:#fdba74;background:rgba(234,88,12,.14);border:1px solid rgba(234,88,12,.3);padding:3px 9px;border-radius:999px}' +
      '.rsp-streak svg{width:13px;height:13px}' +
      '.rsp-card{background:rgba(4,12,28,.45);border:1px solid rgba(148,163,184,.16);border-radius:11px;padding:13px 14px}' +
      '.rsp-badge{display:inline-block;font-size:10.5px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:#fdba74;background:rgba(234,88,12,.16);padding:3px 8px;border-radius:5px;margin-bottom:9px}' +
      '.rsp-meta{display:flex;align-items:center;gap:7px;margin-bottom:6px;font-size:12.5px;color:#94a3b8}' +
      '.rsp-dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;box-shadow:0 0 0 1px rgba(0,0,0,.2) inset}' +
      '.rsp-ref{font-weight:600;color:#cbd5e1}' +
      '.rsp-card-ttl{font-size:15px;font-weight:700;color:#f1f5f9;margin-bottom:5px;line-height:1.35}' +
      '.rsp-text{font-size:13.5px;line-height:1.6;color:#dbe3ef;white-space:pre-wrap;word-break:break-word;max-height:30vh;overflow-y:auto}' +
      '.rsp-foot{display:flex;align-items:center;gap:10px;margin-top:12px}' +
      '.rsp-prog{font-size:11.5px;color:#64748b;font-weight:600;letter-spacing:.3px}' +
      '.rsp-actions{margin-left:auto;display:flex;gap:8px}' +
      '.rsp-btn{background:#ea580c;color:#fff;border:0;padding:9px 14px;border-radius:9px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;transition:background .14s}' +
      '.rsp-btn:hover{background:#c2410c}' +
      '.rsp-btn-ghost{background:rgba(71,85,105,.3);color:#e2e8f0}' +
      '.rsp-btn-ghost:hover{background:rgba(71,85,105,.45)}' +
      '.rsp-done{text-align:center;padding:6px 4px 2px}' +
      '.rsp-done svg{width:34px;height:34px;color:#fb923c;margin-bottom:6px}' +
      '.rsp-done-ttl{font-size:15px;font-weight:800;color:#f1f5f9}' +
      '.rsp-done-sub{font-size:12.5px;color:#94a3b8;line-height:1.5;margin-top:4px;max-width:380px;margin-left:auto;margin-right:auto}' +
      '.rsp-done-cb{font-size:12.5px;color:#fdba74;font-weight:600;margin-top:8px}' +
      'body.light .rsp-panel{background:#fff7ed;border-color:rgba(234,88,12,.25)}' +
      'body.light .rsp-card{background:#fff;border-color:rgba(15,23,42,.1)}' +
      'body.light .rsp-card-ttl,body.light .rsp-done-ttl{color:#0f172a}' +
      'body.light .rsp-text{color:#1e293b}' +
      'body.light .rsp-meta,body.light .rsp-done-sub{color:#475569}';
    var st = document.createElement('style'); st.id = 'jw-resurface-style'; st.textContent = css;
    document.head.appendChild(st);
  }

  var BRAND_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v5h5"/><path d="M3.05 13A9 9 0 1 0 6 5.3L3 8"/><path d="M12 7v5l3 2"/></svg>';
  var FLAME_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 .5-2 .5-2S6 9 6 13a6 6 0 0 0 12 0c0-5-6-11-6-11z"/></svg>';
  var CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>';

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }

  function topBar() {
    var top = el('div', 'rsp-top');
    var ttl = el('div', 'rsp-ttl'); ttl.innerHTML = BRAND_SVG; ttl.appendChild(el('span', null, t('brand')));
    top.appendChild(ttl);
    var s = store().streak || 0;
    if (s > 0) { var chip = el('div', 'rsp-streak'); chip.innerHTML = FLAME_SVG; chip.appendChild(el('span', null, t('streak_days').replace('{n}', s))); top.appendChild(chip); }
    return top;
  }

  function renderCard(M) {
    var c = M.container; c.innerHTML = '';
    var panel = el('div', 'rsp-panel');
    panel.appendChild(topBar());
    var n = M.deck[M.idx];
    var card = el('div', 'rsp-card');
    var badge = el('div', 'rsp-badge');
    if (n.otdYears > 0) { badge.textContent = t('on_this_day') + ' · ' + (n.otdYears === 1 ? t('w_year') : t('w_years').replace('{n}', n.otdYears)); }
    else { badge.textContent = agoLabel(n.created); }
    card.appendChild(badge);
    if ((n.color && HLC[n.color]) || n.ref) {
      var meta = el('div', 'rsp-meta');
      if (n.color && HLC[n.color]) { var dot = el('span', 'rsp-dot'); dot.style.background = HLC[n.color]; meta.appendChild(dot); }
      if (n.ref) meta.appendChild(el('span', 'rsp-ref', n.ref));
      card.appendChild(meta);
    }
    if (n.title) card.appendChild(el('div', 'rsp-card-ttl', n.title));
    if (n.text) card.appendChild(el('div', 'rsp-text', n.text));
    panel.appendChild(card);
    var foot = el('div', 'rsp-foot');
    foot.appendChild(el('div', 'rsp-prog', (M.idx + 1) + ' ' + t('count_sep') + ' ' + M.deck.length));
    var acts = el('div', 'rsp-actions');
    var refl = el('button', 'rsp-btn', t('reflect')); refl.type = 'button'; refl.onclick = function () { reflect(M); };
    acts.appendChild(refl);
    if (M.deck.length > 1) { var sk = el('button', 'rsp-btn rsp-btn-ghost', t('next')); sk.type = 'button'; sk.onclick = function () { M.idx = (M.idx + 1) % M.deck.length; renderCard(M); }; acts.appendChild(sk); }
    foot.appendChild(acts);
    panel.appendChild(foot);
    c.appendChild(panel);
  }

  function renderDone(M) {
    var c = M.container; c.innerHTML = '';
    var panel = el('div', 'rsp-panel');
    panel.appendChild(topBar());
    var done = el('div', 'rsp-done');
    var ic = document.createElement('div'); ic.innerHTML = CHECK_SVG; done.appendChild(ic.firstChild);
    done.appendChild(el('div', 'rsp-done-ttl', t('done_title')));
    done.appendChild(el('div', 'rsp-done-sub', t('done_sub')));
    done.appendChild(el('div', 'rsp-done-cb', t('come_back')));
    panel.appendChild(done);
    c.appendChild(panel);
  }

  function reflect(M) {
    var n = M.deck[M.idx]; if (!n) return;
    var st = store();
    scheduleNext(st, n);
    st.seen[n.guid] = today();
    st.total = (st.total || 0) + 1;
    st.dayDone = (st.dayDone || 0) + 1;
    maybeStreak(st);
    save(st);
    if (window.__jwHaptic) { try { window.__jwHaptic(12); } catch (_) {} }
    rerender(M);
  }

  function rerender(M) {
    buildDeck(M);
    if (M.deck.length === 0) { renderDone(M); return; }
    M.idx = 0; renderCard(M);
  }

  function mount(container, opts) {
    if (!container) return null;
    opts = opts || {};
    injectStyle();
    var M = { container: container, notes: opts.notes || [], deck: [], idx: 0 };
    if (!M.notes.length) { container.innerHTML = ''; return null; }
    rerender(M);
    return M;
  }

  window.JwResurface = { mount: mount, notesFromDb: notesFromDb, notesFromBuffer: notesFromBuffer };
})();

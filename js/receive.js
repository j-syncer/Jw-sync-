/* ──────────────────────────────────────────────────────────────────────────
   receive.js — Receive/adopt shared notes into a backup (window.__jwReceive*).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function(){
  "use strict";
  if(window.__jwReceiveReady) return; window.__jwReceiveReady=true;
  var SQLCDN='https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';
  var ZIPCDN='https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
  var I18N={
    en:{pm_title:'Got notes from a friend?',pm_hint:'Add a .jwshare.json someone sent you — its notes will be added to this merge.',pm_choose:'Choose shared file',pm_loaded:'{n} shared note(s) will be added to this merge.',pm_remove:'Remove',tag_label:'Tag for imported notes',pm_safe:'Added as new notes — your own notes are never replaced.',ov_q:'{n} highlight(s) land on verses you already highlighted. How should we add them?',ov_layer:'Add as a separate layer',ov_note:'Import note only',cat_all:'All',cat_hl:'Highlights',cat_note:'Notes',conf_intro:'These notes are on verses you already highlighted:',imp_title:'Added to your merge',more_hint:'+{n} more — use the filters above to narrow',preview:'Preview',prev_title:'Shared notes',close:'Close',dl:'Download',adding:'Adding shared notes…',added:'{n} note(s) added from a friend — tap Download for the updated file.',invalid:"That file isn't a JW Sync share file.",shared_tag:'Shared'},
    es:{pm_title:'¿Notas de un amigo?',pm_hint:'Agrega un .jwshare.json que te enviaron — sus notas se añadirán a esta fusión.',pm_choose:'Elegir archivo compartido',pm_loaded:'Se añadirán {n} nota(s) compartida(s) a esta fusión.',pm_remove:'Quitar',tag_label:'Etiqueta para las notas importadas',pm_safe:'Se agregan como notas nuevas — tus notas nunca se reemplazan.',ov_q:'{n} resaltado(s) caen en versículos que ya resaltaste. ¿Cómo los agregamos?',ov_layer:'Agregar como capa aparte',ov_note:'Importar solo la nota',cat_all:'Todas',cat_hl:'Resaltados',cat_note:'Notas',conf_intro:'Estas notas están en versículos que ya resaltaste:',imp_title:'Agregadas a tu fusión',more_hint:'+{n} más — usa los filtros para acotar',preview:'Vista previa',prev_title:'Notas compartidas',close:'Cerrar',dl:'Descargar',adding:'Agregando notas compartidas…',added:'{n} nota(s) añadida(s) de un amigo — toca Descargar para el archivo actualizado.',invalid:'Ese archivo no es un archivo de JW Sync.',shared_tag:'Compartido'},
    pt:{pm_title:'Notas de um amigo?',pm_hint:'Adicione um .jwshare.json que enviaram — as notas serão incluídas nesta mesclagem.',pm_choose:'Escolher arquivo',pm_loaded:'{n} nota(s) compartilhada(s) serão adicionadas a esta mesclagem.',pm_remove:'Remover',tag_label:'Etiqueta para as notas importadas',pm_safe:'Adicionadas como notas novas — suas notas nunca são substituídas.',ov_q:'{n} marcação(ões) caem em versículos que você já marcou. Como adicioná-las?',ov_layer:'Adicionar como camada separada',ov_note:'Importar só a nota',cat_all:'Todas',cat_hl:'Marcações',cat_note:'Notas',conf_intro:'Estas notas estão em versículos que você já marcou:',imp_title:'Adicionadas à sua mesclagem',more_hint:'+{n} mais — use os filtros para refinar',preview:'Pré-visualizar',prev_title:'Notas compartilhadas',close:'Fechar',dl:'Baixar',adding:'Adicionando notas compartilhadas…',added:'{n} nota(s) adicionada(s) de um amigo — toque em Baixar para o arquivo atualizado.',invalid:'Esse arquivo não é um arquivo do JW Sync.',shared_tag:'Compartilhado'},
    fr:{pm_title:"Des notes d'un ami ?",pm_hint:'Ajoutez un .jwshare.json reçu — ses notes seront ajoutées à cette fusion.',pm_choose:'Choisir le fichier',pm_loaded:'{n} note(s) partagée(s) seront ajoutées à cette fusion.',pm_remove:'Retirer',tag_label:'Étiquette pour les notes importées',pm_safe:'Ajoutées comme nouvelles notes — vos notes ne sont jamais remplacées.',ov_q:'{n} surlignage(s) tombent sur des versets déjà surlignés. Comment les ajouter ?',ov_layer:'Ajouter comme calque séparé',ov_note:'Importer la note seule',cat_all:'Toutes',cat_hl:'Surlignages',cat_note:'Notes',conf_intro:'Ces notes sont sur des versets déjà surlignés :',imp_title:'Ajoutées à votre fusion',more_hint:'+{n} de plus — utilisez les filtres pour affiner',preview:'Aperçu',prev_title:'Notes partagées',close:'Fermer',dl:'Télécharger',adding:'Ajout des notes partagées…',added:"{n} note(s) ajoutée(s) d'un ami — appuyez sur Télécharger pour le fichier mis à jour.",invalid:"Ce fichier n'est pas un fichier JW Sync.",shared_tag:'Partagé'},
    de:{pm_title:'Notizen von einem Freund?',pm_hint:'Füge eine erhaltene .jwshare.json hinzu — ihre Notizen kommen in diese Zusammenführung.',pm_choose:'Datei wählen',pm_loaded:'{n} geteilte Notiz(en) werden hinzugefügt.',pm_remove:'Entfernen',tag_label:'Tag für importierte Notizen',pm_safe:'Werden als neue Notizen hinzugefügt — deine Notizen werden nie ersetzt.',ov_q:'{n} Markierung(en) liegen auf bereits markierten Versen. Wie hinzufügen?',ov_layer:'Als separate Ebene hinzufügen',ov_note:'Nur Notiz importieren',cat_all:'Alle',cat_hl:'Markierungen',cat_note:'Notizen',conf_intro:'Diese Notizen liegen auf bereits markierten Versen:',imp_title:'Zu deiner Zusammenführung hinzugefügt',more_hint:'+{n} weitere — nutze die Filter zum Eingrenzen',preview:'Vorschau',prev_title:'Geteilte Notizen',close:'Schließen',dl:'Herunterladen',adding:'Geteilte Notizen werden hinzugefügt…',added:'{n} Notiz(en) von einem Freund hinzugefügt — tippe auf Herunterladen für die aktualisierte Datei.',invalid:'Das ist keine JW-Sync-Datei.',shared_tag:'Geteilt'},
    it:{pm_title:'Note da un amico?',pm_hint:'Aggiungi un .jwshare.json ricevuto — le note saranno incluse in questa unione.',pm_choose:'Scegli file',pm_loaded:'{n} nota/e condivisa/e saranno aggiunte a questa unione.',pm_remove:'Rimuovi',tag_label:'Etichetta per le note importate',pm_safe:'Aggiunte come note nuove — le tue note non vengono mai sostituite.',ov_q:'{n} evidenziazione/i su versetti già evidenziati. Come aggiungerle?',ov_layer:'Aggiungi come livello separato',ov_note:'Importa solo la nota',cat_all:'Tutte',cat_hl:'Evidenziazioni',cat_note:'Note',conf_intro:'Queste note sono su versetti già evidenziati:',imp_title:'Aggiunte alla tua unione',more_hint:'+{n} altre — usa i filtri per restringere',preview:'Anteprima',prev_title:'Note condivise',close:'Chiudi',dl:'Scarica',adding:'Aggiunta note condivise…',added:'{n} nota/e aggiunta/e da un amico — tocca Scarica per il file aggiornato.',invalid:'Questo non è un file JW Sync.',shared_tag:'Condiviso'},
    ru:{pm_title:'Заметки от друга?',pm_hint:'Добавьте присланный .jwshare.json — его заметки войдут в это объединение.',pm_choose:'Выбрать файл',pm_loaded:'{n} заметок будет добавлено в это объединение.',pm_remove:'Убрать',tag_label:'Метка для импортированных заметок',pm_safe:'Добавляются как новые заметки — ваши заметки никогда не заменяются.',ov_q:'{n} выделени(й) на уже выделенных стихах. Как их добавить?',ov_layer:'Добавить отдельным слоем',ov_note:'Только заметку',cat_all:'Все',cat_hl:'Выделения',cat_note:'Заметки',conf_intro:'Эти заметки на уже выделенных стихах:',imp_title:'Добавлено в ваше объединение',more_hint:'+{n} ещё — используйте фильтры',preview:'Предпросмотр',prev_title:'Общие заметки',close:'Закрыть',dl:'Скачать',adding:'Добавление заметок…',added:'Добавлено {n} заметок от друга — нажмите «Скачать» для обновлённого файла.',invalid:'Это не файл JW Sync.',shared_tag:'Общие'},
    ja:{pm_title:'友達からのノート？',pm_hint:'受け取った .jwshare.json を追加すると、そのノートがこの結合に加わります。',pm_choose:'共有ファイルを選ぶ',pm_loaded:'{n} 件の共有ノートがこの結合に追加されます。',pm_remove:'削除',tag_label:'取り込むノートのタグ',pm_safe:'新しいノートとして追加されます — あなたのノートは置き換えられません。',ov_q:'{n} 件のハイライトは既にハイライト済みの節にあります。どう追加しますか？',ov_layer:'別レイヤーとして追加',ov_note:'ノートだけ取り込む',cat_all:'すべて',cat_hl:'ハイライト',cat_note:'ノート',conf_intro:'これらは既にハイライト済みの節にあります：',imp_title:'結合に追加されました',more_hint:'他 {n} 件 — フィルターで絞り込み',preview:'プレビュー',prev_title:'共有ノート',close:'閉じる',dl:'ダウンロード',adding:'共有ノートを追加中…',added:'友達から {n} 件のノートを追加しました — ダウンロードで更新ファイルを取得。',invalid:'これは JW Sync の共有ファイルではありません。',shared_tag:'共有'},
    ko:{pm_title:'친구가 보낸 노트?',pm_hint:'받은 .jwshare.json을 추가하면 그 노트가 이 병합에 포함됩니다.',pm_choose:'공유 파일 선택',pm_loaded:'{n}개의 공유 노트가 이 병합에 추가됩니다.',pm_remove:'제거',tag_label:'가져온 노트의 태그',pm_safe:'새 노트로 추가됩니다 — 기존 노트는 절대 교체되지 않습니다.',ov_q:'{n}개의 강조 표시가 이미 강조한 구절에 있습니다. 어떻게 추가할까요?',ov_layer:'별도 레이어로 추가',ov_note:'노트만 가져오기',cat_all:'전체',cat_hl:'강조',cat_note:'노트',conf_intro:'다음은 이미 강조한 구절에 있습니다:',imp_title:'병합에 추가됨',more_hint:'+{n}개 더 — 필터로 좁히기',preview:'미리보기',prev_title:'공유 노트',close:'닫기',dl:'다운로드',adding:'공유 노트 추가 중…',added:'친구로부터 {n}개 노트 추가됨 — 다운로드를 눌러 업데이트된 파일을 받으세요.',invalid:'JW Sync 공유 파일이 아닙니다.',shared_tag:'공유됨'},
    tl:{pm_title:'May tala mula sa kaibigan?',pm_hint:'Magdagdag ng .jwshare.json na ipinadala sa iyo — isasama ang mga tala nito sa merge.',pm_choose:'Pumili ng file',pm_loaded:'{n} ibinahaging tala ang idaragdag sa merge na ito.',pm_remove:'Alisin',tag_label:'Tag para sa mga na-import na tala',pm_safe:'Idinaragdag bilang bagong tala — hindi kailanman papalitan ang iyong mga tala.',ov_q:'{n} highlight ang nasa mga tekstong na-highlight mo na. Paano idaragdag?',ov_layer:'Idagdag bilang hiwalay na layer',ov_note:'Tala lang ang i-import',cat_all:'Lahat',cat_hl:'Mga highlight',cat_note:'Mga tala',conf_intro:'Ang mga talang ito ay nasa tekstong na-highlight mo na:',imp_title:'Naidagdag sa iyong merge',more_hint:'+{n} pa — gamitin ang mga filter',preview:'I-preview',prev_title:'Mga ibinahaging tala',close:'Isara',dl:'I-download',adding:'Idinaragdag ang mga ibinahaging tala…',added:'{n} tala mula sa kaibigan ang naidagdag — i-tap ang Download para sa updated na file.',invalid:'Hindi ito JW Sync share file.',shared_tag:'Shared'}
  ,sv:{pm_title:"Fått anteckningar av en vän?",pm_hint:"Lägg till en .jwshare.json som någon skickat dig — dess anteckningar läggs till i den här sammanslagningen.",pm_choose:"Välj delad fil",pm_loaded:"{n} delad(e) anteckning(ar) läggs till i den här sammanslagningen.",pm_remove:"Ta bort",tag_label:"Tagg för importerade anteckningar",pm_safe:"Tillagda som nya anteckningar — dina egna anteckningar ersätts aldrig.",ov_q:"{n} överstrykning(ar) hamnar på verser du redan strukit över. Hur ska vi lägga till dem?",ov_layer:"Lägg till som ett separat lager",ov_note:"Importera endast anteckning",cat_all:"Alla",cat_hl:"Överstrykningar",cat_note:"Anteckningar",conf_intro:"Dessa anteckningar är på verser du redan strukit över:",imp_title:"Tillagt i din sammanslagning",more_hint:"+{n} till — använd filtren ovan för att begränsa",preview:"Förhandsgranska",prev_title:"Delade anteckningar",close:"Stäng",dl:"Ladda ner",adding:"Lägger till delade anteckningar…",added:"{n} anteckning(ar) tillagda från en vän — tryck på Ladda ner för den uppdaterade filen.",invalid:"Den filen är inte en JW Sync-delningsfil.",shared_tag:"Delad"},ceb:{pm_title:'May mga nota gikan sa higala?',pm_hint:'Magdugang ug .jwshare.json nga gipadala kanimo — ang mga nota niini iduganon sa merge.',pm_choose:'Pilia ang file',pm_loaded:'{n} ka gipaambit nga nota ang iduganon sa merge.',pm_remove:'Tangtangon',tag_label:'Tag para sa mga na-import nga nota',pm_safe:'Gidugang isip mga bag-ong nota — dili gayud mapulihan ang imong mga nota.',ov_q:'{n} ka highlight ang naa sa mga bersikulo nga na-highlight mo na. Unsaon pagidugang?',ov_layer:'Idugang isip lain-laing layer',ov_note:'Ang nota lamang ang i-import',cat_all:'Tanan',cat_hl:'Mga highlight',cat_note:'Mga nota',conf_intro:'Kining mga nota naa sa mga bersikulo nga na-highlight mo na:',imp_title:'Gidugang sa imong merge',more_hint:'+{n} pa — gamiton ang mga filter',preview:'I-preview',prev_title:'Gipaambit nga mga nota',close:'Isira',dl:'I-download',adding:'Gidugang ang mga gipaambit nga nota…',added:'{n} ka nota gikan sa higala ang gidugang — i-tap ang Download para sa gi-update nga file.',invalid:'Dili kini JW Sync share file.',shared_tag:'Shared'},uk:{pm_title:"Отримали нотатки від друга?",pm_hint:"Додайте файл .jwshare.json, який вам надіслали, — його нотатки буде додано до цього об'єднання.",pm_choose:"Вибрати спільний файл",pm_loaded:"{n} спільних нотаток буде додано до цього об'єднання.",pm_remove:"Вилучити",tag_label:"Тег для імпортованих нотаток",pm_safe:"Додаються як нові нотатки — ваші власні нотатки ніколи не замінюються.",ov_q:"{n} виділень припадають на вірші, які ви вже виділили. Як їх додати?",ov_layer:"Додати окремим шаром",ov_note:"Імпортувати лише нотатку",cat_all:"Усі",cat_hl:"Виділення",cat_note:"Нотатки",conf_intro:"Ці нотатки стосуються віршів, які ви вже виділили:",imp_title:"Додано до вашого об'єднання",more_hint:"Ще +{n} — скористайтеся фільтрами вгорі, щоб звузити пошук",preview:"Перегляд",prev_title:"Спільні нотатки",close:"Закрити",dl:"Завантажити",adding:"Додаємо спільні нотатки…",added:"{n} нотаток додано від друга — натисніть «Завантажити», щоб отримати оновлений файл.",invalid:"Цей файл не є файлом спільного доступу JW Sync.",shared_tag:"Спільні"},he:{pm_title:"קיבלתם הערות מחבר?",pm_hint:"הוסיפו קובץ ‎.jwshare.json שמישהו שלח לכם — ההערות שבו יתווספו למיזוג הזה.",pm_choose:"בחירת קובץ משותף",pm_loaded:"{n} הערות משותפות יתווספו למיזוג הזה.",pm_remove:"הסרה",tag_label:"תווית להערות המיובאות",pm_safe:"נוספות כהערות חדשות — ההערות שלכם לעולם לא מוחלפות.",ov_q:"{n} הדגשות נופלות על פסוקים שכבר הדגשתם. איך להוסיף אותן?",ov_layer:"הוספה כשכבה נפרדת",ov_note:"ייבוא ההערה בלבד",cat_all:"הכול",cat_hl:"הדגשות",cat_note:"הערות",conf_intro:"ההערות האלה נמצאות על פסוקים שכבר הדגשתם:",imp_title:"נוספו למיזוג שלכם",more_hint:"+{n} נוספות — השתמשו במסננים שלמעלה כדי לצמצם",preview:"תצוגה מקדימה",prev_title:"הערות משותפות",close:"סגירה",dl:"הורדה",adding:"מוסיף הערות משותפות…",added:"{n} הערות נוספו מחבר — הקישו על הורדה לקבלת הקובץ המעודכן.",invalid:"הקובץ הזה אינו קובץ שיתוף של JW Sync.",shared_tag:"משותף"},ar:{pm_title:"وصلتك ملاحظات من صديق؟",pm_hint:"أضف ملف ‎.jwshare.json‎ أرسله إليك أحدهم — ستُضاف ملاحظاته إلى هذا الدمج.",pm_choose:"اختر الملف المُشارَك",pm_loaded:"ستُضاف {n} ملاحظة مُشارَكة إلى هذا الدمج.",pm_remove:"إزالة",tag_label:"وسم للملاحظات المستوردة",pm_safe:"تُضاف كملاحظات جديدة — ملاحظاتك الخاصة لا تُستبدل أبدًا.",ov_q:"{n} تظليل يقع على آيات ظلّلتها من قبل. كيف تريد إضافتها؟",ov_layer:"أضفها كطبقة مستقلة",ov_note:"استورد الملاحظة فقط",cat_all:"الكل",cat_hl:"التظليلات",cat_note:"الملاحظات",conf_intro:"هذه الملاحظات على آيات ظلّلتها من قبل:",imp_title:"أُضيفت إلى الدمج",more_hint:"+{n} إضافية — استخدم عوامل التصفية أعلاه للتضييق",preview:"معاينة",prev_title:"الملاحظات المُشارَكة",close:"إغلاق",dl:"تنزيل",adding:"جارٍ إضافة الملاحظات المُشارَكة…",added:"أُضيفت {n} ملاحظة من صديق — اضغط تنزيل للحصول على الملف المحدَّث.",invalid:"هذا الملف ليس ملف مشاركة من JW Sync.",shared_tag:"مُشارَكة"}};
  function lang(){ try{ var l=localStorage.getItem('jwsync_lang'); return (l&&I18N[l])?l:'en'; }catch(_){ return 'en'; } }
  function T(){ return I18N[lang()]||I18N.en; }
  function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];}); }
  function fmt(s,n){ return String(s).replace('{n}', n); }

  function loadScript(src){ return new Promise(function(res,rej){ var s=document.createElement('script'); s.src=src; s.onload=res; s.onerror=rej; document.head.appendChild(s); }); }
  function ensureLibs(){ var need=[]; if(typeof window.JSZip!=='function') need.push(loadScript(ZIPCDN)); if(typeof window.initSqlJs!=='function') need.push(loadScript(SQLCDN+'sql-wasm.js')); return Promise.all(need); }
  function uuid(){ return 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g,function(ch){var r=Math.random()*16|0,v=ch==='x'?r:(r&0x3|0x8);return v.toString(16);}); }
  function sanitize(html){ var d=document.createElement('div'); d.innerHTML=String(html||''); var allow={P:1,BR:1,B:1,STRONG:1,I:1,EM:1,U:1,UL:1,OL:1,LI:1}; (function walk(node){ var ch=Array.prototype.slice.call(node.childNodes); ch.forEach(function(n){ if(n.nodeType===1){ if(!allow[n.tagName]){ while(n.firstChild) node.insertBefore(n.firstChild,n); node.removeChild(n); } else { while(n.attributes&&n.attributes.length) n.removeAttribute(n.attributes[0].name); walk(n); } } else if(n.nodeType!==3){ node.removeChild(n); } }); })(d); return d.innerHTML; }

  // Location identity columns used for de-duplication (mirrors merge-worker composite key)
  var LOC_ID_COLS=['BookNumber','ChapterNumber','DocumentId','Track','IssueTagNumber','KeySymbol','MepsLanguage','Type'];
  function intval(v){ v=parseInt(v,10); return isFinite(v)?v:0; }
  function parseEnvelope(text){
    var env=null; try{ env=JSON.parse(text); }catch(_){ return null; }
    if(!env||env.app!=='jwsync'||!Array.isArray(env.notes)) return null;
    return env.notes.map(function(n){
      var note={ title:(typeof n.title==='string')?n.title:'', content:sanitize((typeof n.content==='string')?n.content:''), tags:Array.isArray(n.tags)?n.tags:[], pub:(typeof n.pub==='string')?n.pub:'' };
      if(n && n.loc && typeof n.loc==='object' && Array.isArray(n.ranges) && n.ranges.length){
        note.loc=n.loc; note.color=intval(n.color); note.style=intval(n.style);
        note.ranges=n.ranges.map(function(r){ return { blockType:intval(r&&r.blockType), identifier:intval(r&&r.identifier), startToken:intval(r&&r.startToken), endToken:intval(r&&r.endToken) }; });
      }
      return note;
    });
  }
  function readShareFile(file){ return new Promise(function(res){ var fr=new FileReader(); fr.onload=function(){ res(parseEnvelope(String(fr.result||''))); }; fr.onerror=function(){ res(null); }; fr.readAsText(file); }); }
  window.__jwParseShareEnvelope=parseEnvelope; // for tests

  // ── DB helpers (operate on an open sql.js Database) ──
  function sqlStr(v){ if(v===null||v===undefined) return 'NULL'; if(typeof v==='number'&&isFinite(v)) return String(v); return "'"+String(v).replace(/'/g,"''")+"'"; }
  function tableCols(db,table){ try{ var r=db.exec('PRAGMA table_info("'+table+'")'); return (r.length?r[0].values.map(function(x){return x[1];}):[]); }catch(_){ return []; } }
  function lastId(db){ return db.exec('SELECT last_insert_rowid() AS id')[0].values[0][0]; }
  function getTagId(db,name){ var s=String(name).replace(/'/g,"''"); var r=db.exec("SELECT TagId FROM Tag WHERE Name='"+s+"' COLLATE NOCASE"); if(r.length&&r[0].values.length) return r[0].values[0][0]; db.run('INSERT INTO Tag (Name, Type) VALUES (?,1)',[name]); return lastId(db); }
  function nextTagPos(db,tid){ try{ var r=db.exec('SELECT COALESCE(MAX(Position),-1)+1 AS p FROM TagMap WHERE TagId='+(tid|0)); return (r.length&&r[0].values.length)?r[0].values[0][0]:0; }catch(_){ return 0; } }
  function rangesOverlap(a,b){ return a.blockType===b.blockType && a.identifier===b.identifier && a.startToken<=b.endToken && b.startToken<=a.endToken; }
  function resolveLocationId(db, loc, present, create){
    var idCols=LOC_ID_COLS.filter(function(c){ return present.indexOf(c)>=0; });
    if(!idCols.length) return null;
    var where=idCols.map(function(c){ var v=loc[c]; return (v===undefined||v===null)?('"'+c+'" IS NULL'):('"'+c+'"='+sqlStr(v)); });
    var r=db.exec('SELECT LocationId FROM Location WHERE '+where.join(' AND ')+' LIMIT 1');
    if(r.length&&r[0].values.length) return r[0].values[0][0];
    if(!create) return null;
    var cols=idCols.slice(), vals=idCols.map(function(c){ var v=loc[c]; return (v===undefined)?null:v; });
    if(present.indexOf('Title')>=0){ cols.push('Title'); vals.push(loc.Title!==undefined?loc.Title:null); }
    db.run('INSERT INTO Location ('+cols.map(function(c){return '"'+c+'"';}).join(',')+') VALUES ('+cols.map(function(){return '?';}).join(',')+')', vals);
    return lastId(db);
  }
  function existingRanges(db, locId){
    var r=db.exec('SELECT br.BlockType, br.Identifier, br.StartToken, br.EndToken FROM BlockRange br JOIN UserMark um ON br.UserMarkId=um.UserMarkId WHERE um.LocationId='+(locId|0));
    if(!r.length) return [];
    return r[0].values.map(function(v){ return { blockType:v[0], identifier:v[1], startToken:v[2], endToken:v[3] }; });
  }
  function noteOverlaps(db, nd, present){
    if(!nd.loc||!nd.ranges||!nd.ranges.length) return false;
    var locId=resolveLocationId(db, nd.loc, present, false);
    if(locId===null) return false;
    var ex=existingRanges(db, locId);
    if(!ex.length) return false;
    return nd.ranges.some(function(r){ return ex.some(function(e){ return rangesOverlap(r,e); }); });
  }

  // ── preview / summary UI helpers ──
  var JWL_COLORS={1:'#fde047',2:'#86efac',3:'#7dd3fc',4:'#f9a8d4',5:'#fdba74',6:'#c4b5fd'};
  function stripText(html){ var d=document.createElement('div'); d.innerHTML=String(html||''); return (d.textContent||d.innerText||'').replace(/\s+/g,' ').trim(); }
  function noteHasHl(nd){ return !!(nd && nd.loc && nd.ranges && nd.ranges.length); }
  function notePub(nd){ return (nd&&nd.pub)?String(nd.pub):''; }
  function noteRow(nd){
    var hl=noteHasHl(nd), col=hl?(JWL_COLORS[intval(nd.color)]||'#94a3b8'):null;
    var dot=col?('<span class="jwr-dot" style="background:'+col+'"></span>'):'<span class="jwr-dot jwr-dot-none"></span>';
    var title=esc((nd.title&&String(nd.title).trim())||'—'), ex=esc(stripText(nd.content)), pub=notePub(nd), meta='';
    if(pub) meta+='<span class="jwr-pill jwr-pill-pub">'+esc(pub)+'</span>';
    (Array.isArray(nd.tags)?nd.tags:[]).slice(0,8).forEach(function(tg){ tg=String(tg||'').trim(); if(tg) meta+='<span class="jwr-pill">'+esc(tg)+'</span>'; });
    return '<div class="jwr-nrow">'+dot+'<div class="jwr-nbody"><div class="jwr-ntitle">'+title+'</div>'+(ex?'<div class="jwr-nex">'+ex+'</div>':'')+(meta?'<div class="jwr-nmeta">'+meta+'</div>':'')+'</div></div>';
  }
  function notesStats(notes){ var nHl=0,nPlain=0,tagCounts={}; notes.forEach(function(nd){ if(noteHasHl(nd)) nHl++; else nPlain++; (Array.isArray(nd.tags)?nd.tags:[]).forEach(function(tg){ tg=String(tg||'').trim(); if(tg) tagCounts[tg]=(tagCounts[tg]||0)+1; }); }); return {nHl:nHl,nPlain:nPlain,tagCounts:tagCounts}; }
  function chipsHtml(notes,st){ var L=T(); var h='<button class="jwr-chip" data-f="all">'+esc(L.cat_all)+' ('+notes.length+')</button>'; if(st.nHl) h+='<button class="jwr-chip" data-f="hl">'+esc(L.cat_hl)+' ('+st.nHl+')</button>'; if(st.nPlain) h+='<button class="jwr-chip" data-f="plain">'+esc(L.cat_note)+' ('+st.nPlain+')</button>'; Object.keys(st.tagCounts).sort(function(a,b){return st.tagCounts[b]-st.tagCounts[a];}).slice(0,24).forEach(function(tg){ h+='<button class="jwr-chip" data-f="tag:'+esc(tg)+'">'+esc(tg)+' ('+st.tagCounts[tg]+')</button>'; }); return h; }
  function matchesFilter(nd,f){ if(f.type==='all') return true; if(f.type==='hl') return noteHasHl(nd); if(f.type==='plain') return !noteHasHl(nd); if(f.type==='tag') return (Array.isArray(nd.tags)?nd.tags:[]).some(function(tg){ return String(tg)===f.tag; }); return true; }
  function listHtml(notes,f){ var CAP=300,html='',shown=notes.filter(function(nd){return matchesFilter(nd,f);}); for(var i=0;i<shown.length&&i<CAP;i++) html+=noteRow(shown[i]); if(shown.length>CAP) html+='<div class="jwr-more">'+esc(fmt(T().more_hint,shown.length-CAP))+'</div>'; if(!shown.length) html+='<div class="jwr-more">—</div>'; return html; }
  function openNotesModal(title, notes, buttons){
    var st=notesStats(notes), f={type:'all'};
    var foot=(buttons||[]).map(function(b,i){ return '<button class="jwr-mb'+(b.primary?' jwr-mb-primary':'')+'" data-i="'+i+'">'+esc(b.label)+'</button>'; }).join('');
    var ov=document.createElement('div'); ov.className='jwr-modal';
    ov.innerHTML='<div class="jwr-modal-card jwr-modal-lg"><button class="jwr-x" aria-label="close">×</button><div class="jwr-modal-h">'+esc(title)+'</div><div class="jwr-chips">'+chipsHtml(notes,st)+'</div><div class="jwr-list">'+listHtml(notes,f)+'</div><div class="jwr-modal-foot">'+foot+'</div></div>';
    var listEl=ov.querySelector('.jwr-list');
    function setActive(){ Array.prototype.forEach.call(ov.querySelectorAll('.jwr-chip'),function(ch){ var key=f.type==='tag'?('tag:'+f.tag):f.type; ch.classList.toggle('jwr-chip-on', ch.getAttribute('data-f')===key); }); }
    setActive();
    Array.prototype.forEach.call(ov.querySelectorAll('.jwr-chip'),function(ch){ ch.onclick=function(){ var d=ch.getAttribute('data-f'); if(d.indexOf('tag:')===0) f={type:'tag',tag:d.slice(4)}; else f={type:d}; listEl.innerHTML=listHtml(notes,f); setActive(); }; });
    function close(){ try{ov.remove();}catch(_){ } }
    ov.querySelector('.jwr-x').onclick=close;
    ov.addEventListener('click',function(e){ if(e.target===ov){ close(); return; } var b=e.target.closest&&e.target.closest('[data-i]'); if(b){ var spec=(buttons||[])[+b.getAttribute('data-i')]; close(); if(spec&&spec.onClick) spec.onClick(); } });
    document.body.appendChild(ov); return {ov:ov, close:close};
  }
  function openPreview(notes){ if(!notes||!notes.length) return; openNotesModal(T().prev_title, notes, [{label:T().close}]); }
  function openSummary(imported){ if(!imported||!imported.length) return; openNotesModal(T().imp_title, imported, [{label:T().dl, primary:true, onClick:function(){ var dl=document.getElementById('download-btn'); if(dl){ try{ dl.click(); }catch(_){ } } }}, {label:T().close}]); }

  // ── core adoption: writes only INSERTs, never UPDATE/DELETE on the user's rows ──
  function adoptIntoDb(db, notes, opts){
    var label=(opts&&opts.tagLabel)||'Shared';
    var overlapMode=(opts&&opts.overlapMode)==='note'?'note':'layer';
    var now=new Date().toISOString().replace('T',' ').slice(0,19);
    var locPresent=tableCols(db,'Location');
    var noteCols=tableCols(db,'Note');
    var hasUserMark=tableCols(db,'UserMark').length>0;
    var umCols=hasUserMark?tableCols(db,'UserMark'):[];
    var hasBlockRange=tableCols(db,'BlockRange').length>0;
    var added=0, highlights=0, imported=[];
    try{ db.run('PRAGMA foreign_keys=OFF;'); }catch(_){ }
    notes.forEach(function(nd){ try{
      var title=nd.title||'', content=nd.content||'';
      var hasHl = !!(nd.loc && nd.ranges && nd.ranges.length && hasUserMark && hasBlockRange && locPresent.length);
      var locId=null, userMarkId=null, mode='plain';
      if(hasHl){
        locId=resolveLocationId(db, nd.loc, locPresent, true);
        var overlaps = locId!==null && existingRanges(db, locId).some(function(e){ return nd.ranges.some(function(r){ return rangesOverlap(r,e); }); });
        var makeLayer = (!overlaps) || (overlapMode==='layer'); mode=makeLayer?'layer':'note';
        if(makeLayer && locId!==null){
          var c=['ColorIndex','LocationId','UserMarkGuid','Version'], v=[nd.color||0, locId, uuid(), 1];
          if(umCols.indexOf('StyleIndex')>=0){ c.push('StyleIndex'); v.push(nd.style||0); }
          db.run('INSERT INTO UserMark ('+c.join(',')+') VALUES ('+c.map(function(){return '?';}).join(',')+')', v);
          userMarkId=lastId(db);
          nd.ranges.forEach(function(r){ db.run('INSERT INTO BlockRange (BlockType, Identifier, StartToken, EndToken, UserMarkId) VALUES (?,?,?,?,?)',[r.blockType,r.identifier,r.startToken,r.endToken,userMarkId]); });
          highlights++;
        } else if(locId!==null){
          // note-only: anchor to one of the user's existing highlights on this passage
          var er=db.exec('SELECT um.UserMarkId FROM UserMark um JOIN BlockRange br ON br.UserMarkId=um.UserMarkId WHERE um.LocationId='+(locId|0)+' LIMIT 1');
          if(er.length&&er[0].values.length) userMarkId=er[0].values[0][0];
        }
      }
      var anchor = (hasHl && nd.ranges[0]) ? nd.ranges[0] : null;
      var nc=['Guid','Title','Content','LastModified','Created','BlockType','BlockIdentifier'];
      var nv=[uuid(), title, content, now, now, anchor?anchor.blockType:0, anchor?anchor.identifier:0];
      if(userMarkId!==null && noteCols.indexOf('UserMarkId')>=0){ nc.push('UserMarkId'); nv.push(userMarkId); }
      if(locId!==null && noteCols.indexOf('LocationId')>=0){ nc.push('LocationId'); nv.push(locId); }
      db.run('INSERT INTO Note ('+nc.join(',')+') VALUES ('+nc.map(function(){return '?';}).join(',')+')', nv);
      var noteId=lastId(db);
      var names=[label].concat(Array.isArray(nd.tags)?nd.tags:[]), seen={}, applied=[];
      names.forEach(function(tn){ tn=String(tn||'').trim(); if(!tn||seen[tn.toLowerCase()])return; seen[tn.toLowerCase()]=1; var tid=getTagId(db,tn); try{ db.run('INSERT INTO TagMap (TagId, NoteId, Position) VALUES (?,?,?)',[tid,noteId,nextTagPos(db,tid)]); applied.push(tn); }catch(_){ } });
      imported.push({ title:nd.title, content:nd.content, pub:notePub(nd), color:nd.color, loc:nd.loc, ranges:nd.ranges, tags:applied, mode:mode });
      added++;
    }catch(e){ console.error('[jwr] adopt',e); } });
    return { added:added, highlights:highlights, imported:imported };
  }

  // adopt notes into a .jwlibrary ArrayBuffer → {buffer, added, highlights, overlaps}
  // opts: string (tag) for back-compat, or {tagLabel, onOverlap}
  function adoptIntoBuffer(buffer, notes, opts){
    if(typeof opts==='string') opts={tagLabel:opts};
    opts=opts||{};
    return ensureLibs().then(function(){
      return window.JSZip.loadAsync(buffer).then(function(zip){
        var key=Object.keys(zip.files).find(function(k){return /userdata\.db$/i.test(k);});
        if(!key) throw new Error('not a backup');
        return zip.file(key).async('uint8array').then(function(bytes){
          return window.initSqlJs({locateFile:function(f){return SQLCDN+f;}}).then(function(SQL){
            var db=new SQL.Database(bytes);
            var present=tableCols(db,'Location');
            var conflicts=[];
            notes.forEach(function(nd){ if(noteOverlaps(db, nd, present)) conflicts.push(nd); });
            var decide = (conflicts.length>0 && typeof opts.onOverlap==='function') ? Promise.resolve(opts.onOverlap(conflicts.length, conflicts)) : Promise.resolve('layer');
            return decide.then(function(mode){
              if(mode==='cancel'){ db.close(); return {buffer:buffer, added:0, highlights:0, overlaps:conflicts.length, imported:[], cancelled:true}; }
              var res=adoptIntoDb(db, notes, {tagLabel:opts.tagLabel, overlapMode:(mode==='note'?'note':'layer')});
              var out=db.export(); db.close(); zip.file(key, out);
              return zip.generateAsync({type:'arraybuffer',compression:'DEFLATE'}).then(function(buf){ return {buffer:buf, added:res.added, highlights:res.highlights, overlaps:conflicts.length, imported:res.imported}; });
            });
          });
        });
      });
    });
  }
  window.__jwAdoptSharedIntoBuffer=adoptIntoBuffer; // for tests

  function getMergedBuffer(){ var dl=document.getElementById('download-btn'); if(!dl) return Promise.resolve(null); var href=dl.getAttribute('href')||''; if(href.indexOf('blob:')!==0) return Promise.resolve(null); return fetch(href).then(function(r){return r.arrayBuffer();}).catch(function(){return null;}); }
  function applyMerged(buf, download){ var dl=document.getElementById('download-btn'); var url=URL.createObjectURL(new Blob([buf],{type:'application/octet-stream'})); if(dl) dl.setAttribute('href',url); if(window.__jwUpdateMergedCache) window.__jwUpdateMergedCache(buf); if(download&&dl){ try{ dl.click(); }catch(_){ } } }

  var toastEl=null, toastT=null;
  function toast(msg, isErr){ if(toastEl){ try{toastEl.remove();}catch(_){ } } toastEl=document.createElement('div'); toastEl.className='jwr-toast'; toastEl.style.borderColor=isErr?'rgba(248,113,113,.6)':'rgba(234,88,12,.5)'; toastEl.textContent=msg; document.body.appendChild(toastEl); if(toastT) clearTimeout(toastT); toastT=setTimeout(function(){ if(toastEl){try{toastEl.remove();}catch(_){ }} toastEl=null; }, 4200); }

  // overlap chooser → resolves 'layer' | 'note' | 'cancel'; lists the clashing notes
  function promptOverlap(n, conflicts){
    return new Promise(function(resolve){
      var L=T(); conflicts=conflicts||[];
      var listHTML=''; for(var i=0;i<conflicts.length&&i<200;i++) listHTML+=noteRow(conflicts[i]); if(conflicts.length>200) listHTML+='<div class="jwr-more">'+esc(fmt(L.more_hint,conflicts.length-200))+'</div>';
      var ov=document.createElement('div'); ov.className='jwr-modal';
      ov.innerHTML='<div class="jwr-modal-card jwr-modal-lg"><div class="jwr-modal-h">'+esc(L.pm_title)+'</div><p class="jwr-modal-q">'+esc(fmt(L.ov_q,n))+'</p><p class="jwr-modal-q" style="margin-bottom:8px">'+esc(L.conf_intro)+'</p><div class="jwr-list">'+listHTML+'</div><div class="jwr-modal-foot"><button class="jwr-mb jwr-mb-primary" data-m="layer">'+esc(L.ov_layer)+'</button><button class="jwr-mb" data-m="note">'+esc(L.ov_note)+'</button></div></div>';
      function done(m){ try{ov.remove();}catch(_){ } resolve(m); }
      ov.addEventListener('click',function(e){ var b=e.target.closest&&e.target.closest('[data-m]'); if(b){ done(b.getAttribute('data-m')); return; } if(e.target===ov) done('cancel'); });
      document.body.appendChild(ov);
    });
  }
  function importTag(){ var inp=document.getElementById('jwr-tag'); var v=inp?String(inp.value||'').trim():''; return v || window.__jwImportTag || T().shared_tag; }

  function pickFile(cb){ var inp=document.createElement('input'); inp.type='file'; inp.accept='.json,.jwshare.json,application/json'; inp.style.display='none'; document.body.appendChild(inp); inp.addEventListener('change',function(){ if(inp.files&&inp.files[0]) cb(inp.files[0]); try{inp.remove();}catch(_){ } }); inp.click(); }

  // end-of-merge: pick a share file and adopt into the merged result
  window.__jwReceivePickAndAdopt=function(){ pickFile(function(file){ readShareFile(file).then(function(notes){ if(!notes||!notes.length){ toast(T().invalid, true); return; } getMergedBuffer().then(function(buf){ if(!buf){ toast(T().invalid, true); return; } toast(T().adding); adoptIntoBuffer(buf, notes, {tagLabel:importTag(), onOverlap:promptOverlap}).then(function(res){ if(res.cancelled) return; applyMerged(res.buffer, false); toast(fmt(T().added, res.added)); openSummary(res.imported); }).catch(function(){ toast(T().invalid, true); }); }); }); }); };

  // pre-merge: auto-adopt any attached shared notes when the celebration shows
  window.__jwReceiveOnCelebration=function(ov){ var pending=window.__jwSharedNotes; window.__jwSharedNotes=null; if(!pending||!pending.length) return; getMergedBuffer().then(function(buf){ if(!buf) return; toast(T().adding); adoptIntoBuffer(buf, pending, {tagLabel:(window.__jwImportTag||T().shared_tag), onOverlap:promptOverlap}).then(function(res){ if(res.cancelled) return; applyMerged(res.buffer, false); toast(fmt(T().added, res.added)); openSummary(res.imported); }).catch(function(){ }); }); };

  // pre-merge attach UI on the merge screen
  function setPanelStatus(panel,msg,isErr){ if(!panel) return; var s=panel.querySelector('.jwr-status'); if(!s) return; s.style.display='flex'; s.style.color=isErr?'#f87171':'#4ade80'; s.innerHTML=(isErr?'':'<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>')+'<span>'+esc(msg)+'</span>'; if(!isErr){ var pv=document.createElement('button'); pv.className='jwr-prev-link'; pv.textContent=T().preview; pv.onclick=function(){ if(window.__jwSharedNotes&&window.__jwSharedNotes.length) openPreview(window.__jwSharedNotes); }; s.appendChild(pv); var rm=document.createElement('button'); rm.className='jwr-rm'; rm.textContent=T().pm_remove; rm.onclick=function(){ window.__jwSharedNotes=null; s.style.display='none'; var inp=panel.querySelector('input[type=file]'); if(inp) inp.value=''; }; s.appendChild(rm); } }
  window.__jwLoadSharedFile=function(file, panel){ readShareFile(file).then(function(notes){ if(!notes){ setPanelStatus(panel, T().invalid, true); return; } window.__jwSharedNotes=notes; setPanelStatus(panel, fmt(T().pm_loaded, notes.length), false); }); };
  function injectPanel(){ var btn=document.getElementById('start-merge-btn'); if(!btn||document.getElementById('jwr-panel')) return; var panel=document.createElement('div'); panel.id='jwr-panel'; panel.className='jwr-panel'; var L=T(); panel.innerHTML='<div class="jwr-panel-h"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"/></svg><span>'+esc(L.pm_title)+'</span></div><div class="jwr-panel-hint">'+esc(L.pm_hint)+'</div><label class="jwr-choose">'+esc(L.pm_choose)+'<input type="file" accept=".json,.jwshare.json,application/json" style="display:none"></label><div class="jwr-tag-row"><label class="jwr-tag-label" for="jwr-tag">'+esc(L.tag_label)+'</label><input id="jwr-tag" class="jwr-tag-input" type="text" value="'+esc(L.shared_tag)+'" maxlength="60"></div><div class="jwr-safe"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><span>'+esc(L.pm_safe)+'</span></div><div class="jwr-status" style="display:none"></div>'; var inp=panel.querySelector('input[type=file]'); inp.addEventListener('change',function(){ if(inp.files&&inp.files[0]) window.__jwLoadSharedFile(inp.files[0], panel); }); var tagInp=panel.querySelector('#jwr-tag'); window.__jwImportTag=tagInp.value; tagInp.addEventListener('input',function(){ window.__jwImportTag=String(tagInp.value||'').trim()||T().shared_tag; }); btn.parentNode.insertBefore(panel, btn); if(window.__jwSharedNotes&&window.__jwSharedNotes.length) setPanelStatus(panel, fmt(L.pm_loaded, window.__jwSharedNotes.length), false); }
  try{ var mo=new MutationObserver(function(){ injectPanel(); }); mo.observe(document.documentElement,{childList:true,subtree:true}); }catch(_){ }
  window.__jwPromptOverlap=promptOverlap; window.__jwOpenPreview=openPreview; window.__jwOpenSummary=openSummary; // for tests
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',injectPanel); else injectPanel();
})();

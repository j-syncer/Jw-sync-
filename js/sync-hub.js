/* ──────────────────────────────────────────────────────────────────────────
   sync-hub.js — Saved Devices & Auto-Sync hub (window.__jwOpenSyncHub).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function(){
  "use strict";
  if (window.__jwOpenSyncHub) return;

  /* ── i18n (10 languages; AI-assisted non-English strings — review welcome) ── */
  var I18N = {
    en:{title:"Saved Devices & Auto-Sync",intro:"Save each device's backup here once. Then re-merge everything with one click — no re-uploading.",priv:"Your files stay in this browser only (IndexedDB). Nothing is ever uploaded.",add:"Add a device backup",empty:"No saved devices yet. Add your first backup above.",main:"Main",setmain:"Set as main",remove:"Remove",saved:"Saved",mergenow:"Merge saved devices now",merging:"Merging…",done:"Merged! Your file is downloading.",needtwo:"Add at least two device backups to merge.",reminder:"Remind me to sync",off:"Off",weekly:"Weekly",monthly:"Monthly",clear:"Clear all saved devices",clearconfirm:"Remove all saved devices? This can't be undone.",banner:"It's been a while since your last sync. Merge your saved devices?",bannercta:"Open Sync",dismiss:"Dismiss",close:"Close",fab:"Sync",error:"Something went wrong during the merge. Please try again."},
    es:{title:"Dispositivos guardados y sincronización",intro:"Guarda aquí la copia de cada dispositivo una vez. Luego combina todo con un clic, sin volver a subir nada.",priv:"Tus archivos quedan solo en este navegador (IndexedDB). Nunca se suben.",add:"Añadir copia de un dispositivo",empty:"Aún no hay dispositivos guardados. Añade tu primera copia arriba.",main:"Principal",setmain:"Marcar como principal",remove:"Quitar",saved:"Guardado",mergenow:"Combinar dispositivos ahora",merging:"Combinando…",done:"¡Combinado! Tu archivo se está descargando.",needtwo:"Añade al menos dos copias para combinar.",reminder:"Recordarme sincronizar",off:"Nunca",weekly:"Semanal",monthly:"Mensual",clear:"Borrar todos los dispositivos",clearconfirm:"¿Borrar todos los dispositivos guardados? No se puede deshacer.",banner:"Hace tiempo de tu última sincronización. ¿Combinar tus dispositivos?",bannercta:"Abrir",dismiss:"Descartar",close:"Cerrar",fab:"Sincronizar",error:"Algo salió mal durante la combinación. Inténtalo de nuevo."},
    pt:{title:"Dispositivos salvos e sincronização",intro:"Salve aqui a cópia de cada dispositivo uma vez. Depois combine tudo com um clique, sem reenviar nada.",priv:"Seus arquivos ficam só neste navegador (IndexedDB). Nada é enviado.",add:"Adicionar cópia de um dispositivo",empty:"Nenhum dispositivo salvo ainda. Adicione sua primeira cópia acima.",main:"Principal",setmain:"Definir como principal",remove:"Remover",saved:"Salvo",mergenow:"Combinar dispositivos agora",merging:"Combinando…",done:"Combinado! Seu arquivo está sendo baixado.",needtwo:"Adicione pelo menos duas cópias para combinar.",reminder:"Lembrar de sincronizar",off:"Nunca",weekly:"Semanal",monthly:"Mensal",clear:"Apagar todos os dispositivos",clearconfirm:"Remover todos os dispositivos salvos? Isso não pode ser desfeito.",banner:"Faz tempo desde sua última sincronização. Combinar seus dispositivos?",bannercta:"Abrir",dismiss:"Dispensar",close:"Fechar",fab:"Sincronizar",error:"Algo deu errado durante a combinação. Tente novamente."},
    fr:{title:"Appareils enregistrés et synchro",intro:"Enregistrez ici la sauvegarde de chaque appareil une fois. Fusionnez ensuite tout d'un clic, sans rien re-téléverser.",priv:"Vos fichiers restent uniquement dans ce navigateur (IndexedDB). Rien n'est envoyé.",add:"Ajouter la sauvegarde d'un appareil",empty:"Aucun appareil enregistré. Ajoutez votre première sauvegarde ci-dessus.",main:"Principal",setmain:"Définir comme principal",remove:"Retirer",saved:"Enregistré",mergenow:"Fusionner les appareils",merging:"Fusion…",done:"Fusionné ! Votre fichier se télécharge.",needtwo:"Ajoutez au moins deux sauvegardes à fusionner.",reminder:"Me rappeler de synchroniser",off:"Jamais",weekly:"Hebdomadaire",monthly:"Mensuel",clear:"Effacer tous les appareils",clearconfirm:"Supprimer tous les appareils enregistrés ? Irréversible.",banner:"Cela fait un moment depuis votre dernière synchro. Fusionner vos appareils ?",bannercta:"Ouvrir",dismiss:"Ignorer",close:"Fermer",fab:"Synchro",error:"Une erreur est survenue pendant la fusion. Réessayez."},
    de:{title:"Gespeicherte Geräte & Auto-Sync",intro:"Sichere die Datei jedes Geräts einmal hier. Führe dann alles mit einem Klick zusammen — ohne erneutes Hochladen.",priv:"Deine Dateien bleiben nur in diesem Browser (IndexedDB). Nichts wird hochgeladen.",add:"Geräte-Backup hinzufügen",empty:"Noch keine gespeicherten Geräte. Füge oben dein erstes Backup hinzu.",main:"Haupt",setmain:"Als Haupt festlegen",remove:"Entfernen",saved:"Gespeichert",mergenow:"Geräte jetzt zusammenführen",merging:"Zusammenführen…",done:"Zusammengeführt! Deine Datei wird geladen.",needtwo:"Füge mindestens zwei Backups zum Zusammenführen hinzu.",reminder:"An Sync erinnern",off:"Nie",weekly:"Wöchentlich",monthly:"Monatlich",clear:"Alle Geräte löschen",clearconfirm:"Alle gespeicherten Geräte entfernen? Das kann nicht rückgängig gemacht werden.",banner:"Deine letzte Synchronisierung ist eine Weile her. Geräte zusammenführen?",bannercta:"Öffnen",dismiss:"Verwerfen",close:"Schließen",fab:"Sync",error:"Beim Zusammenführen ist etwas schiefgelaufen. Bitte erneut versuchen."},
    it:{title:"Dispositivi salvati e sincronizzazione",intro:"Salva qui il backup di ogni dispositivo una volta. Poi unisci tutto con un clic, senza ricaricare nulla.",priv:"I tuoi file restano solo in questo browser (IndexedDB). Niente viene caricato.",add:"Aggiungi backup di un dispositivo",empty:"Nessun dispositivo salvato. Aggiungi il primo backup sopra.",main:"Principale",setmain:"Imposta come principale",remove:"Rimuovi",saved:"Salvato",mergenow:"Unisci i dispositivi ora",merging:"Unione…",done:"Unito! Il file si sta scaricando.",needtwo:"Aggiungi almeno due backup da unire.",reminder:"Ricordami di sincronizzare",off:"Mai",weekly:"Settimanale",monthly:"Mensile",clear:"Cancella tutti i dispositivi",clearconfirm:"Rimuovere tutti i dispositivi salvati? Non si può annullare.",banner:"È passato un po' dall'ultima sincronizzazione. Unire i dispositivi?",bannercta:"Apri",dismiss:"Ignora",close:"Chiudi",fab:"Sincronizza",error:"Qualcosa è andato storto durante l'unione. Riprova."},
    ru:{title:"Сохранённые устройства и автосинхронизация",intro:"Сохраните копию каждого устройства один раз. Затем объединяйте всё одним щелчком — без повторной загрузки.",priv:"Ваши файлы остаются только в этом браузере (IndexedDB). Ничего не загружается на сервер.",add:"Добавить копию устройства",empty:"Пока нет сохранённых устройств. Добавьте первую копию выше.",main:"Основное",setmain:"Сделать основным",remove:"Удалить",saved:"Сохранено",mergenow:"Объединить устройства сейчас",merging:"Объединение…",done:"Объединено! Ваш файл загружается.",needtwo:"Добавьте хотя бы две копии для объединения.",reminder:"Напоминать о синхронизации",off:"Никогда",weekly:"Еженедельно",monthly:"Ежемесячно",clear:"Удалить все устройства",clearconfirm:"Удалить все сохранённые устройства? Это нельзя отменить.",banner:"Давно не было синхронизации. Объединить ваши устройства?",bannercta:"Открыть",dismiss:"Закрыть",close:"Закрыть",fab:"Синхр.",error:"Во время объединения произошла ошибка. Попробуйте ещё раз."},
    ja:{title:"保存済みデバイスと自動同期",intro:"各デバイスのバックアップを一度ここに保存。あとはワンクリックで再マージ — 再アップロード不要です。",priv:"ファイルはこのブラウザ内（IndexedDB）だけに保存され、アップロードされません。",add:"デバイスのバックアップを追加",empty:"保存済みのデバイスはまだありません。上から最初のバックアップを追加してください。",main:"メイン",setmain:"メインに設定",remove:"削除",saved:"保存日",mergenow:"保存済みデバイスをマージ",merging:"マージ中…",done:"マージ完了！ファイルをダウンロード中です。",needtwo:"マージするには2つ以上のバックアップを追加してください。",reminder:"同期のリマインド",off:"オフ",weekly:"毎週",monthly:"毎月",clear:"保存済みデバイスをすべて削除",clearconfirm:"保存済みデバイスをすべて削除しますか？元に戻せません。",banner:"前回の同期からしばらく経ちました。デバイスをマージしますか？",bannercta:"開く",dismiss:"閉じる",close:"閉じる",fab:"同期",error:"マージ中に問題が発生しました。もう一度お試しください。"},
    ko:{title:"저장된 기기 및 자동 동기화",intro:"각 기기의 백업을 한 번만 저장하세요. 그러면 다시 업로드 없이 한 번의 클릭으로 병합할 수 있습니다.",priv:"파일은 이 브라우저(IndexedDB)에만 저장되며 업로드되지 않습니다.",add:"기기 백업 추가",empty:"저장된 기기가 없습니다. 위에서 첫 백업을 추가하세요.",main:"메인",setmain:"메인으로 설정",remove:"제거",saved:"저장됨",mergenow:"저장된 기기 지금 병합",merging:"병합 중…",done:"병합 완료! 파일을 다운로드하는 중입니다.",needtwo:"병합하려면 백업을 두 개 이상 추가하세요.",reminder:"동기화 알림",off:"끄기",weekly:"매주",monthly:"매월",clear:"저장된 기기 모두 지우기",clearconfirm:"저장된 기기를 모두 제거하시겠습니까? 되돌릴 수 없습니다.",banner:"마지막 동기화 이후 시간이 지났습니다. 기기를 병합할까요?",bannercta:"열기",dismiss:"닫기",close:"닫기",fab:"동기화",error:"병합 중 문제가 발생했습니다. 다시 시도하세요."},
    tl:{title:"Naka-save na Device at Auto-Sync",intro:"I-save dito ang backup ng bawat device nang isang beses. Pagkatapos ay pagsamahin ang lahat sa isang click — walang muling pag-upload.",priv:"Nananatili ang iyong mga file sa browser na ito lang (IndexedDB). Walang ina-upload kahit kailan.",add:"Magdagdag ng backup ng device",empty:"Wala pang naka-save na device. Idagdag ang unang backup sa itaas.",main:"Pangunahin",setmain:"Itakda bilang pangunahin",remove:"Alisin",saved:"Na-save",mergenow:"Pagsamahin ang mga device ngayon",merging:"Pinagsasama…",done:"Pinagsama na! Dina-download na ang iyong file.",needtwo:"Magdagdag ng hindi bababa sa dalawang backup para pagsamahin.",reminder:"Ipaalala ang pag-sync",off:"Huwag",weekly:"Lingguhan",monthly:"Buwanan",clear:"Burahin lahat ng device",clearconfirm:"Alisin ang lahat ng naka-save na device? Hindi na maibabalik.",banner:"Matagal na mula sa huli mong pag-sync. Pagsamahin ang iyong mga device?",bannercta:"Buksan",dismiss:"I-dismiss",close:"Isara",fab:"Sync",error:"May naganap na problema habang nagsasama. Pakisubukang muli."}
  ,sv:{title:"Sparade enheter och autosynk",intro:"Spara varje enhets säkerhetskopia här en gång. Slå sedan ihop allt med ett klick — ingen ny uppladdning.",priv:"Dina filer stannar enbart i den här webbläsaren (IndexedDB). Inget laddas någonsin upp.",add:"Lägg till en enhetssäkerhetskopia",empty:"Inga sparade enheter än. Lägg till din första säkerhetskopia ovan.",main:"Huvud",setmain:"Ange som huvud",remove:"Ta bort",saved:"Sparad",mergenow:"Slå ihop sparade enheter nu",merging:"Slår ihop…",done:"Sammanslaget! Din fil laddas ner.",needtwo:"Lägg till minst två enhetssäkerhetskopior för att slå ihop.",reminder:"Påminn mig att synka",off:"Av",weekly:"Varje vecka",monthly:"Varje månad",clear:"Rensa alla sparade enheter",clearconfirm:"Ta bort alla sparade enheter? Det kan inte ångras.",banner:"Det var ett tag sedan du synkade. Slå ihop dina sparade enheter?",bannercta:"Öppna synk",dismiss:"Avfärda",close:"Stäng",fab:"Synk",error:"Något gick fel under sammanslagningen. Försök igen."},ceb:{title:"Naka-save nga Mga Device ug Auto-Sync",intro:"I-save dinhi ang backup sa matag device sa makausa. Unya isagol ang tanan sa usa ka click — walay muling pag-upload.",priv:"Nagpabilin ang imong mga file niini nga browser lamang (IndexedDB). Wala gayuy gi-upload.",add:"Magdugang ug backup sa device",empty:"Wala pay naka-save nga device. Idugang ang unang backup sa ibabaw.",main:"Pangunahin",setmain:"Itakda isip pangunahin",remove:"Tangtangon",saved:"Na-save",mergenow:"Isagol ang mga device karon",merging:"Gisagol…",done:"Gisagol na! Gi-download na ang imong file.",needtwo:"Magdugang ug labing menos duha ka backup aron isagol.",reminder:"Papaadunga ako sa pag-sync",off:"Dili",weekly:"Matag semana",monthly:"Matag bulan",clear:"Papason ang tanan nga naka-save nga device",clearconfirm:"Tangtangon ang tanan nga naka-save nga device? Dili na mapaulion.",banner:"Dugay na sukad sa imong katapusang pag-sync. Isagol ang imong mga device?",bannercta:"Buksa ang Sync",dismiss:"I-dismiss",close:"Isira",fab:"Sync",error:"Adunay nahinabo nga problema sa panahon sa merge. Palihug sulayi pag-usab."},pl:{title:"Zapisane urządzenia i autosynchronizacja",intro:"Zapisz tu raz kopię zapasową każdego urządzenia. Potem scalaj wszystko jednym kliknięciem — bez ponownego wczytywania.",priv:"Twoje pliki pozostają tylko w tej przeglądarce (IndexedDB). Nic nie jest wysyłane na serwer.",add:"Dodaj kopię zapasową urządzenia",empty:"Brak zapisanych urządzeń. Dodaj swoją pierwszą kopię powyżej.",main:"Główne",setmain:"Ustaw jako główne",remove:"Usuń",saved:"Zapisano",mergenow:"Scal teraz zapisane urządzenia",merging:"Scalanie…",done:"Scalono! Twój plik jest pobierany.",needtwo:"Aby scalić, dodaj co najmniej dwie kopie zapasowe urządzeń.",reminder:"Przypominaj o synchronizacji",off:"Wyłączone",weekly:"Co tydzień",monthly:"Co miesiąc",clear:"Wyczyść wszystkie zapisane urządzenia",clearconfirm:"Usunąć wszystkie zapisane urządzenia? Tej operacji nie można cofnąć.",banner:"Minęło sporo czasu od ostatniej synchronizacji. Scalić zapisane urządzenia?",bannercta:"Otwórz synchronizację",dismiss:"Zamknij",close:"Zamknij",fab:"Synchronizacja",error:"Coś poszło nie tak podczas scalania. Spróbuj ponownie."},uk:{title:"Збережені пристрої й автосинхронізація",intro:"Збережіть тут резервну копію кожного пристрою один раз. Далі об'єднуйте все одним натисканням — без повторного завантаження.",priv:"Ваші файли залишаються тільки в цьому браузері (IndexedDB). Нічого не надсилається на сервер.",add:"Додати резервну копію пристрою",empty:"Збережених пристроїв ще немає. Додайте свою першу копію вище.",main:"Основний",setmain:"Зробити основним",remove:"Вилучити",saved:"Збережено",mergenow:"Об'єднати збережені пристрої зараз",merging:"Об'єднуємо…",done:"Об'єднано! Ваш файл завантажується.",needtwo:"Щоб об'єднати, додайте щонайменше дві резервні копії пристроїв.",reminder:"Нагадувати про синхронізацію",off:"Вимкнено",weekly:"Щотижня",monthly:"Щомісяця",clear:"Очистити всі збережені пристрої",clearconfirm:"Вилучити всі збережені пристрої? Цю дію не можна скасувати.",banner:"Від останньої синхронізації минуло чимало часу. Об'єднати збережені пристрої?",bannercta:"Відкрити синхронізацію",dismiss:"Закрити",close:"Закрити",fab:"Синхронізація",error:"Під час об'єднання щось пішло не так. Спробуйте ще раз."},he:{title:"מכשירים שמורים וסנכרון אוטומטי",intro:"שמרו כאן פעם אחת את הגיבוי של כל מכשיר. אחר כך מזגו הכול מחדש בלחיצה אחת — בלי להעלות שוב.",priv:"הקבצים שלכם נשארים בדפדפן הזה בלבד (IndexedDB). שום דבר לא מועלה לשרת.",add:"הוספת גיבוי של מכשיר",empty:"אין עדיין מכשירים שמורים. הוסיפו את הגיבוי הראשון שלכם למעלה.",main:"ראשי",setmain:"הגדרה כראשי",remove:"הסרה",saved:"נשמר",mergenow:"מזגו עכשיו את המכשירים השמורים",merging:"ממזג…",done:"מוזג! הקובץ שלכם יורד.",needtwo:"הוסיפו לפחות שני גיבויי מכשירים כדי למזג.",reminder:"הזכירו לי לסנכרן",off:"כבוי",weekly:"שבועי",monthly:"חודשי",clear:"מחיקת כל המכשירים השמורים",clearconfirm:"להסיר את כל המכשירים השמורים? אי אפשר לבטל את הפעולה.",banner:"עבר זמן מאז הסנכרון האחרון שלכם. למזג את המכשירים השמורים?",bannercta:"פתיחת הסנכרון",dismiss:"ביטול",close:"סגירה",fab:"סנכרון",error:"משהו השתבש במהלך המיזוג. נסו שוב."},ar:{title:"الأجهزة المحفوظة والمزامنة التلقائية",intro:"احفظ هنا النسخة الاحتياطية لكل جهاز مرة واحدة. ثم أعِد دمج كل شيء بنقرة واحدة — بلا رفع مجدّد.",priv:"تبقى ملفاتك داخل هذا المتصفح فقط (IndexedDB). لا يُرفع أي شيء إطلاقًا.",add:"أضف نسخة احتياطية لجهاز",empty:"لا توجد أجهزة محفوظة بعد. أضف نسختك الاحتياطية الأولى أعلاه.",main:"رئيسي",setmain:"اجعله الرئيسي",remove:"إزالة",saved:"محفوظ",mergenow:"ادمج الأجهزة المحفوظة الآن",merging:"جارٍ الدمج…",done:"تم الدمج! جارٍ تنزيل ملفك.",needtwo:"أضف نسختين احتياطيتين على الأقل لتتمكن من الدمج.",reminder:"ذكّرني بالمزامنة",off:"معطّل",weekly:"أسبوعيًا",monthly:"شهريًا",clear:"امسح كل الأجهزة المحفوظة",clearconfirm:"هل تريد إزالة كل الأجهزة المحفوظة؟ لا يمكن التراجع عن هذا.",banner:"مضى وقت على آخر مزامنة لك. هل تريد دمج أجهزتك المحفوظة؟",bannercta:"افتح المزامنة",dismiss:"تجاهل",close:"إغلاق",fab:"مزامنة",error:"حدث خطأ ما أثناء الدمج. حاول مرة أخرى."}};
  function lang(){ try{ var l=localStorage.getItem('jwsync_lang'); return (l&&I18N[l])?l:'en'; }catch(_){ return 'en'; } }
  function t(k){ var L=I18N[lang()]||I18N.en; return L[k]!=null?L[k]:(I18N.en[k]!=null?I18N.en[k]:k); }
  function esc(s){ return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];}); }

  /* ── Persistent prefs (cadence + last sync) ── */
  var PK='jwsync_synchub';
  function prefs(){ try{ var d=localStorage.getItem(PK); return d?JSON.parse(d):{cadence:'off',lastSync:0,mainId:null}; }catch(_){ return {cadence:'off',lastSync:0,mainId:null}; } }
  function savePrefs(p){ try{ localStorage.setItem(PK, JSON.stringify(p)); }catch(_){} }

  /* ── IndexedDB store for device backups (own DB; no clash with app's jwsync_db) ── */
  var DB='jwsync_synchub_db', STORE='devices';
  function open(){ return new Promise(function(res,rej){ try{ var r=indexedDB.open(DB,1);
    r.onupgradeneeded=function(){ var db=r.result; if(!db.objectStoreNames.contains(STORE)) db.createObjectStore(STORE,{keyPath:'id'}); };
    r.onsuccess=function(){ res(r.result); }; r.onerror=function(){ rej(r.error); }; }catch(e){ rej(e); } }); }
  function putDevice(d){ return open().then(function(db){ return new Promise(function(res,rej){ var tx=db.transaction(STORE,'readwrite'); tx.objectStore(STORE).put(d); tx.oncomplete=function(){ db.close(); res(true); }; tx.onerror=function(){ db.close(); rej(tx.error); }; }); }); }
  function getDevices(){ return open().then(function(db){ return new Promise(function(res){ var g=db.transaction(STORE,'readonly').objectStore(STORE).getAll(); g.onsuccess=function(){ db.close(); res((g.result||[]).sort(function(a,b){return (a.savedAt||0)-(b.savedAt||0);})); }; g.onerror=function(){ db.close(); res([]); }; }); }).catch(function(){ return []; }); }
  function delDevice(id){ return open().then(function(db){ return new Promise(function(res){ var tx=db.transaction(STORE,'readwrite'); tx.objectStore(STORE).delete(id); tx.oncomplete=function(){ db.close(); res(true); }; tx.onerror=function(){ db.close(); res(false); }; }); }).catch(function(){ return false; }); }
  function clearDevices(){ return open().then(function(db){ return new Promise(function(res){ var tx=db.transaction(STORE,'readwrite'); tx.objectStore(STORE).clear(); tx.oncomplete=function(){ db.close(); res(true); }; tx.onerror=function(){ db.close(); res(false); }; }); }).catch(function(){ return false; }); }

  function fmtDate(ts){ try{ return new Date(ts).toLocaleDateString(undefined,{year:'numeric',month:'short',day:'numeric'}); }catch(_){ return ''; } }

  var overlay=null, busy=false;

  function close(){ if(overlay){ overlay.remove(); overlay=null; } document.removeEventListener('keydown',onKey); }
  function onKey(e){ if(e.key==='Escape'&&!busy) close(); }

  function pickMain(devices){
    var p=prefs();
    if(p.mainId && devices.some(function(d){return d.id===p.mainId;})) return p.mainId;
    return devices.length?devices[0].id:null;
  }

  function setStatus(msg,cls){ if(!overlay) return; var s=overlay.querySelector('.jsh-status'); if(s){ s.textContent=msg||''; s.className='jsh-status'+(cls?' '+cls:''); } }

  function doMerge(devices){
    if(busy) return;
    if(devices.length<2){ setStatus(t('needtwo'),'err'); return; }
    var mainId=pickMain(devices);
    var main=devices.filter(function(d){return d.id===mainId;})[0];
    var secs=devices.filter(function(d){return d.id!==mainId;}).map(function(d){return {buffer:d.buffer.slice(0),name:d.name};});
    busy=true;
    if(window.__jwHaptic) window.__jwHaptic(20);
    var mergeBtn=overlay&&overlay.querySelector('.jsh-merge'); if(mergeBtn) mergeBtn.disabled=true;
    setStatus(t('merging'),'');
    var w;
    try{ w=new Worker('./js/merge-worker.js'); }catch(e){ busy=false; setStatus(t('error'),'err'); if(mergeBtn) mergeBtn.disabled=false; return; }
    w.onmessage=function(ev){
      var d=ev.data||{};
      if(d.type==='done'){
        try{
          var blob=new Blob([d.zipBuffer],{type:'application/octet-stream'});
          var url=URL.createObjectURL(blob);
          var a=document.createElement('a');
          var base=(main&&main.name?main.name.replace(/\.jwlibrary$/i,''):'backup');
          a.href=url; a.download='merged_'+base+'.jwlibrary';
          document.body.appendChild(a); a.click(); a.remove();
          setTimeout(function(){ URL.revokeObjectURL(url); },4000);
          var p=prefs(); p.lastSync=Date.now(); savePrefs(p);
          setStatus(t('done'),'ok');
          dismissReminder();
        }catch(e){ setStatus(t('error'),'err'); }
        busy=false; if(mergeBtn) mergeBtn.disabled=false; w.terminate();
      } else if(d.type==='error'){
        setStatus(d.message||t('error'),'err'); busy=false; if(mergeBtn) mergeBtn.disabled=false; w.terminate();
      } else if(d.type==='impact'){
        /* auto-confirm: this path is an explicit one-click merge */
        w.postMessage({type:'confirmMerge'});
      } else if(d.type==='progress' && d.payload && d.payload.label){
        setStatus(d.payload.label,'');
      }
    };
    w.onerror=function(){ setStatus(t('error'),'err'); busy=false; if(mergeBtn) mergeBtn.disabled=false; try{w.terminate();}catch(_){} };
    var opts={mergeNotes:true,mergeHighlights:true,mergeBookmarks:true,mergeTags:true,smartDedupe:true,
      conflictStrategy:'newest',previewConfirm:false,syncByDate:false,filterDate:'',deepClean:false};
    w.postMessage({type:'merge',mainBuffer:main.buffer.slice(0),mainName:main.name,secondaryFiles:secs,opts:opts,tagManager:{},colorRules:[]});
  }

  function render(devices){
    var p=prefs(), mainId=pickMain(devices);
    var rows=devices.map(function(d){
      var isMain=d.id===mainId;
      return '<li class="jsh-row'+(isMain?' is-main':'')+'" data-id="'+esc(d.id)+'">'+
        '<div class="jsh-row-name">'+esc(d.name)+
          '<div class="jsh-row-meta">'+esc(t('saved'))+' '+esc(fmtDate(d.savedAt))+'</div></div>'+
        (isMain?'<span class="jsh-badge">'+esc(t('main'))+'</span>'
               :'<button class="jsh-setmain" data-setmain="'+esc(d.id)+'">'+esc(t('setmain'))+'</button>')+
        '<button class="jsh-rm" data-rm="'+esc(d.id)+'" title="'+esc(t('remove'))+'">&times;</button>'+
      '</li>';
    }).join('');
    var listHtml = devices.length
      ? '<ul class="jsh-list">'+rows+'</ul>'
      : '<div class="jsh-empty">'+esc(t('empty'))+'</div>';
    var cad=p.cadence||'off';
    return ''+
      '<div class="jsh-panel" role="dialog" aria-modal="true" aria-label="'+esc(t('title'))+'">'+
        '<div class="jsh-head"><h2 class="jsh-title">'+esc(t('title'))+'</h2>'+
          '<button class="jsh-x" data-close title="'+esc(t('close'))+'">&times;</button></div>'+
        '<p class="jsh-intro">'+esc(t('intro'))+'</p>'+
        listHtml+
        '<button class="jsh-add" data-add type="button"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>'+esc(t('add'))+'</button>'+
        '<button class="jsh-merge" data-merge type="button"'+(devices.length<2?' disabled':'')+'>'+esc(t('mergenow'))+'</button>'+
        '<p class="jsh-status"></p>'+
        '<p class="jsh-priv"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" style="flex:0 0 auto;margin-top:1px"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'+esc(t('priv'))+'</p>'+
        '<hr class="jsh-divider">'+
        '<div class="jsh-field"><label>'+esc(t('reminder'))+'</label>'+
          '<select class="jsh-select" data-cadence>'+
            '<option value="off"'+(cad==='off'?' selected':'')+'>'+esc(t('off'))+'</option>'+
            '<option value="weekly"'+(cad==='weekly'?' selected':'')+'>'+esc(t('weekly'))+'</option>'+
            '<option value="monthly"'+(cad==='monthly'?' selected':'')+'>'+esc(t('monthly'))+'</option>'+
          '</select></div>'+
        (devices.length?'<button class="jsh-clear" data-clear type="button">'+esc(t('clear'))+'</button>':'')+
      '</div>';
  }

  function refresh(){
    return getDevices().then(function(devices){
      if(!overlay) return;
      overlay.innerHTML=render(devices);
      wire(devices);
    });
  }

  function wire(devices){
    var panel=overlay.querySelector('.jsh-panel');
    overlay.querySelector('[data-close]').addEventListener('click',function(){ if(!busy) close(); });
    overlay.addEventListener('mousedown',function(e){ if(e.target===overlay&&!busy) close(); });
    var addBtn=overlay.querySelector('[data-add]');
    if(addBtn) addBtn.addEventListener('click',function(){
      var fi=document.createElement('input'); fi.type='file'; fi.accept='.jwlibrary,application/octet-stream';
      fi.onchange=function(){ var f=fi.files&&fi.files[0]; if(!f) return;
        f.arrayBuffer().then(function(buf){
          return putDevice({id:'dev_'+Date.now()+'_'+Math.random().toString(36).slice(2,7),name:f.name,buffer:buf,savedAt:Date.now()});
        }).then(refresh).catch(function(){ setStatus(t('error'),'err'); });
      };
      fi.click();
    });
    var mergeBtn=overlay.querySelector('[data-merge]');
    if(mergeBtn) mergeBtn.addEventListener('click',function(){ doMerge(devices); });
    Array.prototype.forEach.call(overlay.querySelectorAll('[data-setmain]'),function(b){
      b.addEventListener('click',function(){ var p=prefs(); p.mainId=b.getAttribute('data-setmain'); savePrefs(p); refresh(); });
    });
    Array.prototype.forEach.call(overlay.querySelectorAll('[data-rm]'),function(b){
      b.addEventListener('click',function(){ delDevice(b.getAttribute('data-rm')).then(refresh); });
    });
    var cadSel=overlay.querySelector('[data-cadence]');
    if(cadSel) cadSel.addEventListener('change',function(){ var p=prefs(); p.cadence=cadSel.value; savePrefs(p); });
    var clr=overlay.querySelector('[data-clear]');
    if(clr) clr.addEventListener('click',function(){ if(window.confirm(t('clearconfirm'))){ clearDevices().then(function(){ var p=prefs(); p.mainId=null; savePrefs(p); refresh(); }); } });
  }

  function openHub(){
    if(overlay) return;
    overlay=document.createElement('div'); overlay.className='jsh-overlay'; overlay.id='jw-synchub-overlay';
    document.body.appendChild(overlay);
    document.addEventListener('keydown',onKey);
    refresh();
  }
  window.__jwOpenSyncHub=openHub;

  /* ── Floating launcher ── */
  function addFab(){
    if(document.getElementById('jw-synchub-fab')) return;
    var b=document.createElement('button'); b.id='jw-synchub-fab'; b.className='jsh-fab'; b.type='button';
    b.setAttribute('aria-label',t('title'));
    b.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg><span>'+esc(t('fab'))+'</span>';
    b.addEventListener('click',openHub);
    document.body.appendChild(b);
  }

  /* ── Sync reminder banner ── */
  function dismissReminder(){ var r=document.getElementById('jw-synchub-reminder'); if(r) r.remove(); }
  function maybeReminder(){
    var p=prefs(); if(!p.cadence||p.cadence==='off') return;
    var span=p.cadence==='weekly'?7*864e5:30*864e5;
    if(!p.lastSync||Date.now()-p.lastSync<span) return;
    getDevices().then(function(devices){
      if(devices.length<2||document.getElementById('jw-synchub-reminder')) return;
      var r=document.createElement('div'); r.id='jw-synchub-reminder'; r.className='jsh-reminder';
      r.innerHTML='<span>'+esc(t('banner'))+'</span>'+
        '<button class="jsh-reminder-cta" type="button" data-open>'+esc(t('bannercta'))+'</button>'+
        '<button class="jsh-reminder-x" type="button" data-x aria-label="'+esc(t('dismiss'))+'">&times;</button>';
      document.body.appendChild(r);
      r.querySelector('[data-open]').addEventListener('click',function(){ dismissReminder(); openHub(); });
      r.querySelector('[data-x]').addEventListener('click',dismissReminder);
    });
  }

  function init(){ addFab(); setTimeout(maybeReminder,1500); }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init);
  else init();
})();

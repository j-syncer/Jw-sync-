/* ──────────────────────────────────────────────────────────────────────────
   wizard.js — Three-step "How it works" wizard (window.__jwOpenWizard).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.4.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function(){
  if(window.__jwWizardInit)return; window.__jwWizardInit=true;
  var W={
   en:{close:'Close',badge:'100% private — your files never leave this device',how:'How it works',title:'Merge your library in 3 steps',sub:'Everything happens on your device. Your files are never uploaded.',s1t:'Export your backups',s1d:'In JW Library on each device, create a backup and save the .jwlibrary files.',s1btn:'Show me how',s2t:'Add & merge',s2d:'Add your main backup, then the others, and tap Merge.',s3t:'Restore',s3d:'Download the merged file and restore it in JW Library.',s3btn:'Restore guide',start:'Get started',skip:'Skip',tab1:'Merging',tab2:'Other tools',t_intro:'JW Sync includes a few more tools — here’s what each one does:',exp_d:'Open any backup to search, read, edit and tag your notes, change highlight colours, and find notes by meaning with Ask Your Library — then save back to a .jwlibrary file.',stat_d:'Load a backup to see your study totals, streaks and trends, plus an Awards tab with medals you earn for reaching study milestones.',shr_d:'Send chosen notes to a friend as a small share file, or add notes a friend sent you — without merging whole backups.',open:'Open'},
   es:{close:'Cerrar',badge:'100% privado — tus archivos nunca salen de este dispositivo',how:'Cómo funciona',title:'Combina tu biblioteca en 3 pasos',sub:'Todo ocurre en tu dispositivo. Tus archivos nunca se suben.',s1t:'Exporta tus copias',s1d:'En JW Library, crea una copia en cada dispositivo y guarda los archivos .jwlibrary.',s1btn:'Ver cómo',s2t:'Añade y combina',s2d:'Añade tu copia principal, luego las demás y toca Combinar.',s3t:'Restaura',s3d:'Descarga el archivo combinado y restáuralo en JW Library.',s3btn:'Guía de restauración',start:'Empezar',skip:'Omitir',tab1:'Combinar',tab2:'Otras herramientas',t_intro:'JW Sync incluye algunas herramientas más; esto hace cada una:',exp_d:'Abre cualquier copia para buscar, leer, editar y etiquetar tus notas, cambiar colores de resaltado y encontrar notas por significado con Pregunta a tu biblioteca; luego guarda en un archivo .jwlibrary.',stat_d:'Carga una copia para ver tus totales, rachas y tendencias de estudio, además de una pestaña de Logros con medallas que ganas al alcanzar metas.',shr_d:'Envía notas concretas a un amigo como un pequeño archivo, o añade las notas que te enviaron, sin combinar copias enteras.',open:'Abrir'},
   pt:{close:'Fechar',badge:'100% privado — seus arquivos nunca saem deste dispositivo',how:'Como funciona',title:'Combine sua biblioteca em 3 passos',sub:'Tudo acontece no seu dispositivo. Seus arquivos nunca são enviados.',s1t:'Exporte seus backups',s1d:'No JW Library, faça um backup em cada dispositivo e salve os arquivos .jwlibrary.',s1btn:'Ver como',s2t:'Adicione e combine',s2d:'Adicione o backup principal, depois os outros, e toque em Combinar.',s3t:'Restaure',s3d:'Baixe o arquivo combinado e restaure-o no JW Library.',s3btn:'Guia de restauração',start:'Começar',skip:'Pular',tab1:'Combinar',tab2:'Outras ferramentas',t_intro:'O JW Sync inclui mais algumas ferramentas — veja o que cada uma faz:',exp_d:'Abra qualquer backup para pesquisar, ler, editar e marcar suas notas, mudar as cores dos destaques e encontrar notas por significado com o Pergunte à sua biblioteca; depois salve em um arquivo .jwlibrary.',stat_d:'Carregue um backup para ver seus totais, sequências e tendências de estudo, além de uma aba de Conquistas com medalhas por alcançar marcos.',shr_d:'Envie notas específicas a um amigo como um pequeno arquivo, ou adicione as notas que enviaram a você — sem combinar backups inteiros.',open:'Abrir'},
   fr:{close:'Fermer',badge:'100% privé — vos fichiers ne quittent jamais cet appareil',how:'Comment ça marche',title:'Fusionnez votre bibliothèque en 3 étapes',sub:'Tout se passe sur votre appareil. Vos fichiers ne sont jamais envoyés.',s1t:'Exportez vos sauvegardes',s1d:'Dans JW Library, créez une sauvegarde sur chaque appareil et enregistrez les fichiers .jwlibrary.',s1btn:'Voir comment',s2t:'Ajoutez et fusionnez',s2d:'Ajoutez votre sauvegarde principale, puis les autres, et appuyez sur Fusionner.',s3t:'Restaurez',s3d:'Téléchargez le fichier fusionné et restaurez-le dans JW Library.',s3btn:'Guide de restauration',start:'Commencer',skip:'Ignorer',tab1:'Fusion',tab2:'Autres outils',t_intro:'JW Sync propose quelques autres outils — voici ce que fait chacun :',exp_d:'Ouvrez une sauvegarde pour rechercher, lire, modifier et étiqueter vos notes, changer les couleurs de surlignage et retrouver des notes par leur sens avec Interrogez votre bibliothèque, puis enregistrez dans un fichier .jwlibrary.',stat_d:'Chargez une sauvegarde pour voir vos totaux, séries et tendances d’étude, ainsi qu’un onglet Récompenses avec des médailles gagnées en atteignant des objectifs.',shr_d:'Envoyez des notes choisies à un ami sous forme d’un petit fichier de partage, ou ajoutez celles qu’un ami vous a envoyées — sans fusionner des sauvegardes entières.',open:'Ouvrir'},
   de:{close:'Schließen',badge:'100% privat — deine Dateien verlassen nie dieses Gerät',how:'So funktioniert’s',title:'Führe deine Bibliothek in 3 Schritten zusammen',sub:'Alles geschieht auf deinem Gerät. Deine Dateien werden nie hochgeladen.',s1t:'Exportiere deine Sicherungen',s1d:'Erstelle in JW Library auf jedem Gerät eine Sicherung und speichere die .jwlibrary-Dateien.',s1btn:'Anleitung ansehen',s2t:'Hinzufügen & zusammenführen',s2d:'Füge deine Hauptsicherung hinzu, dann die anderen, und tippe auf Zusammenführen.',s3t:'Wiederherstellen',s3d:'Lade die zusammengeführte Datei herunter und stelle sie in JW Library wieder her.',s3btn:'Wiederherstellungs-Anleitung',start:'Loslegen',skip:'Überspringen',tab1:'Zusammenführen',tab2:'Weitere Tools',t_intro:'JW Sync bietet noch einige weitere Tools — das macht jedes davon:',exp_d:'Öffne eine Sicherung, um deine Notizen zu durchsuchen, zu lesen, zu bearbeiten und zu verschlagworten, Markierungsfarben zu ändern und Notizen mit „Frag deine Bibliothek“ nach Sinn zu finden — und speichere dann als .jwlibrary-Datei.',stat_d:'Lade eine Sicherung, um deine Studiensummen, Serien und Trends zu sehen, sowie einen Auszeichnungen-Tab mit Medaillen für erreichte Meilensteine.',shr_d:'Sende ausgewählte Notizen als kleine Teilen-Datei an einen Freund oder füge Notizen hinzu, die dir jemand gesendet hat — ohne ganze Sicherungen zusammenzuführen.',open:'Öffnen'},
   it:{close:'Chiudi',badge:'100% privato — i tuoi file non lasciano mai questo dispositivo',how:'Come funziona',title:'Unisci la tua biblioteca in 3 passaggi',sub:'Tutto avviene sul tuo dispositivo. I tuoi file non vengono mai caricati.',s1t:'Esporta i tuoi backup',s1d:'In JW Library, crea un backup su ogni dispositivo e salva i file .jwlibrary.',s1btn:'Mostrami come',s2t:'Aggiungi e unisci',s2d:'Aggiungi il backup principale, poi gli altri, e tocca Unisci.',s3t:'Ripristina',s3d:'Scarica il file unito e ripristinalo in JW Library.',s3btn:'Guida al ripristino',start:'Inizia',skip:'Salta',tab1:'Unione',tab2:'Altri strumenti',t_intro:'JW Sync include altri strumenti — ecco cosa fa ciascuno:',exp_d:'Apri un backup per cercare, leggere, modificare ed etichettare le note, cambiare i colori delle evidenziazioni e trovare note per significato con Chiedi alla tua biblioteca, poi salva in un file .jwlibrary.',stat_d:'Carica un backup per vedere totali, serie e tendenze di studio, oltre a una scheda Riconoscimenti con medaglie che ottieni raggiungendo traguardi.',shr_d:'Invia note scelte a un amico come piccolo file di condivisione, o aggiungi le note che ti hanno inviato — senza unire interi backup.',open:'Apri'},
   ru:{close:'Закрыть',badge:'100% конфиденциально — ваши файлы не покидают это устройство',how:'Как это работает',title:'Объедините библиотеку за 3 шага',sub:'Всё происходит на вашем устройстве. Ваши файлы никогда не загружаются.',s1t:'Экспортируйте резервные копии',s1d:'В JW Library создайте резервную копию на каждом устройстве и сохраните файлы .jwlibrary.',s1btn:'Показать как',s2t:'Добавьте и объедините',s2d:'Добавьте основную копию, затем остальные и нажмите «Объединить».',s3t:'Восстановите',s3d:'Скачайте объединённый файл и восстановите его в JW Library.',s3btn:'Инструкция по восстановлению',start:'Начать',skip:'Пропустить',tab1:'Объединение',tab2:'Другие инструменты',t_intro:'В JW Sync есть ещё несколько инструментов — вот что делает каждый:',exp_d:'Откройте любую копию, чтобы искать, читать, редактировать и помечать заметки, менять цвета выделений и находить заметки по смыслу с «Спросите свою библиотеку», затем сохраните в файл .jwlibrary.',stat_d:'Загрузите копию, чтобы увидеть итоги, серии и тенденции изучения, а также вкладку «Награды» с медалями за достижение этапов.',shr_d:'Отправьте выбранные заметки другу небольшим файлом или добавьте заметки, которые прислали вам, — без объединения целых копий.',open:'Открыть'},
   ja:{close:'閉じる',badge:'100%プライベート — ファイルはこの端末から出ません',how:'使い方',title:'3ステップでライブラリを統合',sub:'すべて端末内で処理されます。ファイルがアップロードされることはありません。',s1t:'バックアップを書き出す',s1d:'JW Libraryで各端末のバックアップを作成し、.jwlibraryファイルを保存します。',s1btn:'方法を見る',s2t:'追加して統合',s2d:'メインのバックアップを追加し、続けて他のファイルを追加して「統合」をタップします。',s3t:'復元する',s3d:'統合したファイルをダウンロードし、JW Libraryで復元します。',s3btn:'復元ガイド',start:'はじめる',skip:'スキップ',tab1:'統合',tab2:'その他のツール',t_intro:'JW Syncには他にもツールがあります。それぞれの機能は次のとおりです：',exp_d:'バックアップを開いて、ノートの検索・閲覧・編集・タグ付け、ハイライト色の変更ができ、「ライブラリに質問」で意味からノートを探せます。編集後は.jwlibraryファイルに保存します。',stat_d:'バックアップを読み込むと、学習の合計・連続記録・傾向に加え、節目で獲得するメダルを集めた「アワード」タブを確認できます。',shr_d:'選んだノートを小さな共有ファイルとして友だちに送ったり、友だちから届いたノートを追加したりできます（バックアップ全体を統合せずに）。',open:'開く'},
   ko:{close:'닫기',badge:'100% 비공개 — 파일이 이 기기를 벗어나지 않습니다',how:'사용 방법',title:'3단계로 라이브러리 병합',sub:'모든 작업이 기기에서 처리됩니다. 파일이 업로드되지 않습니다.',s1t:'백업 내보내기',s1d:'JW Library에서 각 기기의 백업을 만들고 .jwlibrary 파일을 저장하세요.',s1btn:'방법 보기',s2t:'추가 및 병합',s2d:'기본 백업을 추가한 뒤 나머지를 추가하고 병합을 누르세요.',s3t:'복원하기',s3d:'병합된 파일을 다운로드해 JW Library에서 복원하세요.',s3btn:'복원 가이드',start:'시작하기',skip:'건너뛰기',tab1:'병합',tab2:'다른 도구',t_intro:'JW Sync에는 몇 가지 도구가 더 있습니다. 각 기능은 다음과 같습니다:',exp_d:'백업을 열어 노트를 검색·읽기·편집·태그하고 강조 색을 바꾸며, ‘내 도서관에 묻기’로 의미로 노트를 찾은 뒤 .jwlibrary 파일로 저장하세요.',stat_d:'백업을 불러오면 학습 총계·연속 기록·추세와 함께, 학습 이정표 달성 시 받는 메달을 모은 수상 탭을 볼 수 있습니다.',shr_d:'선택한 노트를 작은 공유 파일로 친구에게 보내거나, 친구가 보낸 노트를 추가하세요 — 전체 백업을 병합하지 않고도요.',open:'열기'},
   tl:{close:'Isara',badge:'100% pribado — hindi umaalis ang iyong mga file sa device na ito',how:'Paano ito gumagana',title:'Pagsamahin ang iyong library sa 3 hakbang',sub:'Lahat ay nangyayari sa iyong device. Hindi kailanman ina-upload ang iyong mga file.',s1t:'I-export ang iyong mga backup',s1d:'Sa JW Library, gumawa ng backup sa bawat device at i-save ang mga .jwlibrary file.',s1btn:'Ipakita kung paano',s2t:'Idagdag at pagsamahin',s2d:'Idagdag ang iyong pangunahing backup, tapos ang iba pa, at i-tap ang Pagsamahin.',s3t:'I-restore',s3d:'I-download ang pinagsamang file at i-restore ito sa JW Library.',s3btn:'Gabay sa pag-restore',start:'Magsimula',skip:'Laktawan',tab1:'Pagsasama',tab2:'Iba pang tool',t_intro:'May ilan pang tool ang JW Sync — ito ang ginagawa ng bawat isa:',exp_d:'Buksan ang anumang backup para hanapin, basahin, i-edit at i-tag ang iyong mga tala, baguhin ang kulay ng highlight, at hanapin ang mga tala ayon sa kahulugan gamit ang Itanong sa Library — pagkatapos ay i-save sa .jwlibrary file.',stat_d:'Mag-load ng backup para makita ang iyong mga total, streak at trend ng pag-aaral, kasama ang Awards tab na may mga medalyang makukuha mo kapag umabot sa mga milestone.',shr_d:'Magpadala ng piling tala sa kaibigan bilang maliit na share file, o idagdag ang mga talang ipinadala sa iyo — nang hindi pinagsasama ang buong backup.',open:'Buksan'},
   sv:{close:'Stäng',badge:'100% privat — dina filer lämnar aldrig den här enheten',how:'Så fungerar det',title:'Slå ihop ditt bibliotek i 3 steg',sub:'Allt sker på din enhet. Dina filer laddas aldrig upp.',s1t:'Exportera dina säkerhetskopior',s1d:'Skapa en säkerhetskopia i JW Library på varje enhet och spara .jwlibrary-filerna.',s1btn:'Visa hur',s2t:'Lägg till och slå ihop',s2d:'Lägg till din huvudsäkerhetskopia, sedan de andra, och tryck på Slå ihop.',s3t:'Återställ',s3d:'Ladda ner den sammanslagna filen och återställ den i JW Library.',s3btn:'Återställningsguide',start:'Kom igång',skip:'Hoppa över',tab1:'Sammanfogning',tab2:'Andra verktyg',t_intro:'JW Sync har några fler verktyg — så här fungerar de:',exp_d:'Öppna en säkerhetskopia för att söka, läsa, redigera och tagga dina anteckningar, ändra färg på markeringar och hitta anteckningar efter betydelse med Fråga ditt bibliotek — spara sedan till en .jwlibrary-fil.',stat_d:'Ladda en säkerhetskopia för att se dina studietotaler, sviter och trender, plus en Utmärkelser-flik med medaljer du tjänar när du når milstolpar.',shr_d:'Skicka utvalda anteckningar till en vän som en liten delningsfil, eller lägg till anteckningar någon skickat dig — utan att slå ihop hela säkerhetskopior.',open:'Öppna'},
   ceb:{close:'Sirad-i',badge:'100% pribado — ang imong mga file dili mobiya niini nga device',how:'Giunsa kini paglihok',title:'Hiusaha ang imong library sa 3 ka lakang',sub:'Tanan mahitabo sa imong device. Ang imong mga file dili gyud ma-upload.',s1t:'I-export ang imong mga backup',s1d:'Sa JW Library, paghimo og backup sa matag device ug i-save ang mga .jwlibrary file.',s1btn:'Ipakita kung unsaon',s2t:'Idugang ug hiusahon',s2d:'Idugang ang imong nag-unang backup, dayon ang uban, ug i-tap ang Hiusahon.',s3t:'I-restore',s3d:'I-download ang gihiusa nga file ug i-restore kini sa JW Library.',s3btn:'Giya sa pag-restore',start:'Sugdi',skip:'Laktawi',tab1:'Paghiusa',tab2:'Uban pang himan',t_intro:'Ang JW Sync adunay pipila pa ka himan — mao kini ang gibuhat sa matag usa:',exp_d:'Ablihi ang bisan unsang backup aron pangitaon, basahon, i-edit ug i-tag ang imong mga nota, usbon ang kolor sa highlight, ug pangitaon ang mga nota pinaagi sa kahulogan gamit ang Pangutana sa imong Library — dayon i-save sa .jwlibrary file.',stat_d:'Pag-load og backup aron makita ang imong mga total, streak ug uso sa pagtuon, lakip ang Awards nga tab nga adunay mga medalya nga imong makuha sa pag-abot sa mga milestone.',shr_d:'Pagpadala og piniling mga nota sa imong higala isip gamay nga share file, o idugang ang mga nota nga gipadala kanimo — nga dili hiusahon ang tibuok backup.',open:'Ablihi'},ar:{close:"إغلاق",badge:"خصوصية 100% — ملفاتك لا تغادر هذا الجهاز أبدًا",how:"طريقة العمل",title:"ادمج مكتبتك في 3 خطوات",sub:"كل شيء يجري على جهازك. ملفاتك لا تُرفع أبدًا.",s1t:"صدّر نسخك الاحتياطية",s1d:"من JW Library على كل جهاز، أنشئ نسخة احتياطية واحفظ ملفات ‎.jwlibrary‎.",s1btn:"أرِني الطريقة",s2t:"أضف وادمج",s2d:"أضف نسختك الاحتياطية الرئيسية، ثم البقية، واضغط دمج.",s3t:"استعادة",s3d:"نزّل الملف المدمج واستعده في JW Library.",s3btn:"دليل الاستعادة",start:"لنبدأ",skip:"تخطٍّ",tab1:"الدمج",tab2:"أدوات أخرى",t_intro:"يضم JW Sync أدوات أخرى — إليك ما تفعله كل منها:",exp_d:"افتح أي نسخة احتياطية للبحث في ملاحظاتك وقراءتها وتحريرها ووسمها، وتغيير ألوان التظليل، والعثور على الملاحظات بالمعنى عبر «اسأل مكتبتك» — ثم احفظها في ملف ‎.jwlibrary‎.",stat_d:"حمّل نسخة احتياطية لترى إجماليات درسك وسلاسل مواظبتك واتجاهاتك، إضافة إلى تبويب الأوسمة بميداليات تكسبها عند بلوغ محطات الدرس.",shr_d:"أرسل ملاحظات مختارة إلى صديق كملف مشاركة صغير، أو أضف ملاحظات أرسلها إليك صديق — دون دمج نسخ احتياطية كاملة.",open:"افتح"}
  };
  function curLang(){try{var l=localStorage.getItem('jwsync_lang');if(l&&W[l])return l;}catch(e){}
    var h=(document.documentElement.lang||'en');if(W[h])return h;h=h.slice(0,2);return W[h]?h:'en';}
  function L(k){var d=W[curLang()]||W.en;return (d&&d[k]!=null)?d[k]:W.en[k];}
  function esc(s){return String(s).replace(/[&<>"']/g,function(ch){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[ch];});}
  function lock(){return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>';}
  function mainPicker(){return document.querySelector('input[type="file"][accept=".jwlibrary"]:not([multiple])');}

  function injectBadge(){
    if(document.getElementById('jw-priv-badge'))return true;
    var inp=mainPicker();if(!inp)return false;
    var host=inp.closest('[class*="step"]')||inp.closest('label')||inp.parentElement;
    if(!host||!host.parentNode)return false;
    var b=document.createElement('div');
    b.id='jw-priv-badge';b.className='jw-priv-badge';
    b.innerHTML=lock()+'<span class="jw-priv-text"></span>';
    host.parentNode.insertBefore(b,host);
    localizeBadge();
    return true;
  }
  function localizeBadge(){var b=document.getElementById('jw-priv-badge');if(!b)return;
    var t=b.querySelector('.jw-priv-text');if(t)t.textContent=L('badge');}
  function wireHowBtn(){var btn=document.getElementById('jw-how-btn');if(!btn)return;
    localizeHowBtn();
    if(!btn.__jwWired){btn.__jwWired=true;btn.addEventListener('click',function(e){e.preventDefault();openWizard();});}}
  function localizeHowBtn(){var s=document.querySelector('#jw-how-btn .jw-how-txt');if(s)s.textContent=L('how');}

  function stepHtml(n,tk,dk,bk,mode){
    return '<li class="jw-wiz-step"><span class="jw-wiz-num">'+n+'</span><div class="jw-wiz-stepbody">'+
      '<div class="jw-wiz-steptitle">'+esc(L(tk))+'</div>'+
      '<div class="jw-wiz-stepdesc">'+esc(L(dk))+'</div>'+
      (bk?'<button type="button" class="jw-wiz-link" data-jw-guide="'+mode+'">'+esc(L(bk))+' →</button>':'')+
      '</div></li>';
  }
  function toolName(which){var map={explorer:'svc_explorer_t',stats:'svc_stats_t',share:'svc_share_t'},def={explorer:'Study Explorer',stats:'Study Stats',share:'Note Share & Receive'};
    try{var l=curLang(),LI=window.__JW_LANDING_I18N||{},o=LI[l]||LI.en||{};
      if(o[map[which]])return o[map[which]];if(LI.en&&LI.en[map[which]])return LI.en[map[which]];}catch(e){}
    return def[which];}
  function toolIcon(which){var s='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">';
    if(which==='explorer')return s+'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>';
    if(which==='stats')return s+'<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>';
    return s+'<circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"></line><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"></line></svg>';}
  function toolHtml(which,dk){return '<li class="jw-wiz-tool"><span class="jw-wiz-tool-ic">'+toolIcon(which)+'</span>'+
    '<div class="jw-wiz-tool-body"><div class="jw-wiz-tool-t">'+esc(toolName(which))+'</div>'+
    '<div class="jw-wiz-tool-d">'+esc(L(dk))+'</div>'+
    '<button type="button" class="jw-wiz-tool-open" data-jw-open="'+which+'">'+esc(L('open'))+' \u2192</button></div></li>';}
  function openTool(which){try{
    if(which==='stats'){if(window.__jwGoHighlights)window.__jwGoHighlights();}
    else if(which==='share'){if(window.__jwGoShare)window.__jwGoShare();}
    else if(which==='explorer'){var bt=window.__jwBootBrowse?window.__jwBootBrowse():Promise.resolve();
      Promise.resolve(bt).then(function(){if(window.__openJwBrowse)window.__openJwBrowse(window.__jwLastFile||undefined);}).catch(function(){});}
  }catch(e){}}
  function openWizard(){
    if(document.getElementById('jw-wiz-ov'))return;
    var ov=document.createElement('div');ov.id='jw-wiz-ov';ov.className='jw-wiz-ov';
    ov.innerHTML='<div class="jw-wiz-back" data-jw-close></div>'+
      '<div class="jw-wiz-card" role="dialog" aria-modal="true" aria-label="'+esc(L('title'))+'">'+
        '<button type="button" class="jw-wiz-x" data-jw-close aria-label="'+esc(L('close'))+'">×</button>'+
        '<div class="jw-wiz-priv">'+lock()+'<span>'+esc(L('badge'))+'</span></div>'+
        '<h2 class="jw-wiz-title">'+esc(L('title'))+'</h2>'+
        '<div class="jw-wiz-tabs" role="tablist">'+
          '<button type="button" class="jw-wiz-tab active" data-jw-tab="merge">'+esc(L('tab1'))+'</button>'+
          '<button type="button" class="jw-wiz-tab" data-jw-tab="tools">'+esc(L('tab2'))+'</button>'+
        '</div>'+
        '<div data-jw-pane="merge">'+
          '<p class="jw-wiz-sub">'+esc(L('sub'))+'</p>'+
          '<ol class="jw-wiz-steps">'+
            stepHtml(1,'s1t','s1d','s1btn','export')+
            stepHtml(2,'s2t','s2d',null,null)+
            stepHtml(3,'s3t','s3d','s3btn','restore')+
          '</ol>'+
        '</div>'+
        '<div data-jw-pane="tools" hidden>'+
          '<p class="jw-wiz-intro">'+esc(L('t_intro'))+'</p>'+
          '<ul class="jw-wiz-tools">'+toolHtml('explorer','exp_d')+toolHtml('stats','stat_d')+toolHtml('share','shr_d')+'</ul>'+
        '</div>'+
        '<div class="jw-wiz-actions">'+
          '<button type="button" class="jw-wiz-skip" data-jw-close>'+esc(L('skip'))+'</button>'+
          '<button type="button" class="jw-wiz-start" data-jw-close>'+esc(L('start'))+'</button>'+
        '</div>'+
      '</div>';
    document.body.appendChild(ov);
    function close(){
      document.removeEventListener('keydown',onKey);
      if(ov.parentNode)ov.parentNode.removeChild(ov);scrollToPicker();}
    function onKey(e){if(e.key==='Escape')close();}
    ov.addEventListener('click',function(e){
      var tb=e.target.closest&&e.target.closest('[data-jw-tab]');
      if(tb){var which=tb.getAttribute('data-jw-tab');
        Array.prototype.forEach.call(ov.querySelectorAll('[data-jw-tab]'),function(b){b.classList.toggle('active',b===tb);});
        Array.prototype.forEach.call(ov.querySelectorAll('[data-jw-pane]'),function(p){p.hidden=(p.getAttribute('data-jw-pane')!==which);});
        return;}
      var op=e.target.closest&&e.target.closest('[data-jw-open]');
      if(op){close();openTool(op.getAttribute('data-jw-open'));return;}
      var g=e.target.closest&&e.target.closest('[data-jw-guide]');
      if(g){if(window.__jwOpenGuide)window.__jwOpenGuide(g.getAttribute('data-jw-guide'));return;}
      if(e.target.closest&&e.target.closest('[data-jw-close]'))close();
    });
    document.addEventListener('keydown',onKey);
  }
  function scrollToPicker(){try{var inp=mainPicker();var node=inp&&(inp.closest('[class*="step"]')||inp.parentElement);
    if(node&&node.scrollIntoView)node.scrollIntoView({behavior:'smooth',block:'center'});}catch(e){}}

  window.__jwOpenWizard=openWizard;

  function boot(){
    wireHowBtn();
    var injected=false,tries=0;
    var iv=setInterval(function(){
      tries++;
      try{ if(!injected&&injectBadge())injected=true; wireHowBtn(); }catch(e){}
      if(injected||tries>40)clearInterval(iv);
    },300);
    try{
      var mo=new MutationObserver(function(){try{if(!document.getElementById('jw-priv-badge'))injectBadge();}catch(e){}});
      if(document.body)mo.observe(document.body,{childList:true,subtree:true});
    }catch(e){}
    try{var sel=document.getElementById('landing-lang-select');
      if(sel)sel.addEventListener('change',function(){setTimeout(function(){localizeBadge();localizeHowBtn();},60);});}catch(e){}
  }
  try{if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();}catch(e){}
})();

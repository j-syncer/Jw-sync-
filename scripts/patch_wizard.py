#!/usr/bin/env python3
"""Inject the first-run Merge Wizard + point-of-action privacy badge into
beta/index.html as a self-contained enhancement block (no React core edits).
Also bumps the Schema.org softwareVersion."""

import io, sys

FILE = 'beta/index.html'

MARKER = '<!-- ── Merge Wizard + Privacy Badge ─'

BLOCK = r'''<!-- ── Merge Wizard + Privacy Badge ──────────────────────── -->
<style>
.jw-priv-badge{display:flex;align-items:center;gap:8px;flex-wrap:wrap;justify-content:center;
  margin:0 auto 12px;padding:7px 13px;max-width:max-content;border-radius:999px;
  background:rgba(4,15,34,.7);border:1px solid rgba(71,85,105,.35);
  font:500 12.5px/1.3 inherit;color:#cbd5e1}
.jw-priv-badge svg{flex:0 0 auto;width:14px;height:14px;color:#34d399}
.jw-priv-text{color:#e2e8f0}
.jw-priv-how{background:none;border:0;padding:0 0 0 4px;cursor:pointer;
  color:#fb923c;font:600 12.5px/1.3 inherit;text-decoration:underline;text-underline-offset:2px}
.jw-priv-how:hover{color:#ea580c}
.jw-wiz-ov{position:fixed;inset:0;z-index:8000;display:flex;align-items:center;justify-content:center;
  padding:16px;font-family:inherit;animation:jw-wiz-fade .2s ease-out}
@keyframes jw-wiz-fade{from{opacity:0}to{opacity:1}}
.jw-wiz-back{position:absolute;inset:0;background:rgba(4,15,34,.82);
  backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.jw-wiz-card{position:relative;z-index:1;width:100%;max-width:480px;max-height:calc(100vh - 32px);
  overflow-y:auto;padding:28px 26px 22px;border-radius:18px;
  background:#0b1426;border:1px solid rgba(71,85,105,.4);
  box-shadow:0 18px 60px rgba(0,0,0,.55);color:#e2e8f0;text-align:left}
.jw-wiz-x{position:absolute;top:12px;right:14px;background:none;border:0;cursor:pointer;
  color:#94a3b8;font-size:26px;line-height:1;padding:2px 6px;border-radius:8px}
.jw-wiz-x:hover{color:#e2e8f0;background:rgba(71,85,105,.3)}
.jw-wiz-priv{display:flex;align-items:center;gap:7px;font:600 12px/1.3 inherit;color:#34d399;margin-bottom:14px}
.jw-wiz-priv svg{width:14px;height:14px}
.jw-wiz-title{margin:0 0 6px;font:700 21px/1.25 inherit;color:#f8fafc}
.jw-wiz-sub{margin:0 0 18px;font:400 13.5px/1.5 inherit;color:#94a3b8}
.jw-wiz-steps{list-style:none;margin:0 0 20px;padding:0;display:flex;flex-direction:column;gap:14px}
.jw-wiz-step{display:flex;gap:13px;align-items:flex-start}
.jw-wiz-num{flex:0 0 auto;width:26px;height:26px;border-radius:50%;
  background:#ea580c;color:#fff;font:700 13px/26px inherit;text-align:center}
.jw-wiz-stepbody{flex:1 1 auto;min-width:0}
.jw-wiz-steptitle{font:600 14.5px/1.3 inherit;color:#f1f5f9;margin-bottom:2px}
.jw-wiz-stepdesc{font:400 13px/1.45 inherit;color:#94a3b8}
.jw-wiz-link{margin-top:6px;background:none;border:0;padding:0;cursor:pointer;
  color:#fb923c;font:600 13px/1.3 inherit;text-decoration:underline;text-underline-offset:2px}
.jw-wiz-link:hover{color:#ea580c}
.jw-wiz-actions{display:flex;align-items:center;justify-content:flex-end;gap:10px}
.jw-wiz-skip{background:rgba(71,85,105,.35);border:0;cursor:pointer;
  color:#cbd5e1;font:600 13.5px/1 inherit;padding:11px 16px;border-radius:10px}
.jw-wiz-skip:hover{background:rgba(71,85,105,.55)}
.jw-wiz-start{background:#ea580c;border:0;cursor:pointer;color:#fff;
  font:700 13.5px/1 inherit;padding:11px 20px;border-radius:10px;box-shadow:0 1px 5px rgba(234,88,12,.4)}
.jw-wiz-start:hover{background:#c2410c}
</style>
<script>
(function(){
  if(window.__jwWizardInit)return; window.__jwWizardInit=true;
  var W={
   en:{close:'Close',badge:'100% private — your files never leave this device',how:'How it works',title:'Merge your library in 3 steps',sub:'Everything happens on your device. Your files are never uploaded.',s1t:'Export your backups',s1d:'In JW Library on each device, create a backup and save the .jwlibrary files.',s1btn:'Show me how',s2t:'Add & merge',s2d:'Add your main backup, then the others, and tap Merge.',s3t:'Restore',s3d:'Download the merged file and restore it in JW Library.',s3btn:'Restore guide',start:'Get started',skip:'Skip'},
   es:{close:'Cerrar',badge:'100% privado — tus archivos nunca salen de este dispositivo',how:'Cómo funciona',title:'Combina tu biblioteca en 3 pasos',sub:'Todo ocurre en tu dispositivo. Tus archivos nunca se suben.',s1t:'Exporta tus copias',s1d:'En JW Library, crea una copia en cada dispositivo y guarda los archivos .jwlibrary.',s1btn:'Ver cómo',s2t:'Añade y combina',s2d:'Añade tu copia principal, luego las demás y toca Combinar.',s3t:'Restaura',s3d:'Descarga el archivo combinado y restáuralo en JW Library.',s3btn:'Guía de restauración',start:'Empezar',skip:'Omitir'},
   pt:{close:'Fechar',badge:'100% privado — seus arquivos nunca saem deste dispositivo',how:'Como funciona',title:'Combine sua biblioteca em 3 passos',sub:'Tudo acontece no seu dispositivo. Seus arquivos nunca são enviados.',s1t:'Exporte seus backups',s1d:'No JW Library, faça um backup em cada dispositivo e salve os arquivos .jwlibrary.',s1btn:'Ver como',s2t:'Adicione e combine',s2d:'Adicione o backup principal, depois os outros, e toque em Combinar.',s3t:'Restaure',s3d:'Baixe o arquivo combinado e restaure-o no JW Library.',s3btn:'Guia de restauração',start:'Começar',skip:'Pular'},
   fr:{close:'Fermer',badge:'100% privé — vos fichiers ne quittent jamais cet appareil',how:'Comment ça marche',title:'Fusionnez votre bibliothèque en 3 étapes',sub:'Tout se passe sur votre appareil. Vos fichiers ne sont jamais envoyés.',s1t:'Exportez vos sauvegardes',s1d:'Dans JW Library, créez une sauvegarde sur chaque appareil et enregistrez les fichiers .jwlibrary.',s1btn:'Voir comment',s2t:'Ajoutez et fusionnez',s2d:'Ajoutez votre sauvegarde principale, puis les autres, et appuyez sur Fusionner.',s3t:'Restaurez',s3d:'Téléchargez le fichier fusionné et restaurez-le dans JW Library.',s3btn:'Guide de restauration',start:'Commencer',skip:'Ignorer'},
   de:{close:'Schließen',badge:'100% privat — deine Dateien verlassen nie dieses Gerät',how:'So funktioniert’s',title:'Führe deine Bibliothek in 3 Schritten zusammen',sub:'Alles geschieht auf deinem Gerät. Deine Dateien werden nie hochgeladen.',s1t:'Exportiere deine Sicherungen',s1d:'Erstelle in JW Library auf jedem Gerät eine Sicherung und speichere die .jwlibrary-Dateien.',s1btn:'Anleitung ansehen',s2t:'Hinzufügen & zusammenführen',s2d:'Füge deine Hauptsicherung hinzu, dann die anderen, und tippe auf Zusammenführen.',s3t:'Wiederherstellen',s3d:'Lade die zusammengeführte Datei herunter und stelle sie in JW Library wieder her.',s3btn:'Wiederherstellungs-Anleitung',start:'Loslegen',skip:'Überspringen'},
   it:{close:'Chiudi',badge:'100% privato — i tuoi file non lasciano mai questo dispositivo',how:'Come funziona',title:'Unisci la tua biblioteca in 3 passaggi',sub:'Tutto avviene sul tuo dispositivo. I tuoi file non vengono mai caricati.',s1t:'Esporta i tuoi backup',s1d:'In JW Library, crea un backup su ogni dispositivo e salva i file .jwlibrary.',s1btn:'Mostrami come',s2t:'Aggiungi e unisci',s2d:'Aggiungi il backup principale, poi gli altri, e tocca Unisci.',s3t:'Ripristina',s3d:'Scarica il file unito e ripristinalo in JW Library.',s3btn:'Guida al ripristino',start:'Inizia',skip:'Salta'},
   ru:{close:'Закрыть',badge:'100% конфиденциально — ваши файлы не покидают это устройство',how:'Как это работает',title:'Объедините библиотеку за 3 шага',sub:'Всё происходит на вашем устройстве. Ваши файлы никогда не загружаются.',s1t:'Экспортируйте резервные копии',s1d:'В JW Library создайте резервную копию на каждом устройстве и сохраните файлы .jwlibrary.',s1btn:'Показать как',s2t:'Добавьте и объедините',s2d:'Добавьте основную копию, затем остальные и нажмите «Объединить».',s3t:'Восстановите',s3d:'Скачайте объединённый файл и восстановите его в JW Library.',s3btn:'Инструкция по восстановлению',start:'Начать',skip:'Пропустить'},
   ja:{close:'閉じる',badge:'100%プライベート — ファイルはこの端末から出ません',how:'使い方',title:'3ステップでライブラリを統合',sub:'すべて端末内で処理されます。ファイルがアップロードされることはありません。',s1t:'バックアップを書き出す',s1d:'JW Libraryで各端末のバックアップを作成し、.jwlibraryファイルを保存します。',s1btn:'方法を見る',s2t:'追加して統合',s2d:'メインのバックアップを追加し、続けて他のファイルを追加して「統合」をタップします。',s3t:'復元する',s3d:'統合したファイルをダウンロードし、JW Libraryで復元します。',s3btn:'復元ガイド',start:'はじめる',skip:'スキップ'},
   ko:{close:'닫기',badge:'100% 비공개 — 파일이 이 기기를 벗어나지 않습니다',how:'사용 방법',title:'3단계로 라이브러리 병합',sub:'모든 작업이 기기에서 처리됩니다. 파일이 업로드되지 않습니다.',s1t:'백업 내보내기',s1d:'JW Library에서 각 기기의 백업을 만들고 .jwlibrary 파일을 저장하세요.',s1btn:'방법 보기',s2t:'추가 및 병합',s2d:'기본 백업을 추가한 뒤 나머지를 추가하고 병합을 누르세요.',s3t:'복원하기',s3d:'병합된 파일을 다운로드해 JW Library에서 복원하세요.',s3btn:'복원 가이드',start:'시작하기',skip:'건너뛰기'},
   tl:{close:'Isara',badge:'100% pribado — hindi umaalis ang iyong mga file sa device na ito',how:'Paano ito gumagana',title:'Pagsamahin ang iyong library sa 3 hakbang',sub:'Lahat ay nangyayari sa iyong device. Hindi kailanman ina-upload ang iyong mga file.',s1t:'I-export ang iyong mga backup',s1d:'Sa JW Library, gumawa ng backup sa bawat device at i-save ang mga .jwlibrary file.',s1btn:'Ipakita kung paano',s2t:'Idagdag at pagsamahin',s2d:'Idagdag ang iyong pangunahing backup, tapos ang iba pa, at i-tap ang Pagsamahin.',s3t:'I-restore',s3d:'I-download ang pinagsamang file at i-restore ito sa JW Library.',s3btn:'Gabay sa pag-restore',start:'Magsimula',skip:'Laktawan'},
   sv:{close:'Stäng',badge:'100% privat — dina filer lämnar aldrig den här enheten',how:'Så fungerar det',title:'Slå ihop ditt bibliotek i 3 steg',sub:'Allt sker på din enhet. Dina filer laddas aldrig upp.',s1t:'Exportera dina säkerhetskopior',s1d:'Skapa en säkerhetskopia i JW Library på varje enhet och spara .jwlibrary-filerna.',s1btn:'Visa hur',s2t:'Lägg till och slå ihop',s2d:'Lägg till din huvudsäkerhetskopia, sedan de andra, och tryck på Slå ihop.',s3t:'Återställ',s3d:'Ladda ner den sammanslagna filen och återställ den i JW Library.',s3btn:'Återställningsguide',start:'Kom igång',skip:'Hoppa över'},
   ceb:{close:'Sirad-i',badge:'100% pribado — ang imong mga file dili mobiya niini nga device',how:'Giunsa kini paglihok',title:'Hiusaha ang imong library sa 3 ka lakang',sub:'Tanan mahitabo sa imong device. Ang imong mga file dili gyud ma-upload.',s1t:'I-export ang imong mga backup',s1d:'Sa JW Library, paghimo og backup sa matag device ug i-save ang mga .jwlibrary file.',s1btn:'Ipakita kung unsaon',s2t:'Idugang ug hiusahon',s2d:'Idugang ang imong nag-unang backup, dayon ang uban, ug i-tap ang Hiusahon.',s3t:'I-restore',s3d:'I-download ang gihiusa nga file ug i-restore kini sa JW Library.',s3btn:'Giya sa pag-restore',start:'Sugdi',skip:'Laktawi'}
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
    b.innerHTML=lock()+'<span class="jw-priv-text"></span><button type="button" class="jw-priv-how" id="jw-priv-how"></button>';
    host.parentNode.insertBefore(b,host);
    localizeBadge();
    var how=document.getElementById('jw-priv-how');
    if(how)how.addEventListener('click',function(e){e.preventDefault();openWizard();});
    return true;
  }
  function localizeBadge(){var b=document.getElementById('jw-priv-badge');if(!b)return;
    var t=b.querySelector('.jw-priv-text');if(t)t.textContent=L('badge');
    var h=b.querySelector('.jw-priv-how');if(h)h.textContent=L('how');}

  function stepHtml(n,tk,dk,bk,mode){
    return '<li class="jw-wiz-step"><span class="jw-wiz-num">'+n+'</span><div class="jw-wiz-stepbody">'+
      '<div class="jw-wiz-steptitle">'+esc(L(tk))+'</div>'+
      '<div class="jw-wiz-stepdesc">'+esc(L(dk))+'</div>'+
      (bk?'<button type="button" class="jw-wiz-link" data-jw-guide="'+mode+'">'+esc(L(bk))+' →</button>':'')+
      '</div></li>';
  }
  function openWizard(){
    if(document.getElementById('jw-wiz-ov'))return;
    var ov=document.createElement('div');ov.id='jw-wiz-ov';ov.className='jw-wiz-ov';
    ov.innerHTML='<div class="jw-wiz-back" data-jw-close></div>'+
      '<div class="jw-wiz-card" role="dialog" aria-modal="true" aria-label="'+esc(L('title'))+'">'+
        '<button type="button" class="jw-wiz-x" data-jw-close aria-label="'+esc(L('close'))+'">×</button>'+
        '<div class="jw-wiz-priv">'+lock()+'<span>'+esc(L('badge'))+'</span></div>'+
        '<h2 class="jw-wiz-title">'+esc(L('title'))+'</h2>'+
        '<p class="jw-wiz-sub">'+esc(L('sub'))+'</p>'+
        '<ol class="jw-wiz-steps">'+
          stepHtml(1,'s1t','s1d','s1btn','export')+
          stepHtml(2,'s2t','s2d',null,null)+
          stepHtml(3,'s3t','s3d','s3btn','restore')+
        '</ol>'+
        '<div class="jw-wiz-actions">'+
          '<button type="button" class="jw-wiz-skip" data-jw-close>'+esc(L('skip'))+'</button>'+
          '<button type="button" class="jw-wiz-start" data-jw-close>'+esc(L('start'))+'</button>'+
        '</div>'+
      '</div>';
    document.body.appendChild(ov);
    function close(){try{localStorage.setItem('jwsync_wizard_seen','1');}catch(e){}
      document.removeEventListener('keydown',onKey);
      if(ov.parentNode)ov.parentNode.removeChild(ov);scrollToPicker();}
    function onKey(e){if(e.key==='Escape')close();}
    ov.addEventListener('click',function(e){
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
    var injected=false,wizDone=false,tries=0;
    var iv=setInterval(function(){
      tries++;
      try{
        if(!injected&&injectBadge())injected=true;
        if(!wizDone){
          var seen=null;try{seen=localStorage.getItem('jwsync_wizard_seen');}catch(e){}
          if(seen==='1'){wizDone=true;}
          else if(mainPicker()){wizDone=true;setTimeout(openWizard,500);}
        }
      }catch(e){}
      if((injected&&wizDone)||tries>40)clearInterval(iv);
    },300);
    try{
      var mo=new MutationObserver(function(){try{if(!document.getElementById('jw-priv-badge'))injectBadge();}catch(e){}});
      if(document.body)mo.observe(document.body,{childList:true,subtree:true});
    }catch(e){}
    try{var sel=document.getElementById('landing-lang-select');
      if(sel)sel.addEventListener('change',function(){setTimeout(localizeBadge,60);});}catch(e){}
  }
  try{if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();}catch(e){}
})();
</script>
<!-- ── End Merge Wizard + Privacy Badge ──────────────────── -->
'''

def main():
    with io.open(FILE, encoding='utf-8') as f:
        c = f.read()
    if MARKER in c:
        print('Wizard block already present — aborting.'); sys.exit(1)
    needle = '\n</body>\n</html>\n'
    if c.count(needle) != 1:
        print('Expected exactly one tail </body></html>, found', c.count(needle)); sys.exit(1)
    c = c.replace(needle, '\n' + BLOCK + needle, 1)

    # bump Schema.org softwareVersion
    if '"softwareVersion": "2.53.0"' in c:
        c = c.replace('"softwareVersion": "2.53.0"', '"softwareVersion": "2.55.0"', 1)
    else:
        print('WARN: softwareVersion 2.53.0 not found; skipped bump')

    with io.open(FILE, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Wizard block injected; file now', len(c), 'chars')

if __name__ == '__main__':
    main()

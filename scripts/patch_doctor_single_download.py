# -*- coding: utf-8 -*-
"""Doctor merge opt-in v2 (v2.64.1): single-download flow. When the user
ticks the pre-merge checkbox, the merged file's automatic download is
suppressed (one-shot flag consumed by the celebration overlay), the Doctor
opens on the merged file in auto mode, cleans without any click, and then
offers ONE download button for the final healthy file. All failure paths
clear the flag and fall back to the normal merged-file download."""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

def rep(s, old, new, what):
    must(s.count(old) == 1, what + ' anchor not unique: %d' % s.count(old))
    return s.replace(old, new, 1)

# ════ 1) Celebration: one-shot suppression of the automatic download ════════
c = rep(c,
"""  function triggerDownload(opts) {
    var dl = document.getElementById('download-btn');""",
"""  function triggerDownload(opts) {
    if (opts && opts.auto && window.__jwDoctorSuppressAutoDl) {
      // the Library Doctor will deliver the final (cleaned) file instead
      window.__jwDoctorSuppressAutoDl = false;
      return false;
    }
    var dl = document.getElementById('download-btn');""",
'triggerDownload guard')

# ════ 2) Doctor block edits ═════════════════════════════════════════════════
START = '<!-- ── Backup Doctor'
END   = '<!-- ── End Backup Doctor'
must(c.count(START) == 1 and c.count(END) == 1, 'doctor block markers')
s_i, e_i = c.index(START), c.index(END)
blk = c[s_i:e_i]

# 2a) i18n: download + done_ready keys appended after err_db in all 12 langs
NEWKEYS = [
    ('err_db:"This backup is missing its notes database (userData.db)."}',
     'download:"Download your file"', 'done_ready:"Your cleaned backup is ready to download."'),
    ('err_db:"A esta copia le falta su base de datos de notas (userData.db)."}',
     'download:"Descargar tu archivo"', 'done_ready:"Tu copia limpia está lista para descargar."'),
    ('err_db:"Este backup está sem o banco de dados de notas (userData.db)."}',
     'download:"Baixar seu arquivo"', 'done_ready:"Seu backup limpo está pronto para baixar."'),
    ('err_db:"Cette sauvegarde n\'a pas sa base de données de notes (userData.db)."}',
     'download:"Télécharger votre fichier"', 'done_ready:"Votre sauvegarde nettoyée est prête à télécharger."'),
    ('err_db:"Dieser Sicherung fehlt ihre Notizdatenbank (userData.db)."}',
     'download:"Deine Datei herunterladen"', 'done_ready:"Deine bereinigte Sicherung ist bereit zum Download."'),
    ('err_db:"A questo backup manca il database delle note (userData.db)."}',
     'download:"Scarica il tuo file"', 'done_ready:"Il tuo backup pulito è pronto da scaricare."'),
    ('err_db:"В этой копии нет базы данных заметок (userData.db)."}',
     'download:"Скачать ваш файл"', 'done_ready:"Ваша очищенная копия готова к скачиванию."'),
    ('err_db:"このバックアップにはメモのデータベース（userData.db）がありません。"}',
     'download:"ファイルをダウンロード"', 'done_ready:"クリーンなバックアップの準備ができました。"'),
    ('err_db:"이 백업에는 메모 데이터베이스(userData.db)가 없습니다."}',
     'download:"파일 다운로드"', 'done_ready:"정리된 백업이 준비되었습니다."'),
    ('err_db:"Walang notes database (userData.db) ang backup na ito."}',
     'download:"I-download ang iyong file"', 'done_ready:"Handa nang i-download ang malinis mong backup."'),
    ('err_db:"Den här säkerhetskopian saknar sin anteckningsdatabas (userData.db)."}',
     'download:"Ladda ner din fil"', 'done_ready:"Din rensade säkerhetskopia är redo att laddas ner."'),
    ('err_db:"Wala kini backup sa notes database (userData.db)."}',
     'download:"I-download ang imong file"', 'done_ready:"Andam na ang limpyo nimong backup nga i-download."'),
]
for tail, dl, dr in NEWKEYS:
    blk = rep(blk, tail, tail[:-1] + ',' + dl + ',' + dr + '}', 'i18n ' + tail[:30])

# 2b) auto-mode flag + download icon
blk = rep(blk,
"  var cur=null; // {overlay, db, zip, dbKey, name, size, report}",
"  var cur=null; // {overlay, db, zip, dbKey, name, size, report}\n"
"  var autoMode=false; // opened from the merge flow: auto-clean, single download",
'cur decl')

blk = rep(blk,
"  var ICON_BROOM=",
"  var ICON_DL='<svg viewBox=\"0 0 24 24\" width=\"17\" height=\"17\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\"/><polyline points=\"7 10 12 15 17 10\"/><line x1=\"12\" y1=\"3\" x2=\"12\" y2=\"15\"/></svg>';\n"
"  var ICON_BROOM=",
'icon decl')

# 2c) openDoctor accepts {auto:true}
blk = rep(blk,
"""  function openDoctor(file){
    closeDoctor();
    cur={overlay:shell(), db:null, zip:null, dbKey:null, name:null, size:0, report:null};""",
"""  function openDoctor(file, opts){
    closeDoctor();
    autoMode=!!(opts&&opts.auto);
    cur={overlay:shell(), db:null, zip:null, dbKey:null, name:null, size:0, report:null};""",
'openDoctor')

# 2d) factor the blob download out of exportCleaned; skip auto-click in auto mode
blk = rep(blk,
"""  function exportCleaned(st){""",
"""  function dlBlob(blob){
    try{
      var base=((cur&&cur.name)||'backup.jwlibrary').replace(/\\.jwlibrary$/i,'');
      var url=URL.createObjectURL(blob);
      var a=document.createElement('a');
      a.href=url; a.download='healthy_'+base+'.jwlibrary';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function(){ URL.revokeObjectURL(url); },4000);
    }catch(_){}
  }

  function exportCleaned(st){""",
'dlBlob helper')

blk = rep(blk,
"""    }).then(function(buf){
      var blob=new Blob([buf],{type:'application/octet-stream'});
      try{
        var base=(st.name||'backup.jwlibrary').replace(/\\.jwlibrary$/i,'');
        var url=URL.createObjectURL(blob);
        var a=document.createElement('a');
        a.href=url; a.download='healthy_'+base+'.jwlibrary';
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function(){ URL.revokeObjectURL(url); },4000);
      }catch(_){}
      return blob;
    });""",
"""    }).then(function(buf){
      var blob=new Blob([buf],{type:'application/octet-stream'});
      if(!autoMode) dlBlob(blob); // auto mode: the Done screen offers the button
      return blob;
    });""",
'exportCleaned download')

# 2e) clean handler passes the blob through
blk = rep(blk,
"""          var fixed=applyFixes(cur.db);
          exportCleaned(cur).then(function(blob){
            if(cur) renderDone(fixed, blob?blob.size:0);
          }).catch(function(){ if(cur) renderDone(fixed, 0); });""",
"""          var fixed=applyFixes(cur.db);
          exportCleaned(cur).then(function(blob){
            if(cur) renderDone(fixed, blob||null);
          }).catch(function(){ if(cur) renderDone(fixed, null); });""",
'clean handler')

# 2f) renderDone: size from blob, ready-text + Download button in auto mode
blk = rep(blk,
"""  function renderDone(fixed, newSize){
    var b=body();""",
"""  function renderDone(fixed, blob){
    var b=body();
    var newSize=blob?blob.size:0;""",
'renderDone sig')

blk = rep(blk,
"      '<p class=\"jbd-done-d\">'+esc(t('done_d'))+'</p>'+",
"      '<p class=\"jbd-done-d\">'+esc(t(autoMode&&blob?'done_ready':'done_d'))+'</p>'+",
'done text')

blk = rep(blk,
"""      sizeRow+
      '<div class="jbd-rows">'+fixedRows+'</div>'+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+""",
"""      sizeRow+
      '<div class="jbd-rows">'+fixedRows+'</div>'+
      (autoMode&&blob ? '<button class="jbd-clean-btn" type="button" data-jbd-dl>'+ICON_DL+' <span>'+esc(t('download'))+'</span></button>' : '')+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+""",
'done markup')

blk = rep(blk,
"""    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function openDoctor""",
"""    var dlBtn=b.querySelector('[data-jbd-dl]');
    if(dlBtn) dlBtn.addEventListener('click', function(){ dlBlob(blob); });
    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function openDoctor""",
'done wiring')

# 2g) renderReport: auto-clean kicks in by itself; perfect file gets a
#     Download button for the merged file as-is
blk = rep(blk,
"      (r.issues>0 ? '<button class=\"jbd-clean-btn\" type=\"button\" data-jbd-clean>'+ICON_BROOM+' <span>'+esc(t('clean'))+'</span></button>' : '')+",
"      (r.issues>0 ? '<button class=\"jbd-clean-btn\" type=\"button\" data-jbd-clean>'+ICON_BROOM+' <span>'+esc(t('clean'))+'</span></button>'\n"
"        : (autoMode ? '<button class=\"jbd-clean-btn\" type=\"button\" data-jbd-dlmerged>'+ICON_DL+' <span>'+esc(t('download'))+'</span></button>' : ''))+",
'report markup')

blk = rep(blk,
"""    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function renderDone""",
"""    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
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

  function renderDone""",
'report wiring')

# 2h) watcher: suppress flag lifecycle + auto mode + download fallback
blk = rep(blk,
"""  var armIv=null;
  window.__jwDoctorArmAfterMerge=function(){
    if(armIv){ clearInterval(armIv); armIv=null; }
    var a0=document.getElementById('download-btn');""",
"""  var armIv=null;
  window.__jwDoctorArmAfterMerge=function(){
    if(armIv){ clearInterval(armIv); armIv=null; }
    // one-shot: tells the celebration overlay to skip its automatic
    // download of the merged file — the Doctor delivers the final
    // (cleaned) file instead. Cleared on timeout or fetch failure so the
    // user's download can never be lost.
    window.__jwDoctorSuppressAutoDl=true;
    var a0=document.getElementById('download-btn');""",
'arm suppress')

blk = rep(blk,
"      if(++tries>720){ clearInterval(armIv); armIv=null; return; }",
"      if(++tries>720){ clearInterval(armIv); armIv=null; window.__jwDoctorSuppressAutoDl=false; return; }",
'arm timeout')

blk = rep(blk,
"""        // small delay so the celebration overlay mounts beneath first
        setTimeout(function(){ openDoctor(file); },1200);
      }).catch(function(){});""",
"""        // small delay so the celebration overlay mounts beneath first
        setTimeout(function(){ openDoctor(file,{auto:true}); },1200);
      }).catch(function(){
        // fall back to the normal merged-file download
        window.__jwDoctorSuppressAutoDl=false;
        try{ var fa=document.getElementById('download-btn'); if(fa) fa.click(); }catch(_){}
      });""",
'arm catch')

c = c[:s_i] + blk + c[e_i:]

# ════ 3) clearer checkbox label (the flow now replaces the download) ════════
RELABEL = [
    ("doctor:'Also health-check the merged file (Library Doctor)'",
     "doctor:'Health-check & clean the merged file before downloading (Library Doctor)'"),
    ("doctor:'Revisar también el archivo combinado (Doctor de Biblioteca)'",
     "doctor:'Revisar y limpiar el archivo combinado antes de descargarlo (Doctor de Biblioteca)'"),
    ("doctor:'Examinar também o arquivo mesclado (Doutor da Biblioteca)'",
     "doctor:'Examinar e limpar o arquivo mesclado antes de baixar (Doutor da Biblioteca)'"),
    ("doctor:'Vérifier aussi le fichier fusionné (Docteur de Bibliothèque)'",
     "doctor:'Vérifier et nettoyer le fichier fusionné avant le téléchargement (Docteur de Bibliothèque)'"),
    ("doctor:'Zusammengeführte Datei zusätzlich prüfen (Bibliothek-Doktor)'",
     "doctor:'Zusammengeführte Datei vor dem Download prüfen und bereinigen (Bibliothek-Doktor)'"),
    ("doctor:'Controlla anche il file unito (Dottore della Biblioteca)'",
     "doctor:'Controlla e pulisci il file unito prima di scaricarlo (Dottore della Biblioteca)'"),
    ("doctor:'Также проверить объединённый файл (Доктор библиотеки)'",
     "doctor:'Проверить и очистить объединённый файл перед скачиванием (Доктор библиотеки)'"),
    ("doctor:'結合したファイルも診断する（ライブラリードクター）'",
     "doctor:'ダウンロード前に結合ファイルを診断してクリーンアップ（ライブラリードクター）'"),
    ("doctor:'병합된 파일도 검진하기 (라이브러리 닥터)'",
     "doctor:'다운로드 전에 병합된 파일을 검진하고 정리 (라이브러리 닥터)'"),
    ("doctor:'Suriin din ang pinagsamang file (Library Doctor)'",
     "doctor:'Suriin at linisin ang pinagsamang file bago i-download (Library Doctor)'"),
    ('doctor:"Hälsokolla även den sammanslagna filen (Biblioteksdoktorn)"',
     'doctor:"Hälsokolla och rensa den sammanslagna filen före nedladdning (Biblioteksdoktorn)"'),
    ("doctor:'Susiha usab ang gisagol nga file (Library Doctor)'",
     "doctor:'Susiha ug limpyohi ang gisagol nga file una i-download (Library Doctor)'"),
]
for old, new in RELABEL:
    c = rep(c, old, new, 'relabel ' + old[:30])

# ════ 4) version bump ═══════════════════════════════════════════════════════
c = rep(c, '"softwareVersion": "2.64.0"', '"softwareVersion": "2.64.1"', 'version')

io.open(f, 'w', encoding='utf-8').write(c)
print('OK: single-download doctor merge flow applied')

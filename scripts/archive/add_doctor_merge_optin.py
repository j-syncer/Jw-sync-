# -*- coding: utf-8 -*-
"""Library Doctor merge opt-in (v2.64.0) — adds a remembered checkbox to the
pre-merge Impact Preview ("Also health-check the merged file"). When ticked,
the Doctor arms itself and waits for the merge worker to finish (the React
download anchor #download-btn receiving a fresh blob: URL — the same signal
the celebration overlay uses), then fetches the merged blob and opens the
Doctor on it. Purely additive: the merge pipeline is never touched and any
failure in this path silently does nothing."""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

# ── 1) i18n: append a `doctor` key to every language in the impact preview ──
START = '<!-- ── Pre-merge Impact Preview'
END   = '<!-- ── End Pre-merge Impact Preview'
must(c.count(START) == 1 and c.count(END) == 1, 'impact preview block markers')
s_i, e_i = c.index(START), c.index(END)
block = c[s_i:e_i]

# (study_answers tail, quote char, doctor label) per language — names match DOC_I18N
LANGS = [
    ("study_answers:'Study answers'}",            "'", 'Also health-check the merged file (Library Doctor)'),
    ("study_answers:'Respuestas de estudio'}",    "'", 'Revisar también el archivo combinado (Doctor de Biblioteca)'),
    ("study_answers:'Respostas de estudo'}",      "'", 'Examinar também o arquivo mesclado (Doutor da Biblioteca)'),
    ("study_answers:'Réponses d’étude'}", "'", 'Vérifier aussi le fichier fusionné (Docteur de Bibliothèque)'),
    ("study_answers:'Studienantworten'}",         "'", 'Zusammengeführte Datei zusätzlich prüfen (Bibliothek-Doktor)'),
    ("study_answers:'Risposte di studio'}",       "'", 'Controlla anche il file unito (Dottore della Biblioteca)'),
    ("study_answers:'Ответы для изучения'}", "'", 'Также проверить объединённый файл (Доктор библиотеки)'),
    ("study_answers:'学習の回答'}", "'", '結合したファイルも診断する（ライブラリードクター）'),
    ("study_answers:'학습 답변'}", "'", '병합된 파일도 검진하기 (라이브러리 닥터)'),
    ("study_answers:'Mga sagot sa pag-aaral'}",   "'", 'Suriin din ang pinagsamang file (Library Doctor)'),
    ('study_answers:"Studiesvar"}',               '"', 'Hälsokolla även den sammanslagna filen (Biblioteksdoktorn)'),
    ("study_answers:'Mga tubag sa pagtuon'}",     "'", 'Susiha usab ang gisagol nga file (Library Doctor)'),
]
for tail, qc, label in LANGS:
    must(block.count(tail) == 1, 'i18n anchor not unique: %r (%d)' % (tail, block.count(tail)))
    block = block.replace(tail, tail[:-1] + ',doctor:' + qc + label + qc + '}', 1)

# ── 2) CSS for the checkbox row ──────────────────────────────────────────────
OLDCSS = '.jip-btn-go:hover{background:#c2410c}'
must(block.count(OLDCSS) == 1, 'css anchor')
block = block.replace(OLDCSS, OLDCSS + '\n' +
  '.jip-doctor{display:flex;align-items:center;gap:9px;margin:-8px 0 16px;padding:10px 12px;'
  'background:rgba(71,85,105,.12);border:1px solid rgba(71,85,105,.3);border-radius:9px;cursor:pointer}\n'
  '.jip-doctor:hover{border-color:rgba(234,88,12,.4)}\n'
  '.jip-doctor input{accent-color:#ea580c;width:15px;height:15px;flex:0 0 auto;cursor:pointer;margin:0}\n'
  '.jip-doctor span{font-size:12.5px;color:#cbd5e1;line-height:1.4}', 1)

# ── 3) remembered preference helper ──────────────────────────────────────────
OLDFN = '  window.__jwImpactPreview = function (counts) {'
must(block.count(OLDFN) == 1, 'impact fn anchor')
block = block.replace(OLDFN,
  "  function doctorPref(){ try{ return localStorage.getItem('jwsync_doctor_after_merge')==='1'; }catch(_){ return false; } }\n"
  + OLDFN, 1)

# ── 4) checkbox markup between the stats grid and the action buttons ─────────
OLDMK = """            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          '<div class="jip-actions">'+"""
must(block.count(OLDMK) == 1, 'markup anchor')
NEWMK = """            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          '<label class="jip-doctor"><input type="checkbox" data-jip-doctor'+(doctorPref()?' checked':'')+'><span>'+esc(t('doctor'))+'</span></label>'+
          '<div class="jip-actions">'+"""
block = block.replace(OLDMK, NEWMK, 1)

# ── 5) confirm handler: persist the choice and arm the Doctor ────────────────
OLDGO = "      overlay.querySelector('[data-jip-go]').addEventListener('click', function(){ done(true); });"
must(block.count(OLDGO) == 1, 'confirm handler anchor')
NEWGO = """      overlay.querySelector('[data-jip-go]').addEventListener('click', function(){
        var cb = overlay.querySelector('[data-jip-doctor]');
        if (cb) {
          try { localStorage.setItem('jwsync_doctor_after_merge', cb.checked ? '1' : '0'); } catch (_) {}
          if (cb.checked && typeof window.__jwDoctorArmAfterMerge === 'function') window.__jwDoctorArmAfterMerge();
        }
        done(true);
      });"""
block = block.replace(OLDGO, NEWGO, 1)

c = c[:s_i] + block + c[e_i:]

# ── 6) Doctor module: the arm/watch function ─────────────────────────────────
OLDEXP = '  window.__openJwDoctor = openDoctor;'
must(c.count(OLDEXP) == 1, 'doctor export anchor')
ARM = """  // ── Opt-in from the pre-merge preview: when the merge worker finishes
  // (the React download anchor #download-btn gets a fresh blob: URL — the
  // same signal the celebration overlay uses), fetch the merged file and
  // open the Doctor on it. Purely additive: the merge pipeline is never
  // touched, and any failure here simply does nothing.
  var armIv=null;
  window.__jwDoctorArmAfterMerge=function(){
    if(armIv){ clearInterval(armIv); armIv=null; }
    var a0=document.getElementById('download-btn');
    var prev=(a0&&a0.getAttribute('href'))||'';
    var tries=0;
    armIv=setInterval(function(){
      if(++tries>720){ clearInterval(armIv); armIv=null; return; }
      var a=document.getElementById('download-btn');
      var href=(a&&a.getAttribute('href'))||'';
      if(href.indexOf('blob:')!==0 || href===prev) return;
      clearInterval(armIv); armIv=null;
      var name=a.getAttribute('download')||'merged.jwlibrary';
      fetch(href).then(function(r){ return r.blob(); }).then(function(b){
        var file; try{ file=new File([b],name,{type:'application/octet-stream'}); }catch(_){ file=b; }
        // small delay so the celebration overlay mounts beneath first
        setTimeout(function(){ openDoctor(file); },1200);
      }).catch(function(){});
    },500);
  };

"""
c = c.replace(OLDEXP, ARM + OLDEXP, 1)

# ── 7) version bump (new user-facing feature → minor) ────────────────────────
OLDV = '"softwareVersion": "2.63.3"'
must(c.count(OLDV) == 1, 'version anchor')
c = c.replace(OLDV, '"softwareVersion": "2.64.0"', 1)

io.open(f, 'w', encoding='utf-8').write(c)
print('OK: beta/index.html patched (doctor merge opt-in)')

# -*- coding: utf-8 -*-
"""Doctor merge checkbox v3 (v2.65.0) — beta/index.html side.
- Impact card: renders the worker's doctor report as a grouped section
  (__jwImpactPreview(counts, doctor)); its own checkbox + remembered pref +
  arming are removed (the box now lives under 'Create My Merged File' and is
  one-shot). Exposes window.__jwDoctorCbLabel for the React checkbox label.
- Doctor module: exposes window.__jwDoctorT (localised strings for the card),
  gains a will_fix i18n key; the post-merge watcher is removed (superseded).
- Celebration: the auto-download suppression guard is reverted (nothing sets
  the flag anymore — the worker now cleans before packaging)."""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

def rep(old, new, what):
    global c
    must(c.count(old) == 1, what + ' anchor not unique: %d' % c.count(old))
    c = c.replace(old, new, 1)

# ── 1) celebration: revert the suppression guard ─────────────────────────────
rep("""  function triggerDownload(opts) {
    if (opts && opts.auto && window.__jwDoctorSuppressAutoDl) {
      // the Library Doctor will deliver the final (cleaned) file instead
      window.__jwDoctorSuppressAutoDl = false;
      return false;
    }
    var dl = document.getElementById('download-btn');""",
"""  function triggerDownload(opts) {
    var dl = document.getElementById('download-btn');""",
'celebration guard revert')

# ── 2) doctor module: remove the watcher, expose __jwDoctorT ────────────────
rep("""  // ── Opt-in from the pre-merge preview: when the merge worker finishes
  // (the React download anchor #download-btn gets a fresh blob: URL — the
  // same signal the celebration overlay uses), fetch the merged file and
  // open the Doctor on it. Purely additive: the merge pipeline is never
  // touched, and any failure here simply does nothing.
  var armIv=null;
  window.__jwDoctorArmAfterMerge=function(){
    if(armIv){ clearInterval(armIv); armIv=null; }
    // one-shot: tells the celebration overlay to skip its automatic
    // download of the merged file — the Doctor delivers the final
    // (cleaned) file instead. Cleared on timeout or fetch failure so the
    // user's download can never be lost.
    window.__jwDoctorSuppressAutoDl=true;
    var a0=document.getElementById('download-btn');
    var prev=(a0&&a0.getAttribute('href'))||'';
    var tries=0;
    armIv=setInterval(function(){
      if(++tries>720){ clearInterval(armIv); armIv=null; window.__jwDoctorSuppressAutoDl=false; return; }
      var a=document.getElementById('download-btn');
      var href=(a&&a.getAttribute('href'))||'';
      if(href.indexOf('blob:')!==0 || href===prev) return;
      clearInterval(armIv); armIv=null;
      var name=a.getAttribute('download')||'merged.jwlibrary';
      fetch(href).then(function(r){ return r.blob(); }).then(function(b){
        var file; try{ file=new File([b],name,{type:'application/octet-stream'}); }catch(_){ file=b; }
        // small delay so the celebration overlay mounts beneath first
        setTimeout(function(){ openDoctor(file,{auto:true}); },1200);
      }).catch(function(){
        // fall back to the normal merged-file download
        window.__jwDoctorSuppressAutoDl=false;
        try{ var fa=document.getElementById('download-btn'); if(fa) fa.click(); }catch(_){}
      });
    },500);
  };

  window.__openJwDoctor = openDoctor;""",
"""  window.__openJwDoctor = openDoctor;
  // Localised Doctor strings for other modules (the pre-merge impact card
  // renders the worker's doctor report with these).
  window.__jwDoctorT = function(k){ return t(k); };""",
'watcher removal + __jwDoctorT')

# ── 3) doctor i18n: will_fix key (anchored on done_ready, all 12 langs) ─────
WILLFIX = [
    ('done_ready:"Your cleaned backup is ready to download."',
     'will_fix:"These will be fixed automatically in your merged file."'),
    ('done_ready:"Tu copia limpia está lista para descargar."',
     'will_fix:"Se corregirán automáticamente en tu archivo combinado."'),
    ('done_ready:"Seu backup limpo está pronto para baixar."',
     'will_fix:"Serão corrigidos automaticamente no seu arquivo mesclado."'),
    ('done_ready:"Votre sauvegarde nettoyée est prête à télécharger."',
     'will_fix:"Ils seront corrigés automatiquement dans votre fichier fusionné."'),
    ('done_ready:"Deine bereinigte Sicherung ist bereit zum Download."',
     'will_fix:"Diese werden in deiner zusammengeführten Datei automatisch behoben."'),
    ('done_ready:"Il tuo backup pulito è pronto da scaricare."',
     'will_fix:"Saranno corretti automaticamente nel file unito."'),
    ('done_ready:"Ваша очищенная копия готова к скачиванию."',
     'will_fix:"Они будут автоматически исправлены в объединённом файле."'),
    ('done_ready:"クリーンなバックアップの準備ができました。"',
     'will_fix:"結合ファイルでは自動的に修復されます。"'),
    ('done_ready:"정리된 백업이 준비되었습니다."',
     'will_fix:"병합된 파일에서 자동으로 수정됩니다."'),
    ('done_ready:"Handa nang i-download ang malinis mong backup."',
     'will_fix:"Awtomatikong aayusin ang mga ito sa iyong pinagsamang file."'),
    ('done_ready:"Din rensade säkerhetskopia är redo att laddas ner."',
     'will_fix:"Dessa åtgärdas automatiskt i din sammanslagna fil."'),
    ('done_ready:"Andam na ang limpyo nimong backup nga i-download."',
     'will_fix:"Awtomatikong ayohon kini sa imong gisagol nga file."'),
]
for anchor, key in WILLFIX:
    rep(anchor, anchor + ',' + key, 'will_fix ' + anchor[:34])

# ── 4) impact module: CSS swap ───────────────────────────────────────────────
rep(""".jip-doctor{display:flex;align-items:center;gap:9px;margin:-8px 0 16px;padding:10px 12px;background:rgba(71,85,105,.12);border:1px solid rgba(71,85,105,.3);border-radius:9px;cursor:pointer}
.jip-doctor:hover{border-color:rgba(234,88,12,.4)}
.jip-doctor input{accent-color:#ea580c;width:15px;height:15px;flex:0 0 auto;cursor:pointer;margin:0}
.jip-doctor span{font-size:12.5px;color:#cbd5e1;line-height:1.4}""",
""".jip-doc{margin:-8px 0 16px;padding:11px 13px;background:rgba(234,88,12,.05);border:1px solid rgba(234,88,12,.25);border-radius:10px}
.jip-doc-head{font-size:11.5px;font-weight:700;color:#fdba74;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.jip-doc-sub{font-size:12.5px;font-weight:600;color:#fbbf24;margin-bottom:4px}
.jip-doc-row{display:flex;align-items:center;justify-content:space-between;padding:4px 0;font-size:13px;color:#cbd5e1}
.jip-doc-num{font-weight:700;color:#fbbf24;font-variant-numeric:tabular-nums}
.jip-doc-note{margin-top:7px;font-size:11.5px;line-height:1.45;color:#34d399}
.jip-doc-perfect{font-size:12.5px;font-weight:600;color:#34d399}""",
'impact css')

# ── 5) impact module: label helper replaces the pref helper ─────────────────
rep("""  function doctorPref(){ try{ return localStorage.getItem('jwsync_doctor_after_merge')==='1'; }catch(_){ return false; } }
  window.__jwImpactPreview = function (counts) {
    counts = counts || {};""",
"""  // Localised label for the one-shot checkbox under 'Create My Merged File'
  // (rendered by the React app in js/app.js).
  window.__jwDoctorCbLabel = function(){ return t('doctor'); };

  window.__jwImpactPreview = function (counts, doctor) {
    counts = counts || {};
    var docGroup = '';
    if (doctor && doctor.checks) {
      var dt = function(k){ return (typeof window.__jwDoctorT==='function') ? window.__jwDoctorT(k) : k; };
      var inner = '';
      ['dup_notes','empty_notes','dup_marks','orph_br','orph_tm','unused_tags','unused_loc'].forEach(function(k){
        var n = doctor.checks[k]||0;
        if (n>0) inner += '<div class="jip-doc-row"><span>'+esc(dt('c_'+k))+'</span><span class="jip-doc-num">'+n+'</span></div>';
      });
      docGroup =
        '<div class="jip-doc">'+
          '<div class="jip-doc-head">'+esc(dt('title'))+'</div>'+
          (doctor.issues>0
            ? '<div class="jip-doc-sub">'+esc(String(doctor.issues===1?dt('issues_one'):dt('issues_many')).replace('{n}', doctor.issues))+'</div>'+inner+
              '<div class="jip-doc-note">'+esc(dt('will_fix'))+'</div>'
            : '<div class="jip-doc-perfect">'+esc(dt('perfect'))+'</div>')+
        '</div>';
    }""",
'impact signature + doc group')

# ── 6) impact markup: checkbox row → doctor group ────────────────────────────
rep("""            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          '<label class="jip-doctor"><input type="checkbox" data-jip-doctor'+(doctorPref()?' checked':'')+'><span>'+esc(t('doctor'))+'</span></label>'+
          '<div class="jip-actions">'+""",
"""            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          docGroup+
          '<div class="jip-actions">'+""",
'impact markup')

# ── 7) impact confirm handler back to the original one-liner ────────────────
rep("""      overlay.querySelector('[data-jip-go]').addEventListener('click', function(){
        var cb = overlay.querySelector('[data-jip-doctor]');
        if (cb) {
          try { localStorage.setItem('jwsync_doctor_after_merge', cb.checked ? '1' : '0'); } catch (_) {}
          if (cb.checked && typeof window.__jwDoctorArmAfterMerge === 'function') window.__jwDoctorArmAfterMerge();
        }
        done(true);
      });""",
"""      overlay.querySelector('[data-jip-go]').addEventListener('click', function(){ done(true); });""",
'confirm handler revert')

# ── 8) version bump ──────────────────────────────────────────────────────────
rep('"softwareVersion": "2.64.1"', '"softwareVersion": "2.65.0"', 'version')

io.open(f, 'w', encoding='utf-8').write(c)
print('OK: beta/index.html patched')

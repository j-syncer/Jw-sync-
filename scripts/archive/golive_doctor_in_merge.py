# -*- coding: utf-8 -*-
"""GO LIVE (v2.65.2): port the beta Library-Doctor-in-merge batch to production.

Mirrors into the production files the NET final state of beta (v2.64.0 →
v2.65.2), skipping the superseded v2.64.x intermediates:
  - js/merge-worker.js : headless Library Doctor (opts.doctorCheck)
  - js/app.js          : one-shot checkbox under 'Create My Merged File'
  - index.html         : impact-card Doctor group, mobile scroll cap,
                         goToHighlights shared-session hand-off,
                         will_fix i18n + __jwDoctorT + __jwDoctorCbLabel
Bumps softwareVersion 2.63.3 → 2.65.2 and CACHE_VERSION.
"""
import io, re, sys

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

def rep(c, old, new, what):
    must(c.count(old) == 1, what + ' anchor not unique: %d' % c.count(old))
    return c.replace(old, new, 1)

# 12-language values, in DOC_I18N order: en es pt fr de it ru ja ko tl sv ceb
DOCTOR_LABEL = [
  'Health-check & clean the merged file before downloading (Library Doctor)',
  'Revisar y limpiar el archivo combinado antes de descargarlo (Doctor de Biblioteca)',
  'Examinar e limpar o arquivo mesclado antes de baixar (Doutor da Biblioteca)',
  'Vérifier et nettoyer le fichier fusionné avant le téléchargement (Docteur de Bibliothèque)',
  'Zusammengeführte Datei vor dem Download prüfen und bereinigen (Bibliothek-Doktor)',
  'Controlla e pulisci il file unito prima di scaricarlo (Dottore della Biblioteca)',
  'Проверить и очистить объединённый файл перед скачиванием (Доктор библиотеки)',
  'ダウンロード前に結合ファイルを診断してクリーンアップ（ライブラリードクター）',
  '다운로드 전에 병합된 파일을 검진하고 정리 (라이브러리 닥터)',
  'Suriin at linisin ang pinagsamang file bago i-download (Library Doctor)',
  'Hälsokolla och rensa den sammanslagna filen före nedladdning (Biblioteksdoktorn)',
  'Susiha ug limpyohi ang gisagol nga file una i-download (Library Doctor)',
]
WILL_FIX = [
  'These will be fixed automatically in your merged file.',
  'Se corregirán automáticamente en tu archivo combinado.',
  'Serão corrigidos automaticamente no seu arquivo mesclado.',
  'Ils seront corrigés automatiquement dans votre fichier fusionné.',
  'Diese werden in deiner zusammengeführten Datei automatisch behoben.',
  'Saranno corretti automaticamente nel file unito.',
  'Они будут автоматически исправлены в объединённом файле.',
  '結合ファイルでは自動的に修復されます。',
  '병합된 파일에서 자동으로 수정됩니다.',
  'Awtomatikong aayusin ang mga ito sa iyong pinagsamang file.',
  'Dessa åtgärdas automatiskt i din sammanslagna fil.',
  'Awtomatikong ayohon kini sa imong gisagol nga file.',
]

# ════════════════════════════════════════════════════════════════════════════
# 1) js/merge-worker.js — same two edits applied to beta
# ════════════════════════════════════════════════════════════════════════════
mwf = 'js/merge-worker.js'
mw = io.open(mwf, encoding='utf-8').read()
beta_mw = io.open('beta/js/merge-worker.js', encoding='utf-8').read()

# extract the doctor block + the impact-message change straight from beta so
# they are byte-identical
doc_block = re.search(r'// ═+ Library Doctor.*?// ═+ end Library Doctor[^\n]*\n', beta_mw, re.S).group(0)

mw = rep(mw,
"""function classifyError(e) {
  const m = ((e && e.message) || '').toLowerCase();
  if (m.includes('memory') || m.includes('allocation') || e instanceof RangeError) return 'oversize';
  if (m.includes('zip') || m.includes('end of central') || m.includes('corrupt')) return 'corrupt';
  if (m.includes('sqlite') || m.includes('database') || m.includes('file is not a database')) return 'not_sqlite';
  return '';
}
""",
"""function classifyError(e) {
  const m = ((e && e.message) || '').toLowerCase();
  if (m.includes('memory') || m.includes('allocation') || e instanceof RangeError) return 'oversize';
  if (m.includes('zip') || m.includes('end of central') || m.includes('corrupt')) return 'corrupt';
  if (m.includes('sqlite') || m.includes('database') || m.includes('file is not a database')) return 'not_sqlite';
  return '';
}

""" + doc_block,
'mw classifyError/doctor block')

mw = rep(mw,
"""  // ── Pre-merge impact preview gate ──────────────────────────────────────
  if (p.previewConfirm) {
    self.postMessage({ type: 'impact', counts: {
      Note: f.Note, UserMark: f.UserMark, Bookmark: f.Bookmark, Tag: f.Tag,
      Updated: f.Updated, Deduplicated: f.Deduplicated, InputField: f.InputFields || 0
    } });
    const proceed = await new Promise(res => { confirmResolver = res; });
    if (!proceed) {
      try { a.close(); } catch {}
      a = null;
      return { cancelled: true };
    }
  }""",
"""  // ── Pre-merge impact preview gate ──────────────────────────────────────
  if (p.previewConfirm) {
    // Opt-in Library Doctor: scan the fully merged database headlessly and
    // send the findings along with the impact card; fix them only after the
    // user confirms. A scan failure never blocks the merge.
    let doctorReport = null;
    if (p.doctorCheck) {
      log('Library Doctor: examining the merged result...');
      try { doctorReport = doctorScan(a); } catch (e) { doctorReport = null; }
    }
    self.postMessage({ type: 'impact', counts: {
      Note: f.Note, UserMark: f.UserMark, Bookmark: f.Bookmark, Tag: f.Tag,
      Updated: f.Updated, Deduplicated: f.Deduplicated, InputField: f.InputFields || 0
    }, doctor: doctorReport });
    const proceed = await new Promise(res => { confirmResolver = res; });
    if (!proceed) {
      try { a.close(); } catch {}
      a = null;
      return { cancelled: true };
    }
    if (doctorReport && doctorReport.issues > 0) {
      log('Library Doctor: fixing ' + doctorReport.issues + ' issue(s)...');
      try { f.Cleaned += doctorFix(a); } catch (e) { log('Library Doctor: cleanup skipped (' + (e && e.message) + ')', false); }
    }
  }""",
'mw impact gate')
io.open(mwf, 'w', encoding='utf-8').write(mw)
print('OK: js/merge-worker.js')

# ════════════════════════════════════════════════════════════════════════════
# 2) js/app.js — same four edits applied to beta
# ════════════════════════════════════════════════════════════════════════════
af = 'js/app.js'
a = io.open(af, encoding='utf-8').read()
a = rep(a, 's("create_merged"))),oe&&ie&&ie.total>0',
    's("create_merged"))),l?React.createElement("label",{id:"doctor-merge-row",'
    'className:"flex items-center justify-center gap-2 mt-3 text-sm text-stone-400 hover:text-stone-300 cursor-pointer select-none"},'
    'React.createElement("input",{id:"doctor-merge-cb",type:"checkbox",defaultChecked:!1,'
    'style:{width:"15px",height:"15px",accentColor:"#ea580c",cursor:"pointer",flexShrink:0}}),'
    'React.createElement("span",null,window.__jwDoctorCbLabel?window.__jwDoctorCbLabel():"Health-check & clean the merged file (Library Doctor)")):null,'
    'oe&&ie&&ie.total>0', 'app checkbox markup')
a = rep(a, 'vt=async()=>{if(!l||!M)return;var n,i;',
    'vt=async()=>{if(!l||!M)return;var n,i;'
    'var __doctorOnce=!1;try{var __dcb=document.getElementById("doctor-merge-cb");'
    'if(__dcb){__doctorOnce=!!__dcb.checked;__dcb.checked=!1;}}catch(_){}', 'app vt read/reset')
a = rep(a, 'opts:Object.assign({},p,{previewConfirm:!0})',
    'opts:Object.assign({},p,{previewConfirm:!0,doctorCheck:__doctorOnce})', 'app opts doctorCheck')
a = rep(a, 'await window.__jwImpactPreview(d.counts):!0',
    'await window.__jwImpactPreview(d.counts,d.doctor||null):!0', 'app impact passthrough')
io.open(af, 'w', encoding='utf-8').write(a)
print('OK: js/app.js')

# ════════════════════════════════════════════════════════════════════════════
# 3) index.html
# ════════════════════════════════════════════════════════════════════════════
hf = 'index.html'
c = io.open(hf, encoding='utf-8').read()

# 3a) impact i18n: append doctor key after each study_answers tail (doc order)
sa_tails = re.findall(r"study_answers:(?:'[^']*'|\"[^\"]*\")\}", c)
must(len(sa_tails) == 12, 'expected 12 study_answers tails, found %d' % len(sa_tails))
for i, tail in enumerate(sa_tails):
    must(c.count(tail) == 1, 'study_answers tail not unique: %s' % tail)
    c = c.replace(tail, tail[:-1] + ",doctor:'" + DOCTOR_LABEL[i].replace("'", "\\'") + "'}", 1)
print('OK: index.html impact doctor i18n (12)')

# 3b) impact CSS: doctor group + scrollable card
c = rep(c, '.jip-btn-go:hover{background:#c2410c}',
'.jip-btn-go:hover{background:#c2410c}\n'
'.jip-doc{margin:-8px 0 16px;padding:11px 13px;background:rgba(234,88,12,.05);border:1px solid rgba(234,88,12,.25);border-radius:10px}\n'
'.jip-doc-head{font-size:11.5px;font-weight:700;color:#fdba74;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}\n'
'.jip-doc-sub{font-size:12.5px;font-weight:600;color:#fbbf24;margin-bottom:4px}\n'
'.jip-doc-row{display:flex;align-items:center;justify-content:space-between;padding:4px 0;font-size:13px;color:#cbd5e1}\n'
'.jip-doc-num{font-weight:700;color:#fbbf24;font-variant-numeric:tabular-nums}\n'
'.jip-doc-note{margin-top:7px;font-size:11.5px;line-height:1.45;color:#34d399}\n'
'.jip-doc-perfect{font-size:12.5px;font-weight:600;color:#34d399}', 'impact doc css')

c = rep(c,
'.jip-card{position:relative;width:100%;max-width:430px;background:rgba(4,15,34,.97);border:1px solid #1f2a3d;border-radius:16px;padding:26px 24px 20px;box-shadow:0 12px 40px rgba(0,0,0,.5);color:#e2e8f0;font-family:inherit}',
'.jip-card{position:relative;width:100%;max-width:430px;max-height:calc(100vh - 40px);max-height:calc(100dvh - 40px);overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;background:rgba(4,15,34,.97);border:1px solid #1f2a3d;border-radius:16px;padding:26px 24px 20px;box-shadow:0 12px 40px rgba(0,0,0,.5);color:#e2e8f0;font-family:inherit}',
'impact card scroll')

# 3c) __jwImpactPreview signature + docGroup + __jwDoctorCbLabel
c = rep(c,
"""  window.__jwImpactPreview = function (counts) {
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
'impact signature + docGroup')

# 3d) docGroup into the markup
c = rep(c,
"""            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          '<div class="jip-actions">'+""",
"""            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          docGroup+
          '<div class="jip-actions">'+""",
'impact markup docGroup')

# 3e) doctor i18n: append will_fix after each err_db tail (doc order)
err_tails = re.findall(r'err_db:"[^"]*"\}', c)
must(len(err_tails) == 12, 'expected 12 err_db tails, found %d' % len(err_tails))
for i, tail in enumerate(err_tails):
    must(c.count(tail) == 1, 'err_db tail not unique: %s' % tail)
    c = c.replace(tail, tail[:-1] + ',will_fix:"' + WILL_FIX[i] + '"}', 1)
print('OK: index.html doctor will_fix i18n (12)')

# 3f) __jwDoctorT export
c = rep(c, '  window.__openJwDoctor = openDoctor;',
"""  window.__openJwDoctor = openDoctor;
  // Localised Doctor strings for other modules (the pre-merge impact card
  // renders the worker's doctor report with these).
  window.__jwDoctorT = function(k){ return t(k); };""",
'doctor __jwDoctorT')

# 3g) goToHighlights → shared-session hand-off
c = rep(c,
"""  function goToHighlights() {
    var blobUrl = cached && cached.blobUrl;
    var name = (cached && cached.name) || 'merged.jwlibrary';
    var href = 'highlights.html';
    if (!blobUrl) { window.location.href = href; return; }
    fetch(blobUrl)
      .then(function(r) { return r.arrayBuffer(); })
      .then(function(buf) {
        var req = indexedDB.open('jwsync_hl_v1', 1);
        req.onupgradeneeded = function(e) { e.target.result.createObjectStore('pending'); };
        req.onsuccess = function(e) {
          var db = e.target.result;
          var tx = db.transaction('pending', 'readwrite');
          tx.objectStore('pending').put({ name: name, buffer: buf }, 'next');
          tx.oncomplete = function() { db.close(); window.location.href = href; };
          tx.onerror = function() { db.close(); window.location.href = href; };
        };
        req.onerror = function() { window.location.href = href; };
      })
      .catch(function() { window.location.href = href; });
  }""",
"""  function goToHighlights() {
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
  }""",
'goToHighlights')

# 3h) version bump
c = rep(c, '"softwareVersion": "2.63.3"', '"softwareVersion": "2.65.2"', 'version')
io.open(hf, 'w', encoding='utf-8').write(c)
print('OK: index.html')

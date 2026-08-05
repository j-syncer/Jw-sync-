/* ──────────────────────────────────────────────────────────────────────────
   conflict-review.js — Merge conflict review UI (window.__jwConflictReview).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.4.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  var SQLJS_URL = 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';

  var I18N = {
    en: { title:"Review your merge", subtitle:"{n} notes were edited differently across your backups. Choose which version to keep — or keep both.", current:"In your merge", keep_this:"Keep this", kept:"✓ Kept", keep_both:"Keep both", keep_both_on:"✓ Keeping both", keep_both_hint:"Adds the other version as a separate note", modified:"Edited", apply:"Apply & download", applying:"Applying…", skip:"Keep merge as-is", close:"Close", untitled:"(untitled note)", empty:"(empty)", more:"+{n} more conflicts will keep the merge's automatic choice.", merged_label:"Merged result" , suggest:"Suggest best",suggested:"Suggested",sg_content:"Has content",sg_newer:"Most recent edit",sg_longer:"Most detailed" },
    es: { title:"Revisa tu fusión", subtitle:"{n} notas se editaron de forma diferente en tus copias. Elige qué versión conservar — o conserva ambas.", current:"En tu fusión", keep_this:"Conservar esta", kept:"✓ Conservada", keep_both:"Conservar ambas", keep_both_on:"✓ Conservando ambas", keep_both_hint:"Añade la otra versión como una nota aparte", modified:"Editada", apply:"Aplicar y descargar", applying:"Aplicando…", skip:"Dejar la fusión como está", close:"Cerrar", untitled:"(nota sin título)", empty:"(vacío)", more:"+{n} conflictos más mantendrán la elección automática de la fusión.", merged_label:"Resultado de la fusión" , suggest:"Sugerir la mejor",suggested:"Sugerida",sg_content:"Tiene contenido",sg_newer:"Edición más reciente",sg_longer:"Más detallada" },
    pt: { title:"Revise sua mesclagem", subtitle:"{n} notas foram editadas de forma diferente nos seus backups. Escolha qual versão manter — ou mantenha ambas.", current:"Na sua mesclagem", keep_this:"Manter esta", kept:"✓ Mantida", keep_both:"Manter ambas", keep_both_on:"✓ Mantendo ambas", keep_both_hint:"Adiciona a outra versão como uma nota separada", modified:"Editada", apply:"Aplicar e baixar", applying:"Aplicando…", skip:"Manter a mesclagem como está", close:"Fechar", untitled:"(nota sem título)", empty:"(vazio)", more:"+{n} conflitos manterão a escolha automática da mesclagem.", merged_label:"Resultado da mesclagem" , suggest:"Sugerir a melhor",suggested:"Sugerida",sg_content:"Tem conteúdo",sg_newer:"Edição mais recente",sg_longer:"Mais detalhada" },
    fr: { title:"Vérifiez votre fusion", subtitle:"{n} notes ont été modifiées différemment dans vos sauvegardes. Choisissez la version à conserver — ou gardez les deux.", current:"Dans votre fusion", keep_this:"Garder celle-ci", kept:"✓ Conservée", keep_both:"Garder les deux", keep_both_on:"✓ Les deux conservées", keep_both_hint:"Ajoute l'autre version comme note distincte", modified:"Modifiée", apply:"Appliquer et télécharger", applying:"Application…", skip:"Laisser la fusion telle quelle", close:"Fermer", untitled:"(note sans titre)", empty:"(vide)", more:"+{n} autres conflits conserveront le choix automatique de la fusion.", merged_label:"Résultat de la fusion" , suggest:"Suggérer la meilleure",suggested:"Suggérée",sg_content:"Contient du texte",sg_newer:"Édition la plus récente",sg_longer:"La plus détaillée" },
    de: { title:"Prüfe deine Zusammenführung", subtitle:"{n} Notizen wurden in deinen Backups unterschiedlich bearbeitet. Wähle, welche Version bleibt — oder behalte beide.", current:"In deiner Zusammenführung", keep_this:"Diese behalten", kept:"✓ Behalten", keep_both:"Beide behalten", keep_both_on:"✓ Beide behalten", keep_both_hint:"Fügt die andere Version als separate Notiz hinzu", modified:"Bearbeitet", apply:"Anwenden & herunterladen", applying:"Wird angewendet…", skip:"Zusammenführung unverändert lassen", close:"Schließen", untitled:"(Notiz ohne Titel)", empty:"(leer)", more:"+{n} weitere Konflikte behalten die automatische Auswahl der Zusammenführung.", merged_label:"Ergebnis der Zusammenführung" , suggest:"Beste vorschlagen",suggested:"Vorschlag",sg_content:"Hat Inhalt",sg_newer:"Neueste Änderung",sg_longer:"Am ausführlichsten" },
    it: { title:"Controlla la tua unione", subtitle:"{n} note sono state modificate in modo diverso nei tuoi backup. Scegli quale versione mantenere — o tienile entrambe.", current:"Nella tua unione", keep_this:"Tieni questa", kept:"✓ Mantenuta", keep_both:"Tieni entrambe", keep_both_on:"✓ Entrambe mantenute", keep_both_hint:"Aggiunge l'altra versione come nota separata", modified:"Modificata", apply:"Applica e scarica", applying:"Applicazione…", skip:"Lascia l'unione com'è", close:"Chiudi", untitled:"(nota senza titolo)", empty:"(vuoto)", more:"+{n} altri conflitti manterranno la scelta automatica dell'unione.", merged_label:"Risultato dell'unione" , suggest:"Suggerisci la migliore",suggested:"Suggerita",sg_content:"Ha contenuto",sg_newer:"Modifica più recente",sg_longer:"Più dettagliata" },
    ru: { title:"Проверьте объединение", subtitle:"{n} заметок были изменены по-разному в ваших копиях. Выберите, какую версию оставить — или оставьте обе.", current:"В объединении", keep_this:"Оставить эту", kept:"✓ Оставлено", keep_both:"Оставить обе", keep_both_on:"✓ Обе оставлены", keep_both_hint:"Добавит другую версию как отдельную заметку", modified:"Изменено", apply:"Применить и скачать", applying:"Применение…", skip:"Оставить как есть", close:"Закрыть", untitled:"(заметка без названия)", empty:"(пусто)", more:"+{n} других конфликтов сохранят автоматический выбор объединения.", merged_label:"Результат объединения" , suggest:"Предложить лучшее",suggested:"Рекомендуется",sg_content:"Есть содержимое",sg_newer:"Последнее изменение",sg_longer:"Наиболее подробная" },
    ja: { title:"マージを確認", subtitle:"{n} 件のメモがバックアップ間で異なる形で編集されています。残すバージョンを選ぶか、両方を残せます。", current:"マージ結果", keep_this:"これを残す", kept:"✓ 残しました", keep_both:"両方残す", keep_both_on:"✓ 両方を残す", keep_both_hint:"もう一方を別のメモとして追加します", modified:"編集", apply:"適用してダウンロード", applying:"適用中…", skip:"マージのままにする", close:"閉じる", untitled:"(無題のメモ)", empty:"(空)", more:"他 +{n} 件の競合はマージの自動選択を維持します。", merged_label:"マージ結果" , suggest:"おすすめを提案",suggested:"おすすめ",sg_content:"内容あり",sg_newer:"最新の編集",sg_longer:"最も詳しい" },
    ko: { title:"병합 검토", subtitle:"{n}개의 메모가 백업마다 다르게 편집되었습니다. 어떤 버전을 남길지 선택하거나 둘 다 보관하세요.", current:"병합 결과", keep_this:"이것 남기기", kept:"✓ 남김", keep_both:"둘 다 남기기", keep_both_on:"✓ 둘 다 보관", keep_both_hint:"다른 버전을 별도의 메모로 추가합니다", modified:"편집됨", apply:"적용 후 다운로드", applying:"적용 중…", skip:"병합 그대로 두기", close:"닫기", untitled:"(제목 없는 메모)", empty:"(비어 있음)", more:"+{n}개의 추가 충돌은 병합의 자동 선택을 유지합니다.", merged_label:"병합 결과" , suggest:"최적 추천",suggested:"추천",sg_content:"내용 있음",sg_newer:"가장 최근 편집",sg_longer:"가장 상세함" },
    tl: { title:"Suriin ang merge", subtitle:"{n} na tala ang iba't iba ang pagkaka-edit sa iyong mga backup. Piliin kung aling bersyon ang itatago — o itago ang pareho.", current:"Sa iyong merge", keep_this:"Itago ito", kept:"✓ Itinago", keep_both:"Itago pareho", keep_both_on:"✓ Itinatago pareho", keep_both_hint:"Idaragdag ang isa pang bersyon bilang hiwalay na tala", modified:"In-edit", apply:"Ilapat at i-download", applying:"Inilalapat…", skip:"Iwan ang merge", close:"Isara", untitled:"(talang walang pamagat)", empty:"(walang laman)", more:"+{n} pang conflicts ang magpapanatili ng awtomatikong pili ng merge.", merged_label:"Resulta ng merge" , suggest:"Imungkahi ang pinakamahusay",suggested:"Iminumungkahi",sg_content:"May nilalaman",sg_newer:"Pinakabagong edit",sg_longer:"Pinakadetalyado" }
  ,sv:{title:"Granska din sammanslagning",subtitle:"{n} anteckningar redigerades olika i dina säkerhetskopior. Välj vilken version du vill behålla — eller behåll båda.",current:"I din sammanslagning",keep_this:"Behåll denna",kept:"✓ Behållen",keep_both:"Behåll båda",keep_both_on:"✓ Behåller båda",keep_both_hint:"Lägger till den andra versionen som en separat anteckning",modified:"Ändrad",apply:"Tillämpa och ladda ner",applying:"Tillämpar…",skip:"Behåll sammanslagningen som den är",close:"Stäng",untitled:"(namnlös anteckning)",empty:"(tom)",more:"+{n} fler konflikter behåller sammanslagningens automatiska val.",merged_label:"Sammanslaget resultat",suggest:"Föreslå bästa",suggested:"Föreslagen",sg_content:"Har innehåll",sg_newer:"Senaste ändringen",sg_longer:"Mest detaljerad"},ceb:{title:"Susihon ang merge",subtitle:"{n} ka nota ang lain-laing gibag-o sa imong mga backup. Pilia kon unsang bersyon ang tipigan — o tipigan ang pareho.",current:"Sa imong merge",keep_this:"Tipigan kini",kept:"✓ Gitipig",keep_both:"Tipigan pareho",keep_both_on:"✓ Gitipig pareho",keep_both_hint:"Idugang ang laing bersyon isip lain-laing nota",modified:"Gibag-o",apply:"Ilapat ug i-download",applying:"Giilapat…",skip:"Biyaan ang merge",close:"Isira",untitled:"(nota nga walay titulo)",empty:"(wala)",more:"+{n} pa nga conflicts ang mogamit sa awtomatikong pagpili sa merge.",merged_label:"Resulta sa merge",suggest:"Imungkahi ang labing maayo",suggested:"Girekomenda",sg_content:"May sulod",sg_newer:"Pinakabag-o nga pag-edit",sg_longer:"Pinaka-detalyado"},ar:{title:"راجِع عملية الدمج",subtitle:"جرى تعديل {n} ملاحظة بصور مختلفة بين نسخك الاحتياطية. اختر النسخة التي تريد الاحتفاظ بها — أو احتفظ بالاثنتين.",current:"في ملف الدمج",keep_this:"احتفظ بهذه",kept:"✓ تم الاحتفاظ",keep_both:"احتفظ بالاثنتين",keep_both_on:"✓ الاحتفاظ بالاثنتين",keep_both_hint:"يضيف النسخة الأخرى كملاحظة مستقلة",modified:"مُعدَّلة",apply:"تطبيق وتنزيل",applying:"جارٍ التطبيق…",skip:"أبقِ الدمج كما هو",close:"إغلاق",untitled:"(ملاحظة بلا عنوان)",empty:"(فارغة)",more:"+{n} تعارض إضافي سيبقى على الاختيار التلقائي للدمج.",merged_label:"نتيجة الدمج",suggest:"اقترح الأفضل",suggested:"مُقترَحة",sg_content:"تحتوي على محتوى",sg_newer:"أحدث تعديل",sg_longer:"الأكثر تفصيلًا"}};
  function curLang() { try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; } }
  function t(k) { var l = curLang(); return (I18N[l] && I18N[l][k]) || I18N.en[k] || k; }
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function stripHtml(s) { return String(s || '').replace(/<[^>]*>?/gm, ' ').replace(/\s+/g, ' ').trim(); }
  function clip(s) { s = String(s || ''); return s.length > 1400 ? s.slice(0, 1400) + '…' : s; }
  function fmtDate(s) {
    if (!s) return '';
    var d = new Date(s);
    if (isNaN(d.getTime())) return String(s);
    try { return d.toLocaleString(undefined, { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }); }
    catch (_) { return d.toISOString().slice(0, 16).replace('T', ' '); }
  }

  // ── Lightweight word-level diff (LCS) ──────────────────────────────
  function lcsDiff(o, n) {
    var m = o.length, k = n.length;
    var dp = []; for (var i = 0; i <= m; i++) dp.push(new Array(k + 1).fill(0));
    for (var a = m - 1; a >= 0; a--) for (var b = k - 1; b >= 0; b--)
      dp[a][b] = (o[a] === n[b]) ? dp[a + 1][b + 1] + 1 : Math.max(dp[a + 1][b], dp[a][b + 1]);
    var out = [], x = 0, y = 0;
    while (x < m && y < k) {
      if (o[x] === n[y]) { out.push({ t: 'eq', s: n[y] }); x++; y++; }
      else if (dp[x + 1][y] >= dp[x][y + 1]) { out.push({ t: 'del', s: o[x] }); x++; }
      else { out.push({ t: 'add', s: n[y] }); y++; }
    }
    while (x < m) out.push({ t: 'del', s: o[x++] });
    while (y < k) out.push({ t: 'add', s: n[y++] });
    return out;
  }
  function diffHtml(curPlain, altPlain) {
    var a = clip(curPlain).split(/(\s+)/), b = clip(altPlain).split(/(\s+)/);
    if (a.length > 600) a = a.slice(0, 600);
    if (b.length > 600) b = b.slice(0, 600);
    return lcsDiff(a, b).map(function (p) {
      if (p.t === 'eq') return esc(p.s);
      if (p.t === 'add') return '<span class="jcr-ins">' + esc(p.s) + '</span>';
      return '<span class="jcr-del">' + esc(p.s) + '</span>';
    }).join('');
  }

  // ── Source-file + DB helpers (all main-thread sql.js) ──────────────
  function readFileBuf(file) {
    if (!file) return Promise.reject(new Error('no file'));
    if (typeof file.arrayBuffer === 'function') return file.arrayBuffer();
    return new Promise(function (res, rej) {
      var r = new FileReader();
      r.onload = function () { res(r.result); };
      r.onerror = function () { rej(new Error('read failed')); };
      r.readAsArrayBuffer(file);
    });
  }
  function collectSourceFiles() {
    var out = [], seen = {};
    var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
    for (var i = 0; i < inputs.length; i++) {
      var fl = inputs[i].files; if (!fl) continue;
      for (var j = 0; j < fl.length; j++) {
        var f = fl[j]; if (!f) continue;
        var key = (f.name || '') + '::' + (f.size || 0);
        if (seen[key]) continue; seen[key] = 1; out.push(f);
      }
    }
    try {
      if (window.__jwLastFile) {
        var lf = window.__jwLastFile, k = (lf.name || '') + '::' + (lf.size || 0);
        if (!seen[k]) { seen[k] = 1; out.push(lf); }
      }
    } catch (_) {}
    return out;
  }
  function openDbFromBuffer(SQL, buf) {
    return window.JSZip.loadAsync(buf).then(function (zip) {
      var key = Object.keys(zip.files).find(function (f) { return /userdata\.db$/i.test(f); });
      if (!key) return null;
      return zip.file(key).async('uint8array').then(function (bytes) { return new SQL.Database(bytes); });
    });
  }
  function queryNotes(db) {
    var map = {};
    try {
      var r = db.exec('SELECT Guid,Title,Content,LastModified FROM Note');
      if (r.length && r[0].values) r[0].values.forEach(function (v) {
        if (v[0] == null) return;
        map[v[0]] = { title: v[1] || '', content: v[2] || '', lastMod: v[3] || '' };
      });
    } catch (_) {}
    return map;
  }

  // ── Detection: which notes were edited differently across backups ──
  function detect(opts) {
    if (typeof window.JSZip !== 'function' || typeof window.initSqlJs !== 'function') return Promise.resolve(null);
    var sources = collectSourceFiles();
    if (sources.length < 2) return Promise.resolve(null);
    var SQL;
    return window.initSqlJs({ locateFile: function (f) { return SQLJS_URL + f; } })
      .then(function (s) {
        SQL = s;
        return sources.reduce(function (chain, file, idx) {
          return chain.then(function (acc) {
            return readFileBuf(file)
              .then(function (buf) { return openDbFromBuffer(SQL, buf); })
              .then(function (db) {
                if (db) { acc.push({ name: file.name || ('Backup ' + (idx + 1)), notes: queryNotes(db) }); db.close(); }
                return acc;
              })
              .catch(function () { return acc; });
          });
        }, Promise.resolve([]));
      })
      .then(function (perFile) {
        if (perFile.length < 2) return null;
        return fetch(opts.blobUrl).then(function (r) { return r.arrayBuffer(); }).then(function (mergedBuf) {
          return openDbFromBuffer(SQL, mergedBuf).then(function (mdb) {
            if (!mdb) return null;
            var mergedNotes = queryNotes(mdb); mdb.close();

            var byGuid = {};
            perFile.forEach(function (pf) {
              Object.keys(pf.notes).forEach(function (guid) {
                var note = pf.notes[guid];
                (byGuid[guid] = byGuid[guid] || []).push({
                  file: pf.name, title: note.title, content: note.content,
                  key: stripHtml(note.content).toLowerCase(), lastMod: note.lastMod
                });
              });
            });

            var conflicts = [];
            Object.keys(byGuid).forEach(function (guid) {
              var list = byGuid[guid];
              if (list.length < 2) return;
              var variants = {};
              list.forEach(function (it) {
                if (!variants[it.key]) variants[it.key] = { key: it.key, content: it.content, title: it.title, plain: stripHtml(it.content), lastMod: it.lastMod, files: [it.file] };
                else { variants[it.key].files.push(it.file); if (String(it.lastMod) > String(variants[it.key].lastMod)) variants[it.key].lastMod = it.lastMod; }
              });
              var keys = Object.keys(variants);
              if (keys.length < 2) return; // identical everywhere → no conflict
              var varr = keys.map(function (k) { return variants[k]; });
              var mn = mergedNotes[guid];
              var curKey = mn ? stripHtml(mn.content).toLowerCase() : null;
              var curIdx = -1;
              for (var x = 0; x < varr.length; x++) { if (curKey != null && varr[x].key === curKey) { curIdx = x; break; } }
              if (curIdx === -1 && mn) {
                varr.unshift({ key: curKey, content: mn.content, title: mn.title, plain: stripHtml(mn.content), lastMod: mn.lastMod, files: [t('merged_label')], synthetic: true });
                curIdx = 0;
              }
              if (curIdx === -1) curIdx = 0;
              conflicts.push({ guid: guid, title: (mn && mn.title) || varr[curIdx].title || '', variants: varr, current: curIdx });
            });

            if (!conflicts.length) return null;
            // Stable order: most-recently-edited conflicts first
            conflicts.sort(function (p, q) {
              var pm = p.variants.reduce(function (a, v) { return String(v.lastMod) > a ? String(v.lastMod) : a; }, '');
              var qm = q.variants.reduce(function (a, v) { return String(v.lastMod) > a ? String(v.lastMod) : a; }, '');
              return qm < pm ? -1 : (qm > pm ? 1 : 0);
            });
            return { conflicts: conflicts, mergedBuf: mergedBuf, SQL: SQL };
          });
        });
      })
      .catch(function () { return null; });
  }

  // ── Apply overrides to the merged DB on the main thread ────────────
  function insertDup(db, cols, vals, variant) {
    var ic = [], iv = [];
    var ng = (window.crypto && crypto.randomUUID) ? crypto.randomUUID().toUpperCase() : ('JWSYNC-' + Date.now() + '-' + Math.random().toString(16).slice(2));
    for (var i = 0; i < cols.length; i++) {
      var c = cols[i]; if (c === 'NoteId') continue;
      var v = vals[i];
      if (c === 'Guid') v = ng;
      else if (c === 'Title') v = variant.title;
      else if (c === 'Content') v = variant.content;
      else if (c === 'LastModified') v = variant.lastMod || new Date().toISOString();
      ic.push('"' + c + '"'); iv.push(v);
    }
    db.run('INSERT INTO Note (' + ic.join(',') + ') VALUES (' + ic.map(function () { return '?'; }).join(',') + ')', iv);
  }
  function applyResolutions(ctx, resolutions) {
    var changed = false;
    return openDbFromBuffer(ctx.SQL, ctx.mergedBuf.slice(0)).then(function (db) {
      if (!db) return null;
      ctx.conflicts.forEach(function (cf, i) {
        var res = resolutions[i]; if (!res) return;
        if (res.choice === 'both') {
          var others = cf.variants.filter(function (_, idx) { return idx !== cf.current; });
          if (!others.length) return;
          try {
            var st = db.prepare('SELECT * FROM Note WHERE Guid = :g');
            st.bind({ ':g': cf.guid });
            var cols = null, vals = null;
            if (st.step()) { cols = st.getColumnNames(); vals = st.get(); }
            st.free();
            if (cols && vals) others.forEach(function (v) { try { insertDup(db, cols, vals, v); changed = true; } catch (_) {} });
          } catch (_) {}
        } else if (typeof res.choice === 'number' && res.choice !== cf.current) {
          var v = cf.variants[res.choice]; if (!v) return;
          try { db.run('UPDATE Note SET Title = ?, Content = ?, LastModified = ? WHERE Guid = ?', [v.title, v.content, v.lastMod || new Date().toISOString(), cf.guid]); changed = true; } catch (_) {}
        }
      });
      if (!changed) { try { db.close(); } catch (_) {} return null; }
      var out = db.export();
      try { db.close(); } catch (_) {}
      return window.JSZip.loadAsync(ctx.mergedBuf.slice(0)).then(function (zip) {
        var key = Object.keys(zip.files).find(function (f) { return /userdata\.db$/i.test(f); });
        zip.file(key, out);
        return zip.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });
      }).then(function (arr) {
        var url = URL.createObjectURL(new Blob([arr], { type: 'application/octet-stream' }));
        return { blobUrl: url, buffer: arr };
      });
    }).catch(function () { return null; });
  }

  // ── Public entry: called by the celebration before it shows ────────
  window.__jwConflictReview = function (opts) {
    opts = opts || {};
    return new Promise(function (resolve) {
      var settled = false, overlay = null;
      var refreshers = [], suggestions = {};
      function done(v) { if (settled) return; settled = true; cleanup(); resolve(v); }
      function cleanup() {
        if (overlay) { overlay.remove(); overlay = null; }
        document.body.classList.remove('jw-modal-open');
        document.removeEventListener('keydown', onKey);
      }
      function onKey(e) { if (e.key === 'Escape') done(null); }

      detect(opts).then(function (ctx) {
        if (!ctx) { done(null); return; }
        render(ctx);
      }).catch(function () { done(null); });

      function render(ctx) {
        var MAX = 100;
        var resolutions = ctx.conflicts.map(function (cf) { return { choice: cf.current }; });
        var shown = ctx.conflicts.slice(0, MAX);
        refreshers.length = 0; suggestions = {};

        var warnIcon = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 2 19a1 1 0 0 0 .87 1.5h18.26A1 1 0 0 0 22 19L12 2z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
        var dlIcon = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';

        var html =
          '<div class="jcr-backdrop" data-jcr-skip></div>' +
          '<div class="jcr-card" role="dialog" aria-modal="true" aria-labelledby="jcr-title">' +
            '<button class="jcr-close" type="button" data-jcr-skip aria-label="' + esc(t('close')) + '">×</button>' +
            '<div class="jcr-head">' +
              '<div class="jcr-icon">' + warnIcon + '</div>' +
              '<div><h2 id="jcr-title" class="jcr-title">' + esc(t('title')) + '</h2>' +
              '<p class="jcr-subtitle">' + esc(t('subtitle').replace('{n}', ctx.conflicts.length)) + '</p></div>' +
            '</div>' +
            '<div class="jcr-body" id="jcr-body"></div>' +
            (ctx.conflicts.length > MAX ? '<div class="jcr-more">' + esc(t('more').replace('{n}', ctx.conflicts.length - MAX)) + '</div>' : '') +
            '<div class="jcr-foot">' +
              '<button class="jcr-btn jcr-btn-ghost jcr-btn-suggest" type="button" data-jcr-suggest>' + esc(t('suggest')) + '</button>' +
              '<button class="jcr-btn jcr-btn-ghost" type="button" data-jcr-skip>' + esc(t('skip')) + '</button>' +
              '<button class="jcr-btn jcr-btn-primary" type="button" data-jcr-apply>' + dlIcon + '<span>' + esc(t('apply')) + '</span></button>' +
            '</div>' +
          '</div>';

        overlay = document.createElement('div');
        overlay.id = 'jw-conflict-overlay';
        overlay.innerHTML = html;
        document.body.appendChild(overlay);
        document.body.classList.add('jw-modal-open');

        var body = overlay.querySelector('#jcr-body');
        shown.forEach(function (cf, ci) { body.appendChild(buildConflict(cf, ci, resolutions)); });

        overlay.querySelectorAll('[data-jcr-skip]').forEach(function (el) {
          el.addEventListener('click', function () { done(null); });
        });
        var applyBtn = overlay.querySelector('[data-jcr-apply]');
        applyBtn.addEventListener('click', function () {
          applyBtn.disabled = true;
          var span = applyBtn.querySelector('span'); if (span) span.textContent = t('applying');
          applyResolutions(ctx, resolutions).then(function (r) { done(r); }).catch(function () { done(null); });
        });
        var suggestBtn = overlay.querySelector('[data-jcr-suggest]');
        if (suggestBtn) suggestBtn.addEventListener('click', function () {
          shown.forEach(function (cf, ci) { var s = suggestFor(cf); suggestions[ci] = s; if (s.reason) resolutions[ci] = { choice: s.vi }; });
          refreshers.forEach(function (fn) { fn(); });
        });
        document.addEventListener('keydown', onKey);
      }

      function suggestFor(cf) {
        var vs = cf.variants, nonEmpty = [];
        vs.forEach(function (v, i) { if (v.plain && v.plain.trim().length > 0) nonEmpty.push(i); });
        if (nonEmpty.length === 0) return { vi: cf.current, reason: null };
        if (nonEmpty.length === 1) return { vi: nonEmpty[0], reason: 'sg_content' };
        var withDate = nonEmpty.filter(function (i) { return vs[i].lastMod; });
        if (withDate.length === nonEmpty.length) {
          var sorted = withDate.slice().sort(function (a2, b2) { return new Date(vs[b2].lastMod) - new Date(vs[a2].lastMod); });
          if (new Date(vs[sorted[0]].lastMod).getTime() !== new Date(vs[sorted[1]].lastMod).getTime())
            return { vi: sorted[0], reason: 'sg_newer' };
        }
        var longest = nonEmpty.slice().sort(function (a2, b2) { return vs[b2].plain.length - vs[a2].plain.length; })[0];
        return { vi: longest, reason: 'sg_longer' };
      }

      function buildConflict(cf, ci, resolutions) {
        var wrap = document.createElement('div');
        wrap.className = 'jcr-conflict';
        var title = cf.title ? stripHtml(cf.title) : t('untitled');

        var head = document.createElement('div');
        head.className = 'jcr-conflict-head';
        head.innerHTML = '<span class="jcr-conflict-n">' + (ci + 1) + '</span><span class="jcr-conflict-title">' + esc(title) + '</span>';
        wrap.appendChild(head);

        var vers = document.createElement('div');
        vers.className = 'jcr-versions';
        var current = cf.variants[cf.current];
        cf.variants.forEach(function (v, vi) {
          var isCur = vi === cf.current;
          var card = document.createElement('div');
          card.className = 'jcr-ver' + (resolutions[ci].choice === vi ? ' sel' : '');
          card.setAttribute('data-vi', vi);
          var contentHtml = isCur ? esc(clip(v.plain)) : diffHtml(current.plain, v.plain);
          if (!contentHtml) contentHtml = '<span class="jcr-empty">' + esc(t('empty')) + '</span>';
          card.innerHTML =
            '<div class="jcr-ver-head">' +
              '<span class="jcr-ver-from">' + esc(v.files.join(', ')) + '</span>' +
              (isCur ? '<span class="jcr-ver-current">' + esc(t('current')) + '</span>' : '') +
            '</div>' +
            (v.lastMod ? '<div class="jcr-ver-date">' + esc(t('modified')) + ' ' + esc(fmtDate(v.lastMod)) + '</div>' : '') +
            '<div class="jcr-ver-body">' + contentHtml + '</div>' +
            '<button class="jcr-ver-pick" type="button">' + esc(resolutions[ci].choice === vi ? t('kept') : t('keep_this')) + '</button>';
          card.querySelector('.jcr-ver-pick').addEventListener('click', function () { resolutions[ci] = { choice: vi }; refresh(); });
          vers.appendChild(card);
        });
        wrap.appendChild(vers);

        var bothRow = document.createElement('div');
        bothRow.className = 'jcr-both-row';
        var bothBtn = document.createElement('button');
        bothBtn.type = 'button';
        bothBtn.className = 'jcr-both-btn' + (resolutions[ci].choice === 'both' ? ' on' : '');
        bothBtn.textContent = resolutions[ci].choice === 'both' ? t('keep_both_on') : t('keep_both');
        bothBtn.addEventListener('click', function () {
          resolutions[ci] = (resolutions[ci].choice === 'both') ? { choice: cf.current } : { choice: 'both' };
          refresh();
        });
        bothRow.appendChild(bothBtn);
        var hint = document.createElement('span');
        hint.className = 'jcr-both-hint';
        hint.textContent = t('keep_both_hint');
        bothRow.appendChild(hint);
        wrap.appendChild(bothRow);

        function refresh() {
          var sg = suggestions[ci];
          vers.querySelectorAll('.jcr-ver').forEach(function (card) {
            var vi = parseInt(card.getAttribute('data-vi'), 10);
            var sel = resolutions[ci].choice === vi;
            card.classList.toggle('sel', sel);
            var isSug = !!(sg && sg.reason && sg.vi === vi);
            card.classList.toggle('jcr-suggested', isSug);
            var badge = card.querySelector('.jcr-suggestion-badge');
            if (isSug) {
              if (!badge) { badge = document.createElement('span'); badge.className = 'jcr-suggestion-badge'; card.querySelector('.jcr-ver-head').appendChild(badge); }
              badge.textContent = t('suggested') + ' \u00b7 ' + t(sg.reason);
            } else if (badge) { badge.remove(); }
            card.querySelector('.jcr-ver-pick').textContent = sel ? t('kept') : t('keep_this');
          });
          var isBoth = resolutions[ci].choice === 'both';
          bothBtn.classList.toggle('on', isBoth);
          bothBtn.textContent = isBoth ? t('keep_both_on') : t('keep_both');
        }
        refreshers.push(refresh);

        return wrap;
      }
    });
  };
})();

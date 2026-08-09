/* ──────────────────────────────────────────────────────────────────────────
   impact-preview.js — Pre-merge impact preview card (window.__jwImpactPreview).
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';
  if (window.__jwImpactPreview) return;
  var I18N = {
    en:{title:'Ready to merge',sub:'Here’s what this merge will change. Review the numbers, then download your merged backup.',added:'Will be added',notes:'Notes',highlights:'Highlights',bookmarks:'Bookmarks',tags:'Tags',updated:'Notes updated (newer version wins)',deduped:'Duplicates skipped',confirm:'Merge & Download',cancel:'Cancel',study_answers:'Study answers',doctor:'Health-check & clean the merged file before downloading (Library Doctor)'},
    es:{title:'Listo para combinar',sub:'Esto es lo que cambiará esta combinación. Revisa los números y descarga tu copia combinada.',added:'Se añadirá',notes:'Notas',highlights:'Destacados',bookmarks:'Marcadores',tags:'Etiquetas',updated:'Notas actualizadas (gana la más reciente)',deduped:'Duplicados omitidos',confirm:'Combinar y descargar',cancel:'Cancelar',study_answers:'Respuestas de estudio',doctor:'Revisar y limpiar el archivo combinado antes de descargarlo (Doctor de Biblioteca)'},
    pt:{title:'Pronto para combinar',sub:'Veja o que esta combinação vai alterar. Revise os números e baixe seu backup combinado.',added:'Será adicionado',notes:'Notas',highlights:'Destaques',bookmarks:'Marcadores',tags:'Etiquetas',updated:'Notas atualizadas (vence a mais recente)',deduped:'Duplicatas ignoradas',confirm:'Combinar e baixar',cancel:'Cancelar',study_answers:'Respostas de estudo',doctor:'Examinar e limpar o arquivo mesclado antes de baixar (Doutor da Biblioteca)'},
    fr:{title:'Prêt à fusionner',sub:'Voici ce que cette fusion va modifier. Vérifiez les chiffres, puis téléchargez votre sauvegarde fusionnée.',added:'Sera ajouté',notes:'Notes',highlights:'Surlignages',bookmarks:'Signets',tags:'Étiquettes',updated:'Notes mises à jour (la plus récente l’emporte)',deduped:'Doublons ignorés',confirm:'Fusionner et télécharger',cancel:'Annuler',study_answers:'Réponses d’étude',doctor:'Vérifier et nettoyer le fichier fusionné avant le téléchargement (Docteur de Bibliothèque)'},
    de:{title:'Bereit zum Zusammenführen',sub:'Das wird beim Zusammenführen geändert. Prüfe die Zahlen und lade dann deine Sicherung herunter.',added:'Wird hinzugefügt',notes:'Notizen',highlights:'Markierungen',bookmarks:'Lesezeichen',tags:'Tags',updated:'Aktualisierte Notizen (neuere gewinnt)',deduped:'Duplikate übersprungen',confirm:'Zusammenführen & herunterladen',cancel:'Abbrechen',study_answers:'Studienantworten',doctor:'Zusammengeführte Datei vor dem Download prüfen und bereinigen (Bibliothek-Doktor)'},
    it:{title:'Pronto per l’unione',sub:'Ecco cosa cambierà questa unione. Controlla i numeri, poi scarica il backup unito.',added:'Verrà aggiunto',notes:'Note',highlights:'Evidenziazioni',bookmarks:'Segnalibri',tags:'Tag',updated:'Note aggiornate (vince la più recente)',deduped:'Duplicati saltati',confirm:'Unisci e scarica',cancel:'Annulla',study_answers:'Risposte di studio',doctor:'Controlla e pulisci il file unito prima di scaricarlo (Dottore della Biblioteca)'},
    ru:{title:'Готово к объединению',sub:'Вот что изменит это объединение. Проверьте числа и скачайте объединённую копию.',added:'Будет добавлено',notes:'Заметки',highlights:'Выделения',bookmarks:'Закладки',tags:'Метки',updated:'Обновлённые заметки (побеждает новейшая)',deduped:'Дубликаты пропущены',confirm:'Объединить и скачать',cancel:'Отмена',study_answers:'Ответы для изучения',doctor:'Проверить и очистить объединённый файл перед скачиванием (Доктор библиотеки)'},
    ja:{title:'結合の準備ができました',sub:'この結合で変わる内容です。数値を確認してから、結合したバックアップをダウンロードしてください。',added:'追加されます',notes:'ノート',highlights:'ハイライト',bookmarks:'しおり',tags:'タグ',updated:'更新されたノート（新しい方を採用）',deduped:'重複をスキップ',confirm:'結合してダウンロード',cancel:'キャンセル',study_answers:'学習の回答',doctor:'ダウンロード前に結合ファイルを診断してクリーンアップ（ライブラリードクター）'},
    ko:{title:'병합 준비 완료',sub:'이 병합으로 변경될 내용입니다. 숫자를 확인한 뒤 병합된 백업을 다운로드하세요.',added:'추가됨',notes:'노트',highlights:'하이라이트',bookmarks:'북마크',tags:'태그',updated:'업데이트된 노트(최신 버전 우선)',deduped:'중복 건너뜀',confirm:'병합 및 다운로드',cancel:'취소',study_answers:'학습 답변',doctor:'다운로드 전에 병합된 파일을 검진하고 정리 (라이브러리 닥터)'},
    tl:{title:'Handa nang i-merge',sub:'Ito ang babaguhin ng merge na ito. Suriin ang mga numero, pagkatapos i-download ang iyong pinagsamang backup.',added:'Idaragdag',notes:'Mga nota',highlights:'Mga highlight',bookmarks:'Mga bookmark',tags:'Mga tag',updated:'Na-update na nota (nananalo ang mas bago)',deduped:'Nilaktawang duplikado',confirm:'I-merge at i-download',cancel:'Kanselahin',study_answers:'Mga sagot sa pag-aaral',doctor:'Suriin at linisin ang pinagsamang file bago i-download (Library Doctor)'}
  ,sv:{title:"Redo att slå ihop",sub:"Här är vad sammanslagningen ändrar. Granska siffrorna och ladda sedan ner din sammanslagna säkerhetskopia.",added:"Kommer att läggas till",notes:"Anteckningar",highlights:"Överstrykningar",bookmarks:"Bokmärken",tags:"Taggar",updated:"Uppdaterade anteckningar (nyare version vinner)",deduped:"Dubbletter överhoppade",confirm:"Slå ihop och ladda ner",cancel:"Avbryt",study_answers:"Studiesvar",doctor:"Hälsokolla och rensa den sammanslagna filen före nedladdning (Biblioteksdoktorn)"},ceb:{title:'Andam na nga isagol',sub:'Mao kini ang pagbabago sa merge. Susihon ang mga numero, unya i-download ang imong gisagol nga backup.',added:'Iduganon',notes:'Mga nota',highlights:'Mga highlight',bookmarks:'Mga bookmark',tags:'Mga tag',updated:'Na-update nga mga nota (mananaog ang mas bago)',deduped:'Gilaktawan nga mga duplicate',confirm:'Isagol ug i-download',cancel:'Ikansela',study_answers:'Mga tubag sa pagtuon',doctor:'Susiha ug limpyohi ang gisagol nga file una i-download (Library Doctor)'},pl:{title:"Gotowe do scalenia",sub:"Oto co zmieni to scalanie. Przejrzyj liczby, a następnie pobierz scaloną kopię zapasową.",added:"Zostanie dodane",notes:"Notatki",highlights:"Wyróżnienia",bookmarks:"Zakładki",tags:"Etykiety",updated:"Zaktualizowane notatki (wygrywa nowsza wersja)",deduped:"Pominięte duplikaty",confirm:"Scal i pobierz",cancel:"Anuluj",study_answers:"Odpowiedzi do studium",doctor:"Sprawdź stan i wyczyść scalony plik przed pobraniem (Doktor biblioteki)"},uk:{title:"Готово до об'єднання",sub:"Ось що змінить це об'єднання. Перегляньте цифри, а тоді завантажте об'єднану резервну копію.",added:"Буде додано",notes:"Нотатки",highlights:"Виділення",bookmarks:"Закладки",tags:"Теги",updated:"Оновлені нотатки (перемагає новіша версія)",deduped:"Пропущені дублікати",confirm:"Об'єднати і завантажити",cancel:"Скасувати",study_answers:"Відповіді для вивчення",doctor:"Перевірити стан і очистити об'єднаний файл перед завантаженням (Лікар бібліотеки)"},he:{title:"מוכן למיזוג",sub:"הנה מה שהמיזוג הזה ישנה. עברו על המספרים, ואז הורידו את הגיבוי הממוזג.",added:"יתווספו",notes:"הערות",highlights:"הדגשות",bookmarks:"סימניות",tags:"תוויות",updated:"הערות שעודכנו (הגרסה החדשה יותר גוברת)",deduped:"כפילויות שדולגו",confirm:"מיזוג והורדה",cancel:"ביטול",study_answers:"תשובות ללימוד",doctor:"בדיקת תקינות וניקוי הקובץ הממוזג לפני ההורדה (רופא הספרייה)"},ar:{title:"جاهز للدمج",sub:"إليك ما سيغيّره هذا الدمج. راجِع الأرقام، ثم نزّل نسختك الاحتياطية المدمجة.",added:"ستتم إضافته",notes:"ملاحظات",highlights:"تظليلات",bookmarks:"علامات مرجعية",tags:"وسوم",updated:"ملاحظات محدَّثة (تُعتمد النسخة الأحدث)",deduped:"تكرارات تم تخطّيها",confirm:"ادمج ونزّل",cancel:"إلغاء",study_answers:"إجابات الدرس",doctor:"افحص الملف المدمج ونظّفه قبل التنزيل (طبيب المكتبة)"}};
  function curLang(){ try{return localStorage.getItem('jwsync_lang')||'en';}catch(_){return 'en';} }
  function t(k){ var l=curLang(); return (I18N[l]&&I18N[l][k])||I18N.en[k]||k; }
  function esc(s){ return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];}); }

  // Localised label for the one-shot checkbox under 'Create My Merged File'
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
    }
    return new Promise(function (resolve) {
      var settled = false, overlay = null;
      function done(v){ if(settled) return; settled = true; if(overlay){overlay.remove();} document.removeEventListener('keydown', onKey); resolve(v); }
      function onKey(e){ if(e.key==='Escape') done(false); }
      function row(label, n, added){
        return '<div class="jip-row'+(added?' jip-added':'')+'"><span class="jip-label">'+esc(label)+'</span><span class="jip-num">'+(added?'+':'')+(n||0)+'</span></div>';
      }
      var html =
        '<div class="jip-backdrop" data-jip-cancel></div>'+
        '<div class="jip-card" role="dialog" aria-modal="true" aria-labelledby="jip-title">'+
          '<h2 id="jip-title" class="jip-title">'+esc(t('title'))+'</h2>'+
          '<p class="jip-sub">'+esc(t('sub'))+'</p>'+
          '<div class="jip-grid">'+
            row(t('notes'), counts.Note, true)+
            row(t('highlights'), counts.UserMark, true)+
            row(t('bookmarks'), counts.Bookmark, true)+
            row(t('tags'), counts.Tag, true)+
            (counts.InputField?row(t('study_answers'), counts.InputField, true):'')+
            row(t('updated'), counts.Updated, false)+
            row(t('deduped'), counts.Deduplicated, false)+
          '</div>'+
          docGroup+
          '<div class="jip-actions">'+
            '<button type="button" class="jip-btn jip-btn-cancel" data-jip-cancel>'+esc(t('cancel'))+'</button>'+
            '<button type="button" class="jip-btn jip-btn-go" data-jip-go>'+esc(t('confirm'))+'</button>'+
          '</div>'+
        '</div>';
      overlay = document.createElement('div');
      overlay.id = 'jw-impact-overlay';
      overlay.innerHTML = html;
      document.body.appendChild(overlay);
      overlay.querySelectorAll('[data-jip-cancel]').forEach(function(el){ el.addEventListener('click', function(){ done(false); }); });
      overlay.querySelector('[data-jip-go]').addEventListener('click', function(){ done(true); });
      document.addEventListener('keydown', onKey);
    });
  };
})();

/* ──────────────────────────────────────────────────────────────────────────
   demo.js — Demo handler — the "Try Demo" merge flow on the landing page.
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0. It used to be an inline <script>, which
   meant its bytes rode in the HTML document at document priority on every page
   load, starving the render-blocking CSS on slow connections. It is now a
   deferred external file: same execution order, off the critical path, and
   cached independently of the page.
   ────────────────────────────────────────────────────────────────────────── */
(function () {
  'use strict';

  // ── Lightweight i18n local to the inline handler (banner + toasts) ──
  var I18N = {
    en: { banner_title: 'Demo mode', banner_body: 'Two sample backups are loaded. Click <strong>Preview Merge</strong> to see how they combine, then <strong>Confirm Merge</strong> to download the result.', banner_dismiss: 'Dismiss demo', err_generic: 'Could not start the demo — please check your connection and try again.', err_inject: 'Could not load the sample files into the app. Please refresh and try again.', overwrite_warn: 'Starting the demo will replace your currently loaded files. Continue?' },
    es: { banner_title: 'Modo demo', banner_body: 'Se cargaron dos copias de seguridad de ejemplo. Haz clic en <strong>Vista previa de fusión</strong> y luego en <strong>Confirmar fusión</strong> para descargar el resultado.', banner_dismiss: 'Cerrar demo', err_generic: 'No se pudo iniciar la demo. Verifica tu conexión e inténtalo de nuevo.', err_inject: 'No se pudieron cargar los archivos de ejemplo. Actualiza la página e inténtalo de nuevo.', overwrite_warn: 'Iniciar la demo reemplazará los archivos cargados. ¿Continuar?' },
    pt: { banner_title: 'Modo demo', banner_body: 'Dois backups de exemplo foram carregados. Clique em <strong>Visualizar mesclagem</strong> e depois em <strong>Confirmar mesclagem</strong> para baixar o resultado.', banner_dismiss: 'Fechar demo', err_generic: 'Não foi possível iniciar a demo. Verifique sua conexão e tente novamente.', err_inject: 'Não foi possível carregar os arquivos de exemplo. Atualize a página.', overwrite_warn: 'Iniciar a demo substituirá os arquivos carregados. Continuar?' },
    fr: { banner_title: 'Mode démo', banner_body: 'Deux sauvegardes d’exemple sont chargées. Cliquez sur <strong>Aperçu de la fusion</strong>, puis sur <strong>Confirmer la fusion</strong> pour télécharger le résultat.', banner_dismiss: 'Fermer la démo', err_generic: 'Impossible de démarrer la démo. Vérifiez votre connexion et réessayez.', err_inject: 'Impossible de charger les fichiers d’exemple. Veuillez actualiser.', overwrite_warn: 'Démarrer la démo remplacera vos fichiers chargés. Continuer ?' },
    de: { banner_title: 'Demo-Modus', banner_body: 'Zwei Beispiel-Backups sind geladen. Klicke auf <strong>Vorschau zusammenführen</strong> und dann auf <strong>Zusammenführung bestätigen</strong>, um das Ergebnis herunterzuladen.', banner_dismiss: 'Demo schließen', err_generic: 'Demo konnte nicht gestartet werden. Bitte Verbindung prüfen und erneut versuchen.', err_inject: 'Die Beispieldateien konnten nicht geladen werden. Bitte aktualisieren.', overwrite_warn: 'Beim Start der Demo werden die geladenen Dateien ersetzt. Fortfahren?' },
    it: { banner_title: 'Modalità demo', banner_body: 'Sono caricati due backup di esempio. Fai clic su <strong>Anteprima fusione</strong> e poi su <strong>Conferma fusione</strong> per scaricare il risultato.', banner_dismiss: 'Chiudi demo', err_generic: 'Impossibile avviare la demo. Controlla la connessione e riprova.', err_inject: 'Impossibile caricare i file di esempio. Aggiorna la pagina.', overwrite_warn: 'Avviare la demo sostituirà i file caricati. Continuare?' },
    ru: { banner_title: 'Демо-режим', banner_body: 'Загружены два примера резервных копий. Нажмите <strong>Предпросмотр объединения</strong>, затем <strong>Подтвердить объединение</strong>, чтобы скачать результат.', banner_dismiss: 'Закрыть демо', err_generic: 'Не удалось запустить демо. Проверьте соединение и попробуйте снова.', err_inject: 'Не удалось загрузить файлы примера. Обновите страницу.', overwrite_warn: 'Запуск демо заменит загруженные файлы. Продолжить?' },
    ja: { banner_title: 'デモモード', banner_body: '2つのサンプルバックアップを読み込みました。<strong>マージのプレビュー</strong>をクリックして結合結果を確認し、<strong>マージを確定</strong>でダウンロードできます。', banner_dismiss: 'デモを閉じる', err_generic: 'デモを開始できませんでした。接続を確認してもう一度お試しください。', err_inject: 'サンプルファイルを読み込めませんでした。ページを更新してください。', overwrite_warn: 'デモを開始すると、現在のファイルが置き換えられます。続行しますか？' },
    ko: { banner_title: '데모 모드', banner_body: '두 개의 샘플 백업이 로드되었습니다. <strong>병합 미리보기</strong>를 클릭한 다음 <strong>병합 확인</strong>을 눌러 결과를 다운로드하세요.', banner_dismiss: '데모 닫기', err_generic: '데모를 시작할 수 없습니다. 연결을 확인하고 다시 시도하세요.', err_inject: '샘플 파일을 로드할 수 없습니다. 페이지를 새로고침해 주세요.', overwrite_warn: '데모를 시작하면 로드된 파일이 교체됩니다. 계속할까요?' },
    tl: { banner_title: 'Demo mode', banner_body: 'Naka-load ang dalawang sample backup. I-click ang <strong>Preview Merge</strong> at pagkatapos <strong>Confirm Merge</strong> upang i-download ang resulta.', banner_dismiss: 'Isara ang demo', err_generic: 'Hindi nasimulan ang demo. Pakisuri ang iyong koneksyon at subukan muli.', err_inject: 'Hindi na-load ang mga sample file. Mangyaring i-refresh ang pahina.', overwrite_warn: 'Papalitan ng demo ang mga naka-load na file. Magpatuloy?' }
  ,sv:{banner_title:"Demoläge",banner_body:"Två exempelsäkerhetskopior är inlästa. Klicka på <strong>Förhandsvisa sammanslagning</strong> för att se hur de kombineras, och sedan <strong>Bekräfta sammanslagning</strong> för att ladda ner resultatet.",banner_dismiss:"Avsluta demo",err_generic:"Kunde inte starta demon — kontrollera din anslutning och försök igen.",err_inject:"Kunde inte läsa in exempelfilerna i appen. Uppdatera sidan och försök igen.",overwrite_warn:"Att starta demon ersätter de filer du har inlästa just nu. Fortsätta?"},ceb:{banner_title:'Demo mode',banner_body:'Naka-load ang duha ka sample backup. I-click ang <strong>Preview Merge</strong> unya <strong>Confirm Merge</strong> aron i-download ang resulta.',banner_dismiss:'Isira ang demo',err_generic:'Dili masimulan ang demo. Pakisusi ang imong koneksyon ug sulayi pag-usab.',err_inject:'Dili na-load ang mga sample file. Palihug i-refresh ang pahina.',overwrite_warn:'Mapulihan sa demo ang mga naka-load na nga file. Magpadayon?'},vi:{banner_title:"Chế độ dùng thử",banner_body:"Đã tải hai bản sao lưu mẫu. Nhấn <strong>Xem trước khi hợp nhất</strong> để thấy chúng kết hợp ra sao, rồi nhấn <strong>Xác nhận hợp nhất</strong> để tải kết quả về.",banner_dismiss:"Đóng bản dùng thử",err_generic:"Không thể bắt đầu bản dùng thử — vui lòng kiểm tra kết nối và thử lại.",err_inject:"Không thể tải các tập tin mẫu vào ứng dụng. Vui lòng tải lại trang và thử lại.",overwrite_warn:"Bắt đầu bản dùng thử sẽ thay thế các tập tin bạn đang tải. Tiếp tục chứ?"},"yue-Hant":{banner_title:"示範模式",banner_body:"已經載入咗兩個範例備份。撳<strong>預覽合併</strong>睇吓佢哋點樣合埋，然後撳<strong>確認合併</strong>就可以下載結果。",banner_dismiss:"關閉示範",err_generic:"起動唔到示範——請檢查吓網絡連線再試過。",err_inject:"載入唔到範例檔案。請重新整理版面再試過。",overwrite_warn:"起動示範會取代而家載入咗嘅檔案。要繼續嗎？"},"zh-Hant":{banner_title:"演示模式",banner_body:"已載入兩個示例備份。點擊<strong>預覽合併</strong>檢視它們如何合併，然後點擊<strong>確認合併</strong>下載結果。",banner_dismiss:"關閉演示",err_generic:"無法啟動演示——請檢查網路連線後重試。",err_inject:"無法將示例檔案載入到應用中。請重新整理頁面後重試。",overwrite_warn:"啟動演示會替換當前已載入的檔案。要繼續嗎？"},"zh-Hans":{banner_title:"演示模式",banner_body:"已加载两个示例备份。点击<strong>预览合并</strong>查看它们如何合并，然后点击<strong>确认合并</strong>下载结果。",banner_dismiss:"关闭演示",err_generic:"无法启动演示——请检查网络连接后重试。",err_inject:"无法将示例文件加载到应用中。请刷新页面后重试。",overwrite_warn:"启动演示会替换当前已加载的文件。要继续吗？"},pl:{banner_title:"Tryb demonstracyjny",banner_body:"Wczytano dwie przykładowe kopie zapasowe. Kliknij <strong>Podgląd scalania</strong>, aby zobaczyć, jak zostaną połączone, a następnie <strong>Potwierdź scalanie</strong>, aby pobrać wynik.",banner_dismiss:"Zamknij demonstrację",err_generic:"Nie udało się uruchomić demonstracji — sprawdź połączenie i spróbuj ponownie.",err_inject:"Nie udało się wczytać przykładowych plików do aplikacji. Odśwież stronę i spróbuj ponownie.",overwrite_warn:"Uruchomienie demonstracji zastąpi obecnie wczytane pliki. Kontynuować?"},uk:{banner_title:"Демонстраційний режим",banner_body:"Завантажено дві зразкові резервні копії. Натисніть <strong>Попередній перегляд об'єднання</strong>, щоб побачити, як вони поєднаються, а тоді <strong>Підтвердити об'єднання</strong>, щоб завантажити результат.",banner_dismiss:"Закрити демонстрацію",err_generic:"Не вдалося запустити демонстрацію — перевірте з'єднання і спробуйте ще раз.",err_inject:"Не вдалося завантажити зразкові файли в програму. Оновіть сторінку і спробуйте ще раз.",overwrite_warn:"Запуск демонстрації замінить файли, які зараз завантажені. Продовжити?"},he:{banner_title:"מצב הדגמה",banner_body:"נטענו שני גיבויים לדוגמה. לחצו על <strong>תצוגה מקדימה של המיזוג</strong> כדי לראות איך הם משתלבים, ואז על <strong>אישור המיזוג</strong> כדי להוריד את התוצאה.",banner_dismiss:"סגירת ההדגמה",err_generic:"לא הצלחנו להפעיל את ההדגמה — בדקו את החיבור ונסו שוב.",err_inject:"לא הצלחנו לטעון את קובצי הדוגמה ליישום. רעננו את הדף ונסו שוב.",overwrite_warn:"הפעלת ההדגמה תחליף את הקבצים שטעונים כעת. להמשיך?"},ar:{banner_title:"الوضع التجريبي",banner_body:"تم تحميل نسختين احتياطيتين تجريبيتين. اضغط <strong>معاينة الدمج</strong> لترى كيف تندمجان، ثم <strong>تأكيد الدمج</strong> لتنزيل النتيجة.",banner_dismiss:"إنهاء العرض التجريبي",err_generic:"تعذّر بدء العرض التجريبي — تحقّق من اتصالك وحاول مرة أخرى.",err_inject:"تعذّر تحميل الملفات التجريبية في التطبيق. أعد تحديث الصفحة وحاول مرة أخرى.",overwrite_warn:"بدء العرض التجريبي سيستبدل الملفات المحمّلة حاليًا. هل تريد المتابعة؟"}};
  function lang() {
    try { return localStorage.getItem('jwsync_lang') || 'en'; } catch (_) { return 'en'; }
  }
  function t(key) {
    var l = lang();
    return (I18N[l] && I18N[l][key]) || I18N.en[key] || key;
  }

  // ── Internal state ────────────────────────────────────────────────
  var demoStarting = false;

  // ── DOM helpers ───────────────────────────────────────────────────
  function demoTriggers() {
    return document.querySelectorAll('[data-demo-trigger], #landing-demo-btn, .nav-btn-demo, .simple-mode-teaser-btn-demo');
  }
  function setBusy(busy) {
    var nodes = demoTriggers();
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (busy) {
        n.setAttribute('aria-busy', 'true');
        n.classList.add('jw-demo-loading');
        if (n.tagName === 'BUTTON') n.disabled = true;
      } else {
        n.removeAttribute('aria-busy');
        n.classList.remove('jw-demo-loading');
        if (n.tagName === 'BUTTON') n.disabled = false;
      }
    }
  }
  function fireAnalytics() {
    try { if (typeof gtag === 'function') gtag('event', 'try_demo_click', { event_category: 'engagement' }); } catch (_) {}
  }
  function showToast(msg, isError) {
    var el = document.createElement('div');
    el.textContent = msg;
    el.className = 'jw-demo-toast' + (isError ? ' jw-demo-toast-error' : '');
    document.body.appendChild(el);
    setTimeout(function () { el.classList.add('jw-demo-toast-out'); }, 3200);
    setTimeout(function () { try { el.remove(); } catch (_) {} }, 3800);
  }

  // ── Demo banner ───────────────────────────────────────────────────
  function showDemoBanner() {
    var existing = document.getElementById('jw-demo-banner');
    if (existing) existing.remove();
    var b = document.createElement('div');
    b.id = 'jw-demo-banner';
    b.setAttribute('role', 'status');
    b.innerHTML =
      '<span class="jw-demo-banner-icon" aria-hidden="true">▶</span>' +
      '<div class="jw-demo-banner-content">' +
        '<strong>' + t('banner_title') + '</strong> &middot; ' + t('banner_body') +
      '</div>' +
      '<button type="button" class="jw-demo-banner-close" aria-label="' + t('banner_dismiss') + '">×</button>';
    document.body.appendChild(b);
    b.querySelector('.jw-demo-banner-close').addEventListener('click', function () { b.remove(); });
  }

  // ── Look up the React-rendered "Preview Merge" button and highlight it ─
  function scrollToPreviewMerge() {
    var btns = document.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) {
      var text = (btns[i].textContent || '').trim();
      if (text.indexOf('Preview Merge') !== -1) {
        try { btns[i].scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (_) {}
        btns[i].classList.add('jw-demo-pulse');
        setTimeout((function (b) { return function () { b.classList.remove('jw-demo-pulse'); }; })(btns[i]), 3600);
        return;
      }
    }
  }

  // ── Are non-demo files already loaded? Avoid clobbering real work. ─
  function userHasRealFilesLoaded() {
    var inputs = document.querySelectorAll('input[type="file"][accept=".jwlibrary"]');
    for (var i = 0; i < inputs.length; i++) {
      var files = inputs[i].files;
      if (!files || files.length === 0) continue;
      for (var j = 0; j < files.length; j++) {
        if (files[j] && files[j].name.indexOf('JWSync_Demo_') !== 0) return true;
      }
    }
    return false;
  }

  // ── Wait helper (poll until predicate true or timeout) ────────────
  function waitFor(predicate, timeoutMs) {
    return new Promise(function (resolve) {
      var start = Date.now();
      (function loop() {
        var v;
        try { v = predicate(); } catch (_) { v = false; }
        if (v) return resolve(v);
        if (Date.now() - start > timeoutMs) return resolve(false);
        setTimeout(loop, 80);
      })();
    });
  }

  // ── The main flow ─────────────────────────────────────────────────
  function openDemo(e) {
    if (e && e.preventDefault) e.preventDefault();
    if (demoStarting) return Promise.resolve();
    demoStarting = true;
    fireAnalytics();

    // Confirm if user already has real files staged (don't silently clobber).
    if (userHasRealFilesLoaded()) {
      try {
        if (!window.confirm(t('overwrite_warn'))) {
          demoStarting = false;
          return Promise.resolve();
        }
      } catch (_) { /* if confirm is blocked, proceed */ }
    }

    setBusy(true);

    return Promise.resolve()
      .then(function () {
        // Navigate to #app so enhancements.js hides landing + shows #root.
        // hashchange also drives the boot loader to load the bundle.
        if (location.hash !== '#app') {
          if (location.hash) location.hash = '#app';
          else { try { location.hash = '#app'; } catch (_) {} }
        }
        if (typeof window.__jwBootApp === 'function') return window.__jwBootApp();
      })
      .then(function () {
        // Wait for the enhancements.js helpers to be exposed.
        return waitFor(function () {
          return typeof window.__jwBuildDemoBackups === 'function'
              && typeof window.__jwInjectMergeDemo === 'function';
        }, 10000);
      })
      .then(function (helpersReady) {
        if (!helpersReady) throw new Error('demo-helpers-unavailable');
        return window.__jwBuildDemoBackups();
      })
      .then(function (files) {
        if (!files || files.length < 2) throw new Error('demo-files-missing');
        return window.__jwInjectMergeDemo(files[0], files[1]);
      })
      .then(function (injected) {
        if (!injected) throw new Error('demo-inject-failed');
        showDemoBanner();
        setTimeout(scrollToPreviewMerge, 420);
      })
      .catch(function (err) {
        console.error('[jwsync] demo failed:', err);
        if (err && String(err.message || err) === 'demo-inject-failed') {
          showToast(t('err_inject'), true);
        } else {
          showToast(t('err_generic'), true);
        }
      })
      .then(function () { setBusy(false); demoStarting = false; },
            function () { setBusy(false); demoStarting = false; });
  }
  window.__jwOpenDemo = openDemo;

  // ── Bind to all demo-trigger elements (now + future React renders) ─
  function bindAll(root) {
    var nodes = (root || document).querySelectorAll('[data-demo-trigger]');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (!el.__demoBound) {
        el.__demoBound = true;
        el.addEventListener('click', openDemo);
      }
    }
    var howto = (root || document).querySelectorAll('[data-howto-trigger]');
    for (var h = 0; h < howto.length; h++) {
      var he = howto[h];
      if (!he.__howtoBound) {
        he.__howtoBound = true;
        he.addEventListener('click', function (ev) {
          if (ev && ev.preventDefault) ev.preventDefault();
          if (window.__jwOpenGuide) window.__jwOpenGuide('export');
        });
      }
    }
  }
  function bindLegacyId() {
    var btn = document.getElementById('landing-demo-btn');
    if (btn && !btn.__demoBound) {
      btn.__demoBound = true;
      btn.addEventListener('click', openDemo);
    }
  }
  function init() {
    bindAll(document);
    bindLegacyId();
    if (typeof MutationObserver === 'function') {
      var obs = new MutationObserver(function (mutations) {
        for (var i = 0; i < mutations.length; i++) {
          var added = mutations[i].addedNodes;
          for (var j = 0; j < added.length; j++) {
            var node = added[j];
            if (node.nodeType === 1) {
              if (node.hasAttribute && node.hasAttribute('data-demo-trigger') && !node.__demoBound) {
                node.__demoBound = true;
                node.addEventListener('click', openDemo);
              }
              if (node.querySelectorAll) bindAll(node);
            }
          }
        }
      });
      obs.observe(document.body, { childList: true, subtree: true });
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

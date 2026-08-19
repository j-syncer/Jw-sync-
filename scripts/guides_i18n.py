# -*- coding: utf-8 -*-
"""
guides_i18n.py — translated copy for the static guide pages.

CHROME     shared page furniture (nav, headings, CTA, footer) per language.
GUIDE_TEXT per-language overrides for each guide, keyed by slug. Any field
           omitted falls back to the English record in build_guides.GUIDES,
           so a language can be filled in gradually.

Adding a language:
  1. add a CHROME entry (every key below is required),
  2. add a GUIDE_TEXT entry with one dict per slug,
  3. run `python3 scripts/build_guides.py` and `python3 scripts/build_seo.py`.
The language then appears in the guides' hreflang cluster and the sitemap
automatically — build_guides derives TRANSLATED from GUIDE_TEXT's keys, so a
half-finished language is never advertised to search engines.
"""

CHROME = {
    "en": {
        "lang_name": "English",
        "lang_label": "Language",
        "lang_other": "This guide in other languages",
        "og_locale": "en_US",
        "site_guides": "JW Sync Guides",
        "nav_guides": "Guides",
        "nav_community": "Community",
        "nav_open_app": "Open the app",
        "crumb_guides": "Guides",
        "h_steps": "Step by step",
        "h_faq": "Frequently asked questions",
        "h_related": "Related guides",
        "cta_title": "Do it now — free, in your browser",
        "cta_body": "JW Sync merges, edits and analyses .jwlibrary backups entirely on your "
                    "device. No account, no uploads, nothing installed.",
        "cta_btn": "Open JW Sync →",
        "index_title": "JW Library Backup, Sync & Notes Guides | JW Sync",
        "index_desc": "Practical guides for JW Library backups: merge backups from two devices, "
                      "transfer notes to a new phone, move Android to iPhone, fix a backup that "
                      "won't restore, edit and search your notes, and more.",
        "index_h1": "Guides & how-tos",
        "index_lede": "Everything about JW Library backups, in plain steps: merging devices, "
                      "moving to a new phone, rescuing notes, and getting more out of the "
                      "library you already have. Every tool mentioned runs free in your "
                      "browser — your files are never uploaded.",
        "index_cta_title": "Skip the reading — just open the tool",
        "index_cta_body": "Merging two backups takes about a minute and the app walks you "
                          "through it.",
        "footer_all_guides": "All guides",
        "footer_community": "Community",
        "footer_stats": "Study Stats",
        "footer_privacy": "JW Sync processes all data locally — your files never leave your "
                          "device. Free to use; no account, no uploads.",
        "footer_disclaimer": "“JW Library” is the property of the Watch Tower Bible and Tract "
                             "Society of Pennsylvania. JW Sync is an independent utility and is "
                             "not affiliated with or endorsed by it.",
        "groups": {
            "Getting started": "Getting started",
            "Sharing scenarios": "Sharing scenarios",
            "Everyday scenarios": "Everyday scenarios",
            "Fixing problems": "Fixing problems",
            "Power tools": "Power tools",
        },
    },
    "es": {
        "lang_name": "Español",
        "lang_label": "Idioma",
        "lang_other": "Esta guía en otros idiomas",
        "og_locale": "es_ES",
        "site_guides": "Guías de JW Sync",
        "nav_guides": "Guías",
        "nav_community": "Comunidad",
        "nav_open_app": "Abrir la app",
        "crumb_guides": "Guías",
        "h_steps": "Paso a paso",
        "h_faq": "Preguntas frecuentes",
        "h_related": "Guías relacionadas",
        "cta_title": "Hazlo ahora: gratis, en tu navegador",
        "cta_body": "JW Sync combina, edita y analiza copias de seguridad .jwlibrary "
                    "enteramente en tu dispositivo. Sin cuenta, sin subir nada, sin "
                    "instalar nada.",
        "cta_btn": "Abrir JW Sync →",
        "index_title": "Guías de copias de seguridad, sincronización y notas de JW Library | JW Sync",
        "index_desc": "Guías prácticas para las copias de seguridad de JW Library: combinar "
                      "copias de dos dispositivos, pasar tus notas a un teléfono nuevo, migrar "
                      "de Android a iPhone, arreglar una copia que no se restaura, editar y "
                      "buscar en tus notas, y mucho más.",
        "index_h1": "Guías y tutoriales",
        "index_lede": "Todo sobre las copias de seguridad de JW Library, en pasos claros: "
                      "combinar dispositivos, cambiar de teléfono, rescatar notas y sacarle "
                      "más partido a la biblioteca que ya tienes. Todas las herramientas "
                      "mencionadas funcionan gratis en tu navegador: tus archivos nunca se "
                      "suben a ningún sitio.",
        "index_cta_title": "Sáltate la lectura: abre la herramienta",
        "index_cta_body": "Combinar dos copias de seguridad lleva alrededor de un minuto y la "
                          "app te guía en todo momento.",
        "footer_all_guides": "Todas las guías",
        "footer_community": "Comunidad",
        "footer_stats": "Estadísticas de estudio",
        "footer_privacy": "JW Sync procesa todos los datos localmente: tus archivos nunca salen "
                          "de tu dispositivo. Es gratis; sin cuenta y sin subir nada.",
        "footer_disclaimer": "«JW Library» es propiedad de la Watch Tower Bible and Tract "
                             "Society of Pennsylvania. JW Sync es una utilidad independiente y "
                             "no está afiliada a ella ni cuenta con su respaldo.",
        "groups": {
            "Getting started": "Para empezar",
            "Sharing scenarios": "Casos para compartir",
            "Everyday scenarios": "Situaciones del día a día",
            "Fixing problems": "Solución de problemas",
            "Power tools": "Herramientas avanzadas",
        },
    },
    "pt": {
        "lang_name": "Português",
        "lang_label": "Idioma",
        "lang_other": "Este guia em outros idiomas",
        "og_locale": "pt_BR",
        "site_guides": "Guias do JW Sync",
        "nav_guides": "Guias",
        "nav_community": "Comunidade",
        "nav_open_app": "Abrir o app",
        "crumb_guides": "Guias",
        "h_steps": "Passo a passo",
        "h_faq": "Perguntas frequentes",
        "h_related": "Guias relacionados",
        "cta_title": "Faça agora — de graça, no seu navegador",
        "cta_body": "O JW Sync mescla, edita e analisa backups .jwlibrary inteiramente no seu "
                    "aparelho. Sem conta, sem envio de arquivos, sem instalar nada.",
        "cta_btn": "Abrir o JW Sync →",
        "index_title": "Guias de backup, sincronização e notas do JW Library | JW Sync",
        "index_desc": "Guias práticos para os backups do JW Library: mesclar backups de dois "
                      "aparelhos, transferir notas para um celular novo, migrar do Android "
                      "para o iPhone, consertar um backup que não restaura, editar e "
                      "pesquisar suas notas, e muito mais.",
        "index_h1": "Guias e tutoriais",
        "index_lede": "Tudo sobre os backups do JW Library, em passos simples: mesclar "
                      "aparelhos, mudar de celular, resgatar notas e tirar mais proveito da "
                      "biblioteca que você já tem. Todas as ferramentas citadas rodam de "
                      "graça no seu navegador — seus arquivos nunca são enviados.",
        "index_cta_title": "Pule a leitura — abra logo a ferramenta",
        "index_cta_body": "Mesclar dois backups leva cerca de um minuto, e o app guia você "
                          "pelo caminho.",
        "footer_all_guides": "Todos os guias",
        "footer_community": "Comunidade",
        "footer_stats": "Estatísticas de Estudo",
        "footer_privacy": "O JW Sync processa todos os dados localmente — seus arquivos nunca "
                          "saem do seu aparelho. É gratuito; sem conta e sem envio de "
                          "arquivos.",
        "footer_disclaimer": "“JW Library” é propriedade da Watch Tower Bible and Tract "
                             "Society of Pennsylvania. O JW Sync é um utilitário "
                             "independente, não é afiliado a ela nem por ela endossado.",
        "groups": {
            "Getting started": "Para começar",
            "Sharing scenarios": "Casos de compartilhamento",
            "Everyday scenarios": "Situações do dia a dia",
            "Fixing problems": "Resolvendo problemas",
            "Power tools": "Ferramentas avançadas",
        },
    },
    "fr": {
        "lang_name": "Français",
        "lang_label": "Langue",
        "lang_other": "Ce guide dans d’autres langues",
        "og_locale": "fr_FR",
        "site_guides": "Guides JW Sync",
        "nav_guides": "Guides",
        "nav_community": "Communauté",
        "nav_open_app": "Ouvrir l'appli",
        "crumb_guides": "Guides",
        "h_steps": "Pas à pas",
        "h_faq": "Questions fréquentes",
        "h_related": "Guides associés",
        "cta_title": "Faites-le maintenant — gratuitement, dans votre navigateur",
        "cta_body": "JW Sync fusionne, modifie et analyse les sauvegardes .jwlibrary "
                    "entièrement sur votre appareil. Sans compte, sans envoi de fichiers, "
                    "sans rien installer.",
        "cta_btn": "Ouvrir JW Sync →",
        "index_title": "Guides sauvegarde, synchronisation et notes JW Library | JW Sync",
        "index_desc": "Des guides pratiques pour les sauvegardes JW Library : fusionner les "
                      "sauvegardes de deux appareils, transférer ses notes vers un nouveau "
                      "téléphone, passer d'Android à iPhone, réparer une sauvegarde qui ne se "
                      "restaure pas, modifier et chercher dans ses notes, et bien plus.",
        "index_h1": "Guides et tutoriels",
        "index_lede": "Tout sur les sauvegardes JW Library, en étapes claires : fusionner des "
                      "appareils, changer de téléphone, sauver ses notes et tirer davantage "
                      "de la bibliothèque que vous avez déjà. Tous les outils cités "
                      "fonctionnent gratuitement dans votre navigateur — vos fichiers ne sont "
                      "jamais envoyés.",
        "index_cta_title": "Passez la lecture — ouvrez directement l'outil",
        "index_cta_body": "Fusionner deux sauvegardes prend environ une minute, et "
                          "l'application vous guide.",
        "footer_all_guides": "Tous les guides",
        "footer_community": "Communauté",
        "footer_stats": "Statistiques d'étude",
        "footer_privacy": "JW Sync traite toutes les données localement — vos fichiers ne "
                          "quittent jamais votre appareil. Gratuit ; sans compte et sans "
                          "envoi de fichiers.",
        "footer_disclaimer": "« JW Library » est la propriété de la Watch Tower Bible and "
                             "Tract Society of Pennsylvania. JW Sync est un utilitaire "
                             "indépendant, sans lien avec elle ni approbation de sa part.",
        "groups": {
            "Getting started": "Pour commencer",
            "Sharing scenarios": "Cas de partage",
            "Everyday scenarios": "Situations du quotidien",
            "Fixing problems": "Résoudre les problèmes",
            "Power tools": "Outils avancés",
        },
    },
    "de": {
        "lang_name": "Deutsch",
        "lang_label": "Sprache",
        "lang_other": "Diese Anleitung in anderen Sprachen",
        "og_locale": "de_DE",
        "site_guides": "JW-Sync-Anleitungen",
        "nav_guides": "Anleitungen",
        "nav_community": "Community",
        "nav_open_app": "App öffnen",
        "crumb_guides": "Anleitungen",
        "h_steps": "Schritt für Schritt",
        "h_faq": "Häufige Fragen",
        "h_related": "Verwandte Anleitungen",
        "cta_title": "Mach es jetzt — kostenlos, in deinem Browser",
        "cta_body": "JW Sync führt .jwlibrary-Sicherungen zusammen, bearbeitet und "
                    "analysiert sie vollständig auf deinem Gerät. Ohne Konto, ohne Uploads, "
                    "ohne Installation.",
        "cta_btn": "JW Sync öffnen →",
        "index_title": "Anleitungen zu JW-Library-Sicherungen, Sync und Notizen | JW Sync",
        "index_desc": "Praktische Anleitungen rund um JW-Library-Sicherungen: Sicherungen von "
                      "zwei Geräten zusammenführen, Notizen aufs neue Handy bringen, von "
                      "Android aufs iPhone wechseln, eine Sicherung reparieren, die sich "
                      "nicht wiederherstellen lässt, Notizen bearbeiten und durchsuchen, und "
                      "mehr.",
        "index_h1": "Anleitungen und Tipps",
        "index_lede": "Alles rund um JW-Library-Sicherungen, in klaren Schritten: Geräte "
                      "zusammenführen, aufs neue Handy wechseln, Notizen retten und mehr aus "
                      "der Bibliothek holen, die du längst hast. Jedes genannte Werkzeug "
                      "läuft kostenlos in deinem Browser — deine Dateien werden nie "
                      "hochgeladen.",
        "index_cta_title": "Lesen überspringen — einfach das Werkzeug öffnen",
        "index_cta_body": "Zwei Sicherungen zusammenzuführen dauert etwa eine Minute, und die "
                          "App führt dich hindurch.",
        "footer_all_guides": "Alle Anleitungen",
        "footer_community": "Community",
        "footer_stats": "Studienstatistik",
        "footer_privacy": "JW Sync verarbeitet alle Daten lokal — deine Dateien verlassen nie "
                          "dein Gerät. Kostenlos; ohne Konto, ohne Uploads.",
        "footer_disclaimer": "„JW Library“ ist Eigentum der Watch Tower Bible and Tract "
                             "Society of Pennsylvania. JW Sync ist ein unabhängiges "
                             "Hilfsprogramm und steht in keiner Verbindung zu ihr und wird "
                             "von ihr nicht unterstützt.",
        "groups": {
            "Getting started": "Erste Schritte",
            "Sharing scenarios": "Notizen weitergeben",
            "Everyday scenarios": "Alltagssituationen",
            "Fixing problems": "Probleme lösen",
            "Power tools": "Fortgeschrittene Werkzeuge",
        },
    },
    "it": {
        "lang_name": "Italiano",
        "lang_label": "Lingua",
        "lang_other": "Questa guida in altre lingue",
        "og_locale": "it_IT",
        "site_guides": "Guide di JW Sync",
        "nav_guides": "Guide",
        "nav_community": "Comunità",
        "nav_open_app": "Apri l'app",
        "crumb_guides": "Guide",
        "h_steps": "Passo passo",
        "h_faq": "Domande frequenti",
        "h_related": "Guide correlate",
        "cta_title": "Fallo ora — gratis, nel tuo browser",
        "cta_body": "JW Sync unisce, modifica e analizza i backup .jwlibrary interamente sul "
                    "tuo dispositivo. Senza account, senza caricamenti, senza installare "
                    "nulla.",
        "cta_btn": "Apri JW Sync →",
        "index_title": "Guide su backup, sincronizzazione e note di JW Library | JW Sync",
        "index_desc": "Guide pratiche per i backup di JW Library: unire i backup di due "
                      "dispositivi, trasferire le note su un telefono nuovo, passare da "
                      "Android a iPhone, riparare un backup che non si ripristina, modificare "
                      "e cercare nelle note, e molto altro.",
        "index_h1": "Guide e istruzioni",
        "index_lede": "Tutto sui backup di JW Library, in passi chiari: unire dispositivi, "
                      "cambiare telefono, salvare le note e sfruttare meglio la biblioteca "
                      "che hai già. Ogni strumento citato funziona gratis nel tuo browser — i "
                      "tuoi file non vengono mai caricati.",
        "index_cta_title": "Salta la lettura — apri direttamente lo strumento",
        "index_cta_body": "Unire due backup richiede circa un minuto, e l'app ti guida passo "
                          "dopo passo.",
        "footer_all_guides": "Tutte le guide",
        "footer_community": "Comunità",
        "footer_stats": "Statistiche di studio",
        "footer_privacy": "JW Sync elabora tutti i dati in locale — i tuoi file non lasciano "
                          "mai il dispositivo. Gratuito; senza account e senza caricamenti.",
        "footer_disclaimer": "«JW Library» è proprietà della Watch Tower Bible and Tract "
                             "Society of Pennsylvania. JW Sync è un'utilità indipendente, non "
                             "affiliata a essa né da essa approvata.",
        "groups": {
            "Getting started": "Per iniziare",
            "Sharing scenarios": "Condividere le note",
            "Everyday scenarios": "Situazioni di tutti i giorni",
            "Fixing problems": "Risolvere i problemi",
            "Power tools": "Strumenti avanzati",
        },
    },
    "ru": {
        "lang_name": "Русский",
        "lang_label": "Язык",
        "lang_other": "Это руководство на других языках",
        "og_locale": "ru_RU",
        "site_guides": "Руководства JW Sync",
        "nav_guides": "Руководства",
        "nav_community": "Сообщество",
        "nav_open_app": "Открыть приложение",
        "crumb_guides": "Руководства",
        "h_steps": "Шаг за шагом",
        "h_faq": "Частые вопросы",
        "h_related": "Похожие руководства",
        "cta_title": "Сделайте это сейчас — бесплатно, прямо в браузере",
        "cta_body": "JW Sync объединяет, редактирует и анализирует резервные копии .jwlibrary "
                    "целиком на вашем устройстве. Без учётной записи, без загрузки файлов, "
                    "без установки.",
        "cta_btn": "Открыть JW Sync →",
        "index_title": "Руководства по резервным копиям, синхронизации и заметкам JW Library | JW Sync",
        "index_desc": "Практические руководства по резервным копиям JW Library: объединить "
                      "копии с двух устройств, перенести заметки на новый телефон, перейти с "
                      "Android на iPhone, починить копию, которая не восстанавливается, "
                      "редактировать заметки и искать по ним, и многое другое.",
        "index_h1": "Руководства и инструкции",
        "index_lede": "Всё о резервных копиях JW Library, понятными шагами: объединить "
                      "устройства, перейти на новый телефон, спасти заметки и извлечь больше "
                      "из той библиотеки, которая у вас уже есть. Каждый упомянутый "
                      "инструмент работает бесплатно в вашем браузере — ваши файлы никогда не "
                      "отправляются.",
        "index_cta_title": "Пропустите чтение — просто откройте инструмент",
        "index_cta_body": "Объединение двух копий занимает около минуты, и приложение "
                          "проведёт вас по шагам.",
        "footer_all_guides": "Все руководства",
        "footer_community": "Сообщество",
        "footer_stats": "Статистика изучения",
        "footer_privacy": "JW Sync обрабатывает все данные локально — ваши файлы никогда не "
                          "покидают устройство. Бесплатно; без учётной записи и без загрузки "
                          "файлов.",
        "footer_disclaimer": "«JW Library» принадлежит Watch Tower Bible and Tract Society of "
                             "Pennsylvania. JW Sync — независимая утилита, не связанная с ней "
                             "и не одобренная ею.",
        "groups": {
            "Getting started": "Начало работы",
            "Sharing scenarios": "Как делиться заметками",
            "Everyday scenarios": "Повседневные ситуации",
            "Fixing problems": "Решение проблем",
            "Power tools": "Продвинутые инструменты",
        },
    },
    "ja": {
        "lang_name": "日本語",
        "lang_label": "言語",
        "lang_other": "このガイドを他の言語で読む",
        "og_locale": "ja_JP",
        "site_guides": "JW Sync ガイド",
        "nav_guides": "ガイド",
        "nav_community": "コミュニティー",
        "nav_open_app": "アプリを開く",
        "crumb_guides": "ガイド",
        "h_steps": "手順",
        "h_faq": "よくある質問",
        "h_related": "関連ガイド",
        "cta_title": "今すぐどうぞ — 無料、ブラウザーの中で",
        "cta_body": "JW Sync は .jwlibrary バックアップの統合・編集・分析を、すべてあなたの"
                    "端末で行います。アカウント不要、アップロードなし、インストール不要です。",
        "cta_btn": "JW Sync を開く →",
        "index_title": "JW Library のバックアップ・同期・ノートのガイド | JW Sync",
        "index_desc": "JW Library のバックアップに関する実用的なガイド：2台の端末の"
                      "バックアップを統合する、ノートを新しいスマホへ移す、Android から "
                      "iPhone へ移行する、復元できないバックアップを直す、ノートを編集・"
                      "検索する、ほか多数。",
        "index_h1": "ガイドと手順",
        "index_lede": "JW Library のバックアップのすべてを、分かりやすい手順で。端末の統合、"
                      "新しいスマホへの移行、ノートの救出、そして今あるライブラリーを"
                      "もっと活かす方法。紹介するツールはすべて、ブラウザーの中で無料で"
                      "動きます——ファイルがアップロードされることはありません。",
        "index_cta_title": "読むのは後回しで、まずツールを開く",
        "index_cta_body": "2つのバックアップの統合は1分ほどで、アプリが手順を案内します。",
        "footer_all_guides": "すべてのガイド",
        "footer_community": "コミュニティー",
        "footer_stats": "研究統計",
        "footer_privacy": "JW Sync はすべてのデータをローカルで処理します——ファイルが端末を"
                          "出ることはありません。無料で、アカウントもアップロードも"
                          "ありません。",
        "footer_disclaimer": "「JW Library」は Watch Tower Bible and Tract Society of "
                             "Pennsylvania の所有物です。JW Sync は独立したユーティリティで"
                             "あり、同協会とは関係がなく、承認も受けていません。",
        "groups": {
            "Getting started": "はじめに",
            "Sharing scenarios": "ノートを共有する",
            "Everyday scenarios": "日々の場面で",
            "Fixing problems": "問題を解決する",
            "Power tools": "上級ツール",
        },
    },
    "ko": {
        "lang_name": "한국어",
        "lang_label": "언어",
        "lang_other": "다른 언어로 된 이 가이드",
        "og_locale": "ko_KR",
        "site_guides": "JW Sync 안내",
        "nav_guides": "안내",
        "nav_community": "커뮤니티",
        "nav_open_app": "앱 열기",
        "crumb_guides": "안내",
        "h_steps": "단계별 안내",
        "h_faq": "자주 묻는 질문",
        "h_related": "관련 안내",
        "cta_title": "지금 해 보세요 — 무료로, 브라우저에서",
        "cta_body": "JW Sync는 .jwlibrary 백업의 병합과 편집, 분석을 모두 당신의 기기에서 "
                    "처리합니다. 계정도, 업로드도, 설치도 필요 없습니다.",
        "cta_btn": "JW Sync 열기 →",
        "index_title": "JW Library 백업·동기화·노트 안내 | JW Sync",
        "index_desc": "JW Library 백업을 위한 실용적인 안내입니다. 두 기기의 백업 병합하기, "
                      "노트를 새 휴대전화로 옮기기, 안드로이드에서 아이폰으로 이동하기, "
                      "복원되지 않는 백업 고치기, 노트 편집하고 검색하기 등을 다룹니다.",
        "index_h1": "안내와 사용법",
        "index_lede": "JW Library 백업에 관한 모든 것을 쉬운 단계로 담았습니다. 기기 병합하기, "
                      "새 휴대전화로 옮기기, 노트 되찾기, 그리고 이미 가진 라이브러리를 더 잘 "
                      "활용하기. 소개하는 모든 도구는 브라우저에서 무료로 작동하며, 파일이 "
                      "업로드되는 일은 없습니다.",
        "index_cta_title": "읽는 건 나중에 — 바로 도구를 열어 보세요",
        "index_cta_body": "백업 두 개를 병합하는 데 1분 남짓이면 되고, 앱이 단계별로 "
                          "안내합니다.",
        "footer_all_guides": "전체 안내",
        "footer_community": "커뮤니티",
        "footer_stats": "연구 통계",
        "footer_privacy": "JW Sync는 모든 데이터를 기기 안에서 처리합니다 — 파일이 기기를 "
                          "떠나지 않습니다. 무료이며 계정도 업로드도 없습니다.",
        "footer_disclaimer": "‘JW Library’는 Watch Tower Bible and Tract Society of "
                             "Pennsylvania의 소유입니다. JW Sync는 독립적인 도구로, 해당 "
                             "협회와 제휴하거나 승인을 받지 않았습니다.",
        "groups": {
            "Getting started": "시작하기",
            "Sharing scenarios": "노트 나누기",
            "Everyday scenarios": "일상 속 상황",
            "Fixing problems": "문제 해결",
            "Power tools": "고급 도구",
        },
    },
    "tl": {
        "lang_name": "Filipino",
        "lang_label": "Wika",
        "lang_other": "Ang gabay na ito sa ibang wika",
        "og_locale": "tl_PH",
        "site_guides": "Mga Gabay sa JW Sync",
        "nav_guides": "Mga Gabay",
        "nav_community": "Komunidad",
        "nav_open_app": "Buksan ang app",
        "crumb_guides": "Mga Gabay",
        "h_steps": "Hakbang-hakbang",
        "h_faq": "Mga madalas itanong",
        "h_related": "Mga kaugnay na gabay",
        "cta_title": "Gawin mo na ngayon — libre, sa browser mo",
        "cta_body": "Pinagsasama, ine-edit at sinusuri ng JW Sync ang mga .jwlibrary na "
                    "backup nang buong-buo sa device mo. Walang account, walang ina-upload, "
                    "walang ini-install.",
        "cta_btn": "Buksan ang JW Sync →",
        "index_title": "Mga gabay sa backup, sync at nota ng JW Library | JW Sync",
        "index_desc": "Mga praktikal na gabay para sa mga backup ng JW Library: pagsamahin "
                      "ang mga backup mula sa dalawang device, ilipat ang mga nota sa bagong "
                      "cellphone, lumipat mula Android patungong iPhone, ayusin ang backup na "
                      "ayaw maisauli, i-edit at hanapin ang mga nota mo, at marami pa.",
        "index_h1": "Mga gabay at paano-gawin",
        "index_lede": "Lahat tungkol sa mga backup ng JW Library, sa malilinaw na hakbang: "
                      "pagsasama ng mga device, paglipat sa bagong cellphone, pagsagip ng mga "
                      "nota, at higit pang pakinabang sa library na mayroon ka na. Libreng "
                      "tumatakbo sa browser mo ang bawat kagamitang nabanggit — hindi "
                      "kailanman ina-upload ang mga file mo.",
        "index_cta_title": "Laktawan ang pagbabasa — buksan na lang ang kagamitan",
        "index_cta_body": "Mga isang minuto lang ang pagsasama ng dalawang backup, at "
                          "gagabayan ka ng app sa bawat hakbang.",
        "footer_all_guides": "Lahat ng gabay",
        "footer_community": "Komunidad",
        "footer_stats": "Study Stats",
        "footer_privacy": "Sa device mismo pinoproseso ng JW Sync ang lahat ng datos — hindi "
                          "kailanman umaalis ang mga file mo sa device mo. Libre; walang "
                          "account, walang ina-upload.",
        "footer_disclaimer": "Ang “JW Library” ay pag-aari ng Watch Tower Bible and Tract "
                             "Society of Pennsylvania. Ang JW Sync ay isang malayang "
                             "kasangkapan at hindi kaugnay nito ni inendorso man nito.",
        "groups": {
            "Getting started": "Pagsisimula",
            "Sharing scenarios": "Pagbabahagi ng mga nota",
            "Everyday scenarios": "Mga pang-araw-araw na sitwasyon",
            "Fixing problems": "Pag-aayos ng problema",
            "Power tools": "Mga masusing kagamitan",
        },
    },
    "sv": {
        "lang_name": "Svenska",
        "lang_label": "Språk",
        "lang_other": "Den här guiden på andra språk",
        "og_locale": "sv_SE",
        "site_guides": "JW Sync-guider",
        "nav_guides": "Guider",
        "nav_community": "Gemenskap",
        "nav_open_app": "Öppna appen",
        "crumb_guides": "Guider",
        "h_steps": "Steg för steg",
        "h_faq": "Vanliga frågor",
        "h_related": "Relaterade guider",
        "cta_title": "Gör det nu — gratis, i din webbläsare",
        "cta_body": "JW Sync slår ihop, redigerar och analyserar .jwlibrary-säkerhetskopior "
                    "helt på din enhet. Inget konto, inga uppladdningar, ingen installation.",
        "cta_btn": "Öppna JW Sync →",
        "index_title": "Guider om JW Library-säkerhetskopior, synk och anteckningar | JW Sync",
        "index_desc": "Praktiska guider för JW Library-säkerhetskopior: slå ihop kopior från "
                      "två enheter, flytta anteckningar till en ny mobil, gå från Android till "
                      "iPhone, reparera en säkerhetskopia som inte går att återställa, "
                      "redigera och söka i dina anteckningar, och mycket mer.",
        "index_h1": "Guider och instruktioner",
        "index_lede": "Allt om JW Library-säkerhetskopior, i tydliga steg: slå ihop enheter, "
                      "byta till en ny mobil, rädda anteckningar och få ut mer av biblioteket "
                      "du redan har. Varje verktyg som nämns körs gratis i din webbläsare — "
                      "dina filer laddas aldrig upp.",
        "index_cta_title": "Hoppa över läsningen — öppna verktyget direkt",
        "index_cta_body": "Att slå ihop två säkerhetskopior tar ungefär en minut, och appen "
                          "leder dig genom det.",
        "footer_all_guides": "Alla guider",
        "footer_community": "Gemenskap",
        "footer_stats": "Studiestatistik",
        "footer_privacy": "JW Sync behandlar all data lokalt — dina filer lämnar aldrig din "
                          "enhet. Gratis att använda; inget konto, inga uppladdningar.",
        "footer_disclaimer": "”JW Library” tillhör Watch Tower Bible and Tract Society of "
                             "Pennsylvania. JW Sync är ett fristående verktyg som varken är "
                             "knutet till eller godkänt av dem.",
        "groups": {
            "Getting started": "Kom igång",
            "Sharing scenarios": "Dela anteckningar",
            "Everyday scenarios": "Vardagliga situationer",
            "Fixing problems": "Lösa problem",
            "Power tools": "Avancerade verktyg",
        },
    },
    "ceb": {
        "lang_name": "Cebuano",
        "lang_label": "Pinulongan",
        "lang_other": "Kini nga giya sa ubang pinulongan",
        "og_locale": "ceb_PH",
        "site_guides": "Mga Giya sa JW Sync",
        "nav_guides": "Mga Giya",
        "nav_community": "Komunidad",
        "nav_open_app": "Ablihi ang app",
        "crumb_guides": "Mga Giya",
        "h_steps": "Lakang-lakang",
        "h_faq": "Kanunayng gipangutana",
        "h_related": "Kalabot nga mga giya",
        "cta_title": "Buhata kini karon — libre, sa imong browser",
        "cta_body": "Hiusahon, i-edit ug tugkaron sa JW Sync ang mga .jwlibrary nga backup nga "
                    "bug-os sa imong device. Walay account, walay gi-upload, walay gi-install.",
        "cta_btn": "Ablihi ang JW Sync →",
        "index_title": "Mga giya sa backup, sync ug nota sa JW Library | JW Sync",
        "index_desc": "Praktikal nga mga giya alang sa mga backup sa JW Library: paghiusa sa "
                      "backup gikan sa duha ka device, pagbalhin sa mga nota ngadto sa bag-ong "
                      "cellphone, pagbalhin gikan Android ngadto iPhone, pag-ayo sa backup nga "
                      "dili mapasig-uli, pag-edit ug pagpangita sa imong mga nota, ug daghan "
                      "pa.",
        "index_h1": "Mga giya ug pamaagi",
        "index_lede": "Ang tanan bahin sa mga backup sa JW Library, sa tin-aw nga mga lakang: "
                      "paghiusa sa mga device, pagbalhin ngadto sa bag-ong cellphone, pagluwas "
                      "sa mga nota, ug pagpahimulos pa sa library nga anaa na nimo. Ang matag "
                      "kagamitan nga gihisgotan modagan nga libre sa imong browser — wala gayod "
                      "gi-upload ang imong mga file.",
        "index_cta_title": "Laktawi ang pagbasa — ablihi na lang ang kagamitan",
        "index_cta_body": "Mga usa ka minuto ang paghiusa sa duha ka backup, ug giyahan ka sa "
                          "app sa matag lakang.",
        "footer_all_guides": "Tanang giya",
        "footer_community": "Komunidad",
        "footer_stats": "Study Stats",
        "footer_privacy": "Giproseso sa JW Sync ang tanang datos sa device mismo — wala gayod "
                          "mobiya ang imong mga file sa imong device. Libre; walay account, "
                          "walay gi-upload.",
        "footer_disclaimer": "Ang “JW Library” gipanag-iya sa Watch Tower Bible and Tract "
                             "Society of Pennsylvania. Ang JW Sync usa ka independenteng himan "
                             "ug walay kalabotan niini ni giuyonan niini.",
        "groups": {
            "Getting started": "Pagsugod",
            "Sharing scenarios": "Pagpaambit sa mga nota",
            "Everyday scenarios": "Mga adlaw-adlaw nga kahimtang",
            "Fixing problems": "Pagsulbad sa mga problema",
            "Power tools": "Mga abanteng kagamitan",
        },
    },
    "ar": {
        "lang_name": "العربية",
        "lang_label": "اللغة",
        "lang_other": "هذا الدليل بلغات أخرى",
        "og_locale": "ar_SA",
        "site_guides": "أدلة JW Sync",
        "nav_guides": "الأدلة",
        "nav_community": "المجتمع",
        "nav_open_app": "افتح التطبيق",
        "crumb_guides": "الأدلة",
        "h_steps": "خطوة بخطوة",
        "h_faq": "الأسئلة الشائعة",
        "h_related": "أدلة ذات صلة",
        "cta_title": "افعلها الآن — مجانًا، داخل متصفحك",
        "cta_body": "يدمج JW Sync نسخ ‎.jwlibrary‎ الاحتياطية ويحرّرها ويحلّلها على جهازك "
                    "بالكامل. بلا حساب، وبلا رفع للملفات، وبلا تثبيت أي شيء.",
        "cta_btn": "افتح JW Sync ←",
        "index_title": "أدلة النسخ الاحتياطي والمزامنة والملاحظات في JW Library | JW Sync",
        "index_desc": "أدلة عملية لنسخ JW Library الاحتياطية: دمج نسختين من جهازين، ونقل "
                      "الملاحظات إلى هاتف جديد، والانتقال من أندرويد إلى آيفون، وإصلاح نسخة "
                      "احتياطية ترفض الاستعادة، وتحرير ملاحظاتك والبحث فيها، وأكثر.",
        "index_h1": "الأدلة وطرق العمل",
        "index_lede": "كل ما يتعلق بنسخ JW Library الاحتياطية، بخطوات واضحة: دمج الأجهزة، "
                      "والانتقال إلى هاتف جديد، وإنقاذ الملاحظات، والاستفادة أكثر من المكتبة "
                      "التي بين يديك. كل أداة مذكورة تعمل مجانًا داخل متصفحك — وملفاتك لا "
                      "تُرفع أبدًا.",
        "index_cta_title": "تخطَّ القراءة — وافتح الأداة مباشرة",
        "index_cta_body": "دمج نسختين احتياطيتين يستغرق نحو دقيقة، والتطبيق يرشدك خطوة بخطوة.",
        "footer_all_guides": "كل الأدلة",
        "footer_community": "المجتمع",
        "footer_stats": "إحصاءات الدرس",
        "footer_privacy": "يعالج JW Sync كل البيانات محليًا — ملفاتك لا تغادر جهازك أبدًا. "
                          "مجاني الاستخدام؛ بلا حساب وبلا رفع للملفات.",
        "footer_disclaimer": "«JW Library» ملك لجمعية برج المراقبة للكتاب المقدس والكراريس في "
                             "بنسلفانيا. JW Sync أداة مستقلة وليست تابعة لها ولا معتمدة منها.",
        "groups": {
            "Getting started": "البداية",
            "Sharing scenarios": "حالات المشاركة",
            "Everyday scenarios": "حالات يومية",
            "Fixing problems": "حل المشكلات",
            "Power tools": "أدوات متقدّمة",
        },
    },
    "he": {
        "lang_name": "עברית",
        "lang_label": "שפה",
        "lang_other": "המדריך הזה בשפות אחרות",
        "og_locale": "he_IL",
        "site_guides": "מדריכי JW Sync",
        "nav_guides": "מדריכים",
        "nav_community": "קהילה",
        "nav_open_app": "פתיחת היישום",
        "crumb_guides": "מדריכים",
        "h_steps": "שלב אחר שלב",
        "h_faq": "שאלות נפוצות",
        "h_related": "מדריכים קשורים",
        "cta_title": "עשו את זה עכשיו — בחינם, בדפדפן שלכם",
        "cta_body": "‏JW Sync ממזג, עורך ומנתח גיבויי ‎.jwlibrary‎ לגמרי על המכשיר שלכם. בלי חשבון, בלי העלאות, בלי שום התקנה.",
        "cta_btn": "פתחו את JW Sync ←",
        "index_title": "מדריכים לגיבוי, לסנכרון ולהערות של JW Library | JW Sync",
        "index_desc": "מדריכים מעשיים לגיבויים של JW Library: מיזוג גיבויים משני מכשירים, העברת הערות לטלפון חדש, מעבר מאנדרואיד לאייפון, תיקון גיבוי שלא מצליח להשתחזר, עריכה וחיפוש בהערות שלכם, ועוד.",
        "index_h1": "מדריכים והדרכות",
        "index_lede": "כל מה שקשור לגיבויים של JW Library, בשלבים פשוטים: מיזוג מכשירים, מעבר לטלפון חדש, הצלת הערות, והפקת יותר מהספרייה שכבר יש לכם. כל כלי שמוזכר רץ בחינם בדפדפן שלכם — הקבצים שלכם לעולם לא מועלים.",
        "index_cta_title": "דלגו על הקריאה — פשוט פתחו את הכלי",
        "index_cta_body": "מיזוג של שני גיבויים לוקח בערך דקה והיישום מלווה אתכם בתהליך.",
        "footer_all_guides": "כל המדריכים",
        "footer_community": "קהילה",
        "footer_stats": "סטטיסטיקת לימוד",
        "footer_privacy": "‏JW Sync מעבד את כל הנתונים מקומית — הקבצים שלכם לעולם לא עוזבים את המכשיר. השימוש חינמי; בלי חשבון, בלי העלאות.",
        "footer_disclaimer": "\u201cJW Library\u201d הוא רכושה של אגודת המצפה, המקרא והחוברות של פנסילבניה. JW Sync הוא כלי עצמאי ואינו מסונף אליה או מאושר על ידה.",
        "groups": {
            "Getting started": "צעדים ראשונים",
            "Sharing scenarios": "תרחישי שיתוף",
            "Everyday scenarios": "תרחישים יומיומיים",
            "Fixing problems": "פתרון בעיות",
            "Power tools": "כלים מתקדמים",
        },
    },
    "uk": {
        "lang_name": "Українська",
        "lang_label": "Мова",
        "lang_other": "Цей посібник іншими мовами",
        "og_locale": "uk_UA",
        "site_guides": "Посібники JW Sync",
        "nav_guides": "Посібники",
        "nav_community": "Спільнота",
        "nav_open_app": "Відкрити програму",
        "crumb_guides": "Посібники",
        "h_steps": "Крок за кроком",
        "h_faq": "Часті запитання",
        "h_related": "Пов'язані посібники",
        "cta_title": "Зробіть це зараз — безкоштовно, у вашому браузері",
        "cta_body": "JW Sync об'єднує, редагує й аналізує резервні копії .jwlibrary цілком на вашому пристрої. Без облікового запису, без надсилання на сервер, без встановлення.",
        "cta_btn": "Відкрити JW Sync →",
        "index_title": "Посібники з резервних копій, синхронізації та нотаток JW Library | JW Sync",
        "index_desc": "Практичні посібники з резервних копій JW Library: об'єднання копій із двох пристроїв, перенесення нотаток на новий телефон, перехід з Android на iPhone, виправлення копії, яка не відновлюється, редагування й пошук у ваших нотатках тощо.",
        "index_h1": "Посібники та інструкції",
        "index_lede": "Усе про резервні копії JW Library простими кроками: об'єднання пристроїв, перехід на новий телефон, порятунок нотаток і краще використання бібліотеки, яку ви вже маєте. Кожен згаданий інструмент працює безкоштовно у вашому браузері — ваші файли ніколи не надсилаються на сервер.",
        "index_cta_title": "Не хочете читати — просто відкрийте інструмент",
        "index_cta_body": "Об'єднання двох копій займає близько хвилини, і програма проведе вас крок за кроком.",
        "footer_all_guides": "Усі посібники",
        "footer_community": "Спільнота",
        "footer_stats": "Статистика вивчення",
        "footer_privacy": "JW Sync обробляє всі дані локально — ваші файли ніколи не залишають ваш пристрій. Користування безкоштовне; без облікового запису, без надсилання на сервер.",
        "footer_disclaimer": "\u201cJW Library\u201d є власністю Watch Tower Bible and Tract Society of Pennsylvania. JW Sync — незалежна утиліта, не пов'язана з нею і не схвалена нею.",
        "groups": {
            "Getting started": "Перші кроки",
            "Sharing scenarios": "Сценарії поширення",
            "Everyday scenarios": "Щоденні сценарії",
            "Fixing problems": "Розв'язання проблем",
            "Power tools": "Потужні інструменти",
        },
    },
    "pl": {
        "lang_name": "Polski",
        "lang_label": "Język",
        "lang_other": "Ten poradnik w innych językach",
        "og_locale": "pl_PL",
        "site_guides": "Poradniki JW Sync",
        "nav_guides": "Poradniki",
        "nav_community": "Społeczność",
        "nav_open_app": "Otwórz aplikację",
        "crumb_guides": "Poradniki",
        "h_steps": "Krok po kroku",
        "h_faq": "Częste pytania",
        "h_related": "Powiązane poradniki",
        "cta_title": "Zrób to teraz — bezpłatnie, w przeglądarce",
        "cta_body": "JW Sync scala, edytuje i analizuje kopie zapasowe .jwlibrary w całości na Twoim urządzeniu. Bez konta, bez wysyłania na serwer, bez instalowania czegokolwiek.",
        "cta_btn": "Otwórz JW Sync →",
        "index_title": "Poradniki o kopiach zapasowych, synchronizacji i notatkach JW Library | JW Sync",
        "index_desc": "Praktyczne poradniki o kopiach zapasowych JW Library: scalanie kopii z dwóch urządzeń, przenoszenie notatek na nowy telefon, przejście z Androida na iPhone'a, naprawa kopii, która się nie przywraca, edycja i wyszukiwanie notatek i więcej.",
        "index_h1": "Poradniki i instrukcje",
        "index_lede": "Wszystko o kopiach zapasowych JW Library w prostych krokach: scalanie urządzeń, przejście na nowy telefon, ratowanie notatek i lepsze wykorzystanie biblioteki, którą już masz. Każde wymienione narzędzie działa bezpłatnie w Twojej przeglądarce — Twoje pliki nigdy nie są wysyłane na serwer.",
        "index_cta_title": "Nie chcesz czytać — po prostu otwórz narzędzie",
        "index_cta_body": "Scalenie dwóch kopii zajmuje około minuty, a aplikacja przeprowadzi Cię przez to krok po kroku.",
        "footer_all_guides": "Wszystkie poradniki",
        "footer_community": "Społeczność",
        "footer_stats": "Statystyki studium",
        "footer_privacy": "JW Sync przetwarza wszystkie dane lokalnie — Twoje pliki nigdy nie opuszczają urządzenia. Korzystanie jest bezpłatne; bez konta, bez wysyłania na serwer.",
        "footer_disclaimer": "\u201cJW Library\u201d jest własnością Watch Tower Bible and Tract Society of Pennsylvania. JW Sync to niezależne narzędzie, niezwiązane z nią ani przez nią nieautoryzowane.",
        "groups": {
            "Getting started": "Pierwsze kroki",
            "Sharing scenarios": "Scenariusze udostępniania",
            "Everyday scenarios": "Scenariusze codzienne",
            "Fixing problems": "Rozwiązywanie problemów",
            "Power tools": "Narzędzia zaawansowane",
        },
    },
    "zh-Hans": {
        "lang_name": "简体中文",
        "lang_label": "语言",
        "lang_other": "本指南的其他语言版本",
        "og_locale": "zh_CN",
        "site_guides": "JW Sync 指南",
        "nav_guides": "指南",
        "nav_community": "社区",
        "nav_open_app": "打开应用",
        "crumb_guides": "指南",
        "h_steps": "分步操作",
        "h_faq": "常见问题",
        "h_related": "相关指南",
        "cta_title": "现在就试——免费，在浏览器里完成",
        "cta_body": "JW Sync 完全在你的设备上合并、编辑和分析 .jwlibrary 备份。不需要账号，不上传，不用安装任何东西。",
        "cta_btn": "打开 JW Sync →",
        "index_title": "JW Library 备份、同步与笔记指南 | JW Sync",
        "index_desc": "实用的 JW Library 备份指南：合并两台设备的备份、把笔记转移到新手机、从 Android 换到 iPhone、修复无法还原的备份、编辑和搜索笔记等等。",
        "index_h1": "指南与教程",
        "index_lede": "关于 JW Library 备份的一切，用最简单的步骤讲清楚：合并设备、换新手机、抢救笔记，以及更好地利用你已有的书库。文中提到的每个工具都在你的浏览器里免费运行——你的文件绝不会被上传。",
        "index_cta_title": "不想看文字——直接打开工具",
        "index_cta_body": "合并两个备份大约只要一分钟，应用会一步步带着你做。",
        "footer_all_guides": "全部指南",
        "footer_community": "社区",
        "footer_stats": "研读统计",
        "footer_privacy": "JW Sync 所有数据都在本地处理——你的文件绝不会离开你的设备。免费使用；不需要账号，不上传。",
        "footer_disclaimer": "“JW Library” 是 Watch Tower Bible and Tract Society of Pennsylvania 的财产。JW Sync 是独立的实用工具，与其并无关联，也未获其认可。",
        "groups": {
            "Getting started": "入门",
            "Sharing scenarios": "分享场景",
            "Everyday scenarios": "日常场景",
            "Fixing problems": "解决问题",
            "Power tools": "进阶工具",
        },
    },
    "zh-Hant": {
        "lang_name": "繁體中文",
        "lang_label": "語言",
        "lang_other": "本指南的其他語言版本",
        "og_locale": "zh_TW",
        "site_guides": "JW Sync 指南",
        "nav_guides": "指南",
        "nav_community": "社群",
        "nav_open_app": "開啟應用程式",
        "crumb_guides": "指南",
        "h_steps": "逐步操作",
        "h_faq": "常見問題",
        "h_related": "相關指南",
        "cta_title": "現在就試——免費，在瀏覽器裡完成",
        "cta_body": "JW Sync 完全在你的裝置上合併、編輯和分析 .jwlibrary 備份。不需要帳號，不上傳，不用安裝任何東西。",
        "cta_btn": "開啟 JW Sync →",
        "index_title": "JW Library 備份、同步與筆記指南 | JW Sync",
        "index_desc": "實用的 JW Library 備份指南：合併兩台裝置的備份、把筆記轉移到新手機、從 Android 換到 iPhone、修復無法還原的備份、編輯和搜尋筆記等等。",
        "index_h1": "指南與教學",
        "index_lede": "關於 JW Library 備份的一切，用最簡單的步驟講清楚：合併裝置、換新手機、搶救筆記，以及更好地運用你已有的書庫。文中提到的每個工具都在你的瀏覽器裡免費執行——你的檔案絕不會被上傳。",
        "index_cta_title": "不想看文字——直接開啟工具",
        "index_cta_body": "合併兩個備份大約只要一分鐘，應用程式會一步步帶著你做。",
        "footer_all_guides": "全部指南",
        "footer_community": "社群",
        "footer_stats": "研讀統計",
        "footer_privacy": "JW Sync 所有資料都在本機處理——你的檔案絕不會離開你的裝置。免費使用；不需要帳號，不上傳。",
        "footer_disclaimer": "“JW Library” 是 Watch Tower Bible and Tract Society of Pennsylvania 的財產。JW Sync 是獨立的實用工具，與其並無關聯，也未獲其認可。",
        "groups": {
            "Getting started": "入門",
            "Sharing scenarios": "分享情境",
            "Everyday scenarios": "日常情境",
            "Fixing problems": "解決問題",
            "Power tools": "進階工具",
        },
    },
    "yue-Hant": {
        "lang_name": "粵語",
        "lang_label": "語言",
        "lang_other": "呢份指南嘅其他語言版本",
        "og_locale": "zh_HK",
        "site_guides": "JW Sync 指南",
        "nav_guides": "指南",
        "nav_community": "社群",
        "nav_open_app": "開啟應用程式",
        "crumb_guides": "指南",
        "h_steps": "一步一步做",
        "h_faq": "常見問題",
        "h_related": "相關指南",
        "cta_title": "而家就試——免費，喺瀏覽器度做晒",
        "cta_body": "JW Sync 完全喺你部裝置度合併、編輯同分析 .jwlibrary 備份。唔使帳號，唔使上載，亦都唔使裝任何嘢。",
        "cta_btn": "開啟 JW Sync →",
        "index_title": "JW Library 備份、同步同筆記指南 | JW Sync",
        "index_desc": "實用嘅 JW Library 備份指南：合併兩部裝置嘅備份、將筆記搬去新手機、由 Android 轉去 iPhone、整返還原唔到嘅備份、編輯同搜尋筆記等等。",
        "index_h1": "指南同教學",
        "index_lede": "關於 JW Library 備份嘅一切，用最簡單嘅步驟講清楚：合併裝置、換新手機、搶救筆記，仲有點樣善用你已經有嘅書庫。文入面提到嘅每件工具都喺你嘅瀏覽器度免費運行——你嘅檔案絕對唔會上載。",
        "index_cta_title": "唔想睇字——直接開個工具",
        "index_cta_body": "合併兩個備份大概一分鐘搞掂，應用程式會一步一步帶你做。",
        "footer_all_guides": "全部指南",
        "footer_community": "社群",
        "footer_stats": "研讀統計",
        "footer_privacy": "JW Sync 所有資料都喺本機處理——你嘅檔案絕對唔會離開你部裝置。免費用；唔使帳號，唔使上載。",
        "footer_disclaimer": "“JW Library” 係 Watch Tower Bible and Tract Society of Pennsylvania 嘅財產。JW Sync 係獨立嘅工具，同佢冇任何關聯，亦都未獲佢認可。",
        "groups": {
            "Getting started": "入門",
            "Sharing scenarios": "分享情境",
            "Everyday scenarios": "日常情境",
            "Fixing problems": "解決問題",
            "Power tools": "進階工具",
        },
    },
    "vi": {
        "lang_name": "Tiếng Việt",
        "lang_label": "Ngôn ngữ",
        "lang_other": "Hướng dẫn này trong các ngôn ngữ khác",
        "og_locale": "vi_VN",
        "site_guides": "Hướng dẫn JW Sync",
        "nav_guides": "Hướng dẫn",
        "nav_community": "Cộng đồng",
        "nav_open_app": "Mở ứng dụng",
        "crumb_guides": "Hướng dẫn",
        "h_steps": "Từng bước một",
        "h_faq": "Câu hỏi thường gặp",
        "h_related": "Hướng dẫn liên quan",
        "cta_title": "Làm ngay bây giờ — miễn phí, ngay trong trình duyệt",
        "cta_body": "JW Sync hợp nhất, chỉnh sửa và phân tích các bản sao lưu .jwlibrary hoàn toàn trên thiết bị của bạn. Không cần tài khoản, không tải lên, không phải cài gì cả.",
        "cta_btn": "Mở JW Sync →",
        "index_title": "Hướng dẫn về sao lưu, đồng bộ và ghi chú JW Library | JW Sync",
        "index_desc": "Hướng dẫn thiết thực về bản sao lưu JW Library: hợp nhất bản sao lưu từ hai thiết bị, chuyển ghi chú sang điện thoại mới, đổi từ Android sang iPhone, sửa bản sao lưu không khôi phục được, chỉnh sửa và tìm kiếm ghi chú, và nhiều nữa.",
        "index_h1": "Hướng dẫn và cách làm",
        "index_lede": "Mọi điều về bản sao lưu JW Library, qua những bước đơn giản: hợp nhất các thiết bị, chuyển sang điện thoại mới, cứu lấy ghi chú, và tận dụng tốt hơn thư viện bạn đang có. Mọi công cụ được nhắc đến đều chạy miễn phí trong trình duyệt của bạn — tập tin của bạn không bao giờ được tải lên.",
        "index_cta_title": "Không muốn đọc — cứ mở thẳng công cụ",
        "index_cta_body": "Hợp nhất hai bản sao lưu chỉ mất khoảng một phút, và ứng dụng sẽ dẫn bạn đi từng bước.",
        "footer_all_guides": "Tất cả hướng dẫn",
        "footer_community": "Cộng đồng",
        "footer_stats": "Thống kê học hỏi",
        "footer_privacy": "JW Sync xử lý mọi dữ liệu tại chỗ — tập tin của bạn không bao giờ rời khỏi thiết bị. Miễn phí sử dụng; không cần tài khoản, không tải lên.",
        "footer_disclaimer": "“JW Library” là tài sản của Watch Tower Bible and Tract Society of Pennsylvania. JW Sync là một tiện ích độc lập, không liên kết với và không được tổ chức này chứng thực.",
        "groups": {
            "Getting started": "Bắt đầu",
            "Sharing scenarios": "Tình huống chia sẻ",
            "Everyday scenarios": "Tình huống hằng ngày",
            "Fixing problems": "Khắc phục sự cố",
            "Power tools": "Công cụ nâng cao",
        },
    },
    "hu": {
        "lang_name": "Magyar",
        "lang_label": "Nyelv",
        "lang_other": "Ez az útmutató más nyelveken",
        "og_locale": "hu_HU",
        "site_guides": "JW Sync útmutatók",
        "nav_guides": "Útmutatók",
        "nav_community": "Közösség",
        "nav_open_app": "Alkalmazás megnyitása",
        "crumb_guides": "Útmutatók",
        "h_steps": "Lépésről lépésre",
        "h_faq": "Gyakori kérdések",
        "h_related": "Kapcsolódó útmutatók",
        "cta_title": "Csináld most — ingyen, a böngésződben",
        "cta_body": "A JW Sync teljes egészében a te eszközödön egyesíti, szerkeszti és elemzi a .jwlibrary mentéseket. Nincs fiók, nincs feltöltés, nem kell semmit telepíteni.",
        "cta_btn": "JW Sync megnyitása →",
        "index_title": "JW Library mentés-, szinkron- és jegyzetútmutatók | JW Sync",
        "index_desc": "Gyakorlati útmutatók a JW Library-mentésekhez: két eszköz mentésének egyesítése, jegyzetek átvitele új telefonra, váltás Androidról iPhone-ra, vissza nem állítható mentés javítása, jegyzetek szerkesztése és keresése, és még sok más.",
        "index_h1": "Útmutatók és leírások",
        "index_lede": "Minden a JW Library-mentésekről, egyszerű lépésekben: eszközök egyesítése, költözés új telefonra, jegyzetek megmentése, és több haszon abból a könyvtárból, ami már megvan. Minden említett eszköz ingyen fut a böngésződben — a fájljaidat soha nem töltjük fel.",
        "index_cta_title": "Hagyd az olvasást — nyisd meg az eszközt",
        "index_cta_body": "Két mentés egyesítése körülbelül egy perc, és az alkalmazás végigvezet rajta.",
        "footer_all_guides": "Összes útmutató",
        "footer_community": "Közösség",
        "footer_stats": "Tanulmányozási statisztika",
        "footer_privacy": "A JW Sync minden adatot helyben dolgoz fel — a fájljaid soha nem hagyják el az eszközödet. Ingyenes; nincs fiók, nincs feltöltés.",
        "footer_disclaimer": "A „JW Library” a Watch Tower Bible and Tract Society of Pennsylvania tulajdona. A JW Sync független segédeszköz, amely nem áll kapcsolatban vele, és nem is támogatja azt.",
        "groups": {
            "Getting started": "Első lépések",
            "Sharing scenarios": "Megosztási helyzetek",
            "Everyday scenarios": "Hétköznapi helyzetek",
            "Fixing problems": "Hibaelhárítás",
            "Power tools": "Haladó eszközök",
        },
    },
    "ro": {
        "lang_name": "Română",
        "lang_label": "Limbă",
        "lang_other": "Acest ghid în alte limbi",
        "og_locale": "ro_RO",
        "site_guides": "Ghiduri JW Sync",
        "nav_guides": "Ghiduri",
        "nav_community": "Comunitate",
        "nav_open_app": "Deschide aplicația",
        "crumb_guides": "Ghiduri",
        "h_steps": "Pas cu pas",
        "h_faq": "Întrebări frecvente",
        "h_related": "Ghiduri înrudite",
        "cta_title": "Fă-o acum — gratuit, în browserul tău",
        "cta_body": "JW Sync îmbină, modifică și analizează copii de rezervă .jwlibrary în întregime pe dispozitivul tău. Fără cont, fără încărcări, fără nimic de instalat.",
        "cta_btn": "Deschide JW Sync →",
        "index_title": "Ghiduri pentru copii de rezervă, sincronizare și notițe JW Library | JW Sync",
        "index_desc": "Ghiduri practice pentru copiile de rezervă JW Library: îmbină copiile de pe două dispozitive, mută notițe pe un telefon nou, treci de la Android la iPhone, repară o copie care nu se restaurează, modifică și caută în notițe și multe altele.",
        "index_h1": "Ghiduri și instrucțiuni",
        "index_lede": "Tot ce ține de copiile de rezervă JW Library, în pași simpli: îmbinarea dispozitivelor, mutarea pe un telefon nou, salvarea notițelor și cum să scoți mai mult din biblioteca pe care o ai deja. Fiecare instrument amintit rulează gratuit în browserul tău — fișierele tale nu sunt încărcate niciodată.",
        "index_cta_title": "Sari peste citit — deschide direct instrumentul",
        "index_cta_body": "Îmbinarea a două copii de rezervă durează cam un minut, iar aplicația te ghidează pas cu pas.",
        "footer_all_guides": "Toate ghidurile",
        "footer_community": "Comunitate",
        "footer_stats": "Statistici de studiu",
        "footer_privacy": "JW Sync procesează toate datele local — fișierele tale nu părăsesc niciodată dispozitivul. Gratuit; fără cont, fără încărcări.",
        "footer_disclaimer": "„JW Library” este proprietatea Watch Tower Bible and Tract Society of Pennsylvania. JW Sync este un utilitar independent, care nu este afiliat cu aceasta și nici aprobat de ea.",
        "groups": {
            "Getting started": "Primii pași",
            "Sharing scenarios": "Situații de partajare",
            "Everyday scenarios": "Situații de zi cu zi",
            "Fixing problems": "Rezolvarea problemelor",
            "Power tools": "Instrumente avansate",
        },
    },
    "el": {
        "lang_name": "Ελληνικά",
        "lang_label": "Γλώσσα",
        "lang_other": "Αυτός ο οδηγός σε άλλες γλώσσες",
        "og_locale": "el_GR",
        "site_guides": "Οδηγοί JW Sync",
        "nav_guides": "Οδηγοί",
        "nav_community": "Κοινότητα",
        "nav_open_app": "Άνοιγμα εφαρμογής",
        "crumb_guides": "Οδηγοί",
        "h_steps": "Βήμα προς βήμα",
        "h_faq": "Συχνές ερωτήσεις",
        "h_related": "Σχετικοί οδηγοί",
        "cta_title": "Κάντε το τώρα — δωρεάν, μέσα στο πρόγραμμα περιήγησής σας",
        "cta_body": "Το JW Sync συγχωνεύει, επεξεργάζεται και αναλύει αρχεία .jwlibrary εξ ολοκλήρου μέσα στη συσκευή σας. Χωρίς λογαριασμό, χωρίς μεταφορτώσεις, χωρίς εγκατάσταση.",
        "cta_btn": "Άνοιγμα του JW Sync →",
        "index_title": "Οδηγοί για αντίγραφα ασφαλείας, συγχρονισμό και σημειώσεις του JW Library | JW Sync",
        "index_desc": "Πρακτικοί οδηγοί για τα αντίγραφα ασφαλείας του JW Library: συγχωνεύστε τα αντίγραφα δύο συσκευών, μεταφέρετε σημειώσεις σε νέο τηλέφωνο, περάστε από Android σε iPhone, διορθώστε ένα αντίγραφο που δεν επαναφέρεται, επεξεργαστείτε και αναζητήστε τις σημειώσεις σας και πολλά ακόμη.",
        "index_h1": "Οδηγοί και οδηγίες",
        "index_lede": "Όλα όσα αφορούν τα αντίγραφα ασφαλείας του JW Library, σε απλά βήματα: συγχώνευση συσκευών, μετακόμιση σε νέο τηλέφωνο, διάσωση των σημειώσεών σας και πώς να αξιοποιήσετε καλύτερα τη βιβλιοθήκη που ήδη έχετε. Κάθε εργαλείο που αναφέρεται λειτουργεί δωρεάν μέσα στο πρόγραμμα περιήγησής σας — τα αρχεία σας δεν μεταφορτώνονται ποτέ.",
        "index_cta_title": "Παραλείψτε το διάβασμα — ανοίξτε κατευθείαν το εργαλείο",
        "index_cta_body": "Η συγχώνευση δύο αντιγράφων ασφαλείας παίρνει περίπου ένα λεπτό και η εφαρμογή σάς καθοδηγεί βήμα προς βήμα.",
        "footer_all_guides": "Όλοι οι οδηγοί",
        "footer_community": "Κοινότητα",
        "footer_stats": "Στατιστικά μελέτης",
        "footer_privacy": "Το JW Sync επεξεργάζεται όλα τα δεδομένα μέσα στη συσκευή σας — τα αρχεία σας δεν φεύγουν ποτέ από αυτήν. Δωρεάν· χωρίς λογαριασμό, χωρίς μεταφορτώσεις.",
        "footer_disclaimer": "Το «JW Library» ανήκει στη Watch Tower Bible and Tract Society of Pennsylvania. Το JW Sync είναι ανεξάρτητο εργαλείο που δεν συνδέεται με αυτήν ούτε έχει την έγκρισή της.",
        "groups": {
            "Getting started": "Ξεκινώντας",
            "Sharing scenarios": "Σενάρια κοινοποίησης",
            "Everyday scenarios": "Καθημερινά σενάρια",
            "Fixing problems": "Επίλυση προβλημάτων",
            "Power tools": "Προηγμένα εργαλεία",
        },
    },
    "sw": {
        "lang_name": "Kiswahili",
        "lang_label": "Lugha",
        "lang_other": "Mwongozo huu katika lugha nyingine",
        "og_locale": "sw_TZ",
        "site_guides": "Miongozo ya JW Sync",
        "nav_guides": "Miongozo",
        "nav_community": "Jumuiya",
        "nav_open_app": "Fungua programu",
        "crumb_guides": "Miongozo",
        "h_steps": "Hatua kwa hatua",
        "h_faq": "Maswali yanayoulizwa mara kwa mara",
        "h_related": "Miongozo inayohusiana",
        "cta_title": "Ifanye sasa \u2014 bila malipo, ndani ya kivinjari chako",
        "cta_body": "JW Sync huunganisha, huhariri na huchanganua nakala rudufu za .jwlibrary ndani kabisa ya kifaa chako. Hakuna akaunti, hakuna kupakia, hakuna cha kusakinisha.",
        "cta_btn": "Fungua JW Sync \u2192",
        "index_title": "Miongozo ya nakala rudufu, usawazishaji na madokezo ya JW Library | JW Sync",
        "index_desc": "Miongozo ya vitendo kuhusu nakala rudufu za JW Library: unganisha nakala za vifaa viwili, hamisha madokezo kwenye simu mpya, hama kutoka Android kwenda iPhone, rekebisha nakala isiyorejeshwa, hariri na utafute madokezo na mengi zaidi.",
        "index_h1": "Miongozo na maelekezo",
        "index_lede": "Kila kitu kuhusu nakala rudufu za JW Library, kwa hatua rahisi: kuunganisha vifaa, kuhamia simu mpya, kuokoa madokezo yako na jinsi ya kupata zaidi kutoka maktaba uliyo nayo tayari. Kila kifaa kilichotajwa hufanya kazi bila malipo ndani ya kivinjari chako \u2014 mafaili yako hayapakiwi kamwe.",
        "index_cta_title": "Ruka kusoma \u2014 fungua kifaa moja kwa moja",
        "index_cta_body": "Kuunganisha nakala rudufu mbili huchukua kama dakika moja, na programu hukuongoza hatua kwa hatua.",
        "footer_all_guides": "Miongozo yote",
        "footer_community": "Jumuiya",
        "footer_stats": "Takwimu za Funzo",
        "footer_privacy": "JW Sync huchakata data yote ndani ya kifaa chako \u2014 mafaili yako hayaondoki kwenye kifaa chako kamwe. Bila malipo; hakuna akaunti, hakuna kupakia.",
        "footer_disclaimer": "\u201cJW Library\u201d ni mali ya Watch Tower Bible and Tract Society of Pennsylvania. JW Sync ni kifaa huru kisichohusiana nayo wala kuidhinishwa nayo.",
        "groups": {
            "Getting started": "Kuanza",
            "Sharing scenarios": "Hali za kushiriki",
            "Everyday scenarios": "Hali za kila siku",
            "Fixing problems": "Kutatua matatizo",
            "Power tools": "Vifaa vya hali ya juu",
        },
    },
    "nl": {
        "lang_name": "Nederlands",
        "lang_label": "Taal",
        "lang_other": "Deze handleiding in andere talen",
        "og_locale": "nl_NL",
        "site_guides": "JW Sync-handleidingen",
        "nav_guides": "Handleidingen",
        "nav_community": "Community",
        "nav_open_app": "App openen",
        "crumb_guides": "Handleidingen",
        "h_steps": "Stap voor stap",
        "h_faq": "Veelgestelde vragen",
        "h_related": "Verwante handleidingen",
        "cta_title": "Doe het nu — gratis, in je browser",
        "cta_body": "JW Sync voegt .jwlibrary-back-ups samen, bewerkt ze en analyseert ze volledig op je eigen apparaat. Geen account, niets uploaden, niets installeren.",
        "cta_btn": "JW Sync openen \u2192",
        "index_title": "Handleidingen voor JW Library-back-ups, synchronisatie en aantekeningen | JW Sync",
        "index_desc": "Praktische handleidingen voor JW Library-back-ups: back-ups van twee apparaten samenvoegen, aantekeningen naar een nieuwe telefoon overzetten, van Android naar iPhone overstappen, een back-up repareren die niet terugleest, aantekeningen bewerken en doorzoeken en meer.",
        "index_h1": "Handleidingen en instructies",
        "index_lede": "Alles rond JW Library-back-ups, in eenvoudige stappen: apparaten samenvoegen, overstappen naar een nieuwe telefoon, je aantekeningen redden en meer halen uit de bibliotheek die je al hebt. Elk genoemd hulpmiddel draait gratis in je browser — je bestanden worden nooit ge\u00fcpload.",
        "index_cta_title": "Sla het lezen over — open het hulpmiddel meteen",
        "index_cta_body": "Twee back-ups samenvoegen duurt ongeveer een minuut, en de app leidt je stap voor stap.",
        "footer_all_guides": "Alle handleidingen",
        "footer_community": "Community",
        "footer_stats": "Studiestatistieken",
        "footer_privacy": "JW Sync verwerkt alles lokaal — je bestanden verlaten je apparaat nooit. Gratis; geen account, niets uploaden.",
        "footer_disclaimer": "\u201cJW Library\u201d is eigendom van de Watch Tower Bible and Tract Society of Pennsylvania. JW Sync is een onafhankelijk hulpmiddel dat daar niet aan verbonden is en er ook niet door wordt goedgekeurd.",
        "groups": {
            "Getting started": "Aan de slag",
            "Sharing scenarios": "Delen met anderen",
            "Everyday scenarios": "Dagelijks gebruik",
            "Fixing problems": "Problemen oplossen",
            "Power tools": "Geavanceerde hulpmiddelen",
        },
    },
    "id": {
        "lang_name": "Bahasa Indonesia",
        "lang_label": "Bahasa",
        "lang_other": "Panduan ini dalam bahasa lain",
        "og_locale": "id_ID",
        "site_guides": "Panduan JW Sync",
        "nav_guides": "Panduan",
        "nav_community": "Komunitas",
        "nav_open_app": "Buka aplikasinya",
        "crumb_guides": "Panduan",
        "h_steps": "Langkah demi langkah",
        "h_faq": "Pertanyaan yang sering diajukan",
        "h_related": "Panduan terkait",
        "cta_title": "Lakukan sekarang — gratis, di peramban Anda",
        "cta_body": "JW Sync menggabungkan, mengubah, dan menganalisis cadangan .jwlibrary sepenuhnya di perangkat Anda. Tanpa akun, tanpa unggahan, tanpa perlu memasang apa pun.",
        "cta_btn": "Buka JW Sync →",
        "index_title": "Panduan Cadangan, Sinkronisasi & Catatan JW Library | JW Sync",
        "index_desc": "Panduan praktis untuk cadangan JW Library: menggabungkan cadangan dari dua perangkat, memindahkan catatan ke ponsel baru, beralih dari Android ke iPhone, memperbaiki cadangan yang tidak mau dipulihkan, mengubah dan mencari catatan Anda, dan banyak lagi.",
        "index_h1": "Panduan & cara pakai",
        "index_lede": "Segala hal tentang cadangan JW Library, dengan langkah yang sederhana: menggabungkan perangkat, pindah ke ponsel baru, menyelamatkan catatan, dan memanfaatkan lebih banyak dari perpustakaan yang sudah Anda miliki. Setiap alat yang disebutkan berjalan gratis di peramban Anda — berkas Anda tidak pernah diunggah.",
        "index_cta_title": "Lewati bacaannya — langsung buka alatnya",
        "index_cta_body": "Menggabungkan dua cadangan hanya perlu sekitar semenit dan aplikasinya akan memandu Anda.",
        "footer_all_guides": "Semua panduan",
        "footer_community": "Komunitas",
        "footer_stats": "Statistik Pelajaran",
        "footer_privacy": "JW Sync memproses semua data secara lokal — berkas Anda tidak pernah meninggalkan perangkat Anda. Gratis; tanpa akun, tanpa unggahan.",
        "footer_disclaimer": "“JW Library” adalah milik Watch Tower Bible and Tract Society of Pennsylvania. JW Sync adalah alat bantu independen yang tidak berafiliasi dengan maupun didukung olehnya.",
        "groups": {
            "Getting started": "Memulai",
            "Sharing scenarios": "Skenario berbagi",
            "Everyday scenarios": "Skenario sehari-hari",
            "Fixing problems": "Mengatasi masalah",
            "Power tools": "Alat canggih",
        },
    },
    "hi": {
        "lang_name": "हिन्दी",
        "lang_label": "भाषा",
        "lang_other": "यह गाइड दूसरी भाषाओं में",
        "og_locale": "hi_IN",
        "site_guides": "JW Sync गाइड",
        "nav_guides": "गाइड",
        "nav_community": "समुदाय",
        "nav_open_app": "ऐप खोलें",
        "crumb_guides": "गाइड",
        "h_steps": "कदम-दर-कदम",
        "h_faq": "अक्सर पूछे जाने वाले सवाल",
        "h_related": "मिलती-जुलती गाइड",
        "cta_title": "अभी कीजिए — मुफ़्त, आपके ब्राउज़र में",
        "cta_body": "JW Sync .jwlibrary बैकअप पूरी तरह आपके ही डिवाइस पर मर्ज करता, बदलता और जाँचता है। कोई खाता नहीं, कोई अपलोड नहीं, कुछ भी इंस्टॉल करने की ज़रूरत नहीं।",
        "cta_btn": "JW Sync खोलें →",
        "index_title": "JW Library बैकअप, सिंक और नोट गाइड | JW Sync",
        "index_desc": "JW Library बैकअप के काम की गाइड: दो डिवाइस के बैकअप मर्ज करना, नए फ़ोन पर नोट ले जाना, Android से iPhone पर जाना, रीस्टोर न होने वाला बैकअप ठीक करना, नोट बदलना और खोजना, और भी बहुत कुछ।",
        "index_h1": "गाइड और तरीके",
        "index_lede": "JW Library बैकअप के बारे में सब कुछ, आसान कदमों में: डिवाइस मर्ज करना, नए फ़ोन पर जाना, नोट बचाना, और जो लाइब्रेरी पहले से है उससे ज़्यादा फ़ायदा उठाना। यहाँ बताया हर टूल आपके ब्राउज़र में मुफ़्त चलता है — आपकी फ़ाइलें कभी अपलोड नहीं होतीं।",
        "index_cta_title": "पढ़ना छोड़िए — सीधे टूल खोलिए",
        "index_cta_body": "दो बैकअप मर्ज करने में करीब एक मिनट लगता है, और ऐप आपको हर कदम बताता है।",
        "footer_all_guides": "सभी गाइड",
        "footer_community": "समुदाय",
        "footer_stats": "अध्ययन आँकड़े",
        "footer_privacy": "JW Sync सारा डेटा आपके ही डिवाइस पर प्रोसेस करता है — आपकी फ़ाइलें कभी बाहर नहीं जातीं। इस्तेमाल मुफ़्त; न खाता, न अपलोड।",
        "footer_disclaimer": "“JW Library” Watch Tower Bible and Tract Society of Pennsylvania की संपत्ति है। JW Sync एक स्वतंत्र सहायक टूल है, जिसका उससे कोई संबंध नहीं है और न ही उसने इसे मान्यता दी है।",
        "groups": {
            "Getting started": "शुरुआत",
            "Sharing scenarios": "साझा करने की स्थितियाँ",
            "Everyday scenarios": "रोज़मर्रा की स्थितियाँ",
            "Fixing problems": "समस्याएँ सुलझाना",
            "Power tools": "उन्नत टूल",
        },
    },
}

# ── Per-guide translations ───────────────────────────────────────────────
# Populated from guides_ar.py so this module stays navigable; the split is
# purely for readability.
from guides_ar import GUIDES_AR  # noqa: E402
from guides_he import GUIDES_HE  # noqa: E402
from guides_uk import GUIDES_UK  # noqa: E402
from guides_pl import GUIDES_PL  # noqa: E402
from guides_zh_hans import GUIDES_ZH_HANS  # noqa: E402
from guides_zh_hant import GUIDES_ZH_HANT  # noqa: E402
from guides_yue_hant import GUIDES_YUE_HANT  # noqa: E402
from guides_vi import GUIDES_VI  # noqa: E402
from guides_hu import GUIDES_HU  # noqa: E402
from guides_hi import GUIDES_HI  # noqa: E402
from guides_id import GUIDES_ID  # noqa: E402
from guides_ro import GUIDES_RO  # noqa: E402
from guides_nl import GUIDES_NL  # noqa: E402
from guides_es import GUIDES_ES  # noqa: E402
from guides_pt import GUIDES_PT  # noqa: E402
from guides_fr import GUIDES_FR  # noqa: E402
from guides_de import GUIDES_DE  # noqa: E402
from guides_it import GUIDES_IT  # noqa: E402
from guides_ru import GUIDES_RU  # noqa: E402
from guides_ja import GUIDES_JA  # noqa: E402
from guides_ko import GUIDES_KO  # noqa: E402
from guides_tl import GUIDES_TL  # noqa: E402
from guides_sv import GUIDES_SV  # noqa: E402
from guides_ceb import GUIDES_CEB  # noqa: E402
from guides_sw import GUIDES_SW  # noqa: E402

GUIDE_TEXT = {
    "ja": GUIDES_JA,
    "ko": GUIDES_KO,
    "tl": GUIDES_TL,
    "sv": GUIDES_SV,
    "ceb": GUIDES_CEB,
    "es": GUIDES_ES,
    "pt": GUIDES_PT,
    "fr": GUIDES_FR,
    "de": GUIDES_DE,
    "it": GUIDES_IT,
    "ru": GUIDES_RU,
    "ar": GUIDES_AR,
    "he": GUIDES_HE,
    "uk": GUIDES_UK,
    "pl": GUIDES_PL,
    "zh-Hans": GUIDES_ZH_HANS,
    "zh-Hant": GUIDES_ZH_HANT,
    "yue-Hant": GUIDES_YUE_HANT,
    "vi": GUIDES_VI,
    "hu": GUIDES_HU,
    "hi": GUIDES_HI,
    "id": GUIDES_ID,
    "ro": GUIDES_RO,
    "nl": GUIDES_NL,
    "sw": GUIDES_SW,
}

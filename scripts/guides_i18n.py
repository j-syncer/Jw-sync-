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
    "ar": {
        "lang_name": "العربية",
        "lang_label": "اللغة",
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
}

# ── Per-guide translations ───────────────────────────────────────────────
# Populated from guides_ar.py so this module stays navigable; the split is
# purely for readability.
from guides_ar import GUIDES_AR  # noqa: E402
from guides_es import GUIDES_ES  # noqa: E402
from guides_pt import GUIDES_PT  # noqa: E402
from guides_fr import GUIDES_FR  # noqa: E402
from guides_de import GUIDES_DE  # noqa: E402
from guides_it import GUIDES_IT  # noqa: E402
from guides_ru import GUIDES_RU  # noqa: E402

GUIDE_TEXT = {
    "es": GUIDES_ES,
    "pt": GUIDES_PT,
    "fr": GUIDES_FR,
    "de": GUIDES_DE,
    "it": GUIDES_IT,
    "ru": GUIDES_RU,
    "ar": GUIDES_AR,
}

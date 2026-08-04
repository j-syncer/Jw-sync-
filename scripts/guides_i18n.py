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

GUIDE_TEXT = {
    "ar": GUIDES_AR,
}

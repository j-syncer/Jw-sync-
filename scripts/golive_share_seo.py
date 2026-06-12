# -*- coding: utf-8 -*-
"""GO LIVE: port the merge-celebration Share card from beta into production,
and complete production's multilingual SEO (add sv + ceb hreflang that prod
was missing, plus og:locale:alternate). Bumps production softwareVersion."""
import io, sys

beta = io.open('beta/index.html', encoding='utf-8').read()
prod = io.open('index.html', encoding='utf-8').read()
orig = prod

def rep(s, old, new, label):
    if s.count(old) != 1:
        print('ABORT [%s]: expected 1, got %d' % (label, s.count(old))); sys.exit(1)
    return s.replace(old, new, 1)

# ── Extract the two big Share-card blocks from beta (verbatim) ──
A = "cele_awards_btn:'I-explore ang mga ganti →'}};"
i = beta.find(A) + len(A)
j = beta.find('\n  function lang()', i)
if i < len(A) or j < 0: print('ABORT: SHARE_I18N extract failed'); sys.exit(1)
SHARE_I18N_BLOCK = beta[i:j]
if 'var SHARE_I18N=' not in SHARE_I18N_BLOCK or 'function ts(' not in SHARE_I18N_BLOCK:
    print('ABORT: SHARE_I18N block looks wrong'); sys.exit(1)

h0 = beta.find('  function shWrap(ctx,text')
h1 = beta.find('  function renderCelebration(opts) {')
if h0 < 0 or h1 < 0 or h0 > h1: print('ABORT: HELPERS extract failed'); sys.exit(1)
HELPERS = beta[h0:h1]
if 'buildMergeCard' not in HELPERS or 'shareMerge' not in HELPERS:
    print('ABORT: HELPERS block looks wrong'); sys.exit(1)
print('extracted SHARE_I18N(%d) + HELPERS(%d)' % (len(SHARE_I18N_BLOCK), len(HELPERS)))

# ── 1) Share card: i18n + helpers + button + wiring (same anchors as beta) ──
prod = rep(prod, A, A + SHARE_I18N_BLOCK, 'SHARE_I18N')
prod = rep(prod, '  function renderCelebration(opts) {',
           HELPERS + '  function renderCelebration(opts) {', 'HELPERS')

DR_OLD = ("          '</button>' +\n"
          "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-restore>' + esc(t('cele_restore')) + ' →</button>' +")
DR_NEW = ("          '</button>' +\n"
          "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-share>"
          "<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\">"
          "<circle cx=\"18\" cy=\"5\" r=\"3\"/><circle cx=\"6\" cy=\"12\" r=\"3\"/><circle cx=\"18\" cy=\"19\" r=\"3\"/>"
          "<line x1=\"8.59\" y1=\"13.51\" x2=\"15.42\" y2=\"17.49\"/><line x1=\"15.41\" y1=\"6.51\" x2=\"8.59\" y2=\"10.49\"/></svg> ' + esc(ts('cele_share')) + '</button>' +\n"
          "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-restore>' + esc(t('cele_restore')) + ' →</button>' +")
prod = rep(prod, DR_OLD, DR_NEW, 'share button')

RB_OLD = ("    var rBtn = ov.querySelector('[data-jwc-restore]');\n"
          "    if (rBtn) rBtn.addEventListener('click', function () { fireAnalytics('post_merge_restore'); openRestoreGuide(); });")
RB_NEW = (RB_OLD + "\n"
          "    var shBtn = ov.querySelector('[data-jwc-share]');\n"
          "    if (shBtn) shBtn.addEventListener('click', function () { fireAnalytics('post_merge_share'); shareMerge(cached && cached.stats); });")
prod = rep(prod, RB_OLD, RB_NEW, 'share wiring')

# ── 2) SEO: add the two missing hreflang langs (sv, ceb) prod lacked ──
TL = '<link rel="alternate" hreflang="tl" href="https://jwsync.org/?lang=tl">'
prod = rep(prod, TL,
           TL + '\n    <link rel="alternate" hreflang="sv" href="https://jwsync.org/?lang=sv">'
              + '\n    <link rel="alternate" hreflang="ceb" href="https://jwsync.org/?lang=ceb">',
           'hreflang sv+ceb')

# ── 3) SEO: og:locale:alternate (prod had none) ──
LOCALE = {'es':'es_ES','pt':'pt_BR','fr':'fr_FR','de':'de_DE','it':'it_IT','ru':'ru_RU',
          'ja':'ja_JP','ko':'ko_KR','tl':'tl_PH','sv':'sv_SE','ceb':'ceb_PH'}
OGL = '<meta property="og:locale" content="en_US">'
og_alts = '\n    ' + '\n    '.join(
    '<meta property="og:locale:alternate" content="%s">' % v for v in LOCALE.values())
prod = rep(prod, OGL, OGL + og_alts, 'og:locale:alternate')

# ── 4) Version bump ──
prod = rep(prod, '"softwareVersion": "2.56.1"', '"softwareVersion": "2.57.0"', 'version')

if prod == orig:
    print('No changes!'); sys.exit(1)
io.open('index.html', 'w', encoding='utf-8').write(prod)
print('GO LIVE applied; production index.html now', len(prod), 'chars')

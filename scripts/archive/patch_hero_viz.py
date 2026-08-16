#!/usr/bin/env python3
"""v2.67.0 — Hero merge visualization (beta).

Replaces the text-only landing hero in beta/index.html with a split hero:
copy on the left, a pure HTML/CSS product visualization on the right —
two .jwlibrary backup files flowing into one merged library card.
Also: new i18n key hero_viz_private (12 languages), softwareVersion bump
in both index.html files, SW CACHE_VERSION bump.
"""
import json, re

# ─────────────────────────────────────────────────────────────────────────────
# 1. beta/index.html — split-hero markup
# ─────────────────────────────────────────────────────────────────────────────
path = 'beta/index.html'
c = open(path, encoding='utf-8').read()

OLD_HERO = '''<div class="landing-hero">
        <h1 data-i18n="hero_title">Merge JW Library backups privately in your browser</h1>
        <p data-i18n="hero_desc">Merge, browse, and edit your JW Library notes, highlights, and bookmarks — entirely in your browser. Your files never leave your device.</p>
      </div>'''
assert c.count(OLD_HERO) == 1, 'hero block anchor not unique'

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>'
ICON_TABLET = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>'
ICON_LAYERS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>'
ICON_LOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>'

NEW_HERO = '''<div class="landing-hero landing-hero-split">
        <div class="lhv-copy">
          <h1 data-i18n="hero_title">Merge JW Library backups privately in your browser</h1>
          <p data-i18n="hero_desc">Merge, browse, and edit your JW Library notes, highlights, and bookmarks — entirely in your browser. Your files never leave your device.</p>
        </div>
        <!-- ── Hero merge visualization (decorative) ── -->
        <div class="lhv" aria-hidden="true">
          <div class="lhv-sources">
            <div class="lhv-file">
              <div class="lhv-file-head">''' + ICON_PHONE + '''<span class="lhv-fname">phone.jwlibrary</span></div>
              <div class="lhv-doc">
                <span class="lhv-hl lhv-c-y" style="width:84%"></span>
                <span class="lhv-hl lhv-c-n" style="width:62%"></span>
                <span class="lhv-hl lhv-c-g" style="width:71%"></span>
                <span class="lhv-hl lhv-c-b" style="width:46%"></span>
              </div>
            </div>
            <div class="lhv-file">
              <div class="lhv-file-head">''' + ICON_TABLET + '''<span class="lhv-fname">tablet.jwlibrary</span></div>
              <div class="lhv-doc">
                <span class="lhv-hl lhv-c-p" style="width:76%"></span>
                <span class="lhv-hl lhv-c-n" style="width:58%"></span>
                <span class="lhv-hl lhv-c-o" style="width:66%"></span>
              </div>
            </div>
          </div>
          <svg class="lhv-flow" viewBox="0 0 56 168" fill="none" preserveAspectRatio="none">
            <path class="lhv-flow-line" d="M0 40 C26 40 26 84 49 84"></path>
            <path class="lhv-flow-line" d="M0 132 C26 132 26 84 49 84"></path>
            <circle class="lhv-flow-node" cx="49.5" cy="84" r="6"></circle>
            <circle class="lhv-flow-core" cx="49.5" cy="84" r="2.5"></circle>
          </svg>
          <div class="lhv-merged">
            <div class="lhv-file-head">''' + ICON_LAYERS + '''<span class="lhv-fname">merged.jwlibrary</span></div>
            <div class="lhv-doc">
              <span class="lhv-hl lhv-c-y" style="width:86%"></span>
              <span class="lhv-hl lhv-c-p" style="width:64%"></span>
              <span class="lhv-hl lhv-c-g" style="width:74%"></span>
              <span class="lhv-hl lhv-c-o" style="width:50%"></span>
              <span class="lhv-hl lhv-c-b" style="width:68%"></span>
            </div>
            <div class="lhv-foot">''' + ICON_LOCK + '''<span data-i18n="hero_viz_private">Never leaves your device</span></div>
          </div>
        </div>
      </div>'''
c = c.replace(OLD_HERO, NEW_HERO)

# ─────────────────────────────────────────────────────────────────────────────
# 2. beta/index.html — scoped CSS (beta-only, so shared styles.css is untouched
#    and production's centered hero keeps working until "go live")
# ─────────────────────────────────────────────────────────────────────────────
CSS = '''<style id="lhv-css">
/* ── Hero merge visualization (v2.67.0, beta-first) ── */
.landing-hero-split{display:flex;flex-direction:column;align-items:center;gap:36px;max-width:960px;width:100%;margin-bottom:18px}
.landing-hero-split .lhv-copy{max-width:640px}
.lhv{display:flex;align-items:center;width:100%;max-width:470px;filter:drop-shadow(0 16px 30px rgba(2,8,23,.4))}
.lhv-sources{flex:1 1 0;display:flex;flex-direction:column;gap:24px;min-width:0}
.lhv-file,.lhv-merged{background:rgba(4,15,34,.7);border:1px solid rgba(71,85,105,.45);border-radius:12px;padding:12px 14px}
.lhv-merged{flex:1.18 1 0;min-width:0;background:rgba(7,18,38,.88);border-color:rgba(234,88,12,.45);box-shadow:0 0 0 1px rgba(234,88,12,.07)}
.lhv-file-head{display:flex;align-items:center;gap:7px;margin-bottom:10px}
.lhv-file-head svg{width:14px;height:14px;color:rgba(148,163,184,.9);flex:none}
.lhv-merged .lhv-file-head svg{color:#ea580c}
.lhv-fname{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:10.5px;color:rgba(203,213,225,.85);letter-spacing:.2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lhv-merged .lhv-fname{color:#f1f5f9;font-weight:600}
.lhv-doc{display:flex;flex-direction:column;gap:6px}
.lhv-hl{display:block;height:6px;border-radius:3px}
.lhv-merged .lhv-hl{height:7px}
.lhv-c-n{background:rgba(100,116,139,.38)}
.lhv-c-y{background:rgba(250,204,21,.8)}
.lhv-c-g{background:rgba(74,222,128,.75)}
.lhv-c-b{background:rgba(96,165,250,.75)}
.lhv-c-p{background:rgba(244,114,182,.75)}
.lhv-c-o{background:rgba(251,146,60,.8)}
.lhv-flow{flex:0 0 52px;width:52px;align-self:stretch;height:auto;min-height:150px}
.lhv-flow-line{stroke:rgba(100,116,139,.55);stroke-width:1.6;stroke-dasharray:1 6;stroke-linecap:round;fill:none}
.lhv-flow-node{fill:rgba(234,88,12,.22)}
.lhv-flow-core{fill:#ea580c}
.lhv-foot{display:flex;align-items:center;gap:6px;margin-top:11px;padding-top:10px;border-top:1px solid rgba(71,85,105,.35)}
.lhv-foot svg{width:11px;height:11px;color:rgba(52,211,153,.9);flex:none}
.lhv-foot span{font-size:10.5px;color:rgba(148,163,184,.9);line-height:1.35}
@media (min-width:880px){
.landing-hero-split{flex-direction:row;align-items:center;text-align:left;gap:56px;margin-bottom:28px}
.landing-hero-split .lhv-copy{flex:1 1 0;max-width:none}
.landing-hero-split .lhv-copy p{max-width:460px}
.lhv{flex:0 0 440px;max-width:440px}
}
@media (max-width:420px){
.lhv-flow{flex-basis:38px;width:38px}
.lhv-file,.lhv-merged{padding:10px 11px}
.lhv-file-head{gap:5px}
.lhv-fname{font-size:9px}
}
body.light .lhv{filter:drop-shadow(0 14px 26px rgba(11,46,88,.14))}
body.light .lhv-file,body.light .lhv-merged{background:#fff;border-color:rgba(11,46,88,.14)}
body.light .lhv-merged{border-color:rgba(234,88,12,.4);box-shadow:0 0 0 1px rgba(234,88,12,.06)}
body.light .lhv-fname{color:rgba(51,65,85,.9)}
body.light .lhv-merged .lhv-fname{color:#071a38}
body.light .lhv-c-n{background:rgba(100,116,139,.25)}
body.light .lhv-flow-line{stroke:rgba(11,46,88,.3)}
body.light .lhv-flow-node{fill:rgba(234,88,12,.15)}
body.light .lhv-foot{border-top-color:rgba(11,46,88,.1)}
body.light .lhv-foot svg{color:#059669}
body.light .lhv-foot span{color:rgba(71,85,105,.9)}
</style>
'''
LV_ANCHOR = '<section id="landing-view" style="display:none">'
assert c.count(LV_ANCHOR) == 1, 'landing-view anchor not unique'
c = c.replace(LV_ANCHOR, CSS + '    ' + LV_ANCHOR)

# ─────────────────────────────────────────────────────────────────────────────
# 3. beta/index.html — i18n key hero_viz_private in all 12 languages
# ─────────────────────────────────────────────────────────────────────────────
TR = {
    'en': 'Never leaves your device',
    'es': 'Nunca sale de tu dispositivo',
    'pt': 'Nunca sai do seu dispositivo',
    'fr': 'Ne quitte jamais votre appareil',
    'de': 'Verlässt nie dein Gerät',
    'it': 'Non lascia mai il tuo dispositivo',
    'ru': 'Никогда не покидает ваше устройство',
    'ja': 'デバイスから出ることはありません',
    'ko': '기기를 벗어나지 않습니다',
    'tl': 'Hindi umaalis sa iyong device',
    'sv': 'Lämnar aldrig din enhet',
    'ceb': 'Dili mobiya sa imong device',
}
m = re.search(r'__JW_LANDING_I18N *= *', c)
ts = m.end(); d = 0; e = None
for i in range(ts, len(c)):
    if c[i] == '{':
        d += 1
    elif c[i] == '}':
        d -= 1
        if d == 0:
            e = i + 1
            break
obj = json.loads(c[ts:e])
assert set(obj.keys()) == set(TR.keys()), 'language set mismatch: %s' % sorted(obj.keys())
for lang, text in TR.items():
    obj[lang]['hero_viz_private'] = text
c = c[:ts] + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + c[e:]

# ─────────────────────────────────────────────────────────────────────────────
# 4. Version bumps
# ─────────────────────────────────────────────────────────────────────────────
assert c.count('"softwareVersion": "2.66.0"') == 1
c = c.replace('"softwareVersion": "2.66.0"', '"softwareVersion": "2.67.0"')
open(path, 'w', encoding='utf-8').write(c)
print('beta/index.html patched')

p = open('index.html', encoding='utf-8').read()
assert p.count('"softwareVersion": "2.66.0"') == 1
p = p.replace('"softwareVersion": "2.66.0"', '"softwareVersion": "2.67.0"')
open('index.html', 'w', encoding='utf-8').write(p)
print('index.html softwareVersion bumped')

sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v108';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v108';", "const CACHE_VERSION = 'jwsync-v109';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js CACHE_VERSION -> v109')
print('done')

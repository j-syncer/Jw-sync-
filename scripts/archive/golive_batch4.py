#!/usr/bin/env python3
import sys
path = '/home/user/Jw-sync-/highlights.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
errors = []
def R(old, new, label=''):
    global content
    c = content.count(old)
    if c != 1:
        errors.append('ERROR "%s": %d' % (label or old[:60], c))
        return
    content = content.replace(old, new, 1)
    print('OK:', label or old[:60])

# ── CSS ──────────────────────────────────────────────────────────────
new_css = (
    # AP badge (position:relative on disc enables absolute badge)
    "    .jww-medal-disc{position:relative}\n"
    "    .jww-ap{position:absolute;bottom:-3px;right:-5px;font-size:8.5px;font-weight:800;"
    "color:#0b1220;background:var(--tc,#fbbf24);border-radius:7px;padding:1px 4px;line-height:1.4;"
    "pointer-events:none;white-space:nowrap}\n"
    # Shape clip-paths on medal disc
    "    .jww-shape-heart .jww-medal-disc{clip-path:polygon(50% 100%,15% 60%,0% 35%,15% 10%,"
    "38% 0%,50% 12%,62% 0%,85% 10%,100% 35%,85% 60%);border-radius:0}\n"
    "    .jww-shape-shield .jww-medal-disc{clip-path:polygon(0% 0%,100% 0%,100% 65%,50% 100%,"
    "0% 65%);border-radius:0}\n"
    "    .jww-shape-star .jww-medal-disc{clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,"
    "79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);border-radius:0}\n"
    "    .jww-shape-diamond .jww-medal-disc{clip-path:polygon(50% 0%,100% 50%,50% 100%,"
    "0% 50%);border-radius:0}\n"
    "    .jww-shape-crown .jww-medal-disc{clip-path:polygon(0% 100%,0% 55%,20% 20%,30% 55%,"
    "50% 15%,70% 55%,80% 20%,100% 55%,100% 100%);border-radius:0}\n"
    "    .jww-shape-scroll .jww-medal-disc{border-radius:6px}\n"
    "    .jww-shape-tear .jww-medal-disc{border-radius:50% 50% 48% 48% / 38% 38% 58% 58%}\n"
    # Distinguished Honors cabinet
    "    .jww-cabinet{margin:14px 0 4px;padding:12px 14px;background:rgba(251,191,36,.07);"
    "border:1px solid rgba(251,191,36,.25);border-radius:12px}\n"
    "    .jww-cab-hd{display:flex;align-items:center;gap:7px;font-size:11.5px;font-weight:700;"
    "color:#fbbf24;margin-bottom:10px;letter-spacing:.02em;text-transform:uppercase}\n"
    "    .jww-cab-hd svg{width:13px;height:13px;color:#fbbf24;flex-shrink:0}\n"
    "    .jww-cab-row{display:flex;flex-wrap:wrap;gap:10px}\n"
    "    .jww-cab-medal{cursor:pointer;transition:transform .15s}\n"
    "    .jww-cab-medal:hover{transform:scale(1.1)}\n"
    "    .jww-cab-disc{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;"
    "justify-content:center;background:radial-gradient(circle at 33% 27%,#fff,var(--mc,#fbbf24) 52%,"
    "var(--mc2,#d97706) 100%);color:#0b1220;box-shadow:0 4px 12px -4px var(--mc2,#d97706),"
    "0 0 12px -4px var(--mc,#fbbf24)}\n"
    "    .jww-cab-disc svg{width:20px;height:20px}\n"
    "    .jww-shape-heart .jww-cab-disc{clip-path:polygon(50% 100%,15% 60%,0% 35%,15% 10%,"
    "38% 0%,50% 12%,62% 0%,85% 10%,100% 35%,85% 60%);border-radius:0}\n"
    "    .jww-shape-shield .jww-cab-disc{clip-path:polygon(0% 0%,100% 0%,100% 65%,50% 100%,"
    "0% 65%);border-radius:0}\n"
    "    .jww-shape-star .jww-cab-disc{clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,"
    "79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);border-radius:0}\n"
    "    .jww-shape-diamond .jww-cab-disc{clip-path:polygon(50% 0%,100% 50%,50% 100%,"
    "0% 50%);border-radius:0}\n"
    "    .jww-shape-crown .jww-cab-disc{clip-path:polygon(0% 100%,0% 55%,20% 20%,30% 55%,"
    "50% 15%,70% 55%,80% 20%,100% 55%,100% 100%);border-radius:0}\n"
    "    .jww-shape-scroll .jww-cab-disc{border-radius:6px}\n"
    "    .jww-shape-tear .jww-cab-disc{border-radius:50% 50% 48% 48% / 38% 38% 58% 58%}\n"
    # Medal popup overlay
    "    .jww-mp-ov{position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:9999;"
    "display:flex;align-items:center;justify-content:center;padding:20px}\n"
    "    .jww-mp-box{position:relative;background:#0f172a;border:1px solid rgba(251,191,36,.3);"
    "border-radius:18px;padding:24px 22px;max-width:300px;width:100%;text-align:center;"
    "box-shadow:0 20px 60px rgba(0,0,0,.75)}\n"
    "    .jww-mp-close{position:absolute;top:10px;right:14px;background:none;border:none;"
    "color:#64748b;font-size:22px;cursor:pointer;padding:0;line-height:1;font-family:inherit}\n"
    "    .jww-mp-close:hover{color:#e2e8f0}\n"
    "    .jww-mp-disc{width:64px;height:64px;border-radius:50%;margin:0 auto 14px;display:flex;"
    "align-items:center;justify-content:center;background:radial-gradient(circle at 34% 30%,"
    "#1a2333,#0b1220 72%);color:#334155}\n"
    "    .jww-mp-disc.jww-medal-on{background:radial-gradient(circle at 33% 27%,#fff,"
    "var(--mc,#fbbf24) 52%,var(--mc2,#d97706) 100%);color:#0b1220;box-shadow:0 7px 20px -6px "
    "var(--mc2,#d97706),0 0 20px -5px var(--mc,#fbbf24)}\n"
    "    .jww-mp-disc svg{width:28px;height:28px}\n"
    "    .jww-mp-name{font-size:16px;font-weight:800;color:#e2e8f0;margin-bottom:8px}\n"
    "    .jww-mp-desc{font-size:13px;color:#94a3b8;line-height:1.55;margin-bottom:10px}\n"
    "    .jww-mp-ap{display:flex;align-items:center;justify-content:center;gap:6px;"
    "font-size:13px;font-weight:700;color:#fbbf24;margin-top:6px}\n"
    "    .jww-mp-ap svg{width:14px;height:14px}\n"
    "    .jww-mp-prog{margin:8px 0;padding:0 10px}\n"
    "    .jww-mp-prog-track{height:6px;border-radius:4px;background:rgba(148,163,184,.2);overflow:hidden}\n"
    "    .jww-mp-prog-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,"
    "var(--mc,#fb923c),var(--mc2,#ea580c))}\n"
    "    .jww-mp-prog-lbl{font-size:11px;color:#64748b;margin-top:4px;font-variant-numeric:tabular-nums}\n"
)

R(
    '    @media (max-width:520px){.jww-ins{grid-template-columns:repeat(2,1fr)}.jww-ach-grid{grid-template-columns:repeat(3,1fr)}.jww-journey{gap:16px}}\n'
    '    .jww-wc-sub',
    '    @media (max-width:520px){.jww-ins{grid-template-columns:repeat(2,1fr)}.jww-ach-grid{grid-template-columns:repeat(3,1fr)}.jww-journey{gap:16px}}\n'
    + new_css
    + '    .jww-wc-sub',
    'shapes + AP + cabinet + popup CSS'
)

# ── I18N keys (English only; other langs fall back) ───────────────────
new_i18n = (
    # Achievement names for keyword awards
    ",cabinet_title:'Distinguished Honors'"
    ",ach_kw_love1:'First Love'"
    ",ach_kw_love2:'Heart of Love'"
    ",ach_kw_love3:'Love Overflows'"
    ",ach_kw_love4:'Boundless Love'"
    ",ach_kw_faith1:'First Faith'"
    ",ach_kw_faith2:'Growing Faith'"
    ",ach_kw_faith3:'Unshakeable Faith'"
    ",ach_kw_hope1:'Hopeful Heart'"
    ",ach_kw_hope2:'Living Hope'"
    ",ach_kw_proph1:\"Prophet's Eye\""
    ",ach_kw_proph2:'Prophetic Voice'"
    ",ach_kw_proph3:'Seer of the Ages'"
    ",ach_kw_wisd1:'Seeking Wisdom'"
    ",ach_kw_wisd2:'Wisdom Keeper'"
    ",ach_kw_grace1:'Finding Grace'"
    ",ach_kw_grace2:'Vessel of Grace'"
    ",ach_kw_king1:'Kingdom Minded'"
    ",ach_kw_king2:'Kingdom Builder'"
    ",ach_kw_king3:'Kingdom Ambassador'"
    ",ach_kw_pray1:'First Prayer'"
    ",ach_kw_pray2:'Prayer Life'"
    ",ach_kw_pray3:'Prayer Warrior'"
    ",ach_kw_peace:'Seeker of Peace'"
    ",ach_kw_joy:'Full of Joy'"
    ",ach_kw_cov:'Covenant Mind'"
    ",ach_kw_truth:'Truth Seeker'"
    # Standard achievement descriptions
    ",dk_firstnote:'Write your first note in JW Library'"
    ",dk_firsthl:'Highlight your first verse'"
    ",dk_firstbm:'Add your first bookmark'"
    ",dk_firsttag:'Create your first tag'"
    ",dk_firstbook:'Study a verse in your first Bible book'"
    ",dk_deep100:'Write a note of 100 or more words'"
    ",dk_deep300:'Write a note of 300 or more words'"
    ",dk_treatise:'Write a single note of 1,000 or more words'"
    ",dk_scholar:'Reach an average note length of 100+ words'"
    ",dk_bigday:'Write 50 or more notes in a single day'"
    ",dk_polymath:'Write notes across 10 or more publications'"
    ",dk_nightowl:'Write 30 or more notes between midnight and 3 am'"
    ",dk_devoted:'Maintain a study streak of 730 or more days'"
    ",dk_torah:'Write notes in all five books of the Torah'"
    ",dk_historical:'Write notes in all twelve Historical Books'"
    ",dk_wisdom_books:'Write notes in all five Books of Wisdom'"
    ",dk_majorproph:'Write notes in all five Major Prophets'"
    ",dk_minorproph:'Write notes in all twelve Minor Prophets'"
    ",dk_whole_ot:'Write notes in all 39 books of the Hebrew Scriptures'"
    ",dk_gospels:'Write notes in all four Gospels'"
    ",dk_acts:'Write notes in Acts of the Apostles'"
    ",dk_pauline:'Write notes in all thirteen Pauline Letters'"
    ",dk_generalep:'Write notes in all eight General Letters'"
    ",dk_revelation:'Write notes in the book of Revelation'"
    ",dk_whole_nt:'Write notes in all 27 books of the Greek Scriptures'"
    ",dk_wholebible:'Write notes in all 66 books of the Bible'"
    # Keyword achievement descriptions
    ",dk_kw_love1:\"The word \\'love\\' appears in at least one of your notes\""
    ",dk_kw_love2:\"The word \\'love\\' appears in 10 or more of your notes\""
    ",dk_kw_love3:\"The word \\'love\\' appears in 30 or more of your notes\""
    ",dk_kw_love4:\"The word \\'love\\' appears in 75 or more of your notes\""
    ",dk_kw_faith1:\"The word \\'faith\\' appears in at least one of your notes\""
    ",dk_kw_faith2:\"The word \\'faith\\' appears in 15 or more of your notes\""
    ",dk_kw_faith3:\"The word \\'faith\\' appears in 40 or more of your notes\""
    ",dk_kw_hope1:\"The word \\'hope\\' appears in 5 or more of your notes\""
    ",dk_kw_hope2:\"The word \\'hope\\' appears in 25 or more of your notes\""
    ",dk_kw_proph1:\"The word \\'prophecy\\' appears in 3 or more of your notes\""
    ",dk_kw_proph2:\"The word \\'prophecy\\' appears in 15 or more of your notes\""
    ",dk_kw_proph3:\"The word \\'prophecy\\' appears in 40 or more of your notes\""
    ",dk_kw_wisd1:\"The word \\'wisdom\\' appears in 5 or more of your notes\""
    ",dk_kw_wisd2:\"The word \\'wisdom\\' appears in 20 or more of your notes\""
    ",dk_kw_grace1:\"The word \\'grace\\' appears in 3 or more of your notes\""
    ",dk_kw_grace2:\"The word \\'grace\\' appears in 20 or more of your notes\""
    ",dk_kw_king1:\"The word \\'kingdom\\' appears in 5 or more of your notes\""
    ",dk_kw_king2:\"The word \\'kingdom\\' appears in 25 or more of your notes\""
    ",dk_kw_king3:\"The word \\'kingdom\\' appears in 60 or more of your notes\""
    ",dk_kw_pray1:\"The word \\'prayer\\' appears in 3 or more of your notes\""
    ",dk_kw_pray2:\"The word \\'prayer\\' appears in 20 or more of your notes\""
    ",dk_kw_pray3:\"The word \\'prayer\\' appears in 50 or more of your notes\""
    ",dk_kw_peace:\"The word \\'peace\\' appears in 5 or more of your notes\""
    ",dk_kw_joy:\"The word \\'joy\\' appears in 5 or more of your notes\""
    ",dk_kw_cov:\"The word \\'covenant\\' appears in 10 or more of your notes\""
    ",dk_kw_truth:\"The word \\'truth\\' appears in 10 or more of your notes\""
)

R(
    'ach_intro:"Earn awards by studying — add notes, highlight verses, explore more Bible books and keep your streak going. Rarer awards grant more Appreciation. Tap a tier to open it, and use the filters to see what\'s left to unlock."},',
    'ach_intro:"Earn awards by studying — add notes, highlight verses, explore more Bible books and keep your streak going. Rarer awards grant more Appreciation. Tap a tier to open it, and use the filters to see what\'s left to unlock."' + new_i18n + '},',
    'English I18N keys'
)

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Batch 4 OK')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

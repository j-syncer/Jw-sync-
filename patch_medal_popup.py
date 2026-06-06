#!/usr/bin/env python3
import sys

path = '/home/user/Jw-sync-/beta/highlights.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

errors = []

def replace_once(old, new, label=''):
    global content
    c = content.count(old)
    if c != 1:
        errors.append(f'ERROR: anchor "{label or old[:80]}" appears {c} times, expected 1')
        return
    content = content.replace(old, new, 1)
    print(f'OK: {label or old[:80]}')

# ── 1. Add dk to add() function ──────────────────────────────────────────────
replace_once(
    'shape: o.shape || null });',
    'shape: o.shape || null, dk: o.dk || null });',
    'add() dk property'
)

# ── 2. Add module-level cache vars before buildAchievements ──────────────────
replace_once(
    'function buildAchievements(s){',
    'var __achCache = null, __curTCache = 0;\n      function buildAchievements(s){',
    'module cache vars'
)

# ── 3. Set cache vars in achievementsHtml after curT is defined ──────────────
replace_once(
    'var loc = getLang(), curT = journeyData(s).tierIdx;',
    'var loc = getLang(), curT = journeyData(s).tierIdx; __achCache = A; __curTCache = curT;',
    'set cache in achievementsHtml'
)

# ── 4. Add data-seq to medal rendering ───────────────────────────────────────
replace_once(
    "body += '<div class=\"' + cls + '\" data-state=\"'",
    "body += '<div class=\"' + cls + '\" data-seq=\"' + a.seq + '\" data-state=\"'",
    'data-seq medal'
)

# ── 5. Add data-seq to cabinet item ──────────────────────────────────────────
replace_once(
    "rows+='<div class=\"jww-cab-item'+(on?' jww-cab-on':'')+' jww-cab-r'+a.rarity+'\">';",
    "rows+='<div class=\"jww-cab-item'+(on?' jww-cab-on':'')+' jww-cab-r'+a.rarity+'\" data-seq=\"'+a.seq+'\">';",
    'data-seq cabinet'
)

# ── 6. Add dk to specific achievements (non-keyword) ─────────────────────────
replace_once(
    "add(0, notes >= 1, IC.note, t('ach_firstnote'));",
    "add(0, notes >= 1, IC.note, t('ach_firstnote'), {dk:'dk_firstnote'});",
    'dk firstnote'
)
replace_once(
    "add(0, hl >= 1, IC.highlight, t('ach_firsthl'));",
    "add(0, hl >= 1, IC.highlight, t('ach_firsthl'), {dk:'dk_firsthl'});",
    'dk firsthl'
)
replace_once(
    "add(0, bm >= 1, IC.bookmark, t('ach_firstbm'));",
    "add(0, bm >= 1, IC.bookmark, t('ach_firstbm'), {dk:'dk_firstbm'});",
    'dk firstbm'
)
replace_once(
    "add(0, tags >= 1, IC.tag, t('ach_firsttag'));",
    "add(0, tags >= 1, IC.tag, t('ach_firsttag'), {dk:'dk_firsttag'});",
    'dk firsttag'
)
replace_once(
    "add(0, books >= 1, IC.book, t('ach_firstbook'));",
    "add(0, books >= 1, IC.book, t('ach_firstbook'), {dk:'dk_firstbook'});",
    'dk firstbook'
)

# Note depth achievements
replace_once(
    "add(1, longest >= 100, IC.pen, t('ach_deep100'));",
    "add(1, longest >= 100, IC.pen, t('ach_deep100'), {dk:'dk_deep100'});",
    'dk deep100'
)
replace_once(
    "add(3, longest >= 300, IC.pen, t('ach_deep300'));",
    "add(3, longest >= 300, IC.pen, t('ach_deep300'), {dk:'dk_deep300'});",
    'dk deep300'
)

# Secret achievements
replace_once(
    "add(10, longest >= 1000, IC.pen, t('ach_treatise'), { secret: true });",
    "add(10, longest >= 1000, IC.pen, t('ach_treatise'), { secret: true, dk:'dk_treatise' });",
    'dk treatise'
)
replace_once(
    "add(6, avg >= 100, IC.pen, t('ach_scholar'), { secret: true });",
    "add(6, avg >= 100, IC.pen, t('ach_scholar'), { secret: true, dk:'dk_scholar' });",
    'dk scholar'
)
replace_once(
    "add(7, maxDay >= 50, IC.flame, t('ach_bigday'), { secret: true });",
    "add(7, maxDay >= 50, IC.flame, t('ach_bigday'), { secret: true, dk:'dk_bigday' });",
    'dk bigday'
)
replace_once(
    "add(6, pubCount >= 10, IC.layers, t('ach_polymath'), { secret: true });",
    "add(6, pubCount >= 10, IC.layers, t('ach_polymath'), { secret: true, dk:'dk_polymath' });",
    'dk polymath'
)
replace_once(
    "add(4, lateN >= 30, IC.clock, t('ach_nightowl'), { secret: true });",
    "add(4, lateN >= 30, IC.clock, t('ach_nightowl'), { secret: true, dk:'dk_nightowl' });",
    'dk nightowl'
)
replace_once(
    "add(11, (st.longest || 0) >= 730, IC.flame, t('ach_devoted'), { secret: true });",
    "add(11, (st.longest || 0) >= 730, IC.flame, t('ach_devoted'), { secret: true, dk:'dk_devoted' });",
    'dk devoted'
)

# Bible section achievements
replace_once(
    "add(2, allBooks(s, 1, 5), IC.book, t('ach_torah'));",
    "add(2, allBooks(s, 1, 5), IC.book, t('ach_torah'), {dk:'dk_torah'});",
    'dk torah'
)
replace_once(
    "add(3, allBooks(s, 6, 17), IC.book, t('ach_historical'));",
    "add(3, allBooks(s, 6, 17), IC.book, t('ach_historical'), {dk:'dk_historical'});",
    'dk historical'
)
replace_once(
    "add(3, allBooks(s, 18, 22), IC.book, t('ach_wisdom'));",
    "add(3, allBooks(s, 18, 22), IC.book, t('ach_wisdom'), {dk:'dk_wisdom_books'});",
    'dk wisdom_books'
)
replace_once(
    "add(4, allBooks(s, 23, 27), IC.book, t('ach_majorproph'));",
    "add(4, allBooks(s, 23, 27), IC.book, t('ach_majorproph'), {dk:'dk_majorproph'});",
    'dk majorproph'
)
replace_once(
    "add(5, allBooks(s, 28, 39), IC.book, t('ach_minorproph'));",
    "add(5, allBooks(s, 28, 39), IC.book, t('ach_minorproph'), {dk:'dk_minorproph'});",
    'dk minorproph'
)
replace_once(
    "add(6, distinctBooks(s, 1, 39) >= 39, IC.book, t('ach_whole_ot'), { rv: 3 });",
    "add(6, distinctBooks(s, 1, 39) >= 39, IC.book, t('ach_whole_ot'), { rv: 3, dk:'dk_whole_ot' });",
    'dk whole_ot'
)
replace_once(
    "add(2, allBooks(s, 40, 43), IC.book, t('ach_gospels'));",
    "add(2, allBooks(s, 40, 43), IC.book, t('ach_gospels'), {dk:'dk_gospels'});",
    'dk gospels'
)
replace_once(
    "add(3, bk(44), IC.book, t('ach_acts'));",
    "add(3, bk(44), IC.book, t('ach_acts'), {dk:'dk_acts'});",
    'dk acts'
)
replace_once(
    "add(4, allBooks(s, 45, 57), IC.book, t('ach_pauline'));",
    "add(4, allBooks(s, 45, 57), IC.book, t('ach_pauline'), {dk:'dk_pauline'});",
    'dk pauline'
)
replace_once(
    "add(5, allBooks(s, 58, 65), IC.book, t('ach_generalep'));",
    "add(5, allBooks(s, 58, 65), IC.book, t('ach_generalep'), {dk:'dk_generalep'});",
    'dk generalep'
)
replace_once(
    "add(5, bk(66), IC.book, t('ach_revelation'));",
    "add(5, bk(66), IC.book, t('ach_revelation'), {dk:'dk_revelation'});",
    'dk revelation'
)
replace_once(
    "add(7, distinctBooks(s, 40, 66) >= 27, IC.book, t('ach_whole_nt'), { rv: 3 });",
    "add(7, distinctBooks(s, 40, 66) >= 27, IC.book, t('ach_whole_nt'), { rv: 3, dk:'dk_whole_nt' });",
    'dk whole_nt'
)
replace_once(
    "add(9, books >= 66, IC.trophy, t('ach_wholebible'), { rv: 4 });",
    "add(9, books >= 66, IC.trophy, t('ach_wholebible'), { rv: 4, dk:'dk_wholebible' });",
    'dk wholebible'
)

# ── 7. Replace keyword achievement block with dk-annotated version ────────────
old_kw = """      // ── Content keyword achievements ───────────────────────────────────────
      var kw = s.kwHits || {};
      // Way of Love (heart shape)
      add(0, (kw.love||0)>=1, IC.heart, t('ach_kw_love1'), {shape:'heart',rv:0});
      add(2, (kw.love||0)>=10, IC.heart, t('ach_kw_love2'), {shape:'heart',rv:1,cur:Math.min(kw.love||0,10),tgt:10});
      add(4, (kw.love||0)>=30, IC.heart, t('ach_kw_love3'), {shape:'heart',rv:2,cur:Math.min(kw.love||0,30),tgt:30});
      add(6, (kw.love||0)>=75, IC.heart, t('ach_kw_love4'), {shape:'heart',rv:3,secret:true,cur:Math.min(kw.love||0,75),tgt:75});
      // Living Faith (shield shape)
      add(1, (kw.faith||0)>=1, IC.shield, t('ach_kw_faith1'), {shape:'shield',rv:0});
      add(3, (kw.faith||0)>=15, IC.shield, t('ach_kw_faith2'), {shape:'shield',rv:1,cur:Math.min(kw.faith||0,15),tgt:15});
      add(5, (kw.faith||0)>=40, IC.shield, t('ach_kw_faith3'), {shape:'shield',rv:2,secret:true,cur:Math.min(kw.faith||0,40),tgt:40});
      // Blessed Hope (star shape)
      add(1, (kw.hope||0)>=5, IC.star5, t('ach_kw_hope1'), {shape:'star',rv:1,cur:Math.min(kw.hope||0,5),tgt:5});
      add(5, (kw.hope||0)>=25, IC.star5, t('ach_kw_hope2'), {shape:'star',rv:2,secret:true,cur:Math.min(kw.hope||0,25),tgt:25});
      // Prophetic Voice (diamond shape)
      add(2, (kw.prophecy||0)>=3, IC.eye2, t('ach_kw_proph1'), {shape:'diamond',rv:1,cur:Math.min(kw.prophecy||0,3),tgt:3});
      add(5, (kw.prophecy||0)>=15, IC.eye2, t('ach_kw_proph2'), {shape:'diamond',rv:2,cur:Math.min(kw.prophecy||0,15),tgt:15});
      add(7, (kw.prophecy||0)>=40, IC.eye2, t('ach_kw_proph3'), {shape:'diamond',rv:3,secret:true,cur:Math.min(kw.prophecy||0,40),tgt:40});
      // Voice of Wisdom (scroll/octagon shape)
      add(2, (kw.wisdom||0)>=5, IC.scroll2, t('ach_kw_wisd1'), {shape:'scroll',rv:1,cur:Math.min(kw.wisdom||0,5),tgt:5});
      add(5, (kw.wisdom||0)>=20, IC.scroll2, t('ach_kw_wisd2'), {shape:'scroll',rv:3,secret:true,cur:Math.min(kw.wisdom||0,20),tgt:20});
      // Amazing Grace (dove icon, shield shape)
      add(2, (kw.grace||0)>=3, IC.dove2, t('ach_kw_grace1'), {shape:'shield',rv:1,cur:Math.min(kw.grace||0,3),tgt:3});
      add(5, (kw.grace||0)>=20, IC.dove2, t('ach_kw_grace2'), {shape:'shield',rv:3,secret:true,cur:Math.min(kw.grace||0,20),tgt:20});
      // Kingdom Seeker (crown shape)
      add(2, (kw.kingdom||0)>=5, IC.crown2, t('ach_kw_king1'), {shape:'crown',rv:0,cur:Math.min(kw.kingdom||0,5),tgt:5});
      add(5, (kw.kingdom||0)>=25, IC.crown2, t('ach_kw_king2'), {shape:'crown',rv:1,cur:Math.min(kw.kingdom||0,25),tgt:25});
      add(7, (kw.kingdom||0)>=60, IC.crown2, t('ach_kw_king3'), {shape:'crown',rv:3,secret:true,cur:Math.min(kw.kingdom||0,60),tgt:60});
      // Prayer Devotion (lamp icon, star shape)
      add(1, (kw.pray||0)>=3, IC.lamp2, t('ach_kw_pray1'), {shape:'tear',rv:0,cur:Math.min(kw.pray||0,3),tgt:3});
      add(4, (kw.pray||0)>=20, IC.lamp2, t('ach_kw_pray2'), {shape:'tear',rv:1,cur:Math.min(kw.pray||0,20),tgt:20});
      add(7, (kw.pray||0)>=50, IC.lamp2, t('ach_kw_pray3'), {shape:'tear',rv:3,secret:true,cur:Math.min(kw.pray||0,50),tgt:50});
      // Peace & Joy
      add(2, (kw.peace||0)>=5, IC.spark, t('ach_kw_peace'), {rv:1,cur:Math.min(kw.peace||0,5),tgt:5});
      add(2, (kw.joy||0)>=5, IC.spark, t('ach_kw_joy'), {rv:1,cur:Math.min(kw.joy||0,5),tgt:5});
      // Covenant & Truth
      add(3, (kw.covenant||0)>=10, IC.note, t('ach_kw_cov'), {rv:1,cur:Math.min(kw.covenant||0,10),tgt:10});
      add(3, (kw.truth||0)>=10, IC.note, t('ach_kw_truth'), {rv:1,cur:Math.min(kw.truth||0,10),tgt:10});"""

new_kw = """      // ── Content keyword achievements ───────────────────────────────────────
      var kw = s.kwHits || {};
      // Way of Love (heart shape)
      add(0, (kw.love||0)>=1, IC.heart, t('ach_kw_love1'), {shape:'heart',rv:0,dk:'dk_kw_love1'});
      add(2, (kw.love||0)>=10, IC.heart, t('ach_kw_love2'), {shape:'heart',rv:1,cur:Math.min(kw.love||0,10),tgt:10,dk:'dk_kw_love2'});
      add(4, (kw.love||0)>=30, IC.heart, t('ach_kw_love3'), {shape:'heart',rv:2,cur:Math.min(kw.love||0,30),tgt:30,dk:'dk_kw_love3'});
      add(6, (kw.love||0)>=75, IC.heart, t('ach_kw_love4'), {shape:'heart',rv:3,secret:true,cur:Math.min(kw.love||0,75),tgt:75,dk:'dk_kw_love4'});
      // Living Faith (shield shape)
      add(1, (kw.faith||0)>=1, IC.shield, t('ach_kw_faith1'), {shape:'shield',rv:0,dk:'dk_kw_faith1'});
      add(3, (kw.faith||0)>=15, IC.shield, t('ach_kw_faith2'), {shape:'shield',rv:1,cur:Math.min(kw.faith||0,15),tgt:15,dk:'dk_kw_faith2'});
      add(5, (kw.faith||0)>=40, IC.shield, t('ach_kw_faith3'), {shape:'shield',rv:2,secret:true,cur:Math.min(kw.faith||0,40),tgt:40,dk:'dk_kw_faith3'});
      // Blessed Hope (star shape)
      add(1, (kw.hope||0)>=5, IC.star5, t('ach_kw_hope1'), {shape:'star',rv:1,cur:Math.min(kw.hope||0,5),tgt:5,dk:'dk_kw_hope1'});
      add(5, (kw.hope||0)>=25, IC.star5, t('ach_kw_hope2'), {shape:'star',rv:2,secret:true,cur:Math.min(kw.hope||0,25),tgt:25,dk:'dk_kw_hope2'});
      // Prophetic Voice (diamond shape)
      add(2, (kw.prophecy||0)>=3, IC.eye2, t('ach_kw_proph1'), {shape:'diamond',rv:1,cur:Math.min(kw.prophecy||0,3),tgt:3,dk:'dk_kw_proph1'});
      add(5, (kw.prophecy||0)>=15, IC.eye2, t('ach_kw_proph2'), {shape:'diamond',rv:2,cur:Math.min(kw.prophecy||0,15),tgt:15,dk:'dk_kw_proph2'});
      add(7, (kw.prophecy||0)>=40, IC.eye2, t('ach_kw_proph3'), {shape:'diamond',rv:3,secret:true,cur:Math.min(kw.prophecy||0,40),tgt:40,dk:'dk_kw_proph3'});
      // Voice of Wisdom (scroll/octagon shape)
      add(2, (kw.wisdom||0)>=5, IC.scroll2, t('ach_kw_wisd1'), {shape:'scroll',rv:1,cur:Math.min(kw.wisdom||0,5),tgt:5,dk:'dk_kw_wisd1'});
      add(5, (kw.wisdom||0)>=20, IC.scroll2, t('ach_kw_wisd2'), {shape:'scroll',rv:3,secret:true,cur:Math.min(kw.wisdom||0,20),tgt:20,dk:'dk_kw_wisd2'});
      // Amazing Grace (dove icon, shield shape)
      add(2, (kw.grace||0)>=3, IC.dove2, t('ach_kw_grace1'), {shape:'shield',rv:1,cur:Math.min(kw.grace||0,3),tgt:3,dk:'dk_kw_grace1'});
      add(5, (kw.grace||0)>=20, IC.dove2, t('ach_kw_grace2'), {shape:'shield',rv:3,secret:true,cur:Math.min(kw.grace||0,20),tgt:20,dk:'dk_kw_grace2'});
      // Kingdom Seeker (crown shape)
      add(2, (kw.kingdom||0)>=5, IC.crown2, t('ach_kw_king1'), {shape:'crown',rv:0,cur:Math.min(kw.kingdom||0,5),tgt:5,dk:'dk_kw_king1'});
      add(5, (kw.kingdom||0)>=25, IC.crown2, t('ach_kw_king2'), {shape:'crown',rv:1,cur:Math.min(kw.kingdom||0,25),tgt:25,dk:'dk_kw_king2'});
      add(7, (kw.kingdom||0)>=60, IC.crown2, t('ach_kw_king3'), {shape:'crown',rv:3,secret:true,cur:Math.min(kw.kingdom||0,60),tgt:60,dk:'dk_kw_king3'});
      // Prayer Devotion (lamp icon, tear shape)
      add(1, (kw.pray||0)>=3, IC.lamp2, t('ach_kw_pray1'), {shape:'tear',rv:0,cur:Math.min(kw.pray||0,3),tgt:3,dk:'dk_kw_pray1'});
      add(4, (kw.pray||0)>=20, IC.lamp2, t('ach_kw_pray2'), {shape:'tear',rv:1,cur:Math.min(kw.pray||0,20),tgt:20,dk:'dk_kw_pray2'});
      add(7, (kw.pray||0)>=50, IC.lamp2, t('ach_kw_pray3'), {shape:'tear',rv:3,secret:true,cur:Math.min(kw.pray||0,50),tgt:50,dk:'dk_kw_pray3'});
      // Peace & Joy
      add(2, (kw.peace||0)>=5, IC.spark, t('ach_kw_peace'), {rv:1,cur:Math.min(kw.peace||0,5),tgt:5,dk:'dk_kw_peace'});
      add(2, (kw.joy||0)>=5, IC.spark, t('ach_kw_joy'), {rv:1,cur:Math.min(kw.joy||0,5),tgt:5,dk:'dk_kw_joy'});
      // Covenant & Truth
      add(3, (kw.covenant||0)>=10, IC.note, t('ach_kw_cov'), {rv:1,cur:Math.min(kw.covenant||0,10),tgt:10,dk:'dk_kw_cov'});
      add(3, (kw.truth||0)>=10, IC.note, t('ach_kw_truth'), {rv:1,cur:Math.min(kw.truth||0,10),tgt:10,dk:'dk_kw_truth'});"""

replace_once(old_kw, new_kw, 'keyword achievement dk block')

# ── 8. Add I18N description keys to English section ──────────────────────────
# We add them right before the closing of ach_intro value (end of en block)
old_ach_intro = "ach_intro:\"Earn awards by studying — add notes, highlight verses, explore more Bible books and keep your streak going. Rarer awards grant more Appreciation. Tap a tier to open it, and use the filters to see what’s left to unlock.\"},"
new_ach_intro = (
    "ach_intro:\"Earn awards by studying — add notes, highlight verses, explore more Bible books and keep your streak going. Rarer awards grant more Appreciation. Tap a tier to open it, and use the filters to see what’s left to unlock.\","
    "mp_mystery:'This award is still hidden. Keep studying to uncover what lies ahead.',"
    "mp_earned:'Earned!',"
    "mp_crest_d:'Tier crest — reach the required level for this tier to earn it.',"
    "mp_master_d:'Mastery badge — earn every award in this tier to claim it.',"
    "mp_generic_tgt:'You need {x} in total to earn this award.',"
    "dk_firstnote:'Write your very first note to earn this award. Every great library starts with a single thought.',"
    "dk_firsthl:'Make your first highlight in any Bible text to earn this award.',"
    "dk_firstbm:'Create your first bookmark to earn this award.',"
    "dk_firsttag:'Create your first tag to earn this award. Tags help you organize your study themes.',"
    "dk_firstbook:'Write a note in any Bible book to earn this award.',"
    "dk_deep100:'Write a note of at least 100 words. Explore one passage at depth.',"
    "dk_deep300:'Write a single note of 300 or more words — a true study essay on one passage.',"
    "dk_treatise:'Hidden: write a single note exceeding 1,000 words. A full treatise on one topic.',"
    "dk_scholar:'Hidden: reach an average note length of 100+ words across your whole library.',"
    "dk_bigday:'Hidden: write 50 or more notes in a single calendar day.',"
    "dk_polymath:'Hidden: add study notes in 10 or more different publications.',"
    "dk_nightowl:'Hidden: study after midnight on 30 separate occasions.',"
    "dk_devoted:'Hidden: maintain an active study streak for two full years without a break.',"
    "dk_torah:'Write notes in all five books of the Torah: Genesis, Exodus, Leviticus, Numbers, and Deuteronomy.',"
    "dk_historical:'Study through all the historical books of the Hebrew Scriptures, from Joshua to Esther.',"
    "dk_wisdom_books:'Write notes in all five Books of Wisdom: Job, Psalms, Proverbs, Ecclesiastes, and Song of Solomon.',"
    "dk_majorproph:'Explore all five Major Prophets: Isaiah, Jeremiah, Lamentations, Ezekiel, and Daniel.',"
    "dk_minorproph:'Study through all twelve Minor Prophets, from Hosea to Malachi.',"
    "dk_whole_ot:'Write notes in every one of the 39 books of the Hebrew Scriptures.',"
    "dk_gospels:'Write notes in all four Gospels: Matthew, Mark, Luke, and John.',"
    "dk_acts:'Explore the Acts of the Apostles with written study notes.',"
    "dk_pauline:'Study through all thirteen letters of Paul — Romans through Philemon.',"
    "dk_generalep:'Write notes in the eight General Letters: Hebrews, James, 1–2 Peter, 1–3 John, Jude.',"
    "dk_revelation:'Explore the book of Revelation with written notes.',"
    "dk_whole_nt:'Write notes in every one of the 27 books of the Greek Scriptures.',"
    "dk_wholebible:'Extraordinary — add notes in all 66 books of the entire Bible. A lifetime achievement.',"
    "dk_kw_love1:'Earned your first note containing the word “love.” Every great study starts with the greatest commandment.',"
    "dk_kw_love2:'Write notes mentioning love in 10 or more passages. Love is becoming a defining theme of your study.',"
    "dk_kw_love3:'Love appears in 30 of your notes. You truly walk in love as a central conviction.',"
    "dk_kw_love4:'Hidden: love appears in 75+ notes — a true ambassador of agape.',"
    "dk_kw_faith1:'Write your first note about faith. Every journey of trust begins with a single step.',"
    "dk_kw_faith2:'Faith appears in 15 of your notes. Your study is being built on the bedrock of trust.',"
    "dk_kw_faith3:'Hidden: faith mentioned in 40+ notes — you carry the full shield of faith.',"
    "dk_kw_hope1:'Write 5 notes mentioning hope. Hope anchors the soul and steadies every study.',"
    "dk_kw_hope2:'Hidden: hope appears in 25+ notes — your study shines with the blessed hope.',"
    "dk_kw_proph1:'Write 3 notes on prophetic passages. A voice begins to speak through your study.',"
    "dk_kw_proph2:'Prophecy appears in 15 of your notes. Open vision is forming in your library.',"
    "dk_kw_proph3:'Hidden: 40+ notes on prophecy — you have become a true student of what is written.',"
    "dk_kw_wisd1:'Write 5 notes containing the word wisdom. The fear of Jehovah is the very start.',"
    "dk_kw_wisd2:'Hidden: wisdom appears in 20+ notes — a heart of discernment has been cultivated.',"
    "dk_kw_grace1:'Write 3 notes mentioning grace. Every good gift comes through God’s undeserved kindness.',"
    "dk_kw_grace2:'Hidden: grace appears in 20+ notes — abounding grace has shaped your study life.',"
    "dk_kw_king1:'Write 5 notes about the Kingdom. Seek first the Kingdom and his righteousness.',"
    "dk_kw_king2:'Kingdom mentioned in 25 of your notes. You herald the good news with every entry.',"
    "dk_kw_king3:'Hidden: Kingdom appears in 60+ notes — a true Kingdom proclaimer through and through.',"
    "dk_kw_pray1:'Write 3 notes about prayer. Draw close to God through your study and devotion.',"
    "dk_kw_pray2:'Prayer appears in 20 of your notes. Unceasing prayer is woven through your library.',"
    "dk_kw_pray3:'Hidden: prayer mentioned in 50+ notes — you keep a night watch of dedicated study.',"
    "dk_kw_peace:'Write 5 notes mentioning peace. The peace of God surpasses all understanding.',"
    "dk_kw_joy:'Write 5 notes containing joy. May the God of hope fill you with all joy.',"
    "dk_kw_cov:'Write 10 notes about the covenant. Study the terms of God’s precious promise.',"
    "dk_kw_truth:'Write 10 notes about truth. The truth will make you free.\"},")

replace_once(old_ach_intro, new_ach_intro, 'en I18N dk/mp keys')

# ── 9. Add popup CSS before .jww-wc-sub ──────────────────────────────────────
popup_css = """.jww-mp-overlay{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.65);display:flex;align-items:center;justify-content:center;padding:16px}
        .jww-mp-box{background:#0f172a;border:1.5px solid rgba(255,255,255,.12);border-radius:16px;padding:24px 20px 20px;max-width:320px;width:100%;box-shadow:0 8px 40px rgba(0,0,0,.65);position:relative;animation:jwwMpIn .18s ease}
        @keyframes jwwMpIn{from{opacity:0;transform:scale(.92)}to{opacity:1;transform:scale(1)}}
        .jww-mp-close{position:absolute;top:10px;right:12px;background:none;border:none;color:#64748b;font-size:20px;cursor:pointer;line-height:1;padding:4px 7px;border-radius:6px}
        .jww-mp-close:hover{color:#e2e8f0;background:rgba(255,255,255,.06)}
        .jww-mp-head{display:flex;align-items:center;gap:14px;margin-bottom:14px}
        .jww-mp-wrap{flex-shrink:0;width:64px;height:64px;position:relative}
        .jww-mp-wrap .jww-medal-disc{width:64px;height:64px;font-size:28px}
        .jww-mp-wrap.jww-medal-heart .jww-medal-disc{clip-path:path('M32 56C5 40 2 21 12 13C19 5 27 7 32 18C37 7 45 5 52 13C62 21 59 40 32 56Z');border-radius:0}
        .jww-mp-wrap.jww-medal-tear .jww-medal-disc{clip-path:path('M32 4C12 18 4 30 4 41C4 55 17 60 32 60C47 60 60 55 60 41C60 30 52 18 32 4Z');border-radius:0}
        .jww-mp-wrap.jww-medal-shield .jww-medal-disc{clip-path:polygon(50% 0%,100% 20%,100% 68%,50% 100%,0% 68%,0% 20%);border-radius:0}
        .jww-mp-wrap.jww-medal-star .jww-medal-disc{clip-path:polygon(50% 2%,62% 38%,98% 38%,68% 59%,79% 93%,50% 72%,21% 93%,32% 59%,2% 38%,38% 38%);border-radius:0}
        .jww-mp-wrap.jww-medal-diamond .jww-medal-disc{clip-path:polygon(50% 3%,97% 50%,50% 97%,3% 50%);border-radius:0}
        .jww-mp-wrap.jww-medal-crown .jww-medal-disc{clip-path:polygon(0% 100%,0% 42%,18% 16%,36% 42%,50% 8%,64% 42%,82% 16%,100% 42%,100% 100%);border-radius:0}
        .jww-mp-wrap.jww-medal-scroll .jww-medal-disc{clip-path:polygon(20% 0%,80% 0%,100% 20%,100% 80%,80% 100%,20% 100%,0% 80%,0% 20%);border-radius:0}
        .jww-mp-info{flex:1;min-width:0}
        .jww-mp-name{font-size:15px;font-weight:700;color:#e2e8f0;margin-bottom:3px;line-height:1.3}
        .jww-mp-rar{font-size:11px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.06em}
        .jww-mp-ap{font-size:13px;color:#fbbf24;font-weight:700;margin-top:4px}
        .jww-mp-body{color:#94a3b8;font-size:13px;line-height:1.6}
        .jww-mp-desc{margin-bottom:0}
        .jww-mp-status{margin-top:12px;padding-top:12px;border-top:1px solid rgba(255,255,255,.08)}
        .jww-mp-earned{display:flex;align-items:center;gap:6px;color:#4ade80;font-weight:700;font-size:13px}
        .jww-mp-prog-row{display:flex;align-items:center;gap:8px;font-size:12px;color:#94a3b8}
        .jww-mp-prog-bar{flex:1;height:5px;background:rgba(255,255,255,.1);border-radius:3px;overflow:hidden}
        .jww-mp-prog-fill{height:100%;background:#ea580c;border-radius:3px}
        .jww-mp-prog-lbl{flex-shrink:0;font-variant-numeric:tabular-nums}
        """
replace_once(
    '.jww-wc-sub{font-size:12.5px;color:#64748b;margin:0 0 12px}',
    popup_css + '.jww-wc-sub{font-size:12.5px;color:#64748b;margin:0 0 12px}',
    'popup CSS'
)

# ── 10. Add openMedalPopup + wireAchMedals functions before wireAchFilters ────
popup_functions = r"""    function openMedalPopup(a, on, rvd){
      var mystery = !rvd || (a.secret && !on);
      var nm = mystery ? '???' : a.name;
      var disc = mystery ? IC_LOCK : a.icon;
      var col = (!a.crest && !a.master) ? achColor(a) : null;
      var cstyle = col ? '--mc:' + col[0] + ';--mc2:' + col[1] : '';
      var shapeClass = (a.shape && !mystery) ? ' jww-medal-' + a.shape : '';
      var onClass = on ? ' jww-medal-on' : '';
      var ap = ACH_RENOWN[a.rarity] || 0;
      var rl = t(ACH_RARKEY[a.rarity]);
      var discHtml = '<div class="jww-mp-wrap' + shapeClass + '" style="' + cstyle + '"><div class="jww-medal-disc' + onClass + '">' + disc + '</div></div>';
      var desc = '';
      if (mystery) { desc = t('mp_mystery'); }
      else if (a.crest) { desc = t('mp_crest_d'); }
      else if (a.master) { desc = t('mp_master_d'); }
      else if (a.dk) { desc = t(a.dk); }
      else if (a.tgt) { desc = t('mp_generic_tgt').replace('{x}', a.tgt); }
      else { desc = a.name + '.'; }
      var status = '';
      if (on) {
        status = '<div class="jww-mp-status"><div class="jww-mp-earned">✓ ' + esc(t('mp_earned')) + '</div></div>';
      } else if (rvd && !a.secret && a.tgt) {
        var pct = Math.round(clamp01((a.cur || 0) / a.tgt) * 100);
        status = '<div class="jww-mp-status"><div class="jww-mp-prog-row"><div class="jww-mp-prog-bar"><div class="jww-mp-prog-fill" style="width:' + pct + '%"></div></div><span class="jww-mp-prog-lbl">' + (a.cur || 0) + ' / ' + a.tgt + '</span></div></div>';
      }
      var apLine = (!mystery && !a.crest && !a.master) ? '<div class="jww-mp-ap">+' + ap + ' ' + esc(t('renown_label')) + '</div>' : '';
      var html = '<div class="jww-mp-overlay" id="jww-mp-ol"><div class="jww-mp-box"><button class="jww-mp-close" id="jww-mp-x" aria-label="Close">×</button><div class="jww-mp-head">' + discHtml + '<div class="jww-mp-info"><div class="jww-mp-name">' + esc(nm) + '</div><div class="jww-mp-rar">' + esc(rl) + '</div>' + apLine + '</div></div><div class="jww-mp-body"><div class="jww-mp-desc">' + esc(desc) + '</div>' + status + '</div></div></div>';
      var el = document.createElement('div'); el.innerHTML = html;
      var overlay = el.firstChild;
      document.body.appendChild(overlay);
      function close(){ if (overlay.parentNode) overlay.parentNode.removeChild(overlay); }
      overlay.addEventListener('click', function(e){ if (e.target === overlay) close(); });
      overlay.querySelector('#jww-mp-x').addEventListener('click', close);
      var onKey = function(e){ if (e.key === 'Escape'){ close(); document.removeEventListener('keydown', onKey); } };
      document.addEventListener('keydown', onKey);
    }
    function wireAchMedals(body){
      if (!__achCache) return;
      var A = __achCache, curT = __curTCache;
      function handleClick(e){
        var el = e.target.closest('[data-seq]'); if (!el) return;
        var seq = parseInt(el.getAttribute('data-seq'), 10); if (isNaN(seq)) return;
        var a = A[seq]; if (!a) return;
        var rvd = a.tier <= curT, on = rvd && a.on;
        openMedalPopup(a, on, rvd);
      }
      var wall = body.querySelector('.jww-ach-wall');
      if (wall) wall.addEventListener('click', handleClick);
    }
    """

replace_once(
    '    function wireAchFilters(body){',
    popup_functions + '    function wireAchFilters(body){',
    'openMedalPopup + wireAchMedals functions'
)

# ── 11. Call wireAchMedals after wireAchFilters ───────────────────────────────
replace_once(
    '      wireAchFilters(body);',
    '      wireAchFilters(body);\n      wireAchMedals(body);',
    'wireAchMedals call'
)

# ── Final checks and write ────────────────────────────────────────────────────
if errors:
    print('\n=== ERRORS ===')
    for e in errors:
        print(e)
    sys.exit(1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\nAll done. File written: {path}')

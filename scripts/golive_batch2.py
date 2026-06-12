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
        errors.append('ERROR "%s": %d' % (label or old[:50], c))
        return
    content = content.replace(old, new, 1)
    print('OK:', label or old[:50])

# keyword achievements block
kw_ach = (
    '      // Content keyword achievements\n'
    '      var kw = s.kwHits || {};\n'
    "      add(0, (kw.love||0)>=1, IC.heart, t('ach_kw_love1'), {shape:'heart',rv:0,dk:'dk_kw_love1'});\n"
    "      add(2, (kw.love||0)>=10, IC.heart, t('ach_kw_love2'), {shape:'heart',rv:1,cur:Math.min(kw.love||0,10),tgt:10,dk:'dk_kw_love2'});\n"
    "      add(4, (kw.love||0)>=30, IC.heart, t('ach_kw_love3'), {shape:'heart',rv:2,cur:Math.min(kw.love||0,30),tgt:30,dk:'dk_kw_love3'});\n"
    "      add(6, (kw.love||0)>=75, IC.heart, t('ach_kw_love4'), {shape:'heart',rv:3,secret:true,cur:Math.min(kw.love||0,75),tgt:75,dk:'dk_kw_love4'});\n"
    "      add(1, (kw.faith||0)>=1, IC.shield, t('ach_kw_faith1'), {shape:'shield',rv:0,dk:'dk_kw_faith1'});\n"
    "      add(3, (kw.faith||0)>=15, IC.shield, t('ach_kw_faith2'), {shape:'shield',rv:1,cur:Math.min(kw.faith||0,15),tgt:15,dk:'dk_kw_faith2'});\n"
    "      add(5, (kw.faith||0)>=40, IC.shield, t('ach_kw_faith3'), {shape:'shield',rv:2,secret:true,cur:Math.min(kw.faith||0,40),tgt:40,dk:'dk_kw_faith3'});\n"
    "      add(1, (kw.hope||0)>=5, IC.star5, t('ach_kw_hope1'), {shape:'star',rv:1,cur:Math.min(kw.hope||0,5),tgt:5,dk:'dk_kw_hope1'});\n"
    "      add(5, (kw.hope||0)>=25, IC.star5, t('ach_kw_hope2'), {shape:'star',rv:2,secret:true,cur:Math.min(kw.hope||0,25),tgt:25,dk:'dk_kw_hope2'});\n"
    "      add(2, (kw.prophecy||0)>=3, IC.eye2, t('ach_kw_proph1'), {shape:'diamond',rv:1,cur:Math.min(kw.prophecy||0,3),tgt:3,dk:'dk_kw_proph1'});\n"
    "      add(5, (kw.prophecy||0)>=15, IC.eye2, t('ach_kw_proph2'), {shape:'diamond',rv:2,cur:Math.min(kw.prophecy||0,15),tgt:15,dk:'dk_kw_proph2'});\n"
    "      add(7, (kw.prophecy||0)>=40, IC.eye2, t('ach_kw_proph3'), {shape:'diamond',rv:3,secret:true,cur:Math.min(kw.prophecy||0,40),tgt:40,dk:'dk_kw_proph3'});\n"
    "      add(2, (kw.wisdom||0)>=5, IC.scroll2, t('ach_kw_wisd1'), {shape:'scroll',rv:1,cur:Math.min(kw.wisdom||0,5),tgt:5,dk:'dk_kw_wisd1'});\n"
    "      add(5, (kw.wisdom||0)>=20, IC.scroll2, t('ach_kw_wisd2'), {shape:'scroll',rv:3,secret:true,cur:Math.min(kw.wisdom||0,20),tgt:20,dk:'dk_kw_wisd2'});\n"
    "      add(2, (kw.grace||0)>=3, IC.dove2, t('ach_kw_grace1'), {shape:'shield',rv:1,cur:Math.min(kw.grace||0,3),tgt:3,dk:'dk_kw_grace1'});\n"
    "      add(5, (kw.grace||0)>=20, IC.dove2, t('ach_kw_grace2'), {shape:'shield',rv:3,secret:true,cur:Math.min(kw.grace||0,20),tgt:20,dk:'dk_kw_grace2'});\n"
    "      add(2, (kw.kingdom||0)>=5, IC.crown2, t('ach_kw_king1'), {shape:'crown',rv:0,cur:Math.min(kw.kingdom||0,5),tgt:5,dk:'dk_kw_king1'});\n"
    "      add(5, (kw.kingdom||0)>=25, IC.crown2, t('ach_kw_king2'), {shape:'crown',rv:1,cur:Math.min(kw.kingdom||0,25),tgt:25,dk:'dk_kw_king2'});\n"
    "      add(7, (kw.kingdom||0)>=60, IC.crown2, t('ach_kw_king3'), {shape:'crown',rv:3,secret:true,cur:Math.min(kw.kingdom||0,60),tgt:60,dk:'dk_kw_king3'});\n"
    "      add(1, (kw.pray||0)>=3, IC.lamp2, t('ach_kw_pray1'), {shape:'tear',rv:0,cur:Math.min(kw.pray||0,3),tgt:3,dk:'dk_kw_pray1'});\n"
    "      add(4, (kw.pray||0)>=20, IC.lamp2, t('ach_kw_pray2'), {shape:'tear',rv:1,cur:Math.min(kw.pray||0,20),tgt:20,dk:'dk_kw_pray2'});\n"
    "      add(7, (kw.pray||0)>=50, IC.lamp2, t('ach_kw_pray3'), {shape:'tear',rv:3,secret:true,cur:Math.min(kw.pray||0,50),tgt:50,dk:'dk_kw_pray3'});\n"
    "      add(2, (kw.peace||0)>=5, IC.spark, t('ach_kw_peace'), {rv:1,cur:Math.min(kw.peace||0,5),tgt:5,dk:'dk_kw_peace'});\n"
    "      add(2, (kw.joy||0)>=5, IC.spark, t('ach_kw_joy'), {rv:1,cur:Math.min(kw.joy||0,5),tgt:5,dk:'dk_kw_joy'});\n"
    "      add(3, (kw.covenant||0)>=10, IC.note, t('ach_kw_cov'), {rv:1,cur:Math.min(kw.covenant||0,10),tgt:10,dk:'dk_kw_cov'});\n"
    "      add(3, (kw.truth||0)>=10, IC.note, t('ach_kw_truth'), {rv:1,cur:Math.min(kw.truth||0,10),tgt:10,dk:'dk_kw_truth'});\n"
    '      var jd = journeyData(s), curL = jd.level;'
)
R('      var jd = journeyData(s), curL = jd.level;', kw_ach, 'kw achievements')

# dk annotations for standard achievements
R("add(0, notes >= 1, IC.note, t('ach_firstnote'));","add(0, notes >= 1, IC.note, t('ach_firstnote'), {dk:'dk_firstnote'});","dk firstnote")
R("add(0, hl >= 1, IC.highlight, t('ach_firsthl'));","add(0, hl >= 1, IC.highlight, t('ach_firsthl'), {dk:'dk_firsthl'});","dk firsthl")
R("add(0, bm >= 1, IC.bookmark, t('ach_firstbm'));","add(0, bm >= 1, IC.bookmark, t('ach_firstbm'), {dk:'dk_firstbm'});","dk firstbm")
R("add(0, tags >= 1, IC.tag, t('ach_firsttag'));","add(0, tags >= 1, IC.tag, t('ach_firsttag'), {dk:'dk_firsttag'});","dk firsttag")
R("add(0, books >= 1, IC.book, t('ach_firstbook'));","add(0, books >= 1, IC.book, t('ach_firstbook'), {dk:'dk_firstbook'});","dk firstbook")
R("add(1, longest >= 100, IC.pen, t('ach_deep100'));","add(1, longest >= 100, IC.pen, t('ach_deep100'), {dk:'dk_deep100'});","dk deep100")
R("add(3, longest >= 300, IC.pen, t('ach_deep300'));","add(3, longest >= 300, IC.pen, t('ach_deep300'), {dk:'dk_deep300'});","dk deep300")
R("add(10, longest >= 1000, IC.pen, t('ach_treatise'), { secret: true });","add(10, longest >= 1000, IC.pen, t('ach_treatise'), { secret: true, dk:'dk_treatise' });","dk treatise")
R("add(6, avg >= 100, IC.pen, t('ach_scholar'), { secret: true });","add(6, avg >= 100, IC.pen, t('ach_scholar'), { secret: true, dk:'dk_scholar' });","dk scholar")
R("add(7, maxDay >= 50, IC.flame, t('ach_bigday'), { secret: true });","add(7, maxDay >= 50, IC.flame, t('ach_bigday'), { secret: true, dk:'dk_bigday' });","dk bigday")
R("add(6, pubCount >= 10, IC.layers, t('ach_polymath'), { secret: true });","add(6, pubCount >= 10, IC.layers, t('ach_polymath'), { secret: true, dk:'dk_polymath' });","dk polymath")
R("add(4, lateN >= 30, IC.clock, t('ach_nightowl'), { secret: true });","add(4, lateN >= 30, IC.clock, t('ach_nightowl'), { secret: true, dk:'dk_nightowl' });","dk nightowl")
R("add(11, (st.longest || 0) >= 730, IC.flame, t('ach_devoted'), { secret: true });","add(11, (st.longest || 0) >= 730, IC.flame, t('ach_devoted'), { secret: true, dk:'dk_devoted' });","dk devoted")
R("add(2, allBooks(s, 1, 5), IC.book, t('ach_torah'));","add(2, allBooks(s, 1, 5), IC.book, t('ach_torah'), {dk:'dk_torah'});","dk torah")
R("add(3, allBooks(s, 6, 17), IC.book, t('ach_historical'));","add(3, allBooks(s, 6, 17), IC.book, t('ach_historical'), {dk:'dk_historical'});","dk historical")
R("add(3, allBooks(s, 18, 22), IC.book, t('ach_wisdom'));","add(3, allBooks(s, 18, 22), IC.book, t('ach_wisdom'), {dk:'dk_wisdom_books'});","dk wisdom_books")
R("add(4, allBooks(s, 23, 27), IC.book, t('ach_majorproph'));","add(4, allBooks(s, 23, 27), IC.book, t('ach_majorproph'), {dk:'dk_majorproph'});","dk majorproph")
R("add(5, allBooks(s, 28, 39), IC.book, t('ach_minorproph'));","add(5, allBooks(s, 28, 39), IC.book, t('ach_minorproph'), {dk:'dk_minorproph'});","dk minorproph")
R("add(6, distinctBooks(s, 1, 39) >= 39, IC.book, t('ach_whole_ot'), { rv: 3 });","add(6, distinctBooks(s, 1, 39) >= 39, IC.book, t('ach_whole_ot'), { rv: 3, dk:'dk_whole_ot' });","dk whole_ot")
R("add(2, allBooks(s, 40, 43), IC.book, t('ach_gospels'));","add(2, allBooks(s, 40, 43), IC.book, t('ach_gospels'), {dk:'dk_gospels'});","dk gospels")
R("add(3, bk(44), IC.book, t('ach_acts'));","add(3, bk(44), IC.book, t('ach_acts'), {dk:'dk_acts'});","dk acts")
R("add(4, allBooks(s, 45, 57), IC.book, t('ach_pauline'));","add(4, allBooks(s, 45, 57), IC.book, t('ach_pauline'), {dk:'dk_pauline'});","dk pauline")
R("add(5, allBooks(s, 58, 65), IC.book, t('ach_generalep'));","add(5, allBooks(s, 58, 65), IC.book, t('ach_generalep'), {dk:'dk_generalep'});","dk generalep")
R("add(5, bk(66), IC.book, t('ach_revelation'));","add(5, bk(66), IC.book, t('ach_revelation'), {dk:'dk_revelation'});","dk revelation")
R("add(7, distinctBooks(s, 40, 66) >= 27, IC.book, t('ach_whole_nt'), { rv: 3 });","add(7, distinctBooks(s, 40, 66) >= 27, IC.book, t('ach_whole_nt'), { rv: 3, dk:'dk_whole_nt' });","dk whole_nt")
R("add(9, books >= 66, IC.trophy, t('ach_wholebible'), { rv: 4 });","add(9, books >= 66, IC.trophy, t('ach_wholebible'), { rv: 4, dk:'dk_wholebible' });","dk wholebible")

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Batch 2 OK')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

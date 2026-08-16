# -*- coding: utf-8 -*-
"""Add a 'Share' card to the merge celebration: generates a branded result
image (notes/highlights/bookmarks/tags merged) and shares it via the Web
Share API, with download + copy-link fallback. Localised in 12 languages."""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()
orig = c

def rep(old, new):
    global c
    if c.count(old) != 1:
        print('ABORT: expected 1 of:\n', old[:90], '\n got', c.count(old)); sys.exit(1)
    c = c.replace(old, new, 1)

# ── 1) Share i18n (own map, English fallback) + accessor ──
SHARE_I18N = '''
  var SHARE_I18N={
   en:{cele_share:'Share',share_headline:'Library merged!',share_text:'I just merged my JW Library notes with JW Sync — a free, private tool that combines your notes, highlights and bookmarks from all your devices. https://jwsync.org'},
   es:{cele_share:'Compartir',share_headline:'¡Biblioteca combinada!',share_text:'Acabo de combinar mis notas de JW Library con JW Sync, una herramienta gratuita y privada que une tus notas, subrayados y marcadores de todos tus dispositivos. https://jwsync.org'},
   pt:{cele_share:'Compartilhar',share_headline:'Biblioteca combinada!',share_text:'Acabei de combinar minhas notas do JW Library com o JW Sync — uma ferramenta gratuita e privada que une suas notas, destaques e marcadores de todos os seus dispositivos. https://jwsync.org'},
   fr:{cele_share:'Partager',share_headline:'Bibliothèque fusionnée !',share_text:'Je viens de fusionner mes notes JW Library avec JW Sync — un outil gratuit et privé qui réunit vos notes, surlignages et signets de tous vos appareils. https://jwsync.org'},
   de:{cele_share:'Teilen',share_headline:'Bibliothek zusammengeführt!',share_text:'Ich habe gerade meine JW Library-Notizen mit JW Sync zusammengeführt — ein kostenloses, privates Tool, das deine Notizen, Markierungen und Lesezeichen von allen Geräten vereint. https://jwsync.org'},
   it:{cele_share:'Condividi',share_headline:'Biblioteca unita!',share_text:'Ho appena unito le mie note di JW Library con JW Sync — uno strumento gratuito e privato che riunisce note, evidenziazioni e segnalibri da tutti i tuoi dispositivi. https://jwsync.org'},
   ru:{cele_share:'Поделиться',share_headline:'Библиотека объединена!',share_text:'Я объединил свои заметки JW Library с помощью JW Sync — бесплатного и приватного инструмента, который собирает заметки, выделения и закладки со всех устройств. https://jwsync.org'},
   ja:{cele_share:'共有',share_headline:'ライブラリを統合しました！',share_text:'JW Syncで JW Library のノートを統合しました。すべての端末のノート・ハイライト・しおりを一つにまとめる無料＆プライベートなツールです。https://jwsync.org'},
   ko:{cele_share:'공유',share_headline:'라이브러리 병합 완료!',share_text:'JW Sync로 JW Library 노트를 병합했어요 — 모든 기기의 노트, 강조, 책갈피를 하나로 합쳐 주는 무료 비공개 도구입니다. https://jwsync.org'},
   tl:{cele_share:'Ibahagi',share_headline:'Pinagsama ang library!',share_text:'Kakapagsama ko lang ng aking JW Library notes gamit ang JW Sync — isang libre at pribadong tool na pinagsasama ang iyong mga tala, highlight at bookmark mula sa lahat ng device. https://jwsync.org'},
   sv:{cele_share:'Dela',share_headline:'Biblioteket sammanfogat!',share_text:'Jag sammanfogade just mina JW Library-anteckningar med JW Sync — ett gratis och privat verktyg som samlar dina anteckningar, markeringar och bokmärken från alla enheter. https://jwsync.org'},
   ceb:{cele_share:'Ipaambit',share_headline:'Nahiusa ang library!',share_text:'Bag-o lang nako gihiusa ang akong JW Library notes gamit ang JW Sync — usa ka libre ug pribado nga tool nga naghiusa sa imong mga nota, highlight ug bookmark gikan sa tanan nimong device. https://jwsync.org'}
  };
  function ts(k){var l;try{l=lang();}catch(_){l='en';}return (SHARE_I18N[l]&&SHARE_I18N[l][k])||SHARE_I18N.en[k]||k;}'''
rep("cele_awards_btn:'I-explore ang mga ganti →'}};",
    "cele_awards_btn:'I-explore ang mga ganti →'}};" + SHARE_I18N)

# ── 2) Canvas card + share helpers (before renderCelebration) ──
HELPERS = (
  "  function shWrap(ctx,text,cx,y,maxW,lh){var words=String(text||'').split(' '),line='',yy=y;"
  "for(var n=0;n<words.length;n++){var tt=line+words[n]+' ';if(ctx.measureText(tt).width>maxW&&n>0){"
  "ctx.fillText(line.replace(/ $/,''),cx,yy);line=words[n]+' ';yy+=lh;}else{line=tt;}}"
  "ctx.fillText(line.replace(/ $/,''),cx,yy);}\n"
  "  function buildMergeCard(stats){try{var s=stats||{},W=1080,H=1080,cv=document.createElement('canvas');cv.width=W;cv.height=H;"
  "var ctx;try{ctx=cv.getContext('2d');}catch(_){return null;}if(!ctx)return null;var loc;try{loc=lang();}catch(_){loc='en';}\n"
  "    ctx.fillStyle='#0b1426';ctx.fillRect(0,0,W,H);\n"
  "    ctx.strokeStyle='rgba(234,88,12,.5)';ctx.lineWidth=8;ctx.strokeRect(30,30,W-60,H-60);\n"
  "    ctx.textAlign='center';\n"
  "    ctx.fillStyle='#fb923c';ctx.font='700 40px Inter,Arial,sans-serif';ctx.fillText('J W   S Y N C',W/2,132);\n"
  "    ctx.beginPath();ctx.arc(W/2,300,84,0,Math.PI*2);ctx.fillStyle='#ea580c';ctx.fill();\n"
  "    ctx.strokeStyle='#fff';ctx.lineWidth=14;ctx.lineCap='round';ctx.lineJoin='round';ctx.beginPath();"
  "ctx.moveTo(W/2-38,300);ctx.lineTo(W/2-8,334);ctx.lineTo(W/2+46,262);ctx.stroke();\n"
  "    ctx.fillStyle='#f8fafc';ctx.font='800 62px Inter,Arial,sans-serif';ctx.fillText(ts('share_headline'),W/2,468);\n"
  "    ctx.fillStyle='#94a3b8';ctx.font='400 30px Inter,Arial,sans-serif';shWrap(ctx,t('cele_subtitle'),W/2,528,W-240,40);\n"
  "    var items=[[s.notes,'stat_notes'],[s.highlights,'stat_highlights'],[s.bookmarks,'stat_bookmarks'],[s.tags,'stat_tags']],gx=[W/2-210,W/2+210],gy=[722,902];\n"
  "    for(var i=0;i<4;i++){var x=gx[i%2],y=gy[i>1?1:0],v=items[i][0];if(v==null||v==='\\u2013')v=0;v=Number(v)||0;\n"
  "      ctx.fillStyle='#fb923c';ctx.font='800 74px Inter,Arial,sans-serif';ctx.fillText(v.toLocaleString(loc),x,y);\n"
  "      ctx.fillStyle='#cbd5e1';ctx.font='600 26px Inter,Arial,sans-serif';ctx.fillText(String(t(items[i][1])).toUpperCase(),x,y+46);}\n"
  "    ctx.fillStyle='#64748b';ctx.font='600 30px Inter,Arial,sans-serif';ctx.fillText('jwsync.org',W/2,H-74);\n"
  "    return cv;}catch(_){return null;}}\n"
  "  function shareMerge(stats){var url='https://jwsync.org',text=ts('share_text');\n"
  "    function dl(b){try{var u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='jwsync.png';"
  "document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u);},3000);}catch(_){}"
  "try{if(navigator.clipboard)navigator.clipboard.writeText(url);}catch(_){}}\n"
  "    function linkShare(){try{if(navigator.share){navigator.share({title:'JW Sync',text:text,url:url}).catch(function(){});return true;}}catch(_){}return false;}\n"
  "    var cv=buildMergeCard(stats);\n"
  "    try{if(cv&&cv.toBlob){cv.toBlob(function(b){if(b){try{if(navigator.canShare&&typeof File==='function'){"
  "var fl=new File([b],'jwsync.png',{type:'image/png'});if(navigator.canShare({files:[fl]})){"
  "navigator.share({files:[fl],text:text}).catch(function(){dl(b);});return;}}}catch(_){}"
  "if(!linkShare())dl(b);}else{linkShare();}},'image/png');}else{linkShare();}}catch(_){linkShare();}}\n"
  "  function renderCelebration(opts) {"
)
rep("  function renderCelebration(opts) {", HELPERS)

# ── 3) Share button in the celebration actions (after Download) ──
rep(
  "          '</button>' +\n"
  "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-restore>' + esc(t('cele_restore')) + ' →</button>' +",
  "          '</button>' +\n"
  "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-share>"
  "<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\">"
  "<circle cx=\"18\" cy=\"5\" r=\"3\"/><circle cx=\"6\" cy=\"12\" r=\"3\"/><circle cx=\"18\" cy=\"19\" r=\"3\"/>"
  "<line x1=\"8.59\" y1=\"13.51\" x2=\"15.42\" y2=\"17.49\"/><line x1=\"15.41\" y1=\"6.51\" x2=\"8.59\" y2=\"10.49\"/></svg> ' + esc(ts('cele_share')) + '</button>' +\n"
  "          '<button class=\"jwc-btn jwc-btn-outline\" type=\"button\" data-jwc-restore>' + esc(t('cele_restore')) + ' →</button>' +"
)

# ── 4) Wire the Share button ──
rep(
  "    var rBtn = ov.querySelector('[data-jwc-restore]');\n"
  "    if (rBtn) rBtn.addEventListener('click', function () { fireAnalytics('post_merge_restore'); openRestoreGuide(); });",
  "    var rBtn = ov.querySelector('[data-jwc-restore]');\n"
  "    if (rBtn) rBtn.addEventListener('click', function () { fireAnalytics('post_merge_restore'); openRestoreGuide(); });\n"
  "    var shBtn = ov.querySelector('[data-jwc-share]');\n"
  "    if (shBtn) shBtn.addEventListener('click', function () { fireAnalytics('post_merge_share'); shareMerge(cached && cached.stats); });"
)

# ── 5) Version bump ──
rep('"softwareVersion": "2.56.2"', '"softwareVersion": "2.57.0"')

if c == orig:
    print('No changes!'); sys.exit(1)
io.open(f, 'w', encoding='utf-8').write(c)
print('Share card added; file now', len(c), 'chars')

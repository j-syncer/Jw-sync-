# -*- coding: utf-8 -*-
"""Add an 'Other tools' tab to the How-it-works wizard, explaining the
Study Explorer, Study Stats & Awards, and Note Share & Receive tools.
Tool names are pulled from the existing landing i18n so they match the
'Choose a tool' cards; descriptions/UI strings are localised in-module."""
import io, sys

FILE = 'beta/index.html'
with io.open(FILE, encoding='utf-8') as f:
    c = f.read()
orig = c

def rep(old, new):
    global c
    if c.count(old) != 1:
        print('ABORT: expected 1 occurrence of:\n', old[:80], '\n got', c.count(old)); sys.exit(1)
    c = c.replace(old, new, 1)

# ── 1) New i18n keys appended to every language object (after `skip`) ──
NEW = {
 'en':  {'tab1':'Merging','tab2':'Other tools','t_intro':'JW Sync includes a few more tools — here’s what each one does:',
   'exp_d':'Open any backup to search, read, edit and tag your notes, change highlight colours, and find notes by meaning with Ask Your Library — then save back to a .jwlibrary file.',
   'stat_d':'Load a backup to see your study totals, streaks and trends, plus an Awards tab with medals you earn for reaching study milestones.',
   'shr_d':'Send chosen notes to a friend as a small share file, or add notes a friend sent you — without merging whole backups.','open':'Open'},
 'es':  {'tab1':'Combinar','tab2':'Otras herramientas','t_intro':'JW Sync incluye algunas herramientas más; esto hace cada una:',
   'exp_d':'Abre cualquier copia para buscar, leer, editar y etiquetar tus notas, cambiar colores de resaltado y encontrar notas por significado con Pregunta a tu biblioteca; luego guarda en un archivo .jwlibrary.',
   'stat_d':'Carga una copia para ver tus totales, rachas y tendencias de estudio, además de una pestaña de Logros con medallas que ganas al alcanzar metas.',
   'shr_d':'Envía notas concretas a un amigo como un pequeño archivo, o añade las notas que te enviaron, sin combinar copias enteras.','open':'Abrir'},
 'pt':  {'tab1':'Combinar','tab2':'Outras ferramentas','t_intro':'O JW Sync inclui mais algumas ferramentas — veja o que cada uma faz:',
   'exp_d':'Abra qualquer backup para pesquisar, ler, editar e marcar suas notas, mudar as cores dos destaques e encontrar notas por significado com o Pergunte à sua biblioteca; depois salve em um arquivo .jwlibrary.',
   'stat_d':'Carregue um backup para ver seus totais, sequências e tendências de estudo, além de uma aba de Conquistas com medalhas por alcançar marcos.',
   'shr_d':'Envie notas específicas a um amigo como um pequeno arquivo, ou adicione as notas que enviaram a você — sem combinar backups inteiros.','open':'Abrir'},
 'fr':  {'tab1':'Fusion','tab2':'Autres outils','t_intro':'JW Sync propose quelques autres outils — voici ce que fait chacun :',
   'exp_d':'Ouvrez une sauvegarde pour rechercher, lire, modifier et étiqueter vos notes, changer les couleurs de surlignage et retrouver des notes par leur sens avec Interrogez votre bibliothèque, puis enregistrez dans un fichier .jwlibrary.',
   'stat_d':'Chargez une sauvegarde pour voir vos totaux, séries et tendances d’étude, ainsi qu’un onglet Récompenses avec des médailles gagnées en atteignant des objectifs.',
   'shr_d':'Envoyez des notes choisies à un ami sous forme d’un petit fichier de partage, ou ajoutez celles qu’un ami vous a envoyées — sans fusionner des sauvegardes entières.','open':'Ouvrir'},
 'de':  {'tab1':'Zusammenführen','tab2':'Weitere Tools','t_intro':'JW Sync bietet noch einige weitere Tools — das macht jedes davon:',
   'exp_d':'Öffne eine Sicherung, um deine Notizen zu durchsuchen, zu lesen, zu bearbeiten und zu verschlagworten, Markierungsfarben zu ändern und Notizen mit „Frag deine Bibliothek“ nach Sinn zu finden — und speichere dann als .jwlibrary-Datei.',
   'stat_d':'Lade eine Sicherung, um deine Studiensummen, Serien und Trends zu sehen, sowie einen Auszeichnungen-Tab mit Medaillen für erreichte Meilensteine.',
   'shr_d':'Sende ausgewählte Notizen als kleine Teilen-Datei an einen Freund oder füge Notizen hinzu, die dir jemand gesendet hat — ohne ganze Sicherungen zusammenzuführen.','open':'Öffnen'},
 'it':  {'tab1':'Unione','tab2':'Altri strumenti','t_intro':'JW Sync include altri strumenti — ecco cosa fa ciascuno:',
   'exp_d':'Apri un backup per cercare, leggere, modificare ed etichettare le note, cambiare i colori delle evidenziazioni e trovare note per significato con Chiedi alla tua biblioteca, poi salva in un file .jwlibrary.',
   'stat_d':'Carica un backup per vedere totali, serie e tendenze di studio, oltre a una scheda Riconoscimenti con medaglie che ottieni raggiungendo traguardi.',
   'shr_d':'Invia note scelte a un amico come piccolo file di condivisione, o aggiungi le note che ti hanno inviato — senza unire interi backup.','open':'Apri'},
 'ru':  {'tab1':'Объединение','tab2':'Другие инструменты','t_intro':'В JW Sync есть ещё несколько инструментов — вот что делает каждый:',
   'exp_d':'Откройте любую копию, чтобы искать, читать, редактировать и помечать заметки, менять цвета выделений и находить заметки по смыслу с «Спросите свою библиотеку», затем сохраните в файл .jwlibrary.',
   'stat_d':'Загрузите копию, чтобы увидеть итоги, серии и тенденции изучения, а также вкладку «Награды» с медалями за достижение этапов.',
   'shr_d':'Отправьте выбранные заметки другу небольшим файлом или добавьте заметки, которые прислали вам, — без объединения целых копий.','open':'Открыть'},
 'ja':  {'tab1':'統合','tab2':'その他のツール','t_intro':'JW Syncには他にもツールがあります。それぞれの機能は次のとおりです：',
   'exp_d':'バックアップを開いて、ノートの検索・閲覧・編集・タグ付け、ハイライト色の変更ができ、「ライブラリに質問」で意味からノートを探せます。編集後は.jwlibraryファイルに保存します。',
   'stat_d':'バックアップを読み込むと、学習の合計・連続記録・傾向に加え、節目で獲得するメダルを集めた「アワード」タブを確認できます。',
   'shr_d':'選んだノートを小さな共有ファイルとして友だちに送ったり、友だちから届いたノートを追加したりできます（バックアップ全体を統合せずに）。','open':'開く'},
 'ko':  {'tab1':'병합','tab2':'다른 도구','t_intro':'JW Sync에는 몇 가지 도구가 더 있습니다. 각 기능은 다음과 같습니다:',
   'exp_d':'백업을 열어 노트를 검색·읽기·편집·태그하고 강조 색을 바꾸며, ‘내 도서관에 묻기’로 의미로 노트를 찾은 뒤 .jwlibrary 파일로 저장하세요.',
   'stat_d':'백업을 불러오면 학습 총계·연속 기록·추세와 함께, 학습 이정표 달성 시 받는 메달을 모은 수상 탭을 볼 수 있습니다.',
   'shr_d':'선택한 노트를 작은 공유 파일로 친구에게 보내거나, 친구가 보낸 노트를 추가하세요 — 전체 백업을 병합하지 않고도요.','open':'열기'},
 'tl':  {'tab1':'Pagsasama','tab2':'Iba pang tool','t_intro':'May ilan pang tool ang JW Sync — ito ang ginagawa ng bawat isa:',
   'exp_d':'Buksan ang anumang backup para hanapin, basahin, i-edit at i-tag ang iyong mga tala, baguhin ang kulay ng highlight, at hanapin ang mga tala ayon sa kahulugan gamit ang Itanong sa Library — pagkatapos ay i-save sa .jwlibrary file.',
   'stat_d':'Mag-load ng backup para makita ang iyong mga total, streak at trend ng pag-aaral, kasama ang Awards tab na may mga medalyang makukuha mo kapag umabot sa mga milestone.',
   'shr_d':'Magpadala ng piling tala sa kaibigan bilang maliit na share file, o idagdag ang mga talang ipinadala sa iyo — nang hindi pinagsasama ang buong backup.','open':'Buksan'},
 'sv':  {'tab1':'Sammanfogning','tab2':'Andra verktyg','t_intro':'JW Sync har några fler verktyg — så här fungerar de:',
   'exp_d':'Öppna en säkerhetskopia för att söka, läsa, redigera och tagga dina anteckningar, ändra färg på markeringar och hitta anteckningar efter betydelse med Fråga ditt bibliotek — spara sedan till en .jwlibrary-fil.',
   'stat_d':'Ladda en säkerhetskopia för att se dina studietotaler, sviter och trender, plus en Utmärkelser-flik med medaljer du tjänar när du når milstolpar.',
   'shr_d':'Skicka utvalda anteckningar till en vän som en liten delningsfil, eller lägg till anteckningar någon skickat dig — utan att slå ihop hela säkerhetskopior.','open':'Öppna'},
 'ceb': {'tab1':'Paghiusa','tab2':'Uban pang himan','t_intro':'Ang JW Sync adunay pipila pa ka himan — mao kini ang gibuhat sa matag usa:',
   'exp_d':'Ablihi ang bisan unsang backup aron pangitaon, basahon, i-edit ug i-tag ang imong mga nota, usbon ang kolor sa highlight, ug pangitaon ang mga nota pinaagi sa kahulogan gamit ang Pangutana sa imong Library — dayon i-save sa .jwlibrary file.',
   'stat_d':'Pag-load og backup aron makita ang imong mga total, streak ug uso sa pagtuon, lakip ang Awards nga tab nga adunay mga medalya nga imong makuha sa pag-abot sa mga milestone.',
   'shr_d':'Pagpadala og piniling mga nota sa imong higala isip gamay nga share file, o idugang ang mga nota nga gipadala kanimo — nga dili hiusahon ang tibuok backup.','open':'Ablihi'},
}
SKIP = {'en':'Skip','es':'Omitir','pt':'Pular','fr':'Ignorer','de':'Überspringen','it':'Salta',
        'ru':'Пропустить','ja':'スキップ',
        'ko':'건너뛰기','tl':'Laktawan','sv':'Hoppa över','ceb':'Laktawi'}
ORDER = ['tab1','tab2','t_intro','exp_d','stat_d','shr_d','open']
for lang, sk in SKIP.items():
    suffix = ''.join(",%s:'%s'" % (k, NEW[lang][k]) for k in ORDER)
    rep(",skip:'%s'}" % sk, ",skip:'%s'%s}" % (sk, suffix))

# ── 2) CSS for tabs + tool list ──
rep('.jw-wiz-start:hover{background:#c2410c}\n</style>',
    '.jw-wiz-start:hover{background:#c2410c}\n'
    '.jw-wiz-tabs{display:flex;gap:6px;margin:2px 0 16px;background:rgba(71,85,105,.25);padding:4px;border-radius:12px}\n'
    '.jw-wiz-tab{flex:1;cursor:pointer;border:0;background:none;color:#94a3b8;font:600 13px/1 inherit;padding:9px 8px;border-radius:9px}\n'
    '.jw-wiz-tab.active{background:#ea580c;color:#fff}\n'
    '[data-jw-pane][hidden]{display:none}\n'
    '.jw-wiz-intro{margin:0 0 14px;font:400 13.5px/1.5 inherit;color:#94a3b8}\n'
    '.jw-wiz-tools{list-style:none;margin:0 0 18px;padding:0;display:flex;flex-direction:column;gap:15px}\n'
    '.jw-wiz-tool{display:flex;gap:13px;align-items:flex-start}\n'
    '.jw-wiz-tool-ic{flex:0 0 auto;width:34px;height:34px;border-radius:9px;display:flex;align-items:center;justify-content:center;background:rgba(71,85,105,.3);color:#fb923c}\n'
    '.jw-wiz-tool-ic svg{width:18px;height:18px}\n'
    '.jw-wiz-tool-body{flex:1 1 auto;min-width:0}\n'
    '.jw-wiz-tool-t{font:600 14.5px/1.3 inherit;color:#f1f5f9;margin-bottom:2px}\n'
    '.jw-wiz-tool-d{font:400 13px/1.45 inherit;color:#94a3b8}\n'
    '.jw-wiz-tool-open{margin-top:6px;background:none;border:0;padding:0;cursor:pointer;color:#fb923c;font:600 13px/1.3 inherit;text-decoration:underline;text-underline-offset:2px}\n'
    '.jw-wiz-tool-open:hover{color:#ea580c}\n'
    '</style>')

# ── 3) Helpers (tool name from landing i18n, icons, open dispatch) ──
HELPERS = (
  "  function toolName(which){var map={explorer:'svc_explorer_t',stats:'svc_stats_t',share:'svc_share_t'},"
  "def={explorer:'Study Explorer',stats:'Study Stats',share:'Note Share & Receive'};\n"
  "    try{var l=curLang(),LI=window.__JW_LANDING_I18N||{},o=LI[l]||LI.en||{};\n"
  "      if(o[map[which]])return o[map[which]];if(LI.en&&LI.en[map[which]])return LI.en[map[which]];}catch(e){}\n"
  "    return def[which];}\n"
  "  function toolIcon(which){var s='<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\">';\n"
  "    if(which==='explorer')return s+'<path d=\"M4 19.5A2.5 2.5 0 0 1 6.5 17H20\"></path><path d=\"M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z\"></path></svg>';\n"
  "    if(which==='stats')return s+'<line x1=\"18\" y1=\"20\" x2=\"18\" y2=\"10\"></line><line x1=\"12\" y1=\"20\" x2=\"12\" y2=\"4\"></line><line x1=\"6\" y1=\"20\" x2=\"6\" y2=\"14\"></line></svg>';\n"
  "    return s+'<circle cx=\"18\" cy=\"5\" r=\"3\"></circle><circle cx=\"6\" cy=\"12\" r=\"3\"></circle><circle cx=\"18\" cy=\"19\" r=\"3\"></circle><line x1=\"8.6\" y1=\"13.5\" x2=\"15.4\" y2=\"17.5\"></line><line x1=\"15.4\" y1=\"6.5\" x2=\"8.6\" y2=\"10.5\"></line></svg>';}\n"
  "  function toolHtml(which,dk){return '<li class=\"jw-wiz-tool\"><span class=\"jw-wiz-tool-ic\">'+toolIcon(which)+'</span>'+\n"
  "    '<div class=\"jw-wiz-tool-body\"><div class=\"jw-wiz-tool-t\">'+esc(toolName(which))+'</div>'+\n"
  "    '<div class=\"jw-wiz-tool-d\">'+esc(L(dk))+'</div>'+\n"
  "    '<button type=\"button\" class=\"jw-wiz-tool-open\" data-jw-open=\"'+which+'\">'+esc(L('open'))+' \\u2192</button></div></li>';}\n"
  "  function openTool(which){try{\n"
  "    if(which==='stats'){if(window.__jwGoHighlights)window.__jwGoHighlights();}\n"
  "    else if(which==='share'){if(window.__jwGoShare)window.__jwGoShare();}\n"
  "    else if(which==='explorer'){var bt=window.__jwBootBrowse?window.__jwBootBrowse():Promise.resolve();\n"
  "      Promise.resolve(bt).then(function(){if(window.__openJwBrowse)window.__openJwBrowse(window.__jwLastFile||undefined);}).catch(function(){});}\n"
  "  }catch(e){}}\n"
  "  function openWizard(){"
)
rep("  function openWizard(){", HELPERS)

# ── 4) Wizard markup: insert tabs + wrap merge pane + add tools pane ──
rep(
  "        '<h2 class=\"jw-wiz-title\">'+esc(L('title'))+'</h2>'+\n"
  "        '<p class=\"jw-wiz-sub\">'+esc(L('sub'))+'</p>'+\n"
  "        '<ol class=\"jw-wiz-steps\">'+\n"
  "          stepHtml(1,'s1t','s1d','s1btn','export')+\n"
  "          stepHtml(2,'s2t','s2d',null,null)+\n"
  "          stepHtml(3,'s3t','s3d','s3btn','restore')+\n"
  "        '</ol>'+\n",
  "        '<h2 class=\"jw-wiz-title\">'+esc(L('title'))+'</h2>'+\n"
  "        '<div class=\"jw-wiz-tabs\" role=\"tablist\">'+\n"
  "          '<button type=\"button\" class=\"jw-wiz-tab active\" data-jw-tab=\"merge\">'+esc(L('tab1'))+'</button>'+\n"
  "          '<button type=\"button\" class=\"jw-wiz-tab\" data-jw-tab=\"tools\">'+esc(L('tab2'))+'</button>'+\n"
  "        '</div>'+\n"
  "        '<div data-jw-pane=\"merge\">'+\n"
  "          '<p class=\"jw-wiz-sub\">'+esc(L('sub'))+'</p>'+\n"
  "          '<ol class=\"jw-wiz-steps\">'+\n"
  "            stepHtml(1,'s1t','s1d','s1btn','export')+\n"
  "            stepHtml(2,'s2t','s2d',null,null)+\n"
  "            stepHtml(3,'s3t','s3d','s3btn','restore')+\n"
  "          '</ol>'+\n"
  "        '</div>'+\n"
  "        '<div data-jw-pane=\"tools\" hidden>'+\n"
  "          '<p class=\"jw-wiz-intro\">'+esc(L('t_intro'))+'</p>'+\n"
  "          '<ul class=\"jw-wiz-tools\">'+toolHtml('explorer','exp_d')+toolHtml('stats','stat_d')+toolHtml('share','shr_d')+'</ul>'+\n"
  "        '</div>'+\n"
)

# ── 5) Click handler: tab switching + tool open dispatch ──
rep(
  "    ov.addEventListener('click',function(e){\n"
  "      var g=e.target.closest&&e.target.closest('[data-jw-guide]');\n"
  "      if(g){if(window.__jwOpenGuide)window.__jwOpenGuide(g.getAttribute('data-jw-guide'));return;}\n"
  "      if(e.target.closest&&e.target.closest('[data-jw-close]'))close();\n"
  "    });",
  "    ov.addEventListener('click',function(e){\n"
  "      var tb=e.target.closest&&e.target.closest('[data-jw-tab]');\n"
  "      if(tb){var which=tb.getAttribute('data-jw-tab');\n"
  "        Array.prototype.forEach.call(ov.querySelectorAll('[data-jw-tab]'),function(b){b.classList.toggle('active',b===tb);});\n"
  "        Array.prototype.forEach.call(ov.querySelectorAll('[data-jw-pane]'),function(p){p.hidden=(p.getAttribute('data-jw-pane')!==which);});\n"
  "        return;}\n"
  "      var op=e.target.closest&&e.target.closest('[data-jw-open]');\n"
  "      if(op){close();openTool(op.getAttribute('data-jw-open'));return;}\n"
  "      var g=e.target.closest&&e.target.closest('[data-jw-guide]');\n"
  "      if(g){if(window.__jwOpenGuide)window.__jwOpenGuide(g.getAttribute('data-jw-guide'));return;}\n"
  "      if(e.target.closest&&e.target.closest('[data-jw-close]'))close();\n"
  "    });"
)

# ── 6) Version bumps ──
rep('"softwareVersion": "2.55.1"', '"softwareVersion": "2.56.0"')

if c == orig:
    print('No changes!'); sys.exit(1)
with io.open(FILE, 'w', encoding='utf-8') as f:
    f.write(c)
print('Tools tab added; file now', len(c), 'chars')

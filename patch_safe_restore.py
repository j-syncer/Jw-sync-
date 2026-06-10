# -*- coding: utf-8 -*-
"""Safe Restore confidence layer: a beautiful, reassuring panel shown on the
merge celebration AND in the restore guide — confirms originals are safe,
warns clearly that restoring replaces the device library, and nudges keeping
the combined file as a master backup. Localised in 12 languages."""
import io, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()
orig = c

def rep(old, new, label):
    global c
    if c.count(old) != 1:
        print('ABORT [%s]: expected 1, got %d' % (label, c.count(old))); sys.exit(1)
    c = c.replace(old, new, 1)

# ── 1) SAFE_I18N + accessor + panel builder (after ts()) ──
TS = "function ts(k){var l;try{l=lang();}catch(_){l='en';}return (SHARE_I18N[l]&&SHARE_I18N[l][k])||SHARE_I18N.en[k]||k;}"

SAFE = '''
  var SAFE_I18N={
   en:{safe_title:'Restore safely',safe_originals:'Your original backups are safe — JW Sync never changes them. This is a brand-new combined file.',safe_master:'Keep this combined file as your master backup.'},
   es:{safe_title:'Restaura con seguridad',safe_originals:'Tus copias originales están a salvo: JW Sync nunca las modifica. Este es un archivo combinado totalmente nuevo.',safe_master:'Guarda este archivo combinado como tu copia maestra.'},
   pt:{safe_title:'Restaure com segurança',safe_originals:'Seus backups originais estão seguros — o JW Sync nunca os altera. Este é um arquivo combinado totalmente novo.',safe_master:'Guarde este arquivo combinado como sua cópia mestra.'},
   fr:{safe_title:'Restaurer en toute sécurité',safe_originals:'Vos sauvegardes d’origine sont intactes — JW Sync ne les modifie jamais. Ceci est un nouveau fichier combiné.',safe_master:'Conservez ce fichier combiné comme copie maîtresse.'},
   de:{safe_title:'Sicher wiederherstellen',safe_originals:'Deine ursprünglichen Sicherungen sind sicher — JW Sync ändert sie nie. Dies ist eine brandneue kombinierte Datei.',safe_master:'Bewahre diese kombinierte Datei als deine Hauptsicherung auf.'},
   it:{safe_title:'Ripristina in sicurezza',safe_originals:'I tuoi backup originali sono al sicuro: JW Sync non li modifica mai. Questo è un nuovo file combinato.',safe_master:'Conserva questo file combinato come copia principale.'},
   ru:{safe_title:'Безопасное восстановление',safe_originals:'Ваши исходные копии в безопасности — JW Sync их не меняет. Это совершенно новый объединённый файл.',safe_master:'Сохраните этот объединённый файл как основную копию.'},
   ja:{safe_title:'安全に復元',safe_originals:'元のバックアップは安全です。JW Syncが変更することはありません。これは新しく統合されたファイルです。',safe_master:'この統合ファイルをマスターバックアップとして保管してください。'},
   ko:{safe_title:'안전하게 복원',safe_originals:'원본 백업은 안전합니다 — JW Sync는 절대 변경하지 않습니다. 이것은 완전히 새로운 통합 파일입니다.',safe_master:'이 통합 파일을 마스터 백업으로 보관하세요.'},
   tl:{safe_title:'Mag-restore nang ligtas',safe_originals:'Ligtas ang iyong orihinal na mga backup — hindi ito kailanman binabago ng JW Sync. Ito ay isang bagong pinagsamang file.',safe_master:'Itago ang pinagsamang file na ito bilang iyong master backup.'},
   sv:{safe_title:'Återställ tryggt',safe_originals:'Dina ursprungliga säkerhetskopior är trygga — JW Sync ändrar dem aldrig. Detta är en helt ny sammanslagen fil.',safe_master:'Spara den här sammanslagna filen som din huvudkopia.'},
   ceb:{safe_title:'Pag-restore nga luwas',safe_originals:'Luwas ang imong orihinal nga mga backup — dili kini usbon sa JW Sync. Kini usa ka bag-ong gihiusa nga file.',safe_master:'Tipigi kini nga gihiusa nga file isip imong master backup.'}
  };
  function sg(k){var l;try{l=lang();}catch(_){l='en';}return (SAFE_I18N[l]&&SAFE_I18N[l][k])||SAFE_I18N.en[k]||k;}
  function safeRow(color,bg,icon,text){return '<div style="display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:10px;background:'+bg+'">'+'<span style="flex:0 0 auto;color:'+color+';line-height:0;margin-top:2px">'+icon+'</span>'+'<span style="flex:1 1 auto;font:500 13px/1.5 inherit;color:#cbd5e1">'+esc(text)+'</span></div>';}
  function buildSafePanel(){var ck='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>';'''  '''
    var wn='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>';
    var st='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>';
    var sh='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>';
    return '<div style="width:100%;box-sizing:border-box;text-align:left;margin:16px 0 2px;padding:16px;border-radius:14px;background:rgba(4,15,34,.6);border:1px solid rgba(71,85,105,.4)">'+'<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;color:#34d399;font:700 13px/1.2 inherit">'+sh+'<span>'+esc(sg('safe_title'))+'</span></div>'+'<div style="display:flex;flex-direction:column;gap:8px">'+safeRow('#34d399','rgba(16,185,129,.08)',ck,sg('safe_originals'))+safeRow('#fbbf24','rgba(245,158,11,.09)',wn,t('guide_warning'))+safeRow('#fb923c','rgba(234,88,12,.09)',st,sg('safe_master'))+'</div></div>';}'''
rep(TS, TS + SAFE, 'SAFE block')

# ── 2) Celebration: insert the panel right after the stats grid ──
rep(
  "esc(t('stat_tags')) + '</span></div>' +\n        '</div>' +\n        buildPerfHtml() +",
  "esc(t('stat_tags')) + '</span></div>' +\n        '</div>' +\n        buildSafePanel() +\n        buildPerfHtml() +",
  'celebration panel')

# ── 3) Restore guide: replace the lone warning with the Safe Restore panel ──
GUIDE_OLD = ('\'<div class="jwrg-warning" id="jwrg-warning"><svg viewBox="0 0 24 24" width="16" height="16" '
  'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
  'aria-hidden="true"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'
  '<line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
  '<span>\' + esc(t(\'guide_warning\')) + \'</span></div>\'')
GUIDE_NEW = "'<div id=\"jwrg-warning\">' + buildSafePanel() + '</div>'"
rep(GUIDE_OLD, GUIDE_NEW, 'guide warning')

# ── 4) Version bump ──
rep('"softwareVersion": "2.57.0"', '"softwareVersion": "2.58.0"', 'version')

if c == orig:
    print('No changes!'); sys.exit(1)
io.open(f, 'w', encoding='utf-8').write(c)
print('Safe Restore layer added; file now', len(c), 'chars')

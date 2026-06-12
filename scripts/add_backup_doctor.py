# -*- coding: utf-8 -*-
"""Backup Doctor (v2.63.0) — a beautiful, private health check + one-click
repair for any .jwlibrary backup. Self-contained module (CSS + JS, .jbd-*
namespace), injected before the Collapsible-tool-sections block. Finds and
fixes: duplicate notes, empty notes, duplicate highlights, stray highlight
fragments, broken tag links, unused tags, leftover location records.
Localised in 12 languages. Entry: landing banner card + window.__openJwDoctor.
"""
import io, json, re, sys

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()
orig = c

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# 1) The module block
# ─────────────────────────────────────────────────────────────────────────────
BLOCK = r'''
<!-- ── Backup Doctor (v2.63.0) ───────────────────────────── -->
<style>
/* ── Landing CTA banner ── */
.jbd-cta{display:flex;align-items:center;gap:14px;width:100%;box-sizing:border-box;margin:14px 0 0;
  padding:15px 18px;text-align:left;cursor:pointer;font-family:inherit;
  background:rgba(4,15,34,.7);border:1px solid rgba(71,85,105,.4);border-radius:14px;
  transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease}
.jbd-cta:hover{border-color:rgba(234,88,12,.55);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.3)}
.jbd-cta-ic{flex:0 0 auto;width:42px;height:42px;border-radius:11px;display:flex;align-items:center;justify-content:center;
  background:rgba(234,88,12,.12);border:1px solid rgba(234,88,12,.4);color:#fb923c}
.jbd-cta-txt{flex:1 1 auto;min-width:0;display:flex;flex-direction:column;gap:3px}
.jbd-cta-title{display:flex;align-items:center;gap:8px;font:700 15px/1.2 inherit;color:#f1f5f9}
.jbd-new{font:800 9px/1 inherit;letter-spacing:.08em;color:#fff;background:#ea580c;border-radius:5px;padding:3px 6px}
.jbd-cta-desc{font:500 12.5px/1.45 inherit;color:#94a3b8}
.jbd-cta-arrow{flex:0 0 auto;color:#64748b;font-size:18px;transition:color .2s ease,transform .2s ease}
.jbd-cta:hover .jbd-cta-arrow{color:#fb923c;transform:translateX(3px)}
/* ── Overlay / card ── */
.jbd-overlay{position:fixed;inset:0;z-index:10090;display:flex;align-items:center;justify-content:center;padding:18px}
.jbd-backdrop{position:absolute;inset:0;background:rgba(4,15,34,.82);
  animation:modal-backdrop-blur .5s cubic-bezier(.16,1,.3,1) forwards}
.jbd-card{position:relative;z-index:1;width:100%;max-width:560px;max-height:calc(100vh - 36px);overflow-y:auto;
  padding:28px 26px 24px;background:linear-gradient(180deg,#0c1830,#06101f);
  border:1px solid rgba(234,88,12,.35);border-radius:18px;color:#f1f5f9;
  box-shadow:0 24px 80px rgba(0,0,0,.6),0 0 60px rgba(234,88,12,.12);
  animation:jwc-pop-in .4s cubic-bezier(.16,1,.3,1)}
.jbd-x{position:absolute;top:12px;right:12px;width:36px;height:36px;border:none;border-radius:10px;
  background:rgba(71,85,105,.3);color:#cbd5e1;font-size:20px;line-height:1;cursor:pointer;transition:background .15s}
.jbd-x:hover{background:rgba(71,85,105,.55)}
.jbd-head{display:flex;align-items:center;gap:13px;margin-bottom:18px;
  animation:modal-element-fade-slide .4s cubic-bezier(.16,1,.3,1) .05s both}
.jbd-head-ic{flex:0 0 auto;width:46px;height:46px;border-radius:12px;display:flex;align-items:center;justify-content:center;
  background:rgba(234,88,12,.13);border:1px solid rgba(234,88,12,.45);color:#fb923c}
.jbd-title{margin:0;font:800 20px/1.2 inherit;letter-spacing:-.01em}
.jbd-sub{margin:3px 0 0;font:500 12.5px/1.4 inherit;color:#94a3b8}
/* ── Pick state ── */
.jbd-pick-btn{display:flex;align-items:center;justify-content:center;gap:9px;width:100%;box-sizing:border-box;
  padding:15px 18px;background:#ea580c;border:none;border-radius:11px;color:#fff;font:700 14.5px/1 inherit;
  cursor:pointer;box-shadow:0 1px 5px rgba(234,88,12,.4);transition:all .2s ease;
  animation:modal-element-fade-slide .4s cubic-bezier(.16,1,.3,1) .15s both}
.jbd-pick-btn:hover{background:#f97316;transform:translateY(-2px);box-shadow:0 4px 12px rgba(234,88,12,.5)}
.jbd-use-last{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;box-sizing:border-box;
  margin-top:10px;padding:13px 16px;background:transparent;border:1px solid rgba(234,88,12,.5);border-radius:11px;
  color:#fdba74;font:600 13.5px/1.3 inherit;cursor:pointer;transition:all .2s ease;
  animation:modal-element-fade-slide .4s cubic-bezier(.16,1,.3,1) .22s both;word-break:break-all}
.jbd-use-last:hover{background:rgba(234,88,12,.1);color:#fff;border-color:#ea580c;transform:translateY(-1px)}
.jbd-priv{display:flex;align-items:center;justify-content:center;gap:7px;margin-top:16px;font:500 11.5px/1.4 inherit;color:#64748b;
  animation:modal-element-fade-slide .4s cubic-bezier(.16,1,.3,1) .3s both}
.jbd-priv-dot{width:6px;height:6px;border-radius:50%;background:#34d399;flex:0 0 auto}
/* ── Scan state ── */
.jbd-ecg-wrap{position:relative;height:74px;margin:4px 0 14px;overflow:hidden;border-radius:12px;
  background:rgba(4,15,34,.6);border:1px solid rgba(71,85,105,.35)}
.jbd-ecg{position:absolute;inset:0;width:100%;height:100%}
.jbd-ecg path{fill:none;stroke:#34d399;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;
  filter:drop-shadow(0 0 5px rgba(52,211,153,.6));
  stroke-dasharray:130 530;stroke-dashoffset:660;animation:jbd-ecg-run 2.2s linear infinite}
@keyframes jbd-ecg-run{to{stroke-dashoffset:0}}
.jbd-scan-file{font:600 12.5px/1.4 inherit;color:#94a3b8;text-align:center;margin:0 0 14px;word-break:break-all}
.jbd-rows{display:flex;flex-direction:column;gap:7px}
.jbd-row{display:flex;align-items:center;gap:10px;padding:10px 13px;border-radius:10px;
  background:rgba(71,85,105,.1);border:1px solid rgba(71,85,105,.25);
  opacity:0;transform:translateY(6px);transition:opacity .35s cubic-bezier(.16,1,.3,1),transform .35s cubic-bezier(.16,1,.3,1),border-color .3s,background .3s}
.jbd-row.jbd-on{opacity:1;transform:translateY(0)}
.jbd-row-label{flex:1 1 auto;font:600 13px/1.35 inherit;color:#cbd5e1}
.jbd-row-spin{flex:0 0 auto;width:15px;height:15px;border:2px solid rgba(148,163,184,.3);border-top-color:#fb923c;
  border-radius:50%;animation:jbd-spin .7s linear infinite}
@keyframes jbd-spin{to{transform:rotate(360deg)}}
.jbd-chip{flex:0 0 auto;display:inline-flex;align-items:center;gap:5px;font:700 12px/1 inherit;border-radius:7px;padding:5px 9px;
  animation:checkmark-bounce .45s cubic-bezier(.34,1.56,.64,1)}
.jbd-chip-ok{color:#34d399;background:rgba(16,185,129,.12)}
.jbd-chip-warn{color:#fbbf24;background:rgba(245,158,11,.13)}
.jbd-row-fixed{border-color:rgba(16,185,129,.35)!important;background:rgba(16,185,129,.07)!important}
/* ── Report state ── */
.jbd-ring-wrap{position:relative;width:128px;height:128px;margin:6px auto 4px}
.jbd-ring{width:100%;height:100%;transform:rotate(-90deg)}
.jbd-ring-bg{fill:none;stroke:rgba(71,85,105,.3);stroke-width:9}
.jbd-ring-fg{fill:none;stroke-width:9;stroke-linecap:round;transition:stroke-dashoffset 1.15s cubic-bezier(.34,.66,.66,1)}
.jbd-tier-a{stroke:#34d399;filter:drop-shadow(0 0 6px rgba(52,211,153,.5))}
.jbd-tier-b{stroke:#a3e635;filter:drop-shadow(0 0 6px rgba(163,230,53,.45))}
.jbd-tier-c{stroke:#fbbf24;filter:drop-shadow(0 0 6px rgba(245,158,11,.45))}
.jbd-tier-d{stroke:#f87171;filter:drop-shadow(0 0 6px rgba(248,113,113,.45))}
.jbd-ring-num{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.jbd-ring-num strong{font:800 34px/1 inherit;font-variant-numeric:tabular-nums;color:#f8fafc}
.jbd-ring-num span{font:600 10.5px/1 inherit;color:#64748b;margin-top:3px;letter-spacing:.06em;text-transform:uppercase}
.jbd-verdict{display:flex;justify-content:center;margin:8px 0 2px}
.jbd-verdict-pill{font:700 12.5px/1 inherit;border-radius:999px;padding:7px 16px}
.jbd-verdict-a{color:#34d399;background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.4)}
.jbd-verdict-b{color:#a3e635;background:rgba(163,230,53,.1);border:1px solid rgba(163,230,53,.35)}
.jbd-verdict-c{color:#fbbf24;background:rgba(245,158,11,.12);border:1px solid rgba(245,158,11,.4)}
.jbd-verdict-d{color:#f87171;background:rgba(248,113,113,.1);border:1px solid rgba(248,113,113,.4)}
.jbd-totals{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:16px 0;padding-bottom:16px;position:relative}
.jbd-totals::after{content:'';position:absolute;bottom:0;left:12%;right:12%;height:1px;
  background:linear-gradient(90deg,transparent 0%,rgba(71,85,105,.25) 50%,transparent 100%)}
.jbd-total{display:flex;flex-direction:column;align-items:center;gap:2px;padding:10px 4px;border-radius:10px;
  background:rgba(255,255,255,.035);border:1px solid rgba(255,255,255,.06)}
.jbd-total strong{font:800 17px/1.2 inherit;font-variant-numeric:tabular-nums;color:#f8fafc}
.jbd-total span{font:600 9.5px/1.2 inherit;color:#64748b;text-transform:uppercase;letter-spacing:.05em;text-align:center}
.jbd-issues-line{text-align:center;font:600 12.5px/1.4 inherit;color:#fbbf24;margin:0 0 12px}
.jbd-perfect{display:flex;align-items:center;justify-content:center;gap:9px;margin:0 0 14px;padding:13px 16px;border-radius:11px;
  color:#34d399;background:rgba(16,185,129,.09);border:1px solid rgba(16,185,129,.3);font:700 13.5px/1.4 inherit}
.jbd-clean-btn{display:flex;align-items:center;justify-content:center;gap:9px;width:100%;box-sizing:border-box;margin-top:14px;
  padding:15px 18px;background:#ea580c;border:none;border-radius:11px;color:#fff;font:700 14.5px/1 inherit;
  cursor:pointer;box-shadow:0 1px 5px rgba(234,88,12,.4);transition:all .2s ease}
.jbd-clean-btn:hover{background:#f97316;transform:translateY(-2px);box-shadow:0 4px 12px rgba(234,88,12,.5)}
.jbd-clean-btn:disabled{background:rgba(71,85,105,.4);color:#94a3b8;cursor:not-allowed;box-shadow:none;transform:none}
.jbd-safe{display:flex;align-items:flex-start;gap:8px;margin-top:12px;font:500 11.5px/1.5 inherit;color:#64748b}
.jbd-safe svg{flex:0 0 auto;margin-top:1px;color:#34d399}
.jbd-ghost-btn{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;box-sizing:border-box;margin-top:10px;
  padding:12px 16px;background:transparent;border:1px solid rgba(71,85,105,.5);border-radius:11px;
  color:#cbd5e1;font:600 13px/1 inherit;cursor:pointer;transition:all .2s ease}
.jbd-ghost-btn:hover{border-color:rgba(234,88,12,.5);color:#fff;background:rgba(234,88,12,.06)}
/* ── Done state ── */
.jbd-done-ic{width:58px;height:58px;border-radius:15px;margin:6px auto 14px;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;box-shadow:0 8px 24px rgba(34,197,94,.45);
  animation:jwc-icon-pop .5s cubic-bezier(.34,1.56,.64,1)}
.jbd-done-t{margin:0;text-align:center;font:800 19px/1.25 inherit}
.jbd-done-d{margin:6px 0 14px;text-align:center;font:500 13px/1.5 inherit;color:#94a3b8}
.jbd-size-row{display:flex;align-items:center;justify-content:center;gap:10px;margin:0 0 16px;font:700 14px/1 inherit;color:#cbd5e1}
.jbd-size-arrow{color:#64748b}
.jbd-size-pct{font:800 11.5px/1 inherit;color:#34d399;background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.4);
  border-radius:7px;padding:5px 9px}
.jbd-err{margin:8px 0 4px;padding:12px 15px;border-radius:10px;font:600 12.5px/1.5 inherit;color:#fca5a5;
  background:rgba(248,113,113,.08);border:1px solid rgba(248,113,113,.3)}
@media (max-width:520px){.jbd-card{padding:22px 16px 18px;border-radius:14px}.jbd-totals{gap:6px}}
@media (prefers-reduced-motion:reduce){.jbd-ecg path{animation:none}.jbd-ring-fg{transition:none}}
</style>
<script>
(function () {
  'use strict';
  var DOC_I18N = {
  en:{title:"Backup Doctor",sub:"A private health check for your backup",priv:"100% private — your file never leaves this device.",pick:"Choose a .jwlibrary file",use_last:"Check {name}",scanning:"Examining your backup…",c_dup_notes:"Duplicate notes",c_empty_notes:"Empty notes",c_dup_marks:"Duplicate highlights",c_orph_br:"Stray highlight fragments",c_orph_tm:"Broken tag links",c_unused_tags:"Unused tags",c_unused_loc:"Leftover location records",l_notes:"notes",l_marks:"highlights",l_bm:"bookmarks",l_tags:"tags",health:"Health score",v_a:"Excellent",v_b:"Good",v_c:"Fair",v_d:"Needs care",issues_one:"1 fixable issue found",issues_many:"{n} fixable issues found",perfect:"Perfect health — nothing to fix!",clean:"Clean & Download",cleaning:"Cleaning…",done_t:"All fixed!",done_d:"Your cleaned backup is downloading.",smaller:"smaller",safe:"Your original file is never changed — fixes go into a new copy.",another:"Check another file",close:"Close",err_read:"Could not read this backup — it may be corrupted or the wrong type of file.",err_db:"This backup is missing its notes database (userData.db)."},
  es:{title:"Doctor de Copias",sub:"Un chequeo privado para tu copia de seguridad",priv:"100% privado — tu archivo nunca sale de este dispositivo.",pick:"Elegir archivo .jwlibrary",use_last:"Revisar {name}",scanning:"Examinando tu copia…",c_dup_notes:"Notas duplicadas",c_empty_notes:"Notas vacías",c_dup_marks:"Subrayados duplicados",c_orph_br:"Fragmentos de subrayado sueltos",c_orph_tm:"Enlaces de etiqueta rotos",c_unused_tags:"Etiquetas sin usar",c_unused_loc:"Registros de ubicación sobrantes",l_notes:"notas",l_marks:"subrayados",l_bm:"marcadores",l_tags:"etiquetas",health:"Puntuación de salud",v_a:"Excelente",v_b:"Buena",v_c:"Regular",v_d:"Necesita atención",issues_one:"1 problema corregible encontrado",issues_many:"{n} problemas corregibles encontrados",perfect:"¡Salud perfecta — nada que corregir!",clean:"Limpiar y Descargar",cleaning:"Limpiando…",done_t:"¡Todo corregido!",done_d:"Tu copia limpia se está descargando.",smaller:"más pequeña",safe:"Tu archivo original nunca se modifica — las correcciones van a una copia nueva.",another:"Revisar otro archivo",close:"Cerrar",err_read:"No se pudo leer esta copia — puede estar dañada o ser un tipo de archivo incorrecto.",err_db:"A esta copia le falta su base de datos de notas (userData.db)."},
  pt:{title:"Doutor de Backup",sub:"Um exame privado para o seu backup",priv:"100% privado — seu arquivo nunca sai deste dispositivo.",pick:"Escolher arquivo .jwlibrary",use_last:"Examinar {name}",scanning:"Examinando seu backup…",c_dup_notes:"Notas duplicadas",c_empty_notes:"Notas vazias",c_dup_marks:"Destaques duplicados",c_orph_br:"Fragmentos de destaque soltos",c_orph_tm:"Vínculos de etiqueta quebrados",c_unused_tags:"Etiquetas sem uso",c_unused_loc:"Registros de local restantes",l_notes:"notas",l_marks:"destaques",l_bm:"marcadores",l_tags:"etiquetas",health:"Pontuação de saúde",v_a:"Excelente",v_b:"Boa",v_c:"Razoável",v_d:"Precisa de cuidado",issues_one:"1 problema corrigível encontrado",issues_many:"{n} problemas corrigíveis encontrados",perfect:"Saúde perfeita — nada para corrigir!",clean:"Limpar e Baixar",cleaning:"Limpando…",done_t:"Tudo corrigido!",done_d:"Seu backup limpo está sendo baixado.",smaller:"menor",safe:"Seu arquivo original nunca é alterado — as correções vão para uma nova cópia.",another:"Examinar outro arquivo",close:"Fechar",err_read:"Não foi possível ler este backup — pode estar corrompido ou ser o tipo errado de arquivo.",err_db:"Este backup está sem o banco de dados de notas (userData.db)."},
  fr:{title:"Docteur de Sauvegarde",sub:"Un bilan de santé privé pour votre sauvegarde",priv:"100 % privé — votre fichier ne quitte jamais cet appareil.",pick:"Choisir un fichier .jwlibrary",use_last:"Examiner {name}",scanning:"Examen de votre sauvegarde…",c_dup_notes:"Notes en double",c_empty_notes:"Notes vides",c_dup_marks:"Surlignages en double",c_orph_br:"Fragments de surlignage orphelins",c_orph_tm:"Liens d'étiquette cassés",c_unused_tags:"Étiquettes inutilisées",c_unused_loc:"Entrées de lieu superflues",l_notes:"notes",l_marks:"surlignages",l_bm:"signets",l_tags:"étiquettes",health:"Score de santé",v_a:"Excellent",v_b:"Bon",v_c:"Moyen",v_d:"À soigner",issues_one:"1 problème corrigeable trouvé",issues_many:"{n} problèmes corrigeables trouvés",perfect:"Santé parfaite — rien à corriger !",clean:"Nettoyer et Télécharger",cleaning:"Nettoyage…",done_t:"Tout est réparé !",done_d:"Votre sauvegarde nettoyée se télécharge.",smaller:"plus légère",safe:"Votre fichier d'origine n'est jamais modifié — les corrections vont dans une nouvelle copie.",another:"Examiner un autre fichier",close:"Fermer",err_read:"Impossible de lire cette sauvegarde — elle est peut-être corrompue ou du mauvais type.",err_db:"Cette sauvegarde n'a pas sa base de données de notes (userData.db)."},
  de:{title:"Backup-Doktor",sub:"Ein privater Gesundheitscheck für deine Sicherung",priv:"100 % privat — deine Datei verlässt dieses Gerät nie.",pick:".jwlibrary-Datei wählen",use_last:"{name} prüfen",scanning:"Deine Sicherung wird untersucht…",c_dup_notes:"Doppelte Notizen",c_empty_notes:"Leere Notizen",c_dup_marks:"Doppelte Markierungen",c_orph_br:"Verwaiste Markierungsfragmente",c_orph_tm:"Defekte Tag-Verknüpfungen",c_unused_tags:"Unbenutzte Tags",c_unused_loc:"Übrige Ortseinträge",l_notes:"Notizen",l_marks:"Markierungen",l_bm:"Lesezeichen",l_tags:"Tags",health:"Gesundheitswert",v_a:"Ausgezeichnet",v_b:"Gut",v_c:"Mittel",v_d:"Braucht Pflege",issues_one:"1 behebbares Problem gefunden",issues_many:"{n} behebbare Probleme gefunden",perfect:"Perfekte Gesundheit — nichts zu beheben!",clean:"Bereinigen & Herunterladen",cleaning:"Bereinige…",done_t:"Alles behoben!",done_d:"Deine bereinigte Sicherung wird heruntergeladen.",smaller:"kleiner",safe:"Deine Originaldatei wird nie verändert — Korrekturen kommen in eine neue Kopie.",another:"Weitere Datei prüfen",close:"Schließen",err_read:"Diese Sicherung konnte nicht gelesen werden — sie ist evtl. beschädigt oder der falsche Dateityp.",err_db:"Dieser Sicherung fehlt ihre Notizdatenbank (userData.db)."},
  it:{title:"Dottore dei Backup",sub:"Un controllo privato per il tuo backup",priv:"100% privato — il tuo file non lascia mai questo dispositivo.",pick:"Scegli file .jwlibrary",use_last:"Esamina {name}",scanning:"Esame del tuo backup…",c_dup_notes:"Note duplicate",c_empty_notes:"Note vuote",c_dup_marks:"Evidenziazioni duplicate",c_orph_br:"Frammenti di evidenziazione orfani",c_orph_tm:"Collegamenti di etichetta rotti",c_unused_tags:"Etichette inutilizzate",c_unused_loc:"Record di posizione residui",l_notes:"note",l_marks:"evidenziazioni",l_bm:"segnalibri",l_tags:"etichette",health:"Punteggio di salute",v_a:"Eccellente",v_b:"Buono",v_c:"Discreto",v_d:"Da curare",issues_one:"1 problema risolvibile trovato",issues_many:"{n} problemi risolvibili trovati",perfect:"Salute perfetta — niente da correggere!",clean:"Pulisci e Scarica",cleaning:"Pulizia…",done_t:"Tutto sistemato!",done_d:"Il tuo backup pulito è in download.",smaller:"più leggero",safe:"Il file originale non viene mai modificato — le correzioni vanno in una nuova copia.",another:"Esamina un altro file",close:"Chiudi",err_read:"Impossibile leggere questo backup — potrebbe essere danneggiato o del tipo sbagliato.",err_db:"A questo backup manca il database delle note (userData.db)."},
  ru:{title:"Доктор резервных копий",sub:"Приватная проверка здоровья вашей копии",priv:"100% приватно — файл никогда не покидает это устройство.",pick:"Выбрать файл .jwlibrary",use_last:"Проверить {name}",scanning:"Осматриваем вашу копию…",c_dup_notes:"Дубликаты заметок",c_empty_notes:"Пустые заметки",c_dup_marks:"Дубликаты выделений",c_orph_br:"Осиротевшие фрагменты выделений",c_orph_tm:"Битые связи тегов",c_unused_tags:"Неиспользуемые теги",c_unused_loc:"Лишние записи мест",l_notes:"заметки",l_marks:"выделения",l_bm:"закладки",l_tags:"теги",health:"Оценка здоровья",v_a:"Отлично",v_b:"Хорошо",v_c:"Средне",v_d:"Требует внимания",issues_one:"Найдена 1 исправимая проблема",issues_many:"Найдено исправимых проблем: {n}",perfect:"Идеальное здоровье — исправлять нечего!",clean:"Очистить и скачать",cleaning:"Очистка…",done_t:"Всё исправлено!",done_d:"Ваша очищенная копия скачивается.",smaller:"меньше",safe:"Исходный файл не изменяется — исправления попадают в новую копию.",another:"Проверить другой файл",close:"Закрыть",err_read:"Не удалось прочитать эту копию — возможно, она повреждена или неверного типа.",err_db:"В этой копии нет базы данных заметок (userData.db)."},
  ja:{title:"バックアップドクター",sub:"バックアップのプライベート健康診断",priv:"100%プライベート — ファイルがこの端末から出ることはありません。",pick:".jwlibraryファイルを選択",use_last:"{name} を診断",scanning:"バックアップを検査中…",c_dup_notes:"重複したメモ",c_empty_notes:"空のメモ",c_dup_marks:"重複したハイライト",c_orph_br:"孤立したハイライト断片",c_orph_tm:"壊れたタグリンク",c_unused_tags:"未使用のタグ",c_unused_loc:"残された場所レコード",l_notes:"メモ",l_marks:"ハイライト",l_bm:"ブックマーク",l_tags:"タグ",health:"健康スコア",v_a:"非常に良好",v_b:"良好",v_c:"普通",v_d:"要ケア",issues_one:"修復可能な問題が1件見つかりました",issues_many:"修復可能な問題が{n}件見つかりました",perfect:"完璧な状態 — 修復は不要です！",clean:"クリーンアップしてダウンロード",cleaning:"クリーンアップ中…",done_t:"すべて修復しました！",done_d:"クリーンなバックアップをダウンロード中です。",smaller:"削減",safe:"元のファイルは変更されません — 修復は新しいコピーに適用されます。",another:"別のファイルを診断",close:"閉じる",err_read:"このバックアップを読み込めませんでした — 破損しているか、ファイル形式が違う可能性があります。",err_db:"このバックアップにはメモのデータベース（userData.db）がありません。"},
  ko:{title:"백업 닥터",sub:"백업을 위한 프라이빗 건강 검진",priv:"100% 프라이빗 — 파일은 이 기기를 절대 벗어나지 않습니다.",pick:".jwlibrary 파일 선택",use_last:"{name} 검진하기",scanning:"백업을 검사하는 중…",c_dup_notes:"중복된 메모",c_empty_notes:"빈 메모",c_dup_marks:"중복된 하이라이트",c_orph_br:"고아 하이라이트 조각",c_orph_tm:"끊어진 태그 연결",c_unused_tags:"사용하지 않는 태그",c_unused_loc:"남은 위치 기록",l_notes:"메모",l_marks:"하이라이트",l_bm:"북마크",l_tags:"태그",health:"건강 점수",v_a:"최상",v_b:"양호",v_c:"보통",v_d:"관리 필요",issues_one:"수정 가능한 문제 1건 발견",issues_many:"수정 가능한 문제 {n}건 발견",perfect:"완벽한 상태 — 고칠 것이 없습니다!",clean:"정리 후 다운로드",cleaning:"정리 중…",done_t:"모두 수정했습니다!",done_d:"정리된 백업이 다운로드되고 있습니다.",smaller:"감소",safe:"원본 파일은 절대 변경되지 않습니다 — 수정 사항은 새 복사본에 적용됩니다.",another:"다른 파일 검진",close:"닫기",err_read:"이 백업을 읽을 수 없습니다 — 손상되었거나 잘못된 파일 형식일 수 있습니다.",err_db:"이 백업에는 메모 데이터베이스(userData.db)가 없습니다."},
  tl:{title:"Backup Doctor",sub:"Pribadong health check para sa iyong backup",priv:"100% pribado — hindi kailanman aalis ang iyong file sa device na ito.",pick:"Pumili ng .jwlibrary file",use_last:"Suriin ang {name}",scanning:"Sinusuri ang iyong backup…",c_dup_notes:"Mga duplicate na tala",c_empty_notes:"Mga walang lamang tala",c_dup_marks:"Mga duplicate na highlight",c_orph_br:"Mga ulilang piraso ng highlight",c_orph_tm:"Mga sirang tag link",c_unused_tags:"Mga hindi ginagamit na tag",c_unused_loc:"Mga natirang tala ng lokasyon",l_notes:"mga tala",l_marks:"mga highlight",l_bm:"mga bookmark",l_tags:"mga tag",health:"Health score",v_a:"Napakahusay",v_b:"Mabuti",v_c:"Katamtaman",v_d:"Kailangan ng pag-aalaga",issues_one:"1 maaayos na problema ang natagpuan",issues_many:"{n} maaayos na problema ang natagpuan",perfect:"Perpektong kalusugan — walang dapat ayusin!",clean:"Linisin at I-download",cleaning:"Naglilinis…",done_t:"Naayos na lahat!",done_d:"Dina-download na ang iyong malinis na backup.",smaller:"mas maliit",safe:"Hindi kailanman binabago ang orihinal mong file — ang mga pag-aayos ay napupunta sa bagong kopya.",another:"Suriin ang ibang file",close:"Isara",err_read:"Hindi mabasa ang backup na ito — maaaring sira o maling uri ng file.",err_db:"Walang notes database (userData.db) ang backup na ito."},
  sv:{title:"Backup-doktorn",sub:"En privat hälsokontroll för din säkerhetskopia",priv:"100 % privat — din fil lämnar aldrig den här enheten.",pick:"Välj .jwlibrary-fil",use_last:"Undersök {name}",scanning:"Undersöker din säkerhetskopia…",c_dup_notes:"Dubblerade anteckningar",c_empty_notes:"Tomma anteckningar",c_dup_marks:"Dubblerade överstrykningar",c_orph_br:"Övergivna överstrykningsfragment",c_orph_tm:"Trasiga tagglänkar",c_unused_tags:"Oanvända taggar",c_unused_loc:"Kvarblivna platsposter",l_notes:"anteckningar",l_marks:"överstrykningar",l_bm:"bokmärken",l_tags:"taggar",health:"Hälsopoäng",v_a:"Utmärkt",v_b:"Bra",v_c:"Okej",v_d:"Behöver omsorg",issues_one:"1 åtgärdbart problem hittades",issues_many:"{n} åtgärdbara problem hittades",perfect:"Perfekt hälsa — inget att åtgärda!",clean:"Rensa och ladda ner",cleaning:"Rensar…",done_t:"Allt åtgärdat!",done_d:"Din rensade säkerhetskopia laddas ner.",smaller:"mindre",safe:"Din originalfil ändras aldrig — åtgärderna hamnar i en ny kopia.",another:"Undersök en annan fil",close:"Stäng",err_read:"Kunde inte läsa den här säkerhetskopian — den kan vara skadad eller fel filtyp.",err_db:"Den här säkerhetskopian saknar sin anteckningsdatabas (userData.db)."},
  ceb:{title:"Backup Doctor",sub:"Pribadong health check para sa imong backup",priv:"100% pribado — dili gayud mogawas ang imong file niini nga device.",pick:"Pilia ang .jwlibrary file",use_last:"Susiha ang {name}",scanning:"Gisusi ang imong backup…",c_dup_notes:"Mga duplicate nga nota",c_empty_notes:"Mga walay sulod nga nota",c_dup_marks:"Mga duplicate nga highlight",c_orph_br:"Mga nabiyaan nga piraso sa highlight",c_orph_tm:"Mga naputol nga tag link",c_unused_tags:"Mga wala magamit nga tag",c_unused_loc:"Mga nahibilin nga rekord sa lokasyon",l_notes:"mga nota",l_marks:"mga highlight",l_bm:"mga bookmark",l_tags:"mga tag",health:"Health score",v_a:"Maayo kaayo",v_b:"Maayo",v_c:"Igo-igo",v_d:"Nagkinahanglan ug pag-atiman",issues_one:"1 ka maayos nga problema ang nakit-an",issues_many:"{n} ka maayos nga problema ang nakit-an",perfect:"Hingpit nga kahimsog — walay angay ayohon!",clean:"Limpyohi ug I-download",cleaning:"Naglimpyo…",done_t:"Naayo na ang tanan!",done_d:"Gi-download na ang imong limpyo nga backup.",smaller:"mas gamay",safe:"Dili gayud usbon ang imong orihinal nga file — ang mga pag-ayo moadto sa bag-ong kopya.",another:"Susiha ang laing file",close:"Sirado",err_read:"Dili mabasa kini nga backup — tingali nadaot o sayop nga klase sa file.",err_db:"Wala kini backup sa notes database (userData.db)."}
  };
  function lang(){ try{ return localStorage.getItem('jwsync_lang')||'en'; }catch(_){ return 'en'; } }
  function t(k){ var l=lang(); return (DOC_I18N[l]&&DOC_I18N[l][k])||DOC_I18N.en[k]||k; }
  function esc(s){ return String(s==null?'':s).replace(/[&<>"']/g,function(ch){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]; }); }
  function fmtSize(b){ if(!b&&b!==0) return ''; if(b>=1048576) return (b/1048576).toFixed(1)+' MB'; if(b>=1024) return Math.round(b/1024)+' KB'; return b+' B'; }

  var SQLJS_CDN='https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/';
  function ensureDeps(){
    var boot = (typeof window.__jwBootBrowse==='function') ? window.__jwBootBrowse().catch(function(){}) : Promise.resolve();
    return boot.then(function(){
      if(window.JSZip && window.initSqlJs) return;
      function load(src){ return new Promise(function(res,rej){ var s=document.createElement('script'); s.src=src; s.async=true; s.crossOrigin='anonymous'; s.onload=res; s.onerror=rej; document.head.appendChild(s); }); }
      var p=[];
      if(!window.JSZip) p.push(load('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'));
      if(!window.initSqlJs) p.push(load(SQLJS_CDN+'sql-wasm.js'));
      return Promise.all(p);
    });
  }

  // ── SQL helpers ─────────────────────────────────────────────────────
  function q(db,sql){ var out=[],st=db.prepare(sql); try{ while(st.step()) out.push(st.getAsObject()); } finally { st.free(); } return out; }
  function qv(db,sql){ var r=q(db,sql); if(!r.length) return 0; var k=Object.keys(r[0])[0]; return r[0][k]||0; }
  function col1(db,sql){ var st=db.prepare(sql),out=[]; try{ while(st.step()) out.push(st.get()[0]); } finally { st.free(); } return out; }
  function hasTable(db,n){ return qv(db,"SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='"+n+"'")>0; }
  function hasCol(db,tbl,cname){ try{ return q(db,'PRAGMA table_info('+tbl+')').some(function(r){ return r.name===cname; }); }catch(_){ return false; } }

  // ── Health checks ───────────────────────────────────────────────────
  var CHECKS=['dup_notes','empty_notes','dup_marks','orph_br','orph_tm','unused_tags','unused_loc'];
  var WEIGHTS={dup_notes:1.2,empty_notes:.4,dup_marks:.8,orph_br:.15,orph_tm:.15,unused_tags:.3,unused_loc:.02};

  function idsFor(db,key){
    switch(key){
      case 'dup_notes':
        if(!hasTable(db,'Note')) return [];
        return col1(db,
          "SELECT NoteId FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'') AND NoteId NOT IN ("+
          " SELECT MIN(NoteId) FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'')"+
          " GROUP BY IFNULL(Title,''), IFNULL(Content,''), IFNULL(LocationId,-1))");
      case 'empty_notes':
        if(!hasTable(db,'Note')) return [];
        return col1(db,"SELECT NoteId FROM Note WHERE TRIM(IFNULL(Title,''))='' AND TRIM(IFNULL(Content,''))=''");
      case 'dup_marks':
        if(!hasTable(db,'UserMark')||!hasTable(db,'BlockRange')) return [];
        return col1(db,
          "SELECT DISTINCT um2.UserMarkId FROM UserMark um1"+
          " JOIN UserMark um2 ON um2.UserMarkId>um1.UserMarkId"+
          "  AND IFNULL(um2.LocationId,-1)=IFNULL(um1.LocationId,-1)"+
          "  AND IFNULL(um2.ColorIndex,-1)=IFNULL(um1.ColorIndex,-1)"+
          " JOIN BlockRange b1 ON b1.UserMarkId=um1.UserMarkId"+
          " JOIN BlockRange b2 ON b2.UserMarkId=um2.UserMarkId"+
          "  AND IFNULL(b2.BlockType,-1)=IFNULL(b1.BlockType,-1)"+
          "  AND IFNULL(b2.Identifier,-1)=IFNULL(b1.Identifier,-1)"+
          "  AND IFNULL(b2.StartToken,-1)=IFNULL(b1.StartToken,-1)"+
          "  AND IFNULL(b2.EndToken,-1)=IFNULL(b1.EndToken,-1)"+
          " WHERE (SELECT COUNT(*) FROM BlockRange WHERE UserMarkId=um1.UserMarkId)=1"+
          "  AND (SELECT COUNT(*) FROM BlockRange WHERE UserMarkId=um2.UserMarkId)=1"+
          "  AND um2.UserMarkId NOT IN (SELECT IFNULL(UserMarkId,-1) FROM Note)");
      case 'orph_br':
        if(!hasTable(db,'BlockRange')||!hasTable(db,'UserMark')) return [];
        return col1(db,"SELECT BlockRangeId FROM BlockRange WHERE UserMarkId NOT IN (SELECT UserMarkId FROM UserMark)");
      case 'orph_tm':
        if(!hasTable(db,'TagMap')||!hasTable(db,'Note')) return [];
        return col1(db,"SELECT TagMapId FROM TagMap WHERE NoteId IS NOT NULL AND NoteId NOT IN (SELECT NoteId FROM Note)");
      case 'unused_tags':
        if(!hasTable(db,'Tag')) return [];
        var typeFilter = hasCol(db,'Tag','Type') ? "IFNULL(Type,1)=1 AND " : "";
        var tmRef = hasTable(db,'TagMap') ? " AND TagId NOT IN (SELECT DISTINCT TagId FROM TagMap WHERE TagId IS NOT NULL)" : "";
        return col1(db,"SELECT TagId FROM Tag WHERE "+typeFilter+"1=1"+tmRef);
      case 'unused_loc':
        if(!hasTable(db,'Location')) return [];
        var refs=[];
        [['Note','LocationId'],['UserMark','LocationId'],['Bookmark','LocationId'],['Bookmark','PublicationLocationId'],
         ['TagMap','LocationId'],['InputField','LocationId'],['PlaylistItemLocationMap','LocationId'],['PlaylistMedia','LocationId']
        ].forEach(function(tc){ if(hasTable(db,tc[0])&&hasCol(db,tc[0],tc[1])) refs.push('SELECT '+tc[1]+' FROM '+tc[0]+' WHERE '+tc[1]+' IS NOT NULL'); });
        if(!refs.length) return [];
        return col1(db,'SELECT LocationId FROM Location WHERE LocationId NOT IN ('+refs.join(' UNION ')+')');
      default: return [];
    }
  }

  function runChecks(db){
    var res={checks:{},totals:{},score:100,issues:0};
    res.totals.notes = hasTable(db,'Note')?qv(db,'SELECT COUNT(*) FROM Note'):0;
    res.totals.marks = hasTable(db,'UserMark')?qv(db,'SELECT COUNT(*) FROM UserMark'):0;
    res.totals.bm    = hasTable(db,'Bookmark')?qv(db,'SELECT COUNT(*) FROM Bookmark'):0;
    res.totals.tags  = hasTable(db,'Tag')?qv(db,'SELECT COUNT(*) FROM Tag'):0;
    var pen=0;
    CHECKS.forEach(function(k){
      var n=0; try{ n=idsFor(db,k).length; }catch(_){ n=0; }
      res.checks[k]=n; res.issues+=n; pen+=n*WEIGHTS[k];
    });
    res.score = res.issues===0 ? 100 : Math.max(35, Math.min(99, Math.round(100-pen)));
    return res;
  }

  function delNotes(db, ids){
    if(!ids.length) return;
    var list=ids.join(',');
    if(hasTable(db,'TagMap')) db.run('DELETE FROM TagMap WHERE NoteId IN ('+list+')');
    db.run('DELETE FROM Note WHERE NoteId IN ('+list+')');
  }
  function delMarks(db, ids){
    if(!ids.length) return;
    var list=ids.join(',');
    if(hasTable(db,'BlockRange')) db.run('DELETE FROM BlockRange WHERE UserMarkId IN ('+list+')');
    db.run('DELETE FROM UserMark WHERE UserMarkId IN ('+list+')');
  }
  function applyFixes(db){
    var fixed={};
    var dn=idsFor(db,'dup_notes');   delNotes(db,dn); fixed.dup_notes=dn.length;
    var en=idsFor(db,'empty_notes'); delNotes(db,en); fixed.empty_notes=en.length;
    var dm=idsFor(db,'dup_marks');   delMarks(db,dm); fixed.dup_marks=dm.length;
    var ob=idsFor(db,'orph_br');     if(ob.length) db.run('DELETE FROM BlockRange WHERE BlockRangeId IN ('+ob.join(',')+')'); fixed.orph_br=ob.length;
    var ot=idsFor(db,'orph_tm');     if(ot.length) db.run('DELETE FROM TagMap WHERE TagMapId IN ('+ot.join(',')+')'); fixed.orph_tm=ot.length;
    var ut=idsFor(db,'unused_tags'); if(ut.length) db.run('DELETE FROM Tag WHERE TagId IN ('+ut.join(',')+')'); fixed.unused_tags=ut.length;
    var ul=idsFor(db,'unused_loc');  if(ul.length) db.run('DELETE FROM Location WHERE LocationId IN ('+ul.join(',')+')'); fixed.unused_loc=ul.length;
    try{ db.run('VACUUM'); }catch(_){}
    return fixed;
  }

  // ── File loading ────────────────────────────────────────────────────
  function loadDb(file){
    var name=(file&&file.name)||'backup.jwlibrary';
    var size=(file&&(file.size||file.byteLength))||0;
    var zipRef=null;
    return ensureDeps()
      .then(function(){ return window.JSZip.loadAsync(file).catch(function(){ throw {code:'read'}; }); })
      .then(function(zip){
        zipRef=zip;
        var dbKey=Object.keys(zip.files).find(function(k){ return /userdata\.db$/i.test(k); });
        if(!dbKey) throw {code:'db'};
        return zip.files[dbKey].async('uint8array').then(function(bytes){ return {bytes:bytes,dbKey:dbKey}; });
      })
      .then(function(r){
        return window.initSqlJs({locateFile:function(fn){ return SQLJS_CDN+fn; }}).then(function(SQL){
          var db;
          try{ db=new SQL.Database(r.bytes); qv(db,'SELECT COUNT(*) FROM sqlite_master'); }
          catch(_){ throw {code:'read'}; }
          return {db:db, zip:zipRef, dbKey:r.dbKey, name:name, size:size};
        });
      });
  }

  function exportCleaned(st){
    var bytes=st.db.export();
    st.zip.file(st.dbKey, bytes);
    var mf=st.zip.file('manifest.json');
    var p = mf ? mf.async('string').then(function(s){
      try{
        var raw=JSON.parse(s);
        raw.creationDate=new Date().toISOString();
        raw.name=(raw.name||'Backup')+' (Cleaned)';
        st.zip.file('manifest.json', JSON.stringify(raw,null,2));
      }catch(_){}
    }) : Promise.resolve();
    return p.then(function(){
      return st.zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}});
    }).then(function(blob){
      try{
        var url=URL.createObjectURL(blob);
        var a=document.createElement('a');
        a.href=url; a.download='healthy_'+(st.name||'backup.jwlibrary');
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function(){ URL.revokeObjectURL(url); },4000);
      }catch(_){}
      return blob;
    });
  }

  // ── UI ──────────────────────────────────────────────────────────────
  var ICON_HEART='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></svg>';
  var ICON_CHECK='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>';
  var ICON_SHIELD='<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>';
  var ICON_BROOM='<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m13 11 9-9"/><path d="M14.6 12.6c.8.8.9 2 .2 2.8l-1.4 1.4a8 8 0 0 1-11.2 0 8 8 0 0 1 0-11.2l1.4-1.4c.8-.7 2-.6 2.8.2Z"/></svg>';

  var cur=null; // {overlay, db, zip, dbKey, name, size, report}

  function closeDoctor(){
    if(!cur) return;
    try{ if(cur.db) cur.db.close(); }catch(_){}
    if(cur.overlay) cur.overlay.remove();
    document.removeEventListener('keydown', onKey);
    cur=null;
  }
  function onKey(e){ if(e.key==='Escape') closeDoctor(); }

  function shell(){
    var ov=document.createElement('div');
    ov.className='jbd-overlay';
    ov.innerHTML=
      '<div class="jbd-backdrop" data-jbd-close></div>'+
      '<div class="jbd-card" role="dialog" aria-modal="true" aria-labelledby="jbd-title">'+
        '<button class="jbd-x" type="button" data-jbd-close aria-label="'+esc(t('close'))+'">×</button>'+
        '<div class="jbd-head">'+
          '<div class="jbd-head-ic">'+ICON_HEART+'</div>'+
          '<div><h2 class="jbd-title" id="jbd-title">'+esc(t('title'))+'</h2>'+
          '<p class="jbd-sub">'+esc(t('sub'))+'</p></div>'+
        '</div>'+
        '<div class="jbd-body"></div>'+
      '</div>';
    document.body.appendChild(ov);
    ov.querySelectorAll('[data-jbd-close]').forEach(function(el){
      el.addEventListener('click', closeDoctor);
    });
    document.addEventListener('keydown', onKey);
    return ov;
  }
  function body(){ return cur && cur.overlay.querySelector('.jbd-body'); }

  function renderPick(){
    var last=window.__jwLastFile;
    var b=body();
    b.innerHTML=
      '<button class="jbd-pick-btn" type="button" data-jbd-pick>'+ICON_HEART+' <span>'+esc(t('pick'))+'</span></button>'+
      (last&&last.name ? '<button class="jbd-use-last" type="button" data-jbd-last>'+esc(t('use_last').replace('{name}', last.name))+'</button>' : '')+
      '<div class="jbd-priv"><span class="jbd-priv-dot"></span><span>'+esc(t('priv'))+'</span></div>';
    var pick=b.querySelector('[data-jbd-pick]');
    pick.addEventListener('click', function(){
      var inp=document.createElement('input');
      inp.type='file'; inp.accept='.jwlibrary';
      inp.addEventListener('change', function(){ if(inp.files&&inp.files[0]) startScan(inp.files[0]); });
      inp.click();
    });
    var lastBtn=b.querySelector('[data-jbd-last]');
    if(lastBtn) lastBtn.addEventListener('click', function(){ startScan(window.__jwLastFile); });
  }

  function renderError(code){
    var b=body();
    b.innerHTML=
      '<div class="jbd-err">'+esc(t(code==='db'?'err_db':'err_read'))+'</div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';
    b.querySelector('[data-jbd-again]').addEventListener('click', renderPick);
  }

  function startScan(file){
    var b=body();
    var rows=CHECKS.map(function(k){
      return '<div class="jbd-row" data-jbd-row="'+k+'">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-row-state"></span>'+
      '</div>';
    }).join('');
    b.innerHTML=
      '<div class="jbd-ecg-wrap"><svg class="jbd-ecg" viewBox="0 0 560 74" preserveAspectRatio="none">'+
        '<path d="M0,40 L120,40 L138,40 L146,16 L154,58 L162,30 L170,40 L300,40 L318,40 L326,16 L334,58 L342,30 L350,40 L560,40"/>'+
      '</svg></div>'+
      '<p class="jbd-scan-file">'+esc(t('scanning'))+' · '+esc((file&&file.name)||'backup.jwlibrary')+'</p>'+
      '<div class="jbd-rows">'+rows+'</div>';
    loadDb(file).then(function(st){
      cur.db=st.db; cur.zip=st.zip; cur.dbKey=st.dbKey; cur.name=st.name; cur.size=st.size;
      // progressive reveal: one check at a time
      var report={checks:{},totals:{},score:100,issues:0};
      report.totals.notes = hasTable(st.db,'Note')?qv(st.db,'SELECT COUNT(*) FROM Note'):0;
      report.totals.marks = hasTable(st.db,'UserMark')?qv(st.db,'SELECT COUNT(*) FROM UserMark'):0;
      report.totals.bm    = hasTable(st.db,'Bookmark')?qv(st.db,'SELECT COUNT(*) FROM Bookmark'):0;
      report.totals.tags  = hasTable(st.db,'Tag')?qv(st.db,'SELECT COUNT(*) FROM Tag'):0;
      var pen=0, i=0;
      function step(){
        if(!cur) return;
        if(i>=CHECKS.length){
          report.score = report.issues===0 ? 100 : Math.max(35, Math.min(99, Math.round(100-pen)));
          cur.report=report;
          setTimeout(function(){ if(cur) renderReport(); }, 420);
          return;
        }
        var k=CHECKS[i++];
        var row=b.querySelector('[data-jbd-row="'+k+'"]');
        if(row){ row.classList.add('jbd-on'); var stEl=row.querySelector('.jbd-row-state'); stEl.innerHTML='<span class="jbd-row-spin"></span>'; }
        setTimeout(function(){
          if(!cur) return;
          var n=0; try{ n=idsFor(cur.db,k).length; }catch(_){ n=0; }
          report.checks[k]=n; report.issues+=n; pen+=n*WEIGHTS[k];
          if(row){
            var stEl=row.querySelector('.jbd-row-state');
            stEl.innerHTML = n===0
              ? '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+'</span>'
              : '<span class="jbd-chip jbd-chip-warn">'+n+'</span>';
          }
          setTimeout(step, 140);
        }, 170);
      }
      step();
    }).catch(function(e){ if(cur) renderError(e&&e.code); });
  }

  function tier(score){ return score>=97?'a':score>=85?'b':score>=65?'c':'d'; }

  function renderReport(){
    var r=cur.report, b=body();
    var C=326.7, tr=tier(r.score);
    var rows=CHECKS.map(function(k){
      var n=r.checks[k]||0;
      return '<div class="jbd-row jbd-on" data-jbd-row="'+k+'">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-row-state">'+(n===0
          ? '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+'</span>'
          : '<span class="jbd-chip jbd-chip-warn">'+n+'</span>')+'</span>'+
      '</div>';
    }).join('');
    b.innerHTML=
      '<div class="jbd-ring-wrap">'+
        '<svg class="jbd-ring" viewBox="0 0 120 120">'+
          '<circle class="jbd-ring-bg" cx="60" cy="60" r="52"/>'+
          '<circle class="jbd-ring-fg jbd-tier-'+tr+'" cx="60" cy="60" r="52" stroke-dasharray="'+C+'" stroke-dashoffset="'+C+'"/>'+
        '</svg>'+
        '<div class="jbd-ring-num"><strong>0</strong><span>'+esc(t('health'))+'</span></div>'+
      '</div>'+
      '<div class="jbd-verdict"><span class="jbd-verdict-pill jbd-verdict-'+tr+'">'+esc(t('v_'+tr))+'</span></div>'+
      '<div class="jbd-totals">'+
        '<div class="jbd-total"><strong>'+r.totals.notes+'</strong><span>'+esc(t('l_notes'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.marks+'</strong><span>'+esc(t('l_marks'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.bm+'</strong><span>'+esc(t('l_bm'))+'</span></div>'+
        '<div class="jbd-total"><strong>'+r.totals.tags+'</strong><span>'+esc(t('l_tags'))+'</span></div>'+
      '</div>'+
      (r.issues>0
        ? '<p class="jbd-issues-line">'+esc((r.issues===1?t('issues_one'):t('issues_many')).replace('{n}', r.issues))+'</p>'
        : '<div class="jbd-perfect">'+ICON_CHECK+' '+esc(t('perfect'))+'</div>')+
      '<div class="jbd-rows">'+rows+'</div>'+
      (r.issues>0 ? '<button class="jbd-clean-btn" type="button" data-jbd-clean>'+ICON_BROOM+' <span>'+esc(t('clean'))+'</span></button>' : '')+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';

    // animate ring + score count-up
    var fg=b.querySelector('.jbd-ring-fg'), num=b.querySelector('.jbd-ring-num strong');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){
      if(fg) fg.style.strokeDashoffset=(C*(1-r.score/100)).toFixed(1);
    }); });
    var elapsed=0, dur=1100;
    var iv=setInterval(function(){
      elapsed+=16;
      var p=Math.min(elapsed/dur,1), ease=1-Math.pow(1-p,4);
      if(num) num.textContent=Math.round(r.score*ease);
      if(p>=1) clearInterval(iv);
    },16);

    var cleanBtn=b.querySelector('[data-jbd-clean]');
    if(cleanBtn) cleanBtn.addEventListener('click', function(){
      cleanBtn.disabled=true;
      cleanBtn.innerHTML='<span class="jbd-row-spin" style="border-top-color:#fff"></span> <span>'+esc(t('cleaning'))+'</span>';
      setTimeout(function(){
        if(!cur) return;
        try{
          var fixed=applyFixes(cur.db);
          exportCleaned(cur).then(function(blob){
            if(cur) renderDone(fixed, blob?blob.size:0);
          }).catch(function(){ if(cur) renderDone(fixed, 0); });
        }catch(_){ renderError('read'); }
      }, 60);
    });
    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function renderDone(fixed, newSize){
    var b=body();
    var fixedRows=CHECKS.filter(function(k){ return fixed[k]>0; }).map(function(k){
      return '<div class="jbd-row jbd-on jbd-row-fixed">'+
        '<span class="jbd-row-label">'+esc(t('c_'+k))+'</span>'+
        '<span class="jbd-chip jbd-chip-ok">'+ICON_CHECK+' '+fixed[k]+'</span>'+
      '</div>';
    }).join('');
    var sizeRow='';
    if(cur.size>0 && newSize>0 && newSize<cur.size){
      var pct=Math.round((1-newSize/cur.size)*100);
      sizeRow='<div class="jbd-size-row"><span>'+fmtSize(cur.size)+'</span><span class="jbd-size-arrow">→</span><span>'+fmtSize(newSize)+'</span>'+
        (pct>=1?'<span class="jbd-size-pct">↓ '+pct+'% '+esc(t('smaller'))+'</span>':'')+'</div>';
    }
    b.innerHTML=
      '<div class="jbd-done-ic"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>'+
      '<h3 class="jbd-done-t">'+esc(t('done_t'))+'</h3>'+
      '<p class="jbd-done-d">'+esc(t('done_d'))+'</p>'+
      sizeRow+
      '<div class="jbd-rows">'+fixedRows+'</div>'+
      '<div class="jbd-safe">'+ICON_SHIELD+'<span>'+esc(t('safe'))+'</span></div>'+
      '<button class="jbd-ghost-btn" type="button" data-jbd-again>'+esc(t('another'))+'</button>';
    b.querySelector('[data-jbd-again]').addEventListener('click', function(){
      try{ if(cur.db) cur.db.close(); }catch(_){}
      cur.db=null; cur.zip=null; cur.report=null;
      renderPick();
    });
  }

  function openDoctor(file){
    closeDoctor();
    cur={overlay:shell(), db:null, zip:null, dbKey:null, name:null, size:0, report:null};
    if(file) startScan(file); else renderPick();
  }

  window.__openJwDoctor = openDoctor;
  window.__jwDoctorInternals = { runChecks:runChecks, applyFixes:applyFixes, idsFor:idsFor };
})();
</script>
<!-- ── End Backup Doctor ─────────────────────────────────── -->
'''

ANCHOR_BLOCK = '<!-- ── Collapsible tool sections (Extract / Bulk Color / Manage Tags) v2.62.0 ── -->'
must(c.count(ANCHOR_BLOCK) == 1, 'collapsible block anchor not unique')
c = c.replace(ANCHOR_BLOCK, BLOCK.strip() + '\n\n' + ANCHOR_BLOCK, 1)

# ─────────────────────────────────────────────────────────────────────────────
# 2) Landing CTA banner (below the svc-grid, above the secondary CTA row)
# ─────────────────────────────────────────────────────────────────────────────
CTA = '''        <button type="button" class="jbd-cta" id="jbd-cta" onclick="window.__openJwDoctor&amp;&amp;window.__openJwDoctor()">
          <span class="jbd-cta-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></svg></span>
          <span class="jbd-cta-txt">
            <span class="jbd-cta-title"><span data-i18n="svc_doctor_t">Backup Doctor</span><span class="jbd-new">NEW</span></span>
            <span class="jbd-cta-desc" data-i18n="svc_doctor_d">Free health check — find and fix duplicates, empty notes and clutter.</span>
          </span>
          <span class="jbd-cta-arrow">&#8594;</span>
        </button>
'''
CTA_ANCHOR = '        <div class="cta-row svc-secondary">'
must(c.count(CTA_ANCHOR) == 1, 'cta-row anchor not unique')
c = c.replace(CTA_ANCHOR, CTA + CTA_ANCHOR, 1)

# ─────────────────────────────────────────────────────────────────────────────
# 3) Landing i18n: add svc_doctor_t / svc_doctor_d to all 12 languages
# ─────────────────────────────────────────────────────────────────────────────
DOCTOR_LANDING = {
 'en': ("Backup Doctor", "Free health check — find and fix duplicates, empty notes and clutter."),
 'es': ("Doctor de Copias", "Chequeo gratuito: encuentra y corrige duplicados, notas vacías y desorden."),
 'pt': ("Doutor de Backup", "Exame gratuito: encontre e corrija duplicados, notas vazias e acúmulos."),
 'fr': ("Docteur de Sauvegarde", "Bilan de santé gratuit : trouvez et corrigez doublons, notes vides et encombrement."),
 'de': ("Backup-Doktor", "Kostenloser Gesundheitscheck — findet und behebt Duplikate, leere Notizen und Ballast."),
 'it': ("Dottore dei Backup", "Controllo gratuito: trova e corregge duplicati, note vuote e disordine."),
 'ru': ("Доктор резервных копий", "Бесплатная проверка: находит и устраняет дубликаты, пустые заметки и мусор."),
 'ja': ("バックアップドクター", "無料ヘルスチェック — 重複や空のメモ、不要データを見つけて修復。"),
 'ko': ("백업 닥터", "무료 건강 검진 — 중복, 빈 메모, 불필요한 데이터를 찾아 정리합니다."),
 'tl': ("Backup Doctor", "Libreng health check — hanapin at ayusin ang mga duplicate, walang lamang tala, at kalat."),
 'sv': ("Backup-doktorn", "Gratis hälsokontroll — hitta och åtgärda dubbletter, tomma anteckningar och skräp."),
 'ceb': ("Backup Doctor", "Libre nga health check — pangitaa ug ayoha ang mga duplicate, walay sulod nga nota, ug kalat."),
}
m = re.search(r'window\.__JW_LANDING_I18N = (\{.*?\});\n', c, re.DOTALL)
must(m is not None, '__JW_LANDING_I18N not found')
landing = json.loads(m.group(1))
must(len(landing) == 12, 'landing i18n does not have 12 languages (has %d)' % len(landing))
for lg, (title, desc) in DOCTOR_LANDING.items():
    must(lg in landing, 'landing i18n missing lang ' + lg)
    landing[lg]['svc_doctor_t'] = title
    landing[lg]['svc_doctor_d'] = desc
new_json = json.dumps(landing, ensure_ascii=False, separators=(',', ': '))
c = c[:m.start(1)] + new_json + c[m.end(1):]

# ─────────────────────────────────────────────────────────────────────────────
# 4) Version bump
# ─────────────────────────────────────────────────────────────────────────────
must(c.count('"softwareVersion": "2.62.0"') == 1, 'version anchor')
c = c.replace('"softwareVersion": "2.62.0"', '"softwareVersion": "2.63.0"', 1)

must(c != orig, 'no changes made')
io.open(f, 'w', encoding='utf-8').write(c)
print('Backup Doctor added; file now', len(c), 'chars')

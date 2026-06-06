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

# 1. Module cache vars before achievementsHtml
R(
    '    function achievementsHtml(s){',
    '    var __achCache = null, __curTCache = 0;\n    function achievementsHtml(s){',
    'module cache vars'
)

# 2. Cache assignment after A and curT are computed
R(
    "      var A = buildAchievements(s); if (!A.length) return '';\n      var loc = getLang(), curT = journeyData(s).tierIdx;",
    "      var A = buildAchievements(s); if (!A.length) return '';\n      var loc = getLang(), curT = journeyData(s).tierIdx;\n      __achCache = A; __curTCache = curT;",
    'cache assignment'
)

# 3. Shape class on medals
R(
    "          if (a.secret) cls += ' jww-secret';\n          var nm = mystery",
    "          if (a.secret) cls += ' jww-secret';\n          if (a.shape) cls += ' jww-shape-' + a.shape;\n          var nm = mystery",
    'shape class on medals'
)

# 4. AP badge + data-seq on medal div (put cabinet INSIDE wall before closing tag)
R(
    "          var tip = mystery ? t('ach_secret_hint') : (a.name + ' · ' + t(ACH_RARKEY[a.rarity]));\n"
    "          body += '<div class=\"' + cls + '\" data-state=\"' + (on ? 'earned' : 'locked') + '\" title=\"' + esc(tip) + '\" style=\"' + cstyle + '\"><div class=\"jww-medal-disc\">' + disc + '</div><div class=\"jww-medal-name\">' + esc(nm) + '</div>' + prog + '</div>';",
    "          var tip = mystery ? t('ach_secret_hint') : (a.name + ' · ' + t(ACH_RARKEY[a.rarity]));\n"
    "          var apBadge = (on && a.rarity > 0) ? '<span class=\"jww-ap\">+' + (ACH_RENOWN[a.rarity] || 0) + '</span>' : '';\n"
    "          body += '<div class=\"' + cls + '\" data-seq=\"' + a.seq + '\" data-state=\"' + (on ? 'earned' : 'locked') + '\" title=\"' + esc(tip) + '\" style=\"' + cstyle + '\"><div class=\"jww-medal-disc\">' + disc + apBadge + '</div><div class=\"jww-medal-name\">' + esc(nm) + '</div>' + prog + '</div>';",
    'AP badge + data-seq'
)

# 5. Cabinet call INSIDE .jww-ach-wall (before closing tag), then return
R(
    "      body += '</div>';\n"
    "      return section(IC.trophy, fmt2(t('ach_title'), earned + '/' + total), body);",
    "      body += cabinetHtml(A, curT);\n"
    "      body += '</div>';\n"
    "      return section(IC.trophy, fmt2(t('ach_title'), earned + '/' + total), body);",
    'cabinet call'
)

# 6. Add cabinetHtml, openMedalPopup, wireAchMedals after wireAchFilters
old6 = (
    "        wall.classList.remove('jww-flt-all','jww-flt-earned','jww-flt-locked');\n"
    "        wall.classList.add('jww-flt-' + flt);\n"
    "        wall.classList.toggle('jww-allopen', flt !== 'all'); // reveal matches across all shelves while filtering\n"
    "      }); });\n"
    "    }\n"
)
new6 = (
    "        wall.classList.remove('jww-flt-all','jww-flt-earned','jww-flt-locked');\n"
    "        wall.classList.add('jww-flt-' + flt);\n"
    "        wall.classList.toggle('jww-allopen', flt !== 'all'); // reveal matches across all shelves while filtering\n"
    "      }); });\n"
    "    }\n"
    "    function cabinetHtml(A, curT){\n"
    "      var rare = A.filter(function(a){ return a.rarity >= 2 && a.tier <= curT && a.on; });\n"
    "      if (!rare.length) return '';\n"
    "      var items = rare.map(function(a){\n"
    "        var col = achColor(a);\n"
    "        var cstyle = col ? '--mc:' + col[0] + ';--mc2:' + col[1] : '';\n"
    "        var shcls = a.shape ? ' jww-shape-' + a.shape : '';\n"
    "        return '<div class=\"jww-cab-medal' + shcls + '\" data-seq=\"' + a.seq + '\" style=\"' + cstyle + '\" title=\"' + esc(a.name) + '\"><div class=\"jww-cab-disc\">' + a.icon + '</div></div>';\n"
    "      }).join('');\n"
    "      return '<div class=\"jww-cabinet\"><div class=\"jww-cab-hd\">' + IC.spark + '<span>' + esc(t('cabinet_title')) + '</span></div><div class=\"jww-cab-row\">' + items + '</div></div>';\n"
    "    }\n"
    "    function openMedalPopup(seq){\n"
    "      var a = __achCache && __achCache[seq]; if (!a) return;\n"
    "      var ap = ACH_RENOWN[a.rarity] || 0;\n"
    "      var col = achColor(a), cstyle = col ? '--mc:' + col[0] + ';--mc2:' + col[1] : '';\n"
    "      var desc = a.dk ? t(a.dk) : '';\n"
    "      var prog = '';\n"
    "      if (!a.on && !a.secret && a.tgt){ var pgp = Math.round(clamp01(a.cur / a.tgt) * 100); prog = '<div class=\"jww-mp-prog\"><div class=\"jww-mp-prog-track\"><div class=\"jww-mp-prog-fill\" style=\"width:' + pgp + '%\"></div></div><div class=\"jww-mp-prog-lbl\">' + (a.cur || 0) + ' / ' + a.tgt + '</div></div>'; }\n"
    "      var html = '<div class=\"jww-mp-ov\" id=\"jww-mp-ov\"><div class=\"jww-mp-box\" style=\"' + cstyle + '\">'\n"
    "        + '<button class=\"jww-mp-close\" aria-label=\"close\">×</button>'\n"
    "        + '<div class=\"jww-mp-disc' + (a.on ? ' jww-medal-on' : '') + '\">' + (a.on ? a.icon : IC_LOCK) + '</div>'\n"
    "        + '<div class=\"jww-mp-name\">' + esc(a.name) + '</div>'\n"
    "        + (desc ? '<div class=\"jww-mp-desc\">' + esc(desc) + '</div>' : '')\n"
    "        + prog\n"
    "        + (ap ? '<div class=\"jww-mp-ap\">' + IC.spark + '<span>+' + ap + ' ' + esc(t('renown_label')) + '</span></div>' : '')\n"
    "        + '</div></div>';\n"
    "      var el = document.createElement('div'); el.innerHTML = html; var ov = el.firstChild;\n"
    "      document.body.appendChild(ov);\n"
    "      ov.addEventListener('click', function(e){ if (e.target === ov || e.target.classList.contains('jww-mp-close')) ov.remove(); });\n"
    "    }\n"
    "    function wireAchMedals(body){\n"
    "      var wall = body.querySelector('.jww-ach-wall'); if (!wall) return;\n"
    "      wall.addEventListener('click', function(e){\n"
    "        var medal = e.target.closest('.jww-medal,.jww-cab-medal'); if (!medal) return;\n"
    "        var seq = medal.getAttribute('data-seq'); if (seq == null) return;\n"
    "        openMedalPopup(+seq);\n"
    "      });\n"
    "    }\n"
)
R(old6, new6, 'cabinetHtml + openMedalPopup + wireAchMedals')

# 7. Call wireAchMedals after wireAchFilters
R(
    '      wireAchFilters(body);',
    '      wireAchFilters(body); wireAchMedals(body);',
    'wireAchMedals call'
)

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Batch 3 OK')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

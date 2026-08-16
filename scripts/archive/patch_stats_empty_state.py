#!/usr/bin/env python3
"""v2.69.0 — App-interior aesthetic pass: Study Stats empty state (shared file).

Brings the Study Stats (highlights.html) file-picker empty state up to the
polish level of the Share page: a proper surface card with a stats icon, the
existing title + subtitle, the Open File button, a drag-and-drop hint with a
working drop zone, and an "on your device / nothing uploaded" privacy line.

Theme-aware (dark + light). Two new localised keys (pick_drop, pick_private)
across all 12 languages. Applied identically to highlights.html and
beta/highlights.html (shared files ship in lockstep). Bumps SW CACHE_VERSION
(highlights.html is precached) and softwareVersion in both index.html files.
"""
import re

OLD_CSS = """    .hl-pick { display: flex; flex-direction: column; align-items: center; justify-content: center;
      min-height: 60vh; gap: 20px; text-align: center; }
    .hl-pick-title { font-size: 22px; font-weight: 700; color: #f1f5f9; }
    .hl-pick-sub { color: #64748b; font-size: 15px; max-width: 360px; line-height: 1.5; }
    .hl-pick-btn { background: #ea580c; color: #fff; border: none; border-radius: 8px;
      padding: 13px 28px; font-size: 15px; font-weight: 600; cursor: pointer; transition: background .15s;
      font-family: inherit; }
    .hl-pick-btn:hover { background: #c2410c; }"""

NEW_CSS = """    .hl-pick { display: flex; flex-direction: column; align-items: center; justify-content: center;
      min-height: 64vh; padding: 24px 16px; text-align: center; }
    .hl-pick-card { display: flex; flex-direction: column; align-items: center; gap: 14px;
      max-width: 420px; width: 100%; padding: 36px 32px; box-sizing: border-box;
      background: rgba(4,15,34,.7); border: 1px solid rgba(71,85,105,.45); border-radius: 16px;
      box-shadow: 0 16px 40px rgba(2,8,23,.35); transition: border-color .15s ease, box-shadow .15s ease; }
    .hl-pick-card.is-dragover { border-color: #ea580c;
      box-shadow: 0 0 0 3px rgba(234,88,12,.18), 0 16px 40px rgba(2,8,23,.35); }
    .hl-pick-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center;
      background: rgba(234,88,12,.12); border: 1px solid rgba(234,88,12,.3); color: #ea580c; }
    .hl-pick-icon svg { width: 26px; height: 26px; }
    .hl-pick-title { font-size: 22px; font-weight: 700; color: #f1f5f9; }
    .hl-pick-sub { color: #94a3b8; font-size: 15px; max-width: 340px; line-height: 1.5; margin-top: -4px; }
    .hl-pick-btn { background: #ea580c; color: #fff; border: none; border-radius: 8px;
      padding: 13px 28px; font-size: 15px; font-weight: 600; cursor: pointer; transition: background .15s;
      font-family: inherit; margin-top: 4px; }
    .hl-pick-btn:hover { background: #c2410c; }
    .hl-pick-drop { font-size: 12.5px; color: #64748b; }
    .hl-pick-private { display: flex; align-items: center; gap: 6px; margin-top: 6px; padding-top: 14px;
      border-top: 1px solid rgba(71,85,105,.3); font-size: 12px; color: #94a3b8; line-height: 1.4; }
    .hl-pick-private svg { width: 13px; height: 13px; color: #34d399; flex: none; }
    body.light .hl-pick-card { background: #fff; border-color: rgba(11,46,88,.14); box-shadow: 0 14px 34px rgba(11,46,88,.12); }
    body.light .hl-pick-title { color: #071a38; }
    body.light .hl-pick-icon { background: rgba(234,88,12,.1); }
    body.light .hl-pick-sub, body.light .hl-pick-private { color: #475569; }
    body.light .hl-pick-private { border-top-color: rgba(11,46,88,.1); }
    body.light .hl-pick-private svg { color: #059669; }"""

OLD_MARKUP = """      setMain(
        '<div class="hl-pick">' +
          '<div class="hl-pick-title">' + esc(t('title')) + '</div>' +
          '<div class="hl-pick-sub">' + esc(t('pick_file')) + '</div>' +
          '<button class="hl-pick-btn" id="hl-pick-trigger">' + esc(t('open_file')) + '</button>' +
        '</div>'
      );"""

NEW_MARKUP = """      var STATS_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>';
      var LOCK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>';
      setMain(
        '<div class="hl-pick">' +
          '<div class="hl-pick-card" id="hl-drop">' +
            '<div class="hl-pick-icon">' + STATS_ICON + '</div>' +
            '<div class="hl-pick-title">' + esc(t('title')) + '</div>' +
            '<div class="hl-pick-sub">' + esc(t('pick_file')) + '</div>' +
            '<button class="hl-pick-btn" id="hl-pick-trigger">' + esc(t('open_file')) + '</button>' +
            '<div class="hl-pick-drop">' + esc(t('pick_drop')) + '</div>' +
            '<div class="hl-pick-private">' + LOCK_ICON + '<span>' + esc(t('pick_private')) + '</span></div>' +
          '</div>' +
        '</div>'
      );"""

OLD_WIRE = """      var btn = document.getElementById('hl-pick-trigger');
      if (btn) btn.addEventListener('click', function () { input.click(); });
    }"""

NEW_WIRE = """      var btn = document.getElementById('hl-pick-trigger');
      if (btn) btn.addEventListener('click', function () { input.click(); });
      var drop = document.getElementById('hl-drop');
      if (drop) {
        ['dragenter', 'dragover'].forEach(function (ev) {
          drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('is-dragover'); });
        });
        ['dragleave', 'dragend'].forEach(function (ev) {
          drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('is-dragover'); });
        });
        drop.addEventListener('drop', function (e) {
          e.preventDefault(); drop.classList.remove('is-dragover');
          var f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
          if (f) { try { window.__jwLastFile = f; } catch (_) {} loadFromFile(f); }
        });
      }
    }"""

# pick_drop, pick_private per language
I18N = {
    'en':  ('or drag a file here', 'Your file is read on your device — nothing is uploaded.'),
    'es':  ('o arrastra un archivo aquí', 'Tu archivo se lee en tu dispositivo; no se sube nada.'),
    'pt':  ('ou arraste um arquivo aqui', 'Seu arquivo é lido no seu dispositivo; nada é enviado.'),
    'fr':  ('ou faites glisser un fichier ici', "Votre fichier est lu sur votre appareil ; rien n'est envoyé."),
    'de':  ('oder ziehe eine Datei hierher', 'Deine Datei wird auf deinem Gerät gelesen; nichts wird hochgeladen.'),
    'it':  ('o trascina qui un file', 'Il tuo file viene letto sul tuo dispositivo; non viene caricato nulla.'),
    'ru':  ('или перетащите файл сюда', 'Файл читается на вашем устройстве; ничего не загружается.'),
    'ja':  ('またはファイルをここにドラッグ', 'ファイルはお使いの端末で読み込まれます。アップロードされません。'),
    'ko':  ('또는 파일을 여기로 끌어다 놓으세요', '파일은 기기에서 읽히며 업로드되지 않습니다.'),
    'tl':  ('o i-drag ang file dito', 'Binabasa ang iyong file sa device mo; walang ina-upload.'),
    'sv':  ('eller dra en fil hit', 'Din fil läses på din enhet; ingenting laddas upp.'),
    'ceb': ('o i-drag ang file dinhi', 'Ang imong file gibasa sa imong device; walay gi-upload.'),
}


def patch(path):
    c = open(path, encoding='utf-8').read()
    assert c.count(OLD_CSS) == 1, '%s: CSS anchor' % path
    assert c.count(OLD_MARKUP) == 1, '%s: markup anchor' % path
    assert c.count(OLD_WIRE) == 1, '%s: wire anchor' % path
    c = c.replace(OLD_CSS, NEW_CSS).replace(OLD_MARKUP, NEW_MARKUP).replace(OLD_WIRE, NEW_WIRE)

    # insert the two keys after each language's open_file value
    i18n_start = c.find('var I18N')
    for lang, (drop, priv) in I18N.items():
        ls = c.find(lang + ':{', i18n_start)
        assert ls != -1, '%s: language %s not found' % (path, lang)
        m = re.search(r'open_file:(["\'])(?:[^"\'\\]|\\.)*?\1', c[ls:])
        assert m, '%s: open_file for %s not found' % (path, lang)
        ins_at = ls + m.end()
        # escape per value: use double quotes; values contain no double quote
        assert '"' not in drop and '"' not in priv
        addition = ',pick_drop:"%s",pick_private:"%s"' % (drop, priv)
        c = c[:ins_at] + addition + c[ins_at:]

    open(path, 'w', encoding='utf-8').write(c)
    print('%s: picker redesigned + 12 langs' % path)


patch('highlights.html')
patch('beta/highlights.html')

# version bumps
sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v111';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v111';", "const CACHE_VERSION = 'jwsync-v112';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js: CACHE_VERSION -> v112')

for idx in ('beta/index.html', 'index.html'):
    p = open(idx, encoding='utf-8').read()
    assert p.count('"softwareVersion": "2.68.1"') == 1, idx
    p = p.replace('"softwareVersion": "2.68.1"', '"softwareVersion": "2.69.0"')
    open(idx, 'w', encoding='utf-8').write(p)
    print('%s: softwareVersion -> 2.69.0' % idx)
print('done')

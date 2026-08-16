#!/usr/bin/env python3
"""Merge-tool redesign (BETA ONLY) — injects one scoped style+script block into
beta/index.html. Re-runnable: replaces the block between its markers.

What it does (all scoped to #root, the merge app; production untouched):
  1. Palette: warm "stone" -> cool navy/slate. Scoped to dark mode only
     (body:not(.light)) so the app's light theme is never affected.
  2. Declutter: hides the redundant second header (duplicate logo + language
     picker — the site nav already provides both and its picker drives the app)
     and the toolbar's duplicate Study Explorer / Community buttons.
  3. De-emoji: a small DOM script strips emojis from the merge tool's functional
     UI (labels live in the shared app.js, so they can't be edited beta-only).

index.html (production) and the shared app.js / styles.css are untouched.
"""
PATH = 'beta/index.html'
START = '<style id="beta-merge-redesign">'
END = '<!-- /beta-merge-redesign -->'

# dark-only palette remap (warm stone -> cool navy/slate)
PAL = [
    ('bg-stone-950', 'background-color:#05101f'),
    ('bg-stone-900', 'background-color:#0a1424'),
    ('bg-stone-800', 'background-color:#111f38'),
    ('bg-stone-700', 'background-color:#1a2c4d'),
    (r'bg-stone-900\/50', 'background-color:rgba(10,20,36,.5)'),
    (r'bg-stone-900\/60', 'background-color:rgba(10,20,36,.6)'),
    (r'bg-stone-900\/40', 'background-color:rgba(10,20,36,.4)'),
    (r'bg-stone-800\/80', 'background-color:rgba(17,31,56,.8)'),
    (r'bg-stone-800\/50', 'background-color:rgba(17,31,56,.5)'),
    (r'bg-stone-800\/30', 'background-color:rgba(17,31,56,.3)'),
    (r'bg-stone-950\/50', 'background-color:rgba(5,16,31,.5)'),
    (r'bg-stone-700\/30', 'background-color:rgba(26,44,77,.3)'),
    (r'bg-stone-600\/30', 'background-color:rgba(36,57,94,.3)'),
    ('border-stone-800', 'border-color:rgba(148,163,184,.12)'),
    ('border-stone-700', 'border-color:rgba(148,163,184,.18)'),
    ('border-stone-600', 'border-color:rgba(148,163,184,.26)'),
    (r'border-stone-800\/50', 'border-color:rgba(148,163,184,.08)'),
    (r'border-stone-700\/50', 'border-color:rgba(148,163,184,.13)'),
    ('text-stone-100', 'color:#f1f5f9'),
    ('text-stone-200', 'color:#e2e8f0'),
    ('text-stone-300', 'color:#cbd5e1'),
    ('text-stone-400', 'color:#94a3b8'),
    ('text-stone-500', 'color:#64748b'),
    ('text-stone-600', 'color:#475569'),
    ('text-stone-700', 'color:#334155'),
]
HOVERS = [
    (r'hover\:bg-stone-700:hover', 'background-color:#1a2c4d'),
    (r'hover\:bg-stone-800:hover', 'background-color:#111f38'),
    (r'hover\:bg-stone-800\/50:hover', 'background-color:rgba(17,31,56,.5)'),
    (r'hover\:bg-stone-700\/30:hover', 'background-color:rgba(26,44,77,.3)'),
    (r'hover\:text-stone-200:hover', 'color:#e2e8f0'),
    (r'hover\:text-stone-300:hover', 'color:#cbd5e1'),
    (r'hover\:text-stone-400:hover', 'color:#94a3b8'),
    (r'hover\:border-stone-700:hover', 'border-color:rgba(148,163,184,.18)'),
]

pal_lines = '\n'.join('body:not(.light) #root .%s{%s}' % (cls, decl) for cls, decl in PAL)
hover_lines = '\n'.join('body:not(.light) #root .%s{%s}' % (cls, decl) for cls, decl in HOVERS)
pal_lines += '\nbody:not(.light) #root .placeholder-stone-600::placeholder{color:#475569}'

BLOCK = START + """
/* ============================================================================
   Merge-tool redesign — BETA preview only (production untouched).
   ========================================================================== */
/* 1) palette: warm stone -> cool navy/slate (dark mode only) */
%s
%s
/* 2) declutter: hide the redundant second header (logo + language picker; the
      site nav already has both and its picker drives the app) */
#root .h-13{display:none}
/* toolbar now sits just below the site nav: a little air + a quiet divider */
#root .overflow-x-auto.pb-2\\.5{padding-top:6px;padding-bottom:12px;margin-bottom:4px;border-bottom:1px solid rgba(148,163,184,.10)}
/* drop the toolbar's duplicate Study Explorer / Community (in the site nav) */
#root .nav-btn-browse,#root .nav-btn-community{display:none}
</style>
<script id="beta-merge-deemoji">
/* BETA-only: strip emojis from the merge tool's functional UI. Labels live in
   the shared app.js, so we clean them in the DOM after React renders.
   Childlist-only observer (we never observe characterData, so our own text
   edits can't re-trigger it). */
(function(){
  var EMOJI=/[\\u{1F000}-\\u{1FAFF}\\u2600-\\u27BF\\u2B00-\\u2BFF\\u25A0-\\u25FF\\u2300-\\u23FF\\u2261\\uFE0F]/gu;
  function strip(root){
    if(!root)return;
    root.querySelectorAll('.nav-btn,.simple-merge-btn,.nav-btn-demo').forEach(function(el){
      el.childNodes.forEach(function(n){
        if(n.nodeType===3&&EMOJI.test(n.nodeValue)){
          n.nodeValue=n.nodeValue.replace(EMOJI,'').replace(/\\s{2,}/g,' ').replace(/^\\s+/,'');
        }
      });
    });
  }
  function run(){strip(document.getElementById('root'));}
  var t,mo=new MutationObserver(function(){clearTimeout(t);t=setTimeout(run,40);});
  (function obs(){var r=document.getElementById('root');if(r){mo.observe(r,{childList:true,subtree:true});run();}else setTimeout(obs,200);})();
})();
</script>
""" % (pal_lines, hover_lines) + END


def main():
    c = open(PATH, encoding='utf-8').read()
    if START in c:
        s = c.index(START); e = c.index(END) + len(END)
        c = c[:s] + BLOCK + c[e:]
        print('replaced existing block')
    else:
        assert c.count('</head>') == 1
        c = c.replace('</head>', BLOCK + '\n</head>', 1)
        print('inserted new block')
    open(PATH, 'w', encoding='utf-8').write(c)
    print('done')


main()

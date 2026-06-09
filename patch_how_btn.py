#!/usr/bin/env python3
"""QoL tweak: move the "How it works" trigger above the "Choose a tool"
section and make the wizard open ONLY on click (no first-run auto-popup)."""
import io, sys

FILE = 'beta/index.html'
with io.open(FILE, encoding='utf-8') as f:
    c = f.read()

orig = c

def rep(old, new, n=1):
    global c
    if c.count(old) != 1:
        print('ABORT: expected 1 occurrence of:\n', old[:90], '\n got', c.count(old))
        sys.exit(1)
    c = c.replace(old, new, n)

# 1) Static HTML: add the "How it works" button just above "Choose a tool".
rep(
  '<div class="svc-section">\n        <h2 class="svc-section-title" data-i18n="svc_heading">Choose a tool</h2>',
  '<div class="svc-section">\n'
  '        <div class="jw-how-row"><button type="button" id="jw-how-btn" class="jw-how-btn">'
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
  '<span class="jw-how-txt">How it works</span></button></div>\n'
  '        <h2 class="svc-section-title" data-i18n="svc_heading">Choose a tool</h2>'
)

# 2) CSS: drop the badge "how" link style, add the standalone how-button styles.
rep(
  '.jw-priv-how{background:none;border:0;padding:0 0 0 4px;cursor:pointer;\n'
  '  color:#fb923c;font:600 12.5px/1.3 inherit;text-decoration:underline;text-underline-offset:2px}\n'
  '.jw-priv-how:hover{color:#ea580c}',
  '.jw-how-row{display:flex;justify-content:center;margin:0 0 16px}\n'
  '.jw-how-btn{display:inline-flex;align-items:center;gap:7px;cursor:pointer;\n'
  '  padding:9px 16px;border-radius:999px;background:rgba(71,85,105,.35);\n'
  '  border:1px solid rgba(71,85,105,.45);color:#cbd5e1;font:600 13px/1 inherit}\n'
  '.jw-how-btn:hover{background:rgba(71,85,105,.5);color:#f1f5f9}\n'
  '.jw-how-btn svg{width:15px;height:15px;color:#fb923c}'
)

# 3) injectBadge: badge is now a pure trust signal (no embedded "how" link).
rep(
  "    b.innerHTML=lock()+'<span class=\"jw-priv-text\"></span><button type=\"button\" class=\"jw-priv-how\" id=\"jw-priv-how\"></button>';\n"
  "    host.parentNode.insertBefore(b,host);\n"
  "    localizeBadge();\n"
  "    var how=document.getElementById('jw-priv-how');\n"
  "    if(how)how.addEventListener('click',function(e){e.preventDefault();openWizard();});\n"
  "    return true;",
  "    b.innerHTML=lock()+'<span class=\"jw-priv-text\"></span>';\n"
  "    host.parentNode.insertBefore(b,host);\n"
  "    localizeBadge();\n"
  "    return true;"
)

# 4) localizeBadge: no more "how" link inside the badge.
rep(
  "  function localizeBadge(){var b=document.getElementById('jw-priv-badge');if(!b)return;\n"
  "    var t=b.querySelector('.jw-priv-text');if(t)t.textContent=L('badge');\n"
  "    var h=b.querySelector('.jw-priv-how');if(h)h.textContent=L('how');}",
  "  function localizeBadge(){var b=document.getElementById('jw-priv-badge');if(!b)return;\n"
  "    var t=b.querySelector('.jw-priv-text');if(t)t.textContent=L('badge');}\n"
  "  function wireHowBtn(){var btn=document.getElementById('jw-how-btn');if(!btn)return;\n"
  "    localizeHowBtn();\n"
  "    if(!btn.__jwWired){btn.__jwWired=true;btn.addEventListener('click',function(e){e.preventDefault();openWizard();});}}\n"
  "  function localizeHowBtn(){var s=document.querySelector('#jw-how-btn .jw-how-txt');if(s)s.textContent=L('how');}"
)

# 5) close(): drop the now-unused first-run flag.
rep(
  "    function close(){try{localStorage.setItem('jwsync_wizard_seen','1');}catch(e){}\n",
  "    function close(){\n"
)

# 6) boot(): remove first-run auto-popup; wire the how button + relocalise it.
rep(
  "  function boot(){\n"
  "    var injected=false,wizDone=false,tries=0;\n"
  "    var iv=setInterval(function(){\n"
  "      tries++;\n"
  "      try{\n"
  "        if(!injected&&injectBadge())injected=true;\n"
  "        if(!wizDone){\n"
  "          var seen=null;try{seen=localStorage.getItem('jwsync_wizard_seen');}catch(e){}\n"
  "          if(seen==='1'){wizDone=true;}\n"
  "          else if(mainPicker()){wizDone=true;setTimeout(openWizard,500);}\n"
  "        }\n"
  "      }catch(e){}\n"
  "      if((injected&&wizDone)||tries>40)clearInterval(iv);\n"
  "    },300);\n",
  "  function boot(){\n"
  "    wireHowBtn();\n"
  "    var injected=false,tries=0;\n"
  "    var iv=setInterval(function(){\n"
  "      tries++;\n"
  "      try{ if(!injected&&injectBadge())injected=true; wireHowBtn(); }catch(e){}\n"
  "      if(injected||tries>40)clearInterval(iv);\n"
  "    },300);\n"
)
rep(
  "      if(sel)sel.addEventListener('change',function(){setTimeout(localizeBadge,60);});}catch(e){}",
  "      if(sel)sel.addEventListener('change',function(){setTimeout(function(){localizeBadge();localizeHowBtn();},60);});}catch(e){}"
)

if c == orig:
    print('No changes made!'); sys.exit(1)
with io.open(FILE, 'w', encoding='utf-8') as f:
    f.write(c)
print('Tweak applied; file now', len(c), 'chars')

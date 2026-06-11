# -*- coding: utf-8 -*-
"""Doctor merge checkbox v3 (v2.65.0) — app.js side.
One-shot checkbox under the 'Create My Merged File' button: read & reset in
vt(), forwarded to the worker as opts.doctorCheck; the worker's doctor
report is passed through to the impact card."""
import io, sys

f = 'beta/js/app.js'
c = io.open(f, encoding='utf-8').read()

def must(cond, msg):
    if not cond:
        print('ABORT:', msg); sys.exit(1)

def rep(old, new, what):
    global c
    must(c.count(old) == 1, what + ' anchor not unique: %d' % c.count(old))
    c = c.replace(old, new, 1)

# 1) one-shot checkbox row directly below the Create My Merged File button
rep('s("create_merged"))),oe&&ie&&ie.total>0',
    's("create_merged"))),l?React.createElement("label",{id:"doctor-merge-row",'
    'className:"flex items-center justify-center gap-2 mt-3 text-sm text-stone-400 hover:text-stone-300 cursor-pointer select-none"},'
    'React.createElement("input",{id:"doctor-merge-cb",type:"checkbox",defaultChecked:!1,'
    'style:{width:"15px",height:"15px",accentColor:"#ea580c",cursor:"pointer",flexShrink:0}}),'
    'React.createElement("span",null,window.__jwDoctorCbLabel?window.__jwDoctorCbLabel():"Health-check & clean the merged file (Library Doctor)")):null,'
    'oe&&ie&&ie.total>0',
    'checkbox markup')

# 2) vt(): read the box once, untick it immediately (one-time use)
rep('vt=async()=>{if(!l||!M)return;var n,i;',
    'vt=async()=>{if(!l||!M)return;var n,i;'
    'var __doctorOnce=!1;try{var __dcb=document.getElementById("doctor-merge-cb");'
    'if(__dcb){__doctorOnce=!!__dcb.checked;__dcb.checked=!1;}}catch(_){}',
    'vt read/reset')

# 3) forward the flag to the worker
rep('opts:Object.assign({},p,{previewConfirm:!0})',
    'opts:Object.assign({},p,{previewConfirm:!0,doctorCheck:__doctorOnce})',
    'opts doctorCheck')

# 4) hand the doctor report to the impact card
rep('await window.__jwImpactPreview(d.counts):!0',
    'await window.__jwImpactPreview(d.counts,d.doctor||null):!0',
    'impact passthrough')

io.open(f, 'w', encoding='utf-8').write(c)
print('OK: beta/js/app.js patched')

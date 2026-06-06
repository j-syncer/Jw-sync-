#!/usr/bin/env python3
"""Improve Ask indexing progress: animated bar, smooth interpolation, ETA."""

import sys

path = 'beta/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

original_len = len(c)
changes = []

def R(old, new, label):
    global c
    count = c.count(old)
    if count != 1:
        print(f'  FAIL ({count} occurrences): {label}')
        sys.exit(1)
    c = c.replace(old, new, 1)
    changes.append(label)
    print(f'  OK: {label}')

# ── 1. Upgrade progress bar CSS ─────────────────────────────────────────────
# Taller bar, animated shimmer sweep, smooth width transition
R(
    '.jb-ask-prog{height:8px;border-radius:6px;background:rgba(71,85,105,.35);overflow:hidden;margin:14px auto 8px;max-width:520px}\n'
    '.jb-ask-prog-fill{height:100%;border-radius:6px;background:linear-gradient(90deg,#fb923c,#ea580c);width:0;transition:width .25s ease}',

    '.jb-ask-prog{height:12px;border-radius:8px;background:rgba(71,85,105,.35);overflow:hidden;margin:14px auto 6px;max-width:520px;width:100%}\n'
    '.jb-ask-prog-fill{height:100%;border-radius:8px;background:linear-gradient(90deg,#ea580c,#f97316,#fb923c);width:0;transition:width 1.6s ease-out;position:relative;overflow:hidden}\n'
    '.jb-ask-prog-fill::after{content:\'\';position:absolute;inset:0;background:linear-gradient(90deg,transparent 0%,rgba(255,255,255,.4) 50%,transparent 100%);animation:askShimmer 1.3s ease-in-out infinite}\n'
    '@keyframes askShimmer{0%{transform:translateX(-180%)}100%{transform:translateX(280%)}}\n'
    '.jb-ask-eta{font-size:11.5px;color:#64748b;text-align:center;margin:0 0 8px}',

    'CSS: taller bar, shimmer sweep, ETA class'
)

# ── 2. Add ticker fields to ASK object ──────────────────────────────────────
R(
    'var ASK = { worker:null, vecs:null, pending:{}, reqId:0, _onReady:null };',
    'var ASK = { worker:null, vecs:null, pending:{}, reqId:0, _onReady:null, _ticker:null, _buildStart:0, _snap:null };',
    'ASK: add ticker/ETA fields'
)

# ── 3. Replace buildAskIndex with instrumented version ──────────────────────
R(
    '''  function buildAskIndex(model){
    var notes=askNotes(); state.askTotal=notes.length; state.askDone=0;
    if(!notes.length){ state.askPhase='ready'; ASK.vecs=[]; renderBody(); return; }
    state.askPhase='building'; state.askProgress=0; renderBody();
    idbGetModel(model).then(function(cached){
      var need=[]; notes.forEach(function(n){ var c=cached[n.note.NoteId]; if(!c||c.hash!==n.hash) need.push(n); });
      state.askDone=notes.length-need.length;
      var B=48, i=0;
      function step(){
        if(i>=need.length){
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          state.askPhase='ready'; state.askProgress=100; renderBody(); return;
        }
        var batch=need.slice(i,i+B); i+=B;
        embedBatch(batch.map(function(x){ return x.text; })).then(function(r){
          var dim=r.dim, arr=r.vec;
          for(var j=0;j<batch.length;j++){ var v=arr.slice(j*dim,(j+1)*dim); cached[batch[j].note.NoteId]={ hash:batch[j].hash, vec:v }; idbPutVec(model,batch[j].note.NoteId,batch[j].hash,v,dim); }
          state.askDone=Math.min(notes.length, state.askDone+batch.length);
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          state.askProgress=Math.round(state.askDone/notes.length*100); updateAskProgress();
          step();
        }).catch(function(){ state.askError=t('ask_err'); state.askPhase='idle'; renderBody(); });
      }
      step();
    });
  }''',

    '''  function buildAskIndex(model){
    var notes=askNotes(); state.askTotal=notes.length; state.askDone=0;
    if(!notes.length){ state.askPhase='ready'; ASK.vecs=[]; renderBody(); return; }
    state.askPhase='building'; state.askProgress=0; renderBody();
    ASK._buildStart=Date.now(); ASK._snap=null;
    if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; }
    ASK._ticker=setInterval(function(){
      if(state.askPhase!=='building'){ clearInterval(ASK._ticker); ASK._ticker=null; return; }
      var total=state.askTotal||1, rawDone=state.askDone, snap=ASK._snap;
      var dispDone=rawDone;
      if(snap&&snap.rate>0&&rawDone<total){ dispDone=Math.min(total, rawDone+(Date.now()-snap.time)*snap.rate); }
      var pct=Math.min(99, dispDone/total*100);
      var f=state.overlay&&state.overlay.querySelector('.jb-ask-prog-fill'); if(f) f.style.width=pct+'%';
      var elapsed=(Date.now()-ASK._buildStart)/1000, eta='';
      if(rawDone>2&&rawDone<total&&elapsed>1){
        var secs=Math.ceil((total-rawDone)/(rawDone/elapsed));
        eta=secs>=60?'~'+Math.floor(secs/60)+'m '+(secs%60)+'s left':'~'+secs+'s left';
      }
      var s=state.overlay&&state.overlay.querySelector('.jb-ask-status');
      if(s){ s.textContent=t('ask_building',{done:Math.min(total,Math.round(dispDone)),total:total})+(eta?' · '+eta:''); }
      var e=state.overlay&&state.overlay.querySelector('.jb-ask-eta'); if(e) e.textContent=eta;
    },250);
    idbGetModel(model).then(function(cached){
      var need=[]; notes.forEach(function(n){ var c=cached[n.note.NoteId]; if(!c||c.hash!==n.hash) need.push(n); });
      state.askDone=notes.length-need.length;
      var B=48, i=0;
      function step(){
        if(i>=need.length){
          if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; }
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          state.askPhase='ready'; state.askProgress=100; renderBody(); return;
        }
        var batch=need.slice(i,i+B); i+=B; var batchStart=Date.now();
        embedBatch(batch.map(function(x){ return x.text; })).then(function(r){
          var dim=r.dim, arr=r.vec;
          for(var j=0;j<batch.length;j++){ var v=arr.slice(j*dim,(j+1)*dim); cached[batch[j].note.NoteId]={ hash:batch[j].hash, vec:v }; idbPutVec(model,batch[j].note.NoteId,batch[j].hash,v,dim); }
          state.askDone=Math.min(notes.length, state.askDone+batch.length);
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          var batchMs=Math.max(1,Date.now()-batchStart); ASK._snap={time:Date.now(),done:state.askDone,rate:batch.length/batchMs};
          state.askProgress=Math.round(state.askDone/notes.length*100);
          step();
        }).catch(function(){ if(ASK._ticker){clearInterval(ASK._ticker);ASK._ticker=null;} state.askError=t('ask_err'); state.askPhase='idle'; renderBody(); });
      }
      step();
    });
  }''',

    'buildAskIndex: ticker + interpolation + ETA'
)

# ── 4. Add ETA element to renderAsk building phase ───────────────────────────
# Add a .jb-ask-eta div after the progress bar (inside the building block)
R(
    "if(state.askPhase==='building'){\n        var hint=document.createElement('div'); hint.className='jb-ask-once-hint'; hint.textContent='First-time only — saved to your device, instant next time.'; panel.appendChild(hint);",

    "if(state.askPhase==='building'){\n        var etaEl=document.createElement('div'); etaEl.className='jb-ask-eta'; panel.appendChild(etaEl);"
    "\n        var hint=document.createElement('div'); hint.className='jb-ask-once-hint'; hint.textContent='First-time only — saved to your device, instant next time.'; panel.appendChild(hint);",

    'renderAsk: add ETA element in building block'
)

# ── 5. Clear ticker on closeOverlay / new file load ─────────────────────────
R(
    'if(ASK.worker){ try{ ASK.worker.terminate(); }catch(_){} ASK.worker=null; } ASK.vecs=null; ASK.pending={}; ASK._onReady=null;',
    'if(ASK.worker){ try{ ASK.worker.terminate(); }catch(_){} ASK.worker=null; } if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; } ASK.vecs=null; ASK.pending={}; ASK._onReady=null; ASK._snap=null;',
    'clear ticker on closeOverlay'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'\nAll {len(changes)} changes applied. File: {len(c):,} bytes (was {original_len:,})')

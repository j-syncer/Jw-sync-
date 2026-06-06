#!/usr/bin/env python3
"""Patch beta/index.html: faster Ask indexing + search-while-indexing."""

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

# 1. Add CSS for once-hint (after .jb-ask-err rule)
R(
    '.jb-ask-err{color:#fca5a5;font-size:12.5px;text-align:center;padding:10px;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:10px;margin:8px auto;max-width:520px}',
    '.jb-ask-err{color:#fca5a5;font-size:12.5px;text-align:center;padding:10px;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:10px;margin:8px auto;max-width:520px}'
    '.jb-ask-once-hint{font-size:11.5px;color:#4ade80;text-align:center;margin:8px 0 2px;opacity:.85}'
    '.jb-ask-part-note{font-size:11.5px;color:#94a3b8;text-align:center;margin:4px 0 10px}',
    'CSS: once-hint + part-note'
)

# 2. Increase batch size 24 → 48
R(
    'var B=24, i=0;',
    'var B=48, i=0;',
    'batch size 24→48'
)

# 3. Update ASK.vecs incrementally after each batch so partial search works
R(
    '''          state.askDone=Math.min(notes.length, state.askDone+batch.length);
          state.askProgress=Math.round(state.askDone/notes.length*100); updateAskProgress();''',
    '''          state.askDone=Math.min(notes.length, state.askDone+batch.length);
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          state.askProgress=Math.round(state.askDone/notes.length*100); updateAskProgress();''',
    'incremental ASK.vecs update per batch'
)

# 4. Allow doAskSearch during 'building' phase (if partial index exists)
R(
    'if(state.askPhase!==\'ready\'||!ASK.vecs){ return; }',
    'if((state.askPhase!==\'ready\'&&state.askPhase!==\'building\')||!ASK.vecs||!ASK.vecs.length){ return; }',
    'doAskSearch: allow during building phase'
)

# 5. Enable Search button during building if partial index exists
R(
    'go.disabled=(state.askPhase!==\'ready\');',
    'go.disabled=(state.askPhase!==\'ready\'&&!(state.askPhase===\'building\'&&ASK.vecs&&ASK.vecs.length));',
    'Search button enabled during building'
)

# 6. In the building phase block: add once-hint + partial results
R(
    '''      var pr=document.createElement('div'); pr.className='jb-ask-prog'; var pf=document.createElement('div'); pf.className='jb-ask-prog-fill'; pf.style.width=state.askProgress+'%'; pr.appendChild(pf); panel.appendChild(pr);
    } else if(state.askError){''',
    '''      var pr=document.createElement('div'); pr.className='jb-ask-prog'; var pf=document.createElement('div'); pf.className='jb-ask-prog-fill'; pf.style.width=state.askProgress+'%'; pr.appendChild(pf); panel.appendChild(pr);
      if(state.askPhase==='building'){
        var hint=document.createElement('div'); hint.className='jb-ask-once-hint'; hint.textContent='First-time only — saved to your device, instant next time.'; panel.appendChild(hint);
        if(ASK.vecs&&ASK.vecs.length){
          var pn=document.createElement('div'); pn.className='jb-ask-part-note'; pn.textContent='Searching '+ASK.vecs.length+' of '+(state.askTotal||0)+' notes indexed so far.'; panel.appendChild(pn);
          if(state.askResults&&state.askResults.length){
            var rh=document.createElement('div'); rh.className='jb-ask-results-head'; rh.textContent=t('ask_results_head',{n:state.askResults.length}); panel.appendChild(rh);
            state.askResults.forEach(function(res){ var wrap=document.createElement('div'); wrap.style.position='relative'; var row=buildRow(res.note); var sc=document.createElement('span'); sc.className='jb-ask-score'; sc.textContent=Math.round(res.score*100)+'%'; sc.style.cssText='position:absolute;top:10px;right:10px;pointer-events:none'; wrap.appendChild(row); wrap.appendChild(sc); panel.appendChild(wrap); });
          }
        }
      }
    } else if(state.askError){''',
    'building phase: once-hint + partial results'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'\nAll {len(changes)} changes applied. File: {len(c):,} bytes (was {original_len:,})')

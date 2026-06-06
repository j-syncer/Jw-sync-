#!/usr/bin/env python3
"""Fix ETA: use rolling batch rate instead of cumulative elapsed-time rate."""

import sys

path = 'beta/index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

original_len = len(c)

def R(old, new, label):
    count = c.count(old)
    if count != 1:
        print(f'  FAIL ({count} occurrences): {label}')
        sys.exit(1)
    return c.replace(old, new, 1), label

changes = []
def apply(old, new, label):
    global c
    c, lbl = R(old, new, label)
    changes.append(lbl)
    print(f'  OK: {lbl}')

# 1. Add _rates:[] to ASK object so we can track rolling batch rates
apply(
    'var ASK = { worker:null, vecs:null, pending:{}, reqId:0, _onReady:null, _ticker:null, _buildStart:0, _snap:null };',
    'var ASK = { worker:null, vecs:null, pending:{}, reqId:0, _onReady:null, _ticker:null, _buildStart:0, _snap:null, _rates:[] };',
    'ASK: add _rates array'
)

# 2. Reset _rates at start of buildAskIndex
apply(
    'ASK._buildStart=Date.now(); ASK._snap=null;',
    'ASK._buildStart=Date.now(); ASK._snap=null; ASK._rates=[];',
    'reset _rates at build start'
)

# 3. Replace broken cumulative ETA with snap.rate-based ETA (counts down smoothly)
apply(
    'var elapsed=(Date.now()-ASK._buildStart)/1000, eta=\'\';\n'
    '      if(rawDone>2&&rawDone<total&&elapsed>1){\n'
    '        var secs=Math.ceil((total-rawDone)/(rawDone/elapsed));\n'
    '        eta=secs>=60?\'~\'+Math.floor(secs/60)+\'m \'+(secs%60)+\'s left\':\'~\'+secs+\'s left\';\n'
    '      }',

    'var eta=\'\';\n'
    '      if(snap&&snap.rate>0&&rawDone<total){\n'
    '        var etaSecs=Math.ceil((total-Math.min(total,dispDone))/(snap.rate*1000));\n'
    '        if(etaSecs>0) eta=etaSecs>=60?\'~\'+Math.floor(etaSecs/60)+\'m \'+(etaSecs%60)+\'s left\':\'~\'+etaSecs+\'s left\';\n'
    '      }',

    'ETA: use snap.rate not cumulative rate'
)

# 4. Track rolling 4-batch average rate instead of single-batch rate
apply(
    'var batchMs=Math.max(1,Date.now()-batchStart); ASK._snap={time:Date.now(),done:state.askDone,rate:batch.length/batchMs};',

    'var batchMs=Math.max(1,Date.now()-batchStart);\n'
    '          ASK._rates.push(batch.length/batchMs); if(ASK._rates.length>4) ASK._rates.shift();\n'
    '          var avgRate=ASK._rates.reduce(function(a,b){return a+b;},0)/ASK._rates.length;\n'
    '          ASK._snap={time:Date.now(),done:state.askDone,rate:avgRate};',

    'rolling 4-batch average rate for snap'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'\nAll {len(changes)} changes applied. File: {len(c):,} bytes (was {original_len:,})')

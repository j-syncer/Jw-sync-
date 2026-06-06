#!/usr/bin/env python3
"""Fix Explorer nav button: shimmer, rename, and boot-then-open bug."""

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

# 1. Nav link: add shimmer class + rename text to "Study Explorer"
R(
    '<a href="index.html#browse" id="site-nav-explorer" class="site-nav-link" data-i18n="nav_explorer" onclick="__jwGoExplorer();return false;">Explorer</a>',
    '<a href="index.html#browse" id="site-nav-explorer" class="site-nav-link site-nav-shimmer-explorer" data-i18n="nav_explorer" onclick="__jwGoExplorer();return false;">Study Explorer</a>',
    'nav link: shimmer class + rename'
)

# 2. Fix __jwGoExplorer to boot Browse first (same pattern as the service card)
R(
    '''function __jwGoExplorer(){
  var file=null; try{file=window.__jwLastFile||null;}catch(_){}
  if(typeof window.__openJwBrowse==='function'){ window.__openJwBrowse(file||undefined); return; }
  if(window.JwSession){ window.JwSession.goTo('index.html#browse',file); return; }
  window.location.href='index.html#browse';
}''',
    '''function __jwGoExplorer(){
  var file=null; try{file=window.__jwLastFile||null;}catch(_){}
  var open=function(){ if(typeof window.__openJwBrowse==='function') window.__openJwBrowse(file||undefined); };
  if(window.__jwBootBrowse){ window.__jwBootBrowse().then(open).catch(open); } else { open(); }
}''',
    '__jwGoExplorer: boot then open'
)

# 3. Update English nav_explorer text in __JW_LANDING_I18N from "Explorer" to "Study Explorer"
R(
    '"nav_explorer": "Explorer"}, "es":',
    '"nav_explorer": "Study Explorer"}, "es":',
    'landing i18n en: nav_explorer → Study Explorer'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'\nAll {len(changes)} changes applied. File: {len(c):,} bytes (was {original_len:,})')

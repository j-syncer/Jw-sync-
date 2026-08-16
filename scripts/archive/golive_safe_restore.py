# -*- coding: utf-8 -*-
"""GO LIVE: port the Safe Restore confidence layer from beta into production."""
import io, sys

beta = io.open('beta/index.html', encoding='utf-8').read()
prod = io.open('index.html', encoding='utf-8').read()
orig = prod

# Extract the SAFE block (SAFE_I18N + sg + safeRow + buildSafePanel) from beta.
TS = "function ts(k){var l;try{l=lang();}catch(_){l='en';}return (SHARE_I18N[l]&&SHARE_I18N[l][k])||SHARE_I18N.en[k]||k;}"
i = beta.find(TS) + len(TS)
j = beta.find("\n  function renderCelebration", i)
# the SAFE block sits between ts() and the share helpers (shWrap...); grab up to shWrap
k = beta.find("\n  function shWrap(ctx,text", i)
SAFE_BLOCK = beta[i:k]
if 'var SAFE_I18N=' not in SAFE_BLOCK or 'function buildSafePanel' not in SAFE_BLOCK:
    print('ABORT: SAFE block extract failed'); sys.exit(1)
print('extracted SAFE block:', len(SAFE_BLOCK), 'chars')

def rep(s, old, new, label):
    if s.count(old) != 1:
        print('ABORT [%s]: expected 1, got %d' % (label, s.count(old))); sys.exit(1)
    return s.replace(old, new, 1)

# 1) Insert SAFE block right after ts() in prod.
prod = rep(prod, TS, TS + SAFE_BLOCK, 'SAFE block')

# 2) Celebration panel after stats grid.
prod = rep(prod,
  "esc(t('stat_tags')) + '</span></div>' +\n        '</div>' +\n        buildPerfHtml() +",
  "esc(t('stat_tags')) + '</span></div>' +\n        '</div>' +\n        buildSafePanel() +\n        buildPerfHtml() +",
  'celebration panel')

# 3) Restore-guide warning → Safe Restore panel.
GUIDE_OLD = ('\'<div class="jwrg-warning" id="jwrg-warning"><svg viewBox="0 0 24 24" width="16" height="16" '
  'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
  'aria-hidden="true"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'
  '<line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
  '<span>\' + esc(t(\'guide_warning\')) + \'</span></div>\'')
prod = rep(prod, GUIDE_OLD, "'<div id=\"jwrg-warning\">' + buildSafePanel() + '</div>'", 'guide warning')

# 4) Version bump.
prod = rep(prod, '"softwareVersion": "2.57.0"', '"softwareVersion": "2.58.0"', 'version')

if prod == orig:
    print('No changes!'); sys.exit(1)
io.open('index.html', 'w', encoding='utf-8').write(prod)
print('GO LIVE applied; production now', len(prod), 'chars')

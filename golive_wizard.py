# -*- coding: utf-8 -*-
"""GO LIVE: port the final How-it-works wizard (Merge Wizard + privacy badge
+ 'How it works' button + Other tools tab) from beta/index.html into the
production index.html, verbatim. Bumps production softwareVersion."""
import io, sys

beta = io.open('beta/index.html', encoding='utf-8').read()
prod = io.open('index.html', encoding='utf-8').read()
orig = prod

# 1) Extract the self-contained wizard block from beta (markers inclusive).
START = '<!-- ── Merge Wizard + Privacy Badge ─'
END = '<!-- ── End Merge Wizard + Privacy Badge ──────────────────── -->'
si = beta.find(START); ei = beta.find(END)
if si < 0 or ei < 0:
    print('ABORT: wizard markers not found in beta'); sys.exit(1)
block = beta[si:ei + len(END)]
print('extracted wizard block:', len(block), 'chars')

# 2) Extract the "How it works" button row from beta.
hr0 = beta.find('<div class="jw-how-row">')
hr1 = beta.find('</div>', hr0) + len('</div>')
howrow = beta[hr0:hr1]
if '<button type="button" id="jw-how-btn"' not in howrow:
    print('ABORT: how-row not found in beta'); sys.exit(1)
print('extracted how-row:', len(howrow), 'chars')

def rep(s, old, new):
    if s.count(old) != 1:
        print('ABORT: expected 1 of', repr(old[:60]), 'got', s.count(old)); sys.exit(1)
    return s.replace(old, new, 1)

# 3) Insert the How-it-works button above "Choose a tool".
prod = rep(prod,
  '<div class="svc-section">\n        <h2 class="svc-section-title" data-i18n="svc_heading">Choose a tool</h2>',
  '<div class="svc-section">\n        ' + howrow + '\n        <h2 class="svc-section-title" data-i18n="svc_heading">Choose a tool</h2>')

# 4) Guard: don't double-inject the wizard.
if START in prod:
    print('ABORT: wizard block already present in production'); sys.exit(1)

# 5) Inject the wizard block just before the closing </body></html>.
tail = '\n</body>\n</html>\n'
prod = rep(prod, tail, '\n' + block + tail)

# 6) Bump production softwareVersion to match beta.
prod = rep(prod, '"softwareVersion": "2.53.0"', '"softwareVersion": "2.56.0"')

if prod == orig:
    print('No changes!'); sys.exit(1)
io.open('index.html', 'w', encoding='utf-8').write(prod)
print('GO LIVE applied; production index.html now', len(prod), 'chars')

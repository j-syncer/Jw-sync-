#!/usr/bin/env python3
"""v2.72.0-beta — Bring the Community forum on-brand (BETA ONLY).

The live Community forum (#forum-view, embedded in index.html) renders with a
blue accent (#3282bc), a multi-colour gradient logo, and emojis in its buttons
and filter chips — off-brand against the orange identity. Since the accent
lives in the shared styles.css, this previews the fix on BETA only via a
scoped override in beta/index.html, leaving production unchanged until go-live:

- beta-only CSS: #forum-view --accent -> orange, flat orange logo, icon sizing
- de-emoji functional UI: filter pills + New Post button get clean line icons;
  the compose category dropdown drops emojis (native <option> can't hold SVG)

Only beta/index.html changes. softwareVersion bumped (beta file). No SW bump
(index.html is not precached by the service worker).
"""

path = 'beta/index.html'
c = open(path, encoding='utf-8').read()

I = {
    'pencil': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"></path></svg>',
    'help': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    'alert': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    'bulb': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="9" y1="18" x2="15" y2="18"></line><line x1="10" y1="22" x2="14" y2="22"></line><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"></path></svg>',
    'msg': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>',
}

# 1. functional-UI de-emoji (pills + New Post button)
markup = [
    ('>✏️ New Post</button>', '>' + I['pencil'] + 'New Post</button>'),
    ('>❓ Questions</span>', '>' + I['help'] + 'Questions</span>'),
    ('>🐛 Bugs</span>', '>' + I['alert'] + 'Bugs</span>'),
    ('>💡 Features</span>', '>' + I['bulb'] + 'Features</span>'),
    ('>💬 General</span>', '>' + I['msg'] + 'General</span>'),
    # compose dropdown: native <option> can't render SVG -> plain text
    ('<option value="question">❓ Question</option>', '<option value="question">Question</option>'),
    ('<option value="bug">🐛 Bug Report</option>', '<option value="bug">Bug Report</option>'),
    ('<option value="feature">💡 Feature Request</option>', '<option value="feature">Feature Request</option>'),
    ('<option value="general">💬 General</option>', '<option value="general">General</option>'),
]
for old, new in markup:
    assert c.count(old) == 1, '%s: markup anchor not unique: %r' % (path, old)
    c = c.replace(old, new)

# 2. beta-only scoped orange override (placed last in <head> so it wins)
OVERRIDE = """<style id="beta-forum-theme">
/* BETA-only: bring the Community forum onto the orange brand (preview before go-live) */
#forum-view{--accent:#ea580c;--accent2:#fb923c}
#forum-view .logo-icon{background:#ea580c}
#forum-view .pill svg,#forum-view .btn svg{width:14px;height:14px;flex:none}
#forum-view .pill svg{margin-right:4px}
</style>
</head>"""
assert c.count('</head>') == 1, '%s: head anchor' % path
c = c.replace('</head>', OVERRIDE, 1)

assert c.count('"softwareVersion": "2.71.0"') == 1
c = c.replace('"softwareVersion": "2.71.0"', '"softwareVersion": "2.72.0"')

open(path, 'w', encoding='utf-8').write(c)
print('%s patched (beta forum on-brand preview)' % path)

# beta/index.html is precached (beta scope) -> parity test requires a cache bump
sw = open('service-worker.js', encoding='utf-8').read()
assert "const CACHE_VERSION = 'jwsync-v114';" in sw
sw = sw.replace("const CACHE_VERSION = 'jwsync-v114';", "const CACHE_VERSION = 'jwsync-v115';")
open('service-worker.js', 'w', encoding='utf-8').write(sw)
print('service-worker.js: CACHE_VERSION -> v115')
print('done')

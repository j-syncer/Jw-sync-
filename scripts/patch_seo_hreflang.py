# -*- coding: utf-8 -*-
"""Multilingual SEO: add hreflang + og:locale:alternate tags for all 12
languages to the <head>, and regenerate sitemap.xml with every language."""
import io, sys

LANGS = ['en','es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb']
LOCALE = {'en':'en_US','es':'es_ES','pt':'pt_BR','fr':'fr_FR','de':'de_DE',
          'it':'it_IT','ru':'ru_RU','ja':'ja_JP','ko':'ko_KR','tl':'tl_PH',
          'sv':'sv_SE','ceb':'ceb_PH'}
TODAY = '2026-06-09'
SITE = 'https://jwsync.org'

# ---- 1) <head> hreflang + og:locale:alternate (beta/index.html) ----
def head_links():
    out = ['<link rel="alternate" hreflang="x-default" href="%s/">' % SITE]
    for l in LANGS:
        out.append('<link rel="alternate" hreflang="%s" href="%s/?lang=%s">' % (l, SITE, l))
    return '\n    ' + '\n    '.join(out)

def og_alts():
    return '\n    ' + '\n    '.join(
        '<meta property="og:locale:alternate" content="%s">' % LOCALE[l]
        for l in LANGS if l != 'en')

f = 'beta/index.html'
c = io.open(f, encoding='utf-8').read()
orig = c

canon = '<link rel="canonical" href="https://jwsync.org/beta/">'
if c.count(canon) != 1:
    print('ABORT: canonical anchor not unique:', c.count(canon)); sys.exit(1)
if 'hreflang=' in c[:c.find('</head>')]:
    print('ABORT: hreflang already present in head'); sys.exit(1)
c = c.replace(canon, canon + head_links(), 1)

ogl = '<meta property="og:locale" content="en_US">'
if c.count(ogl) != 1:
    print('ABORT: og:locale anchor not unique:', c.count(ogl)); sys.exit(1)
c = c.replace(ogl, ogl + og_alts(), 1)

# version bump
c = c.replace('"softwareVersion": "2.56.1"', '"softwareVersion": "2.56.2"', 1)

if c == orig:
    print('No head changes!'); sys.exit(1)
io.open(f, 'w', encoding='utf-8').write(c)
print('head: added', len(LANGS) + 1, 'hreflang links +', len(LANGS) - 1, 'og:locale:alternate')

# ---- 2) Regenerate sitemap.xml with all 12 languages ----
def alt_block():
    lines = ['    <xhtml:link rel="alternate" hreflang="x-default" href="%s/"/>' % SITE]
    for l in LANGS:
        lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s/?lang=%s"/>' % (l, SITE, l))
    return '\n'.join(lines)

def url(loc, prio):
    return ('  <url>\n'
            '    <loc>%s</loc>\n%s\n'
            '    <lastmod>%s</lastmod>\n'
            '    <changefreq>weekly</changefreq>\n'
            '    <priority>%s</priority>\n'
            '  </url>') % (loc, alt_block(), TODAY, prio)

blocks = [url('%s/' % SITE, '1.0')]
for l in LANGS:
    blocks.append(url('%s/?lang=%s' % (SITE, l), '0.8'))

sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + '\n'.join(blocks) + '\n</urlset>\n')
io.open('sitemap.xml', 'w', encoding='utf-8').write(sitemap)
print('sitemap.xml regenerated:', len(blocks), 'url blocks ×', len(LANGS) + 1, 'hreflang each')

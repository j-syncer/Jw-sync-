#!/usr/bin/env python3
path = '/home/user/Jw-sync-/highlights.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

check_tail = r"""check:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"20 6 9 17 4 12\"/></svg>'
    };"""

count = content.count(check_tail)
print(f'check_tail count: {count}')

if count == 1:
    new_icons = (
        r"""check:'<svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"20 6 9 17 4 12\"/></svg>',"""
        r"""heart:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"currentColor\" stroke=\"none\"><path d=\"M12 21.593c-.526-.43-10.5-8.64-10.5-13.593a6 6 0 0 1 10.5-3.959 6 6 0 0 1 10.5 3.959c0 4.953-9.974 13.163-10.5 13.593z\"/></svg>',"""
        r"""shield:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"currentColor\" stroke=\"none\"><path d=\"M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5L12 1z\"/></svg>',"""
        r"""star5:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"currentColor\" stroke=\"none\"><polygon points=\"12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2\"/></svg>',"""
        r"""eye2:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z\"/><circle cx=\"12\" cy=\"12\" r=\"3.5\" fill=\"currentColor\" stroke=\"none\"/></svg>',"""
        r"""scroll2:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 19.5A2.5 2.5 0 0 1 6.5 17H20\"/><path d=\"M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z\"/><line x1=\"9\" y1=\"9\" x2=\"15\" y2=\"9\"/><line x1=\"9\" y1=\"13\" x2=\"13\" y2=\"13\"/></svg>',"""
        r"""crown2:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"currentColor\" stroke=\"none\"><path d=\"M2 19.5l1.8-8 3.6 3.6 4.6-9.6 4.6 9.6 3.6-3.6 1.8 8H2z\"/><rect x=\"2\" y=\"20\" width=\"20\" height=\"2\" rx=\"1\"/></svg>',"""
        r"""dove2:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M3 17l9-9-3-3 3-3 3 3 6-3-3 9-6 3\" /><path d=\"M12 8l-3 9\"/></svg>',"""
        r"""lamp2:'<svg viewBox=\"0 0 24 24\" width=\"22\" height=\"22\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M9 18h6\"/><path d=\"M10 22h4\"/><path d=\"M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14h6.18z\"/></svg>'"""
        "\n    };"
    )
    content = content.replace(check_tail, new_icons, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK: IC keyword icons added')
else:
    print('ERROR: anchor not found')

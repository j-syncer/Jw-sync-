#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_rtl.py — generate rtl.css, the right-to-left override layer.

Arabic is the site's first RTL language. Rather than hand-auditing ~160 KB of
CSS spread across styles.css, tailwind.css and nineteen embedded <style>
blocks, this script reads every stylesheet the site ships, finds the rules
that contain direction-sensitive declarations, and emits a mirrored copy of
each one scoped to `[dir="rtl"]`.

The generated selector is always the original selector prefixed with
`[dir="rtl"] `, which raises specificity by one attribute selector — so the
override wins regardless of source order, and nothing changes for the twelve
LTR languages.

Because this is an override layer rather than an in-place rewrite, a rule that
sets only one side (`margin-left:8px`) must also neutralise that side, or the
original declaration would still apply. Each swap therefore emits the mirrored
property *and* resets the original to its initial value.

Run from the repo root:  python3 scripts/build_rtl.py
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Every stylesheet that ships to a page which can be switched to Arabic.
# rtl.css must be byte-identical between the two sites (15_parity.js enforces
# it), so the embedded CSS of *both* index.html copies is collected. beta runs
# ahead of production, so its blocks are a superset; mirroring a rule whose
# selector production does not yet use is inert.
CSS_FILES = ["styles.css", "tailwind.css"]
HTML_WITH_EMBEDDED_CSS = ["index.html", "beta/index.html", "highlights.html",
                          "share.html", "forum.html"]

# ── Direction-sensitive properties ────────────────────────────────────────
# property -> (mirrored property, value to reset the original to)
SWAP_PROP = {}


def _pair(a, b, reset):
    SWAP_PROP[a] = (b, reset)
    SWAP_PROP[b] = (a, reset)


_pair("margin-left", "margin-right", "0")
_pair("padding-left", "padding-right", "0")
_pair("left", "right", "auto")
_pair("border-left", "border-right", "0")
_pair("border-left-width", "border-right-width", "0")
_pair("border-left-style", "border-right-style", "none")
_pair("border-left-color", "border-right-color", "transparent")
_pair("border-top-left-radius", "border-top-right-radius", "0")
_pair("border-bottom-left-radius", "border-bottom-right-radius", "0")
_pair("scroll-margin-left", "scroll-margin-right", "0")
_pair("scroll-padding-left", "scroll-padding-right", "0")
_pair("inset-inline-start", "inset-inline-end", "auto")

# property -> {value: mirrored value}
SWAP_VALUE = {
    "text-align": {"left": "right", "right": "left"},
    "float": {"left": "right", "right": "left"},
    "clear": {"left": "right", "right": "left"},
    "flex-direction": {"row": "row-reverse", "row-reverse": "row"},
    "background-position": {"left": "right", "right": "left"},
    "object-position": {"left": "right", "right": "left"},
    "transform-origin": {"left": "right", "right": "left"},
}

# Four-value shorthands mirror as t r b l -> t l b r.
QUAD_SHORTHAND = ("margin", "padding", "inset", "scroll-margin", "scroll-padding")

LEN = r"-?(?:\d*\.)?\d+(?:px|em|rem|%|vw|vh|pt|ch|ex)?"


# ── Minimal tolerant CSS parser ───────────────────────────────────────────
def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def parse(css):
    """Yield (at_rule_prelude_or_None, selector, declaration_text) triples."""
    css = strip_comments(css)
    out = []

    def walk(text, context):
        i = 0
        n = len(text)
        while i < n:
            brace = text.find("{", i)
            if brace == -1:
                break
            prelude = text[i:brace].strip()
            depth = 0
            j = brace
            while j < n:
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            body = text[brace + 1:j]
            if prelude.startswith("@"):
                name = prelude.split()[0].lower()
                # Nested-rule at-rules recurse; @keyframes and @font-face do not
                # carry direction-sensitive layout we can mirror safely.
                if name in ("@media", "@supports", "@layer", "@container"):
                    walk(body, (context + " " if context else "") + prelude)
            elif prelude:
                out.append((context, prelude, body))
            i = j + 1

    walk(css, "")
    return out


def split_decls(body):
    """Split a declaration block, ignoring semicolons inside parentheses."""
    decls = []
    depth = 0
    cur = ""
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth == 0:
            decls.append(cur)
            cur = ""
        else:
            cur += ch
    decls.append(cur)
    out = []
    for d in decls:
        if ":" not in d:
            continue
        prop, _, val = d.partition(":")
        prop = prop.strip().lower()
        val = val.strip()
        if prop and val:
            out.append((prop, val))
    return out


# ── Mirroring ─────────────────────────────────────────────────────────────
def mirror_quad(val):
    """t r b l -> t l b r. Returns None when the value is not four parts."""
    parts = val.split()
    if len(parts) != 4 or any(p.startswith("var(") for p in parts):
        return None
    return " ".join([parts[0], parts[3], parts[2], parts[1]])


def mirror_radius(val):
    """border-radius corners mirror horizontally: tl tr br bl -> tr tl bl br."""
    if "/" in val:
        return None
    parts = val.split()
    if len(parts) == 2:
        return " ".join([parts[1], parts[0]])
    if len(parts) == 3:
        return " ".join([parts[1], parts[0], parts[1], parts[2]])
    if len(parts) == 4:
        return " ".join([parts[1], parts[0], parts[3], parts[2]])
    return None


def negate(m):
    v = m.group(0)
    return v[1:] if v.startswith("-") else "-" + v


def mirror_transform(val):
    if "translateX(" not in val and "translate(" not in val and "translate3d(" not in val:
        return None
    def fix_x(m):
        fn, args = m.group(1), m.group(2)
        parts = [p.strip() for p in args.split(",")]
        parts[0] = re.sub(LEN, negate, parts[0], count=1)
        return "%s(%s)" % (fn, ", ".join(parts))
    out = re.sub(r"\b(translateX|translate|translate3d)\(([^)]*)\)", fix_x, val)
    return out if out != val else None


def split_top_level(val, sep=","):
    """Split on `sep`, ignoring separators inside parentheses (rgba(), var())."""
    parts = []
    depth = 0
    cur = ""
    for ch in val:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return parts


def mirror_shadow(val):
    """Negate the horizontal offset of each shadow in a shadow list.

    The offset is the first length token, and it always precedes any colour
    function — so only the text before the first '(' is searched. Splitting the
    whole value on commas would tear rgba(...) apart and negate its channels.
    """
    if val.strip() in ("none", "inherit", "initial") or "var(" in val:
        return None
    out = []
    changed = False
    for shadow in split_top_level(val):
        s = shadow.strip()
        head_end = s.find("(")
        head = s if head_end == -1 else s[:head_end]
        m = re.search(LEN, head)
        if m and m.group(0) not in ("0", "0px"):
            s = s[:m.start()] + negate(m) + s[m.end():]
            changed = True
        out.append(s)
    return ", ".join(out) if changed else None


def mirror_decls(decls):
    """Return the mirrored declaration list, or [] when nothing is directional."""
    present = {p for p, _ in decls}
    out = []
    for prop, val in decls:
        important = ""
        if val.endswith("!important"):
            important = " !important"
            val = val[:-len("!important")].strip()

        if prop in SWAP_PROP:
            other, reset = SWAP_PROP[prop]
            out.append((other, val + important))
            # Only neutralise the original side when the rule does not set it
            # itself — if it does, that declaration produces its own mirror.
            if other not in present:
                out.append((prop, reset + important))
            continue

        if prop in SWAP_VALUE:
            words = val.split()
            new = [SWAP_VALUE[prop].get(w, w) for w in words]
            if new != words:
                out.append((prop, " ".join(new) + important))
            continue

        if prop in QUAD_SHORTHAND:
            m = mirror_quad(val)
            if m:
                out.append((prop, m + important))
            continue

        if prop == "border-radius":
            m = mirror_radius(val)
            if m:
                out.append((prop, m + important))
            continue

        if prop == "transform":
            m = mirror_transform(val)
            if m:
                out.append((prop, m + important))
            continue

        if prop in ("box-shadow", "text-shadow"):
            m = mirror_shadow(val)
            if m:
                out.append((prop, m + important))
            continue

        # border-width / border-color / border-style quad shorthands are
        # deliberately NOT mirrored. In this codebase they draw glyphs rather
        # than layout borders — `.jb-check-on::after` is a tick made from
        # `border-width:0 2px 2px 0` plus a 45° rotation, and a tick reads the
        # same in Arabic. Real directional borders use the explicit
        # border-left / border-right longhands, which are mirrored above.

    return out


# Selectors that must not simply be prefixed — the prefix would never match.
ROOT_SELECTORS = ("html", ":root", "body", "*", "html body")


def scope(selector):
    """Prefix one comma-separated selector list with [dir="rtl"]."""
    parts = []
    for sel in selector.split(","):
        sel = sel.strip()
        if not sel:
            continue
        low = sel.lower()
        if low in ROOT_SELECTORS:
            parts.append('[dir="rtl"]' if low != "body" else '[dir="rtl"] body')
        elif low.startswith("html "):
            parts.append('html[dir="rtl"] ' + sel[5:])
        elif low.startswith("body "):
            parts.append('[dir="rtl"] ' + sel)
        else:
            parts.append('[dir="rtl"] ' + sel)
    return ", ".join(parts)


def collect_css():
    """All CSS the site ships, as (origin_label, css_text)."""
    blobs = []
    for f in CSS_FILES:
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            blobs.append((f, io.open(p, encoding="utf-8").read()))
    for f in HTML_WITH_EMBEDDED_CSS:
        p = os.path.join(REPO, f)
        if not os.path.exists(p):
            continue
        c = io.open(p, encoding="utf-8").read()
        for i, m in enumerate(re.finditer(r"<style[^>]*>(.*?)</style>", c, re.S)):
            blobs.append(("%s <style> #%d" % (f, i + 1), m.group(1)))
    return blobs


HAND_WRITTEN = """
/* ── Hand-written rules the mirror cannot derive ───────────────────────── */

/* Arabic needs a font stack that actually has Arabic glyphs; the site's
   -apple-system/Segoe/Roboto stack falls back inconsistently across
   platforms and renders Arabic at a noticeably smaller optical size. */
[dir="rtl"], [dir="rtl"] body {
  font-family: "Noto Naskh Arabic", "Geeza Pro", "Segoe UI", Tahoma,
               "Arabic Typesetting", -apple-system, BlinkMacSystemFont, sans-serif;
}
/* Naskh faces sit smaller on the em than Latin faces at the same size. */
[dir="rtl"] body { font-size: 1.05em; line-height: 1.85; }

/* Latin runs (file names, .jwlibrary, JW Sync, URLs, version numbers) must not
   have their punctuation dragged to the wrong end by the bidi algorithm. */
[dir="rtl"] code, [dir="rtl"] kbd, [dir="rtl"] samp, [dir="rtl"] pre,
[dir="rtl"] input[type="file"], [dir="rtl"] .file-name, [dir="rtl"] .jb-meta-pub {
  unicode-bidi: isolate;
}

/* Numeric readouts (stat counters, percentages, dates) stay LTR internally. */
[dir="rtl"] .stat-value, [dir="rtl"] .jb-tab-count, [dir="rtl"] .jb-head-count,
[dir="rtl"] .num, [dir="rtl"] time {
  unicode-bidi: isolate;
  direction: ltr;
  display: inline-block;
}

/* Form controls and progress bars fill from the right. */
[dir="rtl"] input, [dir="rtl"] textarea, [dir="rtl"] select { text-align: right; }
[dir="rtl"] input[type="date"], [dir="rtl"] input[type="number"] {
  direction: ltr;
  text-align: right;
}

/* Native scrollbars and overflow containers. */
[dir="rtl"] .jb-list, [dir="rtl"] .jb-detail { direction: rtl; }

/* User-written content takes its direction from its own first strong
   character, not from the UI language. Without this, an English note read in
   the Arabic UI has its full stop dragged to the left-hand edge
   (".This is my note") because trailing punctuation is bidi-neutral. Arabic
   notes in the same list still render RTL — `plaintext` decides per
   paragraph, which is exactly the mixed-language case this app creates. */
[dir="rtl"] .jb-note-title, [dir="rtl"] .jb-note-excerpt,
[dir="rtl"] .jb-detail-title, [dir="rtl"] .jb-detail-content,
[dir="rtl"] .jb-detail-hl-block, [dir="rtl"] .jb-edit-input,
[dir="rtl"] .jb-edit-textarea, [dir="rtl"] .jb-edit-rte,
[dir="rtl"] .jb-tag, [dir="rtl"] .jb-pub, [dir="rtl"] .jb-detail-pub,
[dir="rtl"] .jb-if-tag, [dir="rtl"] .jb-bm-slot,
[dir="rtl"] .sh-item-title, [dir="rtl"] .sh-item-ex, [dir="rtl"] .sh-item-body,
[dir="rtl"] .sh-ntitle, [dir="rtl"] .sh-nex, [dir="rtl"] .sh-nbody,
[dir="rtl"] .sh-pill-pub, [dir="rtl"] .sh-taglabel {
  unicode-bidi: plaintext;
}

/* The step counter badge in the guides is absolutely positioned at left:0. */
[dir="rtl"] ol.steps li { padding: 0 52px 20px 0; }
[dir="rtl"] ol.steps li::before { left: auto; right: 0; }

/* Breadcrumb separators point the other way. */
[dir="rtl"] .crumbs { direction: rtl; }

/* Language picker keeps its flag emoji on the leading edge. */
[dir="rtl"] .nav-lang-select { background-position: left 8px center; padding: 6px 10px 6px 28px; }
"""


def main():
    blobs = collect_css()
    seen = set()
    chunks = []
    rules = 0
    for origin, css in blobs:
        emitted = []
        for context, selector, body in parse(css):
            if "[dir=" in selector:
                continue
            decls = split_decls(body)
            mirrored = mirror_decls(decls)
            # Drop mirrors that reproduce the original exactly (symmetric
            # padding, symmetric radii) — they would only pad the file.
            original = dict(decls)
            mirrored = [(p, v) for p, v in mirrored if original.get(p) != v]
            if not mirrored:
                continue
            sel = scope(selector)
            if not sel:
                continue
            # A source rule may set the same property twice; keep the last
            # value, as the cascade would.
            collapsed = {}
            for p, v in mirrored:
                collapsed[p] = v
            decl_text = ";".join("%s:%s" % (p, v) for p, v in collapsed.items())
            key = (context, sel, decl_text)
            if key in seen:
                continue
            seen.add(key)
            rule = "%s{%s}" % (sel, decl_text)
            if context:
                rule = "%s{%s}" % (context, rule)
            emitted.append(rule)
            rules += 1
        if emitted:
            chunks.append("/* from %s */\n%s" % (origin, "\n".join(emitted)))

    out = ("/* rtl.css — GENERATED by scripts/build_rtl.py. Do not edit by hand.\n"
           "   Mirrors every direction-sensitive rule the site ships, scoped to\n"
           "   [dir=\"rtl\"] so only Arabic is affected. Re-run the script after\n"
           "   changing any stylesheet. */\n\n"
           + "\n\n".join(chunks)
           + "\n" + HAND_WRITTEN)

    for path in ("rtl.css", os.path.join("beta", "rtl.css")):
        io.open(os.path.join(REPO, path), "w", encoding="utf-8").write(out)
    print("rtl.css: %d mirrored rules from %d stylesheets (%d bytes)"
          % (rules, len(blobs), len(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

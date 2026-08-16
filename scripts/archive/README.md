# scripts/archive — one-off patchers, kept as history

Every file here was run **once**, against a state of the repository that no
longer exists. They are kept because they record what was actually done to ship
a feature or a language, and because their docstrings are often the only
explanation of why a piece of the site looks the way it does.

## Do not run them

That is not a style preference. Re-running one of these has broken the site
three separate times:

- **`add_rtl_wiring.py`** carried its own copy of the `<head>` bootstrap. It was
  re-run, overwrote the shipped copy, and silently reverted a first-paint fix —
  `rtl.css` had been made lazy so it stopped blocking render for the LTR
  languages, and that was undone with nothing to object.
- **the ten `add_*_plumbing.py`** were written by copy-paste from each other and
  shipped two bugs between them: a stale `jw-dir-init` language list on
  Romanian, and a duplicated `<option>` in the nav picker on the same release.
  They are superseded by `../add_language.py`, which derives every insertion
  point from the current files.
- **`patch_navbar_i18n.py`** still contains the seven navbar/mode keys swept in
  v3.35.1. Running it would put them back.

**`build_forum_i18n.py` is here despite its name.** It translated the forum in
two halves that came apart — the dictionary into `forum.html`, the `FT()` calls
into `js/forum.js` — so neither surface worked. `fix_forum_i18n_parity.py`
(also here) replaced it with a single implementation. The `build_` prefix makes
it look like part of the toolchain; it is not.

The general rule, from CLAUDE.md: **a stale script is not necessarily older than
the file it writes.** If you ever do need something in here, read what it writes
and diff that against what is actually in the file first.

## What is *not* here

`scripts/` proper holds only the maintained toolchain — the four builders, the
i18n tools, the guide checkers, `add_language.py`, `verify_wtlocale.py`, and the
`guides_<lang>.py` copy modules. `01_static.js` fails the build if anything else
appears there, so a new one-off belongs in this directory from the start.

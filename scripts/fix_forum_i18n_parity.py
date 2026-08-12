#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_forum_i18n_parity.py — one forum implementation, one dictionary, both sites.

build_forum_i18n.py translated the forum in two halves and they came apart:

  * it embedded window.__FORUM_I18N and the applier in *forum.html only*, and
  * it rewired the runtime strings in *js/forum.js only*.

But the forum ships from two places. forum.html serves the standalone page with
its own inline copy of the forum logic — never rewired, so every dynamic string
there is English in all 25 languages. index.html (and its beta twin) embed the
same markup behind the #forum route and load js/forum.js — which is rewired,
but has no dictionary to read, so window.__forumT is undefined and FT() returns
the key. Readers saw the literal strings "cat_feature", "ago_h" and
"no_replies" on the page.

This script collapses the duplication rather than patching each half again:

  1. writes js/forum-i18n.js — the dictionary plus the applier, one shared copy
     both surfaces load (and 15_parity.js keeps the beta twin identical);
  2. deletes forum.html's inline forum logic and points it at js/forum.js, the
     newer of the two implementations, keeping old #post/<id> links working;
  3. tags the embedded markup in both index.html files with the data-i18n
     attributes forum.html already had;
  4. scopes the landing page's own [data-i18n] pass away from #forum-view,
     because both dictionaries define "hero_title";
  5. rewires the last few runtime strings in js/forum.js that had no key.

Idempotent: every step checks for its own marker first.
"""
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "scripts", "i18n_data", "forum.json")
I18N_JS = os.path.join(REPO, "js", "forum-i18n.js")


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, c):
    io.open(p, "w", encoding="utf-8").write(c)


def sub1(c, old, new, where):
    """Replace exactly one occurrence, or abort."""
    if new in c:
        return c, 0
    n = c.count(old)
    if n != 1:
        sys.exit("ABORT %s: anchor x%d: %s" % (where, n, old[:80]))
    return c.replace(old, new, 1), 1


# ── 1. the shared dictionary + applier ──────────────────────────────────────

RUNTIME = r'''
(function(){
  var L = window.__FORUM_I18N || {};

  function lang(){
    try{ var l = localStorage.getItem('jwsync_lang'); if(l && L[l]) return l; }catch(e){}
    var h = document.documentElement.lang || 'en';
    return L[h] ? h : 'en';
  }
  // Read the table per call rather than once at load: index.html switches
  // language at runtime through the React picker, with no reload to re-run us.
  function table(){ return L[lang()] || L.en || {}; }

  // A value is either a plain string or a map of CLDR plural categories.
  // Intl.PluralRules is what makes Arabic (zero/one/two/few/many/other) and
  // Russian (one/few/many/other) come out right; a one/other pair cannot.
  window.__forumT = function(k, n){
    var v = table()[k];
    if(v == null) v = (L.en && L.en[k]);
    if(v == null) return k;
    if(v && typeof v === 'object'){
      var cat = 'other';
      try{ cat = new Intl.PluralRules(lang()).select(n); }catch(e){}
      v = v[cat] || v.other || v.one || v[Object.keys(v)[0]];
    }
    return n == null ? v : String(v).replace('{n}', n);
  };

  // Scoped to #forum-view where that exists: on index.html the landing page
  // runs its own [data-i18n] pass over a different dictionary, and the two
  // share the key "hero_title".
  function root(){ return document.getElementById('forum-view') || document; }

  function apply(){
    var T = table(), r = root();
    r.querySelectorAll('[data-i18n]').forEach(function(el){
      var v = T[el.getAttribute('data-i18n')]; if(v != null) el.textContent = v; });
    r.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var v = T[el.getAttribute('data-i18n-ph')]; if(v != null) el.setAttribute('placeholder', v); });
    // <option> keeps its leading emoji, which is not part of the translation.
    r.querySelectorAll('[data-i18n-opt]').forEach(function(el){
      var v = T[el.getAttribute('data-i18n-opt')]; if(v == null) return;
      var m = el.textContent.match(/^\s*(\S+)\s/); el.textContent = (m ? m[1] + ' ' : '') + v; });
    // The headline emphasises one word; translations mark it with *asterisks*
    // so each language can put the accent wherever its grammar puts it.
    r.querySelectorAll('[data-i18n-em]').forEach(function(el){
      var v = T[el.getAttribute('data-i18n-em')]; if(v == null) return;
      var parts = String(v).split('*');
      el.textContent = '';
      parts.forEach(function(p, i){
        if(i % 2){ var s = document.createElement('span'); s.textContent = p; el.appendChild(s); }
        else el.appendChild(document.createTextNode(p)); });
    });
    // Post cards, reply counts and relative dates are drawn by js/forum.js from
    // its own state, so they need a redraw rather than an attribute pass.
    if(typeof window.__forumRerender === 'function') window.__forumRerender();
  }
  window.__forumApplyI18N = apply;

  // The tab title and meta description are derived from strings that are
  // already translated, so the forum needs no extra copy to localize them.
  // Standalone page only — inside the app the landing copy owns the title and
  // enhancements.js sets it for the #forum route.
  function meta(){
    if(document.getElementById('forum-view')) return;
    var T = table();
    if(T.logo_sub) document.title = 'JW Sync — ' + T.logo_sub;
    var dm = document.querySelector('meta[name="description"]');
    if(dm && T.hero_sub) dm.setAttribute('content', T.hero_sub);
  }

  meta();
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply);
  else apply();
}());
'''

HEADER = '''/* ─────────────────────────────────────────────────────────────────────────────
   JW Sync — js/forum-i18n.js
   The community forum's UI copy in all 25 languages, plus the runtime that
   applies it.

   This table used to live inline in forum.html only, but the forum ships from
   two places: that page, and the #forum route inside both index.html files.
   On the embedded route window.__forumT did not exist, so js/forum.js fell
   back to returning the key and readers saw "cat_feature", "ago_h" and
   "no_replies" on the page. One shared copy is the fix — a file rather than a
   second inline blob, because 44 KB of dictionary in the document would land
   in front of the render-blocking CSS.

   Generated by scripts/fix_forum_i18n_parity.py from
   scripts/i18n_data/forum.json — edit the JSON, not this file.

   Declares: window.__FORUM_I18N, window.__forumT, window.__forumApplyI18N
   ───────────────────────────────────────────────────────────────────────── */
window.__FORUM_I18N='''


def build_i18n_js():
    data = json.load(io.open(DATA, encoding="utf-8"))
    body = (HEADER
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            + ";\n" + RUNTIME)
    write(I18N_JS, body)
    write(os.path.join(REPO, "beta", "js", "forum-i18n.js"), body)
    print("js/forum-i18n.js: %d languages, %d keys" % (len(data), len(data["en"])))


# ── 2. forum.html: drop the duplicate implementation ────────────────────────

FORUM_HTML_TAIL = """<script src="js/forum-i18n.js"></script>
<script src="js/forum.js"></script>
<script>
// The standalone page has no router of its own, so it boots the forum straight
// away. Inside the app, enhancements.js calls this on the #forum route instead.
jwsyncForumInit();
</script>"""


def patch_forum_html():
    path = os.path.join(REPO, "forum.html")
    c = read(path)
    orig = c

    # (a) inline dictionary -> shared file
    if 'id="forum-i18n-data"' in c:
        m = re.search(r'<script id="forum-i18n-data">.*?</script>\n?', c, re.S)
        if not m:
            sys.exit("ABORT forum.html: dictionary block not matched")
        c = c[:m.start()] + c[m.end():]

    # (b) inline applier -> shared file
    if 'id="forum-i18n"' in c:
        m = re.search(r'<script id="forum-i18n">.*?</script>\n?', c, re.S)
        if not m:
            sys.exit("ABORT forum.html: applier block not matched")
        c = c[:m.start()] + c[m.end():]

    # (c) the inline copy of the forum logic -> js/forum.js
    if "js/forum.js" not in c:
        m = re.search(r"<script>\n// ── Supabase ─+\n.*?\n</script>", c, re.S)
        if not m:
            sys.exit("ABORT forum.html: inline forum logic not matched")
        c = c[:m.start()] + FORUM_HTML_TAIL + c[m.end():]

    if c != orig:
        write(path, c)
        print("forum.html: inline duplicate removed, shared scripts wired")
    else:
        print("forum.html: already patched")


# ── 3. the embedded forum view in both index.html files ─────────────────────

# The embedded markup diverged from forum.html's (SVG icons instead of emoji,
# an email card, longer category labels), so it needs its own anchors.
EMBED_MARKUP = [
    ('<div class="logo-sub">Community</div>',
     '<div class="logo-sub" data-i18n="logo_sub">Community</div>'),
    ('<a class="back-btn" href="#">← Back to app</a>',
     '<a class="back-btn" href="#" data-i18n="back_app">← Back to app</a>'),
    ('<h1>Ask questions, share <span>tips</span>, report bugs.</h1>',
     '<h1 data-i18n-em="hero_title">Ask questions, share <span>tips</span>, report bugs.</h1>'),
    ('<p>A space for JW Sync users — all questions welcome, no matter how simple.</p>',
     '<p data-i18n="hero_sub">A space for JW Sync users — all questions welcome, no matter how simple.</p>'),
    ('</svg>New Post</button>',
     '</svg><span data-i18n="new_post">New Post</span></button>'),
    ('<h3>New Post</h3>', '<h3 data-i18n="new_post">New Post</h3>'),
    ('<label class="form-label">Category</label>',
     '<label class="form-label" data-i18n="f_category">Category</label>'),
    ('<option value="question">Question</option>',
     '<option value="question" data-i18n="cat_question">Question</option>'),
    ('<option value="bug">Bug Report</option>',
     '<option value="bug" data-i18n="cat_bug">Bug Report</option>'),
    ('<option value="feature">Feature Request</option>',
     '<option value="feature" data-i18n="cat_feature">Feature Request</option>'),
    ('<option value="general">General</option>',
     '<option value="general" data-i18n="cat_general">General</option>'),
    ('<label class="form-label">Title <span style="color:var(--red)">*</span></label>',
     '<label class="form-label"><span data-i18n="f_title">Title</span> '
     '<span style="color:var(--red)">*</span></label>'),
    ('placeholder="What\'s your question or topic?"',
     'placeholder="What\'s your question or topic?" data-i18n-ph="ph_title"'),
    ('<label class="form-label">Details</label>',
     '<label class="form-label" data-i18n="f_details">Details</label>'),
    ('placeholder="Describe in more detail (optional)…"',
     'placeholder="Describe in more detail (optional)…" data-i18n-ph="ph_details"'),
    ('<label class="form-label">Your name <span style="color:var(--red)">*</span></label>',
     '<label class="form-label"><span data-i18n="f_name">Your name</span> '
     '<span style="color:var(--red)">*</span></label>'),
    ('placeholder="How should we call you?"',
     'placeholder="How should we call you?" data-i18n-ph="ph_name"'),
    ('onclick="toggleCompose()">Cancel</button>',
     'onclick="toggleCompose()" data-i18n="cancel">Cancel</button>'),
    ('onclick="submitPost()">Post →</button>',
     'onclick="submitPost()" data-i18n="post_btn">Post →</button>'),
    ("onclick=\"setFilter('all')\">All posts</span>",
     "onclick=\"setFilter('all')\" data-i18n=\"filter_all\">All posts</span>"),
    ('</svg>Questions</span>',
     '</svg><span data-i18n="filter_questions">Questions</span></span>'),
    ('</svg>Bugs</span>',
     '</svg><span data-i18n="filter_bugs">Bugs</span></span>'),
    ('</svg>Features</span>',
     '</svg><span data-i18n="filter_features">Features</span></span>'),
    ('</svg>General</span>',
     '</svg><span data-i18n="filter_general">General</span></span>'),
    ('<strong id="s-posts">—</strong>Posts</div>',
     '<strong id="s-posts">—</strong><span data-i18n="s_posts">Posts</span></div>'),
    ('<strong id="s-replies">—</strong>Replies</div>',
     '<strong id="s-replies">—</strong><span data-i18n="s_replies">Replies</span></div>'),
    ('<strong id="s-solved">—</strong>Solved</div>',
     '<strong id="s-solved">—</strong><span data-i18n="s_solved">Solved</span></div>'),
    ('<p>Loading posts…</p>', '<p data-i18n="loading">Loading posts…</p>'),
    ('<p>JW Sync Community · <a href="#">← Back to the app</a></p>',
     '<p><span data-i18n="footer_txt">JW Sync Community</span> · '
     '<a href="#" data-i18n="back_app">← Back to the app</a></p>'),
    ('onclick="closeThread()">← Back to community</button>',
     'onclick="closeThread()" data-i18n="back_community">← Back to community</button>'),
    ('<h4>Write a reply</h4>', '<h4 data-i18n="write_reply">Write a reply</h4>'),
    ('placeholder="Your name / nickname"',
     'placeholder="Your name / nickname" data-i18n-ph="ph_r_name"'),
    ('placeholder="Write your reply…"',
     'placeholder="Write your reply…" data-i18n-ph="ph_reply"'),
    ('onclick="submitReply()">Reply →</button>',
     'onclick="submitReply()" data-i18n="reply_btn">Reply →</button>'),
]

# The landing page applies its own dictionary to every [data-i18n] in the
# document. Both tables define "hero_title", so the forum view is excluded.
LANDING_SCOPE_OLD = """    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k=el.getAttribute('data-i18n');
      var v=T[k]; if(v==null||v==='')v=TL[k];
      if(v!=null)el.textContent=v;
    });"""
LANDING_SCOPE_NEW = """    document.querySelectorAll('[data-i18n]').forEach(function(el){
      // The embedded forum view carries its own dictionary (js/forum-i18n.js)
      // and the two tables share the key "hero_title".
      if(el.closest('#forum-view'))return;
      var k=el.getAttribute('data-i18n');
      var v=T[k]; if(v==null||v==='')v=TL[k];
      if(v!=null)el.textContent=v;
    });"""


def patch_index(rel):
    path = os.path.join(REPO, rel)
    c = read(path)
    orig = c

    c, _ = sub1(c, '<script src="js/forum.js" defer></script>',
                '<script src="js/forum-i18n.js" defer></script>\n'
                '<script src="js/forum.js" defer></script>', rel)

    tagged = 0
    for old, new in EMBED_MARKUP:
        c, n = sub1(c, old, new, rel)
        tagged += n

    c, _ = sub1(c, LANDING_SCOPE_OLD, LANDING_SCOPE_NEW, rel)

    if c != orig:
        write(path, c)
        print("%s: %d markup tag(s), dictionary wired, landing pass scoped"
              % (rel, tagged))
    else:
        print("%s: already patched" % rel)


# ── 4. js/forum.js: the strings that had no key, plus the shared hooks ───────

JS_PATCHES = [
    # Legacy deep links. forum.html addressed threads at #post/<id> before the
    # app embedded the forum at #forum/post/<id>; links shared from the old
    # page are still in circulation.
    ("const THREAD_HASH_RE = /^#forum\\/post\\/(.+)$/;",
     "const THREAD_HASH_RE = /^#forum\\/post\\/(.+)$/;\n"
     "// forum.html addressed threads at #post/<id> before the app embedded the\n"
     "// forum; links shared from that page are still in circulation.\n"
     "const LEGACY_HASH_RE = /^#post\\/(.+)$/;"),
    ("<h3>Couldn't load posts</h3>", "<h3>${FT('err_load_posts')}</h3>"),
    ('onclick="load()">Try again</button>',
     'onclick="load()">${FT(\'try_again\')}</button>'),
    ("'<div style=\"padding:14px 0;color:var(--muted);font-size:13px\">Loading replies…</div>'",
     "`<div style=\"padding:14px 0;color:var(--muted);font-size:13px\">${FT('loading_replies')}</div>`"),
    ("                    Copy link\n", "                    ${FT('copy_link')}\n"),
    ("title=\"Copy a direct link to this post\"", "title=\"${esc(FT('copy_link'))}\""),
    ("<div style=\"font-size:15px;font-weight:600;color:#e8ddd5;margin-bottom:6px\">Could not load community forum</div>",
     "<div style=\"font-size:15px;font-weight:600;color:#e8ddd5;margin-bottom:6px\">' + FT('err_load_posts') + '</div>"),
]

# syncThreadRoute() reads the hash on load and on every hashchange.
SYNC_OLD = """function syncThreadRoute() {"""
SYNC_NEW = """function syncThreadRoute() {
    // Rewrite a legacy #post/<id> link to the canonical route before matching.
    const legacy = location.hash.match(LEGACY_HASH_RE);
    if (legacy) {
        history.replaceState(null, '', '#forum/post/' + legacy[1]);
    }"""

RERENDER = """

// ── Language changes ───────────────────────────────────────────────────────
// index.html switches language without a reload, so the applier in
// js/forum-i18n.js calls this to redraw what is already on screen.
window.__forumRerender = function () {
    if (!posts.length) return;   // still loading: leave the state box alone
    render();
    stats();
    if (activePostId && document.getElementById('overlay').classList.contains('open')) {
        showThread(activePostId);
    }
};
"""


def patch_forum_js():
    path = os.path.join(REPO, "js", "forum.js")
    c = read(path)
    orig = c

    applied = 0
    for old, new in JS_PATCHES:
        c, n = sub1(c, old, new, "js/forum.js")
        applied += n

    # The solved badge is drawn twice — once per post card, once per thread.
    badge_old = "'<span class=\"solved-badge\">✓ Solved</span>'"
    badge_new = "`<span class=\"solved-badge\">✓ ${FT('s_solved')}</span>`"
    if badge_new not in c:
        n = c.count(badge_old)
        if n != 2:
            sys.exit("ABORT js/forum.js: solved badge x%d, expected 2" % n)
        c = c.replace(badge_old, badge_new)
        applied += n

    if "LEGACY_HASH_RE" in c and "legacy[1]" not in c:
        c, _ = sub1(c, SYNC_OLD, SYNC_NEW, "js/forum.js")

    if "__forumRerender" not in c:
        anchor = "// ── Lazy initialization ──"
        if c.count(anchor) != 1:
            sys.exit("ABORT js/forum.js: no place for the rerender hook")
        c = c.replace(anchor, RERENDER.lstrip("\n") + "\n" + anchor, 1)

    # The comment describing where the dictionary lives is now wrong.
    c = c.replace(
        "// UI copy lives in window.__FORUM_I18N (embedded in forum.html) and is read\n"
        "// through the helper the page installs. The fallback keeps this file usable if\n"
        "// the script order ever changes.",
        "// UI copy lives in window.__FORUM_I18N (js/forum-i18n.js, loaded by both the\n"
        "// standalone page and the app) and is read through the helper it installs.\n"
        "// The fallback keeps this file usable if the script order ever changes.")

    if c != orig:
        write(path, c)
        print("js/forum.js: %d string(s) rewired, legacy route + rerender hook added"
              % applied)
    else:
        print("js/forum.js: already patched")

    write(os.path.join(REPO, "beta", "js", "forum.js"), read(path))


# ── 5. enhancements.js: re-apply on route entry ─────────────────────────────

ENH_OLD = """      if (isForum && typeof window.jwsyncForumInit === 'function') {
        window.jwsyncForumInit();
      }
      // Update <title> for clarity
      document.title = isForum
        ? 'JW Sync — Community'
        : 'JW Library Backup Merger | Combine Notes & Highlights';"""

ENH_NEW = """      if (isForum && typeof window.jwsyncForumInit === 'function') {
        window.jwsyncForumInit();
      }
      // The forum view carries its own dictionary and the language may have
      // changed in the app since it was last applied.
      if (isForum && typeof window.__forumApplyI18N === 'function') {
        window.__forumApplyI18N();
      }
      // Update <title> for clarity
      var forumT = window.__forumT;
      document.title = isForum
        ? 'JW Sync — ' + (forumT ? forumT('logo_sub') : 'Community')
        : 'JW Library Backup Merger | Combine Notes & Highlights';"""


def patch_enhancements():
    for rel in ("js/enhancements.js", "beta/js/enhancements.js"):
        path = os.path.join(REPO, rel)
        c = read(path)
        c2, n = sub1(c, ENH_OLD, ENH_NEW, rel)
        if n:
            write(path, c2)
            print("%s: forum route re-applies i18n" % rel)
        else:
            print("%s: already patched" % rel)


if __name__ == "__main__":
    build_i18n_js()
    patch_forum_html()
    patch_index("index.html")
    patch_index("beta/index.html")
    patch_forum_js()
    patch_enhancements()

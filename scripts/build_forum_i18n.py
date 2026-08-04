#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_forum_i18n.py — translate the community forum.

forum.html and js/forum.js were the last English-only surface on the site: no
dictionary at all, so every one of the thirteen languages saw an English page
with a translated header above it.

This script:
  1. embeds scripts/i18n_data/forum.json as window.__FORUM_I18N,
  2. tags the static markup with data-i18n / data-i18n-ph attributes and adds
     the tiny applier that runs them,
  3. rewires the runtime strings in js/forum.js (toasts, empty states, the
     category badges and the relative-time formatter) to read the same
     dictionary,
  4. mirrors js/forum.js to beta/, which 15_parity.js requires.

The language comes from jwsync_lang, which the jw-dir-init snippet in <head>
already populates from ?lang= — the forum has no picker of its own, matching
the other satellite pages.

Idempotent: every step checks for its own marker first.
"""
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_data", "forum.json")

# (search, replace) over forum.html's static markup.
MARKUP = [
    ('<div class="logo-sub">Community</div>',
     '<div class="logo-sub" data-i18n="logo_sub">Community</div>'),
    ('<a class="back-btn" href="index.html">← Back to app</a>',
     '<a class="back-btn" href="index.html" data-i18n="back_app">← Back to the app</a>'),
    ('<h1>Ask questions, share <span>tips</span>, report bugs.</h1>',
     '<h1 data-i18n-em="hero_title">Ask questions, share <span>tips</span>, report bugs.</h1>'),
    ('<p>A space for JW Sync users — all questions welcome, no matter how simple.</p>',
     '<p data-i18n="hero_sub">A space for JW Sync users — all questions welcome, no matter how simple.</p>'),
    ('onclick="toggleCompose()">✏️ New Post</button>',
     'onclick="toggleCompose()">✏️ <span data-i18n="new_post">New Post</span></button>'),
    ('<h3>New Post</h3>', '<h3 data-i18n="new_post">New Post</h3>'),
    ('<label class="form-label">Category</label>',
     '<label class="form-label" data-i18n="f_category">Category</label>'),
    ('<option value="question">❓ Question</option>',
     '<option value="question" data-i18n-opt="cat_question">❓ Question</option>'),
    ('<option value="bug">🐛 Bug Report</option>',
     '<option value="bug" data-i18n-opt="cat_bug">🐛 Bug</option>'),
    ('<option value="feature">💡 Feature Request</option>',
     '<option value="feature" data-i18n-opt="cat_feature">💡 Feature</option>'),
    ('<option value="general">💬 General</option>',
     '<option value="general" data-i18n-opt="cat_general">💬 General</option>'),
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
    ("onclick=\"setFilter('question')\">❓ Questions</span>",
     "onclick=\"setFilter('question')\">❓ <span data-i18n=\"filter_questions\">Questions</span></span>"),
    ("onclick=\"setFilter('bug')\">🐛 Bugs</span>",
     "onclick=\"setFilter('bug')\">🐛 <span data-i18n=\"filter_bugs\">Bugs</span></span>"),
    ("onclick=\"setFilter('feature')\">💡 Features</span>",
     "onclick=\"setFilter('feature')\">💡 <span data-i18n=\"filter_features\">Features</span></span>"),
    ("onclick=\"setFilter('general')\">💬 General</span>",
     "onclick=\"setFilter('general')\">💬 <span data-i18n=\"filter_general\">General</span></span>"),
    ('<strong id="s-posts">—</strong>Posts</div>',
     '<strong id="s-posts">—</strong><span data-i18n="s_posts">Posts</span></div>'),
    ('<strong id="s-replies">—</strong>Replies</div>',
     '<strong id="s-replies">—</strong><span data-i18n="s_replies">Replies</span></div>'),
    ('<strong id="s-solved">—</strong>Solved</div>',
     '<strong id="s-solved">—</strong><span data-i18n="s_solved">Solved</span></div>'),
    ('<p>Loading posts…</p>', '<p data-i18n="loading">Loading posts…</p>'),
    ('<p>JW Sync Community · <a href="index.html">← Back to the app</a></p>',
     '<p><span data-i18n="footer_txt">JW Sync Community</span> · '
     '<a href="index.html" data-i18n="back_app">← Back to the app</a></p>'),
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

APPLIER = """<script id="forum-i18n">
(function(){
  var L=window.__FORUM_I18N||{};
  function lang(){try{var l=localStorage.getItem('jwsync_lang');if(l&&L[l])return l;}catch(e){}
    var h=document.documentElement.lang||'en';return L[h]?h:'en';}
  var T=L[lang()]||L.en||{};
  // Exposed for js/forum.js, which needs the same table for its runtime copy.
  // A value is either a plain string or a map of CLDR plural categories.
  // Intl.PluralRules is what makes Arabic (zero/one/two/few/many/other) and
  // Russian (one/few/many/other) come out right; a one/other pair cannot.
  window.__forumT=function(k,n){
    var v=T[k];if(v==null)v=(L.en&&L.en[k]);if(v==null)return k;
    if(v&&typeof v==='object'){
      var cat='other';
      try{cat=new Intl.PluralRules(lang()).select(n);}catch(e){}
      v=v[cat]||v.other||v.one||v[Object.keys(v)[0]];
    }
    return n==null?v:String(v).replace('{n}',n);};
  function apply(){
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var v=T[el.getAttribute('data-i18n')];if(v!=null)el.textContent=v;});
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var v=T[el.getAttribute('data-i18n-ph')];if(v!=null)el.setAttribute('placeholder',v);});
    // <option> keeps its leading emoji, which is not part of the translation.
    document.querySelectorAll('[data-i18n-opt]').forEach(function(el){
      var v=T[el.getAttribute('data-i18n-opt')];if(v==null)return;
      var m=el.textContent.match(/^\\s*(\\S+)\\s/);el.textContent=(m?m[1]+' ':'')+v;});
    // The headline emphasises one word; translations mark it with *asterisks*
    // so each language can put the accent wherever its grammar puts it.
    document.querySelectorAll('[data-i18n-em]').forEach(function(el){
      var v=T[el.getAttribute('data-i18n-em')];if(v==null)return;
      var parts=String(v).split('*');
      el.textContent='';
      parts.forEach(function(p,i){
        if(i%2){var s=document.createElement('span');s.textContent=p;el.appendChild(s);}
        else el.appendChild(document.createTextNode(p));});
    });
  }
  // The tab title and meta description are derived from strings that are
  // already translated, so the forum needs no extra copy to localize them.
  function meta(){
    if(T.logo_sub)document.title='JW Sync \u2014 '+T.logo_sub;
    var dm=document.querySelector('meta[name="description"]');
    if(dm&&T.hero_sub)dm.setAttribute('content',T.hero_sub);
  }
  meta();
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply);
  else apply();
}());
</script>"""

# (search, replace) over js/forum.js's runtime strings.
RUNTIME = [
    ("toast('Please add a title.','error')", "toast(FT('err_title'),'error')"),
    ("toast('Please add your name.','error')", "toast(FT('err_name'),'error')"),
    ("toast('Posted! ✓')", "toast(FT('posted'))"),
    ("toast('Reply posted! ✓')", "toast(FT('reply_posted'))"),
    ("toast('Reply cannot be empty.','error')", "toast(FT('reply_empty'),'error')"),
    ("toast('Already upvoted!','error',1800)", "toast(FT('already_voted'),'error',1800)"),
    ("toast('Vote failed: '+e.message,'error')", "toast(FT('vote_failed')+e.message,'error')"),
    ("toast('Error: '+e.message,'error')", "toast(FT('err_generic')+e.message,'error')"),
    ("toast('That post could not be found.','error')", "toast(FT('not_found'),'error')"),
    ("toast('Link copied ✓')", "toast(FT('link_copied'))"),
    ("toast('Could not copy the link.','error')", "toast(FT('copy_failed'),'error')"),
    ("btn.textContent = 'Posting…';", "btn.textContent = FT('posting');"),
    ("new Error('Could not load forum library')", "new Error(FT('lib_failed'))"),
    ("filter==='all'?'No posts yet':'No posts here'",
     "filter==='all'?FT('no_posts_yet'):FT('no_posts_here')"),
    ("filter==='all'?'Be the first to post!':'Try a different filter.'",
     "filter==='all'?FT('be_first'):FT('try_filter')"),
    ("replies.length===0 ? 'No replies yet — be the first!' : "
     "`${replies.length} ${replies.length===1?'reply':'replies'}`",
     "replies.length===0 ? FT('no_replies') : FT('n_replies', replies.length)"),
    # Reply-count chip on each post card. n_reply/n_replies already carry the
    # number, so the separate ${rc} goes with them.
    ("💬 ${rc} ${rc===1?'reply':'replies'}",
     "💬 ${FT('n_replies', rc)}"),
    ("({question:'❓ Question',bug:'🐛 Bug',feature:'💡 Feature',general:'💬 General'}[c]||c)",
     "({question:'❓ '+FT('cat_question'),bug:'🐛 '+FT('cat_bug'),"
     "feature:'💡 '+FT('cat_feature'),general:'💬 '+FT('cat_general')}[c]||c)"),
    ("""    if (m < 1) return 'just now';
    if (m < 60) return m + 'm ago';
    const h = Math.floor(m/60);
    if (h < 24) return h + 'h ago';
    const d = Math.floor(h/24);
    return d < 7 ? d + 'd ago' : new Date(iso).toLocaleDateString();""",
     """    if (m < 1) return FT('ago_now');
    if (m < 60) return FT('ago_m', m);
    const h = Math.floor(m/60);
    if (h < 24) return FT('ago_h', h);
    const d = Math.floor(h/24);
    // Past a week an absolute date is clearer, and toLocaleDateString already
    // formats it for the reader's locale.
    return d < 7 ? FT('ago_d', d) : new Date(iso).toLocaleDateString();"""),
]

FT_HELPER = """// UI copy lives in window.__FORUM_I18N (embedded in forum.html) and is read
// through the helper the page installs. The fallback keeps this file usable if
// the script order ever changes.
const FT = (k, n) => (window.__forumT ? window.__forumT(k, n) : k);
"""


def patch_html():
    path = os.path.join(REPO, "forum.html")
    c = io.open(path, encoding="utf-8").read()
    orig = c

    if "__FORUM_I18N" not in c:
        data = json.load(io.open(DATA, encoding="utf-8"))
        block = ('<script id="forum-i18n-data">window.__FORUM_I18N='
                 + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
                 + ';</script>')
        anchor = "</head>"
        if c.count(anchor) != 1:
            sys.exit("ABORT forum.html: %d </head>" % c.count(anchor))
        c = c.replace(anchor, block + "\n" + anchor, 1)

    applied = 0
    for old, new in MARKUP:
        if new in c:
            continue
        if c.count(old) != 1:
            sys.exit("ABORT forum.html: markup anchor x%d: %s"
                     % (c.count(old), old[:70]))
        c = c.replace(old, new, 1)
        applied += 1

    if 'id="forum-i18n"' not in c:
        anchor = "</body>"
        if c.count(anchor) != 1:
            sys.exit("ABORT forum.html: %d </body>" % c.count(anchor))
        c = c.replace(anchor, APPLIER + "\n" + anchor, 1)

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("forum.html: %d markup tag(s), dictionary + applier installed" % applied)
    else:
        print("forum.html: already patched")


def patch_js():
    path = os.path.join(REPO, "js", "forum.js")
    c = io.open(path, encoding="utf-8").read()
    orig = c

    applied = 0
    for old, new in RUNTIME:
        n = c.count(old)
        if not n:
            if new in c:
                continue  # already applied
            sys.exit("ABORT forum.js: anchor not found: %s" % old[:70])
        # Several toasts are raised from both the post and the reply path, so
        # every occurrence is rewritten rather than just the first.
        c = c.replace(old, new)
        applied += n

    if "const FT =" not in c:
        m = re.search(r"^const ago = ", c, re.M)
        if not m:
            sys.exit("ABORT forum.js: no place to install the FT helper")
        c = c[:m.start()] + FT_HELPER + "\n" + c[m.start():]

    if c != orig:
        io.open(path, "w", encoding="utf-8").write(c)
        print("js/forum.js: %d runtime string(s) rewired" % applied)
    else:
        print("js/forum.js: already patched")

    # Shared tool-layer file: both sites ship the same copy.
    beta = os.path.join(REPO, "beta", "js", "forum.js")
    io.open(beta, "w", encoding="utf-8").write(io.open(path, encoding="utf-8").read())


if __name__ == "__main__":
    patch_html()
    patch_js()

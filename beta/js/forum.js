/* =============================================================================
   JW Sync Beta — js/forum.js
   Community forum: state management, rendering, Supabase data layer.
   Loaded as a plain <script> tag after the DOM. No module system.
   Declares: window.jwsyncForumInit, window.__jwsync_forum_loaded__
   ============================================================================= */


// ── Supabase ──────────────────────────────────────────────────
let createClient;  // assigned in jwsyncForumInit after Supabase library loads
let db;  // assigned in jwsyncForumInit

// ── State ─────────────────────────────────────────────────────
let posts = [], filter = 'all', activePostId = null;
let votedP = new Set(JSON.parse(localStorage.getItem('vp') || '[]'));
let votedR = new Set(JSON.parse(localStorage.getItem('vr') || '[]'));
const saveVotes = () => {
    localStorage.setItem('vp', JSON.stringify([...votedP]));
    localStorage.setItem('vr', JSON.stringify([...votedR]));
};

// ── Utils ─────────────────────────────────────────────────────
const esc = s => String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const ago = iso => {
    const m = Math.floor((Date.now() - new Date(iso)) / 60000);
    if (m < 1) return 'just now';
    if (m < 60) return m + 'm ago';
    const h = Math.floor(m/60);
    if (h < 24) return h + 'h ago';
    const d = Math.floor(h/24);
    return d < 7 ? d + 'd ago' : new Date(iso).toLocaleDateString();
};
const aColor = n => {
    const c = ['#f97316','#60a5fa','#22c55e','#a78bfa','#f472b6','#fb923c','#34d399','#38bdf8'];
    let h = 0; for (const x of String(n||'?')) h = (h*31 + x.charCodeAt(0)) & 0xffffffff;
    return c[Math.abs(h) % c.length];
};
const catLabel = c => ({question:'❓ Question',bug:'🐛 Bug',feature:'💡 Feature',general:'💬 General'}[c]||c);
const catCls   = c => 'cat-'+(c||'general');
const cc = (src, dst, max) => { const el = document.getElementById(dst); if(el) el.textContent = document.getElementById(src)?.value?.length||0; };

let toastTimer;
const toast = (msg, type='success', ms=3000) => {
    const t = document.getElementById('toast');
    t.textContent = msg; t.className = 'toast show ' + type;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.className = 'toast', ms);
};

// ── Load posts ────────────────────────────────────────────────
async function load() {
    try {
        const { data, error } = await db
            .from('posts')
            .select('*, replies(count)')
            .order('created_at', { ascending: false });
        if (error) throw error;
        posts = data || [];
        render(); stats();
    } catch(e) {
        document.getElementById('post-list').innerHTML = `
            <div class="state-box">
                <div class="icon">⚠️</div>
                <h3>Couldn't load posts</h3>
                <p>${esc(e.message)}</p>
                <button class="btn btn-ghost" style="margin-top:12px" onclick="load()">Try again</button>
            </div>`;
    }
}

function render() {
    const shown = filter === 'all' ? posts : posts.filter(p => p.category === filter);
    const list  = document.getElementById('post-list');
    if (!shown.length) {
        list.innerHTML = `<div class="state-box"><div class="icon">💬</div><h3>${filter==='all'?'No posts yet':'No posts here'}</h3><p>${filter==='all'?'Be the first to post!':'Try a different filter.'}</p></div>`;
        return;
    }
    list.innerHTML = shown.map(p => {
        const rc = p.replies?.[0]?.count ?? 0;
        const col = aColor(p.author);
        const voted = votedP.has(p.id);
        return `<div class="post-item" onclick="openThread('${esc(p.id)}')">
            <div class="vote-col" onclick="event.stopPropagation()">
                <button class="vote-btn${voted?' voted':''}" onclick="votePost('${esc(p.id)}',this)">▲</button>
                <span class="vote-count${p.votes>0?' hi':''}" id="pv-${esc(p.id)}">${p.votes}</span>
            </div>
            <div class="post-body">
                <div class="badges">
                    <span class="cat-badge ${catCls(p.category)}">${catLabel(p.category)}</span>
                    ${p.solved?'<span class="solved-badge">✓ Solved</span>':''}
                </div>
                <div class="post-title">${esc(p.title)}</div>
                ${p.content?`<div class="post-excerpt">${esc(p.content)}</div>`:''}
                <div class="post-meta">
                    <span class="meta-chip"><div class="avatar-sm" style="background:${col}">${esc((p.author[0]||'?').toUpperCase())}</div>${esc(p.author)}</span>
                    <span class="meta-chip reply-chip">💬 ${rc} ${rc===1?'reply':'replies'}</span>
                    <span class="meta-chip mono">${ago(p.created_at)}</span>
                </div>
            </div>
        </div>`;
    }).join('');
}

function stats() {
    document.getElementById('s-posts').textContent   = posts.length;
    document.getElementById('s-solved').textContent  = posts.filter(p=>p.solved).length;
    document.getElementById('s-replies').textContent = posts.reduce((a,p) => a + (p.replies?.[0]?.count??0), 0);
}

// ── Filter ────────────────────────────────────────────────────
function setFilter(cat) {
    filter = cat;
    document.querySelectorAll('.pill').forEach(p => p.classList.toggle('active', p.dataset.cat === cat));
    render();
}

// ── Compose ───────────────────────────────────────────────────
function toggleCompose() {
    const p = document.getElementById('compose-panel');
    const open = p.classList.toggle('open');
    if (open) p.scrollIntoView({ behavior:'smooth', block:'nearest' });
}

async function submitPost() {
    const title  = document.getElementById('new-title').value.trim();
    const body   = document.getElementById('new-body').value.trim();
    const author = document.getElementById('new-author').value.trim();
    const cat    = document.getElementById('new-cat').value;
    if (!title)  { toast('Please add a title.','error'); return; }
    if (!author) { toast('Please add your name.','error'); return; }
    const btn = document.getElementById('post-btn');
    btn.disabled = true; btn.textContent = 'Posting…';
    try {
        const { error } = await db.from('posts').insert({ title, content: body||null, author, category: cat, votes: 0 });
        if (error) throw error;
        ['new-title','new-body','new-author'].forEach(id => document.getElementById(id).value='');
        ['tc','bc'].forEach(id => document.getElementById(id).textContent='0');
        document.getElementById('compose-panel').classList.remove('open');
        toast('Posted! ✓');
        await load();
    } catch(e) {
        toast('Error: '+e.message,'error');
    } finally {
        btn.disabled = false; btn.textContent = 'Post →';
    }
}

// ── Vote post ─────────────────────────────────────────────────
async function votePost(id, btn) {
    if (votedP.has(id)) { toast('Already upvoted!','error',1800); return; }
    const post = posts.find(p=>p.id===id);
    if (post) post.votes++;
    const el = document.getElementById('pv-'+id);
    if (el) { el.textContent = post?.votes??''; el.classList.add('hi'); }
    btn?.classList.add('voted');
    votedP.add(id); saveVotes();
    try {
        const { error } = await db.from('posts').update({ votes: post?.votes??1 }).eq('id',id);
        if (error) throw error;
    } catch(e) {
        votedP.delete(id); saveVotes();
        if (post) post.votes--;
        if (el) el.textContent = post?.votes??'';
        btn?.classList.remove('voted');
        toast('Vote failed: '+e.message,'error');
    }
}

// ── Thread ────────────────────────────────────────────────────
async function openThread(id) {
    activePostId = id;
    const post = posts.find(p=>p.id===id);
    if (!post) return;
    document.getElementById('overlay').classList.add('open');
    document.body.style.overflow = 'hidden';
    const col = aColor(post.author);
    const voted = votedP.has(id);
    document.getElementById('thread-post').innerHTML = `
        <div class="thread-card original">
            <div class="badges">
                <span class="cat-badge ${catCls(post.category)}">${catLabel(post.category)}</span>
                ${post.solved?'<span class="solved-badge">✓ Solved</span>':''}
            </div>
            <div class="thread-title">${esc(post.title)}</div>
            ${post.content?`<div class="thread-content">${esc(post.content)}</div>`:''}
            <div class="thread-footer">
                <div class="author-chip">
                    <div class="avatar-md" style="background:${col}">${esc((post.author[0]||'?').toUpperCase())}</div>
                    <span style="font-size:13px;font-weight:600">${esc(post.author)}</span>
                    <span class="reply-time">${ago(post.created_at)}</span>
                </div>
                <button class="react-btn${voted?' voted':''}" id="tv-btn" onclick="votePostThread('${esc(id)}')">
                    ▲ <span id="tv-count">${post.votes}</span>
                </button>
            </div>
        </div>`;
    document.getElementById('replies-section').style.display = 'block';
    document.getElementById('reply-compose').style.display   = 'block';
    document.getElementById('replies-list').innerHTML = '<div style="padding:14px 0;color:var(--muted);font-size:13px">Loading replies…</div>';
    await loadReplies(id);
}

async function loadReplies(postId) {
    try {
        const { data, error } = await db.from('replies').select('*').eq('post_id',postId).order('created_at',{ascending:true});
        if (error) throw error;
        const replies = data||[];
        document.getElementById('replies-hdr').textContent =
            replies.length===0 ? 'No replies yet — be the first!' : `${replies.length} ${replies.length===1?'reply':'replies'}`;
        document.getElementById('replies-list').innerHTML = replies.length===0 ? '' : replies.map(r => {
            const col = aColor(r.author);
            const voted = votedR.has(r.id);
            return `<div class="reply-item">
                <div class="avatar-md" style="background:${col}">${esc((r.author[0]||'?').toUpperCase())}</div>
                <div class="reply-body">
                    <div class="reply-author-row">
                        <span class="reply-author">${esc(r.author)}</span>
                        <span class="reply-time">${ago(r.created_at)}</span>
                        <button class="react-btn${voted?' voted':''}" onclick="voteReply('${esc(r.id)}',this)">▲ <span id="rv-${esc(r.id)}">${r.votes}</span></button>
                    </div>
                    <div class="reply-text">${esc(r.content)}</div>
                    ${r.is_solution?'<div class="solution-badge">✓ Marked as solution</div>':''}
                </div>
            </div>`;
        }).join('');
    } catch(e) {
        document.getElementById('replies-list').innerHTML = `<p style="color:var(--red);font-size:13px;padding:12px 0">Error: ${esc(e.message)}</p>`;
    }
}

async function votePostThread(id) {
    if (votedP.has(id)) { toast('Already upvoted!','error',1800); return; }
    const post = posts.find(p=>p.id===id);
    if (post) post.votes++;
    const tc = document.getElementById('tv-count');
    if (tc) tc.textContent = post?.votes??'';
    document.getElementById('tv-btn')?.classList.add('voted');
    const lc = document.getElementById('pv-'+id);
    if (lc) { lc.textContent = post?.votes??''; lc.classList.add('hi'); }
    votedP.add(id); saveVotes();
    try {
        const { error } = await db.from('posts').update({ votes: post?.votes??1 }).eq('id',id);
        if (error) throw error;
    } catch(e) {
        votedP.delete(id); saveVotes();
        if (post) post.votes--;
        if (tc) tc.textContent = post?.votes??'';
        document.getElementById('tv-btn')?.classList.remove('voted');
        toast('Vote failed: '+e.message,'error');
    }
}

async function voteReply(id, btn) {
    if (votedR.has(id)) { toast('Already upvoted!','error',1800); return; }
    const el = document.getElementById('rv-'+id);
    let cur = parseInt(el?.textContent||'0')+1;
    if (el) el.textContent = cur;
    btn.classList.add('voted');
    votedR.add(id); saveVotes();
    try {
        const { error } = await db.from('replies').update({ votes: cur }).eq('id',id);
        if (error) throw error;
    } catch(e) {
        votedR.delete(id); saveVotes();
        if (el) el.textContent = cur-1;
        btn.classList.remove('voted');
        toast('Vote failed: '+e.message,'error');
    }
}

async function submitReply() {
    if (!activePostId) return;
    const author  = document.getElementById('r-author').value.trim();
    const content = document.getElementById('r-text').value.trim();
    if (!author)  { toast('Please add your name.','error'); return; }
    if (!content) { toast('Reply cannot be empty.','error'); return; }
    const btn = document.getElementById('reply-btn');
    btn.disabled = true; btn.textContent = 'Posting…';
    try {
        const { error } = await db.from('replies').insert({ post_id:activePostId, author, content, votes:0, is_solution:false });
        if (error) throw error;
        document.getElementById('r-text').value = '';
        document.getElementById('rc').textContent = '0';
        toast('Reply posted! ✓');
        await loadReplies(activePostId);
        await load(); // refresh reply counts
    } catch(e) {
        toast('Error: '+e.message,'error');
    } finally {
        btn.disabled = false; btn.textContent = 'Reply →';
    }
}

function closeThread() {
    document.getElementById('overlay').classList.remove('open');
    document.body.style.overflow = '';
    activePostId = null;
}

document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    if (document.getElementById('overlay').classList.contains('open')) closeThread();
    else if (document.getElementById('compose-panel').classList.contains('open')) toggleCompose();
});


// ── Lazy initialization ────────────────────────────────────────────────
// The Supabase JS library is ~50KB and only needed when the user actually
// visits the community forum. Load it on demand instead of paying that cost
// up front for every visitor to the main app.
window.__jwsync_forum_loaded__ = false;
window.jwsyncForumInit = async function () {
    if (window.__jwsync_forum_loaded__) return;
    window.__jwsync_forum_loaded__ = true;
    try {
        if (typeof supabase === 'undefined') {
            await new Promise(function (resolve, reject) {
                var s = document.createElement('script');
                s.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';
                s.onload = resolve;
                s.onerror = function () { reject(new Error('Could not load forum library')); };
                document.head.appendChild(s);
            });
        }
        createClient = supabase.createClient;
        db = createClient('https://owwsfbtbjmdskjfkxtjy.supabase.co', 'sb_publishable_KJJJAafNJR8o0tcBMYcK6g_M7IqlRsC');
        load();
    } catch (e) {
        console.error('Forum failed to initialize:', e);
        var list = document.getElementById('post-list');
        if (list) list.innerHTML = '<div style="padding:48px 16px;text-align:center;color:#7a6558;font-family:system-ui,sans-serif"><div style="font-size:32px;margin-bottom:12px">⚠️</div><div style="font-size:15px;font-weight:600;color:#e8ddd5;margin-bottom:6px">Could not load community forum</div><div style="font-size:13px">' + ((e && e.message) || 'Unknown error — check your connection') + '</div></div>';
        // Reset flag so a retry (re-entering the route) will try again
        window.__jwsync_forum_loaded__ = false;
    }
};


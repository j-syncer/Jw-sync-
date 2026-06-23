export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/api/notify' && request.method === 'POST') {
      return handleNotify(request, env);
    }
    return env.ASSETS.fetch(request);
  },
};

function esc(s) {
  return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

async function handleNotify(request, env) {
  if (!env.RESEND_API_KEY) return new Response('Not configured', { status: 500 });

  let body;
  try { body = await request.json(); } catch { return new Response('Bad request', { status: 400 }); }

  const { type, post, reply } = body;
  const OWNER = 'jacecrobinson@gmail.com';
  const FROM  = 'JW Sync <noreply@jwsync.org>';
  const FORUM = 'https://jwsync.org/beta#forum';

  let to, subject, html;

  if (type === 'new_post') {
    to      = OWNER;
    subject = `[JW Sync Forum] New post: ${post.title}`;
    html    = `<p><b>${esc(post.author)}</b> posted a new ${esc(post.category || 'post')}:</p>
<h2 style="font-size:18px;margin:8px 0">${esc(post.title)}</h2>
${post.content ? `<p style="color:#555">${esc(post.content)}</p>` : ''}
<p style="margin-top:16px"><a href="${FORUM}" style="color:#ea580c;font-weight:600">View on JW Sync Community →</a></p>`;

  } else if (type === 'new_reply') {
    if (!post?.author_email) return new Response('No email', { status: 200 });
    to      = post.author_email;
    subject = `Someone replied to your JW Sync question`;
    html    = `<p>Hi ${esc(post.author_name || 'there')},</p>
<p><b>${esc(reply.author)}</b> replied to your question "<b>${esc(post.title)}</b>":</p>
<blockquote style="border-left:3px solid #ea580c;margin:12px 0;padding:8px 16px;color:#444;font-style:normal">${esc(reply.content)}</blockquote>
<p style="margin-top:16px"><a href="${FORUM}" style="color:#ea580c;font-weight:600">View on JW Sync Community →</a></p>`;

  } else {
    return new Response('Unknown type', { status: 400 });
  }

  const res = await fetch('https://api.resend.com/emails', {
    method:  'POST',
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
    body:    JSON.stringify({ from: FROM, to: [to], subject, html }),
  });

  return new Response(null, { status: res.ok ? 200 : 500 });
}

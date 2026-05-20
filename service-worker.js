/**
 * JW Sync — Service Worker
 *
 * Strategy:
 *   - Precache the app shell on install (just index.html in this single-file build)
 *   - Network-first for HTML so users get updates when online
 *   - Stale-while-revalidate for CDN scripts (React, Tailwind, SQL.js WASM, JSZip)
 *   - Skip Supabase API calls (those are dynamic data)
 *
 * Versioning: bump CACHE_VERSION whenever you ship a new index.html.
 * Old caches are cleaned up on activate.
 */

const CACHE_VERSION = 'jwsync-v7';
const SHELL_CACHE = CACHE_VERSION + '-shell';
const RUNTIME_CACHE = CACHE_VERSION + '-runtime';

const SHELL = ['./', './index.html'];

const CDN_HOSTS = [
  'cdn.jsdelivr.net',
  'cdnjs.cloudflare.com',
  'unpkg.com',
  'fonts.googleapis.com',
  'fonts.gstatic.com',
  'sql.js.org',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(SHELL_CACHE);
      await Promise.allSettled(SHELL.map((u) => cache.add(u)));
      await self.skipWaiting();
    })(),
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys.filter((k) => !k.startsWith(CACHE_VERSION)).map((k) => caches.delete(k)),
      );
      await self.clients.claim();
    })(),
  );
});

async function networkFirst(request) {
  const cache = await caches.open(SHELL_CACHE);
  try {
    const fresh = await fetch(request);
    if (fresh && fresh.ok) cache.put(request, fresh.clone());
    return fresh;
  } catch (_e) {
    const cached = await cache.match(request);
    if (cached) return cached;
    const fallback = await cache.match('./index.html');
    if (fallback) return fallback;
    throw new Error('Offline and no cache available');
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(request);
  const networkPromise = fetch(request)
    .then((response) => {
      if (response && response.ok) cache.put(request, response.clone());
      return response;
    })
    .catch(() => cached);
  return cached || networkPromise;
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Supabase = dynamic data — never cache, never intercept
  if (url.hostname.includes('supabase.co')) return;
  // Plausible analytics — let the network handle it
  if (url.hostname.includes('plausible')) return;
  // QR code API — dynamic image, let the network handle it
  if (url.hostname.includes('qrserver.com')) return;

  const isSameOrigin = url.origin === self.location.origin;
  const isKnownCdn = CDN_HOSTS.some((h) => url.hostname.includes(h));
  if (!isSameOrigin && !isKnownCdn) return;

  if (req.mode === 'navigate' || req.destination === 'document') {
    event.respondWith(networkFirst(req));
    return;
  }
  event.respondWith(staleWhileRevalidate(req));
});

self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});

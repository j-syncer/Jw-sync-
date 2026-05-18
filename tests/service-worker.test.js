import { describe, it, expect, beforeEach, vi } from 'vitest';
import {
  loadServiceWorker,
  seedCache,
  makeFetchEvent,
  ORIGIN,
  SHELL_CACHE,
  RUNTIME_CACHE,
} from './helpers/loadServiceWorker.js';

// ── helpers ───────────────────────────────────────────────────────────────────

function okResponse() {
  const r = { ok: true };
  r.clone = () => r;
  return r;
}

function networkDownFetch() {
  return vi.fn(async () => { throw new Error('Network unavailable'); });
}

// ── Fetch routing — which requests are intercepted ────────────────────────────

describe('fetch routing', () => {
  let sw;
  beforeEach(() => { sw = loadServiceWorker(); });

  it('does not intercept Supabase requests (dynamic data)', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(
      'https://owwsfbtbjmdskjfkxtjy.supabase.co/rest/v1/posts', respondWith,
    ));
    expect(respondWith).not.toHaveBeenCalled();
  });

  it('does not intercept Plausible analytics requests', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent('https://plausible.io/api/event', respondWith));
    expect(respondWith).not.toHaveBeenCalled();
  });

  it('does not intercept QR code API requests', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent('https://api.qrserver.com/v1/create-qr-code/', respondWith));
    expect(respondWith).not.toHaveBeenCalled();
  });

  it('does not intercept unknown third-party requests', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent('https://example.com/some-api', respondWith));
    expect(respondWith).not.toHaveBeenCalled();
  });

  it('does not intercept non-GET requests', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(
      `${ORIGIN}/api/data`, respondWith, { method: 'POST' },
    ));
    expect(respondWith).not.toHaveBeenCalled();
  });

  it('intercepts same-origin document navigations', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(
      `${ORIGIN}/`, respondWith, { mode: 'navigate', destination: 'document' },
    ));
    expect(respondWith).toHaveBeenCalledOnce();
  });

  it('intercepts same-origin asset requests (non-navigate)', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(`${ORIGIN}/styles.css`, respondWith));
    expect(respondWith).toHaveBeenCalledOnce();
  });

  it('intercepts known CDN requests (cdnjs.cloudflare.com)', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(
      'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js', respondWith,
    ));
    expect(respondWith).toHaveBeenCalledOnce();
  });

  it('intercepts known CDN requests (cdn.jsdelivr.net)', () => {
    const respondWith = vi.fn();
    sw.trigger('fetch', makeFetchEvent(
      'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/main.js', respondWith,
    ));
    expect(respondWith).toHaveBeenCalledOnce();
  });

  it('uses network-first for document navigations', async () => {
    const mockFetch = vi.fn(async () => okResponse());
    const sw2 = loadServiceWorker(mockFetch);
    const respondWith = vi.fn();

    sw2.trigger('fetch', makeFetchEvent(
      `${ORIGIN}/`, respondWith, { mode: 'navigate', destination: 'document' },
    ));

    const result = await respondWith.mock.calls[0][0];
    expect(mockFetch).toHaveBeenCalledOnce();
    expect(result.ok).toBe(true);
  });

  it('uses stale-while-revalidate for CDN assets (returns cached without waiting)', async () => {
    const cdnUrl = 'https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/react.min.js';
    const cached = okResponse();
    const mockFetch = vi.fn(async () => okResponse());
    const sw2 = loadServiceWorker(mockFetch);

    // Pre-populate the runtime cache
    await seedCache(sw2.cacheStore, RUNTIME_CACHE, cdnUrl, cached);

    const respondWith = vi.fn();
    sw2.trigger('fetch', makeFetchEvent(cdnUrl, respondWith));

    const result = await respondWith.mock.calls[0][0];
    expect(result).toBe(cached);   // served from cache immediately
  });
});

// ── networkFirst strategy ─────────────────────────────────────────────────────

describe('networkFirst strategy', () => {
  it('returns fresh response and caches it when network is available', async () => {
    const fresh = okResponse();
    const mockFetch = vi.fn(async () => fresh);
    const sw = loadServiceWorker(mockFetch);

    const req = { url: `${ORIGIN}/index.html`, method: 'GET' };
    const result = await sw.sandbox.networkFirst(req);

    expect(result).toBe(fresh);
    expect(mockFetch).toHaveBeenCalledOnce();

    // Response should now be in the shell cache
    const cacheMap = sw.cacheStore.get(SHELL_CACHE);
    expect(cacheMap?.has(req.url)).toBe(true);
  });

  it('falls back to the cached response when the network is down', async () => {
    const cached = okResponse();
    const sw = loadServiceWorker(networkDownFetch());

    const req = { url: `${ORIGIN}/index.html`, method: 'GET' };
    await seedCache(sw.cacheStore, SHELL_CACHE, req.url, cached);

    const result = await sw.sandbox.networkFirst(req);
    expect(result).toBe(cached);
  });

  it('falls back to index.html when network is down and the exact URL is not cached', async () => {
    const indexFallback = okResponse();
    const sw = loadServiceWorker(networkDownFetch());

    // Only index.html is cached, not the requested URL
    await seedCache(sw.cacheStore, SHELL_CACHE, './index.html', indexFallback);

    const req = { url: `${ORIGIN}/some-page`, method: 'GET' };
    const result = await sw.sandbox.networkFirst(req);
    expect(result).toBe(indexFallback);
  });

  it('throws when network is down and there is no cache at all', async () => {
    const sw = loadServiceWorker(networkDownFetch());
    const req = { url: `${ORIGIN}/index.html`, method: 'GET' };
    await expect(sw.sandbox.networkFirst(req)).rejects.toThrow('Offline and no cache available');
  });
});

// ── staleWhileRevalidate strategy ────────────────────────────────────────────

describe('staleWhileRevalidate strategy', () => {
  it('returns the cached response immediately when a cache entry exists', async () => {
    const cached = okResponse();
    const mockFetch = vi.fn(async () => okResponse());
    const sw = loadServiceWorker(mockFetch);

    const url = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
    await seedCache(sw.cacheStore, RUNTIME_CACHE, url, cached);

    const req = { url };
    const result = await sw.sandbox.staleWhileRevalidate(req);
    expect(result).toBe(cached);
  });

  it('still triggers a background network update when serving from cache', async () => {
    const fresh = okResponse();
    const mockFetch = vi.fn(async () => fresh);
    const sw = loadServiceWorker(mockFetch);

    const url = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
    await seedCache(sw.cacheStore, RUNTIME_CACHE, url, okResponse());

    await sw.sandbox.staleWhileRevalidate({ url });

    // Allow the background fetch to settle
    await new Promise(r => setTimeout(r, 10));
    expect(mockFetch).toHaveBeenCalledOnce();
  });

  it('waits for the network when there is no cache entry', async () => {
    const fresh = okResponse();
    const mockFetch = vi.fn(async () => fresh);
    const sw = loadServiceWorker(mockFetch);

    const result = await sw.sandbox.staleWhileRevalidate({
      url: 'https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/react.min.js',
    });
    expect(result).toBe(fresh);
    expect(mockFetch).toHaveBeenCalledOnce();
  });
});

// ── activate — old cache cleanup ─────────────────────────────────────────────

describe('activate event — old cache cleanup', () => {
  it('deletes caches from previous CACHE_VERSION on activate', async () => {
    const sw = loadServiceWorker();

    // Simulate two old caches from a prior SW version
    sw.cacheStore.set('jwsync-v1-shell',   new Map());
    sw.cacheStore.set('jwsync-v2-runtime', new Map());
    // Current-version caches should be kept
    sw.cacheStore.set(SHELL_CACHE,   new Map());
    sw.cacheStore.set(RUNTIME_CACHE, new Map());

    const waitForPromises = [];
    sw.trigger('activate', { waitUntil: (p) => waitForPromises.push(p) });
    await Promise.all(waitForPromises);

    expect(sw.cacheStore.has('jwsync-v1-shell')).toBe(false);
    expect(sw.cacheStore.has('jwsync-v2-runtime')).toBe(false);
    expect(sw.cacheStore.has(SHELL_CACHE)).toBe(true);
    expect(sw.cacheStore.has(RUNTIME_CACHE)).toBe(true);
  });
});

// ── message event — SKIP_WAITING ─────────────────────────────────────────────

describe('message event', () => {
  it('calls skipWaiting when it receives the SKIP_WAITING message', async () => {
    const sw = loadServiceWorker();
    const skipSpy = vi.spyOn(sw.sandbox.self, 'skipWaiting');

    sw.trigger('message', { data: 'SKIP_WAITING' });
    await new Promise(r => setTimeout(r, 0));  // let async skipWaiting settle

    expect(skipSpy).toHaveBeenCalledOnce();
  });
});

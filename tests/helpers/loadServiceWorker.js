/**
 * Loads service-worker.js in a vm context with fully mocked SW globals
 * (self, caches, fetch).  Returns helpers for triggering event listeners
 * and inspecting cache state.
 *
 * SHELL_CACHE  = 'jwsync-v3-shell'
 * RUNTIME_CACHE = 'jwsync-v3-runtime'
 * These values are derived from CACHE_VERSION = 'jwsync-v3' in the source.
 */
import { createContext, Script } from 'node:vm';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join, dirname } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SW_PATH = join(__dirname, '../../service-worker.js');
const SW_SRC  = readFileSync(SW_PATH, 'utf8');

export const ORIGIN      = 'https://jwsync.org';
export const SHELL_CACHE   = 'jwsync-v3-shell';
export const RUNTIME_CACHE = 'jwsync-v3-runtime';

/**
 * @param {Function} [fetchImpl] - Optional fetch mock. Defaults to a fn that
 *   resolves with `{ ok: true, clone: () => res }`.
 * @returns {{ trigger, listeners, sandbox, cacheStore }}
 */
export function loadServiceWorker(fetchImpl) {
  const listeners = {};

  // --- in-memory caches mock -------------------------------------------
  // cacheStore: Map<cacheName, Map<url-string, response>>
  const cacheStore = new Map();

  function makeCacheObj(store) {
    return {
      async add()       {},   // no-op (install precache)
      async put(req, res) { store.set(urlKey(req), res); },
      async match(req)    { return store.get(urlKey(req)) ?? null; },
    };
  }

  const mockCaches = {
    async open(name) {
      if (!cacheStore.has(name)) cacheStore.set(name, new Map());
      return makeCacheObj(cacheStore.get(name));
    },
    async keys()       { return [...cacheStore.keys()]; },
    async delete(name) { cacheStore.delete(name); return true; },
  };

  function urlKey(req) {
    return typeof req === 'string' ? req : req.url;
  }

  // --- self mock --------------------------------------------------------
  const selfObj = {
    addEventListener(type, fn) { listeners[type] = fn; },
    skipWaiting: async () => {},
    clients: { claim: async () => {} },
    location: { origin: ORIGIN },
  };

  // --- default fetch (network-ok) ---------------------------------------
  const defaultFetch = async (req) => {
    const res = { ok: true };
    res.clone = () => res;
    return res;
  };

  const sandbox = {};
  sandbox.self   = selfObj;
  sandbox.caches = mockCaches;
  sandbox.fetch  = fetchImpl ?? defaultFetch;
  sandbox.URL    = URL;     // Node.js built-in — needed for new URL(req.url)
  sandbox.console = console;

  createContext(sandbox);
  new Script(SW_SRC).runInContext(sandbox);

  return {
    /** Fire a registered event listener by name. */
    trigger(type, event) {
      if (!listeners[type]) throw new Error(`No '${type}' listener registered`);
      return listeners[type](event);
    },
    listeners,
    sandbox,   // gives access to networkFirst / staleWhileRevalidate
    cacheStore,
  };
}

/** Pre-populate a named cache with a response. */
export async function seedCache(cacheStore, cacheName, url, response) {
  if (!cacheStore.has(cacheName)) cacheStore.set(cacheName, new Map());
  cacheStore.get(cacheName).set(url, response);
}

/** Build a minimal fetch-event mock. respondWith is a vi.fn() you pass in. */
export function makeFetchEvent(url, respondWith, { method = 'GET', mode = 'no-cors', destination = '' } = {}) {
  return {
    request: { url, method, mode, destination },
    respondWith,
  };
}

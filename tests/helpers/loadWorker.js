/**
 * Loads beta/js/merge-worker.js into a Node.js vm context, providing the
 * browser/worker globals (importScripts, self, initSqlJs, JSZip, crypto) it
 * expects.  Returns a `send(data)` function that drives the worker and
 * collects its postMessage output.
 */
import { createContext, Script } from 'node:vm';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join, dirname } from 'node:path';
import { createRequire } from 'node:module';
import { getSQL } from './createBackup.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const WORKER_PATH = join(__dirname, '../../beta/js/merge-worker.js');

const _require = createRequire(import.meta.url);
const JSZip = _require('jszip');

let _sandbox = null;
let _messages = null;

/**
 * Returns a lazily-created, shared worker sandbox.
 * The sandbox is re-used across tests; state is safe because:
 *   - `cancelled` is reset to false at the top of every merge
 *   - the in-memory SQLite database is created fresh per merge
 */
async function getSandbox() {
  if (_sandbox) return { sandbox: _sandbox, messages: _messages };

  const SQL = await getSQL();    // pre-initialised sql.js (WASM compiled once)
  _messages = [];

  const selfObj = {
    postMessage(msg, _transfer) { _messages.push(msg); },
    onmessage: null,
  };

  const sandbox = {
    self: selfObj,
    importScripts: () => {},           // no-op: sql.js and JSZip provided below
    initSqlJs: async () => SQL,        // ignore locateFile; return cached instance
    JSZip,
    crypto: globalThis.crypto,         // Node.js 19+ web-crypto
    console,
    setTimeout,
    clearTimeout,
  };

  createContext(sandbox);
  new Script(readFileSync(WORKER_PATH, 'utf8')).runInContext(sandbox);

  _sandbox = sandbox;
  return { sandbox, messages: _messages };
}

/**
 * Send a message to the worker and await completion.
 * Returns only the messages produced by this call.
 *
 * @param {object} data - the message payload (type, mainBuffer, secondaryFiles, opts, …)
 * @returns {Promise<object[]>} messages posted by the worker during this merge
 */
export async function send(data) {
  const { sandbox, messages } = await getSandbox();
  const before = messages.length;
  await sandbox.self.onmessage({ data });
  return messages.slice(before);
}

/**
 * Access a top-level function declared (not const) in the worker script.
 * Only `function` declarations become properties of the vm sandbox global.
 */
export async function getWorkerFn(name) {
  const { sandbox } = await getSandbox();
  return sandbox[name];
}

/** Default opts that enable all merge features. */
export const ALL_ON = {
  mergeNotes: true,
  mergeHighlights: true,
  mergeBookmarks: true,
  mergeTags: true,
  smartDedupe: false,
  syncByDate: false,
  filterDate: null,
  conflictStrategy: 'keep',
  importTag: '',
  deepClean: false,
};

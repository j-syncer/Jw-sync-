/**
 * Loads beta/js/forum.js in a minimal vm context and extracts the pure
 * utility functions (ago, aColor, esc, catLabel, catCls).
 *
 * forum.js defines its utilities as `const` arrow functions, so they are
 * NOT properties of the vm sandbox global.  We patch the source by
 * appending one line that writes them onto `window` (which is the sandbox),
 * making them accessible after execution.
 */
import { createContext, Script } from 'node:vm';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join, dirname } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const FORUM_PATH = join(__dirname, '../../beta/js/forum.js');

let _cached = null;

export function loadForumUtils() {
  if (_cached) return _cached;

  const src = readFileSync(FORUM_PATH, 'utf8');

  // Append an export shim — writes const-scoped functions onto window (the sandbox)
  const patched = src + '\nwindow._jwutils = { ago: ago, aColor: aColor, esc: esc, catLabel: catLabel, catCls: catCls };';

  const lsData = new Map();
  const mockLocalStorage = {
    getItem:    (k) => lsData.get(k) ?? null,
    setItem:    (k, v) => lsData.set(k, String(v)),
    removeItem: (k) => lsData.delete(k),
  };

  const mockDocument = {
    addEventListener:  () => {},
    getElementById:    () => null,
    querySelectorAll:  () => ({ forEach: () => {} }),
    createElement:     () => ({ textContent: '', className: '', style: {} }),
    body:              { appendChild: () => {}, contains: () => false, style: {}, classList: { toggle: () => {} } },
    head:              { appendChild: () => {} },
  };

  const sandbox = {};
  sandbox.window    = sandbox;
  sandbox.self      = sandbox;     // needed for the injected export shim
  sandbox.localStorage = mockLocalStorage;
  sandbox.document  = mockDocument;
  sandbox.console   = console;
  sandbox.setTimeout    = setTimeout;
  sandbox.clearTimeout  = clearTimeout;

  createContext(sandbox);
  new Script(patched).runInContext(sandbox);

  _cached = sandbox._jwutils;
  return _cached;
}

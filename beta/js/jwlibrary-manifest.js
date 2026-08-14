/* ─────────────────────────────────────────────────────────────────────────────
   JW Sync — js/jwlibrary-manifest.js
   Write a .jwlibrary that JW Library will actually restore.

   A .jwlibrary is a ZIP holding userData.db plus a manifest.json that describes
   it — including userDataBackup.hash, the SHA-256 of the database file. If the
   manifest is missing, or its hash no longer matches the database beside it,
   JW Library refuses the file. It refuses *silently*: the app flickers and
   returns to the same screen, with no error and no confirmation prompt. So a
   backup that is one stale field away from valid is indistinguishable, to the
   person holding it, from a corrupt one.

   That is what happened to the Study Explorer and the Library Doctor. The
   Explorer re-zipped the edited database on its own and shipped it with no
   manifest at all; the Doctor kept the original manifest but left its hash
   pointing at the database the file used to contain. Merged files worked, which
   made it look like a Doctor/Explorer bug rather than one rule nobody had
   written down.

   Every path that writes a backup now goes through finalizeBackup() so there is
   one place that knows the rule.

   Declares: window.__jwFinalizeBackup / self.__jwFinalizeBackup (+ .sha256Hex,
   .touchLastModified for tests)
   ───────────────────────────────────────────────────────────────────────── */
(function (root) {
  'use strict';

  // ── SHA-256 ───────────────────────────────────────────────────────────────
  // crypto.subtle is the fast path and what actually runs on jwsync.org. The
  // fallback exists because a wrong hash is a silent restore failure, so
  // "hashing was unavailable" must not become "ship it anyway and hope".
  var K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2];

  function sha256Js(bytes) {
    var h = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
             0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
    var len = bytes.length;
    var withPad = new Uint8Array((((len + 8) >> 6) + 1) * 64);
    withPad.set(bytes);
    withPad[len] = 0x80;
    // Length in bits as a 64-bit big-endian value. Backups run to tens of MB,
    // far inside 2^32 bits, so the high word only carries the top 3 bits.
    var bitsHi = Math.floor(len / 536870912);
    var bitsLo = (len << 3) >>> 0;
    var end = withPad.length;
    withPad[end - 8] = (bitsHi >>> 24) & 0xff; withPad[end - 7] = (bitsHi >>> 16) & 0xff;
    withPad[end - 6] = (bitsHi >>> 8) & 0xff;  withPad[end - 5] = bitsHi & 0xff;
    withPad[end - 4] = (bitsLo >>> 24) & 0xff; withPad[end - 3] = (bitsLo >>> 16) & 0xff;
    withPad[end - 2] = (bitsLo >>> 8) & 0xff;  withPad[end - 1] = bitsLo & 0xff;

    var w = new Int32Array(64);
    for (var i = 0; i < withPad.length; i += 64) {
      var j;
      for (j = 0; j < 16; j++) {
        w[j] = (withPad[i + j * 4] << 24) | (withPad[i + j * 4 + 1] << 16) |
               (withPad[i + j * 4 + 2] << 8) | withPad[i + j * 4 + 3];
      }
      for (j = 16; j < 64; j++) {
        var g0 = w[j - 15], g1 = w[j - 2];
        var s0 = ((g0 >>> 7) | (g0 << 25)) ^ ((g0 >>> 18) | (g0 << 14)) ^ (g0 >>> 3);
        var s1 = ((g1 >>> 17) | (g1 << 15)) ^ ((g1 >>> 19) | (g1 << 13)) ^ (g1 >>> 10);
        w[j] = (w[j - 16] + s0 + w[j - 7] + s1) | 0;
      }
      var a = h[0], b = h[1], c = h[2], d = h[3], e = h[4], f = h[5], g = h[6], hh = h[7];
      for (j = 0; j < 64; j++) {
        var S1 = ((e >>> 6) | (e << 26)) ^ ((e >>> 11) | (e << 21)) ^ ((e >>> 25) | (e << 7));
        var ch = (e & f) ^ (~e & g);
        var t1 = (hh + S1 + ch + K[j] + w[j]) | 0;
        var S0 = ((a >>> 2) | (a << 30)) ^ ((a >>> 13) | (a << 19)) ^ ((a >>> 22) | (a << 10));
        var maj = (a & b) ^ (a & c) ^ (b & c);
        var t2 = (S0 + maj) | 0;
        hh = g; g = f; f = e; e = (d + t1) | 0; d = c; c = b; b = a; a = (t1 + t2) | 0;
      }
      h[0] = (h[0] + a) | 0; h[1] = (h[1] + b) | 0; h[2] = (h[2] + c) | 0; h[3] = (h[3] + d) | 0;
      h[4] = (h[4] + e) | 0; h[5] = (h[5] + f) | 0; h[6] = (h[6] + g) | 0; h[7] = (h[7] + hh) | 0;
    }
    var out = '';
    for (var k = 0; k < 8; k++) out += ((h[k] >>> 0).toString(16)).padStart(8, '0');
    return out;
  }

  function toHex(buf) {
    var v = new Uint8Array(buf), s = '';
    for (var i = 0; i < v.length; i++) s += v[i].toString(16).padStart(2, '0');
    return s;
  }

  function sha256Hex(bytes) {
    var u8 = (bytes instanceof Uint8Array) ? bytes : new Uint8Array(bytes);
    try {
      if (root.crypto && root.crypto.subtle && root.crypto.subtle.digest) {
        // digest() wants its own buffer, not a view into a larger one.
        var copy = u8.slice();
        return Promise.resolve(root.crypto.subtle.digest('SHA-256', copy.buffer))
          .then(toHex)
          .catch(function () { return sha256Js(u8); });
      }
    } catch (e) { /* fall through */ }
    return Promise.resolve(sha256Js(u8));
  }

  // ── the backup itself ─────────────────────────────────────────────────────
  function stamp() {
    // The format JW Library's own backups use: no milliseconds.
    return new Date().toISOString().replace(/\.\d+Z$/, 'Z');
  }

  // A single-row table recording when the library last changed. JW Library
  // writes it on every backup, so a file we have edited should say so too.
  function touchLastModified(db, iso) {
    try {
      var t = db.exec("SELECT name FROM sqlite_master WHERE type='table' AND name='LastModified'");
      if (!t.length || !t[0].values.length) return false;
      var info = db.exec('PRAGMA table_info(LastModified)');
      if (!info.length || !info[0].values.length) return false;
      var col = info[0].values[0][1];
      db.run('DELETE FROM LastModified');
      db.run('INSERT INTO LastModified ("' + col + '") VALUES (?)', [iso || stamp()]);
      return true;
    } catch (e) { return false; }
  }

  /**
   * Put dbBytes into the zip and bring manifest.json back in step with it.
   * Only the fields that have actually gone stale are touched: an existing
   * manifest keeps everything else it came with, because the parts we do not
   * understand are exactly the parts we must not rewrite.
   *
   * @returns Promise<zip>
   */
  function finalizeBackup(zip, dbKey, dbBytes, opts) {
    opts = opts || {};
    var key = dbKey || 'userData.db';
    var iso = stamp();
    zip.file(key, dbBytes);
    var mf = zip.file('manifest.json');
    var read = mf ? mf.async('string') : Promise.resolve(null);
    return read.then(function (text) {
      return sha256Hex(dbBytes).then(function (hash) {
        var m = null;
        if (text) { try { m = JSON.parse(text); } catch (e) { m = null; } }
        if (!m || typeof m !== 'object') m = {};
        if (m.name == null) m.name = opts.name || 'JW Sync backup';
        else if (opts.nameSuffix && String(m.name).indexOf(opts.nameSuffix) < 0) m.name = m.name + opts.nameSuffix;
        if (m.creationDate == null) m.creationDate = iso;
        if (m.version == null) m.version = 1;
        var ud = m.userDataBackup;
        if (!ud || typeof ud !== 'object') ud = m.userDataBackup = {};
        ud.hash = hash;
        ud.lastModifiedDate = iso;
        if (ud.databaseName == null) ud.databaseName = key.split('/').pop();
        if (ud.deviceName == null) ud.deviceName = 'JW Sync';
        // schemaVersion is deliberately not invented when it is absent: a wrong
        // version is another silently-refused file, and only the backup that
        // came out of JW Library knows the right one.
        zip.file('manifest.json', JSON.stringify(m, null, 2));
        return zip;
      });
    });
  }

  root.__jwFinalizeBackup = finalizeBackup;
  root.__jwFinalizeBackup.sha256Hex = sha256Hex;
  root.__jwFinalizeBackup.touchLastModified = touchLastModified;
  root.__jwFinalizeBackup.stamp = stamp;
}(typeof self !== 'undefined' ? self : this));

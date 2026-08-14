/* merge-worker.js
   Off-thread merge pipeline for JW Sync.

   Protocol
   --------
   IN  { type: 'merge', mainBuffer, mainName, secondaryFiles: [{buffer, name}],
         opts, tagManager, colorRules }
       Buffers are Transferred (zero-copy) from the main thread.

   IN  { type: 'cancel' }
       Main thread requests graceful stop; worker throws on next yield.

   OUT { type: 'log',      text, isError }
   OUT { type: 'progress', payload: {current, total, eta, label} | null }
   OUT { type: 'done',     zipBuffer, stats, previewNotes }
       zipBuffer is Transferred back (zero-copy).
   OUT { type: 'error',    message }
*/

importScripts(
  'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'
);
// Same rules as every other path that writes a .jwlibrary; resolved against
// this worker's own URL, so it loads from js/ on both sites.
importScripts('jwlibrary-manifest.js');

let cancelled = false;
let confirmResolver = null;

const stripHTML = d => String(d || '').replace(/<[^>]*>?/gm, '').trim().toLowerCase();
const safeText  = d => String(d || '').replace(/<[^>]*>?/gm, '').trim();
const A = () => new Promise(r => setTimeout(r, 0));

function log(text, isError) {
  self.postMessage({ type: 'log', text, isError: !!isError });
}
function prog(payload) {
  self.postMessage({ type: 'progress', payload });
}

async function sha1Buf(buf) {
  try {
    const digest = await crypto.subtle.digest('SHA-1', buf);
    return Array.from(new Uint8Array(digest)).map(b => b.toString(16).padStart(2, '0')).join('');
  } catch { return null; }
}

function mapTagName(name, tagManager) {
  const t = tagManager[name];
  if (!t || t.action === 'keep') return name;
  if (t.action === 'merge') return t.targetName;
  return (t.action === 'rename' && t.customName.trim()) || name;
}

function taggedError(code, message) {
  const err = new Error(message);
  err.code = code;
  return err;
}

function classifyError(e) {
  const m = ((e && e.message) || '').toLowerCase();
  if (m.includes('memory') || m.includes('allocation') || e instanceof RangeError) return 'oversize';
  if (m.includes('zip') || m.includes('end of central') || m.includes('corrupt')) return 'corrupt';
  if (m.includes('sqlite') || m.includes('database') || m.includes('file is not a database')) return 'not_sqlite';
  return '';
}

// ═══ Library Doctor (opt-in via opts.doctorCheck) ═══════════════════════════
// Headless version of the Library Doctor's health checks, run on the fully
// merged database while the pre-merge impact preview is on screen. Results
// ride along with the {type:'impact'} message; fixes are applied only after
// the user confirms. Keep these queries in sync with the Doctor module in
// beta/index.html (dupNotePairs / idsFor / applyFixes).
const DOCTOR_CHECKS = ['dup_notes', 'empty_notes', 'dup_marks', 'orph_br', 'orph_tm', 'unused_tags', 'unused_loc'];

function dCol(db, sql) { const r = db.exec(sql); return r[0] ? r[0].values.map(v => v[0]) : []; }
function dHasTable(db, n) { return dCol(db, "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='" + n + "'")[0] > 0; }
function dHasCol(db, tbl, cname) {
  try {
    const r = db.exec('PRAGMA table_info(' + tbl + ')');
    if (!r[0]) return false;
    const i = r[0].columns.indexOf('name');
    return r[0].values.some(v => v[i] === cname);
  } catch { return false; }
}

// Two notes are duplicates only when BOTH the text AND the anchor match:
// same Title, Content, Location, BlockType and BlockIdentifier. Identical
// text on a different verse/paragraph of the same chapter is NOT a
// duplicate. The kept copy prefers the one linked to a highlight.
function dDupNotePairs(db) {
  if (!dHasTable(db, 'Note')) return [];
  const bt  = dHasCol(db, 'Note', 'BlockType') ? 'IFNULL(BlockType,-1)' : '-1';
  const bi  = dHasCol(db, 'Note', 'BlockIdentifier') ? 'IFNULL(BlockIdentifier,-1)' : '-1';
  const btN = dHasCol(db, 'Note', 'BlockType') ? 'IFNULL(n.BlockType,-1)' : '-1';
  const biN = dHasCol(db, 'Note', 'BlockIdentifier') ? 'IFNULL(n.BlockIdentifier,-1)' : '-1';
  const keep = dHasCol(db, 'Note', 'UserMarkId')
    ? 'COALESCE(MIN(CASE WHEN UserMarkId IS NOT NULL THEN NoteId END),MIN(NoteId))'
    : 'MIN(NoteId)';
  const r = db.exec(
    "SELECT n.NoteId AS dup, g.keepId AS keep FROM Note n JOIN (" +
    " SELECT IFNULL(Title,'') AS t, IFNULL(Content,'') AS c, IFNULL(LocationId,-1) AS l, " + bt + " AS bt, " + bi + " AS bi, " + keep + " AS keepId" +
    " FROM Note WHERE (TRIM(IFNULL(Title,''))<>'' OR TRIM(IFNULL(Content,''))<>'')" +
    " GROUP BY t, c, l, bt, bi HAVING COUNT(*)>1) g" +
    " ON IFNULL(n.Title,'')=g.t AND IFNULL(n.Content,'')=g.c AND IFNULL(n.LocationId,-1)=g.l AND " + btN + "=g.bt AND " + biN + "=g.bi" +
    " WHERE n.NoteId<>g.keepId");
  return r[0] ? r[0].values.map(v => ({ dup: v[0], keep: v[1] })) : [];
}

function dIdsFor(db, key) {
  switch (key) {
    case 'dup_notes':
      return dDupNotePairs(db).map(p => p.dup);
    case 'empty_notes':
      if (!dHasTable(db, 'Note')) return [];
      return dCol(db, "SELECT NoteId FROM Note WHERE TRIM(IFNULL(Title,''))='' AND TRIM(IFNULL(Content,''))=''");
    case 'dup_marks':
      if (!dHasTable(db, 'UserMark') || !dHasTable(db, 'BlockRange')) return [];
      return dCol(db,
        "SELECT DISTINCT um2.UserMarkId FROM UserMark um1" +
        " JOIN UserMark um2 ON um2.UserMarkId>um1.UserMarkId" +
        "  AND IFNULL(um2.LocationId,-1)=IFNULL(um1.LocationId,-1)" +
        "  AND IFNULL(um2.ColorIndex,-1)=IFNULL(um1.ColorIndex,-1)" +
        " JOIN BlockRange b1 ON b1.UserMarkId=um1.UserMarkId" +
        " JOIN BlockRange b2 ON b2.UserMarkId=um2.UserMarkId" +
        "  AND IFNULL(b2.BlockType,-1)=IFNULL(b1.BlockType,-1)" +
        "  AND IFNULL(b2.Identifier,-1)=IFNULL(b1.Identifier,-1)" +
        "  AND IFNULL(b2.StartToken,-1)=IFNULL(b1.StartToken,-1)" +
        "  AND IFNULL(b2.EndToken,-1)=IFNULL(b1.EndToken,-1)" +
        " WHERE (SELECT COUNT(*) FROM BlockRange WHERE UserMarkId=um1.UserMarkId)=1" +
        "  AND (SELECT COUNT(*) FROM BlockRange WHERE UserMarkId=um2.UserMarkId)=1" +
        "  AND um2.UserMarkId NOT IN (SELECT IFNULL(UserMarkId,-1) FROM Note)");
    case 'orph_br':
      if (!dHasTable(db, 'BlockRange') || !dHasTable(db, 'UserMark')) return [];
      return dCol(db, "SELECT BlockRangeId FROM BlockRange WHERE UserMarkId NOT IN (SELECT UserMarkId FROM UserMark)");
    case 'orph_tm':
      if (!dHasTable(db, 'TagMap') || !dHasTable(db, 'Note')) return [];
      return dCol(db, "SELECT TagMapId FROM TagMap WHERE NoteId IS NOT NULL AND NoteId NOT IN (SELECT NoteId FROM Note)");
    case 'unused_tags': {
      if (!dHasTable(db, 'Tag')) return [];
      const typeFilter = dHasCol(db, 'Tag', 'Type') ? "IFNULL(Type,1)=1 AND " : "";
      const tmRef = dHasTable(db, 'TagMap') ? " AND TagId NOT IN (SELECT DISTINCT TagId FROM TagMap WHERE TagId IS NOT NULL)" : "";
      return dCol(db, "SELECT TagId FROM Tag WHERE " + typeFilter + "1=1" + tmRef);
    }
    case 'unused_loc': {
      if (!dHasTable(db, 'Location')) return [];
      const refs = [];
      [['Note', 'LocationId'], ['UserMark', 'LocationId'], ['Bookmark', 'LocationId'], ['Bookmark', 'PublicationLocationId'],
       ['TagMap', 'LocationId'], ['InputField', 'LocationId'], ['PlaylistItemLocationMap', 'LocationId'], ['PlaylistMedia', 'LocationId']
      ].forEach(tc => { if (dHasTable(db, tc[0]) && dHasCol(db, tc[0], tc[1])) refs.push('SELECT ' + tc[1] + ' FROM ' + tc[0] + ' WHERE ' + tc[1] + ' IS NOT NULL'); });
      if (!refs.length) return [];
      return dCol(db, 'SELECT LocationId FROM Location WHERE LocationId NOT IN (' + refs.join(' UNION ') + ')');
    }
    default: return [];
  }
}

function doctorScan(db) {
  const checks = {};
  let issues = 0;
  DOCTOR_CHECKS.forEach(k => {
    let n = 0;
    try { n = dIdsFor(db, k).length; } catch { n = 0; }
    checks[k] = n; issues += n;
  });
  return { checks, issues };
}

function doctorFix(db) {
  let fixed = 0;
  const pairs = dDupNotePairs(db);
  if (dHasTable(db, 'TagMap')) pairs.forEach(p => {
    // keep tag assignments: move the removed copy's tags onto the kept copy
    db.run('UPDATE TagMap SET NoteId=' + p.keep + ' WHERE NoteId=' + p.dup +
           ' AND TagId IS NOT NULL AND TagId NOT IN (SELECT TagId FROM TagMap WHERE NoteId=' + p.keep + ' AND TagId IS NOT NULL)');
  });
  const delNotes = ids => {
    if (!ids.length) return;
    if (dHasTable(db, 'TagMap')) db.run('DELETE FROM TagMap WHERE NoteId IN (' + ids.join(',') + ')');
    db.run('DELETE FROM Note WHERE NoteId IN (' + ids.join(',') + ')');
    fixed += ids.length;
  };
  delNotes(pairs.map(p => p.dup));
  delNotes(dIdsFor(db, 'empty_notes'));
  const dm = dIdsFor(db, 'dup_marks');
  if (dm.length) {
    if (dHasTable(db, 'BlockRange')) db.run('DELETE FROM BlockRange WHERE UserMarkId IN (' + dm.join(',') + ')');
    db.run('DELETE FROM UserMark WHERE UserMarkId IN (' + dm.join(',') + ')');
    fixed += dm.length;
  }
  const ob = dIdsFor(db, 'orph_br');
  if (ob.length) { db.run('DELETE FROM BlockRange WHERE BlockRangeId IN (' + ob.join(',') + ')'); fixed += ob.length; }
  const ot = dIdsFor(db, 'orph_tm');
  if (ot.length) { db.run('DELETE FROM TagMap WHERE TagMapId IN (' + ot.join(',') + ')'); fixed += ot.length; }
  const ut = dIdsFor(db, 'unused_tags');
  if (ut.length) { db.run('DELETE FROM Tag WHERE TagId IN (' + ut.join(',') + ')'); fixed += ut.length; }
  const ul = dIdsFor(db, 'unused_loc');
  if (ul.length) { db.run('DELETE FROM Location WHERE LocationId IN (' + ul.join(',') + ')'); fixed += ul.length; }
  try { db.run('VACUUM'); } catch {}
  return fixed;
}
// ═══ end Library Doctor ═════════════════════════════════════════════════════

self.onmessage = async ({ data }) => {
  if (data.type === 'cancel') { cancelled = true; if (confirmResolver) { confirmResolver(false); confirmResolver = null; } return; }
  if (data.type === 'confirmMerge') { if (confirmResolver) { confirmResolver(true); confirmResolver = null; } return; }
  if (data.type !== 'merge') return;
  cancelled = false;
  try {
    const result = await runMerge(data);
    if (result.cancelled) {
      self.postMessage({ type: 'cancelled' });
      return;
    }
    self.postMessage(
      { type: 'done', zipBuffer: result.zipBuffer, stats: result.stats, previewNotes: result.previewNotes, timings: result.timings },
      [result.zipBuffer]
    );
  } catch (e) {
    self.postMessage({ type: 'error', code: e.code || classifyError(e), message: e.message });
  }
};

async function runMerge({ mainBuffer, secondaryFiles, opts, tagManager, colorRules }) {
  const SQL = await initSqlJs({
    locateFile: f => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${f}`
  });

  const p   = opts;
  const _now = () => (self.performance && performance.now) ? performance.now() : Date.now();
  const _t0 = _now(); let _tm = _t0; const timings = {};
  const ne  = tagManager;
  const Le  = colorRules || [];
  const ma  = name => mapTagName(name, ne);

  // ── Step 1: Open main ZIP ───────────────────────────────────────────────
  log('Step 1: Unzipping main backup...');
  await A();

  let o;
  try { o = await new JSZip().loadAsync(mainBuffer); }
  catch (e) { throw taggedError('corrupt', "This file isn't a readable .jwlibrary backup."); }
  const manifestFile = o.file('manifest.json');
  if (manifestFile) {
    try {
      const raw = JSON.parse(await manifestFile.async('string'));
      raw.creationDate = new Date().toISOString();
      raw.name = (raw.name || 'Backup') + (secondaryFiles.length > 0 ? ' (Merged)' : ' (Updated)');
      o.file('manifest.json', JSON.stringify(raw, null, 2));
    } catch {}
  }

  const dbKey  = Object.keys(o.files).find(k => /userdata\.db$/i.test(k));
  if (!dbKey) throw taggedError('no_db', 'This .jwlibrary backup is missing its notes database (userData.db).');
  const dbBytes = await o.files[dbKey].async('uint8array');

  // ── Step 2: Open base database ──────────────────────────────────────────
  log('Step 2: Preparing database framework...');
  await A();

  let a;
  try { a = new SQL.Database(dbBytes); }
  catch (e) { throw taggedError('not_sqlite', "The backup's database couldn't be opened."); }
  a.run('PRAGMA foreign_keys = OFF;');
  timings.prepare = _now() - _tm; _tm = _now();

  const f = { Note: 0, UserMark: 0, Bookmark: 0, Tag: 0, Deduplicated: 0,
              Updated: 0, Errors: 0, Cleaned: 0, ColorsMapped: 0, InputFields: 0 };

  // ── Bulk Color Changer ──────────────────────────────────────────────────
  if (Le.length > 0) {
    log('Applying Bulk Color Changer rules...');
    await A();
    a.run('BEGIN TRANSACTION;');
    try {
      Le.forEach(k => {
        const from = parseInt(k.from), to = parseInt(k.to);
        if (from !== to && from >= 1 && from <= 6 && to >= 1 && to <= 6) {
          a.run('UPDATE UserMark SET ColorIndex = ?, Version = Version + 1 WHERE ColorIndex = ?', [to, from]);
          f.ColorsMapped++;
        }
      });
      a.run('COMMIT;');
    } catch { a.run('ROLLBACK;'); }
  }

  // ── Tag Manager ─────────────────────────────────────────────────────────
  if (p.mergeTags && Object.keys(ne).length > 0) {
    log('Applying Tag Manager updates...');
    await A();
    a.run('BEGIN TRANSACTION;');
    try {
      for (const [name, spec] of Object.entries(ne)) {
        const mapped = ma(name);
        if (spec.checked) {
          if (mapped !== name) {
            const dest = a.exec('SELECT TagId FROM Tag WHERE Name = ?', [mapped]);
            const src  = a.exec('SELECT TagId FROM Tag WHERE Name = ?', [name]);
            if (src.length > 0 && src[0].values) {
              const srcId = src[0].values[0][0];
              if (dest.length > 0 && dest[0].values) {
                const dstId = dest[0].values[0][0];
                a.run('UPDATE OR IGNORE TagMap SET TagId = ? WHERE TagId = ?', [dstId, srcId]);
                a.run('DELETE FROM TagMap WHERE TagId = ?', [srcId]);
                a.run('DELETE FROM Tag WHERE TagId = ?', [srcId]);
              } else {
                a.run('UPDATE Tag SET Name = ? WHERE TagId = ?', [mapped, srcId]);
              }
              f.Updated++;
            }
          }
        } else {
          const row = a.exec('SELECT TagId FROM Tag WHERE Name = ?', [name]);
          if (row.length > 0 && row[0].values) {
            const id = row[0].values[0][0];
            a.run('DELETE FROM TagMap WHERE TagId = ?', [id]);
            a.run('DELETE FROM Tag WHERE TagId = ?', [id]);
            f.Updated++;
          }
        }
      }
      a.run('COMMIT;');
    } catch { a.run('ROLLBACK;'); }
  }

  // ── Import tag ──────────────────────────────────────────────────────────
  let importTagId = null;
  if (p.importTag && p.importTag.trim() !== '' && secondaryFiles.length > 0) {
    const tagName = p.importTag.trim();
    a.run('INSERT OR IGNORE INTO Tag (Name) VALUES (?)', [tagName]);
    const row = a.exec('SELECT TagId FROM Tag WHERE Name = ?', [tagName]);
    if (row.length > 0 && row[0].values) importTagId = row[0].values[0][0];
  }

  const previewNotes = [];

  // ── Step 3: Merge secondary files ──────────────────────────────────────
  if (secondaryFiles.length > 0) {
    log(`Step 3: Beginning import of ${secondaryFiles.length} file(s)...`);
    await A();

    const dateFilter = (p.syncByDate && p.filterDate)
      ? new Date(p.filterDate).getTime() - 1440 * 60 * 1000
      : 0;

    const dedupeSet = p.smartDedupe
      ? (() => {
          try {
            const r = a.exec('SELECT Content FROM Note');
            return r.length > 0 && r[0].values
              ? new Set(r[0].values.map(v => stripHTML(v[0])))
              : new Set();
          } catch { return new Set(); }
        })()
      : new Set();

    // Prepared-statement cache (freed after all files are processed)
    const stmtCache = new Map();
    const getStmt = (tbl, cols) => {
      const key = `${tbl}|${cols.join(',')}`;
      let s = stmtCache.get(key);
      if (!s) {
        const sql = `INSERT OR IGNORE INTO "${tbl}" (${cols.map(c => `"${c}"`).join(',')}) VALUES (${cols.map(() => '?').join(',')})`;
        s = a.prepare(sql);
        stmtCache.set(key, s);
      }
      return s;
    };
    const insertRow = (tbl, cols, vals) => {
      try {
        if (getStmt(tbl, cols).run(vals), !a.getRowsModified()) return 0;
        const r = a.exec('SELECT last_insert_rowid()');
        return r && r[0] && r[0].values[0][0] ? r[0].values[0][0] : 0;
      } catch { return 0; }
    };
    const freeStmts = () => { stmtCache.forEach(s => { try { s.free(); } catch {} }); stmtCache.clear(); };

    // Hash the main file for dedup
    const seenHashes = new Set();
    try { const h = await sha1Buf(mainBuffer); if (h) seenHashes.add(h); } catch {}

    // Pre-count rows across all secondary files for progress ETA
    let totalRows = 0, processedRows = 0;
    const startTime = Date.now();
    try {
      for (const sf of secondaryFiles) {
        try {
          const zip = await new JSZip().loadAsync(sf.buffer);
          const key = Object.keys(zip.files).find(k => /userdata\.db$/i.test(k));
          if (!key) continue;
          const bytes = await zip.files[key].async('uint8array');
          const tmp = new SQL.Database(bytes);
          try {
            for (const tbl of ['Location','Tag','UserMark','BlockRange','Note','TagMap','Bookmark','InputField']) {
              try { const r = tmp.exec(`SELECT COUNT(*) FROM "${tbl}"`); r[0] && (totalRows += r[0].values[0][0]); } catch {}
            }
          } finally { try { tmp.close(); } catch {} }
        } catch {}
      }
      prog({ current: 0, total: totalRows, eta: null, label: 'Starting…' });
    } catch {}

    const TABLES = [
      { name: 'Location',   idCol: 'LocationId',   fkCols: [],                                                                                                                        condition: true },
      { name: 'Tag',        idCol: 'TagId',         fkCols: [],                                                                                                                        condition: p.mergeTags },
      { name: 'UserMark',   idCol: 'UserMarkId',    fkCols: [{ name: 'LocationId',          map: 'Location' }],                                                                        condition: p.mergeHighlights },
      { name: 'BlockRange', idCol: 'BlockRangeId',  fkCols: [{ name: 'UserMarkId',           map: 'UserMark' }],                                                                        condition: p.mergeHighlights },
      { name: 'Note',       idCol: 'NoteId',        fkCols: [{ name: 'LocationId',          map: 'Location' }, { name: 'UserMarkId', map: 'UserMark' }],                               condition: p.mergeNotes },
      { name: 'TagMap',     idCol: 'TagMapId',      fkCols: [{ name: 'TagId', map: 'Tag' }, { name: 'NoteId', map: 'Note' }, { name: 'LocationId', map: 'Location' }],                condition: p.mergeTags },
      { name: 'Bookmark',   idCol: 'BookmarkId',    fkCols: [{ name: 'LocationId',          map: 'Location' }, { name: 'PublicationLocationId', map: 'Location' }],                   condition: p.mergeBookmarks },
      { name: 'InputField', idCol: null,            fkCols: [{ name: 'LocationId',          map: 'Location' }],                                                                        condition: p.mergeNotes },
    ];

    for (const sf of secondaryFiles) {
      if (cancelled) { log('Merge cancelled by user.'); break; }

      let srcDb = null;
      try {
        log(`>> Opening ${sf.name}...`);
        await A();

        const hash = await sha1Buf(sf.buffer);
        if (hash && seenHashes.has(hash)) {
          log(`Skipping ${sf.name} — identical to a previously processed file.`);
          continue;
        }
        if (hash) seenHashes.add(hash);

        const zip = await new JSZip().loadAsync(sf.buffer);
        const dbEntry = Object.keys(zip.files).find(k => /userdata\.db$/i.test(k));
        if (!dbEntry) {
          log(`'${sf.name}' doesn't look like a JW Library backup (missing userData.db). Skipping.`, true);
          continue;
        }

        srcDb = new SQL.Database(await zip.files[dbEntry].async('uint8array'));
        a.run('BEGIN TRANSACTION;');

        const idMap      = { Location: {}, UserMark: {}, BlockRange: {}, Note: {}, Tag: {}, TagMap: {}, Bookmark: {} };
        const pendingTag = [];

        for (const tbl of TABLES) {
          const { name: S, idCol: fa, fkCols: Ha, condition: Ga } = tbl;
          if (!Ga) continue;
          try {
            const res = srcDb.exec(`SELECT * FROM "${S}"`);
            if (!(res.length > 0 && res[0].values)) continue;

            const cols = res[0].columns;
            const pkIdx = fa ? cols.indexOf(fa) : -1;
            const fkInfo = (Ha || []).map(fk => ({ idx: cols.indexOf(fk.name), map: idMap[fk.map] })).filter(fk => fk.idx > -1);

            log(`Processing ${res[0].values.length} items from ${S}...`);
            await A();

            // Build lookup maps for dedup/conflict detection
            const existing = new Map();
            const existingMarkIds = new Set();
            const locDedupeKeys = S === 'Location' ? cols.filter(c => c !== 'LocationId' && c !== 'Title') : [];

            if (S === 'Tag') {
              try { const r = a.exec('SELECT Name, TagId FROM Tag'); r[0] && r[0].values.forEach(h => existing.set(h[0], h[1])); } catch {}
            } else if (S === 'Location' && locDedupeKeys.length > 0) {
              try {
                const r = a.exec(`SELECT LocationId, ${locDedupeKeys.map(c => `ifnull("${c}", '')`).join(',')} FROM Location`);
                r[0] && r[0].values.forEach(h => {
                  existing.set(h.slice(1).map(v => v === null ? '' : String(v)).join('|||'), h[0]);
                });
              } catch {}
            } else if (S === 'Note') {
              try { const r = a.exec('SELECT Guid, NoteId, LastModified FROM Note'); r[0] && r[0].values.forEach(h => existing.set(h[0], { id: h[1], lastMod: h[2] })); } catch {}
            } else if (S === 'UserMark') {
              try { const r = a.exec('SELECT UserMarkGuid, UserMarkId, Version FROM UserMark'); r[0] && r[0].values.forEach(h => existing.set(h[0], { id: h[1], version: h[2] })); } catch {}
            } else if (S === 'BlockRange') {
              try { const r = a.exec('SELECT UserMarkId FROM BlockRange'); r[0] && r[0].values.forEach(h => existingMarkIds.add(h[0])); } catch {}
            }

            let inserted = 0;

            for (let N = 0; N < res[0].values.length; N++) {
              const row = [...res[0].values[N]];   // mutable copy

              // Yield every 250 rows — lets the cancel message be processed
              if (N % 250 === 0) {
                await A();
                if (cancelled) throw new Error('Merge cancelled by user');
                if (totalRows > 0) {
                  processedRows += 250;
                  const elapsed = Date.now() - startTime;
                  const ratio   = Math.min(1, processedRows / totalRows);
                  const eta     = ratio > 0.05 ? Math.max(0, Math.round((elapsed / ratio - elapsed) / 1000)) : null;
                  prog({ current: Math.min(processedRows, totalRows), total: totalRows, eta, label: `${S} (${sf.name})` });
                }
              }

              const pkVal = pkIdx > -1 ? row[pkIdx] : null;

              // Remap foreign keys; skip row if any required FK is missing
              let brokenFK = false;
              fkInfo.forEach(fk => {
                const srcId = row[fk.idx];
                if (srcId !== null && fk.map[srcId] !== undefined) {
                  const mapped = fk.map[srcId];
                  if (mapped === -1) brokenFK = true;
                  row[fk.idx] = mapped;
                }
              });

              let shouldInsert = !brokenFK;

              // Date filter (Notes only)
              if (shouldInsert && p.syncByDate && p.filterDate && S === 'Note') {
                const lmIdx = cols.indexOf('LastModified');
                if (lmIdx > -1 && row[lmIdx] && new Date(row[lmIdx]).getTime() < dateFilter) shouldInsert = false;
              }

              if (shouldInsert) {
                if (S === 'Tag') {
                  const nameIdx = cols.indexOf('Name');
                  if (nameIdx > -1) {
                    const rawName = row[nameIdx];
                    const spec = ne[rawName];
                    if (spec && !spec.checked) {
                      shouldInsert = false;
                      if (pkVal !== null) idMap[S][pkVal] = -1;
                    } else {
                      const mapped = ma(rawName);
                      row[nameIdx] = mapped;
                      if (existing.has(mapped)) {
                        shouldInsert = false;
                        if (pkVal !== null) idMap[S][pkVal] = existing.get(mapped);
                      }
                    }
                  }
                } else if (S === 'Location' && locDedupeKeys.length > 0) {
                  const key = locDedupeKeys.map(c => { const v = row[cols.indexOf(c)]; return v == null ? '' : String(v); }).join('|||');
                  if (existing.has(key)) {
                    shouldInsert = false;
                    if (pkVal !== null) idMap[S][pkVal] = existing.get(key);
                  }
                } else if (S === 'Note') {
                  const guidIdx = cols.indexOf('Guid');
                  if (guidIdx > -1) {
                    const guid = row[guidIdx];
                    if (existing.has(guid)) {
                      const { id: existId, lastMod } = existing.get(guid);
                      const lmIdx = cols.indexOf('LastModified');
                      const srcMod = lmIdx > -1 ? row[lmIdx] : null;
                      if (p.conflictStrategy === 'newest' && srcMod &&
                          new Date(srcMod).getTime() - new Date(lastMod).getTime() > 5000) {
                        a.run(`DELETE FROM Note WHERE NoteId = ${existId}`);
                        f.Updated++;
                      } else {
                        shouldInsert = false;
                        if (pkVal !== null) idMap[S][pkVal] = existId;
                        if (importTagId) pendingTag.push(existId);
                      }
                    } else if (p.smartDedupe) {
                      const contentIdx = cols.indexOf('Content');
                      if (contentIdx > -1 && row[contentIdx]) {
                        if (dedupeSet.has(stripHTML(row[contentIdx]))) {
                          shouldInsert = false;
                          f.Deduplicated++;
                        }
                      }
                    }
                  }
                } else if (S === 'UserMark') {
                  const guidIdx = cols.indexOf('UserMarkGuid');
                  if (guidIdx > -1) {
                    const guid = row[guidIdx];
                    if (existing.has(guid)) {
                      const { id: existId, version: existVer } = existing.get(guid);
                      const verIdx = cols.indexOf('Version');
                      const srcVer = verIdx > -1 ? row[verIdx] : 0;
                      if (p.conflictStrategy === 'newest' && srcVer > (existVer || 0)) {
                        const ciIdx = cols.indexOf('ColorIndex');
                        const updates = [];
                        if (ciIdx > -1) updates.push(`ColorIndex = ${row[ciIdx]}`);
                        updates.push(`Version = ${srcVer}`);
                        if (updates.length) { a.run(`UPDATE UserMark SET ${updates.join(', ')} WHERE UserMarkId = ${existId}`); f.Updated++; }
                      }
                      shouldInsert = false;
                      if (pkVal !== null) idMap[S][pkVal] = existId;
                    }
                  }
                } else if (S === 'BlockRange') {
                  const umIdx = cols.indexOf('UserMarkId');
                  if (umIdx > -1 && existingMarkIds.has(row[umIdx])) shouldInsert = false;
                }
              }

              if (shouldInsert) {
                const insertCols = pkIdx > -1 ? cols.filter((_, i) => i !== pkIdx)  : cols;
                const insertVals = pkIdx > -1 ? row.filter((_, i) => i !== pkIdx)   : row;
                const newId = insertRow(S, insertCols, insertVals);
                if (newId > 0) {
                  if (pkVal !== null && pkIdx > -1) idMap[S][pkVal] = newId;
                  inserted++;
                  if (S === 'Note') {
                    if (p.smartDedupe) {
                      const ci = cols.indexOf('Content');
                      if (ci > -1 && row[ci]) dedupeSet.add(stripHTML(row[ci]));
                    }
                    if (importTagId) pendingTag.push(newId);
                    if (previewNotes.length < 20) {
                      const ti = cols.indexOf('Title'), ci = cols.indexOf('Content');
                      previewNotes.push({
                        title:   ti > -1 ? safeText(row[ti]) : '(untitled)',
                        content: ci > -1 ? safeText(row[ci]).slice(0, 200) : '',
                        source:  sf.name,
                      });
                    }
                  }
                }
              }
            }

            if (f[S] !== undefined) f[S] += inserted;
            else if (S === 'InputField') f.InputFields = (f.InputFields || 0) + inserted;
          } catch (err) { console.error(err); }
        }

        if (importTagId && pendingTag.length > 0) {
          pendingTag.forEach(noteId => {
            try { a.run(`INSERT OR IGNORE INTO TagMap (TagId, NoteId) VALUES (${importTagId}, ${noteId})`); } catch {}
          });
        }

        a.run('COMMIT;');
      } catch (err) {
        log(`Error processing ${sf.name}: ${err.message}`, true);
        try { a.run('ROLLBACK;'); } catch {}
        f.Errors++;
      } finally {
        if (srcDb) try { srcDb.close(); } catch {}
      }
    }

    freeStmts();
  }

  // ── Step 4: Deep clean ──────────────────────────────────────────────────
  if (p.deepClean) {
    log('Step 4: Executing deep clean optimizer...');
    await A();
    try {
      a.run('DELETE FROM TagMap WHERE TagId NOT IN (SELECT TagId FROM Tag)');
      a.run('DELETE FROM Tag WHERE TagId NOT IN (SELECT TagId FROM TagMap)');
      f.Cleaned++;
    } catch {}
  }

  // ── Step 5: Integrity check + vacuum ───────────────────────────────────
  log('Step 5: Verifying and compressing database...');
  await A();
  a.run('PRAGMA foreign_keys = ON;');
  const check = a.exec('PRAGMA integrity_check;');
  if (check.length > 0 && check[0].values[0][0] !== 'ok')
    throw new Error('Safety check failed. Database is corrupt.');
  a.run('VACUUM;');

  // ── Pre-merge impact preview gate ──────────────────────────────────────
  if (p.previewConfirm) {
    // Opt-in Library Doctor: scan the fully merged database headlessly and
    // send the findings along with the impact card; fix them only after the
    // user confirms. A scan failure never blocks the merge.
    let doctorReport = null;
    if (p.doctorCheck) {
      log('Library Doctor: examining the merged result...');
      try { doctorReport = doctorScan(a); } catch (e) { doctorReport = null; }
    }
    self.postMessage({ type: 'impact', counts: {
      Note: f.Note, UserMark: f.UserMark, Bookmark: f.Bookmark, Tag: f.Tag,
      Updated: f.Updated, Deduplicated: f.Deduplicated, InputField: f.InputFields || 0
    }, doctor: doctorReport });
    const proceed = await new Promise(res => { confirmResolver = res; });
    if (!proceed) {
      try { a.close(); } catch {}
      a = null;
      return { cancelled: true };
    }
    if (doctorReport && doctorReport.issues > 0) {
      log('Library Doctor: fixing ' + doctorReport.issues + ' issue(s)...');
      try { f.Cleaned += doctorFix(a); } catch (e) { log('Library Doctor: cleanup skipped (' + (e && e.message) + ')', false); }
    }
  }

  // ── Step 6: Package output ZIP ─────────────────────────────────────────
  log('Step 6: Packaging final download...');
  await A();
  timings.merge = _now() - _tm; _tm = _now();
  if (self.__jwFinalizeBackup) self.__jwFinalizeBackup.touchLastModified(a);
  const exportedDb = a.export();
  a.close();
  a = null;

  const outKey = Object.keys(o.files).find(k => /userdata\.db$/i.test(k));
  // manifest.json must describe the merged database, hash included.
  if (self.__jwFinalizeBackup) await self.__jwFinalizeBackup(o, outKey, exportedDb);
  else o.file(outKey, exportedDb);
  const zipBuf = await o.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });
  timings.package = _now() - _tm; timings.total = _now() - _t0;
  timings.rows = (f.Note + f.UserMark + f.Bookmark + f.Tag + (f.InputFields || 0) + f.Updated + f.Deduplicated) || 0;

  return { zipBuffer: zipBuf, stats: f, previewNotes, timings };
}

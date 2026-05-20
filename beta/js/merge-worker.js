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

let cancelled = false;

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

self.onmessage = async ({ data }) => {
  if (data.type === 'cancel') { cancelled = true; return; }
  if (data.type !== 'merge') return;
  cancelled = false;
  try {
    const result = await runMerge(data);
    self.postMessage(
      { type: 'done', zipBuffer: result.zipBuffer, stats: result.stats, previewNotes: result.previewNotes },
      [result.zipBuffer]
    );
  } catch (e) {
    self.postMessage({ type: 'error', message: e.message });
  }
};

async function runMerge({ mainBuffer, secondaryFiles, opts, tagManager, colorRules }) {
  const SQL = await initSqlJs({
    locateFile: f => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/${f}`
  });

  const p   = opts;
  const ne  = tagManager;
  const Le  = colorRules || [];
  const ma  = name => mapTagName(name, ne);

  // ── Step 1: Open main ZIP ───────────────────────────────────────────────
  log('Step 1: Unzipping main backup...');
  await A();

  const o = await new JSZip().loadAsync(mainBuffer);
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
  const dbBytes = await o.files[dbKey].async('uint8array');

  // ── Step 2: Open base database ──────────────────────────────────────────
  log('Step 2: Preparing database framework...');
  await A();

  let a = new SQL.Database(dbBytes);
  a.run('PRAGMA foreign_keys = OFF;');

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

  // ── Step 6: Package output ZIP ─────────────────────────────────────────
  log('Step 6: Packaging final download...');
  await A();
  const exportedDb = a.export();
  a.close();
  a = null;

  o.file(Object.keys(o.files).find(k => /userdata\.db$/i.test(k)), exportedDb);
  const zipBuf = await o.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });

  return { zipBuffer: zipBuf, stats: f, previewNotes };
}

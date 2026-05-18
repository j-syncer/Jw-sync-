/**
 * Creates minimal .jwlibrary fixture files (ZIP containing userData.db) for tests.
 * Mirrors the real JW Library SQLite schema just enough for the merge worker to operate.
 */
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

const initSqlJs = require('sql.js');
const JSZip = require('jszip');

let _SQL = null;

export async function getSQL() {
  if (!_SQL) _SQL = await initSqlJs();
  return _SQL;
}

const SCHEMA = `
  CREATE TABLE IF NOT EXISTS Location (
    LocationId    INTEGER PRIMARY KEY,
    BookNumber    INTEGER,
    ChapterNumber INTEGER,
    DocumentId    INTEGER,
    Track         INTEGER,
    IssueTagNumber INTEGER DEFAULT 0,
    KeySymbol     TEXT,
    MepsLanguage  INTEGER DEFAULT 0,
    Type          INTEGER DEFAULT 0,
    Title         TEXT
  );
  CREATE TABLE IF NOT EXISTS Note (
    NoteId          INTEGER PRIMARY KEY,
    Guid            TEXT UNIQUE NOT NULL,
    UserMarkId      INTEGER,
    LocationId      INTEGER,
    Title           TEXT,
    Content         TEXT,
    LastModified    TEXT NOT NULL,
    Created         TEXT NOT NULL,
    BlockType       INTEGER DEFAULT 0,
    BlockIdentifier INTEGER
  );
  CREATE TABLE IF NOT EXISTS UserMark (
    UserMarkId   INTEGER PRIMARY KEY,
    ColorIndex   INTEGER DEFAULT 1,
    LocationId   INTEGER,
    StyleIndex   INTEGER DEFAULT 0,
    UserMarkGuid TEXT UNIQUE,
    Version      INTEGER DEFAULT 0
  );
  CREATE TABLE IF NOT EXISTS BlockRange (
    BlockRangeId INTEGER PRIMARY KEY,
    BlockType    INTEGER DEFAULT 2,
    Identifier   INTEGER,
    StartToken   INTEGER,
    EndToken     INTEGER,
    UserMarkId   INTEGER
  );
  CREATE TABLE IF NOT EXISTS Tag (
    TagId INTEGER PRIMARY KEY,
    Type  INTEGER DEFAULT 0,
    Name  TEXT UNIQUE
  );
  CREATE TABLE IF NOT EXISTS TagMap (
    TagMapId       INTEGER PRIMARY KEY,
    PlaylistItemId INTEGER,
    LocationId     INTEGER,
    NoteId         INTEGER,
    TagId          INTEGER NOT NULL,
    Position       INTEGER DEFAULT 0
  );
  CREATE TABLE IF NOT EXISTS Bookmark (
    BookmarkId          INTEGER PRIMARY KEY,
    LocationId          INTEGER,
    PublicationLocationId INTEGER,
    Slot                INTEGER DEFAULT 0,
    Title               TEXT,
    Snippet             TEXT,
    BlockType           INTEGER DEFAULT 0,
    BlockIdentifier     INTEGER
  );
  CREATE TABLE IF NOT EXISTS InputField (
    LocationId INTEGER NOT NULL,
    TextTag    TEXT NOT NULL,
    Value      TEXT,
    PRIMARY KEY (LocationId, TextTag)
  );
`;

/**
 * @param {object} opts
 * @param {Array<{guid, title?, content?, lastModified?, tags?}>} opts.notes
 * @param {Array<{name}>} opts.tags
 * @param {Array<{guid, colorIndex?, version?}>} opts.marks
 * @param {Array<{title?, snippet?}>} opts.bookmarks
 * @param {string} opts.dbKey - path inside ZIP (default: 'userData.db')
 * @param {boolean} opts.omitDb - if true, create ZIP without any .db file (for error-path tests)
 * @returns {Promise<ArrayBuffer>}
 */
export async function createBackup({
  notes = [],
  tags = [],
  marks = [],
  bookmarks = [],
  dbKey = 'userData.db',
  omitDb = false,
} = {}) {
  const zip = new JSZip();
  zip.file('manifest.json', JSON.stringify({
    name: 'Test Backup',
    creationDate: new Date().toISOString(),
  }));

  if (!omitDb) {
    const SQL = await getSQL();
    const db = new SQL.Database();
    db.run(SCHEMA);

    const tagIdMap = {};
    for (const tag of tags) {
      db.run('INSERT INTO Tag (Name) VALUES (?)', [tag.name]);
      const r = db.exec('SELECT last_insert_rowid()');
      tagIdMap[tag.name] = r[0].values[0][0];
    }

    const now = new Date().toISOString();
    for (const note of notes) {
      db.run(
        'INSERT INTO Note (Guid, Title, Content, LastModified, Created) VALUES (?, ?, ?, ?, ?)',
        [note.guid, note.title ?? null, note.content ?? null, note.lastModified ?? now, now],
      );
      const r = db.exec('SELECT last_insert_rowid()');
      const noteId = r[0].values[0][0];

      for (const tagName of (note.tags ?? [])) {
        const tagId = tagIdMap[tagName];
        if (tagId !== undefined) {
          db.run('INSERT INTO TagMap (NoteId, TagId) VALUES (?, ?)', [noteId, tagId]);
        }
      }
    }

    for (const mark of marks) {
      db.run(
        'INSERT INTO UserMark (ColorIndex, UserMarkGuid, Version) VALUES (?, ?, ?)',
        [mark.colorIndex ?? 1, mark.guid, mark.version ?? 0],
      );
    }

    for (const bm of bookmarks) {
      db.run(
        'INSERT INTO Bookmark (Title, Snippet) VALUES (?, ?)',
        [bm.title ?? null, bm.snippet ?? null],
      );
    }

    zip.file(dbKey, db.export());
    db.close();
  }

  return zip.generateAsync({ type: 'arraybuffer' });
}

/**
 * Open a result zipBuffer and return a sql.js Database ready for querying.
 * Caller must call db.close() when done.
 */
export async function openResult(zipBuffer) {
  const SQL = await getSQL();
  const zip = await new JSZip().loadAsync(zipBuffer);
  const dbEntry = Object.keys(zip.files).find(k => /userdata\.db$/i.test(k));
  if (!dbEntry) throw new Error('No userData.db found in result ZIP');
  const bytes = await zip.files[dbEntry].async('uint8array');
  return new SQL.Database(bytes);
}

/** Convenience: run a SELECT and return rows as plain objects. */
export function query(db, sql, params = []) {
  const res = db.exec(sql, params);
  if (!res.length || !res[0].values.length) return [];
  const { columns, values } = res[0];
  return values.map(row =>
    Object.fromEntries(columns.map((col, i) => [col, row[i]])),
  );
}

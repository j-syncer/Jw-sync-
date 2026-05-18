import { describe, it, expect, beforeAll } from 'vitest';
import { send, getWorkerFn, ALL_ON } from './helpers/loadWorker.js';
import { createBackup, openResult, query } from './helpers/createBackup.js';

// ─── helpers ────────────────────────────────────────────────────────────────

function mergeMsg(mainBuffer, secondaryFiles = [], opts = {}, extra = {}) {
  return {
    type: 'merge',
    mainBuffer,
    mainName: 'main.jwlibrary',
    secondaryFiles,
    opts: { ...ALL_ON, ...opts },
    tagManager: {},
    colorRules: [],
    ...extra,
  };
}

function doneMsg(msgs) {
  return msgs.find(m => m.type === 'done');
}
function errorMsg(msgs) {
  return msgs.find(m => m.type === 'error');
}
function logMsgs(msgs) {
  return msgs.filter(m => m.type === 'log');
}

// ─── Pure function: mapTagName ───────────────────────────────────────────────

describe('mapTagName (pure function)', () => {
  let mapTagName;
  beforeAll(async () => { mapTagName = await getWorkerFn('mapTagName'); });

  it('returns the original name when the tag has no entry', () => {
    expect(mapTagName('Study', {})).toBe('Study');
  });

  it('returns the original name for action "keep"', () => {
    expect(mapTagName('Study', { Study: { action: 'keep' } })).toBe('Study');
  });

  it('returns targetName for action "merge"', () => {
    expect(mapTagName('Study', { Study: { action: 'merge', targetName: 'Research' } }))
      .toBe('Research');
  });

  it('returns customName for action "rename" with a non-empty customName', () => {
    expect(mapTagName('Study', { Study: { action: 'rename', customName: 'Research' } }))
      .toBe('Research');
  });

  it('falls back to original name for action "rename" with blank customName', () => {
    expect(mapTagName('Study', { Study: { action: 'rename', customName: '   ' } }))
      .toBe('Study');
  });
});

// ─── Basic merge ─────────────────────────────────────────────────────────────

describe('basic merge', () => {
  it('preserves primary data when there are no secondary files', async () => {
    const main = await createBackup({ notes: [
      { guid: 'n1', title: 'Alpha', content: 'Hello' },
      { guid: 'n2', title: 'Beta',  content: 'World' },
    ]});
    const msgs = await send(mergeMsg(main));
    const done = doneMsg(msgs);

    expect(done).toBeTruthy();
    expect(done.stats.Note).toBe(0);   // nothing was merged from secondary

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(2);
    db.close();
  });

  it('merges non-overlapping notes from a secondary file', async () => {
    const main = await createBackup({ notes: [
      { guid: 'n1', title: 'Main note 1' },
      { guid: 'n2', title: 'Main note 2' },
    ]});
    const secondary = await createBackup({ notes: [
      { guid: 'n3', title: 'Secondary note 1' },
      { guid: 'n4', title: 'Secondary note 2' },
    ]});

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'secondary.jwlibrary' }]));
    const done = doneMsg(msgs);

    expect(done).toBeTruthy();
    expect(done.stats.Note).toBe(2);

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(4);
    db.close();
  });

  it('populates previewNotes with up to 20 entries from secondary files', async () => {
    const main = await createBackup();
    const secondaryNotes = Array.from({ length: 25 }, (_, i) => ({
      guid: `sn${i}`,
      title: `Note ${i}`,
      content: `Content ${i}`,
    }));
    const secondary = await createBackup({ notes: secondaryNotes });

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'sec.jwlibrary' }]));
    const done = doneMsg(msgs);

    expect(done.previewNotes.length).toBe(20);
    expect(done.previewNotes[0]).toMatchObject({ title: 'Note 0', source: 'sec.jwlibrary' });
  });

  it('result ZIP passes SQLite integrity_check', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1', content: 'test' }] });
    const msgs = await send(mergeMsg(main));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const [{ integrity_check }] = query(db, 'PRAGMA integrity_check');
    expect(integrity_check).toBe('ok');
    db.close();
  });

  it('merges bookmarks from a secondary file', async () => {
    const main = await createBackup();
    const secondary = await createBackup({ bookmarks: [
      { title: 'BM 1', snippet: 'Snippet 1' },
      { title: 'BM 2', snippet: 'Snippet 2' },
    ]});

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'sec.jwlibrary' }]));
    const done = doneMsg(msgs);

    expect(done.stats.Bookmark).toBe(2);
    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Bookmark')[0].c).toBe(2);
    db.close();
  });
});

// ─── Note deduplication ──────────────────────────────────────────────────────

describe('note deduplication', () => {
  it('keeps the existing note when both have the same GUID (strategy: keep)', async () => {
    const main = await createBackup({ notes: [
      { guid: 'shared', title: 'Main version', content: 'original',
        lastModified: '2024-01-01T00:00:00.000Z' },
    ]});
    const secondary = await createBackup({ notes: [
      { guid: 'shared', title: 'Secondary version', content: 'override',
        lastModified: '2024-06-01T00:00:00.000Z' },
    ]});

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'sec.jwlibrary' }]));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const notes = query(db, 'SELECT Title FROM Note WHERE Guid = ?', ['shared']);
    expect(notes).toHaveLength(1);
    expect(notes[0].Title).toBe('Main version');
    db.close();
  });

  it('replaces existing note when secondary is newer (strategy: newest)', async () => {
    const OLD = '2024-01-01T00:00:00.000Z';
    const NEW = '2024-06-01T12:00:00.000Z';

    const main = await createBackup({ notes: [
      { guid: 'shared', title: 'Old title', content: 'old content', lastModified: OLD },
    ]});
    const secondary = await createBackup({ notes: [
      { guid: 'shared', title: 'New title', content: 'new content', lastModified: NEW },
    ]});

    const msgs = await send(mergeMsg(
      main,
      [{ buffer: secondary, name: 'sec.jwlibrary' }],
      { conflictStrategy: 'newest' },
    ));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const notes = query(db, 'SELECT Title FROM Note WHERE Guid = ?', ['shared']);
    expect(notes).toHaveLength(1);
    expect(notes[0].Title).toBe('New title');
    db.close();
  });

  it('keeps existing note when secondary is older (strategy: newest)', async () => {
    const OLDER = '2023-01-01T00:00:00.000Z';
    const NEWER = '2024-06-01T12:00:00.000Z';

    const main = await createBackup({ notes: [
      { guid: 'shared', title: 'Main version', lastModified: NEWER },
    ]});
    const secondary = await createBackup({ notes: [
      { guid: 'shared', title: 'Secondary version', lastModified: OLDER },
    ]});

    const msgs = await send(mergeMsg(
      main,
      [{ buffer: secondary, name: 'sec.jwlibrary' }],
      { conflictStrategy: 'newest' },
    ));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const notes = query(db, 'SELECT Title FROM Note WHERE Guid = ?', ['shared']);
    expect(notes[0].Title).toBe('Main version');
    db.close();
  });

  it('deduplicates by content when smartDedupe is enabled', async () => {
    const main = await createBackup({ notes: [
      // Content has HTML; stripped form is 'hello world'
      { guid: 'n1', content: '<b>Hello World</b>' },
    ]});
    const secondary = await createBackup({ notes: [
      // Different GUID but same stripped content
      { guid: 'n2', content: 'Hello World' },
    ]});

    const msgs = await send(mergeMsg(
      main,
      [{ buffer: secondary, name: 'sec.jwlibrary' }],
      { smartDedupe: true },
    ));
    const done = doneMsg(msgs);

    expect(done.stats.Deduplicated).toBe(1);
    expect(done.stats.Note).toBe(0);    // nothing new inserted

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(1);
    db.close();
  });
});

// ─── Tag manager ─────────────────────────────────────────────────────────────

describe('tag manager (main-file operations)', () => {
  it('renames a tag in the main file', async () => {
    const main = await createBackup({
      tags: [{ name: 'Study' }],
      notes: [{ guid: 'n1', content: 'tagged note', tags: ['Study'] }],
    });

    const msgs = await send(mergeMsg(main, [], {}, {
      tagManager: { Study: { action: 'rename', customName: 'Research', checked: true } },
    }));
    const done = doneMsg(msgs);
    expect(done.stats.Updated).toBe(1);

    const db = await openResult(done.zipBuffer);
    const tags = query(db, 'SELECT Name FROM Tag');
    expect(tags.map(r => r.Name)).toContain('Research');
    expect(tags.map(r => r.Name)).not.toContain('Study');

    // TagMap must still link the note to the renamed tag
    const taggedNotes = query(db, `
      SELECT n.Guid FROM Note n
      JOIN TagMap tm ON tm.NoteId = n.NoteId
      JOIN Tag    t  ON t.TagId   = tm.TagId
      WHERE t.Name = 'Research'
    `);
    expect(taggedNotes).toHaveLength(1);
    db.close();
  });

  it('merges one tag into another in the main file', async () => {
    const main = await createBackup({
      tags: [{ name: 'Study' }, { name: 'Research' }],
      notes: [
        { guid: 'n1', content: 'note 1', tags: ['Study'] },
        { guid: 'n2', content: 'note 2', tags: ['Research'] },
      ],
    });

    const msgs = await send(mergeMsg(main, [], {}, {
      tagManager: { Study: { action: 'merge', targetName: 'Research', checked: true } },
    }));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const tags = query(db, 'SELECT Name FROM Tag');
    expect(tags.map(r => r.Name)).not.toContain('Study');
    expect(tags.map(r => r.Name)).toContain('Research');

    // Both notes should now be tagged with Research
    const tagged = query(db, `
      SELECT COUNT(*) as c FROM TagMap tm
      JOIN Tag t ON t.TagId = tm.TagId WHERE t.Name = 'Research'
    `);
    expect(tagged[0].c).toBe(2);
    db.close();
  });

  it('deletes a tag and its TagMap entries when checked is false', async () => {
    const main = await createBackup({
      tags: [{ name: 'ToDelete' }],
      notes: [{ guid: 'n1', content: 'note', tags: ['ToDelete'] }],
    });

    const msgs = await send(mergeMsg(main, [], {}, {
      tagManager: { ToDelete: { action: 'keep', checked: false } },
    }));
    const done = doneMsg(msgs);
    expect(done.stats.Updated).toBe(1);

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT * FROM Tag WHERE Name = ?', ['ToDelete'])).toHaveLength(0);
    expect(query(db, 'SELECT COUNT(*) as c FROM TagMap')[0].c).toBe(0);
    db.close();
  });

  it('renames an incoming tag from a secondary file', async () => {
    const main = await createBackup();
    const secondary = await createBackup({
      tags: [{ name: 'OldName' }],
      notes: [{ guid: 'n1', content: 'tagged', tags: ['OldName'] }],
    });

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'sec.jwlibrary' }], {}, {
      tagManager: { OldName: { action: 'rename', customName: 'NewName', checked: true } },
    }));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT Name FROM Tag WHERE Name = ?', ['OldName'])).toHaveLength(0);
    expect(query(db, 'SELECT Name FROM Tag WHERE Name = ?', ['NewName'])).toHaveLength(1);
    db.close();
  });
});

// ─── Color rules ─────────────────────────────────────────────────────────────

describe('bulk colour changer', () => {
  it('remaps UserMark colours according to rules', async () => {
    const main = await createBackup({ marks: [
      { guid: 'um1', colorIndex: 1 },
      { guid: 'um2', colorIndex: 1 },
      { guid: 'um3', colorIndex: 3 },
    ]});

    const msgs = await send(mergeMsg(main, [], {}, {
      colorRules: [{ from: '1', to: '2' }],
    }));
    const done = doneMsg(msgs);

    expect(done.stats.ColorsMapped).toBe(1);   // one rule applied

    const db = await openResult(done.zipBuffer);
    const marks = query(db, 'SELECT ColorIndex FROM UserMark ORDER BY UserMarkId');
    expect(marks[0].ColorIndex).toBe(2);
    expect(marks[1].ColorIndex).toBe(2);
    expect(marks[2].ColorIndex).toBe(3);   // unaffected
    db.close();
  });

  it('skips rules where from === to', async () => {
    const main = await createBackup({ marks: [{ guid: 'um1', colorIndex: 2 }] });

    const msgs = await send(mergeMsg(main, [], {}, {
      colorRules: [{ from: '2', to: '2' }],
    }));
    const done = doneMsg(msgs);

    expect(done.stats.ColorsMapped).toBe(0);
    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT ColorIndex FROM UserMark')[0].ColorIndex).toBe(2);
    db.close();
  });
});

// ─── Import tag ───────────────────────────────────────────────────────────────

describe('import tag', () => {
  it('tags all newly merged notes with the import tag', async () => {
    const main = await createBackup();
    const secondary = await createBackup({ notes: [
      { guid: 'n1', title: 'Note A' },
      { guid: 'n2', title: 'Note B' },
    ]});

    const msgs = await send(mergeMsg(
      main,
      [{ buffer: secondary, name: 'sec.jwlibrary' }],
      { importTag: 'Imported' },
    ));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    const tagged = query(db, `
      SELECT COUNT(*) as c FROM TagMap tm
      JOIN Tag t ON t.TagId = tm.TagId WHERE t.Name = 'Imported'
    `);
    expect(tagged[0].c).toBe(2);
    db.close();
  });

  it('does not create import tag when there are no secondary files', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1' }] });

    const msgs = await send(mergeMsg(main, [], { importTag: 'Imported' }));
    const done = doneMsg(msgs);

    const db = await openResult(done.zipBuffer);
    expect(query(db, "SELECT * FROM Tag WHERE Name = 'Imported'")).toHaveLength(0);
    db.close();
  });
});

// ─── Date filter ─────────────────────────────────────────────────────────────

describe('date filter (syncByDate)', () => {
  it('excludes notes modified before the filter date', async () => {
    const main = await createBackup();
    const secondary = await createBackup({ notes: [
      { guid: 'old',    content: 'too old',  lastModified: '2023-01-01T00:00:00.000Z' },
      { guid: 'recent', content: 'keep me',  lastModified: '2024-06-01T00:00:00.000Z' },
    ]});

    const msgs = await send(mergeMsg(
      main,
      [{ buffer: secondary, name: 'sec.jwlibrary' }],
      { syncByDate: true, filterDate: '2024-01-01' },
    ));
    const done = doneMsg(msgs);

    expect(done.stats.Note).toBe(1);
    const db = await openResult(done.zipBuffer);
    const notes = query(db, 'SELECT Guid FROM Note');
    expect(notes.map(r => r.Guid)).toContain('recent');
    expect(notes.map(r => r.Guid)).not.toContain('old');
    db.close();
  });
});

// ─── Deep clean ──────────────────────────────────────────────────────────────

describe('deep clean', () => {
  it('removes tags with no TagMap entries', async () => {
    const main = await createBackup({
      tags: [{ name: 'Orphan' }, { name: 'Used' }],
      notes: [{ guid: 'n1', content: 'note', tags: ['Used'] }],
    });

    const msgs = await send(mergeMsg(main, [], { deepClean: true }));
    const done = doneMsg(msgs);

    expect(done.stats.Cleaned).toBe(1);
    const db = await openResult(done.zipBuffer);
    const tags = query(db, 'SELECT Name FROM Tag');
    expect(tags.map(r => r.Name)).not.toContain('Orphan');
    expect(tags.map(r => r.Name)).toContain('Used');
    db.close();
  });
});

// ─── Stats counters ──────────────────────────────────────────────────────────

describe('stats counters', () => {
  it('counts all inserted entity types correctly', async () => {
    const main = await createBackup();
    const secondary = await createBackup({
      notes:     [{ guid: 'n1' }, { guid: 'n2' }],
      tags:      [{ name: 'T1' }, { name: 'T2' }],
      marks:     [{ guid: 'um1' }],
      bookmarks: [{ title: 'BM' }],
    });

    const msgs = await send(mergeMsg(main, [{ buffer: secondary, name: 'sec.jwlibrary' }]));
    const { stats } = doneMsg(msgs);

    expect(stats.Note).toBe(2);
    expect(stats.Tag).toBe(2);
    expect(stats.UserMark).toBe(1);
    expect(stats.Bookmark).toBe(1);
    expect(stats.Errors).toBe(0);
  });
});

// ─── Edge cases / error paths ────────────────────────────────────────────────

describe('edge cases', () => {
  it('skips a secondary file that has no userData.db', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1' }] });
    const badZip = await createBackup({ omitDb: true });    // ZIP without userData.db

    const msgs = await send(mergeMsg(main, [{ buffer: badZip, name: 'bad.jwlibrary' }]));
    const done = doneMsg(msgs);

    expect(done).toBeTruthy();
    expect(done.stats.Errors).toBe(0);   // skipped, not crashed

    const errLog = logMsgs(msgs).find(m => m.isError);
    expect(errLog).toBeTruthy();
    expect(errLog.text).toMatch(/missing userData\.db/i);

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(1);  // primary data intact
    db.close();
  });

  it('skips an identical secondary file (duplicate hash)', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1', content: 'main note' }] });
    // Pass the exact same buffer twice — worker computes SHA-1 and deduplicates
    const secondary = await createBackup({ notes: [{ guid: 'n2', content: 'secondary' }] });

    const msgs = await send(mergeMsg(main, [
      { buffer: secondary, name: 'copy1.jwlibrary' },
      { buffer: secondary, name: 'copy2.jwlibrary' },   // identical buffer
    ]));
    const done = doneMsg(msgs);

    expect(done.stats.Note).toBe(1);   // only 1 unique secondary note, not 2

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(2);  // main + 1 secondary
    db.close();
  });

  it('reports an error message on corrupt input', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1' }] });
    const corrupt = new ArrayBuffer(64);   // not a valid ZIP

    const msgs = await send(mergeMsg(main, [{ buffer: corrupt, name: 'corrupt.jwlibrary' }]));
    const done = doneMsg(msgs);
    expect(done.stats.Errors).toBe(1);
  });

  it('produces a valid ZIP even when no secondary files are provided', async () => {
    const main = await createBackup({ notes: [{ guid: 'n1' }, { guid: 'n2' }] });
    const msgs = await send(mergeMsg(main, []));
    const done = doneMsg(msgs);

    expect(done).toBeTruthy();
    expect(errorMsg(msgs)).toBeUndefined();

    const db = await openResult(done.zipBuffer);
    expect(query(db, 'SELECT COUNT(*) as c FROM Note')[0].c).toBe(2);
    db.close();
  });
});

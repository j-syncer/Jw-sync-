// 25_md_tolerance.js — the promises the guide makes, enforced.
//
// The guide tells people they can write `pub: Matt. 26:39`, capitalise their
// keys, forget the space after the colon, leave the `---` fences off entirely
// and still have the note land on Matthew 26:39. Every one of those sentences
// is a promise, and a promise about parsing is exactly the kind that rots
// quietly: nothing throws when a reference stops being recognised, the note
// just arrives somewhere else.
//
// So each row below is a line in the guide. If a case here fails, either the
// parser regressed or the guide is now lying — and both are bugs.
//
// The second half is the part that keeps it honest: a spelling we had to guess,
// and a book we cannot place at all, must be *flagged for the reader* rather
// than acted on. Being liberal about what a file looks like is only safe while
// being strict about where a note ends up.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');
const JSZip = require('jszip');
const initSqlJs = require('sql.js');

const REPO = path.join(__dirname, '..');
let failures = 0;
const ok = (m) => console.log('  ✓ ' + m);
const fail = (m) => { failures++; console.log('  ✗ ' + m); };
const section = (t) => console.log('\n== ' + t + ' ==');

function boot() {
  const browseBlock = require('./helpers/browse-source').browseBlock(REPO + '/beta/index.html');
  if (!browseBlock) { fail('Browse module not found'); process.exit(1); }
  const dom = new JSDOM(`<!DOCTYPE html><html><body>${browseBlock}</body></html>`,
    { url: 'https://jwsync.org/', runScripts: 'dangerously', pretendToBeVisual: true });
  const win = dom.window;
  win.JSZip = JSZip;
  win.initSqlJs = () => initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  win.matchMedia = () => ({ matches: false, addListener() {}, removeListener() {} });
  win.localStorage.setItem('jwsync_lang', 'en');
  win.__bootBrowse();
  return win;
}

const win = boot();
const parse = (md, name) => win.__jwMdImport.parse(name || 'note.md', md);

// "Matthew 26:39" | "Matthew 26" | null (no reference) | "?" (flagged unknown)
function refOf(note) {
  const r = note.ref;
  if (!r) return null;
  if (r.unknown) return '?';
  return (r.guessed ? '~' : '') + r.label;
}

section('Front matter the way people write it');
const FM = [
  ['exactly as exported',
   '---\ntitle: A\npublication: Matthew 26:39\nbook: Matthew\nchapter: 26\nverse: 39\n---\n\nBody', 'Matthew 26:39'],
  ['no space after the colon', '---\ntitle:A\npublication:Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['extra spaces and tabs', '---\ntitle:   A  \n  publication:\tMatthew 26:39  \n---\nBody', 'Matthew 26:39'],
  ['capitalised keys', '---\nTitle: A\nPublication: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['shortened keys', '---\ntitle: A\npub: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['"reference" instead', '---\ntitle: A\nreference: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['"scripture" instead', '---\ntitle: A\nscripture: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['no fences at all', 'title: A\npub: Matthew 26:39\n\nBody', 'Matthew 26:39'],
  ['four dashes', '---- \ntitle: A\npub: Matthew 26:39\n----\nBody', 'Matthew 26:39'],
  ['closing with ...', '---\ntitle: A\npub: Matthew 26:39\n...\nBody', 'Matthew 26:39'],
  ['quoted values', '---\ntitle: "A"\npub: \'Matthew 26:39\'\n---\nBody', 'Matthew 26:39'],
  ['a trailing comment', '---\ntitle: A # mine\npub: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['windows line endings', '---\r\ntitle: A\r\npub: Matthew 26:39\r\n---\r\nBody', 'Matthew 26:39'],
  ['a byte order mark', '﻿---\ntitle: A\npub: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
  ['blank line before the fence', '\n\n---\ntitle: A\npub: Matthew 26:39\n---\nBody', 'Matthew 26:39'],
];
for (const [label, md, want] of FM) {
  const got = refOf(parse(md));
  if (got === want) ok(label);
  else fail(`${label}: expected ${want}, got ${got}`);
}

section('Bible references the way people write them');
const REFS = [
  ['full name', 'Matthew 26:39', 'Matthew 26:39'],
  ['abbreviated with a dot', 'Matt. 26:39', 'Matthew 26:39'],
  ['two-letter abbreviation', 'Mt 26:39', 'Matthew 26:39'],
  ['a full stop for the colon', 'John 3.16', 'John 3:16'],
  ['a "v" for the verse', '1 Cor 13 v4', '1 Corinthians 13:4'],
  ['no spaces at all', '1Cor13:4', '1 Corinthians 13:4'],
  ['roman numeral', 'II Timothy 3:16', '2 Timothy 3:16'],
  ['spelled-out number', 'Second Timothy 3:16', '2 Timothy 3:16'],
  ['chapter only', 'Matthew 26', 'Matthew 26'],
  ['a verse range keeps the first verse', 'Matthew 26:39-41', 'Matthew 26:39'],
  ['psalm singular', 'Psalm 23:1', 'Psalms 23:1'],
  ['song of songs', 'Song of Songs 2:1', 'Song of Solomon 2:1'],
];
for (const [label, ref, want] of REFS) {
  const got = refOf(parse(`---\ntitle: A\npub: ${ref}\n---\nBody`));
  if (got === want) ok(`${label} — ${ref}`);
  else fail(`${ref}: expected ${want}, got ${got}`);
}

section('Discrete book / chapter / verse fields');
for (const [label, fm, want] of [
  ['plain', 'book: Psalms\nchapter: 23\nverse: 1', 'Psalms 23:1'],
  ['abbreviated keys', 'book: Psalms\nch: 23\nv: 1', 'Psalms 23:1'],
  ['verse range', 'book: Matthew\nchapter: 26\nverse: 39-41', 'Matthew 26:39'],
  ['no verse', 'book: Matthew\nchapter: 26', 'Matthew 26'],
]) {
  const got = refOf(parse(`---\ntitle: A\n${fm}\n---\nBody`));
  if (got === want) ok(`${label}`);
  else fail(`${label}: expected ${want}, got ${got}`);
}

section('Tags, however they are written');
for (const [label, line, want] of [
  ['inline list', 'tags: [study, greek]', ['study', 'greek']],
  ['bare commas', 'tags: study, greek', ['study', 'greek']],
  ['semicolons', 'tags: study; greek', ['study', 'greek']],
  ['hashtags', 'tags: #study #greek', ['study', 'greek']],
  ['a block list', 'tags:\n  - study\n  - greek', ['study', 'greek']],
  ['singular key', 'tag: study', ['study']],
  ['keywords', 'keywords: study, greek', ['study', 'greek']],
]) {
  const got = parse(`---\ntitle: A\n${line}\n---\nBody`).tags;
  if (JSON.stringify(got) === JSON.stringify(want)) ok(label);
  else fail(`${label}: expected ${JSON.stringify(want)}, got ${JSON.stringify(got)}`);
}

section('Files with nothing to go on');
{
  const n = parse('# My heading\n\nSome text.');
  if (n.title === 'My heading') ok('title comes from the first heading');
  else fail('title not taken from heading: ' + n.title);
  if (!/My heading/.test(n.content)) ok('the heading is not repeated in the body');
  else fail('heading duplicated into the body');

  const f = parse('Just some text with no heading.', '12-my-study-note.md');
  if (f.title === 'my study note') ok('title falls back to a tidied filename');
  else fail('filename fallback wrong: ' + f.title);

  const extra = parse('title: A\nauthor: someone\npub: Matthew 26:39\n\nBody');
  if (refOf(extra) === 'Matthew 26:39') ok('unfenced front matter tolerates fields we do not use');
  else fail('unfenced block with an unknown field lost its reference: ' + refOf(extra));

  const c = parse('A sentence: with a colon in it.\n\nMore.');
  if (!/^A sentence/.test(c.title) && /A sentence: with a colon/.test(c.content))
    ok('a first line containing a colon is body text, not front matter');
  else fail('a sentence was eaten as front matter: ' + JSON.stringify({ t: c.title, c: c.content }));
}

section('Publication notes are not treated as broken references');
for (const pub of ['The Watchtower—2023 No. 4', 'Awake!—2023', 'Insight on the Scriptures, Volume 1']) {
  const got = refOf(parse(`---\ntitle: A\npublication: ${pub}\n---\nBody`));
  if (got === null) ok(`"${pub}" imports as an ordinary note, no question asked`);
  else fail(`"${pub}" was treated as a reference: ${got}`);
}

section('Anything interpreted is flagged, never assumed');
for (const [label, ref, want] of [
  ['a misspelled book is a guess', 'Mathew 26:39', '~Matthew 26:39'],
  ['another misspelling', 'Ecclesiates 3:1', '~Ecclesiastes 3:1'],
  ['a book we do not know is flagged', 'Enoch 3:5', '?'],
  ['a number that is not a book', 'Chapter 26:39', '?'],
]) {
  const got = refOf(parse(`---\ntitle: A\npub: ${ref}\n---\nBody`));
  if (got === want) ok(`${label} — ${ref}`);
  else fail(`${ref}: expected ${want}, got ${got}`);
}
{
  // "1 John" must never be corrected into "2 John": the number is not a typo.
  const got = refOf(parse('---\ntitle: A\npub: 1 Jonh 4:8\n---\nBody'));
  if (got === '~1 John 4:8') ok('a numbered book keeps its number when corrected');
  else fail('numbered book corrected wrongly: ' + got);
}

section('The guide and the parser agree');
{
  // The guide names specific aliases and abbreviations. If someone trims the
  // parser's tables, the page keeps promising them — a lie that no build step
  // and no page load would notice.
  const guide = fs.readFileSync(path.join(REPO, 'guides/import-markdown-notes-jw-library.html'), 'utf8');
  const browse = fs.readFileSync(path.join(REPO, 'js/browse.js'), 'utf8');
  const PROMISED_KEYS = ['pub', 'reference', 'ref', 'scripture', 'citation', 'source',
    'passage', 'keywords', 'categories', 'labels', 'topics', 'heading', 'chapter', 'verses'];
  const missingKeys = PROMISED_KEYS.filter(k => !new RegExp('\\b' + k + ":'").test(browse));
  if (!missingKeys.length) ok(`parser accepts all ${PROMISED_KEYS.length} field names the guide lists`);
  else fail('guide promises field names the parser does not accept: ' + missingKeys.join(', '));

  const PROMISED_ABBR = ['matt', 'mt', '1cor', 'ps'];
  const missingAbbr = PROMISED_ABBR.filter(a => !new RegExp("'" + a + "':").test(browse));
  if (!missingAbbr.length) ok('parser knows the abbreviations the guide names');
  else fail('guide promises abbreviations the parser lacks: ' + missingAbbr.join(', '));

  for (const claim of ['Matt', 'Mt', '1Cor13:4', 'Second Timothy', 'Song of Songs']) {
    if (guide.includes(claim)) continue;
    fail(`the guide no longer documents "${claim}" — this suite still enforces it`);
  }
  ok('the guide still documents the reference forms this suite enforces');

  // Every language must have the page, not just English.
  const LANGS = ['es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk',
    'pl','zh-Hans','zh-Hant','yue-Hant','vi','hu','hi','id','ro','nl'];
  const absent = LANGS.filter(l =>
    !fs.existsSync(path.join(REPO, 'guides', l, 'import-markdown-notes-jw-library.html')));
  if (!absent.length) ok(`the guide is published in all ${LANGS.length} languages`);
  else fail('guide missing for: ' + absent.join(', '));
}

section('The authoring guide shows files the reader can actually copy');
{
  // The companion page — how to *write* the .md file, as opposed to what the
  // importer accepts. Its whole subject is three sample files, so what needs
  // guarding is that they survive as samples: build_guides.section_body()
  // renders a ``` fence as <pre>, and a translation that drops the fence turns
  // the example back into run-on prose. Nothing else notices that, because the
  // page is still valid, still translated, and still passes 17_guides.js.
  const SLUG = 'write-markdown-notes-for-jw-library';
  const LANGS = ['es','pt','fr','de','it','ru','ja','ko','tl','sv','ceb','ar','he','uk',
    'pl','zh-Hans','zh-Hant','yue-Hant','vi','hu','hi','id','ro','nl'];
  const read = (l) => {
    const p = l === 'en' ? `guides/${SLUG}.html` : `guides/${l}/${SLUG}.html`;
    return fs.existsSync(path.join(REPO, p))
      ? fs.readFileSync(path.join(REPO, p), 'utf8') : null;
  };
  const samples = (h) => [...h.matchAll(/<pre class="code">([\s\S]*?)<\/pre>/g)].map((m) => m[1]);

  const en = read('en');
  if (!en) { fail('the English authoring guide was not built'); }
  else {
    const enSamples = samples(en);
    if (enSamples.length === 3) ok('English renders its 3 sample files as <pre> blocks');
    else fail(`English has ${enSamples.length} sample blocks, expected 3`);

    // A sample the reader copies has to carry the field name the parser
    // matches, and the English book name it recognises — those two are syntax,
    // not prose, so they must not have been translated along with the rest.
    const bad = [];
    for (const l of LANGS) {
      const h = read(l);
      if (!h) { bad.push(`${l}: page missing`); continue; }
      const s = samples(h);
      if (s.length !== enSamples.length) { bad.push(`${l}: ${s.length} samples`); continue; }
      const joined = s.join('\n');
      if (!joined.includes('publication: Matthew 26:39')) bad.push(`${l}: sample lost its reference line`);
      else if (!joined.includes('date: 2026-08-15')) bad.push(`${l}: sample lost its date field`);
    }
    if (!bad.length) ok(`sample files intact in all ${LANGS.length} translations`);
    else fail('sample files damaged — ' + bad.slice(0, 4).join(' | '));

    // The page tells people to type these; the parser has to accept them.
    const browse = fs.readFileSync(path.join(REPO, 'js/browse.js'), 'utf8');
    const TYPED = ['publication', 'title', 'date', 'tags'];
    const unread = TYPED.filter((k) => !new RegExp('\\b' + k + ":'").test(browse));
    if (!unread.length) ok('the parser accepts every field the samples type');
    else fail('samples type fields the parser ignores: ' + unread.join(', '));

    // Both directions of the pair, so neither becomes an island again.
    const imp = fs.readFileSync(path.join(REPO, 'guides/import-markdown-notes-jw-library.html'), 'utf8');
    if (en.includes('href="import-markdown-notes-jw-library"') && imp.includes(`href="${SLUG}"`))
      ok('the two Markdown guides link to each other');
    else fail('the Markdown guides are no longer cross-linked');
  }
}

section('Nothing is written until the reader agrees');
(async () => {
  const SQL = await initSqlJs({ locateFile: f => path.join(__dirname, 'node_modules/sql.js/dist/' + f) });
  const db = new SQL.Database();
  db.run(`
    CREATE TABLE Location (LocationId INTEGER PRIMARY KEY, BookNumber INTEGER, ChapterNumber INTEGER,
      DocumentId INTEGER, Track INTEGER, IssueTagNumber INTEGER, KeySymbol TEXT, MepsLanguage INTEGER,
      Type INTEGER, Title TEXT);
    CREATE TABLE UserMark (UserMarkId INTEGER PRIMARY KEY, ColorIndex INTEGER, LocationId INTEGER,
      StyleIndex INTEGER, UserMarkGuid TEXT, Version INTEGER);
    CREATE TABLE Note (NoteId INTEGER PRIMARY KEY, Guid TEXT, UserMarkId INTEGER, LocationId INTEGER,
      Title TEXT, Content TEXT, LastModified TEXT, Created TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
    CREATE TABLE Tag (TagId INTEGER PRIMARY KEY, Type INTEGER, Name TEXT);
    CREATE TABLE TagMap (TagMapId INTEGER PRIMARY KEY, PlaylistItemId INTEGER, LocationId INTEGER,
      NoteId INTEGER, TagId INTEGER, Position INTEGER);
    CREATE TABLE Bookmark (BookmarkId INTEGER PRIMARY KEY, LocationId INTEGER, PublicationLocationId INTEGER,
      Slot INTEGER, Title TEXT, Snippet TEXT, BlockType INTEGER, BlockIdentifier INTEGER);
    CREATE TABLE BlockRange (BlockRangeId INTEGER PRIMARY KEY, BlockType INTEGER, Identifier INTEGER,
      StartToken INTEGER, EndToken INTEGER, UserMarkId INTEGER);
    CREATE TABLE InputField (LocationId INTEGER, TextTag TEXT, Value TEXT, PRIMARY KEY (LocationId, TextTag));
    INSERT INTO Location (LocationId, BookNumber, ChapterNumber, IssueTagNumber, KeySymbol, MepsLanguage, Type)
      VALUES (1, 43, 3, 0, 'nwtsty', 0, 0);
  `);
  const bytes = db.export();
  db.close();
  const zip = new JSZip();
  zip.file('userData.db', bytes);
  zip.file('manifest.json', JSON.stringify({ version: 1 }));
  const buf = await zip.generateAsync({ type: 'arraybuffer' });

  const w = boot();
  w.alert = () => {};
  w.__openJwBrowse(buf);
  const t0 = Date.now();
  while (Date.now() - t0 < 10000 && !w.document.querySelector('.jb-list')) await new Promise(r => setTimeout(r, 50));

  // A reference for a chapter the backup does not have: opening the panel and
  // previewing it must not create the Location — the preview used to do that
  // just by looking.
  const notes = await w.__jwMdImport.readFiles([
    new w.File(['---\ntitle: New chapter\nbook: Matthew\nchapter: 26\nverse: 39\n---\nBody'], 'a.md'),
  ]);
  const importBtn = Array.from(w.document.querySelectorAll('.jb-md-btn'))
    .find(b => /import markdown/i.test(b.textContent || ''));
  if (importBtn) {
    importBtn.click();
    const panel = w.document.querySelector('.jbs-overlay');
    if (panel) ok('the import panel opens without writing anything');
    else fail('import panel did not open');
    if (panel) panel.remove();
  } else fail('import button missing');

  // Now actually import and check it landed, so the read-only preview has not
  // broken the write path.
  const res = w.__jwMdImport.importNotes(notes);
  if (res.added === 1 && res.anchored === 1) ok('the note imports and anchors once confirmed');
  else fail('import after preview wrong: ' + JSON.stringify(res));

  // An unrecognised book must not reach the database as a location.
  const unknown = await w.__jwMdImport.readFiles([
    new w.File(['---\ntitle: Odd\npub: Enoch 3:5\n---\nBody'], 'b.md'),
  ]);
  const res2 = w.__jwMdImport.importNotes(unknown);
  if (res2.added === 1 && res2.anchored === 0) ok('a flagged note imports unanchored, never onto a guess');
  else fail('unrecognised book was anchored: ' + JSON.stringify(res2));

  console.log(failures ? `\n${failures} failure(s)` : '\nAll Markdown tolerance checks passed');
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });

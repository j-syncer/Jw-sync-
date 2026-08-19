// Independent audit of the .jwlibrary the Conflict Reviewer hands back:
// is the SQLite valid, and is manifest.json still describing it truthfully?
const path=require('path'), fs=require('fs'), crypto=require('crypto');
const {JSDOM}=require('jsdom'); const JSZip=require('jszip'); const initSqlJs=require('sql.js');
const {inlineModules}=require('/home/user/Jw-sync-/tests/helpers/page-source');
const REPO='/home/user/Jw-sync-';
const SQL_OPTS={locateFile:f=>path.join(REPO,'tests/node_modules/sql.js/dist/'+f)};
const sha=b=>crypto.createHash('sha256').update(Buffer.from(b)).digest('hex');

async function buildBackup(SQL,notes){
  const db=new SQL.Database();
  db.run(`CREATE TABLE Note(NoteId INTEGER PRIMARY KEY,Guid TEXT,UserMarkId INTEGER,LocationId INTEGER,
    Title TEXT,Content TEXT,LastModified TEXT,Created TEXT,BlockType INTEGER,BlockIdentifier INTEGER);`);
  db.run(`CREATE TABLE LastModified(LastModified TEXT);`);
  db.run(`INSERT INTO LastModified VALUES('2024-01-01T00:00:00Z')`);
  notes.forEach((n,i)=>db.run('INSERT INTO Note (NoteId,Guid,Title,Content,LastModified) VALUES (?,?,?,?,?)',
    [i+1,n.guid,n.title,n.content,n.lastMod]));
  const bytes=db.export(); db.close();
  const zip=new JSZip();
  zip.file('userData.db',bytes);
  // A REALISTIC manifest — the kind JW Library actually writes and validates.
  zip.file('manifest.json',JSON.stringify({name:'UserdataBackup',creationDate:'2024-01-01',
    version:1,type:0,userDataBackup:{lastModifiedDate:'2024-01-01T00:00:00Z',deviceName:'Phone',
    databaseName:'userData.db',hash:sha(bytes),schemaVersion:'16'}}));
  return zip.generateAsync({type:'arraybuffer'});
}

(async()=>{
  const SQL=await initSqlJs(SQL_OPTS);
  const G='g1';
  const phone={guid:G,title:'Faith',content:'<p>Shared line.</p><p>Phone edit.</p>',lastMod:'2024-03-01 09:00:00'};
  const tablet={guid:G,title:'Faith',content:'<p>Shared line.</p><p>Tablet edit.</p>',lastMod:'2024-04-15 18:00:00'};
  const [pB,tB,mB]=await Promise.all([buildBackup(SQL,[phone]),buildBackup(SQL,[tablet]),buildBackup(SQL,[phone])]);

  const html=inlineModules(fs.readFileSync(REPO+'/beta/index.html','utf8'),REPO+'/beta/index.html');
  const block=html.match(/<!-- ── Merge Conflict Reviewer \(v2\.11\.0\) ─[\s\S]*?<!-- ── End Merge Conflict Reviewer ─[─]*\s*-->/)[0];
  const dom=new JSDOM(`<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>${block}</body></html>`,
    {url:'https://jwsync.org/beta/',runScripts:'dangerously',pretendToBeVisual:true});
  const win=dom.window, doc=win.document;
  win.localStorage.setItem('jwsync_lang','en');
  win.JSZip=JSZip; win.initSqlJs=()=>initSqlJs(SQL_OPTS);
  win.eval(fs.readFileSync(REPO+'/js/jwlibrary-manifest.js','utf8'));   // both index.html files load this
  win.URL.createObjectURL=()=>'blob:x';
  win.fetch=()=>Promise.resolve({arrayBuffer:async()=>mB.slice(0)});
  const input=doc.createElement('input'); input.type='file'; input.setAttribute('accept','.jwlibrary');
  doc.body.appendChild(input);
  const fl=[{name:'phone.jwlibrary',size:pB.byteLength,arrayBuffer:async()=>pB},
            {name:'tablet.jwlibrary',size:tB.byteLength,arrayBuffer:async()=>tB}];
  Object.defineProperty(input,'files',{get:()=>fl});

  const p=win.__jwConflictReview({blobUrl:'blob:merged'});
  let overlay=null; for(let i=0;i<150&&!overlay;i++){overlay=doc.getElementById('jw-conflict-overlay');await new Promise(r=>setTimeout(r,40));}
  overlay.querySelector('.jcr-compare-btn').click();
  Array.from(overlay.querySelectorAll('.jcr-cmp-act'))[2].click();   // Keep both sides
  overlay.querySelector('.jcr-use-combined').click();
  overlay.querySelector('.jcr-btn-primary').click();
  const res=await p;

  console.log('\n=== AUDIT OF THE RETURNED .jwlibrary ===');
  const zip=await JSZip.loadAsync(res.buffer);
  console.log('entries:', Object.keys(zip.files).join(', '));
  const dbBytes=await zip.file('userData.db').async('uint8array');

  // 1. Is the SQLite intact?
  const out=new SQL.Database(dbBytes);
  console.log('integrity_check :', out.exec('PRAGMA integrity_check')[0].values[0][0]);
  const note=out.exec('SELECT Content FROM Note WHERE Guid=?',[G])[0].values[0][0];
  console.log('combined Content:', JSON.stringify(note));
  console.log('both sides kept :', note.includes('Phone edit.')&&note.includes('Tablet edit.'));
  out.close();

  // 2. Does manifest.json still describe THIS database?
  const mf=zip.file('manifest.json');
  if(!mf){ console.log('manifest.json : *** MISSING ***'); }
  else{
    const m=JSON.parse(await mf.async('string'));
    const stated=m.userDataBackup&&m.userDataBackup.hash, actual=sha(dbBytes);
    console.log('manifest hash  :', stated);
    console.log('actual db hash :', actual);
    console.log(stated===actual ? 'HASH MATCHES — JW Library will restore this file'
                                : '*** HASH STALE — JW Library will SILENTLY REFUSE this file ***');
  }
  dom.window.close();
})().catch(e=>{console.error('CRASH',e);process.exit(2);});

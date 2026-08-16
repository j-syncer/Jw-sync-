#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_backup_manifest.py — make every export a backup JW Library will restore.

Reported on the community page: a file that has been through the Library Doctor,
or through the Study Explorer's editor / Markdown import, will not restore into
JW Library. The app flickers and returns to the same screen — no confirmation
prompt, no error. Merged files restore normally.

A .jwlibrary carries manifest.json describing the database beside it, including
userDataBackup.hash, the SHA-256 of userData.db. JW Library validates it and
refuses the file if it does not match, saying nothing at all. Three of our four
export paths were writing files that could not pass:

  js/browse.js     re-zipped the edited database on its own — the output had NO
                   manifest.json whatsoever
  js/doctor.js     kept the original manifest, hash still pointing at the
                   database the file used to contain
  js/receive.js    same, when adopting shared notes into a backup
  js/merge-worker  same stale hash; this is the path users report as working,
                   so the field is evidently not always fatal — but a stale
                   hash is never correct, and it is fixed here too

The fix is one shared helper, js/jwlibrary-manifest.js, that every path now
calls: it writes the database into the zip, recomputes the hash, refreshes
lastModifiedDate, and updates the LastModified table inside the database. It
edits only the fields that have gone stale — an existing manifest keeps
everything else, because the parts we do not understand are the parts we must
not rewrite.

Idempotent; mirrors js/ to beta/js/ as 15_parity.js requires.
"""
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(p):
    return io.open(os.path.join(REPO, p), encoding="utf-8").read()


def write(p, c):
    io.open(os.path.join(REPO, p), "w", encoding="utf-8").write(c)


def sub1(c, old, new, where, done_marker=None):
    if (done_marker or new) in c:
        return c, 0
    n = c.count(old)
    if n != 1:
        sys.exit("ABORT %s: anchor x%d: %s" % (where, n, old[:90]))
    return c.replace(old, new, 1), 1


# ── js/browse.js ────────────────────────────────────────────────────────────
# The Explorer threw the uploaded zip away and kept only the database, so it had
# nothing to write a manifest from. Keep the zip.

BROWSE_KEEP_OLD = """    new JSZip().loadAsync(file).then(function(zip){
      var dbName = Object.keys(zip.files).find(function(n){ return /userdata\\.db$/i.test(n); });
      if(!dbName) throw new Error('userData.db not found in backup.');
      return zip.files[dbName].async('uint8array');
    }).then(function(bytes){"""

BROWSE_KEEP_NEW = """    new JSZip().loadAsync(file).then(function(zip){
      var dbName = Object.keys(zip.files).find(function(n){ return /userdata\\.db$/i.test(n); });
      if(!dbName) throw new Error('userData.db not found in backup.');
      // Hold on to the whole archive, not just the database. Everything else in
      // it — manifest.json above all — has to travel with the file we hand back,
      // or JW Library silently refuses to restore it.
      state.zip = zip; state.dbKey = dbName;
      return zip.files[dbName].async('uint8array');
    }).then(function(bytes){"""

BROWSE_EXPORT_OLD = """    try{
      var bytes=state.db.export();
      var zip=new JSZip();
      zip.file('userData.db', bytes);
      zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}}).then(function(blob){
        var url=URL.createObjectURL(blob);"""

BROWSE_EXPORT_NEW = """    try{
      if(window.__jwFinalizeBackup) window.__jwFinalizeBackup.touchLastModified(state.db);
      var bytes=state.db.export();
      var zip=state.zip||new JSZip();
      var key=state.dbKey||'userData.db';
      finalizeZip(zip, key, bytes, ' (Edited)').then(function(z){
        // application/octet-stream, not JSZip's application/zip, so iOS Safari
        // saves it as .jwlibrary — the same wrapping the merge tool uses.
        return z.generateAsync({type:'arraybuffer',compression:'DEFLATE',compressionOptions:{level:6}});
      }).then(function(buf){
        var blob=new Blob([buf],{type:'application/octet-stream'});
        var url=URL.createObjectURL(blob);"""

BROWSE_EXTRACT_OLD = """      var zip=new JSZip(); zip.file('userData.db', bytes);
      zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}}).then(function(blob){
        var url=URL.createObjectURL(blob);
        var base=(state.fileName?state.fileName.replace(/\\.jwlibrary$/i,''):'backup');
        var a=document.createElement('a'); a.href=url; a.download='extracted_'+base+'.jwlibrary';"""

BROWSE_EXTRACT_NEW = """      var zip=state.zip||new JSZip();
      var key=state.dbKey||'userData.db';
      finalizeZip(zip, key, bytes, ' (Extract)').then(function(z){
        return z.generateAsync({type:'arraybuffer',compression:'DEFLATE',compressionOptions:{level:6}});
      }).then(function(buf){
        var blob=new Blob([buf],{type:'application/octet-stream'});
        var url=URL.createObjectURL(blob);
        var base=(state.fileName?state.fileName.replace(/\\.jwlibrary$/i,''):'backup');
        var a=document.createElement('a'); a.href=url; a.download='extracted_'+base+'.jwlibrary';"""

BROWSE_HELPER_ANCHOR = "  function exportDb(){"
BROWSE_HELPER = """  // Everything that writes a .jwlibrary goes through js/jwlibrary-manifest.js,
  // which recomputes manifest.json's hash to match the database beside it. A
  // file whose hash is stale — or which has no manifest at all, which is what
  // this module used to produce — is refused by JW Library without a word.
  function finalizeZip(zip, key, bytes, suffix){
    if(window.__jwFinalizeBackup) return window.__jwFinalizeBackup(zip, key, bytes, {nameSuffix:suffix});
    zip.file(key, bytes);
    return Promise.resolve(zip);
  }
"""

# extractByDate works on a clone, so its LastModified needs the same touch.
BROWSE_EXTRACT_TOUCH_OLD = """      var bytes=clone.export();
      try{ clone.close(); }catch(_){}"""
BROWSE_EXTRACT_TOUCH_NEW = """      if(window.__jwFinalizeBackup) window.__jwFinalizeBackup.touchLastModified(clone);
      var bytes=clone.export();
      try{ clone.close(); }catch(_){}"""


def patch_browse():
    c = read("js/browse.js")
    orig = c
    c, _ = sub1(c, BROWSE_KEEP_OLD, BROWSE_KEEP_NEW, "browse.js", "state.zip = zip;")
    c, _ = sub1(c, BROWSE_HELPER_ANCHOR, BROWSE_HELPER + BROWSE_HELPER_ANCHOR,
                "browse.js", "function finalizeZip(")
    c, _ = sub1(c, BROWSE_EXPORT_OLD, BROWSE_EXPORT_NEW, "browse.js", "finalizeZip(zip, key, bytes, ' (Edited)')")
    c, _ = sub1(c, BROWSE_EXTRACT_TOUCH_OLD, BROWSE_EXTRACT_TOUCH_NEW, "browse.js",
                "touchLastModified(clone)")
    c, _ = sub1(c, BROWSE_EXTRACT_OLD, BROWSE_EXTRACT_NEW, "browse.js", "finalizeZip(zip, key, bytes, ' (Extract)')")
    if c != orig:
        write("js/browse.js", c)
        print("js/browse.js: keeps the archive, writes a matching manifest")
    else:
        print("js/browse.js: already patched")


# ── js/doctor.js ────────────────────────────────────────────────────────────
DOCTOR_OLD = """  function exportCleaned(st){
    var bytes=st.db.export();
    st.zip.file(st.dbKey, bytes);
    var mf=st.zip.file('manifest.json');
    var p = mf ? mf.async('string').then(function(s){
      try{
        var raw=JSON.parse(s);
        raw.creationDate=new Date().toISOString();
        raw.name=(raw.name||'Backup')+' (Cleaned)';
        st.zip.file('manifest.json', JSON.stringify(raw,null,2));
      }catch(_){}
    }) : Promise.resolve();
    return p.then(function(){"""

DOCTOR_NEW = """  function exportCleaned(st){
    // The manifest's hash has to be recomputed from the cleaned database.
    // Leaving the original in place produced a file JW Library refuses to
    // restore, silently — see js/jwlibrary-manifest.js.
    if(window.__jwFinalizeBackup) window.__jwFinalizeBackup.touchLastModified(st.db);
    var bytes=st.db.export();
    var p = window.__jwFinalizeBackup
      ? window.__jwFinalizeBackup(st.zip, st.dbKey, bytes, {nameSuffix:' (Cleaned)'}).then(function(){})
      : Promise.resolve(st.zip.file(st.dbKey, bytes)).then(function(){});
    return p.then(function(){"""


def patch_doctor():
    c = read("js/doctor.js")
    c2, n = sub1(c, DOCTOR_OLD, DOCTOR_NEW, "doctor.js", "__jwFinalizeBackup(st.zip")
    if n:
        write("js/doctor.js", c2)
        print("js/doctor.js: manifest hash recomputed on export")
    else:
        print("js/doctor.js: already patched")


# ── js/receive.js ───────────────────────────────────────────────────────────
RECEIVE_OLD = """              var out=db.export(); db.close(); zip.file(key, out);
              return zip.generateAsync({type:'arraybuffer',compression:'DEFLATE'}).then(function(buf){ return {buffer:buf, added:res.added, highlights:res.highlights, overlaps:conflicts.length, imported:res.imported}; });"""

RECEIVE_NEW = """              if(window.__jwFinalizeBackup) window.__jwFinalizeBackup.touchLastModified(db);
              var out=db.export(); db.close();
              // manifest.json has to describe the database we just wrote, not
              // the one that arrived — see js/jwlibrary-manifest.js.
              var ready = window.__jwFinalizeBackup
                ? window.__jwFinalizeBackup(zip, key, out, {nameSuffix:' (Updated)'})
                : Promise.resolve(zip.file(key, out));
              return ready.then(function(){ return zip.generateAsync({type:'arraybuffer',compression:'DEFLATE'}); }).then(function(buf){ return {buffer:buf, added:res.added, highlights:res.highlights, overlaps:conflicts.length, imported:res.imported}; });"""


def patch_receive():
    c = read("js/receive.js")
    c2, n = sub1(c, RECEIVE_OLD, RECEIVE_NEW, "receive.js", "__jwFinalizeBackup(zip, key, out")
    if n:
        write("js/receive.js", c2)
        print("js/receive.js: manifest hash recomputed when adopting notes")
    else:
        print("js/receive.js: already patched")


# ── js/merge-worker.js ──────────────────────────────────────────────────────
WORKER_IMPORT_OLD = """importScripts(
  'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'
);"""
WORKER_IMPORT_NEW = """importScripts(
  'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/sql-wasm.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js'
);
// Same rules as every other path that writes a .jwlibrary; resolved against
// this worker's own URL, so it loads from js/ on both sites.
importScripts('jwlibrary-manifest.js');"""

WORKER_EXPORT_OLD = """  const exportedDb = a.export();
  a.close();
  a = null;

  o.file(Object.keys(o.files).find(k => /userdata\\.db$/i.test(k)), exportedDb);
  const zipBuf = await o.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });"""

WORKER_EXPORT_NEW = """  if (self.__jwFinalizeBackup) self.__jwFinalizeBackup.touchLastModified(a);
  const exportedDb = a.export();
  a.close();
  a = null;

  const outKey = Object.keys(o.files).find(k => /userdata\\.db$/i.test(k));
  // manifest.json must describe the merged database, hash included.
  if (self.__jwFinalizeBackup) await self.__jwFinalizeBackup(o, outKey, exportedDb);
  else o.file(outKey, exportedDb);
  const zipBuf = await o.generateAsync({ type: 'arraybuffer', compression: 'DEFLATE' });"""


def patch_worker():
    c = read("js/merge-worker.js")
    orig = c
    c, _ = sub1(c, WORKER_IMPORT_OLD, WORKER_IMPORT_NEW, "merge-worker.js", "importScripts('jwlibrary-manifest.js')")
    c, _ = sub1(c, WORKER_EXPORT_OLD, WORKER_EXPORT_NEW, "merge-worker.js", "__jwFinalizeBackup(o, outKey")
    if c != orig:
        write("js/merge-worker.js", c)
        print("js/merge-worker.js: manifest hash recomputed on merge")
    else:
        print("js/merge-worker.js: already patched")


# ── the pages ───────────────────────────────────────────────────────────────
def patch_pages():
    for rel in ("index.html", "beta/index.html"):
        c = read(rel)
        c2, n = sub1(c, '<script src="js/receive.js" defer></script>',
                     '<script src="js/jwlibrary-manifest.js" defer></script>\n'
                     '<script src="js/receive.js" defer></script>', rel,
                     'js/jwlibrary-manifest.js')
        if n:
            write(rel, c2)
            print("%s: loads js/jwlibrary-manifest.js" % rel)
        else:
            print("%s: already patched" % rel)


if __name__ == "__main__":
    patch_browse()
    patch_doctor()
    patch_receive()
    patch_worker()
    patch_pages()
    # Shared tool-layer files ship to both sites.
    for f in ("browse.js", "doctor.js", "receive.js", "merge-worker.js", "jwlibrary-manifest.js"):
        write(os.path.join("beta", "js", f), read(os.path.join("js", f)))
    print("beta/js: mirrored")

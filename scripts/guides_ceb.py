# -*- coding: utf-8 -*-
"""Cebuano translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → backup (ang .jwlibrary nga file)
  Personal Study            → Personal nga Pagtuon
  Backup and Restore        → Backup ug Pagpasig-uli
  restore                   → ipasig-uli
  merge                     → paghiusa / hiusahon
  notes                     → mga nota
  highlights                → mga highlight
  bookmarks                 → mga bookmark
  tags                      → mga tag
  Study Explorer            → Study Explorer
  Library Doctor            → Library Doctor
  Reading Companion         → Reading Companion
  Resurface                 → Resurface
  Study Map                 → Study Map
  Study Stats               → Study Stats
  Conflict Reviewer         → Conflict Reviewer
  meeting                   → tigom
  congregation              → kongregasyon
  assembly / convention     → asembliya / kombensiyon
"""

GUIDES_CEB = {}

GUIDES_CEB["merge-jw-library-backups"] = {
    "title": "Unsaon paghiusa ang mga backup sa JW Library gikan sa duha ka device",
    "h1": "Unsaon paghiusa ang mga backup sa JW Library gikan sa duha ka device",
    "description": "Hiusaha ang mga nota, highlight, bookmark ug tag gikan sa duha o labaw pa "
                   "nga backup sa JW Library ngadto sa usa ka .jwlibrary nga file — libre, "
                   "pribado, sulod mismo sa imong browser.",
    "intro": [
        "Kon magtuon ka sa kapin sa usa ka device — cellphone sa Kingdom Hall, tablet sa "
        "balay — matag usa maghupot ug kaugalingong mga nota ug highlight. Dili kini "
        "mahiusa sa Backup ug Pagpasig-uli sa JW Library: ang pagpasig-uli sa usa ka backup "
        "mopuli sa tanan nga anaa sa device ug mapapas ang gibuhat sa pikas.",
        "Gisulbad kini sa JW Sync. Basahon niini ang duha (o labaw pa) nga .jwlibrary nga "
        "backup ug hiusahon ang mga nota, highlight, bookmark ug tag sa tanan ngadto sa usa ka "
        "bag-ong backup. Ang paghiusa mahitabo sa sulod mismo sa imong browser — ang imong "
        "mga file wala gayod i-upload sa bisan unsang server, busa magpabiling pribado ang "
        "imong mga nota sa personal nga pagtuon.",
    ],
    "steps": [
        ("Paghimo ug backup sa matag device",
         "Sa JW Library, ablihi ang Personal nga Pagtuon, i-tap ang tulo-ka-tuldok nga menu, "
         "pilia ang Backup ug Pagpasig-uli, dayon Paghimo ug backup. Buhata kini sa matag "
         "device. Ang matag usa maghatag ug .jwlibrary nga file."),
        ("Ablihi ang JW Sync",
         "Adto sa jwsync.org sa bisan unsang browser — sa cellphone, tablet o kompyuter. "
         "Walay kinahanglang i-install."),
        ("I-load ang duha ka backup nga file",
         "I-drop (o pilia) ang mga .jwlibrary nga file. Basahon kini sa JW Sync sa imong "
         "device mismo."),
        ("Susiha ang preview sa dili pa maghiusa",
         "Sa dili pa masulat ang bisan unsa, ipakita sa preview kon unsa gyoy hiusahon. Kon "
         "lahi ang pag-edit sa samang nota sa matag device, ipakita sa Conflict Reviewer ang "
         "duha ka bersiyon nga magtapad, uban ang kalainan pulong-por-pulong, aron ikaw ang "
         "mopili kon hain ang huptan — o pasagdi nga ang “Isugyot ang labing maayo” ang "
         "mopili para nimo."),
        ("I-download ang gihiusang file ug ipasig-uli kini",
         "I-download ang gihiusang .jwlibrary nga file, dayon ipasig-uli kini sa matag device "
         "pinaagi sa Backup ug Pagpasig-uli → Ipasig-uli. Kompleto na ug pareho ang library "
         "sa duha ka device."),
    ],
    "sections": [
        ("Unsa may gihiusa?",
         "Mga nota, highlight, bookmark, tag ug ang mga koneksiyon niini. Awtomatikong "
         "mamatikdan ang mga duplicate, busa ang pagpasig-uli sa gihiusang file wala gayod "
         "magdoble ug bisan unsa. Managsama ang format sa mga backup gikan sa Android, "
         "iPhone, iPad ug sa Windows app, busa gawasnon silang maghiusa."),
        ("Luwas ba kini?",
         "Wala gayod usba sa paghiusa ang imong orihinal nga mga file — maghimo kini ug "
         "bag-ong backup, busa magpabiling buo ang mga orihinal isip andam nga kopya. Ug "
         "tungod kay sa browser modagan ang tanan, walay datos nga mobiya sa imong device."),
    ],
    "faq": [
        ("Mahimo bang hiusahon ang kapin sa duha ka backup?",
         "Oo — i-load ang tanang .jwlibrary nga file, kutob sa gidaghanon sa imong device. "
         "Hiusahon silang tanan ngadto sa usa ka backup."),
        ("Magdoble ba ang mga nota kon hiusahon?",
         "Dili. Mamatikdan ang managsamang mga nota, highlight ug bookmark, ug usa ra ang "
         "huptan. Ang tinuod nga magkalahing bersiyon sa samang nota motungha sa Conflict "
         "Reviewer aron ikaw ang modesisyon."),
        ("Molihok ba kini tali sa Android ug iPhone?",
         "Oo. Managsama ang .jwlibrary nga format sa Android, iOS, iPadOS ug Windows, busa "
         "ang mga backup gikan sa lainlaing plataporma maghiusa nga walay conversion."),
    ],
}

GUIDES_CEB["sync-jw-library-multiple-devices"] = {
    "title": "Unsaon pag-sync ang JW Library tali sa daghang device",
    "h1": "Unsaon paghupot ug pareho nga JW Library sa daghang device",
    "description": "Walay built-in nga sync ang JW Library tali sa mga device. Ania ang "
                   "simple ug pribadong rutina aron magpabiling pareho ang mga nota, "
                   "highlight ug bookmark sa imong cellphone, tablet ug kompyuter.",
    "intro": [
        "Wala i-sync sa JW Library ang datos sa personal nga pagtuon tali sa mga device — "
        "walay account nga modala sa imong mga nota gikan sa cellphone ngadto sa tablet. Ang "
        "opisyal nga paagi mao ang Backup ug Pagpasig-uli, ug ang pagpasig-uli mopuli sa "
        "tibuok datos sa device. Busa unsaon paghupot ug pareho nga duha o tulo ka device nga "
        "walay mawala?",
        "Ang tubag maoy usa ka mubo nga rutina: hiusahon, dayon ipasig-uli. Kon buhaton "
        "matag semana o matag bulan, mokabat kini ug duha ka minuto ug magpabilin ang kompleto "
        "nimong library sa matag device.",
    ],
    "steps": [
        ("I-backup ang matag device",
         "Sa matag usa: Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug "
         "Pagpasig-uli → Paghimo ug backup. Makakuha kag usa ka .jwlibrary nga file matag "
         "device."),
        ("Hiusaha ang mga backup sa jwsync.org",
         "I-load ang tanang file. Hiusahon sa JW Sync ang mga nota, highlight, bookmark ug "
         "tag sa matag device ngadto sa usa ka gihiusang .jwlibrary nga file — sa browser "
         "mismo, walay gi-upload."),
        ("Ipasig-uli ang gihiusang file sa matag device",
         "Backup ug Pagpasig-uli → Ipasig-uli, pilia ang gihiusang file. Pareho na ug "
         "kompleto ang tanang device."),
        ("Papahinumdomi ka sa JW Sync",
         "I-on ang pahinumdom sa pag-sync (matag semana o matag bulan) sa JW Sync ug "
         "pahibaloon ka niini kon panahon na sa pagsubli. Mahinumdom usab kini sa imong mga "
         "natipigang device, busa mas paspas ang matag sunod nga hugna."),
    ],
    "sections": [
        ("Nganong dili na lang ipasig-uli ang pinakabag-ong backup?",
         "Kay ang “pinakabag-o” usa ra ka device ang gipakita. Kon sa samang semana nagnota "
         "ka sa tigom gikan sa cellphone ug nagnota sa pagtuon gikan sa tablet, ang matag "
         "backup naay sulod nga wala sa pikas. Ang pagpasig-uli sa usa ibabaw sa lain "
         "mawad-an nimo sa katunga sa imong gibuhat. Ang paghiusa maoy naghimo niining "
         "rutinaha nga luwas."),
        ("Unsa ka subsob ako mag-sync?",
         "Ipahiuyon sa imong paagi sa pagtuon. Duha ka aktibong device nga adlaw-adlaw "
         "gamiton: komportable ang kausa sa usa ka semana. Tablet nga mogawas lang sa mga "
         "tigom: igo na ang kausa sa usa ka bulan. Ang paghulat ug dugay nagpasabot lang nga "
         "mas daghan ang hiusahon — walay mawala tali sa mga hugna."),
    ],
    "faq": [
        ("Modagan ba ang JW Sync sa background?",
         "Dili — usa kini ka web page, dili gi-install nga serbisyo. Walay nagsusi sa imong "
         "mga device. Ikaw ang modagan sa rutina kon kanus-a nimo gusto; ang opsiyonal nga "
         "pahinumdom usa lang ka pahibalo."),
        ("Mahimo bang i-sync ang tulo o labaw pa ka device?",
         "Oo. I-backup ang matag usa, i-load ang tanang file, hiusaha kausa, ug ipasig-uli "
         "ang gihiusang file sa tanan."),
    ],
}

GUIDES_CEB["transfer-jw-library-notes-new-phone"] = {
    "title": "Unsaon pagbalhin ang mga nota sa JW Library ngadto sa bag-ong cellphone",
    "h1": "Unsaon pagbalhin ang mga nota sa JW Library ngadto sa bag-ong cellphone",
    "description": "Lakang-lakang: dad-a ang tanan nimong nota, highlight, bookmark ug tag sa "
                   "JW Library ngadto sa bag-ong cellphone gamit ang .jwlibrary nga backup — "
                   "ug unsaon paghiusa kon naay nota na sa bag-ong cellphone.",
    "intro": [
        "Ang mga tool sa pagbalhin ug cellphone modala sa mga app ug hulagway, apan dili "
        "kasaligan nga madala nila ang datos sa personal nga pagtuon sa JW Library. Ang "
        "kasaligang paagi aron madala ang imong mga nota, highlight, bookmark ug tag ngadto "
        "sa bag-ong cellphone mao ang backup nga file mismo sa JW Library — pipila lang ka "
        "minuto ug molihok kini tali sa lainlaing plataporma.",
    ],
    "steps": [
        ("Paghimo ug backup sa daang cellphone",
         "Ablihi ang JW Library → Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug "
         "Pagpasig-uli → Paghimo ug backup. Motipig kini ug .jwlibrary nga file nga naglangkob "
         "sa tanan nimong datos sa pagtuon."),
        ("Balhina ang file ngadto sa bag-ong cellphone",
         "I-email kini sa imong kaugalingon, o gamita ang Google Drive, iCloud, AirDrop o USB "
         "cable. Gamay ra ang file — kasagaran pipila ka megabyte."),
        ("Ipasig-uli sa bag-ong cellphone",
         "I-install ang JW Library, dayon Personal nga Pagtuon → Backup ug Pagpasig-uli → "
         "Ipasig-uli, ug pilia ang .jwlibrary nga file. Motungha ang tanang nota, highlight, "
         "bookmark ug tag."),
    ],
    "sections": [
        ("Naa na kay nota sa bag-ong cellphone? Hiusaha, ayaw i-overwrite",
         "Ang pagpasig-uli mopuli sa unsay anaa sa device. Kon dugay-dugay na nimong gamiton "
         "ang bag-ong cellphone ug naay kaugalingong mga nota, ayaw ipasig-uli ibabaw niini — "
         "i-backup pod ang bag-ong cellphone, hiusaha ang daan ug bag-ong backup ngadto sa usa "
         "ka file sa jwsync.org (libre, sa browser, walay gi-upload) ug ipasig-uli ang "
         "gihiusang file. Mahuptan nimo ang duha ka set sa nota."),
        ("Usa ka komon nga suliran sa iPhone",
         "Kon moabot sa iPhone ang backup nga file nga giilisan ug .zip, ibalik kini sa "
         ".jwlibrary sa dili pa magpasig-uli — maayo ra ang sulod; ang extension lang ang "
         "nausab sa dalan."),
    ],
    "faq": [
        ("Mabalhin ba pod ang akong na-download nga mga publikasyon?",
         "Ang backup nagdala sa imong datos sa personal nga pagtuon — mga nota, highlight, "
         "bookmark, tag ug playlist. Ma-download lang pag-usab ang mga publikasyon sa bag-ong "
         "cellphone."),
        ("Importante ba kon lahi ang bersiyon sa Android sa mga cellphone?",
         "Dili. Managsama ang .jwlibrary nga format bisan asa, apil tali sa mga bersiyon sa "
         "Android ug tali sa Android ug iPhone."),
    ],
}

GUIDES_CEB["jw-library-android-to-iphone"] = {
    "title": "Balhina ang JW Library gikan Android ngadto iPhone (buo ang mga nota)",
    "h1": "Pagbalhin sa JW Library gikan Android ngadto iPhone o iPad — walay nota nga mawala",
    "description": "Managsama ang .jwlibrary nga format sa backup sa Android ug iOS. Unsaon "
                   "pagbalhin ang imong mga nota, highlight ug bookmark tali sa mga "
                   "plataporma — ug unsaon paghiusa kon naay nota ang duha ka device.",
    "intro": [
        "Ang pag-ilis ug plataporma mao ang panahon nga mahadlok ang daghan nga mawala ang "
        "tuig-tuig nga nota sa pagtuon — gilaktawan gayod sa mga app sa pagbalhin gikan "
        "Android ngadto iPhone ang datos sa JW Library. Ang maayong balita: managsama ang "
        "format sa backup sa JW Library sa Android, iPhone, iPad ug Windows, busa ang "
        "pag-ilis ug plataporma backup lang, pagbalhin ug file, ug pagpasig-uli.",
    ],
    "steps": [
        ("Pag-backup sa Android nga cellphone",
         "JW Library → Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug Pagpasig-uli "
         "→ Paghimo ug backup. Itipig ang .jwlibrary nga file."),
        ("Ipadala ang file ngadto sa iPhone o iPad",
         "Email, Google Drive, iCloud Drive — bisan unsa nga makabalhin ug file. Kon ilisan "
         "kini sa iOS ug .zip sa dalan, ibalik kini sa .jwlibrary."),
        ("Ipasig-uli sa bag-ong device",
         "I-install ang JW Library, mag-sign in, dayon Backup ug Pagpasig-uli → Ipasig-uli ug "
         "pilia ang file. Moabot ang tanang nota, highlight, bookmark, tag ug playlist."),
    ],
    "sections": [
        ("Kon naay nota na ang iPhone",
         "Ang pagpasig-uli mopuli sa datos sa device. Kon naay kaugalingong mga nota na ang "
         "bag-ong device, i-backup pod kini ug hiusaha una ang duha ka backup ngadto sa usa ka "
         "file sa jwsync.org — hiusahon sa paghiusa ang duha ka library sa imong browser, "
         "walay gi-upload — dayon ipasig-uli ang gihiusang file. Walay mawala sa bisan hain "
         "nga kilid."),
        ("Molihok ang samang lakang sa bisan unsang direksiyon",
         "Gikan iPhone ngadto Android, gikan Android ngadto Android, sa pagdugang ug iPad "
         "isip ikaduhang device sa pagtuon, o sa pagbalhin ngadto sa Windows app — ang backup "
         "nga file mao ang komon nga pinulongan nilang tanan."),
    ],
    "faq": [
        ("Kinahanglan ba nako ug kompyuter alang niini?",
         "Dili. Ang tibuok pagbalhin mahimong buhaton gikan sa cellphone ngadto sa cellphone "
         "pinaagi sa email o cloud drive."),
        ("Mapreserbar ba ang mga kolor sa akong highlight?",
         "Oo — magpabilin ang kolor sa mga highlight, ang tag sa mga nota, ug ang lugar sa "
         "mga bookmark."),
    ],
}

GUIDES_CEB["backup-jw-library"] = {
    "title": "Unsaon pag-backup sa JW Library sa hustong paagi",
    "h1": "Unsaon pag-backup sa JW Library sa hustong paagi",
    "description": "Usa ka rutina nga 30 segundos ra nga manalipod sa tuig-tuig nga nota, "
                   "highlight ug bookmark sa imong pagtuon sa JW Library — ug ang komon nga "
                   "sayop nga nakalit sa daghan.",
    "intro": [
        "Ang husto nga backup sa JW Library mokabat ug tunga sa minuto ug manalipod sa "
        "tuig-tuig nga natigom nga pagtuon. Halos parehas ang sinugdanan sa mga sugilanon bahin "
        "sa nawad-ang datos: walay bag-o nga .jwlibrary nga file dihang nawala, na-reset o "
        "gipulihan ang cellphone.",
    ],
    "steps": [
        ("Paghimo sa backup",
         "Ablihi ang JW Library → Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug "
         "Pagpasig-uli → Paghimo ug backup. Maghimo kini ug .jwlibrary nga file nga naay matag "
         "nota, highlight, bookmark ug tag."),
        ("Itipig kini sa gawas sa cellphone",
         "I-email kini sa imong kaugalingon, o itipig sa Google Drive, iCloud o OneDrive. Ang "
         "backup nga anaa ra sa cellphone mawala uban sa cellphone."),
        ("Subli-a kini nga regular",
         "Maayong sumbanan ang kausa sa usa ka bulan; gikinahanglan gayod sa dili pa "
         "mag-ilis ug device, mag-reset o mag-update sa sistema. Huptan ang daan nga mga "
         "kopya — gagmay ra ang file, ug daghan na ang natabangan sa daang backup."),
    ],
    "sections": [
        ("Ang komon nga sayop: pagsalig sa cloud backup sa cellphone",
         "Ang backup sa tibuok cellphone (Google One, iCloud device backup) sagad "
         "magpasig-uli ug daan nga kopya sa datos sa JW Library — o wala gyoy mapasig-uli. Ang "
         ".jwlibrary nga file mao lang ang backup nga bug-os nimong kontrolado ug madala tali "
         "sa mga plataporma. Isipa ang backup sa cellphone nga bonus, dili plano."),
        ("Naay duha ka lahi nga backup?",
         "Mahitabo kini: usa gikan sa cellphone, usa nga mas daan gikan sa tablet, ug ang "
         "matag usa naay kaugalingong nota. Dili gyod nimo kinahanglang mopili tali kanila — "
         "hiusaha sila ngadto sa usa ka kompletong file sa jwsync.org, libre ug pribado, sa "
         "browser mismo."),
    ],
    "faq": [
        ("Unsa ka dako ang backup nga file?",
         "Kasagaran pipila ka megabyte bisan sa dagko kaayong library — igo ra ipadala isip "
         "attachment sa email."),
        ("Naay mausab ba sa akong cellphone kon maghimo kog backup?",
         "Wala. Isulat lang niini ang file; wala matandog ang imong library."),
    ],
}

GUIDES_CEB["jw-library-restore-replaced-notes"] = {
    "title": "Gipulihan ba sa pagpasig-uli sa JW Library ang imong mga nota? Unsaon pagbawi",
    "h1": "Gipulihan sa pagpasig-uli ang imong mga nota? Ania unsaon paghiusa ang duha ka backup",
    "description": "Bug-os nga pag-ilis ang pagpasig-uli sa JW Library, dili paghiusa — daw "
                   "nawala ang mga nota human sa petsa sa backup. Kon anaa pa nimo ang duha ka "
                   "backup nga file, walay nawala. Ania ang solusyon.",
    "intro": [
        "Makapaguol nga higayon: nagpasig-uli kag backup sa device nga naay mga nota na, ug "
        "gipulihan sa pagpasig-uli ang tanan — daw nawala ang mga nota nga imong gisulat sukad "
        "niadtong backup. Nahitabo kini kay ang Backup ug Pagpasig-uli sa JW Library bug-os "
        "nga pag-ilis, dili paghiusa.",
        "Ang hinungdanong punto: kon ang mas bag-ong buhat anaa pa sa bisan unsang backup nga "
        "file, wala gyoy nawala. Ang solusyon mao ang paghiusa sa duha ka backup imbes mopili "
        "tali kanila.",
    ],
    "steps": [
        ("Hunong — ayaw usa pagpasig-uli pag-usab",
         "Ang matag pagpasig-uli mopuli sa kasamtangang datos sa device. Hunong una sa dili pa "
         "may lain nga mawala."),
        ("I-backup ang device sa kasamtangan niining kahimtang",
         "Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup. Mapreserbar niini "
         "ang kasamtangang kahimtang, bisan unsa pay sulod."),
        ("Pangitaa ang backup nga naay nawalang mga nota",
         "Ang .jwlibrary nga file nga imong gigamit sa pagpasig-uli, o usa nga mas sayo — "
         "susiha ang imong email, Drive, iCloud ug ang downloads folder."),
        ("Hiusaha ang duha ka file sa jwsync.org",
         "I-load ang duha ka backup. Hiusahon sa JW Sync ang tanang nota, highlight, bookmark "
         "ug tag sa duha ngadto sa usa ka bag-ong file — sa browser, walay gi-upload. Ang "
         "nagkasumpaki nga bersiyon sa samang nota ipakita nga magtapad aron ikaw ang mopili."),
        ("Ipasig-uli ang gihiusang file",
         "Backup ug Pagpasig-uli → Ipasig-uli gamit ang gihiusang .jwlibrary. Anaa na pag-usab "
         "sa device ang duha ka set sa nota."),
    ],
    "sections": [
        ("Unsa kon walay backup sa mas bag-ong mga nota?",
         "Kon ang bugtong kopya sa mas bag-ong mga nota anaa sa device ug na-overwrite na kini "
         "sa pagpasig-uli, walay pag-undo ang JW Library mismo. Mao nga hinungdanon kaayo ang "
         "lakang 2 sa ibabaw — ang pag-backup sa kasamtangang kahimtang sa dili pa ang bisan "
         "unsa — matag higayon nga daw sayop ang datos. Sa umaabot, ang rutina nga “hiusaha "
         "una” maghimo niining problemaha nga imposible gyod."),
    ],
    "faq": [
        ("Magdoble ba ang mga nota nga anaa sa duha ka backup?",
         "Dili — mamatikdan ang managsamang mga butang ug usa ra ang huptan. Ang tinuod lang "
         "nga magkalahing bersiyon sa samang nota ang ipatimaan alang sa pagsusi."),
        ("Maayo ba kini sa backup nga dili gyod mapasig-uli?",
         "Kasagaran daot kana nga file, dili na-overwrite — tan-awa sa ubos ang giya bahin sa "
         "pag-ayo sa daot nga backup."),
    ],
}

GUIDES_CEB["fix-corrupted-jw-library-backup"] = {
    "title": "Ayoha ang daot nga backup sa JW Library nga dili mapasig-uli",
    "h1": "Pag-ayo sa daot nga backup sa JW Library gamit ang Library Doctor",
    "description": "Gibalibaran ba sa JW Library ang imong .jwlibrary nga file? Susihon sa "
                   "Library Doctor ang backup sa imong browser, ayohon ang komon nga mga "
                   "problema, ug maghatag ug limpyo nga kopya nga mapasig-uli.",
    "intro": [
        "Usahay dili dawaton sa JW Library ang backup nga file — mapakyas ang pagpasig-uli, "
        "may error, o dili moabli ang file. Komon nga hinungdan: naputol nga download, cloud "
        "drive nga nakadaot sa file, extension nga nausab sa dalan, o mga internal nga "
        "kakulangan nga natigom sa tuig-tuig nga paggamit.",
        "Nalakip sa JW Sync ang Library Doctor, usa ka pagsusi nga mobasa sa .jwlibrary nga "
        "file ug mo-ayo sa komon nga mga problema — bug-os sulod sa imong browser, ug wala "
        "gayod mobiya ang file sa imong device.",
    ],
    "steps": [
        ("Ablihi ang JW Sync ug i-load ang problemadong file",
         "Adto sa jwsync.org ug i-load ang .jwlibrary nga file nga dili mapasig-uli. (Kon "
         "miabot ang file nga giilisan ug .zip, ibalik una kini sa .jwlibrary — kana ra, "
         "daghan na ang masulbad.)"),
        ("Padagana ang pagsusi sa Library Doctor",
         "Susihon sa Doctor ang internal nga istruktura sa backup ug ilista sa yano nga "
         "pinulongan ang nakit-an niini — gikan sa dili makadaot nga kakulian hangtod sa tinuod "
         "nga kadaot."),
        ("Ipadapat ang mga pag-ayo",
         "Usa ka tap, maayo na ang maayohan. Wala gayod usba sa Doctor ang imong orihinal nga "
         "file; maghimo kini ug limpyo nga kopya, busa magpabiling buo ang orihinal isip andam "
         "nga kopya."),
        ("I-download ug ipasig-uli ang naayong file",
         "Ipasig-uli ang limpyo nga .jwlibrary pinaagi sa Backup ug Pagpasig-uli → Ipasig-uli "
         "sa JW Library."),
    ],
    "sections": [
        ("Modagan pod ang Doctor sa matag paghiusa",
         "Awtomatikong modagan ang samang pagsusi sulod sa merge engine, busa kanunayng "
         "limpyo ang gihatag nga gihiusang backup — bisan pa kon ang usa sa mga file naay "
         "problema nga wala nimo mahibaloi."),
        ("Kon dili na maayo ang file",
         "Kon naputol pag-ayo ang file mao nga wala na gyoy datos, walay tool nga makahimo "
         "niini pag-usab. Isulti kini sa Doctor nga prangka imbes maghatag ug duhaduhaan nga "
         "file — ug kana ang timailhan nga mangita ug mas sayo nga kopya sa email, Drive o "
         "iCloud, nga maoy usa usab ka rason nganong bililhon ang pagtipig sa daang backup."),
    ],
    "faq": [
        ("Gi-upload ba ang akong datos alang sa pagsusi?",
         "Wala. Ang pagsusi, mga pag-ayo ug ang pag-export tanan modagan sulod sa browser."),
        ("Makabawi ba kini sa mga nota nga gipapas sulod sa JW Library?",
         "Dili — ang istruktura sa file ang iyang ayohon. Ang mga nota nga gipapas sa app sa "
         "dili pa nahimo ang backup wala sa file aron mabawi pa."),
    ],
}

GUIDES_CEB["edit-jw-library-notes"] = {
    "title": "Tan-awa ug i-edit ang mga nota sa JW Library sa browser",
    "h1": "Tan-awa, pangitaa ug i-edit ang imong mga nota sa JW Library — Study Explorer",
    "description": "Ablihi ang bisan unsang .jwlibrary nga backup sa imong browser aron "
                   "sublay-sublayon, pangitaon, i-edit, ilisan ug tag, ilisan ug kolor ug "
                   "hinlo-on nga tinapok ang imong mga nota, highlight ug bookmark sa JW "
                   "Library. Walay gi-upload.",
    "intro": [
        "Gihimo ang JW Library para sa pagsulat ug nota, dili sa pagdumala sa liboan niini. "
        "Ablihan sa Study Explorer ang bisan unsang .jwlibrary nga backup diretso sa browser "
        "ug himoon kining mapangitaan ug ma-edit nga tigdumala sa library — mga nota, "
        "highlight ug bookmark sa usa ka dapit, ug walay gi-upload bisan asa.",
    ],
    "steps": [
        ("Pag-load ug backup",
         "Paghimo ug backup sa JW Library (Personal nga Pagtuon → Backup ug Pagpasig-uli → "
         "Paghimo ug backup), dayon ablihi ang jwsync.org ug i-load ang file sa Study "
         "Explorer."),
        ("Sublaya ug pangitaa ang tanan",
         "Tulo ka tab — Mga Nota, Mga Highlight, Mga Bookmark — nga naay bug-os nga pagpangita "
         "sa teksto ug mga salaan sa kolor, tag ug publikasyon. Ang tab nga Mga Tubag sa "
         "Pagtuon nagpakita usab sa mga tubag nga imong gisulat sa mga publikasyon."),
        ("Mag-edit diretso",
         "Ablihi ang bisan unsang nota aron i-edit ang ulohan ug sulod niini nga naay pormat "
         "(bold, italic, ilalom nga linya, listahan), ilisan ang kolor sa highlight, ug "
         "dugangan o kuhaan ug tag. Sama ra ang pag-edit sa mga bookmark ug kolor sa "
         "highlight."),
        ("Paghinlo nga tinapok",
         "Pilia ang daghang nota nga dungan aron ilisan ug tag, ilisan ug kolor o papason nga "
         "dungan — nga naay bug-os nga undo ug redo, busa dili gyod makamatay ang sayop. "
         "Mahimo ka pod mokuha ug mga nota sulod sa usa ka gilay-on sa petsa ngadto sa bag-ong "
         "backup, o kopyahon ang mga nota isip Markdown."),
        ("I-export ang imong na-edit nga library",
         "I-download ang na-edit nga .jwlibrary ug ipasig-uli kini sa JW Library. Anaa na sa "
         "device ang imong mga kausaban."),
    ],
    "sections": [
        ("Nganong mag-edit sa browser imbes sa app?",
         "Tungod sa gidak-on. Ang pag-ilis ug ngalan sa usa ka tag sa 300 ka nota, ang pag-ilis "
         "ug kolor sa tanang dalag nga highlight sa usa ka publikasyon, o ang pagpapas sa "
         "tuig-tuig nga daang bookmark pipila lang ka minuto dinhi ug oras-oras nga pag-tap sa "
         "app. Ordinaryong backup ang na-export nga file, busa ipasig-uli kini sa JW Library "
         "sama sa uban."),
    ],
    "faq": [
        ("Matandog ba ang akong orihinal nga backup kon mag-edit ko?",
         "Dili — himoon ang mga pag-edit sa usa ka kopya sulod sa browser ug itipig sa bag-ong "
         "na-export nga file. Magpabilin ang orihinal sama sa una."),
        ("Naay limitasyon ba sa gidak-on sa library?",
         "Bahinon sa mga panid ang dagko kaayong library aron magpabiling paspas ang "
         "pagsublay-sublay; molihok ang pagpangita ug mga salaan sa tanan."),
    ],
}

GUIDES_CEB["search-jw-library-notes"] = {
    "title": "Pangitaa ang mga nota sa JW Library sumala sa kahulogan — Pangutan-a ang Imong Library",
    "h1": "Pangutan-a ang Imong Library: pangitaa ang imong mga nota sumala sa kahulogan",
    "description": "Pagpangita sumala sa kahulogan alang sa imong mga nota sa JW Library: "
                   "pangitaa ang halos nakalimtang nota pinaagi sa paghulagway niini, bisan "
                   "kon dili nimo mahinumdoman ang eksaktong mga pulong. Sa device, molihok "
                   "nga offline, pribado.",
    "intro": [
        "Nailhan sa tanan nga naay tuig-tuig nga nota kining problemaha: nahinumdom ka nga "
        "nagsulat ka bahin sa pag-antos sa mga pagsulay nga malipayon, apan walay pulong nga "
        "“pagpailob” sa nota, busa walay makit-an ang pagpangita sa keyword. Sumala sa "
        "kahulogan mangita ang Pangutan-a ang Imong Library — ihulagway ang hunahuna, ug "
        "motungha ang labing suod nga mga nota, bisan unsa pay pagkasulat.",
        "Sa imong device modagan ang tanan: makausa ra ma-download ang language model ngadto "
        "sa browser ug molihok kini nga offline human niana, nga naay pagpaspas sa WebGPU kon "
        "anaa. Wala gayod ipadala ang imong mga nota bisan asa.",
    ],
    "steps": [
        ("Pag-load ug backup sa Study Explorer",
         "Sa jwsync.org, i-load ang imong .jwlibrary nga file ug ablihi ang tab nga "
         "Mangutana."),
        ("Pasagdi nga mangandam ang model kausa",
         "Sa unang paggamit, ma-download ang model sa device ug i-index ang imong mga nota. "
         "Kausa ra kini; human niana, diretso na kini molihok, bisan offline."),
        ("Pangutana sa imong kaugalingong pulong",
         "I-type ang imong mahinumdoman — “kadtong nota bahin sa pagpailob sa mga bag-o sa "
         "pag-alagad”, “pagdasig sa naluya nga mga payunir” — ug motungha ang labing suod nga "
         "mga nota, gilistahan sumala sa kahulogan."),
    ],
    "sections": [
        ("Unsay kalainan sa ordinaryong pagpangita",
         "Mga letra ang gitandi sa pagpangita sa keyword; mga ideya ang gitandi sa pagpangita "
         "sumala sa kahulogan. Ang pangutana bahin sa “kabalaka” makakita usab sa mga nota nga "
         "nagsulat ug “kahingawa”, “mga kabalaka sa kinabuhi” o usa ka teksto bahin sa "
         "hilisgotan. Anaa sa Study Explorer ang duha ka matang sa pagpangita — nagdinugtongay "
         "sila."),
        ("Pribado sa disenyo",
         "Dili kini serbisyo sa AI sa cloud. Sulod sa tab sa imong browser modagan ang model, "
         "anaa sa imong device ang index, ug kon sirad-an nimo ang tab, human na kana. Walay "
         "bahin sa imong mga nota nga mobiya sa imong makina."),
    ],
    "faq": [
        ("Kinahanglan ba ug kusgang device?",
         "Kaya kini pag-ayo sa bag-ong cellphone o laptop; labing paspas sa mga device nga "
         "naay WebGPU. Naay mapilian nga gidak-on sa model sumala sa imong hardware."),
        ("Molihok ba kini sa akong pinulongan?",
         "Oo — molihok ang pagpangita sa mga pinulongan nga gigamit sa imong mga nota, ug "
         "gihubad ang interface sa tanang 12 ka pinulongan nga gisuportahan sa JW Sync."),
    ],
}

GUIDES_CEB["jw-library-study-stats"] = {
    "title": "Tan-awa ang imong Study Stats sa JW Library: streak, heatmap ug ganti",
    "h1": "Ang imong study stats sa JW Library: streak, heatmap, kasakop ug mga ganti",
    "description": "Himoa ang backup sa JW Library nga pribadong analisis sa pagtuon — mga "
                   "kinatibuk-an, heatmap sa kalihokan, streak, kasakop sa Bibliya sa 66 ka "
                   "libro, profile sa batasan sa pagtuon ug mga 200 ka ganti.",
    "intro": [
        "Hilom nga girekord sa imong backup nga file ang tuig-tuig nga kasaysayan sa pagtuon — "
        "kanus-a ka magnota, unsay imong gi-highlight, unsang mga libro ang nasakop nimo. "
        "Basahon sa panid nga Study Stats ang .jwlibrary nga backup ug himoon kanang "
        "kasaysayana nga pribadong dashboard, nga bug-os gikuwenta sulod sa imong browser.",
    ],
    "steps": [
        ("Paghimo ug backup",
         "Sa JW Library: Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup."),
        ("Ablihi ang panid nga Study Stats",
         "Adto sa jwsync.org/highlights.html ug i-load ang file."),
        ("Susiha ang sugilanon sa imong pagtuon",
         "Ang mga nag-unang kinatibuk-an, ang mga panglantaw sa Tuig sa Pag-alagad ug sa "
         "Tibuok Panahon, ang pagtubo tuig-tuig — dayon ang makalingaw nga mga bahin sa ubos."),
    ],
    "sections": [
        ("Unsay imong makita",
         "Usa ka heatmap sa kalihokan nga naay imong labing taas ug kasamtangang streak; ritmo "
         "matag semana, labing busy nga mga oras ug bulan; kasakop sa Bibliya sa tanang 66 ka "
         "libro nga naay bahin sa Hebreohanon ug Gregong Kasulatan; usa ka ligid sa kolor sa "
         "mga highlight, histogram sa gitas-on sa mga nota ug word cloud; 24-oras nga relo sa "
         "pagtuon ug radar sa panahon."),
        ("Profile, panaw ug mga ganti",
         "Usa ka Study Profile nga naay unom ka kinaiya (Pagkamakanunayon, Kakugi, Kalalom, "
         "Kalapad, Pamalandong, Kalig-on) nga naay “Study Signature”; usa ka Study Journey nga "
         "60 ka lebel sa 12 ka ginganlang ang-ang; ug mga 200 ka ganti gikan sa Komon ngadto "
         "sa Legendaryo, apil ang mga medalya nga nagtan-aw sa sulod. Ang Shareable Card "
         "nagsumaryo sa imong tuig nga walay gipagawas nga bisan usa ka nota."),
        ("Usa ka adlaw-adlaw nga rason sa pagbalik",
         "Ipakita sa Resurface ang mga nota nga imong gisulat niining maong adlaw sa milabayng "
         "mga tuig ug maghimo ug malumo nga pagsubli nga may agwat — gamay apan subsob, mao "
         "kanay nagpabilin sa pagtuon."),
    ],
    "faq": [
        ("Naay gi-upload ba niini?",
         "Wala. Sa imong browser gitugkad ang backup; wala gayod mobiya ang estadistika sa "
         "imong device."),
        ("Mag-update ba ang estadistika sa iyaha ra?",
         "Gipakita niini ang backup nga imong gi-load — paghimo ug bag-ong backup aron makita "
         "ang bag-ong estadistika."),
    ],
}

GUIDES_CEB["share-jw-library-notes"] = {
    "title": "Unsaon pagpaambit sa mga nota sa JW Library sa usa ka higala",
    "h1": "Unsaon pagpaambit sa mga nota sa JW Library sa usa ka higala — walay server",
    "description": "Ipadala sa higala ang pinili nga mga nota sa JW Library (uban ang mga "
                   "highlight niini) isip gamay nga file — walay server, walay account. "
                   "Idugang kini sa modawat nga wala ma-overwrite ang iyang kaugalingong mga "
                   "nota.",
    "intro": [
        "Walay paagi sa JW Library aron hatagan ang laing tawo ug kopya sa piho nga mga nota. "
        "Molihok ang pagpadala sa tibuok backup — apan itugyan niini ang tanan, ug ang "
        "pagpasig-uli mopapas sa library sa modawat. Gisulbad sa pagpaambit sa nota sa JW Sync "
        "ang duha: pilion nimo gyod kon unsang nota ang ipaambit, ug idugang kini sa modawat "
        "nga walay mawala.",
    ],
    "steps": [
        ("Pilia ang mga nota nga ipaambit",
         "Sa panid sa pagpaambit sa jwsync.org/share.html, i-load ang imong backup ug pilia "
         "ang mga nota — pipila gikan sa usa ka pakigpulong, o ang tanan ubos sa usa ka tag "
         "sa usa ka klik pinaagi sa salaan sa tag. Mokuyog usab ang mga highlight nga "
         "nasumpay niadtong mga notaha."),
        ("Ipadala ang share file",
         "Maghimo ang JW Sync ug gamay nga file nga naay pinili lang nga mga nota. Ipadala "
         "kini sa bisan unsang paagi — messaging app, email, AirDrop. Walay server ug walay "
         "account; ang file mao ang tibuok pagbayloay."),
        ("Idugang kini sa modawat",
         "Ablihan sa imong higala ang samang panid, i-load ang share file uban sa iyang "
         "kaugalingong backup, ug makakuha siya ug bag-ong backup nga naay dugang nga imong "
         "mga nota. Wala gayod ma-overwrite ang iyang kaugalingong mga nota — kon "
         "magkasumpaki ang gipaambit nga nota ug ang iya, siya ang mopili kon unsaon kini "
         "idugang — ug naay tag ang na-import nga mga nota, busa sayon kining pangitaon, "
         "susihon o kuhaon unya."),
    ],
    "sections": [
        ("Maayong mga gamit",
         "Ang pagtunol sa panukiduki ngadto sa kauban sa pagtuon, ang pagpaambit sa nota sa "
         "tigom ngadto sa wala makatambong, ang paghatag sa bag-ong magmamantala ug "
         "sinugdanang set sa nota bahin sa usa ka publikasyon, o ang pagbalhin sa mga nota sa "
         "usa ka proyekto ngadto sa paryente — tanan kini nga wala ipagawas ang uban pa sa "
         "bisan hain nga library."),
    ],
    "faq": [
        ("Kinahanglan ba nga mag-install ug JW Sync ang modawat?",
         "Walay gi-install sa bisan hain nga kilid — web page kini. Ang gikinahanglan lang sa "
         "modawat mao ang share file ug ang iyang kaugalingong backup."),
        ("Mahimo ba nakong bawion ang pagpaambit o pahunongon ang file?",
         "Ordinaryong file lang ang imong gipadala — walay kopya sa server nga mahurot ang "
         "panahon. Ipaambit lang ang imong ipaambit usab sa bisan unsang mensahe."),
    ],
}

GUIDES_CEB["bible-reading-plan"] = {
    "title": "Adlaw-adlaw nga plano sa pagbasa sa Bibliya uban sa imong kaugalingong mga nota",
    "h1": "Reading Companion: plano sa pagbasa sa Bibliya uban sa imong mga nota",
    "description": "Usa ka pribadong adlaw-adlaw nga eskedyul sa pagbasa sa Bibliya nga "
                   "nagpakita sa mga nota ug highlight nga imong gihimo sa mga kapitulo "
                   "karong adlawa. Pilia ang tulin, huptan ang streak, tan-awa ang grid sa 66 "
                   "ka libro nga mapuno.",
    "intro": [
        "Daghang app ang naghatag ug eskedyul sa pagbasa sa Bibliya. Naay mahimo ang Reading "
        "Companion nga walay laing makahimo: kay basahon niini ang imong kaugalingong "
        ".jwlibrary nga backup, ang basahonon karong adlawa moabot uban sa mga nota ug "
        "highlight nga ikaw mismo ang naghimo niadtong mga kapituloha — “upat ka bersikulo sa "
        "Salmo 37 ang imong gi-highlight duha ka tuig na ang milabay.” Pagbasa pinaagi sa "
        "lente sa imong kaugalingong kasaysayan sa pagtuon, ug tanan anaa sa imong device.",
    ],
    "steps": [
        ("Pilia ang han-ay ug tulin",
         "Basaha sumala sa han-ay sa Bibliya o sa gibanabanang han-ay sa panahon; humana sa 3 "
         "ka bulan, 6 ka bulan, 1 ka tuig, 2 ka tuig, o itakda ang imong kaugalingong "
         "gidaghanon sa kapitulo kada adlaw — nga naay live nga banabana nga “mahuman ka mga "
         "petsa…”."),
        ("Basaha ang bahin karong adlawa",
         "Usa ka tap lang ang matag kapitulo ug moabli kini diretso sa JW Library o sa "
         "Watchtower ONLINE LIBRARY sa imong pinulongan. Tsekan ang mga kapitulo samtang "
         "nagpadayon ka."),
        ("Dad-a ang imong mga nota (opsiyonal)",
         "Pag-load ug backup sa bisan unsang tool sa JW Sync ug motungha ang imong "
         "kaugalingong mga nota ug ang gidaghanon sa highlight diretso sa ubos sa mga kapitulo "
         "karong adlawa."),
        ("Tan-awa ang pagtubo sa progreso",
         "Mapuno ang grid sa 66 ka libro samtang nagbasa ka, nga naay bar sa nabasang "
         "kapitulo, banabana base sa tulin, ug mga milyahe sa paghuman sa matag libro, sa "
         "Hebreohanon-Aramaikong Kasulatan, sa Gregong Kasulatan — ug sa tibuok Bibliya."),
    ],
    "sections": [
        ("Streak nga walay pagbasol",
         "Ang paghuman sa usa ka adlaw magpataas sa imong streak; ang paglaktaw ug adlaw "
         "magbalhin lang sa gibanabanang petsa sa pagtapos. Walay natapok nga utang — ang "
         "plano ang mopahiuyon sa imong kinabuhi, dili ikaw ang badlongon."),
    ],
    "faq": [
        ("Kinahanglan ba nakong mag-load ug backup aron magamit kini?",
         "Dili — molihok ang plano, streak ug progreso sa ilang kaugalingon. Ang backup "
         "magdugang lang sa imong personal nga mga nota sa basahonon matag adlaw."),
        ("Pribado ba ang akong progreso sa pagbasa?",
         "Oo. Anaa ang progreso sa browser sa imong device — walay account ug walay gi-upload."),
    ],
}

GUIDES_CEB["open-jwlibrary-file"] = {
    "title": "Unsa ang .jwlibrary nga file ug unsaon kini pag-abli?",
    "h1": "Unsa ang .jwlibrary nga file — ug unsaon pag-abli niini sa bisan unsang device",
    "description": "Ang .jwlibrary nga file mao ang imong backup sa JW Library: usa ka file "
                   "nga naay matag nota, highlight, bookmark ug tag. Ania ang sulod niini ug "
                   "kon unsaon kini pag-abli ug pagbasa.",
    "intro": [
        "Kon mag-backup ka sa JW Library, makakuha kag file nga matapos sa .jwlibrary. Usa "
        "kini ka nag-inusarang madala nga pakete nga naglangkob sa tanan sa imong personal nga "
        "pagtuon — mga nota, highlight, bookmark, tag ug playlist — sa usa ka siksik nga "
        "database. Dili kini dokumento nga imong ablihan sa Word o sa PDF reader; gihimo kini "
        "aron ipasig-uli balik sa JW Library.",
        "Apan dili nimo kinahanglang ipasig-uli kini aron lang makatan-aw sa sulod. Ablihan sa "
        "JW Sync ang .jwlibrary nga file diretso sa imong browser aron mabasa, mapangita ug "
        "ma-edit nimo ang sulod niini nga walay gikutlo sa cellphone.",
    ],
    "steps": [
        ("Pagkuha ug .jwlibrary nga file",
         "Gihimo kini sa JW Library: Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup "
         "ug Pagpasig-uli → Paghimo ug backup. Kanang file ang atong gihisgotan."),
        ("Ablihi kini sa JW Sync",
         "Adto sa jwsync.org ug i-load ang file sa Study Explorer. Diretso kining moabli, sa "
         "imong device — walay gi-upload."),
        ("Basaha ug gamita kini",
         "Sublaya ang mga nota, highlight ug bookmark; pangitaa sa tanan; i-edit, ilisan ug "
         "tag o i-export. Kon mahuman ka na, mahimo nimong ipasig-uli ang file (o ang na-edit "
         "nga kopya) balik sa JW Library."),
    ],
    "sections": [
        ("Unsa gyoy sulod sa file",
         "Sa teknikal nga paagi, ang .jwlibrary nga file usa ka gi-zip nga SQLite database "
         "dugang sa manifest. Mao nga usahay maaksidente kining mailisan ug .zip sa dalan — ug "
         "mao nang maayo ra kon ibalik kini sa .jwlibrary. Dili nimo kinahanglang mahibaloan "
         "kining tanan aron magamit kini, apan gipatin-aw niini nganong gamay, kompleto sa "
         "kaugalingon, ug managsama kini sa Android, iPhone, iPad ug Windows."),
        ("Pag-abli niini sa kompyuter",
         "Molihok usab ang samang panid nga jwsync.org sa browser sa laptop o desktop — "
         "mapuslanon sa pagbasa sa tuig-tuig nga nota sa dakong screen, o sa tinapok nga "
         "paghinlo nga makahago sa cellphone. Walay kinahanglang i-install."),
    ],
    "faq": [
        ("Mahimo ba nakong ablihan ang .jwlibrary nga file sa Excel o Notepad?",
         "Dili mapuslanon — database kini, dili spreadsheet o text file. Ablihi kini sa JW "
         "Sync aron mabasa, o i-export ang imong mga nota isip Markdown/teksto gikan sa Study "
         "Explorer."),
        ("Luwas ba ang pag-abli sa akong backup sa browser?",
         "Oo. Basahon sa JW Sync ang file sulod sa tab sa imong browser; walay ipadala sa "
         "server, ug wala gayod usba ang imong orihinal nga file."),
    ],
}

GUIDES_CEB["jw-library-windows-pc"] = {
    "title": "Pag-backup ug paghiusa sa JW Library sa Windows PC",
    "h1": "Paggamit sa mga backup sa JW Library sa Windows PC",
    "description": "Unsaon pag-backup sa JW Library sa Windows, ug unsaon paghiusa ang backup "
                   "sa PC ug ang sa cellphone ug tablet aron magpabiling tingob ang mga nota, "
                   "highlight ug bookmark sa matag device.",
    "intro": [
        "Modagan ang JW Library sa Windows sama sa mga cellphone ug tablet, ug maghimo kini sa "
        "samang .jwlibrary nga backup. Nagpasabot kana nga mahimong bahin ang imong PC sa "
        "samang library sa pagtuon sama sa imong cellphone — basta hiusahon nimo ang mga "
        "backup imbes ipasig-uli ang usa ibabaw sa lain.",
    ],
    "steps": [
        ("Pag-backup sa Windows",
         "Sa JW Library app para sa Windows, ablihi ang menu, adto sa Backup ug Pagpasig-uli, "
         "ug paghimo ug backup. Itipig ang .jwlibrary nga file sa dapit nga sayon pangitaon."),
        ("I-backup pod ang imong cellphone ug tablet",
         "Sa matag device: Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug "
         "Pagpasig-uli → Paghimo ug backup."),
        ("Hiusaha sila sa jwsync.org",
         "Ablihi ang jwsync.org sa bisan unsang browser sa PC ug i-load ang tanang backup nga "
         "file. Hiusahon sa JW Sync ang mga nota, highlight, bookmark ug tag sa matag device "
         "ngadto sa usa ka gihiusang .jwlibrary nga file — sa PC mismo, walay gi-upload."),
        ("Ipasig-uli ang gihiusang file bisan asa",
         "Ipasig-uli ang gihiusang file sa Windows app ug sa matag mobile device. Kompleto na "
         "ang library sa PC, cellphone ug tablet."),
    ],
    "sections": [
        ("Nganong sa PC kini labing sayon",
         "Sa browser sa kompyuter, mas paspas ang pag-load ug daghang file, ang pagsusi sa "
         "preview sa paghiusa, ug ang pagtipig sa resulta kay sa pag-tap sa cellphone. Daghan "
         "ang nagtipig sa ilang nag-unang rutina sa paghiusa sa kompyuter ug ipasig-uli na "
         "lang ang gihiusang file sa ilang mga mobile device."),
    ],
    "faq": [
        ("Molihok ba ang backup sa Windows uban sa iPhone ug Android?",
         "Oo — managsama ang .jwlibrary nga format sa tanang plataporma, busa gawasnong "
         "maghiusa ang backup sa Windows ug ang sa cellphone ug tablet."),
        ("Naay kinahanglan ba nakong i-install sa PC?",
         "Wala. Web page ang JW Sync; modagan kini sa Edge, Chrome o Firefox nga walay "
         "gi-install."),
    ],
}

GUIDES_CEB["recover-jw-library-notes-lost-phone"] = {
    "title": "Unsaon pagbawi sa mga nota sa JW Library human mawala o maguba ang cellphone",
    "h1": "Pagbawi sa mga nota sa JW Library gikan sa nawala, naguba o na-reset nga cellphone",
    "description": "Nawala o na-reset ang cellphone nga naay mga nota sa JW Library? Ang "
                   "mabawi nimo nagdepende sa imong mga backup. Ania kon unsaon gyod pagbawi "
                   "sa imong mga nota — ug unsay buhaton sa sunod nga higayon.",
    "intro": [
        "Igo na gyoy makapaguol ang pagkawala sa cellphone bisan walay kahadlok nga nawala pod "
        "ang tuig-tuig nga nota sa pagtuon. Kon mabawi ba nimo sila nagdepende sa usa ka "
        "pangutana: naa bay .jwlibrary nga backup bisan asa sa gawas nianang cellphone?",
        "Giubanan ka niining giyaha sa pagpangita sa bisan unsang backup nga mahimong anaa "
        "nimo — apil ang mga nakalimtan nimong gihimo — ug sa pagbalik niini ngadto sa "
        "kompletong library sa JW Library sa imong bag-ong device.",
    ],
    "steps": [
        ("Pangitaa sa matag dapit nga posibleng naay backup",
         "Susiha ang imong email (pangitaa ang “jwlibrary” o “backup”), Google Drive, iCloud "
         "Drive, OneDrive, Dropbox ug ang Downloads folder sa imong kompyuter. Gagmay nga file "
         "ang mga backup nga sayon kalimtan nga imong gitipigan."),
        ("Susiha ang imong ubang device",
         "Kon nakagamit ka na ug JW Library sa tablet o PC, naa kiniy kaugalingong datos sa "
         "pagtuon — paghimo ug backup gikan niini karon dayon aron mapreserbar ang sulod "
         "niini."),
        ("Ipasig-uli ang imong nakit-an sa bag-ong cellphone",
         "I-install ang JW Library sa bag-ong device, dayon Backup ug Pagpasig-uli → "
         "Ipasig-uli, ug i-load ang .jwlibrary nga file. Mobalik ang imong mga nota, highlight "
         "ug bookmark."),
        ("Hiusaha kon kapin sa usa ang backup nga nakit-an",
         "Ang lainlaing device o petsa mahimong naay kaugalingong talagsaong mga nota. Ayaw "
         "pagpili ug usa lang — i-load silang tanan sa jwsync.org, hiusaha sila ngadto sa usa "
         "ka kompletong file, ug kana ang ipasig-uli. Walay mahibilin."),
    ],
    "sections": [
        ("Kon wala gyoy backup bisan asa",
         "Pagmatinud-anon sa imong kaugalingon sayo pa: kon ang bugtong kopya sa imong mga "
         "nota anaa sa nawalang cellphone ug wala ka gayod nag-export ug backup, walay kopya "
         "sa cloud ang JW Library nga mapasig-ulian. Sakit kana — ug mao gyoy hinungdan nganong "
         "hinungdanon kaayo ang batasan sa ubos."),
        ("Aron dili na kini mausab",
         "Pagtakda ug binulan nga pahinumdom sa pag-backup ug itipig ang matag .jwlibrary nga "
         "file sa gawas sa cellphone (igo na ang pag-email niini sa imong kaugalingon). "
         "Mahimo pa kang pahinumdoman sa JW Sync ug hiusahon ang imong mga device nga regular. "
         "Ang file nga anaa sa imong inbox mabuhi ug mas dugay kay sa bisan unsang cellphone."),
    ],
    "faq": [
        ("Mabawi ba sa JW Sync ang mga nota gikan sa cellphone nga wala na nako?",
         "Walay tool nga makahimo — nagdepende ang pagbawi sa paglungtad sa backup nga file "
         "bisan asa. Ang buluhaton sa JW Sync mao ang pagbasa, pag-ayo ug paghiusa sa mga "
         "backup nga anaa nimo."),
        ("Daan na ang akong backup — bililhon pa ba kining ipasig-uli?",
         "Bililhon gyod. Mas maayo ang daang backup nga naay kadaghanan sa imong mga nota kay "
         "sa pagsugod sa wala, ug mahimo nimo kining hiusahon unya sa bisan unsang mas bag-o "
         "nga imong makit-an."),
    ],
}

GUIDES_CEB["handle-merge-conflicts"] = {
    "title": "Samang nota, na-edit sa duha ka device? Pagdumala sa mga conflict sa paghiusa",
    "h1": "Pagdumala sa mga conflict sa paghiusa: samang nota nga na-edit sa duha ka device",
    "description": "Kon lahi ang imong pag-edit sa samang nota sa duha ka device, kinahanglang "
                   "mopili ang paghiusa. Ipakita sa Conflict Reviewer ang duha ka bersiyon nga "
                   "magtapad aron ikaw ang modesisyon — walay mawala.",
    "intro": [
        "Halos walay kalisod ang kadaghanan sa paghiusa — ang mga nota nga anaa lang sa usa ka "
        "device basta maghiusa lang. Ang bugtong kaso nga nagkinahanglag desisyon mao ang "
        "tinuod nga conflict: samang nota, lahi ang pag-edit sa duha ka device, mao nga "
        "wala magkauyon ang duha ka backup kon unsa unta ang sulod niini. Wala gayod "
        "magtag-an ang JW Sync sa hilom; kanimo ihatag ang pagpili.",
    ],
    "steps": [
        ("I-load ang duha ka backup",
         "Sa jwsync.org, i-load ang mga .jwlibrary nga file gikan sa duha ka device. Itandi "
         "kini sa JW Sync samtang naghiusa."),
        ("Ablihi ang Conflict Reviewer",
         "Kon naay mga notang nagkasumpaki, ilistahan sila sa reviewer. Nahiusa na ang tanang "
         "walay sumpaki — para lang sa tinuod nga panagsangka kining lakanga."),
        ("Itandi nga magtapad",
         "Ang matag conflict magpakita sa duha ka bersiyon nga naay kalainan nga gipatimaan "
         "pulong-por-pulong. Mahimong pilion sa “Isugyot ang labing maayo” ang mas kompletong "
         "bersiyon para nimo, o ikaw ang mopili — nota por nota."),
        ("Humana ug ipasig-uli",
         "Kon nasulbad na ang tanang conflict, i-download ang gihiusang file ug ipasig-uli "
         "kini. Nagkauyon na ang duha ka device, uban sa bersiyon nga imong gipili sa matag "
         "nota."),
    ],
    "sections": [
        ("Nganong mas maayo kini kay sa paghupot na lang sa pinakabag-o",
         "Ang “ang pinakabag-o modaog” hilom nga mopapas sa mga pag-edit nga tingali gusto pa "
         "nimong huptan. Tingali naay parapo sa daang bersiyon nga aksidente nimong gikuha sa "
         "pikas device. Ang pagtan-aw sa duha, pulong-por-pulong, nagpasabot nga wala gayod "
         "kay mawad-ang teksto nga wala nimo hibaloi — mao gyod kanay tibuok tuyo sa paghiusa "
         "imbes pag-overwrite."),
        ("Asa gikan ang mga conflict",
         "Kasagaran gikan sa pag-edit nga offline sa duha ka device tali sa mga paghiusa, o sa "
         "pagpasig-uli sa daang backup ug pagdugang niini. Ang regular nga paghiusa "
         "magpabiling gamay sa gidaghanon sa conflict ug lab-as sa panumdoman ang mga "
         "kalainan."),
    ],
    "faq": [
        ("Kinahanglan ba nakong susihon ang gatosan ka conflict?",
         "Panagsa ra. Ang mga nota lang nga lahi ang pag-edit sa duha ka kilid ang "
         "magkasumpaki; awtomatikong maghiusa ang bag-ong nota ug ang giusab sa usa lang ka "
         "device. Sa kadaghanan sa paghiusa, pipila ra ka conflict o wala gyod."),
        ("Mahimo ba nakong usbon ang akong hunahuna human mopili?",
         "Oo — walay masulat sa device hangtod nga ipasig-uli nimo ang gihiusang file, ug wala "
         "gayod usba ang imong orihinal nga mga backup, busa mahimo nimong subson ang "
         "paghiusa."),
    ],
}

GUIDES_CEB["export-jw-library-notes"] = {
    "title": "Unsaon pag-export sa mga nota sa JW Library ngadto sa teksto o Markdown",
    "h1": "Pag-export sa imong mga nota sa JW Library ngadto sa teksto, Markdown o bag-ong backup",
    "description": "Ipagawas ang imong mga nota sa JW Library gikan sa app: kopyaha o "
                   "i-export sila isip Markdown o yanong teksto aron magamit bisan asa, o "
                   "kuhaa ang usa ka pinili ngadto sa bag-ong .jwlibrary nga backup. Tanan sa "
                   "browser mo.",
    "intro": [
        "Dili unta makulong sa usa ka app ang imong mga nota sa pagtuon. Usahay gusto nimo "
        "sila isip yanong teksto — aron itapot sa balangkas sa pakigpulong, sa usa ka "
        "dokumento, o sa imong kaugalingong notes app — ug usahay gusto nimo ug limpyo nga "
        "backup nga naay bahin lang. Kaya sa Study Explorer ang duha, ug basahon niini ang "
        "imong backup nga bug-os sulod sa browser.",
    ],
    "steps": [
        ("I-load ang imong backup",
         "Paghimo ug backup sa JW Library (Personal nga Pagtuon → Backup ug Pagpasig-uli → "
         "Paghimo ug backup), dayon ablihi ang jwsync.org ug i-load kini sa Study Explorer."),
        ("Pangitaa ang mga nota nga imong gusto",
         "Gamita ang pagpangita uban sa mga salaan sa kolor, tag ug publikasyon aron makaabot "
         "gyod sa mga nota nga imong gipangita — usa ka publikasyon, usa ka tag, usa ka "
         "hilisgotan."),
        ("Kopyaha o i-export isip Markdown o teksto",
         "Ipagawas ang mga nota isip Markdown o yanong teksto aron itapot bisan asa. "
         "Magpabilin ang pormat (bold, italic, listahan), busa magpabiling nahan-ay ang mga "
         "notang nahan-ay."),
        ("O kuhaa ngadto sa bag-ong backup",
         "Mas gusto nimo ug file? I-export ang usa ka pinili o gilay-on sa petsa ngadto sa "
         "bag-ong .jwlibrary nga backup — mapuslanon sa pagtipig sa usa ka proyekto o sa "
         "paghatag ug piho nga set sa nota ngadto sa laing device."),
    ],
    "sections": [
        ("Nganong mag-export gyod",
         "Mas mapuslanon ang mga nota kon makabiyahe sila: ngadto sa dokumento para sa usa ka "
         "asaynment sa tigom, ngadto sa personal nga wiki, ngadto sa giimprinta para sa "
         "wala mogamit sa app. Gitipigan sa Markdown ang han-ay samtang mabasa gihapon isip "
         "yanong teksto bisan asa."),
    ],
    "faq": [
        ("Mausab ba ang akong mga nota sa JW Library kon mag-export?",
         "Dili. Usa ka kopya sa imong backup ang basahon sa pag-export sa browser; wala "
         "matandog ang imong orihinal nga file ug ang app."),
        ("Mahimo ba nakong i-export ang tanan nga dungan?",
         "Oo — hawa-i ang mga salaan aron pilion ang tibuok library, o pig-ota una aron "
         "i-export ang bahin lang."),
    ],
}

GUIDES_CEB["organize-jw-library-tags"] = {
    "title": "Unsaon paghan-ay ug paghinlo sa mga tag sa JW Library",
    "h1": "Paghan-ay sa imong mga tag sa JW Library: ilisan ug ngalan, hiusahon ug hinloan nga tinapok",
    "description": "Modaghan ang mga tag sa paglabay sa tuig sa pagtuon. Ilisan ug ngalan ang "
                   "usa ka tag sa tanang nota, hiusaha ang mga duplicate, ug kuhaa ang wala na "
                   "nimo gamita — nga tinapok, sa browser, ug naay bug-os nga undo.",
    "intro": [
        "Ang mga tag mao ang imong paagi sa pagpangita sa mga nota unya — apan human sa "
        "pipila ka tuig, magkatag na sila. Matapos ka nga naay “Ministeryo”, “ministeryo” ug "
        "“Pag-alagad sa kanataran” nga usa ra ang kahulogan, mga tag nga gihimo kausa ug wala "
        "na gamita, ug dili managsamang pagngalan nga naghimo sa pag-salang nga dili "
        "kasaligan. Walay paagi sa JW Library aron ayohon kini sa dagkong sukod. Sa Study "
        "Explorer, naa.",
    ],
    "steps": [
        ("I-load ang imong backup sa Study Explorer",
         "Sa jwsync.org, i-load ang imong .jwlibrary nga file. Salaa pinaagi sa tag aron "
         "makita ang matag tag ug kon pila ka nota ang nagdala niini."),
        ("Ilisan ug ngalan ang usa ka tag sa tanan niining nota",
         "Ilisan ang tag nga tinapok: ilisan ug ngalan ang tag kausa ug ma-update ang matag "
         "nota nga naggamit niini — wala nay pag-edit ug tagsa-tagsa aron ayohon lang ang usa "
         "ka sayop nga letra."),
        ("Hiusaha ang mga duplicate",
         "Balhina ang tag sa mga nota gikan sa duplicate ngadto sa nag-unang tag, dayon kuhaa "
         "ang walay sulod nga duplicate. Mahimong usa ka limpyo nga tag ang “Ministeryo” ug "
         "“ministeryo”."),
        ("Kuhaa ang mga tag nga wala na nimo gamita",
         "Pilia ug papasa nga tinapok ang mga daan nga tag. Mabawi ang tanan, busa dili gayod "
         "permanente ang sobra ka kugihan nga paghinlo."),
        ("I-export ang nahan-ay nga library",
         "I-download ang na-edit nga .jwlibrary ug ipasig-uli kini sa JW Library. Managsama na "
         "ang imong mga tag bisan asa."),
    ],
    "sections": [
        ("Sistema sa tag nga makatabang gyod",
         "Kon managsama na ang mga tag, masaligan na ang pag-salang — usa ka tap ug makita "
         "ang matag nota bahin sa usa ka tema, sa tanang publikasyon. Mao kanay kalainan sa "
         "mga tag isip kagubot ug sa mga tag isip tinuod nga indeks sa imong pagtuon."),
        ("Ang managsamang tag naghimo sa pagpaambit nga duha ka klik lang",
         "Ang tigpili ug nota sa panid sa pagpaambit naay kaugalingong salaan sa tag, busa ang "
         "limpyong tag mao pod ang labing paspas nga paagi sa pagpadala ug set sa nota ngadto "
         "sa uban: pilia ang tag, i-press ang Pilia tanan, himoa ang file. Doble ang kabayran "
         "sa walay pagtagad nga mga tag — sa dihang mangita kag nota, ug sa dihang paningkamotan "
         "nimong ipaambit sila."),
    ],
    "faq": [
        ("Matandog ba ang teksto sa nota kon mag-ilis ug tag nga tinapok?",
         "Dili — ang mga tag lang nga nasumpay ang mausab. Magpabilin ang mga ulohan ug sulod "
         "sa imong nota sama gyod sa imong gisulat."),
        ("Naay undo ba kon masayop ko?",
         "Naa. Naay bug-os nga undo ug redo ang Study Explorer, ug wala gayod usba ang imong "
         "orihinal nga backup — moadto sa na-export nga kopya ang mga kausaban."),
    ],
}

GUIDES_CEB["manage-jw-library-highlights"] = {
    "title": "Unsaon pagdumala ug pag-ilis ug kolor sa mga highlight sa JW Library",
    "h1": "Pagdumala sa imong mga highlight sa JW Library: ilisan ug kolor ug han-aya nga tinapok",
    "description": "Han-aya ang tuig-tuig nga highlight sa JW Library: ilisan ang mga kolor nga "
                   "tinapok, hatagi ug managsamang kahulogan ang imong sistema sa kolor, ug "
                   "sublaya ang matag highlight sa usa ka dapit. Sa browser mo.",
    "intro": [
        "Makatabang lang ang mga kolor sa highlight kon naa silay managsamang kahulogan. Sa "
        "paglabay sa panahon, magkalain-lain na ang highlight sa kadaghanan — lahi ang "
        "kahulogan sa dalag niadtong 2019 ug lahi na karon, ug walay paagi sa JW Library aron "
        "makita silang tanan nga dungan o ayohon sa dagkong sukod. Tigumon sa Study Explorer "
        "ang matag highlight ngadto sa usa ka panglantaw ug tugotan ka nga mag-ilis ug kolor "
        "nga tinapok.",
    ],
    "steps": [
        ("I-load ang imong backup",
         "Sa jwsync.org, ablihi ang imong .jwlibrary nga file sa Study Explorer ug balhin sa "
         "tab nga Mga Highlight."),
        ("Sublaya ug salaa ang imong mga highlight",
         "Tan-awa ang matag highlight sa usa ka listahan, salaa pinaagi sa kolor o "
         "publikasyon, ug pangitaa ang gi-highlight nga teksto ug ang bisan unsang nasumpay "
         "nga nota."),
        ("Ilisan ang kolor nga tinapok",
         "Pilia ang daghang highlight ug ilisan ang kolor nila nga dungan — pananglitan, "
         "hiusaha sa usa ka kolor ang tanan nga imong gipasabot nga “mahinungdanong teksto” sa "
         "tibuok library."),
        ("I-edit pod ang nasumpay nga mga nota",
         "Kon naay nota nga nasumpay sa usa ka highlight, dinhi mismo nimo mahimong i-edit ang "
         "ulohan ug sulod niadtong notaha."),
        ("I-export ug ipasig-uli",
         "I-download ang na-edit nga .jwlibrary ug ipasig-uli kini sa JW Library aron anaa sa "
         "matag device ang imong managsamang sistema sa kolor."),
    ],
    "sections": [
        ("Hukmi kon unsay kahulogan sa imong mga kolor",
         "Ang usa ka yanong laraw — usa ka kolor sa nag-unang mga punto, usa sa mga teksto nga "
         "sag-ulohon, usa sa mga pangutana nga sukitsukiton — maghimo sa mga highlight nga "
         "kagamitan sa pagtuon imbes dayandayan. Ang pag-ilis ug kolor nga tinapok magtugot "
         "nimo nga ipadapat kanang laraw pabalik sa tuig-tuig nga pagbasa."),
    ],
    "faq": [
        ("Makita ba nako ang mga highlight nga walay nasumpay nga nota?",
         "Oo — ipakita silang tanan sa tab nga Mga Highlight, may nasumpay man o wala."),
        ("Maapektuhan ba ang teksto sa ilalom kon mag-ilis ug kolor?",
         "Dili, ang kolor lang sa highlight ang mausab; wala matandog ang teksto sa "
         "publikasyon ug ang imong mga nota."),
    ],
}

GUIDES_CEB["jw-library-study-answers"] = {
    "title": "Tan-awa ug i-edit ang imong mga tubag sa pagtuon sa JW Library",
    "h1": "Pagpangita sa imong mga tubag sa pagtuon sa JW Library sa usa ka dapit",
    "description": "Ang mga tubag nga imong gi-type sa mga pangutana sa artikulo sa pagtuon ug "
                   "workbook natago sa imong backup. Ang tab nga Mga Tubag sa Pagtuon sa Study "
                   "Explorer motugot nimo sa pagbasa, pagpangita ug pag-edit kanilang tanan "
                   "nga dungan.",
    "intro": [
        "Samtang magtuon ka, mag-type kag mga tubag sa mga kahon sa artikulo sa pagtuon, sa "
        "Bantayanang Torre, ug sa mga workbook sa tigom. Natipigan sila sa imong backup — apan "
        "ipakita ra sila sa JW Library nga tagsa-tagsa, natabonan sa ilang kaugalingong "
        "publikasyon. Walay usa ka dapit diin masusi ang tanan nimong gisulat. Ang tab nga Mga "
        "Tubag sa Pagtuon sa Study Explorer mao kanang dapita.",
    ],
    "steps": [
        ("I-load ang imong backup sa Study Explorer",
         "Sa jwsync.org, i-load ang imong .jwlibrary nga file ug ablihi ang tab nga Mga Tubag "
         "sa Pagtuon."),
        ("Basaha ang tanan nimong tubag nga dungan",
         "Motungha sa usa ka mapangitaan nga listahan ang matag tubag nga imong gi-type, busa "
         "masusi nimo sa usa ka tan-aw ang tibuok nimong hunahuna sa usa ka artikulo sa "
         "pagtuon."),
        ("Pangitaa ug i-edit",
         "Pangitaa ang tubag pinaagi sa teksto niini, dayon i-edit ug pinuha kini diretso — "
         "mapuslanon sa pagsusi sa dili pa ang tigom o sa paghan-ay sa dinalidali nga "
         "pagkasulat."),
        ("I-export o ipasig-uli",
         "Ipasig-uli ang na-edit nga file aron dad-on balik ang imong mga kausaban sa JW "
         "Library, o kopyaha ang mga tubag isip teksto para sa pakigpulong o personal nga "
         "talaan."),
    ],
    "sections": [
        ("Nganong mapuslanon kini sa dili pa ang tigom",
         "Ang pagsusi sa imong giandam nga mga tubag sa usa ka nagpadayong listahan — imbes "
         "mag-scroll sa matag parapo sa app — mas paspas nga paagi sa paghinumdom kon unsay "
         "imong isulti, ug sa pagmatikod sa mga tubag nga nabilin nga walay sulod."),
    ],
    "faq": [
        ("Pareho ba kini sa akong personal nga mga nota?",
         "Dili — ang mga tubag sa pagtuon mao ang imong gi-type sa mga kahon sa tubag sa usa "
         "ka publikasyon. Ipakita sila sa Study Explorer sa kaugalingong tab, bulag sa gawasnong "
         "mga nota."),
        ("Naay gi-upload ba aron mabasa ang akong mga tubag?",
         "Wala. Sama sa tanan sa JW Sync, basahon ang imong backup sulod sa browser ug wala "
         "gayod ipadala bisan asa."),
    ],
}

GUIDES_CEB["extract-jw-library-notes-by-date"] = {
    "title": "Pagkuha sa mga nota sa JW Library gikan sa usa ka panahon ngadto sa bag-ong backup",
    "h1": "Pagkuha sa mga nota sulod sa usa ka gilay-on sa petsa ngadto sa bag-ong backup",
    "description": "Ilain ang mga nota lang gikan sa piho nga panahon — usa ka tuig sa "
                   "pag-alagad, usa ka kombensiyon, usa ka proyekto sa pagtuon — ngadto sa "
                   "kaugalingong limpyo nga .jwlibrary nga backup. Bug-os sa imong browser.",
    "intro": [
        "Usahay bahin lang sa imong library ang imong gusto, dili tanan: ang mga nota karong "
        "tuiga alang sa pagsusi, ang tanan gikan sa usa ka kombensiyon, o ang panukiduki sa "
        "usa ka proyekto aron ihatag sa uban. Kaya sa Study Explorer nga kuhaon ang mga nota "
        "sulod sa usa ka gilay-on sa petsa ngadto sa bag-o gyod nga .jwlibrary nga backup, ug "
        "wala matandog ang imong nag-unang library.",
    ],
    "steps": [
        ("I-load ang imong backup",
         "Sa jwsync.org, ablihi ang imong .jwlibrary nga file sa Study Explorer."),
        ("Itakda ang gilay-on sa petsa",
         "Pilia ang sinugdanan ug kataposang petsa sa mga nota nga imong gusto — usa ka tuig "
         "sa pag-alagad, usa ka bulan, ang mga petsa sa usa ka piho nga hitabo."),
        ("Kuhaa ngadto sa bag-ong backup",
         "I-export ang mohaom nga mga nota ngadto sa bag-ong .jwlibrary nga file. Naay sulod "
         "lang kini nga mga nota ug highlight nianang panahona, uban ang ilang mga tag."),
        ("Gamita ang nakuhang file",
         "Ipasig-uli kini sa JW Library alang sa nakapunting nga pagsusi, itipig kini, o "
         "ipaambit sa usa nga kanang bahina lang ang gikinahanglan."),
    ],
    "sections": [
        ("Maayong mga rason sa pagkuha pinaagi sa petsa",
         "Usa ka tinuig nga tipiganan sa imong pagtuon; usa ka limpyo nga file sa mga nota sa "
         "kombensiyon nga gilain; ang paghatag sa kauban sa pagtuon sa mga nota lang gikan sa "
         "proyekto nga inyong gibuhat nga duha; o ang pagbahin sa dako kaayong library ngadto "
         "sa madumala ug may petsa nga mga bahin — tanan nga wala gikutlo ang imong nag-unang "
         "backup."),
    ],
    "faq": [
        ("Makuha ba sa akong library ang mga notang gikuha?",
         "Dili. Kopyahon lang niini ang mohaom nga mga nota ngadto sa bag-ong file; magpabiling "
         "buo ang imong orihinal nga backup."),
        ("Unsang petsa ang gigamit — kanus-a ko nagsulat o kanus-a ko kataposang nag-edit?",
         "Gigamit ang mga timaan sa oras sa nota mismo sulod sa backup, busa gipakita sa "
         "gilay-on kon kanus-a gihimo o giusab ang mga nota."),
    ],
}

GUIDES_CEB["connect-jw-library-notes-study-map"] = {
    "title": "Tan-awa kon unsaon pagsumpay sa imong mga nota sa JW Library — Study Map",
    "h1": "Study Map: pribadong mapa sa kahibalo gikan sa imong mga nota sa JW Library",
    "description": "Himoon sa Study Map nga interaktibong lambat ang imong mga nota sa JW "
                   "Library, nga magsumpay kanila pinaagi sa managsamang teksto, managsamang "
                   "tag ug susamang pagkasulti — aron makita nimo ang mga tema nga milatas sa "
                   "imong pagtuon.",
    "intro": [
        "Naay mga sumpay sa tuig-tuig nga nota nga wala pa nimo makita: ang samang teksto nga "
        "gikutlo sa napulog duha ka entrada, usa ka tema nga imong balik-balikan, mga ideya nga "
        "nagsanong sa usag usa sa lainlaing publikasyon. Idrowing sa Study Map kanang mga "
        "sumpaya isip interaktibong graph, aron makita ang porma sa imong kaugalingong "
        "pagtuon.",
    ],
    "steps": [
        ("Ablihi ang panid nga Study Stats ug mag-load ug backup",
         "Adto sa jwsync.org/highlights.html ug i-load ang imong .jwlibrary nga file. Basahon "
         "kini sa Study Map sa imong browser."),
        ("Ablihi ang Study Map",
         "Sugdi ang mapa aron makita ang imong mga nota isip nagkasumpay nga mga tuldok, nga "
         "gisumpay sa managsamang teksto, managsamang tag ug susamang pagkasulti."),
        ("Susiha ang mga sumpay",
         "Balhin-balhin tali sa panglantaw nga Mga Tema ug Mga Nota, ipatong ang cursor aron "
         "ipasiga ang mga sumpay sa usa ka nota, guyora ang mga butang, ug gamita ang slider "
         "sa kusog aron ipakita lang ang labing suod nga mga sumpay. Naay luna ang full-screen "
         "mode aron makalihok."),
        ("Paghimo ug pagtipig ug mga study chain",
         "Idrowing ang imong kaugalingong “study chain” tali sa nalambigit nga mga nota aron "
         "matipigan ang linya sa pangatarongan, ug i-export ang mapa isip PNG nga hulagway aron "
         "itipig o ipakita."),
    ],
    "sections": [
        ("Unsay gipadayag sa mapa",
         "Ang mga pundok nagpakita sa mga tema nga labing gitun-an nimo; ang tekstong nasumpay "
         "sa daghang nota nagpakita sa bersikulo nga imong balik-balikan; ang nag-inusarang "
         "nota mahimong lugas nga angayng palamboon. Usa kini ka paagi sa pagtuon sa imong "
         "pagtuon — ug sa pag-andam ug pakigpulong pinaagi sa pagsunod sa mga sumpay nga imong "
         "nahimo na."),
    ],
    "faq": [
        ("Kinahanglan ba ug daghang nota aron mapuslanon ang mapa?",
         "Bisan ang kasarangang library nagpakita nag mga sumpay; kon mas dato ang imong mga "
         "nota, mas daghan ang ipadayag sa mapa. Sa gagmay kaayong library, motungha ang "
         "pahinumdom nga magdugang una ug nota."),
        ("Pribado ba ang mapa?",
         "Bug-os. Gihimo kini sa imong browser gikan sa imong backup ug wala gayod "
         "gi-upload; bisan ang PNG nga export gihimo sa imong device."),
    ],
}

GUIDES_CEB["review-old-jw-library-notes"] = {
    "title": "Unsaon pagsusi sa imong daang mga nota sa JW Library (aron magpabilin sila)",
    "h1": "Pagsusi sa daang mga nota gamit ang Resurface — gamay apan subsob",
    "description": "Ang mga nota nga wala nimo balika mao ang mga nota nga imong makalimtan. "
                   "Ipakita sa Resurface ang imong gisulat niining adlawa sa milabayng mga "
                   "tuig ug maghimo ug malumo nga pagsubli nga may agwat, aron magpadayon sa "
                   "pagtabang nimo ang milabayng pagtuon.",
    "intro": [
        "Kadaghanan sa mga nota sa pagtuon gisulat kausa ug wala na gyod makita pag-usab. "
        "Hilom nga pag-usik kana — takos untang isulat ang panabot, dayon nalunod kini sa "
        "ilalom sa library. Ibalik sa Resurface sa ibabaw ang imong kaugalingong daang mga "
        "nota, tag-pipila lang, aron ang pagbalik-tan-aw mahimong gamayng adlaw-adlaw nga "
        "batasan imbes proyekto nga “unya-unya lang”.",
    ],
    "steps": [
        ("Ablihi ang panid nga Study Stats ug mag-load ug backup",
         "Adto sa jwsync.org/highlights.html ug i-load ang imong .jwlibrary nga file. Basahon "
         "sa Resurface ang imong mga nota sa device mismo."),
        ("Tan-awa ang “Niining adlawa”",
         "Ipatungha sa Resurface ang mga notang imong gisulat niining petsaha sa milabayng mga "
         "tuig — “gisulat duha ka tuig na karong adlawa” — nga magsumpay nimo pag-usab sa "
         "milabayng pagtuon sa higayon nga labing makahuloganon."),
        ("Paghimo ug mubo nga pagsusi kada adlaw",
         "Magtanyag kini ug pipila ka nota nga balikan ug markahan nga nasusi na. Gamay apan "
         "subsob — mao kanay nagpabilin sa pagtuon, ug motubo ang streak samtang gihuptan nimo "
         "ang batasan."),
        ("Balik ugma",
         "Ang pagsubli nga may agwat magplano kon kanus-a motungha pag-usab ang mga nota, busa "
         "ang mga takos hinumdoman magpadayon sa pagbalik hangtod sila mahimong imo gyod."),
    ],
    "sections": [
        ("Nganong molihok ang pagsubli nga may agwat",
         "Ang pagsusi sa usa ka butang sa higayon nga hapit na nimo kini malimtan mas epektibo "
         "kay sa pagsag-ulo nga dungan. Pinaagi sa pagbahin-bahin sa pipila ka nota sa daghang "
         "adlaw, gihimo sa Resurface ang imong naa nang library nga padayon ug dili "
         "makahago nga pagsusi, nga hinay-hinayng nagpalalom sa imong natun-an."),
    ],
    "faq": [
        ("Asa gitipigan ang akong progreso sa pagsusi?",
         "Sa browser sa imong device — walay account ug walay gi-upload. Imo ra ang streak ug "
         "ang eskedyul."),
        ("Kinahanglan ba nakog bag-ong nota alang niini?",
         "Dili — molihok ang Resurface gamit ang mga notang imo nang gisulat. Kon mas daan ang "
         "imong library, mas makapalipay ang mga higayon nga “niining adlawa”."),
    ],
}

GUIDES_CEB["jw-library-achievements-streaks"] = {
    "title": "Mga streak, lebel ug kalampusan sa pagtuon sa JW Library",
    "h1": "Himoa ang imong pagtuon sa JW Library nga mga streak, lebel ug ganti",
    "description": "Tan-awa ang imong mga streak sa pagtuon, saka sa 60 ka lebel sa 12 ka "
                   "ang-ang sa imong Study Journey, ug ablihi ang mga 200 ka kalampusan — tanan "
                   "gibasa nga pribado gikan sa imong kaugalingong backup sa JW Library.",
    "intro": [
        "Ang pagkamakanunayon mao ang lisod nga bahin sa personal nga pagtuon, ug sayon "
        "pasagdan ang progreso nga dili makita. Himoon sa panid nga Study Stats ang kasaysayan "
        "sa imong backup nga usa ka butang nga imong makita nga motubo: mga streak, lebel ug "
        "ganti nga nagpakita sa pagtuon nga tinuod nimong gibuhat — walay gipatuman nga tumong, "
        "ang imong kaugalingong talaan lang nga gihimong makita.",
    ],
    "steps": [
        ("Ablihi ang panid nga Study Stats",
         "Adto sa jwsync.org/highlights.html ug i-load ang imong .jwlibrary nga backup. "
         "Kuwentahon ang tanan sulod sa imong browser."),
        ("Susiha ang imong mga streak",
         "Tan-awa ang imong labing taas ug kasamtangang streak sa pagtuon, ang imong ritmo "
         "matag semana, ug ang labing busy nga mga oras ug bulan — ang pitik sa imong batasan "
         "sa pagtuon."),
        ("Saka sa imong Study Journey",
         "Padayon sa 60 ka lebel sa 12 ka ginganlang ang-ang (gikan sa Liso hangtod sa "
         "Kanunayng Lunhaw), nga naay bola nga nag-usab ug kolor ug selebrasyon sa matag "
         "lebel, base sa tibuok nimong pagtuon."),
        ("Panguha ug mga kalampusan",
         "Ablihi ang mga 200 ka ganti gikan sa Komon ngadto sa Legendaryo, apil ang mga "
         "medalya nga may tema base sa sulod; ablihi ang bisan unsang medalya aron makita ang "
         "imong progreso paingon sa sunod."),
    ],
    "sections": [
        ("Pagdasig nga walay pit-os",
         "Dili kini mga tumong nga gibutang sa uban — salamin kini sa imo nang nabuhat. Ang "
         "pagkakita sa streak nga dili nimo gusto mabugto, o sa lebel nga hapit na maabot, "
         "usa ka malumo nga tulod aron ipadayon ang maayong batasan. Ug ang Shareable Card "
         "nagsumaryo sa imong tuig nga walay gipagawas nga bisan usa ka pribadong nota."),
    ],
    "faq": [
        ("Mag-update ba ang mga streak ug ganti sa ilang kaugalingon?",
         "Gipakita nila ang backup nga imong gi-load, busa paghimo ug bag-ong backup aron "
         "makita ang imong pinakabag-ong progreso. Walay modagan sa background."),
        ("Naay gipaambit o gi-upload ba niini?",
         "Wala. Kuwentahon ang tanan sa device gikan sa imong backup; ang sumaryo nga card lang "
         "ang mahimo nimong ipaambit, ug walay teksto sa bisan unsang nota niini."),
    ],
}

GUIDES_CEB["share-convention-assembly-notes"] = {
    "title": "Unsaon pagpaambit sa mga nota sa kombensiyon ug asembliya gikan sa JW Library",
    "h1": "Pagpaambit sa imong mga nota sa kombensiyon, asembliya ug tigom",
    "description": "Itunol ang imong mga nota sa kombensiyon, asembliya o tigom ngadto sa "
                   "pamilya ug mga higala isip gamay nga file — nga wala itugyan ang tibuok "
                   "nimong library ni ma-overwrite ang ila. Usa ka praktikal nga gamit sa "
                   "pagpaambit sa nota.",
    "intro": [
        "Nagnota kag maayo sa tibuok kombensiyon; malipay unta ang higala nga nakalaktaw ug "
        "sesyon; gusto sa mga paryente ang mga punto para sa ilang kaugalingong pagsusi. Sobra "
        "ra ang pagpadala sa tibuok backup ug mapapas niini ang mga nota sa modawat kon "
        "ipasig-uli. Ang pagpaambit sa nota magtugot nimo sa pagtunol gyod sa mga nota nga "
        "imong gusto — ug magtugot sa modawat nga huptan ang tanan nga anaa na niya.",
    ],
    "steps": [
        ("I-load ang imong backup sa panid sa pagpaambit",
         "Adto sa jwsync.org/share.html ug i-load ang imong .jwlibrary nga file."),
        ("Pilia ang mga nota lang sa kombensiyon",
         "Pilia ang tag sa hitabo gikan sa salaan sa tag sa tigpili ug nota ug i-press ang "
         "Pilia tanan — ang listahan mao na gyod ang mga notang imong gitagan. Mokuyog usab "
         "ang mga highlight nga nasumpay niadtong mga notaha."),
        ("Ipadala ang gamayng share file",
         "Maghimo ang JW Sync ug gamay nga file nga naay kanang mga notaha lang. Ipadala kini "
         "sumala sa imong gusto — messaging app, email, AirDrop. Walay server, walay account."),
        ("Idugang kini sa pamilya ug mga higala",
         "Ablihan sa matag usa ang samang panid, i-load ang imong file uban sa kaugalingong "
         "backup, ug makakuha ug bag-ong backup nga naay dugang nga imong mga nota. Wala gayod "
         "ma-overwrite ang ilang kaugalingong mga nota, ug naay tag ang imong na-import nga "
         "mga nota busa sayon silang pangitaon."),
    ],
    "sections": [
        ("Usa ka tag ug sayon na ang tanan",
         "Kon tagan nimo ang imong mga nota panahon sa hitabo (pananglitan, “Kombensiyon "
         "2026”), ang pagpili kanila unya usa lang ka klik sa salaan ug usa ka Pilia tanan. "
         "Bililhon ang pagsugod ug bag-ong tag sa sinugdanan sa bisan unsang kombensiyon, "
         "asembliya o linaing tigom tungod gyod niini."),
    ],
    "faq": [
        ("Mahimo ba nakong ipaambit sa daghang tawo nga dungan?",
         "Oo — file ra ang share file. Ipadala kini sa kadaghan sa tawo nga imong gusto; "
         "idugang kini sa matag usa sa kaugalingong library niya nga bulag."),
        ("Mapadayag ba ang tibuok nakong library?",
         "Dili. Ang mga nota lang nga imong gipili ang anaa sa file; magpabiling pribado ang "
         "uban pa sa imong library."),
    ],
}

GUIDES_CEB["share-jw-library-notes-by-tag"] = {
    "title": "Ipaambit lang ang mga nota sa JW Library ubos sa usa ka tag",
    "h1": "Pagpaambit lang sa mga nota nga nagdala sa usa ka tag",
    "description": "Magpadala ug usa ka hilisgotan, usa ka proyekto o ang para sa usa ka "
                   "estudyante imbes ang tibuok nimong library — ug mokuyog ang imong mga tag, "
                   "busa moabot sila nga nahan-ay sa pikas kilid.",
    "intro": [
        "Kasagaran ang tag mao ang natural nga sukod sa pagpaambit. Gitagan nimo ang tanan "
        "nimong natigom bahin sa usa ka hilisgotan, ang tanan gikan sa usa ka hitabo, o ang "
        "tanan nga imong gilatas uban sa usa ka tawo — ug kanang setiha, dili ang tibuok nimong "
        "library, ang tinuod nga gusto sa pikas.",
        "Nota-por-nota molihok ang pagpaambit sa nota sa JW Sync, busa ang tag mao lang ang "
        "listahan nga imong tsekan. Huptan sa mga nota ang ilang mga tag sa paggawas, nga "
        "nagpasabot nga masala sa modawat ang eksaktong samang set sulod sa iyang kaugalingong "
        "library unya.",
    ],
    "steps": [
        ("Siguroha nga naay tag ang mga nota",
         "Tagi sila sa JW Library samtang nagsulat ka, o ablihi ang imong backup sa Study "
         "Explorer sa jwsync.org ug gamita ang tag editor aron magdugang ug tag sa daghang "
         "nota nga dungan. Ang managsamang pagtag karon maoy maghimo sa pagpaambit nga usa ka "
         "minuto lang unya."),
        ("Ablihi ang panid sa pagpaambit ug i-load ang imong backup",
         "Adto sa jwsync.org/share.html, pilia ang Magpadala ug mga nota ug i-load ang imong "
         ".jwlibrary nga file. Basahon kini sa imong browser ug wala gayod mobiya sa imong "
         "device."),
        ("Pilia ang tag sa salaan, dayon Pilia tanan",
         "Ang tigpili ug nota naay salaan sa tag nga naglista sa matag tag sa imong backup uban "
         "ang gidaghanon sa nota ubos niini. Pilia ang imong tag ug mipig-ot ang listahan "
         "ngadto gyod niadtong mga notaha; tsekan silang tanan sa Pilia tanan. Mao na kanay "
         "tibuok pagpili — duha ka klik."),
        ("Himoa ang file ug ipadala kini",
         "Maghimo ang JW Sync ug gamayng share file nga naay gitsekan lang nga mga nota. "
         "Ipadala kini pinaagi sa chat, email o AirDrop — walay server nga nalambigit ug walay "
         "account sa bisan hain nga kilid."),
        ("Idugang niya kini sa iyang kaugalingong backup",
         "Ablihan niya ang samang panid, pilion ang Modawat, tan-awon ang mga nota, ug "
         "idugang sila sa iyang backup. Mokuyog ang imong mga tag sa mga nota, dugang ang tag "
         "para sa pag-import mismo, busa usa ka salaan lang ang gilay-on sa tibuok set para "
         "niya usab."),
    ],
    "sections": [
        ("Nganong tag ang ipaambit imbes backup",
         "Ang pagtugyan sa bug-os nga .jwlibrary nga backup naghatag sa tanan nga imong "
         "gisulat sukad, ug mapapas sa pagpasig-uli niini ang mga nota sa pikas. Ang "
         "pagpaambit sa tinagan nga pinili mao ang kaatbang sa duha: ang imong gipili lang "
         "ang iyang makita, ug walay mawala nga iya."),
        ("Pagpig-ot pa, o pagpaambit sa daghang tag",
         "Nagdungan sa paglihok ang salaan sa tag ug ang kahon sa pagpangita: pilia ang tag, "
         "dayon i-type ang usa ka pulong aron pig-oton pa, ug ang Pilia tanan magtsek gihapon "
         "sa anaa lang sa imong atubangan. Makit-an usab sa pagpangita ang ngalan sa tag, busa "
         "ang keyword nga gipaambit sa daghang tag magtigom kanila sa usa ka lakang. Ang matag "
         "nota sa listahan nagpakita sa mga tag niini, busa makita nimo ang imong ipadala sa "
         "dili pa nimo kini ipadala."),
        ("Mga tag nga takos huptan alang sa pagpaambit",
         "Bililhon ang paghupot ug pipila ka tag nga naglungtad lang aron ipaambit — ngalan sa "
         "usa ka hitabo, hilisgotan nga imong gisusi para sa uban, ang tawo nga imong kauban sa "
         "pagtuon. Kon moabot na ang panahon sa pagpadala, walay pangitaon: andam na ang set."),
    ],
    "faq": [
        ("Moadto ba sa pikas ang akong mga tag?",
         "Oo. Nagdala ang gipaambit nga mga nota sa ilang mga tag, ug ang pag-import naay "
         "kaugalingong tag, busa mahimo sa modawat nga pangitaon, susihon o kuhaon ang tibuok "
         "grupo unya."),
        ("Unsa man kon daghag tag ang usa ka nota?",
         "Motungha kini ubos sa matag usa kanila sa salaan, ug mokuyog ang tanan niining tag. "
         "Wala gayod tangtanga sa pag-salang sa usa ka tag ang uban."),
        ("Makuha ba sa akong library ang mga nota kon magpaambit ko?",
         "Dili. Kopyahon lang sa pagpaambit ang mga nota ngadto sa gamay nga file; wala "
         "matandog ang imong backup ug ang imong app."),
        ("Mahimo ba nakong ipadala ang samang tag sa daghang tawo?",
         "Oo — ordinaryong file ang share file. Ipadala kini sa kadaghan nga imong gusto, ug "
         "idugang kini sa matag usa sa kaugalingong library niya nga bulag."),
    ],
}

GUIDES_CEB["share-notes-with-bible-student"] = {
    "title": "Ipaambit ang mga nota sa JW Library sa estudyante sa Bibliya",
    "h1": "Pagpaambit sa mga nota sa pagtuon ngadto sa imong gitun-an sa Bibliya",
    "description": "Ipadala ang mga nota sa usa ka leksiyon — mga teksto, ilustrasyon, ang mga "
                   "puntong imong giandam — diretso ngadto sa kaugalingong JW Library sa "
                   "pikas, nga wala matandog ang iyang gisulat mismo.",
    "intro": [
        "Kon mag-andam kag pagtuon, kadaghanan sa buluhaton mosulod sa imong kaugalingong mga "
        "nota: ang dugang nga mga teksto, ang ilustrasyon nga nagpasabot sa punto, ang tubag sa "
        "pangutana niya sa milabayng semana. Laing butang ang pagbasa niini og kusog; laing "
        "butang ang pagbilin niya ug kopya nga iyang mabasa balik sa tibuok semana.",
        "Ibutang sa pagpaambit sa nota ang imong giandam nga mga nota sa iyang library isip "
        "tinuod nga mga nota sa JW Library, nasumpay sa samang parapo ug bersikulo — dili isip "
        "screenshot o mensahe nga iyang i-scroll lang.",
    ],
    "steps": [
        ("Andama ang mga nota sa leksiyon sa JW Library",
         "Isulat ang mga nota sama sa naandan, sa mga parapo ug teksto nga gisakop sa "
         "leksiyon. Hatagi sila ug tag — ang ngalan sa tawo, o ang publikasyon — aron sayon "
         "pilion ang set unya."),
        ("Ablihi ang panid sa pagpaambit ug i-load ang imong backup",
         "Paghimo ug backup (Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug "
         "backup), dayon ablihi ang jwsync.org/share.html, pilia ang Magpadala ug mga nota ug "
         "i-load ang file. Wala gayod kini mobiya sa imong device."),
        ("Tsekan ang mga nota alang niining leksiyona",
         "Salaa ang tigpili pinaagi sa tag nga imong gigamit ug i-press ang Pilia tanan, o "
         "pangitaa ug tsekan sila tagsa-tagsa. Himoa ang share file — magpabilin sa iyang "
         "lugar ang tanan pang uban sa imong library."),
        ("Ipadala kini ug giyahi siya sa pagdawat",
         "Kinahanglan una niya ug kaugalingong backup — Personal nga Pagtuon → Backup ug "
         "Pagpasig-uli → Paghimo ug backup. Dayon ablihan niya ang jwsync.org/share.html, "
         "pilion ang Modawat, i-load ang imong file ug ang iyang backup, ug i-download ang "
         "na-update nga backup."),
        ("Ipasig-uli niya kini sa JW Library",
         "Backup ug Pagpasig-uli → Ipasig-uli, pilion ang na-update nga file, ug motungha ang "
         "imong mga nota sa iyang library tapad sa iyang kaugalingon — tinagan, busa nahibalo "
         "siya kon hain ang gikan nimo."),
    ],
    "sections": [
        ("Wala gayod ma-overwrite ang iyang mga nota",
         "Mao kini ang hinungdanong kalainan sa pagpadala ug backup. Ang pagpasig-uli mopuli "
         "sa tibuok library sa usa ka device; ang pagdawat sa gipaambit nga nota magdugang "
         "niini. Ang tanan nga iyang gisulat mismo — apil sa samang mga parapo — magpabilin "
         "gyod sama sa una."),
        ("Usa ka lingguhanong ritmo nga duha ka minuto",
         "Kon nabuhat na ninyong duha kini sa unang higayon, mubo na ang rutina: mag-andam, "
         "mag-tsek, magpadala, magpasig-uli. Alang sa daghan, mas sayon ang pagpadala sa mga "
         "nota dayon human sa pag-andam, aron anaa na sa estudyante sa dili pa ang pagtuon "
         "imbes human."),
    ],
    "faq": [
        ("Kinahanglan ba ang estudyante ug account o naka-install nga app?",
         "Walay account bisan asa, ug walay i-install gawas sa JW Library mismo — ordinaryong "
         "web page ang panid sa pagpaambit."),
        ("Unsa man kon wala pa gyod makahimo ug backup ang estudyante?",
         "Maghimo siya ug usa una, sa JW Library ubos sa Personal nga Pagtuon → Backup ug "
         "Pagpasig-uli. Bisan ang library nga daw walay sulod molihok; ang backup mao ang "
         "dugangan sa gipaambit nga mga nota."),
        ("Mahimo ba nakong bawion ang mga nota unya?",
         "Imo ang file samtang wala pa nimo ipadala. Kon anaa na sa uban, iya na kana, sama sa "
         "bisan unsang mensahe — busa ipaambit lang ang imong komportableng ipaambit sa "
         "sinulat."),
    ],
}

GUIDES_CEB["share-meeting-notes-with-family"] = {
    "title": "Ipaambit ang mga nota sa tigom sa imong pamilya o panimalay",
    "h1": "Pagpaambit sa mga nota sa tigom karong semanaha sa pamilya",
    "description": "Naay nasakit, nagtrabaho o wala didto — ipadala kaniya ang mga nota sa "
                   "semana isip gamayng file nga iyang madugang sa kaugalingong JW Library, "
                   "nga walay mawala kaninyong duha.",
    "intro": [
        "Sa kadaghanan sa panimalay, ang matag usa naay kaugalingong nota sa kaugalingong "
        "device, ug kanunayng naay makalaktaw ug tigom. Kausa ra molihok ang pagbasa sa imong "
        "mga nota sa panihapon; ang pagbutang niini sa library sa pikas mao ang magtugot niya "
        "sa paggamit sa materyal unya, sa dapit nga iyang pangitaan gyod.",
        "Tungod kay nota-por-nota ang pagpaambit imbes backup-por-backup, mahimong magbayloay "
        "ug nota ang daghang tawo nga walay ma-overwrite nga library ni bisan kinsa.",
    ],
    "steps": [
        ("I-backup ang device diin ka nagnota",
         "JW Library → Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup."),
        ("Pilia ang mga nota sa semana",
         "Sa jwsync.org/share.html pilia ang Magpadala ug mga nota, i-load ang imong backup, "
         "ug tsekan ang mga nota karong semanaha — paspas silang matigom pinaagi sa pagpangita "
         "sa publikasyon, ug kon tagan nimo ang mga nota sa semana, tigumon sila sa salaan sa "
         "tag sa usa ka klik."),
        ("Ipadala kini sa chat sa pamilya",
         "Himoa ang share file ug ipadala kini sa paagi nga gigamit na sa panimalay — "
         "messaging app, email, AirDrop. Gamay nga file kini nga naay gitsekan lang nga mga "
         "nota."),
        ("Idugang kini sa matag usa sa kaugalingong backup",
         "Ablihan niya ang samang panid, pilion ang Modawat, i-load ang imong file uban sa "
         "kaugalingong backup, i-download ang na-update nga backup ug ipasig-uli kini sa JW "
         "Library."),
    ],
    "sections": [
        ("Magpabiling iya ang library sa matag usa",
         "Walay mapulihan nga nota ni bisan kinsa, ug walay kinahanglang motugyan sa tibuok "
         "library aron makaapil. Moabot ang na-import nga mga nota ubos sa usa ka tag, busa "
         "makita dayon sa matag usa kon hain nga nota ang gikan sa uban ug mapapas niya ang "
         "grupo unya kon dili niya gusto huptan."),
        ("Pamilyahanong pagsimba: pagtigom imbes pagkatag",
         "Molihok usab ang samang kagamitan sa pikas direksiyon. Kon ang tanan magnota panahon "
         "sa pamilyahanong pagsimba, mahimong tigumon sa usa ka tawo ang share file sa uban "
         "ngadto sa usa ka backup ug makabaton sa gihiusang nota sa panimalay sa samang "
         "materyal."),
    ],
    "faq": [
        ("Makaapil ba ang mga device sa mga bata?",
         "Makaapil ang bisan unsang device nga makadagan sa JW Library ug makaabli ug web "
         "page. Managsama ang mga lakang sa cellphone, tablet o kompyuter."),
        ("Kinahanglan ba nga managsama mi ug plataporma?",
         "Dili. Managsama ang format sa backup sa Android, iPhone, iPad ug sa Windows app, "
         "busa motabok ang mga nota nga walay conversion."),
    ],
}

GUIDES_CEB["receive-shared-jw-library-notes"] = {
    "title": "Naay nagpadala nakog mga nota sa JW Library — unsaon nako pag-abli?",
    "h1": "Pagdugang sa imong kaugalingong JW Library sa mga nota nga gipaambit kanimo",
    "description": "Naay gipadala nga file sa gipaambit nga nota o bloke sa teksto. Ania kon "
                   "unsaon kini pagtan-aw ug pagdugang sa imong kaugalingong backup sa JW "
                   "Library nga walay bisan usa nimong nota nga mawala.",
    "intro": [
        "Moabot ang gipaambit nga nota sa JW Library isip gamayng file (nga matapos sa "
        ".jwshare.json) o isip blokeng teksto nga gitapot sa mensahe. Dili maablihan sa JW "
        "Library ang bisan hain niini — apan dili pod nimo kini kinahanglan. Basahon sa kilid "
        "nga modawat sa JW Sync ang gipaambit nga mga nota, ipakita ang sulod niini, ug isulat "
        "sila sa usa ka backup nimo.",
        "Mahitabo sa imong device ang tibuok pagbayloay. Walay account, walay gi-upload, ug "
        "madugangan lang ang imong kaugalingong mga nota, wala gayod pulihi.",
    ],
    "steps": [
        ("Paghimo una ug backup sa imong kaugalingong library",
         "Sa JW Library: Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup. "
         "Mao kini ang file nga dugangan sa gipaambit nga mga nota, busa angay kining bag-o."),
        ("Ablihi ang panid sa pagpaambit ug pilia ang Modawat",
         "Adto sa jwsync.org/share.html ug pilia ang Modawat ug mga nota."),
        ("I-load ang gipadala kanimo",
         "Pilia ang .jwshare.json nga file, o itapot ang gipaambit nga teksto diretso sa kahon "
         "kon miabot kini isip mensahe. Sa bisan hain nga paagi, makakita kag read-only nga "
         "pagtan-aw sa matag nota sa dili pa masulat ang bisan unsa."),
        ("Idugang sila sa imong backup",
         "I-load ang imong kaugalingong backup, pilia ang tag nga dad-on sa na-import nga mga "
         "nota, ug idugang sila. Maghimo ang JW Sync ug na-update nga backup nga imong "
         "i-download."),
        ("Ipasig-uli ang na-update nga backup sa JW Library",
         "Personal nga Pagtuon → Backup ug Pagpasig-uli → Ipasig-uli, pilia ang na-update nga "
         "file. Anaa na sa imong library ang gipaambit nga mga nota, sa hustong parapo ug "
         "bersikulo."),
    ],
    "sections": [
        ("Walay imoha nga mapulihan",
         "Idugang ang gipaambit nga mga nota isip bag-ong nota. Bisan kon modapo ang usa ka "
         "gipaambit nga nota sa parapo nga imo nang gisulatan, mabuhi ang duha — buo ang imoha, "
         "tapad ang iya. Ang hinumdoman lang mao ang naandang lagda sa pagpasig-uli: ipasig-uli "
         "ang na-update nga backup, dili ang mas daan."),
        ("Nausab ang imong hunahuna unya?",
         "Nagdala ang matag na-import nga nota sa tag nga imong gipili sa dihang gidugang nimo "
         "sila. Ablihi ang imong backup sa Study Explorer, salaa pinaagi nianang taga, ug "
         "masusi o mapapas nimo ang tibuok grupo sa usa ka lakang."),
    ],
    "faq": [
        ("Miabot ang file nga giilisan ug .txt o miabli isip teksto — daot ba kini?",
         "Dili. Kanunay kining buhaton sa mga messaging app. Kopyaha ang teksto ug itapot kini "
         "sa kahon sa Modawat; parehas gyod ang paglihok."),
        ("Kinahanglan ba nako ang tibuok backup sa nagpadala?",
         "Dili. Ang share file naay sulod lang nga mga nota nga iyang gipili ipadala — wala "
         "nay lain gikan sa iyang library."),
        ("Naay gi-upload ba kon tan-awon nako ang mga nota?",
         "Wala. Ang pagbasa sa gipaambit nga file, ang pagtan-aw niini ug ang pagsulat sa "
         "na-update nga backup mahitabo tanan sa browser sa imong device."),
    ],
}

GUIDES_CEB["share-notes-with-study-group"] = {
    "title": "Ipaambit ang mga nota sa panukiduki sa usa ka study group",
    "h1": "Pagpaambit sa panukiduki sa usa ka grupo — ug pagtigom sa ila",
    "description": "Usa ka file, daghang tawo: ipadala ang usa ka set sa nota sa panukiduki sa "
                   "tanan nga nagtuon sa samang hilisgotan, ug tigumon ang ilang gipadala "
                   "balik ngadto sa usa ka set nga imoha.",
    "intro": [
        "Kon daghan ang nagkalot sa samang hilisgotan, kasagaran magkatag ang panukiduki — ang "
        "usa nakakita sa mga cross-reference, ang lain sa makasaysayanong luyo, ang ikatulo sa "
        "mga ilustrasyon. Lahi ra kaayo ang pagbasa sa screenshot sa usag usa kay sa pagbaton "
        "sa materyal sa kaugalingong library, sa samang mga bersikulo, ug mapangitaan pa sa "
        "sunod tuig.",
        "Tungod kay file ra ang share file, usa ka export igo na sa tibuok grupo, ug ang "
        "samang paagi magdala balik kanimo sa ilang buhat.",
    ],
    "steps": [
        ("Tagi ang imong panukiduki samtang nagtigom ka",
         "Hatagi ug tag ang hilisgotan sa JW Library aron magpabiling tingob ang set. Sa Study "
         "Explorer, mahimo kang magdugang ug tag sa daghang nota nga tinapok kon wala nimo "
         "kini nabuhat kaniadto."),
        ("Paghimo ug usa ka share file para sa grupo",
         "Sa jwsync.org/share.html pilia ang Magpadala ug mga nota, i-load ang imong backup, "
         "kuhaa ang tag sa hilisgotan sa salaan, i-press ang Pilia tanan ug himoa ang file."),
        ("I-post kini kausa lang",
         "Ipadala ang samang file sa tanan — group chat, email ngadto sa daghan, kon unsa nay "
         "gigamit sa grupo. Walay setup matag tawo ug walay kopya sa server."),
        ("Pangayoa ang ila isip balos",
         "Mahimo sa matag usa ang samang butang sa iyang kilid. Idugang sa imong backup ang "
         "matag file nga imong madawat sa tinagsa, nga naay kaugalingong tag ang matag "
         "pag-import — maayo ang ngalan sa nagpadala — aron kanunay nimong mahibaloan kang "
         "kinsa ang matag panukiduki."),
    ],
    "sections": [
        ("Usa ka gihiusang set, apan mailhan gihapon ang tinubdan",
         "Human sa pipila ka hugna, anaa na sa imong kaugalingong library ang tibuok panukiduki "
         "sa grupo bahin sa hilisgotan, sa hustong parapo ug bersikulo, ug tinagan ang matag "
         "amot sumala sa tinubdan. Makit-an sa pagpangita ang tanan nga dungan; ang mga tag "
         "magtugot nimo sa pagbulag kanila pag-usab bisan kanus-a nimo gusto."),
        ("Walay kinahanglang magpadayag sa iyang library",
         "Ang gitsekan lang sa matag usa ang iyang ipaambit. Wala gayod mosulod sa file ang "
         "uban pa sa library sa matag tawo — personal nga pagtuon, pribadong pahinumdom, ug ang "
         "tanan pang uban."),
    ],
    "faq": [
        ("Naay limitasyon ba kon pila ka nota ang mapaambit nako nga dungan?",
         "Sa praktika, wala. Gagmay ang mga nota; bisan ang dakong set maghatag gihapon ug "
         "file nga imong ikapadala sa usa ka mensahe."),
        ("Unsa man kon duha ka tawo ang magpadala nako sa samang nota?",
         "Makita nimo kini kaduha, ang matag usa ubos sa tag sa nagpadala. Sayon ra sa "
         "pagpangita sa Study Explorer nga mamatikdan ug mapapas ang halos managsamang nota."),
        ("Mahimo bang modawat nga walay ipadala balos?",
         "Oo. Bulag ang pagdawat ug ang pagpadala — walay obligado nga mopaambit aron "
         "makadugang sa iyang nadawat."),
    ],
}

GUIDES_CEB["share-talk-preparation-notes"] = {
    "title": "Itunol ang panukiduki luyo sa usa ka pakigpulong o asaynment",
    "h1": "Pagtunol sa imong panukiduki sa pakigpulong ug asaynment",
    "description": "Ikaw ang nagkalot para sa usa ka pakigpulong, bahin o asaynment. Ania kon "
                   "unsaon pagtunol sa panukiduki ngadto sa mosunod nga magkinahanglan niini — "
                   "isip tinuod nga mga nota sa iyang library, o isip yanong teksto para sa "
                   "dokumento.",
    "intro": [
        "Panagsa ra magamit kausa lang ang pag-andam. Ang mga tekstong imong gipangita, ang "
        "luyo nga imong gibasa, ang paagi nga sa kataposan imong gipili sa pagpahayag sa usa ka "
        "punto — mas gusto sa mosunod nga molatas sa samang materyal nga magsugod didto kay sa "
        "blangkong panid.",
        "Duha ka paagi ang gihatag sa JW Sync aron itunol kini, ug lahi ang kaangayan nila sa "
        "lainlaing tawo: isip mga nota nga modapo sa JW Library sa pikas, o isip yanong teksto "
        "nga iyang itapot sa dokumento.",
    ],
    "steps": [
        ("Tigoma ang panukiduki ubos sa usa ka tag",
         "Samtang nag-andam ka, tagi ang mga nota sumala sa tema o sa asaynment. Kon nasulat "
         "na sila ug walay tag, ablihi ang imong backup sa Study Explorer ug tagi silang tanan "
         "sulod sa pipila ka minuto."),
        ("Hukmi kon unsang porma ang haom sa pikas",
         "Ang nagtuon sa JW Library gusto ug mga nota sa iyang library. Ang naghimo ug "
         "dokumento gusto ug teksto. Mahimo nimong buhaton ang duha gikan sa samang set."),
        ("Aron magpadala ug nota: gamita ang panid sa pagpaambit",
         "Sa jwsync.org/share.html pilia ang Magpadala ug mga nota, i-load ang imong backup, "
         "salaa pinaagi sa tag nga imong gigamit ug i-press ang Pilia tanan, dayon himoa ang "
         "file. Idugang niya kini sa kaugalingong backup ug ipasig-uli — wala matandog ang "
         "iyang kaugalingong mga nota."),
        ("Aron magpadala ug teksto: mag-export gikan sa Study Explorer",
         "Salaa ngadto sa samang set ug kopyaha o i-export kini isip Markdown o yanong teksto. "
         "Magpabilin ang pormat, busa magpabiling nahan-ay ang nahan-ay nga balangkas kon "
         "itapot sa dokumento."),
    ],
    "sections": [
        ("Pagbilin ug kopya para sa imong kaugalingon, sa porma nga imong makit-an pag-usab",
         "Bililhon usab nga tipigan ang samang export para sa imong kaugalingong gamit. Ang "
         "tag dugang sa gilay-on sa petsa maghimo sa tibuok pag-andam nga makit-an pa human sa "
         "mga tuig, nga mao gyoy panahon nga imo kining kinahanglanon — ug ang pagkuha pinaagi "
         "sa petsa sa Study Explorer maghimo sa bisan unsang yugto sa panahon nga kaugalingong "
         "file."),
    ],
    "faq": [
        ("Magpabilin ba nga nasumpay sa hustong bersikulo ang mga teksto?",
         "Oo — huptan sa gipaambit nga mga nota ang parapo ug bersikulo nga ilang gikasumpayan, "
         "busa modapo sila sa hustong dapit sa library sa pikas."),
        ("Mahimo ba nakong ipaambit ang mga nota nga naay highlight?",
         "Oo. Mokuyog ang mga highlight nga nasumpay sa mga notang imong gipaambit."),
    ],
}

GUIDES_CEB["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Pag-andam sa tigom gamit ang mga notang imo nang gisulat",
    "h1": "Lingguhanong pag-andam gamit ang mga nota nga anaa na nimo",
    "description": "Natun-an na nimo kining materyala kaniadto. Ania ang mubo nga lingguhanong "
                   "rutina nga magpatungha sa imong daang mga nota, highlight ug tubag bahin sa "
                   "samang publikasyon sa dili pa ka mag-andam pag-usab.",
    "intro": [
        "Kadaghanan mag-andam matag semana gikan sa blangkong panid, bisan pag nakasulat na sila "
        "bahin sa samang hilisgotan — usahay sa samang teksto — sa makadaghang higayon. Anaa sa "
        "imong library kanang naunang hunahuna; ang problema lang mao nga walay nagdala niini "
        "balik kanimo sa hustong higayon.",
        "Giayo kini sa lima ka minuto nga rutina sa sinugdanan sa pag-andam, ug walay lain "
        "kining gamiton gawas sa backup nga anaa na nimo.",
    ],
    "steps": [
        ("Pag-load ug bag-ong backup sa Study Explorer",
         "Paghimo ug backup sa JW Library, dayon ablihi kini sa jwsync.org. Basahon ang tanan "
         "sulod sa imong browser."),
        ("Pangitaa ang hilisgotan sa dili pa magsugod",
         "Pangitaa ang teksto sa tema, ang hilisgotan o ang publikasyon. Motungha nga tingob "
         "ang tanan nimong gisulat bahin niini sa milabayng mga tuig, sa matag publikasyon nga "
         "gigikanan niini."),
        ("Susiha ang imong mga tubag sa pagtuon",
         "Gitigom sa panglantaw nga Mga Tubag sa Pagtuon ang mga tubag nga imong gi-type sa mga "
         "pangutana, busa anaa ang milabayng mga paglatas sa samang materyal aron patungnan "
         "imbes subson."),
        ("Idugang ang nakulang, dayon ibalik kini",
         "Mahimong i-edit o himoon ang mga nota didto mismo — ulohan, teksto, tag, kolor sa "
         "highlight. I-export ang na-edit nga backup ug ipasig-uli kini sa JW Library, ug anaa "
         "na sa app ang imong pag-andam alang sa tigom."),
    ],
    "sections": [
        ("Nganong hinungdanon ang daang mga nota",
         "Ang pagsusi sa imong nahukman sa milabay maghimo sa pag-andam nga nagtapok. Mohunong "
         "ka sa pagdiskobre pag-usab sa samang mga punto ug magsugod sa pagtukod ibabaw "
         "kanila — ug ang mga nota nga imong idugang karong semanaha mahimong sinugdanan sa "
         "sunod nga hugna."),
        ("Usa ka mas malumo nga bersiyon: pasagdi nga moduol kanimo ang mga nota",
         "Kon morag trabaho ang lingguhanong pagpangita, ang Resurface sa panid nga Study Stats "
         "magdala mismo ug pipila ka daang nota matag adlaw, apil ang imong gisulat niining "
         "petsaha sa milabayng mga tuig. Samang kaayohan, walay rutina nga hinumdoman."),
    ],
    "faq": [
        ("Direktang mausab ba ang akong library kon mag-edit ko sa browser?",
         "Dili. Mag-export kag na-update nga backup ug ipasig-uli kini sa JW Library — mausab "
         "lang ang app pinaagi sa pagpasig-uli nga ikaw mismo ang mobuhat."),
        ("Gi-upload ba ang akong backup kon mangita ko niini?",
         "Wala. Basahon ang file sulod sa imong browser; walay ipadala bisan asa."),
    ],
}

GUIDES_CEB["print-jw-library-notes"] = {
    "title": "Unsaon pag-print sa imong mga nota sa JW Library",
    "h1": "Pagdala sa imong mga nota sa JW Library ngadto sa papel",
    "description": "Walay print button ang JW Library. I-export ang imong mga nota isip teksto "
                   "o Markdown, itapot sa bisan unsang dokumento, ug i-print — usa ka talaan "
                   "sa pagtuon, set sa nota para sa walay app, o tipiganan.",
    "intro": [
        "Walay paagi sa pag-print gikan sa JW Library, ug lisod basahon ang screenshot sa "
        "screen sa cellphone. Apan imo ang mga nota, ug sayon ra silang ibutang sa "
        "mai-print nga dokumento kon mabasa na nimo ang backup nga file.",
        "Basahon sa Study Explorer ang .jwlibrary nga backup sa imong browser ug tugotan ka nga "
        "kopyahon o i-export ang bisan unsang pinili nga mga nota isip yanong teksto o Markdown "
        "— nga nasabtan na sa matag word processor, notes app ug printer.",
    ],
    "steps": [
        ("Paghimo ug backup ug ablihi kini",
         "JW Library → Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup, "
         "dayon i-load ang file sa jwsync.org."),
        ("Pig-ota ngadto sa imong gusto sa papel",
         "Salaa pinaagi sa publikasyon, tag, kolor sa highlight o gilay-on sa petsa, o pangitaa "
         "ang usa ka hilisgotan. Mahimo ang pag-print sa tanan, apan kasagaran mas mapuslanong "
         "dokumento ang gikan sa sinala nga set."),
        ("Kopyaha o i-export isip teksto o Markdown",
         "Ipagawas ang pinili isip Markdown o yanong teksto. Magpabilin ang bold, italic ug "
         "listahan, busa magpabiling nahan-ay sa panid ang mga notang nahan-ay."),
        ("Itapot sa dokumento ug i-print",
         "Bisan unsang word processor o notes app haom na. Han-aya ang mga ulohan ug margin "
         "sumala sa imong gusto, dayon i-print o itipig isip PDF."),
    ],
    "sections": [
        ("Paghimo ug talaan sa pagtuon",
         "Ang gilay-on sa petsa mao ang natural nga sukod alang sa giimprintang talaan — usa ka "
         "tuig nga nota, o ang yugto nga naglangkob sa usa ka publikasyon. Ang pagkuha pinaagi "
         "sa petsa maghatag kanimo ug limpyo ug sunod-sunod nga set nga i-print o bugkoson, nga "
         "makapalipay bation gawas sa screen."),
        ("Pag-print para sa wala mogamit sa app",
         "Dili tanan magtuon gikan sa device. Tinuod nga mapuslanon ang giimprintang set sa "
         "nota bahin sa kasamtangang materyal alang sa mas gusto ug papel, ug samang duha ka "
         "minuto lang kini sama sa bisan unsang export."),
    ],
    "faq": [
        ("Mahimo ba nakong i-print pod ang akong mga highlight?",
         "Gilista sa panglantaw sa highlight ang mga bahin nga imong gimarkahan, ug makopya "
         "usab kanang listahana isip teksto uban sa imong mga nota."),
        ("Naay mausab ba sa JW Library kon mag-export ko?",
         "Wala. Usa ka kopya sa imong backup ang basahon sa pag-export; wala matandog ang imong "
         "orihinal nga file ug ang app."),
    ],
}

GUIDES_CEB["clean-up-duplicate-jw-library-notes"] = {
    "title": "Hinloi ang doble ug walay sulod nga mga nota sa JW Library",
    "h1": "Paghinlo sa doble nga nota, walay sulod nga nota ug kagubot",
    "description": "Nakapasig-uli kag backup kaduha, o na-import pag-usab ang samang mga nota? "
                   "Susihon sa Library Doctor ang imong .jwlibrary nga file sa browser, "
                   "pangitaon ang mga doble ug walay sulod nga nota, ug maghatag ug limpyo nga "
                   "kopya.",
    "intro": [
        "Nagtipon ug kagubot ang mga library. Ang pagpasig-uli ug backup sa device nga naay "
        "bahin na sa samang mga nota, ang pag-import kaduha sa gipaambit nga set, o ang "
        "tuig-tuig nga tunga-tungang nota nga wala nahuman — ang matag usa nagbilin ug butang, "
        "ug walay paagi sa JW Library aron silhigon kining tanan nga tinapok.",
        "Usa ka libreng health check para sa .jwlibrary nga file ang Library Doctor. Susihon "
        "niini ang backup sa imong browser, isulti sa yano nga pinulongan ang nakit-an niini, "
        "ug ayohon sa usa ka tap ang maayohan.",
    ],
    "steps": [
        ("Pag-backup una — sama sa kanunay",
         "JW Library → Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup. "
         "Huptan kining file; kini ang imong andam nga kopya."),
        ("Padagana ang health check",
         "Ablihi ang jwsync.org, i-load ang backup ug sugdi ang Library Doctor. Susihon niini "
         "ang sulod ug istruktura sa file nga wala kini ipadala bisan asa."),
        ("Basaha ang iyang nakit-an",
         "Tin-aw nga gilista ang mga doble, walay sulod nga nota ug uban pang kagubot, uban "
         "ang gidaghanon, aron makita nimo ang gidak-on sa problema sa dili pa nimo usbon ang "
         "bisan unsa."),
        ("Ayoha ug i-download ang limpyo nga kopya",
         "Usa ka tap ang mopadapat sa mga pag-ayo ug maghimo ug bag-o, nahinloan nga .jwlibrary "
         "nga file. Wala gayod usba ang imong orihinal."),
        ("Ipasig-uli ang limpyo nga file",
         "Backup ug Pagpasig-uli → Ipasig-uli, ug pilia ang nahinloan nga file. Mao gihapon "
         "ang imong library, gawas sa kagubot."),
    ],
    "sections": [
        ("Asa gikan ang mga doble",
         "Halos kanunay gikan sa pagpasig-uli. Kon magpasig-uli kag backup sa device nga naay "
         "bahin na sa samang materyal — o magpasig-uli sa samang file kaduha pinaagi sa "
         "lainlaing dalan — walay paagi ang app aron mahibaloan nga nakita na niya kadtong mga "
         "notaha."),
        ("Ang paghiusa mao ang paagi aron malikayan sila",
         "Mao gyoy hinungdan nganong mas luwas ang paghiusa sa duha ka backup kay sa "
         "pagpasig-uli sa usa ibabaw sa lain: mamatikdan sa paghiusa ang materyal nga naa na ug "
         "usa ra ang huptan. Modagan ang samang pagsusi sulod sa matag paghiusa, busa limpyo "
         "ang mogula nga gihiusang backup bisan kon dili limpyo ang mga file nga misulod."),
    ],
    "faq": [
        ("Papason ba niini ang mga nota nga gusto gyod nako?",
         "Kuhaon niini ang eksaktong doble ug ang walay sulod nga nota — mga butang nga walay "
         "mawala. Ug tungod kay bag-ong file ang isulat niini imbes usbon ang imoha, anaa "
         "kanunay ang orihinal nga mabalikan."),
        ("Mabawi ba niini ang mga nota nga akong gipapas sa app?",
         "Dili. Kon gipapas ang usa ka nota sa JW Library sa dili pa nahimo ang backup, wala "
         "kini sa file aron mabawi — ang mas daang backup ang dapit nga pangitaan."),
    ],
}

GUIDES_CEB["backup-jw-library-before-phone-repair"] = {
    "title": "Pag-backup sa JW Library sa dili pa ang factory reset o pag-ayo",
    "h1": "Sa dili pa ang factory reset, pag-ayo o pagbaligya sa cellphone",
    "description": "Papason sa reset ang mga nota sa JW Library uban sa tanan, ug dili sila "
                   "dad-on sa mga tool sa pagbalhin. Paghimo ug backup, siguroha nga moabli "
                   "gyod kini, dayon mag-reset nga walay meligro.",
    "intro": [
        "I-reset ang cellphone, ipaayo kini, o ihatag sa uban, ug mokuyog ang datos sa personal "
        "nga pagtuon sa JW Library. Mobalik ang mga hulagway ug app gikan sa cloud backup; ang "
        "tuig-tuig nga nota, highlight ug bookmark kasagaran dili, kay gilaktawan sa mga tool sa "
        "pagbalhin ang pribadong datos sa app.",
        "Lima ka minuto ra ang solusyon, ug ang lakang nga gilaktawan sa daghan mao gyoy labing "
        "hinungdanon: ang pagsusi nga mabasa gyod ang backup nga file sa dili pa mapapas ang "
        "device.",
    ],
    "steps": [
        ("Himoa ang backup",
         "JW Library → Personal nga Pagtuon → Backup ug Pagpasig-uli → Paghimo ug backup. "
         "Makakuha kag .jwlibrary nga file — kasagaran pipila ra ka megabyte."),
        ("Ipagawas kini sa device",
         "I-email kini sa imong kaugalingon, o ibutang sa Drive, iCloud o sa folder sa "
         "kompyuter. Ang backup nga anaa lang sa cellphone nga imong papason dili backup."),
        ("Siguroha nga moabli kini sa dili pa ka magpapas ug bisan unsa",
         "I-load ang file sa jwsync.org ug tan-awa kini — kinahanglang anaa ang tanang nota, "
         "highlight ug bookmark, ug ipahibalo sa health check ang bisan unsang sayop sa file. "
         "Mao kini ang tibuok tuyo sa buluhaton: ulahi na kaayo ang pagkahibalo human nga dili "
         "diay mabasa ang file."),
        ("Mag-reset, dayon magpasig-uli",
         "Human sa reset o pag-ayo, i-install ang JW Library, mag-sign in, dayon Backup ug "
         "Pagpasig-uli → Ipasig-uli ug pilia ang imong file."),
        ("Migamit kag hinulaman nga cellphone sa taliwala? Hiusaha, ayaw i-overwrite",
         "Kon nagnota ka sa temporaryong device, i-backup pod kana ug hiusaha ang duha ka file "
         "sa jwsync.org sa dili pa magpasig-uli — kay kon dili, papason sa pagpasig-uli sa daang "
         "backup ang tanan nimong gisulat samtang naghulat ka."),
    ],
    "sections": [
        ("Nganong takos ang dugang nga usa ka minuto sa pagsusi",
         "Ang naputol nga pagbalhin, ang cloud drive nga nakadaot sa file, ug ang extension nga "
         "nailisan sa dalan tanan naghimo ug mga backup nga daw maayo ra sa folder apan "
         "mapakyas sa pagpasig-uli. Ang pag-abli sa file una maghimo sa hilom nga problema nga "
         "problema nga imong maayo pa, samtang anaa pa ang datos sa orihinal nga device."),
        ("Huptan ang file human sa pagpasig-uli",
         "Ayaw kini papasa kon molihok na ang bag-ong device. Ang daang mga backup mao lang ang "
         "dalan pabalik kon aksidenteng mapapas ang usa ka nota human sa pipila ka bulan, ug "
         "wala silay bayad sa pagtipig."),
    ],
    "faq": [
        ("Mobalik ba ang akong na-download nga mga publikasyon?",
         "Nagdala ang backup sa imong datos sa personal nga pagtuon — mga nota, highlight, "
         "bookmark, tag ug playlist. Ma-download lang pag-usab ang mga publikasyon human "
         "niana."),
        ("Molihok ba ang file kon mag-ilis kog brand sa cellphone o plataporma?",
         "Oo. Managsama ang .jwlibrary nga format sa Android, iPhone, iPad ug Windows."),
    ],
}

GUIDES_CEB["jw-library-notes-missing-after-update"] = {
    "title": "Nawala ang mga nota sa JW Library human sa update o pag-install pag-usab",
    "h1": "Nawala ang mga nota human sa update, pag-install pag-usab o pagpasig-uli",
    "description": "Nawala ang imong mga nota human sa update, pag-install pag-usab o "
                   "pag-sign in pag-usab. Unsay buhaton una, unsay dili buhaton, ug unsaon "
                   "pagbawi kanila nga walay mawala sa imong gisulat sukad niadto.",
    "intro": [
        "Dili maayong higayon: moabli ang JW Library, ug wala ang mga nota. Sa dili pa ang "
        "tanan, usa ka tambag — ayaw pagdali. Kadaghanan sa naghimo niining kahimtanga nga dili "
        "mabawi mahitabo sa unang napulo ka minuto, pinaagi sa pag-overwrite gyod sa backup nga "
        "naay sulod pa sa nawalang mga nota.",
        "Sunda ang mga lakang sa ubos sumala sa han-ay. Ang tumong mao ang pagtapos nga naay "
        "usa ka file nga naglangkob sa daang mga nota ug sa tanan nga imong gisulat sukad "
        "niadto.",
    ],
    "steps": [
        ("Ayaw usa i-overwrite ang imong mga backup",
         "Likayi ang paghimo ug bag-ong backup ibabaw sa daan, ug ayaw pagpasig-uli sa bisan "
         "unsa nga walay pagsusi. Ang mas daang backup nga file mao ang labing lagmit nga dapit "
         "diin anaa pa ang imong mga nota."),
        ("Pangitaa ang pinakabag-ong backup nga anaa nimo",
         "Susiha ang mga attachment sa email, Google Drive, iCloud Drive, ang downloads folder "
         "sa imong kompyuter, ug ang bisan unsang laing device diin ka nagpasig-uli. Gagmay "
         "ang mga backup, busa kasagaran mas daghan ang kopya kay sa mahinumdoman."),
        ("Tan-awa ang sulod sa file sa dili pa kini ipasig-uli",
         "I-load ang kandidatong file sa jwsync.org ug tan-awa kon unsa gyoy sulod niini — pila "
         "ka nota, gikan sa unsang publikasyon, hangtod sa unsang petsa. Kana ang magsulti "
         "kanimo kon husto ba ang file, sa dili pa ka mopadayon sa pagpasig-uli."),
        ("I-backup pod ang kasamtangang device",
         "Bisan kon daw walay sulod, i-backup kini. Kon naay imong gisulat sukad nawala ang mga "
         "nota, kanang file ra ang bugtong kopya niini."),
        ("Hiusaha ang duha, dayon magpasig-uli",
         "Hiusaha ang daang backup ug ang kasamtangan sa jwsync.org. Ang resulta naay sulod nga "
         "nabawing mga nota ug ang tanan nga gisulat sukad niadto, nga usa ra ang gihuptan sa "
         "mga doble. Ipasig-uli kanang gihiusang file — dili gayod ang daang backup nga "
         "nag-inusara."),
    ],
    "sections": [
        ("Nganong sayop ang pagpasig-uli sa daang backup nga nag-inusara",
         "Ang pagpasig-uli mopuli sa tibuok library sa device. Kon ipasig-uli nimo diretso ang "
         "daang backup, mabawi nimo ang nawalang mga nota apan mawala ang tanan nga gisulat "
         "human nahimo kadtong backup. Ang paghiusa una maoy naghimo sa pagbawi nga walay "
         "mawala."),
        ("Kon ang backup mismo ang dili mapasig-uli",
         "Dili gayod nawala ang file nga naay error sa pagpasig-uli. Padagana niini ang health "
         "check — kasagaran maayohan ang kadaot gikan sa naputol nga download, cloud sync o "
         "nailisan nga extension, ug normal nga mapasig-uli ang nahinloan nga kopya."),
    ],
    "faq": [
        ("Anaa pa ba ang mga nota bisan asa sa device?",
         "Dili sa porma nga makab-ot gikan sa gawas sa app. Sa tinuoray, ang pagbawi nagpasabot "
         "ug mas naunang backup nga file — mao gyoy hinungdan nganong hinungdanon ang pagtipig "
         "sa daan."),
        ("Mobalik ba ang mga nota kon mag-sign in ko pag-usab?",
         "Dili. Wala gitipigan sa account ang datos sa personal nga pagtuon; anaa kini sa "
         "device ug pinaagi lang sa backup nga file kini mobiyahe."),
        ("Unsa man kon pipila na ka bulan ang bugtong backup nako?",
         "Hiusaha kini sa backup sa device sa kasamtangan niining kahimtang. Mabawi nimo ang "
         "tanan nga anaa sa daang file ug mahuptan ang tanan nga anaa pa sa device, nga dili "
         "kinahanglang mopili tali kanila."),
    ],
}

GUIDES_CEB["help-family-member-move-jw-library-notes"] = {
    "title": "Tabangi ang paryente sa pagbalhin sa iyang mga nota sa JW Library",
    "h1": "Pagtabang sa uban sa pagbalhin o pagluwas sa ilang mga nota sa JW Library",
    "description": "Ikaw ang kanunayng ginapangayoan ug tabang sa cellphone. Ania ang labing "
                   "mubo ug kasaligang dalan sa pagbalhin sa mga nota sa JW Library sa usa ka "
                   "paryente ngadto sa bag-ong device — apil kon unsaon kini nga dili basahon "
                   "ang iyang mga nota.",
    "intro": [
        "Sa ngadtongadto, naay motunol kanimo sa iyang cellphone, nga naay bag-o sa tapad. Ang "
        "mga nota sa JW Library mao ang bahin nga dili molihok sa iyang kaugalingon, ug "
        "kasagaran ang bahin nga labing hinungdanon — tuig-tuig nga pagtuon nga walay tool sa "
        "pagbalhin nga modala.",
        "Pareho ra ang proseso sa imong buhaton para sa imong kaugalingon, apan naay usa ka "
        "dugang nga hunahunaon una: kang kinsang device himoon ang buluhaton.",
    ],
    "steps": [
        ("Giyahi siya sa paghimo ug backup sa daang device",
         "JW Library → Personal nga Pagtuon → tulo-ka-tuldok nga menu → Backup ug Pagpasig-uli "
         "→ Paghimo ug backup. Motipig kini ug .jwlibrary nga file. Kon wala ka sa iyang tapad, "
         "matudlo ra kining bahina sa telepono."),
        ("Kuhaa ang file diin nimo kini gikinahanglan",
         "Pa-email kini niya sa iyang kaugalingon, o papaambita kanimo. Gamay ra kini aron "
         "ikapadala pinaagi sa bisan unsang messaging app."),
        ("Siguroha nga moabli ang file",
         "I-load kini sa jwsync.org ug kumpirmaha nga anaa ang mga nota. Ang pagbuhat niini sa "
         "dili pa mapapas o maihatag ang daang device mao ang maghimo sa daotang katingala nga "
         "walay hitabo."),
        ("Hiusaha kon naay nota na ang bag-ong device",
         "Kon dugay-dugay na niyang gamiton ang bag-ong cellphone, i-backup pod kana ug hiusaha "
         "ang duha ka file — kay kon dili, papason sa pagpasig-uli sa daang backup ang tanan "
         "nga iyang gisulat sa bag-ong device."),
        ("Ubani siya sa pagpasig-uli",
         "Sa bag-ong device: Backup ug Pagpasig-uli → Ipasig-uli, pilia ang file. Motungha ang "
         "tanang nota, highlight, bookmark ug tag."),
    ],
    "sections": [
        ("Pagbuhat niini nga dili basahon ang iyang mga nota",
         "Personal ang mga nota sa personal nga pagtuon. Kon mas gusto nimong dili kini makita "
         "— o mas gusto niya nga dili nimo kini makita — buhata ang tanan sa iyang device: web "
         "page kini, busa mahimo nimong ablihan ang jwsync.org sa iyang cellphone o tablet, "
         "i-load didto ang iyang mga file, ug dili gayod maanaa sa imong kaugalingong makina "
         "ang backup. Walay gi-upload sa bisan hain nga paagi, apan niining paagiha wala gayod "
         "mobiya ang file sa iyang mga kamot."),
        ("Bilini siya ug backup nga iyang makit-an",
         "Sa dili pa nimo iuli ang cellphone, siguroha nga ang backup nga file anaa sa dapit "
         "nga iyang makit-an pag-usab — sa iyang kaugalingong email o cloud drive, dili lang sa "
         "imong downloads folder. Sa sunod, basin dili na gyod ka niya kinahanglanon."),
    ],
    "faq": [
        ("Mahimo ba nako kini sa layo?",
         "Oo. Kon makahimo siya ug backup ug makapadala kanimo sa file, molihok sa layo ang "
         "tanan pang uban — ug pipila ra ka tap ang pagpasig-uli nga imong ikatudlo kaniya."),
        ("Android ang iya ug iPhone ang bag-o. Naay epekto ba?",
         "Wala. Managsama ang format sa backup sa Android, iPhone, iPad ug Windows."),
        ("Unsa man kon wala pa gyod siya makahimo ug backup ug wala na ang daang cellphone?",
         "Nan wala gyoy mabawian — anaa sa maong device ang datos. Mas maayong sugdan dayon sa "
         "bag-ong cellphone ang batasan sa regular nga pag-backup."),
    ],
}

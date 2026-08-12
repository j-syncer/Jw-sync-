# -*- coding: utf-8 -*-
"""Tagalog translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → backup (ang .jwlibrary na file)
  Personal Study            → Personal na Pag-aaral
  Backup and Restore        → Backup at Pagsasauli
  restore                   → isauli
  merge                     → pagsamahin / pagsasama
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
  meeting                   → pulong
  congregation              → kongregasyon
  assembly / convention     → asamblea / kombensiyon
"""

GUIDES_TL = {}

GUIDES_TL["merge-jw-library-backups"] = {
    "title": "Paano pagsamahin ang mga backup ng JW Library mula sa dalawang device",
    "h1": "Paano pagsamahin ang mga backup ng JW Library mula sa dalawang device",
    "description": "Pagsamahin ang mga nota, highlight, bookmark at tag mula sa dalawa o "
                   "higit pang backup ng JW Library sa iisang .jwlibrary na file — libre, "
                   "pribado, sa loob mismo ng browser mo.",
    "intro": [
        "Pinag-aralan mo ang Bantayan sa telepono at ibang artikulo naman sa tablet. Ngayon ay may laman ang bawat device na wala sa isa, at hindi sila mapagsasama ng JW Library: ang pag-restore doon ay buong pagpapalit, hindi paghahalo, kaya alinmang backup ang i-restore mo ay buburahin nito ang pinag-aralan sa kabilang device. Sa app lamang, walang paraan para mapanatili ang dalawa.",
        "Para diyan ang site na ito. Binabasa nito ang dalawa (o higit pa) na .jwlibrary at pinagsasama ang mga tala, highlight, bookmark at tag ng lahat ng iyon sa isang bagong backup — kaya wala nang kailangang piliin. Sa loob mismo ng browser mo nangyayari ang lahat: hindi kailanman ina-upload ang mga file mo sa anumang server, kaya nananatiling pribado ang iyong mga tala sa pag-aaral.",
        "Kaya rin pang-iwas ito at hindi panlunas: kapag regular kang nagsasama, hindi mo na kailangang tandaan na mag-restore bago mag-aral sa ibang device. Mag-aral kung nasaan ka, magsama kapag maginhawa, at aabot ang bawat device.",
    ],
    "steps": [
        ("Gumawa ng backup sa bawat device",
         "Sa JW Library, buksan ang Personal na Pag-aaral, i-tap ang tatlong-tuldok na menu, "
         "piliin ang Backup at Pagsasauli, tapos Gumawa ng backup. Gawin ito sa bawat device. "
         "Bawat isa ay gagawa ng isang .jwlibrary na file."),
        ("Buksan ang JW Sync",
         "Pumunta sa jwsync.org sa kahit anong browser — sa cellphone, tablet o computer. "
         "Walang kailangang i-install."),
        ("I-load ang dalawang backup na file",
         "I-drop (o piliin) ang mga .jwlibrary na file. Binabasa ang mga iyon ng JW Sync sa "
         "device mo mismo."),
        ("Suriin ang preview bago pagsamahin",
         "Bago pa may maisulat, ipapakita ng preview kung ano nga ba ang pagsasamahin. Kung "
         "iba-iba ang naging pag-edit sa iisang nota sa bawat device, ipapakita ng Conflict "
         "Reviewer ang dalawang bersiyon nang magkatabi, na may pagkakaiba salita-por-salita, "
         "para ikaw ang pumili kung alin ang itatago — o hayaan mong ang “Imungkahi ang "
         "pinakamainam” ang pumili para sa iyo."),
        ("I-download ang pinagsamang file at isauli ito",
         "I-download ang pinagsamang .jwlibrary na file, tapos isauli ito sa bawat device sa "
         "pamamagitan ng Backup at Pagsasauli → Isauli. Kumpleto na at magkatulad ang "
         "library sa dalawang device."),
    ],
    "sections": [
        ("Ano ang pinagsasama?",
         "Mga nota, highlight, bookmark, tag at ang mga ugnayan nila. Awtomatikong "
         "natutukoy ang mga duplicate, kaya hindi nadodoble ang anuman kapag isinauli ang "
         "pinagsamang file. Iisa ang format ng mga backup mula sa Android, iPhone, iPad at "
         "Windows app, kaya malayang nagsasama ang mga ito."),
        ("Ligtas ba ito?",
         "Hindi kailanman binabago ng pagsasama ang orihinal mong mga file — gumagawa ito ng "
         "bagong-bagong backup, kaya buo pa rin ang mga orihinal bilang panangga. At dahil "
         "sa browser lahat tumatakbo, walang datos na umaalis sa device mo."),
        ("Ano talaga ang laman ng isang .jwlibrary na file",
         "Ang backup na .jwlibrary ay isang ZIP archive. Kopyahin ito, palitan ang pangalan ng kopya ng .zip at buksan: makikita mo ang userData.db, isang SQLite database na naglalaman ng lahat ng nota, highlight, bookmark at tag na nagawa mo, kasama ang maliit na manifest.json na naglalarawan sa backup. Nasa talahanayang Note ang iyong mga nota, nasa UserMark at BlockRange ang mga highlight, nasa Bookmark ang mga bookmark, at nasa Tag at TagMap ang mga tag. Kapag naunawaan mong ang backup ay isang buong database at hindi tipak-tipak na mga file, malilinawan ang lahat ng iba pa sa pahinang ito: iyan ang dahilan kung bakit ang pagsasauli ay lahat-o-wala, at kung bakit puwedeng pagsamahin ang dalawang backup."),
        ("Bakit hindi makapagsama ang sariling Pagsasauli ng JW Library",
         "Kapag nagsasauli, hindi binabasa ng JW Library ang backup mo para idagdag ang kulang sa nasa device na. Pinapalitan nito ang database ng device ng nasa file. Sinadya at ligtas ang disenyong ito dahil tiyak na kilalang kalagayan ang matatapos sa device, pero ang ibig sabihin ay kapag isinauli mo sa telepono ang backup ng tablet, mawawala ang lahat ng nasa telepono na wala sa tablet. Walang setting na makapagbabago nito, at iyan mismo ang puwang na pinupunan ng pagsasama: gumagawa ito ng iisang file na naglalaman na ng gawa ng dalawang device, kaya kumpleto ang device na pagsasaulian mo."),
        ("Paano natutukoy ang mga duplicate",
         "May GUID ang bawat nota, highlight at bookmark — isang natatanging pagkakakilanlan na ipinagkakaloob sa paggawa at napananatili sa lahat ng sumunod na backup. Kapag lumitaw ang parehong bagay sa dalawang backup, iisa ang GUID ng dalawang kopya, kaya nakikilala itong iisang bagay at isang beses lang iniingatan. Kaya nga hindi dumodoble ang anuman kahit dalawang beses mong pagsamahin ang parehong dalawang file, at kaya ligtas kang makapag-uulit linggo-linggo. Kapag tugma ang GUID pero magkaiba ang teksto — iisang nota na binago sa dalawang device — hindi ito kusang malulutas, kaya lumilitaw ito sa Conflict Reviewer nang may salita-por-salitang paghahambing para ikaw ang pumili."),
        ("Ano ang wala sa backup",
         "Datos lang ng personal mong pag-aaral ang dala ng backup. Hindi kasama ang mga na-download na publikasyon, salin ng Bibliya, video at audio, at kaya maliliit ang mga file ng backup — karaniwang ilang megabyte lang kahit taon-taong pag-aaral. Pagkatapos magsauli sa bagong device, baka kailanganin mong i-download uli ang mga publikasyong madalas mong basahin. Walang naaapektuhan sa isinulat mo: naka-angkla ang mga nota sa mga publikasyon sa pamamagitan ng reperensiya, kaya muli itong dumidikit pagdating ng publikasyon."),
        ("Kung 0 ang naidagdag na nota ayon sa pagsasama",
         "Halos palaging tama ito, hindi depekto. Ibig sabihin, nasa unang file na ang lahat ng nota sa pangalawa — karaniwan kapag kamakailan ka lang nagsama, o kapag mas luma lang ang isang device kaysa sa isa. Tingnan ang preview: inilalahad nito kung ano ang dala ng bawat file bago pa may maisulat. Kung umaasa kang may bago at wala kang nakikita, tiyakin mong ginawa mo ang backup ng device pagkatapos ng pag-aaral na hinahanap mo, dahil ang laman lang ng backup ay ang umiiral noong ginawa ito."),
    ],
    "faq": [
        ("Puwede bang mahigit dalawang backup ang pagsamahin?",
         "Oo — i-load ang lahat ng .jwlibrary na file, kasindami ng device mo. Pagsasama-"
         "samahin ang lahat sa iisang backup."),
        ("Magkakaroon ba ng dobleng nota kapag pinagsama?",
         "Hindi. Natutukoy ang magkakaparehong nota, highlight at bookmark, at isa lang ang "
         "itatago. Ang tunay na magkaibang bersiyon ng iisang nota ay lalabas sa Conflict "
         "Reviewer para ikaw ang magpasiya."),
        ("Gumagana ba ito sa pagitan ng Android at iPhone?",
         "Oo. Pareho ang .jwlibrary na format sa Android, iOS, iPadOS at Windows, kaya "
         "nagsasama ang mga backup mula sa magkaibang plataporma nang walang anumang "
         "conversion."),
        ("Kailangan ba ng partikular na pagkakasunod-sunod sa pagsasama?",
         "Hindi. Walang kinalaman ang pagkakasunod-sunod — pareho ang lalabas sa iisang pangkat ng mga file, alinman ang unahin mo. Ang tanging naaapektuhan ay kung aling file ang ituturing na batayan sa buod ng preview."),
        ("Ano ang mangyayari sa mga tag na nasa iisang device lang?",
         "Buo silang naililipat, pati ang ugnayan ng mga tag at ng mga notang minarkahan nila. Kung pareho ang pangalan ng tag sa dalawang device, iisa ang ituturing at mapupunta rito ang mga nota mula sa dalawa."),
        ("Gaano kalaki ang pinagsamang file?",
         "Halos kasinlaki ng dalawang orihinal na pinagsama, bawas ang mga duplicate — karaniwang ilang megabyte pa rin. Walang media ng publikasyon sa mga backup, kaya kahit napakaraming markang aklatan ay kasya pa rin sa email."),
        ("Puwede bang bawiin ang isang pagsasauli?",
         "Hindi mula sa loob ng JW Library, at iyan ang dahilan kung bakit mahalagang itago ang orihinal mong mga backup. Hindi kailanman binabago ng pagsasama ang mga file na inilo-load mo, kaya nananatiling gayon ang mga backup mo bago ang pagsasama at maisasauli kung gusto mong bumalik."),
    ],
}

GUIDES_TL["sync-jw-library-multiple-devices"] = {
    "title": "Paano i-sync ang JW Library sa maraming device",
    "h1": "Paano panatilihing pare-pareho ang JW Library sa maraming device",
    "description": "Walang built-in na sync ang JW Library sa pagitan ng mga device. Narito "
                   "ang simple at pribadong rutina para manatiling magkatulad ang mga nota, "
                   "highlight at bookmark sa cellphone, tablet at computer mo.",
    "intro": [
        "Halos lahat ng nag-aaral sa dalawang device ay iisa ang paraan ng pagkatuklas sa suliranin: wala sa telepono ang mga notang isinulat sa tablet, at kung isasauli ang backup ng isa sa isa pa ay mabubura ang nasa huli. Walang inaalok na pag-sync ang JW Library, at sinadyang lahat-o-wala ang pagsasauli nito, kaya kailangan ng gawain at hindi ng setting para manatiling magkatugma ang mga device.",
        "Hindi sini-sync ng JW Library ang datos ng personal na pag-aaral sa pagitan ng mga "
        "device — walang account na magdadala ng mga nota mo mula sa cellphone patungo sa "
        "tablet. Ang opisyal na paraan ay Backup at Pagsasauli, at pinapalitan ng pagsasauli "
        "ang buong datos ng device. Paano nga ba mapananatiling magkatulad ang dalawa o "
        "tatlong device nang walang nawawala?",
        "Ang sagot ay isang maikling rutina: pagsamahin, tapos isauli. Kapag ginawa lingguhan "
        "o buwanan, mga dalawang minuto lang ito at nananatiling kumpleto ang library sa "
        "bawat device.",
    ],
    "steps": [
        ("I-backup ang bawat device",
         "Sa bawat isa: Personal na Pag-aaral → tatlong-tuldok na menu → Backup at Pagsasauli "
         "→ Gumawa ng backup. Magkakaroon ka ng isang .jwlibrary na file kada device."),
        ("Pagsamahin ang mga backup sa jwsync.org",
         "I-load ang lahat ng file. Pinagsasama ng JW Sync ang mga nota, highlight, bookmark "
         "at tag ng bawat device sa iisang pinagsamang .jwlibrary na file — sa browser mo "
         "mismo, walang ina-upload."),
        ("Isauli ang pinagsamang file sa bawat device",
         "Backup at Pagsasauli → Isauli, piliin ang pinagsamang file. Magkatulad na at "
         "kumpleto ang lahat ng device."),
        ("Hayaang paalalahanan ka ng JW Sync",
         "I-on ang paalala sa pag-sync (lingguhan o buwanan) sa JW Sync at sasabihan ka nito "
         "kapag panahon na para ulitin. Naaalala rin nito ang mga naka-save mong device, "
         "kaya mas mabilis ang bawat susunod."),
    ],
    "sections": [
        ("Bakit hindi na lang isauli ang pinakabagong backup?",
         "Dahil ang “pinakabago” ay isang device lang ang sinasalamin. Kung sa iisang linggo "
         "ay may nota ka sa pulong mula sa cellphone at nota sa pag-aaral mula sa tablet, may "
         "laman ang bawat backup na wala sa isa. Kapag isinauli mo ang isa sa ibabaw ng isa "
         "pa, mawawala ang kalahati ng ginawa mo. Ang pagsasama ang nagpapaligtas sa rutinang "
         "ito."),
        ("Gaano kadalas dapat mag-sync?",
         "Ibagay sa paraan ng pag-aaral mo. Dalawang aktibong device na araw-araw ginagamit: "
         "kumportable ang minsan sa isang linggo. Tablet na lumalabas lang tuwing pulong: "
         "sapat na ang minsan sa isang buwan. Ang tanging bunga ng mas mahabang paghihintay "
         "ay mas marami ang pagsasamahin — walang nawawala sa pagitan ng bawat ulit."),
        ("Bakit walang tunay na pag-sync",
         "Walang account ang JW Library na nagdadala ng datos ng personal na pag-aaral mula sa isang device tungo sa isa pa. Nasa database sa loob ng bawat device ang mga nota, highlight at bookmark, at doon sila nananatili. Ang tanging opisyal na paraan para ilipat ang mga ito ay ang Backup at Pagsasauli, at pinapalitan ng pagsasauli ang datos ng patutunguhang device sa halip na pagsamahin. Kaya nagkakalayo nang tuluyan ang dalawang device na hiwalay na ginagamit, maliban kung may magsasama sa kanila — at iyan mismo ang layunin ng gawain sa ibaba."),
        ("Magpanatili ng isang pangunahing file",
         "Pinakamainam ang gawaing ito kung ituturing mong pangunahin sa kasalukuyan ang isang pinagsamang file. Sa bawat ikot, i-backup ang lahat ng device, pagsamahin ang mga backup na iyon, at isauli ang bunga saanman. Ang pinagsamang file ang magiging pangunahin sa susunod na ikot. Ang pag-iingat ng may-petsang pangunahing file sa cloud ay nagbibigay sa iyo ng paraan ng pag-sync at ng talaan nang sabay: kung may mabura kang hindi sinasadya, naroon pa rin ito sa naunang pangunahing file."),
        ("Ano ang mangyayari kung malalaktawan mo ang isang device nang matagal",
         "Walang nawawala. Ang device na nalaktawan sa ilang ikot ay simpleng may mas lumang datos; kapag naisama mo na rin, sumasanib ang mga nota nito sa lahat ng iba pa at pinagtutugma sa pamamagitan ng GUID ang mga paulit-ulit na bagay sa halip na dumoble. Ang tanging kalagayang kailangan ng pasiya ay ang iisang notang binago sa dalawang device mula nang huling pagsamahin, at lumilitaw iyon sa Conflict Reviewer nang magkatabi ang dalawang bersiyon."),
        ("Gaano kadalas ang sapat",
         "Iakma sa dami ng gawaing ayaw mong ulitin. Bagay ang lingguhan kung halos araw-araw kang nag-aaral sa dalawang device; sobra-sobra na ang buwanan kung paminsan-minsan lang ang isa. Ang mahalaga ay gawin ito bago ang anumang hindi na mababawi — pagpapalit ng telepono, pag-reset, pagpapaayos — dahil doon nagiging pagkawala ang pagkakalayo."),
        ("Telepono, tablet at ang app para sa Windows nang sabay",
         "Walang pakialam ang gawaing ito kung ilan ang device o ano ang pinapatakbo ng mga ito. I-backup ang bawat isa, pagsamahin lahat sa isang hakbang, isauli ang pinagsamang file saanman. Nagsasama ang kompyuter na Windows na ginagamit sa paghahanda at ang teleponong dala sa pulong gaya mismo ng dalawang telepono, dahil iisang anyo ng backup ang isinusulat ng bawat plataporma."),
        ("Bawasan ang salungatan bago pa ito mangyari",
         "Nangyayari lang ang salungatan kapag binago ang iisang nota sa dalawang device sa pagitan ng mga pagsasama. Sa katotohanan, bihira ito, at lalo pang bumibihira kung sa isang device ka lang magsusulat — magbasa saanman, pero magtipa kung saan ka karaniwang nagtitipa. Ang mas madalas na pagsasama ay nagpapaikli rin sa panahong maaaring mangyari ang pagkakalayo, at mas mabisa ito kaysa sa pagsisikap na tandaan kung aling device ang may pinakabagong bersiyon."),
        ("Kung saan sumasagot ang gawaing ito",
         "Ang halaga ng pagpapanatiling pinagsama ang mga device ay hindi ang kaayusan — ito ay ang pagiging buong backup ng bawat device sa aklatan ng iyong pag-aaral. Mawala man o masira ang alinman sa kanila, dala pa rin ng iba ang lahat, at ginagawa nitong abala lamang ang dating pinakamasamang kalagayan ng taon-taong nawawalang nota. Mas matatag itong kalagayan kaysa sa maibibigay ng anumang ugali ng pag-backup sa iisang device."),
    ],
    "faq": [
        ("Tumatakbo ba ang JW Sync sa background?",
         "Hindi — isa itong web page, hindi naka-install na serbisyo. Walang nagsu-scan sa "
         "mga device mo. Ikaw ang nagpapatakbo ng rutina kung kailan mo gusto; ang opsiyonal "
         "na paalala ay abiso lamang."),
        ("Puwede bang tatlo o higit pang device ang i-sync?",
         "Oo. I-backup ang bawat isa, i-load ang lahat ng file, pagsamahin nang minsan, at "
         "isauli ang pinagsamang file sa lahat."),
        ("Paano kung binago ko ang iisang nota sa dalawang device?",
         "Iniingatan ang dalawang bersiyon hanggang pumili ka. Ipinapakita ng Conflict Reviewer ang mga ito nang magkatabi na may salita-por-salitang paghahambing, o puwede mong ipasuggest ang mas kumpleto."),
        ("Mahalaga ba ang pagkakasunod-sunod ng pagsasauli?",
         "Hindi. Kapag nagawa na ang pinagsamang file, ang pagsasauli nito sa bawat device ay naglalagay sa lahat sa iisang buong kalagayan, sa anumang pagkakasunod-sunod na akma sa iyo."),
        ("Puwede bang tatlo o higit pang device?",
         "Oo. I-backup ang bawat isa at i-load lahat sa iisang pagsasama — walang hangganang nakatali sa dami ng device."),
        ("Puwede ba itong gawing awtomatiko?",
         "Hindi lubusan, dahil walang API ng pag-sync ang JW Library at nangyayari sa loob ng app ang hakbang ng pagsasauli. Mga dalawang minuto ang manwal na gawain kapag nasanay ka na."),
        ("Kailangan ko bang magsama kung nagbabasa lang ako sa pangalawang device?",
         "Kung hindi ka kailanman nagmamarka roon, sapat nang magsauli ka rito paminsan-minsan para dalhin nito ang kasalukuyan mong mga nota."),
    ],
}

GUIDES_TL["transfer-jw-library-notes-new-phone"] = {
    "title": "Paano ilipat ang mga nota sa JW Library sa bagong cellphone",
    "h1": "Paano ilipat ang mga nota sa JW Library sa bagong cellphone",
    "description": "Ang paglipat ng mga tala sa JW Library papunta sa bagong telepono ay isang backup at isang restore, at kaya iyon ng app sa mga dalawang minuto. Narito ang mga hakbang — pati ang tanging kaso na hindi nito kaya: kapag may sariling mga tala na ang bagong telepono.",
    "intro": [
        "Mas madali ito kaysa inaasahan ng marami, at hindi mo kailangan ng anumang karagdagang kasangkapan. Nakapaloob na sa JW Library ang backup at restore, at dala nito ang bawat tala, highlight, bookmark at tag papunta sa bagong telepono — pati sa pagitan ng Android at iPhone. Gawin mo habang gumagana pa ang lumang device at ilang minuto lang ang buong proseso.",
        "Ang tanging bahaging dapat sadyain ay ang paglilipat mismo: inililipat ng mga kasangkapan sa paglipat ng telepono ang iyong apps at mga larawan, pero nilalaktawan nila ang personal na datos ng pag-aaral sa JW Library, kaya gawin mo ang backup file sa halip na asahang kasama na ito.",
        "May eksaktong isang sitwasyon na hindi kaya ng app, at makabubuting malaman bago ka magsimula: kung nag-aaral ka na sa bagong telepono, buburahin ng pag-restore ng backup ng luma ang trabahong iyon, dahil pinapalitan ng restore ang buong aklatan ng device. Kung iyan ang kalagayan mo, ang bahagi tungkol sa pagsasama sa ibaba ang kailangan mo.",
    ],
    "steps": [
        ("Gumawa ng backup sa lumang cellphone",
         "Buksan ang JW Library → Personal na Pag-aaral → tatlong-tuldok na menu → Backup at "
         "Pagsasauli → Gumawa ng backup. Magse-save ito ng .jwlibrary na file na naglalaman "
         "ng lahat ng datos mo sa pag-aaral."),
        ("Ilipat ang file sa bagong cellphone",
         "I-email ito sa sarili mo, o gumamit ng Google Drive, iCloud, AirDrop o USB cable. "
         "Maliit ang file — kadalasan ay ilang megabyte lang."),
        ("Isauli sa bagong cellphone",
         "I-install ang JW Library, tapos Personal na Pag-aaral → Backup at Pagsasauli → "
         "Isauli, at piliin ang .jwlibrary na file. Lalabas ang lahat ng nota, highlight, "
         "bookmark at tag."),
    ],
    "sections": [
        ("May nota ka na sa bagong cellphone? Magsama, huwag mag-overwrite",
         "Pinapalitan ng pagsasauli ang anumang nasa device. Kung ilang panahon mo nang "
         "ginagamit ang bagong cellphone at may sarili itong mga nota, huwag isauli sa ibabaw "
         "ng mga iyon — i-backup din ang bagong cellphone, pagsamahin ang luma at bagong "
         "backup sa iisang file sa jwsync.org (libre, sa browser, walang ina-upload) at "
         "isauli ang pinagsamang file. Maiingatan mo ang dalawang set ng nota."),
        ("Isang karaniwang problema sa iPhone",
         "Kung dumating sa iPhone ang backup na file na napalitan ang pangalan ng .zip, "
         "ibalik ito sa .jwlibrary bago isauli — maayos ang laman; ang extension lang ang "
         "nagbago sa daan."),
        ("Gawin ito bago burahin o ipagpalit ang lumang telepono",
         "Kailangang gawin ang backup habang gumagana pa ang lumang telepono at naka-install pa rito ang JW Library. Kapag na-reset na ang device, naipagpalit o naipasa sa iba, kasama nitong mawawala ang mga nota: walang itinatagong kopya sa cloud ang JW Library para sa datos ng personal na pag-aaral, at ang backup ng buong telepono gaya ng Google One o backup ng device sa iCloud ay madalas na nagsasauli ng mas lumang kalagayan ng datos ng app, o wala man lang. Gawin muna ang .jwlibrary na file, ilagay sa ligtas na lugar, at tiyaking nakikita mo ito bago ka magbura ng kahit ano."),
        ("Paano ilabas ang file mula sa lumang telepono",
         "Sa Android, naisusulat ang file sa folder na pinili mo — kadalasan ay Downloads o Documents — at mailILipat ito ng anumang file manager, mai-email mo sa sarili mo, o mailalagay sa cloud. Sa iPhone, lumilitaw ang share sheet pagkagawa mismo ng backup: i-save sa Files, ipadala sa bagong telepono sa AirDrop, o ipadala sa sarili mo. Walang bisa ang paraan at hindi nito masisira ang file: iisang archive ang .jwlibrary, kaya buo itong dumarating o hindi dumarating."),
        ("Bakit hindi sapat ang app na panlipat mula telepono tungo sa telepono",
         "Ang mga kasangkapang gaya ng Smart Switch, Move to iOS o pagsasauli mula sa iCloud ay kumokopya ng mga app at datos ng sistema, pero madalas na nalalaktawan, bahagya lang naisasauli, o naisasauli mula sa mas naunang panahon ang pribadong database ng bawat app. Karaniwang natutuklasan ang kulang pagkalipas ng ilang linggo, kapag wala na ang lumang telepono. Ituring mong ang .jwlibrary na file ang tunay na kopya at ang paglilipat ng telepono ay ginhawa lang: kung nagkataóng dala nito ang mga nota mo, walang mawawala kung isasauli mo pa rin ang sarili mong backup sa ibabaw."),
        ("Tiyaking talagang umubra ang paglilipat",
         "Pagkatapos magsauli sa bagong telepono, magbukas ng dalawa o tatlong publikasyong kamakailan mong minarkahan at tiyaking naroon ang mga nota, kulay ng highlight at bookmark. Mas mabilis na pagsusuri: buksan mismo ang file ng backup sa iyong browser bago mo burahin ang lumang device — makikita mo ang bawat nota, highlight at bookmark na nasa loob, kaya alam mo kung ano ang dapat lumitaw. Burahin lang ang lumang telepono kapag napatunayan mo na ang bago."),
        ("Kung sabay ka ring lilipat sa tablet o kompyuter",
         "Pareho ang file na gagana saanman. Kung sabay mong isasaayos ang bagong telepono at tablet, isauli ang parehong .jwlibrary na file sa dalawa at magsisimula silang magkatulad. Mula roon, muli silang maghihiwalay ayon sa pinag-aaralan mo sa bawat isa, kaya mainam nang magpasya ngayon kung pagsasama-samahin mo sila paminsan-minsan o ituturing mong pangunahin ang isa."),
        ("Kung may nota na ang bagong telepono",
         "Nangyayari ito kapag isang linggo mo nang ginagamit ang bagong device bago mo asikasuhin ang paglilipat. Papalitan ng datos ng lumang telepono ang gawang iyon kung tuwirang magsasauli ka. Gawin muna ang backup ng bagong telepono, pagsamahin ito sa backup ng luma, at isauli ang bunga — mapupunta sa iisang aklatan ang dalawang pangkat ng nota sa halip na patungan ng isa ang isa."),
        ("Ano ang gagawin kapag umaandar na ang bagong telepono",
         "Suriin bago mo pakawalan ang kahit ano. Magbukas sa bagong telepono ng ilang publikasyong kamakailan mong minarkahan at tiyaking naroon ang mga nota, kulay at bookmark; saka mo lang burahin o ipagpalit ang lumang device — ganito ang pagkakasunod-sunod at huwag kailanman baligtarin. Kapag maayos na, maglagay ng backup sa labas ng telepono, dahil babalik ang kalagayang nagdala sa iyo sa pahinang ito sa susunod mong pagpapalit."),
    ],
    "faq": [
        ("Malilipat din ba ang mga na-download kong publikasyon?",
         "Dala ng backup ang datos ng personal na pag-aaral mo — mga nota, highlight, "
         "bookmark, tag at playlist. Muling mada-download lang ang mga publikasyon sa bagong "
         "cellphone."),
        ("May epekto ba kung magkaiba ang bersiyon ng Android ng mga cellphone?",
         "Wala. Pareho ang .jwlibrary na format saanman, pati na sa pagitan ng mga bersiyon "
         "ng Android at sa pagitan ng Android at iPhone."),
        ("MailILipat ko pa ba ang mga nota kung wala na ang lumang telepono?",
         "Kung may .jwlibrary na file sa kung saan lang: sa Files, Downloads, isang email sa sarili mo o sa cloud. Kung wala, walang maisasauli, dahil sa device lang nakaimbak ang datos ng personal na pag-aaral."),
        ("Kailangan bang pareho ang bersiyon ng JW Library sa dalawang telepono?",
         "Hindi kailangang eksaktong magkatugma, pero i-update ang bagong telepono sa kasalukuyang bersiyon bago magsauli. Ang backup na gawa ng mas bagong bersiyon ay maaaring gumamit ng istruktura ng database na hindi nauunawaan ng mas lumang app."),
        ("Kakailanganin ko bang i-download uli ang mga publikasyon?",
         "Kadalasan ay oo — walang media ng publikasyon sa backup. Muling dumidikit ang mga nota mo sa bawat publikasyon pagka-download nito, kaya walang mawawala sa isinulat mo samantala."),
        ("Gaano katagal ang lahat?",
         "Ilang minuto. Ilang segundo lang ang paggawa ng backup, nakadepende sa paraan ang paglilipat ng file, at mabilis ang pagsasauli. Ang pinakamatagal ay ang muling pag-download ng mga publikasyon, at puwede itong tumakbo sa likod."),
        ("Puwede bang gawin ito nang walang Wi-Fi?",
         "Ang paglilipat mismo, oo, sa AirDrop o kable. Kailangan ng koneksiyon sa muling pag-download ng mga publikasyon sa bagong device."),
    ],
}

GUIDES_TL["jw-library-android-to-iphone"] = {
    "title": "Ilipat ang JW Library mula Android papuntang iPhone (buo ang mga nota)",
    "h1": "Paglipat ng JW Library mula Android papuntang iPhone o iPad — walang mawawalang nota",
    "description": "Pareho ang .jwlibrary na format ng backup sa Android at iOS. Kung paano "
                   "ilipat ang mga nota, highlight at bookmark sa magkaibang plataporma — at "
                   "kung paano magsama kung may nota ang dalawang device.",
    "intro": [
        "Mukhang mahirap ang paglipat sa pagitan ng Android at iPhone, pero ito ang madali. Iisang anyo ng backup ang isinusulat ng JW Library sa bawat plataporma kung saan ito tumatakbo, kaya ang paglilipat ng aklatan ng pag-aaral mula Android tungong iOS ay katulad na katulad ng paglilipat sa pagitan ng dalawang Android na telepono — walang pagpapalit ng anyo, walang pipiliing format ng pag-export, walang nawawala sa daan.",
        "Ang paglipat ng plataporma ang sandaling kinatatakutan ng marami na mawala ang "
        "taon-taong nota sa pag-aaral — laktaw nang laktaw ang mga app na panlipat mula "
        "Android papuntang iPhone sa datos ng JW Library. Ang magandang balita: pareho ang "
        "format ng backup ng JW Library sa Android, iPhone, iPad at Windows, kaya ang "
        "paglipat ay backup, paglilipat ng file, at pagsasauli lang.",
    ],
    "steps": [
        ("Mag-backup sa Android na cellphone",
         "JW Library → Personal na Pag-aaral → tatlong-tuldok na menu → Backup at Pagsasauli "
         "→ Gumawa ng backup. I-save ang .jwlibrary na file."),
        ("Ipadala ang file sa iPhone o iPad",
         "Email, Google Drive, iCloud Drive — kahit ano na naglilipat ng file. Kung palitan "
         "ito ng iOS ng .zip sa daan, ibalik ito sa .jwlibrary."),
        ("Isauli sa bagong device",
         "I-install ang JW Library, mag-sign in, tapos Backup at Pagsasauli → Isauli at "
         "piliin ang file. Darating lahat ang mga nota, highlight, bookmark, tag at "
         "playlist."),
    ],
    "sections": [
        ("Kung may mga nota na ang iPhone",
         "Pinapalitan ng pagsasauli ang datos ng device. Kapag may sariling mga nota na ang "
         "bagong device, i-backup din ito at pagsamahin muna ang dalawang backup sa iisang "
         "file sa jwsync.org — pinagsasama ng pagsasama ang dalawang library sa browser mo, "
         "walang ina-upload — tapos isauli ang pinagsamang file. Walang mawawala sa "
         "kahit aling panig."),
        ("Gumagana ang parehong hakbang sa anumang direksiyon",
         "iPhone papuntang Android, Android papuntang Android, pagdaragdag ng iPad bilang "
         "pangalawang device sa pag-aaral, o paglipat sa Windows app — ang backup na file ang "
         "karaniwang wika ng lahat ng ito."),
        ("Bakit magkatulad ang anyo sa dalawang plataporma",
         "Iisang anyo ng backup ang ginagamit ng JW Library saanman ito tumakbo — Android, iOS, iPadOS at Windows. Ang .jwlibrary na file ay isang ZIP na naglalaman ng SQLite database na may parehong talahanayan at parehong istruktura, anuman ang device na sumulat nito. Walang hakbang ng pagpapalit ng anyo, walang balikang pag-export at pag-import, at walang bahaging nakatali sa plataporma sa loob ng file. Naisasauli ang backup mula sa Android sa iPhone gaya mismo ng gagawin ng backup mula sa iPhone."),
        ("Ang tanging bahaging talagang nagkakaiba",
         "Hindi ang file — ang paraan lang ng pagkuha rito. Sa Android, naise-save ang backup sa folder na pinili mo at mailILipat ng anumang file manager. Sa iPhone, dumadaan ito sa share sheet patungong Files, AirDrop, o kung saan mo gusto. Ang hirap na nararanasan sa paglipat ng plataporma ay laging nasa hakbang na ito ng paghawak, hindi kailanman sa pagkakatugma. Umuubra nang pantay ang email, cloud o AirDrop; buo ang dating ng archive o hindi ito dumarating."),
        ("Kulay ng highlight, mga tag at sagot sa pag-aaral",
         "Nananatili ang lahat. Nakaimbak bilang bilang ang kulay ng mga highlight — dilaw, berde, asul, rosas, kahel at lila — at pare-pareho ang anyo sa anumang plataporma. Naililipat ang mga tag at ang ugnayan ng tag at nota, gayundin ang mga sagot na tinipa sa mga patlang ng tanong sa pag-aaral. Ang makikita mo sa iPhone pagkatapos magsauli ay iyon mismo ang nasa Android mong device."),
        ("Kung hindi ka payagan ng iOS na piliin ang file",
         "I-save muna ang file sa Files app, saka piliin mula roon sa halip na mula sa kalakip ng email o sa preview ng isang messaging app. May mga app na nagbibigay sa iOS ng pansamantalang kopyang pang-preview sa halip na ang tunay na file, at hindi ito mabubuksan ng JW Library. Kung dumating ang file bilang kalakip, pindutin ito, piliin ang Save to Files, at magsauli mula sa Files."),
        ("Ihanda ang iPhone bago magsauli",
         "I-install ang JW Library mula sa App Store at i-update ito sa kasalukuyang bersiyon bago ka magsauli ng anuman. Ang backup na isinulat ng mas bagong bersiyon ay maaaring gumamit ng istruktura ng database na hindi nauunawaan ng mas lumang bersiyon, at basta na lang tatanggihan ang pagsasauli. Hindi kailangang mag-sign in kahit saan: nasa file na isinasauli mo ang datos ng personal na pag-aaral, hindi sa isang account."),
        ("Kung nakapagsimula ka nang mag-aral sa iPhone",
         "I-backup muna ang iPhone. Papalitan ng tuwirang pagsasauli ng file mula sa Android ang lahat ng isinulat mo mula nang lumipat ka. Ang pagsasama ng dalawang backup ay gumagawa ng file na naglalaman ng pareho, na isasauli mo — mapupunta sa iisang aklatan ang kasaysayan mula sa Android at ang bagong nota sa iPhone."),
        ("Kung gagamitin mo pa rin ang dalawang telepono",
         "May mga nag-iingat sa lumang Android bilang pangalawang pambasa sa halip na itabi na ito. Umuubra iyon, pero maghihiwalay sila sa sandaling magmarka ka sa dalawa, dahil walang pag-sync sa pagitan nila. Kung balak mong gamitin ang dalawa, ihanda mo ang sarili mong pagsamahin ang kanilang mga backup paminsan-minsan sa halip na akalaing mananatili silang magkatugma."),
        ("Pagkatapos ng paglipat",
         "Bigyan ng panahon ang iPhone na muling i-download ang mga publikasyong pinakamadalas mong gamitin, saka suriin ang ilang minarkahan para tiyaking dumating ang lahat: mga nota, kulay ng highlight, bookmark at tag. Itago ang file ng backup mula sa Android kahit tapos na ang paglipat: isa itong may-petsang larawan ng iyong aklatan, at walang gastos ang pag-iingat nito."),
    ],
    "faq": [
        ("Kailangan ko ba ng computer para dito?",
         "Hindi. Kayang gawin ang buong paglipat mula cellphone patungong cellphone gamit ang "
         "email o cloud drive."),
        ("Mananatili ba ang mga kulay ng highlight ko?",
         "Oo — nananatili ang kulay ng mga highlight, ang tag ng mga nota, at ang puwesto ng "
         "mga bookmark."),
        ("Kailangan ko ba ng kompyuter para dito?",
         "Hindi. Ang AirDrop, email o anumang app ng cloud storage ay tuwirang naglilipat ng file sa pagitan ng dalawang telepono."),
        ("Umuubra ba ito sa kabilang direksiyon, mula iPhone tungong Android?",
         "Oo, gayon din. Umuubra ang parehong hakbang sa kahit anong direksiyon, pati na sa app para sa Windows."),
        ("Kakailanganin ba ng iPhone ang parehong na-download na publikasyon?",
         "Oo, dahil walang media ng publikasyon sa backup. Dumidikit uli ang mga nota sa bawat publikasyon pagka-download nito."),
        ("Kailangan ko bang itago ang Android na telepono pagkatapos?",
         "Hindi na, kapag natiyak mong nasa iPhone na ang mga nota. Suriin ang ilang minarkahang publikasyon bago burahin o ipagpalit ang lumang device."),
        ("Naililipat ba ang mga sagot sa tanong sa pag-aaral?",
         "Oo. Bahagi ng datos ng personal na pag-aaral ang mga tinipang sagot at kasama ito sa lahat ng iba pa."),
        ("May panganib bang mawalan ng nota sa paglipat?",
         "Wala kung itatago mo ang backup mula sa Android. Sumusulat ang pagsasauli sa iPhone at hindi kailanman binabago ang file na binabasa nito, kaya buo ang orihinal bilang kapalit. Itago ito hanggang matiyak mong nasa iPhone na ang lahat, at mabuti nang pati pagkatapos."),
        ("Paano kung hindi makagawa ng backup ang Android na telepono?",
         "Suriin muna ang natitirang espasyo, dahil kailangan ng app ng lugar para isulat ang file. Kung ang mismong app ang may problema, kadalasang naaayos ito sa pag-update o pag-restart ng device. Buo pa rin ang datos habang inaayos mo ito."),
    ],
}

GUIDES_TL["backup-jw-library"] = {
    "title": "Paano mag-backup ng JW Library sa tamang paraan",
    "h1": "Paano mag-backup ng JW Library sa tamang paraan",
    "description": "Isang 30-segundong gawi sa pag-backup: ano talaga ang laman ng isang .jwlibrary file, saan ito itatago, at bakit sulit magkaroon ng bago kahit walang namamalihan.",
    "intro": [
        "Mga kalahating minuto lang ang isang backup, at sulit itong gawing gawi — bagaman hindi eksakto sa dahilang karaniwang ibinibigay. Nailipat na nang maayos ng sariling backup at restore ng JW Library ang isang aklatan papunta sa bagong device, kaya ang backup ay hindi gaanong seguro kundi ang hilaw na materyal ng lahat ng iba pang gusto mong gawin sa iyong pag-aaral.",
        "Ang .jwlibrary file ang tanging anyo na ginagawa ng iyong aklatan sa labas ng app. Ito ang pinagsasama mo kapag pinag-aralan sa dalawang device, ito ang binubuksan mo para basahin, palitan ang tag o ayusin ang mga taon ng tala, ito ang hinahanap mo ayon sa kahulugan kapag kalahati lang ang natatandaan mo sa isinulat mo, at dito mo kinukuha ang mga talang ipadadala mo sa isang kaibigan. Ang pagkakaroon ng bago ang siyang nagbibigay-daan sa lahat ng iyon.",
    ],
    "steps": [
        ("Gumawa ng backup",
         "Buksan ang JW Library → Personal na Pag-aaral → tatlong-tuldok na menu → Backup at "
         "Pagsasauli → Gumawa ng backup. Gagawa ito ng .jwlibrary na file na naglalaman ng "
         "bawat nota, highlight, bookmark at tag."),
        ("Itago ito sa labas ng cellphone",
         "I-email ito sa sarili mo, o i-save sa Google Drive, iCloud o OneDrive. Ang backup "
         "na nasa cellphone lang ay mawawala kasama ng cellphone."),
        ("Ulitin nang regular",
         "Magandang panimula ang minsan sa isang buwan; kailangang-kailangan bago ang anumang "
         "pagpapalit ng device, pag-reset o pag-update ng sistema. Itago ang mga lumang kopya "
         "— maliliit lang ang file, at nakatulong na ang lumang backup sa marami."),
    ],
    "sections": [
        ("Ang karaniwang pagkakamali: pagtitiwala sa cloud backup ng cellphone",
         "Ang backup ng buong cellphone (Google One, iCloud device backup) ay madalas na "
         "lumang kopya ng datos ng JW Library ang naisasauli — o wala man lang. Ang "
         ".jwlibrary na file ang tanging backup na buo mong kontrolado at kayang dalhin sa "
         "iba't ibang plataporma. Ituring mong bonus ang backup ng cellphone, hindi ang "
         "pangunahing plano."),
        ("Napunta ka sa dalawang magkaibang backup?",
         "Nangyayari ito: isang backup mula sa cellphone, isang mas luma mula sa tablet, at "
         "may sariling mga nota ang bawat isa. Hindi mo kailangang mamili sa dalawa — "
         "pagsamahin ang mga ito sa isang kumpletong file sa jwsync.org, libre at pribado, sa "
         "browser mismo."),
        ("Ano ang laman ng file, at ano ang wala",
         "Iniingatan ng backup ang datos ng personal mong pag-aaral: mga nota, highlight at ang kulay ng mga ito, bookmark, tag, at ang mga sagot na tinipa mo sa mga patlang ng tanong sa pag-aaral. Hindi nito iniingatan ang mismong mga publikasyon — walang Bibliya, magasin, aklat, video o audio. Kaya nga ilang megabyte lang ang backup ng taon-taong pag-aaral, at kaya kapag nagsauli ka sa bagong device ay nagda-download ka pa ng mga publikasyon samantalang nasa lugar na ang bawat notang isinulat mo."),
        ("Ilang backup ang dapat itago",
         "Higit sa isa. Ang bagay na kumukuha ng mga nota ng tao ay bihirang nawawalang file — mas madalas na magandang backup na napatungan ng masama, o pagsasauli sa maling device. Dahil maliliit ang mga file, walang dahilan para burahin ang luma: itago ang mga ito nang may petsa sa isang folder sa cloud. Hindi nawawalan ng halaga ang backup na anim na buwan na ang tanda kahit may mas bago ka na, dahil ang anumang nabura mo nang hindi sinasadya mula noon ay naroon pa rin sa loob."),
        ("Saan itago ang mga ito",
         "Kahit saan basta hindi lang sa mismong device. Sagot na ng folder sa Drive, iCloud, Dropbox o OneDrive ang pinakamahalagang kalagayan — ang mawala, manakaw, ma-reset o masira ang device. Umuubra rin ang pag-email ng file sa sarili mo, at may bentahe pang mailalagay nito ang petsa. Nasa file ang sarili mong mga nota sa pag-aaral, kaya pakitunguhan ito gaya ng anumang personal na dokumento."),
        ("Suriin ang backup bago ka umasa rito",
         "Ang backup na hindi mo pa nabuksan ay palagay, hindi kaligtasan. Puwede mong buksan ang .jwlibrary na file sa iyong browser at makita mismo kung anong mga nota, highlight at bookmark ang laman nito — tatlumpung segundong pagsusuri na gumagawang katotohanan ang palagay. Pinakamahalaga ito bago mismo ang isang bagay na hindi na mababawi: factory reset, pagpapalit ng device, pagpapaayos, o malaking pag-update ng sistema."),
        ("Ang mga sandaling sulit magbackup",
         "Anumang punto na nagpapalit ng may-ari o kalagayan ang device: pag-update ng sistema, factory reset, pagpapaayos o pagpapalit ng screen, pagpapalit ng device, o pagbibigay nito sa iba. Idagdag pa ang katapusan ng anumang ayaw mong ulitin — isang kombensiyon, isang asamblea, isang panahon ng paghahanda ng pahayag. Mabilis at mura ang mga backup, kaya ang kapaki-pakinabang na ugali ay iugnay ang mga ito sa mga pangyayari at hindi sa kalendaryo."),
        ("Ang backup ng telepono ay hindi backup ng JW Library",
         "Ang Google One, ang backup ng device sa iCloud o ang kasangkapang panlipat ng gumawa ng telepono ay gumagana sa antas ng device at hindi pare-pareho ang pagtrato sa pribadong datos ng mga app. Karaniwan nang natutuklasan ng mga tao na ibinalik ng buong pagsasauli ng telepono ang mga app at setting pero hindi ang mga nota sa pag-aaral, o ibinalik ang bersiyong ilang linggo nang nakaraan. Ang .jwlibrary na file ang tanging kopyang kontrolado mo ang laman at kaya mong suriin, kaya ituring mong bonus ang backup ng telepono, hindi ang plano."),
        ("Gawin itong ugaling tatagal",
         "Ang gawaing talagang tumatagal ay ang nakakabit sa isang bagay na ginagawa mo na: magbackup pagkatapos mong ihanda ang linggo, o sa mismong araw na inaasikaso mo ang ibang panapanahong gawain. Palaging mag-save sa iisang folder para sa iisang lugar magtipon ang mga file, at iwan doon ang mga luma. Ang folder ng mga backup na may petsa na umaabot sa maraming taon ang pinakamatibay na anyo nito, at ilang segundo lang bawat linggo ang panatilihin ito."),
    ],
    "faq": [
        ("Gaano kalaki ang isang backup na file?",
         "Kadalasan ay ilang megabyte lang kahit sa napakalaking library — kasinliit ng "
         "attachment sa email."),
        ("May binabago ba sa cellphone ko ang paggawa ng backup?",
         "Wala. Isinusulat lang nito ang file; buo pa rin ang library mo."),
        ("Kasama ba sa backup ang mga na-download kong publikasyon?",
         "Hindi. Datos lang ng personal na pag-aaral. Muling nada-download ang mga publikasyon sa bagong device, at kusang dumidikit uli rito ang mga nota mo."),
        ("Puwede ko bang buksan ang backup para makita ang laman?",
         "Oo. Puwede mong buksan ang .jwlibrary na file sa iyong browser at tingnan ang lahat ng nota, highlight at bookmark na nasa loob, nang walang ini-install at nang hindi lumalabas ang file sa device mo."),
        ("Nag-e-expire ba ang mga backup?",
         "Hindi. Nananatiling maisasauli ang .jwlibrary na file kahit kailan. Magsauli sa kasalukuyang bersiyon ng JW Library sa halip na sa luma, dahil nababasa ng app ang mas lumang anyo ng backup pero hindi ang mas bago."),
        ("Dapat ba akong magbackup bago ang bawat pulong?",
         "Hindi kailangan. Iugnay ang mga backup sa mga pangyayaring maaaring magpawala ng datos — mga update, pagpapaayos, bagong device — kasama ang panapanahong ritmong akma sa dami ng pag-aaral na ayaw mong ulitin."),
        ("Sulit bang itago ang mga backup mula pa noong nakaraang taon?",
         "Oo. Maliliit ang mga ito, at ang anumang nabura mo nang hindi sinasadya mula noon ay naroon pa rin sa loob."),
    ],
}

GUIDES_TL["jw-library-restore-replaced-notes"] = {
    "title": "Pinalitan ng pagsasauli ng JW Library ang mga nota mo? Paano ito mabawi",
    "h1": "Pinalitan ng pagsasauli ang mga nota mo? Narito kung paano pagsamahin ang dalawang backup",
    "description": "Buong palit ang pagsasauli sa JW Library, hindi pagsasama — mukhang "
                   "nawala ang mga notang ginawa pagkatapos ng petsa ng backup. Kung nasa iyo "
                   "pa ang dalawang backup na file, walang nawala. Narito ang solusyon.",
    "intro": [
        "Nakakapanghina ng loob: nagsauli ka ng backup sa device na may mga nota na, at "
        "pinalitan ng pagsasauli ang lahat — mukhang nawala ang mga notang ginawa mo mula noong "
        "backup na iyon. Nangyayari ito dahil buong palit ang Backup at Pagsasauli ng JW "
        "Library, hindi pagsasama.",
        "Ang mahalagang punto: kung nasa isang backup na file pa rin ang mas bagong gawa, wala "
        "talagang nawala. Ang solusyon ay pagsamahin ang dalawang backup sa halip na pumili sa "
        "kanila.",
    ],
    "steps": [
        ("Huminto — huwag munang magsauli ulit",
         "Bawat pagsasauli ay pumapalit sa kasalukuyang datos ng device. Huminto muna bago pa "
         "may mawala."),
        ("I-backup ang device sa kasalukuyang kalagayan nito",
         "Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup. Iniingatan nito ang "
         "kasalukuyang kalagayan, anuman ang laman."),
        ("Hanapin ang backup na may nawawalang mga nota",
         "Ang .jwlibrary na file na pinagsaulian mo, o isang mas luma — tingnan ang email, "
         "Drive, iCloud at ang downloads folder mo."),
        ("Pagsamahin ang dalawang file sa jwsync.org",
         "I-load ang dalawang backup. Pinagsasama ng JW Sync ang lahat ng nota, highlight, "
         "bookmark at tag ng dalawa sa isang bagong file — sa browser, walang ina-upload. Ang "
         "magkasalungat na bersiyon ng iisang nota ay ipapakitang magkatabi para ikaw ang "
         "pumili."),
        ("Isauli ang pinagsamang file",
         "Backup at Pagsasauli → Isauli gamit ang pinagsamang .jwlibrary. Nasa device na muli "
         "ang dalawang set ng nota."),
    ],
    "sections": [
        ("Paano kung walang backup ng mas bagong mga nota?",
         "Kung nasa device lang ang tanging kopya ng mas bagong mga nota at na-overwrite na ito "
         "ng pagsasauli, walang pag-undo ang JW Library. Kaya napakahalaga ng hakbang 2 sa "
         "itaas — ang pag-backup sa kasalukuyang kalagayan bago ang anupamang gawin — tuwing "
         "may mukhang mali sa datos. Sa susunod, ang rutinang “pagsamahin muna” ang gagawing "
         "imposible ang problemang ito."),
    ],
    "faq": [
        ("Madodoble ba ang mga notang nasa dalawang backup?",
         "Hindi — natutukoy ang magkakaparehong item at isa lang ang itatago. Ang tunay na "
         "magkaibang bersiyon lang ng iisang nota ang itatanghal para suriin."),
        ("Naaayos ba nito ang backup na ayaw talagang maisauli?",
         "Kadalasan ay sira ang file, hindi na-overwrite — tingnan sa ibaba ang gabay sa "
         "pag-aayos ng sirang backup."),
    ],
}

GUIDES_TL["fix-corrupted-jw-library-backup"] = {
    "title": "Ayusin ang sirang backup ng JW Library na ayaw maisauli",
    "h1": "Pag-aayos ng sirang backup ng JW Library gamit ang Library Doctor",
    "description": "Ayaw tanggapin ng JW Library ang .jwlibrary na file mo? Sinusuri ng "
                   "Library Doctor ang backup sa browser mo, inaayos ang karaniwang problema, "
                   "at gumagawa ng malinis na kopyang naisasauli.",
    "intro": [
        "Ang backup na hindi naisasauli ay hindi kinakailangang backup na nawalan ng mga nota mo. Karamihan sa mga file na inilalarawan ng mga tao bilang sira ay maayos ang istruktura at tinatanggihan dahil sa isang bagay na maaaring ayusin, o nasira sa paglilipat sa paraang naaayos ng bagong kopya. Sulit dumaan sa mga sanhi bago mo isuko ang file.",
        "Kung minsan ay ayaw tanggapin ng JW Library ang isang backup na file — nabibigo ang "
        "pagsasauli, may error, o ayaw magbukas ng file. Karaniwang dahilan: naputol na "
        "download, cloud drive na nakasira sa file, extension na napalitan sa daan, o mga "
        "hindi pagkakatugma sa loob na naipon sa paglipas ng mga taon.",
        "May kasamang Library Doctor ang JW Sync, isang pagsusuring bumabasa ng .jwlibrary na "
        "file at nag-aayos ng karaniwang problema — buong-buo sa browser mo, at hindi "
        "kailanman umaalis ang file sa device mo.",
    ],
    "steps": [
        ("Buksan ang JW Sync at i-load ang problemang file",
         "Pumunta sa jwsync.org at i-load ang .jwlibrary na file na ayaw maisauli. (Kung "
         "dumating ang file na napalitan ng .zip, ibalik muna ito sa .jwlibrary — iyon lang, "
         "maayos na ang marami.)"),
        ("Patakbuhin ang pagsusuri ng Library Doctor",
         "Sinusuri ng Doctor ang panloob na istruktura ng backup at inililista sa simpleng "
         "salita ang natagpuan nito — mula sa walang bisang kakaiba hanggang sa tunay na "
         "pinsala."),
        ("Ilapat ang mga pag-aayos",
         "Isang tap lang, naaayos ang naaayos. Hindi kailanman ini-edit ng Doctor ang "
         "orihinal mong file; gumagawa ito ng nalinis na kopya, kaya buo pa rin ang orihinal "
         "bilang panangga."),
        ("I-download at isauli ang naayos na file",
         "Isauli ang nalinis na .jwlibrary sa pamamagitan ng Backup at Pagsasauli → Isauli sa "
         "JW Library."),
    ],
    "sections": [
        ("Tumatakbo rin ang Doctor sa bawat pagsasama",
         "Awtomatikong tumatakbo ang parehong pagsusuri sa loob ng merge engine, kaya laging "
         "malinis ang naibibigay na pinagsamang backup — kahit may problema pala ang isa sa "
         "mga file na hindi mo alam."),
        ("Kapag hindi na maaayos ang file",
         "Kung naputol ang file nang husto kaya wala na talaga ang datos, walang tool na "
         "kayang likhain itong muli. Sasabihin ito ng Doctor nang tapat sa halip na maglabas "
         "ng kaduda-dudang file — at iyon ang hudyat para maghanap ng mas lumang kopya sa "
         "email, Drive o iCloud, na siya ring dahilan kung bakit sulit ang pag-iingat ng mga "
         "lumang backup."),
        ("Ano ang karaniwang ibig sabihin ng sira",
         "Sa katotohanan, bihirang sirang datos ito. Ang karaniwang sanhi ay file na naputol sa paglilipat — pinaikli ng nabigong pag-upload o ng messaging app na nag-compress nito — o archive na buo pero may hindi magkatugmang bahagi sa loob na tinatanggihan ng app. Dahil ang .jwlibrary ay ZIP na bumabalot sa SQLite database, maaaring nasa alinman sa dalawang patong ang suliranin, at magkaiba ang kailangang lunas. Hindi maaayos ang naputol na file at kailangang kunin uli; ang hindi magkatugmang database ay karaniwang naaayos."),
        ("Ano talaga ang sinusuri ng isang pag-scan",
         "Tinitiyak ng pag-scan na bumubukas ang archive, na ang userData.db ay nababasang SQLite database na pumapasa sa pagsusuri ng integridad, na tugma ang istruktura sa inaasahan ng JW Library, at na sang-ayon ang manifest sa database na inilalarawan nito — pati ang hash na ginagamit ng app para tiyaking hindi nabago ang file. Ang hindi pagkakatugma ng manifest at database ang isa sa pinakakaraniwang dahilan kung bakit tinatanggihan sa pagsasauli ang backup na maayos naman sa teknikal, at tuwiran itong naaayos."),
        ("Karaniwang walang pinsala ang mga naulilang tala",
         "Madalas mag-ulat ang pag-scan ng tunay na backup ng mga talang tumuturo sa isang bagay na wala na — halimbawa, isang highlight na nakaturo sa lugar ng publikasyong lumipat. Ang mismong mga backup ng JW Library ay kadalasang naglalaman ng daan-daan nito at naisasauli nang walang reklamo. Karaniwang bunga ito ng pag-update ng mga publikasyon sa paglipas ng panahon at hindi patunay ng pinsala, at hindi kailangang linisin ang mga ito para gumana ang file."),
        ("Pagsagip ng mga nota mula sa file na hindi naisasauli",
         "Kahit hindi maayos ang backup nang sapat para tanggapin ito ng JW Library, madalas na nababasa pa rin ang mga notang nasa loob. Ang pagbukas ng file sa iyong browser ay nagbibigay-daan sa iyong makita at makopya nang tuwiran ang teksto ng nota, at ginagawa nitong nabawing materyal sa pag-aaral ang isang file na hindi na magagamit. Kung may pangalawa at mas lumang backup kang naisasauli, mapagsasama sa loob nito ang nababasang laman ng sirang file sa halip na muling itipa."),
        ("Kapag nabigo ang pagsasauli nang walang malinaw na error",
         "Madalas tanggihan ng JW Library ang file nang hindi ipinapaliwanag kung bakit. Ang pinakamadalas na sanhi ay manifest na ang hash ay hindi na tugma sa database na inilalarawan nito, file na naputol sa paglilipat, o backup na isinulat ng bersiyon ng app na mas bago kaysa sa pinagsasaulian mo. Naaayos ang una, kailangang kunin uli sa pinagmulan ang pangalawa, at naaayos ang pangatlo sa pag-update ng app bago magsauli."),
        ("Paano ito maiiwasan sa susunod",
         "Halos lahat ng pinsala ay nangyayari sa daan. Ilipat ang mga backup bilang file at hindi sa pamamagitan ng anumang maaaring mag-compress muli, at piliin ang cloud, AirDrop o kable kaysa sa mga messaging app. Pagkatapos maglipat, tiyaking tugma ang laki sa orihinal — ang file na kapansin-pansing mas maliit kaysa sa ipinadala mo ay naputol, at walang pag-aayos na magbabalik ng byte na hindi naman dumating."),
        ("Kung wala nang umuubra",
         "Ang file na hindi maaayos ay maaaring nababasa pa rin, at madalas na sapat na ang mabasa ito — nababawi nang tuwiran ang teksto ng nota kahit tinatanggihan ng JW Library ang file. Pagsamahin ito sa anumang mas lumang backup na naisasauli at karaniwang mananatili sa iyo ang nakararaming bahagi ng aklatan. Bago mo ipasyang wala nang silbi ang isang file, buksan ito at tingnan kung ano talaga ang nasa loob."),
    ],
    "faq": [
        ("Ina-upload ba ang datos ko para sa pagsusuri?",
         "Hindi. Ang pagsusuri, pag-aayos at pag-export ay pawang tumatakbo sa loob ng "
         "browser."),
        ("Kaya ba nitong mabawi ang mga notang binura sa loob ng JW Library?",
         "Hindi — ang istruktura ng file ang inaayos nito. Ang mga notang binura sa app bago "
         "gawin ang backup ay wala sa file para mabawi pa."),
        ("May mawawala bang nota sa pag-aayos ng file?",
         "Sa kopya gumagana ang pag-aayos at tumutugon ito sa suliranin ng istruktura, hindi ng nilalaman. Hindi kailanman binabago ang orihinal mong file, kaya nananatili itong magagamit kung gusto mong magsimula uli."),
        ("Bakit nasira ang backup ko?",
         "Kadalasan, nabago ang file sa daan — ipinadala sa app na nag-compress o nagputol nito, o hindi natapos na pag-upload. Karaniwang naaayos ito sa muling paglilipat mula sa pinagmulan."),
        ("Nakakabawi ba ang pag-scan ng mga notang binura ko sa loob ng JW Library?",
         "Hindi. Kapag nabura na sa app at nakagawa ng bagong backup, wala na ang nota sa file na iyon. Naroon pa rin ito sa backup na mas nauna sa pagbura."),
        ("Masasabi ba sa laki ng file kung naputol ito?",
         "Madalas, oo. Ihambing sa orihinal kung nasa iyo pa; ang malaking pagkakaiba ay nangangahulugang hindi natapos ang paglilipat."),
        ("Tiyak bang maisasauli ang backup na bumubukas sa browser?",
         "Hindi tiyak, pero malakas itong palatandaan na maayos ang archive at ang database, na nag-aalis sa pinakakaraniwang pagkabigo."),
    ],
}

GUIDES_TL["edit-jw-library-notes"] = {
    "title": "Tingnan at i-edit ang mga nota sa JW Library sa browser",
    "h1": "Tingnan, hanapin at i-edit ang mga nota mo sa JW Library — Study Explorer",
    "description": "Buksan ang kahit anong .jwlibrary na backup sa browser mo para tingnan, "
                   "hanapin, i-edit, palitan ng tag, palitan ng kulay at maramihang linisin "
                   "ang mga nota, highlight at bookmark mo sa JW Library. Walang ina-upload.",
    "intro": [
        "Ginawa ang JW Library para sa pagsulat ng nota, hindi sa pamamahala ng libu-libo. "
        "Binubuksan ng Study Explorer ang kahit anong .jwlibrary na backup sa browser mismo at "
        "ginagawa itong mahahanap at ma-e-edit na tagapamahala ng library — mga nota, "
        "highlight at bookmark sa iisang lugar, at walang ina-upload kahit saan.",
    ],
    "steps": [
        ("Mag-load ng backup",
         "Gumawa ng backup sa JW Library (Personal na Pag-aaral → Backup at Pagsasauli → "
         "Gumawa ng backup), tapos buksan ang jwsync.org at i-load ang file sa Study "
         "Explorer."),
        ("Tingnan at hanapin ang lahat",
         "Tatlong tab — Mga Nota, Mga Highlight, Mga Bookmark — na may buong paghahanap sa "
         "teksto at pang-salang kulay, tag at publikasyon. May tab din para sa Mga Sagot sa "
         "Pag-aaral na nagpapakita ng mga isinulat mong sagot sa mga publikasyon."),
        ("Mag-edit nang diretso",
         "Buksan ang kahit anong nota para i-edit ang pamagat at nilalaman nito nang may "
         "pormat (bold, italic, salungguhit, listahan), palitan ang kulay ng highlight, at "
         "magdagdag o mag-alis ng tag. Ganoon din ang pag-edit sa mga bookmark at kulay ng "
         "highlight."),
        ("Maglinis nang maramihan",
         "Pumili ng maraming nota nang sabay para palitan ng tag, palitan ng kulay o burahin "
         "nang sama-sama — may buong undo at redo, kaya hindi kailanman nakamamatay ang "
         "pagkakamali. Puwede ka ring kumuha ng mga notang nasa isang saklaw ng petsa tungo sa "
         "bagong backup, o kopyahin ang mga nota bilang Markdown."),
        ("I-export ang na-edit mong library",
         "I-download ang na-edit na .jwlibrary at isauli ito sa JW Library. Nasa device na ang "
         "mga pagbabago mo."),
    ],
    "sections": [
        ("Bakit sa browser mag-edit sa halip na sa app?",
         "Dahil sa dami. Ang pagpapalit ng pangalan ng isang tag sa 300 nota, ang pagpapalit "
         "ng kulay ng lahat ng dilaw na highlight sa isang publikasyon, o ang pagbura sa "
         "taon-taong lumang bookmark ay ilang minuto lang dito at oras-oras na pag-tap sa app. "
         "Karaniwang backup ang na-export na file, kaya isinasauli ito ng JW Library gaya ng "
         "iba."),
    ],
    "faq": [
        ("Naaapektuhan ba ng pag-edit ang orihinal kong backup?",
         "Hindi — sa isang kopya sa loob ng browser ginagawa ang mga pag-edit at nase-save sa "
         "bagong na-export na file. Nananatiling gaya ng dati ang orihinal."),
        ("May limitasyon ba sa laki ng library?",
         "Hinahati sa pahina ang napakalaking library para manatiling mabilis ang "
         "pagtingin-tingin; gumagana ang paghahanap at mga salang sa kabuuan."),
    ],
}

GUIDES_TL["search-jw-library-notes"] = {
    "title": "Hanapin ang mga nota sa JW Library ayon sa kahulugan — Tanungin ang Library Mo",
    "h1": "Tanungin ang Library Mo: hanapin ang mga nota mo ayon sa kahulugan",
    "description": "Paghahanap ayon sa kahulugan para sa mga nota mo sa JW Library: hanapin "
                   "ang halos nakalimutan mong nota sa pamamagitan ng paglalarawan dito, kahit "
                   "hindi mo maalala ang eksaktong salita. Nasa device, kayang offline, "
                   "pribado.",
    "intro": [
        "Alam ng may taon-taong nota ang problemang ito: naaalala mong sumulat ka tungkol sa "
        "pagbabata ng pagsubok nang may kagalakan, pero walang salitang “pagbabata” sa nota, "
        "kaya walang nakikita ang paghahanap sa keyword. Ayon sa kahulugan naghahanap ang "
        "Tanungin ang Library Mo — ilarawan mo ang kaisipan, at lilitaw ang pinakamalalapit na "
        "nota, anuman ang pagkakasulat.",
        "Sa device mo lang ito tumatakbo: minsan lang nada-download ang language model sa "
        "browser at pagkatapos ay gumagana na kahit offline, na may pabilis na WebGPU kung "
        "saan available. Hindi kailanman ipinapadala ang mga nota mo kahit saan.",
    ],
    "steps": [
        ("Mag-load ng backup sa Study Explorer",
         "Sa jwsync.org, i-load ang .jwlibrary na file mo at buksan ang tab na Magtanong."),
        ("Hayaang maghanda ang model nang minsan",
         "Sa unang paggamit, nada-download ang model sa device at ini-index ang mga nota mo. "
         "Minsan lang ito; pagkatapos ay agad na itong gumagana, kahit offline."),
        ("Magtanong sa sarili mong salita",
         "I-type ang naaalala mo — “iyong notang tungkol sa pagiging matiyaga sa mga bago sa "
         "paglilingkod”, “pampatibay para sa nanghihinang payunir” — at lilitaw ang "
         "pinakamalalapit na nota, nakaayos ayon sa kahulugan."),
    ],
    "sections": [
        ("Ano ang pagkakaiba sa karaniwang paghahanap",
         "Titik ang itinatapat ng paghahanap sa keyword; kaisipan naman ang itinatapat ng "
         "paghahanap ayon sa kahulugan. Ang tanong tungkol sa “pagkabalisa” ay nakakahanap din "
         "ng mga notang gumamit ng “alalahanin”, “kabalisahan sa buhay” o ng isang tekstong "
         "may kaugnayan. Nasa Study Explorer ang dalawang uri ng paghahanap — nagtutulungan "
         "sila."),
        ("Pribado sa pagkakadisenyo",
         "Hindi ito serbisyo ng AI sa cloud. Sa loob ng tab ng browser mo tumatakbo ang model, "
         "nasa device mo ang index, at kapag isinara mo ang tab, tapos na iyon. Walang tungkol "
         "sa mga nota mo ang umaalis sa makina mo."),
    ],
    "faq": [
        ("Kailangan ba ng malakas na device?",
         "Kayang-kaya ito ng makabagong cellphone o laptop; pinakamabilis sa mga device na may "
         "WebGPU. May mapagpipiliang laki ng model ayon sa hardware mo."),
        ("Gumagana ba ito sa wika ko?",
         "Oo — gumagana ang paghahanap sa mga wikang ginamit sa mga nota mo, at nakasalin ang "
         "interface sa lahat ng 12 wikang sinusuportahan ng JW Sync."),
    ],
}

GUIDES_TL["jw-library-study-stats"] = {
    "title": "Tingnan ang Study Stats mo sa JW Library: streak, heatmap at parangal",
    "h1": "Ang study stats mo sa JW Library: streak, heatmap, saklaw at parangal",
    "description": "Gawing pribadong pagsusuri ng pag-aaral ang isang backup ng JW Library — "
                   "kabuuan, heatmap ng aktibidad, streak, saklaw ng Bibliya sa 66 aklat, "
                   "profile ng ugali sa pag-aaral at mga 200 parangal.",
    "intro": [
        "Tahimik na iniingatan ng backup na file mo ang taon-taong kasaysayan ng pag-aaral — "
        "kung kailan ka sumusulat ng nota, kung ano ang hina-highlight mo, kung aling aklat "
        "ang natapos mo. Binabasa ng pahinang Study Stats ang .jwlibrary na backup at ginagawa "
        "itong pribadong dashboard, na buong kinakalkula sa loob ng browser mo.",
    ],
    "steps": [
        ("Gumawa ng backup",
         "Sa JW Library: Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup."),
        ("Buksan ang pahinang Study Stats",
         "Pumunta sa jwsync.org/highlights.html at i-load ang file."),
        ("Galugarin ang kuwento ng pag-aaral mo",
         "Mga pangunahing kabuuan, tanawin ayon sa Taon ng Paglilingkod at sa Buong Panahon, "
         "paglago taon-taon — tapos nasa ibaba ang mga nakalilibang na bahagi."),
    ],
    "sections": [
        ("Ano ang makikita mo",
         "Isang heatmap ng aktibidad na may pinakamahaba at kasalukuyang streak; ritmo bawat "
         "linggo, pinakaabalang oras at buwan; saklaw ng Bibliya sa lahat ng 66 aklat na may "
         "hati sa Hebreong at Griegong Kasulatan; gulong ng kulay ng mga highlight, histogram "
         "ng haba ng nota at word cloud; 24-oras na orasan ng pag-aaral at radar ng "
         "panahunan."),
        ("Profile, paglalakbay at parangal",
         "Isang Study Profile na may anim na katangian (Pagiging Palagian, Kasipagan, Lalim, "
         "Lawak, Pagbubulay-bulay, Katatagan) na may “Study Signature”; isang Study Journey na "
         "60 antas sa 12 pinangalanang baitang; at mga 200 parangal mula Karaniwan hanggang "
         "Alamat, kasama ang mga medalyang nakabatay sa nilalaman. Isang Shareable Card ang "
         "bumubuod sa taon mo nang walang inilalantad na kahit isang nota."),
        ("Isang dahilan araw-araw para bumalik",
         "Ipinapakita ng Resurface ang mga notang isinulat mo sa araw ding ito noong mga "
         "nakaraang taon at bumubuo ng banayad na pag-uulit sa may agwat — kaunti ngunit "
         "madalas, iyon ang nagpapanatili ng pag-aaral."),
    ],
    "faq": [
        ("May ina-upload ba rito?",
         "Wala. Sa browser mo binabasa ang backup; hindi umaalis ang estadistika sa device "
         "mo."),
        ("Kusa bang nag-a-update ang estadistika?",
         "Sinasalamin nila ang backup na ini-load mo — gumawa ng bagong backup para sa bagong "
         "estadistika."),
    ],
}

GUIDES_TL["share-jw-library-notes"] = {
    "title": "Paano ibahagi ang mga nota sa JW Library sa isang kaibigan",
    "h1": "Paano ibahagi ang mga nota sa JW Library sa isang kaibigan — walang server",
    "description": "Ipadala sa kaibigan ang piling mga nota sa JW Library (kasama ang mga "
                   "highlight nito) sa maliit na file — walang server, walang account. "
                   "Maidaragdag ito ng tumatanggap nang hindi napapalitan ang sarili niyang "
                   "mga nota.",
    "intro": [
        "Walang paraan sa JW Library para bigyan ang iba ng kopya ng piling mga nota. Puwedeng "
        "ipadala ang buong backup — pero ibinibigay nito ang lahat, at buburahin ng pagsasauli "
        "ang library ng tatanggap. Nilulutas ng pagbabahagi ng nota sa JW Sync ang dalawa: "
        "pipiliin mo mismo kung aling nota ang ibabahagi, at maidaragdag iyon ng tatanggap "
        "nang walang nawawala.",
    ],
    "steps": [
        ("Piliin ang mga notang ibabahagi",
         "Sa pahina ng pagbabahagi sa jwsync.org/share.html, i-load ang backup mo at piliin "
         "ang mga nota — ilan mula sa isang pahayag, o lahat ng nasa ilalim ng isang tag sa "
         "isang klik gamit ang pang-salang tag. Kasama ring dadala ang mga highlight na "
         "nakakabit sa mga notang iyon."),
        ("Ipadala ang share file",
         "Gumagawa ang JW Sync ng maliit na file na naglalaman lamang ng mga piniling nota. "
         "Ipadala ito sa kahit anong paraan — messaging app, email, AirDrop. Walang server at "
         "walang account; ang file na iyon ang buong palitan."),
        ("Idaragdag ito ng tatanggap",
         "Bubuksan ng kaibigan mo ang parehong pahina, ilo-load ang share file kasama ang "
         "sarili niyang backup, at makakakuha siya ng bagong backup na may dagdag na mga nota "
         "mo. Hindi kailanman napapalitan ang sarili niyang mga nota — kung may sagutan ang "
         "isang ibinahaging nota at isa sa kaniya, siya ang pipili kung paano ito idaragdag — "
         "at may tag ang mga na-import na nota, kaya madaling hanapin, suriin o alisin sa "
         "bandang huli."),
    ],
    "sections": [
        ("Mabubuting gamit",
         "Pagpapasa ng pananaliksik sa katuwang sa pag-aaral, pagbabahagi ng nota sa pulong sa "
         "isang lumiban, pagbibigay sa bagong mamamahayag ng panimulang set ng nota sa isang "
         "publikasyon, o paglilipat ng mga nota ng isang proyekto sa kapamilya — lahat ito nang "
         "hindi inilalantad ang natitira sa alinmang library."),
    ],
    "faq": [
        ("Kailangan bang mag-install ng JW Sync ang tatanggap?",
         "Walang ini-install sa alinmang panig — isa itong web page. Ang kailangan lang ng "
         "tatanggap ay ang share file at ang sarili niyang backup."),
        ("Puwede ko bang bawiin ang pagbabahagi o patapusin ang file?",
         "Karaniwang file lang ang ipinadala mo — walang kopya sa server na puwedeng "
         "patapusin. Ibahagi lang ang ibabahagi mo rin sa kahit anong mensahe."),
    ],
}

GUIDES_TL["bible-reading-plan"] = {
    "title": "Araw-araw na plano sa pagbabasa ng Bibliya kasama ang sarili mong mga nota",
    "h1": "Reading Companion: plano sa pagbabasa ng Bibliya kasama ang mga nota mo",
    "description": "Isang pribadong araw-araw na iskedyul sa pagbabasa ng Bibliya na "
                   "nagpapakita ng mga nota at highlight na ginawa mo sa mga kabanata ngayong "
                   "araw. Pumili ng bilis, panatilihin ang streak, panoorin ang grid ng 66 "
                   "aklat na napupuno.",
    "intro": [
        "Maraming app ang may iskedyul sa pagbabasa ng Bibliya. May kayang gawin ang Reading "
        "Companion na wala sa iba: dahil binabasa nito ang sarili mong .jwlibrary na backup, "
        "kasama ng babasahin ngayong araw ang mga nota at highlight na ikaw mismo ang gumawa "
        "sa mga kabanatang iyon — “apat na talata sa Awit 37 ang na-highlight mo dalawang taon "
        "na ang nakalipas.” Pagbabasa sa pamamagitan ng iyong sariling kasaysayan sa "
        "pag-aaral, at nasa device mo lahat.",
    ],
    "steps": [
        ("Pumili ng pagkakasunod-sunod at bilis",
         "Magbasa ayon sa pagkakasunod ng Bibliya o sa tinatayang pagkakasunod ayon sa "
         "panahon; tapusin sa 3 buwan, 6 na buwan, 1 taon, 2 taon, o itakda ang sarili mong "
         "bilang ng kabanata kada araw — may live na tanawing “matatapos ka sa palagay na…”."),
        ("Basahin ang bahagi ngayong araw",
         "Isang tap lang ang bawat kabanata, at bubukas ito nang diretso sa JW Library o sa "
         "Watchtower ONLINE LIBRARY sa wika mo. Tsekan ang mga kabanata habang sumusulong."),
        ("Isama ang mga nota mo (opsiyonal)",
         "Mag-load ng backup sa kahit anong tool ng JW Sync at lilitaw ang sarili mong mga "
         "nota at bilang ng highlight sa mismong ilalim ng mga kabanata ngayong araw."),
        ("Panoorin ang paglago ng pagsulong",
         "Napupuno ang grid ng 66 aklat habang nagbabasa ka, na may bar ng nabasang kabanata, "
         "hulang batay sa bilis, at mga hangganang natatapos ang bawat aklat, ang Hebreo-Aramaikong "
         "Kasulatan, ang Griegong Kasulatan — at ang buong Bibliya."),
    ],
    "sections": [
        ("Streak nang walang pagkokonsiyensiya",
         "Ang pagtatapos ng isang araw ay nagpapahaba ng streak mo; ang pagkakalampas naman ay "
         "naglilipat lang ng inaasahang petsa ng pagtatapos. Walang natitipong utang — ang "
         "plano ang umaayon sa buhay mo, hindi ikaw ang pinapagalitan."),
    ],
    "faq": [
        ("Kailangan ko bang mag-load ng backup para magamit ito?",
         "Hindi — kusang gumagana ang plano, streak at pagsulong. Ang backup ay nagdaragdag "
         "lang ng sarili mong mga nota sa babasahin ng bawat araw."),
        ("Pribado ba ang pagsulong ko sa pagbabasa?",
         "Oo. Nananatili ang pagsulong sa browser sa device mo — walang account at walang "
         "ina-upload."),
    ],
}

GUIDES_TL["open-jwlibrary-file"] = {
    "title": "Ano ang .jwlibrary na file at paano ito buksan?",
    "h1": "Ano ang .jwlibrary na file — at paano ito buksan sa kahit anong device",
    "description": "Ang .jwlibrary na file ay ang backup mo sa JW Library: isang file na "
                   "naglalaman ng bawat nota, highlight, bookmark at tag. Narito ang laman "
                   "nito at kung paano ito buksan at basahin.",
    "intro": [
        "Mukhang hindi mababasa ang .jwlibrary na file, pero hindi naman. Karaniwang ZIP archive ito sa paligid ng karaniwang SQLite database, na nangangahulugang mababasa mo ang sarili mong backup — makikita mismo kung anong mga nota, highlight at bookmark ang laman nito — nang walang JW Library at nang wala kang ini-install kahit ano.",
        "Kapag nag-backup ka ng JW Library, may makukuha kang file na nagtatapos sa "
        ".jwlibrary. Isa itong nag-iisa at nadadalang pakete na naglalaman ng lahat ng nasa "
        "personal mong pag-aaral — mga nota, highlight, bookmark, tag at playlist — sa isang "
        "siksik na database. Hindi ito dokumentong binubuksan sa Word o sa PDF reader; ginawa "
        "ito para maisauli pabalik sa JW Library.",
        "Pero hindi mo kailangang isauli ito para lang sumilip sa loob. Binubuksan ng JW Sync "
        "ang .jwlibrary na file diretso sa browser mo, kaya nababasa, nahahanap at "
        "nae-edit mo ang laman nito nang hindi ginagalaw ang cellphone.",
    ],
    "steps": [
        ("Kumuha ng .jwlibrary na file",
         "Ginagawa ito sa JW Library: Personal na Pag-aaral → tatlong-tuldok na menu → Backup "
         "at Pagsasauli → Gumawa ng backup. Iyan ang file na tinutukoy natin."),
        ("Buksan ito sa JW Sync",
         "Pumunta sa jwsync.org at i-load ang file sa Study Explorer. Agad itong bumubukas, sa "
         "device mo — walang ina-upload."),
        ("Basahin at gamitin ito",
         "Tingnan ang mga nota, highlight at bookmark; maghanap sa lahat; mag-edit, magpalit "
         "ng tag o mag-export. Kapag tapos ka na, puwede mong isauli ang file (o ang na-edit "
         "na kopya) pabalik sa JW Library."),
    ],
    "sections": [
        ("Ano talaga ang laman ng file",
         "Sa teknikal na paraan, ang .jwlibrary na file ay isang naka-zip na SQLite database "
         "kasama ang manifest. Kaya nga minsan ay aksidenteng napapalitan ito ng .zip sa "
         "daan — at kaya rin naaayos ito kapag ibinalik sa .jwlibrary. Hindi mo kailangang "
         "alamin ito para magamit ang file, pero ipinapaliwanag nito kung bakit maliit, "
         "kompleto sa sarili, at magkatulad ito sa Android, iPhone, iPad at Windows."),
        ("Pagbubukas nito sa computer",
         "Gumagana rin ang parehong pahinang jwsync.org sa browser ng laptop o desktop — "
         "madaling gamitin para basahin ang taon-taong nota sa malaking screen, o para sa "
         "maramihang paglilinis na nakakapagod sa cellphone. Walang kailangang i-install."),
        ("Ano talaga ang file",
         "Ang .jwlibrary na file ay ZIP archive na iba lang ang extension. Nasa loob nito ang userData.db — isang SQLite database na may mga nota, highlight, bookmark at tag mo — at ang manifest.json, isang maliit na file na naglalarawan sa backup, kasama ang hash ng database na ginagamit ng JW Library para tiyaking hindi nabago ang file. Walang pag-aari o naka-encrypt dito; karaniwang archive ito sa paligid ng karaniwang database."),
        ("Pagbukas nito nang walang JW Library",
         "Hindi mo kailangan ang app, ni anumang software, para basahin ang sarili mong backup. Ipinapakita ng pagbukas ng file sa iyong browser ang lahat ng nota, highlight at bookmark na nasa loob, may paghahanap at pagsala, at hindi kailanman lumalabas ang file sa device mo — binabasa ito sa lugar mismo sa halip na i-upload. Ito ang pinakamabilis na paraan para tiyaking naglalaman ang backup ng inaakala mo bago ang isang reset, pagpapalit ng device, o pagsasauli sa bagong telepono."),
        ("Pagsilip sa loob nang manwal",
         "Kung interesado ka, kopyahin ang file, palitan ang pangalan ng kopya ng .zip at buksan sa anumang kasangkapan sa archive. Makikita mo ang userData.db at ang manifest.json. Kailangan ng SQLite viewer para buksan ang database, at ipinangalan ang mga talahanayan sa laman nila — Note, UserMark, Bookmark, Tag. Palaging sa kopya magtrabaho: ang pagbabago sa database nang manwal nang hindi ina-update ang hash sa manifest ay gumagawa ng file na tatanggihang isauli ng JW Library."),
        ("Ligtas na pagbabago",
         "Puwedeng itama, palitan ng tag, palitan ng kulay o burahin ang mga nota sa labas ng app, at i-export ang bunga bilang bagong .jwlibrary na file na isasauli mo nang normal. Ang tuntuning gumagawa nitong ligtas ay ang pag-iingat sa orihinal: baguhin ang kopya, isauli ang binagong file, at kung may hindi naaayon sa inaasahan mo, naroon pa rin ang hindi ginalaw na orihinal na mababalikan."),
        ("Pagbasa ng backup sa telepono",
         "Hindi kailangan ng kompyuter. Gumagana rin ang pagbukas ng file sa browser ng telepono, na kapaki-pakinabang kapag nasa telepono na ang backup at gusto mong tiyakin ang laman nito bago magsauli o bago burahin ang device. Binabasa ang file sa lugar mismo, kaya gumagana ito nang walang koneksiyon maliban sa pag-load ng pahina."),
        ("Bakit mahalaga ang hash sa manifest",
         "Itinatala ng manifest.json ang hash ng userData.db. Ginagamit ito ng JW Library para tiyaking hindi nabago ang database mula nang isulat ang backup, kaya tinatanggihan sa pagsasauli ang file na binago ang database nang hindi muling kinuwenta ang hash. Ito ang pinakakaraniwang dahilan kung bakit tumitigil sa paggana ang backup na binago nang manwal, at ang dahilan kung bakit mas ligtas ang pagbabago sa pamamagitan ng kasangkapang muling sumusulat ng manifest kaysa sa tuwirang paggalaw sa database."),
        ("Para saan ito kapaki-pakinabang",
         "Binabago ng kakayahang basahin ang backup ang mismong halaga ng backup. Matitiyak mong naglalaman ang file ng inaakala mo bago mo burahin ang telepono, matitingnan kung sulit isauli ang lumang file, mahahanap ang notang alam mong isinulat mo nang hindi naghahalungkat sa app, o mababawi ang teksto mula sa file na hindi tinatanggap ng JW Library. Wala sa mga ito ang nangangailangang ipagkatiwala mo ang file kaninuman — sa sarili mong device ito binabasa."),
    ],
    "faq": [
        ("Puwede ko bang buksan ang .jwlibrary na file sa Excel o Notepad?",
         "Hindi kapaki-pakinabang — database ito, hindi spreadsheet o text file. Buksan ito sa "
         "JW Sync para basahin, o i-export ang mga nota mo bilang Markdown/teksto mula sa "
         "Study Explorer."),
        ("Ligtas bang buksan ang backup ko sa browser?",
         "Oo. Binabasa ng JW Sync ang file sa loob ng tab ng browser mo; walang ipinapadala sa "
         "server, at hindi kailanman binabago ang orihinal mong file."),
        ("Puwede ko bang basta palitan ng .zip ang pangalan?",
         "Oo, sa isang kopya. Hindi binabago ng pagpapalit ng pangalan ang nilalaman, at nagbibigay-daan ito sa anumang kasangkapan sa archive na ipakita sa iyo ang nasa loob."),
        ("Nababago ba ang file kapag binuksan?",
         "Hindi. Ang pagbasa ng backup — sa browser o sa kasangkapan sa archive — ay nag-iiwan ditong walang pinagbago kahit sa antas ng byte. Bagong file lang ang nabubuo kapag nag-save o nag-export ka."),
        ("Kailangan ko bang naka-online?",
         "Para lang ma-load ang pahina. Binabasa ang file sa device mo at hindi ito ina-upload, kaya hindi kailanman dumadaan sa network ang mga nota mo."),
        ("Puwede ko bang buksan ang backup na ipinadala sa akin ng iba?",
         "Oo, hindi nakatali ang anyo sa isang device o account. Ibang usapan kung dapat mo bang isauli ito, dahil pinapalitan ng pagsasauli ang sarili mong aklatan."),
        ("May kailangan ba akong i-install para makasilip sa loob?",
         "Wala. Sapat na ang browser para basahin ang mga nota; ang manwal na pagsusuri lang sa mismong database ang nangangailangan ng SQLite viewer."),
    ],
}

GUIDES_TL["jw-library-windows-pc"] = {
    "title": "Mag-backup at magsama ng JW Library sa Windows PC",
    "h1": "Paggamit ng mga backup ng JW Library sa Windows PC",
    "description": "Kung paano mag-backup ng JW Library sa Windows, at kung paano pagsamahin "
                   "ang backup ng PC sa cellphone at tablet mo para manatiling magkakasama ang "
                   "mga nota, highlight at bookmark sa bawat device.",
    "intro": [
        "Tumatakbo ang JW Library sa Windows gaya sa cellphone at tablet, at gumagawa ito ng "
        "parehong .jwlibrary na backup. Ibig sabihin, puwedeng maging bahagi ang PC mo ng "
        "parehong library sa pag-aaral gaya ng cellphone mo — basta pagsasamahin mo ang mga "
        "backup sa halip na isauli ang isa sa ibabaw ng isa pa.",
    ],
    "steps": [
        ("Mag-backup sa Windows",
         "Sa JW Library app para sa Windows, buksan ang menu, pumunta sa Backup at Pagsasauli, "
         "at gumawa ng backup. I-save ang .jwlibrary na file sa lugar na madaling hanapin."),
        ("I-backup din ang cellphone at tablet mo",
         "Sa bawat device: Personal na Pag-aaral → tatlong-tuldok na menu → Backup at "
         "Pagsasauli → Gumawa ng backup."),
        ("Pagsamahin ang mga ito sa jwsync.org",
         "Buksan ang jwsync.org sa kahit anong browser sa PC at i-load ang lahat ng backup na "
         "file. Pinagsasama ng JW Sync ang mga nota, highlight, bookmark at tag ng bawat "
         "device sa iisang pinagsamang .jwlibrary na file — sa PC mismo, walang ina-upload."),
        ("Isauli ang pinagsamang file kahit saan",
         "Isauli ang pinagsamang file sa Windows app at sa bawat mobile device. Kumpleto na "
         "ang library sa PC, cellphone at tablet."),
    ],
    "sections": [
        ("Bakit sa PC ito pinakamadali",
         "Mas mabilis sa browser ng computer ang pag-load ng maraming file, pagsusuri sa "
         "preview ng pagsasama, at pag-save ng resulta kaysa sa pag-tap sa cellphone. Marami "
         "ang nag-iingat ng pangunahing rutina ng pagsasama sa computer at isinasauli na lang "
         "ang pinagsamang file sa mga mobile device nila."),
    ],
    "faq": [
        ("Gumagana ba ang backup sa Windows kasama ang sa iPhone at Android?",
         "Oo — pareho ang .jwlibrary na format sa lahat ng plataporma, kaya malayang "
         "nagsasama ang backup sa Windows at ang sa cellphone at tablet."),
        ("May kailangan ba akong i-install sa PC?",
         "Wala. Web page ang JW Sync; tumatakbo ito sa Edge, Chrome o Firefox nang walang "
         "ini-install."),
    ],
}

GUIDES_TL["recover-jw-library-notes-lost-phone"] = {
    "title": "Paano mabawi ang mga nota sa JW Library matapos mawala o masira ang cellphone",
    "h1": "Pagbawi ng mga nota sa JW Library mula sa nawala, nasirang o na-reset na cellphone",
    "description": "Nawala o na-reset ang cellphone na may mga nota mo sa JW Library? Ang "
                   "mababawi mo ay nakasalalay sa mga backup mo. Narito kung paano eksaktong "
                   "mababawi ang mga nota — at kung ano ang gagawin sa susunod.",
    "intro": [
        "Una ang tapat na sagot, dahil makatitipid ito sa iyong pagbabasa. Kung may .jwlibrary backup saanman sa labas ng nawalang device, babalik ang lahat ng laman nito sa pamamagitan ng sariling restore ng JW Library, at hindi mo kailangan ang site na ito para sa bahaging iyon. Kung wala talagang backup sa anumang anyo, hindi na mababawi ang personal na datos ng pag-aaral: sa device lamang ito nakatira, at walang kasangkapang makapagbabago niyan.",
        "Ang tunay na natutulungan ng pahinang ito ay ang gitnang kaso, at mas madalas pa ito kaysa sa dalawa: may backup ka, pero hindi ito ang buong kuwento. Maaaring ilang buwan na ito, o baka nag-aaral ka na sa pamalit na telepono — kaya ang basta pag-restore ay magpapalit lang ng isang set ng tala sa isa pa sa halip na maibalik ang lahat.",
        "Ang pagsasama ng dalawa ang mismong hindi kayang gawin ng JW Library, at iyan ang paksa ng natitirang bahagi ng pahinang ito. Pero una, ang paghahanap: madalas na mas marami ang backup ng mga tao kaysa sa natatandaan nilang ginawa.",
    ],
    "steps": [
        ("Hanapin sa bawat lugar na maaaring may backup",
         "Tingnan ang email mo (maghanap ng “jwlibrary” o “backup”), Google Drive, iCloud "
         "Drive, OneDrive, Dropbox at ang Downloads folder ng computer mo. Maliliit na file "
         "ang mga backup kaya madaling makalimutang na-save mo pala."),
        ("Tingnan ang iba mong device",
         "Kung nakagamit ka na ng JW Library sa tablet o PC, may sarili itong datos sa "
         "pag-aaral — gumawa ka ng backup mula rito ngayon din para maingatan ang laman "
         "nito."),
        ("Isauli ang nahanap mo sa bagong cellphone",
         "I-install ang JW Library sa bagong device, tapos Backup at Pagsasauli → Isauli, at "
         "i-load ang .jwlibrary na file. Babalik ang mga nota, highlight at bookmark mo."),
        ("Magsama kung mahigit isa ang backup na nahanap",
         "Ang magkaibang device o petsa ay maaaring may sariling natatanging mga nota. Huwag "
         "pumili ng isa lang — i-load lahat sa jwsync.org, pagsamahin sa isang kumpletong file, "
         "at iyon ang isauli. Walang naiiwan."),
    ],
    "sections": [
        ("Kung wala talagang backup kahit saan",
         "Maging tapat ka sa sarili mo agad: kung nasa nawalang cellphone lang ang tanging "
         "kopya ng mga nota mo at hindi ka kailanman nag-export ng backup, walang kopya sa "
         "cloud ang JW Library na mapagsasaulian. Masakit iyon — at iyan mismo ang dahilan "
         "kung bakit napakahalaga ng ugaling nasa ibaba."),
        ("Para hindi na maulit",
         "Maglagay ng buwanang paalala sa pag-backup at itago ang bawat .jwlibrary na file sa "
         "labas ng cellphone (sapat nang i-email mo ito sa sarili mo). Kaya ka pang "
         "paalalahanan ng JW Sync at pagsamahin ang mga device mo nang regular. Nabubuhay "
         "nang mas matagal kaysa sa kahit anong cellphone ang file na nasa inbox mo."),
        ("Kung saan maaaring may backup na",
         "Bago mo tapusing wala, suriin ang lahat ng lugar kung saan maaaring na-save ang file: ang folder ng Downloads at Documents ng anumang kompyuter na pinagkabitan mo ng telepono, ang mga naipadala sa email, ang mga messaging app kung saan maaaring naipadala mo ang file, at bawat cloud account na ginagamit mo. Madalas na minsang gumawa ng backup ang tao, ilang buwan na ang nakalipas, at nalimutan — at ang backup na ilang buwan na ay naglalaman pa rin ng nakararaming bahagi ng aklatan ng pag-aaral."),
        ("Pagsasauli sa ibang telepono o plataporma",
         "Hindi kailangang katulad ng nawala ang kapalit na device. Naisasauli sa iPhone ang backup mula sa Android na telepono at gayundin sa kabaligtaran, dahil magkatulad ang anyo sa Android, iOS, iPadOS at Windows. I-install ang JW Library sa bagong device, i-update ito sa kasalukuyang bersiyon, saka magsauli sa Personal na Pag-aaral → Backup at Pagsasauli."),
        ("Kung luma o bahagya lang ang backup na mayroon ka",
         "Isauli pa rin. Ang pagbawi ng nakararaming bahagi ng mga nota mo ay hindi pang-aliw — iyon ang bunga. Kung may makita kang pangalawa at ibang backup mamaya, puwedeng pagsamahin ang dalawa sa isang file na naglalaman ng lahat mula sa dalawa, kaya hindi hadlang sa pagdaragdag mamaya ang pagsasauli ng mas luma ngayon."),
        ("Ano ang hindi na mababawi",
         "Kung walang backup sa anumang anyo, hindi na mababawi ang datos ng personal na pag-aaral. Nasa pribadong imbakan lang ito ng app sa device, at hindi maaasahang iniingatan ito ng JW Library ni ng backup sa cloud sa antas ng telepono. Sulit itong sabihin nang tuwiran, dahil ito mismo ang dahilan kung bakit umiiral ang gawaing nasa sityong ito."),
        ("Suriin bago burahin ang device mula sa malayo",
         "Kung nawala lang at hindi nasira ang telepono, at iniisip mong burahin ito mula sa malayo, maghanap muna ng umiiral na backup: hindi na mababawi ang pagbura at inaalis nito ang huling pagkakataong may makagawa ng isa. Kung naiwala lang ito at naaabot pa, hindi puwedeng gumawa ng backup mula sa malayo, pero buo pa rin ang datos hangga't hindi ito binubura o nire-reset."),
        ("Para hindi na maulit",
         "Ang dahilan kung bakit nagkakahalaga ng taon-taong pag-aaral ang nawalang telepono ay dahil nasa telepono lang ang tanging kopya. Kapag nakapagsauli ka na sa kapalit na device, maglagay ng backup sa labas ng device sa mismong araw ding iyon, at ulitin sa ritmong talagang matutupad mo. Sapat na maliliit ang mga file para itago lahat nang walang katapusan nang walang gastos."),
        ("Kung talagang walang backup",
         "Kung gayon, ang tapat na sagot ay hindi na mababawi ang mga nota, at mas mabuting marinig iyon kaysa magpatuloy sa paghahanap. Ang magagawa mo ay gawin itong huling pagkawala: i-install ang JW Library sa kapalit, at bago ka pa nakapagtipon ng anumang ikalulungkot mong mawala, gumawa ng backup at ilagay sa labas ng device. Mula roon, wala kang mawawala sa parehong pangyayari."),
    ],
    "faq": [
        ("Kaya bang bawiin ng JW Sync ang mga nota mula sa cellphone na wala na sa akin?",
         "Walang tool na kayang gawin iyon — nakasalalay ang pagbawi sa pagkakaroon ng backup "
         "na file kahit saan. Ang gawain ng JW Sync ay basahin, ayusin at pagsamahin ang mga "
         "backup na mayroon ka."),
        ("Luma na ang backup ko — sulit pa rin bang isauli?",
         "Talagang sulit. Mas mabuti ang lumang backup na may halos lahat ng nota mo kaysa "
         "magsimula sa wala, at puwede mo itong pagsamahin sa mas bago kung may makita ka "
         "pang iba."),
        ("May kopya ba ang JW Library ng mga nota ko sa cloud?",
         "Wala. Nananatili sa device ang datos ng personal na pag-aaral maliban kung ikaw mismo ang gagawa ng file ng backup."),
        ("Nababawi ba ang mga nota sa teleponong basag ang screen?",
         "Kung minsan — kung bumubukas pa ang telepono at makokontrol, o kung kayang paandarin ng repair shop ang display, makakagawa pa rin ng backup ang JW Library. Buo ang datos hangga't buo ang imbakan."),
        ("Naisasauli pa ba ang lumang backup sa kasalukuyang app?",
         "Oo. Nababasa ng JW Library ang mas lumang anyo ng backup. I-update muna ang app at magsauli sa kasalukuyang bersiyon."),
        ("Nakakita ako ng dalawang lumang backup — alin ang gagamitin ko?",
         "Wala sa kanilang mag-isa: pagsamahin sila. Naglalaman ang bunga ng lahat mula sa dalawa, pati ng nasa mas luma na nabura na noong panahon ng mas bago."),
        ("Puwede ko bang makita ang laman ng backup bago isauli?",
         "Oo. Buksan ang file sa iyong browser at tingnan muna ang mga nota, highlight at bookmark nito, para alam mo ang isasauli mo."),
    ],
}

GUIDES_TL["handle-merge-conflicts"] = {
    "title": "Iisang nota, na-edit sa dalawang device? Pag-aayos ng conflict sa pagsasama",
    "h1": "Pag-aayos ng conflict sa pagsasama: iisang nota na na-edit sa dalawang device",
    "description": "Kapag magkaiba ang naging pag-edit mo sa iisang nota sa dalawang device, "
                   "kailangang pumili ng mananaig sa pagsasama. Ipinapakita ng Conflict "
                   "Reviewer ang dalawang bersiyon nang magkatabi para ikaw ang magpasiya — "
                   "walang nawawala.",
    "intro": [
        "Halos walang kahirap-hirap ang karamihan sa pagsasama — basta nagsasama ang mga notang "
        "nasa isang device lang. Ang tanging kaso na nangangailangan ng pasiya ay ang tunay na "
        "conflict: iisang nota, magkaiba ang pag-edit sa dalawang device, kaya hindi "
        "magkasundo ang dalawang backup kung ano dapat ang laman nito. Hindi tahimik na "
        "nanghuhula ang JW Sync; sa iyo ibinibigay ang pagpili.",
    ],
    "steps": [
        ("I-load ang dalawang backup",
         "Sa jwsync.org, i-load ang mga .jwlibrary na file mula sa dalawang device. "
         "Pinaghahambing ang mga ito ng JW Sync habang nagsasama."),
        ("Buksan ang Conflict Reviewer",
         "Kung may mga notang nagkakasalungatan, ililista ang mga ito ng reviewer. Nakasama na "
         "ang lahat ng walang salungatan — para lang sa tunay na banggaan ang hakbang na ito."),
        ("Ihambing nang magkatabi",
         "Bawat conflict ay nagpapakita ng dalawang bersiyon na may pagkakaiba salita-por-"
         "salita. Kayang piliin ng “Imungkahi ang pinakamainam” ang mas kumpletong bersiyon "
         "para sa iyo, o ikaw ang pumili — kada nota."),
        ("Tapusin at isauli",
         "Kapag naayos na ang lahat ng conflict, i-download ang pinagsamang file at isauli. "
         "Magkasundo na ang dalawang device, na may piniling bersiyon mo sa bawat nota."),
    ],
    "sections": [
        ("Bakit mas mainam ito kaysa panatilihin na lang ang pinakabago",
         "Tahimik na binubura ng “ang pinakabago ang panalo” ang mga pag-edit na baka gusto mo "
         "pang itago. Baka may talataan sa lumang bersiyon na aksidenteng inalis mo sa kabilang "
         "device. Kapag nakikita mo ang dalawa, salita-por-salita, hindi ka nawawalan ng "
         "teksto nang hindi mo alam — at iyon mismo ang buong punto ng pagsasama sa halip na "
         "pag-overwrite."),
        ("Saan ba nagmumula ang mga conflict",
         "Kadalasan sa pag-edit nang offline sa dalawang device sa pagitan ng mga pagsasama, o "
         "sa pagsasauli ng lumang backup at pagdaragdag doon. Ang regular na pagsasama ang "
         "nagpapanatiling kaunti ang conflict at sariwa pa sa alaala ang pagkakaiba."),
    ],
    "faq": [
        ("Kailangan ko bang suriin ang daan-daang conflict?",
         "Bihira. Nagkakasalungatan lang ang mga notang magkaiba ang pag-edit sa magkabilang "
         "panig; kusang nagsasama ang mga bagong nota at ang mga binago sa isang device lang. "
         "Sa karamihan ng pagsasama, ilan lang o wala man lang ang conflict."),
        ("Puwede ba akong magbago ng isip pagkatapos pumili?",
         "Oo — walang naisusulat sa device hangga't hindi mo isinasauli ang pinagsamang file, "
         "at hindi kailanman binabago ang orihinal mong mga backup, kaya puwede mong ulitin "
         "ang pagsasama."),
    ],
}

GUIDES_TL["export-jw-library-notes"] = {
    "title": "Paano i-export ang mga nota sa JW Library sa teksto o Markdown",
    "h1": "Pag-export ng mga nota mo sa JW Library sa teksto, Markdown o bagong backup",
    "description": "Ilabas ang mga nota mo sa JW Library mula sa app: kopyahin o i-export ang "
                   "mga ito bilang Markdown o payak na teksto para magamit kahit saan, o kumuha "
                   "ng piling bahagi tungo sa bagong .jwlibrary na backup. Lahat sa browser mo.",
    "intro": [
        "Ang mga notang isinulat sa JW Library ay madaling basahin sa loob ng app at mahirap gamitin saanman pa — sa isang dokumento, sa balangkas ng pahayag, sa papel, o sa kamay ng taong hindi gumagamit ng app. Nilulutas ito ng pag-export, at ang pangunahing pasiya ay hindi kung paano mag-export kundi kung gaano karami: halos palaging mas kapaki-pakinabang ang sinalang pag-export kaysa sa lahat nang sabay-sabay.",
        "Hindi dapat nakakulong sa isang app ang mga nota mo sa pag-aaral. Minsan gusto mo "
        "silang payak na teksto — para idikit sa balangkas ng pahayag, sa isang dokumento, o "
        "sa sarili mong notes app — at minsan naman ay malinis na backup na may bahagi lang "
        "ang gusto mo. Kaya ng Study Explorer ang dalawa, at binabasa nito ang backup mo nang "
        "buong-buo sa browser.",
    ],
    "steps": [
        ("I-load ang backup mo",
         "Gumawa ng backup sa JW Library (Personal na Pag-aaral → Backup at Pagsasauli → "
         "Gumawa ng backup), tapos buksan ang jwsync.org at i-load ito sa Study Explorer."),
        ("Hanapin ang mga notang gusto mo",
         "Gamitin ang paghahanap kasama ang pang-salang kulay, tag at publikasyon para makarating "
         "sa eksaktong mga notang hinahanap mo — isang publikasyon, isang tag, isang paksa."),
        ("Kopyahin o i-export bilang Markdown o teksto",
         "Ilabas ang mga nota bilang Markdown o payak na teksto para maidikit kahit saan. "
         "Nananatili ang pormat (bold, italic, listahan) kaya nananatiling maayos ang "
         "istruktura ng mga notang may istruktura."),
        ("O kumuha tungo sa bagong backup",
         "Mas gusto mo ang file? I-export ang piniling bahagi o saklaw ng petsa tungo sa "
         "bagong .jwlibrary na backup — kapaki-pakinabang sa pag-iimbak ng isang proyekto o "
         "sa pagbibigay ng tiyak na set ng nota sa ibang device."),
    ],
    "sections": [
        ("Bakit mag-export",
         "Mas kapaki-pakinabang ang mga nota kapag nakakagalaw sila: patungo sa dokumento para "
         "sa atas sa pulong, sa personal na wiki, sa nakalimbag na kopya para sa hindi "
         "gumagamit ng app. Iniingatan ng Markdown ang istruktura habang nananatiling "
         "nababasa bilang payak na teksto kahit saan."),
        ("Pagpili ng anyo",
         "Ang payak na teksto ang pinakamadaling dalhin at malinis na naididikit sa anumang dokumento o email. Iniingatan ng may-format na labas ang balangkas ng mahahabang nota at bagay sa pag-print o pagbabahagi. Kung gusto mong maibalik ang mga nota sa loob ng JW Library mamaya — sa ibang device, o sa aklatan ng iba — itago ang mismong .jwlibrary na file sa halip na pag-export ng teksto, dahil iyon lang ang nag-iingat sa ugnayan ng mga nota, highlight, tag at ng eksaktong lugar sa publikasyon kung saan sila nakaangkla."),
        ("Pag-export ng bahagi lang ng aklatan",
         "Bihirang ang buong pag-export ng taon-taong pag-aaral ang gusto mo. Ang paunang pagsala — sa isang tag, publikasyon, kulay ng highlight, o saklaw ng petsa — ay gumagawa ng isang bagay na talagang magagamit mo, gaya ng lahat ng notang may tag para sa isang pahayag, o lahat ng isinulat sa isang kombensiyon. Ang mga salaan ding nagpapaliit sa tanawin ay nagpapaliit sa pag-export, kaya ang nakikita mo ang siyang makukuha mo."),
        ("Ano ang kasamang naglalakbay ng teksto, at ano ang hindi",
         "Dala ng pag-export ang mga salita mo. Hindi nito dala ang mga angklang nag-uugnay sa nota sa isang tiyak na talata ng isang tiyak na publikasyon, dahil may kahulugan lang ang mga reperensiyang iyon sa loob ng JW Library. Ito ang praktikal na dahilan para mag-ingat din ng mga backup: ang pag-export ay para sa pagbasa, pag-print at pagbabahagi sa labas ng app, samantalang ang .jwlibrary na file ang naglalagay muli ng mga nota sa aklatan nang buo ang konteksto."),
        ("Pagtitipon ng lahat para sa isang pahayag o atas",
         "Ito ang pinakakaraniwang dahilan ng pag-export. Salain ayon sa tag, publikasyon o saklaw ng petsa kung saan nakalagay ang materyal, suriin ang bunga, at i-export lang iyon. Ang makukuha mo ay iisang dokumentong naglalaman ng mga kaugnay na nota at ng mga bahaging na-highlight mo, sa pagkakasunod-sunod ng paglitaw ng mga ito, sa halip na hindi mapangasiwaang buhos ng buong aklatan."),
        ("Pagbabahagi ng mga nota sa iba",
         "May dalawang magkaibang bagay na tinutukoy ng pagbabahagi. Kung gustong basahin ng ibang tao ang mga nota mo, tama ang pag-export ng teksto — bumubukas ito saanman at walang kailangang natatanging programa. Kung gusto niyang nasa loob ng sarili niyang JW Library ang mga nota, nakaangkla sa parehong talata at may dala niyang tag at kulay, ang kailangan mo ay .jwlibrary na file, dahil walang maibabalik sa app ang pag-export ng teksto."),
        ("Pag-iingat ng talaang mababasa mo pa makalipas ang matagal",
         "Sulit din ang mga pag-export sa ganang sarili. Bubukas pa rin makalipas ang tatlumpung taon ang kopyang payak na teksto ng mga nota mo sa pag-aaral, sa mga programang wala pang sumusulat ngayon, at hindi iyan maipapangako ng anumang anyong pag-aari ng isang app. Ang pag-iingat sa dalawa — ang .jwlibrary para sa pagsasauli at ang pag-export ng teksto para sa pagbasa — ay halos walang gastos at sumasaklaw sa dalawang kinabukasan."),
        ("Pag-export o backup — alin ang kailangan mo",
         "Magkaiba ang sinasagot nilang tanong. Ang pag-export ay para gamitin ang mga nota mo sa labas ng JW Library: pagbasa, pag-print, pagsipi, pagpapadala sa iba. Ang .jwlibrary na backup ay para maibalik ang mga ito sa JW Library, sa device na ito o sa iba, nang buo ang bawat angkla, tag at kulay. Walang kapalit ang isa sa isa, at walang dahilan para hindi mo taglayin pareho."),
    ],
    "faq": [
        ("Nagbabago ba ang mga nota ko sa JW Library kapag nag-export?",
         "Hindi. Isang kopya ng backup mo ang binabasa ng pag-export sa browser; hindi "
         "nagagalaw ang orihinal mong file at ang app."),
        ("Puwede bang i-export lahat nang sabay?",
         "Oo — burahin ang mga salang para piliin ang buong library, o mag-salang muna para "
         "i-export ang bahagi lang."),
        ("Puwede ko bang dalhin ang mga nota ko sa Word o Google Docs?",
         "Oo — mag-export bilang teksto at idikit. Dumarating ang teksto nang buo ang balangkas at mabibigyan ng estilo mula roon."),
        ("Nae-export din ba ang mga highlight kasama ng mga nota?",
         "Oo, pati ang bahaging na-highlight at ang kulay nito, kaya ipinapakita ng nakalimbag na kopya kung ano ang minarkahan mo at kung ano ang isinulat mo."),
        ("Puwede bang i-export ang lahat nang sabay?",
         "Oo, bagaman kadalasang mas kapaki-pakinabang ang sinalang pag-export. Puwedeng i-export ang lahat sa isang hakbang kapag gusto mo ng buong kopya."),
        ("Puwede ko bang i-export ang mga sagot na tinipa ko sa mga tanong sa pag-aaral?",
         "Oo. Bahagi ng datos ng personal mong pag-aaral ang mga tinipang sagot at nae-export ito kasama ng mga nota at highlight."),
        ("Kasama ba sa pag-export kung aling publikasyon ang pinagmulan ng bawat nota?",
         "Oo, ipinapakita ng pag-export kung saan nanggaling ang bawat nota, kahit ang mismong angkla ay gumagana lang sa loob ng JW Library."),
        ("May nababago ba sa aklatan ko ang pag-export?",
         "Wala. Binabasa ng pag-export ang datos mo at sumusulat ng hiwalay na file; walang nababago, nailILipat o naaalis sa loob ng JW Library."),
        ("Puwede bang mag-export mula sa backup sa halip na sa app?",
         "Oo. Puwedeng tuwirang buksan ang .jwlibrary na file at i-export ang mga nota nito, na kapaki-pakinabang kapag nasa lumang backup at hindi sa kasalukuyan mong device ang mga notang gusto mo."),
    ],
}

GUIDES_TL["organize-jw-library-tags"] = {
    "title": "Paano ayusin at linisin ang mga tag sa JW Library",
    "h1": "Pag-aayos ng mga tag sa JW Library: palitan ng pangalan, pagsamahin at linisin nang maramihan",
    "description": "Dumadami ang mga tag sa paglipas ng taon ng pag-aaral. Palitan ang "
                   "pangalan ng isang tag sa lahat ng nota, pagsamahin ang mga duplicate, at "
                   "alisin ang hindi mo na ginagamit — nang maramihan, sa browser, at may "
                   "buong undo.",
    "intro": [
        "Ang mga tag ang paraan mo para mahanap ang mga nota sa bandang huli — pero pagkalipas "
        "ng ilang taon ay nagkakalat na sila. Napupunta ka sa “Ministeryo”, “ministeryo” at "
        "“Paglilingkod sa larangan” na iisa lang ang ibig sabihin, sa mga tag na minsan mo "
        "lang ginawa at hindi na muling ginamit, at sa magkakaibang pangalan na nagpapahina sa "
        "pagtitiwala sa pag-salang. Walang paraan sa JW Library para ayusin ito nang malawakan. "
        "Sa Study Explorer, mayroon.",
    ],
    "steps": [
        ("I-load ang backup mo sa Study Explorer",
         "Sa jwsync.org, i-load ang .jwlibrary na file mo. Mag-salang ayon sa tag para "
         "makita ang bawat tag at kung ilang nota ang may taglay nito."),
        ("Palitan ang pangalan ng tag sa lahat ng notang gumagamit nito",
         "Magpalit ng tag nang maramihan: palitan ang pangalan minsan lang at mag-a-update ang "
         "bawat notang gumagamit nito — wala nang pag-edit isa-isa para lang itama ang baybay."),
        ("Pagsamahin ang mga duplicate",
         "Ilipat ang tag ng mga notang may duplicate tungo sa opisyal na tag, tapos alisin ang "
         "walang lamang duplicate. Magiging isang malinis na tag ang “Ministeryo” at "
         "“ministeryo”."),
        ("Alisin ang mga tag na hindi mo na ginagamit",
         "Piliin at burahin nang maramihan ang mga lumang tag. Nababawi ang lahat, kaya "
         "hindi kailanman panghabambuhay ang sobrang sigasig sa paglilinis."),
        ("I-export ang naayos na library",
         "I-download ang na-edit na .jwlibrary at isauli ito sa JW Library. Pare-pareho na ang "
         "mga tag mo kahit saan."),
    ],
    "sections": [
        ("Sistema ng tag na talagang nakakatulong",
         "Kapag pare-pareho na ang mga tag, mapagkakatiwalaan na ang pag-salang — isang tap at "
         "makikita ang bawat nota tungkol sa isang tema, sa lahat ng publikasyon. Iyan ang "
         "pagkakaiba ng mga tag bilang kalat at mga tag bilang tunay na indise ng pag-aaral "
         "mo."),
        ("Ang pare-parehong tag ay ginagawang dalawang klik lang ang pagbabahagi",
         "May sariling pang-salang tag ang pumipili ng nota sa pahina ng pagbabahagi, kaya ang "
         "malinis na tag ang pinakamabilis ding paraan para magpadala sa iba ng set ng nota: "
         "piliin ang tag, pindutin ang Piliin lahat, gumawa ng file. Doble ang halaga ng "
         "magulong tag — kapag naghahanap ka ng nota, at kapag sinusubukan mo silang "
         "ibahagi."),
    ],
    "faq": [
        ("Nagagalaw ba ng maramihang pagpapalit ng tag ang teksto ng nota?",
         "Hindi — kung aling tag lang ang nakakabit ang nababago. Nananatiling gaya ng "
         "pagkakasulat mo ang mga pamagat at nilalaman ng nota."),
        ("May pag-undo ba kung magkamali ako?",
         "Mayroon. May buong undo at redo ang Study Explorer, at hindi kailanman binabago ang "
         "orihinal mong backup — napupunta sa na-export na kopya ang mga pagbabago."),
    ],
}

GUIDES_TL["manage-jw-library-highlights"] = {
    "title": "Paano pamahalaan at palitan ng kulay ang mga highlight sa JW Library",
    "h1": "Pamamahala sa mga highlight sa JW Library: maramihang pagpapalit ng kulay at pag-aayos",
    "description": "Ayusin ang taon-taong highlight sa JW Library: palitan ang mga kulay nang "
                   "maramihan, bigyan ng pare-parehong kahulugan ang color code mo, at tingnan "
                   "ang bawat highlight sa iisang lugar. Sa browser mo.",
    "intro": [
        "Nakakatulong lang ang kulay ng highlight kung may pare-parehong kahulugan ito. Sa "
        "paglipas ng panahon, naliligaw ang mga highlight ng karamihan — ibang ibig sabihin ng "
        "dilaw noong 2019 at iba na ngayon, at walang paraan sa JW Library para makita silang "
        "lahat nang sabay o ayusin nang malawakan. Tinitipon ng Study Explorer ang bawat "
        "highlight sa iisang tanawin at pinapayagan kang magpalit ng kulay nang maramihan.",
    ],
    "steps": [
        ("I-load ang backup mo",
         "Sa jwsync.org, buksan ang .jwlibrary na file mo sa Study Explorer at lumipat sa tab "
         "na Mga Highlight."),
        ("Tingnan at salain ang mga highlight mo",
         "Makikita ang bawat highlight sa iisang listahan, masasala ayon sa kulay o "
         "publikasyon, at mahahanap ang naka-highlight na teksto at anumang nakakabit na "
         "nota."),
        ("Magpalit ng kulay nang maramihan",
         "Pumili ng maraming highlight at palitan ang kulay nila nang sabay — halimbawa, "
         "pag-isahin sa iisang kulay ang lahat ng itinuring mong “mahalagang teksto” sa buong "
         "library mo."),
        ("I-edit din ang mga nakakabit na nota",
         "Kung may notang nakakabit sa isang highlight, dito mo na rin puwedeng i-edit ang "
         "pamagat at nilalaman ng notang iyon."),
        ("I-export at isauli",
         "I-download ang na-edit na .jwlibrary at isauli ito sa JW Library para nasa bawat "
         "device na ang pare-pareho mong color code."),
    ],
    "sections": [
        ("Magpasiya kung ano ang ibig sabihin ng mga kulay mo",
         "Isang simpleng balangkas — isang kulay para sa pangunahing punto, isa para sa mga "
         "tekstong sasaulohin, isa para sa mga tanong na sasaliksikin — ang nagpapabago sa mga "
         "highlight mula palamuti tungo sa kagamitan sa pag-aaral. Sa maramihang pagpapalit ng "
         "kulay, maisasagawa mo ang balangkas na iyon nang paurong sa taon-taong pagbabasa."),
    ],
    "faq": [
        ("Makikita ko ba ang mga highlight na walang nakakabit na nota?",
         "Oo — ipinapakita silang lahat ng tab na Mga Highlight, may nakakabit man o wala."),
        ("Naaapektuhan ba ng pagpapalit ng kulay ang teksto sa ilalim?",
         "Hindi, ang kulay lang ng highlight ang nagbabago; hindi nagagalaw ang teksto ng "
         "publikasyon at ang mga nota mo."),
    ],
}

GUIDES_TL["jw-library-study-answers"] = {
    "title": "Tingnan at i-edit ang mga sagot mo sa pag-aaral sa JW Library",
    "h1": "Paghahanap sa lahat ng sagot mo sa pag-aaral sa JW Library sa iisang lugar",
    "description": "Nakatago sa backup mo ang mga sagot na tinipa mo sa mga tanong ng artikulo "
                   "sa pag-aaral at workbook. Sa tab na Mga Sagot sa Pag-aaral ng Study "
                   "Explorer, mababasa, mahahanap at mae-edit mo silang lahat nang sabay.",
    "intro": [
        "Habang nag-aaral ka, tinitipa mo ang mga sagot sa mga kahon ng artikulo sa pag-aaral, "
        "ng Bantayan, at ng workbook sa pulong. Nase-save sila sa backup mo — pero isa-isa "
        "lang silang ipinapakita ng JW Library, nakabaon sa kani-kaniyang publikasyon. Walang "
        "iisang lugar kung saan masusuri ang lahat ng naisulat mo. Ang tab na Mga Sagot sa "
        "Pag-aaral ng Study Explorer ang lugar na iyon.",
    ],
    "steps": [
        ("I-load ang backup mo sa Study Explorer",
         "Sa jwsync.org, i-load ang .jwlibrary na file mo at buksan ang tab na Mga Sagot sa "
         "Pag-aaral."),
        ("Basahin nang sabay ang lahat ng sagot mo",
         "Lumalabas sa isang mahahanap na listahan ang bawat sagot na tinipa mo, kaya "
         "masusuri mo sa isang tingin ang buong kaisipan mo sa isang artikulo sa pag-aaral."),
        ("Maghanap at mag-edit",
         "Hanapin ang isang sagot ayon sa teksto nito, tapos i-edit at pagandahin ito diretso "
         "— nakakatulong kapag naghahanda bago ang pulong o nililinis ang mabilisang "
         "pagkakasulat."),
        ("Mag-export o magsauli",
         "Isauli ang na-edit na file para maibalik ang mga pagbabago sa JW Library, o kopyahin "
         "ang mga sagot bilang teksto para sa pahayag o personal na tala."),
    ],
    "sections": [
        ("Bakit kapaki-pakinabang ito bago ang pulong",
         "Ang pagsusuri sa inihanda mong mga sagot sa isang tuloy-tuloy na listahan — sa halip "
         "na mag-scroll sa bawat talataan sa app — ay mas mabilis na paraan para maalala kung "
         "ano ang balak mong sabihin, at para mapansin ang mga sagot na naiwang blangko."),
    ],
    "faq": [
        ("Pareho ba ito sa personal kong mga nota?",
         "Hindi — ang mga sagot sa pag-aaral ay ang tinipa mo sa mga kahon ng sagot ng isang "
         "publikasyon. Ipinapakita sila ng Study Explorer sa sarili nilang tab, hiwalay sa "
         "malayang mga nota."),
        ("May ina-upload ba para mabasa ang mga sagot ko?",
         "Wala. Gaya ng lahat sa JW Sync, binabasa ang backup mo sa loob ng browser at hindi "
         "kailanman ipinapadala kahit saan."),
    ],
}

GUIDES_TL["extract-jw-library-notes-by-date"] = {
    "title": "Kumuha ng mga nota sa JW Library mula sa isang panahon tungo sa bagong backup",
    "h1": "Pagkuha ng mga notang nasa isang saklaw ng petsa tungo sa bagong backup",
    "description": "Ibukod ang mga nota lang mula sa isang tiyak na panahon — isang taon ng "
                   "paglilingkod, isang kombensiyon, isang proyekto sa pag-aaral — tungo sa "
                   "sarili nilang malinis na .jwlibrary na backup. Buong-buo sa browser mo.",
    "intro": [
        "Minsan bahagi lang ng library mo ang gusto mo, hindi lahat: mga nota ngayong taon "
        "para sa balik-aral, lahat ng mula sa isang kombensiyon, o ang pananaliksik ng isang "
        "proyekto para ipasa sa iba. Kayang kunin ng Study Explorer ang mga notang nasa isang "
        "saklaw ng petsa tungo sa bagong-bagong .jwlibrary na backup, at hindi nagagalaw ang "
        "pangunahing library mo.",
    ],
    "steps": [
        ("I-load ang backup mo",
         "Sa jwsync.org, buksan ang .jwlibrary na file mo sa Study Explorer."),
        ("Itakda ang saklaw ng petsa",
         "Piliin ang simula at katapusang petsa ng mga notang gusto mo — isang taon ng "
         "paglilingkod, isang buwan, ang mga petsa ng isang tiyak na kaganapan."),
        ("Kumuha tungo sa bagong backup",
         "I-export ang mga tugmang nota tungo sa bagong .jwlibrary na file. Nasa loob lang "
         "nito ang mga nota at highlight ng panahong iyon, kasama ang mga tag nila."),
        ("Gamitin ang nakuhang file",
         "Isauli ito sa JW Library para sa nakapokus na balik-aral, itago ito, o ibahagi sa "
         "taong iyon lang ang kailangan."),
    ],
    "sections": [
        ("Magagandang dahilan para kumuha ayon sa petsa",
         "Isang taunang imbakan ng pag-aaral mo; isang malinis na file ng mga nota sa "
         "kombensiyon na hiwalay na itinatago; pagbibigay sa katuwang sa pag-aaral ng mga nota "
         "lang mula sa proyektong pinagtulungan ninyo; o paghahati ng napakalaking library sa "
         "mapapamahalaang bahagi ayon sa petsa — lahat nang hindi ginagalaw ang pangunahing "
         "backup mo."),
    ],
    "faq": [
        ("Naaalis ba sa library ko ang mga notang kinuha?",
         "Hindi. Kinokopya lang nito ang mga tugmang nota tungo sa bagong file; nananatiling "
         "buo ang orihinal mong backup."),
        ("Anong petsa ang ginagamit — kung kailan ko sinulat o kung kailan ko huling na-edit?",
         "Ang mga oras na nakatala sa mismong nota sa loob ng backup ang ginagamit, kaya "
         "sinasalamin ng saklaw kung kailan ginawa o binago ang mga nota."),
    ],
}

GUIDES_TL["connect-jw-library-notes-study-map"] = {
    "title": "Tingnan kung paano nag-uugnay ang mga nota mo sa JW Library — Study Map",
    "h1": "Study Map: pribadong mapa ng kaalaman mula sa mga nota mo sa JW Library",
    "description": "Ginagawa ng Study Map na isang interaktibong sapot ang mga nota mo sa JW "
                   "Library, na iniuugnay sila sa pamamagitan ng magkakatulad na teksto, tag "
                   "at pananalita — para makita mo ang mga temang tumatagos sa pag-aaral mo.",
    "intro": [
        "May mga ugnayan sa taon-taong nota na hindi mo pa nakikita: ang iisang tekstong "
        "sinipi sa dose-dosenang tala, isang temang laging binabalikan mo, mga kaisipang "
        "nagkakatugma sa magkakaibang publikasyon. Iginuguhit ng Study Map ang mga ugnayang "
        "iyon bilang interaktibong graph, kaya nagiging nakikita ang hugis ng sarili mong "
        "pag-aaral.",
    ],
    "steps": [
        ("Buksan ang pahinang Study Stats at mag-load ng backup",
         "Pumunta sa jwsync.org/highlights.html at i-load ang .jwlibrary na file mo. Binabasa "
         "ito ng Study Map sa browser mo."),
        ("Buksan ang Study Map",
         "Simulan ang mapa para makita ang mga nota mo bilang magkakaugnay na tuldok, na "
         "pinag-uugnay ng magkakatulad na teksto, tag at pananalita."),
        ("Galugarin ang mga ugnayan",
         "Maglipat-lipat sa tanawing Mga Tema at Mga Nota, ipatong ang cursor para tanglawan "
         "ang ugnayan ng isang nota, hilahin ang mga bagay, at gamitin ang slider ng lakas "
         "para ipakita lang ang pinakamalapit na ugnayan. Bumubuka ang espasyo sa full-screen "
         "mode."),
        ("Gumawa at mag-save ng mga study chain",
         "Iguhit ang sarili mong mga “study chain” sa pagitan ng magkakaugnay na nota para "
         "maitala ang daloy ng pangangatuwiran, at i-export ang mapa bilang larawang PNG para "
         "itago o ibahagi."),
    ],
    "sections": [
        ("Ano ang isinisiwalat ng mapa",
         "Ipinapakita ng mga kumpol ang mga temang pinakamadalas mong pag-aralan; ang tekstong "
         "nakaugnay sa maraming nota ay talatang laging binabalikan mo; ang notang nakabukod "
         "ay maaaring sinulid na sulit palawakin. Isa itong paraan para pag-aralan ang "
         "pag-aaral mo — at para maghanda ng pahayag sa pamamagitan ng pagsunod sa mga "
         "ugnayang nagawa mo na."),
    ],
    "faq": [
        ("Kailangan ba ng maraming nota para maging kapaki-pakinabang ang mapa?",
         "May naipapakitang ugnayan kahit ang katamtamang library; kapag mas mayaman ang mga "
         "nota mo, mas marami ang isinisiwalat ng mapa. Sa napakaliliit na library, may "
         "paalalang magdagdag muna ng nota."),
        ("Pribado ba ang mapa?",
         "Buong-buo. Binubuo ito sa browser mo mula sa backup mo at hindi kailanman "
         "ina-upload; kahit ang PNG na export ay ginagawa sa device mo."),
    ],
}

GUIDES_TL["review-old-jw-library-notes"] = {
    "title": "Paano suriin ang mga lumang nota mo sa JW Library (para manatili sa isip)",
    "h1": "Pagsusuri sa mga lumang nota gamit ang Resurface — kaunti ngunit madalas",
    "description": "Ang mga notang hindi mo binabalikan ay mga notang nakakalimutan mo. "
                   "Ipinapakita ng Resurface ang isinulat mo sa araw ding ito noong mga "
                   "nakaraang taon at bumubuo ng banayad na pag-uulit, para patuloy na "
                   "makinabang ka sa nakaraang pag-aaral.",
    "intro": [
        "Karamihan sa mga nota sa pag-aaral ay minsan lang naisusulat at hindi na muling "
        "nakikita. Isa iyang tahimik na sayang — sulit itala ang kaisipan, pero lumubog ito sa "
        "ilalim ng library. Ibinabalik ng Resurface sa ibabaw ang sarili mong mga lumang nota, "
        "tig-iilan lang, kaya nagiging maliit na pang-araw-araw na ugali ang pagbabalik-tanaw "
        "sa halip na proyektong “balang-araw”.",
    ],
    "steps": [
        ("Buksan ang pahinang Study Stats at mag-load ng backup",
         "Pumunta sa jwsync.org/highlights.html at i-load ang .jwlibrary na file mo. Binabasa "
         "ng Resurface ang mga nota mo sa device mismo."),
        ("Tingnan ang “Sa araw na ito”",
         "Ibinabangon ng Resurface ang mga notang isinulat mo sa petsang ito noong nakaraang "
         "mga taon — “isinulat dalawang taon na ang nakalipas ngayong araw” — na muling "
         "nag-uugnay sa iyo sa nakaraang pag-aaral sa sandaling pinakamakahulugan."),
        ("Gumawa ng maikling pagsusuri araw-araw",
         "Naghahain ito ng ilang notang babalikan at tatatakan bilang nasuri na. Kaunti ngunit "
         "madalas — iyan ang nagpapanatili ng pag-aaral, at lumalago ang streak habang "
         "pinapanatili mo ang ugali."),
        ("Bumalik bukas",
         "Isinasaayos ng pag-uulit sa may agwat kung kailan muling lilitaw ang mga nota, kaya "
         "ang mga sulit tandaan ay patuloy na babalik hanggang sa maging tunay mong pag-aari."),
    ],
    "sections": [
        ("Bakit gumagana ang pag-uulit sa may agwat",
         "Higit na mabisa ang pagbabalik-aral sa bagay na muntik mo nang malimutan kaysa sa "
         "biglaang pagsasaulo. Sa paghahati ng ilang nota sa maraming araw, ginagawa ng "
         "Resurface na tuloy-tuloy at magaang balik-aral ang library na mayroon ka na, na "
         "unti-unting nagpapalalim sa napag-aralan mo."),
    ],
    "faq": [
        ("Saan nase-save ang pagsulong ko sa pagsusuri?",
         "Sa browser sa device mo — walang account at walang ina-upload. Sa iyo lang ang "
         "streak at ang iskedyul."),
        ("Kailangan ko ba ng bagong nota para dito?",
         "Hindi — gumagamit ang Resurface ng mga notang naisulat mo na. Habang tumatanda ang "
         "library mo, mas nakakatuwa ang mga sandaling “sa araw na ito”."),
    ],
}

GUIDES_TL["jw-library-achievements-streaks"] = {
    "title": "Mga streak, antas at tagumpay sa pag-aaral sa JW Library",
    "h1": "Gawing streak, antas at parangal ang pag-aaral mo sa JW Library",
    "description": "Tingnan ang mga streak mo sa pag-aaral, umakyat sa 60 antas sa 12 baitang "
                   "ng Study Journey mo, at buksan ang mga 200 tagumpay — lahat ay pribadong "
                   "binabasa mula sa sarili mong backup ng JW Library.",
    "intro": [
        "Ang pagiging palagian ang mahirap na bahagi ng personal na pag-aaral, at madaling "
        "mapabayaan ang pagsulong na hindi mo nakikita. Ginagawa ng pahinang Study Stats na "
        "isang bagay na makikita mong lumalago ang kasaysayang nasa backup mo: mga streak, "
        "antas at parangal na sumasalamin sa pag-aaral na tunay mong ginawa — walang "
        "ipinapataw na tunguhin, ang sarili mo lang na tala na ginawang nakikita.",
    ],
    "steps": [
        ("Buksan ang pahinang Study Stats",
         "Pumunta sa jwsync.org/highlights.html at i-load ang .jwlibrary na backup mo. Sa "
         "browser mo kinakalkula ang lahat."),
        ("Tingnan ang mga streak mo",
         "Makikita ang pinakamahaba at kasalukuyang streak sa pag-aaral, ang ritmo mo bawat "
         "linggo, at ang pinakaabalang oras at buwan — ang pulso ng ugali mo sa pag-aaral."),
        ("Umakyat sa Study Journey mo",
         "Sumulong sa 60 antas na hati sa 12 pinangalanang baitang (mula Buto hanggang "
         "Laging-Luntian), na may globong nagpapalit ng kulay at pagdiriwang sa bawat antas, "
         "batay sa kabuuang pag-aaral mo."),
        ("Mangolekta ng mga tagumpay",
         "Buksan ang mga 200 parangal mula Karaniwan hanggang Alamat, kasama ang mga "
         "medalyang may temang batay sa nilalaman; buksan ang alinmang medalya para makita "
         "ang pagsulong mo tungo sa susunod."),
    ],
    "sections": [
        ("Pampasigla nang walang presyon",
         "Hindi ito mga tunguhing itinakda ng iba — salamin ito ng nagawa mo na. Ang makakita "
         "ng streak na ayaw mong maputol, o ng antas na muntik mo nang maabot, ay banayad na "
         "tulak para ipagpatuloy ang mabuting ugali. At ang Shareable Card ay bumubuod sa taon "
         "mo nang walang inilalantad na kahit isang pribadong nota."),
    ],
    "faq": [
        ("Kusa bang nag-a-update ang mga streak at parangal?",
         "Sinasalamin nila ang backup na ini-load mo, kaya gumawa ng bagong backup para "
         "makita ang pinakabagong pagsulong. Walang tumatakbo sa background."),
        ("May ibinabahagi o ina-upload ba rito?",
         "Wala. Lahat ay kinakalkula sa device mula sa backup mo; ang buod na card lang ang "
         "puwede mong piliing ibahagi, at wala itong teksto ng kahit anong nota."),
    ],
}

GUIDES_TL["share-convention-assembly-notes"] = {
    "title": "Paano ibahagi ang mga nota sa kombensiyon at asamblea mula sa JW Library",
    "h1": "Pagbabahagi ng mga nota mo sa kombensiyon, asamblea at pulong",
    "description": "Ipasa ang mga nota mo sa kombensiyon, asamblea o pulong sa pamilya at "
                   "kaibigan sa maliit na file — nang hindi ibinibigay ang buong library mo at "
                   "hindi napapalitan ang sa kanila. Isang praktikal na gamit ng pagbabahagi "
                   "ng nota.",
    "intro": [
        "Maingat kang sumulat ng nota sa buong kombensiyon; matutuwa ang kaibigang nakalampas "
        "sa isang sesyon; gusto ng mga kapamilya ang mga punto para sa sarili nilang "
        "balik-aral. Sobra-sobra ang pagpapadala ng buong backup at buburahin nito ang mga "
        "nota ng tatanggap kapag isinauli. Sa pagbabahagi ng nota, maipapasa mo mismo ang "
        "mga notang gusto mo — at mapapanatili ng tatanggap ang lahat ng mayroon na siya.",
    ],
    "steps": [
        ("I-load ang backup mo sa pahina ng pagbabahagi",
         "Pumunta sa jwsync.org/share.html at i-load ang .jwlibrary na file mo."),
        ("Piliin lang ang mga nota sa kombensiyon",
         "Piliin ang tag ng kaganapan mula sa pang-salang tag sa pumipili ng nota at pindutin "
         "ang Piliin lahat — ang listahan ay eksaktong mga notang tinagan mo na. Kasamang "
         "darating ang mga highlight na nakakabit sa mga notang iyon."),
        ("Ipadala ang maliit na share file",
         "Gumagawa ang JW Sync ng maliit na file na naglalaman lamang ng mga notang iyon. "
         "Ipadala ito kung paano mo gusto — messaging app, email, AirDrop. Walang server, "
         "walang account."),
        ("Idaragdag ito ng pamilya at mga kaibigan",
         "Bubuksan ng bawat isa ang parehong pahina, ilo-load ang file mo kasama ang sarili "
         "niyang backup, at makakakuha ng bagong backup na may dagdag na mga nota mo. Hindi "
         "kailanman napapalitan ang sarili nilang mga nota, at may tag ang mga na-import "
         "mong nota kaya madali silang mahanap."),
    ],
    "sections": [
        ("Isang tag lang, madali na ang lahat",
         "Kung tinatagan mo ang mga nota mo habang nagaganap ang kaganapan (halimbawa, "
         "“Kombensiyon 2026”), ang pagpili sa kanila pagkatapos ay isang klik lang sa salang "
         "at isang Piliin lahat. Sulit magsimula ng bagong tag sa umpisa ng anumang "
         "kombensiyon, asamblea o natatanging pulong para dito mismo."),
    ],
    "faq": [
        ("Puwede ba akong magbahagi sa maraming tao nang sabay?",
         "Oo — file lang ang share file. Ipadala ito sa kasindaming taong gusto mo; "
         "idaragdag ito ng bawat isa sa sariling library niya nang hiwalay."),
        ("Malalantad ba ang buong library ko?",
         "Hindi. Ang mga notang pinili mo lang ang nasa file; nananatiling pribado ang "
         "natitira sa library mo."),
    ],
}

GUIDES_TL["share-jw-library-notes-by-tag"] = {
    "title": "Ibahagi lang ang mga nota sa JW Library na nasa ilalim ng isang tag",
    "h1": "Pagbabahagi lang ng mga notang may isang tiyak na tag",
    "description": "Magpadala ng isang paksa, isang proyekto o ng para sa isang estudyante sa "
                   "halip na ang buong library mo — at kasamang dumadala ang mga tag mo, kaya "
                   "maayos na silang dumarating sa kabilang panig.",
    "intro": [
        "Karaniwang ang tag ang likas na yunit ng pagbabahagi. Tinagan mo ang lahat ng "
        "naipon mo tungkol sa isang paksa, lahat ng mula sa isang kaganapan, o lahat ng "
        "dinadaanan mo kasama ang isang tao — at iyon mismong set, hindi ang buong library mo, "
        "ang talagang gusto ng kabila.",
        "Nota-por-nota gumagana ang pagbabahagi ng nota sa JW Sync, kaya ang tag ay ang "
        "listahang tsinetsekan mo lang. Dala pa rin ng mga nota ang tag nila paglabas, ibig "
        "sabihin ay masasala ng tatanggap ang eksaktong parehong set sa loob ng sariling "
        "library niya pagkatapos.",
    ],
    "steps": [
        ("Tiyaking may tag ang mga nota",
         "Tagan sila sa JW Library habang isinusulat, o buksan ang backup mo sa Study Explorer "
         "sa jwsync.org at gamitin ang tag editor para magdagdag ng tag sa maraming nota nang "
         "sabay. Ang pare-parehong pagtatag ngayon ang gagawing isang minutong gawain ang "
         "pagbabahagi mamaya."),
        ("Buksan ang pahina ng pagbabahagi at i-load ang backup mo",
         "Pumunta sa jwsync.org/share.html, piliin ang Magpadala ng mga nota at i-load ang "
         ".jwlibrary na file mo. Binabasa ito sa browser mo at hindi kailanman umaalis sa "
         "device mo."),
        ("Piliin ang tag sa salang, tapos Piliin lahat",
         "May pang-salang tag ang pumipili ng nota na naglilista ng bawat tag sa backup mo "
         "kasama ang bilang ng notang nasa ilalim nito. Piliin ang tag mo at makikipot ang "
         "listahan sa eksaktong mga notang iyon; tsinetsek silang lahat ng Piliin lahat. Iyan "
         "na ang buong pagpili — dalawang klik."),
        ("Gumawa ng file at ipadala ito",
         "Bumubuo ang JW Sync ng maliit na share file na naglalaman lamang ng mga tsinetsek "
         "mong nota. Ipadala ito sa chat, email o AirDrop — walang kasamang server at walang "
         "account sa alinmang panig."),
        ("Idaragdag ito ng kabila sa sarili niyang backup",
         "Bubuksan niya ang parehong pahina, pipiliin ang Tumanggap, titingnan ang mga nota, at "
         "idaragdag ang mga ito sa backup niya. Kasamang dumarating ang mga tag mo, at may "
         "karagdagang tag para sa pag-import, kaya isang salang lang din ang layo ng buong set "
         "para sa kaniya."),
    ],
    "sections": [
        ("Bakit tag ang ibahagi sa halip na backup",
         "Ang pagbibigay ng buong .jwlibrary na backup ay pagbibigay ng lahat ng naisulat mo, "
         "at buburahin ng pagsasauli nito ang mga nota ng kabila. Kabaligtaran nito sa "
         "dalawang bagay ang pagbabahagi ng tinagang piniling set: ang pinili mo lang ang "
         "nakikita niya, at wala siyang nawawala sa sarili niya."),
        ("Higit pang pagkipot, o pagbabahagi sa maraming tag",
         "Magkasabay na gumagana ang pang-salang tag at ang kahon ng paghahanap: pumili ng "
         "tag, tapos mag-type ng salita para higit pang paliitin, at tsinetsek pa rin ng "
         "Piliin lahat ang nasa harapan mo lang. Nakakahanap din ang paghahanap ng pangalan ng "
         "tag, kaya ang keyword na sinasalo ng maraming tag ay nagtitipon sa kanila sa isang "
         "paghakbang. Ipinapakita ng bawat nota sa listahan ang mga tag nito, kaya nakikita mo "
         "ang ipapadala bago mo ipadala."),
        ("Mga tag na sulit itago para sa pagbabahagi",
         "Sulit magpanatili ng ilang tag na para lang talaga sa pagbabahagi — pangalan ng "
         "kaganapan, paksang sinasaliksik mo para sa iba, ang taong kasama mong nag-aaral. "
         "Pagdating ng sandali ng pagpapadala, wala nang hahanapin: handa na ang set."),
    ],
    "faq": [
        ("Napupunta ba sa kabila ang mga tag ko?",
         "Oo. Dala ng mga ibinahaging nota ang mga tag nila, at may sariling tag ang "
         "pag-import, kaya mahahanap, masusuri o maaalis ng tatanggap ang buong batch sa "
         "bandang huli."),
        ("Paano kung maraming tag ang isang nota?",
         "Lalabas ito sa ilalim ng bawat isa sa salang, at kasamang dadala ang lahat ng tag "
         "nito. Hindi kailanman naaalis ng pag-salang sa isang tag ang iba pa."),
        ("Naaalis ba sa library ko ang mga nota kapag nagbahagi ako?",
         "Hindi. Kinokopya lang ng pagbabahagi ang mga nota sa maliit na file; hindi "
         "nagagalaw ang backup mo at ang app mo."),
        ("Puwede ko bang ipadala ang parehong tag sa maraming tao?",
         "Oo — karaniwang file lang ang share file. Ipadala ito sa kasindaming taong gusto mo, "
         "at idaragdag ito ng bawat isa sa sariling library niya nang hiwalay."),
    ],
}

GUIDES_TL["share-notes-with-bible-student"] = {
    "title": "Ibahagi ang mga nota sa JW Library sa isang estudyante sa Bibliya",
    "h1": "Pagbabahagi ng mga nota sa pag-aaral sa taong kaaral mo sa Bibliya",
    "description": "Ipadala ang mga nota para sa isang aralin — mga teksto, ilustrasyon, ang "
                   "mga puntong inihanda mo — diretso sa JW Library ng kabila, nang hindi "
                   "ginagalaw ang anumang isinulat niya mismo.",
    "intro": [
        "Kapag naghahanda ka ng pag-aaral, karamihan sa trabaho ay napupunta sa sarili mong "
        "mga nota: ang dagdag na mga teksto, ang ilustrasyong nagpaunawa ng punto, ang sagot "
        "sa tanong niya noong isang linggo. Isang bagay ang basahin ito nang malakas; ibang "
        "bagay ang mag-iwan sa kaniya ng kopyang mababasa niyang muli sa buong linggo.",
        "Inilalagay ng pagbabahagi ng nota ang inihanda mong mga nota sa library niya bilang "
        "tunay na mga nota ng JW Library, nakakabit sa parehong talataan at talata — hindi "
        "bilang screenshot o mensaheng lalampasan lang niya.",
    ],
    "steps": [
        ("Ihanda ang mga nota ng aralin sa JW Library",
         "Isulat ang mga nota gaya ng dati, sa mga talataan at tekstong sakop ng aralin. "
         "Bigyan sila ng tag — ang pangalan ng tao, o ang publikasyon — para madaling piliin "
         "ang set sa bandang huli."),
        ("Buksan ang pahina ng pagbabahagi at i-load ang backup mo",
         "Gumawa ng backup (Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup), "
         "tapos buksan ang jwsync.org/share.html, piliin ang Magpadala ng mga nota at i-load "
         "ang file. Hindi ito kailanman umaalis sa device mo."),
        ("Tsekan ang mga nota para sa araling ito",
         "Salain ang pumipili ayon sa tag na ginamit mo at pindutin ang Piliin lahat, o "
         "maghanap at tsekan isa-isa. Gumawa ng share file — nananatili sa kinalalagyan ang "
         "lahat ng iba pa sa library mo."),
        ("Ipadala ito at gabayan siya sa pagtanggap",
         "Kailangan muna niya ng sarili niyang backup — Personal na Pag-aaral → Backup at "
         "Pagsasauli → Gumawa ng backup. Tapos bubuksan niya ang jwsync.org/share.html, "
         "pipiliin ang Tumanggap, ilo-load ang file mo at ang backup niya, at ida-download "
         "ang na-update na backup."),
        ("Isasauli niya ito sa JW Library",
         "Backup at Pagsasauli → Isauli, piliin ang na-update na file, at lilitaw ang mga "
         "nota mo sa library niya katabi ng sarili niya — may tag, kaya alam niya kung alin "
         "ang galing sa iyo."),
    ],
    "sections": [
        ("Hindi kailanman napapalitan ang mga nota niya",
         "Ito ang mahalagang pagkakaiba sa pagpapadala ng backup. Pinapalitan ng pagsasauli "
         "ang buong library ng isang device; nagdaragdag naman dito ang pagtanggap ng "
         "ibinahaging nota. Ang anumang isinulat niya mismo — pati sa mismong parehong "
         "talataan — ay nananatiling gaya ng dati."),
        ("Isang lingguhang ritmo na dalawang minuto lang",
         "Kapag nagawa na ninyong dalawa ito nang minsan, maikli na ang rutina: maghanda, "
         "tsekan, ipadala, isauli. Para sa marami, mas madaling ipadala ang mga nota kaagad "
         "pagkatapos maghanda, para nasa estudyante na ito bago ang pag-aaral at hindi "
         "pagkatapos."),
    ],
    "faq": [
        ("Kailangan ba ng estudyante ng account o naka-install na app?",
         "Walang account kahit saan, at walang ini-install maliban sa JW Library mismo — "
         "karaniwang web page ang pahina ng pagbabahagi."),
        ("Paano kung hindi pa siya nakakagawa ng backup?",
         "Gumawa muna siya ng isa, sa JW Library sa ilalim ng Personal na Pag-aaral → Backup "
         "at Pagsasauli. Puwede kahit mukhang walang laman ang library; ang backup ang "
         "pagdaragdagan ng mga ibinahaging nota."),
        ("Puwede ko bang bawiin ang mga nota mamaya?",
         "Sa iyo ang file hangga't hindi mo ipinapadala. Kapag nasa iba na ito, sa kaniya na "
         "iyon, gaya ng kahit anong mensahe — kaya ibahagi lang ang komportable mong ibahagi "
         "sa pasulat."),
    ],
}

GUIDES_TL["share-meeting-notes-with-family"] = {
    "title": "Ibahagi ang mga nota sa pulong sa pamilya o sambahayan mo",
    "h1": "Pagbabahagi ng mga nota sa pulong ngayong linggo sa pamilya",
    "description": "May nagkasakit, may trabaho o nasa malayo — ipadala sa kaniya ang mga nota "
                   "ng linggo bilang maliit na file na maidaragdag niya sa sarili niyang JW "
                   "Library, nang walang nawawala kahit kanino.",
    "intro": [
        "Sa karamihan ng sambahayan, may sariling nota ang bawat isa sa sariling device, at "
        "laging may nakakalampas sa pulong. Minsan lang nakakatulong ang pagbabasa ng nota mo "
        "sa hapag; ang paglalagay ng mga ito sa library ng iba ang magpapagamit sa kaniya ng "
        "materyal sa bandang huli, sa mismong lugar na hahanapan niya.",
        "Dahil nota-por-nota ang pagbabahagi at hindi backup-por-backup, malayang "
        "makapagpapalitan ng nota ang maraming tao nang walang napapalitang library kahit "
        "kanino.",
    ],
    "steps": [
        ("I-backup ang device na pinagsulatan mo ng nota",
         "JW Library → Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup."),
        ("Piliin ang mga nota ng linggo",
         "Sa jwsync.org/share.html piliin ang Magpadala ng mga nota, i-load ang backup mo, at "
         "tsekan ang mga nota ngayong linggo — mabilis silang matitipon sa paghahanap ayon sa "
         "publikasyon, at kung tinagan mo ang mga nota ng linggo, matitipon sila ng pang-salang "
         "tag sa isang klik."),
        ("Ipadala ito sa chat ng pamilya",
         "Gumawa ng share file at ipadala ito sa paraang ginagamit na ng sambahayan — "
         "messaging app, email, AirDrop. Maliit na file ito na tsinetsek mong mga nota lang "
         "ang laman."),
        ("Idaragdag ito ng bawat isa sa sariling backup niya",
         "Bubuksan niya ang parehong pahina, pipiliin ang Tumanggap, ilo-load ang file mo "
         "kasama ang sarili niyang backup, ida-download ang na-update na backup at isasauli "
         "ito sa JW Library."),
    ],
    "sections": [
        ("Sa bawat isa nananatili ang sariling library",
         "Walang napapalitang nota ninuman, at hindi kailangang ibigay ninuman ang buong "
         "library para makasali. May tag ang mga na-import na nota, kaya nakikita agad ng "
         "bawat isa kung alin ang galing sa iba at puwede niyang burahin ang batch mamaya kung "
         "mas gusto niyang hindi ito itago."),
        ("Pampamilyang pagsamba: magtipon sa halip na magkalat",
         "Gumagana rin ang parehong kagamitan sa kabilang direksiyon. Kung sumusulat ng nota "
         "ang lahat tuwing pampamilyang pagsamba, puwedeng tipunin ng isang tao ang mga share "
         "file ng iba sa iisang backup at magkaroon ng pinagsamang nota ng sambahayan sa "
         "parehong materyal."),
    ],
    "faq": [
        ("Puwede bang sumali ang mga device ng mga bata?",
         "Puwede ang kahit anong device na kayang patakbuhin ang JW Library at magbukas ng web "
         "page. Pareho ang mga hakbang sa cellphone, tablet o computer."),
        ("Kailangan ba naming magkapareho ng plataporma?",
         "Hindi. Iisa ang format ng backup ng Android, iPhone, iPad at Windows app, kaya "
         "nakakatawid ang mga nota nang walang conversion."),
    ],
}

GUIDES_TL["receive-shared-jw-library-notes"] = {
    "title": "May nagpadala sa akin ng mga nota sa JW Library — paano ko ito bubuksan?",
    "h1": "Pagdaragdag sa sarili mong JW Library ng mga notang ibinahagi sa iyo",
    "description": "May pinadalang file ng ibinahaging nota o bloke ng teksto. Narito kung "
                   "paano ito tingnan at idagdag sa sarili mong backup ng JW Library nang wala "
                   "ni isang mawawala sa iyo.",
    "intro": [
        "Dumarating ang ibinahaging nota sa JW Library bilang maliit na file (nagtatapos sa "
        ".jwshare.json) o bilang blokeng tekstong idinikit sa mensahe. Hindi kayang buksan ng "
        "JW Library ang alinman dito — pero hindi mo naman ito kailangan. Binabasa ng panig na "
        "tumatanggap ng JW Sync ang ibinahaging nota, ipinapakita ang laman nito, at isinusulat "
        "ang mga ito sa isang backup mo.",
        "Nangyayari ang buong palitan sa device mo. Walang account, walang ina-upload, at "
        "nadaragdagan lang ang sarili mong mga nota, hindi kailanman napapalitan.",
    ],
    "steps": [
        ("Gumawa muna ng backup ng sarili mong library",
         "Sa JW Library: Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup. Ito "
         "ang file na dadagdagan ng ibinahaging mga nota, kaya dapat bago ito."),
        ("Buksan ang pahina ng pagbabahagi at piliin ang Tumanggap",
         "Pumunta sa jwsync.org/share.html at piliin ang Tumanggap ng mga nota."),
        ("I-load ang ipinadala sa iyo",
         "Piliin ang .jwshare.json na file, o idikit ang ibinahaging teksto diretso sa kahon "
         "kung dumating ito bilang mensahe. Sa alinmang paraan, makikita mo ang read-only na "
         "tanaw ng bawat nota bago pa may maisulat."),
        ("Idagdag ang mga ito sa backup mo",
         "I-load ang sarili mong backup, piliin ang tag na dapat taglayin ng mga na-import na "
         "nota, at idagdag sila. Bumubuo ang JW Sync ng na-update na backup na ida-download "
         "mo."),
        ("Isauli ang na-update na backup sa JW Library",
         "Personal na Pag-aaral → Backup at Pagsasauli → Isauli, piliin ang na-update na file. "
         "Nasa library mo na ang ibinahaging mga nota, nakaupo sa tamang talataan at talata."),
    ],
    "sections": [
        ("Walang napapalitan sa iyo",
         "Idinaragdag ang ibinahaging nota bilang bagong nota. Kahit dumapo ang isang "
         "ibinahaging nota sa talataang sinulatan mo na, nananatili ang dalawa — buo ang iyo, "
         "katabi ang kaniya. Ang tanging tandaan ay ang karaniwang tuntunin sa pagsasauli: "
         "isauli ang na-update na backup, hindi ang mas luma."),
        ("Nagbago ang isip mo mamaya?",
         "May taglay na tag ang bawat na-import na nota, ang tag na pinili mo noong idinagdag "
         "mo sila. Buksan ang backup mo sa Study Explorer, salain ayon sa tag na iyon, at "
         "masusuri o mabubura mo ang buong batch nang minsanan."),
    ],
    "faq": [
        ("Dumating ang file na napalitan ng .txt o bumukas bilang teksto — sira ba ito?",
         "Hindi. Madalas itong gawin ng mga messaging app. Kopyahin ang teksto at idikit ito "
         "sa kahon ng Tumanggap; eksaktong ganoon din ang gagana."),
        ("Kailangan ko ba ang buong backup ng nagpadala?",
         "Hindi. Nasa share file lang ang mga notang pinili niyang ipadala — wala nang iba "
         "mula sa library niya."),
        ("May ina-upload ba kapag tinitingnan ko ang mga nota?",
         "Wala. Ang pagbabasa ng ibinahaging file, ang pagtingin dito at ang pagsulat ng "
         "na-update na backup ay pawang nangyayari sa browser sa device mo."),
    ],
}

GUIDES_TL["share-notes-with-study-group"] = {
    "title": "Ibahagi ang mga notang pananaliksik sa isang study group",
    "h1": "Pagbabahagi ng pananaliksik sa isang grupo — at pagtitipon ng sa kanila",
    "description": "Isang file, maraming tao: ipadala ang isang set ng notang pananaliksik sa "
                   "lahat ng nag-aaral ng parehong paksa, at tipunin ang ipinadala nilang "
                   "balik sa iisang set na sa iyo.",
    "intro": [
        "Kapag maraming tao ang naghuhukay sa parehong paksa, kadalasang nagkakalat ang "
        "pananaliksik — nahanap ng isa ang mga cross-reference, ng isa pa ang kasaysayan, ng "
        "pangatlo ang mga ilustrasyon. Ibang-iba ang pagbabasa ng screenshot ng isa't isa sa "
        "pagkakaroon ng materyal sa sarili mong library, sa mismong mga talata, at mahahanap "
        "pa sa susunod na taon.",
        "Dahil file lang ang share file, isang export lang ay sapat na sa buong grupo, at "
        "ang parehong paraan ang magdadala pabalik sa iyo ng gawa nila.",
    ],
    "steps": [
        ("Tagan ang pananaliksik mo habang tinitipon",
         "Bigyan ng tag ang paksa sa JW Library para manatiling magkakasama ang set. Sa Study "
         "Explorer, puwede kang magdagdag ng tag sa maraming nota nang sabay kung hindi mo ito "
         "nagawa noon."),
        ("Gumawa ng isang share file para sa grupo",
         "Sa jwsync.org/share.html piliin ang Magpadala ng mga nota, i-load ang backup mo, "
         "kunin ang tag ng paksa sa pang-salang tag, pindutin ang Piliin lahat at gumawa ng "
         "file."),
        ("I-post ito nang minsan lang",
         "Ipadala ang parehong file sa lahat — group chat, email sa maraming tao, kung ano man "
         "ang ginagamit na ng grupo. Walang setup kada tao at walang kopya sa server."),
        ("Hilingin ang sa kanila bilang kapalit",
         "Kayang gawin ng bawat isa ang eksaktong ganito sa panig niya. Idagdag sa backup mo "
         "ang bawat natatanggap mong file nang paisa-isa, na may sariling tag ang bawat "
         "pag-import — mainam ang pangalan ng nagpadala — para laging alam mo kung kanino ang "
         "bawat pananaliksik."),
    ],
    "sections": [
        ("Isang pinagsamang set, natutukoy pa rin ang pinagmulan",
         "Pagkalipas ng ilang ikot, nasa sarili mong library na ang buong pananaliksik ng "
         "grupo sa paksa, nasa tamang talataan at talata, at may tag ang bawat ambag ayon sa "
         "pinagmulan. Nahahanap ng paghahanap ang lahat nang sabay; napaghihiwalay silang muli "
         "ng mga tag kahit kailan mo gusto."),
        ("Walang kailangang maglantad ng library",
         "Ang tsinetsek lang ng bawat isa ang ibinabahagi. Hindi kailanman napupunta sa file "
         "ang natitira sa library ng bawat tao — personal na pag-aaral, pribadong paalala, at "
         "lahat ng iba pa."),
    ],
    "faq": [
        ("May limitasyon ba sa dami ng notang maibabahagi ko nang sabay?",
         "Sa praktika, wala. Maliliit ang mga nota; kahit malaking set ay nagbubunga pa rin ng "
         "file na kayang ipadala sa isang mensahe."),
        ("Paano kung dalawang tao ang magpadala ng parehong nota?",
         "Makikita mo ito nang dalawang beses, bawat isa sa ilalim ng tag ng nagpadala. "
         "Pinapadali ng paghahanap sa Study Explorer ang pagtukoy at pagbura sa halos "
         "magkaparehong nota."),
        ("Puwede bang tumanggap nang walang ipinapadalang kapalit?",
         "Oo. Magkahiwalay ang pagtanggap at pagpapadala — walang obligadong magbahagi para "
         "maidagdag ang natanggap niya."),
    ],
}

GUIDES_TL["share-talk-preparation-notes"] = {
    "title": "Ipasa ang pananaliksik sa likod ng isang pahayag o atas",
    "h1": "Pagpapasa ng pananaliksik mo sa pahayag at atas",
    "description": "Ikaw ang naghukay para sa isang pahayag, bahagi o atas. Narito kung paano "
                   "ipapasa ang pananaliksik sa susunod na mangangailangan nito — bilang tunay "
                   "na nota sa library niya, o bilang payak na teksto para sa dokumento.",
    "intro": [
        "Bihirang minsan lang magamit ang paghahanda. Ang mga tekstong hinanap mo, ang "
        "kasaysayang binasa mo, ang paraang napagpasiyahan mong ipakilala ang isang punto — "
        "mas gugustuhin ng sinumang tatalakay sa parehong materyal na magsimula roon kaysa sa "
        "blangkong pahina.",
        "Dalawang paraan ang ibinibigay ng JW Sync para maipasa ito, at bagay ang bawat isa sa "
        "iba't ibang tao: bilang mga notang dadapo sa JW Library ng kabila, o bilang payak na "
        "tekstong maididikit niya sa dokumento.",
    ],
    "steps": [
        ("Tipunin ang pananaliksik sa ilalim ng isang tag",
         "Habang naghahanda ka, tagan ang mga nota ayon sa tema o sa atas. Kung naisulat na "
         "sila at walang tag, buksan ang backup mo sa Study Explorer at tagan silang lahat sa "
         "loob ng ilang minuto."),
        ("Pagpasiyahan kung anong anyo ang bagay sa kabila",
         "Gusto ng nag-aaral sa JW Library ang mga nota sa library niya. Gusto ng gumagawa ng "
         "dokumento ang teksto. Kaya mong gawin ang dalawa mula sa parehong set."),
        ("Para magpadala ng nota: gamitin ang pahina ng pagbabahagi",
         "Sa jwsync.org/share.html piliin ang Magpadala ng mga nota, i-load ang backup mo, "
         "salain ayon sa tag na ginamit mo at pindutin ang Piliin lahat, tapos gumawa ng file. "
         "Idaragdag niya ito sa sarili niyang backup at isasauli — hindi nagagalaw ang sarili "
         "niyang mga nota."),
        ("Para magpadala ng teksto: mag-export mula sa Study Explorer",
         "Salain patungo sa parehong set at kopyahin o i-export ito bilang Markdown o payak na "
         "teksto. Nananatili ang pormat, kaya nananatiling maayos ang istrukturadong balangkas "
         "kapag idinikit sa dokumento."),
    ],
    "sections": [
        ("Mag-iwan ng kopya para sa sarili mo, sa anyong mahahanap mong muli",
         "Sulit ding itago ang parehong export para sa sarili mong gamit. Ang tag kasama ang "
         "saklaw ng petsa ay nagpapadaling mahanap ang buong paghahanda pagkalipas ng mga "
         "taon, na siya mismong panahong kakailanganin mo ito — at ginagawang hiwalay na file "
         "ng pagkuha ayon sa petsa sa Study Explorer ang kahit anong yugto ng panahon."),
    ],
    "faq": [
        ("Mananatili ba ang mga tekstong nakaugnay sa tamang talata?",
         "Oo — dala ng ibinahaging nota ang talataan at talatang pinagkabitan nito, kaya "
         "dumadapo sila sa tamang lugar sa library ng kabila."),
        ("Puwede ko bang ibahagi ang mga notang may highlight?",
         "Oo. Kasamang dumadala ang mga highlight na nakakabit sa mga notang ibinabahagi mo."),
    ],
}

GUIDES_TL["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Maghanda para sa pulong gamit ang mga notang naisulat mo na",
    "h1": "Lingguhang paghahanda gamit ang mga notang mayroon ka na",
    "description": "Napag-aralan mo na ang materyal na ito. Narito ang maikling lingguhang "
                   "rutina na naglalabas ng mga lumang nota, highlight at sagot mo sa parehong "
                   "publikasyon bago ka maghandang muli.",
    "intro": [
        "Karamihan ay naghahanda tuwing linggo mula sa blangkong pahina, kahit ilang beses na "
        "silang nakasulat tungkol sa parehong paksa — minsan sa parehong teksto pa nga. Nasa "
        "library mo ang naunang kaisipang iyon; ang tanging problema ay walang nagbabalik nito "
        "sa iyo sa tamang sandali.",
        "Inaayos ito ng limang-minutong rutina sa simula ng paghahanda, at wala itong ginagamit "
        "kundi ang backup na mayroon ka na.",
    ],
    "steps": [
        ("Mag-load ng bagong backup sa Study Explorer",
         "Gumawa ng backup sa JW Library, tapos buksan ito sa jwsync.org. Sa browser mo "
         "binabasa ang lahat."),
        ("Hanapin ang paksa bago ka magsimula",
         "Hanapin ang tekstong pantema, ang paksa o ang publikasyon. Sabay-sabay na lilitaw "
         "ang anumang isinulat mo tungkol dito noong mga nakaraang taon, sa lahat ng "
         "publikasyong pinaglabasan nito."),
        ("Tingnan ang mga sagot mo sa pag-aaral",
         "Tinitipon ng tanawing Mga Sagot sa Pag-aaral ang mga sagot na tinipa mo sa mga "
         "tanong, kaya naroon ang mga naunang pagdaan mo sa parehong materyal para "
         "pagtayuan sa halip na ulitin."),
        ("Idagdag ang kulang, tapos ibalik ito",
         "Puwedeng i-edit o gumawa ng nota doon mismo — pamagat, teksto, tag, kulay ng "
         "highlight. I-export ang na-edit na backup at isauli ito sa JW Library, at nasa app "
         "na ang paghahanda mo para sa pulong."),
    ],
    "sections": [
        ("Bakit mahalaga ang mga lumang nota",
         "Ang pagbabalik-tanaw sa napagpasiyahan mo noong huli ang nagpapabago sa paghahanda "
         "tungo sa isang bagay na naiipon. Hindi mo na muling natutuklasan ang parehong mga "
         "punto at sa halip ay pinagtatayuan mo na sila — at ang mga notang idaragdag mo "
         "ngayong linggo ang magiging simula ng susunod na ikot."),
        ("Isang mas banayad na paraan: hayaang lumapit sa iyo ang mga nota",
         "Kung parang trabaho na ang lingguhang paghahanap, ang Resurface sa pahinang Study "
         "Stats ang kusang magdadala ng ilang lumang nota bawat araw, pati na ang mga isinulat "
         "mo sa petsang ito noong mga nakaraang taon. Parehong pakinabang, walang rutinang "
         "kailangang tandaan."),
    ],
    "faq": [
        ("Direktang nababago ba ng pag-edit sa browser ang library ko?",
         "Hindi. Nag-e-export ka ng na-update na backup at isinasauli ito sa JW Library — "
         "nababago lang ang app sa pagsasauling ikaw mismo ang gumagawa."),
        ("Ina-upload ba ang backup ko kapag naghahanap ako rito?",
         "Hindi. Sa browser mo binabasa ang file; walang ipinapadala kahit saan."),
    ],
}

GUIDES_TL["print-jw-library-notes"] = {
    "title": "Paano i-print ang mga nota mo sa JW Library",
    "h1": "Paglalagay sa papel ng mga nota mo sa JW Library",
    "description": "Walang print button ang JW Library. I-export ang mga nota mo bilang teksto "
                   "o Markdown, idikit sa kahit anong dokumento, at i-print — talaarawan sa "
                   "pag-aaral, set ng nota para sa walang app, o imbakan.",
    "intro": [
        "Walang paraan para mag-print mula sa JW Library, at mahirap basahin ang screenshot ng "
        "screen ng cellphone. Pero sa iyo ang mga nota, at madali lang silang mailagay sa "
        "dokumentong napi-print kapag nabasa mo na ang backup na file.",
        "Binabasa ng Study Explorer ang .jwlibrary na backup sa browser mo at pinapayagan kang "
        "kopyahin o i-export ang kahit anong piniling nota bilang payak na teksto o Markdown — "
        "na naiintindihan na ng bawat word processor, notes app at printer.",
    ],
    "steps": [
        ("Gumawa ng backup at buksan ito",
         "JW Library → Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup, tapos "
         "i-load ang file sa jwsync.org."),
        ("Paliitin sa gusto mong mapunta sa papel",
         "Salain ayon sa publikasyon, tag, kulay ng highlight o saklaw ng petsa, o maghanap ng "
         "paksa. Posible ang pag-print ng lahat, pero kadalasang mas kapaki-pakinabang na "
         "dokumento ang nagmumula sa sinalang set."),
        ("Kopyahin o i-export bilang teksto o Markdown",
         "Ilabas ang piniling set bilang Markdown o payak na teksto. Nananatili ang bold, "
         "italic at listahan, kaya nananatiling maayos sa pahina ang istruktura ng mga nota."),
        ("Idikit sa dokumento at i-print",
         "Puwede ang kahit anong word processor o notes app. Itakda ang mga ulo at margin na "
         "gusto mo, tapos i-print o i-save bilang PDF."),
    ],
    "sections": [
        ("Paggawa ng talaarawan sa pag-aaral",
         "Ang saklaw ng petsa ang likas na yunit para sa nakalimbag na talaarawan — isang taon "
         "ng nota, o ang panahong sakop ng isang publikasyon. Nagbubunga ang pagkuha ayon sa "
         "petsa ng malinis at magkakasunod na set na maipi-print o maipapabalat, at kaaya-ayang "
         "hawakan sa labas ng screen."),
        ("Pag-print para sa hindi gumagamit ng app",
         "Hindi lahat ay nag-aaral mula sa device. Tunay na kapaki-pakinabang ang nakalimbag "
         "na set ng nota sa kasalukuyang materyal para sa mas gusto ang papel, at kasingtagal "
         "lang ng dalawang minuto gaya ng ibang export."),
    ],
    "faq": [
        ("Puwede ko rin bang i-print ang mga highlight ko?",
         "Inililista ng tanawing highlight ang mga bahaging minarkahan mo, at nakokopya rin "
         "ang listahang iyon bilang teksto kasama ang mga nota mo."),
        ("May nababago ba sa JW Library kapag nag-export?",
         "Wala. Isang kopya ng backup mo ang binabasa ng pag-export; hindi nagagalaw ang "
         "orihinal mong file at ang app."),
    ],
}

GUIDES_TL["clean-up-duplicate-jw-library-notes"] = {
    "title": "Linisin ang mga dobleng at blangkong nota sa JW Library",
    "h1": "Pag-aalis ng dobleng nota, blangkong nota at kalat",
    "description": "Dalawang beses na nakapagsauli ng backup, o na-import muli ang parehong "
                   "mga nota? Sinusuri ng Library Doctor ang .jwlibrary na file mo sa browser, "
                   "hinahanap ang mga doble at blangkong nota, at gumagawa ng malinis na kopya.",
    "intro": [
        "Nag-iipon ng kalat ang mga library. Ang pagsasauli ng backup sa device na may ilan na "
        "sa parehong nota, ang dalawang beses na pag-import ng ibinahaging set, o ang "
        "taon-taong kalahating nota na hindi natapos — may naiiwan ang bawat isa, at walang "
        "paraan sa JW Library para walisin lahat ito nang sabay.",
        "Isang libreng health check para sa .jwlibrary na file ang Library Doctor. Sinusuri "
        "nito ang backup sa browser mo, sinasabi sa simpleng salita ang natagpuan nito, at "
        "inaayos sa isang tap ang naaayos.",
    ],
    "steps": [
        ("Mag-backup muna — gaya ng dati",
         "JW Library → Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup. Itago "
         "ang file na ito; ito ang panangga mo."),
        ("Patakbuhin ang health check",
         "Buksan ang jwsync.org, i-load ang backup at simulan ang Library Doctor. Sinusuri "
         "nito ang laman at istruktura ng file nang hindi ito ipinapadala kahit saan."),
        ("Basahin ang natagpuan nito",
         "Malinaw na nakalista ang mga doble, blangkong nota at iba pang kalat, kasama ang "
         "bilang, kaya makikita mo ang laki ng problema bago mo baguhin ang anuman."),
        ("Ayusin at i-download ang malinis na kopya",
         "Isang tap ang naglalapat ng mga pag-aayos at gumagawa ng bagong nalinis na "
         ".jwlibrary na file. Hindi kailanman binabago ang orihinal mo."),
        ("Isauli ang malinis na file",
         "Backup at Pagsasauli → Isauli, at piliin ang nalinis na file. Ganoon pa rin ang "
         "library mo, wala na lang ang kalat."),
    ],
    "sections": [
        ("Saan ba nagmumula ang mga doble",
         "Halos palaging sa pagsasauli. Kung isasauli mo ang backup sa device na may ilan na "
         "sa parehong materyal — o isasauli mo ang parehong file nang dalawang beses sa "
         "magkaibang daan — walang paraan ang app para malamang nakita na nito ang mga notang "
         "iyon."),
        ("Ang pagsasama ang paraan para maiwasan sila",
         "Ito mismo ang dahilan kung bakit mas ligtas ang pagsasama ng dalawang backup kaysa "
         "pagsasauli ng isa sa ibabaw ng isa pa: natutukoy ng pagsasama ang materyal na "
         "nariyan na at isa lang ang itinatago. Tumatakbo ang parehong pagsusuri sa loob ng "
         "bawat pagsasama, kaya malinis ang lumalabas na pinagsamang backup kahit hindi "
         "malinis ang mga pumasok na file."),
    ],
    "faq": [
        ("Buburahin ba nito ang mga notang gusto ko talaga?",
         "Inaalis nito ang eksaktong doble at ang blangkong nota — mga bagay na walang laman "
         "na mawawala. At dahil bagong file ang isinusulat nito sa halip na i-edit ang sa iyo, "
         "laging naroon ang orihinal na mababalikan."),
        ("Kaya ba nitong ibalik ang mga notang binura ko sa app?",
         "Hindi. Kung binura ang isang nota sa JW Library bago ginawa ang backup, wala ito sa "
         "file para mabawi — sa mas lumang backup dapat maghanap."),
    ],
}

GUIDES_TL["backup-jw-library-before-phone-repair"] = {
    "title": "Mag-backup ng JW Library bago ang factory reset o pagpapaayos",
    "h1": "Bago ang factory reset, pagpapaayos o pagbebenta ng cellphone",
    "description": "Binubura ng reset ang mga nota sa JW Library kasama ng lahat, at hindi ito "
                   "dala ng mga tool sa paglilipat. Gumawa ng backup, tiyaking bumubukas nga "
                   "ito, tapos mag-reset nang walang panganib.",
    "intro": [
        "I-reset ang cellphone, ipaayos ito, o ipasa sa iba, at kasama nitong aalis ang datos "
        "ng personal na pag-aaral sa JW Library. Bumabalik ang mga litrato at app mula sa "
        "cloud backup; ang taon-taong nota, highlight at bookmark ay kadalasang hindi, dahil "
        "nilalaktawan ng mga tool sa paglilipat ang pribadong datos ng app.",
        "Limang minuto lang ang lunas, at ang hakbang na nilalaktawan ng marami ang siyang "
        "pinakamahalaga: ang pagtiyak na tunay ngang nababasa ang backup na file bago mabura "
        "ang device.",
    ],
    "steps": [
        ("Gumawa ng backup",
         "JW Library → Personal na Pag-aaral → Backup at Pagsasauli → Gumawa ng backup. "
         "Makakakuha ka ng .jwlibrary na file — kadalasan ay ilang megabyte lang."),
        ("Ilabas ito sa device",
         "I-email ito sa sarili mo, o ilagay sa Drive, iCloud o sa folder sa computer. Ang "
         "backup na nasa cellphone lang na buburahin mo ay hindi backup."),
        ("Tiyaking bumubukas ito bago mo burahin ang anuman",
         "I-load ang file sa jwsync.org at tingnan ito — dapat naroon ang lahat ng nota, "
         "highlight at bookmark, at ipapahiwatig ng health check ang anumang mali sa file. Ito "
         "ang buong punto ng pagsasanay na ito: huli na kapag pagkatapos mo pa lang malaman "
         "na hindi mababasa ang file."),
        ("Mag-reset, tapos magsauli",
         "Pagkatapos ng reset o pagpapaayos, i-install ang JW Library, mag-sign in, tapos "
         "Backup at Pagsasauli → Isauli at piliin ang file mo."),
        ("Gumamit ng hiram na cellphone sa pagitan? Magsama, huwag mag-overwrite",
         "Kung sumulat ka ng nota sa pansamantalang device, i-backup din iyon at pagsamahin "
         "ang dalawang file sa jwsync.org bago magsauli — kung hindi, buburahin ng pagsasauli "
         "ng lumang backup ang lahat ng isinulat mo habang naghihintay."),
    ],
    "sections": [
        ("Bakit sulit ang dagdag na isang minuto sa pagtiyak",
         "Ang naputol na paglilipat, ang cloud drive na sumisira ng file, at ang extension na "
         "napapalitan sa daan ay pawang gumagawa ng mga backup na mukhang maayos sa folder pero "
         "nabibigo sa pagsasauli. Ang pagbubukas muna ng file ang nagpapabago sa tahimik na "
         "problema tungo sa problemang naaayos mo pa, habang nasa orihinal na device pa rin "
         "ang datos."),
        ("Itago ang file pagkatapos ng pagsasauli",
         "Huwag itong burahin kapag gumagana na ang bagong device. Ang mga lumang backup lang "
         "ang daan pabalik kapag may aksidenteng nabura kang nota makalipas ang ilang buwan, "
         "at wala namang gastos sa pag-iingat sa kanila."),
    ],
    "faq": [
        ("Babalik ba ang mga na-download kong publikasyon?",
         "Dala ng backup ang datos ng personal na pag-aaral mo — mga nota, highlight, "
         "bookmark, tag at playlist. Muling mada-download lang ang mga publikasyon pagkatapos."),
        ("Gumagana ba ang file kung papalit ako ng brand o plataporma ng cellphone?",
         "Oo. Pareho ang .jwlibrary na format sa Android, iPhone, iPad at Windows."),
    ],
}

GUIDES_TL["jw-library-notes-missing-after-update"] = {
    "title": "Nawawala ang mga nota sa JW Library pagkatapos ng update o muling pag-install",
    "h1": "Nawala ang mga nota pagkatapos ng update, muling pag-install o pagsasauli",
    "description": "Naglaho ang mga nota mo pagkatapos mag-update, mag-install muli o mag-sign "
                   "in ulit. Kung ano ang unang gagawin, kung ano ang huwag gagawin, at kung "
                   "paano mababawi ang mga ito nang hindi nawawala ang isinulat mo simula noon.",
    "intro": [
        "Nakakabahala ang magbukas ng JW Library pagkatapos ng update at makitang wala na ang mga nota mo, at sa karamihan ng pagkakataon ay nababawi ang mga ito. Ang mahalaga ay ang gagawin mo sa susunod na ilang minuto — sa partikular, ang hindi paggawa ng iisang bagay na gumagawang tuluyang pagkawala ang isang kalagayang nababawi pa.",
        "Hindi kaaya-ayang sandali: bumukas ang JW Library, at wala ang mga nota. Bago ang "
        "anupaman, isang payo — huwag magmadali. Karamihan sa nagpapawalang-bawi sa "
        "sitwasyong ito ay nangyayari sa unang sampung minuto, sa pag-overwrite mismo sa "
        "backup na naglalaman pa ng nawawalang mga nota.",
        "Sundin ang mga hakbang sa ibaba ayon sa pagkakasunod. Ang layunin ay makarating sa "
        "iisang file na naglalaman ng lumang mga nota at ng lahat ng isinulat mo simula noon.",
    ],
    "steps": [
        ("Huwag munang i-overwrite ang mga backup mo",
         "Iwasang gumawa ng bagong backup sa ibabaw ng luma, at huwag magsauli nang basta-"
         "basta. Ang mas lumang backup na file ang pinakamalamang na kinalalagyan pa rin ng "
         "mga nota mo."),
        ("Hanapin ang pinakabagong backup na mayroon ka",
         "Tingnan ang mga attachment sa email, Google Drive, iCloud Drive, ang downloads folder "
         "ng computer mo, at ang kahit anong device na pinagsaulian mo. Maliliit ang mga "
         "backup, kaya kadalasan ay mas marami ang kopya kaysa sa naaalala ng tao."),
        ("Tingnan ang loob ng file bago ito isauli",
         "I-load ang kandidatong file sa jwsync.org at tingnan kung ano talaga ang laman — "
         "ilang nota, mula sa aling publikasyon, hanggang anong petsa. Doon mo malalaman kung "
         "tama ba ang file, bago ka magpasiyang magsauli."),
        ("I-backup din ang kasalukuyang device",
         "Kahit mukhang walang laman, i-backup ito. Kung may naisulat ka simula nang mawala "
         "ang mga nota, ang file na ito lang ang kopya nito."),
        ("Pagsamahin ang dalawa, tapos magsauli",
         "Pagsamahin ang lumang backup at ang kasalukuyan sa jwsync.org. Naglalaman ang "
         "resulta ng nabawing mga nota at ng lahat ng naisulat simula noon, at isa lang ang "
         "itinatago sa mga doble. Ang pinagsamang file na iyon ang isauli — hindi kailanman "
         "ang lumang backup nang mag-isa."),
    ],
    "sections": [
        ("Bakit maling hakbang ang isauli ang lumang backup nang mag-isa",
         "Pinapalitan ng pagsasauli ang buong library ng device. Kung isasauli mo nang diretso "
         "ang lumang backup, mababawi mo ang nawawalang mga nota pero mawawala ang lahat ng "
         "naisulat pagkatapos gawin ang backup na iyon. Ang paunang pagsasama ang gumagawang "
         "walang mawawala sa pagbawi."),
        ("Kung ang backup mismo ang ayaw maisauli",
         "Hindi laging wala nang pag-asa ang file na nagkakamali habang isinasauli. Patakbuhin "
         "dito ang health check — kadalasang naaayos ang pinsalang mula sa naputol na "
         "download, cloud sync o napalitang extension, at normal na naisasauli ang nalinis na "
         "kopya."),
        ("Una: huwag ka munang gumawa ng bagong backup",
         "Kung nawala ang mga nota, labanan ang pagnanais na agad magbackup. Kinukunan ng backup ang kasalukuyang kalagayan, at kung walang laman ang kasalukuyang kalagayan ay may panganib kang patungan ang mabuting file na mayroon ka na. Alamin muna kung anong mga backup ang umiiral — sa Downloads, Files, email o cloud — at saka magpasya. Walang gumagaling sa device dahil sa backup na ginawa sa gulat."),
        ("Bakit para bang binubura ng update ang mga nota",
         "Karaniwang hindi pagbura ang dahilan. Maaaring iwan ng update ang app na nakaturo sa bago at walang lamang database habang nasa imbakan pa rin ang luma; ang muling pag-install — pati ang kusang ginawa ng update sa store na kalahating nabigo — ay nagpapasimula sa app mula sa wala; at sa mga device na may maraming gumagamit o profile, maaaring tumakbo ang app sa ilalim ng ibang profile. Sa lahat ng ito, hindi gaanong nabura ang mga nota kundi hindi lang naipapasok, at kaya karaniwang malinis na naibabalik ng pagsasauli mula sa backup ang lahat."),
        ("Bawiin ang lumang backup nang hindi itinatapon ang bagong gawa",
         "Kung nakapag-aral ka na mula nang gawin ang backup, ang basta pagsasauli ay pagpapalit ng isang pagkawala sa iba: ibinabalik nito ang lumang nota at inaalis ang mas bago. Ang paraan para maiwasan ito ay i-backup ang kasalukuyang kalagayan sa hiwalay na file, pagsamahin ito sa mas lumang backup para nasa iisang file ang dalawang pangkat ng nota, at isauli ang bunga. Mapapasaiyo nang sabay ang nabawing nota at ang kamakailan sa halip na pumili sa dalawa."),
        ("Kung kusang muling na-install ang app",
         "Nililinis ng muling pag-install ang pribadong imbakan ng app, kaya hindi na mababawi ang anumang wala sa backup — walang kopya sa cloud na maaasahan. Suriin ang lahat ng lugar kung saan maaaring na-save ang .jwlibrary na file bago mo tapusing wala nito, pati na ang folder ng mga naipadala sa email at anumang cloud storage na nagamit mo na. Pagkakita mo ng isa, isauli ito, at mula noon ay itago ang mga backup sa labas ng device."),
        ("Kapag nakabalik na ang lahat",
         "Kapag naisauli na ang mga nota mo, gumawa ng isa pang backup at itago sa labas ng device — ang pinagdaanan mo mismo ang katuwiran nito. Kung kinailangan mong pagsamahin ang lumang backup at ang kasalukuyang kalagayan para makarating dito, itago rin ang dalawang pinagmulang file: mga may-petsang larawan ang mga ito, at ang pagkakaroon ng marami sa kanila ang mismong dahilan kung bakit naging posible ang pagbawi."),
    ],
    "faq": [
        ("Nasa device pa ba kahit saan ang mga nota?",
         "Wala sa anyong maaabot mula sa labas ng app. Sa katotohanan, ang pagbawi ay "
         "nangangahulugang mas naunang backup na file — kaya napakahalaga ng pag-iingat sa mga "
         "luma."),
        ("Babalik ba ang mga nota kapag nag-sign in ulit?",
         "Hindi. Hindi nakaimbak sa isang account ang datos ng personal na pag-aaral; nasa "
         "device ito at sa pamamagitan lang ng backup na file naglalakbay."),
        ("Paano kung ilang buwan na ang tanging backup ko?",
         "Pagsamahin ito sa backup ng device sa kasalukuyang kalagayan nito. Mababawi mo ang "
         "lahat ng laman ng lumang file, at mapananatili ang lahat ng nasa device pa rin, nang "
         "hindi kailangang mamili sa dalawa."),
        ("Talaga bang wala na ang mga nota ko?",
         "Hindi naman kinakailangan. Kung may backup sa kung saan, ganap na nababawi ang lahat ng nasa loob nito. Ang hindi na mababawi ay ang gawa lang pagkatapos ng pinakahuling backup."),
        ("Puwede ko bang pagsamahin ang lumang backup at ang nasa device ngayon?",
         "Oo — i-backup muna ang kasalukuyang kalagayan, pagsamahin ito sa mas luma, at isauli ang bunga. Mapupunta sa iisang aklatan ang dalawang pangkat ng nota."),
        ("Buburahin ba ng pagsasauli ng lumang backup ang kamakailan kong mga nota?",
         "Kung iyon lang ang gagawin, oo, dahil pinapalitan ng pagsasauli ang datos ng device. Pagsamahin muna ang kasalukuyang backup at ang luma, at isauli ang pinagsamang file."),
        ("Dapat ko bang i-install uli ang app para maayos ito?",
         "Hindi — nililinis ng muling pag-install ang pribadong imbakan ng app at inaalis ang anumang pag-asang mabawi ang nasa device pa. Maghanap muna ng umiiral na backup, at ituring na huling paraan ang muling pag-install kapag mayroon ka na nito."),
    ],
}

GUIDES_TL["help-family-member-move-jw-library-notes"] = {
    "title": "Tulungan ang kapamilya sa paglipat ng mga nota niya sa JW Library",
    "h1": "Pagtulong sa iba na ilipat o masagip ang mga nota niya sa JW Library",
    "description": "Ikaw ang laging inaasahang mag-ayos ng cellphone. Narito ang "
                   "pinakamaikling maaasahang daan para mailipat ang mga nota sa JW Library ng "
                   "isang kamag-anak sa bagong device — pati na kung paano ito gawin nang "
                   "hindi binabasa ang mga nota niya.",
    "intro": [
        "Balang-araw ay may mag-aabot sa iyo ng cellphone niya, may bago sa tabi nito. Ang mga "
        "nota sa JW Library ang bahaging hindi kusang lumilipat, at kadalasan ang bahaging "
        "pinakamahalaga — taon-taong pag-aaral na walang tool sa paglilipat ang magdadala.",
        "Pareho ang proseso sa ginagawa mo para sa sarili mo, may isang dagdag na dapat isipin "
        "muna: kung kaninong device gagawin ang trabaho.",
    ],
    "steps": [
        ("Gabayan siya sa paggawa ng backup sa lumang device",
         "JW Library → Personal na Pag-aaral → tatlong-tuldok na menu → Backup at Pagsasauli → "
         "Gumawa ng backup. Nagse-save ito ng .jwlibrary na file. Kung wala ka sa tabi niya, "
         "kaya itong ituro sa telepono."),
        ("Kunin ang file kung saan mo ito kailangan",
         "Ipa-email niya ito sa sarili niya, o ipabahagi sa iyo. Sapat itong maliit para "
         "maipadala sa kahit anong messaging app."),
        ("Tiyaking bumubukas ang file",
         "I-load ito sa jwsync.org at kumpirmahing naroon ang mga nota. Ang paggawa nito bago "
         "mabura o maipasa ang lumang device ang nagpapabago sa masamang sorpresa tungo sa "
         "walang-anuman."),
        ("Magsama kung may nota na ang bagong device",
         "Kung ilang panahon na niyang ginagamit ang bagong cellphone, i-backup din iyon at "
         "pagsamahin ang dalawang file — kung hindi, buburahin ng pagsasauli ng lumang backup "
         "ang lahat ng isinulat niya sa bagong device."),
        ("Samahan siya sa pagsasauli",
         "Sa bagong device: Backup at Pagsasauli → Isauli, piliin ang file. Lilitaw ang lahat "
         "ng nota, highlight, bookmark at tag."),
    ],
    "sections": [
        ("Paggawa nito nang hindi binabasa ang mga nota niya",
         "Personal ang mga notang pang-personal na pag-aaral. Kung mas gusto mong hindi ito "
         "makita — o mas gusto niyang hindi mo makita — gawin ang lahat sa device niya: web "
         "page ito, kaya puwede mong buksan ang jwsync.org sa cellphone o tablet niya, i-load "
         "doon ang mga file niya, at hindi kailanman mapupunta sa sarili mong makina ang "
         "backup. Wala namang ina-upload sa alinmang paraan, pero sa ganitong paraan ay hindi "
         "man lang umaalis ang file sa kamay niya."),
        ("Iwanan siya ng backup na mahahanap niya",
         "Bago mo ibalik ang cellphone, tiyaking nasa lugar ang backup na file na mahahanap "
         "niyang muli — sa sarili niyang email o cloud drive, hindi lang sa downloads folder "
         "mo. Sa susunod, baka hindi ka na niya kailanganin."),
    ],
    "faq": [
        ("Puwede ko bang gawin ito nang malayuan?",
         "Oo. Kung kaya niyang gumawa ng backup at ipadala sa iyo ang file, gumagana nang "
         "malayuan ang lahat ng iba pa — at ilang tap lang ang pagsasauli na kaya mong ituro "
         "sa kaniya."),
        ("Android ang sa kaniya at iPhone ang bago. May problema ba?",
         "Wala. Pareho ang format ng backup sa Android, iPhone, iPad at Windows."),
        ("Paano kung hindi pa siya nakakagawa ng backup at wala na ang lumang cellphone?",
         "Kung ganoon, wala nang mapagkukunan ng pagbawi — nasa device na iyon ang datos. "
         "Sulit na simulan agad sa bagong cellphone ang ugali ng regular na pag-backup."),
    ],
}

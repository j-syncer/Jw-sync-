# -*- coding: utf-8 -*-
"""Italian translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → backup (il file .jwlibrary)
  Personal Study            → Studio personale
  Backup and Restore        → Backup e ripristino
  restore                   → ripristinare
  merge                     → unire / unione
  notes                     → note
  highlights                → evidenziazioni
  bookmarks                 → segnalibri
  tags                      → etichette
  Study Explorer            → Esplora studio
  Library Doctor            → Dottore della biblioteca
  Reading Companion         → Compagno di lettura
  Resurface                 → Riemergi
  Study Map                 → Mappa dello studio
  Study Stats               → Statistiche di studio
  Conflict Reviewer         → Revisore dei conflitti
  meeting                   → adunanza
  congregation              → congregazione
  assembly / convention     → assemblea / congresso
"""

GUIDES_IT = {}

GUIDES_IT["merge-jw-library-backups"] = {
    "title": "Come unire i backup di JW Library da due dispositivi",
    "h1": "Come unire i backup di JW Library da due dispositivi",
    "description": "Unisci note, evidenziazioni, segnalibri ed etichette di due o più backup "
                   "di JW Library in un unico file .jwlibrary — gratis, in privato, nel tuo "
                   "browser.",
    "intro": [
        "Se studi su più dispositivi — il telefono in Sala del Regno, il tablet a casa — ogni "
        "dispositivo finisce con le proprie note ed evidenziazioni. Il Backup e ripristino "
        "integrato in JW Library non riesce a unirli: ripristinare un backup sostituisce "
        "tutto ciò che c'è sul dispositivo, cancellando il lavoro fatto sull'altro.",
        "JW Sync risolve il problema. Legge due (o più) file di backup .jwlibrary e unisce "
        "note, evidenziazioni, segnalibri ed etichette di tutti in un nuovo file di backup. "
        "L'unione avviene interamente nel tuo browser — i tuoi file non vengono mai caricati "
        "su alcun server, quindi le tue note di studio personale restano private.",
    ],
    "steps": [
        ("Crea un backup su ogni dispositivo",
         "In JW Library apri Studio personale, tocca il menu a tre punti, scegli Backup e "
         "ripristino, poi Crea un backup. Fallo su ogni dispositivo. Ognuno produce un file "
         ".jwlibrary."),
        ("Apri JW Sync",
         "Vai su jwsync.org da qualsiasi browser — telefono, tablet o computer. Non c'è nulla "
         "da installare."),
        ("Carica entrambi i file di backup",
         "Trascina (o seleziona) i file .jwlibrary. JW Sync li legge in locale, sul tuo "
         "dispositivo."),
        ("Controlla l'anteprima prima dell'unione",
         "Prima che venga scritto qualsiasi dato, un'anteprima mostra esattamente cosa verrà "
         "unito. Se la stessa nota è stata modificata in modo diverso sui due dispositivi, il "
         "Revisore dei conflitti mostra entrambe le versioni affiancate, con le differenze "
         "parola per parola, così scegli quale tenere — oppure lascia decidere a «Suggerisci "
         "la migliore»."),
        ("Scarica il file unito e ripristinalo",
         "Scarica il file .jwlibrary unito, poi ripristinalo su ogni dispositivo con Backup e "
         "ripristino → Ripristina. Ora entrambi i dispositivi hanno la biblioteca completa e "
         "unificata."),
    ],
    "sections": [
        ("Cosa viene unito?",
         "Note, evidenziazioni, segnalibri, etichette e i loro collegamenti. I duplicati "
         "vengono rilevati automaticamente, quindi ripristinare il file unito non raddoppia "
         "mai nulla. I backup di Android, iPhone, iPad e dell'app per Windows usano lo stesso "
         "formato e si uniscono liberamente."),
        ("È sicuro?",
         "L'unione non modifica mai i tuoi file originali — produce un backup completamente "
         "nuovo, quindi gli originali restano intatti come rete di sicurezza. E poiché tutto "
         "gira nel browser, nessun dato lascia il tuo dispositivo."),
        ("Cosa c'è davvero dentro un file .jwlibrary",
         "Un backup .jwlibrary è un archivio ZIP. Rinomina una copia in .zip e aprila: troverai userData.db, un database SQLite che contiene tutte le note, le evidenziazioni, i segnalibri e le etichette che hai creato, insieme a un piccolo manifest.json che descrive il backup. Le tue note stanno nella tabella Note, le evidenziazioni in UserMark e BlockRange, i segnalibri in Bookmark, le etichette in Tag e TagMap. Capire che il backup è un database completo, e non un insieme di file sparsi, spiega tutto il resto di questa pagina: è il motivo per cui un ripristino è tutto o niente, ed è il motivo per cui due backup possono essere combinati."),
        ("Perché il ripristino di JW Library non può unire",
         "Quando ripristini, JW Library non legge il backup per aggiungere ciò che manca a quanto già presente sul dispositivo: sostituisce il database del dispositivo con quello del file. È una scelta deliberata e sicura, perché garantisce che il dispositivo resti in uno stato noto, ma significa che ripristinare il backup del tablet sul telefono scarta tutto ciò che il telefono aveva e il tablet no. Nessuna impostazione cambia questo comportamento, ed è esattamente la lacuna che l'unione colma: produce un unico file che contiene già il lavoro di entrambi i dispositivi, così il dispositivo su cui lo ripristini risulta completo."),
        ("Come vengono rilevati i duplicati",
         "Ogni nota, evidenziazione e segnalibro porta un GUID, un identificatore univoco assegnato al momento della creazione e conservato in tutti i backup successivi. Quando lo stesso elemento compare in due backup, entrambe le copie portano lo stesso GUID: viene riconosciuto come un solo elemento e mantenuto una volta. Per questo unire due volte gli stessi file non raddoppia nulla, e per questo puoi riunire ogni settimana senza rischi. Quando i GUID coincidono ma il testo differisce — la stessa nota modificata su entrambi i dispositivi — non è possibile risolvere automaticamente: l'elemento compare nel Revisore dei conflitti con un confronto parola per parola perché tu scelga."),
        ("Cosa non è contenuto nel backup",
         "Un backup contiene soltanto i tuoi dati di studio personale. Le pubblicazioni scaricate, le traduzioni della Bibbia, i video e l'audio non ne fanno parte, ed è per questo che i file di backup sono piccoli: di solito pochi megabyte anche dopo anni di studio. Dopo il ripristino su un nuovo dispositivo potresti dover riscaricare le pubblicazioni che leggi abitualmente. Nulla di ciò che hai scritto ne risente: le note sono ancorate alle pubblicazioni tramite riferimenti e si ricollegano non appena la pubblicazione è presente."),
        ("Se l'unione riporta 0 note aggiunte",
         "Quasi sempre è corretto, non è un difetto. Significa che tutte le note del secondo file esistevano già nel primo — cosa comune se hai unito di recente, o se un dispositivo è semplicemente indietro rispetto all'altro. Controlla l'anteprima: elenca cosa apporta ciascun file prima che venga scritto qualcosa. Se ti aspettavi elementi nuovi e non ne vedi, verifica di aver fatto il backup del dispositivo dopo la sessione di studio che stai cercando, perché un backup contiene solo ciò che esisteva nel momento in cui è stato creato."),
    ],
    "faq": [
        ("Posso unire più di due backup?",
         "Sì — carica tutti i file .jwlibrary che hai, uno per dispositivo. Vengono tutti "
         "uniti in un unico backup."),
        ("L'unione creerà note doppie?",
         "No. Note, evidenziazioni e segnalibri identici vengono rilevati e tenuti una volta "
         "sola. Le versioni davvero diverse della stessa nota compaiono nel Revisore dei "
         "conflitti, perché sia tu a decidere."),
        ("Funziona tra Android e iPhone?",
         "Sì. Il formato .jwlibrary è identico su Android, iOS, iPadOS e Windows, quindi i "
         "backup di piattaforme diverse si uniscono senza alcuna conversione."),
        ("Devo unire in un ordine preciso?",
         "No. L'unione non dipende dall'ordine: lo stesso insieme di file dà lo stesso risultato qualunque sia il primo che carichi. L'ordine incide solo su quale file viene considerato base nel riepilogo dell'anteprima."),
        ("Che fine fanno le etichette presenti su un solo dispositivo?",
         "Vengono mantenute intatte, insieme ai collegamenti tra le etichette e le note che contrassegnano. Se entrambi i dispositivi hanno un'etichetta con lo stesso nome, viene trattata come una sola e riceve le note di entrambi."),
        ("Quanto è grande il file unito?",
         "Più o meno quanto la somma degli originali meno i duplicati: di norma ancora pochi megabyte. I backup non contengono file multimediali delle pubblicazioni, quindi anche una biblioteca molto annotata resta abbastanza piccola da stare in un'email."),
        ("Posso annullare un ripristino?",
         "Non da JW Library, ed è per questo che conservare i backup originali conta. L'unione non modifica mai i file che carichi, quindi i backup precedenti restano esattamente come erano e possono essere ripristinati se vuoi tornare indietro."),
    ],
}

GUIDES_IT["sync-jw-library-multiple-devices"] = {
    "title": "Come sincronizzare JW Library tra più dispositivi",
    "h1": "Come tenere JW Library sincronizzato tra più dispositivi",
    "description": "JW Library non ha una sincronizzazione integrata tra dispositivi. Ecco una "
                   "routine semplice e privata per mantenere note, evidenziazioni e segnalibri "
                   "identici su telefono, tablet e computer.",
    "intro": [
        "Quasi tutti quelli che studiano su due dispositivi scoprono il problema allo stesso modo: le note scritte sul tablet non sono sul telefono, e ripristinare il backup di uno sull'altro cancellerebbe quello che quest'ultimo aveva. JW Library non offre sincronizzazione, e il suo ripristino è deliberatamente tutto o niente: tenere allineati i dispositivi richiede una routine, non un'impostazione.",
        "JW Library non sincronizza i dati di studio personale tra dispositivi: non esiste un "
        "account che porti le tue note dal telefono al tablet. Il meccanismo ufficiale è "
        "Backup e ripristino, e un ripristino sostituisce del tutto i dati del dispositivo. "
        "Come si fa allora a tenere due o tre dispositivi identici senza perdere nulla?",
        "La risposta è una breve routine di unione e ripristino. Fatta ogni settimana o ogni "
        "mese, richiede circa due minuti e lascia ogni dispositivo con la tua biblioteca "
        "completa.",
    ],
    "steps": [
        ("Fai il backup di ogni dispositivo",
         "Su ciascuno: Studio personale → menu a tre punti → Backup e ripristino → Crea un "
         "backup. Ottieni un file .jwlibrary per dispositivo."),
        ("Unisci i backup su jwsync.org",
         "Carica tutti i file. JW Sync unisce note, evidenziazioni, segnalibri ed etichette "
         "di ogni dispositivo in un unico file .jwlibrary — in locale nel browser, senza "
         "caricare nulla."),
        ("Ripristina il file unito su ogni dispositivo",
         "Backup e ripristino → Ripristina, scegli il file unito. Ora tutti i dispositivi "
         "sono identici e completi."),
        ("Lascia che JW Sync te lo ricordi",
         "Attiva un promemoria di sincronizzazione (settimanale o mensile) in JW Sync e ti "
         "avviserà quando è ora di ripetere la routine. Ricorda anche i dispositivi salvati, "
         "così ogni giro è più rapido."),
    ],
    "sections": [
        ("Perché non ripristinare semplicemente il backup più recente?",
         "Perché «più recente» riflette un solo dispositivo. Se nella stessa settimana hai "
         "preso appunti dell'adunanza sul telefono e note di studio sul tablet, ogni backup "
         "contiene qualcosa che manca all'altro. Ripristinarne uno sopra l'altro fa perdere "
         "metà del lavoro. È l'unione a rendere sicura la routine."),
        ("Ogni quanto conviene sincronizzare?",
         "Regolati su come studi. Due dispositivi attivi usati ogni giorno: una volta a "
         "settimana è comodo. Un tablet che esce solo per le adunanze: una volta al mese "
         "basta e avanza. Aspettare di più significa solo che l'unione avrà più materiale da "
         "combinare — tra un giro e l'altro non si perde mai nulla."),
        ("Perché non esiste una vera sincronizzazione",
         "JW Library non ha alcun account che porti i dati di studio personale da un dispositivo all'altro. Note, evidenziazioni e segnalibri vivono in un database dentro ciascun dispositivo e lì restano. L'unico meccanismo ufficiale per spostarli è Backup e ripristino, e un ripristino sostituisce i dati del dispositivo di destinazione anziché combinarli. Due dispositivi usati in modo indipendente divergono quindi in modo permanente, a meno che qualcosa non li unisca — che è esattamente lo scopo della routine qui sotto."),
        ("Tenere un file principale",
         "La routine funziona meglio se tratti un file unito come il principale corrente. A ogni ciclo, fai il backup di tutti i dispositivi, unisci quei backup e ripristina il risultato ovunque. Il file unito diventa il principale del ciclo successivo. Conservare i file principali datati nel cloud ti dà insieme un meccanismo di sincronizzazione e un archivio: se cancelli qualcosa per errore, un file principale precedente lo contiene ancora."),
        ("Cosa succede se salti un dispositivo per un po'",
         "Non si perde nulla. Un dispositivo rimasto fuori da diversi cicli porta semplicemente dati più vecchi; quando finalmente lo includi, le sue note si uniscono a tutto il resto e gli elementi ripetuti vengono abbinati tramite GUID anziché duplicati. L'unica situazione che richiede una decisione è la stessa nota modificata su due dispositivi dall'ultima unione, e compare nel Revisore dei conflitti con le due versioni affiancate."),
        ("Ogni quanto è abbastanza",
         "Regolalo su quanto lavoro ti dispiacerebbe rifare. Settimanale va bene se studi su due dispositivi quasi ogni giorno; mensile è più che sufficiente se uno viene usato di rado. L'importante è farlo prima di qualsiasi cosa irreversibile — un cambio di telefono, un ripristino, una riparazione — perché è allora che una divergenza diventa una perdita."),
        ("Telefono, tablet e l'app per Windows insieme",
         "Alla routine non interessa quanti dispositivi ci siano né cosa eseguano. Fai il backup di ciascuno, uniscili tutti in un solo passaggio, ripristina il file unito ovunque. Un computer Windows usato per la preparazione e un telefono usato alle adunanze si combinano esattamente come due telefoni, perché ogni piattaforma scrive lo stesso formato di backup."),
        ("Ridurre i conflitti prima che nascano",
         "I conflitti nascono solo quando la stessa nota viene modificata su due dispositivi tra un'unione e l'altra. In pratica è raro, e lo diventa ancora di più se scrivi su un dispositivo alla volta: leggendo ovunque, ma digitando dove digiti di solito. Unire più spesso riduce anche la finestra in cui può verificarsi una divergenza, e funziona meglio che cercare di ricordare quale dispositivo ha la versione più recente."),
        ("Dove la routine ripaga",
         "Il valore di tenere i dispositivi uniti non è l'ordine: è che ogni dispositivo diventa un backup completo della tua biblioteca di studio. Perdi o rompi uno qualsiasi e gli altri contengono ancora tutto, il che trasforma il caso peggiore da anni di note perse a un fastidio. È una posizione più solida di quella che può darti qualsiasi abitudine di backup su un unico dispositivo."),
    ],
    "faq": [
        ("JW Sync gira in background?",
         "No — è una pagina web, non un servizio installato. Nulla analizza i tuoi "
         "dispositivi. La routine la avvii tu quando vuoi; il promemoria facoltativo è solo "
         "una notifica."),
        ("Posso sincronizzare tre o più dispositivi?",
         "Sì. Fai il backup di ciascuno, carica tutti i file, unisci una volta e ripristina "
         "ovunque il file unito."),
        ("E se ho modificato la stessa nota su due dispositivi?",
         "Entrambe le versioni vengono mantenute finché non scegli. Il Revisore dei conflitti le mostra affiancate con un confronto parola per parola, oppure puoi lasciargli suggerire la più completa."),
        ("Conta l'ordine in cui ripristino?",
         "No. Una volta creato il file unito, ripristinarlo su ciascun dispositivo li porta tutti allo stesso stato completo, nell'ordine che preferisci."),
        ("Posso sincronizzare tre o più dispositivi?",
         "Sì. Fai il backup di ciascuno e caricali tutti nella stessa unione: non c'è alcun limite legato al numero di dispositivi."),
        ("Si può automatizzare?",
         "Non del tutto, perché JW Library non ha un'API di sincronizzazione e il passaggio di ripristino avviene nell'app. La routine manuale richiede circa due minuti una volta presa la mano."),
        ("Devo unire se sul secondo dispositivo mi limito a leggere?",
         "Se non ci annoti mai, ti basta ripristinarci sopra ogni tanto perché porti le tue note attuali."),
    ],
}

GUIDES_IT["transfer-jw-library-notes-new-phone"] = {
    "title": "Come trasferire le note di JW Library su un telefono nuovo",
    "h1": "Come trasferire le note di JW Library su un telefono nuovo",
    "description": "Passo passo: porta tutte le tue note, evidenziazioni, segnalibri ed "
                   "etichette di JW Library su un telefono nuovo con un backup .jwlibrary — e "
                   "come unire se hai già preso note sul telefono nuovo.",
    "intro": [
        "Cambiare telefono è il momento in cui più spesso si perdono anni di note di JW Library, non perché il trasferimento sia difficile, ma perché va fatto deliberatamente prima che il vecchio dispositivo venga cancellato. I dati di studio personale non seguono in modo affidabile un normale trasferimento tra telefoni, e JW Library non ne conserva copia in alcun account.",
        "Gli strumenti di trasferimento tra telefoni spostano app e foto, ma non portano in "
        "modo affidabile i dati di studio personale di JW Library. Il modo sicuro per portare "
        "note, evidenziazioni, segnalibri ed etichette su un telefono nuovo è il file di "
        "backup di JW Library stesso — pochi minuti, e funziona tra piattaforme diverse.",
    ],
    "steps": [
        ("Crea un backup sul telefono vecchio",
         "Apri JW Library → Studio personale → menu a tre punti → Backup e ripristino → Crea "
         "un backup. Questo salva un file .jwlibrary con tutti i tuoi dati di studio."),
        ("Porta il file sul telefono nuovo",
         "Inviatelo per email, oppure usa Google Drive, iCloud, AirDrop o un cavo USB. Il file "
         "è piccolo — di solito pochi megabyte."),
        ("Ripristina sul telefono nuovo",
         "Installa JW Library, poi Studio personale → Backup e ripristino → Ripristina, e "
         "scegli il file .jwlibrary. Compaiono tutte le note, le evidenziazioni, i segnalibri "
         "e le etichette."),
    ],
    "sections": [
        ("Hai già preso note sul telefono nuovo? Unisci invece di sovrascrivere",
         "Il ripristino sostituisce quello che c'è sul dispositivo. Se usi il telefono nuovo "
         "da un po' e ha già note sue, non ripristinare sopra: fai il backup anche del nuovo, "
         "unisci il backup vecchio e quello nuovo in un unico file su jwsync.org (gratis, nel "
         "browser, senza caricare nulla) e ripristina il file unito. Conservi entrambe le "
         "serie di note."),
        ("Un intoppo comune su iPhone",
         "Se il file di backup arriva su iPhone rinominato in .zip, rinominalo di nuovo in "
         ".jwlibrary prima di ripristinare — il contenuto è a posto; è cambiata solo "
         "l'estensione lungo il percorso."),
        ("Fallo prima di cancellare o cedere il vecchio telefono",
         "Il backup va creato mentre il vecchio telefono funziona ancora e ha ancora JW Library installato. Una volta che il dispositivo viene ripristinato, dato in permuta o passato ad altri, le note se ne vanno con lui: JW Library non conserva copie nel cloud dei dati di studio personale, e un backup del telefono come Google One o un backup del dispositivo iCloud spesso ripristina un'istantanea più vecchia dei dati dell'app, o nessuna. Crea prima il file .jwlibrary, mettilo al sicuro e verifica di vederlo prima di cancellare qualsiasi cosa."),
        ("Come far uscire il file dal vecchio telefono",
         "Su Android il file viene scritto nella cartella che scegli — di solito Download o Documenti — e puoi spostarlo con qualsiasi gestore di file, inviartelo per email o metterlo nel cloud. Su iPhone il menu di condivisione compare appena il backup è creato: salvalo in File, mandalo con AirDrop al telefono nuovo o inviatelo. Il metodo non conta e non può danneggiare il file: un .jwlibrary è un unico archivio che arriva integro o non arriva."),
        ("Perché un'app di trasferimento tra telefoni non basta",
         "Strumenti come Smart Switch, Trasferisci a iOS o un ripristino iCloud copiano app e dati di sistema, ma i database privati delle app vengono spesso saltati, ripristinati in parte o ripristinati da un momento precedente. Capita regolarmente di scoprire la lacuna settimane dopo, quando il vecchio telefono non c'è più. Tratta il file .jwlibrary come la copia che conta e il trasferimento del telefono come una comodità: se per caso porta le tue note, ripristinare il tuo backup sopra non costa nulla."),
        ("Verifica che il trasferimento sia riuscito",
         "Dopo il ripristino sul telefono nuovo, apri due o tre pubblicazioni che hai annotato di recente e conferma che note, colori delle evidenziazioni e segnalibri ci siano. Un controllo più rapido è aprire il file di backup nel browser prima di cancellare il vecchio dispositivo: vedi ogni nota, evidenziazione e segnalibro che contiene, quindi sai cosa dovrebbe comparire. Cancella il vecchio telefono solo dopo aver verificato il nuovo."),
        ("Se passi anche a un tablet o a un computer",
         "Lo stesso file va bene ovunque. Se stai configurando insieme un telefono nuovo e un tablet, ripristina su entrambi lo stesso file .jwlibrary e partiranno identici. Da lì torneranno a divergere in base a dove studi, quindi conviene decidere subito se li terrai uniti periodicamente o se ne tratterai uno come dispositivo principale."),
        ("Se il telefono nuovo ha già delle note",
         "Succede quando si usa il dispositivo nuovo per una settimana prima di occuparsi del trasferimento. Un ripristino diretto sostituirebbe quel lavoro con i dati del vecchio telefono. Fai prima il backup del telefono nuovo, uniscilo a quello del vecchio e ripristina il risultato: i due insiemi di note finiscono in un'unica biblioteca invece che uno sovrascriva l'altro."),
        ("Cosa fare quando il telefono nuovo è operativo",
         "Verifica prima di disfarti di qualcosa. Apri sul telefono nuovo alcune pubblicazioni annotate di recente e conferma che note, colori e segnalibri ci siano; solo allora cancella o cedi il vecchio dispositivo, in quest'ordine e mai al contrario. Una volta sistemato, metti un backup fuori dal telefono, perché la situazione che ti ha portato su questa pagina tornerà al prossimo cambio."),
    ],
    "faq": [
        ("Questo sposta anche le pubblicazioni scaricate?",
         "Il backup contiene i dati di studio personale — note, evidenziazioni, segnalibri, "
         "etichette e playlist. Le pubblicazioni si riscaricano semplicemente sul telefono "
         "nuovo."),
        ("Conta se i telefoni hanno versioni diverse di Android?",
         "No. Il formato .jwlibrary è lo stesso ovunque, anche tra versioni di Android e tra "
         "Android e iPhone."),
        ("Posso recuperare le note se il vecchio telefono non c'è più?",
         "Solo se esiste un file .jwlibrary da qualche parte: in File, Download, un'email che ti sei mandato o nel cloud. Senza di esso non c'è nulla da ripristinare, perché i dati di studio personale stanno soltanto sul dispositivo."),
        ("I due telefoni devono avere la stessa versione di JW Library?",
         "Non devono coincidere esattamente, ma aggiorna il telefono nuovo alla versione attuale prima di ripristinare. Un backup creato da una versione più recente può usare uno schema di database che un'app più vecchia non comprende."),
        ("Dovrò riscaricare le pubblicazioni?",
         "Di norma sì, perché i file multimediali delle pubblicazioni non fanno parte del backup. Le tue note si ricollegano a ogni pubblicazione appena viene scaricata, quindi nulla di ciò che hai scritto va perso nel frattempo."),
        ("Quanto tempo richiede in tutto?",
         "Pochi minuti. Creare il backup richiede secondi, spostare il file dipende dal metodo e il ripristino è rapido. La parte più lunga è riscaricare le pubblicazioni, e può avvenire in secondo piano."),
        ("Posso farlo senza Wi-Fi?",
         "Il trasferimento in sé sì, via AirDrop o cavo. Riscaricare le pubblicazioni sul dispositivo nuovo richiede una connessione."),
    ],
}

GUIDES_IT["jw-library-android-to-iphone"] = {
    "title": "Passare JW Library da Android a iPhone (senza perdere note)",
    "h1": "Passare JW Library da Android a iPhone o iPad — senza perdere una nota",
    "description": "Il formato di backup .jwlibrary è identico su Android e iOS. Come spostare "
                   "note, evidenziazioni e segnalibri tra piattaforme — e come unire se "
                   "entrambi i dispositivi hanno note.",
    "intro": [
        "Passare tra Android e iPhone sembra il caso difficile ed è quello facile. JW Library scrive lo stesso formato di backup su ogni piattaforma su cui gira, quindi portare una biblioteca di studio da Android a iOS è la stessa operazione che spostarla tra due telefoni Android: nessuna conversione, nessun formato di esportazione da scegliere, niente che si perda per strada.",
        "Cambiare piattaforma è il momento in cui si teme di perdere anni di note di studio: "
        "le app di trasferimento da Android a iPhone saltano del tutto i dati di JW Library. "
        "La buona notizia è che il formato di backup di JW Library è identico su Android, "
        "iPhone, iPad e Windows, quindi un cambio di piattaforma si riduce a un backup, un "
        "trasferimento di file e un ripristino.",
    ],
    "steps": [
        ("Fai il backup sul telefono Android",
         "JW Library → Studio personale → menu a tre punti → Backup e ripristino → Crea un "
         "backup. Salva il file .jwlibrary."),
        ("Manda il file su iPhone o iPad",
         "Email, Google Drive, iCloud Drive — qualunque cosa sposti un file. Se iOS lo "
         "rinomina in .zip lungo il percorso, rinominalo di nuovo in .jwlibrary."),
        ("Ripristina sul nuovo dispositivo",
         "Installa JW Library, accedi, poi Backup e ripristino → Ripristina e scegli il file. "
         "Note, evidenziazioni, segnalibri, etichette e playlist arrivano tutti."),
    ],
    "sections": [
        ("Se l'iPhone ha già delle note",
         "Il ripristino sostituisce i dati del dispositivo. Quando il nuovo dispositivo ha già "
         "note sue, fai il backup anche di quello e unisci prima i due backup in un unico "
         "file su jwsync.org — l'unione combina entrambe le biblioteche nel tuo browser, "
         "senza caricare nulla — poi ripristina il file unito. Non si perde nulla da nessuna "
         "delle due parti."),
        ("Gli stessi passi funzionano in ogni direzione",
         "Da iPhone ad Android, da Android ad Android, aggiungendo un iPad come secondo "
         "dispositivo di studio o passando all'app per Windows: il file di backup è la lingua "
         "comune fra tutti."),
        ("Perché il formato è identico sulle due piattaforme",
         "JW Library usa lo stesso formato di backup ovunque giri: Android, iOS, iPadOS e Windows. Un file .jwlibrary è uno ZIP che contiene un database SQLite con le stesse tabelle e lo stesso schema, indipendentemente dal dispositivo che lo ha scritto. Non c'è alcuna fase di conversione, nessun andirivieni tra esportazione e importazione, niente di specifico per piattaforma dentro il file. Un backup Android si ripristina su un iPhone esattamente come farebbe un backup iPhone."),
        ("L'unica parte che cambia davvero",
         "Non il file, solo il modo di metterci le mani sopra. Su Android il backup viene salvato in una cartella che scegli e si sposta con qualsiasi gestore di file. Su iPhone passa dal menu di condivisione verso File, AirDrop o quello che preferisci. L'attrito che si incontra cambiando piattaforma sta sempre in questo passaggio di gestione, mai nella compatibilità. Email, cloud o AirDrop funzionano allo stesso modo; l'archivio arriva integro o non arriva."),
        ("Colori delle evidenziazioni, etichette e risposte di studio",
         "Sopravvive tutto. I colori delle evidenziazioni sono memorizzati come indice numerico — giallo, verde, blu, rosa, arancione e viola — e appaiono uguali su ogni piattaforma. Le etichette e i collegamenti tra etichette e note passano, così come le risposte digitate nei campi delle domande di studio. Quello che vedi sull'iPhone dopo il ripristino è quello che avevi sul dispositivo Android."),
        ("Se iOS non ti lascia scegliere il file",
         "Salva prima il file nell'app File e selezionalo da lì, anziché da un allegato email o dall'anteprima di un'app di messaggistica. Alcune app consegnano a iOS una copia temporanea di anteprima invece del file vero, e JW Library non riesce ad aprirla. Se il file è arrivato come allegato, toccalo, scegli Salva su File e ripristina da lì."),
        ("Prepara l'iPhone prima di ripristinare",
         "Installa JW Library dall'App Store e aggiornala alla versione attuale prima di ripristinare qualsiasi cosa. Un backup scritto da una versione più recente può usare uno schema di database che una versione precedente non comprende, e il ripristino verrà semplicemente rifiutato. Non serve accedere ad alcun account: i dati di studio personale sono nel file che ripristini, non in un account."),
        ("Se hai già iniziato a studiare sull'iPhone",
         "Fai prima il backup dell'iPhone. Ripristinare il file Android sopra sostituirebbe tutto ciò che hai scritto dal cambio. Unire i due backup produce un file che contiene entrambi, che poi ripristini: la cronologia Android e le nuove note dell'iPhone finiscono nella stessa biblioteca."),
        ("Tenere in uso entrambi i telefoni",
         "C'è chi conserva il vecchio Android come secondo lettore anziché metterlo da parte. Funziona, ma i due divergeranno appena annoterai su entrambi, perché tra loro non c'è sincronizzazione. Se intendi usarli entrambi, metti in conto di unire periodicamente i loro backup anziché dare per scontato che restino allineati."),
        ("Dopo il passaggio",
         "Dai all'iPhone il tempo di riscaricare le pubblicazioni che usi di più, poi controlla qualcuna di quelle annotate per confermare che sia arrivato tutto: note, colori delle evidenziazioni, segnalibri ed etichette. Conserva il file di backup Android anche a passaggio concluso: è un'istantanea datata della tua biblioteca, e tenerla non costa nulla."),
    ],
    "faq": [
        ("Serve un computer per farlo?",
         "No. L'intero passaggio si può fare da telefono a telefono, con email o uno spazio "
         "cloud."),
        ("I colori delle mie evidenziazioni sopravvivono al passaggio?",
         "Sì — le evidenziazioni mantengono i colori, le note le etichette e i segnalibri il "
         "loro posto."),
        ("Mi serve un computer per farlo?",
         "No. AirDrop, l'email o una qualsiasi app di archiviazione cloud sposta il file direttamente tra i due telefoni."),
        ("Funziona anche al contrario, da iPhone ad Android?",
         "Sì, allo stesso modo. Gli stessi passaggi funzionano in ogni direzione, compresa l'app per Windows."),
        ("L'iPhone avrà bisogno delle stesse pubblicazioni scaricate?",
         "Sì, dato che i file multimediali delle pubblicazioni non fanno parte di un backup. Le note si ricollegano a ogni pubblicazione appena viene scaricata."),
        ("Devo tenere il telefono Android dopo?",
         "No, una volta verificato che le note siano sull'iPhone. Controlla qualche pubblicazione annotata prima di cancellare o cedere il vecchio dispositivo."),
        ("Il trasferimento funziona per le risposte alle domande di studio?",
         "Sì. Le risposte digitate fanno parte dei dati di studio personale e passano con tutto il resto."),
        ("C'è qualche rischio di perdere note nel passaggio?",
         "Non se conservi il backup Android. Il ripristino scrive sull'iPhone e non altera mai il file che legge, quindi l'originale resta intatto come riserva. Tienilo finché non hai confermato che l'iPhone ha tutto, e possibilmente anche dopo."),
        ("E se il telefono Android non crea il backup?",
         "Controlla prima lo spazio disponibile, perché l'app ha bisogno di posto per scrivere il file. Se è l'app stessa a non funzionare, aggiornarla o riavviare il dispositivo di solito risolve. I dati restano intatti mentre risolvi."),
    ],
}

GUIDES_IT["backup-jw-library"] = {
    "title": "Come fare il backup di JW Library nel modo giusto",
    "h1": "Come fare il backup di JW Library nel modo giusto",
    "description": "Una routine di backup da 30 secondi che protegge anni di note di studio, "
                   "evidenziazioni e segnalibri di JW Library — e l'errore comune che coglie "
                   "tanti di sorpresa.",
    "intro": [
        "Tutto ciò che hai contrassegnato in JW Library — ogni nota, ogni evidenziazione, ogni segnalibro ed etichetta — esiste in un solo posto: il dispositivo che hai in mano. Non c'è alcun account che ne conservi una copia né sincronizzazione automatica nel cloud. Un backup è l'unica cosa che separa una biblioteca di studio costruita in anni da un telefono perso, ripristinato o cambiato.",
        "Un backup fatto bene di JW Library richiede mezzo minuto e protegge anni di studio "
        "accumulato. Quasi tutte le storie di perdita di dati iniziano allo stesso modo: non "
        "esisteva un file .jwlibrary recente quando il telefono è stato perso, ripristinato o "
        "sostituito.",
    ],
    "steps": [
        ("Crea il backup",
         "Apri JW Library → Studio personale → menu a tre punti → Backup e ripristino → Crea "
         "un backup. Produce un file .jwlibrary con ogni nota, evidenziazione, segnalibro ed "
         "etichetta."),
        ("Conservalo fuori dal telefono",
         "Inviatelo per email, oppure salvalo su Google Drive, iCloud o OneDrive. Un backup "
         "che vive solo sul telefono sparisce insieme al telefono."),
        ("Ripetilo con regolarità",
         "Una volta al mese è un buon punto di partenza; prima di ogni cambio di dispositivo, "
         "ripristino o aggiornamento di sistema è indispensabile. Conserva le copie vecchie: i "
         "file sono piccoli, e un backup datato ha già salvato tante persone."),
    ],
    "sections": [
        ("L'errore comune: fidarsi del backup cloud del telefono",
         "Un backup dell'intero telefono (Google One, backup del dispositivo su iCloud) spesso "
         "ripristina una copia vecchia dei dati di JW Library — o nessuna. Il file .jwlibrary "
         "è l'unico backup che controlli davvero e che puoi portare da una piattaforma "
         "all'altra. Considera il backup del telefono un extra, non il piano."),
        ("Ti ritrovi con due backup diversi?",
         "Succede: un backup dal telefono, uno più vecchio dal tablet, ognuno con note "
         "proprie. Non devi mai scegliere fra i due — uniscili in un unico file completo su "
         "jwsync.org, gratis e in privato, direttamente nel browser."),
        ("Cosa contiene il file e cosa no",
         "Il backup conserva i tuoi dati di studio personale: note, evidenziazioni e i loro colori, segnalibri, etichette e le risposte che hai digitato nei campi delle domande di studio. Non conserva le pubblicazioni: né Bibbie, né riviste, né libri, né video, né audio. È per questo che un backup di anni di studio occupa solo pochi megabyte, ed è per questo che ripristinare su un dispositivo nuovo ti lascia a riscaricare pubblicazioni mentre ogni nota che hai scritto è già tornata al suo posto."),
        ("Quanti backup conservare",
         "Più di uno. Ciò che costa le note alle persone raramente è un file perso: è un backup buono sovrascritto da uno cattivo, o un ripristino eseguito sul dispositivo sbagliato. Poiché i file sono piccoli, non c'è motivo di cancellare i vecchi: conservali datati in una cartella nel cloud. Un backup di sei mesi fa non perde valore anche se ne hai di più recenti, perché tutto ciò che hai cancellato per errore da allora esiste ancora al suo interno."),
        ("Dove conservarli",
         "Ovunque tranne che soltanto sul dispositivo stesso. Una cartella su Drive, iCloud, Dropbox o OneDrive copre il caso che conta di più: il dispositivo perso, rubato, ripristinato o danneggiato. Mandarti il file per email funziona altrettanto bene e ha l'utile effetto di datarlo. Il file contiene le tue note di studio, quindi trattalo con la stessa cura di qualsiasi documento personale."),
        ("Verificare un backup prima di farci affidamento",
         "Un backup che non hai mai aperto è un'ipotesi, non una rete di sicurezza. Puoi aprire un file .jwlibrary nel browser e vedere esattamente quali note, evidenziazioni e segnalibri contiene: un controllo di trenta secondi che trasforma l'ipotesi in un fatto. Conta soprattutto subito prima di qualcosa di irreversibile: un ripristino di fabbrica, una permuta, una riparazione o un aggiornamento importante del sistema."),
        ("I momenti in cui vale la pena fare un backup",
         "Qualsiasi momento in cui il dispositivo cambia mani o stato: un aggiornamento di sistema, un ripristino di fabbrica, una riparazione o la sostituzione dello schermo, una permuta, o il passaggio del dispositivo a qualcun altro. Aggiungi la fine di qualsiasi cosa che detesteresti rifare: un congresso, un'assemblea, un periodo di preparazione di un discorso. I backup sono rapidi ed economici, quindi l'abitudine utile è legarli agli eventi anziché al calendario."),
        ("Un backup del telefono non è un backup di JW Library",
         "Google One, un backup del dispositivo iCloud o lo strumento di migrazione del produttore operano a livello di dispositivo e trattano i dati privati delle app in modo incoerente. Capita regolarmente di scoprire che un ripristino completo del telefono ha riportato app e impostazioni ma non le note di studio, o ha riportato una versione di settimane prima. Il file .jwlibrary è l'unica copia il cui contenuto controlli e puoi verificare: tratta il backup del telefono come un extra, non come il piano."),
        ("Trasformarlo in un'abitudine che regge",
         "La routine che regge davvero è quella agganciata a qualcosa che già fai: fare il backup quando finisci di preparare la settimana, o lo stesso giorno in cui sbrighi altre incombenze periodiche. Salva sempre nella stessa cartella così i file si accumulano in un posto solo, e lascia lì i vecchi. Una cartella di backup datati che risale ad anni è la forma più solida che questo possa assumere, e mantenerla richiede secondi a settimana."),
    ],
    "faq": [
        ("Quanto è grande un file di backup?",
         "Di solito pochi megabyte anche per biblioteche molto grandi — sta in un allegato "
         "email."),
        ("Creare un backup cambia qualcosa sul mio telefono?",
         "No. Scrive soltanto il file; la tua biblioteca resta intatta."),
        ("Il backup include le pubblicazioni che ho scaricato?",
         "No. Solo i dati di studio personale. Le pubblicazioni vengono riscaricate sul dispositivo nuovo e le tue note si ricollegano automaticamente."),
        ("Posso aprire un backup per vedere cosa contiene?",
         "Sì. Puoi aprire un file .jwlibrary nel browser e sfogliare tutte le note, le evidenziazioni e i segnalibri che contiene, senza installare nulla e senza che il file esca dal tuo dispositivo."),
        ("I backup scadono?",
         "No. Un file .jwlibrary resta ripristinabile a tempo indeterminato. Ripristina in una versione attuale di JW Library anziché in una vecchia, dato che l'app legge i formati di backup precedenti ma non quelli successivi."),
        ("Devo fare un backup prima di ogni adunanza?",
         "Non serve. Lega i backup agli eventi che potrebbero costarti dati — aggiornamenti, riparazioni, dispositivi nuovi — più un ritmo regolare proporzionato a quanto studio ti dispiacerebbe rifare."),
        ("Vale la pena conservare backup di anni fa?",
         "Sì. Sono piccoli, e tutto ciò che hai cancellato per errore da allora esiste ancora al loro interno."),
    ],
}

GUIDES_IT["jw-library-restore-replaced-notes"] = {
    "title": "Il ripristino di JW Library ha sostituito le tue note? Come recuperarle",
    "h1": "Il ripristino ha sostituito le tue note? Ecco come unire i due backup",
    "description": "Il ripristino di JW Library è una sostituzione totale, non un'unione: le "
                   "note scritte dopo la data del backup sembrano sparite. Se hai ancora "
                   "entrambi i file di backup, non hai perso niente. Ecco la soluzione.",
    "intro": [
        "È un momento terribile: ripristini un backup su un dispositivo che aveva già delle "
        "note, e il ripristino sostituisce tutto — le note scritte da quel backup in poi "
        "sembrano sparite. Succede perché Backup e ripristino di JW Library è una "
        "sostituzione totale, non un'unione.",
        "Il punto chiave: se il lavoro più recente esiste ancora in qualche file di backup, "
        "in realtà non hai perso nulla. La soluzione è unire i due backup invece di scegliere "
        "fra loro.",
    ],
    "steps": [
        ("Fermati — non ripristinare di nuovo",
         "Ogni ripristino sostituisce i dati attuali del dispositivo. Fermati prima che "
         "sparisca qualcos'altro."),
        ("Fai il backup del dispositivo com'è adesso",
         "Studio personale → Backup e ripristino → Crea un backup. Questo conserva lo stato "
         "attuale, qualunque cosa contenga."),
        ("Trova il backup con le note mancanti",
         "Il file .jwlibrary da cui hai ripristinato, o uno precedente — controlla email, "
         "Drive, iCloud e la cartella dei download."),
        ("Unisci i due file su jwsync.org",
         "Carica entrambi i backup. JW Sync unisce tutte le note, evidenziazioni, segnalibri "
         "ed etichette di entrambi in un nuovo file — nel browser, senza caricare nulla. Le "
         "versioni in conflitto della stessa nota vengono mostrate affiancate perché tu "
         "scelga."),
        ("Ripristina il file unito",
         "Backup e ripristino → Ripristina con il .jwlibrary unito. Entrambe le serie di note "
         "sono tornate sul dispositivo."),
    ],
    "sections": [
        ("E se non esiste un backup delle note più recenti?",
         "Se l'unica copia delle note recenti era sul dispositivo e un ripristino le ha già "
         "sovrascritte, JW Library non offre alcun annullamento. Ecco perché il passo 2 qui "
         "sopra — fare il backup dello stato attuale prima di ogni altra cosa — conta così "
         "tanto ogni volta che qualcosa sembra sbagliato. D'ora in avanti, la routine "
         "«prima unire» rende il problema strutturalmente impossibile."),
    ],
    "faq": [
        ("L'unione duplicherà le note presenti in entrambi i backup?",
         "No — gli elementi identici vengono rilevati e tenuti una volta sola. Solo le "
         "versioni davvero diverse della stessa nota vengono segnalate per la revisione."),
        ("Questo risolve un backup che non si ripristina affatto?",
         "Di solito quello è un danno al file, non una sovrascrittura — vedi più sotto la "
         "guida su come riparare un backup danneggiato."),
    ],
}

GUIDES_IT["fix-corrupted-jw-library-backup"] = {
    "title": "Riparare un backup di JW Library danneggiato che non si ripristina",
    "h1": "Riparare un backup di JW Library danneggiato con il Dottore della biblioteca",
    "description": "JW Library rifiuta il tuo file .jwlibrary? Il Dottore della biblioteca "
                   "analizza il backup nel tuo browser, ripara i problemi più comuni e "
                   "produce una copia pulita che si ripristina.",
    "intro": [
        "Un backup che non si ripristina non è necessariamente un backup che ha perso le tue note. La maggior parte dei file che vengono descritti come danneggiati è strutturalmente sana e viene rifiutata per un motivo risolvibile, oppure è stata rovinata nel trasferimento in un modo che una copia nuova risolve. Vale la pena passare in rassegna le cause prima di dare il file per perso.",
        "A volte JW Library rifiuta un file di backup: il ripristino fallisce, dà errore, o il "
        "file non si apre. Cause comuni: un download interrotto, uno spazio cloud che ha "
        "rovinato il file, un'estensione cambiata lungo il percorso, o incoerenze interne "
        "accumulate in anni d'uso.",
        "JW Sync include il Dottore della biblioteca, un controllo che analizza un file "
        ".jwlibrary e ripara i problemi più comuni — interamente nel tuo browser, senza che il "
        "file lasci mai il tuo dispositivo.",
    ],
    "steps": [
        ("Apri JW Sync e carica il file problematico",
         "Vai su jwsync.org e carica il file .jwlibrary che non si ripristina. (Se il file è "
         "arrivato rinominato in .zip, rinominalo prima in .jwlibrary — solo questo risolve "
         "molti casi.)"),
        ("Avvia l'analisi del Dottore della biblioteca",
         "Il Dottore esamina la struttura interna del backup ed elenca ciò che trova — dalle "
         "stranezze innocue ai danni veri — in parole semplici."),
        ("Applica le riparazioni",
         "Un tocco ripara ciò che è riparabile. Il Dottore non modifica mai il tuo file "
         "originale; produce una copia pulita, quindi l'originale resta intatto come rete di "
         "sicurezza."),
        ("Scarica e ripristina il file riparato",
         "Ripristina il .jwlibrary pulito con Backup e ripristino → Ripristina in JW Library."),
    ],
    "sections": [
        ("Il Dottore lavora anche a ogni unione",
         "Gli stessi controlli girano automaticamente nel motore di unione, quindi un backup "
         "unito viene sempre consegnato pulito — anche quando uno dei file di partenza aveva "
         "problemi di cui non sapevi nulla."),
        ("Quando un file è irrecuperabile",
         "Se il file è stato troncato al punto che i dati semplicemente non ci sono più, "
         "nessuno strumento può reinventarli. Il Dottore lo dirà onestamente invece di "
         "produrre un file dubbio — ed è il segnale per cercare una copia precedente in email, "
         "Drive o iCloud, il che spiega anche perché conviene conservare i backup vecchi."),
        ("Cosa significa di solito danneggiato",
         "In pratica raramente si tratta di dati rovinati. Le cause comuni sono un file troncato nel trasferimento — accorciato da un caricamento fallito o da un'app di messaggistica che lo ha compresso — oppure un archivio integro che contiene incoerenze interne che l'app rifiuta. Poiché un .jwlibrary è uno ZIP che avvolge un database SQLite, il problema può stare in entrambi gli strati, e richiedono soluzioni diverse: un file troncato non si può riparare e va recuperato di nuovo; un database incoerente di solito sì."),
        ("Cosa controlla davvero una scansione",
         "Una scansione verifica che l'archivio si apra, che userData.db sia un database SQLite leggibile che supera un controllo di integrità, che lo schema corrisponda a quanto JW Library si aspetta e che il manifest concordi con il database che descrive, incluso l'hash che l'app usa per confermare che il file non è stato alterato. Una discordanza tra manifest e database è uno dei motivi più comuni per cui un backup tecnicamente valido viene rifiutato al ripristino, ed è direttamente riparabile."),
        ("Le righe orfane sono di solito innocue",
         "La scansione di un backup reale segnalerà spesso righe che rimandano a qualcosa che non è più presente: un'evidenziazione che punta a una posizione di una pubblicazione che si è spostata, per esempio. Gli stessi backup di JW Library ne contengono abitualmente centinaia e si ripristinano senza protestare. Sono una normale conseguenza dell'aggiornamento delle pubblicazioni nel tempo, non un indizio di danno, e non serve eliminarle perché il file funzioni."),
        ("Salvare le note da un file che non si ripristina",
         "Anche quando un backup non può essere riparato abbastanza perché JW Library lo accetti, le note al suo interno restano spesso leggibili. Aprire il file nel browser ti permette di vedere e copiare il testo direttamente, e trasforma un file inutilizzabile in materiale di studio recuperato. Se hai un secondo backup più vecchio che si ripristina, il contenuto leggibile di quello danneggiato può essere riunito a esso anziché ridigitato."),
        ("Quando il ripristino fallisce senza un errore chiaro",
         "JW Library rifiuta spesso un file senza spiegare perché. Le cause più frequenti sono un manifest il cui hash non corrisponde più al database che descrive, un file troncato nel trasferimento, o un backup scritto da una versione dell'app più recente di quella in cui stai ripristinando. La prima è riparabile, la seconda richiede di recuperare di nuovo il file dalla fonte e la terza si risolve aggiornando l'app prima di ripristinare."),
        ("Evitarlo la prossima volta",
         "Quasi tutti i danni avvengono in transito. Sposta i backup come file e non tramite qualcosa che possa ricomprimerli, e preferisci cloud, AirDrop o un cavo alle app di messaggistica. Dopo il trasferimento, verifica che la dimensione corrisponda all'originale: un file sensibilmente più piccolo di quello inviato è stato troncato, e nessuna riparazione riporta byte mai arrivati."),
        ("Se non funziona nulla",
         "Un file che non si può riparare può comunque essere leggibile, e leggerlo spesso basta: il testo delle note si recupera direttamente anche quando JW Library rifiuta il file. Combina questo con un backup più vecchio che si ripristina e di solito ti ritrovi con la maggior parte della biblioteca intatta. Prima di dichiarare inutilizzabile un file, aprilo e guarda cosa contiene davvero."),
    ],
    "faq": [
        ("I miei dati vengono caricati per l'analisi?",
         "No. Analisi, riparazioni ed esportazione avvengono tutte in locale, nel browser."),
        ("Può recuperare note cancellate dentro JW Library?",
         "No — ripara la struttura del file. Le note cancellate nell'app prima che il backup "
         "fosse creato non sono nel file, quindi non c'è nulla da recuperare."),
        ("Riparare il file fa perdere delle note?",
         "Le riparazioni lavorano su una copia e riguardano problemi strutturali, non i contenuti. Il tuo file originale non viene mai modificato, quindi resta disponibile se vuoi ricominciare."),
        ("Perché il mio backup si è danneggiato?",
         "Il più delle volte il file è stato alterato in transito: inviato tramite un'app che lo ha compresso o troncato, o un caricamento non completato. Trasferirlo di nuovo dalla fonte di solito risolve."),
        ("Una scansione può recuperare note che ho cancellato dentro JW Library?",
         "No. Una volta cancellata nell'app e creato un nuovo backup, la nota non è più in quel file. Un backup precedente alla cancellazione la conterrà ancora."),
        ("La dimensione del file mi dice se è troncato?",
         "Spesso sì. Confrontala con l'originale, se ce l'hai ancora; una differenza marcata significa che il trasferimento non si è concluso."),
        ("Un backup che si apre nel browser si ripristinerà di sicuro?",
         "Non è una garanzia, ma è un segnale forte che archivio e database sono sani, il che esclude i guasti più comuni."),
    ],
}

GUIDES_IT["edit-jw-library-notes"] = {
    "title": "Vedere e modificare le note di JW Library nel browser",
    "h1": "Vedi, cerca e modifica le tue note di JW Library — Esplora studio",
    "description": "Apri qualsiasi backup .jwlibrary nel browser per sfogliare, cercare, "
                   "modificare, rietichettare, ricolorare e ripulire in blocco note, "
                   "evidenziazioni e segnalibri di JW Library. Niente viene caricato.",
    "intro": [
        "JW Library è fatto per prendere note, non per gestirne migliaia. Esplora studio apre "
        "qualsiasi backup .jwlibrary direttamente nel browser e lo trasforma in un gestore di "
        "biblioteca ricercabile e modificabile — note, evidenziazioni e segnalibri in un unico "
        "posto, senza caricare nulla da nessuna parte.",
    ],
    "steps": [
        ("Carica un backup",
         "Crea un backup in JW Library (Studio personale → Backup e ripristino → Crea un "
         "backup), poi apri jwsync.org e carica il file in Esplora studio."),
        ("Sfoglia e cerca in tutto",
         "Tre schede — Note, Evidenziazioni, Segnalibri — con ricerca a testo pieno e filtri "
         "per colore, etichetta e pubblicazione. Una scheda Risposte di studio mostra anche le "
         "risposte che hai scritto nelle pubblicazioni."),
        ("Modifica sul posto",
         "Apri una nota per modificarne titolo e contenuto con la formattazione (grassetto, "
         "corsivo, sottolineato, elenchi), cambiarne il colore di evidenziazione e aggiungere "
         "o togliere etichette. Segnalibri e colori delle evidenziazioni si modificano allo "
         "stesso modo."),
        ("Ripulisci in blocco",
         "Seleziona molte note insieme per rietichettarle, ricolorarle o eliminarle in gruppo "
         "— con annulla e ripristina completi, quindi una svista non è mai fatale. Puoi anche "
         "estrarre un intervallo di date di note in un nuovo backup, o copiare le note in "
         "Markdown."),
        ("Esporta la biblioteca modificata",
         "Scarica il .jwlibrary modificato e ripristinalo in JW Library. Le tue modifiche sono "
         "ora sul dispositivo."),
    ],
    "sections": [
        ("Perché modificare nel browser invece che nell'app?",
         "La scala. Rinominare un'etichetta su 300 note, ricolorare ogni evidenziazione gialla "
         "di una pubblicazione o cancellare anni di segnalibri superati qui sono minuti, "
         "nell'app sono ore di tocchi. Il file esportato è un backup standard, che JW Library "
         "ripristina come qualunque altro."),
    ],
    "faq": [
        ("Modificare tocca il mio backup originale?",
         "No — le modifiche avvengono su una copia nel browser e vengono salvate in un nuovo "
         "file esportato. L'originale resta com'era."),
        ("C'è un limite alla dimensione della biblioteca?",
         "Le biblioteche molto grandi vengono paginate perché la navigazione resti veloce; "
         "ricerca e filtri lavorano su tutto."),
    ],
}

GUIDES_IT["search-jw-library-notes"] = {
    "title": "Cercare le note di JW Library per significato — Chiedi alla tua biblioteca",
    "h1": "Chiedi alla tua biblioteca: cerca le tue note di JW Library per significato",
    "description": "Ricerca semantica per le tue note di JW Library: trova quella nota che "
                   "ricordi a metà descrivendola, anche senza rammentarne le parole esatte. "
                   "Sul dispositivo, funziona offline, privata.",
    "intro": [
        "Chi ha anni di note conosce il problema: ricordi di aver scritto sul sopportare le "
        "prove con gioia, ma nella nota la parola «perseveranza» non c'è, quindi la ricerca "
        "per parola chiave non trova nulla. Chiedi alla tua biblioteca cerca per significato: "
        "descrivi il pensiero, e riemergono le note più vicine, comunque siano formulate.",
        "Tutto gira sul tuo dispositivo: il modello linguistico viene scaricato una volta nel "
        "browser e poi funziona offline, con accelerazione WebGPU dove è disponibile. Le tue "
        "note non vengono mai inviate da nessuna parte.",
    ],
    "steps": [
        ("Carica un backup in Esplora studio",
         "Su jwsync.org, carica il file .jwlibrary e apri la scheda Chiedi."),
        ("Lascia che il modello si prepari una volta",
         "Al primo utilizzo il modello locale viene scaricato e indicizza le tue note. Succede "
         "una volta sola; dopo funziona all'istante, anche offline."),
        ("Chiedi con parole tue",
         "Scrivi quello che ricordi — «quella nota sulla pazienza con i nuovi nel ministero», "
         "«incoraggiamento per pionieri scoraggiati» — e compaiono le note più vicine, "
         "ordinate per significato."),
    ],
    "sections": [
        ("In cosa è diversa dalla ricerca normale",
         "La ricerca per parola chiave confronta lettere; quella semantica confronta idee. Una "
         "domanda sull'«ansia» trova anche note scritte con «preoccupazione», «ansietà della "
         "vita» o la citazione di una scrittura sul tema. In Esplora studio ci sono entrambi i "
         "tipi di ricerca: si completano a vicenda."),
        ("Privata per progetto",
         "Non è un servizio di IA nel cloud. Il modello gira dentro la scheda del tuo browser, "
         "l'indice sta sul tuo dispositivo, e chiudere la scheda chiude tutto. Nulla delle tue "
         "note lascia mai la tua macchina."),
    ],
    "faq": [
        ("Serve un dispositivo potente?",
         "Un telefono o un portatile recente se la cava bene; sui dispositivi con WebGPU è più "
         "veloce. Ci sono più dimensioni di modello, per adattarsi al tuo hardware."),
        ("Funziona nella mia lingua?",
         "Sì — la ricerca funziona nelle lingue in cui sono scritte le tue note, e l'interfaccia "
         "è tradotta in tutte le 12 lingue supportate da JW Sync."),
    ],
}

GUIDES_IT["jw-library-study-stats"] = {
    "title": "Le tue statistiche di studio di JW Library: serie, mappe e riconoscimenti",
    "h1": "Le tue statistiche di studio: serie, mappe di calore, copertura e riconoscimenti",
    "description": "Trasforma un backup di JW Library in analisi di studio private — totali, "
                   "mappa di calore delle attività, serie, copertura della Bibbia sui 66 "
                   "libri, un profilo di studio e circa 200 riconoscimenti.",
    "intro": [
        "Il tuo file di backup registra in silenzio anni di storia di studio: quando prendi "
        "note, cosa evidenzi, quali libri hai percorso. La pagina Statistiche di studio legge "
        "un backup .jwlibrary e trasforma quella storia in un pannello privato, calcolato "
        "interamente nel tuo browser.",
    ],
    "steps": [
        ("Crea un backup",
         "In JW Library: Studio personale → Backup e ripristino → Crea un backup."),
        ("Apri la pagina Statistiche di studio",
         "Vai su jwsync.org/highlights.html e carica il file."),
        ("Esplora la tua storia di studio",
         "I totali principali, le viste Anno di servizio e Da sempre, la crescita anno su "
         "anno — e poi, più in basso, le parti divertenti."),
    ],
    "sections": [
        ("Cosa vedrai",
         "Una mappa di calore delle attività con la serie più lunga e quella in corso; il "
         "ritmo settimanale, le ore e i mesi più intensi; la copertura della Bibbia su tutti i "
         "66 libri con la divisione fra Scritture Ebraiche e Greche; una ruota dei colori "
         "delle evidenziazioni, un istogramma della profondità delle note e una nuvola di "
         "parole; un orologio dello studio su 24 ore e un radar della stagionalità."),
        ("Profilo, percorso e riconoscimenti",
         "Un Profilo di studio a sei tratti (Costanza, Diligenza, Profondità, Ampiezza, "
         "Riflessione, Stabilità) con una «Firma di studio»; un Percorso di studio di 60 "
         "livelli su 12 fasce con nome; e circa 200 riconoscimenti, da Comune a Leggendario, "
         "comprese medaglie legate al contenuto. Una Scheda condivisibile riassume il tuo anno "
         "senza esporre una sola nota."),
        ("Un motivo quotidiano per tornare",
         "Il pannello Riemergi mostra le note che hai scritto in questo stesso giorno negli "
         "anni passati e costruisce un ripasso dilazionato e leggero — poco, ma spesso: è così "
         "che lo studio resta."),
    ],
    "faq": [
        ("Viene caricato qualcosa?",
         "No. Il backup viene analizzato nel tuo browser; le statistiche non lasciano mai il "
         "tuo dispositivo."),
        ("Le statistiche si aggiornano da sole?",
         "Riflettono il backup che carichi — crea un backup nuovo per vedere statistiche "
         "nuove."),
    ],
}

GUIDES_IT["share-jw-library-notes"] = {
    "title": "Come condividere le note di JW Library con un amico",
    "h1": "Come condividere le note di JW Library con un amico — senza server",
    "description": "Manda a un amico note scelte di JW Library (con le loro evidenziazioni) in "
                   "un piccolo file — niente server, niente account. Chi le riceve le "
                   "aggiunge senza sovrascrivere le proprie.",
    "intro": [
        "JW Library non offre alcun modo di dare a un'altra persona una copia di note "
        "specifiche. Mandare l'intero backup funzionerebbe, ma consegna tutto, e ripristinarlo "
        "cancellerebbe la biblioteca di chi lo riceve. La condivisione di note di JW Sync "
        "risolve entrambi i problemi: scegli esattamente quali note condividere, e chi le "
        "riceve le aggiunge senza perdere nulla.",
    ],
    "steps": [
        ("Scegli le note da condividere",
         "Nella pagina di condivisione, su jwsync.org/share.html, carica il tuo backup e "
         "seleziona le note — alcune di un discorso, oppure tutto ciò che sta sotto "
         "un'etichetta con un clic, usando il filtro per etichetta del selettore. Le "
         "evidenziazioni legate a quelle note viaggiano con loro."),
        ("Manda il file di condivisione",
         "JW Sync produce un piccolo file contenente solo le note selezionate. Mandalo con il "
         "canale che preferisci — app di messaggi, email, AirDrop. Non c'è server né account; "
         "il file è tutto lo scambio."),
        ("Chi lo riceve lo aggiunge",
         "Il tuo amico apre la stessa pagina, carica il file di condivisione insieme al "
         "proprio backup e ottiene un nuovo backup con le tue note aggiunte. Le sue note non "
         "vengono mai sovrascritte — se una nota condivisa entra in conflitto con una sua, "
         "sceglie lui come aggiungerla — e le note importate arrivano etichettate, quindi sono "
         "facili da trovare, rileggere o togliere in seguito."),
    ],
    "sections": [
        ("Buoni usi",
         "Passare una ricerca a un compagno di studio, condividere le note di un'adunanza con "
         "chi era assente, dare a un nuovo proclamatore una prima serie di note su una "
         "pubblicazione, o passare le note di un progetto specifico a un familiare — tutto "
         "senza esporre il resto di nessuna delle due biblioteche."),
    ],
    "faq": [
        ("Chi riceve deve installare JW Sync?",
         "Non si installa nulla da nessuna delle due parti — è una pagina web. A chi riceve "
         "servono solo il file di condivisione e il proprio backup."),
        ("Posso annullare la condivisione o far scadere il file?",
         "Il file è un file qualunque che hai mandato: non c'è una copia su server da far "
         "scadere. Condividi solo ciò che condivideresti in un messaggio."),
    ],
}

GUIDES_IT["bible-reading-plan"] = {
    "title": "Un piano di lettura biblica quotidiano con le tue note accanto",
    "h1": "Compagno di lettura: un piano di lettura biblica con le tue note accanto",
    "description": "Un programma quotidiano e privato di lettura della Bibbia che mostra le "
                   "note e le evidenziazioni fatte sui capitoli di oggi. Scegli il ritmo, "
                   "mantieni una serie, guarda riempirsi la griglia dei 66 libri.",
    "intro": [
        "Di piani di lettura biblica ce ne sono tanti. Il Compagno di lettura fa una cosa che "
        "nessun altro può fare: siccome legge il tuo backup .jwlibrary, la lettura di oggi "
        "arriva con le note e le evidenziazioni che tu stesso hai fatto proprio su quei "
        "capitoli — «hai evidenziato quattro versetti nel Salmo 37 due anni fa». Leggere "
        "attraverso la lente della tua storia di studio, tutto sul tuo dispositivo.",
    ],
    "steps": [
        ("Scegli un ordine e un ritmo",
         "Leggi nell'ordine biblico o in ordine all'incirca cronologico; finisci in 3 mesi, 6 "
         "mesi, 1 anno, 2 anni, oppure imposta il tuo ritmo di capitoli al giorno — con "
         "un'anteprima in tempo reale del «finiresti verso…»."),
        ("Leggi la porzione di oggi",
         "Ogni capitolo è a un tocco di distanza e si apre direttamente in JW Library o nella "
         "BIBLIOTECA ONLINE Watchtower, nella tua lingua. Spunta i capitoli man mano."),
        ("Porta con te le tue note (facoltativo)",
         "Carica un backup in un qualsiasi strumento di JW Sync e le tue note e il numero di "
         "evidenziazioni compaiono subito sotto i capitoli di oggi."),
        ("Guarda crescere i progressi",
         "Una griglia dei 66 libri si riempie mentre leggi, con una barra dei capitoli letti, "
         "una previsione di ritmo e traguardi per il completamento di ogni libro, delle "
         "Scritture Ebraico-Aramaiche, delle Scritture Greche — e dell'intera Bibbia."),
    ],
    "sections": [
        ("Serie senza sensi di colpa",
         "Completare un giorno fa crescere la serie; saltarne uno sposta soltanto la data "
         "prevista di fine. Non c'è nessun arretrato da smaltire — il piano si adatta alla tua "
         "vita invece di rimproverarti."),
    ],
    "faq": [
        ("Devo caricare un backup per usarlo?",
         "No — piano, serie e progressi funzionano da soli. Il backup aggiunge soltanto le tue "
         "note personali alla lettura di ogni giorno."),
        ("I miei progressi di lettura sono privati?",
         "Sì. I progressi restano nel browser, sul tuo dispositivo — non c'è account e non "
         "viene caricato nulla."),
    ],
}

GUIDES_IT["open-jwlibrary-file"] = {
    "title": "Cos'è un file .jwlibrary e come si apre?",
    "h1": "Cos'è un file .jwlibrary — e come aprirne uno su qualsiasi dispositivo",
    "description": "Un file .jwlibrary è il tuo backup di JW Library: un unico file con ogni "
                   "nota, evidenziazione, segnalibro ed etichetta. Ecco cosa contiene e come "
                   "aprirlo e leggerlo.",
    "intro": [
        "Un file .jwlibrary sembra opaco, e non lo è. È un normale archivio ZIP attorno a un normale database SQLite, il che significa che puoi leggere il tuo backup — vedere esattamente quali note, evidenziazioni e segnalibri contiene — senza JW Library e senza installare assolutamente nulla.",
        "Quando fai il backup di JW Library ottieni un file che termina in .jwlibrary. È un "
        "pacchetto unico e portatile che contiene tutto il tuo studio personale — note, "
        "evidenziazioni, segnalibri, etichette e playlist — in un database compatto. Non è un "
        "documento da aprire in Word o in un lettore PDF; è pensato per essere ripristinato "
        "dentro JW Library.",
        "Ma non devi ripristinarlo solo per dare un'occhiata dentro. JW Sync apre un file "
        ".jwlibrary direttamente nel tuo browser, così puoi leggerne, cercarne e modificarne il "
        "contenuto senza toccare il telefono.",
    ],
    "steps": [
        ("Procurati un file .jwlibrary",
         "Si crea in JW Library: Studio personale → menu a tre punti → Backup e ripristino → "
         "Crea un backup. È di quel file che stiamo parlando."),
        ("Aprilo in JW Sync",
         "Vai su jwsync.org e carica il file in Esplora studio. Si apre all'istante, sul tuo "
         "dispositivo — non viene caricato nulla."),
        ("Leggilo e lavoraci",
         "Sfoglia note, evidenziazioni e segnalibri; cerca in tutto; modifica, rietichetta o "
         "esporta. Quando hai finito puoi ripristinare il file (o una copia modificata) dentro "
         "JW Library."),
    ],
    "sections": [
        ("Cosa c'è davvero dentro il file",
         "Tecnicamente un file .jwlibrary è un database SQLite compresso più un manifesto. È "
         "per questo che a volte viene rinominato in .zip per sbaglio lungo il percorso — e "
         "per questo rinominarlo in .jwlibrary risolve. Non ti serve sapere nulla di tutto ciò "
         "per usarlo, ma spiega perché il file è piccolo, autosufficiente e identico su "
         "Android, iPhone, iPad e Windows."),
        ("Aprirlo sul computer",
         "La stessa pagina jwsync.org funziona nel browser di un portatile o di un fisso — "
         "comodo per leggere anni di note su uno schermo grande, o per fare pulizie in blocco "
         "che sul telefono sarebbero noiose. Non c'è nulla da installare."),
        ("Cos'è davvero il file",
         "Un file .jwlibrary è un archivio ZIP con un'estensione diversa. Al suo interno ci sono userData.db — un database SQLite con le tue note, evidenziazioni, segnalibri ed etichette — e manifest.json, un piccolo file che descrive il backup e include un hash del database che JW Library usa per confermare che il file non è stato alterato. Nulla di tutto ciò è proprietario o cifrato: è un archivio standard attorno a un database standard."),
        ("Aprirlo senza JW Library",
         "Non ti serve l'app, né alcun software, per leggere il tuo backup. Aprire il file nel browser mostra tutte le note, le evidenziazioni e i segnalibri che contiene, con ricerca e filtri, e il file non lascia mai il tuo dispositivo: viene letto in locale anziché caricato. È il modo più rapido per confermare che un backup contiene ciò che pensi prima di un ripristino di fabbrica, una permuta o un ripristino su un telefono nuovo."),
        ("Guardarci dentro manualmente",
         "Se sei curioso, copia il file, rinomina la copia in .zip e aprila con un qualsiasi strumento di archiviazione. Vedrai userData.db e manifest.json. Aprire il database richiede un visualizzatore SQLite, e le tabelle prendono il nome da ciò che contengono: Note, UserMark, Bookmark, Tag. Lavora sempre su una copia: modificare il database a mano senza aggiornare l'hash del manifest produce un file che JW Library rifiuterà di ripristinare."),
        ("Modificare in sicurezza",
         "Le note si possono correggere, rietichettare, ricolorare o eliminare fuori dall'app, e il risultato esportare come nuovo file .jwlibrary che ripristini normalmente. La regola che rende tutto ciò sicuro è conservare l'originale: modifica una copia, ripristina il file modificato e, se qualcosa non è come ti aspettavi, l'originale intatto è ancora lì a cui tornare."),
        ("Leggere un backup sul telefono",
         "Non serve un computer. Aprire il file in un browser mobile funziona allo stesso modo, il che è utile quando il backup è già sul telefono e vuoi confermarne il contenuto prima di ripristinare o prima di cancellare il dispositivo. Il file viene letto in locale, quindi funziona senza altra connessione che quella per caricare la pagina."),
        ("Perché l'hash del manifest conta",
         "manifest.json registra un hash di userData.db. JW Library lo usa per confermare che il database non è stato alterato da quando il backup è stato scritto, quindi un file il cui database è stato modificato senza ricalcolare l'hash viene rifiutato al ripristino. È il motivo più comune per cui un backup modificato a mano smette di funzionare, e la ragione per cui modificarlo con uno strumento che riscrive il manifest è più sicuro che mettere mano al database direttamente."),
        ("A cosa serve tutto questo",
         "Poter leggere un backup cambia quanto vale un backup. Puoi confermare che un file contiene ciò che pensi prima di cancellare un telefono, verificare se vale la pena ripristinare un vecchio file, trovare una nota che sai di aver scritto senza frugare nell'app, o recuperare testo da un file che JW Library non accetta. Nulla di ciò richiede di affidare il file a qualcuno: viene letto sul tuo dispositivo."),
    ],
    "faq": [
        ("Posso aprire un file .jwlibrary in Excel o nel Blocco note?",
         "Non in modo utile — è un database, non un foglio di calcolo né un file di testo. "
         "Aprilo in JW Sync per leggerlo, o esporta le note in Markdown/testo da Esplora "
         "studio."),
        ("È sicuro aprire il mio backup nel browser?",
         "Sì. JW Sync legge il file in locale, nella scheda del tuo browser; non viene inviato "
         "nulla a un server e il tuo file originale non viene mai modificato."),
        ("Posso semplicemente rinominarlo in .zip?",
         "Sì, su una copia. Rinominarlo non altera il contenuto e permette a qualsiasi strumento di archiviazione di mostrarti cosa c'è dentro."),
        ("Aprire il file lo modifica?",
         "No. Leggere un backup — nel browser o in uno strumento di archiviazione — lo lascia identico byte per byte. Solo salvare o esportare produce un file nuovo."),
        ("Devo essere online?",
         "Solo per caricare la pagina. Il file viene letto sul tuo dispositivo e non caricato, quindi le tue note non viaggiano mai in rete."),
        ("Posso aprire un backup che mi ha mandato qualcun altro?",
         "Sì, il formato non è legato a un dispositivo o a un account. Se convenga ripristinarlo è un'altra questione, dato che un ripristino sostituisce la tua biblioteca."),
        ("Devo installare qualcosa per guardarci dentro?",
         "No. Un browser basta per leggere le note; solo l'ispezione manuale del database richiede un visualizzatore SQLite."),
    ],
}

GUIDES_IT["jw-library-windows-pc"] = {
    "title": "Fare backup e unire JW Library su un PC Windows",
    "h1": "Usare i backup di JW Library su un PC Windows",
    "description": "Come fare il backup di JW Library su Windows, e come unire il backup del PC "
                   "con quelli di telefono e tablet perché note, evidenziazioni e segnalibri "
                   "restino insieme su ogni dispositivo.",
    "intro": [
        "JW Library gira su Windows come su telefoni e tablet, e produce lo stesso file di "
        "backup .jwlibrary. Vuol dire che il tuo PC può far parte della stessa biblioteca di "
        "studio del telefono — a patto di unire i backup invece di ripristinarne uno sopra "
        "l'altro.",
    ],
    "steps": [
        ("Fai il backup su Windows",
         "Nell'app JW Library per Windows apri il menu, vai su Backup e ripristino e crea un "
         "backup. Salva il file .jwlibrary in un posto facile da ritrovare."),
        ("Fai il backup anche di telefono e tablet",
         "Su ogni dispositivo: Studio personale → menu a tre punti → Backup e ripristino → "
         "Crea un backup."),
        ("Uniscili su jwsync.org",
         "Apri jwsync.org in un qualsiasi browser del PC e carica tutti i file di backup. JW "
         "Sync unisce note, evidenziazioni, segnalibri ed etichette di ogni dispositivo in un "
         "unico file .jwlibrary — in locale, senza caricare nulla."),
        ("Ripristina ovunque il file unito",
         "Ripristina il file unito nell'app di Windows e su ogni dispositivo mobile. Ora PC, "
         "telefono e tablet portano tutti la biblioteca completa."),
    ],
    "sections": [
        ("Perché il PC è il posto più comodo per farlo",
         "Un browser da scrivania rende molto più rapido caricare più file, controllare "
         "l'anteprima dell'unione e salvare il risultato rispetto ai tocchi sul telefono. "
         "Molti tengono la routine principale di unione sul computer e si limitano a "
         "ripristinare il file unito sui dispositivi mobili."),
    ],
    "faq": [
        ("Il backup di Windows funziona con quelli di iPhone e Android?",
         "Sì — il formato .jwlibrary è identico su tutte le piattaforme, quindi un backup di "
         "Windows si unisce liberamente a quelli di telefono e tablet."),
        ("Devo installare qualcosa sul PC?",
         "No. JW Sync è una pagina web; funziona in Edge, Chrome o Firefox, senza "
         "installazioni."),
    ],
}

GUIDES_IT["recover-jw-library-notes-lost-phone"] = {
    "title": "Come recuperare le note di JW Library dopo un telefono perso o rotto",
    "h1": "Recuperare le note di JW Library da un telefono perso, rotto o ripristinato",
    "description": "Hai perso il telefono o l'hai ripristinato con dentro le note di JW "
                   "Library? Quello che puoi recuperare dipende dai tuoi backup. Ecco "
                   "esattamente come riaverle — e come fare la prossima volta.",
    "intro": [
        "Quando un telefono viene perso, rubato o danneggiato irreparabilmente, la sopravvivenza delle tue note di JW Library dipende da una sola domanda: esiste un backup .jwlibrary da qualche parte fuori da quel dispositivo? Se esiste, tutto ciò che contiene torna. Questa pagina spiega come trovarne uno, come ripristinarlo su qualsiasi dispositivo sostitutivo e cosa fare quando l'unico backup che hai è vecchio.",
        "Perdere un telefono è già abbastanza stressante senza il timore di aver perso anche "
        "anni di note di studio. Se potrai recuperarle dipende da una sola domanda: esiste un "
        "backup .jwlibrary da qualche parte fuori da quel telefono?",
        "Questa guida ti accompagna a trovare qualunque backup tu possa avere — anche quelli "
        "che hai dimenticato di aver fatto — e a trasformarlo di nuovo in una biblioteca JW "
        "Library completa sul dispositivo nuovo.",
    ],
    "steps": [
        ("Cerca in ogni posto dove potrebbe esserci un backup",
         "Controlla le email (cerca «jwlibrary» o «backup»), Google Drive, iCloud Drive, "
         "OneDrive, Dropbox e la cartella Download del computer. I backup sono file piccoli, "
         "facili da dimenticare."),
        ("Controlla gli altri dispositivi",
         "Se hai mai usato JW Library su un tablet o un PC, quello ha dati di studio propri: "
         "creane subito un backup per conservare quello che contiene."),
        ("Ripristina quello che trovi sul telefono nuovo",
         "Installa JW Library sul dispositivo nuovo, poi Backup e ripristino → Ripristina, e "
         "carica il file .jwlibrary. Note, evidenziazioni e segnalibri tornano."),
        ("Unisci se trovi più di un backup",
         "Dispositivi o date diverse possono contenere ciascuno note uniche. Non sceglierne "
         "uno solo — caricali tutti su jwsync.org, uniscili in un unico file completo e "
         "ripristina quello. Non resta indietro nulla."),
    ],
    "sections": [
        ("Se non esiste alcun backup",
         "Sii sincero con te stesso fin da subito: se l'unica copia delle tue note viveva sul "
         "telefono perso e non hai mai esportato un backup, JW Library non conserva alcuna "
         "copia nel cloud da cui ripristinare. Fa male — ed è esattamente per questo che "
         "l'abitudine qui sotto conta così tanto."),
        ("Per non ritrovarti mai più qui",
         "Imposta un promemoria mensile di backup e conserva ogni file .jwlibrary fuori dal "
         "telefono (mandartelo per email basta). JW Sync può perfino ricordartelo e unire i "
         "tuoi dispositivi con regolarità. Un file che vive nella tua casella di posta "
         "sopravvive a qualunque telefono."),
        ("Dove potrebbe già esistere un backup",
         "Prima di concludere che non ce n'è nessuno, controlla ogni posto in cui un file potrebbe essere stato salvato: le cartelle Download e Documenti di qualsiasi computer a cui hai collegato il telefono, la posta inviata, le app di messaggistica con cui potresti averlo mandato e ogni account cloud che usi. Capita spesso di aver creato un backup una volta, mesi fa, e averlo dimenticato — e un backup di mesi fa contiene ancora la stragrande maggioranza di una biblioteca di studio."),
        ("Ripristinare su un telefono o una piattaforma diversi",
         "Il dispositivo sostitutivo non deve corrispondere a quello perso. Un backup di un telefono Android si ripristina su un iPhone e viceversa, perché il formato è identico su Android, iOS, iPadOS e Windows. Installa JW Library sul dispositivo nuovo, aggiornala alla versione attuale, poi ripristina da Studio personale → Backup e ripristino."),
        ("Se hai solo un backup vecchio o parziale",
         "Ripristinalo comunque. Recuperare la maggior parte delle tue note non è un premio di consolazione: è il risultato. Se in seguito trovi un secondo backup diverso, i due possono essere uniti in un file che contiene tutto di entrambi, quindi ripristinare ora il più vecchio non ti impedisce di aggiungerci dopo."),
        ("Cosa non si può recuperare",
         "Se non esiste alcun backup in nessuna forma, i dati di studio personale non possono essere recuperati. Sono conservati soltanto nell'archiviazione privata dell'app sul dispositivo, e né JW Library né un backup cloud a livello di telefono li preservano in modo affidabile. Vale la pena dirlo chiaramente, perché è il motivo per cui la routine di questo sito esiste."),
        ("Controlla prima di cancellare il dispositivo da remoto",
         "Se il telefono è perso e non distrutto, e stai valutando una cancellazione remota, cerca prima i backup esistenti: la cancellazione è irreversibile e toglie l'ultima possibilità che qualcuno ne crei uno. Se il dispositivo è solo smarrito e ancora raggiungibile, creare un backup da remoto non è possibile, ma i dati restano intatti finché non viene cancellato o ripristinato."),
        ("Fare in modo che non succeda due volte",
         "Il motivo per cui un telefono perso costa anni di studio è che l'unica copia stava sul telefono. Dopo aver ripristinato su un dispositivo sostitutivo, metti un backup fuori dal dispositivo lo stesso giorno, e ripetilo con un ritmo che manterrai davvero. I file sono abbastanza piccoli da conservarli tutti a tempo indeterminato senza costi."),
        ("Se davvero non c'è alcun backup",
         "Allora la risposta onesta è che le note non si possono recuperare, ed è meglio sentirselo dire che continuare a cercare. Quello che puoi fare è rendere questa l'ultima perdita: installa JW Library sul sostituto e, prima di aver ricostruito qualcosa che ti dispiacerebbe perdere, crea un backup e mettilo fuori dal dispositivo. Da lì in poi lo stesso evento non ti costa nulla."),
    ],
    "faq": [
        ("JW Sync può recuperare note da un telefono che non ho più?",
         "Nessuno strumento può — il recupero dipende dall'esistenza di un file di backup da "
         "qualche parte. Il compito di JW Sync è leggere, riparare e unire i backup che hai."),
        ("Il mio backup è vecchio — vale ancora la pena ripristinarlo?",
         "Assolutamente. Un backup vecchio con la maggior parte delle tue note batte "
         "ripartire da zero, e potrai unirlo in seguito a qualunque cosa di più recente "
         "troverai."),
        ("JW Library conserva una copia delle mie note nel cloud?",
         "No. I dati di studio personale restano sul dispositivo a meno che tu non crei tu stesso un file di backup."),
        ("Si possono recuperare le note da un telefono con lo schermo rotto?",
         "A volte: se il telefono si accende ancora e si può comandare, o se un centro assistenza riesce a pilotare il display, JW Library può ancora creare un backup. I dati sono intatti finché lo è la memoria."),
        ("Un vecchio backup si ripristina ancora nell'app attuale?",
         "Sì. JW Library legge i formati di backup precedenti. Aggiorna prima l'app e ripristina nella versione attuale."),
        ("Ho trovato due vecchi backup — quale uso?",
         "Nessuno da solo: uniscili. Il risultato contiene tutto di entrambi, incluso ciò che stava nel più vecchio ed era già stato cancellato all'epoca del più recente."),
        ("Posso vedere cosa contiene un backup prima di ripristinarlo?",
         "Sì. Apri il file nel browser e sfoglia prima le sue note, evidenziazioni e segnalibri, così sai cosa stai per ripristinare."),
    ],
}

GUIDES_IT["handle-merge-conflicts"] = {
    "title": "Stessa nota modificata su due dispositivi? Gestire i conflitti di unione",
    "h1": "Gestire i conflitti di unione: la stessa nota modificata su due dispositivi",
    "description": "Quando modifichi la stessa nota di JW Library in modo diverso su due "
                   "dispositivi, l'unione deve scegliere. Il Revisore dei conflitti mostra "
                   "entrambe le versioni affiancate perché decida tu — non si perde nulla.",
    "intro": [
        "Gran parte dell'unione non richiede sforzo: le note presenti su un solo dispositivo "
        "si combinano da sole. L'unico caso che richiede una decisione è un conflitto vero: la "
        "stessa nota, modificata in modo diverso su due dispositivi, così che i due backup non "
        "concordano su cosa debba dire. JW Sync non tira mai a indovinare in silenzio: la "
        "scelta la passa a te.",
    ],
    "steps": [
        ("Carica entrambi i backup",
         "Su jwsync.org, carica i file .jwlibrary dei due dispositivi. JW Sync li confronta "
         "mentre unisce."),
        ("Apri il Revisore dei conflitti",
         "Se ci sono note in conflitto, il revisore le elenca. Tutto ciò che non era in "
         "conflitto è già unito — questo passo riguarda solo gli scontri veri."),
        ("Confronta affiancato",
         "Ogni conflitto mostra entrambe le versioni con le differenze evidenziate parola per "
         "parola. «Suggerisci la migliore» può scegliere per te la versione più completa, "
         "oppure scegli tu quale tenere — nota per nota."),
        ("Concludi e ripristina",
         "Risolti tutti i conflitti, scarica il file unito e ripristinalo. Ora i due "
         "dispositivi concordano, con la versione di ogni nota che hai scelto tu."),
    ],
    "sections": [
        ("Perché è meglio che tenere semplicemente la più recente",
         "«Vince la più recente» cancella in silenzio modifiche che magari volevi tenere. "
         "Forse la versione vecchia aveva un paragrafo che sull'altro dispositivo hai tolto "
         "per sbaglio. Vederle entrambe, parola per parola, significa non perdere mai testo "
         "senza saperlo — che è tutto il senso dell'unire invece di sovrascrivere."),
        ("Come nascono i conflitti",
         "Di solito dal modificare offline su due dispositivi fra un'unione e l'altra, o dal "
         "ripristinare un backup vecchio e poi aggiungerci sopra. Unire con regolarità tiene "
         "basso il numero di conflitti e fresche le differenze nella memoria."),
    ],
    "faq": [
        ("Dovrò rivedere centinaia di conflitti?",
         "Raramente. Vanno in conflitto solo le note modificate in modo diverso da entrambe le "
         "parti; le note nuove e quelle cambiate su un solo dispositivo si uniscono da sole. "
         "La maggior parte delle unioni ha una manciata di conflitti o nessuno."),
        ("Posso cambiare idea dopo aver scelto?",
         "Sì — non viene scritto nulla su un dispositivo finché non ripristini il file unito, "
         "e i tuoi backup originali non vengono mai modificati: puoi rifare l'unione."),
    ],
}

GUIDES_IT["export-jw-library-notes"] = {
    "title": "Come esportare le note di JW Library in testo o Markdown",
    "h1": "Esportare le tue note di JW Library in testo, Markdown o un nuovo backup",
    "description": "Tira fuori le tue note di JW Library dall'app: copiale o esportale in "
                   "Markdown/testo semplice per usarle ovunque, oppure estrai una selezione in "
                   "un nuovo backup .jwlibrary. Tutto nel browser.",
    "intro": [
        "Le note scritte in JW Library sono facili da leggere dentro l'app e scomode da usare altrove: in un documento, in una scaletta per un discorso, su carta, o nelle mani di chi l'app non la usa. L'esportazione risolve questo, e la decisione principale non è come esportare ma quanto: un'esportazione filtrata è quasi sempre più utile di tutto in una volta.",
        "Le tue note di studio non dovrebbero restare intrappolate in un'app sola. A volte le "
        "vuoi come testo semplice — da incollare in una scaletta per un discorso, in un "
        "documento o nella tua app di appunti — e a volte vuoi un backup pulito che contenga "
        "solo una parte. Esplora studio fa entrambe le cose, leggendo il backup interamente "
        "nel browser.",
    ],
    "steps": [
        ("Carica il tuo backup",
         "Crea un backup in JW Library (Studio personale → Backup e ripristino → Crea un "
         "backup), poi apri jwsync.org e caricalo in Esplora studio."),
        ("Trova le note che ti servono",
         "Usa la ricerca insieme ai filtri per colore, etichetta e pubblicazione per arrivare "
         "esattamente alle note che cerchi — una pubblicazione, un'etichetta, un argomento."),
        ("Copia o esporta in Markdown/testo",
         "Porta fuori le note in Markdown o testo semplice per incollarle ovunque. La "
         "formattazione (grassetto, corsivo, elenchi) viene mantenuta, quindi le note "
         "strutturate restano strutturate."),
        ("Oppure estrai in un nuovo backup",
         "Preferisci un file? Esporta una selezione o un intervallo di date in un nuovo backup "
         ".jwlibrary — utile per archiviare un progetto o consegnare una serie specifica di "
         "note a un altro dispositivo."),
    ],
    "sections": [
        ("Perché esportare",
         "Le note sono più utili quando possono viaggiare: in un documento per una parte "
         "all'adunanza, in un wiki personale, in una stampa per chi non usa l'app. Il Markdown "
         "conserva la struttura e resta leggibile come testo semplice ovunque."),
        ("Scegliere un formato",
         "Il testo semplice è il più portabile e si incolla pulito in qualsiasi documento o email. L'output formattato conserva la struttura delle note lunghe e va bene per stampare o condividere. Se vuoi che le note tornino dentro JW Library in seguito — su un altro dispositivo, o nella biblioteca di qualcun altro — conserva il file .jwlibrary stesso anziché un'esportazione di testo, perché solo esso preserva i collegamenti tra note, evidenziazioni, etichette e il punto esatto della pubblicazione a cui sono ancorate."),
        ("Esportare solo una parte della biblioteca",
         "Un'esportazione completa di anni di studio è raramente ciò che serve. Restringere prima — a un'etichetta, una pubblicazione, un colore di evidenziazione o un intervallo di date — produce qualcosa di realmente utilizzabile, come tutte le note etichettate per un discorso, o tutto ciò che hai scritto durante un congresso. Gli stessi filtri che restringono la vista restringono l'esportazione: quello che vedi è quello che ottieni."),
        ("Cosa viaggia con il testo e cosa no",
         "Un'esportazione porta con sé le tue parole. Non porta gli ancoraggi che legano una nota a un paragrafo preciso di una pubblicazione precisa, perché quei riferimenti hanno senso solo dentro JW Library. È la ragione pratica per conservare anche i backup: un'esportazione serve a leggere, stampare e condividere fuori dall'app, mentre un file .jwlibrary è ciò che rimette le note in una biblioteca con il loro contesto intatto."),
        ("Mettere insieme tutto per un discorso o un incarico",
         "È il motivo più comune per esportare. Filtra per l'etichetta, la pubblicazione o l'intervallo di date sotto cui si trova il materiale, controlla il risultato ed esporta solo quello. Ottieni un unico documento con le note pertinenti e i passi che hai evidenziato, nell'ordine in cui compaiono, anziché uno scarico ingestibile dell'intera biblioteca."),
        ("Condividere note con qualcun altro",
         "Dietro la condivisione ci sono due cose diverse. Se l'altra persona vuole leggere le tue note, l'esportazione di testo è la scelta giusta: si apre ovunque e non richiede software particolari. Se vuole le note dentro la propria JW Library, ancorate agli stessi paragrafi e con le sue etichette e colori, allora serve un file .jwlibrary, perché un'esportazione di testo non può rimettere nulla nell'app."),
        ("Conservare un archivio leggibile anche fra molti anni",
         "Le esportazioni valgono anche di per sé. Una copia in testo semplice delle tue note di studio si aprirà ancora fra trent'anni con software che nessuno ha ancora scritto, e questo nessun formato proprietario di un'app può prometterlo. Conservare entrambi — il .jwlibrary per ripristinare e un'esportazione di testo per leggere — costa quasi nulla e copre entrambi i futuri."),
        ("Esportazione o backup — quale ti serve",
         "Rispondono a domande diverse. Un'esportazione serve a usare le tue note fuori da JW Library: leggere, stampare, citare, mandare a qualcuno. Un backup .jwlibrary serve a rimetterle dentro JW Library, su questo dispositivo o su un altro, con ogni ancoraggio, etichetta e colore intatti. Nessuno dei due sostituisce l'altro, e non c'è motivo di non avere entrambi."),
    ],
    "faq": [
        ("Esportare cambia le mie note in JW Library?",
         "No. L'esportazione legge una copia del tuo backup nel browser; il file originale e "
         "l'app restano intatti."),
        ("Posso esportare tutto in una volta?",
         "Sì — azzera i filtri per selezionare l'intera biblioteca, oppure restringi prima per "
         "esportarne solo una parte."),
        ("Posso portare le mie note in Word o Google Docs?",
         "Sì: esporta come testo e incolla. Il testo arriva con la struttura intatta e da lì può essere formattato."),
        ("Le evidenziazioni si esportano insieme alle note?",
         "Sì, incluso il passo evidenziato e il suo colore, così una copia stampata mostra sia ciò che hai contrassegnato sia ciò che hai scritto."),
        ("Posso esportare tutto in una volta?",
         "Sì, anche se un'esportazione filtrata è di solito più utile. Tutto può essere esportato in un solo passaggio quando vuoi una copia completa."),
        ("Posso esportare le risposte che ho digitato nelle domande di studio?",
         "Sì. Le risposte digitate fanno parte dei tuoi dati di studio personale e si esportano insieme a note ed evidenziazioni."),
        ("L'esportazione indica a quale pubblicazione appartiene ogni nota?",
         "Sì, l'esportazione identifica da dove proviene ogni nota, anche se l'ancoraggio sottostante funziona solo dentro JW Library."),
        ("Esportare cambia qualcosa nella mia biblioteca?",
         "No. Un'esportazione legge i tuoi dati e scrive un file separato; nulla dentro JW Library viene modificato, spostato o rimosso."),
        ("Posso esportare da un backup anziché dall'app?",
         "Sì. Un file .jwlibrary può essere aperto direttamente e le sue note esportate, il che è utile quando le note che ti servono sono in un vecchio backup e non sul dispositivo attuale."),
    ],
}

GUIDES_IT["organize-jw-library-tags"] = {
    "title": "Come organizzare e ripulire le etichette di JW Library",
    "h1": "Organizzare le etichette di JW Library: rinominare, unire e ripulire in blocco",
    "description": "Le etichette si moltiplicano negli anni di studio. Rinomina un'etichetta su "
                   "tutte le note, unisci i doppioni e togli quelle che non usi più — in "
                   "blocco, nel browser, con annulla completo.",
    "intro": [
        "Le etichette sono il modo per ritrovare le note più tardi, ma dopo qualche anno "
        "proliferano. Ti ritrovi con «Ministero», «ministero» e «Servizio di campo» che "
        "significano la stessa cosa, etichette create una volta e mai più usate, e una "
        "nomenclatura incoerente che rende il filtro inaffidabile. JW Library non offre alcun "
        "modo di sistemare tutto ciò su larga scala. Esplora studio sì.",
    ],
    "steps": [
        ("Carica il backup in Esplora studio",
         "Su jwsync.org carica il file .jwlibrary. Filtra per etichetta per vedere ogni "
         "etichetta e quante note la portano."),
        ("Rinomina un'etichetta su tutte le sue note",
         "Rietichetta in blocco: rinomina un'etichetta una volta e tutte le note che la usano "
         "si aggiornano — niente più modifiche nota per nota per correggere un refuso."),
        ("Unisci i doppioni",
         "Rietichetta le note di un'etichetta doppia su quella ufficiale, poi elimina il "
         "doppione rimasto vuoto. «Ministero» e «ministero» diventano una sola etichetta "
         "pulita."),
        ("Togli le etichette che non usi più",
         "Seleziona ed elimina in blocco le etichette superate. Tutto è annullabile, quindi "
         "una pulizia troppo entusiasta non è mai definitiva."),
        ("Esporta la biblioteca in ordine",
         "Scarica il .jwlibrary modificato e ripristinalo in JW Library. Le tue etichette sono "
         "coerenti ovunque."),
    ],
    "sections": [
        ("Un sistema di etichette che aiuta davvero",
         "Quando le etichette sono coerenti, filtrare diventa affidabile: un tocco mostra ogni "
         "nota su un tema, in tutte le pubblicazioni. È la differenza fra etichette come "
         "disordine ed etichette come vero indice del tuo studio."),
        ("Etichette coerenti rendono la condivisione questione di due clic",
         "Il selettore di note della pagina di condivisione ha il suo filtro per etichetta, "
         "quindi un'etichetta pulita è anche il modo più rapido per mandare a qualcuno una "
         "serie di note: scegli l'etichetta, premi Seleziona tutto, crea il file. Le etichette "
         "trascurate costano due volte — quando cerchi le note e quando provi a condividerle."),
    ],
    "faq": [
        ("Rietichettare in blocco tocca il testo delle note?",
         "No — cambia solo quali etichette sono collegate. Titoli e contenuto delle note "
         "restano esattamente come li hai scritti."),
        ("C'è un annulla se sbaglio?",
         "Sì. Esplora studio ha annulla e ripristina completi, e il tuo backup originale non "
         "viene mai modificato: le modifiche finiscono in una copia esportata."),
    ],
}

GUIDES_IT["manage-jw-library-highlights"] = {
    "title": "Come gestire e ricolorare le evidenziazioni di JW Library",
    "h1": "Gestire le evidenziazioni di JW Library: ricolorare e organizzare in blocco",
    "description": "Metti ordine in anni di evidenziazioni di JW Library: cambia i colori in "
                   "blocco, dai al tuo codice colore un significato coerente e sfoglia tutte "
                   "le evidenziazioni in un posto solo. Nel browser.",
    "intro": [
        "I colori delle evidenziazioni aiutano solo se significano qualcosa di coerente. Col "
        "tempo le evidenziazioni della maggior parte delle persone vanno alla deriva: il "
        "giallo voleva dire una cosa nel 2019 e un'altra oggi, e in JW Library non c'è modo di "
        "vederle tutte insieme o di correggerle su larga scala. Esplora studio raccoglie ogni "
        "evidenziazione in un'unica vista e ti permette di ricolorare in blocco.",
    ],
    "steps": [
        ("Carica il tuo backup",
         "Su jwsync.org apri il file .jwlibrary in Esplora studio e passa alla scheda "
         "Evidenziazioni."),
        ("Sfoglia e filtra le evidenziazioni",
         "Vedi ogni evidenziazione in un unico elenco, filtra per colore o pubblicazione e "
         "cerca nel testo evidenziato e nelle note collegate."),
        ("Ricolora in blocco",
         "Seleziona molte evidenziazioni e cambiane il colore insieme — per esempio unifica "
         "sotto un solo colore tutto ciò che intendevi come «scrittura chiave» in tutta la "
         "biblioteca."),
        ("Modifica anche le note collegate",
         "Dove un'evidenziazione ha una nota allegata, modifica qui stesso titolo e contenuto "
         "di quella nota."),
        ("Esporta e ripristina",
         "Scarica il .jwlibrary modificato e ripristinalo in JW Library, così il tuo codice "
         "colore coerente sarà su ogni dispositivo."),
    ],
    "sections": [
        ("Decidi cosa significano i tuoi colori",
         "Uno schema semplice — un colore per i punti principali, uno per le scritture da "
         "memorizzare, uno per le domande da approfondire — trasforma le evidenziazioni in uno "
         "strumento di studio invece che in decorazione. Ricolorare in blocco ti permette di "
         "applicare quello schema retroattivamente ad anni di letture."),
    ],
    "faq": [
        ("Posso vedere le evidenziazioni senza una nota allegata?",
         "Sì — la scheda Evidenziazioni le mostra tutte, con o senza nota collegata."),
        ("Ricolorare influisce sul testo sottostante?",
         "No, cambia solo il colore dell'evidenziazione; il testo della pubblicazione e le tue "
         "note restano intatti."),
    ],
}

GUIDES_IT["jw-library-study-answers"] = {
    "title": "Vedere e modificare le tue risposte di studio di JW Library",
    "h1": "Trovare le tue risposte di studio di JW Library in un posto solo",
    "description": "Le risposte che scrivi alle domande degli articoli di studio e dei quaderni "
                   "sono nascoste nel tuo backup. La scheda Risposte di studio di Esplora "
                   "studio ti permette di leggerle, cercarle e modificarle tutte insieme.",
    "intro": [
        "Mentre studi, scrivi risposte nei campi degli articoli di studio, della Torre di "
        "Guardia e dei quaderni delle adunanze. Vengono salvate nel tuo backup, ma JW Library "
        "le mostra solo una per una, sepolte nella rispettiva pubblicazione. Non c'è un unico "
        "posto in cui rivedere tutto quello che hai scritto. La scheda Risposte di studio di "
        "Esplora studio è quel posto.",
    ],
    "steps": [
        ("Carica il backup in Esplora studio",
         "Su jwsync.org carica il file .jwlibrary e apri la scheda Risposte di studio."),
        ("Leggi tutte le risposte insieme",
         "Ogni risposta che hai scritto compare in un elenco ricercabile, così rivedi a colpo "
         "d'occhio il tuo ragionamento su un intero articolo di studio."),
        ("Cerca e modifica",
         "Trova una risposta dal suo testo, poi modificala e rifiniscila sul posto — utile "
         "quando ripassi prima di un'adunanza o sistemi una formulazione scritta di fretta."),
        ("Esporta o ripristina",
         "Ripristina il file modificato per riportare le modifiche in JW Library, oppure copia "
         "le risposte come testo per un discorso o per i tuoi appunti."),
    ],
    "sections": [
        ("Perché è utile prima delle adunanze",
         "Rivedere le risposte preparate in un elenco continuo — invece di scorrere paragrafo "
         "per paragrafo nell'app — è un modo più rapido per rinfrescare quello che avevi "
         "pensato di dire e per notare le risposte lasciate in bianco."),
    ],
    "faq": [
        ("Sono la stessa cosa delle mie note personali?",
         "No — le risposte di studio sono quelle che hai scritto nei campi risposta di una "
         "pubblicazione. Esplora studio le mostra in una scheda a parte, separata dalle note "
         "libere."),
        ("Viene caricato qualcosa per leggere le mie risposte?",
         "No. Come tutto in JW Sync, il backup viene letto in locale nel browser e non viene "
         "mai inviato da nessuna parte."),
    ],
}

GUIDES_IT["extract-jw-library-notes-by-date"] = {
    "title": "Estrarre le note di JW Library di un periodo in un nuovo backup",
    "h1": "Estrarre un periodo di note di JW Library in un nuovo backup",
    "description": "Isola solo le note di un periodo preciso — un anno di servizio, un "
                   "congresso, un progetto di studio — in un backup .jwlibrary tutto suo e "
                   "pulito. Interamente nel tuo browser.",
    "intro": [
        "A volte vuoi una fetta della tua biblioteca, non tutta: le note di quest'anno per un "
        "ripasso, tutto quello che viene da un congresso, o la ricerca di un singolo progetto "
        "da passare a qualcuno. Esplora studio può estrarre le note di un periodo in un backup "
        ".jwlibrary nuovo di zecca, lasciando intatta la biblioteca principale.",
    ],
    "steps": [
        ("Carica il tuo backup",
         "Su jwsync.org apri il file .jwlibrary in Esplora studio."),
        ("Imposta il periodo",
         "Scegli le date di inizio e fine delle note che ti servono — un anno di servizio, un "
         "mese, le date di un evento specifico."),
        ("Estrai in un nuovo backup",
         "Esporta le note corrispondenti in un nuovo file .jwlibrary. Contiene solo le note e "
         "le evidenziazioni di quel periodo, con le loro etichette."),
        ("Usa il file estratto",
         "Ripristinalo in JW Library per un ripasso mirato, archivialo, o condividilo con chi "
         "ha bisogno solo di quella fetta."),
    ],
    "sections": [
        ("Buoni motivi per estrarre per data",
         "Un archivio annuale del tuo studio; un file pulito con le note di un congresso, "
         "tenuto a parte; consegnare a un compagno di studio solo le note di un progetto fatto "
         "insieme; o ridurre una biblioteca enorme in pezzi datati e gestibili — tutto senza "
         "toccare il backup principale."),
    ],
    "faq": [
        ("Estrarre toglie quelle note dalla mia biblioteca?",
         "No. Copia le note corrispondenti in un nuovo file; il tuo backup originale conserva "
         "tutto."),
        ("Che data usa — quando ho scritto o quando ho modificato la nota?",
         "Usa le date registrate nella nota stessa dentro il backup, quindi il periodo "
         "riflette quando le note sono state create o modificate."),
    ],
}

GUIDES_IT["connect-jw-library-notes-study-map"] = {
    "title": "Guarda come si collegano le tue note di JW Library — Mappa dello studio",
    "h1": "Mappa dello studio: un grafo privato delle tue note di JW Library",
    "description": "La Mappa dello studio trasforma le tue note di JW Library in una rete "
                   "interattiva, collegandole per scritture in comune, etichette in comune e "
                   "formulazioni simili — così vedi i temi che attraversano il tuo studio.",
    "intro": [
        "Anni di note custodiscono collegamenti che non hai mai visto: la stessa scrittura "
        "citata in una dozzina di voci, un tema a cui torni sempre, idee che si fanno eco in "
        "pubblicazioni diverse. La Mappa dello studio disegna quei legami come un grafo "
        "interattivo, così la forma del tuo studio diventa visibile.",
    ],
    "steps": [
        ("Apri la pagina Statistiche di studio e carica un backup",
         "Vai su jwsync.org/highlights.html e carica il file .jwlibrary. La Mappa dello studio "
         "lo legge nel tuo browser."),
        ("Apri la Mappa dello studio",
         "Avvia la mappa per vedere le tue note come punti collegati da scritture in comune, "
         "etichette in comune e formulazioni simili."),
        ("Esplora i collegamenti",
         "Passa fra le viste Temi e Note, sorvola una nota per illuminarne i legami, trascina "
         "gli elementi e usa il cursore della forza per mostrare solo i collegamenti più "
         "stretti. La modalità a schermo intero ti dà spazio."),
        ("Costruisci e salva catene di studio",
         "Traccia a mano le tue «catene di studio» fra note collegate per fissare un "
         "ragionamento, ed esporta la mappa come immagine PNG da conservare o condividere."),
    ],
    "sections": [
        ("Cosa rivela la mappa",
         "I raggruppamenti mostrano i temi che studi di più; una scrittura collegata a molte "
         "note indica un versetto a cui torni sempre; una nota isolata può essere un filo da "
         "sviluppare. È un modo di studiare il tuo studio — e di preparare discorsi seguendo i "
         "collegamenti che hai già creato."),
    ],
    "faq": [
        ("Servono tante note perché la mappa sia utile?",
         "Anche una biblioteca modesta mostra collegamenti; più le tue note sono ricche, più "
         "la mappa rivela. Le biblioteche molto piccole mostrano un avviso che invita ad "
         "aggiungere prima altre note."),
        ("La mappa è privata?",
         "Del tutto. Viene costruita nel tuo browser dal tuo backup e non viene mai caricata; "
         "anche l'esportazione in PNG è generata sul tuo dispositivo."),
    ],
}

GUIDES_IT["review-old-jw-library-notes"] = {
    "title": "Come rivedere le vecchie note di JW Library (perché restino)",
    "h1": "Rivedere le vecchie note con Riemergi — poco, ma spesso",
    "description": "Le note che non rileggi mai sono note che dimentichi. Riemergi mostra cosa "
                   "hai scritto in questo giorno negli anni passati e costruisce un ripasso "
                   "dilazionato e leggero, così lo studio passato continua a lavorare per te.",
    "intro": [
        "La maggior parte delle note di studio viene scritta una volta e mai più riletta. È "
        "uno spreco silenzioso: l'intuizione meritava di essere annotata, e poi è affondata in "
        "fondo alla biblioteca. Riemergi riporta a galla le tue vecchie note, poche alla "
        "volta, così rileggerle diventa una piccola abitudine quotidiana invece di un progetto "
        "per un giorno qualsiasi.",
    ],
    "steps": [
        ("Apri la pagina Statistiche di studio e carica un backup",
         "Vai su jwsync.org/highlights.html e carica il file .jwlibrary. Riemergi legge le tue "
         "note in locale."),
        ("Guarda «In questo giorno»",
         "Riemergi fa riaffiorare le note scritte in questa data negli anni precedenti — "
         "«scritta due anni fa oggi» — ricollegandoti allo studio passato nel momento in cui "
         "ha più significato."),
        ("Fai un breve ripasso quotidiano",
         "Ti propone una manciata di note da rileggere e segnare come riviste. Poco, ma "
         "spesso: è così che lo studio resta — e una serie cresce finché mantieni l'abitudine."),
        ("Torna domani",
         "Il ripasso dilazionato programma il ritorno delle note nel tempo, così quelle che "
         "vale la pena ricordare continuano a tornare finché non sono davvero tue."),
    ],
    "sections": [
        ("Perché il ripasso dilazionato funziona",
         "Rivedere qualcosa proprio quando stai per dimenticarlo è molto più efficace che "
         "studiare tutto d'un fiato. Distribuendo poche note su molti giorni, Riemergi "
         "trasforma la biblioteca che hai già in un ripasso continuo e a basso sforzo, che "
         "approfondisce piano piano quello che hai studiato."),
    ],
    "faq": [
        ("Dove viene salvato il mio avanzamento nel ripasso?",
         "Nel browser, sul tuo dispositivo — non c'è account e non viene caricato nulla. La "
         "serie e il calendario sono soltanto tuoi."),
        ("Mi servono note nuove per questo?",
         "No — Riemergi lavora con le note che hai già scritto. Più la biblioteca è vecchia, "
         "più i momenti «in questo giorno» sono soddisfacenti."),
    ],
}

GUIDES_IT["jw-library-achievements-streaks"] = {
    "title": "Serie di studio, livelli e obiettivi di JW Library",
    "h1": "Trasforma il tuo studio di JW Library in serie, livelli e riconoscimenti",
    "description": "Guarda le tue serie di studio, sali 60 livelli su 12 fasce nel tuo Percorso "
                   "di studio e sblocca circa 200 obiettivi — tutto letto in privato dal tuo "
                   "backup di JW Library.",
    "intro": [
        "La costanza è la parte difficile dello studio personale, e i progressi che non si "
        "vedono si lasciano andare facilmente. La pagina Statistiche di studio trasforma la "
        "storia del tuo backup in qualcosa che puoi vedere crescere: serie, livelli e "
        "riconoscimenti che riflettono lo studio che hai davvero fatto — nessun obiettivo "
        "imposto, solo il tuo percorso reso visibile.",
    ],
    "steps": [
        ("Apri la pagina Statistiche di studio",
         "Vai su jwsync.org/highlights.html e carica il tuo backup .jwlibrary. Tutto viene "
         "calcolato nel tuo browser."),
        ("Controlla le tue serie",
         "Vedi la serie di studio più lunga e quella in corso, il ritmo settimanale, le ore e "
         "i mesi più intensi — il polso della tua abitudine di studio."),
        ("Sali lungo il Percorso di studio",
         "Avanza per 60 livelli su 12 fasce con nome (dal Seme fino a Sempreverde), con una "
         "sfera che cambia colore e festeggiamenti a ogni livello, in base a tutto il tuo "
         "studio."),
        ("Colleziona obiettivi",
         "Sblocca circa 200 riconoscimenti, da Comune a Leggendario, comprese medaglie a tema "
         "legate al contenuto; apri una medaglia per vedere i progressi verso la successiva."),
    ],
    "sections": [
        ("Motivazione senza pressione",
         "Non sono traguardi fissati da qualcun altro: sono uno specchio di quello che hai già "
         "fatto. Vedere una serie che non vuoi interrompere, o un livello quasi raggiunto, è "
         "una spinta gentile a mantenere la buona abitudine. E una Scheda condivisibile "
         "riassume il tuo anno senza esporre una sola nota privata."),
    ],
    "faq": [
        ("Serie e riconoscimenti si aggiornano da soli?",
         "Riflettono il backup che carichi, quindi crea un backup nuovo per vedere i progressi "
         "più recenti. Non gira nulla in background."),
        ("Qualcosa di tutto ciò viene condiviso o caricato?",
         "No. È tutto calcolato in locale dal tuo backup; solo la scheda riassuntiva è "
         "qualcosa che puoi scegliere di condividere, e non contiene il testo di nessuna nota."),
    ],
}

GUIDES_IT["share-convention-assembly-notes"] = {
    "title": "Come condividere le note di congressi e assemblee da JW Library",
    "h1": "Condividere le note di congressi, assemblee e adunanze",
    "description": "Passa le note di un congresso, di un'assemblea o di un'adunanza a familiari "
                   "e amici in un piccolo file — senza consegnare tutta la tua biblioteca né "
                   "sovrascrivere la loro. Un uso pratico della condivisione di note.",
    "intro": [
        "Hai preso appunti con cura durante un congresso; a un amico che ha perso una sessione "
        "farebbero comodo; i familiari vogliono i punti per il loro ripasso. Mandare l'intero "
        "backup è eccessivo e, se ripristinato, cancellerebbe le note di chi lo riceve. La "
        "condivisione di note ti permette di passare esattamente le note che vuoi — e permette "
        "a chi le riceve di tenere tutto quello che ha già.",
    ],
    "steps": [
        ("Carica il backup nella pagina di condivisione",
         "Vai su jwsync.org/share.html e carica il file .jwlibrary."),
        ("Seleziona solo le note del congresso",
         "Scegli l'etichetta dell'evento dal filtro per etichetta del selettore e premi "
         "Seleziona tutto — l'elenco è già esattamente ciò che hai etichettato. Le "
         "evidenziazioni legate a quelle note vengono con loro."),
        ("Manda il piccolo file di condivisione",
         "JW Sync crea un piccolo file contenente solo quelle note. Mandalo come preferisci — "
         "app di messaggi, email, AirDrop. Nessun server, nessun account."),
        ("Familiari e amici le aggiungono",
         "Ognuno apre la stessa pagina, carica il tuo file insieme al proprio backup e ottiene "
         "un nuovo backup con le tue note aggiunte. Le loro note non vengono mai "
         "sovrascritte, e le tue arrivano etichettate, quindi sono facili da trovare."),
    ],
    "sections": [
        ("Un'etichetta rende tutto immediato",
         "Se etichetti le note durante l'evento (per esempio «Congresso 2026»), selezionarle "
         "dopo è un clic sul filtro e un Seleziona tutto. Vale la pena creare un'etichetta "
         "nuova all'inizio di ogni congresso, assemblea o adunanza speciale proprio per "
         "questo."),
    ],
    "faq": [
        ("Posso condividere con più persone insieme?",
         "Sì — il file di condivisione è solo un file. Mandalo a quante persone vuoi; ognuna "
         "lo aggiunge alla propria biblioteca in modo indipendente."),
        ("Verrà esposta tutta la mia biblioteca?",
         "No. Nel file ci sono solo le note che selezioni; il resto della tua biblioteca "
         "resta privato."),
    ],
}

GUIDES_IT["share-jw-library-notes-by-tag"] = {
    "title": "Condividere solo le note di JW Library sotto un'etichetta",
    "h1": "Condividere solo le note che portano una certa etichetta",
    "description": "Manda un argomento, un progetto o il materiale per uno studente invece di "
                   "tutta la tua biblioteca — e le tue etichette viaggiano con le note, così "
                   "arrivano già organizzate dall'altra parte.",
    "intro": [
        "Un'etichetta è di solito l'unità naturale della condivisione. Hai etichettato tutto "
        "quello che hai raccolto su un argomento, tutto quello che viene da un evento, o tutto "
        "quello che ripassi con una persona — ed è quell'insieme, non l'intera biblioteca, che "
        "l'altra persona vuole davvero.",
        "La condivisione di note di JW Sync lavora nota per nota, quindi un'etichetta è "
        "semplicemente l'elenco che spunti. Le note conservano le etichette mentre escono, il "
        "che significa che chi le riceve potrà filtrare esattamente lo stesso insieme dentro "
        "la propria biblioteca.",
    ],
    "steps": [
        ("Assicurati che le note portino l'etichetta",
         "Etichettale in JW Library mentre scrivi, oppure apri il backup in Esplora studio su "
         "jwsync.org e usa l'editor delle etichette per aggiungerne una a molte note in una "
         "volta. Etichettare con coerenza oggi è ciò che rende la condivisione un lavoro da un "
         "minuto domani."),
        ("Apri la pagina di condivisione e carica il backup",
         "Vai su jwsync.org/share.html, scegli Invia note e carica il file .jwlibrary. Viene "
         "letto nel tuo browser e non lascia mai il tuo dispositivo."),
        ("Scegli l'etichetta dal filtro, poi Seleziona tutto",
         "Il selettore di note ha un filtro che elenca ogni etichetta del backup con il numero "
         "di note che la portano. Scegli la tua e l'elenco si restringe esattamente a quelle "
         "note; Seleziona tutto le spunta tutte. È tutta la selezione — due clic."),
        ("Crea il file e mandalo",
         "JW Sync costruisce un piccolo file di condivisione con solo le note spuntate. "
         "Mandalo via chat, email o AirDrop — non c'è alcun server e nessun account da nessuna "
         "delle due parti."),
        ("L'altra persona le aggiunge al proprio backup",
         "Apre la stessa pagina, sceglie Ricevi, dà un'occhiata alle note e le aggiunge al "
         "proprio backup. Le tue etichette arrivano insieme alle note, più un'etichetta che "
         "identifica l'importazione, così anche per lei tutto l'insieme è a un filtro di "
         "distanza."),
    ],
    "sections": [
        ("Perché condividere un'etichetta invece di un backup",
         "Consegnare un backup .jwlibrary completo rivela tutto quello che hai mai scritto, e "
         "ripristinarlo cancellerebbe le note dell'altra persona. Condividere una selezione "
         "etichettata è l'opposto su entrambi i fronti: vede solo quello che hai scelto e non "
         "perde nulla di suo."),
        ("Restringere ancora, o condividere più etichette",
         "Filtro per etichetta e casella di ricerca lavorano insieme: scegli un'etichetta, poi "
         "digita una parola per restringere ancora, e Seleziona tutto continua a spuntare solo "
         "ciò che hai davanti. La ricerca trova anche i nomi delle etichette, quindi una "
         "parola chiave presente in più etichette le raccoglie in un colpo solo. Ogni nota "
         "dell'elenco mostra le sue etichette, così vedi cosa stai mandando prima di mandarlo."),
        ("Etichette da tenere per condividere",
         "Vale la pena tenere qualche etichetta che esiste solo per essere condivisa — il nome "
         "di un evento, un argomento su cui fai ricerca per altri, la persona con cui studi. "
         "Quando arriva il momento di mandare qualcosa, non c'è nulla da cercare: l'insieme è "
         "già pronto."),
    ],
    "faq": [
        ("Le mie etichette passano all'altra persona?",
         "Sì. Le note condivise portano le loro etichette, e l'importazione riceve "
         "un'etichetta propria, così chi le riceve può trovare, rileggere o togliere l'intero "
         "gruppo in seguito."),
        ("E se una nota ha più etichette?",
         "Compare sotto ciascuna di esse nel filtro, e tutte le sue etichette viaggiano con "
         "lei. Filtrare per un'etichetta non toglie mai le altre."),
        ("Condividere toglie le note dalla mia biblioteca?",
         "No. La condivisione copia le note in un piccolo file; il tuo backup e la tua app "
         "restano intatti."),
        ("Posso mandare la stessa etichetta a più persone?",
         "Sì — il file di condivisione è un file qualunque. Mandalo a quante persone vuoi, e "
         "ognuna lo aggiunge alla propria biblioteca in modo indipendente."),
    ],
}

GUIDES_IT["share-notes-with-bible-student"] = {
    "title": "Condividere le note di JW Library con uno studente della Bibbia",
    "h1": "Condividere le note di studio con chi studia la Bibbia con te",
    "description": "Manda le note di una lezione — scritture, illustrazioni, i punti che hai "
                   "preparato — direttamente nel JW Library dell'altra persona, senza toccare "
                   "nulla di quello che ha scritto lei.",
    "intro": [
        "Quando prepari uno studio, gran parte del lavoro finisce nelle tue note: le scritture "
        "in più, l'illustrazione che ha fatto arrivare il punto, la risposta alla domanda "
        "della settimana scorsa. Leggerlo ad alta voce è una cosa; lasciarle una copia che "
        "può rileggere tutta la settimana è un'altra.",
        "La condivisione di note mette le tue note preparate nella sua biblioteca come vere "
        "note di JW Library, agganciate agli stessi paragrafi e versetti — non come uno "
        "screenshot o un messaggio che scorrerà via.",
    ],
    "steps": [
        ("Prepara le note della lezione in JW Library",
         "Scrivi le note come faresti normalmente, sui paragrafi e sulle scritture che la "
         "lezione tratta. Dai loro un'etichetta — il nome della persona, o la pubblicazione — "
         "così l'insieme sarà facile da selezionare dopo."),
        ("Apri la pagina di condivisione e carica il backup",
         "Crea un backup (Studio personale → Backup e ripristino → Crea un backup), poi apri "
         "jwsync.org/share.html, scegli Invia note e carica il file. Non lascia mai il tuo "
         "dispositivo."),
        ("Spunta le note di questa lezione",
         "Filtra il selettore per l'etichetta che hai usato e premi Seleziona tutto, oppure "
         "cerca e spunta una per una. Crea il file di condivisione — tutto il resto della tua "
         "biblioteca resta dov'è."),
        ("Mandalo e spiega come ricevere",
         "Le serve prima un backup suo — Studio personale → Backup e ripristino → Crea un "
         "backup. Poi apre jwsync.org/share.html, sceglie Ricevi, carica il tuo file e il suo "
         "backup, e scarica il backup aggiornato."),
        ("Lei lo ripristina in JW Library",
         "Backup e ripristino → Ripristina, sceglie il file aggiornato, e le tue note "
         "compaiono nella sua biblioteca accanto alle sue — etichettate, così sa quali "
         "arrivano da te."),
    ],
    "sections": [
        ("Le sue note non vengono mai sovrascritte",
         "È questa la differenza importante rispetto a mandare un backup. Un ripristino "
         "sostituisce l'intera biblioteca di un dispositivo; ricevere note condivise vi "
         "aggiunge. Tutto quello che ha scritto lei — anche sugli stessissimi paragrafi — "
         "resta esattamente com'era."),
        ("Un ritmo settimanale da due minuti",
         "Una volta che l'avete fatto entrambi la prima volta, la routine è breve: preparare, "
         "spuntare, mandare, ripristinare. Molti trovano più comodo mandare le note subito "
         "dopo la preparazione, così lo studente le ha prima dello studio invece che dopo."),
    ],
    "faq": [
        ("Lo studente ha bisogno di un account o di un'app installata?",
         "Nessun account da nessuna parte, e nulla da installare a parte JW Library stesso — "
         "la pagina di condivisione è una normale pagina web."),
        ("E se lo studente non ha mai fatto un backup?",
         "Ne fa uno prima, in JW Library sotto Studio personale → Backup e ripristino. Va bene "
         "anche una biblioteca che sembra vuota; il backup è ciò a cui le note condivise "
         "vengono aggiunte."),
        ("Posso riprendermi le note in seguito?",
         "Il file è tuo finché non lo mandi. Una volta che qualcuno ce l'ha, è suo, esattamente "
         "come qualunque messaggio — quindi condividi quello che condivideresti volentieri per "
         "iscritto."),
    ],
}

GUIDES_IT["share-meeting-notes-with-family"] = {
    "title": "Condividere le note delle adunanze con la famiglia",
    "h1": "Condividere le note dell'adunanza di questa settimana con la famiglia",
    "description": "Qualcuno era malato, al lavoro o via — mandagli le note della settimana in "
                   "un piccolo file che può aggiungere al proprio JW Library, senza che "
                   "nessuno dei due perda nulla.",
    "intro": [
        "Nella maggior parte delle case ognuno prende le proprie note sul proprio dispositivo, "
        "e c'è sempre qualcuno che salta un'adunanza. Leggere le tue note a cena funziona una "
        "volta; metterle nella biblioteca dell'altra persona è ciò che le permette di usare il "
        "materiale in seguito, nel posto in cui andrà davvero a cercarlo.",
        "Siccome la condivisione avviene nota per nota e non backup per backup, più persone "
        "possono scambiarsi note liberamente senza che la biblioteca di nessuno venga "
        "sovrascritta.",
    ],
    "steps": [
        ("Fai il backup del dispositivo su cui hai preso le note",
         "JW Library → Studio personale → Backup e ripristino → Crea un backup."),
        ("Seleziona le note della settimana",
         "Su jwsync.org/share.html scegli Invia note, carica il backup e spunta le note di "
         "questa settimana — cercare per pubblicazione le raggruppa in fretta, e se etichetti "
         "le note della settimana il filtro per etichetta le raccoglie con un clic."),
        ("Mandalo nella chat di famiglia",
         "Crea il file di condivisione e mandalo con il canale che la famiglia usa già — app "
         "di messaggi, email, AirDrop. È un piccolo file con dentro solo le note spuntate."),
        ("Ognuno lo aggiunge al proprio backup",
         "Apre la stessa pagina, sceglie Ricevi, carica il tuo file con un backup suo, scarica "
         "il backup aggiornato e lo ripristina in JW Library."),
    ],
    "sections": [
        ("La biblioteca di ognuno resta sua",
         "Le note di nessuno vengono sostituite, e nessuno deve consegnare l'intera biblioteca "
         "per partecipare. Le note importate arrivano sotto un'etichetta, così ognuno vede a "
         "colpo d'occhio quali note vengono da qualcun altro e può cancellare il gruppo in "
         "seguito, se preferisce non tenerlo."),
        ("Adorazione in famiglia: raccogliere invece di disperdere",
         "Lo stesso strumento funziona anche al contrario. Se tutti prendono note durante "
         "l'adorazione in famiglia, una persona può raccogliere i file di condivisione degli "
         "altri in un unico backup e ritrovarsi con le note della famiglia sullo stesso "
         "materiale."),
    ],
    "faq": [
        ("Possono partecipare i dispositivi dei bambini?",
         "Qualunque dispositivo che possa far girare JW Library e aprire una pagina web. I "
         "passi sono identici su telefono, tablet o computer."),
        ("Dobbiamo essere sulla stessa piattaforma?",
         "No. Android, iPhone, iPad e l'app per Windows usano lo stesso formato di backup, "
         "quindi le note passano tra loro senza conversioni."),
    ],
}

GUIDES_IT["receive-shared-jw-library-notes"] = {
    "title": "Qualcuno mi ha mandato note di JW Library — come le apro?",
    "h1": "Aggiungere al tuo JW Library le note che qualcuno ha condiviso con te",
    "description": "Ti hanno mandato un file di note condivise o un blocco di testo. Ecco come "
                   "vederlo in anteprima e aggiungerlo al tuo backup di JW Library senza "
                   "perdere una sola nota tua.",
    "intro": [
        "Le note condivise di JW Library arrivano come un piccolo file (che termina in "
        ".jwshare.json) o come un blocco di testo incollato in un messaggio. JW Library non "
        "apre né l'uno né l'altro, ma non ti serve. Il lato ricezione di JW Sync legge le note "
        "condivise, ti mostra cosa contengono e le scrive dentro un tuo backup.",
        "L'intero scambio avviene sul tuo dispositivo. Non c'è account, non viene caricato "
        "nulla, e alle tue note si aggiunge qualcosa: non vengono mai sostituite.",
    ],
    "steps": [
        ("Fai prima un backup della tua biblioteca",
         "In JW Library: Studio personale → Backup e ripristino → Crea un backup. È il file a "
         "cui verranno aggiunte le note condivise, quindi conviene che sia aggiornato."),
        ("Apri la pagina di condivisione e scegli Ricevi",
         "Vai su jwsync.org/share.html e scegli Ricevi note."),
        ("Carica quello che ti hanno mandato",
         "Scegli il file .jwshare.json, oppure incolla il testo condiviso direttamente nel "
         "riquadro se è arrivato come messaggio. In entrambi i casi ottieni un'anteprima in "
         "sola lettura di ogni nota prima che venga scritto qualsiasi cosa."),
        ("Aggiungile al tuo backup",
         "Carica il tuo backup, scegli l'etichetta che dovranno portare le note importate e "
         "aggiungile. JW Sync costruisce un backup aggiornato da scaricare."),
        ("Ripristina il backup aggiornato in JW Library",
         "Studio personale → Backup e ripristino → Ripristina, scegli il file aggiornato. Le "
         "note condivise sono ora nella tua biblioteca, sui paragrafi e versetti giusti."),
    ],
    "sections": [
        ("Nulla di tuo viene sostituito",
         "Le note condivise vengono aggiunte come note nuove. Anche dove una nota condivisa "
         "finisce su un paragrafo in cui avevi già scritto, sopravvivono entrambe: la tua "
         "intatta, la sua accanto. L'unica cosa da ricordare è la solita regola del "
         "ripristino: ripristina il backup aggiornato, non uno più vecchio."),
        ("Cambiato idea in seguito?",
         "Ogni nota importata porta l'etichetta che hai scelto quando l'hai aggiunta. Apri il "
         "backup in Esplora studio, filtra per quell'etichetta, e puoi rileggere o cancellare "
         "l'intero gruppo in un colpo solo."),
    ],
    "faq": [
        ("Il file è arrivato rinominato in .txt o si apre come testo — è rotto?",
         "No. Le app di messaggi lo fanno spesso. Copia il testo e incollalo nel riquadro "
         "Ricevi; funziona esattamente allo stesso modo."),
        ("Mi serve l'intero backup di chi ha mandato?",
         "No. Il file di condivisione contiene solo le note che ha scelto di mandare — nulla "
         "d'altro dalla sua biblioteca."),
        ("Viene caricato qualcosa quando vedo le note in anteprima?",
         "No. Leggere il file condiviso, vederlo in anteprima e scrivere il backup aggiornato "
         "avvengono tutti nel tuo browser, sul tuo dispositivo."),
    ],
}

GUIDES_IT["share-notes-with-study-group"] = {
    "title": "Condividere note di ricerca con un gruppo di studio",
    "h1": "Condividere ricerche con un gruppo — e raccogliere le loro",
    "description": "Un file, tante persone: manda una serie di note di ricerca a tutti quelli "
                   "che studiano lo stesso argomento e raccogli quello che ti rimandano in un "
                   "unico insieme tuo.",
    "intro": [
        "Quando più persone approfondiscono lo stesso argomento, la ricerca finisce sparsa: "
        "uno ha trovato i riferimenti incrociati, un altro il contesto storico, un terzo le "
        "illustrazioni. Leggere gli screenshot degli altri non è come avere il materiale nella "
        "propria biblioteca, sugli stessi versetti, ricercabile l'anno prossimo.",
        "Siccome un file di condivisione è solo un file, una sola esportazione serve tutto il "
        "gruppo, e lo stesso meccanismo riporta a te il loro lavoro.",
    ],
    "steps": [
        ("Etichetta la ricerca mentre la raccogli",
         "Dai un'etichetta all'argomento in JW Library perché l'insieme resti unito. In "
         "Esplora studio puoi aggiungere un'etichetta a molte note in blocco se non l'hai "
         "fatto sul momento."),
        ("Crea un file di condivisione per il gruppo",
         "Su jwsync.org/share.html scegli Invia note, carica il backup, prendi l'etichetta "
         "dell'argomento dal filtro, premi Seleziona tutto e crea il file."),
        ("Pubblicalo una volta sola",
         "Manda lo stesso file a tutti — una chat di gruppo, un'email a più persone, quello "
         "che il gruppo usa già. Nessuna configurazione per persona e nessuna copia su "
         "server."),
        ("Chiedi le loro in cambio",
         "Ognuno può fare esattamente lo stesso dalla sua parte. Aggiungi al tuo backup, uno "
         "alla volta, i file che ricevi, dando a ogni importazione un'etichetta propria — il "
         "nome di chi ha mandato funziona bene — così saprai sempre di chi è ogni ricerca."),
    ],
    "sections": [
        ("Un insieme combinato, ma sempre attribuibile",
         "Dopo qualche giro hai tutta la ricerca del gruppo sull'argomento nella tua "
         "biblioteca, sui paragrafi e versetti giusti, con ogni contributo etichettato per "
         "provenienza. La ricerca trova tutto insieme; le etichette ti permettono di separarlo "
         "di nuovo quando vuoi."),
        ("Nessuno deve esporre la propria biblioteca",
         "Ognuno condivide solo le note che spunta. Il resto della biblioteca di ciascuno — "
         "studio personale, promemoria privati, tutto il resto — non entra mai nel file."),
    ],
    "faq": [
        ("C'è un limite a quante note posso condividere in una volta?",
         "In pratica no. Le note sono piccole; anche un insieme ampio produce un file che puoi "
         "mandare in un messaggio."),
        ("E se due persone mi mandano la stessa nota?",
         "La vedrai due volte, ciascuna sotto l'etichetta di chi l'ha mandata. La ricerca di "
         "Esplora studio rende i quasi-doppioni facili da individuare ed eliminare."),
        ("Si può ricevere senza mandare nulla in cambio?",
         "Sì. Ricevere e inviare sono indipendenti — nessuno è obbligato a condividere per "
         "poter aggiungere quello che gli è stato dato."),
    ],
}

GUIDES_IT["share-talk-preparation-notes"] = {
    "title": "Passare la ricerca dietro un discorso o un incarico",
    "h1": "Passare le ricerche dei tuoi discorsi e incarichi",
    "description": "Hai fatto la ricerca per un discorso, una parte o un incarico. Ecco come "
                   "consegnarla a chi ne avrà bisogno — come vere note nella sua biblioteca, o "
                   "come testo semplice per un documento.",
    "intro": [
        "La preparazione serve raramente una volta sola. Le scritture che hai rintracciato, il "
        "contesto che hai letto, il modo in cui hai deciso di impostare un punto: chi tratterà "
        "lo stesso materiale più avanti preferirebbe partire da lì piuttosto che da una pagina "
        "bianca.",
        "JW Sync ti offre due modi per passarla, adatti a persone diverse: come note che "
        "arrivano nel JW Library dell'altra persona, o come testo semplice da incollare in un "
        "documento.",
    ],
    "steps": [
        ("Raccogli la ricerca sotto un'unica etichetta",
         "Mentre prepari, etichetta le note con il tema o con l'incarico. Se sono già scritte "
         "e senza etichetta, apri il backup in Esplora studio ed etichettale in blocco in un "
         "paio di minuti."),
        ("Decidi quale forma è adatta all'altra persona",
         "Chi studia in JW Library vuole note nella propria biblioteca. Chi sta costruendo un "
         "documento vuole testo. Puoi fare entrambe le cose dallo stesso insieme."),
        ("Per mandare note: usa la pagina di condivisione",
         "Su jwsync.org/share.html scegli Invia note, carica il backup, filtra per l'etichetta "
         "che hai usato, premi Seleziona tutto e crea il file. L'altra persona lo aggiunge al "
         "proprio backup e lo ripristina: le sue note restano intatte."),
        ("Per mandare testo: esporta da Esplora studio",
         "Filtra sullo stesso insieme e copialo o esportalo in Markdown o testo semplice. La "
         "formattazione sopravvive, quindi una scaletta strutturata resta strutturata una "
         "volta incollata in un documento."),
    ],
    "sections": [
        ("Tieni una copia anche per te, in una forma che ritroverai",
         "La stessa esportazione vale la pena conservarla per uso tuo. Un'etichetta più un "
         "intervallo di date rendono tutta la preparazione recuperabile anni dopo, che è "
         "esattamente quando ti servirà — e l'estrazione per data di Esplora studio trasforma "
         "qualunque finestra temporale in un file a sé."),
    ],
    "faq": [
        ("Le scritture restano collegate ai versetti giusti?",
         "Sì — le note condivise mantengono il paragrafo e il versetto a cui erano agganciate, "
         "quindi arrivano al posto giusto nella biblioteca dell'altra persona."),
        ("Posso condividere note che hanno evidenziazioni?",
         "Sì. Le evidenziazioni legate alle note che condividi viaggiano con loro."),
    ],
}

GUIDES_IT["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Prepararsi per l'adunanza usando note che hai già scritto",
    "h1": "Preparazione settimanale con le note che hai già",
    "description": "Questo materiale l'hai già studiato. Ecco una breve routine settimanale che "
                   "fa riemergere le tue vecchie note, evidenziazioni e risposte sulla stessa "
                   "pubblicazione prima che tu prepari di nuovo.",
    "intro": [
        "La maggior parte delle persone prepara ogni settimana da una pagina bianca, anche se "
        "ha già scritto sullo stesso argomento — a volte sulla stessa scrittura — diverse "
        "volte. Quel ragionamento precedente è nella tua biblioteca; l'unico problema è che "
        "nulla te lo riporta davanti nel momento giusto.",
        "Una routine di cinque minuti all'inizio della preparazione risolve la cosa, e non usa "
        "nulla oltre al backup che hai già.",
    ],
    "steps": [
        ("Carica un backup aggiornato in Esplora studio",
         "Crea un backup in JW Library, poi aprilo su jwsync.org. Tutto viene letto nel tuo "
         "browser."),
        ("Cerca l'argomento prima di iniziare",
         "Cerca la scrittura tema, l'argomento o la pubblicazione. Tutto quello che hai "
         "scritto negli anni passati riemerge insieme, in ogni pubblicazione in cui compare."),
        ("Controlla le tue risposte di studio",
         "La vista Risposte di studio raccoglie le risposte che hai scritto nelle domande, "
         "quindi i giri precedenti sullo stesso materiale sono lì da sviluppare invece che da "
         "ripetere."),
        ("Aggiungi quello che manca, poi rimettilo a posto",
         "Le note si possono modificare o creare lì stesso — titolo, testo, etichette, colore "
         "dell'evidenziazione. Esporta il backup modificato e ripristinalo in JW Library, e la "
         "tua preparazione sarà nell'app per l'adunanza."),
    ],
    "sections": [
        ("Perché le note vecchie contano",
         "Rivedere quello che avevi concluso l'ultima volta rende la preparazione cumulativa. "
         "Smetti di riscoprire gli stessi punti e cominci a costruirci sopra — e le note che "
         "aggiungi questa settimana diventano il punto di partenza del giro successivo."),
        ("Una versione più gentile: lascia che siano le note a venire da te",
         "Se una ricerca settimanale ti sembra fatica, Riemergi, nella pagina Statistiche di "
         "studio, riporta da solo qualche vecchia nota ogni giorno, comprese quelle scritte in "
         "questa data negli anni passati. Stesso beneficio, nessuna routine da ricordare."),
    ],
    "faq": [
        ("Modificare nel browser cambia direttamente la mia biblioteca?",
         "No. Esporti un backup aggiornato e lo ripristini in JW Library — l'app cambia solo "
         "per un ripristino che esegui tu."),
        ("Il mio backup viene caricato quando ci cerco dentro?",
         "No. Il file viene letto in locale nel tuo browser; non viene mandato nulla da nessuna "
         "parte."),
    ],
}

GUIDES_IT["print-jw-library-notes"] = {
    "title": "Come stampare le tue note di JW Library",
    "h1": "Portare su carta le tue note di JW Library",
    "description": "JW Library non ha un pulsante Stampa. Esporta le note come testo o "
                   "Markdown, incollale in un documento qualsiasi e stampa — un diario di "
                   "studio, una serie di note per chi non usa l'app, o un archivio.",
    "intro": [
        "Da JW Library non si può stampare, e gli screenshot dello schermo di un telefono si "
        "leggono male. Ma le note sono tue, e portarle in un documento stampabile è semplice "
        "una volta che riesci a leggere il file di backup.",
        "Esplora studio legge un backup .jwlibrary nel tuo browser e ti permette di copiare o "
        "esportare qualsiasi selezione di note come testo semplice o Markdown — che ogni "
        "programma di videoscrittura, app di appunti e stampante già capisce.",
    ],
    "steps": [
        ("Crea un backup e aprilo",
         "JW Library → Studio personale → Backup e ripristino → Crea un backup, poi carica il "
         "file su jwsync.org."),
        ("Restringi a quello che vuoi su carta",
         "Filtra per pubblicazione, etichetta, colore dell'evidenziazione o intervallo di "
         "date, oppure cerca un argomento. Stampare tutto è possibile, ma un insieme filtrato "
         "di solito produce un documento molto più utile."),
        ("Copia o esporta come testo o Markdown",
         "Porta fuori la selezione in Markdown o testo semplice. Grassetto, corsivo ed elenchi "
         "sopravvivono, quindi le note strutturate restano strutturate sulla pagina."),
        ("Incolla in un documento e stampa",
         "Va bene qualunque programma di videoscrittura o app di appunti. Imposta titoli e "
         "margini come vuoi, poi stampa o salva in PDF."),
    ],
    "sections": [
        ("Creare un diario di studio",
         "Un intervallo di date è l'unità naturale per un diario stampato — un anno di note, o "
         "il periodo che copre una pubblicazione. L'estrazione per data ti dà un insieme "
         "cronologico pulito da stampare o rilegare, ed è una bella soddisfazione averlo fuori "
         "dallo schermo."),
        ("Stampare per chi non usa l'app",
         "Non tutti studiano da un dispositivo. Una serie stampata di note sul materiale in "
         "corso è davvero utile per chi preferisce la carta, e richiede gli stessi due minuti "
         "di qualunque altra esportazione."),
    ],
    "faq": [
        ("Posso stampare anche le mie evidenziazioni?",
         "La vista delle evidenziazioni elenca i passi che hai segnato, e quell'elenco si copia "
         "come testo insieme alle note."),
        ("Esportare cambia qualcosa in JW Library?",
         "No. L'esportazione legge una copia del tuo backup; il file originale e l'app restano "
         "intatti."),
    ],
}

GUIDES_IT["clean-up-duplicate-jw-library-notes"] = {
    "title": "Ripulire note doppie e vuote di JW Library",
    "h1": "Eliminare note doppie, note vuote e disordine",
    "description": "Hai ripristinato un backup due volte, o importato di nuovo le stesse note? "
                   "Il Dottore della biblioteca analizza il file .jwlibrary nel browser, trova "
                   "doppioni e note vuote e produce una copia pulita.",
    "intro": [
        "Le biblioteche accumulano disordine. Ripristinare un backup su un dispositivo che "
        "aveva già parte delle stesse note, importare due volte un insieme condiviso, o anni "
        "di note lasciate a metà — ognuna di queste cose lascia qualcosa dietro, e JW Library "
        "non offre alcun modo di spazzare via tutto in blocco.",
        "Il Dottore della biblioteca è un controllo di salute gratuito per un file "
        ".jwlibrary. Analizza il backup nel tuo browser, ti dice in parole semplici cosa ha "
        "trovato, e sistema con un tocco quello che è sistemabile.",
    ],
    "steps": [
        ("Fai prima un backup — come sempre",
         "JW Library → Studio personale → Backup e ripristino → Crea un backup. Conserva questo "
         "file; è la tua rete di sicurezza."),
        ("Avvia il controllo di salute",
         "Apri jwsync.org, carica il backup e avvia il Dottore della biblioteca. Esamina "
         "contenuto e struttura del file senza mandarlo da nessuna parte."),
        ("Leggi cosa ha trovato",
         "Doppioni, note vuote e altro disordine sono elencati con chiarezza, con i numeri, "
         "così vedi le dimensioni del problema prima di cambiare qualsiasi cosa."),
        ("Sistema e scarica la copia pulita",
         "Un tocco applica le riparazioni e produce un nuovo file .jwlibrary ripulito. Il tuo "
         "originale non viene mai modificato."),
        ("Ripristina il file pulito",
         "Backup e ripristino → Ripristina, e scegli il file ripulito. La tua biblioteca è la "
         "stessa, meno il disordine."),
    ],
    "sections": [
        ("Come nascono i doppioni",
         "Quasi sempre da un ripristino. Se ripristini un backup su un dispositivo che aveva "
         "già parte dello stesso materiale — o ripristini lo stesso file due volte per strade "
         "diverse — l'app non ha modo di sapere di aver già visto quelle note."),
        ("Unire è il modo per evitarli",
         "È proprio per questo che unire due backup è più sicuro che ripristinarne uno sopra "
         "l'altro: l'unione rileva il materiale già presente e lo tiene una volta sola. Gli "
         "stessi controlli girano dentro ogni unione, quindi un backup unito esce pulito anche "
         "se i file in ingresso non lo erano."),
    ],
    "faq": [
        ("Cancellerà note che voglio davvero tenere?",
         "Rimuove doppioni esatti e note vuote — materiale in cui non c'è nulla da perdere. E "
         "siccome scrive un file nuovo invece di modificare il tuo, l'originale resta sempre "
         "lì come riserva."),
        ("Può recuperare note che ho cancellato nell'app?",
         "No. Se una nota è stata cancellata in JW Library prima che il backup fosse creato, "
         "non è nel file — è un backup più vecchio il posto dove cercare."),
    ],
}

GUIDES_IT["backup-jw-library-before-phone-repair"] = {
    "title": "Fare il backup di JW Library prima di un ripristino o di una riparazione",
    "h1": "Prima di un ripristino di fabbrica, di una riparazione o di vendere il telefono",
    "description": "Un ripristino cancella le note di JW Library insieme a tutto il resto, e "
                   "gli strumenti di trasferimento non le portano. Fai un backup, verifica che "
                   "si apra davvero, poi ripristina senza rischiare nulla.",
    "intro": [
        "Ripristina il telefono, mandalo in riparazione o passalo a qualcun altro, e i dati di "
        "studio personale di JW Library se ne vanno con lui. Foto e app tornano da un backup "
        "cloud; anni di note, evidenziazioni e segnalibri di solito no, perché gli strumenti "
        "di trasferimento saltano i dati privati dell'app.",
        "Il rimedio richiede cinque minuti, e il passo che tutti saltano è proprio quello che "
        "conta di più: verificare che il file di backup sia davvero leggibile prima che il "
        "dispositivo venga azzerato.",
    ],
    "steps": [
        ("Crea il backup",
         "JW Library → Studio personale → Backup e ripristino → Crea un backup. Ottieni un "
         "file .jwlibrary — di solito pochi megabyte."),
        ("Portalo fuori dal dispositivo",
         "Inviatelo per email, o mettilo su Drive, iCloud o in una cartella del computer. Un "
         "backup che esiste solo sul telefono che stai per azzerare non è un backup."),
        ("Verifica che si apra prima di cancellare qualsiasi cosa",
         "Carica il file su jwsync.org e guardalo — note, evidenziazioni e segnalibri "
         "dovrebbero esserci tutti, e il controllo di salute segnalerà se c'è qualcosa che non "
         "va nel file. È tutto qui il senso dell'esercizio: scoprire dopo che il file è "
         "illeggibile è troppo tardi."),
        ("Ripristina il telefono, poi ripristina il backup",
         "Dopo il ripristino o la riparazione, installa JW Library, accedi, poi Backup e "
         "ripristino → Ripristina e scegli il tuo file."),
        ("Hai usato un telefono in prestito nel frattempo? Unisci, non sovrascrivere",
         "Se hai preso note su un dispositivo temporaneo, fai il backup anche di quello e "
         "unisci i due file su jwsync.org prima di ripristinare — altrimenti ripristinare il "
         "backup vecchio cancella tutto quello che hai scritto nell'attesa."),
    ],
    "sections": [
        ("Perché la verifica vale il minuto in più",
         "Trasferimenti interrotti, spazi cloud che rovinano i file ed estensioni rinominate "
         "lungo il percorso producono tutti backup che nella cartella sembrano a posto e "
         "falliscono al ripristino. Aprire prima il file trasforma un problema silenzioso in "
         "uno che puoi ancora risolvere, mentre il dispositivo originale ha ancora i dati."),
        ("Conserva il file dopo il ripristino",
         "Non cancellarlo appena il nuovo dispositivo funziona. I backup vecchi sono l'unica "
         "via di ritorno da una nota cancellata per sbaglio mesi dopo, e conservarli non costa "
         "nulla."),
    ],
    "faq": [
        ("Le mie pubblicazioni scaricate torneranno?",
         "Il backup contiene i dati di studio personale — note, evidenziazioni, segnalibri, "
         "etichette e playlist. Le pubblicazioni si riscaricano semplicemente dopo."),
        ("Il file funziona se cambio marca di telefono o piattaforma?",
         "Sì. Il formato .jwlibrary è lo stesso su Android, iPhone, iPad e Windows."),
    ],
}

GUIDES_IT["jw-library-notes-missing-after-update"] = {
    "title": "Note di JW Library sparite dopo un aggiornamento o una reinstallazione",
    "h1": "Note sparite dopo un aggiornamento, una reinstallazione o un ripristino",
    "description": "Le tue note sono sparite dopo un aggiornamento, una reinstallazione o un "
                   "nuovo accesso. Cosa fare per prima cosa, cosa non fare, e come recuperarle "
                   "senza perdere quello che hai scritto nel frattempo.",
    "intro": [
        "Aprire JW Library dopo un aggiornamento e trovare le note sparite spaventa, e nella grande maggioranza dei casi sono recuperabili. Ciò che conta è quello che fai nei minuti successivi — nello specifico, non fare l'unica cosa che trasforma una situazione recuperabile in una perdita definitiva.",
        "È un momento sgradevole: JW Library si apre, e le note non ci sono. Prima di tutto, un "
        "consiglio: non avere fretta. Quasi tutto ciò che rende questa situazione "
        "irrecuperabile accade nei primi dieci minuti, sovrascrivendo proprio il backup che "
        "contiene ancora le note mancanti.",
        "Segui i passi qui sotto nell'ordine. L'obiettivo è arrivare a un unico file che "
        "contenga sia le note vecchie sia tutto quello che hai scritto da allora.",
    ],
    "steps": [
        ("Non sovrascrivere ancora i tuoi backup",
         "Evita di creare un backup nuovo sopra uno vecchio, e non ripristinare nulla alla "
         "cieca. Un file di backup più vecchio è il posto più probabile in cui le tue note "
         "esistono ancora."),
        ("Cerca il backup più recente che hai",
         "Controlla gli allegati delle email, Google Drive, iCloud Drive, la cartella dei "
         "download del computer e ogni altro dispositivo su cui hai ripristinato. I backup "
         "sono piccoli, quindi spesso se ne hanno più copie di quante se ne ricordino."),
        ("Guarda dentro il file prima di ripristinarlo",
         "Carica il candidato su jwsync.org e vedi cosa contiene davvero — quante note, da "
         "quali pubblicazioni, fino a che data. Così sai se è il file giusto, prima di "
         "impegnarti in un ripristino."),
        ("Fai il backup anche del dispositivo attuale",
         "Anche se sembra vuoto, fanne il backup. Se hai scritto qualcosa da quando le note "
         "sono sparite, quel file ne è l'unica copia."),
        ("Unisci i due, poi ripristina",
         "Unisci il backup vecchio con quello attuale su jwsync.org. Il risultato contiene le "
         "note recuperate e tutto ciò che è stato scritto da allora, con i doppioni tenuti una "
         "volta sola. Ripristina quel file unito — mai il backup vecchio da solo."),
    ],
    "sections": [
        ("Perché ripristinare il backup vecchio da solo è la mossa sbagliata",
         "Un ripristino sostituisce del tutto la biblioteca del dispositivo. Se ripristini "
         "direttamente il backup vecchio, riavrai le note mancanti e perderai tutto quello che "
         "è stato scritto dopo. È l'unione preventiva a rendere il recupero senza perdite."),
        ("Se è il backup stesso a non ripristinarsi",
         "Un file che dà errore durante il ripristino non è necessariamente perduto. Passaci "
         "il controllo di salute — i danni da download interrotti, sincronizzazione cloud o "
         "un'estensione rinominata sono spesso riparabili, e una copia ripulita si ripristina "
         "normalmente."),
        ("Prima cosa: non creare ancora un nuovo backup",
         "Se le note sono sparite, resisti al riflesso di fare subito un backup. Un backup fotografa lo stato attuale, e se lo stato attuale è quello vuoto rischi di sovrascrivere il file buono che già avevi. Scopri prima quali backup esistono — in Download, File, nella posta o nel cloud — e solo allora decidi. Nulla sul dispositivo migliora grazie a un backup fatto nel panico."),
        ("Perché un aggiornamento può sembrare cancellare le note",
         "La causa abituale non è una cancellazione. Un aggiornamento può lasciare l'app puntata a un database nuovo e vuoto mentre quello vecchio è ancora su disco; una reinstallazione — inclusa quella eseguita automaticamente da un aggiornamento dello store fallito a metà — avvia l'app da zero; e su dispositivi condivisi o con più profili l'app può finire per girare sotto un profilo diverso. In ogni caso le note non sono tanto cancellate quanto non caricate, ed è per questo che un ripristino da backup di solito riporta tutto senza problemi."),
        ("Recuperare un vecchio backup senza buttare il lavoro nuovo",
         "Se hai studiato da quando il backup è stato fatto, un ripristino semplice scambia una perdita con un'altra: riporta le note vecchie e rimuove quelle più recenti. Il modo per aggirarlo è fare il backup dello stato attuale in un file separato, unirlo al backup più vecchio così che entrambi gli insiemi di note stiano in un solo file, e ripristinare il risultato. Ti ritrovi con le note recuperate e quelle recenti insieme anziché doverne scegliere una."),
        ("Se l'app si è reinstallata da sola",
         "Una reinstallazione svuota l'archiviazione privata dell'app, quindi tutto ciò che non è in un backup è irrecuperabile: non c'è alcuna copia nel cloud a cui appoggiarsi. Controlla ogni posto in cui un file .jwlibrary potrebbe essere stato salvato prima di concludere che non ce n'è nessuno, inclusa la cartella della posta inviata e qualsiasi archiviazione cloud tu abbia mai usato. Appena ne trovi uno, ripristinalo, e da lì in poi conserva i backup fuori dal dispositivo."),
        ("Quando è tornato tutto",
         "Quando le tue note sono ripristinate, fai un altro backup e conservalo fuori dal dispositivo: l'episodio che hai appena passato è l'argomento a favore. Se hai dovuto unire un vecchio backup con lo stato attuale per arrivare qui, conserva anche i due file di partenza: sono istantanee datate, e averne di più è proprio ciò che ha reso possibile il recupero."),
    ],
    "faq": [
        ("Le note sono ancora da qualche parte sul dispositivo?",
         "Non in una forma raggiungibile da fuori dell'app. Il recupero passa realisticamente "
         "da un file di backup precedente — ecco perché conservare quelli vecchi conta tanto."),
        ("Riaccedere riporta le note?",
         "No. I dati di studio personale non stanno in un account; vivono sul dispositivo e "
         "viaggiano solo tramite file di backup."),
        ("E se l'unico backup che ho è di mesi fa?",
         "Uniscilo con un backup del dispositivo com'è adesso. Recuperi tutto quello che ha il "
         "file vecchio e tieni tutto quello che il dispositivo ha ancora, senza dover "
         "scegliere."),
        ("Le mie note sono davvero perse?",
         "Non necessariamente. Se esiste un backup da qualche parte, tutto ciò che contiene è completamente recuperabile. È irrecuperabile solo il lavoro svolto dopo il backup più recente."),
        ("Posso combinare un vecchio backup con quello che è sul dispositivo ora?",
         "Sì — fai prima il backup dello stato attuale, poi uniscilo a quello più vecchio e ripristina il risultato. I due insiemi di note finiscono nella stessa biblioteca."),
        ("Ripristinare un vecchio backup cancellerà le mie note recenti?",
         "Da solo sì, perché un ripristino sostituisce i dati del dispositivo. Unisci prima il backup attuale a quello vecchio e ripristina il file unito."),
        ("Devo reinstallare l'app per risolvere?",
         "No: reinstallare svuota l'archiviazione privata dell'app ed elimina ogni possibilità di recuperare quanto è ancora sul dispositivo. Cerca prima un backup esistente e considera la reinstallazione l'ultima risorsa, quando ne hai uno."),
    ],
}

GUIDES_IT["help-family-member-move-jw-library-notes"] = {
    "title": "Aiutare un familiare a spostare le sue note di JW Library",
    "h1": "Aiutare qualcun altro a spostare o salvare le sue note di JW Library",
    "description": "Sei tu quello a cui chiedono di sistemare il telefono. Ecco la strada più "
                   "breve e affidabile per spostare le note di JW Library di un parente su un "
                   "dispositivo nuovo — anche senza leggere le sue note.",
    "intro": [
        "Prima o poi qualcuno ti mette in mano il suo telefono, con uno nuovo accanto. Le note "
        "di JW Library sono la parte che non si sposta da sola, e spesso quella che conta di "
        "più: anni di studio che nessuno strumento di trasferimento porta di là.",
        "Il procedimento è lo stesso che faresti per te, con una considerazione in più che vale "
        "la pena chiarire prima: su quale dispositivo si svolge il lavoro.",
    ],
    "steps": [
        ("Guidalo nel fare un backup sul dispositivo vecchio",
         "JW Library → Studio personale → menu a tre punti → Backup e ripristino → Crea un "
         "backup. Salva un file .jwlibrary. Se non sei con lui, questa parte si può fare al "
         "telefono."),
        ("Porta il file dove ti serve",
         "Fatti mandare il file da lui, o fa' che se lo mandi per email. È abbastanza piccolo "
         "da passare per qualunque app di messaggi."),
        ("Verifica che il file si apra",
         "Caricalo su jwsync.org e conferma che le note ci siano. Farlo prima che il "
         "dispositivo vecchio venga azzerato o ceduto è ciò che trasforma una brutta sorpresa "
         "in un non-evento."),
        ("Unisci se il dispositivo nuovo ha già delle note",
         "Se usa il telefono nuovo da un po', fai il backup anche di quello e unisci i due "
         "file — altrimenti ripristinare il backup vecchio cancella tutto quello che ha "
         "scritto sul dispositivo nuovo."),
        ("Accompagnalo nel ripristino",
         "Sul dispositivo nuovo: Backup e ripristino → Ripristina, scegliere il file. Note, "
         "evidenziazioni, segnalibri ed etichette compaiono tutti."),
    ],
    "sections": [
        ("Farlo senza leggere le sue note",
         "Le note di studio personale sono personali. Se preferisci non vederle — o preferisce "
         "lui che tu non le veda — fai tutto sul suo dispositivo: è una pagina web, quindi "
         "puoi aprire jwsync.org sul suo telefono o tablet, caricare lì i suoi file e non "
         "avere mai il backup sulla tua macchina. In ogni caso non viene caricato nulla, ma "
         "così il file non lascia mai le sue mani."),
        ("Lasciagli un backup che riesca a ritrovare",
         "Prima di restituire il telefono, assicurati che il file di backup sia da qualche "
         "parte dove lui possa ritrovarlo — la sua email o il suo spazio cloud, non solo la "
         "tua cartella dei download. La prossima volta magari non avrà bisogno di te."),
    ],
    "faq": [
        ("Posso farlo a distanza?",
         "Sì. Se riesce a creare un backup e a mandarti il file, tutto il resto funziona a "
         "distanza — e il ripristino sono pochi tocchi che puoi spiegargli al telefono."),
        ("Lui ha un Android e il nuovo è un iPhone. Cambia qualcosa?",
         "No. Il formato di backup è identico su Android, iPhone, iPad e Windows."),
        ("E se non ha mai fatto un backup e il telefono vecchio non c'è più?",
         "Allora non c'è nulla da cui recuperare — i dati vivevano su quel dispositivo. Vale "
         "la pena impostare subito sul telefono nuovo l'abitudine a backup regolari."),
    ],
}

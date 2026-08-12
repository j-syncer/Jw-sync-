# -*- coding: utf-8 -*-
"""Swedish translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → säkerhetskopia (.jwlibrary-filen)
  Personal Study            → Personligt studium
  Backup and Restore        → Säkerhetskopiera och återställ
  restore                   → återställa
  merge                     → slå ihop / sammanslagning
  notes                     → anteckningar
  highlights                → markeringar
  bookmarks                 → bokmärken
  tags                      → etiketter
  Study Explorer            → Studieutforskaren
  Library Doctor            → Biblioteksdoktorn
  Reading Companion         → Läsledsagaren
  Resurface                 → Återblick
  Study Map                 → Studiekartan
  Study Stats               → Studiestatistik
  Conflict Reviewer         → Konfliktgranskaren
  meeting                   → möte
  congregation              → församling
  assembly / convention     → sammankomst / regionalt sammankomst
"""

GUIDES_SV = {}

GUIDES_SV["merge-jw-library-backups"] = {
    "title": "Så slår du ihop JW Library-säkerhetskopior från två enheter",
    "h1": "Så slår du ihop JW Library-säkerhetskopior från två enheter",
    "description": "Slå ihop anteckningar, markeringar, bokmärken och etiketter från två eller "
                   "flera JW Library-säkerhetskopior till en enda .jwlibrary-fil — gratis, "
                   "privat, direkt i webbläsaren.",
    "intro": [
        "Du studerade Vakttornet på telefonen och en annan artikel på surfplattan. Nu har varje enhet arbete som den andra saknar, och JW Library kan inte förena dem: återställning där byter ut allt i stället för att slå ihop, så vilken säkerhetskopia du än återställer raderar den andra enhetens studium. Med enbart appen finns det inget sätt att behålla båda.",
        "Det är vad den här webbplatsen är till för. Den läser två (eller fler) .jwlibrary-filer och för samman anteckningarna, överstrykningarna, bokmärkena och taggarna från alla till en ny säkerhetskopia — så att inget behöver väljas bort. Sammanslagningen sker helt i din webbläsare; dina filer laddas aldrig upp till någon server, så dina personliga studieanteckningar förblir privata.",
        "Det är också därför vanan är förebyggande snarare än reparerande: när du slår ihop med jämna mellanrum behöver du inte längre komma ihåg att återställa innan du studerar någon annanstans. Studera där du är, slå ihop när det passar, och varje enhet hinner i kapp.",
    ],
    "steps": [
        ("Skapa en säkerhetskopia på varje enhet",
         "Öppna Personligt studium i JW Library, tryck på trepunktsmenyn, välj "
         "Säkerhetskopiera och återställ och sedan Skapa en säkerhetskopia. Gör det på varje "
         "enhet. Varje enhet ger en .jwlibrary-fil."),
        ("Öppna JW Sync",
         "Gå till jwsync.org i vilken webbläsare som helst — på mobilen, surfplattan eller "
         "datorn. Inget behöver installeras."),
        ("Ladda in båda säkerhetskopiorna",
         "Släpp in (eller välj) .jwlibrary-filerna. JW Sync läser dem lokalt, på din enhet."),
        ("Granska förhandsvisningen före sammanslagningen",
         "Innan något skrivs visar en förhandsvisning exakt vad som kommer att slås ihop. Om "
         "samma anteckning har redigerats olika på de två enheterna visar Konfliktgranskaren "
         "båda versionerna sida vid sida, med skillnaderna ord för ord, så att du väljer "
         "vilken som ska behållas — eller låter ”Föreslå bästa” välja åt dig."),
        ("Ladda ner den sammanslagna filen och återställ den",
         "Ladda ner den sammanslagna .jwlibrary-filen och återställ den på varje enhet via "
         "Säkerhetskopiera och återställ → Återställ. Nu har båda enheterna hela det förenade "
         "biblioteket."),
    ],
    "sections": [
        ("Vad slås ihop?",
         "Anteckningar, markeringar, bokmärken, etiketter och kopplingarna mellan dem. "
         "Dubbletter upptäcks automatiskt, så att återställa den sammanslagna filen dubblerar "
         "aldrig något. Säkerhetskopior från Android, iPhone, iPad och Windows-appen har samma "
         "format och kan slås ihop fritt."),
        ("Är det säkert?",
         "Sammanslagningen ändrar aldrig dina ursprungliga filer — den skapar en helt ny "
         "säkerhetskopia, så originalen finns kvar orörda som reserv. Och eftersom allt körs i "
         "webbläsaren lämnar inga data din enhet."),
        ("Vad en .jwlibrary-fil faktiskt innehåller",
         "En .jwlibrary-säkerhetskopia är ett ZIP-arkiv. Byt namn på en kopia till .zip och öppna den, så hittar du userData.db — en SQLite-databas med alla anteckningar, markeringar, bokmärken och etiketter du någonsin skapat — och en liten manifest.json som beskriver kopian. Dina anteckningar ligger i tabellen Note, markeringarna i UserMark och BlockRange, bokmärkena i Bookmark och etiketterna i Tag och TagMap. När du förstår att säkerhetskopian är en komplett databas och inte en samling lösa filer faller allt annat på den här sidan på plats: därför är en återställning allt eller inget, och därför går två kopior att slå ihop över huvud taget."),
        ("Varför JW Librarys egen återställning inte kan slå ihop",
         "Vid återställning läser JW Library inte din säkerhetskopia för att lägga till det som saknas på enheten. Programmet ersätter enhetens databas med den i filen. Det är medvetet och säkert konstruerat, eftersom enheten garanterat hamnar i ett känt läge, men det innebär att om du återställer surfplattans kopia på telefonen försvinner allt som fanns på telefonen men inte på plattan. Ingen inställning ändrar det, och det är precis den luckan en sammanslagning fyller: den skapar en enda fil som redan innehåller båda enheternas arbete, så att den enhet du återställer den på blir komplett."),
        ("Så upptäcks dubbletter",
         "Varje anteckning, markering och bokmärke bär ett GUID — en unik identifierare som tilldelas när posten skapas och bevaras i alla senare säkerhetskopior. När samma post finns i två kopior bär båda exemplaren samma GUID, så den känns igen som en post och behålls en gång. Därför dubbleras ingenting om du slår ihop samma två filer två gånger, och därför kan du tryggt slå ihop på nytt varje vecka. När GUID stämmer men texten skiljer sig — samma anteckning redigerad på båda enheterna — går det inte att lösa automatiskt, så posten visas i Konfliktgranskaren med en jämförelse ord för ord så att du väljer."),
        ("Vad som inte finns i säkerhetskopian",
         "En säkerhetskopia innehåller bara dina personliga studiedata. Nedladdade publikationer, bibelöversättningar, video och ljud ingår inte, och det är därför kopiorna är små — vanligtvis några megabyte även efter många års studium. Efter en återställning på en ny enhet kan du behöva ladda ner de publikationer du läser regelbundet igen. Ingenting du skrivit påverkas av det: anteckningar är förankrade i publikationer via referenser och kopplas tillbaka så snart publikationen finns på plats."),
        ("Om sammanslagningen rapporterar 0 tillagda anteckningar",
         "Det stämmer nästan alltid och är inget fel. Det betyder att alla anteckningar i den andra filen redan fanns i den första — vanligt om du slagit ihop nyligen, eller om en enhet helt enkelt ligger efter den andra. Titta i förhandsgranskningen: den visar vad varje fil bidrar med innan något skrivs. Om du väntade dig nya poster och inte ser några, kontrollera att du säkerhetskopierade enheten efter det studiepass du letar efter — en säkerhetskopia innehåller bara det som fanns i det ögonblick den skapades."),
    ],
    "faq": [
        ("Kan jag slå ihop fler än två säkerhetskopior?",
         "Ja — ladda in lika många .jwlibrary-filer som du har enheter. Alla förenas till en "
         "enda säkerhetskopia."),
        ("Blir det dubbla anteckningar när jag slår ihop?",
         "Nej. Identiska anteckningar, markeringar och bokmärken upptäcks och behålls en gång. "
         "Verkligt olika versioner av samma anteckning dyker upp i Konfliktgranskaren så att "
         "du får bestämma."),
        ("Fungerar det mellan Android och iPhone?",
         "Ja. .jwlibrary-formatet är identiskt på Android, iOS, iPadOS och Windows, så "
         "säkerhetskopior från olika plattformar slås ihop utan någon konvertering."),
        ("Måste jag slå ihop i en viss ordning?",
         "Nej. Sammanslagningen är oberoende av ordning — samma uppsättning filer ger samma resultat oavsett vilken du laddar först. Ordningen påverkar bara vilken fil som räknas som utgångspunkt i förhandsgranskningens sammanfattning."),
        ("Vad händer med etiketter som bara finns på en enhet?",
         "De följer med oförändrade, tillsammans med kopplingarna mellan etiketterna och de anteckningar de märker. Om båda enheterna har en etikett med samma namn behandlas den som en enda och får anteckningarna från båda."),
        ("Hur stor blir den sammanslagna filen?",
         "Ungefär som originalen tillsammans minus dubbletterna — i regel fortfarande bara några megabyte. Säkerhetskopior innehåller inga publikationsmedier, så även ett hårt annoterat bibliotek ryms i ett mejl."),
        ("Kan jag ångra en återställning?",
         "Inte inifrån JW Library, och därför är det viktigt att spara originalkopiorna. Sammanslagningen ändrar aldrig filerna du laddar in, så dina kopior från före sammanslagningen finns kvar exakt som de var och kan återställas om du vill backa."),
    ],
}

GUIDES_SV["sync-jw-library-multiple-devices"] = {
    "title": "Så synkroniserar du JW Library mellan flera enheter",
    "h1": "Så håller du JW Library likadant på flera enheter",
    "description": "JW Library har ingen inbyggd synkronisering mellan enheter. Här är en "
                   "enkel och privat rutin som håller anteckningar, markeringar och bokmärken "
                   "identiska på mobilen, surfplattan och datorn.",
    "intro": [
        "De flesta som studerar på två enheter upptäcker problemet på samma sätt: anteckningarna som skrevs på surfplattan finns inte på telefonen, och att återställa den enas kopia på den andra skulle radera det den hade. JW Library erbjuder ingen synkronisering, och dess återställning är medvetet allt eller inget, så att hålla enheterna i takt kräver en rutin snarare än en inställning.",
        "JW Library synkroniserar inte personliga studiedata mellan enheter — det finns inget "
        "konto som flyttar dina anteckningar från mobilen till surfplattan. Den officiella "
        "vägen är Säkerhetskopiera och återställ, och en återställning ersätter enhetens data "
        "helt. Hur håller man då två eller tre enheter likadana utan att förlora något?",
        "Svaret är en kort rutin: slå ihop och återställ. Gjord varje vecka eller varje månad "
        "tar den ett par minuter och lämnar hela ditt bibliotek på varje enhet.",
    ],
    "steps": [
        ("Säkerhetskopiera varje enhet",
         "På varje enhet: Personligt studium → trepunktsmenyn → Säkerhetskopiera och återställ "
         "→ Skapa en säkerhetskopia. Du får en .jwlibrary-fil per enhet."),
        ("Slå ihop säkerhetskopiorna på jwsync.org",
         "Ladda in alla filerna. JW Sync förenar anteckningar, markeringar, bokmärken och "
         "etiketter från varje enhet till en enda sammanslagen .jwlibrary-fil — lokalt i "
         "webbläsaren, inget laddas upp."),
        ("Återställ den sammanslagna filen på varje enhet",
         "Säkerhetskopiera och återställ → Återställ, välj den sammanslagna filen. Nu är alla "
         "enheter likadana och kompletta."),
        ("Låt JW Sync påminna dig",
         "Slå på en synkroniseringspåminnelse (varje vecka eller varje månad) i JW Sync, så "
         "hör den av sig när det är dags att göra om rutinen. Den kommer också ihåg dina "
         "sparade enheter, så varje omgång går snabbare."),
    ],
    "sections": [
        ("Varför inte bara återställa den senaste säkerhetskopian?",
         "För att ”senaste” bara speglar en enhet. Om du skrev mötesanteckningar på mobilen "
         "och studieanteckningar på surfplattan samma vecka innehåller varje säkerhetskopia "
         "sådant som saknas i den andra. Att återställa den ena över den andra kostar dig "
         "halva arbetet. Det är sammanslagningen som gör rutinen trygg."),
        ("Hur ofta bör jag synkronisera?",
         "Anpassa det efter hur du studerar. Två aktiva enheter som används varje dag: en gång "
         "i veckan är bekvämt. En surfplatta som bara plockas fram till mötena: en gång i "
         "månaden räcker gott. Att vänta längre betyder bara att sammanslagningen har mer att "
         "förena — inget går förlorat mellan omgångarna."),
        ("Varför det inte finns någon riktig synkronisering",
         "JW Library har inget konto som bär personliga studiedata mellan enheter. Anteckningar, markeringar och bokmärken lever i en databas inuti varje enhet och stannar där. Det enda officiella sättet att flytta dem är Säkerhetskopiera och återställ, och en återställning ersätter målenhetens data i stället för att kombinera dem. Två enheter som används oberoende av varandra glider därför isär permanent om inte något slår ihop dem — vilket är hela poängen med rutinen nedan."),
        ("Håll en huvudfil",
         "Rutinen fungerar bäst om du behandlar en sammanslagen fil som den aktuella huvudfilen. Varje omgång: säkerhetskopiera alla enheter, slå ihop kopiorna och återställ resultatet överallt. Den sammanslagna filen blir sedan huvudfil för nästa omgång. Att spara de daterade huvudfilerna i molnet ger dig både en synkroniseringsmekanism och ett arkiv — om du raderar något av misstag finns det kvar i en tidigare huvudfil."),
        ("Vad som händer om du hoppar över en enhet ett tag",
         "Ingenting går förlorat. En enhet som stått utanför flera omgångar bär helt enkelt äldre data; när du till slut tar med den slås dess anteckningar ihop med allt annat, och återkommande poster paras via GUID i stället för att dubbleras. Det enda som kräver ett beslut är samma anteckning redigerad på två enheter sedan förra sammanslagningen, och den visas i Konfliktgranskaren med båda versionerna sida vid sida."),
        ("Hur ofta som räcker",
         "Anpassa det efter hur mycket arbete du skulle ogilla att göra om. Varje vecka passar om du studerar på två enheter nästan dagligen; varje månad räcker gott om den ena används sporadiskt. Det viktiga är att göra det före allt oåterkalleligt — ett telefonbyte, en återställning, en reparation — för det är då en avvikelse blir en förlust."),
        ("Telefon, surfplatta och Windows-appen tillsammans",
         "Rutinen bryr sig inte om hur många enheter det gäller eller vad de kör. Säkerhetskopiera var och en, slå ihop dem alla i ett svep och återställ den sammanslagna filen överallt. En Windows-dator för förberedelse och en telefon för mötena kombineras precis som två telefoner, eftersom alla plattformar skriver samma säkerhetskopieformat."),
        ("Minska konflikterna innan de uppstår",
         "Konflikter uppstår bara när samma anteckning redigeras på två enheter mellan två sammanslagningar. I praktiken är det sällsynt, och det blir ännu sällsyntare om du skriver på en enhet i taget — läs var du vill, men skriv där du brukar skriva. Att slå ihop oftare krymper också fönstret då en avvikelse kan uppstå, vilket fungerar bättre än att försöka minnas vilken enhet som har den nyaste versionen."),
        ("Var rutinen lönar sig",
         "Värdet av att hålla enheterna sammanslagna är inte ordningen — det är att varje enhet blir en fullständig säkerhetskopia av ditt studiebibliotek. Tappar eller förstör du någon av dem bär de andra fortfarande allt, vilket förvandlar värsta fallet från år av förlorade anteckningar till ett besvär. Det är ett starkare läge än någon vana att säkerhetskopiera på en enda enhet kan ge."),
    ],
    "faq": [
        ("Körs JW Sync i bakgrunden?",
         "Nej — det är en webbsida, inte en installerad tjänst. Ingenting genomsöker dina "
         "enheter. Du kör rutinen när du själv vill; den valfria påminnelsen är bara en "
         "avisering."),
        ("Kan jag synkronisera tre eller fler enheter?",
         "Ja. Säkerhetskopiera varje enhet, ladda in alla filerna, slå ihop en gång och "
         "återställ den sammanslagna filen överallt."),
        ("Tänk om jag redigerat samma anteckning på två enheter?",
         "Båda versionerna behålls tills du väljer. Konfliktgranskaren visar dem sida vid sida med en jämförelse ord för ord, eller så låter du den föreslå den mer utförliga."),
        ("Spelar ordningen jag återställer i någon roll?",
         "Nej. När den sammanslagna filen väl är skapad försätter en återställning av den varje enhet i samma fullständiga läge, i vilken ordning som passar dig."),
        ("Kan jag hålla tre eller fler enheter i takt?",
         "Ja. Säkerhetskopiera var och en och ladda in dem alla i samma sammanslagning — det finns ingen gräns kopplad till antalet enheter."),
        ("Går det att automatisera?",
         "Inte fullt ut, eftersom JW Library saknar ett synkroniseringsgränssnitt och återställningssteget sker i appen. Den manuella rutinen tar ungefär två minuter när du vant dig."),
        ("Måste jag slå ihop om jag bara läser på den andra enheten?",
         "Om du aldrig annoterar där behöver du bara återställa på den då och då så att den bär dina aktuella anteckningar."),
    ],
}

GUIDES_SV["transfer-jw-library-notes-new-phone"] = {
    "title": "Så flyttar du JW Library-anteckningar till en ny mobil",
    "h1": "Så flyttar du JW Library-anteckningar till en ny mobil",
    "description": "Att flytta JW Library-anteckningar till en ny telefon är en säkerhetskopia och en återställning, och appen klarar det på ett par minuter. Här är stegen — plus det enda fall den inte klarar: när den nya telefonen redan har egna anteckningar.",
    "intro": [
        "Det här är enklare än folk väntar sig, och du behöver inget extra verktyg. JW Library har säkerhetskopiering och återställning inbyggt, och det bär över varje anteckning, överstrykning, bokmärke och tagg till den nya telefonen — även mellan Android och iPhone. Gör det medan den gamla enheten fortfarande fungerar, så tar det hela ett par minuter.",
        "Den enda delen att göra medvetet är själva överföringen: verktyg som flyttar innehåll från telefon till telefon tar med appar och foton, men hoppar över JW Librarys personliga studiedata. Skapa alltså säkerhetskopian i stället för att räkna med att den följer med av sig själv.",
        "Det finns exakt en situation appen inte klarar, och den är värd att känna till innan du börjar: har du redan studerat på den nya telefonen raderar en återställning av den gamlas säkerhetskopia det arbetet, eftersom en återställning byter ut enhetens hela bibliotek. Är det din situation är avsnittet om sammanslagning längre ner det du vill ha.",
    ],
    "steps": [
        ("Skapa en säkerhetskopia på den gamla mobilen",
         "Öppna JW Library → Personligt studium → trepunktsmenyn → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia. Det sparar en .jwlibrary-fil med alla dina "
         "studiedata."),
        ("Flytta filen till den nya mobilen",
         "Mejla den till dig själv, eller använd Google Drive, iCloud, AirDrop eller en "
         "USB-kabel. Filen är liten — oftast några megabyte."),
        ("Återställ på den nya mobilen",
         "Installera JW Library och gå sedan till Personligt studium → Säkerhetskopiera och "
         "återställ → Återställ och välj .jwlibrary-filen. Alla anteckningar, markeringar, "
         "bokmärken och etiketter dyker upp."),
    ],
    "sections": [
        ("Redan skrivit anteckningar på den nya mobilen? Slå ihop i stället för att skriva över",
         "En återställning ersätter det som finns på enheten. Om du använt den nya mobilen ett "
         "tag och den har egna anteckningar ska du inte återställa över dem — säkerhetskopiera "
         "även den nya mobilen, slå ihop den gamla och den nya säkerhetskopian till en fil på "
         "jwsync.org (gratis, i webbläsaren, inget laddas upp) och återställ den sammanslagna "
         "filen. Då behåller du båda uppsättningarna anteckningar."),
        ("Ett vanligt problem på iPhone",
         "Om säkerhetskopian når iPhone omdöpt till .zip, döp om den till .jwlibrary innan du "
         "återställer — innehållet är intakt; bara filändelsen ändrades på vägen."),
        ("Gör det här innan den gamla telefonen raderas eller lämnas in",
         "Säkerhetskopian måste skapas medan den gamla telefonen fortfarande fungerar och JW Library finns kvar på den. När enheten återställts, lämnats in eller getts bort försvinner anteckningarna med den: JW Library sparar ingen molnkopia av personliga studiedata, och en telefonkopia som Google One eller en enhetskopia i iCloud återställer ofta en äldre ögonblicksbild av appens data, eller ingen alls. Skapa .jwlibrary-filen först, lägg den på en säker plats och se att du hittar den innan du raderar något."),
        ("Så får du ut filen ur den gamla telefonen",
         "På Android skrivs filen till den mapp du väljer — vanligtvis Nedladdningar eller Dokument — och kan flyttas med vilken filhanterare som helst, mejlas till dig själv eller läggas i molnet. På iPhone visas delningsmenyn så snart kopian skapats: spara den i Filer, skicka den med AirDrop till den nya telefonen eller skicka den till dig själv. Metoden spelar ingen roll och kan inte skada filen: en .jwlibrary är ett enda arkiv som antingen kommer fram helt eller inte alls."),
        ("Varför en överföringsapp mellan telefoner inte räcker",
         "Verktyg som Smart Switch, Flytta till iOS eller en iCloud-återställning kopierar appar och systemdata, men appars egna databaser hoppas ofta över, återställs delvis eller återställs från en tidigare tidpunkt. Luckan upptäcks regelbundet först veckor senare, när den gamla telefonen är borta. Betrakta .jwlibrary-filen som den gällande kopian och telefonöverföringen som en bekvämlighet — om den råkar få med dina anteckningar kostar det ingenting att återställa din egen kopia ovanpå."),
        ("Kontrollera att flytten verkligen fungerade",
         "Öppna två eller tre publikationer du nyligen annoterat på den nya telefonen efter återställningen och se att anteckningar, markeringsfärger och bokmärken finns där. En snabbare kontroll är att öppna själva säkerhetskopian i webbläsaren innan du raderar den gamla enheten — du ser varje anteckning, markering och bokmärke den innehåller och vet därmed vad som borde dyka upp. Radera den gamla telefonen först när den nya är kontrollerad."),
        ("Om du samtidigt byter surfplatta eller dator",
         "Samma fil fungerar överallt. Om du ställer in en ny telefon och en surfplatta samtidigt kan du återställa samma .jwlibrary-fil på båda, så börjar de likadant. Därefter glider de isär igen allteftersom du studerar på var och en, så det är värt att bestämma redan nu om du ska slå ihop dem regelbundet eller behandla en av dem som huvudenhet."),
        ("Om den nya telefonen redan har anteckningar",
         "Det händer när man använt den nya enheten en vecka innan man tar tag i flytten. En rak återställning skulle ersätta det arbetet med den gamla telefonens data. Säkerhetskopiera den nya telefonen först, slå ihop den filen med den gamlas kopia och återställ resultatet — båda uppsättningarna anteckningar hamnar i ett bibliotek i stället för att den ena skriver över den andra."),
        ("Vad du gör när den nya telefonen är igång",
         "Kontrollera innan du gör dig av med något. Öppna några nyligen annoterade publikationer på den nya telefonen och bekräfta att anteckningar, färger och bokmärken finns; radera eller lämna först därefter in den gamla enheten — i den ordningen och aldrig tvärtom. När allt sitter, lägg en säkerhetskopia utanför telefonen, för situationen som förde dig hit återkommer vid nästa byte."),
    ],
    "faq": [
        ("Följer mina nedladdade publikationer med?",
         "Säkerhetskopian innehåller dina personliga studiedata — anteckningar, markeringar, "
         "bokmärken, etiketter och spellistor. Publikationerna laddas helt enkelt ner igen på "
         "den nya mobilen."),
        ("Spelar det roll om mobilerna har olika Android-versioner?",
         "Nej. .jwlibrary-formatet är detsamma överallt, även mellan Android-versioner och "
         "mellan Android och iPhone."),
        ("Kan jag flytta anteckningarna om den gamla telefonen redan är borta?",
         "Bara om det finns en .jwlibrary-fil någonstans — i Filer, Nedladdningar, ett mejl till dig själv eller i molnet. Utan den finns inget att återställa, eftersom personliga studiedata bara lagras på enheten."),
        ("Måste båda telefonerna ha samma version av JW Library?",
         "De behöver inte stämma exakt, men uppdatera den nya telefonen till aktuell version innan du återställer. En kopia skapad av en nyare version kan använda ett databasschema som en äldre app inte förstår."),
        ("Måste jag ladda ner publikationerna igen?",
         "Oftast ja — publikationsmedier ingår inte i säkerhetskopian. Dina anteckningar kopplas tillbaka till varje publikation så snart den laddats ner, så ingenting du skrivit går förlorat under tiden."),
        ("Hur lång tid tar det hela?",
         "Några minuter. Att skapa kopian tar sekunder, att flytta filen beror på metoden och återställningen går snabbt. Det som tar längst är att ladda ner publikationerna igen, och det kan ske i bakgrunden."),
        ("Går det utan wifi?",
         "Själva överföringen ja, via AirDrop eller kabel. Att ladda ner publikationerna igen på den nya enheten kräver uppkoppling."),
    ],
}

GUIDES_SV["jw-library-android-to-iphone"] = {
    "title": "Flytta JW Library från Android till iPhone (behåll alla anteckningar)",
    "h1": "Flytta JW Library från Android till iPhone eller iPad — utan att förlora en anteckning",
    "description": ".jwlibrary-formatet är identiskt på Android och iOS. Så flyttar du dina "
                   "anteckningar, markeringar och bokmärken mellan plattformar — och så slår "
                   "du ihop om båda enheterna har anteckningar.",
    "intro": [
        "Att byta mellan Android och iPhone låter som det svåra fallet, men är det lätta. JW Library skriver samma säkerhetskopieformat på alla plattformar där det körs, så att flytta ett studiebibliotek från Android till iOS är samma sak som att flytta det mellan två Android-telefoner — ingen konvertering, inget exportformat att välja, ingenting som tappas på vägen.",
        "Plattformsbytet är stunden då många är rädda att förlora år av studieanteckningar — "
        "flyttappar från Android till iPhone hoppar helt över JW Librarys data. Den goda "
        "nyheten: JW Librarys säkerhetskopieformat är identiskt på Android, iPhone, iPad och "
        "Windows, så ett plattformsbyte är bara en säkerhetskopia, en filöverföring och en "
        "återställning.",
    ],
    "steps": [
        ("Säkerhetskopiera på Android-mobilen",
         "JW Library → Personligt studium → trepunktsmenyn → Säkerhetskopiera och återställ → "
         "Skapa en säkerhetskopia. Spara .jwlibrary-filen."),
        ("Skicka filen till iPhone eller iPad",
         "E-post, Google Drive, iCloud Drive — vad som helst som flyttar en fil. Om iOS döper "
         "om den till .zip på vägen, döp tillbaka den till .jwlibrary."),
        ("Återställ på den nya enheten",
         "Installera JW Library, logga in och gå till Säkerhetskopiera och återställ → "
         "Återställ och välj filen. Anteckningar, markeringar, bokmärken, etiketter och "
         "spellistor kommer med."),
    ],
    "sections": [
        ("Om iPhone redan har anteckningar",
         "En återställning ersätter enhetens data. När den nya enheten redan har egna "
         "anteckningar ska du säkerhetskopiera även den och först slå ihop båda "
         "säkerhetskopiorna till en fil på jwsync.org — sammanslagningen förenar båda "
         "biblioteken i din webbläsare utan att ladda upp något — och sedan återställa den "
         "sammanslagna filen. Ingenting går förlorat från någon sida."),
        ("Samma steg fungerar åt alla håll",
         "Från iPhone till Android, från Android till Android, när du lägger till en iPad som "
         "andra studieenhet eller när du går över till Windows-appen — säkerhetskopian är det "
         "gemensamma språket för dem alla."),
        ("Varför formatet är identiskt på båda plattformarna",
         "JW Library använder samma säkerhetskopieformat överallt där det körs — Android, iOS, iPadOS och Windows. En .jwlibrary-fil är ett ZIP-arkiv med en SQLite-databas som har samma tabeller och samma schema oavsett vilken enhet som skrivit den. Det finns inget konverteringssteg, ingen turnerande export och import, och ingenting plattformsspecifikt inuti filen. En Android-kopia återställs på en iPhone precis som en iPhone-kopia skulle göra."),
        ("Den enda delen som verkligen skiljer sig",
         "Inte filen — bara hur du får tag i den. På Android sparas kopian i en mapp du väljer och kan flyttas med vilken filhanterare som helst. På iPhone går den via delningsmenyn till Filer, AirDrop eller vad du föredrar. Det som skaver vid ett plattformsbyte sitter alltid i det här hanteringssteget, aldrig i kompatibiliteten. Mejl, moln eller AirDrop fungerar lika bra; arkivet kommer fram helt eller inte alls."),
        ("Markeringsfärger, etiketter och studiesvar",
         "Allt överlever. Markeringsfärger lagras som ett numeriskt index — gult, grönt, blått, rosa, orange och lila — och ser likadana ut på alla plattformar. Etiketter och kopplingarna mellan etiketter och anteckningar följer med, liksom svaren du skrivit i studiefrågornas fält. Det du ser på iPhone efter återställningen är det du hade på Android-enheten."),
        ("Om iOS inte låter dig välja filen",
         "Spara filen i appen Filer först och välj den därifrån, i stället för från en mejlbilaga eller förhandsvisningen i en meddelandeapp. Vissa appar lämnar en tillfällig förhandskopia till iOS i stället för den riktiga filen, och den kan JW Library inte öppna. Om filen kom som bilaga: tryck på den, välj Spara i Filer och återställ därifrån."),
        ("Förbered iPhonen innan du återställer",
         "Installera JW Library från App Store och uppdatera till aktuell version innan du återställer något. En kopia som skrivits av en nyare version kan använda ett databasschema som en äldre version inte förstår, och då avvisas återställningen helt enkelt. Du behöver inte logga in någonstans: personliga studiedata finns i filen du återställer, inte i ett konto."),
        ("Om du redan börjat studera på iPhonen",
         "Säkerhetskopiera iPhonen först. Att återställa Android-filen rakt ovanpå skulle ersätta allt du skrivit sedan bytet. Att slå ihop de två kopiorna ger en fil som innehåller båda, som du sedan återställer — historiken från Android och de nya iPhone-anteckningarna hamnar i samma bibliotek."),
        ("Att fortsätta använda båda telefonerna",
         "Vissa behåller den gamla Android-enheten som en andra läsenhet i stället för att pensionera den. Det fungerar, men de två glider isär så snart du annoterar på båda, eftersom det inte finns någon synkronisering mellan dem. Om du tänker använda båda bör du räkna med att slå ihop deras kopior med jämna mellanrum snarare än att anta att de förblir lika."),
        ("Efter bytet",
         "Ge iPhonen tid att ladda ner de publikationer du använder mest, och kontrollera sedan några annoterade för att bekräfta att allt kommit fram: anteckningar, markeringsfärger, bokmärken och etiketter. Behåll Android-kopian även efter att bytet är klart: den är en daterad ögonblicksbild av ditt bibliotek, och att spara den kostar ingenting."),
    ],
    "faq": [
        ("Behöver jag en dator för det här?",
         "Nej. Hela flytten går att göra mobil till mobil med e-post eller en molntjänst."),
        ("Överlever mina markeringsfärger flytten?",
         "Ja — markeringarna behåller sina färger, anteckningarna sina etiketter och "
         "bokmärkena sina platser."),
        ("Behöver jag en dator för det här?",
         "Nej. AirDrop, mejl eller vilken molntjänstapp som helst flyttar filen direkt mellan de två telefonerna."),
        ("Fungerar det åt andra hållet, från iPhone till Android?",
         "Ja, likadant. Samma steg fungerar i alla riktningar, även till och från Windows-appen."),
        ("Behöver iPhonen samma publikationer nedladdade?",
         "Ja, eftersom publikationsmedier inte ingår i en säkerhetskopia. Anteckningarna kopplas tillbaka till varje publikation så snart den laddats ner."),
        ("Måste jag behålla Android-telefonen efteråt?",
         "Nej, när du kontrollerat att anteckningarna finns på iPhonen. Titta på några annoterade publikationer innan du raderar eller lämnar in den gamla enheten."),
        ("Fungerar överföringen för svaren på studiefrågorna?",
         "Ja. Inskrivna svar är en del av de personliga studiedata och följer med allt annat."),
        ("Finns det någon risk att förlora anteckningar vid bytet?",
         "Inte om du behåller Android-kopian. Återställningen skriver till iPhonen och ändrar aldrig filen den läser, så originalet finns kvar orört som reserv. Behåll det tills du bekräftat att iPhonen har allt, och gärna även efteråt."),
        ("Tänk om Android-telefonen inte skapar någon säkerhetskopia?",
         "Kontrollera ledigt utrymme först, eftersom appen behöver plats att skriva filen. Om det är appen själv som krånglar brukar en uppdatering eller en omstart av enheten lösa det. Dina data är oförändrade under tiden."),
    ],
}

GUIDES_SV["backup-jw-library"] = {
    "title": "Så säkerhetskopierar du JW Library på rätt sätt",
    "h1": "Så säkerhetskopierar du JW Library på rätt sätt",
    "description": "En säkerhetskopiering på 30 sekunder: vad en .jwlibrary-fil faktiskt innehåller, var du ska förvara den, och varför en aktuell är värd att ha även när inget har gått fel.",
    "intro": [
        "En säkerhetskopia tar en halv minut och är värd att göra till vana — om än inte riktigt av det skäl man brukar höra. JW Librarys egen säkerhetskopiering och återställning flyttar redan ett bibliotek till en ny enhet alldeles utmärkt, så en säkerhetskopia är mindre en försäkring än råmaterialet för allt annat du kan vilja göra med ditt studium.",
        "En .jwlibrary-fil är den enda form ditt bibliotek antar utanför appen. Det är den du slår ihop när två enheter båda har studerats på, den du öppnar för att läsa, tagga om eller ordna år av anteckningar, den du söker i efter betydelse när du bara halvt minns vad du skrev, och den du hämtar ett urval anteckningar ur när du vill skicka några till en vän. Att ha en aktuell är det som gör allt det möjligt.",
    ],
    "steps": [
        ("Skapa säkerhetskopian",
         "Öppna JW Library → Personligt studium → trepunktsmenyn → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia. Det ger en .jwlibrary-fil med varje anteckning, "
         "markering, bokmärke och etikett."),
        ("Förvara den någon annanstans än i mobilen",
         "Mejla den till dig själv, eller spara den i Google Drive, iCloud eller OneDrive. En "
         "säkerhetskopia som bara finns i mobilen försvinner med mobilen."),
        ("Upprepa regelbundet",
         "En gång i månaden är ett bra riktmärke; före varje enhetsbyte, återställning eller "
         "systemuppdatering är det nödvändigt. Behåll äldre kopior — filerna är små, och en "
         "gammal säkerhetskopia har räddat många."),
    ],
    "sections": [
        ("Det vanliga misstaget: att lita på mobilens egen molnkopia",
         "En säkerhetskopia av hela mobilen (Google One, iCloud-enhetskopia) återställer ofta "
         "en gammal version av JW Librarys data — eller ingen alls. .jwlibrary-filen är den "
         "enda säkerhetskopia du själv styr helt över och kan ta med mellan plattformar. Se "
         "mobilens säkerhetskopia som en bonus, inte som planen."),
        ("Har du fått två olika säkerhetskopior?",
         "Det händer: en från mobilen, en äldre från surfplattan, båda med egna anteckningar. "
         "Du behöver aldrig välja mellan dem — slå ihop dem till en komplett fil på "
         "jwsync.org, gratis och privat, direkt i webbläsaren."),
        ("Vad filen innehåller och vad den inte innehåller",
         "Säkerhetskopian bevarar dina personliga studiedata: anteckningar, markeringar och deras färger, bokmärken, etiketter och svaren du skrivit in i studiefrågornas fält. Den bevarar inte publikationerna — varken biblar, tidskrifter, böcker, video eller ljud. Det är därför en kopia av många års studium bara upptar några megabyte, och därför en återställning på en ny enhet lämnar dig att ladda ner publikationer medan varje anteckning du skrivit redan är tillbaka på sin plats."),
        ("Hur många kopior du bör spara",
         "Fler än en. Det som kostar folk deras anteckningar är sällan en förlorad fil — det är en bra kopia som skrivits över av en dålig, eller en återställning som gjorts på fel enhet. Eftersom filerna är små finns ingen anledning att radera de gamla: spara dem daterade i en mapp i molnet. En kopia från ett halvår tillbaka blir inte värdelös bara för att du har nyare, för allt du råkat radera sedan dess finns fortfarande kvar i den."),
        ("Var du sparar dem",
         "Var som helst utom bara på enheten själv. En mapp i Drive, iCloud, Dropbox eller OneDrive täcker det fall som betyder mest — att enheten tappas bort, blir stulen, återställs eller går sönder. Att mejla filen till dig själv fungerar också och har den nyttiga bieffekten att den blir daterad. Filen innehåller dina egna studieanteckningar, så hantera den lika omsorgsfullt som vilket personligt dokument som helst."),
        ("Kontrollera en säkerhetskopia innan du litar på den",
         "En säkerhetskopia du aldrig öppnat är ett antagande, inte ett skyddsnät. Du kan öppna en .jwlibrary-fil i webbläsaren och se exakt vilka anteckningar, markeringar och bokmärken den innehåller — en kontroll på trettio sekunder som gör antagandet till ett faktum. Det spelar störst roll strax före något oåterkalleligt: en fabriksåterställning, en inbytesaffär, en reparation eller en större systemuppdatering."),
        ("Tillfällena det är värt att säkerhetskopiera inför",
         "Varje tillfälle då enheten byter ägare eller tillstånd: en systemuppdatering, en fabriksåterställning, en reparation eller ett skärmbyte, ett inbyte, eller att enheten ges vidare. Lägg till slutet på allt du skulle ogilla att göra om — en sammankomst, ett kretsbesök, en period av talförberedelse. Säkerhetskopior går snabbt och kostar lite, så den användbara vanan är att knyta dem till händelser snarare än till kalendern."),
        ("En telefonkopia är inte en JW Library-kopia",
         "Google One, en enhetskopia i iCloud eller tillverkarens överföringsverktyg arbetar på enhetsnivå och behandlar appars egna data ojämnt. Det visar sig regelbundet att en fullständig telefonåterställning gav tillbaka appar och inställningar men inte studieanteckningarna, eller gav tillbaka en version från flera veckor tidigare. .jwlibrary-filen är den enda kopia vars innehåll du styr över och kan kontrollera, så betrakta telefonkopian som en bonus och inte som planen."),
        ("Gör det till en vana som håller",
         "Rutinen som verkligen håller är den som hänger på något du redan gör: säkerhetskopiera när du är klar med veckans förberedelse, eller samma dag som du sköter andra återkommande sysslor. Spara alltid i samma mapp så att filerna samlas på ett ställe, och låt de gamla ligga kvar. En mapp med daterade kopior som sträcker sig år tillbaka är den mest robusta formen av det här, och att underhålla den tar sekunder i veckan."),
    ],
    "faq": [
        ("Hur stor är en säkerhetskopia?",
         "Oftast några megabyte även för mycket stora bibliotek — litet nog för en "
         "e-postbilaga."),
        ("Ändras något i mobilen när jag skapar en säkerhetskopia?",
         "Nej. Den skriver bara filen; ditt bibliotek rörs inte."),
        ("Ingår mina nedladdade publikationer i säkerhetskopian?",
         "Nej. Bara personliga studiedata. Publikationerna laddas ner igen på den nya enheten, och dina anteckningar kopplas tillbaka till dem automatiskt."),
        ("Kan jag öppna en säkerhetskopia för att se vad som finns i den?",
         "Ja. Du kan öppna en .jwlibrary-fil i webbläsaren och bläddra bland alla anteckningar, markeringar och bokmärken den innehåller, utan att installera något och utan att filen lämnar din enhet."),
        ("Slutar säkerhetskopior gälla?",
         "Nej. En .jwlibrary-fil går att återställa hur länge som helst. Återställ i en aktuell version av JW Library snarare än en gammal, eftersom appen läser äldre kopieformat men inte nyare."),
        ("Bör jag säkerhetskopiera före varje möte?",
         "Det behövs inte. Knyt kopiorna till händelser som skulle kunna kosta dig data — uppdateringar, reparationer, nya enheter — plus en regelbunden takt som motsvarar hur mycket studium du skulle ogilla att göra om."),
        ("Är det värt att spara kopior från flera år tillbaka?",
         "Ja. De är små, och allt du råkat radera sedan dess finns fortfarande kvar i dem."),
    ],
}

GUIDES_SV["jw-library-restore-replaced-notes"] = {
    "title": "Ersatte återställningen i JW Library dina anteckningar? Så får du dem tillbaka",
    "h1": "Ersatte återställningen dina anteckningar? Så förenar du båda säkerhetskopiorna",
    "description": "Återställningen i JW Library är ett fullständigt utbyte, inte en "
                   "sammanslagning — anteckningar skrivna efter säkerhetskopians datum verkar "
                   "borta. Om du fortfarande har båda filerna är ingenting förlorat. Så här "
                   "löser du det.",
    "intro": [
        "Det är ett obehagligt ögonblick: du återställer en säkerhetskopia på en enhet som "
        "redan hade anteckningar, och återställningen ersätter allt — anteckningarna du skrivit "
        "sedan den säkerhetskopian verkar borta. Det beror på att JW Librarys Säkerhetskopiera "
        "och återställ är ett fullständigt utbyte, inte en sammanslagning.",
        "Det avgörande: om det nyare arbetet fortfarande finns i någon säkerhetskopia är "
        "ingenting egentligen förlorat. Lösningen är att slå ihop de två säkerhetskopiorna i "
        "stället för att välja mellan dem.",
    ],
    "steps": [
        ("Stopp — återställ inte igen",
         "Varje återställning ersätter enhetens nuvarande data. Pausa innan något mer "
         "försvinner."),
        ("Säkerhetskopiera enheten som den är just nu",
         "Personligt studium → Säkerhetskopiera och återställ → Skapa en säkerhetskopia. Det "
         "bevarar det nuvarande läget, vad det än innehåller."),
        ("Hitta säkerhetskopian med de saknade anteckningarna",
         "Den .jwlibrary-fil du återställde från, eller en tidigare — leta i e-posten, Drive, "
         "iCloud och nedladdningsmappen."),
        ("Slå ihop båda filerna på jwsync.org",
         "Ladda in båda säkerhetskopiorna. JW Sync förenar alla anteckningar, markeringar, "
         "bokmärken och etiketter från båda till en ny fil — i webbläsaren, inget laddas upp. "
         "Motstridiga versioner av samma anteckning visas sida vid sida så att du väljer."),
        ("Återställ den sammanslagna filen",
         "Säkerhetskopiera och återställ → Återställ med den sammanslagna .jwlibrary-filen. "
         "Båda uppsättningarna anteckningar är tillbaka på enheten."),
    ],
    "sections": [
        ("Tänk om det inte finns någon säkerhetskopia av de nyare anteckningarna?",
         "Om den enda kopian av de nyare anteckningarna fanns på enheten och en återställning "
         "redan skrivit över dem finns ingen ångerfunktion i JW Library. Det är just därför "
         "steg 2 ovan — att säkerhetskopiera det nuvarande läget innan något annat görs — "
         "spelar så stor roll så fort data ser fel ut. Framöver gör rutinen ”slå ihop först” "
         "problemet strukturellt omöjligt."),
    ],
    "faq": [
        ("Blir anteckningar som finns i båda säkerhetskopiorna dubblerade?",
         "Nej — identiska poster upptäcks och behålls en gång. Bara verkligt olika versioner av "
         "samma anteckning lyfts fram för granskning."),
        ("Löser det här en säkerhetskopia som inte går att återställa alls?",
         "Det är oftast en skadad fil snarare än överskrivning — se guiden om att reparera en "
         "skadad säkerhetskopia nedan."),
    ],
}

GUIDES_SV["fix-corrupted-jw-library-backup"] = {
    "title": "Reparera en skadad JW Library-säkerhetskopia som inte går att återställa",
    "h1": "Reparera en skadad JW Library-säkerhetskopia med Biblioteksdoktorn",
    "description": "Vägrar JW Library ta emot din .jwlibrary-fil? Biblioteksdoktorn granskar "
                   "säkerhetskopian i din webbläsare, reparerar de vanliga problemen och ger "
                   "dig en ren kopia som går att återställa.",
    "intro": [
        "En säkerhetskopia som inte går att återställa är inte nödvändigtvis en kopia som förlorat dina anteckningar. De flesta filer folk beskriver som skadade är strukturellt hela och avvisas av ett åtgärdbart skäl, eller har tagit skada under överföringen på ett sätt som en ny kopia löser. Det är värt att gå igenom orsakerna innan du skriver av filen.",
        "Ibland vägrar JW Library en säkerhetskopia — återställningen misslyckas, ger ett fel "
        "eller så går filen inte att öppna. Vanliga orsaker: en avbruten nedladdning, en "
        "molntjänst som förvanskat filen, en filändelse som ändrats på vägen, eller inre "
        "inkonsekvenser som samlats under årens lopp.",
        "JW Sync har Biblioteksdoktorn, en kontroll som granskar en .jwlibrary-fil och "
        "reparerar de vanliga problemen — helt i din webbläsare, utan att filen någonsin lämnar "
        "din enhet.",
    ],
    "steps": [
        ("Öppna JW Sync och ladda in den problematiska filen",
         "Gå till jwsync.org och ladda in .jwlibrary-filen som inte går att återställa. (Om "
         "filen kom omdöpt till .zip, döp först tillbaka den till .jwlibrary — bara det löser "
         "många fall.)"),
        ("Kör Biblioteksdoktorns granskning",
         "Doktorn undersöker säkerhetskopians inre struktur och listar i klarspråk vad den "
         "hittar — från harmlösa egenheter till verkliga skador."),
        ("Använd reparationerna",
         "Ett tryck reparerar det som går att reparera. Doktorn ändrar aldrig din ursprungliga "
         "fil; den skapar en rensad kopia, så originalet finns kvar orört som reserv."),
        ("Ladda ner och återställ den reparerade filen",
         "Återställ den rensade .jwlibrary-filen via Säkerhetskopiera och återställ → Återställ "
         "i JW Library."),
    ],
    "sections": [
        ("Doktorn körs också vid varje sammanslagning",
         "Samma kontroller körs automatiskt i sammanslagningsmotorn, så en sammanslagen "
         "säkerhetskopia levereras alltid ren — även när en av filerna hade problem du inte "
         "kände till."),
        ("När en fil inte går att rädda",
         "Om filen kapats så illa att uppgifterna helt enkelt inte finns kvar kan inget verktyg "
         "uppfinna dem igen. Doktorn säger det ärligt i stället för att lämna ifrån sig en "
         "tvivelaktig fil — och det är signalen att leta efter en tidigare kopia i e-posten, "
         "Drive eller iCloud, vilket också är skälet att spara gamla säkerhetskopior."),
        ("Vad skadad brukar betyda",
         "I praktiken handlar det sällan om trasiga data. De vanliga orsakerna är en fil som kapats under överföringen — förkortad av en misslyckad uppladdning eller av en meddelandeapp som komprimerat den — eller ett arkiv som är helt men innehåller inre motsägelser som appen avvisar. Eftersom en .jwlibrary är ett ZIP runt en SQLite-databas kan problemet sitta i vilket av de två lagren som helst, och de kräver olika åtgärder: en kapad fil går inte att reparera och måste hämtas på nytt; en motsägelsefull databas går oftast att reparera."),
        ("Vad en genomsökning faktiskt kontrollerar",
         "En genomsökning verifierar att arkivet öppnas, att userData.db är en läsbar SQLite-databas som klarar en integritetskontroll, att schemat motsvarar det JW Library förväntar sig, och att manifestet stämmer med databasen det beskriver — inklusive den kontrollsumma appen använder för att bekräfta att filen inte ändrats. En avvikelse mellan manifest och databas är ett av de vanligaste skälen till att en tekniskt felfri kopia avvisas vid återställning, och det går att åtgärda direkt."),
        ("Föräldralösa rader är oftast ofarliga",
         "En genomsökning av en verklig kopia rapporterar ofta rader som pekar på något som inte längre finns — till exempel en markering som pekar på en plats i en publikation som flyttats. JW Librarys egna kopior innehåller rutinmässigt hundratals sådana och återställs utan invändningar. De är en normal följd av att publikationer uppdateras med tiden, inte ett tecken på skada, och de behöver inte rensas för att filen ska fungera."),
        ("Rädda anteckningar ur en fil som inte går att återställa",
         "Även när en kopia inte kan repareras tillräckligt för att JW Library ska acceptera den är anteckningarna inuti ofta fortfarande läsbara. Att öppna filen i webbläsaren låter dig se och kopiera texten direkt, vilket förvandlar en oanvändbar fil till räddat studiematerial. Har du en andra, äldre kopia som går att återställa kan det läsbara innehållet från den skadade föras samman med den i stället för att skrivas av."),
        ("När återställningen misslyckas utan tydligt felmeddelande",
         "JW Library avvisar ofta en fil utan att förklara varför. Vanligast är ett manifest vars kontrollsumma inte längre stämmer med databasen det beskriver, en fil som kapats under överföringen, eller en kopia skriven av en nyare appversion än den du återställer i. Det första går att åtgärda, det andra kräver att filen hämtas på nytt från källan, och det tredje löses genom att uppdatera appen före återställningen."),
        ("Undvik det nästa gång",
         "Merparten av skadorna uppstår under transporten. Flytta kopior som filer och inte via något som kan komprimera om dem, och välj molnet, AirDrop eller en kabel framför meddelandeappar. Kontrollera efter överföringen att storleken stämmer med originalet — en fil som är märkbart mindre än den du skickade har kapats, och ingen reparation ger tillbaka byte som aldrig kom fram."),
        ("Om ingenting fungerar",
         "En fil som inte går att reparera kan ändå vara läsbar, och att läsa den räcker ofta — anteckningstexten går att rädda direkt även när JW Library avvisar filen. Kombinera det med en äldre kopia som går att återställa så har du oftast merparten av biblioteket kvar. Innan du dömer ut en fil: öppna den och se vad som faktiskt finns i den."),
    ],
    "faq": [
        ("Laddas mina data upp för granskningen?",
         "Nej. Granskningen, reparationerna och exporten sker alla lokalt i webbläsaren."),
        ("Kan den återskapa anteckningar som raderats inne i JW Library?",
         "Nej — den reparerar filens struktur. Anteckningar som raderats i appen innan "
         "säkerhetskopian skapades finns inte i filen att återskapa."),
        ("Går några anteckningar förlorade när filen repareras?",
         "Reparationer arbetar på en kopia och rör strukturella problem, inte innehåll. Din originalfil ändras aldrig, så den finns kvar om du vill börja om."),
        ("Varför blev min säkerhetskopia skadad?",
         "Oftast ändrades filen under transporten — skickad via en app som komprimerade eller kapade den, eller en uppladdning som inte blev klar. Att överföra filen på nytt från källan brukar lösa det."),
        ("Kan en genomsökning rädda anteckningar jag raderat inuti JW Library?",
         "Nej. När den raderats i appen och en ny kopia tagits finns anteckningen inte kvar i den filen. En kopia från före raderingen innehåller den fortfarande."),
        ("Kan filstorleken avslöja om den är kapad?",
         "Ofta ja. Jämför med originalet om du har det kvar; en tydlig skillnad betyder att överföringen inte slutfördes."),
        ("Går en kopia som öppnas i webbläsaren garanterat att återställa?",
         "Inte garanterat, men det är ett starkt tecken på att arkivet och databasen är hela, vilket utesluter de vanligaste felen."),
    ],
}

GUIDES_SV["edit-jw-library-notes"] = {
    "title": "Visa och redigera JW Library-anteckningar i webbläsaren",
    "h1": "Visa, sök och redigera dina JW Library-anteckningar — Studieutforskaren",
    "description": "Öppna vilken .jwlibrary-säkerhetskopia som helst i webbläsaren för att "
                   "bläddra, söka, redigera, etikettera om, färga om och storstäda dina "
                   "anteckningar, markeringar och bokmärken i JW Library. Inget laddas upp.",
    "intro": [
        "JW Library är byggt för att skriva anteckningar, inte för att hantera tusentals av "
        "dem. Studieutforskaren öppnar vilken .jwlibrary-säkerhetskopia som helst direkt i "
        "webbläsaren och gör den till en sökbar och redigerbar bibliotekshanterare — "
        "anteckningar, markeringar och bokmärken på ett ställe, och ingenting laddas upp någon "
        "annanstans.",
    ],
    "steps": [
        ("Ladda in en säkerhetskopia",
         "Skapa en säkerhetskopia i JW Library (Personligt studium → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia), öppna sedan jwsync.org och ladda in filen i "
         "Studieutforskaren."),
        ("Bläddra och sök i allt",
         "Tre flikar — Anteckningar, Markeringar, Bokmärken — med fritextsökning samt filter "
         "för färg, etikett och publikation. En flik för Studiesvar visar också svaren du "
         "skrivit in i publikationerna."),
        ("Redigera på plats",
         "Öppna vilken anteckning som helst för att redigera rubrik och innehåll med formatering "
         "(fet, kursiv, understruken, listor), byta markeringsfärg och lägga till eller ta bort "
         "etiketter. Bokmärken och markeringsfärger redigeras på samma sätt."),
        ("Storstäda",
         "Markera många anteckningar samtidigt för att etikettera om, färga om eller radera "
         "dem tillsammans — med full ångra och gör om, så ett felgrepp är aldrig ödesdigert. Du "
         "kan också plocka ut ett datumintervall av anteckningar till en ny säkerhetskopia, "
         "eller kopiera ut anteckningarna som Markdown."),
        ("Exportera ditt redigerade bibliotek",
         "Ladda ner den redigerade .jwlibrary-filen och återställ den i JW Library. Nu finns "
         "dina ändringar på enheten."),
    ],
    "sections": [
        ("Varför redigera i en webbläsare i stället för i appen?",
         "Skalan. Att byta namn på en etikett över 300 anteckningar, färga om varje gul "
         "markering i en publikation eller radera år av inaktuella bokmärken tar minuter här "
         "och timmar av tryckande i appen. Den exporterade filen är en helt vanlig "
         "säkerhetskopia som JW Library återställer som vilken annan som helst."),
    ],
    "faq": [
        ("Påverkar redigeringen min ursprungliga säkerhetskopia?",
         "Nej — ändringarna görs i en kopia i webbläsaren och sparas i en ny exporterad fil. "
         "Originalet är kvar som det var."),
        ("Finns det någon gräns för bibliotekets storlek?",
         "Mycket stora bibliotek delas upp i sidor så att bläddrandet förblir snabbt; sökning "
         "och filter arbetar över allt."),
    ],
}

GUIDES_SV["search-jw-library-notes"] = {
    "title": "Sök i JW Library-anteckningar efter innebörd — Fråga ditt bibliotek",
    "h1": "Fråga ditt bibliotek: sök i dina JW Library-anteckningar efter innebörd",
    "description": "Semantisk sökning för dina JW Library-anteckningar: hitta den halvt "
                   "ihågkomna anteckningen genom att beskriva den, även när du inte minns de "
                   "exakta orden. På enheten, fungerar offline, privat.",
    "intro": [
        "Alla med år av anteckningar känner igen problemet: du minns att du skrivit om att "
        "uthärda prövningar med glädje, men ordet ”uthållighet” står inte i anteckningen, så "
        "sökning på nyckelord hittar ingenting. Fråga ditt bibliotek söker i stället efter "
        "innebörd — beskriv tanken, så lyfts de närmaste anteckningarna fram, hur de än är "
        "formulerade.",
        "Allt körs på din enhet: språkmodellen laddas ner en gång till webbläsaren och fungerar "
        "sedan offline, med WebGPU-acceleration där den finns. Dina anteckningar skickas aldrig "
        "någonstans.",
    ],
    "steps": [
        ("Ladda in en säkerhetskopia i Studieutforskaren",
         "På jwsync.org, ladda in din .jwlibrary-fil och öppna fliken Fråga."),
        ("Låt modellen förbereda sig en gång",
         "Vid första användningen laddas modellen ner till enheten och indexerar dina "
         "anteckningar. Det sker en gång; därefter går det direkt, även offline."),
        ("Fråga med dina egna ord",
         "Skriv det du minns — ”den där anteckningen om att vara tålmodig med nya i tjänsten”, "
         "”uppmuntran till modfällda pionjärer” — så dyker de närmaste anteckningarna upp, "
         "rangordnade efter innebörd."),
    ],
    "sections": [
        ("Hur den skiljer sig från vanlig sökning",
         "Nyckelordssökning jämför bokstäver; semantisk sökning jämför tankar. En fråga om "
         "”oro” hittar också anteckningar skrivna med ”bekymmer”, ”livets bekymmer” eller en "
         "bibelhänvisning i ämnet. Båda söksätten finns i Studieutforskaren — de kompletterar "
         "varandra."),
        ("Privat genom sin konstruktion",
         "Det här är ingen AI-tjänst i molnet. Modellen körs i din webbläsarflik, indexet "
         "ligger på din enhet, och när du stänger fliken är det slut. Ingenting om dina "
         "anteckningar lämnar någonsin din maskin."),
    ],
    "faq": [
        ("Krävs det en kraftfull enhet?",
         "En modern mobil eller laptop klarar det bra; på enheter med WebGPU går det snabbast. "
         "Det finns flera modellstorlekar att välja mellan efter din hårdvara."),
        ("Fungerar det på mitt språk?",
         "Ja — sökningen fungerar på de språk dina anteckningar är skrivna på, och gränssnittet "
         "är översatt till alla 12 språk som JW Sync stöder."),
    ],
}

GUIDES_SV["jw-library-study-stats"] = {
    "title": "Se din JW Library-studiestatistik: svit, värmekarta och utmärkelser",
    "h1": "Din JW Library-studiestatistik: sviter, värmekartor, täckning och utmärkelser",
    "description": "Gör en JW Library-säkerhetskopia till privat studiestatistik — summor, "
                   "aktivitetsvärmekarta, sviter, bibeltäckning över alla 66 böcker, en "
                   "studieprofil och omkring 200 utmärkelser.",
    "intro": [
        "Din säkerhetskopia registrerar i tysthet år av studiehistorik — när du skriver "
        "anteckningar, vad du markerar, vilka böcker du gått igenom. Sidan Studiestatistik "
        "läser en .jwlibrary-säkerhetskopia och gör den historiken till en privat "
        "översiktsvy, helt uträknad i din webbläsare.",
    ],
    "steps": [
        ("Skapa en säkerhetskopia",
         "I JW Library: Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia."),
        ("Öppna sidan Studiestatistik",
         "Gå till jwsync.org/highlights.html och ladda in filen."),
        ("Utforska din studiehistoria",
         "De stora summorna, vyer för tjänsteår och för hela tiden, tillväxt år för år — och "
         "längre ner de roliga delarna."),
    ],
    "sections": [
        ("Vad du får se",
         "En aktivitetsvärmekarta med din längsta och din pågående svit; veckorytm, mest "
         "intensiva timmar och månader; bibeltäckning över alla 66 böcker med uppdelning på "
         "hebreiska och grekiska skrifterna; ett färghjul för markeringar, ett histogram över "
         "anteckningarnas djup och ett ordmoln; en studieklocka över dygnets 24 timmar och en "
         "säsongsradar."),
        ("Profil, resa och utmärkelser",
         "En studieprofil med sex egenskaper (Regelbundenhet, Flit, Djup, Bredd, Eftertanke, "
         "Stadga) och en ”studiesignatur”; en studieresa med 60 nivåer i 12 namngivna steg; och "
         "omkring 200 utmärkelser från Vanlig till Legendarisk, inklusive innehållsmedvetna "
         "medaljer. Ett delbart kort sammanfattar ditt år utan att avslöja en enda anteckning."),
        ("Ett dagligt skäl att komma tillbaka",
         "Panelen Återblick visar anteckningar du skrev den här dagen tidigare år och bygger en "
         "mjuk repetition med mellanrum — lite, men ofta, är så studiet sätter sig."),
    ],
    "faq": [
        ("Laddas något av det här upp?",
         "Nej. Säkerhetskopian tolkas i din webbläsare; statistiken lämnar aldrig din enhet."),
        ("Uppdateras statistiken automatiskt?",
         "Den speglar den säkerhetskopia du laddar in — skapa en ny säkerhetskopia för färsk "
         "statistik."),
    ],
}

GUIDES_SV["share-jw-library-notes"] = {
    "title": "Så delar du JW Library-anteckningar med en vän",
    "h1": "Så delar du JW Library-anteckningar med en vän — helt utan server",
    "description": "Skicka utvalda JW Library-anteckningar (och deras markeringar) till en vän "
                   "som en liten fil — ingen server, inget konto. Mottagaren lägger till dem "
                   "utan att skriva över sina egna.",
    "intro": [
        "JW Library har inget sätt att ge någon annan en kopia av vissa anteckningar. Att "
        "skicka hela säkerhetskopian skulle fungera — men då lämnar du ifrån dig allt, och att "
        "återställa den skulle radera mottagarens bibliotek. JW Syncs anteckningsdelning löser "
        "båda problemen: du väljer exakt vilka anteckningar som ska delas, och mottagaren "
        "lägger till dem utan att förlora något.",
    ],
    "steps": [
        ("Välj anteckningarna som ska delas",
         "På delningssidan jwsync.org/share.html laddar du in din säkerhetskopia och markerar "
         "anteckningarna — några från ett tal, eller allt under en etikett med ett klick via "
         "etikettfiltret i väljaren. Markeringar som hör till de anteckningarna följer med."),
        ("Skicka delningsfilen",
         "JW Sync skapar en liten fil som bara innehåller de valda anteckningarna. Skicka den "
         "hur du vill — meddelandeapp, e-post, AirDrop. Det finns ingen server och inget konto; "
         "filen är hela utbytet."),
        ("Mottagaren lägger till den",
         "Din vän öppnar samma sida, laddar in delningsfilen tillsammans med sin egen "
         "säkerhetskopia och får en ny säkerhetskopia med dina anteckningar tillagda. Hans egna "
         "anteckningar skrivs aldrig över — om en delad anteckning krockar med en av hans "
         "väljer han hur den ska läggas till — och importerade anteckningar kommer etiketterade "
         "så att de är lätta att hitta, gå igenom eller ta bort senare."),
    ],
    "sections": [
        ("Bra användningar",
         "Att lämna över efterforskningar till en studiekamrat, dela mötesanteckningar med "
         "någon som var borta, ge en ny förkunnare en första uppsättning anteckningar till en "
         "publikation, eller flytta anteckningarna från ett visst projekt till en "
         "familjemedlem — allt utan att blotta resten av något av biblioteken."),
    ],
    "faq": [
        ("Behöver mottagaren installera JW Sync?",
         "Ingenting installeras på någondera sidan — det är en webbsida. Mottagaren behöver "
         "bara delningsfilen och sin egen säkerhetskopia."),
        ("Kan jag ta tillbaka en delning eller låta filen gå ut?",
         "Filen är en helt vanlig fil som du skickat — det finns ingen serverkopia som kan "
         "upphöra. Dela bara sådant du skulle dela i vilket meddelande som helst."),
    ],
}

GUIDES_SV["bible-reading-plan"] = {
    "title": "En daglig bibelläsningsplan med dina egna anteckningar bredvid",
    "h1": "Läsledsagaren: en bibelläsningsplan med dina egna anteckningar bredvid",
    "description": "Ett privat dagligt bibelläsningsschema som visar de anteckningar och "
                   "markeringar du gjort i dagens kapitel. Välj takt, håll en svit och se "
                   "rutnätet med 66 böcker fyllas i.",
    "intro": [
        "Många appar erbjuder ett bibelläsningsschema. Läsledsagaren gör något ingen av dem "
        "kan: eftersom den läser din egen .jwlibrary-säkerhetskopia kommer dagens läsning med "
        "de anteckningar och markeringar du själv gjort i just de kapitlen — ”du markerade fyra "
        "verser i Psalm 37 för två år sedan”. Att läsa genom linsen av din egen studiehistoria, "
        "helt på din enhet.",
    ],
    "steps": [
        ("Välj ordning och takt",
         "Läs i bibelordning eller i ungefärlig kronologisk ordning; bli klar på 3 månader, 6 "
         "månader, 1 år, 2 år, eller sätt din egen takt i kapitel per dag — med en löpande "
         "förhandsvisning av ”du skulle bli klar omkring…”."),
        ("Läs dagens del",
         "Varje kapitel är ett tryck bort och öppnas direkt i JW Library eller i Vakttornets "
         "ONLINEBIBLIOTEK på ditt språk. Bocka av kapitlen efter hand."),
        ("Ta med dina anteckningar (valfritt)",
         "Ladda in en säkerhetskopia i vilket JW Sync-verktyg som helst, så dyker dina egna "
         "anteckningar och antalet markeringar upp direkt under dagens kapitel."),
        ("Se hur framstegen växer",
         "Ett rutnät med 66 böcker fylls i medan du läser, med en stapel över lästa kapitel, en "
         "prognos utifrån takten och milstolpar för varje avslutad bok, för de "
         "hebreisk-arameiska skrifterna, för de grekiska skrifterna — och för hela Bibeln."),
    ],
    "sections": [
        ("Sviter utan dåligt samvete",
         "Att fullborda en dag förlänger din svit; att missa en dag flyttar bara fram det "
         "beräknade slutdatumet. Det byggs ingen skuldhög — planen böjer sig efter ditt liv i "
         "stället för att läxa upp dig."),
    ],
    "faq": [
        ("Måste jag ladda in en säkerhetskopia för att använda den?",
         "Nej — planen, sviterna och framstegen fungerar på egen hand. Säkerhetskopian lägger "
         "bara till dina personliga anteckningar till varje dags läsning."),
        ("Är mina läsframsteg privata?",
         "Ja. Framstegen ligger i webbläsaren på din enhet — det finns inget konto och "
         "ingenting laddas upp."),
    ],
}

GUIDES_SV["open-jwlibrary-file"] = {
    "title": "Vad är en .jwlibrary-fil och hur öppnar man den?",
    "h1": "Vad en .jwlibrary-fil är — och hur du öppnar en på vilken enhet som helst",
    "description": "En .jwlibrary-fil är din JW Library-säkerhetskopia: en enda fil med varje "
                   "anteckning, markering, bokmärke och etikett. Här är vad den innehåller och "
                   "hur du öppnar och läser den.",
    "intro": [
        "En .jwlibrary-fil ser ogenomtränglig ut, och är det inte. Den är ett helt vanligt ZIP-arkiv runt en helt vanlig SQLite-databas, vilket betyder att du kan läsa din egen säkerhetskopia — se exakt vilka anteckningar, markeringar och bokmärken den innehåller — utan JW Library och utan att installera någonting alls.",
        "När du säkerhetskopierar JW Library får du en fil som slutar på .jwlibrary. Det är ett "
        "enda, flyttbart paket som innehåller allt från ditt personliga studium — anteckningar, "
        "markeringar, bokmärken, etiketter och spellistor — i en kompakt databas. Det är inget "
        "dokument du öppnar i Word eller en PDF-läsare; det är gjort för att återställas "
        "tillbaka in i JW Library.",
        "Men du behöver inte återställa den bara för att titta inuti. JW Sync öppnar en "
        ".jwlibrary-fil direkt i din webbläsare så att du kan läsa, söka i och redigera "
        "innehållet utan att röra mobilen.",
    ],
    "steps": [
        ("Skaffa en .jwlibrary-fil",
         "Den skapas i JW Library: Personligt studium → trepunktsmenyn → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia. Det är den filen vi pratar om."),
        ("Öppna den i JW Sync",
         "Gå till jwsync.org och ladda in filen i Studieutforskaren. Den öppnas direkt, på din "
         "enhet — ingenting laddas upp."),
        ("Läs och arbeta med den",
         "Bläddra bland anteckningar, markeringar och bokmärken; sök i allt; redigera, "
         "etikettera om eller exportera. När du är klar kan du återställa filen (eller en "
         "redigerad kopia) tillbaka in i JW Library."),
    ],
    "sections": [
        ("Vad som faktiskt finns i filen",
         "Tekniskt sett är en .jwlibrary-fil en zippad SQLite-databas plus ett manifest. Det är "
         "därför den ibland av misstag döps om till .zip på vägen — och därför det löser sig "
         "att döpa tillbaka den till .jwlibrary. Du behöver aldrig veta något av det för att "
         "använda den, men det förklarar varför filen är liten, självständig och identisk på "
         "Android, iPhone, iPad och Windows."),
        ("Att öppna den på en dator",
         "Samma sida jwsync.org fungerar i webbläsaren på en laptop eller stationär dator — "
         "praktiskt för att läsa år av anteckningar på en stor skärm, eller för storstädning "
         "som skulle vara tröttsam på mobilen. Inget behöver installeras."),
        ("Vad filen faktiskt är",
         "En .jwlibrary-fil är ett ZIP-arkiv med en annan filändelse. Inuti finns userData.db — en SQLite-databas med dina anteckningar, markeringar, bokmärken och etiketter — och manifest.json, en liten fil som beskriver kopian och innehåller en kontrollsumma för databasen som JW Library använder för att bekräfta att filen inte ändrats. Ingenting i den är proprietärt eller krypterat; det är ett standardarkiv runt en standarddatabas."),
        ("Öppna den utan JW Library",
         "Du behöver varken appen eller någon programvara för att läsa din egen säkerhetskopia. Att öppna filen i webbläsaren visar alla anteckningar, markeringar och bokmärken den innehåller, med sökning och filtrering, och filen lämnar aldrig din enhet — den läses lokalt i stället för att laddas upp. Det är snabbaste sättet att bekräfta att en kopia innehåller det du tror, före en återställning, ett inbyte eller en återställning på en ny telefon."),
        ("Titta inuti manuellt",
         "Är du nyfiken: kopiera filen, byt namn på kopian till .zip och öppna den med valfritt arkivverktyg. Du ser userData.db och manifest.json. Att öppna databasen kräver en SQLite-visare, och tabellerna heter det de innehåller — Note, UserMark, Bookmark, Tag. Arbeta alltid på en kopia: att redigera databasen för hand utan att uppdatera manifestets kontrollsumma ger en fil som JW Library vägrar återställa."),
        ("Redigera tryggt",
         "Anteckningar kan rättas, märkas om, färgas om eller raderas utanför appen, och resultatet exporteras som en ny .jwlibrary-fil som du återställer på vanligt sätt. Regeln som håller det tryggt är att behålla originalet: redigera en kopia, återställ den redigerade filen, och om något inte blev som du tänkt finns det orörda originalet kvar att gå tillbaka till."),
        ("Läsa en säkerhetskopia på en telefon",
         "Du behöver ingen dator. Att öppna filen i en mobil webbläsare fungerar likadant, vilket är praktiskt när kopian redan ligger på telefonen och du vill bekräfta innehållet före en återställning eller innan du raderar enheten. Filen läses lokalt, så det fungerar utan annan uppkoppling än den som laddar sidan."),
        ("Varför manifestets kontrollsumma spelar roll",
         "manifest.json noterar en kontrollsumma för userData.db. JW Library använder den för att bekräfta att databasen inte ändrats sedan kopian skrevs, så en fil vars databas redigerats utan att kontrollsumman räknats om avvisas vid återställning. Det är det enskilt vanligaste skälet till att en handredigerad kopia slutar fungera, och skälet till att redigera via ett verktyg som skriver om manifestet är säkrare än att gå direkt på databasen."),
        ("Vad det här är bra för",
         "Att kunna läsa en säkerhetskopia ändrar vad en säkerhetskopia är värd. Du kan bekräfta att en fil innehåller det du tror innan du raderar en telefon, se om en gammal fil är värd att återställa, hitta en anteckning du vet att du skrivit utan att leta igenom appen, eller rädda text ur en fil som JW Library inte accepterar. Inget av det kräver att du anförtror filen åt någon — den läses på din egen enhet."),
    ],
    "faq": [
        ("Kan jag öppna en .jwlibrary-fil i Excel eller Anteckningar?",
         "Inte på något användbart sätt — det är en databas, inte ett kalkylblad eller en "
         "textfil. Öppna den i JW Sync för att läsa den, eller exportera dina anteckningar till "
         "Markdown eller text från Studieutforskaren."),
        ("Är det säkert att öppna min säkerhetskopia i webbläsaren?",
         "Ja. JW Sync läser filen lokalt i din webbläsarflik; ingenting skickas till en server, "
         "och din ursprungliga fil ändras aldrig."),
        ("Kan jag bara byta namn på den till .zip?",
         "Ja, på en kopia. Namnbytet ändrar inte innehållet och låter vilket arkivverktyg som helst visa dig vad som finns inuti."),
        ("Ändras filen av att jag öppnar den?",
         "Nej. Att läsa en säkerhetskopia — i webbläsaren eller ett arkivverktyg — lämnar den byte för byte oförändrad. Först när du sparar eller exporterar skapas en ny fil."),
        ("Måste jag vara uppkopplad?",
         "Bara för att ladda sidan. Filen läses på din enhet och laddas inte upp, så dina anteckningar färdas aldrig över nätet."),
        ("Kan jag öppna en säkerhetskopia som någon annan skickat mig?",
         "Ja, formatet är inte bundet till en enhet eller ett konto. Om du bör återställa den är en annan fråga, eftersom en återställning ersätter ditt eget bibliotek."),
        ("Måste jag installera något för att titta inuti?",
         "Nej. En webbläsare räcker för att läsa anteckningarna; bara manuell granskning av själva databasen kräver en SQLite-visare."),
    ],
}

GUIDES_SV["jw-library-windows-pc"] = {
    "title": "Säkerhetskopiera och slå ihop JW Library på en Windows-dator",
    "h1": "Att använda JW Library-säkerhetskopior på en Windows-dator",
    "description": "Så säkerhetskopierar du JW Library i Windows, och så slår du ihop datorns "
                   "säkerhetskopia med mobilens och surfplattans så att anteckningar, "
                   "markeringar och bokmärken hålls samlade på varje enhet.",
    "intro": [
        "JW Library körs på Windows lika väl som på mobiler och surfplattor, och det skapar "
        "samma .jwlibrary-säkerhetskopia. Det betyder att din dator kan vara en del av samma "
        "studiebibliotek som mobilen — så länge du slår ihop säkerhetskopiorna i stället för "
        "att återställa den ena över den andra.",
    ],
    "steps": [
        ("Säkerhetskopiera i Windows",
         "Öppna menyn i JW Library-appen för Windows, gå till Säkerhetskopiera och återställ "
         "och skapa en säkerhetskopia. Spara .jwlibrary-filen någonstans där den är lätt att "
         "hitta."),
        ("Säkerhetskopiera mobilen och surfplattan också",
         "På varje enhet: Personligt studium → trepunktsmenyn → Säkerhetskopiera och återställ "
         "→ Skapa en säkerhetskopia."),
        ("Slå ihop dem på jwsync.org",
         "Öppna jwsync.org i vilken webbläsare som helst på datorn och ladda in alla "
         "säkerhetskopiorna. JW Sync förenar anteckningar, markeringar, bokmärken och etiketter "
         "från varje enhet till en enda sammanslagen .jwlibrary-fil — lokalt, inget laddas upp."),
        ("Återställ den sammanslagna filen överallt",
         "Återställ den sammanslagna filen i Windows-appen och på varje mobil enhet. Nu bär "
         "datorn, mobilen och surfplattan hela biblioteket."),
    ],
    "sections": [
        ("Varför datorn är det enklaste stället",
         "I en webbläsare på datorn går det mycket snabbare att ladda in flera filer, granska "
         "förhandsvisningen och spara resultatet än att trycka sig fram på mobilen. Många har "
         "sin huvudsakliga sammanslagningsrutin på datorn och återställer bara den sammanslagna "
         "filen till sina mobila enheter."),
    ],
    "faq": [
        ("Fungerar Windows-säkerhetskopian ihop med iPhone- och Android-kopior?",
         "Ja — .jwlibrary-formatet är identiskt på alla plattformar, så en Windows-kopia slås "
         "ihop fritt med mobil- och surfplattekopior."),
        ("Måste jag installera något på datorn?",
         "Nej. JW Sync är en webbsida; den körs i Edge, Chrome eller Firefox utan installation."),
    ],
}

GUIDES_SV["recover-jw-library-notes-lost-phone"] = {
    "title": "Så räddar du JW Library-anteckningar efter en borttappad eller trasig mobil",
    "h1": "Att rädda JW Library-anteckningar från en borttappad, trasig eller återställd mobil",
    "description": "Tappat mobilen eller fått den återställd med JW Library-anteckningar på? "
                   "Vad du kan rädda beror på dina säkerhetskopior. Så får du tillbaka dina "
                   "anteckningar — och så gör du nästa gång.",
    "intro": [
        "Först det ärliga svaret, för det besparar dig fortsatt läsning. Finns det en .jwlibrary-säkerhetskopia någonstans utanför den förlorade enheten kommer allt i den tillbaka via JW Librarys egen återställning, och till den delen behöver du inte den här webbplatsen. Finns ingen säkerhetskopia alls går personliga studiedata inte att få tillbaka över huvud taget: de lever bara på enheten, och inget verktyg ändrar på det.",
        "Där den här sidan verkligen hjälper är mellanfallet, och det är vanligare än de båda andra: du har en säkerhetskopia, men den är inte hela historien. Den kan vara flera månader gammal, eller så har du redan studerat på ersättningstelefonen — att bara återställa den skulle då byta en uppsättning anteckningar mot en annan i stället för att ge dig allt.",
        "Att föra samman de två är just det JW Library inte kan, och det handlar resten av sidan om. Men först letandet: folk har regelbundet fler säkerhetskopior än de minns att de gjort.",
    ],
    "steps": [
        ("Leta på varje ställe där en säkerhetskopia kan finnas",
         "Kolla e-posten (sök på ”jwlibrary” eller ”säkerhetskopia”), Google Drive, iCloud "
         "Drive, OneDrive, Dropbox och datorns nedladdningsmapp. Säkerhetskopior är små filer "
         "som det är lätt att glömma att man sparat."),
        ("Kolla dina andra enheter",
         "Om du någon gång använt JW Library på en surfplatta eller dator har den egna "
         "studiedata — skapa en säkerhetskopia av den nu för att bevara det den innehåller."),
        ("Återställ det du hittar på den nya mobilen",
         "Installera JW Library på den nya enheten, gå sedan till Säkerhetskopiera och "
         "återställ → Återställ och ladda in .jwlibrary-filen. Dina anteckningar, markeringar "
         "och bokmärken kommer tillbaka."),
        ("Slå ihop om du hittar fler än en säkerhetskopia",
         "Olika enheter eller datum kan var för sig innehålla unika anteckningar. Välj inte "
         "bara en — ladda in alla på jwsync.org, slå ihop dem till en komplett fil och "
         "återställ den. Ingenting lämnas kvar."),
    ],
    "sections": [
        ("Om det inte finns någon säkerhetskopia alls",
         "Var ärlig mot dig själv tidigt: om den enda kopian av dina anteckningar fanns på den "
         "borttappade mobilen och du aldrig exporterade en säkerhetskopia så har JW Library "
         "ingen molnkopia att återställa från. Det gör ont — och det är just därför vanan nedan "
         "spelar så stor roll."),
        ("Så hamnar du aldrig här igen",
         "Ställ in en månatlig påminnelse om säkerhetskopiering och förvara varje "
         ".jwlibrary-fil utanför mobilen (att mejla den till dig själv räcker). JW Sync kan till "
         "och med påminna dig och slå ihop dina enheter enligt schema. En fil som ligger i "
         "inkorgen överlever vilken mobil som helst."),
        ("Var det redan kan finnas en kopia",
         "Innan du drar slutsatsen att ingen finns: leta överallt där en fil kan ha sparats. Mapparna Nedladdningar och Dokument på varje dator du kopplat telefonen till, skickat i mejlen, meddelandeappar du kan ha skickat filen genom, och varje molnkonto du använder. Många skapade en kopia en gång, för månader sedan, och glömde bort det — och en månader gammal kopia innehåller fortfarande det allra mesta av ett studiebibliotek."),
        ("Återställa på en annan telefon eller plattform",
         "Ersättningsenheten behöver inte motsvara den förlorade. En kopia från en Android-telefon återställs på en iPhone och tvärtom, eftersom formatet är identiskt på Android, iOS, iPadOS och Windows. Installera JW Library på den nya enheten, uppdatera till aktuell version och återställ via Personligt studium → Säkerhetskopiera och återställ."),
        ("Om allt du har är en gammal eller ofullständig kopia",
         "Återställ den ändå. Att få tillbaka merparten av dina anteckningar är inget tröstpris — det är resultatet. Om du senare hittar en andra, annan kopia kan de två slås ihop till en fil med allt från båda, så att återställa den äldre nu hindrar dig inte från att fylla på senare."),
        ("Vad som inte går att rädda",
         "Om ingen kopia finns i någon form går personliga studiedata inte att få tillbaka. De lagras bara i appens egna lagringsutrymme på enheten, och varken JW Library eller en molnkopia på telefonnivå bevarar dem tillförlitligt. Det är värt att säga rakt ut, för det är själva skälet till att rutinen på den här sajten finns."),
        ("Kontrollera innan enheten raderas på distans",
         "Om telefonen är borttappad snarare än förstörd och du överväger en fjärradering: leta efter befintliga kopior först. Raderingen går inte att ångra och tar bort den sista chansen att någon skapar en. Är enheten bara på villovägar och fortfarande nåbar går det inte att skapa en kopia på distans, men data ligger kvar oförändrade så länge den varken raderas eller återställs."),
        ("Se till att det inte händer igen",
         "Skälet till att en förlorad telefon kostar folk år av studium är att den enda kopian låg på telefonen. När du återställt på en ersättningsenhet: lägg en kopia utanför enheten samma dag, och upprepa i en takt du faktiskt håller. Filerna är små nog att spara allihop hur länge som helst utan kostnad."),
        ("Om det verkligen inte finns någon kopia",
         "Då är det ärliga svaret att anteckningarna inte går att få tillbaka, och det är bättre att höra det än att fortsätta leta. Det du kan göra är att låta förlusten bli den sista: installera JW Library på ersättaren och skapa en kopia utanför enheten innan du byggt upp något som skulle svida att förlora. Från den punkten kostar samma händelse dig ingenting."),
    ],
    "faq": [
        ("Kan JW Sync rädda anteckningar från en mobil jag inte längre har?",
         "Inget verktyg kan det — räddningen bygger på att det finns en säkerhetskopia "
         "någonstans. JW Syncs uppgift är att läsa, reparera och slå ihop de säkerhetskopior du "
         "faktiskt har."),
        ("Min säkerhetskopia är gammal — är den ändå värd att återställa?",
         "Absolut. En gammal säkerhetskopia med det mesta av dina anteckningar är långt bättre "
         "än att börja från noll, och du kan slå ihop den senare med allt nyare du hittar."),
        ("Sparar JW Library en kopia av mina anteckningar i molnet?",
         "Nej. Personliga studiedata stannar på enheten om du inte själv skapar en säkerhetskopia."),
        ("Går anteckningar att rädda från en telefon med trasig skärm?",
         "Ibland — om telefonen fortfarande startar och går att styra, eller om en verkstad kan driva skärmen, kan JW Library fortfarande skapa en kopia. Data är oskadda så länge lagringen är det."),
        ("Går en gammal kopia fortfarande att återställa i den aktuella appen?",
         "Ja. JW Library läser äldre kopieformat. Uppdatera appen först och återställ i aktuell version."),
        ("Jag hittade två gamla kopior — vilken ska jag använda?",
         "Ingen av dem ensam: slå ihop dem. Resultatet innehåller allt från båda, inklusive sådant som fanns i den äldre och redan hunnit raderas när den nyare togs."),
        ("Kan jag se vad som finns i en kopia innan jag återställer den?",
         "Ja. Öppna filen i webbläsaren och bläddra igenom dess anteckningar, markeringar och bokmärken först, så vet du vad du återställer."),
    ],
}

GUIDES_SV["handle-merge-conflicts"] = {
    "title": "Samma anteckning redigerad på två enheter? Så hanterar du konflikter",
    "h1": "Att hantera konflikter vid sammanslagning: samma anteckning redigerad på två enheter",
    "description": "När du redigerar samma JW Library-anteckning olika på två enheter måste "
                   "sammanslagningen välja en vinnare. Konfliktgranskaren visar båda "
                   "versionerna sida vid sida så att du bestämmer — ingenting går förlorat.",
    "intro": [
        "Det mesta av en sammanslagning sker utan ansträngning — anteckningar som bara finns på "
        "en enhet förenas helt enkelt. Det enda fall som kräver ett beslut är en verklig "
        "konflikt: samma anteckning, olika redigerad på två enheter, så att de två "
        "säkerhetskopiorna inte är överens om vad den ska innehålla. JW Sync gissar aldrig i "
        "tysthet; valet lämnas till dig.",
    ],
    "steps": [
        ("Ladda in båda säkerhetskopiorna",
         "På jwsync.org, ladda in .jwlibrary-filerna från båda enheterna. JW Sync jämför dem "
         "medan sammanslagningen görs."),
        ("Öppna Konfliktgranskaren",
         "Om några anteckningar krockar listar granskaren dem. Allt som inte krockade är redan "
         "sammanslaget — det här steget gäller bara de verkliga kollisionerna."),
        ("Jämför sida vid sida",
         "Varje konflikt visar båda versionerna med skillnaderna markerade ord för ord. "
         "”Föreslå bästa” kan välja den fylligare versionen åt dig, eller så väljer du "
         "själv — anteckning för anteckning."),
        ("Slutför och återställ",
         "När alla konflikter är lösta laddar du ner den sammanslagna filen och återställer "
         "den. Nu är de två enheterna överens, med din valda version av varje anteckning."),
    ],
    "sections": [
        ("Varför det är bättre än att bara behålla den senaste",
         "”Senast vinner” raderar i tysthet ändringar du kanske ville ha kvar. Kanske innehöll "
         "den äldre versionen ett stycke du råkade ta bort på den andra enheten. Att se båda, "
         "ord för ord, betyder att du aldrig förlorar text utan att veta om det — vilket är "
         "hela poängen med att slå ihop i stället för att skriva över."),
        ("Var konflikterna kommer ifrån",
         "Oftast från att man redigerat offline på två enheter mellan två sammanslagningar, "
         "eller från att man återställt en gammal säkerhetskopia och sedan lagt till i den. Att "
         "slå ihop regelbundet håller antalet konflikter litet och skillnaderna färska i "
         "minnet."),
    ],
    "faq": [
        ("Måste jag gå igenom hundratals konflikter?",
         "Sällan. Bara anteckningar som redigerats olika på båda sidor krockar; nya "
         "anteckningar, och sådana som ändrats på bara en enhet, slås ihop automatiskt. De "
         "flesta sammanslagningar har en handfull konflikter eller inga alls."),
        ("Kan jag ändra mig efter att jag valt?",
         "Ja — ingenting skrivs till en enhet förrän du återställer den sammanslagna filen, och "
         "dina ursprungliga säkerhetskopior ändras aldrig, så du kan göra om sammanslagningen."),
    ],
}

GUIDES_SV["export-jw-library-notes"] = {
    "title": "Så exporterar du JW Library-anteckningar till text eller Markdown",
    "h1": "Exportera dina JW Library-anteckningar till text, Markdown eller en ny säkerhetskopia",
    "description": "Få ut dina JW Library-anteckningar ur appen: kopiera eller exportera dem "
                   "som Markdown eller vanlig text för användning var som helst, eller plocka "
                   "ut ett urval till en ny .jwlibrary-säkerhetskopia. Allt i webbläsaren.",
    "intro": [
        "Anteckningar skrivna i JW Library är lätta att läsa inuti appen och otympliga att använda någon annanstans — i ett dokument, i ett talutkast, på papper, eller i händerna på någon som inte använder appen. Export löser det, och huvudbeslutet är inte hur du exporterar utan hur mycket: en filtrerad export är nästan alltid mer användbar än allt på en gång.",
        "Dina studieanteckningar ska inte sitta fast i en enda app. Ibland vill du ha dem som "
        "vanlig text — att klistra in i ett talutkast, ett dokument eller din egen "
        "anteckningsapp — och ibland vill du ha en ren säkerhetskopia med bara en delmängd. "
        "Studieutforskaren gör båda, och läser din säkerhetskopia helt i webbläsaren.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia",
         "Skapa en säkerhetskopia i JW Library (Personligt studium → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia), öppna sedan jwsync.org och ladda in den i "
         "Studieutforskaren."),
        ("Hitta anteckningarna du vill ha",
         "Använd sökningen tillsammans med filtren för färg, etikett och publikation för att "
         "smalna av till exakt de anteckningar du är ute efter — en publikation, en etikett, "
         "ett ämne."),
        ("Kopiera eller exportera som Markdown eller text",
         "Ta ut anteckningarna som Markdown eller vanlig text och klistra in dem var du vill. "
         "Formateringen (fet, kursiv, listor) bevaras, så strukturerade anteckningar förblir "
         "strukturerade."),
        ("Eller plocka ut till en ny säkerhetskopia",
         "Föredrar du en fil? Exportera ett urval eller ett datumintervall till en ny "
         ".jwlibrary-säkerhetskopia — praktiskt för att arkivera ett projekt eller lämna över "
         "en viss uppsättning anteckningar till en annan enhet."),
    ],
    "sections": [
        ("Varför exportera över huvud taget",
         "Anteckningar är mer användbara när de kan resa: in i ett dokument för en uppgift på "
         "mötet, in i en personlig wiki, in i en utskrift till någon som inte använder appen. "
         "Markdown behåller strukturen och är samtidigt läsbar som vanlig text överallt."),
        ("Välja format",
         "Ren text är mest portabel och klistras in snyggt i vilket dokument eller mejl som helst. Formaterad utdata bevarar strukturen i långa anteckningar och passar för utskrift eller delning. Vill du ha tillbaka anteckningarna i JW Library senare — på en annan enhet, eller i någon annans bibliotek — spara själva .jwlibrary-filen i stället för en textexport, eftersom bara den bevarar kopplingarna mellan anteckningar, markeringar, etiketter och den exakta plats i publikationen de är förankrade vid."),
        ("Exportera bara en del av biblioteket",
         "En fullständig export av många års studium är sällan det du vill ha. Att avgränsa först — till en etikett, en publikation, en markeringsfärg eller ett datumintervall — ger något du faktiskt kan använda, som alla anteckningar märkta för ett tal, eller allt skrivet under en sammankomst. Samma filter som avgränsar vyn avgränsar exporten, så det du ser är det du får."),
        ("Vad som följer med texten och vad som inte gör det",
         "En export bär med sig dina ord. Den bär inte med sig ankarna som binder en anteckning till ett bestämt stycke i en bestämd publikation, eftersom de referenserna bara betyder något inuti JW Library. Det är det praktiska skälet att spara säkerhetskopior också: en export är till för att läsa, skriva ut och dela utanför appen, medan en .jwlibrary-fil är det som lägger tillbaka anteckningarna i ett bibliotek med sitt sammanhang intakt."),
        ("Samla ihop allt inför ett tal eller ett uppdrag",
         "Det är det vanligaste skälet att exportera. Filtrera på etiketten, publikationen eller datumintervallet materialet ligger under, kontrollera resultatet och exportera bara det. Du får ett enda dokument med de relevanta anteckningarna och de avsnitt du markerat, i den ordning de förekommer, i stället för en ohanterlig tömning av hela ditt bibliotek."),
        ("Dela anteckningar med någon annan",
         "Två olika saker döljer sig bakom att dela. Vill den andra personen läsa dina anteckningar är en textexport rätt: den öppnas överallt och kräver ingen särskild programvara. Vill personen ha anteckningarna inuti sitt eget JW Library, förankrade vid samma stycken och med sina etiketter och färger, då är det en .jwlibrary-fil du vill ha, eftersom en textexport inte kan lägga tillbaka något i appen."),
        ("Behålla ett arkiv du kan läsa långt senare",
         "Exporter är värda något i sig själva. En kopia av dina studieanteckningar i ren text går fortfarande att öppna om trettio år, i program ingen ännu skrivit, och det kan inget appspecifikt format lova. Att behålla båda — .jwlibrary för återställning och en textexport för läsning — kostar nästan ingenting och täcker båda framtiderna."),
        ("Export eller säkerhetskopia — vilket du behöver",
         "De besvarar olika frågor. En export är till för att använda anteckningarna utanför JW Library: läsa, skriva ut, citera, skicka till någon. En .jwlibrary-kopia är till för att lägga tillbaka dem i JW Library, på den här enheten eller en annan, med varje ankare, etikett och färg intakt. Ingendera ersätter den andra, och det finns ingen anledning att inte ha båda."),
    ],
    "faq": [
        ("Ändrar exporten mina anteckningar i JW Library?",
         "Nej. Exporten läser en kopia av din säkerhetskopia i webbläsaren; din ursprungliga "
         "fil och din app rörs inte."),
        ("Kan jag exportera allt på en gång?",
         "Ja — rensa filtren för att välja hela biblioteket, eller smalna av först för att bara "
         "exportera en del."),
        ("Kan jag få in mina anteckningar i Word eller Google Dokument?",
         "Ja — exportera som text och klistra in. Texten kommer med sin struktur intakt och kan formateras därifrån."),
        ("Exporteras markeringar lika väl som anteckningar?",
         "Ja, inklusive det markerade avsnittet och dess färg, så att en utskrift visar både vad du markerat och vad du skrivit."),
        ("Kan jag exportera allt på en gång?",
         "Ja, även om en filtrerad export oftast är mer användbar. Allt kan exporteras i ett svep när du vill ha en fullständig kopia."),
        ("Kan jag exportera svaren jag skrivit in i studiefrågorna?",
         "Ja. Inskrivna svar är en del av dina personliga studiedata och exporteras tillsammans med anteckningar och markeringar."),
        ("Framgår det av exporten vilken publikation varje anteckning hör till?",
         "Ja, exporten anger var varje anteckning kommer ifrån, även om själva ankaret bara fungerar inuti JW Library."),
        ("Ändrar en export något i mitt bibliotek?",
         "Nej. En export läser dina data och skriver en separat fil; ingenting inuti JW Library ändras, flyttas eller tas bort."),
        ("Kan jag exportera från en säkerhetskopia i stället för från appen?",
         "Ja. En .jwlibrary-fil kan öppnas direkt och dess anteckningar exporteras, vilket är användbart när anteckningarna du vill åt ligger i en gammal kopia och inte på din nuvarande enhet."),
    ],
}

GUIDES_SV["organize-jw-library-tags"] = {
    "title": "Så ordnar och rensar du etiketterna i JW Library",
    "h1": "Ordna dina JW Library-etiketter: byt namn, slå samman och rensa i stor skala",
    "description": "Etiketter förökar sig under år av studium. Byt namn på en etikett i varje "
                   "anteckning, slå samman dubbletter och ta bort dem du inte längre använder "
                   "— i stor skala, i webbläsaren, med full ångerfunktion.",
    "intro": [
        "Etiketterna är hur du hittar anteckningar senare — men efter några år breder de ut "
        "sig. Du hamnar med ”Tjänsten”, ”tjänsten” och ”Fälttjänsten” som betyder samma sak, "
        "etiketter du skapade en gång och aldrig återanvände, och en osammanhängande "
        "namngivning som gör filtreringen opålitlig. JW Library ger dig inget sätt att rätta "
        "till det i stor skala. Studieutforskaren gör det.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia i Studieutforskaren",
         "På jwsync.org, ladda in din .jwlibrary-fil. Filtrera på etikett för att se varje "
         "etikett och hur många anteckningar som bär den."),
        ("Byt namn på en etikett i alla dess anteckningar",
         "Etikettera om i stor skala: byt namn på en etikett en gång så uppdateras varje "
         "anteckning som använder den — inget mer redigerande av en anteckning i taget för att "
         "rätta en stavning."),
        ("Slå samman dubbletter",
         "Flytta anteckningarna från en dubblettetikett till den riktiga, och ta sedan bort den "
         "tomma dubbletten. ”Tjänsten” och ”tjänsten” blir en enda ren etikett."),
        ("Ta bort etiketter du inte längre använder",
         "Markera och radera inaktuella etiketter i stor skala. Allt går att ångra, så en "
         "överivrig städning är aldrig permanent."),
        ("Exportera det uppstädade biblioteket",
         "Ladda ner den redigerade .jwlibrary-filen och återställ den i JW Library. Nu är dina "
         "etiketter enhetliga överallt."),
    ],
    "sections": [
        ("Ett etikettsystem som faktiskt hjälper",
         "När etiketterna väl är enhetliga blir filtreringen pålitlig — ett tryck visar varje "
         "anteckning om ett tema, tvärs över alla publikationer. Det är skillnaden mellan "
         "etiketter som skräp och etiketter som ett verkligt register över ditt studium."),
        ("Enhetliga etiketter gör delning till ett par klick",
         "Anteckningsväljaren på delningssidan har ett eget etikettfilter, så en ren etikett är "
         "också det snabbaste sättet att skicka någon en uppsättning anteckningar: välj "
         "etiketten, tryck Markera alla, skapa filen. Slarviga etiketter kostar dig två gånger "
         "— när du letar efter anteckningar och när du försöker dela dem."),
    ],
    "faq": [
        ("Rör ometikettering i stor skala anteckningarnas text?",
         "Nej — bara vilka etiketter som är kopplade ändras. Dina rubriker och ditt innehåll "
         "förblir precis som du skrev dem."),
        ("Går det att ångra om jag gör fel?",
         "Ja. Studieutforskaren har full ångra och gör om, och din ursprungliga säkerhetskopia "
         "ändras aldrig — ändringarna hamnar i en exporterad kopia."),
    ],
}

GUIDES_SV["manage-jw-library-highlights"] = {
    "title": "Så hanterar och färgar du om markeringar i JW Library",
    "h1": "Hantera dina JW Library-markeringar: färga om och ordna i stor skala",
    "description": "Få ordning på år av markeringar i JW Library: byt färger i stor skala, ge "
                   "din färgkod en enhetlig innebörd och bläddra bland alla markeringar på ett "
                   "ställe. I webbläsaren.",
    "intro": [
        "Markeringsfärger hjälper bara om de betyder något enhetligt. Med tiden glider de "
        "flestas markeringar isär — gult betydde en sak 2019 och något annat i dag, och det "
        "finns inget sätt i JW Library att se dem alla tillsammans eller rätta till dem i stor "
        "skala. Studieutforskaren samlar varje markering i en enda vy och låter dig färga om i "
        "stor skala.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia",
         "På jwsync.org, öppna din .jwlibrary-fil i Studieutforskaren och byt till fliken "
         "Markeringar."),
        ("Bläddra och filtrera dina markeringar",
         "Se varje markering i en enda lista, filtrera på färg eller publikation, och sök i den "
         "markerade texten och i kopplade anteckningar."),
        ("Färga om i stor skala",
         "Markera många markeringar och byt färg på dem tillsammans — till exempel för att "
         "samla allt du menade som ”viktig bibeltext” till en enda färg i hela biblioteket."),
        ("Redigera kopplade anteckningar också",
         "Där en markering har en anteckning kopplad kan du redigera den anteckningens rubrik "
         "och innehåll direkt här."),
        ("Exportera och återställ",
         "Ladda ner den redigerade .jwlibrary-filen och återställ den i JW Library så att din "
         "enhetliga färgkod finns på varje enhet."),
    ],
    "sections": [
        ("Bestäm vad dina färger betyder",
         "Ett enkelt system — en färg för huvudtankar, en för bibeltexter att lära utantill, en "
         "för frågor att undersöka — gör markeringar till ett studieverktyg i stället för "
         "dekoration. Att färga om i stor skala låter dig tillämpa det systemet i efterhand på "
         "år av läsning."),
    ],
    "faq": [
        ("Kan jag se markeringar som inte har någon anteckning kopplad?",
         "Ja — fliken Markeringar visar dem alla, med eller utan kopplad anteckning."),
        ("Påverkar omfärgningen den underliggande texten?",
         "Nej, bara markeringens färg ändras; publikationens text och dina anteckningar rörs "
         "inte."),
    ],
}

GUIDES_SV["jw-library-study-answers"] = {
    "title": "Visa och redigera dina ifyllda studiesvar i JW Library",
    "h1": "Att hitta dina JW Library-studiesvar på ett och samma ställe",
    "description": "Dina inskrivna svar på frågorna i studieartiklar och arbetshäften ligger "
                   "gömda i din säkerhetskopia. Fliken Studiesvar i Studieutforskaren låter dig "
                   "läsa, söka i och redigera dem allihop på en gång.",
    "intro": [
        "När du studerar skriver du in svar i rutorna i studieartiklar, Vakttornet och "
        "arbetshäften för mötena. De sparas i din säkerhetskopia — men JW Library visar bara "
        "vart och ett begravt i sin egen publikation. Det finns inget enda ställe där du kan gå "
        "igenom allt du skrivit. Fliken Studiesvar i Studieutforskaren är det stället.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia i Studieutforskaren",
         "På jwsync.org, ladda in din .jwlibrary-fil och öppna fliken Studiesvar."),
        ("Läs alla dina svar tillsammans",
         "Varje svar du skrivit in dyker upp i en sökbar lista, så att du kan gå igenom en hel "
         "studieartikels värde av dina egna tankar på en gång."),
        ("Sök och redigera",
         "Hitta ett svar via dess text och redigera och putsa det på plats — praktiskt när du "
         "går igenom inför ett möte eller snyggar till en formulering du skrev i hast."),
        ("Exportera eller återställ",
         "Återställ den redigerade filen för att ta med dina ändringar tillbaka till JW "
         "Library, eller kopiera ut svaren som text till ett tal eller för egna anteckningar."),
    ],
    "sections": [
        ("Varför det är användbart före mötena",
         "Att gå igenom dina förberedda svar i en sammanhängande lista — i stället för att "
         "rulla genom varje stycke i appen — är ett snabbare sätt att friska upp vad du tänkt "
         "säga, och att upptäcka svar du lämnat tomma."),
    ],
    "faq": [
        ("Är det här samma sak som mina personliga anteckningar?",
         "Nej — studiesvaren är det du skrivit in i en publikations svarsrutor. "
         "Studieutforskaren visar dem på en egen flik, skild från fria anteckningar."),
        ("Laddas något upp för att läsa mina svar?",
         "Nej. Som allt i JW Sync läses din säkerhetskopia lokalt i webbläsaren och skickas "
         "aldrig någonstans."),
    ],
}

GUIDES_SV["extract-jw-library-notes-by-date"] = {
    "title": "Plocka ut JW Library-anteckningar från en period till en ny säkerhetskopia",
    "h1": "Att plocka ut ett datumintervall av anteckningar till en ny säkerhetskopia",
    "description": "Ta ut bara anteckningarna från en viss period — ett tjänsteår, en "
                   "sammankomst, ett studieprojekt — till en egen ren .jwlibrary-säkerhetskopia. "
                   "Helt i din webbläsare.",
    "intro": [
        "Ibland vill du ha en skiva av ditt bibliotek, inte allt: årets anteckningar för en "
        "genomgång, allt från en sammankomst, eller ett enskilt projekts efterforskningar att "
        "lämna vidare. Studieutforskaren kan plocka ut anteckningar från ett datumintervall "
        "till en splitterny .jwlibrary-säkerhetskopia och lämnar ditt huvudbibliotek orört.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia",
         "På jwsync.org, öppna din .jwlibrary-fil i Studieutforskaren."),
        ("Ställ in datumintervallet",
         "Välj start- och slutdatum för anteckningarna du vill ha — ett tjänsteår, en månad, "
         "datumen för ett visst evenemang."),
        ("Plocka ut till en ny säkerhetskopia",
         "Exportera de matchande anteckningarna till en ny .jwlibrary-fil. Den innehåller bara "
         "den periodens anteckningar och markeringar, med deras etiketter."),
        ("Använd den uttagna filen",
         "Återställ den i JW Library för en fokuserad genomgång, arkivera den, eller dela den "
         "med någon som bara behöver den skivan."),
    ],
    "sections": [
        ("Goda skäl att plocka ut efter datum",
         "Ett årligt arkiv över ditt studium; en ren fil med sammankomstanteckningar att hålla "
         "för sig; att lämna en studiekamrat bara anteckningarna från ett projekt ni gjorde "
         "tillsammans; eller att dela upp ett enormt bibliotek i hanterbara, daterade delar — "
         "allt utan att röra din huvudsakliga säkerhetskopia."),
    ],
    "faq": [
        ("Tar uttaget bort de anteckningarna från mitt bibliotek?",
         "Nej. Det kopierar de matchande anteckningarna till en ny fil; din ursprungliga "
         "säkerhetskopia behåller allt."),
        ("Vilket datum används — när jag skrev eller när jag senast redigerade anteckningen?",
         "Anteckningens egna tidsstämplar i säkerhetskopian används, så intervallet speglar när "
         "anteckningarna skapades eller ändrades."),
    ],
}

GUIDES_SV["connect-jw-library-notes-study-map"] = {
    "title": "Se hur dina JW Library-anteckningar hänger ihop — Studiekartan",
    "h1": "Studiekartan: en privat kunskapsgraf över dina JW Library-anteckningar",
    "description": "Studiekartan gör dina JW Library-anteckningar till ett interaktivt nät och "
                   "kopplar dem via gemensamma bibeltexter, gemensamma etiketter och liknande "
                   "formuleringar — så att du ser temana som löper genom ditt studium.",
    "intro": [
        "År av anteckningar rymmer kopplingar du aldrig sett: samma bibeltext citerad i ett "
        "dussin poster, ett tema du ständigt återvänder till, tankar som ekar mot varandra i "
        "olika publikationer. Studiekartan ritar de kopplingarna som en interaktiv graf, så att "
        "formen på ditt eget studium blir synlig.",
    ],
    "steps": [
        ("Öppna sidan Studiestatistik och ladda in en säkerhetskopia",
         "Gå till jwsync.org/highlights.html och ladda in din .jwlibrary-fil. Studiekartan "
         "läser den i din webbläsare."),
        ("Öppna Studiekartan",
         "Starta kartan för att se dina anteckningar som sammanlänkade punkter, kopplade via "
         "gemensamma bibeltexter, gemensamma etiketter och liknande formuleringar."),
        ("Utforska kopplingarna",
         "Växla mellan vyerna Teman och Anteckningar, håll pekaren över en anteckning för att "
         "lyfta fram dess kopplingar, dra runt saker och använd styrkereglaget för att bara "
         "visa de närmaste kopplingarna. Helskärmsläget ger dig utrymme att röra dig."),
        ("Bygg och spara studiekedjor",
         "Rita dina egna manuella ”studiekedjor” mellan besläktade anteckningar för att fånga "
         "en tankegång, och exportera kartan som en PNG-bild att spara eller visa."),
    ],
    "sections": [
        ("Vad kartan avslöjar",
         "Klustren visar temana du studerar mest; en bibeltext kopplad till många anteckningar "
         "visar en vers du ständigt återvänder till; en isolerad anteckning kan vara en tråd "
         "värd att utveckla. Det är ett sätt att studera ditt studium — och att förbereda tal "
         "genom att följa kopplingar du redan gjort."),
    ],
    "faq": [
        ("Behöver jag många anteckningar för att kartan ska vara till nytta?",
         "Ett blygsamt bibliotek visar redan kopplingar; ju rikare dina anteckningar är, desto "
         "mer avslöjar kartan. Mycket små bibliotek får en uppmaning att lägga till fler "
         "anteckningar först."),
        ("Är kartan privat?",
         "Helt och hållet. Den byggs i din webbläsare utifrån din säkerhetskopia och laddas "
         "aldrig upp; även PNG-exporten skapas på din enhet."),
    ],
}

GUIDES_SV["review-old-jw-library-notes"] = {
    "title": "Så går du igenom dina gamla JW Library-anteckningar (så att de fastnar)",
    "h1": "Att gå igenom gamla anteckningar med Återblick — lite, men ofta",
    "description": "Anteckningar du aldrig återvänder till är anteckningar du glömmer. "
                   "Återblick visar vad du skrev den här dagen tidigare år och bygger en mjuk "
                   "repetition med mellanrum, så att tidigare studium fortsätter arbeta för "
                   "dig.",
    "intro": [
        "De flesta studieanteckningar skrivs en gång och ses aldrig igen. Det är ett tyst "
        "slöseri — insikten var värd att fånga, och sedan sjönk den till botten av biblioteket. "
        "Återblick lyfter upp dina egna gamla anteckningar till ytan igen, några i taget, så "
        "att återbesöka dem blir en liten daglig vana i stället för ett någon-gång-projekt.",
    ],
    "steps": [
        ("Öppna sidan Studiestatistik och ladda in en säkerhetskopia",
         "Gå till jwsync.org/highlights.html och ladda in din .jwlibrary-fil. Återblick läser "
         "dina anteckningar lokalt."),
        ("Se ”Den här dagen”",
         "Återblick lyfter fram anteckningar du skrev det här datumet tidigare år — ”skriven "
         "för två år sedan i dag” — och kopplar dig till tidigare studium i det ögonblick då "
         "det betyder mest."),
        ("Gör en kort daglig genomgång",
         "Den lägger fram en handfull anteckningar att återbesöka och markera som genomgångna. "
         "Lite, men ofta, är så studiet sätter sig — och en svit växer så länge du håller "
         "vanan."),
        ("Kom tillbaka i morgon",
         "Repetition med mellanrum schemalägger anteckningar att dyka upp igen över tid, så att "
         "de som är värda att minnas fortsätter komma tillbaka tills de verkligen är dina."),
    ],
    "sections": [
        ("Varför repetition med mellanrum fungerar",
         "Att repetera något precis när du håller på att glömma det är långt mer effektivt än "
         "att plugga allt på en gång. Genom att sprida några anteckningar över många dagar gör "
         "Återblick ditt befintliga bibliotek till en pågående repetition med låg ansträngning, "
         "som stadigt fördjupar det du studerat."),
    ],
    "faq": [
        ("Var sparas mina genomgångsframsteg?",
         "I webbläsaren på din enhet — det finns inget konto och ingenting laddas upp. Sviten "
         "och schemat är bara dina."),
        ("Behöver jag nya anteckningar för det här?",
         "Nej — Återblick arbetar med de anteckningar du redan skrivit. Ju äldre ditt "
         "bibliotek är, desto mer givande blir ”den här dagen”-stunderna."),
    ],
}

GUIDES_SV["jw-library-achievements-streaks"] = {
    "title": "Studiesviter, nivåer och utmärkelser i JW Library",
    "h1": "Gör ditt JW Library-studium till sviter, nivåer och utmärkelser",
    "description": "Se dina studiesviter, klättra 60 nivåer i 12 steg på din studieresa och lås "
                   "upp omkring 200 utmärkelser — allt läst privat från din egen JW "
                   "Library-säkerhetskopia.",
    "intro": [
        "Regelbundenheten är den svåra biten i personligt studium, och framsteg man inte ser är "
        "lätta att låta glida. Sidan Studiestatistik gör historiken i din säkerhetskopia till "
        "något du kan se växa: sviter, nivåer och utmärkelser som speglar det studium du "
        "faktiskt gjort — inga påtvingade mål, bara din egen historik gjord synlig.",
    ],
    "steps": [
        ("Öppna sidan Studiestatistik",
         "Gå till jwsync.org/highlights.html och ladda in din .jwlibrary-säkerhetskopia. Allt "
         "räknas ut i din webbläsare."),
        ("Kolla dina sviter",
         "Se din längsta och din pågående studiesvit, din veckorytm och dina mest intensiva "
         "timmar och månader — pulsen i din studievana."),
        ("Klättra på din studieresa",
         "Ta dig genom 60 nivåer i 12 namngivna steg (från Frö hela vägen till Vintergrön), med "
         "en färgskiftande sfär och firande vid varje ny nivå, utifrån hela ditt studium."),
        ("Samla utmärkelser",
         "Lås upp omkring 200 utmärkelser från Vanlig till Legendarisk, inklusive tematiska "
         "medaljer som utgår från innehållet; öppna vilken medalj som helst för att se dina "
         "framsteg mot nästa."),
    ],
    "sections": [
        ("Motivation utan press",
         "Det här är inte mål som någon annan satt — det är en spegel av vad du redan gjort. "
         "Att se en svit du inte vill bryta, eller en nivå du nästan nått, är en vänlig knuff "
         "att hålla den goda vanan vid liv. Och ett delbart kort sammanfattar ditt år utan att "
         "avslöja en enda privat anteckning."),
    ],
    "faq": [
        ("Uppdateras sviter och utmärkelser av sig själva?",
         "De speglar den säkerhetskopia du laddar in, så skapa en ny säkerhetskopia för att se "
         "dina senaste framsteg. Ingenting körs i bakgrunden."),
        ("Delas eller laddas något av det här upp?",
         "Nej. Allt räknas ut lokalt utifrån din säkerhetskopia; bara sammanfattningskortet är "
         "något du kan välja att dela, och det innehåller ingen anteckningstext."),
    ],
}

GUIDES_SV["share-convention-assembly-notes"] = {
    "title": "Så delar du sammankomstanteckningar från JW Library",
    "h1": "Att dela dina anteckningar från sammankomster och möten",
    "description": "Lämna vidare dina anteckningar från en sammankomst eller ett möte till "
                   "familj och vänner som en liten fil — utan att lämna ifrån dig hela ditt "
                   "bibliotek eller skriva över deras. En praktisk användning av "
                   "anteckningsdelning.",
    "intro": [
        "Du antecknade noggrant genom en hel sammankomst; en vän som missade ett pass skulle "
        "gärna vilja ha dem; familjemedlemmar vill ha punkterna för sin egen genomgång. Att "
        "skicka hela din säkerhetskopia är överdrivet och skulle radera mottagarens egna "
        "anteckningar vid återställning. Anteckningsdelning låter dig lämna vidare precis de "
        "anteckningar du vill — och låter mottagaren behålla allt hon redan har.",
    ],
    "steps": [
        ("Ladda in din säkerhetskopia på delningssidan",
         "Gå till jwsync.org/share.html och ladda in din .jwlibrary-fil."),
        ("Markera bara sammankomstanteckningarna",
         "Välj evenemangets etikett i etikettfiltret i anteckningsväljaren och tryck Markera "
         "alla — listan är redan precis de anteckningar du etiketterat. Markeringar som hör "
         "till dem följer med."),
        ("Skicka den lilla delningsfilen",
         "JW Sync skapar en liten fil som bara innehåller de anteckningarna. Skicka den hur du "
         "vill — meddelandeapp, e-post, AirDrop. Ingen server, inget konto."),
        ("Familj och vänner lägger till den",
         "Var och en öppnar samma sida, laddar in din fil tillsammans med sin egen "
         "säkerhetskopia och får en ny säkerhetskopia med dina anteckningar tillagda. Deras "
         "egna anteckningar skrivs aldrig över, och dina importerade anteckningar kommer "
         "etiketterade så att de är lätta att hitta."),
    ],
    "sections": [
        ("En etikett gör det här enkelt",
         "Om du etiketterar dina anteckningar under evenemanget (säg ”Sammankomst 2026”) är det "
         "efteråt ett filterklick och ett Markera alla att välja dem. Det är värt att starta en "
         "ny etikett i början av varje sammankomst eller särskilt möte just av det skälet."),
    ],
    "faq": [
        ("Kan jag dela med flera personer samtidigt?",
         "Ja — delningsfilen är bara en fil. Skicka den till hur många du vill; var och en "
         "lägger till den i sitt eget bibliotek oberoende av de andra."),
        ("Blottas hela mitt bibliotek?",
         "Nej. Bara anteckningarna du markerar finns i filen; resten av ditt bibliotek förblir "
         "privat."),
    ],
}

GUIDES_SV["share-jw-library-notes-by-tag"] = {
    "title": "Dela bara JW Library-anteckningarna under en etikett",
    "h1": "Att dela bara anteckningarna som bär en viss etikett",
    "description": "Skicka ett ämne, ett projekt eller en students material i stället för hela "
                   "ditt bibliotek — och dina etiketter följer med, så att anteckningarna kommer "
                   "fram ordnade på andra sidan.",
    "intro": [
        "En etikett är oftast delningens naturliga enhet. Du etiketterade allt du samlat om ett "
        "ämne, allt från ett evenemang, eller allt du går igenom med en viss person — och det "
        "är den uppsättningen, inte hela ditt bibliotek, som den andra personen faktiskt vill "
        "ha.",
        "JW Syncs anteckningsdelning arbetar anteckning för anteckning, så en etikett är helt "
        "enkelt listan du bockar av. Anteckningarna behåller sina etiketter på vägen ut, vilket "
        "betyder att mottagaren kan filtrera fram exakt samma uppsättning inne i sitt eget "
        "bibliotek efteråt.",
    ],
    "steps": [
        ("Se till att anteckningarna bär etiketten",
         "Etikettera dem i JW Library medan du skriver, eller öppna din säkerhetskopia i "
         "Studieutforskaren på jwsync.org och använd etikettredigeraren för att sätta en "
         "etikett på många anteckningar samtidigt. Att etikettera enhetligt nu är det som gör "
         "delning till ett minutjobb senare."),
        ("Öppna delningssidan och ladda in din säkerhetskopia",
         "Gå till jwsync.org/share.html, välj Skicka anteckningar och ladda in din "
         ".jwlibrary-fil. Den läses i din webbläsare och lämnar aldrig din enhet."),
        ("Välj etiketten i filtret, sedan Markera alla",
         "Anteckningsväljaren har ett etikettfilter som listar varje etikett i din "
         "säkerhetskopia med antalet anteckningar under den. Välj din etikett så smalnar listan "
         "till exakt de anteckningarna; Markera alla bockar av hela högen. Det är hela "
         "urvalet — två klick."),
        ("Skapa filen och skicka den",
         "JW Sync bygger en liten delningsfil med bara anteckningarna du bockat av. Skicka den "
         "via chatt, e-post eller AirDrop — ingen server är inblandad och inget konto på "
         "någondera sidan."),
        ("Hon lägger till den i sin egen säkerhetskopia",
         "Den andra personen öppnar samma sida, väljer Ta emot, förhandsgranskar anteckningarna "
         "och lägger till dem i sin säkerhetskopia. Dina etiketter kommer med anteckningarna, "
         "plus en etikett för själva importen, så hela uppsättningen är ett filter bort även "
         "för henne."),
    ],
    "sections": [
        ("Varför dela en etikett i stället för en säkerhetskopia",
         "Att lämna ifrån sig en hel .jwlibrary-säkerhetskopia ger bort allt du någonsin "
         "skrivit, och att återställa den skulle radera den andra personens egna anteckningar. "
         "Att dela ett etiketterat urval är motsatsen på båda punkterna: hon ser bara det du "
         "valt, och hon förlorar ingenting av sitt eget."),
        ("Att smalna av ytterligare, eller dela över flera etiketter",
         "Etikettfiltret och sökrutan arbetar tillsammans: välj en etikett, skriv sedan ett ord "
         "för att smalna av ännu mer, och Markera alla bockar fortfarande bara av det som "
         "ligger framför dig. Sökningen träffar också etikettnamn, så ett nyckelord som flera "
         "etiketter delar samlar ihop dem i ett svep. Varje anteckning i listan visar sina "
         "etiketter, så du ser vad du skickar innan du skickar det."),
        ("Etiketter värda att behålla för delning",
         "Det är värt att ha några etiketter som bara finns för att delas — ett evenemangsnamn, "
         "ett ämne du undersöker åt andra, personen du studerar med. När stunden kommer att "
         "skicka något finns inget att leta efter: uppsättningen är redan färdig."),
    ],
    "faq": [
        ("Följer mina etiketter med till den andra personen?",
         "Ja. Delade anteckningar bär sina etiketter, och importen märks med en egen etikett, "
         "så mottagaren kan hitta, gå igenom eller ta bort hela satsen senare."),
        ("Tänk om en anteckning har flera etiketter?",
         "Den syns under var och en av dem i filtret, och alla dess etiketter följer med. Att "
         "filtrera på en etikett tar aldrig bort de andra."),
        ("Tar delning bort anteckningarna från mitt bibliotek?",
         "Nej. Delning kopierar anteckningar till en liten fil; din säkerhetskopia och din app "
         "rörs inte."),
        ("Kan jag skicka samma etikett till flera personer?",
         "Ja — delningsfilen är en helt vanlig fil. Skicka den till hur många du vill, och var "
         "och en lägger till den i sitt eget bibliotek oberoende av de andra."),
    ],
}

GUIDES_SV["share-notes-with-bible-student"] = {
    "title": "Dela JW Library-anteckningar med en bibelstudieelev",
    "h1": "Att dela studieanteckningar med någon du studerar Bibeln med",
    "description": "Skicka anteckningarna för en lektion — bibeltexter, illustrationer, "
                   "punkterna du förberett — rakt in i den andra personens eget JW Library, "
                   "utan att röra något hon själv skrivit.",
    "intro": [
        "När du förbereder ett studium hamnar det mesta av arbetet i dina egna anteckningar: "
        "de extra bibeltexterna, illustrationen som fick poängen att landa, svaret på frågan "
        "hon ställde förra veckan. Att läsa upp det är en sak; att lämna henne en kopia hon kan "
        "läsa om hela veckan är en annan.",
        "Anteckningsdelning lägger dina förberedda anteckningar i hennes bibliotek som riktiga "
        "JW Library-anteckningar, fästa vid samma stycken och verser — inte som en skärmbild "
        "eller ett meddelande hon scrollar förbi.",
    ],
    "steps": [
        ("Förbered lektionens anteckningar i JW Library",
         "Skriv anteckningarna som vanligt, vid styckena och bibeltexterna lektionen täcker. Ge "
         "dem en etikett — personens namn, eller publikationen — så att uppsättningen är lätt "
         "att markera senare."),
        ("Öppna delningssidan och ladda in din säkerhetskopia",
         "Skapa en säkerhetskopia (Personligt studium → Säkerhetskopiera och återställ → Skapa "
         "en säkerhetskopia), öppna sedan jwsync.org/share.html, välj Skicka anteckningar och "
         "ladda in filen. Den lämnar aldrig din enhet."),
        ("Bocka av anteckningarna för den här lektionen",
         "Filtrera väljaren på etiketten du använde och tryck Markera alla, eller sök och bocka "
         "av dem en och en. Skapa delningsfilen — allt annat i ditt bibliotek stannar där det "
         "är."),
        ("Skicka den och visa hur mottagandet går till",
         "Hon behöver först en egen säkerhetskopia — Personligt studium → Säkerhetskopiera och "
         "återställ → Skapa en säkerhetskopia. Sedan öppnar hon jwsync.org/share.html, väljer "
         "Ta emot, laddar in din fil och sin säkerhetskopia och laddar ner den uppdaterade "
         "säkerhetskopian."),
        ("Hon återställer den i JW Library",
         "Säkerhetskopiera och återställ → Återställ, välj den uppdaterade filen, och dina "
         "anteckningar dyker upp i hennes bibliotek vid sidan av hennes egna — etiketterade, så "
         "att hon vet vilka som kom från dig."),
    ],
    "sections": [
        ("Hennes anteckningar skrivs aldrig över",
         "Det är den viktiga skillnaden mot att skicka en säkerhetskopia. En återställning "
         "ersätter en enhets hela bibliotek; att ta emot delade anteckningar lägger till i det. "
         "Allt hon själv skrivit — även vid precis samma stycken — förblir exakt som det var."),
        ("En veckorytm som tar två minuter",
         "När ni båda gjort det en första gång är rutinen kort: förbered, bocka av, skicka, "
         "återställ. Många tycker det är enklast att skicka anteckningarna direkt efter "
         "förberedelsen, så att eleven har dem före studiet i stället för efter."),
    ],
    "faq": [
        ("Behöver eleven ett konto eller en installerad app?",
         "Inget konto någonstans, och inget att installera utöver JW Library självt — "
         "delningssidan är en helt vanlig webbsida."),
        ("Tänk om eleven aldrig gjort en säkerhetskopia?",
         "Då gör hon en först, i JW Library under Personligt studium → Säkerhetskopiera och "
         "återställ. Även ett till synes tomt bibliotek fungerar; säkerhetskopian är det de "
         "delade anteckningarna läggs till i."),
        ("Kan jag ta tillbaka anteckningarna senare?",
         "Filen är din att skicka eller låta bli. När någon väl har den är den hennes, precis "
         "som vilket meddelande som helst — så dela bara sådant du skulle vara bekväm med att "
         "dela skriftligt."),
    ],
}

GUIDES_SV["share-meeting-notes-with-family"] = {
    "title": "Dela mötesanteckningar med din familj eller ditt hushåll",
    "h1": "Att dela den här veckans mötesanteckningar med familjen",
    "description": "Någon var sjuk, jobbade eller var bortrest — skicka veckans anteckningar "
                   "som en liten fil som hon kan lägga till i sitt eget JW Library, utan att "
                   "någon av er förlorar något.",
    "intro": [
        "I de flesta hushåll antecknar var och en på sin egen enhet, och någon missar alltid ett "
        "möte. Att läsa upp dina anteckningar över middagen fungerar en gång; att lägga dem i "
        "den andra personens bibliotek är det som gör att hon kan använda materialet senare, på "
        "det ställe där hon faktiskt kommer att leta.",
        "Eftersom delningen sker anteckning för anteckning i stället för säkerhetskopia för "
        "säkerhetskopia kan flera personer byta anteckningar fritt utan att någons bibliotek "
        "skrivs över.",
    ],
    "steps": [
        ("Säkerhetskopiera enheten du antecknade på",
         "JW Library → Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia."),
        ("Markera veckans anteckningar",
         "På jwsync.org/share.html väljer du Skicka anteckningar, laddar in din säkerhetskopia "
         "och bockar av den här veckans anteckningar — att söka på publikationen samlar ihop "
         "dem snabbt, och om du etiketterar veckans anteckningar samlar etikettfiltret dem med "
         "ett klick."),
        ("Skicka den i familjechatten",
         "Skapa delningsfilen och skicka den så som hushållet redan pratar — meddelandeapp, "
         "e-post, AirDrop. Det är en liten fil med bara anteckningarna du bockat av."),
        ("Var och en lägger till den i sin egen säkerhetskopia",
         "Hon öppnar samma sida, väljer Ta emot, laddar in din fil tillsammans med en egen "
         "säkerhetskopia, laddar ner den uppdaterade säkerhetskopian och återställer den i JW "
         "Library."),
    ],
    "sections": [
        ("Allas bibliotek förblir deras eget",
         "Ingens anteckningar ersätts, och ingen behöver lämna ifrån sig hela sitt bibliotek "
         "för att vara med. Importerade anteckningar kommer under en etikett, så var och en ser "
         "på en gång vilka anteckningar som kom från någon annan och kan radera satsen senare "
         "om hon hellre vill slippa den."),
        ("Familjens tillbedjan: samla i stället för att sprida",
         "Samma verktyg fungerar åt andra hållet. Om alla antecknar under familjens tillbedjan "
         "kan en person samla de andras delningsfiler i en enda säkerhetskopia och sitta med "
         "hushållets samlade anteckningar om samma material."),
    ],
    "faq": [
        ("Kan barnens enheter vara med?",
         "Vilken enhet som helst som kan köra JW Library och öppna en webbsida kan det. Stegen "
         "är identiska på mobil, surfplatta eller dator."),
        ("Måste vi vara på samma plattform?",
         "Nej. Android, iPhone, iPad och Windows-appen använder samma säkerhetskopieformat, så "
         "anteckningar går mellan dem utan konvertering."),
    ],
}

GUIDES_SV["receive-shared-jw-library-notes"] = {
    "title": "Någon har skickat mig JW Library-anteckningar — hur öppnar jag dem?",
    "h1": "Att lägga till anteckningar som någon delat med dig i ditt eget JW Library",
    "description": "Du har fått en fil med delade anteckningar eller ett textblock. Så "
                   "förhandsgranskar du det och lägger till det i din egen JW "
                   "Library-säkerhetskopia utan att förlora en enda egen anteckning.",
    "intro": [
        "Delade JW Library-anteckningar kommer som en liten fil (som slutar på .jwshare.json) "
        "eller som ett textblock inklistrat i ett meddelande. JW Library kan inte öppna någon "
        "av dem — men det behöver du inte heller. Mottagarsidan i JW Sync läser de delade "
        "anteckningarna, visar dig vad som finns i dem och skriver in dem i en säkerhetskopia "
        "av ditt.",
        "Hela utbytet sker på din enhet. Det finns inget konto, ingenting laddas upp, och dina "
        "egna anteckningar får tillägg, aldrig ersättningar.",
    ],
    "steps": [
        ("Gör först en säkerhetskopia av ditt eget bibliotek",
         "I JW Library: Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia. Det är den filen de delade anteckningarna läggs till i, så den bör "
         "vara aktuell."),
        ("Öppna delningssidan och välj Ta emot",
         "Gå till jwsync.org/share.html och välj Ta emot anteckningar."),
        ("Ladda in det du fått",
         "Välj .jwshare.json-filen, eller klistra in den delade texten direkt i rutan om den "
         "kom som ett meddelande. Hur som helst får du en skrivskyddad förhandsvisning av varje "
         "anteckning innan något skrivs."),
        ("Lägg till dem i din säkerhetskopia",
         "Ladda in din egen säkerhetskopia, välj etiketten de importerade anteckningarna ska "
         "bära och lägg till dem. JW Sync bygger en uppdaterad säkerhetskopia som du laddar "
         "ner."),
        ("Återställ den uppdaterade säkerhetskopian i JW Library",
         "Personligt studium → Säkerhetskopiera och återställ → Återställ, välj den uppdaterade "
         "filen. De delade anteckningarna finns nu i ditt bibliotek, vid rätt stycken och "
         "verser."),
    ],
    "sections": [
        ("Ingenting av ditt ersätts",
         "Delade anteckningar läggs till som nya anteckningar. Även där en delad anteckning "
         "hamnar vid ett stycke du redan skrivit vid överlever båda — din orörd, hennes "
         "bredvid. Det enda att tänka på är den vanliga regeln för återställning: återställ den "
         "uppdaterade säkerhetskopian, inte en äldre."),
        ("Ändrat dig senare?",
         "Varje importerad anteckning bär etiketten du valde när du lade till den. Öppna din "
         "säkerhetskopia i Studieutforskaren, filtrera på den etiketten, så kan du gå igenom "
         "eller radera hela satsen i ett svep."),
    ],
    "faq": [
        ("Filen kom omdöpt till .txt eller öppnades som text — är den trasig?",
         "Nej. Meddelandeappar gör ofta så. Kopiera texten och klistra in den i rutan för Ta "
         "emot; det fungerar precis likadant."),
        ("Behöver jag avsändarens hela säkerhetskopia?",
         "Nej. Delningsfilen innehåller bara anteckningarna hon valde att skicka — inget annat "
         "från hennes bibliotek."),
        ("Laddas något upp när jag förhandsgranskar anteckningarna?",
         "Nej. Att läsa den delade filen, förhandsgranska den och skriva den uppdaterade "
         "säkerhetskopian sker allt i din webbläsare på din enhet."),
    ],
}

GUIDES_SV["share-notes-with-study-group"] = {
    "title": "Dela efterforskningar med en studiegrupp",
    "h1": "Att dela efterforskningar med en grupp — och samla in deras",
    "description": "En fil, många personer: skicka en uppsättning efterforskningsanteckningar "
                   "till alla som studerar samma ämne, och samla ihop det de skickar tillbaka "
                   "till en enda egen uppsättning.",
    "intro": [
        "När flera personer gräver i samma ämne hamnar efterforskningarna oftast utspridda — en "
        "hittade hänvisningarna, en annan den historiska bakgrunden, en tredje "
        "illustrationerna. Att läsa varandras skärmbilder är inte samma sak som att ha "
        "materialet i sitt eget bibliotek, vid samma verser, sökbart nästa år.",
        "Eftersom en delningsfil bara är en fil räcker en export åt hela gruppen, och samma "
        "mekanism bär deras arbete tillbaka till dig.",
    ],
    "steps": [
        ("Etikettera dina efterforskningar medan du samlar",
         "Ge ämnet en etikett i JW Library så att uppsättningen hålls samman. I "
         "Studieutforskaren kan du sätta en etikett på många anteckningar i efterhand om du "
         "inte hann då."),
        ("Skapa en delningsfil för gruppen",
         "På jwsync.org/share.html väljer du Skicka anteckningar, laddar in din säkerhetskopia, "
         "tar ämnets etikett i etikettfiltret, trycker Markera alla och skapar filen."),
        ("Lägg upp den en gång",
         "Skicka samma fil till alla — en gruppchatt, ett mejl till flera, vad gruppen redan "
         "använder. Ingen inställning per person och ingen serverkopia."),
        ("Be om deras i gengäld",
         "Var och en kan göra exakt samma sak från sitt håll. Lägg till varje fil du får i din "
         "säkerhetskopia i tur och ordning, och ge varje import en egen etikett — avsändarens "
         "namn fungerar bra — så vet du alltid vems efterforskningar som är vems."),
    ],
    "sections": [
        ("En samlad uppsättning, men fortfarande spårbar",
         "Efter några omgångar har du gruppens hela efterforskning om ämnet i ditt eget "
         "bibliotek, vid rätt stycken och verser, med varje bidrag etiketterat efter källa. "
         "Sökningen hittar allt på en gång; etiketterna låter dig skilja det åt igen närhelst du "
         "vill."),
        ("Ingen behöver blotta sitt bibliotek",
         "Var och en delar bara anteckningarna hon bockar av. Resten av varje persons bibliotek "
         "— personligt studium, privata påminnelser, allt annat — hamnar aldrig i filen."),
    ],
    "faq": [
        ("Finns det någon gräns för hur många anteckningar jag kan dela på en gång?",
         "I praktiken nej. Anteckningar är små; även en stor uppsättning ger en fil du kan "
         "skicka i ett meddelande."),
        ("Tänk om två personer skickar mig samma anteckning?",
         "Du ser den två gånger, var och en under sin avsändares etikett. Sökningen i "
         "Studieutforskaren gör nästan-dubbletter lätta att hitta och radera."),
        ("Kan någon ta emot utan att skicka något tillbaka?",
         "Ja. Att ta emot och att skicka är oberoende av varandra — ingen är skyldig att dela "
         "för att kunna lägga till det hon fått."),
    ],
}

GUIDES_SV["share-talk-preparation-notes"] = {
    "title": "Lämna vidare efterforskningarna bakom ett tal eller en uppgift",
    "h1": "Att lämna vidare dina efterforskningar för tal och uppgifter",
    "description": "Du gjorde grävandet för ett tal, en programpunkt eller en uppgift. Så "
                   "lämnar du efterforskningarna till nästa som behöver dem — som riktiga "
                   "anteckningar i hennes bibliotek, eller som vanlig text för ett dokument.",
    "intro": [
        "Förberedelser används sällan bara en gång. Bibeltexterna du spårade upp, bakgrunden du "
        "läste, sättet du till slut valde att lägga upp en tanke på — den som täcker samma "
        "material senare skulle hellre börja där än vid ett tomt blad.",
        "JW Sync ger dig två sätt att lämna vidare det, och de passar olika personer: som "
        "anteckningar som landar i den andra personens JW Library, eller som vanlig text hon "
        "kan klistra in i ett dokument.",
    ],
    "steps": [
        ("Samla efterforskningarna under en etikett",
         "Etikettera anteckningarna med temat eller uppgiften medan du förbereder. Om de redan "
         "är skrivna och saknar etikett kan du öppna din säkerhetskopia i Studieutforskaren och "
         "etikettera dem i klump på ett par minuter."),
        ("Bestäm vilken form som passar den andra personen",
         "Den som studerar i JW Library vill ha anteckningar i sitt bibliotek. Den som bygger "
         "ett dokument vill ha text. Du kan göra båda från samma uppsättning."),
        ("För att skicka anteckningar: använd delningssidan",
         "På jwsync.org/share.html väljer du Skicka anteckningar, laddar in din säkerhetskopia, "
         "filtrerar på etiketten du använde och trycker Markera alla, och skapar sedan filen. "
         "Hon lägger till den i sin egen säkerhetskopia och återställer den — hennes egna "
         "anteckningar rörs inte."),
        ("För att skicka text: exportera från Studieutforskaren",
         "Filtrera fram samma uppsättning och kopiera eller exportera den som Markdown eller "
         "vanlig text. Formateringen överlever, så ett strukturerat utkast förblir strukturerat "
         "när det klistras in i ett dokument."),
    ],
    "sections": [
        ("Behåll en kopia åt dig själv, i en form du hittar igen",
         "Samma export är värd att spara för egen del. En etikett plus ett datumintervall gör "
         "hela förberedelsen återfinningsbar flera år senare, vilket är precis när du kommer "
         "att vilja ha den — och Studieutforskarens uttag efter datum gör vilket tidsfönster "
         "som helst till en egen fil."),
    ],
    "faq": [
        ("Förblir bibeltexterna kopplade till rätt verser?",
         "Ja — delade anteckningar behåller stycket och versen de var fästa vid, så de landar "
         "på rätt plats i den andra personens bibliotek."),
        ("Kan jag dela anteckningar som har markeringar?",
         "Ja. Markeringar som hör till anteckningarna du delar följer med dem."),
    ],
}

GUIDES_SV["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Förbered mötet med anteckningar du redan skrivit",
    "h1": "Veckoförberedelse med anteckningarna du redan har",
    "description": "Du har studerat det här materialet förut. Här är en kort veckorutin som "
                   "lyfter fram dina gamla anteckningar, markeringar och svar om samma "
                   "publikation innan du förbereder på nytt.",
    "intro": [
        "De flesta förbereder varje vecka från ett tomt blad, trots att de skrivit om samma "
        "ämne — ibland samma bibeltext — flera gånger förut. De tidigare tankarna ligger i ditt "
        "bibliotek; det enda problemet är att ingenting bär tillbaka dem till dig i rätt "
        "ögonblick.",
        "En rutin på fem minuter i början av förberedelsen rättar till det, och den använder "
        "ingenting annat än säkerhetskopian du redan har.",
    ],
    "steps": [
        ("Ladda in en aktuell säkerhetskopia i Studieutforskaren",
         "Skapa en säkerhetskopia i JW Library och öppna den sedan på jwsync.org. Allt läses i "
         "din webbläsare."),
        ("Sök på ämnet innan du börjar",
         "Sök på temabibeltexten, ämnet eller publikationen. Allt du skrivit om det tidigare år "
         "kommer upp samlat, tvärs över varje publikation där det förekommer."),
        ("Kolla dina studiesvar",
         "Vyn Studiesvar samlar svaren du skrivit in i studiefrågorna, så att tidigare rundor "
         "genom samma material finns där att bygga vidare på i stället för att upprepa."),
        ("Lägg till det som saknas och lägg tillbaka det",
         "Anteckningar kan redigeras eller skapas direkt där — rubrik, text, etiketter, "
         "markeringsfärg. Exportera den redigerade säkerhetskopian och återställ den i JW "
         "Library, så finns din förberedelse i appen till mötet."),
    ],
    "sections": [
        ("Varför de gamla anteckningarna spelar roll",
         "Att gå igenom vad du kom fram till förra gången gör förberedelsen kumulativ. Du "
         "slutar återupptäcka samma punkter och börjar bygga vidare på dem — och "
         "anteckningarna du lägger till den här veckan blir nästa rundas utgångspunkt."),
        ("En mjukare variant: låt anteckningarna komma till dig",
         "Om en veckosökning känns som arbete hämtar Återblick på sidan Studiestatistik själv "
         "fram några gamla anteckningar varje dag, inklusive dem du skrev det här datumet "
         "tidigare år. Samma nytta, ingen rutin att komma ihåg."),
    ],
    "faq": [
        ("Ändrar redigering i webbläsaren mitt bibliotek direkt?",
         "Nej. Du exporterar en uppdaterad säkerhetskopia och återställer den i JW Library — "
         "appen ändras bara av en återställning du själv utför."),
        ("Laddas min säkerhetskopia upp när jag söker i den?",
         "Nej. Filen läses lokalt i din webbläsare; ingenting skickas någonstans."),
    ],
}

GUIDES_SV["print-jw-library-notes"] = {
    "title": "Så skriver du ut dina JW Library-anteckningar",
    "h1": "Att få dina JW Library-anteckningar på papper",
    "description": "JW Library har ingen utskriftsknapp. Exportera dina anteckningar som text "
                   "eller Markdown, klistra in dem i vilket dokument som helst och skriv ut — "
                   "en studiedagbok, ett set anteckningar till någon utan appen, eller ett "
                   "arkiv.",
    "intro": [
        "Det går inte att skriva ut från JW Library, och skärmbilder av en mobilskärm blir "
        "dålig läsning. Men anteckningarna är dina, och att få in dem i ett utskrivbart "
        "dokument är enkelt så fort du kan läsa säkerhetskopian.",
        "Studieutforskaren läser en .jwlibrary-säkerhetskopia i din webbläsare och låter dig "
        "kopiera eller exportera vilket urval av anteckningar som helst som vanlig text eller "
        "Markdown — något varje ordbehandlare, anteckningsapp och skrivare redan förstår.",
    ],
    "steps": [
        ("Skapa en säkerhetskopia och öppna den",
         "JW Library → Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia, ladda sedan in filen på jwsync.org."),
        ("Smalna av till det du vill ha på papper",
         "Filtrera på publikation, etikett, markeringsfärg eller datumintervall, eller sök på "
         "ett ämne. Att skriva ut allt går, men ett filtrerat urval ger oftast ett långt mer "
         "användbart dokument."),
        ("Kopiera eller exportera som text eller Markdown",
         "Ta ut urvalet som Markdown eller vanlig text. Fet stil, kursiv och listor överlever, "
         "så strukturerade anteckningar förblir strukturerade på sidan."),
        ("Klistra in i ett dokument och skriv ut",
         "Vilken ordbehandlare eller anteckningsapp som helst duger. Ställ in rubriker och "
         "marginaler som du vill och skriv sedan ut eller spara som PDF."),
    ],
    "sections": [
        ("Att göra en studiedagbok",
         "Ett datumintervall är den naturliga enheten för en utskriven dagbok — ett års "
         "anteckningar, eller perioden som täcker en publikation. Uttag efter datum ger dig ett "
         "rent kronologiskt set att skriva ut eller binda, vilket är en tillfredsställande sak "
         "att ha utanför skärmen."),
        ("Att skriva ut åt någon som inte använder appen",
         "Alla studerar inte från en enhet. Ett utskrivet set anteckningar om det aktuella "
         "materialet är verkligt användbart för den som föredrar papper, och det tar samma två "
         "minuter som vilken annan export som helst."),
    ],
    "faq": [
        ("Kan jag skriva ut mina markeringar också?",
         "Markeringsvyn listar avsnitten du markerat, och den listan kopieras ut som text "
         "tillsammans med dina anteckningar."),
        ("Ändras något i JW Library när jag exporterar?",
         "Nej. Exporten läser en kopia av din säkerhetskopia; din ursprungliga fil och appen "
         "rörs inte."),
    ],
}

GUIDES_SV["clean-up-duplicate-jw-library-notes"] = {
    "title": "Rensa dubbla och tomma anteckningar i JW Library",
    "h1": "Att rensa bort dubbletter, tomma anteckningar och skräp",
    "description": "Återställt en säkerhetskopia två gånger, eller importerat samma "
                   "anteckningar igen? Biblioteksdoktorn granskar din .jwlibrary-fil i "
                   "webbläsaren, hittar dubbletter och tomma anteckningar och ger dig en ren "
                   "kopia.",
    "intro": [
        "Bibliotek samlar skräp. Att återställa en säkerhetskopia på en enhet som redan hade en "
        "del av samma anteckningar, att importera ett delat set två gånger, eller år av "
        "halvskrivna anteckningar som aldrig blev färdiga — var och en lämnar något efter sig, "
        "och JW Library ger dig inget sätt att sopa upp det i klump.",
        "Biblioteksdoktorn är en gratis hälsokontroll för en .jwlibrary-fil. Den granskar "
        "säkerhetskopian i din webbläsare, berättar i klarspråk vad den hittat och åtgärdar det "
        "som går att åtgärda med ett tryck.",
    ],
    "steps": [
        ("Säkerhetskopiera först — som alltid",
         "JW Library → Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia. Behåll den filen; den är din reserv."),
        ("Kör hälsokontrollen",
         "Öppna jwsync.org, ladda in säkerhetskopian och starta Biblioteksdoktorn. Den "
         "undersöker filens innehåll och struktur utan att skicka den någonstans."),
        ("Läs vad den hittade",
         "Dubbletter, tomma anteckningar och annat skräp listas klart och tydligt, med antal, "
         "så att du ser problemets omfattning innan du ändrar något."),
        ("Åtgärda och ladda ner den rena kopian",
         "Ett tryck tillämpar reparationerna och skapar en ny, rensad .jwlibrary-fil. Ditt "
         "original ändras aldrig."),
        ("Återställ den rena filen",
         "Säkerhetskopiera och återställ → Återställ, och välj den rensade filen. Ditt "
         "bibliotek är detsamma, minus skräpet."),
    ],
    "sections": [
        ("Hur dubbletter uppstår från början",
         "Nästan alltid genom en återställning. Om du återställer en säkerhetskopia på en enhet "
         "som redan bar en del av samma material — eller återställer samma fil två gånger via "
         "olika vägar — har appen inget sätt att veta att den sett de anteckningarna förut."),
        ("Sammanslagning är sättet att undvika dem",
         "Det är precis därför det är säkrare att slå ihop två säkerhetskopior än att återställa "
         "den ena över den andra: sammanslagningen upptäcker material som redan finns och "
         "behåller det en gång. Samma kontroller körs inuti varje sammanslagning, så en "
         "sammanslagen säkerhetskopia kommer ut ren även om filerna som gick in inte var det."),
    ],
    "faq": [
        ("Raderar den anteckningar jag faktiskt vill ha?",
         "Den tar bort exakta dubbletter och tomma anteckningar — material där det inte finns "
         "något att förlora. Och eftersom den skriver en ny fil i stället för att ändra din "
         "finns originalet alltid kvar att falla tillbaka på."),
        ("Kan den återskapa anteckningar jag raderat i appen?",
         "Nej. Om en anteckning raderades i JW Library innan säkerhetskopian skapades finns den "
         "inte i filen — en äldre säkerhetskopia är stället att leta på."),
    ],
}

GUIDES_SV["backup-jw-library-before-phone-repair"] = {
    "title": "Säkerhetskopiera JW Library före en fabriksåterställning eller reparation",
    "h1": "Före en fabriksåterställning, en reparation eller när du säljer mobilen",
    "description": "En återställning raderar JW Librarys anteckningar tillsammans med allt "
                   "annat, och flyttverktyg tar dem inte med. Gör en säkerhetskopia, bekräfta "
                   "att den verkligen öppnas, och återställ sedan utan att riskera något.",
    "intro": [
        "Återställ mobilen, lämna in den på reparation eller ge den vidare, så följer JW "
        "Librarys personliga studiedata med. Foton och appar kommer tillbaka från en "
        "molnkopia; år av anteckningar, markeringar och bokmärken gör det i regel inte, "
        "eftersom flyttverktyg hoppar över appens privata data.",
        "Åtgärden tar fem minuter, och steget folk hoppar över är det som betyder mest: att "
        "kontrollera att säkerhetskopian verkligen går att läsa innan enheten rensas.",
    ],
    "steps": [
        ("Skapa säkerhetskopian",
         "JW Library → Personligt studium → Säkerhetskopiera och återställ → Skapa en "
         "säkerhetskopia. Du får en .jwlibrary-fil — oftast bara några megabyte."),
        ("Få ut den från enheten",
         "Mejla den till dig själv, eller lägg den i Drive, iCloud eller en mapp på datorn. En "
         "säkerhetskopia som bara finns på mobilen du är på väg att rensa är ingen "
         "säkerhetskopia."),
        ("Kontrollera att den öppnas innan du rensar något",
         "Ladda in filen på jwsync.org och titta på den — anteckningarna, markeringarna och "
         "bokmärkena ska alla vara där, och hälsokontrollen flaggar allt som är fel på filen. "
         "Det är hela poängen med övningen: att i efterhand upptäcka att filen inte går att "
         "läsa är för sent."),
        ("Återställ enheten, återställ sedan filen",
         "Efter återställningen eller reparationen installerar du JW Library, loggar in och går "
         "till Säkerhetskopiera och återställ → Återställ och väljer din fil."),
        ("Använt en lånemobil under tiden? Slå ihop, skriv inte över",
         "Om du antecknat på en tillfällig enhet ska du säkerhetskopiera även den och slå ihop "
         "båda filerna på jwsync.org innan du återställer — annars raderar återställningen av "
         "den gamla säkerhetskopian allt du skrev under väntetiden."),
    ],
    "sections": [
        ("Varför kontrollen är den extra minuten värd",
         "Avbrutna överföringar, molntjänster som förvanskar filer och filändelser som byts på "
         "vägen ger alla säkerhetskopior som ser fina ut i en mapp och misslyckas vid "
         "återställning. Att öppna filen först gör ett tyst problem till ett du fortfarande kan "
         "lösa, medan den ursprungliga enheten fortfarande har data."),
        ("Behåll filen efter återställningen",
         "Radera den inte så fort den nya enheten fungerar. Gamla säkerhetskopior är den enda "
         "vägen tillbaka från en anteckning som råkar raderas månader senare, och de kostar "
         "ingenting att spara."),
    ],
    "faq": [
        ("Kommer mina nedladdade publikationer tillbaka?",
         "Säkerhetskopian innehåller dina personliga studiedata — anteckningar, markeringar, "
         "bokmärken, etiketter och spellistor. Publikationerna laddas helt enkelt ner igen "
         "efteråt."),
        ("Fungerar filen om jag byter mobilmärke eller plattform?",
         "Ja. .jwlibrary-formatet är detsamma på Android, iPhone, iPad och Windows."),
    ],
}

GUIDES_SV["jw-library-notes-missing-after-update"] = {
    "title": "JW Library-anteckningar borta efter en uppdatering eller ominstallation",
    "h1": "Anteckningar borta efter en appuppdatering, ominstallation eller återställning",
    "description": "Dina anteckningar försvann efter en uppdatering, en ominstallation eller en "
                   "ny inloggning. Vad du ska göra först, vad du inte ska göra, och hur du får "
                   "tillbaka dem utan att förlora något du skrivit sedan dess.",
    "intro": [
        "Att öppna JW Library efter en uppdatering och hitta anteckningarna borta är oroande, och i de allra flesta fall går de att få tillbaka. Det som avgör är vad du gör de närmaste minuterna — närmare bestämt att inte göra det enda som förvandlar ett räddningsbart läge till en definitiv förlust.",
        "Det är ett obehagligt ögonblick: JW Library öppnas, och anteckningarna är inte där. "
        "Före allt annat ett råd — stressa inte. Det mesta som gör den här situationen "
        "oåterkallelig görs under de första tio minuterna, genom att man skriver över just den "
        "säkerhetskopia som fortfarande innehåller de saknade anteckningarna.",
        "Arbeta igenom stegen nedan i ordning. Målet är att sluta med en enda fil som innehåller "
        "både de gamla anteckningarna och allt du skrivit sedan dess.",
    ],
    "steps": [
        ("Skriv inte över dina säkerhetskopior än",
         "Undvik att skapa en ny säkerhetskopia ovanpå en gammal, och återställ ingenting i "
         "blindo. En äldre säkerhetskopia är det mest sannolika stället där dina anteckningar "
         "fortfarande finns."),
        ("Leta rätt på den nyaste säkerhetskopian du har",
         "Kolla e-postbilagor, Google Drive, iCloud Drive, datorns nedladdningsmapp och varje "
         "annan enhet du återställt till. Säkerhetskopior är små, så folk har ofta fler kopior "
         "än de minns."),
        ("Titta inuti filen innan du återställer den",
         "Ladda in kandidaten på jwsync.org och se vad som faktiskt finns i den — hur många "
         "anteckningar, från vilka publikationer, fram till vilket datum. Då vet du om det är "
         "rätt fil, innan du binder dig vid en återställning."),
        ("Säkerhetskopiera den nuvarande enheten också",
         "Även om den ser tom ut, säkerhetskopiera den. Om du skrivit något sedan anteckningarna "
         "försvann är den filen den enda kopian av det."),
        ("Slå ihop de två, återställ sedan",
         "Slå ihop den gamla säkerhetskopian med den nuvarande på jwsync.org. Resultatet "
         "innehåller de återfunna anteckningarna och allt som skrivits sedan dess, med "
         "dubbletter behållna en gång. Återställ den sammanslagna filen — aldrig den gamla "
         "säkerhetskopian ensam."),
    ],
    "sections": [
        ("Varför det är fel drag att återställa den gamla säkerhetskopian ensam",
         "En återställning ersätter enhetens bibliotek helt. Om du återställer den gamla "
         "säkerhetskopian direkt får du tillbaka de saknade anteckningarna och förlorar allt "
         "som skrivits efter att den säkerhetskopian gjordes. Det är sammanslagningen först som "
         "gör räddningen förlustfri."),
        ("Om säkerhetskopian i sig inte går att återställa",
         "En fil som ger fel under återställningen är inte nödvändigtvis förlorad. Kör "
         "hälsokontrollen på den — skador från avbrutna nedladdningar, molnsynkning eller en "
         "omdöpt filändelse går ofta att reparera, och en rensad kopia återställs normalt."),
        ("Först: skapa ingen ny säkerhetskopia än",
         "Om anteckningarna försvunnit: motstå reflexen att säkerhetskopiera direkt. En säkerhetskopia fångar det aktuella läget, och om det aktuella läget är det tomma riskerar du att skriva över den bra fil du redan hade. Ta först reda på vilka kopior som finns — i Nedladdningar, Filer, mejlen eller molnet — och bestäm dig först därefter. Ingenting på enheten blir bättre av en kopia tagen i panik."),
        ("Varför en uppdatering kan se ut att radera anteckningar",
         "Den vanliga orsaken är inte radering. En uppdatering kan lämna appen pekande mot en ny, tom databas medan den gamla ligger kvar på disken; en ominstallation — även en som en halvt misslyckad butiksuppdatering utfört automatiskt — startar appen från noll; och på delade enheter eller enheter med flera profiler kan appen hamna under en annan profil. I samtliga fall är anteckningarna snarare inte inlästa än raderade, och det är också därför en återställning från säkerhetskopia oftast tar tillbaka allt utan problem."),
        ("Hämta tillbaka en gammal kopia utan att kasta det nya arbetet",
         "Om du studerat sedan kopian skapades byter en rak återställning en förlust mot en annan: den tar tillbaka de gamla anteckningarna och tar bort det nyare. Vägen runt är att säkerhetskopiera det aktuella läget till en separat fil, slå ihop den med den äldre kopian så att båda uppsättningarna anteckningar finns i en fil, och återställa resultatet. Du får de återfunna och de nya anteckningarna tillsammans i stället för att behöva välja."),
        ("Om appen installerade om sig själv",
         "En ominstallation tömmer appens egna lagringsutrymme, så allt som inte finns i en säkerhetskopia går inte att få tillbaka — det finns ingen molnkopia att falla tillbaka på. Kontrollera varenda plats där en .jwlibrary-fil kan ha sparats innan du drar slutsatsen att ingen finns, inklusive mappen för skickat i mejlen och alla molntjänster du någonsin sparat till. När du hittar en: återställ den, och förvara därefter kopiorna utanför enheten."),
        ("När allt är tillbaka",
         "När anteckningarna är återställda: ta en kopia till och lägg den utanför enheten — det du just varit med om är argumentet för det. Om du behövde slå ihop en gammal kopia med det aktuella läget för att komma hit, spara även de två källfilerna: de är daterade ögonblicksbilder, och att ha flera av dem var precis det som gjorde räddningen möjlig."),
    ],
    "faq": [
        ("Finns anteckningarna kvar någonstans på enheten?",
         "Inte i en form du kommer åt utifrån appen. Räddning betyder i praktiken en tidigare "
         "säkerhetskopia — vilket är just därför det spelar så stor roll att spara de gamla."),
        ("Får jag tillbaka anteckningarna om jag loggar in igen?",
         "Nej. Personliga studiedata ligger inte i ett konto; de finns på enheten och färdas "
         "bara via säkerhetskopior."),
        ("Tänk om den enda säkerhetskopia jag har är flera månader gammal?",
         "Slå ihop den med en säkerhetskopia av enheten som den ser ut nu. Du får tillbaka allt "
         "den gamla filen har och behåller allt enheten fortfarande har, utan att behöva välja "
         "mellan dem."),
        ("Är mina anteckningar verkligen borta?",
         "Inte nödvändigtvis. Finns det en säkerhetskopia någonstans går allt i den att få tillbaka fullt ut. Det enda som inte går att rädda är arbete gjort efter den senaste kopian."),
        ("Kan jag kombinera en gammal kopia med det som finns på enheten nu?",
         "Ja — säkerhetskopiera det aktuella läget först, slå ihop det med den äldre och återställ resultatet. Båda uppsättningarna anteckningar hamnar i samma bibliotek."),
        ("Raderar en återställning av en gammal kopia mina nya anteckningar?",
         "På egen hand, ja, eftersom en återställning ersätter enhetens data. Slå ihop den aktuella kopian med den gamla först och återställ den sammanslagna filen."),
        ("Bör jag installera om appen för att fixa det?",
         "Nej — en ominstallation tömmer appens egna lagringsutrymme och tar bort varje chans att rädda det som fortfarande finns på enheten. Leta efter en befintlig kopia först, och betrakta ominstallationen som en sista utväg när du har en."),
    ],
}

GUIDES_SV["help-family-member-move-jw-library-notes"] = {
    "title": "Hjälp en familjemedlem att flytta sina JW Library-anteckningar",
    "h1": "Att hjälpa någon annan flytta eller rädda sina JW Library-anteckningar",
    "description": "Du är den som får frågan när mobilen krånglar. Här är den kortaste "
                   "pålitliga vägen att flytta en släktings JW Library-anteckningar till en ny "
                   "enhet — inklusive hur du gör det utan att läsa hennes anteckningar.",
    "intro": [
        "Förr eller senare räcker någon dig sin mobil med en ny bredvid. JW Library-"
        "anteckningarna är den del som inte flyttar sig själv, och ofta den del som betyder "
        "mest — år av studium som inget flyttverktyg tar med sig.",
        "Processen är densamma som när du gör det åt dig själv, med en extra sak värd att tänka "
        "igenom först: på vems enhet arbetet ska ske.",
    ],
    "steps": [
        ("Guida henne genom att göra en säkerhetskopia på den gamla enheten",
         "JW Library → Personligt studium → trepunktsmenyn → Säkerhetskopiera och återställ → "
         "Skapa en säkerhetskopia. Det sparar en .jwlibrary-fil. Om du inte är på plats går den "
         "här delen bra att ta över telefon."),
        ("Få filen dit du behöver den",
         "Låt henne mejla den till sig själv, eller dela den med dig. Den är liten nog att "
         "skickas via vilken meddelandeapp som helst."),
        ("Kontrollera att filen öppnas",
         "Ladda in den på jwsync.org och bekräfta att anteckningarna finns där. Att göra det "
         "innan den gamla enheten rensas eller lämnas vidare är vad som gör en otäck överraskning "
         "till en icke-händelse."),
        ("Slå ihop om den nya enheten redan har anteckningar",
         "Om hon använt den nya mobilen ett tag ska du säkerhetskopiera även den och slå ihop "
         "båda filerna — annars raderar återställningen av den gamla säkerhetskopian allt hon "
         "skrivit på den nya enheten."),
        ("Guida henne genom återställningen",
         "På den nya enheten: Säkerhetskopiera och återställ → Återställ, välj filen. "
         "Anteckningar, markeringar, bokmärken och etiketter dyker upp allihop."),
    ],
    "sections": [
        ("Att göra det utan att läsa hennes anteckningar",
         "Personliga studieanteckningar är personliga. Om du hellre slipper se dem — eller hon "
         "hellre slipper att du gör det — gör då hela arbetet på hennes enhet: det är en "
         "webbsida, så du kan öppna jwsync.org på hennes mobil eller surfplatta, ladda in "
         "hennes filer där och aldrig ha säkerhetskopian på din egen maskin. Ingenting laddas "
         "upp i något av fallen, men så här lämnar filen aldrig hennes händer."),
        ("Lämna henne en säkerhetskopia hon kan hitta",
         "Innan du lämnar tillbaka mobilen, se till att säkerhetskopian ligger någonstans där "
         "hon kan hitta den igen — hennes egen e-post eller molntjänst, inte bara din "
         "nedladdningsmapp. Nästa gång behöver hon kanske inte dig alls."),
    ],
    "faq": [
        ("Kan jag göra det här på distans?",
         "Ja. Om hon kan skapa en säkerhetskopia och skicka dig filen fungerar allt annat på "
         "avstånd — och återställningen är några tryck som du kan lotsa henne igenom."),
        ("Hon har en Android och den nya är en iPhone. Spelar det roll?",
         "Nej. Säkerhetskopieformatet är identiskt på Android, iPhone, iPad och Windows."),
        ("Tänk om hon aldrig gjort en säkerhetskopia och den gamla mobilen är borta?",
         "Då finns det ingenting att rädda från — data låg på den enheten. Desto större skäl "
         "att direkt sätta upp en vana med regelbundna säkerhetskopior på den nya mobilen."),
    ],
}

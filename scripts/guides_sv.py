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
        "Om du studerar på fler än en enhet — mobilen i Rikets sal, surfplattan hemma — får "
        "varje enhet sina egna anteckningar och markeringar. JW Librarys inbyggda "
        "Säkerhetskopiera och återställ kan inte förena dem: att återställa en säkerhetskopia "
        "ersätter allt på enheten och raderar arbetet från den andra.",
        "JW Sync löser det. Programmet läser två (eller fler) .jwlibrary-säkerhetskopior och "
        "slår ihop anteckningar, markeringar, bokmärken och etiketter från alla till en ny "
        "säkerhetskopia. Sammanslagningen sker helt i din webbläsare — dina filer laddas "
        "aldrig upp till någon server, så dina personliga studieanteckningar förblir privata.",
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
    ],
}

GUIDES_SV["sync-jw-library-multiple-devices"] = {
    "title": "Så synkroniserar du JW Library mellan flera enheter",
    "h1": "Så håller du JW Library likadant på flera enheter",
    "description": "JW Library har ingen inbyggd synkronisering mellan enheter. Här är en "
                   "enkel och privat rutin som håller anteckningar, markeringar och bokmärken "
                   "identiska på mobilen, surfplattan och datorn.",
    "intro": [
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
    ],
    "faq": [
        ("Körs JW Sync i bakgrunden?",
         "Nej — det är en webbsida, inte en installerad tjänst. Ingenting genomsöker dina "
         "enheter. Du kör rutinen när du själv vill; den valfria påminnelsen är bara en "
         "avisering."),
        ("Kan jag synkronisera tre eller fler enheter?",
         "Ja. Säkerhetskopiera varje enhet, ladda in alla filerna, slå ihop en gång och "
         "återställ den sammanslagna filen överallt."),
    ],
}

GUIDES_SV["transfer-jw-library-notes-new-phone"] = {
    "title": "Så flyttar du JW Library-anteckningar till en ny mobil",
    "h1": "Så flyttar du JW Library-anteckningar till en ny mobil",
    "description": "Steg för steg: flytta alla dina anteckningar, markeringar, bokmärken och "
                   "etiketter i JW Library till en ny mobil med en .jwlibrary-säkerhetskopia — "
                   "och hur du slår ihop om du redan skrivit anteckningar på den nya mobilen.",
    "intro": [
        "Verktyg för mobilflytt tar med appar och foton, men de flyttar inte tillförlitligt JW "
        "Librarys personliga studiedata. Det säkra sättet att få med dina anteckningar, "
        "markeringar, bokmärken och etiketter till en ny mobil är JW Librarys egen "
        "säkerhetskopia — det tar några minuter och fungerar mellan plattformar.",
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
    ],
    "faq": [
        ("Följer mina nedladdade publikationer med?",
         "Säkerhetskopian innehåller dina personliga studiedata — anteckningar, markeringar, "
         "bokmärken, etiketter och spellistor. Publikationerna laddas helt enkelt ner igen på "
         "den nya mobilen."),
        ("Spelar det roll om mobilerna har olika Android-versioner?",
         "Nej. .jwlibrary-formatet är detsamma överallt, även mellan Android-versioner och "
         "mellan Android och iPhone."),
    ],
}

GUIDES_SV["jw-library-android-to-iphone"] = {
    "title": "Flytta JW Library från Android till iPhone (behåll alla anteckningar)",
    "h1": "Flytta JW Library från Android till iPhone eller iPad — utan att förlora en anteckning",
    "description": ".jwlibrary-formatet är identiskt på Android och iOS. Så flyttar du dina "
                   "anteckningar, markeringar och bokmärken mellan plattformar — och så slår "
                   "du ihop om båda enheterna har anteckningar.",
    "intro": [
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
    ],
    "faq": [
        ("Behöver jag en dator för det här?",
         "Nej. Hela flytten går att göra mobil till mobil med e-post eller en molntjänst."),
        ("Överlever mina markeringsfärger flytten?",
         "Ja — markeringarna behåller sina färger, anteckningarna sina etiketter och "
         "bokmärkena sina platser."),
    ],
}

GUIDES_SV["backup-jw-library"] = {
    "title": "Så säkerhetskopierar du JW Library på rätt sätt",
    "h1": "Så säkerhetskopierar du JW Library på rätt sätt",
    "description": "En rutin på 30 sekunder som skyddar år av studieanteckningar, markeringar "
                   "och bokmärken i JW Library — och det vanliga misstaget som överraskar "
                   "många.",
    "intro": [
        "En ordentlig säkerhetskopia av JW Library tar en halv minut och skyddar år av samlat "
        "studium. Nästan alla berättelser om förlorade data börjar likadant: det fanns ingen "
        "färsk .jwlibrary-fil när mobilen tappades bort, återställdes eller byttes ut.",
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
    ],
    "faq": [
        ("Hur stor är en säkerhetskopia?",
         "Oftast några megabyte även för mycket stora bibliotek — litet nog för en "
         "e-postbilaga."),
        ("Ändras något i mobilen när jag skapar en säkerhetskopia?",
         "Nej. Den skriver bara filen; ditt bibliotek rörs inte."),
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
    ],
    "faq": [
        ("Laddas mina data upp för granskningen?",
         "Nej. Granskningen, reparationerna och exporten sker alla lokalt i webbläsaren."),
        ("Kan den återskapa anteckningar som raderats inne i JW Library?",
         "Nej — den reparerar filens struktur. Anteckningar som raderats i appen innan "
         "säkerhetskopian skapades finns inte i filen att återskapa."),
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
    ],
    "faq": [
        ("Kan jag öppna en .jwlibrary-fil i Excel eller Anteckningar?",
         "Inte på något användbart sätt — det är en databas, inte ett kalkylblad eller en "
         "textfil. Öppna den i JW Sync för att läsa den, eller exportera dina anteckningar till "
         "Markdown eller text från Studieutforskaren."),
        ("Är det säkert att öppna min säkerhetskopia i webbläsaren?",
         "Ja. JW Sync läser filen lokalt i din webbläsarflik; ingenting skickas till en server, "
         "och din ursprungliga fil ändras aldrig."),
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
        "Att tappa bort en mobil är stressigt nog utan rädslan att år av studieanteckningar gick "
        "med. Om du kan rädda dem avgörs av en enda fråga: finns det en "
        ".jwlibrary-säkerhetskopia någonstans utanför den mobilen?",
        "Den här guiden går igenom hur du hittar varje säkerhetskopia du kan tänkas ha — även "
        "sådana du glömt att du gjorde — och gör den till ett fullständigt JW Library på din "
        "nya enhet.",
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
    ],
    "faq": [
        ("Kan JW Sync rädda anteckningar från en mobil jag inte längre har?",
         "Inget verktyg kan det — räddningen bygger på att det finns en säkerhetskopia "
         "någonstans. JW Syncs uppgift är att läsa, reparera och slå ihop de säkerhetskopior du "
         "faktiskt har."),
        ("Min säkerhetskopia är gammal — är den ändå värd att återställa?",
         "Absolut. En gammal säkerhetskopia med det mesta av dina anteckningar är långt bättre "
         "än att börja från noll, och du kan slå ihop den senare med allt nyare du hittar."),
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
    ],
    "faq": [
        ("Ändrar exporten mina anteckningar i JW Library?",
         "Nej. Exporten läser en kopia av din säkerhetskopia i webbläsaren; din ursprungliga "
         "fil och din app rörs inte."),
        ("Kan jag exportera allt på en gång?",
         "Ja — rensa filtren för att välja hela biblioteket, eller smalna av först för att bara "
         "exportera en del."),
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

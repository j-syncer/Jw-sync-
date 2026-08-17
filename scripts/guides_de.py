# -*- coding: utf-8 -*-
"""German translations of the static guide pages.

Address form: du (matches the app's existing German UI copy).

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → Sicherung (die .jwlibrary-Datei)
  Personal Study            → Persönliches Studium
  Backup and Restore        → Sicherung und Wiederherstellung
  restore                   → wiederherstellen
  merge                     → zusammenführen / Zusammenführung
  notes                     → Notizen
  highlights                → Markierungen
  bookmarks                 → Lesezeichen
  tags                      → Schlagwörter
  Study Explorer            → Studien-Explorer
  Library Doctor            → Bibliotheksdoktor
  Reading Companion         → Lesebegleiter
  Resurface                 → Wiedervorlage
  Study Map                 → Studienkarte
  Study Stats               → Studienstatistik
  Conflict Reviewer         → Konfliktvergleich
  meeting                   → Zusammenkunft
  congregation              → Versammlung
  assembly / convention     → Kongress
"""

GUIDES_DE = {}

GUIDES_DE["merge-jw-library-backups"] = {
    "title": "JW-Library-Sicherungen von zwei Geräten zusammenführen",
    "h1": "So führst du JW-Library-Sicherungen von zwei Geräten zusammen",
    "description": "Führe Notizen, Markierungen, Lesezeichen und Schlagwörter aus zwei oder "
                   "mehr JW-Library-Sicherungen in einer .jwlibrary-Datei zusammen — "
                   "kostenlos, privat, in deinem Browser.",
    "intro": [
        "Du hast den Wachtturm auf dem Handy studiert und einen anderen Artikel auf dem Tablet. Jetzt enthält jedes Gerät Arbeit, die das andere nicht hat, und JW Library kann sie nicht zusammenbringen: Die Wiederherstellung ersetzt alles, sie führt nicht zusammen. Welche Sicherung du auch wiederherstellst, sie löscht das Studium des anderen Geräts. Mit der App allein gibt es keinen Weg, beides zu behalten.",
        "Dafür ist diese Seite da. Sie liest zwei (oder mehr) .jwlibrary-Dateien und vereint die Notizen, Markierungen, Lesezeichen und Tags aus allen in einer neuen Sicherung — es muss also zwischen nichts entschieden werden. Alles läuft in deinem Browser: Deine Dateien werden nie auf einen Server hochgeladen, deine persönlichen Studiennotizen bleiben privat.",
        "Genau deshalb ist die Gewohnheit vorbeugend und nicht heilend: Wer regelmäßig zusammenführt, muss nicht mehr daran denken, vor dem Studieren anderswo wiederherzustellen. Studiere, wo du gerade bist, führe zusammen, wann es dir passt, und jedes Gerät zieht nach.",
    ],
    "steps": [
        ("Erstelle auf jedem Gerät eine Sicherung",
         "Öffne in JW Library das Persönliche Studium, tippe auf das Drei-Punkte-Menü, wähle "
         "Sicherung und Wiederherstellung und dann Sicherung erstellen. Mach das auf jedem "
         "Gerät. Jedes erzeugt eine .jwlibrary-Datei."),
        ("Öffne JW Sync",
         "Geh in einem beliebigen Browser auf jwsync.org — am Handy, Tablet oder Computer. "
         "Nichts zu installieren."),
        ("Lade beide Sicherungsdateien",
         "Zieh die .jwlibrary-Dateien hinein oder wähl sie aus. JW Sync liest sie lokal auf "
         "deinem Gerät."),
        ("Sieh dir die Vorschau vor der Zusammenführung an",
         "Bevor irgendetwas geschrieben wird, zeigt eine Vorschau genau, was vereint wird. "
         "Wurde dieselbe Notiz auf beiden Geräten unterschiedlich bearbeitet, stellt der "
         "Konfliktvergleich beide Fassungen nebeneinander — mit den Unterschieden Wort für "
         "Wort —, damit du wählst, welche bleibt. Oder du lässt „Beste vorschlagen“ "
         "entscheiden."),
        ("Lade die zusammengeführte Datei herunter und stelle sie wieder her",
         "Lade die zusammengeführte .jwlibrary-Datei herunter und stelle sie auf jedem Gerät "
         "über Sicherung und Wiederherstellung → Wiederherstellen ein. Beide Geräte haben "
         "jetzt die vollständige, vereinte Bibliothek."),
    ],
    "sections": [
        ("Was wird zusammengeführt?",
         "Notizen, Markierungen, Lesezeichen, Schlagwörter und ihre Verknüpfungen. Duplikate "
         "werden automatisch erkannt, das Wiederherstellen der zusammengeführten Datei "
         "verdoppelt also nie etwas. Sicherungen von Android, iPhone, iPad und der "
         "Windows-App verwenden dasselbe Format und lassen sich frei kombinieren."),
        ("Ist das sicher?",
         "Die Zusammenführung verändert deine Ausgangsdateien nie — sie erzeugt eine "
         "brandneue Sicherung, deine Originale bleiben also als Rückfallebene unangetastet. "
         "Und weil alles im Browser läuft, verlassen keine Daten dein Gerät."),
        ("Was in einer .jwlibrary-Datei wirklich steckt",
         "Eine .jwlibrary-Sicherung ist ein ZIP-Archiv. Benenne eine Kopie in .zip um und öffne sie: Darin findest du userData.db, eine SQLite-Datenbank mit allen Notizen, Markierungen, Lesezeichen und Schlagwörtern, die du je angelegt hast, dazu eine kleine manifest.json, die die Sicherung beschreibt. Deine Notizen liegen in der Tabelle Note, die Markierungen in UserMark und BlockRange, die Lesezeichen in Bookmark, die Schlagwörter in Tag und TagMap. Zu verstehen, dass die Sicherung eine vollständige Datenbank ist und keine Sammlung einzelner Dateien, erklärt alles Weitere auf dieser Seite: deshalb ist eine Wiederherstellung alles oder nichts, und deshalb lassen sich zwei Sicherungen überhaupt kombinieren."),
        ("Warum die Wiederherstellung von JW Library nicht zusammenführen kann",
         "Beim Wiederherstellen liest JW Library deine Sicherung nicht, um das Fehlende zu ergänzen: Es ersetzt die Datenbank des Geräts durch die aus der Datei. Das ist bewusst so gebaut und sicher, weil das Gerät danach in einem bekannten Zustand ist, bedeutet aber, dass die Sicherung des Tablets auf dem Telefon alles verwirft, was das Telefon hatte und das Tablet nicht. Es gibt keine Einstellung, die das ändert, und genau diese Lücke füllt eine Zusammenführung: Sie erzeugt eine einzige Datei, die die Arbeit beider Geräte bereits enthält, sodass jedes Gerät, auf dem du sie wiederherstellst, vollständig ist."),
        ("Wie Duplikate erkannt werden",
         "Jede Notiz, jede Markierung und jedes Lesezeichen trägt eine GUID — eine eindeutige Kennung, die beim Anlegen vergeben und in allen späteren Sicherungen beibehalten wird. Taucht dasselbe Element in zwei Sicherungen auf, tragen beide Kopien dieselbe GUID, es wird als ein Element erkannt und einmal behalten. Deshalb verdoppelt zweimaliges Zusammenführen derselben Dateien nichts, und deshalb kannst du gefahrlos jede Woche erneut zusammenführen. Stimmen die GUIDs überein, der Text aber nicht — dieselbe Notiz auf beiden Geräten bearbeitet —, lässt sich das nicht automatisch klären: Das Element erscheint im Konfliktvergleich mit einem wortgenauen Vergleich, damit du wählst."),
        ("Was nicht in der Sicherung steckt",
         "Eine Sicherung enthält ausschließlich deine persönlichen Studiendaten. Heruntergeladene Publikationen, Bibelübersetzungen, Videos und Audio gehören nicht dazu, und deshalb sind Sicherungsdateien klein — meist wenige Megabyte, selbst nach Jahren. Nach dem Wiederherstellen auf einem neuen Gerät musst du die Publikationen, die du regelmäßig liest, eventuell erneut herunterladen. Nichts von dem, was du geschrieben hast, ist davon betroffen: Notizen sind über Verweise an Publikationen gebunden und hängen sich wieder an, sobald die Publikation vorhanden ist."),
        ("Wenn die Zusammenführung 0 hinzugefügte Notizen meldet",
         "Das ist fast immer richtig und kein Fehler. Es bedeutet, dass alle Notizen der zweiten Datei bereits in der ersten vorhanden waren — üblich, wenn du kürzlich zusammengeführt hast oder ein Gerät schlicht hinter dem anderen zurückliegt. Sieh in die Vorschau: Sie listet auf, was jede Datei beisteuert, bevor irgendetwas geschrieben wird. Wenn du neue Elemente erwartet hast und keine siehst, prüfe, ob du das Gerät nach der gesuchten Studiensitzung gesichert hast — eine Sicherung enthält nur, was im Moment ihrer Erstellung vorhanden war."),
    ],
    "faq": [
        ("Kann ich mehr als zwei Sicherungen zusammenführen?",
         "Ja — lade so viele .jwlibrary-Dateien, wie du Geräte hast. Sie werden alle zu einer "
         "einzigen Sicherung vereint."),
        ("Entstehen dabei doppelte Notizen?",
         "Nein. Identische Notizen, Markierungen und Lesezeichen werden erkannt und nur "
         "einmal behalten. Wirklich unterschiedliche Fassungen derselben Notiz erscheinen im "
         "Konfliktvergleich, damit du entscheidest."),
        ("Funktioniert das zwischen Android und iPhone?",
         "Ja. Das .jwlibrary-Format ist unter Android, iOS, iPadOS und Windows identisch, "
         "Sicherungen verschiedener Plattformen lassen sich also ohne Umwandlung "
         "zusammenführen."),
        ("Muss ich in einer bestimmten Reihenfolge zusammenführen?",
         "Nein. Die Zusammenführung hängt nicht von der Reihenfolge ab — derselbe Satz Dateien ergibt dasselbe Ergebnis, egal welche du zuerst lädst. Die Reihenfolge bestimmt nur, welche Datei in der Zusammenfassung der Vorschau als Basis gilt."),
        ("Was passiert mit Schlagwörtern, die es nur auf einem Gerät gibt?",
         "Sie werden unverändert übernommen, samt der Verknüpfungen zwischen Schlagwörtern und den Notizen, die sie markieren. Haben beide Geräte ein Schlagwort mit demselben Namen, gilt es als eines und erhält die Notizen von beiden."),
        ("Wie groß ist die zusammengeführte Datei?",
         "Ungefähr so groß wie beide Originale zusammen abzüglich der Duplikate — in der Regel weiterhin nur wenige Megabyte. Sicherungen enthalten keine Publikationsmedien, deshalb bleibt selbst eine stark kommentierte Bibliothek klein genug für eine E-Mail."),
        ("Kann ich eine Wiederherstellung rückgängig machen?",
         "Nicht aus JW Library heraus, und genau deshalb sind deine ursprünglichen Sicherungen wichtig. Die Zusammenführung verändert die geladenen Dateien nie, deine früheren Sicherungen bleiben also exakt erhalten und lassen sich wiederherstellen, wenn du zurück willst."),
    ],
}

GUIDES_DE["sync-jw-library-multiple-devices"] = {
    "title": "JW Library zwischen mehreren Geräten synchron halten",
    "h1": "So hältst du JW Library auf mehreren Geräten synchron",
    "description": "JW Library hat keine eingebaute Synchronisierung zwischen Geräten. Hier "
                   "ist eine einfache, private Routine, mit der Notizen, Markierungen und "
                   "Lesezeichen auf Handy, Tablet und Computer gleich bleiben.",
    "intro": [
        "Die meisten, die auf zwei Geräten studieren, stoßen auf dieselbe Weise auf das Problem: Die auf dem Tablet geschriebenen Notizen sind nicht auf dem Telefon, und die Sicherung des einen auf dem anderen wiederherzustellen würde löschen, was dieses hatte. JW Library bietet keine Synchronisierung, und seine Wiederherstellung ist bewusst alles oder nichts — Geräte gleichzuhalten braucht also eine Routine, keine Einstellung.",
        "JW Library synchronisiert persönliche Studiendaten nicht zwischen Geräten — es gibt "
        "kein Konto, das deine Notizen vom Handy aufs Tablet bringt. Der offizielle Weg ist "
        "Sicherung und Wiederherstellung, und eine Wiederherstellung ersetzt die Daten des "
        "Geräts vollständig. Wie hältst du also zwei oder drei Geräte gleich, ohne etwas zu "
        "verlieren?",
        "Die Antwort ist eine kurze Routine aus Zusammenführen und Wiederherstellen. "
        "Wöchentlich oder monatlich gemacht, dauert sie etwa zwei Minuten und lässt jedes "
        "Gerät deine vollständige Bibliothek tragen.",
    ],
    "steps": [
        ("Sichere jedes Gerät",
         "Auf jedem Gerät: Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Du bekommst eine .jwlibrary-Datei pro "
         "Gerät."),
        ("Führe die Sicherungen auf jwsync.org zusammen",
         "Lade alle Dateien. JW Sync vereint die Notizen, Markierungen, Lesezeichen und "
         "Schlagwörter jedes Geräts in einer zusammengeführten .jwlibrary-Datei — lokal im "
         "Browser, ohne dass etwas hochgeladen wird."),
        ("Stelle die zusammengeführte Datei auf jedem Gerät wieder her",
         "Sicherung und Wiederherstellung → Wiederherstellen, wähle die zusammengeführte "
         "Datei. Jetzt sind alle Geräte gleich und vollständig."),
        ("Lass dich von JW Sync erinnern",
         "Aktiviere in JW Sync eine Synchronisierungs-Erinnerung (wöchentlich oder monatlich) "
         "und du wirst angestupst, wenn es Zeit ist. JW Sync merkt sich auch deine "
         "gespeicherten Geräte, jede Runde geht also schneller."),
    ],
    "sections": [
        ("Warum nicht einfach die neueste Sicherung wiederherstellen?",
         "Weil „neueste“ nur ein Gerät widerspiegelt. Hast du in derselben Woche Notizen zur "
         "Zusammenkunft am Handy und Studiennotizen am Tablet gemacht, enthält jede Sicherung "
         "etwas, das der anderen fehlt. Eine über die andere wiederherzustellen kostet dich "
         "die Hälfte deiner Arbeit. Erst das Zusammenführen macht die Routine sicher."),
        ("Wie oft sollte ich synchronisieren?",
         "Richte dich danach, wie du studierst. Zwei aktive Geräte im täglichen Gebrauch: "
         "wöchentlich ist angenehm. Ein Tablet, das nur zu den Zusammenkünften herauskommt: "
         "monatlich reicht völlig. Länger zu warten bedeutet nur, dass die Zusammenführung "
         "mehr zu vereinen hat — zwischen den Runden geht nie etwas verloren."),
        ("Warum es keine echte Synchronisierung gibt",
         "JW Library hat kein Konto, das persönliche Studiendaten von einem Gerät zum anderen trägt. Notizen, Markierungen und Lesezeichen liegen in einer Datenbank auf jedem Gerät und bleiben dort. Der einzige offizielle Weg, sie zu bewegen, ist Sicherung und Wiederherstellung, und eine Wiederherstellung ersetzt die Daten des Zielgeräts, statt sie zu kombinieren. Zwei unabhängig genutzte Geräte laufen daher dauerhaft auseinander, sofern nichts sie zusammenführt — genau darum geht es in der Routine unten."),
        ("Eine Hauptdatei führen",
         "Die Routine funktioniert am besten, wenn du eine zusammengeführte Datei als die aktuelle Hauptdatei behandelst. Sichere in jedem Durchgang alle Geräte, führe diese Sicherungen zusammen und stelle das Ergebnis überall wieder her. Die zusammengeführte Datei wird zur Hauptdatei des nächsten Durchgangs. Die datierten Hauptdateien in der Cloud zu behalten gibt dir zugleich einen Synchronisierungsmechanismus und ein Archiv: Löschst du versehentlich etwas, enthält eine frühere Hauptdatei es noch."),
        ("Was passiert, wenn du ein Gerät eine Weile auslässt",
         "Nichts geht verloren. Ein Gerät, das mehrere Durchgänge ausgelassen hat, trägt schlicht ältere Daten; nimmst du es schließlich hinzu, fügen sich seine Notizen neben allem anderen ein, und wiederholte Elemente werden über die GUID zugeordnet statt verdoppelt. Entscheiden musst du nur bei derselben Notiz, die seit der letzten Zusammenführung auf zwei Geräten bearbeitet wurde — und die erscheint im Konfliktvergleich mit beiden Fassungen nebeneinander."),
        ("Wie oft ist oft genug",
         "Richte es danach, wie viel Arbeit du ungern wiederholen würdest. Wöchentlich passt, wenn du fast täglich auf zwei Geräten studierst; monatlich genügt reichlich, wenn eines gelegentlich genutzt wird. Wichtig ist, es vor allem Unumkehrbaren zu tun — einem Telefonwechsel, einem Zurücksetzen, einer Reparatur —, denn dann wird aus einem Auseinanderlaufen ein Verlust."),
        ("Telefon, Tablet und die Windows-App zusammen",
         "Der Routine ist es gleich, wie viele Geräte beteiligt sind und worauf sie laufen. Sichere jedes, führe alle in einem Durchgang zusammen, stelle die zusammengeführte Datei überall wieder her. Ein Windows-Rechner für die Vorbereitung und ein Telefon für die Zusammenkünfte kombinieren sich genau wie zwei Telefone, denn jede Plattform schreibt dasselbe Sicherungsformat."),
        ("Konflikte verringern, bevor sie entstehen",
         "Konflikte entstehen nur, wenn dieselbe Notiz zwischen zwei Zusammenführungen auf zwei Geräten bearbeitet wird. In der Praxis ist das selten, und es wird noch seltener, wenn du jeweils auf einem Gerät schreibst — überall lesen, aber dort tippen, wo du üblicherweise tippst. Häufiger zusammenzuführen verkleinert außerdem das Zeitfenster, in dem ein Auseinanderlaufen möglich ist, und das wirkt besser, als sich merken zu wollen, welches Gerät die neuere Fassung hat."),
        ("Wo sich die Routine auszahlt",
         "Der Wert des Zusammenführens ist nicht die Ordnung — es ist, dass jedes Gerät zu einer vollständigen Sicherung deiner Studienbibliothek wird. Geht eines verloren oder kaputt, tragen die anderen weiterhin alles, und aus dem schlimmsten Fall von Jahren verlorener Notizen wird eine Unannehmlichkeit. Das ist eine stärkere Position, als jede Sicherungsgewohnheit auf einem einzelnen Gerät sie geben kann."),
    ],
    "faq": [
        ("Läuft JW Sync im Hintergrund?",
         "Nein — es ist eine Webseite, kein installierter Dienst. Nichts durchsucht deine "
         "Geräte. Du startest die Routine, wann du willst; die optionale Erinnerung ist nur "
         "eine Benachrichtigung."),
        ("Kann ich drei oder mehr Geräte synchronisieren?",
         "Ja. Sichere jedes, lade alle Dateien, führe einmal zusammen und stelle die "
         "zusammengeführte Datei überall wieder her."),
        ("Was, wenn ich dieselbe Notiz auf zwei Geräten bearbeitet habe?",
         "Beide Fassungen bleiben erhalten, bis du wählst. Der Konfliktvergleich zeigt sie nebeneinander mit einem wortgenauen Vergleich, oder du lässt dir die vollständigere vorschlagen."),
        ("Spielt die Reihenfolge beim Wiederherstellen eine Rolle?",
         "Nein. Ist die zusammengeführte Datei erst erstellt, bringt ihre Wiederherstellung jedes Gerät in denselben vollständigen Zustand, in welcher Reihenfolge auch immer."),
        ("Kann ich drei oder mehr Geräte abgleichen?",
         "Ja. Sichere jedes und lade alle in dieselbe Zusammenführung — es gibt keine an die Gerätezahl gebundene Grenze."),
        ("Lässt sich das automatisieren?",
         "Nicht vollständig, denn JW Library hat keine Synchronisierungsschnittstelle und der Wiederherstellungsschritt geschieht in der App. Die manuelle Routine dauert eingespielt etwa zwei Minuten."),
        ("Muss ich zusammenführen, wenn ich auf dem zweiten Gerät nur lese?",
         "Wenn du dort nie kommentierst, musst du nur gelegentlich darauf wiederherstellen, damit es deine aktuellen Notizen trägt."),
    ],
}

GUIDES_DE["transfer-jw-library-notes-new-phone"] = {
    "title": "JW-Library-Notizen auf ein neues Handy übertragen",
    "h1": "So überträgst du deine JW-Library-Notizen auf ein neues Handy",
    "description": "Notizen aus JW Library auf ein neues Handy zu bringen ist eine Sicherung und eine Wiederherstellung — die App erledigt das in etwa zwei Minuten. Hier stehen die Schritte, und dazu der eine Fall, den sie nicht lösen kann: wenn auf dem neuen Handy bereits eigene Notizen liegen.",
    "intro": [
        "Das ist einfacher, als die meisten erwarten, und du brauchst kein zusätzliches Werkzeug dafür. JW Library bringt Sicherung und Wiederherstellung mit, und damit kommt jede Notiz, jede Markierung, jedes Lesezeichen und jedes Tag auf das neue Handy — auch zwischen Android und iPhone. Mach es, solange das alte Gerät noch läuft, dann dauert das Ganze ein paar Minuten.",
        "Der einzige Teil, den du bewusst erledigen musst, ist die Übertragung selbst: Umzugshelfer von Handy zu Handy nehmen Apps und Fotos mit, überspringen aber die persönlichen Studiendaten von JW Library. Erstelle also die Sicherungsdatei, statt darauf zu vertrauen, dass sie von allein mitkommt.",
        "Es gibt genau eine Situation, die die App nicht lösen kann, und die solltest du vorher kennen: Hast du auf dem neuen Handy bereits studiert, löscht das Wiederherstellen der alten Sicherung diese Arbeit, denn eine Wiederherstellung ersetzt die Bibliothek des Geräts vollständig. Trifft das auf dich zu, ist der Abschnitt zum Zusammenführen weiter unten der richtige.",
    ],
    "steps": [
        ("Erstelle auf dem alten Handy eine Sicherung",
         "Öffne JW Library → Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Das speichert eine .jwlibrary-Datei mit "
         "allen deinen Studiendaten."),
        ("Bring die Datei aufs neue Handy",
         "Schick sie dir selbst per E-Mail oder nutze Google Drive, iCloud, AirDrop oder ein "
         "USB-Kabel. Die Datei ist klein — meist ein paar Megabyte."),
        ("Stelle sie auf dem neuen Handy wieder her",
         "Installiere JW Library, dann Persönliches Studium → Sicherung und Wiederherstellung "
         "→ Wiederherstellen und wähle die .jwlibrary-Datei. Alle Notizen, Markierungen, "
         "Lesezeichen und Schlagwörter erscheinen."),
    ],
    "sections": [
        ("Schon Notizen auf dem neuen Handy? Zusammenführen statt überschreiben",
         "Wiederherstellen ersetzt, was auf dem Gerät ist. Wenn du das neue Handy schon eine "
         "Weile benutzt und es eigene Notizen hat, stelle nicht darüber wieder her — sichere "
         "auch das neue Handy, führe die alte und die neue Sicherung auf jwsync.org zu einer "
         "Datei zusammen (kostenlos, im Browser, ohne Upload) und stelle die zusammengeführte "
         "Datei wieder her. Du behältst beide Notizsätze."),
        ("Eine typische iPhone-Falle",
         "Kommt die Sicherungsdatei auf dem iPhone als .zip umbenannt an, benenne sie vor dem "
         "Wiederherstellen wieder in .jwlibrary um — der Inhalt ist in Ordnung, nur die "
         "Endung hat sich unterwegs geändert."),
        ("Erledige das, bevor das alte Telefon gelöscht oder abgegeben wird",
         "Die Sicherung muss entstehen, solange das alte Telefon noch läuft und JW Library darauf installiert ist. Sobald das Gerät zurückgesetzt, in Zahlung gegeben oder weitergereicht ist, sind die Notizen mit ihm weg: JW Library hält keine Cloud-Kopie persönlicher Studiendaten vor, und eine Telefonsicherung wie Google One oder eine iCloud-Gerätesicherung stellt oft einen älteren Stand der App-Daten wieder her — oder gar keinen. Erstelle zuerst die .jwlibrary-Datei, bringe sie in Sicherheit und überzeuge dich, dass du sie siehst, bevor du irgendetwas löschst."),
        ("Wie die Datei vom alten Telefon kommt",
         "Unter Android wird die Datei in den von dir gewählten Ordner geschrieben — meist Downloads oder Dokumente — und lässt sich mit jedem Dateimanager verschieben, per E-Mail an dich selbst senden oder in die Cloud legen. Auf dem iPhone erscheint das Teilen-Menü, sobald die Sicherung erstellt ist: Sichere sie in Dateien, schicke sie per AirDrop an das neue Telefon oder sende sie dir selbst. Die Methode spielt keine Rolle und kann die Datei nicht beschädigen: Eine .jwlibrary ist ein einzelnes Archiv, das entweder vollständig ankommt oder gar nicht."),
        ("Warum eine Übertragungs-App zwischen Telefonen nicht reicht",
         "Werkzeuge wie Smart Switch, Auf iOS übertragen oder eine iCloud-Wiederherstellung kopieren Apps und Systemdaten, doch app-eigene Datenbanken werden häufig übersprungen, unvollständig übernommen oder von einem älteren Zeitpunkt wiederhergestellt. Die Lücke fällt regelmäßig erst Wochen später auf, wenn das alte Telefon längst weg ist. Behandle die .jwlibrary-Datei als die maßgebliche Kopie und die Telefonübertragung als Bequemlichkeit: Bringt sie deine Notizen zufällig mit, kostet es nichts, deine eigene Sicherung darüber wiederherzustellen."),
        ("Prüfe, ob die Übertragung wirklich geklappt hat",
         "Öffne nach dem Wiederherstellen auf dem neuen Telefon zwei oder drei kürzlich kommentierte Publikationen und vergewissere dich, dass Notizen, Markierungsfarben und Lesezeichen vorhanden sind. Schneller geht es, wenn du die Sicherungsdatei selbst im Browser öffnest, bevor du das alte Gerät löschst: Du siehst jede Notiz, jede Markierung und jedes Lesezeichen darin und weißt damit, was erscheinen sollte. Lösche das alte Telefon erst, wenn das neue geprüft ist."),
        ("Wenn du zugleich auf Tablet oder Computer umziehst",
         "Dieselbe Datei passt überall. Richtest du neues Telefon und Tablet gleichzeitig ein, stelle dieselbe .jwlibrary-Datei auf beiden wieder her, dann starten sie identisch. Danach laufen sie wieder auseinander, je nachdem, worauf du studierst — es lohnt sich also, jetzt zu entscheiden, ob du sie regelmäßig zusammenführst oder eines als Hauptgerät behandelst."),
        ("Wenn auf dem neuen Telefon schon Notizen liegen",
         "Das passiert, wenn man das neue Gerät eine Woche nutzt, bevor man sich um den Umzug kümmert. Eine direkte Wiederherstellung würde diese Arbeit durch die Daten des alten Telefons ersetzen. Sichere zuerst das neue Telefon, führe diese Datei mit der Sicherung des alten zusammen und stelle das Ergebnis wieder her — beide Notizbestände landen in einer Bibliothek, statt dass einer den anderen überschreibt."),
        ("Was zu tun ist, sobald das neue Telefon läuft",
         "Prüfe, bevor du dich von etwas trennst. Öffne auf dem neuen Telefon einige kürzlich kommentierte Publikationen und bestätige, dass Notizen, Farben und Lesezeichen da sind; erst danach löschst oder gibst du das alte Gerät ab — in dieser Reihenfolge und nie umgekehrt. Wenn alles steht, lege eine Sicherung außerhalb des Telefons ab, denn die Situation, die dich auf diese Seite geführt hat, kommt beim nächsten Wechsel wieder."),
    ],
    "faq": [
        ("Werden damit auch meine heruntergeladenen Publikationen übertragen?",
         "Die Sicherung enthält deine persönlichen Studiendaten — Notizen, Markierungen, "
         "Lesezeichen, Schlagwörter und Wiedergabelisten. Publikationen werden auf dem neuen "
         "Handy einfach neu heruntergeladen."),
        ("Macht es etwas aus, wenn die Handys verschiedene Android-Versionen haben?",
         "Nein. Das .jwlibrary-Format ist überall gleich, auch zwischen Android-Versionen und "
         "zwischen Android und iPhone."),
        ("Kann ich meine Notizen holen, wenn das alte Telefon schon weg ist?",
         "Nur wenn irgendwo eine .jwlibrary-Datei existiert — in Dateien, Downloads, einer E-Mail an dich selbst oder in der Cloud. Ohne sie gibt es nichts wiederherzustellen, denn persönliche Studiendaten liegen ausschließlich auf dem Gerät."),
        ("Brauchen beide Telefone dieselbe JW-Library-Version?",
         "Sie müssen nicht exakt übereinstimmen, aktualisiere das neue Telefon aber vor dem Wiederherstellen auf die aktuelle Version. Eine von einer neueren Version erstellte Sicherung kann ein Datenbankschema nutzen, das eine ältere App nicht versteht."),
        ("Muss ich meine Publikationen erneut herunterladen?",
         "In der Regel ja — Publikationsmedien gehören nicht zur Sicherung. Deine Notizen hängen sich wieder an jede Publikation, sobald sie heruntergeladen ist, es geht also nichts Geschriebenes verloren."),
        ("Wie lange dauert das Ganze?",
         "Ein paar Minuten. Die Sicherung ist in Sekunden erstellt, das Verschieben hängt von der Methode ab, und das Wiederherstellen geht schnell. Am längsten dauert das erneute Herunterladen der Publikationen, und das kann im Hintergrund laufen."),
        ("Geht das ohne WLAN?",
         "Die Übertragung selbst ja, per AirDrop oder Kabel. Das erneute Herunterladen der Publikationen auf dem neuen Gerät braucht eine Verbindung."),
    ],
}

GUIDES_DE["jw-library-android-to-iphone"] = {
    "title": "JW Library von Android aufs iPhone umziehen (mit allen Notizen)",
    "h1": "JW Library von Android aufs iPhone oder iPad umziehen — ohne eine Notiz zu verlieren",
    "description": "Das .jwlibrary-Sicherungsformat ist unter Android und iOS identisch. So "
                   "bringst du Notizen, Markierungen und Lesezeichen plattformübergreifend "
                   "mit — und so führst du zusammen, wenn beide Geräte Notizen haben.",
    "intro": [
        "Der Wechsel zwischen Android und iPhone klingt nach dem schwierigen Fall und ist der einfache. JW Library schreibt auf jeder Plattform dasselbe Sicherungsformat, eine Studienbibliothek von Android nach iOS zu bringen ist also derselbe Vorgang wie zwischen zwei Android-Telefonen: keine Umwandlung, kein Exportformat zur Auswahl, nichts, was unterwegs verloren geht.",
        "Der Plattformwechsel ist der Moment, in dem viele fürchten, Jahre an Studiennotizen "
        "zu verlieren — Umzugs-Apps von Android aufs iPhone überspringen die Daten von JW "
        "Library komplett. Die gute Nachricht: Das Sicherungsformat von JW Library ist unter "
        "Android, iPhone, iPad und Windows identisch, ein Plattformwechsel besteht also nur "
        "aus Sichern, Datei übertragen und Wiederherstellen.",
    ],
    "steps": [
        ("Sichere auf dem Android-Handy",
         "JW Library → Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Speichere die .jwlibrary-Datei."),
        ("Schick die Datei aufs iPhone oder iPad",
         "E-Mail, Google Drive, iCloud Drive — alles, was eine Datei überträgt. Benennt iOS "
         "sie unterwegs in .zip um, benenne sie wieder in .jwlibrary um."),
        ("Stelle sie auf dem neuen Gerät wieder her",
         "Installiere JW Library, melde dich an, dann Sicherung und Wiederherstellung → "
         "Wiederherstellen und wähle die Datei. Notizen, Markierungen, Lesezeichen, "
         "Schlagwörter und Wiedergabelisten kommen alle mit."),
    ],
    "sections": [
        ("Wenn auf dem iPhone schon Notizen sind",
         "Wiederherstellen ersetzt die Daten des Geräts. Trägt das neue Gerät schon eigene "
         "Notizen, sichere es ebenfalls und führe beide Sicherungen erst auf jwsync.org zu "
         "einer Datei zusammen — die Zusammenführung vereint beide Bibliotheken in deinem "
         "Browser, ohne Upload — und stelle dann die zusammengeführte Datei wieder her. Auf "
         "keiner Seite geht etwas verloren."),
        ("Dieselben Schritte funktionieren in jede Richtung",
         "iPhone zu Android, Android zu Android, ein iPad als zweites Studiengerät ergänzen "
         "oder auf die Windows-App wechseln — die Sicherungsdatei ist die gemeinsame Sprache "
         "zwischen allen."),
        ("Warum das Format auf beiden Plattformen identisch ist",
         "JW Library nutzt überall dasselbe Sicherungsformat — Android, iOS, iPadOS und Windows. Eine .jwlibrary-Datei ist ein ZIP mit einer SQLite-Datenbank, die dieselben Tabellen und dasselbe Schema hat, unabhängig davon, welches Gerät sie geschrieben hat. Es gibt keinen Umwandlungsschritt, kein Hin und Her aus Export und Import und nichts Plattformspezifisches in der Datei. Eine Android-Sicherung stellt sich auf einem iPhone genauso wieder her wie eine iPhone-Sicherung."),
        ("Der einzige Teil, der sich wirklich unterscheidet",
         "Nicht die Datei — nur der Zugriff darauf. Unter Android wird die Sicherung in einen Ordner deiner Wahl gespeichert und lässt sich mit jedem Dateimanager verschieben. Auf dem iPhone läuft sie über das Teilen-Menü nach Dateien, AirDrop oder wohin du möchtest. Die Reibung beim Plattformwechsel liegt immer in diesem Handhabungsschritt, nie in der Kompatibilität. E-Mail, Cloud oder AirDrop funktionieren gleichermaßen; das Archiv kommt vollständig an oder gar nicht."),
        ("Markierungsfarben, Schlagwörter und Studienantworten",
         "Alles bleibt erhalten. Markierungsfarben werden als numerischer Index gespeichert — Gelb, Grün, Blau, Rosa, Orange und Violett — und sehen auf jeder Plattform gleich aus. Schlagwörter und die Verknüpfungen zwischen Schlagwörtern und Notizen kommen mit, ebenso die in die Studienfragen getippten Antworten. Was du nach dem Wiederherstellen auf dem iPhone siehst, ist das, was du auf dem Android-Gerät hattest."),
        ("Wenn iOS dich die Datei nicht auswählen lässt",
         "Sichere die Datei zuerst in der App Dateien und wähle sie von dort, statt aus einem Mailanhang oder der Vorschau einer Messenger-App. Manche Apps übergeben iOS eine temporäre Vorschaukopie statt der echten Datei, und die kann JW Library nicht öffnen. Kam die Datei als Anhang, tippe sie an, wähle In Dateien sichern und stelle von dort wieder her."),
        ("Richte das iPhone ein, bevor du wiederherstellst",
         "Installiere JW Library aus dem App Store und aktualisiere es auf die aktuelle Version, bevor du etwas wiederherstellst. Eine von einer neueren Version geschriebene Sicherung kann ein Datenbankschema nutzen, das eine ältere Version nicht versteht — die Wiederherstellung wird dann schlicht abgelehnt. Eine Anmeldung ist nirgends nötig: Persönliche Studiendaten stecken in der Datei, die du wiederherstellst, nicht in einem Konto."),
        ("Wenn du auf dem iPhone schon zu studieren begonnen hast",
         "Sichere zuerst das iPhone. Die Android-Datei direkt darüber wiederherzustellen würde alles ersetzen, was du seit dem Wechsel geschrieben hast. Beide Sicherungen zusammenzuführen ergibt eine Datei mit beidem, die du dann wiederherstellst — der Android-Verlauf und die neuen iPhone-Notizen landen in derselben Bibliothek."),
        ("Beide Telefone danach weiterbenutzen",
         "Manche behalten das alte Android-Gerät als Zweitlesegerät, statt es auszumustern. Das geht, aber beide laufen auseinander, sobald du auf beiden kommentierst, denn zwischen ihnen gibt es keine Synchronisierung. Wenn du beide nutzen willst, plane ein, ihre Sicherungen regelmäßig zusammenzuführen, statt anzunehmen, sie blieben gleich."),
        ("Nach dem Wechsel",
         "Gib dem iPhone Zeit, die Publikationen, die du am meisten nutzt, erneut zu laden, und prüfe dann einige kommentierte, um zu bestätigen, dass alles angekommen ist: Notizen, Markierungsfarben, Lesezeichen und Schlagwörter. Behalte die Android-Sicherungsdatei auch nach abgeschlossenem Wechsel: Sie ist eine datierte Momentaufnahme deiner Bibliothek, und sie zu behalten kostet nichts."),
    ],
    "faq": [
        ("Brauche ich dafür einen Computer?",
         "Nein. Der ganze Umzug lässt sich von Handy zu Handy per E-Mail oder Cloud-Speicher "
         "erledigen."),
        ("Bleiben meine Markierungsfarben erhalten?",
         "Ja — Markierungen behalten ihre Farben, Notizen ihre Schlagwörter und Lesezeichen "
         "ihre Stellen."),
        ("Brauche ich dafür einen Computer?",
         "Nein. AirDrop, E-Mail oder eine beliebige Cloud-App verschiebt die Datei direkt zwischen den beiden Telefonen."),
        ("Funktioniert es auch andersherum, von iPhone zu Android?",
         "Ja, genauso. Dieselben Schritte funktionieren in jede Richtung, auch von und zur Windows-App."),
        ("Braucht das iPhone dieselben heruntergeladenen Publikationen?",
         "Ja, da Publikationsmedien nicht Teil einer Sicherung sind. Die Notizen hängen sich wieder an jede Publikation, sobald sie geladen ist."),
        ("Muss ich das Android-Telefon danach behalten?",
         "Nein, sobald du geprüft hast, dass die Notizen auf dem iPhone sind. Sieh dir einige kommentierte Publikationen an, bevor du das alte Gerät löschst oder abgibst."),
        ("Werden auch die Antworten auf Studienfragen übertragen?",
         "Ja. Getippte Antworten gehören zu den persönlichen Studiendaten und kommen mit allem anderen mit."),
        ("Besteht beim Wechsel ein Risiko, Notizen zu verlieren?",
         "Nicht, wenn du die Android-Sicherung behältst. Die Wiederherstellung schreibt auf das iPhone und verändert die gelesene Datei nie, das Original bleibt also als Rückfalloption unversehrt. Behalte es, bis du bestätigt hast, dass das iPhone alles hat — und am besten auch danach."),
        ("Was, wenn das Android-Telefon keine Sicherung erstellt?",
         "Prüfe zuerst den freien Speicher, denn die App braucht Platz zum Schreiben. Versagt die App selbst, hilft meist ein Update oder ein Neustart des Geräts. Die Daten bleiben unversehrt, während du das klärst."),
    ],
}

GUIDES_DE["backup-jw-library"] = {
    "title": "JW Library richtig sichern",
    "h1": "So sicherst du JW Library richtig",
    "description": "Eine 30-Sekunden-Sicherungsroutine: was in einer .jwlibrary-Datei wirklich steckt, wo du sie aufbewahrst, und warum eine aktuelle sich lohnt, auch wenn nichts schiefgegangen ist.",
    "intro": [
        "Eine Sicherung dauert eine halbe Minute und lohnt sich als Gewohnheit — wenn auch nicht ganz aus dem Grund, den man üblicherweise hört. Sicherung und Wiederherstellung in JW Library bringen eine Bibliothek bereits problemlos auf ein neues Gerät. Eine Sicherung ist deshalb weniger eine Versicherung als der Rohstoff für alles andere, was du mit deinem Studium anfangen möchtest.",
        "Eine .jwlibrary-Datei ist die einzige Form, die deine Bibliothek außerhalb der App annimmt. Sie ist das, was du zusammenführst, wenn auf zwei Geräten studiert wurde; was du öffnest, um Jahre von Notizen zu lesen, neu zu verschlagworten oder zu ordnen; was du dem Sinn nach durchsuchst, wenn du dich nur halb erinnerst, was du geschrieben hast; und woraus du eine Auswahl an Notizen ziehst, wenn du einem Freund etwas schicken willst. Eine aktuelle zu haben ist das, was all das möglich macht.",
    ],
    "steps": [
        ("Erstelle die Sicherung",
         "Öffne JW Library → Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Es entsteht eine .jwlibrary-Datei mit jeder "
         "Notiz, Markierung, jedem Lesezeichen und Schlagwort."),
        ("Bewahre sie außerhalb des Handys auf",
         "Schick sie dir per E-Mail oder speichere sie in Google Drive, iCloud oder OneDrive. "
         "Eine Sicherung, die nur auf dem Handy liegt, verschwindet mit dem Handy."),
        ("Wiederhole das regelmäßig",
         "Monatlich ist ein guter Standard; vor jedem Gerätewechsel, Zurücksetzen oder "
         "System-Update ist es unverzichtbar. Behalte ältere Kopien — die Dateien sind klein, "
         "und eine alte Sicherung hat schon viele gerettet."),
    ],
    "sections": [
        ("Der typische Fehler: sich auf die Cloud-Sicherung des Handys verlassen",
         "Eine Sicherung des ganzen Handys (Google One, iCloud-Gerätesicherung) stellt oft "
         "eine alte Kopie der JW-Library-Daten wieder her — oder gar keine. Die "
         ".jwlibrary-Datei ist die einzige Sicherung, die du vollständig kontrollierst und "
         "zwischen Plattformen mitnehmen kannst. Sieh die Handysicherung als Zugabe, nicht "
         "als Plan."),
        ("Am Ende zwei verschiedene Sicherungen?",
         "Kommt vor: eine Sicherung vom Handy, eine ältere vom Tablet, jede mit eigenen "
         "Notizen. Du musst dich nie zwischen ihnen entscheiden — führe sie auf jwsync.org zu "
         "einer vollständigen Datei zusammen, kostenlos und privat, direkt im Browser."),
        ("Was die Datei enthält und was nicht",
         "Die Sicherung bewahrt deine persönlichen Studiendaten: Notizen, Markierungen samt Farben, Lesezeichen, Schlagwörter und die Antworten, die du in die Felder der Studienfragen getippt hast. Sie bewahrt keine Publikationen — weder Bibeln noch Zeitschriften, Bücher, Videos oder Audio. Deshalb belegt eine Sicherung von Jahren des Studiums nur wenige Megabyte, und deshalb lädst du nach dem Wiederherstellen auf einem neuen Gerät Publikationen nach, während jede geschriebene Notiz schon wieder an ihrem Platz ist."),
        ("Wie viele Sicherungen du behalten solltest",
         "Mehr als eine. Was Menschen ihre Notizen kostet, ist selten eine verlorene Datei — es ist eine gute Sicherung, die von einer schlechten überschrieben wurde, oder eine Wiederherstellung auf dem falschen Gerät. Da die Dateien klein sind, gibt es keinen Grund, alte zu löschen: Bewahre sie mit Datum in einem Ordner in der Cloud auf. Eine Sicherung von vor einem halben Jahr verliert ihren Wert nicht, auch wenn du neuere hast, denn alles, was du seither versehentlich gelöscht hast, steckt noch darin."),
        ("Wo du sie aufbewahrst",
         "Überall, nur nicht ausschließlich auf dem Gerät selbst. Ein Ordner in Drive, iCloud, Dropbox oder OneDrive deckt den wichtigsten Fall ab: dass das Gerät verloren geht, gestohlen, zurückgesetzt oder beschädigt wird. Die Datei an dich selbst zu mailen funktioniert ebenfalls und hat den nützlichen Nebeneffekt, sie zu datieren. Die Datei enthält deine eigenen Studiennotizen — behandle sie so sorgfältig wie jedes persönliche Dokument."),
        ("Eine Sicherung prüfen, bevor du dich darauf verlässt",
         "Eine Sicherung, die du nie geöffnet hast, ist eine Annahme und kein Sicherheitsnetz. Du kannst eine .jwlibrary-Datei im Browser öffnen und genau sehen, welche Notizen, Markierungen und Lesezeichen darin sind — eine Prüfung von dreißig Sekunden, die aus der Annahme eine Tatsache macht. Das zählt vor allem unmittelbar vor etwas Unumkehrbarem: einem Zurücksetzen auf Werkseinstellungen, einer Abgabe, einer Reparatur oder einem großen Systemupdate."),
        ("Die Momente, vor denen sich eine Sicherung lohnt",
         "Jeder Punkt, an dem das Gerät den Besitzer oder den Zustand wechselt: ein Systemupdate, ein Zurücksetzen, eine Reparatur oder ein Displaytausch, eine Inzahlungnahme oder die Weitergabe an jemanden. Dazu das Ende von allem, was du ungern wiederholen würdest — ein Kongress, eine Zusammenkunftsreihe, eine Zeit der Vorbereitung auf einen Vortrag. Sicherungen sind schnell und billig, die nützliche Gewohnheit knüpft sie also an Ereignisse statt an den Kalender."),
        ("Eine Telefonsicherung ist keine JW-Library-Sicherung",
         "Google One, eine iCloud-Gerätesicherung oder das Übertragungswerkzeug des Herstellers arbeiten auf Geräteebene und behandeln app-eigene Daten uneinheitlich. Regelmäßig stellt sich heraus, dass eine vollständige Telefonwiederherstellung Apps und Einstellungen zurückbrachte, aber nicht die Studiennotizen — oder einen Stand von vor Wochen. Die .jwlibrary-Datei ist die einzige Kopie, deren Inhalt du kontrollierst und prüfen kannst: Behandle die Telefonsicherung als Zugabe, nicht als Plan."),
        ("Eine Gewohnheit daraus machen, die hält",
         "Die Routine, die wirklich hält, hängt an etwas, das du ohnehin tust: sichern, wenn du die Vorbereitung der Woche abschließt, oder am selben Tag, an dem du andere wiederkehrende Dinge erledigst. Speichere immer in denselben Ordner, damit sich die Dateien an einem Ort sammeln, und lass die alten dort liegen. Ein Ordner mit datierten Sicherungen aus mehreren Jahren ist die robusteste Form davon, und ihn zu pflegen kostet Sekunden pro Woche."),
    ],
    "faq": [
        ("Wie groß ist eine Sicherungsdatei?",
         "Meist ein paar Megabyte, selbst bei sehr großen Bibliotheken — klein genug für den "
         "E-Mail-Anhang."),
        ("Verändert das Erstellen einer Sicherung etwas auf meinem Handy?",
         "Nein. Es schreibt nur die Datei; deine Bibliothek bleibt unangetastet."),
        ("Enthält die Sicherung meine heruntergeladenen Publikationen?",
         "Nein. Nur persönliche Studiendaten. Publikationen werden auf dem neuen Gerät erneut heruntergeladen, und deine Notizen hängen sich automatisch wieder an."),
        ("Kann ich eine Sicherung öffnen, um zu sehen, was drin ist?",
         "Ja. Du kannst eine .jwlibrary-Datei im Browser öffnen und alle Notizen, Markierungen und Lesezeichen durchsehen, ohne etwas zu installieren und ohne dass die Datei dein Gerät verlässt."),
        ("Laufen Sicherungen ab?",
         "Nein. Eine .jwlibrary-Datei bleibt unbegrenzt wiederherstellbar. Stelle in einer aktuellen Version von JW Library wieder her statt in einer alten, denn die App liest ältere Sicherungsformate, aber keine neueren."),
        ("Soll ich vor jeder Zusammenkunft sichern?",
         "Nicht nötig. Knüpfe Sicherungen an Ereignisse, die Daten kosten könnten — Updates, Reparaturen, neue Geräte — plus einen regelmäßigen Rhythmus, der dazu passt, wie viel Studium du ungern wiederholen würdest."),
        ("Lohnt es sich, Sicherungen von vor Jahren zu behalten?",
         "Ja. Sie sind klein, und alles, was du seither versehentlich gelöscht hast, steckt noch darin."),
    ],
}

GUIDES_DE["jw-library-restore-replaced-notes"] = {
    "title": "JW-Library-Wiederherstellung hat deine Notizen ersetzt? So holst du sie zurück",
    "h1": "Wiederherstellung hat deine Notizen ersetzt? So vereinst du beide Sicherungen",
    "description": "Die Wiederherstellung in JW Library ist ein kompletter Austausch, keine "
                   "Zusammenführung — Notizen nach dem Sicherungsdatum scheinen weg. Wenn du "
                   "noch beide Sicherungsdateien hast, ist nichts verloren. Hier die Lösung.",
    "intro": [
        "Ein furchtbarer Moment: Du stellst eine Sicherung auf einem Gerät wieder her, das "
        "schon Notizen hatte, und die Wiederherstellung ersetzt alles — die Notizen seit "
        "jener Sicherung scheinen verschwunden. Das passiert, weil Sicherung und "
        "Wiederherstellung in JW Library ein kompletter Austausch ist, keine Zusammenführung.",
        "Der entscheidende Punkt: Wenn die neuere Arbeit noch in irgendeiner Sicherungsdatei "
        "steckt, ist tatsächlich nichts verloren. Die Lösung besteht darin, die beiden "
        "Sicherungen zusammenzuführen, statt zwischen ihnen zu wählen.",
    ],
    "steps": [
        ("Stopp — stelle nichts noch einmal wieder her",
         "Jede Wiederherstellung ersetzt die aktuellen Daten des Geräts. Halte inne, bevor "
         "noch mehr verschwindet."),
        ("Sichere das Gerät so, wie es jetzt ist",
         "Persönliches Studium → Sicherung und Wiederherstellung → Sicherung erstellen. Das "
         "bewahrt den aktuellen Stand, was auch immer darin ist."),
        ("Finde die Sicherung mit den fehlenden Notizen",
         "Die .jwlibrary-Datei, aus der du wiederhergestellt hast, oder eine ältere — schau in "
         "deinen E-Mails, in Drive, iCloud und im Download-Ordner nach."),
        ("Führe beide Dateien auf jwsync.org zusammen",
         "Lade beide Sicherungen. JW Sync vereint alle Notizen, Markierungen, Lesezeichen und "
         "Schlagwörter aus beiden in einer neuen Datei — im Browser, ohne Upload. Widersprüche "
         "derselben Notiz werden nebeneinander gezeigt, damit du wählst."),
        ("Stelle die zusammengeführte Datei wieder her",
         "Sicherung und Wiederherstellung → Wiederherstellen mit der zusammengeführten "
         ".jwlibrary. Beide Notizsätze sind zurück auf dem Gerät."),
    ],
    "sections": [
        ("Was, wenn es keine Sicherung der neueren Notizen gibt?",
         "Wenn die einzige Kopie der neueren Notizen auf dem Gerät lag und eine "
         "Wiederherstellung sie bereits überschrieben hat, bietet JW Library kein "
         "Rückgängigmachen. Genau deshalb ist Schritt 2 oben — den aktuellen Stand zu "
         "sichern, bevor du sonst etwas tust — so wichtig, sobald Daten falsch aussehen. "
         "Künftig macht die Routine „erst zusammenführen“ das Problem strukturell unmöglich."),
    ],
    "faq": [
        ("Verdoppelt die Zusammenführung Notizen, die in beiden Sicherungen sind?",
         "Nein — identische Einträge werden erkannt und nur einmal behalten. Nur wirklich "
         "unterschiedliche Fassungen derselben Notiz werden zur Prüfung markiert."),
        ("Repariert das eine Sicherung, die sich gar nicht wiederherstellen lässt?",
         "Das ist meist ein Dateischaden statt eines Überschreibens — sieh dir unten die "
         "Anleitung zur beschädigten Sicherung an."),
    ],
}

GUIDES_DE["fix-corrupted-jw-library-backup"] = {
    "title": "Beschädigte JW-Library-Sicherung reparieren, die sich nicht wiederherstellen lässt",
    "h1": "Beschädigte JW-Library-Sicherung mit dem Bibliotheksdoktor reparieren",
    "description": "JW Library verweigert deine .jwlibrary-Datei? Der Bibliotheksdoktor prüft "
                   "die Sicherung in deinem Browser, repariert die häufigen Probleme und "
                   "liefert eine saubere Kopie, die sich wiederherstellen lässt.",
    "intro": [
        "Eine Sicherung, die sich nicht wiederherstellen lässt, ist nicht zwangsläufig eine Sicherung, die deine Notizen verloren hat. Die meisten Dateien, die als beschädigt beschrieben werden, sind strukturell in Ordnung und werden aus einem behebbaren Grund abgelehnt — oder sie wurden beim Übertragen so beschädigt, dass eine frische Kopie es löst. Es lohnt sich, die Ursachen durchzugehen, bevor du die Datei abschreibst.",
        "Manchmal weist JW Library eine Sicherungsdatei zurück — die Wiederherstellung "
        "schlägt fehl, bricht mit einem Fehler ab, oder die Datei öffnet sich nicht. Häufige "
        "Ursachen: ein abgebrochener Download, ein Cloud-Speicher, der die Datei verstümmelt "
        "hat, eine unterwegs geänderte Endung oder innere Ungereimtheiten, die sich über "
        "Jahre angesammelt haben.",
        "JW Sync enthält den Bibliotheksdoktor, eine Prüfung, die eine .jwlibrary-Datei "
        "untersucht und die häufigen Probleme repariert — vollständig in deinem Browser, ohne "
        "dass die Datei je dein Gerät verlässt.",
    ],
    "steps": [
        ("Öffne JW Sync und lade die problematische Datei",
         "Geh auf jwsync.org und lade die .jwlibrary-Datei, die sich nicht wiederherstellen "
         "lässt. (Kam die Datei in .zip umbenannt an, benenne sie zuerst wieder in .jwlibrary "
         "um — das allein löst viele Fälle.)"),
        ("Starte die Prüfung des Bibliotheksdoktors",
         "Der Doktor untersucht die innere Struktur der Sicherung und listet in klarer "
         "Sprache auf, was er findet — von harmlosen Eigenheiten bis zu echten Schäden."),
        ("Wende die Reparaturen an",
         "Ein Tippen repariert, was reparierbar ist. Der Doktor bearbeitet nie deine "
         "Originaldatei; er erzeugt eine gereinigte Kopie, das Original bleibt also als "
         "Rückfallebene erhalten."),
        ("Lade die reparierte Datei herunter und stelle sie wieder her",
         "Stelle die gereinigte .jwlibrary über Sicherung und Wiederherstellung → "
         "Wiederherstellen in JW Library ein."),
    ],
    "sections": [
        ("Der Doktor läuft auch bei jeder Zusammenführung",
         "Dieselben Prüfungen laufen automatisch im Zusammenführungs-Motor, eine "
         "zusammengeführte Sicherung kommt also immer sauber heraus — selbst wenn eine der "
         "Eingangsdateien Probleme hatte, von denen du nichts wusstest."),
        ("Wenn eine Datei nicht mehr zu retten ist",
         "Wurde die Datei so stark abgeschnitten, dass die Daten schlicht nicht mehr darin "
         "sind, kann kein Werkzeug sie zurückerfinden. Der Doktor sagt das ehrlich, statt "
         "eine zweifelhafte Datei zu liefern — und das ist das Signal, in E-Mails, Drive oder "
         "iCloud nach einer älteren Kopie zu suchen. Auch deshalb lohnt es sich, alte "
         "Sicherungen aufzuheben."),
        ("Was beschädigt meist bedeutet",
         "In der Praxis sind es selten kaputte Daten. Die üblichen Ursachen sind eine beim Übertragen abgeschnittene Datei — verkürzt durch einen fehlgeschlagenen Upload oder eine Messenger-App, die sie komprimiert hat — oder ein unversehrtes Archiv mit inneren Widersprüchen, die die App ablehnt. Da eine .jwlibrary ein ZIP um eine SQLite-Datenbank ist, kann jede der beiden Schichten das Problem sein, und sie brauchen unterschiedliche Lösungen: Eine abgeschnittene Datei lässt sich nicht reparieren und muss neu beschafft werden; eine widersprüchliche Datenbank meist schon."),
        ("Was eine Prüfung tatsächlich kontrolliert",
         "Eine Prüfung stellt fest, ob das Archiv sich öffnet, ob userData.db eine lesbare SQLite-Datenbank ist, die eine Integritätsprüfung besteht, ob das Schema dem entspricht, was JW Library erwartet, und ob das Manifest zu der Datenbank passt, die es beschreibt — einschließlich der Prüfsumme, mit der die App bestätigt, dass die Datei unverändert ist. Eine Abweichung zwischen Manifest und Datenbank gehört zu den häufigsten Gründen, warum eine technisch einwandfreie Sicherung abgelehnt wird, und sie ist direkt behebbar."),
        ("Verwaiste Einträge sind meist harmlos",
         "Die Prüfung einer echten Sicherung meldet oft Einträge, die auf etwas verweisen, das nicht mehr vorhanden ist — etwa eine Markierung, die auf eine verschobene Stelle einer Publikation zeigt. JW Librarys eigene Sicherungen enthalten routinemäßig Hunderte davon und lassen sich klaglos wiederherstellen. Sie sind eine normale Folge davon, dass Publikationen mit der Zeit aktualisiert werden, kein Hinweis auf Schaden, und sie zu entfernen ist nicht nötig, damit die Datei funktioniert."),
        ("Notizen aus einer Datei retten, die sich nicht wiederherstellen lässt",
         "Auch wenn eine Sicherung nicht so weit repariert werden kann, dass JW Library sie annimmt, sind die Notizen darin oft noch lesbar. Die Datei im Browser zu öffnen erlaubt dir, den Notiztext direkt zu sehen und zu kopieren, und macht aus einer unbrauchbaren Datei gerettetes Studienmaterial. Hast du eine zweite, ältere Sicherung, die sich wiederherstellen lässt, kann der lesbare Inhalt der beschädigten mit ihr zusammengebracht werden, statt ihn abzutippen."),
        ("Wenn die Wiederherstellung ohne klare Meldung scheitert",
         "JW Library lehnt eine Datei oft ab, ohne zu erklären, warum. Am häufigsten sind ein Manifest, dessen Prüfsumme nicht mehr zur beschriebenen Datenbank passt, eine beim Übertragen abgeschnittene Datei, oder eine Sicherung, die von einer neueren App-Version geschrieben wurde als der, in die du wiederherstellst. Das Erste ist behebbar, das Zweite verlangt, die Datei erneut von der Quelle zu holen, und das Dritte löst sich, indem du die App vor dem Wiederherstellen aktualisierst."),
        ("Beim nächsten Mal vermeiden",
         "Die meisten Schäden entstehen unterwegs. Verschiebe Sicherungen als Dateien und nicht über irgendetwas, das sie erneut komprimieren könnte, und bevorzuge Cloud, AirDrop oder ein Kabel gegenüber Messenger-Apps. Prüfe nach dem Übertragen, ob die Größe zum Original passt: Eine deutlich kleinere Datei wurde abgeschnitten, und keine Reparatur bringt Bytes zurück, die nie angekommen sind."),
        ("Wenn nichts hilft",
         "Eine Datei, die sich nicht reparieren lässt, kann trotzdem lesbar sein, und Lesen genügt oft — der Notiztext lässt sich direkt retten, auch wenn JW Library die Datei ablehnt. Kombiniere das mit einer älteren Sicherung, die sich wiederherstellen lässt, und du hast meist den größten Teil deiner Bibliothek. Bevor du eine Datei für unbrauchbar erklärst, öffne sie und sieh, was wirklich darin steht."),
    ],
    "faq": [
        ("Werden meine Daten für die Prüfung hochgeladen?",
         "Nein. Prüfung, Reparaturen und Export laufen alle lokal im Browser."),
        ("Kann er in JW Library gelöschte Notizen wiederherstellen?",
         "Nein — er repariert die Dateistruktur. Notizen, die vor dem Erstellen der Sicherung "
         "in der App gelöscht wurden, sind gar nicht erst in der Datei."),
        ("Gehen beim Reparieren Notizen verloren?",
         "Reparaturen arbeiten auf einer Kopie und betreffen strukturelle Probleme, nicht den Inhalt. Deine Originaldatei wird nie verändert und bleibt verfügbar, falls du neu ansetzen willst."),
        ("Warum ist meine Sicherung beschädigt worden?",
         "Meist wurde die Datei unterwegs verändert — über eine App gesendet, die sie komprimiert oder abgeschnitten hat, oder durch einen Upload, der nicht fertig wurde. Sie erneut von der Quelle zu übertragen löst es in der Regel."),
        ("Kann eine Prüfung Notizen retten, die ich in JW Library gelöscht habe?",
         "Nein. Ist sie in der App gelöscht und eine neue Sicherung erstellt, steht die Notiz nicht mehr in dieser Datei. Eine Sicherung von vor dem Löschen enthält sie noch."),
        ("Sagt mir die Dateigröße, ob sie abgeschnitten ist?",
         "Oft ja. Vergleiche sie mit dem Original, falls du es noch hast; ein deutlicher Unterschied bedeutet, dass die Übertragung nicht abgeschlossen wurde."),
        ("Lässt sich eine Sicherung, die im Browser aufgeht, sicher wiederherstellen?",
         "Garantiert ist das nicht, aber es ist ein starkes Zeichen, dass Archiv und Datenbank in Ordnung sind, was die häufigsten Fehler ausschließt."),
    ],
}

GUIDES_DE["edit-jw-library-notes"] = {
    "title": "JW-Library-Notizen im Browser ansehen und bearbeiten",
    "h1": "Notizen ansehen, durchsuchen und bearbeiten — der Studien-Explorer",
    "description": "Öffne jede .jwlibrary-Sicherung im Browser, um deine JW-Library-Notizen, "
                   "Markierungen und Lesezeichen zu durchstöbern, zu durchsuchen, zu "
                   "bearbeiten, neu zu verschlagworten, umzufärben und in großen Mengen "
                   "aufzuräumen. Nichts wird hochgeladen.",
    "intro": [
        "JW Library ist zum Notizenmachen gebaut, nicht zum Verwalten von Tausenden davon. "
        "Der Studien-Explorer öffnet jede .jwlibrary-Sicherung direkt im Browser und macht "
        "daraus einen durchsuchbaren, bearbeitbaren Bibliotheksverwalter — Notizen, "
        "Markierungen und Lesezeichen an einem Ort, ohne dass irgendetwas hochgeladen wird.",
    ],
    "steps": [
        ("Lade eine Sicherung",
         "Erstelle in JW Library eine Sicherung (Persönliches Studium → Sicherung und "
         "Wiederherstellung → Sicherung erstellen), öffne dann jwsync.org und lade die Datei "
         "in den Studien-Explorer."),
        ("Durchstöbere und durchsuche alles",
         "Drei Reiter — Notizen, Markierungen, Lesezeichen — mit Volltextsuche sowie Farb-, "
         "Schlagwort- und Publikationsfiltern. Ein Reiter Studienantworten zeigt außerdem "
         "deine ausgefüllten Antworten aus den Publikationen."),
        ("Bearbeite direkt",
         "Öffne eine Notiz, um Titel und Inhalt mit Formatierung zu bearbeiten (fett, kursiv, "
         "unterstrichen, Listen), ihre Markierungsfarbe zu ändern und Schlagwörter "
         "hinzuzufügen oder zu entfernen. Lesezeichen und Markierungsfarben lassen sich "
         "genauso bearbeiten."),
        ("Räume in großen Mengen auf",
         "Wähle viele Notizen auf einmal aus, um sie gemeinsam neu zu verschlagworten, "
         "umzufärben oder zu löschen — mit vollständigem Rückgängig und Wiederholen, ein "
         "Ausrutscher ist also nie endgültig. Du kannst auch einen Zeitraum an Notizen in "
         "eine neue Sicherung herausziehen oder Notizen als Markdown kopieren."),
        ("Exportiere deine bearbeitete Bibliothek",
         "Lade die bearbeitete .jwlibrary herunter und stelle sie in JW Library wieder her. "
         "Deine Änderungen sind jetzt auf dem Gerät."),
    ],
    "sections": [
        ("Warum im Browser bearbeiten statt in der App?",
         "Der Umfang. Ein Schlagwort über 300 Notizen umzubenennen, jede gelbe Markierung in "
         "einer Publikation umzufärben oder Jahre alter Lesezeichen zu löschen, sind hier "
         "Minuten und in der App Stunden des Tippens. Die exportierte Datei ist eine normale "
         "Sicherung, die JW Library wie jede andere wiederherstellt."),
    ],
    "faq": [
        ("Berührt das Bearbeiten meine Originalsicherung?",
         "Nein — Änderungen erfolgen an einer Kopie im Browser und werden in eine neue "
         "exportierte Datei geschrieben. Das Original bleibt, wie es war."),
        ("Gibt es eine Grenze für die Bibliotheksgröße?",
         "Sehr große Bibliotheken werden seitenweise dargestellt, damit das Blättern schnell "
         "bleibt; Suche und Filter gelten für alles."),
    ],
}

GUIDES_DE["search-jw-library-notes"] = {
    "title": "JW-Library-Notizen nach Bedeutung durchsuchen — Frag deine Bibliothek",
    "h1": "Frag deine Bibliothek: durchsuche deine JW-Library-Notizen nach Bedeutung",
    "description": "Semantische Suche für deine JW-Library-Notizen: Finde die halb erinnerte "
                   "Notiz, indem du sie beschreibst, auch wenn dir die genauen Worte fehlen. "
                   "Auf dem Gerät, offlinefähig, privat.",
    "intro": [
        "Wer Jahre an Notizen hat, kennt das Problem: Du erinnerst dich, etwas über das "
        "freudige Ertragen von Prüfungen geschrieben zu haben, aber in der Notiz steht das "
        "Wort „Ausharren“ gar nicht — die Stichwortsuche findet also nichts. Frag deine "
        "Bibliothek sucht stattdessen nach Bedeutung: Beschreib den Gedanken, und die "
        "nächstliegenden Notizen kommen hoch, wie auch immer sie formuliert sind.",
        "Alles läuft auf deinem Gerät: Das Sprachmodell wird einmal in den Browser geladen "
        "und arbeitet danach offline, mit WebGPU-Beschleunigung, wo verfügbar. Deine Notizen "
        "werden nie irgendwohin geschickt.",
    ],
    "steps": [
        ("Lade eine Sicherung in den Studien-Explorer",
         "Lade auf jwsync.org deine .jwlibrary-Datei und öffne den Reiter Fragen."),
        ("Lass das Modell sich einmal vorbereiten",
         "Beim ersten Mal wird das Modell auf dem Gerät geladen und indiziert deine Notizen. "
         "Das passiert einmal; danach geht es sofort, sogar offline."),
        ("Frag in deinen eigenen Worten",
         "Tippe, woran du dich erinnerst — „die Notiz über Geduld mit Neuen im Predigtdienst“, "
         "„Ermunterung für entmutigte Pioniere“ — und die nächstliegenden Notizen erscheinen, "
         "nach Bedeutung sortiert."),
    ],
    "sections": [
        ("Wie sich das von der normalen Suche unterscheidet",
         "Die Stichwortsuche vergleicht Buchstaben; die semantische Suche vergleicht Gedanken. "
         "Eine Anfrage zu „Angst“ findet auch Notizen mit „Sorge“, „Sorgen des Lebens“ oder "
         "einem Bibeltext zum Thema. Beide Suchformen gibt es im Studien-Explorer — sie "
         "ergänzen einander."),
        ("Privat von Grund auf",
         "Das ist kein KI-Dienst in der Cloud. Das Modell läuft in deinem Browser-Tab, der "
         "Index liegt auf deinem Gerät, und mit dem Schließen des Tabs ist Schluss. Nichts "
         "über deine Notizen verlässt je deinen Rechner."),
    ],
    "faq": [
        ("Braucht es ein leistungsstarkes Gerät?",
         "Ein modernes Handy oder Notebook schafft das gut; auf Geräten mit WebGPU ist es am "
         "schnellsten. Es gibt verschiedene Modellgrößen passend zu deiner Hardware."),
        ("Funktioniert es in meiner Sprache?",
         "Ja — die Suche funktioniert in den Sprachen, in denen deine Notizen geschrieben "
         "sind, und die Oberfläche ist in alle 12 von JW Sync unterstützten Sprachen "
         "übersetzt."),
    ],
}

GUIDES_DE["jw-library-study-stats"] = {
    "title": "Deine JW-Library-Studienstatistik: Serien, Heatmaps und Auszeichnungen",
    "h1": "Deine JW-Library-Studienstatistik: Serien, Heatmaps, Abdeckung und Auszeichnungen",
    "description": "Verwandle eine JW-Library-Sicherung in private Studienanalysen — Summen, "
                   "Aktivitäts-Heatmap, Serien, Bibelabdeckung über alle 66 Bücher, ein "
                   "Studienprofil und rund 200 Auszeichnungen.",
    "intro": [
        "Deine Sicherungsdatei hält still und leise Jahre an Studiengeschichte fest — wann du "
        "Notizen machst, was du markierst, welche Bücher du behandelt hast. Die Seite "
        "Studienstatistik liest eine .jwlibrary-Sicherung und macht aus dieser Geschichte ein "
        "privates Dashboard, vollständig in deinem Browser berechnet.",
    ],
    "steps": [
        ("Erstelle eine Sicherung",
         "In JW Library: Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen."),
        ("Öffne die Seite Studienstatistik",
         "Geh auf jwsync.org/highlights.html und lade die Datei."),
        ("Erkunde deine Studiengeschichte",
         "Die großen Summen, Ansichten für das Dienstjahr und für die ganze Zeit, das "
         "Wachstum von Jahr zu Jahr — und weiter unten die schönen Teile."),
    ],
    "sections": [
        ("Was du sehen wirst",
         "Eine Aktivitäts-Heatmap mit deiner längsten und deiner aktuellen Serie; "
         "Wochenrhythmus, geschäftigste Stunden und Monate; Bibelabdeckung über alle 66 "
         "Bücher mit Aufteilung in Hebräische und Griechische Schriften; ein Farbrad der "
         "Markierungen, ein Histogramm der Notiztiefe und eine Wortwolke; eine "
         "24-Stunden-Studienuhr und ein Saisonalitäts-Radar."),
        ("Profil, Reise und Auszeichnungen",
         "Ein Studienprofil mit sechs Merkmalen (Beständigkeit, Fleiß, Tiefe, Breite, "
         "Nachdenken, Stetigkeit) samt einer „Studien-Signatur“; eine Studienreise über 60 "
         "Stufen in 12 benannten Rängen; und rund 200 Auszeichnungen von Gewöhnlich bis "
         "Legendär, darunter inhaltsbezogene Medaillen. Eine teilbare Karte fasst dein Jahr "
         "zusammen, ohne eine einzige Notiz preiszugeben."),
        ("Ein täglicher Grund zurückzukommen",
         "Die Wiedervorlage zeigt Notizen, die du an diesem Tag in früheren Jahren "
         "geschrieben hast, und baut daraus eine sanfte, verteilte Wiederholung — ein wenig, "
         "aber oft, so bleibt Studiertes hängen."),
    ],
    "faq": [
        ("Wird davon irgendetwas hochgeladen?",
         "Nein. Die Sicherung wird in deinem Browser ausgewertet; die Statistiken verlassen "
         "nie dein Gerät."),
        ("Aktualisiert sich die Statistik von selbst?",
         "Sie spiegelt die Sicherung wider, die du lädst — erstelle eine frische Sicherung "
         "für frische Zahlen."),
    ],
}

GUIDES_DE["share-jw-library-notes"] = {
    "title": "JW-Library-Notizen mit einem Freund teilen",
    "h1": "So teilst du JW-Library-Notizen mit einem Freund — ganz ohne Server",
    "description": "Schick ausgewählte JW-Library-Notizen (samt Markierungen) als kleine Datei "
                   "an einen Freund — ohne Server, ohne Konto. Der Empfänger fügt sie ein, "
                   "ohne eigene Notizen zu überschreiben.",
    "intro": [
        "JW Library bietet keine Möglichkeit, jemandem eine Kopie bestimmter Notizen zu geben. "
        "Die ganze Sicherung zu schicken würde funktionieren — aber sie gibt alles preis, und "
        "das Wiederherstellen würde die Bibliothek des Empfängers löschen. Das Notizenteilen "
        "von JW Sync löst beides: Du wählst genau, welche Notizen du teilst, und der "
        "Empfänger fügt sie hinzu, ohne etwas zu verlieren.",
    ],
    "steps": [
        ("Wähle die Notizen zum Teilen aus",
         "Lade auf der Teilen-Seite unter jwsync.org/share.html deine Sicherung und wähle die "
         "Notizen aus — eine Handvoll aus einem Vortrag, oder mit dem Schlagwortfilter der "
         "Auswahl alles unter einem Schlagwort mit einem Klick. Markierungen, die an diesen "
         "Notizen hängen, kommen mit."),
        ("Schick die Teilen-Datei",
         "JW Sync erzeugt eine kleine Datei mit ausschließlich den ausgewählten Notizen. "
         "Schick sie über den Kanal deiner Wahl — Messenger, E-Mail, AirDrop. Es gibt keinen "
         "Server und kein Konto; die Datei ist der ganze Austausch."),
        ("Der Empfänger fügt sie ein",
         "Dein Freund öffnet dieselbe Seite, lädt die Teilen-Datei zusammen mit seiner "
         "eigenen Sicherung und erhält eine neue Sicherung mit deinen Notizen darin. Seine "
         "eigenen Notizen werden nie überschrieben — kollidiert eine geteilte Notiz mit einer "
         "seiner Notizen, wählt er, wie sie eingefügt wird — und importierte Notizen kommen "
         "verschlagwortet an, sind also leicht zu finden, durchzusehen oder später zu "
         "entfernen."),
    ],
    "sections": [
        ("Gute Anwendungen",
         "Recherche an einen Studienpartner weitergeben, Notizen einer Zusammenkunft mit "
         "jemandem teilen, der gefehlt hat, einem neuen Verkündiger einen Grundstock an "
         "Notizen zu einer Publikation geben, oder die Notizen eines bestimmten Projekts an "
         "ein Familienmitglied weiterreichen — ohne den Rest einer der beiden Bibliotheken "
         "preiszugeben."),
    ],
    "faq": [
        ("Muss der Empfänger JW Sync installieren?",
         "Auf keiner Seite wird etwas installiert — es ist eine Webseite. Der Empfänger "
         "braucht nur die Teilen-Datei und seine eigene Sicherung."),
        ("Kann ich das Teilen zurücknehmen oder die Datei ablaufen lassen?",
         "Die Datei ist eine ganz normale Datei, die du verschickt hast — es gibt keine "
         "Serverkopie, die ablaufen könnte. Teile nur, was du auch in einer Nachricht teilen "
         "würdest."),
    ],
}

GUIDES_DE["bible-reading-plan"] = {
    "title": "Ein täglicher Bibelleseplan mit deinen eigenen Notizen daneben",
    "h1": "Lesebegleiter: ein Bibelleseplan mit deinen eigenen Notizen daneben",
    "description": "Ein privater täglicher Bibelleseplan, der dir die Notizen und Markierungen "
                   "zeigt, die du zu den heutigen Kapiteln gemacht hast. Wähle dein Tempo, "
                   "halte eine Serie, sieh dem Raster aus 66 Büchern beim Füllen zu.",
    "intro": [
        "Bibelleseplände gibt es in vielen Apps. Der Lesebegleiter kann etwas, das keine "
        "andere kann: Weil er deine eigene .jwlibrary-Sicherung liest, kommt die heutige "
        "Lesung mit genau den Notizen und Markierungen, die du selbst zu diesen Kapiteln "
        "gemacht hast — „du hast vor zwei Jahren vier Verse in Psalm 37 markiert“. Lesen durch "
        "die Linse deiner eigenen Studiengeschichte, vollständig auf deinem Gerät.",
    ],
    "steps": [
        ("Wähle Reihenfolge und Tempo",
         "Lies in Bibelreihenfolge oder in ungefähr chronologischer Ordnung; schaff es in 3 "
         "Monaten, 6 Monaten, 1 Jahr, 2 Jahren, oder setz dein eigenes Tempo an Kapiteln pro "
         "Tag — mit einer laufenden Vorschau „du wärst etwa fertig am …“."),
        ("Lies den heutigen Abschnitt",
         "Jedes Kapitel ist ein Tippen entfernt und öffnet sich direkt in JW Library oder in "
         "der WACHTTURM ONLINE-BIBLIOTHEK in deiner Sprache. Hake die Kapitel ab, während du "
         "vorankommst."),
        ("Nimm deine Notizen mit (optional)",
         "Lade eine Sicherung in ein beliebiges JW-Sync-Werkzeug, und deine eigenen Notizen "
         "und Markierungszahlen erscheinen direkt unter den heutigen Kapiteln."),
        ("Sieh dem Fortschritt beim Wachsen zu",
         "Ein Raster aus 66 Büchern füllt sich beim Lesen, mit einem Balken gelesener Kapitel, "
         "einer Tempo-Prognose und Meilensteinen für jedes abgeschlossene Buch, die "
         "Hebräisch-Aramäischen Schriften, die Griechischen Schriften — und die ganze Bibel."),
    ],
    "sections": [
        ("Serien ohne schlechtes Gewissen",
         "Einen Tag abzuschließen lässt deine Serie wachsen; einen Tag auszulassen verschiebt "
         "nur das prognostizierte Enddatum. Es gibt keinen Berg an Rückstand — der Plan passt "
         "sich deinem Leben an, statt dich zu tadeln."),
    ],
    "faq": [
        ("Muss ich eine Sicherung laden, um ihn zu benutzen?",
         "Nein — Plan, Serien und Fortschritt funktionieren für sich. Die Sicherung fügt nur "
         "deine persönlichen Notizen zur Lesung jedes Tages hinzu."),
        ("Ist mein Lesefortschritt privat?",
         "Ja. Der Fortschritt liegt in deinem Browser auf deinem Gerät — es gibt kein Konto "
         "und nichts wird hochgeladen."),
    ],
}

GUIDES_DE["open-jwlibrary-file"] = {
    "title": "Was ist eine .jwlibrary-Datei und wie öffnet man sie?",
    "h1": "Was eine .jwlibrary-Datei ist — und wie du eine auf jedem Gerät öffnest",
    "description": "Eine .jwlibrary-Datei ist deine JW-Library-Sicherung: eine einzige Datei "
                   "mit jeder Notiz, Markierung, jedem Lesezeichen und Schlagwort. Was drin "
                   "steckt und wie du sie öffnest und liest.",
    "intro": [
        "Eine .jwlibrary-Datei wirkt undurchsichtig, ist es aber nicht. Sie ist ein gewöhnliches ZIP-Archiv um eine gewöhnliche SQLite-Datenbank, was bedeutet: Du kannst deine eigene Sicherung lesen — genau sehen, welche Notizen, Markierungen und Lesezeichen sie enthält — ohne JW Library und ohne irgendetwas zu installieren.",
        "Wenn du JW Library sicherst, bekommst du eine Datei mit der Endung .jwlibrary. Sie "
        "ist ein einziges, tragbares Paket mit allem aus deinem persönlichen Studium — "
        "Notizen, Markierungen, Lesezeichen, Schlagwörter und Wiedergabelisten — in einer "
        "kompakten Datenbank. Es ist kein Dokument, das man in Word oder einem PDF-Programm "
        "öffnet; sie ist dafür gedacht, wieder in JW Library eingespielt zu werden.",
        "Aber du musst sie nicht erst wiederherstellen, um hineinzuschauen. JW Sync öffnet "
        "eine .jwlibrary-Datei direkt in deinem Browser, sodass du ihren Inhalt lesen, "
        "durchsuchen und bearbeiten kannst, ohne dein Handy anzufassen.",
    ],
    "steps": [
        ("Besorg dir eine .jwlibrary-Datei",
         "Sie entsteht in JW Library: Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Von dieser Datei ist die Rede."),
        ("Öffne sie in JW Sync",
         "Geh auf jwsync.org und lade die Datei in den Studien-Explorer. Sie öffnet sich "
         "sofort, auf deinem Gerät — nichts wird hochgeladen."),
        ("Lies sie und arbeite damit",
         "Durchstöbere Notizen, Markierungen und Lesezeichen; durchsuche alles; bearbeite, "
         "verschlagworte neu oder exportiere. Wenn du fertig bist, kannst du die Datei (oder "
         "eine bearbeitete Kopie) wieder in JW Library einspielen."),
    ],
    "sections": [
        ("Was tatsächlich in der Datei steckt",
         "Technisch ist eine .jwlibrary-Datei eine gepackte SQLite-Datenbank plus ein "
         "Manifest. Deshalb wird sie unterwegs manchmal versehentlich in .zip umbenannt — und "
         "deshalb hilft das Zurückbenennen in .jwlibrary. Du musst nichts davon wissen, um "
         "sie zu benutzen, aber es erklärt, warum die Datei klein, in sich geschlossen und "
         "auf Android, iPhone, iPad und Windows identisch ist."),
        ("Am Computer öffnen",
         "Dieselbe Seite jwsync.org funktioniert im Browser eines Notebooks oder Desktops — "
         "praktisch, um Jahre an Notizen auf großem Bildschirm zu lesen oder Aufräumarbeiten "
         "zu erledigen, die am Handy mühsam wären. Nichts zu installieren."),
        ("Was die Datei wirklich ist",
         "Eine .jwlibrary-Datei ist ein ZIP-Archiv mit einer anderen Endung. Darin liegen userData.db — eine SQLite-Datenbank mit deinen Notizen, Markierungen, Lesezeichen und Schlagwörtern — und manifest.json, eine kleine Datei, die die Sicherung beschreibt und eine Prüfsumme der Datenbank enthält, mit der JW Library bestätigt, dass die Datei unverändert ist. Nichts daran ist proprietär oder verschlüsselt: Es ist ein Standardarchiv um eine Standarddatenbank."),
        ("Sie ohne JW Library öffnen",
         "Du brauchst weder die App noch sonst eine Software, um deine eigene Sicherung zu lesen. Die Datei im Browser zu öffnen zeigt alle Notizen, Markierungen und Lesezeichen darin, mit Suche und Filtern, und die Datei verlässt dein Gerät nie — sie wird lokal gelesen, nicht hochgeladen. Das ist der schnellste Weg zu bestätigen, dass eine Sicherung enthält, was du glaubst, bevor du zurücksetzt, abgibst oder auf einem neuen Telefon wiederherstellst."),
        ("Von Hand hineinsehen",
         "Wenn dich interessiert, was drin ist, kopiere die Datei, benenne die Kopie in .zip um und öffne sie mit einem beliebigen Archivwerkzeug. Du siehst userData.db und manifest.json. Die Datenbank zu öffnen braucht einen SQLite-Betrachter, und die Tabellen heißen nach dem, was sie enthalten — Note, UserMark, Bookmark, Tag. Arbeite immer auf einer Kopie: Die Datenbank von Hand zu ändern, ohne die Prüfsumme im Manifest zu erneuern, erzeugt eine Datei, die JW Library beim Wiederherstellen ablehnt."),
        ("Sicher bearbeiten",
         "Notizen lassen sich außerhalb der App korrigieren, neu verschlagworten, umfärben oder löschen, und das Ergebnis als neue .jwlibrary-Datei exportieren, die du normal wiederherstellst. Die Regel, die das sicher macht, ist, das Original zu behalten: Bearbeite eine Kopie, stelle die bearbeitete Datei wieder her, und falls etwas nicht wie erwartet ist, liegt das unangetastete Original noch da."),
        ("Eine Sicherung auf dem Telefon lesen",
         "Ein Computer ist nicht nötig. Die Datei in einem mobilen Browser zu öffnen funktioniert genauso, was nützlich ist, wenn die Sicherung schon auf dem Telefon liegt und du ihren Inhalt vor dem Wiederherstellen oder vor dem Löschen des Geräts prüfen willst. Die Datei wird lokal gelesen, das funktioniert also ohne weitere Verbindung als die zum Laden der Seite."),
        ("Warum die Prüfsumme im Manifest zählt",
         "manifest.json hält eine Prüfsumme von userData.db fest. JW Library bestätigt damit, dass die Datenbank seit dem Schreiben der Sicherung unverändert ist — eine Datei, deren Datenbank ohne Neuberechnung der Prüfsumme bearbeitet wurde, wird beim Wiederherstellen abgelehnt. Das ist der häufigste Grund, warum eine von Hand bearbeitete Sicherung nicht mehr funktioniert, und der Grund, warum ein Werkzeug, das das Manifest neu schreibt, sicherer ist als der direkte Griff in die Datenbank."),
        ("Wofür das gut ist",
         "Eine Sicherung lesen zu können ändert, was eine Sicherung wert ist. Du kannst bestätigen, dass eine Datei enthält, was du denkst, bevor du ein Telefon löschst, prüfen, ob eine alte Datei das Wiederherstellen lohnt, eine Notiz finden, von der du weißt, dass du sie geschrieben hast, ohne die App zu durchsuchen, oder Text aus einer Datei retten, die JW Library ablehnt. Nichts davon verlangt, die Datei jemandem anzuvertrauen — sie wird auf deinem eigenen Gerät gelesen."),
    ],
    "faq": [
        ("Kann ich eine .jwlibrary-Datei in Excel oder im Editor öffnen?",
         "Nicht sinnvoll — es ist eine Datenbank, keine Tabelle und keine Textdatei. Öffne sie "
         "in JW Sync zum Lesen, oder exportiere deine Notizen aus dem Studien-Explorer als "
         "Markdown/Text."),
        ("Ist es sicher, meine Sicherung im Browser zu öffnen?",
         "Ja. JW Sync liest die Datei lokal in deinem Browser-Tab; nichts wird an einen Server "
         "geschickt, und deine Originaldatei wird nie verändert."),
        ("Kann ich sie einfach in .zip umbenennen?",
         "Ja, auf einer Kopie. Das Umbenennen ändert den Inhalt nicht und lässt jedes Archivwerkzeug zeigen, was darin steckt."),
        ("Verändert das Öffnen die Datei?",
         "Nein. Eine Sicherung zu lesen — im Browser oder in einem Archivwerkzeug — lässt sie Byte für Byte unverändert. Erst Speichern oder Exportieren erzeugt eine neue Datei."),
        ("Muss ich online sein?",
         "Nur zum Laden der Seite. Die Datei wird auf deinem Gerät gelesen und nicht hochgeladen, deine Notizen gehen also nie über das Netz."),
        ("Kann ich eine Sicherung öffnen, die mir jemand geschickt hat?",
         "Ja, das Format ist weder an ein Gerät noch an ein Konto gebunden. Ob du sie wiederherstellen solltest, ist eine andere Frage, denn eine Wiederherstellung ersetzt deine eigene Bibliothek."),
        ("Muss ich etwas installieren, um hineinzusehen?",
         "Nein. Ein Browser genügt zum Lesen der Notizen; nur die manuelle Untersuchung der Datenbank braucht einen SQLite-Betrachter."),
    ],
}

GUIDES_DE["jw-library-windows-pc"] = {
    "title": "JW Library auf einem Windows-PC sichern und zusammenführen",
    "h1": "JW-Library-Sicherungen auf einem Windows-PC nutzen",
    "description": "So sicherst du JW Library unter Windows und führst die PC-Sicherung mit "
                   "Handy und Tablet zusammen, damit Notizen, Markierungen und Lesezeichen auf "
                   "jedem Gerät beisammen bleiben.",
    "intro": [
        "JW Library läuft unter Windows genauso wie auf Handys und Tablets und erzeugt "
        "dieselbe .jwlibrary-Sicherungsdatei. Dein PC kann also Teil derselben "
        "Studienbibliothek sein wie dein Handy — solange du die Sicherungen zusammenführst, "
        "statt eine über die andere wiederherzustellen.",
    ],
    "steps": [
        ("Sichere unter Windows",
         "Öffne in der JW-Library-App für Windows das Menü, geh zu Sicherung und "
         "Wiederherstellung und erstelle eine Sicherung. Speichere die .jwlibrary-Datei an "
         "einem gut auffindbaren Ort."),
        ("Sichere auch Handy und Tablet",
         "Auf jedem Gerät: Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen."),
        ("Führe sie auf jwsync.org zusammen",
         "Öffne jwsync.org in einem beliebigen Browser am PC und lade alle Sicherungsdateien. "
         "JW Sync vereint die Notizen, Markierungen, Lesezeichen und Schlagwörter jedes Geräts "
         "in einer zusammengeführten .jwlibrary-Datei — lokal, ohne Upload."),
        ("Stelle die zusammengeführte Datei überall wieder her",
         "Spiel die zusammengeführte Datei in der Windows-App und auf jedem Mobilgerät ein. "
         "Jetzt tragen PC, Handy und Tablet die vollständige Bibliothek."),
    ],
    "sections": [
        ("Warum der PC dafür der bequemste Ort ist",
         "Am Desktop-Browser geht das Laden mehrerer Dateien, das Prüfen der "
         "Zusammenführungs-Vorschau und das Speichern des Ergebnisses deutlich schneller als "
         "Tippen am Handy. Viele halten ihre Haupt-Zusammenführungsroutine am Computer und "
         "spielen die zusammengeführte Datei anschließend nur noch auf ihre Mobilgeräte ein."),
    ],
    "faq": [
        ("Funktioniert die Windows-Sicherung mit iPhone- und Android-Sicherungen?",
         "Ja — das .jwlibrary-Format ist auf allen Plattformen identisch, eine "
         "Windows-Sicherung lässt sich also frei mit Handy- und Tablet-Sicherungen "
         "zusammenführen."),
        ("Muss ich etwas auf dem PC installieren?",
         "Nein. JW Sync ist eine Webseite; sie läuft in Edge, Chrome oder Firefox, ohne "
         "Installation."),
    ],
}

GUIDES_DE["recover-jw-library-notes-lost-phone"] = {
    "title": "JW-Library-Notizen nach einem verlorenen oder kaputten Handy retten",
    "h1": "JW-Library-Notizen von einem verlorenen, kaputten oder zurückgesetzten Handy retten",
    "description": "Handy verloren oder zurückgesetzt, mit JW-Library-Notizen darauf? Was du "
                   "retten kannst, hängt von deinen Sicherungen ab. So holst du deine Notizen "
                   "zurück — und so machst du es beim nächsten Mal.",
    "intro": [
        "Zuerst die ehrliche Antwort, sie erspart dir das Weiterlesen. Existiert irgendwo außerhalb des verlorenen Geräts eine .jwlibrary-Sicherung, kommt alles darin über die Wiederherstellung von JW Library selbst zurück — dafür brauchst du diese Seite nicht. Existiert überhaupt keine Sicherung, lassen sich persönliche Studiendaten gar nicht wiederherstellen: Sie liegen nur auf dem Gerät, und daran ändert kein Werkzeug etwas.",
        "Wirklich helfen kann diese Seite im mittleren Fall, und der ist häufiger als die beiden anderen: Du hast eine Sicherung, aber sie erzählt nicht die ganze Geschichte. Sie kann Monate alt sein, oder du hast auf dem Ersatzhandy schon studiert — sie einfach wiederherzustellen würde dann einen Satz Notizen gegen einen anderen tauschen, statt dir alles zu geben.",
        "Beides zu vereinen ist genau das, was JW Library nicht kann, und darum geht es im Rest dieser Seite. Zuerst aber die Suche: Man hat regelmäßig mehr Sicherungen, als man sich zu machen erinnert.",
    ],
    "steps": [
        ("Such an jedem Ort, wo eine Sicherung liegen könnte",
         "Prüfe deine E-Mails (such nach „jwlibrary“ oder „Sicherung“), Google Drive, iCloud "
         "Drive, OneDrive, Dropbox und den Download-Ordner deines Computers. Sicherungen sind "
         "kleine Dateien, die man leicht vergisst."),
        ("Prüfe deine anderen Geräte",
         "Hast du JW Library je auf einem Tablet oder PC benutzt, hat es eigene Studiendaten — "
         "erstelle sofort davon eine Sicherung, um zu bewahren, was darin ist."),
        ("Stelle das Gefundene auf dem neuen Handy wieder her",
         "Installiere JW Library auf dem neuen Gerät, dann Sicherung und Wiederherstellung → "
         "Wiederherstellen und lade die .jwlibrary-Datei. Deine Notizen, Markierungen und "
         "Lesezeichen kommen zurück."),
        ("Führe zusammen, wenn du mehr als eine Sicherung findest",
         "Verschiedene Geräte oder Zeitpunkte können jeweils eigene Notizen enthalten. Wähl "
         "nicht nur eine — lade alle auf jwsync.org, führe sie zu einer vollständigen Datei "
         "zusammen und stelle diese wieder her. Nichts bleibt zurück."),
    ],
    "sections": [
        ("Wenn es nirgends eine Sicherung gibt",
         "Sei früh ehrlich zu dir: Wenn die einzige Kopie deiner Notizen auf dem verlorenen "
         "Handy lag und du nie eine Sicherung exportiert hast, hält JW Library keine "
         "Cloud-Kopie bereit. Das tut weh — und genau deshalb ist die Gewohnheit unten so "
         "wichtig."),
        ("Nie wieder hier landen",
         "Richte eine monatliche Sicherungs-Erinnerung ein und lege jede .jwlibrary-Datei "
         "außerhalb des Handys ab (sie sich selbst zu mailen genügt). JW Sync kann dich sogar "
         "erinnern und deine Geräte regelmäßig zusammenführen. Eine Datei im Posteingang "
         "überlebt jedes Handy."),
        ("Wo bereits eine Sicherung liegen könnte",
         "Bevor du schließt, es gebe keine, prüfe jeden Ort, an dem eine Datei gespeichert worden sein könnte: die Ordner Downloads und Dokumente jedes Computers, mit dem du das Telefon verbunden hast, deine gesendeten E-Mails, Messenger-Apps, über die du die Datei geschickt haben könntest, und jedes Cloud-Konto, das du nutzt. Viele haben einmal, vor Monaten, eine Sicherung erstellt und es vergessen — und eine Monate alte Sicherung enthält immer noch den weitaus größten Teil einer Studienbibliothek."),
        ("Auf einem anderen Telefon oder einer anderen Plattform wiederherstellen",
         "Das Ersatzgerät muss dem verlorenen nicht entsprechen. Eine Sicherung von einem Android-Telefon stellt sich auf einem iPhone wieder her und umgekehrt, denn das Format ist unter Android, iOS, iPadOS und Windows identisch. Installiere JW Library auf dem neuen Gerät, aktualisiere es auf die aktuelle Version und stelle über Persönliches Studium → Sicherung und Wiederherstellung wieder her."),
        ("Wenn du nur eine alte oder unvollständige Sicherung hast",
         "Stelle sie trotzdem wieder her. Den größten Teil deiner Notizen zurückzubekommen ist kein Trostpreis — es ist das Ergebnis. Findest du später eine zweite, andere Sicherung, lassen sich beide zu einer Datei mit allem aus beiden zusammenführen: Die ältere jetzt wiederherzustellen hindert dich also nicht daran, später zu ergänzen."),
        ("Was sich nicht wiederherstellen lässt",
         "Existiert in keiner Form eine Sicherung, lassen sich persönliche Studiendaten nicht zurückholen. Sie liegen ausschließlich im app-eigenen Speicher auf dem Gerät, und weder JW Library noch eine Cloud-Sicherung auf Telefonebene bewahrt sie zuverlässig. Das gehört klar gesagt, denn es ist der Grund, warum es die Routine auf dieser Seite überhaupt gibt."),
        ("Prüfe, bevor das Gerät aus der Ferne gelöscht wird",
         "Ist das Telefon verloren und nicht zerstört und erwägst du eine Fernlöschung, suche zuerst nach vorhandenen Sicherungen: Das Löschen ist unumkehrbar und nimmt die letzte Möglichkeit, noch eine zu erstellen. Ist das Gerät nur verlegt und weiterhin erreichbar, lässt sich aus der Ferne keine Sicherung erstellen, doch die Daten bleiben unversehrt, solange es weder gelöscht noch zurückgesetzt wird."),
        ("Dafür sorgen, dass das kein zweites Mal passiert",
         "Dass ein verlorenes Telefon Jahre des Studiums kostet, liegt daran, dass die einzige Kopie auf dem Telefon lag. Hast du auf einem Ersatzgerät wiederhergestellt, lege noch am selben Tag eine Sicherung außerhalb des Geräts ab und wiederhole das in einem Rhythmus, den du wirklich hältst. Die Dateien sind klein genug, um sie alle unbegrenzt aufzubewahren."),
        ("Wenn es wirklich keine Sicherung gibt",
         "Dann ist die ehrliche Antwort, dass die Notizen nicht wiederherstellbar sind, und das zu hören ist besser als weiterzusuchen. Was du tun kannst, ist, diesen Verlust zum letzten zu machen: Installiere JW Library auf dem Ersatzgerät und erstelle, bevor du etwas aufgebaut hast, dessen Verlust schmerzen würde, eine Sicherung außerhalb des Geräts. Von da an kostet dich dasselbe Ereignis nichts."),
    ],
    "faq": [
        ("Kann JW Sync Notizen von einem Handy retten, das ich nicht mehr habe?",
         "Kein Werkzeug kann das — die Rettung hängt daran, dass irgendwo eine Sicherungsdatei "
         "existiert. JW Syncs Aufgabe ist es, die Sicherungen zu lesen, zu reparieren und "
         "zusammenzuführen, die du hast."),
        ("Meine Sicherung ist alt — lohnt sich das Wiederherstellen noch?",
         "Unbedingt. Eine alte Sicherung mit dem Großteil deiner Notizen schlägt einen "
         "Neuanfang bei null, und du kannst sie später mit allem Neueren zusammenführen, das "
         "du noch findest."),
        ("Bewahrt JW Library eine Kopie meiner Notizen in der Cloud auf?",
         "Nein. Persönliche Studiendaten bleiben auf dem Gerät, sofern du nicht selbst eine Sicherungsdatei erstellst."),
        ("Lassen sich Notizen von einem Telefon mit kaputtem Display retten?",
         "Manchmal — wenn das Telefon noch startet und sich bedienen lässt, oder eine Werkstatt die Anzeige ansteuern kann, kann JW Library weiterhin eine Sicherung erstellen. Die Daten sind unversehrt, solange der Speicher es ist."),
        ("Lässt sich eine alte Sicherung noch in der aktuellen App wiederherstellen?",
         "Ja. JW Library liest ältere Sicherungsformate. Aktualisiere zuerst die App und stelle in der aktuellen Version wieder her."),
        ("Ich habe zwei alte Sicherungen gefunden — welche nehme ich?",
         "Keine für sich allein: Führe sie zusammen. Das Ergebnis enthält alles aus beiden, auch das, was in der älteren stand und zum Zeitpunkt der neueren bereits gelöscht war."),
        ("Kann ich vor dem Wiederherstellen sehen, was in einer Sicherung ist?",
         "Ja. Öffne die Datei im Browser und sieh dir zuerst ihre Notizen, Markierungen und Lesezeichen an, damit du weißt, was du wiederherstellst."),
    ],
}

GUIDES_DE["handle-merge-conflicts"] = {
    "title": "Dieselbe Notiz auf zwei Geräten bearbeitet? Konflikte beim Zusammenführen",
    "h1": "Konflikte beim Zusammenführen: dieselbe Notiz auf zwei Geräten bearbeitet",
    "description": "Wenn du dieselbe JW-Library-Notiz auf zwei Geräten unterschiedlich "
                   "bearbeitest, muss die Zusammenführung entscheiden. Der Konfliktvergleich "
                   "zeigt beide Fassungen nebeneinander, damit du wählst — nichts geht "
                   "verloren.",
    "intro": [
        "Das meiste beim Zusammenführen geht mühelos — Notizen, die es nur auf einem Gerät "
        "gibt, kommen einfach zusammen. Der einzige Fall, der eine Entscheidung braucht, ist "
        "ein echter Konflikt: dieselbe Notiz, auf zwei Geräten unterschiedlich bearbeitet, "
        "sodass die beiden Sicherungen uneins sind, was darin stehen soll. JW Sync rät nie "
        "still vor sich hin; es übergibt dir die Wahl.",
    ],
    "steps": [
        ("Lade beide Sicherungen",
         "Lade auf jwsync.org die .jwlibrary-Dateien beider Geräte. JW Sync vergleicht sie "
         "beim Zusammenführen."),
        ("Öffne den Konfliktvergleich",
         "Gibt es Notizen im Konflikt, listet der Vergleich sie auf. Alles Konfliktfreie ist "
         "bereits zusammengeführt — dieser Schritt betrifft nur die echten Zusammenstöße."),
        ("Vergleiche nebeneinander",
         "Jeder Konflikt zeigt beide Fassungen mit Wort-für-Wort hervorgehobenen "
         "Unterschieden. „Beste vorschlagen“ kann die vollständigere Fassung für dich wählen, "
         "oder du entscheidest selbst — Notiz für Notiz."),
        ("Abschließen und wiederherstellen",
         "Sind alle Konflikte gelöst, lade die zusammengeführte Datei herunter und stelle sie "
         "wieder her. Beide Geräte sind sich nun einig, mit deiner gewählten Fassung jeder "
         "Notiz."),
    ],
    "sections": [
        ("Warum das besser ist, als einfach die neueste zu behalten",
         "„Die neueste gewinnt“ löscht still Bearbeitungen, die du vielleicht behalten "
         "wolltest. Womöglich enthielt die ältere Fassung einen Absatz, den du auf dem anderen "
         "Gerät versehentlich entfernt hast. Beide zu sehen, Wort für Wort, heißt, dass du nie "
         "unbemerkt Text verlierst — und genau darum geht es beim Zusammenführen statt "
         "Überschreiben."),
        ("Wie Konflikte überhaupt entstehen",
         "Meist durch Offline-Bearbeitung auf zwei Geräten zwischen zwei Zusammenführungen, "
         "oder durch das Wiederherstellen einer alten Sicherung und anschließendes Ergänzen. "
         "Regelmäßiges Zusammenführen hält die Zahl der Konflikte klein und die Unterschiede "
         "frisch in Erinnerung."),
    ],
    "faq": [
        ("Muss ich Hunderte Konflikte durchsehen?",
         "Selten. Nur Notizen, die auf beiden Seiten unterschiedlich bearbeitet wurden, "
         "kollidieren; neue Notizen und solche, die nur auf einem Gerät geändert wurden, "
         "werden automatisch zusammengeführt. Die meisten Zusammenführungen haben eine "
         "Handvoll Konflikte oder gar keine."),
        ("Kann ich es mir nach der Wahl anders überlegen?",
         "Ja — nichts wird auf ein Gerät geschrieben, bis du die zusammengeführte Datei "
         "wiederherstellst, und deine ursprünglichen Sicherungen werden nie verändert. Du "
         "kannst die Zusammenführung also neu machen."),
    ],
}

GUIDES_DE["export-jw-library-notes"] = {
    "title": "JW-Library-Notizen als Text oder Markdown exportieren",
    "h1": "Deine JW-Library-Notizen als Text, Markdown oder neue Sicherung exportieren",
    "description": "Hol deine JW-Library-Notizen aus der App: kopiere oder exportiere sie als "
                   "Markdown/reinen Text für jede Verwendung, oder zieh eine Auswahl in eine "
                   "neue .jwlibrary-Sicherung. Alles im Browser.",
    "intro": [
        "In JW Library geschriebene Notizen sind in der App leicht zu lesen und überall sonst unhandlich — in einem Dokument, in einer Vortragsgliederung, auf Papier oder in den Händen von jemandem, der die App nicht nutzt. Der Export löst das, und die Hauptfrage ist nicht wie, sondern wie viel: Ein gefilterter Export ist fast immer nützlicher als alles auf einmal.",
        "Deine Studiennotizen sollten nicht in einer App gefangen sein. Mal willst du sie als "
        "reinen Text — für ein Vortragsgerüst, ein Dokument oder deine eigene Notiz-App — und "
        "mal willst du eine saubere Sicherung mit nur einem Teil davon. Der Studien-Explorer "
        "kann beides und liest deine Sicherung vollständig im Browser.",
    ],
    "steps": [
        ("Lade deine Sicherung",
         "Erstelle in JW Library eine Sicherung (Persönliches Studium → Sicherung und "
         "Wiederherstellung → Sicherung erstellen), öffne dann jwsync.org und lade sie in den "
         "Studien-Explorer."),
        ("Finde die gewünschten Notizen",
         "Nutze die Suche zusammen mit Farb-, Schlagwort- und Publikationsfiltern, um genau "
         "die gesuchten Notizen einzugrenzen — eine Publikation, ein Schlagwort, ein Thema."),
        ("Kopiere oder exportiere als Markdown/Text",
         "Nimm die Notizen als Markdown oder reinen Text heraus und füge sie überall ein. Die "
         "Formatierung (fett, kursiv, Listen) bleibt erhalten, strukturierte Notizen bleiben "
         "also strukturiert."),
        ("Oder zieh sie in eine neue Sicherung",
         "Lieber eine Datei? Exportiere eine Auswahl oder einen Zeitraum in eine neue "
         ".jwlibrary-Sicherung — praktisch, um ein Projekt zu archivieren oder einen "
         "bestimmten Satz Notizen an ein anderes Gerät zu geben."),
    ],
    "sections": [
        ("Warum überhaupt exportieren",
         "Notizen sind nützlicher, wenn sie reisen können: in ein Dokument für einen Programm­"
         "punkt, in ein persönliches Wiki, in einen Ausdruck für jemanden ohne die App. "
         "Markdown erhält die Struktur und bleibt dabei überall als reiner Text lesbar."),
        ("Ein Format wählen",
         "Reiner Text ist am portabelsten und lässt sich sauber in jedes Dokument oder jede E-Mail einfügen. Formatierte Ausgabe bewahrt die Struktur langer Notizen und eignet sich zum Drucken oder Teilen. Willst du die Notizen später wieder in JW Library haben — auf einem anderen Gerät oder in der Bibliothek einer anderen Person —, behalte die .jwlibrary-Datei selbst statt eines Textexports, denn nur sie bewahrt die Verknüpfungen zwischen Notizen, Markierungen, Schlagwörtern und der genauen Stelle in der Publikation, an der sie hängen."),
        ("Nur einen Teil der Bibliothek exportieren",
         "Ein vollständiger Export aus Jahren des Studiums ist selten das, was man will. Vorher einzugrenzen — auf ein Schlagwort, eine Publikation, eine Markierungsfarbe oder einen Zeitraum — ergibt etwas Brauchbares, etwa alle für einen Vortrag markierten Notizen oder alles, was während eines Kongresses entstand. Dieselben Filter, die die Ansicht eingrenzen, grenzen den Export ein: Was du siehst, bekommst du."),
        ("Was mit dem Text mitgeht und was nicht",
         "Ein Export nimmt deine Worte mit. Er nimmt nicht die Anker mit, die eine Notiz an einen bestimmten Absatz einer bestimmten Publikation binden, denn diese Verweise bedeuten nur innerhalb von JW Library etwas. Das ist der praktische Grund, auch Sicherungen zu behalten: Ein Export dient dem Lesen, Drucken und Teilen außerhalb der App, während eine .jwlibrary-Datei die Notizen mit unversehrtem Zusammenhang in eine Bibliothek zurückbringt."),
        ("Alles für einen Vortrag oder eine Aufgabe zusammentragen",
         "Das ist der häufigste Grund zu exportieren. Filtere auf das Schlagwort, die Publikation oder den Zeitraum, unter dem das Material liegt, prüfe das Ergebnis und exportiere nur das. Heraus kommt ein einzelnes Dokument mit den einschlägigen Notizen und den markierten Passagen in der Reihenfolge ihres Auftretens statt einer unhandlichen Ausgabe deiner gesamten Bibliothek."),
        ("Notizen mit jemandem teilen",
         "Hinter Teilen stecken zwei verschiedene Dinge. Will die andere Person deine Notizen lesen, ist ein Textexport das Richtige: Er öffnet sich überall und braucht keine besondere Software. Will sie die Notizen in ihrer eigenen JW Library haben, an denselben Absätzen verankert und mit ihren Schlagwörtern und Farben, dann brauchst du eine .jwlibrary-Datei, denn ein Textexport kann nichts in die App zurückbringen."),
        ("Ein Archiv behalten, das du auch später noch lesen kannst",
         "Exporte lohnen sich auch um ihrer selbst willen. Eine Kopie deiner Studiennotizen in reinem Text wird sich in dreißig Jahren noch mit Software öffnen lassen, die niemand geschrieben hat, und das kann kein app-eigenes Format versprechen. Beides zu behalten — die .jwlibrary zum Wiederherstellen und einen Textexport zum Lesen — kostet fast nichts und deckt beide Zukünfte ab."),
        ("Export oder Sicherung — was du brauchst",
         "Beide beantworten verschiedene Fragen. Ein Export dient dazu, deine Notizen außerhalb von JW Library zu nutzen: lesen, drucken, zitieren, jemandem schicken. Eine .jwlibrary-Sicherung dient dazu, sie nach JW Library zurückzubringen, auf dieses Gerät oder ein anderes, mit jedem Anker, Schlagwort und jeder Farbe. Keines ersetzt das andere, und es spricht nichts dagegen, beides zu haben."),
    ],
    "faq": [
        ("Verändert der Export meine JW-Library-Notizen?",
         "Nein. Der Export liest eine Kopie deiner Sicherung im Browser; deine Originaldatei "
         "und deine App bleiben unangetastet."),
        ("Kann ich alles auf einmal exportieren?",
         "Ja — setz die Filter zurück, um die ganze Bibliothek auszuwählen, oder grenze erst "
         "ein, um nur einen Teil zu exportieren."),
        ("Bekomme ich meine Notizen in Word oder Google Docs?",
         "Ja — als Text exportieren und einfügen. Der Text kommt mit unversehrter Struktur an und lässt sich von dort formatieren."),
        ("Werden Markierungen ebenso exportiert wie Notizen?",
         "Ja, samt der markierten Passage und ihrer Farbe, sodass ein Ausdruck sowohl zeigt, was du markiert, als auch, was du geschrieben hast."),
        ("Kann ich alles auf einmal exportieren?",
         "Ja, auch wenn ein gefilterter Export meist nützlicher ist. Für eine vollständige Kopie lässt sich alles in einem Durchgang exportieren."),
        ("Kann ich die in Studienfragen getippten Antworten exportieren?",
         "Ja. Getippte Antworten gehören zu deinen persönlichen Studiendaten und lassen sich zusammen mit Notizen und Markierungen exportieren."),
        ("Steht im Export, zu welcher Publikation jede Notiz gehört?",
         "Ja, der Export weist aus, woher jede Notiz stammt, auch wenn der zugrunde liegende Anker nur in JW Library funktioniert."),
        ("Verändert ein Export etwas in meiner Bibliothek?",
         "Nein. Ein Export liest deine Daten und schreibt eine separate Datei; in JW Library wird nichts geändert, verschoben oder entfernt."),
        ("Kann ich aus einer Sicherung statt aus der App exportieren?",
         "Ja. Eine .jwlibrary-Datei lässt sich direkt öffnen und ihre Notizen exportieren — nützlich, wenn die gewünschten Notizen in einer alten Sicherung stehen und nicht auf deinem aktuellen Gerät."),
    ],
}

GUIDES_DE["organize-jw-library-tags"] = {
    "title": "JW-Library-Schlagwörter ordnen und aufräumen",
    "h1": "Schlagwörter ordnen: umbenennen, zusammenlegen und in Mengen aufräumen",
    "description": "Schlagwörter vermehren sich über Jahre des Studiums. Benenne ein Schlagwort "
                   "über alle Notizen um, lege Duplikate zusammen und entferne, was du nicht "
                   "mehr nutzt — in Mengen, im Browser, mit vollständigem Rückgängig.",
    "intro": [
        "Über Schlagwörter findest du Notizen später wieder — aber nach ein paar Jahren "
        "wuchern sie. Man endet mit „Dienst“, „dienst“ und „Predigtdienst“ für dieselbe Sache, "
        "mit Schlagwörtern, die einmal entstanden und nie wieder benutzt wurden, und mit "
        "uneinheitlicher Benennung, die das Filtern unzuverlässig macht. JW Library bietet "
        "keine Möglichkeit, das im großen Stil zu beheben. Der Studien-Explorer schon.",
    ],
    "steps": [
        ("Lade deine Sicherung in den Studien-Explorer",
         "Lade auf jwsync.org deine .jwlibrary-Datei. Filtere nach Schlagwort, um jedes "
         "Schlagwort und die Zahl der Notizen dazu zu sehen."),
        ("Benenne ein Schlagwort über alle Notizen um",
         "Verschlagworte in Mengen neu: Benenne ein Schlagwort einmal um, und jede Notiz, die "
         "es verwendet, wird aktualisiert — kein Notiz-für-Notiz-Bearbeiten mehr, nur um einen "
         "Tippfehler zu beheben."),
        ("Lege Duplikate zusammen",
         "Verschlagworte die Notizen eines doppelten Schlagworts auf das maßgebliche um und "
         "lösch dann das leer gewordene Duplikat. Aus „Dienst“ und „dienst“ wird ein sauberes "
         "Schlagwort."),
        ("Entferne, was du nicht mehr nutzt",
         "Wähle veraltete Schlagwörter aus und lösche sie in Mengen. Alles ist umkehrbar, ein "
         "übereifriges Aufräumen ist also nie endgültig."),
        ("Exportiere die aufgeräumte Bibliothek",
         "Lade die bearbeitete .jwlibrary herunter und stelle sie in JW Library wieder her. "
         "Deine Schlagwörter sind überall einheitlich."),
    ],
    "sections": [
        ("Ein Schlagwortsystem, das wirklich hilft",
         "Sind die Schlagwörter erst einheitlich, wird das Filtern verlässlich — ein Tippen "
         "zeigt jede Notiz zu einem Thema, über alle Publikationen hinweg. Das ist der "
         "Unterschied zwischen Schlagwörtern als Krempel und Schlagwörtern als echtem Index "
         "deines Studiums."),
        ("Einheitliche Schlagwörter machen das Teilen zur Zwei-Klick-Sache",
         "Die Notizauswahl auf der Teilen-Seite hat einen eigenen Schlagwortfilter, ein "
         "sauberes Schlagwort ist also auch der schnellste Weg, jemandem einen Satz Notizen zu "
         "schicken: Schlagwort wählen, Alle auswählen, Datei erstellen. Schlampige "
         "Schlagwörter kosten dich doppelt — beim Suchen und beim Teilen."),
    ],
    "faq": [
        ("Berührt das Neuverschlagworten den Notiztext?",
         "Nein — es ändert nur, welche Schlagwörter angehängt sind. Titel und Inhalt deiner "
         "Notizen bleiben genau so, wie du sie geschrieben hast."),
        ("Gibt es ein Rückgängig, wenn ich etwas falsch mache?",
         "Ja. Der Studien-Explorer hat vollständiges Rückgängig und Wiederholen, und deine "
         "Originalsicherung wird nie verändert — die Änderungen landen in einer exportierten "
         "Kopie."),
    ],
}

GUIDES_DE["manage-jw-library-highlights"] = {
    "title": "JW-Library-Markierungen verwalten und umfärben",
    "h1": "Deine JW-Library-Markierungen verwalten: umfärben und in Mengen ordnen",
    "description": "Bring Ordnung in Jahre von JW-Library-Markierungen: ändere Farben in "
                   "Mengen, gib deinem Farbcode eine einheitliche Bedeutung und durchstöbere "
                   "alle Markierungen an einem Ort. Im Browser.",
    "intro": [
        "Markierungsfarben helfen nur, wenn sie etwas Einheitliches bedeuten. Mit der Zeit "
        "driften die Markierungen der meisten ab — Gelb bedeutete 2019 etwas anderes als "
        "heute, und in JW Library gibt es keine Möglichkeit, sie alle zusammen zu sehen oder "
        "im großen Stil zu korrigieren. Der Studien-Explorer sammelt jede Markierung in einer "
        "Ansicht und lässt dich in Mengen umfärben.",
    ],
    "steps": [
        ("Lade deine Sicherung",
         "Öffne auf jwsync.org deine .jwlibrary-Datei im Studien-Explorer und wechsle zum "
         "Reiter Markierungen."),
        ("Durchstöbere und filtere deine Markierungen",
         "Sieh jede Markierung in einer Liste, filtere nach Farbe oder Publikation und "
         "durchsuche den markierten Text sowie verknüpfte Notizen."),
        ("Färbe in Mengen um",
         "Wähle viele Markierungen aus und ändere ihre Farbe gemeinsam — vereinheitliche zum "
         "Beispiel alles, was du als „Schlüsseltext“ gemeint hast, in deiner ganzen Bibliothek "
         "auf eine Farbe."),
        ("Bearbeite auch verknüpfte Notizen",
         "Wo an einer Markierung eine Notiz hängt, bearbeite Titel und Inhalt dieser Notiz "
         "gleich hier mit."),
        ("Exportieren und wiederherstellen",
         "Lade die bearbeitete .jwlibrary herunter und stelle sie in JW Library wieder her, "
         "damit dein einheitlicher Farbcode auf jedem Gerät ist."),
    ],
    "sections": [
        ("Entscheide, was deine Farben bedeuten",
         "Ein einfaches Schema — eine Farbe für Hauptgedanken, eine für Texte zum Auswendig­"
         "lernen, eine für Fragen zum Nachforschen — macht aus Markierungen ein "
         "Studienwerkzeug statt Dekoration. Umfärben in Mengen lässt dich dieses Schema "
         "rückwirkend auf Jahre des Lesens anwenden."),
    ],
    "faq": [
        ("Kann ich Markierungen ohne angehängte Notiz sehen?",
         "Ja — der Reiter Markierungen zeigt sie alle, mit und ohne verknüpfte Notiz."),
        ("Wirkt sich das Umfärben auf den Text darunter aus?",
         "Nein, es ändert nur die Markierungsfarbe; der Publikationstext und deine Notizen "
         "bleiben unangetastet."),
    ],
}

GUIDES_DE["jw-library-study-answers"] = {
    "title": "Deine JW-Library-Studienantworten ansehen und bearbeiten",
    "h1": "Deine JW-Library-Studienantworten an einem Ort finden",
    "description": "Deine getippten Antworten zu Fragen aus Studienartikeln und Arbeitsheften "
                   "stecken versteckt in deiner Sicherung. Der Reiter Studienantworten im "
                   "Studien-Explorer lässt dich alle auf einmal lesen, durchsuchen und "
                   "bearbeiten.",
    "intro": [
        "Beim Studieren tippst du Antworten in die Felder von Studienartikeln, dem Wachtturm "
        "und den Arbeitsheften für die Zusammenkünfte. Sie werden in deiner Sicherung "
        "gespeichert — aber JW Library zeigt jede einzelne nur vergraben in ihrer Publikation. "
        "Es gibt keinen einzigen Ort, an dem du alles Geschriebene durchsehen kannst. Der "
        "Reiter Studienantworten im Studien-Explorer ist dieser Ort.",
    ],
    "steps": [
        ("Lade deine Sicherung in den Studien-Explorer",
         "Lade auf jwsync.org deine .jwlibrary-Datei und öffne den Reiter Studienantworten."),
        ("Lies alle deine Antworten zusammen",
         "Jede getippte Antwort erscheint in einer durchsuchbaren Liste, sodass du deine "
         "Gedanken zu einem ganzen Studienartikel auf einen Blick durchgehen kannst."),
        ("Suchen und bearbeiten",
         "Finde eine Antwort über ihren Text, dann bearbeite und feile sie gleich hier — "
         "hilfreich beim Durchsehen vor einer Zusammenkunft oder beim Glätten hastig "
         "formulierter Sätze."),
        ("Exportieren oder wiederherstellen",
         "Stelle die bearbeitete Datei wieder her, um deine Änderungen zurück in JW Library zu "
         "bringen, oder kopiere Antworten als Text für einen Vortrag oder deine Unterlagen."),
    ],
    "sections": [
        ("Warum das vor Zusammenkünften nützlich ist",
         "Deine vorbereiteten Antworten in einer durchgehenden Liste durchzugehen — statt in "
         "der App jeden Absatz zu scrollen — ist ein schnellerer Weg, dir in Erinnerung zu "
         "rufen, was du sagen wolltest, und zu sehen, welche Antworten leer geblieben sind."),
    ],
    "faq": [
        ("Sind das dieselben wie meine persönlichen Notizen?",
         "Nein — Studienantworten sind das, was du in die Antwortfelder einer Publikation "
         "getippt hast. Der Studien-Explorer zeigt sie in einem eigenen Reiter, getrennt von "
         "freien Notizen."),
        ("Wird etwas hochgeladen, um meine Antworten zu lesen?",
         "Nein. Wie alles in JW Sync wird deine Sicherung lokal im Browser gelesen und nie "
         "irgendwohin geschickt."),
    ],
}

GUIDES_DE["extract-jw-library-notes-by-date"] = {
    "title": "JW-Library-Notizen eines Zeitraums in eine neue Sicherung herausziehen",
    "h1": "Einen Zeitraum an JW-Library-Notizen in eine neue Sicherung herausziehen",
    "description": "Zieh nur die Notizen eines bestimmten Zeitraums heraus — ein Dienstjahr, "
                   "ein Kongress, ein Studienprojekt — in eine eigene, saubere "
                   ".jwlibrary-Sicherung. Vollständig in deinem Browser.",
    "intro": [
        "Manchmal willst du einen Ausschnitt deiner Bibliothek, nicht das Ganze: die Notizen "
        "dieses Jahres für eine Rückschau, alles von einem Kongress, oder die Recherche eines "
        "einzelnen Projekts zum Weitergeben. Der Studien-Explorer kann Notizen eines Zeitraums "
        "in eine brandneue .jwlibrary-Sicherung herausziehen und lässt deine Hauptbibliothek "
        "dabei unangetastet.",
    ],
    "steps": [
        ("Lade deine Sicherung",
         "Öffne auf jwsync.org deine .jwlibrary-Datei im Studien-Explorer."),
        ("Lege den Zeitraum fest",
         "Wähle Start- und Enddatum der gewünschten Notizen — ein Dienstjahr, ein Monat, die "
         "Tage einer bestimmten Veranstaltung."),
        ("Zieh sie in eine neue Sicherung",
         "Exportiere die passenden Notizen in eine frische .jwlibrary-Datei. Sie enthält nur "
         "die Notizen und Markierungen dieses Zeitraums samt ihren Schlagwörtern."),
        ("Nutze die herausgezogene Datei",
         "Stelle sie für eine gezielte Rückschau in JW Library ein, archiviere sie, oder teile "
         "sie mit jemandem, der nur diesen Ausschnitt braucht."),
    ],
    "sections": [
        ("Gute Gründe, nach Datum herauszuziehen",
         "Ein Jahresarchiv deines Studiums; eine saubere Datei mit Kongressnotizen, separat "
         "aufbewahrt; einem Studienpartner nur die Notizen eines gemeinsam bearbeiteten "
         "Projekts geben; oder eine riesige Bibliothek in handliche, datierte Teile zerlegen — "
         "alles, ohne deine Hauptsicherung anzurühren."),
    ],
    "faq": [
        ("Entfernt das Herausziehen diese Notizen aus meiner Bibliothek?",
         "Nein. Es kopiert die passenden Notizen in eine neue Datei; deine Originalsicherung "
         "behält alles."),
        ("Welches Datum wird verwendet — Erstellung oder letzte Bearbeitung?",
         "Es nutzt die in der Notiz selbst gespeicherten Zeitstempel, der Zeitraum spiegelt "
         "also wider, wann die Notizen erstellt oder geändert wurden."),
    ],
}

GUIDES_DE["connect-jw-library-notes-study-map"] = {
    "title": "Sieh, wie deine JW-Library-Notizen zusammenhängen — die Studienkarte",
    "h1": "Studienkarte: ein privater Wissensgraph deiner JW-Library-Notizen",
    "description": "Die Studienkarte macht aus deinen JW-Library-Notizen ein interaktives Netz "
                   "und verbindet sie über gemeinsame Bibeltexte, gemeinsame Schlagwörter und "
                   "ähnliche Formulierungen — damit du die Themen siehst, die dein Studium "
                   "durchziehen.",
    "intro": [
        "In Jahren an Notizen stecken Verbindungen, die du nie gesehen hast: derselbe "
        "Bibeltext, in einem Dutzend Einträgen zitiert, ein Thema, zu dem du immer "
        "zurückkehrst, Gedanken, die sich in verschiedenen Publikationen spiegeln. Die "
        "Studienkarte zeichnet diese Verbindungen als interaktiven Graphen — so wird die Form "
        "deines eigenen Studiums sichtbar.",
    ],
    "steps": [
        ("Öffne die Seite Studienstatistik und lade eine Sicherung",
         "Geh auf jwsync.org/highlights.html und lade deine .jwlibrary-Datei. Die Studienkarte "
         "liest sie in deinem Browser."),
        ("Öffne die Studienkarte",
         "Starte die Karte, um deine Notizen als verbundene Punkte zu sehen, verknüpft über "
         "gemeinsame Bibeltexte, gemeinsame Schlagwörter und ähnliche Formulierungen."),
        ("Erkunde die Verbindungen",
         "Wechsle zwischen den Ansichten Themen und Notizen, fahr über eine Notiz, um ihre "
         "Verbindungen hervorzuheben, zieh Elemente umher und nutze den Stärkeregler, um nur "
         "die engsten Verbindungen zu zeigen. Der Vollbildmodus gibt dir Platz."),
        ("Baue und speichere Studienketten",
         "Zeichne eigene „Studienketten“ von Hand zwischen verwandten Notizen, um einen "
         "Gedankengang festzuhalten, und exportiere die Karte als PNG zum Aufbewahren oder "
         "Teilen."),
    ],
    "sections": [
        ("Was die Karte zeigt",
         "Ballungen zeigen die Themen, die du am meisten studierst; ein Bibeltext mit vielen "
         "Verbindungen zeigt einen Vers, zu dem du immer wieder zurückkommst; eine einzeln "
         "stehende Notiz ist vielleicht ein Faden, den du weiterspinnen solltest. Es ist eine "
         "Art, dein Studium zu studieren — und Vorträge vorzubereiten, indem du den "
         "Verbindungen folgst, die du längst geknüpft hast."),
    ],
    "faq": [
        ("Brauche ich viele Notizen, damit die Karte nützlich ist?",
         "Schon eine bescheidene Bibliothek zeigt Verbindungen; je reicher deine Notizen, "
         "desto mehr zeigt die Karte. Sehr kleine Bibliotheken bekommen einen Hinweis, erst "
         "mehr Notizen zu sammeln."),
        ("Ist die Karte privat?",
         "Vollständig. Sie wird in deinem Browser aus deiner Sicherung gebaut und nie "
         "hochgeladen; auch der PNG-Export entsteht auf deinem Gerät."),
    ],
}

GUIDES_DE["review-old-jw-library-notes"] = {
    "title": "Alte JW-Library-Notizen durchsehen (damit sie hängen bleiben)",
    "h1": "Alte Notizen mit der Wiedervorlage durchsehen — ein wenig, aber oft",
    "description": "Notizen, die du nie wieder ansiehst, sind Notizen, die du vergisst. Die "
                   "Wiedervorlage zeigt, was du an diesem Tag in früheren Jahren geschrieben "
                   "hast, und baut eine sanfte verteilte Wiederholung — damit vergangenes "
                   "Studium weiter für dich arbeitet.",
    "intro": [
        "Die meisten Studiennotizen werden einmal geschrieben und nie wieder gesehen. Das ist "
        "eine stille Verschwendung — der Gedanke war es wert, festgehalten zu werden, und dann "
        "sank er auf den Grund der Bibliothek. Die Wiedervorlage holt deine eigenen alten "
        "Notizen wieder an die Oberfläche, ein paar auf einmal, sodass das Wiederlesen zur "
        "kleinen täglichen Gewohnheit wird statt zum Projekt für irgendwann.",
    ],
    "steps": [
        ("Öffne die Seite Studienstatistik und lade eine Sicherung",
         "Geh auf jwsync.org/highlights.html und lade deine .jwlibrary-Datei. Die "
         "Wiedervorlage liest deine Notizen lokal."),
        ("Sieh dir „An diesem Tag“ an",
         "Die Wiedervorlage bringt Notizen hoch, die du an diesem Datum in früheren Jahren "
         "geschrieben hast — „vor zwei Jahren heute geschrieben“ — und verbindet dich mit "
         "vergangenem Studium genau dann, wenn es am meisten bedeutet."),
        ("Mach eine kurze tägliche Durchsicht",
         "Sie legt dir eine Handvoll Notizen zum Wiederlesen vor, die du als durchgesehen "
         "markierst. Ein wenig, aber oft, so bleibt Studiertes hängen — und eine Serie wächst, "
         "solange du die Gewohnheit hältst."),
        ("Komm morgen wieder",
         "Die verteilte Wiederholung plant Notizen so ein, dass sie über die Zeit wieder "
         "auftauchen: Was es wert ist, behalten zu werden, kommt zurück, bis es wirklich dir "
         "gehört."),
    ],
    "sections": [
        ("Warum verteilte Wiederholung funktioniert",
         "Etwas genau dann zu wiederholen, wenn du es fast vergessen hättest, ist weit "
         "wirksamer als Pauken. Indem sie ein paar Notizen über viele Tage verteilt, macht die "
         "Wiedervorlage aus deiner bestehenden Bibliothek eine laufende, mühelose Durchsicht, "
         "die stetig vertieft, was du studiert hast."),
    ],
    "faq": [
        ("Wo wird mein Durchsicht-Fortschritt gespeichert?",
         "In deinem Browser auf deinem Gerät — es gibt kein Konto und nichts wird hochgeladen. "
         "Serie und Zeitplan gehören allein dir."),
        ("Brauche ich dafür neue Notizen?",
         "Nein — die Wiedervorlage arbeitet mit den Notizen, die du schon geschrieben hast. Je "
         "älter deine Bibliothek, desto schöner die „An diesem Tag“-Momente."),
    ],
}

GUIDES_DE["jw-library-achievements-streaks"] = {
    "title": "JW-Library-Studienserien, Stufen und Erfolge",
    "h1": "Mach aus deinem JW-Library-Studium Serien, Stufen und Auszeichnungen",
    "description": "Sieh deine Studienserien, steig auf deiner Studienreise über 60 Stufen in "
                   "12 Rängen und schalte rund 200 Erfolge frei — alles privat aus deiner "
                   "eigenen JW-Library-Sicherung gelesen.",
    "intro": [
        "Beständigkeit ist der schwierige Teil des persönlichen Studiums, und Fortschritt, den "
        "man nicht sieht, lässt man leicht schleifen. Die Seite Studienstatistik macht aus der "
        "Geschichte in deiner Sicherung etwas, dem du beim Wachsen zusehen kannst: Serien, "
        "Stufen und Auszeichnungen, die das Studium widerspiegeln, das du wirklich getan "
        "hast — keine vorgegebenen Ziele, nur dein eigener Verlauf, sichtbar gemacht.",
    ],
    "steps": [
        ("Öffne die Seite Studienstatistik",
         "Geh auf jwsync.org/highlights.html und lade deine .jwlibrary-Sicherung. Alles wird "
         "in deinem Browser berechnet."),
        ("Sieh dir deine Serien an",
         "Deine längste und deine aktuelle Studienserie, dein Wochenrhythmus und deine "
         "geschäftigsten Stunden und Monate — der Puls deiner Studiengewohnheit."),
        ("Steig auf deiner Studienreise",
         "Arbeite dich durch 60 Stufen in 12 benannten Rängen (von Samen bis Immergrün), mit "
         "einer farbwechselnden Kugel und Aufstiegs-Feiern, basierend auf deinem gesamten "
         "Studium."),
        ("Sammle Erfolge",
         "Schalte rund 200 Auszeichnungen frei, von Gewöhnlich bis Legendär, darunter "
         "inhaltsbezogene, thematische Medaillen; öffne eine Medaille, um deinen Fortschritt "
         "zur nächsten zu sehen."),
    ],
    "sections": [
        ("Motivation ohne Druck",
         "Das sind keine Ziele, die jemand anders gesetzt hat — es ist ein Spiegel dessen, was "
         "du bereits getan hast. Eine Serie zu sehen, die du nicht brechen willst, oder eine "
         "fast erreichte Stufe, ist ein sanfter Anstoß, die gute Gewohnheit zu halten. Und "
         "eine teilbare Karte fasst dein Jahr zusammen, ohne eine einzige private Notiz "
         "preiszugeben."),
    ],
    "faq": [
        ("Aktualisieren sich Serien und Auszeichnungen von selbst?",
         "Sie spiegeln die Sicherung wider, die du lädst — erstelle eine frische Sicherung, um "
         "deinen neuesten Fortschritt zu sehen. Nichts läuft im Hintergrund."),
        ("Wird davon etwas geteilt oder hochgeladen?",
         "Nein. Alles wird lokal aus deiner Sicherung berechnet; nur die Zusammenfassungskarte "
         "kannst du bewusst teilen, und sie enthält keinen Notiztext."),
    ],
}

GUIDES_DE["share-convention-assembly-notes"] = {
    "title": "Kongressnotizen aus JW Library teilen",
    "h1": "Deine Kongress- und Zusammenkunftsnotizen teilen",
    "description": "Gib deine Kongress- oder Zusammenkunftsnotizen als kleine Datei an Familie "
                   "und Freunde weiter — ohne deine ganze Bibliothek herauszugeben oder ihre "
                   "zu überschreiben. Eine praktische Anwendung des Notizenteilens.",
    "intro": [
        "Du hast auf einem Kongress sorgfältig mitgeschrieben; ein Freund, der eine Sitzung "
        "verpasst hat, hätte die Notizen gern; Familienmitglieder wollen die Punkte für ihre "
        "eigene Nacharbeit. Die ganze Sicherung zu schicken ist übertrieben und würde beim "
        "Wiederherstellen die Notizen des Empfängers löschen. Das Notizenteilen lässt dich "
        "genau die Notizen weitergeben, die du willst — und lässt den Empfänger alles "
        "behalten, was er schon hat.",
    ],
    "steps": [
        ("Lade deine Sicherung auf der Teilen-Seite",
         "Geh auf jwsync.org/share.html und lade deine .jwlibrary-Datei."),
        ("Wähle nur die Kongressnotizen aus",
         "Nimm das Schlagwort der Veranstaltung aus dem Schlagwortfilter der Notizauswahl und "
         "tippe auf Alle auswählen — die Liste sind bereits genau die Notizen, die du "
         "verschlagwortet hast. Markierungen an diesen Notizen kommen mit."),
        ("Schick die kleine Teilen-Datei",
         "JW Sync erzeugt eine kleine Datei mit nur diesen Notizen. Schick sie, wie du "
         "magst — Messenger, E-Mail, AirDrop. Kein Server, kein Konto."),
        ("Familie und Freunde fügen sie ein",
         "Jeder öffnet dieselbe Seite, lädt deine Datei mit der eigenen Sicherung und erhält "
         "eine neue Sicherung mit deinen Notizen darin. Ihre eigenen Notizen werden nie "
         "überschrieben, und deine importierten Notizen kommen verschlagwortet an, sind also "
         "leicht zu finden."),
    ],
    "sections": [
        ("Ein Schlagwort macht das mühelos",
         "Wenn du deine Notizen während der Veranstaltung verschlagwortest (etwa „Kongress "
         "2026“), ist ihre spätere Auswahl ein Filterklick und ein Alle auswählen. Genau "
         "deshalb lohnt es sich, zu Beginn jedes Kongresses oder jeder besonderen "
         "Zusammenkunft ein frisches Schlagwort anzulegen."),
    ],
    "faq": [
        ("Kann ich mit mehreren Personen gleichzeitig teilen?",
         "Ja — die Teilen-Datei ist einfach eine Datei. Schick sie an so viele Leute, wie du "
         "willst; jeder fügt sie unabhängig in seine eigene Bibliothek ein."),
        ("Wird meine ganze Bibliothek preisgegeben?",
         "Nein. Nur die Notizen, die du auswählst, sind in der Datei; der Rest deiner "
         "Bibliothek bleibt privat."),
    ],
}

GUIDES_DE["share-jw-library-notes-by-tag"] = {
    "title": "Nur die JW-Library-Notizen unter einem Schlagwort teilen",
    "h1": "Nur die Notizen mit einem bestimmten Schlagwort teilen",
    "description": "Schick ein Thema, ein Projekt oder das Material für einen Studierenden "
                   "statt deiner ganzen Bibliothek — und deine Schlagwörter reisen mit, sodass "
                   "die Notizen auf der anderen Seite geordnet ankommen.",
    "intro": [
        "Ein Schlagwort ist meist die natürliche Einheit des Teilens. Du hast alles zu einem "
        "Thema verschlagwortet, alles von einer Veranstaltung, oder alles, was du mit einer "
        "Person durchgehst — und genau dieser Satz, nicht deine ganze Bibliothek, ist das, was "
        "die andere Person wirklich will.",
        "Das Notizenteilen von JW Sync arbeitet Notiz für Notiz, ein Schlagwort ist also "
        "einfach die Liste, die du abhakst. Die Notizen behalten beim Hinausgehen ihre "
        "Schlagwörter, was heißt: Wer sie bekommt, kann danach in der eigenen Bibliothek genau "
        "denselben Satz herausfiltern.",
    ],
    "steps": [
        ("Stell sicher, dass die Notizen das Schlagwort tragen",
         "Verschlagworte sie in JW Library gleich beim Schreiben, oder öffne deine Sicherung "
         "im Studien-Explorer auf jwsync.org und füge mit dem Schlagwort-Editor mehreren "
         "Notizen auf einmal eines hinzu. Jetzt einheitlich zu verschlagworten ist das, was "
         "das Teilen später zur Ein-Minuten-Sache macht."),
        ("Öffne die Teilen-Seite und lade deine Sicherung",
         "Geh auf jwsync.org/share.html, wähle Notizen senden und lade deine "
         ".jwlibrary-Datei. Sie wird in deinem Browser gelesen und verlässt nie dein Gerät."),
        ("Wähle das Schlagwort im Filter, dann Alle auswählen",
         "Die Notizauswahl hat einen Schlagwortfilter, der jedes Schlagwort deiner Sicherung "
         "mit der Anzahl der Notizen darunter auflistet. Wähl deines, und die Liste "
         "beschränkt sich auf genau diese Notizen; Alle auswählen hakt sie alle ab. Das ist "
         "die ganze Auswahl — zwei Klicks."),
        ("Erstelle die Datei und schick sie",
         "JW Sync baut eine kleine Teilen-Datei mit nur den abgehakten Notizen. Schick sie per "
         "Chat, E-Mail oder AirDrop — kein Server ist beteiligt und auf keiner Seite ein "
         "Konto nötig."),
        ("Die andere Person fügt sie ihrer Sicherung hinzu",
         "Sie öffnet dieselbe Seite, wählt Empfangen, sieht sich die Notizen an und fügt sie "
         "ihrer Sicherung hinzu. Deine Schlagwörter kommen mit den Notizen an, dazu ein "
         "Schlagwort für den Import — der ganze Satz ist also auch für sie einen Filter "
         "entfernt."),
    ],
    "sections": [
        ("Warum ein Schlagwort statt einer Sicherung teilen",
         "Eine vollständige .jwlibrary-Sicherung herauszugeben verrät alles, was du je "
         "geschrieben hast, und ihr Wiederherstellen würde die Notizen der anderen Person "
         "löschen. Eine verschlagwortete Auswahl zu teilen ist in beidem das Gegenteil: Sie "
         "sieht nur, was du gewählt hast, und verliert nichts Eigenes."),
        ("Weiter eingrenzen oder über Schlagwörter hinweg teilen",
         "Schlagwortfilter und Suchfeld arbeiten zusammen: Wähl ein Schlagwort, tipp dann ein "
         "Wort, um weiter einzugrenzen — Alle auswählen hakt weiterhin nur ab, was vor dir "
         "liegt. Die Suche findet auch Schlagwortnamen, ein Stichwort in mehreren "
         "Schlagwörtern sammelt sie also in einem Durchgang. Jede Notiz in der Liste zeigt "
         "ihre Schlagwörter, du siehst also vor dem Senden, was du sendest."),
        ("Schlagwörter, die es fürs Teilen zu behalten lohnt",
         "Es lohnt sich, ein paar Schlagwörter zu führen, die es nur zum Teilen gibt — ein "
         "Veranstaltungsname, ein Thema, zu dem du für andere nachforschst, die Person, mit "
         "der du studierst. Kommt der Moment, etwas zu schicken, muss nichts gesucht werden: "
         "Der Satz steht schon."),
    ],
    "faq": [
        ("Gehen meine Schlagwörter mit zur anderen Person?",
         "Ja. Geteilte Notizen tragen ihre Schlagwörter, und der Import bekommt ein eigenes "
         "Schlagwort — der Empfänger kann den ganzen Stapel später finden, durchsehen oder "
         "entfernen."),
        ("Was, wenn eine Notiz mehrere Schlagwörter hat?",
         "Sie erscheint unter jedem davon im Filter, und alle ihre Schlagwörter reisen mit. "
         "Nach einem Schlagwort zu filtern entfernt die anderen nie."),
        ("Entfernt das Teilen die Notizen aus meiner Bibliothek?",
         "Nein. Teilen kopiert Notizen in eine kleine Datei; deine Sicherung und deine App "
         "bleiben unangetastet."),
        ("Kann ich dasselbe Schlagwort an mehrere Leute schicken?",
         "Ja — die Teilen-Datei ist eine ganz normale Datei. Schick sie an so viele Leute, wie "
         "du willst; jeder fügt sie unabhängig in die eigene Bibliothek ein."),
    ],
}

GUIDES_DE["share-notes-with-bible-student"] = {
    "title": "JW-Library-Notizen mit einem Bibelschüler teilen",
    "h1": "Studiennotizen mit jemandem teilen, mit dem du die Bibel studierst",
    "description": "Schick die Notizen zu einer Lektion — Bibeltexte, Veranschaulichungen, die "
                   "vorbereiteten Gedanken — direkt in das JW Library der anderen Person, ohne "
                   "irgendetwas anzurühren, was sie selbst geschrieben hat.",
    "intro": [
        "Wenn du ein Studium vorbereitest, landet die meiste Arbeit in deinen eigenen Notizen: "
        "die zusätzlichen Bibeltexte, die Veranschaulichung, die den Gedanken hat ankommen "
        "lassen, die Antwort auf die Frage von letzter Woche. Es vorzulesen ist eine Sache; "
        "der Person eine Kopie zu hinterlassen, die sie die ganze Woche nachlesen kann, eine "
        "andere.",
        "Das Notizenteilen legt deine vorbereiteten Notizen als echte JW-Library-Notizen in "
        "ihre Bibliothek, an denselben Absätzen und Versen — nicht als Screenshot oder "
        "Nachricht, an der sie vorbeiscrollt.",
    ],
    "steps": [
        ("Bereite die Notizen zur Lektion in JW Library vor",
         "Schreib die Notizen wie gewohnt, an den Absätzen und Bibeltexten, die die Lektion "
         "behandelt. Gib ihnen ein Schlagwort — den Namen der Person oder die Publikation — "
         "damit der Satz später leicht auszuwählen ist."),
        ("Öffne die Teilen-Seite und lade deine Sicherung",
         "Erstelle eine Sicherung (Persönliches Studium → Sicherung und Wiederherstellung → "
         "Sicherung erstellen), öffne dann jwsync.org/share.html, wähle Notizen senden und "
         "lade die Datei. Sie verlässt nie dein Gerät."),
        ("Hake die Notizen dieser Lektion ab",
         "Filtere die Auswahl nach dem verwendeten Schlagwort und tippe auf Alle auswählen, "
         "oder such und hak sie einzeln ab. Erstelle die Teilen-Datei — alles andere in deiner "
         "Bibliothek bleibt, wo es ist."),
        ("Schick sie und erklär das Empfangen",
         "Die Person braucht zuerst eine eigene Sicherung — Persönliches Studium → Sicherung "
         "und Wiederherstellung → Sicherung erstellen. Dann öffnet sie jwsync.org/share.html, "
         "wählt Empfangen, lädt deine Datei und ihre Sicherung und lädt die aktualisierte "
         "Sicherung herunter."),
        ("Sie stellt sie in JW Library wieder her",
         "Sicherung und Wiederherstellung → Wiederherstellen, sie wählt die aktualisierte "
         "Datei, und deine Notizen erscheinen in ihrer Bibliothek neben den eigenen — "
         "verschlagwortet, damit sie weiß, welche von dir stammen."),
    ],
    "sections": [
        ("Ihre Notizen werden nie überschrieben",
         "Das ist der wichtige Unterschied zum Verschicken einer Sicherung. Eine "
         "Wiederherstellung ersetzt die ganze Bibliothek eines Geräts; geteilte Notizen zu "
         "empfangen ergänzt sie. Alles, was die Person selbst geschrieben hat — auch zu genau "
         "denselben Absätzen — bleibt exakt so, wie es war."),
        ("Ein Wochenrhythmus, der zwei Minuten dauert",
         "Wenn ihr es beide einmal gemacht habt, ist die Routine kurz: vorbereiten, abhaken, "
         "senden, wiederherstellen. Viele finden es am einfachsten, die Notizen gleich nach "
         "der Vorbereitung zu schicken, damit der Schüler sie vor dem Studium hat und nicht "
         "danach."),
    ],
    "faq": [
        ("Braucht der Schüler ein Konto oder eine installierte App?",
         "Nirgends ein Konto, und nichts zu installieren außer JW Library selbst — die "
         "Teilen-Seite ist eine ganz normale Webseite."),
        ("Was, wenn der Schüler noch nie eine Sicherung gemacht hat?",
         "Dann macht er zuerst eine, in JW Library unter Persönliches Studium → Sicherung und "
         "Wiederherstellung. Auch eine scheinbar leere Bibliothek funktioniert; die Sicherung "
         "ist das, wozu die geteilten Notizen hinzukommen."),
        ("Kann ich die Notizen später zurückholen?",
         "Die Datei gehört dir, solange du sie nicht verschickst. Sobald jemand sie hat, "
         "gehört sie ihm, genau wie jede Nachricht — teile also nur, was du auch schriftlich "
         "teilen würdest."),
    ],
}

GUIDES_DE["share-meeting-notes-with-family"] = {
    "title": "Notizen der Zusammenkunft mit der Familie teilen",
    "h1": "Die Notizen dieser Woche mit der Familie teilen",
    "description": "Jemand war krank, bei der Arbeit oder verreist — schick ihm die Notizen der "
                   "Woche als kleine Datei, die er seinem eigenen JW Library hinzufügen kann, "
                   "ohne dass jemand etwas verliert.",
    "intro": [
        "In den meisten Haushalten macht jeder eigene Notizen auf dem eigenen Gerät, und immer "
        "verpasst jemand eine Zusammenkunft. Beim Abendessen vorzulesen funktioniert einmal; "
        "die Notizen in die Bibliothek der anderen Person zu legen ist das, was sie später "
        "nutzen lässt — an dem Ort, an dem sie wirklich nachschauen wird.",
        "Weil das Teilen Notiz für Notiz und nicht Sicherung für Sicherung läuft, können "
        "mehrere Leute frei Notizen tauschen, ohne dass jemandes Bibliothek überschrieben "
        "wird.",
    ],
    "steps": [
        ("Sichere das Gerät, auf dem du die Notizen gemacht hast",
         "JW Library → Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen."),
        ("Wähle die Notizen der Woche aus",
         "Wähle auf jwsync.org/share.html Notizen senden, lade deine Sicherung und hak die "
         "Notizen dieser Woche ab — die Suche nach der Publikation bringt sie schnell "
         "zusammen, und wenn du die Notizen der Woche verschlagwortest, sammelt der "
         "Schlagwortfilter sie mit einem Klick."),
        ("Schick sie in den Familienchat",
         "Erstelle die Teilen-Datei und schick sie über den Kanal, den der Haushalt ohnehin "
         "nutzt — Messenger, E-Mail, AirDrop. Es ist eine kleine Datei mit nur den abgehakten "
         "Notizen."),
        ("Jeder fügt sie der eigenen Sicherung hinzu",
         "Die Person öffnet dieselbe Seite, wählt Empfangen, lädt deine Datei mit einer "
         "eigenen Sicherung, lädt die aktualisierte Sicherung herunter und stellt sie in JW "
         "Library wieder her."),
    ],
    "sections": [
        ("Die Bibliothek jedes Einzelnen bleibt seine eigene",
         "Niemandes Notizen werden ersetzt, und niemand muss seine ganze Bibliothek "
         "herausgeben, um mitzumachen. Importierte Notizen kommen unter einem Schlagwort an, "
         "jeder sieht also auf einen Blick, welche Notizen von jemand anderem stammen, und "
         "kann den Stapel später löschen, wenn er ihn lieber nicht behalten möchte."),
        ("Familienstudium: sammeln statt zerstreuen",
         "Dasselbe Werkzeug funktioniert in die andere Richtung. Wenn alle beim Familienstudium "
         "mitschreiben, kann eine Person die Teilen-Dateien der anderen in eine einzige "
         "Sicherung sammeln und hat am Ende die gebündelten Notizen des Haushalts zum selben "
         "Stoff."),
    ],
    "faq": [
        ("Können die Geräte der Kinder mitmachen?",
         "Jedes Gerät, das JW Library ausführen und eine Webseite öffnen kann. Die Schritte "
         "sind auf Handy, Tablet und Computer identisch."),
        ("Müssen wir auf derselben Plattform sein?",
         "Nein. Android, iPhone, iPad und die Windows-App nutzen dasselbe Sicherungsformat, "
         "Notizen wechseln also ohne Umwandlung zwischen ihnen."),
    ],
}

GUIDES_DE["receive-shared-jw-library-notes"] = {
    "title": "Jemand hat mir JW-Library-Notizen geschickt — wie öffne ich sie?",
    "h1": "Geteilte Notizen in dein eigenes JW Library einfügen",
    "description": "Du hast eine Datei mit geteilten Notizen oder einen Textblock bekommen. So "
                   "siehst du sie dir an und fügst sie deiner eigenen JW-Library-Sicherung "
                   "hinzu, ohne eine einzige eigene Notiz zu verlieren.",
    "intro": [
        "Geteilte JW-Library-Notizen kommen als kleine Datei (Endung .jwshare.json) oder als "
        "Textblock in einer Nachricht an. JW Library selbst kann beides nicht öffnen — aber du "
        "brauchst es dafür auch nicht. Die Empfangsseite von JW Sync liest die geteilten "
        "Notizen, zeigt dir, was drin ist, und schreibt sie in eine Sicherung von dir.",
        "Der ganze Austausch findet auf deinem Gerät statt. Kein Konto, nichts wird "
        "hochgeladen, und zu deinen eigenen Notizen kommt etwas hinzu, sie werden nie ersetzt.",
    ],
    "steps": [
        ("Sichere zuerst deine eigene Bibliothek",
         "In JW Library: Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen. Das ist die Datei, zu der die geteilten Notizen hinzukommen, sie sollte "
         "also aktuell sein."),
        ("Öffne die Teilen-Seite und wähle Empfangen",
         "Geh auf jwsync.org/share.html und wähle Notizen empfangen."),
        ("Lade, was man dir geschickt hat",
         "Wähl die .jwshare.json-Datei, oder füg den geteilten Text direkt in das Feld ein, "
         "wenn er als Nachricht kam. So oder so bekommst du eine schreibgeschützte Vorschau "
         "jeder Notiz, bevor irgendetwas geschrieben wird."),
        ("Füg sie deiner Sicherung hinzu",
         "Lade deine eigene Sicherung, wähle das Schlagwort, das die importierten Notizen "
         "tragen sollen, und füg sie hinzu. JW Sync baut dir eine aktualisierte Sicherung zum "
         "Herunterladen."),
        ("Stelle die aktualisierte Sicherung in JW Library wieder her",
         "Persönliches Studium → Sicherung und Wiederherstellung → Wiederherstellen, wähle die "
         "aktualisierte Datei. Die geteilten Notizen sind jetzt in deiner Bibliothek, an den "
         "richtigen Absätzen und Versen."),
    ],
    "sections": [
        ("Nichts von dir wird ersetzt",
         "Geteilte Notizen kommen als neue Notizen hinzu. Selbst wenn eine geteilte Notiz auf "
         "einem Absatz landet, zu dem du schon geschrieben hast, überleben beide — deine "
         "unangetastet, ihre daneben. Zu beachten ist nur die übliche Regel des "
         "Wiederherstellens: Stelle die aktualisierte Sicherung wieder her, nicht eine ältere."),
        ("Später anders entschieden?",
         "Jede importierte Notiz trägt das Schlagwort, das du beim Hinzufügen gewählt hast. "
         "Öffne deine Sicherung im Studien-Explorer, filtere nach diesem Schlagwort, und du "
         "kannst den ganzen Stapel in einem Durchgang durchsehen oder löschen."),
    ],
    "faq": [
        ("Die Datei kam als .txt umbenannt an oder öffnet sich als Text — ist sie kaputt?",
         "Nein. Messenger machen das oft. Kopiere den Text und füg ihn in das Empfangen-Feld "
         "ein; es funktioniert genau gleich."),
        ("Brauche ich die ganze Sicherung des Absenders?",
         "Nein. Die Teilen-Datei enthält nur die Notizen, die er senden wollte — sonst nichts "
         "aus seiner Bibliothek."),
        ("Wird etwas hochgeladen, wenn ich die Notizen ansehe?",
         "Nein. Das Lesen der geteilten Datei, die Vorschau und das Schreiben der "
         "aktualisierten Sicherung passieren alle in deinem Browser, auf deinem Gerät."),
    ],
}

GUIDES_DE["share-notes-with-study-group"] = {
    "title": "Recherche-Notizen mit einer Studiengruppe teilen",
    "h1": "Recherche mit einer Gruppe teilen — und ihre wieder einsammeln",
    "description": "Eine Datei, viele Leute: Schick einen Satz Recherche-Notizen an alle, die "
                   "dasselbe Thema bearbeiten, und sammle das Zurückgeschickte zu einem "
                   "einzigen eigenen Satz.",
    "intro": [
        "Wenn mehrere Leute dasselbe Thema durcharbeiten, liegt die Recherche am Ende meist "
        "verstreut — einer hat die Querverweise gefunden, ein anderer den geschichtlichen "
        "Hintergrund, ein dritter die Veranschaulichungen. Sich gegenseitig Screenshots "
        "anzusehen ist etwas anderes, als den Stoff in der eigenen Bibliothek zu haben, an "
        "denselben Versen, nächstes Jahr durchsuchbar.",
        "Weil eine Teilen-Datei einfach eine Datei ist, bedient ein Export die ganze Gruppe, "
        "und derselbe Mechanismus bringt ihre Arbeit zu dir zurück.",
    ],
    "steps": [
        ("Verschlagworte deine Recherche beim Sammeln",
         "Gib dem Thema in JW Library ein Schlagwort, damit der Satz zusammenbleibt. Im "
         "Studien-Explorer kannst du mehreren Notizen nachträglich in einem Zug ein Schlagwort "
         "geben."),
        ("Erstelle eine Teilen-Datei für die Gruppe",
         "Wähle auf jwsync.org/share.html Notizen senden, lade deine Sicherung, nimm das "
         "Schlagwort des Themas aus dem Filter, tippe auf Alle auswählen und erstelle die "
         "Datei."),
        ("Poste sie einmal",
         "Schick dieselbe Datei an alle — Gruppenchat, E-Mail an mehrere Leute, was die Gruppe "
         "ohnehin nutzt. Keine Einrichtung pro Person und keine Serverkopie."),
        ("Bitte um ihre im Gegenzug",
         "Jeder kann von seiner Seite genau dasselbe tun. Füg jede empfangene Datei "
         "nacheinander deiner Sicherung hinzu und gib jedem Import ein eigenes Schlagwort — "
         "der Name des Absenders funktioniert gut — damit du immer weißt, wessen Recherche "
         "welche ist."),
    ],
    "sections": [
        ("Ein gebündelter Satz, trotzdem zuordenbar",
         "Nach ein paar Runden hast du die gesamte Recherche der Gruppe zum Thema in deiner "
         "eigenen Bibliothek, an den richtigen Absätzen und Versen, jeder Beitrag nach Quelle "
         "verschlagwortet. Die Suche findet alles auf einmal; die Schlagwörter lassen dich "
         "alles wieder trennen, wann immer du willst."),
        ("Niemand muss seine Bibliothek preisgeben",
         "Jeder teilt nur die Notizen, die er abhakt. Der Rest der Bibliothek jeder Person — "
         "persönliches Studium, private Erinnerungen, alles andere — kommt nie in die Datei."),
    ],
    "faq": [
        ("Gibt es eine Grenze, wie viele Notizen ich auf einmal teilen kann?",
         "Praktisch nicht. Notizen sind klein; auch ein großer Satz ergibt eine Datei, die du "
         "in einer Nachricht verschicken kannst."),
        ("Was, wenn zwei Leute mir dieselbe Notiz schicken?",
         "Du siehst sie zweimal, jeweils unter dem Schlagwort des Absenders. Die Suche im "
         "Studien-Explorer macht Fast-Duplikate leicht auffindbar und löschbar."),
        ("Kann jemand empfangen, ohne selbst etwas zu schicken?",
         "Ja. Empfangen und Senden sind unabhängig — niemand muss teilen, um das Erhaltene "
         "einfügen zu können."),
    ],
}

GUIDES_DE["share-talk-preparation-notes"] = {
    "title": "Die Recherche hinter einem Vortrag oder einer Aufgabe weitergeben",
    "h1": "Deine Vortrags- und Aufgabenrecherche weitergeben",
    "description": "Du hast für einen Vortrag, einen Programmpunkt oder eine Aufgabe recherchiert. "
                   "So gibst du die Recherche an den Nächsten weiter — als echte Notizen in "
                   "seiner Bibliothek oder als reinen Text für ein Dokument.",
    "intro": [
        "Vorbereitung wird selten nur einmal gebraucht. Die Bibeltexte, die du "
        "zusammengetragen hast, der Hintergrund, den du gelesen hast, die Art, wie du einen "
        "Gedanken schließlich formuliert hast — wer denselben Stoff später behandelt, würde "
        "lieber damit anfangen als mit einem leeren Blatt.",
        "JW Sync bietet dir zwei Wege, das weiterzugeben, und sie passen zu verschiedenen "
        "Leuten: als Notizen, die im JW Library der anderen Person landen, oder als reiner "
        "Text, den sie in ein Dokument einfügen kann.",
    ],
    "steps": [
        ("Fass die Recherche unter einem Schlagwort zusammen",
         "Verschlagworte die Notizen beim Vorbereiten mit dem Thema oder der Aufgabe. Sind sie "
         "schon geschrieben und ohne Schlagwort, öffne deine Sicherung im Studien-Explorer und "
         "verschlagworte sie in ein paar Minuten in einem Zug."),
        ("Entscheide, welche Form zur anderen Person passt",
         "Wer in JW Library studiert, will Notizen in seiner Bibliothek. Wer ein Dokument "
         "baut, will Text. Beides geht aus demselben Satz."),
        ("Notizen senden: über die Teilen-Seite",
         "Wähle auf jwsync.org/share.html Notizen senden, lade deine Sicherung, filtere nach "
         "dem verwendeten Schlagwort, tippe auf Alle auswählen und erstelle die Datei. Die "
         "andere Person fügt sie ihrer Sicherung hinzu und stellt sie wieder her — ihre "
         "eigenen Notizen bleiben unangetastet."),
        ("Text senden: Export aus dem Studien-Explorer",
         "Filtere auf denselben Satz und kopiere oder exportiere ihn als Markdown oder reinen "
         "Text. Die Formatierung bleibt erhalten, ein strukturiertes Gerüst bleibt also "
         "strukturiert, wenn es in ein Dokument eingefügt wird."),
    ],
    "sections": [
        ("Behalte eine Kopie für dich, in einer Form, die du wiederfindest",
         "Derselbe Export lohnt sich auch für dich selbst. Ein Schlagwort plus ein Zeitraum "
         "machen die ganze Vorbereitung Jahre später wieder auffindbar — genau dann, wenn du "
         "sie brauchst — und die Datumsextraktion des Studien-Explorers macht aus jedem "
         "Zeitfenster eine eigene Datei."),
    ],
    "faq": [
        ("Bleiben die Bibeltexte mit den richtigen Versen verknüpft?",
         "Ja — geteilte Notizen behalten den Absatz und Vers, an dem sie hingen, sie landen "
         "also an der richtigen Stelle in der Bibliothek der anderen Person."),
        ("Kann ich Notizen mit Markierungen teilen?",
         "Ja. Markierungen, die an den geteilten Notizen hängen, reisen mit."),
    ],
}

GUIDES_DE["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Die Zusammenkunft mit Notizen vorbereiten, die du schon geschrieben hast",
    "h1": "Wöchentliche Vorbereitung mit den Notizen, die du schon hast",
    "description": "Du hast diesen Stoff schon einmal studiert. Hier ist eine kurze "
                   "wöchentliche Routine, die deine alten Notizen, Markierungen und Antworten "
                   "zur selben Publikation hochholt, bevor du erneut vorbereitest.",
    "intro": [
        "Die meisten bereiten jede Woche mit einem leeren Blatt vor, obwohl sie über dasselbe "
        "Thema — manchmal denselben Bibeltext — schon mehrfach geschrieben haben. Diese "
        "früheren Gedanken liegen in deiner Bibliothek; das Problem ist nur, dass sie dir "
        "nichts im richtigen Moment zurückbringt.",
        "Eine Fünf-Minuten-Routine zu Beginn der Vorbereitung behebt das, und sie braucht "
        "nichts außer der Sicherung, die du ohnehin hast.",
    ],
    "steps": [
        ("Lade eine aktuelle Sicherung in den Studien-Explorer",
         "Erstelle in JW Library eine Sicherung und öffne sie dann auf jwsync.org. Alles wird "
         "in deinem Browser gelesen."),
        ("Such das Thema, bevor du anfängst",
         "Such nach dem Thementext, dem Thema oder der Publikation. Was du in früheren Jahren "
         "dazu geschrieben hast, kommt gebündelt hoch, über alle Publikationen hinweg, in "
         "denen es vorkommt."),
        ("Sieh dir deine Studienantworten an",
         "Die Ansicht Studienantworten sammelt die Antworten, die du in Studienfragen getippt "
         "hast, frühere Durchgänge durch denselben Stoff sind also da, um darauf aufzubauen, "
         "statt sie zu wiederholen."),
        ("Ergänze, was fehlt, und spiel es zurück",
         "Notizen lassen sich gleich dort bearbeiten oder neu anlegen — Titel, Text, "
         "Schlagwörter, Markierungsfarbe. Exportiere die bearbeitete Sicherung und stelle sie "
         "in JW Library wieder her, dann ist deine Vorbereitung für die Zusammenkunft in der "
         "App."),
    ],
    "sections": [
        ("Warum die alten Notizen zählen",
         "Durchzusehen, was du beim letzten Mal geschlossen hast, macht die Vorbereitung "
         "kumulativ. Du entdeckst nicht mehr dieselben Punkte neu, sondern baust darauf auf — "
         "und die Notizen dieser Woche werden zum Ausgangspunkt der nächsten Runde."),
        ("Die sanftere Variante: lass die Notizen zu dir kommen",
         "Fühlt sich eine wöchentliche Suche nach Arbeit an, holt die Wiedervorlage auf der "
         "Seite Studienstatistik von selbst täglich ein paar alte Notizen hoch, darunter die, "
         "die du an diesem Datum in früheren Jahren geschrieben hast. Derselbe Nutzen, keine "
         "Routine zu merken."),
    ],
    "faq": [
        ("Ändert das Bearbeiten im Browser direkt meine Bibliothek?",
         "Nein. Du exportierst eine aktualisierte Sicherung und stellst sie in JW Library "
         "wieder her — die App ändert sich nur durch eine Wiederherstellung, die du selbst "
         "ausführst."),
        ("Wird meine Sicherung hochgeladen, wenn ich darin suche?",
         "Nein. Die Datei wird lokal in deinem Browser gelesen; nichts wird irgendwohin "
         "geschickt."),
    ],
}

GUIDES_DE["print-jw-library-notes"] = {
    "title": "JW-Library-Notizen ausdrucken",
    "h1": "Deine JW-Library-Notizen aufs Papier bringen",
    "description": "JW Library hat keinen Drucken-Knopf. Exportiere deine Notizen als Text oder "
                   "Markdown, füg sie in ein beliebiges Dokument ein und drucke — ein "
                   "Studientagebuch, ein Satz Notizen für jemanden ohne die App, oder ein "
                   "Archiv.",
    "intro": [
        "Aus JW Library lässt sich nicht drucken, und Screenshots eines Handybildschirms lesen "
        "sich schlecht. Aber die Notizen gehören dir, und sie in ein druckbares Dokument zu "
        "bringen ist unkompliziert, sobald du die Sicherungsdatei lesen kannst.",
        "Der Studien-Explorer liest eine .jwlibrary-Sicherung in deinem Browser und lässt dich "
        "jede Auswahl an Notizen als reinen Text oder Markdown kopieren oder exportieren — was "
        "jedes Textprogramm, jede Notiz-App und jeder Drucker längst versteht.",
    ],
    "steps": [
        ("Erstelle eine Sicherung und öffne sie",
         "JW Library → Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen, dann lade die Datei auf jwsync.org."),
        ("Grenze auf das ein, was aufs Papier soll",
         "Filtere nach Publikation, Schlagwort, Markierungsfarbe oder Zeitraum, oder such nach "
         "einem Thema. Alles zu drucken ist möglich, aber ein gefilterter Satz ergibt meist "
         "ein weit nützlicheres Dokument."),
        ("Kopiere oder exportiere als Text oder Markdown",
         "Nimm die Auswahl als Markdown oder reinen Text heraus. Fett, Kursiv und Listen "
         "bleiben erhalten, strukturierte Notizen bleiben also auf der Seite strukturiert."),
        ("In ein Dokument einfügen und drucken",
         "Jedes Textprogramm oder jede Notiz-App genügt. Stell Überschriften und Ränder ein, "
         "wie du magst, dann drucke oder speichere als PDF."),
    ],
    "sections": [
        ("Ein Studientagebuch anlegen",
         "Ein Zeitraum ist die natürliche Einheit für ein gedrucktes Tagebuch — ein Jahr an "
         "Notizen, oder der Zeitraum einer Publikation. Die Extraktion nach Datum gibt dir "
         "einen sauberen chronologischen Satz zum Drucken oder Binden, was abseits des "
         "Bildschirms etwas Erfreuliches ist."),
        ("Drucken für jemanden, der die App nicht nutzt",
         "Nicht alle studieren am Gerät. Ein gedruckter Satz Notizen zum aktuellen Stoff ist "
         "für jemanden, der Papier bevorzugt, wirklich nützlich, und er kostet dieselben zwei "
         "Minuten wie jeder andere Export."),
    ],
    "faq": [
        ("Kann ich auch meine Markierungen drucken?",
         "Die Markierungsansicht listet die von dir markierten Stellen auf, und diese Liste "
         "lässt sich zusammen mit deinen Notizen als Text herauskopieren."),
        ("Ändert der Export etwas in JW Library?",
         "Nein. Der Export liest eine Kopie deiner Sicherung; deine Originaldatei und die App "
         "bleiben unangetastet."),
    ],
}

GUIDES_DE["clean-up-duplicate-jw-library-notes"] = {
    "title": "Doppelte und leere JW-Library-Notizen aufräumen",
    "h1": "Doppelte Notizen, leere Notizen und Krempel entfernen",
    "description": "Eine Sicherung zweimal wiederhergestellt oder dieselben Notizen nochmal "
                   "importiert? Der Bibliotheksdoktor prüft deine .jwlibrary-Datei im Browser, "
                   "findet Duplikate und leere Notizen und liefert eine saubere Kopie.",
    "intro": [
        "Bibliotheken sammeln Krempel. Eine Sicherung auf einem Gerät wiederherzustellen, das "
        "schon einen Teil derselben Notizen hatte, einen geteilten Satz zweimal zu "
        "importieren, oder Jahre halb geschriebener, nie fertiger Notizen — jedes davon lässt "
        "etwas zurück, und JW Library bietet keinen Weg, das in Mengen wegzukehren.",
        "Der Bibliotheksdoktor ist ein kostenloser Gesundheitscheck für eine "
        ".jwlibrary-Datei. Er prüft die Sicherung in deinem Browser, sagt dir in klarer "
        "Sprache, was er gefunden hat, und behebt mit einem Tippen, was behebbar ist.",
    ],
    "steps": [
        ("Sichere zuerst — wie immer",
         "JW Library → Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen. Behalte diese Datei; sie ist deine Rückfallebene."),
        ("Starte den Gesundheitscheck",
         "Öffne jwsync.org, lade die Sicherung und starte den Bibliotheksdoktor. Er untersucht "
         "Inhalt und Struktur der Datei, ohne sie irgendwohin zu schicken."),
        ("Lies, was er gefunden hat",
         "Duplikate, leere Notizen und anderer Krempel werden klar aufgelistet, mit Zahlen, "
         "damit du das Ausmaß siehst, bevor du etwas änderst."),
        ("Beheben und die saubere Kopie herunterladen",
         "Ein Tippen wendet die Reparaturen an und erzeugt eine neue, gereinigte "
         ".jwlibrary-Datei. Dein Original wird nie verändert."),
        ("Stelle die saubere Datei wieder her",
         "Sicherung und Wiederherstellung → Wiederherstellen und wähle die gereinigte Datei. "
         "Deine Bibliothek ist dieselbe, nur ohne den Krempel."),
    ],
    "sections": [
        ("Wie Duplikate überhaupt entstehen",
         "Fast immer durch eine Wiederherstellung. Wenn du eine Sicherung auf einem Gerät "
         "einspielst, das schon einen Teil desselben Stoffs hatte — oder dieselbe Datei "
         "zweimal auf verschiedenen Wegen einspielst — kann die App nicht wissen, dass sie "
         "diese Notizen schon gesehen hat."),
        ("Zusammenführen ist der Weg, sie zu vermeiden",
         "Genau deshalb ist das Zusammenführen zweier Sicherungen sicherer, als eine über die "
         "andere zu spielen: Die Zusammenführung erkennt schon vorhandenen Stoff und behält "
         "ihn einmal. Dieselben Prüfungen laufen bei jeder Zusammenführung, eine "
         "zusammengeführte Sicherung kommt also sauber heraus, selbst wenn die Eingangsdateien "
         "es nicht waren."),
    ],
    "faq": [
        ("Löscht er Notizen, die ich eigentlich behalten will?",
         "Er entfernt exakte Duplikate und leere Notizen — Material, in dem nichts zu "
         "verlieren ist. Und weil er eine neue Datei schreibt statt deine zu bearbeiten, ist "
         "das Original immer noch da."),
        ("Kann er Notizen retten, die ich in der App gelöscht habe?",
         "Nein. Wurde eine Notiz vor dem Erstellen der Sicherung in JW Library gelöscht, ist "
         "sie nicht in der Datei — dafür ist eine ältere Sicherung der richtige Ort."),
    ],
}

GUIDES_DE["backup-jw-library-before-phone-repair"] = {
    "title": "JW Library vor Zurücksetzen oder Reparatur sichern",
    "h1": "Vor dem Zurücksetzen, einer Reparatur oder dem Verkauf des Handys",
    "description": "Ein Zurücksetzen löscht die JW-Library-Notizen mit allem anderen, und "
                   "Umzugs-Werkzeuge nehmen sie nicht mit. Mach eine Sicherung, prüfe, dass "
                   "sie sich wirklich öffnen lässt, dann setz ohne Risiko zurück.",
    "intro": [
        "Setz das Handy zurück, gib es zur Reparatur oder weiter, und die persönlichen "
        "Studiendaten von JW Library gehen mit. Fotos und Apps kommen aus einer Cloud-Sicherung "
        "zurück; Jahre an Notizen, Markierungen und Lesezeichen in der Regel nicht, weil "
        "Umzugs-Werkzeuge die privaten Daten der App überspringen.",
        "Die Abhilfe dauert fünf Minuten, und der Schritt, den die meisten auslassen, ist der "
        "wichtigste: zu prüfen, dass die Sicherungsdatei wirklich lesbar ist, bevor das Gerät "
        "gelöscht wird.",
    ],
    "steps": [
        ("Erstelle die Sicherung",
         "JW Library → Persönliches Studium → Sicherung und Wiederherstellung → Sicherung "
         "erstellen. Du bekommst eine .jwlibrary-Datei — meist nur ein paar Megabyte."),
        ("Bring sie vom Gerät herunter",
         "Schick sie dir per E-Mail oder leg sie in Drive, iCloud oder einen Ordner am "
         "Computer. Eine Sicherung, die nur auf dem Handy liegt, das du gleich löschst, ist "
         "keine Sicherung."),
        ("Prüfe, dass sie sich öffnet, bevor du etwas löschst",
         "Lade die Datei auf jwsync.org und sieh sie dir an — Notizen, Markierungen und "
         "Lesezeichen sollten alle da sein, und der Gesundheitscheck meldet, wenn etwas mit "
         "der Datei nicht stimmt. Genau darum geht es: Hinterher zu merken, dass die Datei "
         "unlesbar ist, ist zu spät."),
        ("Zurücksetzen, dann wiederherstellen",
         "Nach dem Zurücksetzen oder der Reparatur installiere JW Library, melde dich an, dann "
         "Sicherung und Wiederherstellung → Wiederherstellen und wähle deine Datei."),
        ("Zwischendurch ein Leihgerät benutzt? Zusammenführen, nicht überschreiben",
         "Hast du auf einem Übergangsgerät Notizen gemacht, sichere auch das und führe beide "
         "Dateien vor dem Wiederherstellen auf jwsync.org zusammen — sonst löscht das "
         "Wiederherstellen der alten Sicherung alles, was du in der Wartezeit geschrieben "
         "hast."),
    ],
    "sections": [
        ("Warum die Prüfung die zusätzliche Minute wert ist",
         "Abgebrochene Übertragungen, Cloud-Speicher, die Dateien verstümmeln, und unterwegs "
         "umbenannte Endungen erzeugen alle Sicherungen, die im Ordner in Ordnung aussehen und "
         "beim Wiederherstellen scheitern. Die Datei vorher zu öffnen macht aus einem stillen "
         "Problem eines, das du noch beheben kannst, solange das ursprüngliche Gerät die Daten "
         "noch hat."),
        ("Behalte die Datei nach dem Wiederherstellen",
         "Lösch sie nicht, sobald das neue Gerät läuft. Alte Sicherungen sind der einzige Weg "
         "zurück, wenn Monate später versehentlich eine Notiz gelöscht wird, und sie kosten "
         "nichts."),
    ],
    "faq": [
        ("Kommen meine heruntergeladenen Publikationen zurück?",
         "Die Sicherung enthält deine persönlichen Studiendaten — Notizen, Markierungen, "
         "Lesezeichen, Schlagwörter und Wiedergabelisten. Publikationen werden danach einfach "
         "neu heruntergeladen."),
        ("Funktioniert die Datei, wenn ich Handymarke oder Plattform wechsle?",
         "Ja. Das .jwlibrary-Format ist unter Android, iPhone, iPad und Windows dasselbe."),
    ],
}

GUIDES_DE["jw-library-notes-missing-after-update"] = {
    "title": "JW-Library-Notizen nach einem Update oder einer Neuinstallation weg",
    "h1": "Notizen weg nach App-Update, Neuinstallation oder Wiederherstellung",
    "description": "Deine Notizen sind nach einem Update, einer Neuinstallation oder erneutem "
                   "Anmelden verschwunden. Was du zuerst tun solltest, was nicht, und wie du "
                   "sie zurückbekommst, ohne das Neuere zu verlieren.",
    "intro": [
        "JW Library nach einem Update zu öffnen und die Notizen verschwunden vorzufinden ist erschreckend, und in der großen Mehrheit der Fälle sind sie wiederherstellbar. Entscheidend ist, was du in den nächsten Minuten tust — genauer: das Eine nicht zu tun, das aus einer behebbaren Lage einen endgültigen Verlust macht.",
        "Ein unangenehmer Moment: JW Library öffnet sich, und die Notizen sind nicht da. Vor "
        "allem anderen ein Rat — überstürz nichts. Das meiste, was diese Lage unrettbar macht, "
        "passiert in den ersten zehn Minuten, indem genau die Sicherung überschrieben wird, "
        "die die fehlenden Notizen noch enthält.",
        "Geh die Schritte unten der Reihe nach durch. Das Ziel ist eine einzige Datei mit "
        "sowohl den alten Notizen als auch allem, was du seitdem geschrieben hast.",
    ],
    "steps": [
        ("Überschreib deine Sicherungen noch nicht",
         "Widersteh dem Drang, eine frische Sicherung über eine alte zu legen, und stelle "
         "nichts blind wieder her. Eine ältere Sicherungsdatei ist der wahrscheinlichste Ort, "
         "an dem deine Notizen noch existieren."),
        ("Such die neueste Sicherung, die du hast",
         "Prüfe E-Mail-Anhänge, Google Drive, iCloud Drive, den Download-Ordner deines "
         "Computers und jedes andere Gerät, auf dem du wiederhergestellt hast. Sicherungen "
         "sind klein, viele haben mehr Kopien, als sie denken."),
        ("Schau in die Datei, bevor du sie wiederherstellst",
         "Lade den Kandidaten auf jwsync.org und sieh, was wirklich drin ist — wie viele "
         "Notizen, aus welchen Publikationen, bis zu welchem Datum. Das sagt dir, ob es die "
         "richtige Datei ist, bevor du dich auf eine Wiederherstellung festlegst."),
        ("Sichere auch das aktuelle Gerät",
         "Auch wenn es leer wirkt, sichere es. Hast du seit dem Verschwinden der Notizen "
         "irgendetwas geschrieben, ist diese Datei die einzige Kopie davon."),
        ("Führe beide zusammen, dann stelle wieder her",
         "Führe die alte Sicherung mit der aktuellen auf jwsync.org zusammen. Das Ergebnis "
         "enthält die geretteten Notizen und alles seither Geschriebene, Duplikate nur einmal. "
         "Stelle diese zusammengeführte Datei wieder her — nie die alte Sicherung allein."),
    ],
    "sections": [
        ("Warum die alte Sicherung allein wiederherzustellen falsch ist",
         "Eine Wiederherstellung ersetzt die Bibliothek des Geräts vollständig. Spielst du die "
         "alte Sicherung direkt ein, bekommst du die fehlenden Notizen zurück und verlierst "
         "alles, was nach jener Sicherung geschrieben wurde. Erst das Zusammenführen macht die "
         "Rettung verlustfrei."),
        ("Wenn sich die Sicherung selbst nicht wiederherstellen lässt",
         "Eine Datei, die beim Wiederherstellen abbricht, ist nicht zwangsläufig verloren. "
         "Lass den Gesundheitscheck darüber laufen — Schäden durch abgebrochene Downloads, "
         "Cloud-Synchronisierung oder eine umbenannte Endung sind oft reparabel, und eine "
         "gereinigte Kopie lässt sich normal einspielen."),
        ("Zuerst: Erstelle jetzt noch keine neue Sicherung",
         "Sind die Notizen verschwunden, widerstehe dem Reflex, sofort zu sichern. Eine Sicherung hält den aktuellen Zustand fest, und wenn der aktuelle Zustand der leere ist, riskierst du, die gute Datei zu überschreiben, die du bereits hattest. Finde zuerst heraus, welche Sicherungen existieren — in Downloads, Dateien, der E-Mail oder der Cloud — und entscheide erst dann. Nichts auf dem Gerät wird durch eine hastige Sicherung besser."),
        ("Warum ein Update so wirken kann, als seien Notizen weg",
         "Die übliche Ursache ist kein Löschen. Ein Update kann die App auf eine frische, leere Datenbank zeigen lassen, während die alte noch auf dem Speicher liegt; eine Neuinstallation — auch eine, die ein halb fehlgeschlagenes Store-Update selbst ausgelöst hat — startet die App bei null; und auf gemeinsam genutzten Geräten oder solchen mit mehreren Profilen kann die App unter einem anderen Profil laufen. In allen Fällen sind die Notizen weniger gelöscht als nicht geladen, und deshalb bringt eine Wiederherstellung aus einer Sicherung meist alles sauber zurück."),
        ("Eine alte Sicherung zurückholen, ohne neue Arbeit zu verwerfen",
         "Hast du seit der Sicherung studiert, tauscht eine einfache Wiederherstellung einen Verlust gegen einen anderen: Sie bringt die alten Notizen zurück und entfernt alles Neuere. Der Ausweg ist, den aktuellen Zustand in eine eigene Datei zu sichern, diese mit der älteren Sicherung zusammenzuführen, sodass beide Notizbestände in einer Datei stehen, und das Ergebnis wiederherzustellen. Du hast dann die zurückgeholten und die neuen Notizen zusammen, statt wählen zu müssen."),
        ("Wenn die App sich selbst neu installiert hat",
         "Eine Neuinstallation leert den app-eigenen Speicher: Alles, was nicht in einer Sicherung steht, ist unwiederbringlich — es gibt keine Cloud-Kopie als Rückhalt. Prüfe jeden Ort, an dem eine .jwlibrary-Datei gespeichert worden sein könnte, bevor du schließt, es gebe keine: auch den Gesendet-Ordner deiner E-Mail und jeden Cloud-Speicher, den du je genutzt hast. Sobald du eine findest, stelle sie wieder her — und bewahre Sicherungen fortan außerhalb des Geräts auf."),
        ("Wenn alles zurück ist",
         "Sind deine Notizen wiederhergestellt, mach noch eine Sicherung und lege sie außerhalb des Geräts ab — das gerade Erlebte ist das Argument dafür. Musstest du eine alte Sicherung mit dem aktuellen Zustand zusammenführen, behalte auch beide Ausgangsdateien: Sie sind datierte Momentaufnahmen, und mehr davon zu haben war genau das, was die Rettung möglich gemacht hat."),
    ],
    "faq": [
        ("Sind die Notizen noch irgendwo auf dem Gerät?",
         "Nicht in einer Form, an die man von außerhalb der App herankommt. Rettung heißt "
         "realistisch: eine frühere Sicherungsdatei — deshalb ist das Aufheben alter "
         "Sicherungen so wichtig."),
        ("Bringt erneutes Anmelden die Notizen zurück?",
         "Nein. Persönliche Studiendaten hängen nicht an einem Konto; sie liegen auf dem Gerät "
         "und reisen nur über Sicherungsdateien."),
        ("Was, wenn meine einzige Sicherung Monate alt ist?",
         "Führe sie mit einer Sicherung des Geräts zusammen, wie es jetzt ist. Du bekommst "
         "alles zurück, was die alte Datei hat, und behältst alles, was das Gerät noch hat, "
         "ohne zwischen beiden zu wählen."),
        ("Sind meine Notizen wirklich weg?",
         "Nicht zwangsläufig. Existiert irgendwo eine Sicherung, ist alles darin vollständig wiederherstellbar. Unwiederbringlich ist nur die Arbeit nach der jüngsten Sicherung."),
        ("Kann ich eine alte Sicherung mit dem jetzigen Stand verbinden?",
         "Ja — sichere zuerst den aktuellen Zustand, führe ihn mit der älteren zusammen und stelle das Ergebnis wieder her. Beide Notizbestände landen in derselben Bibliothek."),
        ("Löscht das Wiederherstellen einer alten Sicherung meine neuen Notizen?",
         "Für sich genommen ja, denn eine Wiederherstellung ersetzt die Daten des Geräts. Führe die aktuelle Sicherung zuerst mit der alten zusammen und stelle die zusammengeführte Datei wieder her."),
        ("Soll ich die App neu installieren, um das zu beheben?",
         "Nein — eine Neuinstallation leert den app-eigenen Speicher und nimmt jede Chance, noch Vorhandenes zu retten. Suche zuerst eine vorhandene Sicherung und behandle die Neuinstallation als letztes Mittel, wenn du eine hast."),
    ],
}

GUIDES_DE["help-family-member-move-jw-library-notes"] = {
    "title": "Einem Familienmitglied beim Umzug seiner JW-Library-Notizen helfen",
    "h1": "Jemand anderem helfen, seine JW-Library-Notizen umzuziehen oder zu retten",
    "description": "Du bist der, den man fragt, wenn das Handy nicht will. Hier ist der "
                   "kürzeste verlässliche Weg, die JW-Library-Notizen eines Verwandten auf ein "
                   "neues Gerät zu bringen — auch, ohne seine Notizen zu lesen.",
    "intro": [
        "Früher oder später drückt dir jemand sein Handy in die Hand, ein neues daneben. Die "
        "JW-Library-Notizen sind der Teil, der nicht von allein mitkommt, und oft der, der am "
        "meisten zählt — Jahre an Studium, die kein Umzugs-Werkzeug hinüberträgt.",
        "Der Ablauf ist derselbe wie bei dir selbst, mit einer zusätzlichen Überlegung, die man "
        "vorher klären sollte: auf wessen Gerät die Arbeit stattfindet.",
    ],
    "steps": [
        ("Erklär ihm, wie er auf dem alten Gerät sichert",
         "JW Library → Persönliches Studium → Drei-Punkte-Menü → Sicherung und "
         "Wiederherstellung → Sicherung erstellen. Das speichert eine .jwlibrary-Datei. Wenn "
         "du nicht dabei bist, geht dieser Teil auch am Telefon."),
        ("Hol dir die Datei dorthin, wo du sie brauchst",
         "Lass sie ihn sich selbst mailen oder mit dir teilen. Sie ist klein genug für jeden "
         "Messenger."),
        ("Prüfe, dass die Datei sich öffnet",
         "Lade sie auf jwsync.org und bestätige, dass die Notizen da sind. Das zu tun, bevor "
         "das alte Gerät gelöscht oder weitergegeben wird, macht aus einer bösen Überraschung "
         "ein Nicht-Ereignis."),
        ("Führe zusammen, wenn das neue Gerät schon Notizen hat",
         "Nutzt die Person das neue Handy schon eine Weile, sichere auch das und führe beide "
         "Dateien zusammen — sonst löscht das Wiederherstellen der alten Sicherung alles, was "
         "sie auf dem neuen Gerät geschrieben hat."),
        ("Begleite sie beim Wiederherstellen",
         "Auf dem neuen Gerät: Sicherung und Wiederherstellung → Wiederherstellen, Datei "
         "wählen. Notizen, Markierungen, Lesezeichen und Schlagwörter erscheinen alle."),
    ],
    "sections": [
        ("Das Ganze, ohne ihre Notizen zu lesen",
         "Persönliche Studiennotizen sind persönlich. Wenn du sie lieber nicht sehen "
         "möchtest — oder sie es lieber nicht hätte — mach alles auf ihrem Gerät: Es ist eine "
         "Webseite, du kannst also jwsync.org auf ihrem Handy oder Tablet öffnen, ihre Dateien "
         "dort laden und die Sicherung nie auf deinem eigenen Rechner haben. Hochgeladen wird "
         "so oder so nichts, aber so verlässt die Datei nie ihre Hände."),
        ("Hinterlass ihr eine Sicherung, die sie wiederfindet",
         "Bevor du das Handy zurückgibst, sorg dafür, dass die Sicherungsdatei irgendwo liegt, "
         "wo sie sie wiederfindet — ihr eigenes Postfach oder ihr Cloud-Speicher, nicht nur "
         "dein Download-Ordner. Beim nächsten Mal braucht sie dich vielleicht gar nicht."),
    ],
    "faq": [
        ("Geht das auch aus der Ferne?",
         "Ja. Wenn die Person eine Sicherung erstellen und dir die Datei schicken kann, "
         "funktioniert alles Weitere aus der Ferne — und das Wiederherstellen sind ein paar "
         "Schritte, durch die du sie am Telefon führen kannst."),
        ("Sie hat ein Android und das neue ist ein iPhone. Macht das etwas aus?",
         "Nein. Das Sicherungsformat ist unter Android, iPhone, iPad und Windows identisch."),
        ("Was, wenn sie nie gesichert hat und das alte Handy weg ist?",
         "Dann gibt es nichts, woraus man retten könnte — die Daten lagen auf diesem Gerät. "
         "Umso mehr lohnt es sich, auf dem neuen Handy sofort die Gewohnheit regelmäßiger "
         "Sicherungen einzuführen."),
    ],
}

GUIDES_DE["import-markdown-notes-jw-library"] = {
  "title": "Markdown-Notizen in JW Library importieren",
  "h1": "So importierst du Markdown-Notizen in JW Library",
  "description": "Verwandle .md-Dateien aus Obsidian, Notion oder einem beliebigen Markdown-Editor in echte JW-Library-Notizen, gesetzt auf den richtigen Vers — kostenlos, privat, im Browser.",
  "intro": [
   "JW Library bietet keinerlei Möglichkeit, Text hineinzubekommen. Innerhalb der App kannst du Notizen schreiben, aber eine anderswo verfasste Notiz — in Obsidian, in Notion, in einer schlichten Textdatei auf dem Rechner — hat überhaupt keinen Weg in deine Bibliothek. Man tippt sie neu ab oder gibt auf und pflegt zwei Sammlungen von Studiennotizen, die nie zusammenfinden.",
   "JW Sync schließt diese Lücke. Lade eine Sicherung in den Studien-Explorer, klicke auf „Markdown importieren“, und deine .md-Dateien werden darin zu echten Notizen: Titel, Datum und Tags bleiben erhalten, und wenn die Datei angibt, zu welcher Bibelstelle sie gehört, hängt die Notiz an genau diesem Vers — so, als hättest du sie beim Lesen in der App geschrieben.",
   "Das funktioniert in beide Richtungen. Von dieser Seite exportierte Notizen tragen Buch, Kapitel und Vers mit sich und kehren deshalb genau dorthin zurück, wo sie herkamen. Anderswo geschriebene Notizen haben so etwas meist nicht, und darum erklärt diese Seite die ein bis zwei Zeilen, die sie platzieren — und was passiert, wenn eine Datei sie nicht hat.",
  ],
  "steps": [
   ("Erstelle in JW Library eine Sicherung",
    "Öffne JW Library, geh zu Persönliches Studium, tippe auf das Drei-Punkte-Menü, wähle Sichern und Wiederherstellen und dann Sicherung erstellen. Das ergibt eine .jwlibrary-Datei — die Bibliothek, zu der deine Notizen hinzukommen."),
   ("Öffne den Studien-Explorer",
    "Geh auf jwsync.org, öffne den Studien-Explorer und lade diese .jwlibrary-Datei. Alles läuft in deinem Browser; die Datei wird nie hochgeladen."),
   ("Klicke auf „Markdown importieren“",
    "Die Schaltfläche steht neben „Markdown exportieren“. Wähle so viele .md-Dateien, wie du möchtest, oder ein .zip mit ihnen — auch das .zip, das diese Seite beim Exportieren erzeugt."),
   ("Lies die Zusammenfassung, bevor etwas geschrieben wird",
    "Du erfährst, wie viele Notizen auf einem Vers landen, wie viele als freie Notizen hinzukommen und wie viele bereits in deiner Sicherung stehen und übersprungen werden. Alles, was die Seite deuten musste, steht Zeile für Zeile da, mit einem Häkchen — du entscheidest, statt es später zu entdecken."),
   ("Exportieren und wiederherstellen",
    "Klicke auf „.jwlibrary exportieren“ und stelle diese Datei in JW Library über Sichern und Wiederherstellen → Wiederherstellen wieder her. Deine importierten Notizen gehören nun zu deiner Bibliothek auf diesem Gerät."),
  ],
  "sections": [
   ("Die kürzeste Datei, die funktioniert",
    "Eine Markdown-Datei braucht gar nichts, um importiert zu werden: Eine Datei, die nur Text enthält, wird zu einer Notiz und nimmt ihren Titel aus der ersten Überschrift oder ersatzweise aus dem Dateinamen. Alles Weitere dient dazu, zu sagen, wohin die Notiz gehört. Eine vollständige Datei sieht so aus:\n\n---\ntitle: Der Kelch, um den er betete\ntags: [studium, gethsemane]\npublication: Matthew 26:39\n---\n\nSein Gebet zeigt Unterordnung, nicht Widerwillen.\n\nDer Block zwischen den beiden Strichzeilen heißt Front Matter. Die Zeilen darunter sind die Notiz selbst."),
   ("Die Felder, die gelesen werden",
    "Nur fünf Dinge werden gelesen, und jedes davon versteht mehrere Schreibweisen, damit du dir keine bestimmte merken musst. **title** (oder name, heading) wird zum Titel der Notiz. **tags** (oder tag, keywords, categories, labels, topics) werden zu echten JW-Library-Tags, die angelegt werden, falls es sie noch nicht gibt. **date** (oder created, modified) setzt das Datum der Notiz; verstanden wird alles, was JJJJ-MM-TT enthält. **publication** (oder pub, reference, ref, scripture, citation, source, passage) ist die Stelle für die Bibelstelle. **book**, **chapter** und **verse** (oder ch, v, vs, verses) tun dasselbe in getrennten Feldern. Jedes andere Feld, das du für dich behältst — Autor, Status, was dein Editor sonst ergänzt —, wird ignoriert und nicht als Fehler behandelt."),
   ("Drei Wege, eine Notiz auf einen Vers zu setzen",
    "Schreib die Stelle in eine Zeile: `publication: Matthew 26:39`. Oder teile sie auf: `book: Matthew`, `chapter: 26`, `verse: 39`. Oder nimm beides — genau das macht der Export dieser Seite, damit die Datei für Menschen gut lesbar und für die Maschine eindeutig ist. Alle drei ergeben dasselbe; nimm, was zu deinem Editor passt."),
   ("Wie großzügig die Bibelstelle sein darf",
    "Buchnamen werden großzügig erkannt. Vollständige Namen funktionieren, und ebenso die Abkürzungen, die Menschen tatsächlich tippen: Matt, Matt., Mt, 1 Cor, 1Cor, I Corinthians, Second Timothy, Psalm ebenso wie Psalms, Song of Songs ebenso wie Song of Solomon. Zwischen Kapitel und Vers darf ein Doppelpunkt, ein Punkt oder ein v stehen — `John 3:16`, `John 3.16` und `1 Cor 13 v4` werden gleich gelesen. Leerzeichen sind überall optional, `1Cor13:4` geht also auch.\n\nDas Front Matter ist ebenso nachsichtig. Feldnamen dürfen großgeschrieben sein. Das Leerzeichen nach dem Doppelpunkt darf fehlen. Überzählige Leerzeichen und Tabulatoren werden ignoriert, ebenso Anführungszeichen um Werte und ein abschließender #-Kommentar. Windows-Zeilenenden stören nicht. Du kannst die ---Zeilen sogar ganz weglassen und die Datei direkt mit den Feldern beginnen, solange die allererste Zeile einer der erkannten Namen ist — diese Regel gibt es, damit eine Notiz, die mit einem gewöhnlichen Satz mit Doppelpunkt beginnt, ihren ersten Absatz nicht verliert."),
   ("Tags, wie immer du sie schreibst",
    "All diese Formen ergeben dieselben zwei Tags: `tags: [studium, griechisch]`, `tags: studium, griechisch`, `tags: studium; griechisch`, `tags: #studium #griechisch`, oder eine Liste in eigenen Zeilen unter `tags:`, jeder Eintrag mit einem Bindestrich davor. Tags, die es in deiner Bibliothek schon gibt, werden wiederverwendet statt doppelt angelegt — die importierte Notiz hängt sich also an genau das Tag, nach dem du ohnehin filterst."),
   ("Was passiert, wenn etwas unklar ist",
    "Nichts Unsicheres wird für dich entschieden. Ist ein Buchname einem echten ähnlich, aber nicht gleich — `Mathew`, `Ecclesiates` —, wird die Notiz nicht automatisch gesetzt. Sie erscheint in der Zusammenfassung in einer eigenen Zeile mit dem, was die Seite daraus gemacht hat: „gelesen als Matthew 26:39“, mit einem Häkchen. Nimm das Häkchen weg, und sie bleibt draußen; lass es stehen, und sie geht dorthin, wo die Zeile es sagt.\n\nWird das Buch überhaupt nicht erkannt, sagt die Zeile das, und die Notiz kommt stattdessen als freie Notiz hinzu — nie auf eine Vermutung gezwungen. Ein nummeriertes Buch behält seine Nummer: `1 Jonh` kann nur zu 1. Johannes korrigiert werden, niemals zu 2. Johannes."),
   ("Was bewusst nicht geschieht",
    "Ein Versbereich hängt die Notiz an den ersten Vers: `Matthew 26:39-41` setzt sie auf Vers 39, weil eine JW-Library-Notiz an einem Punkt im Text hängt und nicht an einer Spanne. Eine Stelle mit Kapitel, aber ohne Vers — `Matthew 26` — hängt die Notiz an dieses Kapitel. Eine Datei, die eine Publikation statt einer Bibelstelle nennt — `The Watchtower—2023 No. 4` —, wird ohne Nachfrage als gewöhnliche freie Notiz importiert, denn genau das schreibt der Export dieser Seite für Notizen aus einem Artikel."),
   ("Formatierung, die die Reise übersteht",
    "Absätze, Zeilenumbrüche, **fett**, *kursiv* und Aufzählungen kommen als echte Formatierung in JW Library an. Eine Überschrift am Dateianfang wird als Titel der Notiz verwendet, statt darin wiederholt zu werden. Alles, was Markdown ausdrücken kann und JW-Library-Notizen nicht — Tabellen, Bilder, Links, Codeblöcke —, wird auf seinen Text reduziert; kein Wort geht verloren, auch wenn das Layout nicht mitkommen kann."),
   ("Wo die Notizen wirklich landen, und warum das sicher ist",
    "Um eine Notiz an einen Vers zu hängen, braucht JW Library interne Kennungen für dieses Kapitel, die für deine Bibliothek eigen sind. JW Sync erfindet sie nie. Es verwendet den Ort wieder, den deine eigene Sicherung für dieses Kapitel bereits hat, oder kopiert diese Kennungen von einem anderen Bibelort in derselben Datei. Enthält eine Sicherung überhaupt keine Notizen oder Markierungen in der Bibel, gibt es nichts zu kopieren — dann kommen die Notizen als freie Notizen hinzu, statt an etwas gehängt zu werden, das die App womöglich nicht erkennt. Das ist Absicht: Eine Notiz, die still an der falschen Stelle landet, ist schlimmer als eine, die sichtbar ungebunden ankommt."),
   ("Dieselben Dateien zweimal importieren",
    "Eine Notiz gilt als bereits vorhanden, wenn Titel, Text und Ort mit etwas in der Sicherung übereinstimmen — denselben Export erneut zu importieren verdoppelt also nichts. Die Zusammenfassung nennt dir vor dem Bestätigen, wie viele deshalb übersprungen werden. Alles, was ein Import hinzufügt, ist ein einziger Rückgängig-Schritt, und importierte Notizen bekommen das Tag „Imported“, damit du sie später als Gruppe finden, filtern oder löschen kannst."),
  ],
  "faq": [
   ("Muss ich die ---Zeilen verwenden?",
    "Nein. Sie machen die Datei eindeutig und jeder Markdown-Editor versteht sie, aber du kannst die Datei auch direkt mit den Feldern beginnen — `title: …` in der ersten Zeile — oder ganz auf Front Matter verzichten und die Notiz ihren Titel aus der ersten Überschrift nehmen lassen."),
   ("Was, wenn ich einen Buchnamen falsch schreibe?",
    "Meist findet die Seite heraus, was gemeint war, handelt aber nicht allein danach. Die Notiz erscheint in der Zusammenfassung mit der gewählten Lesart und einem Häkchen, damit du bestätigst, bevor etwas geschrieben wird."),
   ("Kann ich einen ganzen Obsidian-Ordner importieren?",
    "Wähle auf einmal so viele .md-Dateien, wie du willst, oder pack den Ordner in ein .zip und nimm das. Dateien darin werden genauso gelesen wie einzelne."),
   ("Überschreibt der Import meine vorhandenen Notizen?",
    "Nein. Der Import fügt nur hinzu. Deine bestehenden Notizen, Markierungen, Lesezeichen und Tags bleiben unangetastet, und die geladene Datei wird nie verändert — am Ende lädst du eine neue .jwlibrary herunter."),
   ("Werden meine Notizen irgendwohin hochgeladen?",
    "Nein. Alles läuft in deinem Browser, wie alles andere auf dieser Seite. Weder deine Sicherung noch deine Markdown-Dateien verlassen dein Gerät."),
   ("In welchen Sprachen darf die Bibelstelle stehen?",
    "Buchnamen werden derzeit auf Englisch erkannt — das schreibt auch der Export. Wenn du deine Notizen in einer anderen Sprache führst, nimm die Felder `book`, `chapter` und `verse` mit dem englischen Buchnamen, oder importiere die Notizen ungebunden und ordne sie später von Hand zu."),
   ("Bekomme ich meine Notizen wieder heraus?",
    "Ja — „Markdown exportieren“ auf demselben Bildschirm schreibt jede Notiz in eine .md-Datei mit denselben Feldern. Notizen können JW Library also verlassen und zurückkehren, ohne ihren Platz zu verlieren."),
  ],
}

GUIDES_DE["write-markdown-notes-for-jw-library"] = {
  "title": "Eine Markdown-Datei schreiben, die sich in JW Library importieren lässt",
  "h1": "So schreibst du eine Markdown-Datei, die sich in JW Library importieren lässt",
  "description": "Schreibe eine Notiz in Notepad, TextEdit oder Obsidian und lass sie beim richtigen Vers in JW Library landen. Die genauen Zeilen zum Tippen — und alles, was du weglassen kannst.",
  "intro": [
   "JW Sync kann Markdown-Dateien in eine JW-Library-Sicherung einlesen, und damit stellt sich die einzige Frage, die wirklich zählt, sobald man von der Funktion weiß: Wie muss die Datei eigentlich aussehen? Diese Seite beantwortet das von der Schreibseite her — nicht, was der Import akzeptiert, sondern was du tatsächlich tippst.",
   "Kurz gesagt: Eine Notiz ist eine Textdatei. Datei anlegen, Notiz hineinschreiben, mit .md am Ende speichern — und sie wird importiert. Alles Weitere hier dreht sich um eine einzige optionale Zeile: die, die sagt, zu welcher Bibelstelle die Notiz gehört, damit sie in JW Library beim Lesen dieses Verses erscheint statt lose zwischen deinen übrigen Notizen zu liegen.",
   "Nichts davon braucht einen Markdown-Editor, und nichts davon verlangt, dass du Markdown lernst. Notepad unter Windows und TextEdit auf dem Mac genügen. Wenn du deine Studiennotizen ohnehin in Obsidian oder Notion führst: Diese Dateien sind bereits Markdown, und weiter unten steht zu beiden ein eigener Abschnitt.",
  ],
  "steps": [
   ("Öffne irgendeinen Editor für reinen Text",
    "Notepad unter Windows, TextEdit auf dem Mac oder die Markdown-App, die du schon benutzt — Obsidian, Typora, iA Writer, Joplin. Zu vermeiden ist nur eine Textverarbeitung: Word und Google Docs speichern Layout und Formatierung statt reinen Text, und keines von beiden erzeugt eine Datei, die der Import lesen kann."),
   ("Tippe die Notiz",
    "Schreibe den Titel in die erste Zeile, mit einem # davor, lass eine Leerzeile und schreibe die Notiz darunter. Das ist bereits eine vollständige, gültige Datei. Wenn du gar keine Titelzeile schreiben möchtest, wird stattdessen der Dateiname verwendet."),
   ("Speichere sie mit .md am Ende",
    "Nenne sie, wie du willst — meine notiz.md. Unter Windows speichert Notepad eine .txt, solange du nicht vorher „Dateityp“ auf „Alle Dateien“ umstellst; das wird am häufigsten übersehen. Auf dem Mac wählst du vor dem Speichern Format und dann In reinen Text umwandeln."),
   ("Ergänze die Zeile, die sie auf einen Vers setzt",
    "Ganz oben in der Datei, über allem anderen, schreibst du eine Zeile aus drei Bindestrichen, dann publication: Matthew 26:39, dann noch einmal drei Bindestriche. Die Notiz hängt jetzt an diesem Vers. Lässt du das weg, wird die Notiz trotzdem importiert — sie kommt eben ohne Verknüpfung an."),
   ("Importiere sie in eine Sicherung",
    "Geh in JW Library auf Persönliches Studium, öffne das Drei-Punkte-Menü, wähle Sichern und Wiederherstellen und erstelle eine Sicherung. Lade diese Datei auf jwsync.org im Studien-Explorer, klicke auf „Markdown importieren“, wähle deine .md-Dateien und lies die Zusammenfassung, die dir gezeigt wird, bevor irgendetwas geschrieben wird. Danach „.jwlibrary exportieren“ und diese Datei in JW Library wiederherstellen."),
  ],
  "sections": [
   ("Die kürzeste Datei, die funktioniert",
    "Eine Datei, in der nichts als Text steht, ist bereits eine gültige Notiz. Das ist alles:\n\n```\n# Der Kelch, um den er betete\n\nSein Gebet zeigt Unterordnung, nicht Widerwillen.\n```\n\nDie Zeile, die mit # beginnt, wird zum Titel der Notiz, und alles darunter wird die Notiz. Diese Datei wird anstandslos importiert. Sie kommt einfach als eigenständige Notiz an, zwischen deinen Notizen statt an eine Bibelstelle gehängt."),
   ("Die Datei unter Windows anlegen",
    "Öffne Notepad, tippe die Notiz und wähle Datei und Speichern unter. Stelle vor dem Speichern „Dateityp“ von „Textdokumente“ auf „Alle Dateien“ um — ohne diesen Schritt hängt Notepad still .txt an und du hast meine notiz.md.txt, die der Import nicht sieht. Tippe dann den Namen mit .md am Ende. Windows warnt dich vielleicht, dass das Ändern der Dateiendung die Datei unbrauchbar machen könnte; genau diese Warnung ist das Zeichen, dass du es richtig gemacht hast."),
   ("Die Datei auf einem Mac anlegen",
    "Öffne TextEdit und wähle Format und dann In reinen Text umwandeln, bevor du irgendetwas tippst. TextEdit startet im Rich-Text-Modus und speichert .rtf, was überhaupt keine Textdatei ist. Sobald es im Modus für reinen Text ist, wählst du Ablage und Sichern und lässt den Namen auf .md enden. Wenn macOS anbietet, .txt anzuhängen, lehne ab."),
   ("Die Datei auf einem Handy oder Tablet anlegen",
    "Es genügt jede App, die Markdown speichern oder exportieren kann — Obsidian, Bear, iA Writer, Joplin, Markor unter Android. Die vorinstallierten Notiz-Apps von iPhone und Android können in der Regel keine .md-Datei speichern; auf dem Handy führt der Weg also über eine dieser Apps, oder du schreibst gleich am Computer. Beim Import kannst du beliebig viele Dateien auf einmal auswählen, und ein ganzer Ordner lässt sich zippen und als eine einzige .zip übergeben."),
   ("Die eine Zeile, die eine Notiz auf einen Vers setzt",
    "Alles, was dem Import sagt, wohin die Notiz gehört, steht in einem kleinen Block ganz oben in der Datei, zwischen zwei Zeilen aus drei Bindestrichen. Das heißt Front Matter, und für die meisten Notizen ist es eine einzige Zeile:\n\n```\n---\npublication: Matthew 26:39\n---\n\n# Der Kelch, um den er betete\n\nSein Gebet zeigt Unterordnung, nicht Widerwillen.\n```\n\nDiese Notiz hängt jetzt an Matthäus 26:39. Sie erscheint in JW Library, während du diesen Vers liest — genau so, als hättest du sie dort in der App geschrieben."),
   ("Die Bibelstelle so schreiben, dass sie verstanden wird",
    "Schreibe den Buchnamen auf Englisch, auch wenn die Notiz selbst in einer anderen Sprache ist: Matthew, nicht Matthäus. Auch die Abkürzungen, die Menschen tatsächlich tippen, werden verstanden — Matt, Matt., Mt, 1 Cor, 1Cor, I Corinthians, Second Timothy. Zwischen Kapitel und Vers kannst du einen Doppelpunkt, einen Punkt oder den Buchstaben v setzen: John 3:16, John 3.16 und 1 Cor 13 v4 bedeuten dasselbe, und Leerzeichen sind optional, 1Cor13:4 geht also auch. Ein Bereich wie Matthew 26:39-41 setzt die Notiz auf den ersten Vers, also 39, weil eine JW-Library-Notiz an einem Punkt im Text hängt und nicht an einer Spanne."),
   ("Die vollständige Datei, mit Titel, Datum und Tags",
    "Drei weitere Zeilen stehen zur Verfügung, wenn du sie möchtest, und jede davon ist optional:\n\n```\n---\ntitle: Der Kelch, um den er betete\ndate: 2026-08-15\ntags: [studium, gethsemane]\npublication: Matthew 26:39\n---\n\nSein Gebet zeigt Unterordnung, nicht Widerwillen.\n```\n\ntitle leistet dasselbe wie die Überschrift mit #, du brauchst also nur eines von beidem. date setzt das Datum der Notiz, statt den Tag des Imports stehen zu lassen. tags werden zu echten JW-Library-Tags, nach denen du filtern kannst, und ein Tag, den du schon hast, wird wiederverwendet statt verdoppelt. Die tags-Zeile lässt sich auch als studium, gethsemane ohne Klammern schreiben, oder als #studium #gethsemane, oder als Strichliste in eigenen Zeilen darunter — alle vier werden gleich gelesen."),
   ("Eine Notiz pro Datei",
    "Jede .md-Datei wird zu einer Notiz. Mehrere Notizen in eine Datei zu packen und sie auftrennen zu lassen, geht nicht, denn nichts in einer Markdown-Datei markiert verlässlich, wo eine Notiz endet und die nächste beginnt — eine Überschrift auf halbem Weg kann eine zweite Notiz sein oder eine Zwischenüberschrift der ersten, und ein Fehlgriff würde dein Geschriebenes zerstreuen. Schreibe also eine Datei pro Notiz und wähle beim Import alle auf einmal aus, oder zippe den Ordner und nimm die .zip."),
   ("Formatierung, die heil ankommt",
    "Absätze, Zeilenumbrüche, Fettdruck, Kursivschrift und Aufzählungen kommen in JW Library als echte Formatierung an. Überschriften nach der ersten werden zu gewöhnlichen Absätzen. Alles, was Markdown ausdrücken kann und eine JW-Library-Notiz nicht — Tabellen, Bilder, Links, Codeblöcke — wird auf seinen Text reduziert, sodass die Worte überleben, auch wo das Layout nicht mitkommt."),
   ("Wenn du ohnehin in Obsidian schreibst",
    "Obsidian-Dateien sind bereits Markdown, und das Eigenschaften-Panel schreibt genau das hier beschriebene Front Matter: Füge eine Eigenschaft publication mit dem Wert Matthew 26:39 hinzu, und die Notiz landet dort. Obsidians eigene Eigenschaft tags wird als tags gelesen. Links in doppelten eckigen Klammern und eingebettete Notizen werden auf ihren Text reduziert, denn eine JW-Library-Notiz hat nichts, worauf sie zeigen könnte. Du kannst die .md-Dateien eines ganzen Ordners in einem Import auswählen oder den Ordner zippen und die .zip übergeben."),
   ("Wenn du ohnehin in Notion schreibst",
    "Notion kann Markdown exportieren: Seitenmenü öffnen, Exportieren wählen und „Markdown & CSV“ nehmen. Heraus kommt eine .zip, die der Import so annimmt, wie sie ist. Notion schreibt den Seitentitel als Überschrift und seine eigenen Eigenschaften als gewöhnliche Zeilen darunter, und Felder, die der Import nicht kennt, werden ignoriert statt als Fehler behandelt — um eine Notiz auf einen Vers zu setzen, ergänzt du also selbst eine publication-Zeile ganz oben in der exportierten Datei."),
   ("Dinge, die du nicht richtig treffen musst",
    "Großbuchstaben in den Feldnamen sind egal. Das Leerzeichen nach dem Doppelpunkt darf fehlen. Zusätzliche Leerzeichen und Tabulatoren werden ignoriert, ebenso Anführungszeichen um einen Wert und ein Kommentar hinter einem #. Windows-Zeilenenden sind kein Problem. Du kannst die ---Zeilen sogar ganz weglassen und die Datei direkt mit den Feldern beginnen, solange die allererste Zeile eines davon ist. Und wenn du einen Buchnamen falsch schreibst — Mathew —, sagt dir der Import, dass er das als Matthew 26:39 gelesen hat, und wartet darauf, dass du das Kästchen ankreuzt, statt allein zu entscheiden."),
   ("Was der Import deiner Bibliothek nicht antut",
    "Importieren fügt ausschließlich hinzu. Die Notizen, Markierungen, Lesezeichen und Tags, die schon in deiner Sicherung sind, bleiben unangetastet, und die Datei, die du lädst, wird nie verändert — am Ende lädst du eine neue .jwlibrary herunter und stellst diese wieder her. Eine Notiz, deren Titel, Text und Fundstelle mit etwas übereinstimmen, das schon in der Sicherung steht, wird übersprungen; dieselben Dateien zweimal zu importieren verdoppelt also nichts. Alles, was ein Import hinzufügt, ist ein einziger Schritt von Rückgängig, und importierte Notizen tragen den Tag Imported, damit du sie später finden, danach filtern oder sie als Gruppe entfernen kannst. Nichts davon verlässt dein Gerät."),
  ],
  "faq": [
   ("Muss ich vorher Markdown lernen?",
    "Nein. Eine Datei mit ganz normalen Sätzen ist bereits eine gültige Notiz. Markdown kommt nur ins Spiel, wenn du Fettdruck, Kursives oder Aufzählungspunkte willst, und selbst dann sind es zwei Sternchen um ein Wort für fett und ein Bindestrich am Zeilenanfang für einen Aufzählungspunkt."),
   ("Spielt der Dateiname eine Rolle?",
    "Nur wenn die Datei keinen eigenen Titel hat. Gibt es weder eine title:-Zeile noch eine Überschrift mit #, wird der Dateiname aufgeräumt und stattdessen verwendet: aus der-kelch-um-den-er-betete.md wird eine Notiz namens „der kelch um den er betete“. Ansonsten nenne die Datei, wie du magst."),
   ("Was, wenn ich sie versehentlich als .txt gespeichert habe?",
    "Benenne sie so um, dass sie auf .md endet, und importiere erneut — am Inhalt muss sich nichts ändern. Unter Windows musst du eventuell zuerst im Menü Ansicht des Explorers die Dateinamenerweiterungen einblenden, sonst bleibt dir die Endung verborgen."),
   ("Kann ich den Buchnamen in meiner Sprache schreiben?",
    "Derzeit nicht. Buchnamen werden auf Englisch erkannt, und genau das schreibt auch der Markdown-Export dieser Seite. Die Notiz selbst schreibst du in der Sprache, die du willst; nur die Referenzzeile braucht den englischen Namen. Wenn dir das nicht behagt, lass die Referenz weg und ordne die Notiz später von Hand zu."),
   ("Kann ich mehrere Notizen in eine Datei packen?",
    "Nein — jede Datei wird zu einer Notiz. Wähle bei einem Import beliebig viele Dateien aus, oder zippe den Ordner und nimm die .zip."),
   ("Verändert das die Notizen, die ich schon habe?",
    "Nein. Importieren fügt nur hinzu. Deine vorhandenen Notizen bleiben unangetastet, und die geladene Sicherung wird nie verändert: Am Ende lädst du eine neue Datei herunter und entscheidest, ob du sie wiederherstellst."),
   ("Was passiert, wenn ich die Referenzzeile weglasse?",
    "Die Notiz wird trotzdem importiert. Sie kommt als eigenständige Notiz in deiner Bibliothek an statt an eine Bibelstelle gehängt — und genau das will eine Notiz zu einem Vortrag, einem Gespräch oder einem eigenen Gedanken meistens ohnehin."),
  ],
}

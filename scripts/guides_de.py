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
        "Wenn du auf mehreren Geräten studierst — Handy im Königreichssaal, Tablet zu Hause — "
        "hat am Ende jedes Gerät eigene Notizen und Markierungen. Die eingebaute Sicherung "
        "und Wiederherstellung von JW Library kann sie nicht vereinen: Eine Sicherung "
        "wiederherzustellen ersetzt alles auf dem Gerät und löscht damit die Arbeit vom "
        "anderen.",
        "JW Sync löst das. Es liest zwei (oder mehr) .jwlibrary-Sicherungen und führt die "
        "Notizen, Markierungen, Lesezeichen und Schlagwörter aus allen zu einer neuen "
        "Sicherungsdatei zusammen. Die Zusammenführung läuft vollständig in deinem Browser — "
        "deine Dateien werden nie auf einen Server geladen, deine persönlichen Studiennotizen "
        "bleiben also privat.",
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
    ],
}

GUIDES_DE["sync-jw-library-multiple-devices"] = {
    "title": "JW Library zwischen mehreren Geräten synchron halten",
    "h1": "So hältst du JW Library auf mehreren Geräten synchron",
    "description": "JW Library hat keine eingebaute Synchronisierung zwischen Geräten. Hier "
                   "ist eine einfache, private Routine, mit der Notizen, Markierungen und "
                   "Lesezeichen auf Handy, Tablet und Computer gleich bleiben.",
    "intro": [
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
    ],
    "faq": [
        ("Läuft JW Sync im Hintergrund?",
         "Nein — es ist eine Webseite, kein installierter Dienst. Nichts durchsucht deine "
         "Geräte. Du startest die Routine, wann du willst; die optionale Erinnerung ist nur "
         "eine Benachrichtigung."),
        ("Kann ich drei oder mehr Geräte synchronisieren?",
         "Ja. Sichere jedes, lade alle Dateien, führe einmal zusammen und stelle die "
         "zusammengeführte Datei überall wieder her."),
    ],
}

GUIDES_DE["transfer-jw-library-notes-new-phone"] = {
    "title": "JW-Library-Notizen auf ein neues Handy übertragen",
    "h1": "So überträgst du deine JW-Library-Notizen auf ein neues Handy",
    "description": "Schritt für Schritt: Bring alle deine JW-Library-Notizen, Markierungen, "
                   "Lesezeichen und Schlagwörter mit einer .jwlibrary-Sicherung auf ein neues "
                   "Handy — und so führst du zusammen, wenn du auf dem neuen Handy schon "
                   "Notizen gemacht hast.",
    "intro": [
        "Umzugs-Assistenten für Handys übertragen Apps und Fotos, aber die persönlichen "
        "Studiendaten von JW Library bringen sie nicht zuverlässig mit. Der verlässliche Weg, "
        "deine Notizen, Markierungen, Lesezeichen und Schlagwörter aufs neue Handy zu holen, "
        "ist die Sicherungsdatei von JW Library selbst — ein paar Minuten, und es "
        "funktioniert plattformübergreifend.",
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
    ],
    "faq": [
        ("Werden damit auch meine heruntergeladenen Publikationen übertragen?",
         "Die Sicherung enthält deine persönlichen Studiendaten — Notizen, Markierungen, "
         "Lesezeichen, Schlagwörter und Wiedergabelisten. Publikationen werden auf dem neuen "
         "Handy einfach neu heruntergeladen."),
        ("Macht es etwas aus, wenn die Handys verschiedene Android-Versionen haben?",
         "Nein. Das .jwlibrary-Format ist überall gleich, auch zwischen Android-Versionen und "
         "zwischen Android und iPhone."),
    ],
}

GUIDES_DE["jw-library-android-to-iphone"] = {
    "title": "JW Library von Android aufs iPhone umziehen (mit allen Notizen)",
    "h1": "JW Library von Android aufs iPhone oder iPad umziehen — ohne eine Notiz zu verlieren",
    "description": "Das .jwlibrary-Sicherungsformat ist unter Android und iOS identisch. So "
                   "bringst du Notizen, Markierungen und Lesezeichen plattformübergreifend "
                   "mit — und so führst du zusammen, wenn beide Geräte Notizen haben.",
    "intro": [
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
    ],
    "faq": [
        ("Brauche ich dafür einen Computer?",
         "Nein. Der ganze Umzug lässt sich von Handy zu Handy per E-Mail oder Cloud-Speicher "
         "erledigen."),
        ("Bleiben meine Markierungsfarben erhalten?",
         "Ja — Markierungen behalten ihre Farben, Notizen ihre Schlagwörter und Lesezeichen "
         "ihre Stellen."),
    ],
}

GUIDES_DE["backup-jw-library"] = {
    "title": "JW Library richtig sichern",
    "h1": "So sicherst du JW Library richtig",
    "description": "Eine 30-Sekunden-Sicherungsroutine, die Jahre an JW-Library-Studiennotizen, "
                   "Markierungen und Lesezeichen schützt — und der typische Fehler, der viele "
                   "kalt erwischt.",
    "intro": [
        "Eine ordentliche JW-Library-Sicherung dauert eine halbe Minute und schützt Jahre "
        "angesammelten Studiums. Die meisten Datenverlust-Geschichten fangen gleich an: Es "
        "gab keine aktuelle .jwlibrary-Datei, als das Handy verloren ging, zurückgesetzt oder "
        "ersetzt wurde.",
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
    ],
    "faq": [
        ("Wie groß ist eine Sicherungsdatei?",
         "Meist ein paar Megabyte, selbst bei sehr großen Bibliotheken — klein genug für den "
         "E-Mail-Anhang."),
        ("Verändert das Erstellen einer Sicherung etwas auf meinem Handy?",
         "Nein. Es schreibt nur die Datei; deine Bibliothek bleibt unangetastet."),
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
    ],
    "faq": [
        ("Werden meine Daten für die Prüfung hochgeladen?",
         "Nein. Prüfung, Reparaturen und Export laufen alle lokal im Browser."),
        ("Kann er in JW Library gelöschte Notizen wiederherstellen?",
         "Nein — er repariert die Dateistruktur. Notizen, die vor dem Erstellen der Sicherung "
         "in der App gelöscht wurden, sind gar nicht erst in der Datei."),
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
    ],
    "faq": [
        ("Kann ich eine .jwlibrary-Datei in Excel oder im Editor öffnen?",
         "Nicht sinnvoll — es ist eine Datenbank, keine Tabelle und keine Textdatei. Öffne sie "
         "in JW Sync zum Lesen, oder exportiere deine Notizen aus dem Studien-Explorer als "
         "Markdown/Text."),
        ("Ist es sicher, meine Sicherung im Browser zu öffnen?",
         "Ja. JW Sync liest die Datei lokal in deinem Browser-Tab; nichts wird an einen Server "
         "geschickt, und deine Originaldatei wird nie verändert."),
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
        "Ein Handy zu verlieren ist stressig genug, auch ohne die Sorge, Jahre an "
        "Studiennotizen mitverloren zu haben. Ob du sie zurückbekommst, hängt an einer Frage: "
        "Gibt es irgendwo außerhalb dieses Handys eine .jwlibrary-Sicherung?",
        "Diese Anleitung hilft dir, jede Sicherung zu finden, die du haben könntest — auch "
        "solche, die du längst vergessen hast — und daraus wieder eine vollständige "
        "JW-Library-Bibliothek auf deinem neuen Gerät zu machen.",
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
    ],
    "faq": [
        ("Verändert der Export meine JW-Library-Notizen?",
         "Nein. Der Export liest eine Kopie deiner Sicherung im Browser; deine Originaldatei "
         "und deine App bleiben unangetastet."),
        ("Kann ich alles auf einmal exportieren?",
         "Ja — setz die Filter zurück, um die ganze Bibliothek auszuwählen, oder grenze erst "
         "ein, um nur einen Teil zu exportieren."),
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

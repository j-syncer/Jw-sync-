# -*- coding: utf-8 -*-
"""Polish copy for the static guide pages, keyed by slug.

Field names mirror build_guides.GUIDES. Anything left out falls back to
English. `group` and `related` are deliberately not translated — the first is
looked up through CHROME["pl"]["groups"], the second is a list of slugs.

Product names stay in Latin script (JW Library, JW Sync, .jwlibrary, Google
Drive, iCloud), matching how they appear in the file system and in the app.

Glossary settled on for all 37 guides:

  backup              kopia zapasowa
  to merge / merge    scalić / scalanie
  notes               notatki
  highlights          wyróżnienia
  bookmarks           zakładki
  tags                etykiety
  device              urządzenie
  to restore          przywrócić
  Personal Study      Studium osobiste
  Backup and Restore  Kopia zapasowa i przywracanie
  browser             przeglądarka
  database            baza danych
  Conflict Reviewer   przegląd konfliktów
  duplicate           duplikat
  publication         publikacja
  meeting             zebranie
  convention          kongres
  talk                przemówienie
  Hebrew Scriptures   Pisma Hebrajskie
  Greek Scriptures    Pisma Greckie
"""

GUIDES_PL = {

 "merge-jw-library-backups": {
  "title": "Jak scalić kopie zapasowe JW Library z dwóch urządzeń",
  "h1": "Jak scalić kopie zapasowe JW Library z dwóch urządzeń",
  "description": "Połącz notatki, wyróżnienia, zakładki i etykiety z dwóch lub więcej kopii zapasowych JW Library w jeden plik .jwlibrary — bezpłatnie, prywatnie, w Twojej przeglądarce.",
  "intro": [
   "Studiowałeś Strażnicę na telefonie, a inny artykuł na tablecie. Teraz każde urządzenie ma pracę, której nie ma to drugie, a JW Library nie potrafi ich pogodzić: przywracanie jest tam pełną podmianą, a nie scaleniem, więc którąkolwiek kopię przywrócisz, skasuje ona studium z drugiego urządzenia. Samą aplikacją nie da się zachować obu.",
   "Po to jest ta strona. Czyta dwa (lub więcej) pliki .jwlibrary i łączy notatki, zakreślenia, zakładki i etykiety z nich wszystkich w jedną nową kopię zapasową — więc niczego nie trzeba wybierać kosztem czegoś innego. Scalanie odbywa się w całości w twojej przeglądarce; twoje pliki nigdy nie trafiają na żaden serwer, więc twoje osobiste notatki pozostają prywatne.",
   "Dlatego też ten nawyk jest zapobiegawczy, a nie naprawczy: gdy scalasz co jakiś czas, nie musisz już pamiętać o przywracaniu, zanim zaczniesz studiować gdzie indziej. Studiuj tam, gdzie jesteś, scalaj, kiedy ci wygodnie, a każde urządzenie nadrobi zaległości.",
  ],
  "steps": [
   ("Utwórz kopię zapasową na każdym urządzeniu", "W JW Library otwórz Studium osobiste, dotknij menu z trzema kropkami, wybierz Kopia zapasowa i przywracanie, a potem Utwórz kopię zapasową. Zrób to na każdym urządzeniu. Każde utworzy plik .jwlibrary."),
   ("Otwórz JW Sync", "Wejdź na jwsync.org w dowolnej przeglądarce — na telefonie, tablecie lub komputerze. Nic nie trzeba instalować."),
   ("Wczytaj oba pliki kopii zapasowych", "Przeciągnij (albo wybierz) pliki .jwlibrary. JW Sync odczytuje je lokalnie na Twoim urządzeniu."),
   ("Przejrzyj podgląd przed scalaniem", "Zanim cokolwiek zostanie zapisane, podgląd pokaże dokładnie, co zostanie połączone. Jeśli tę samą notatkę edytowano inaczej na każdym urządzeniu, przegląd konfliktów pokaże obie wersje obok siebie z porównaniem słowo po słowie, abyś wybrał, którą zachować — albo pozwolił funkcji „Zaproponuj najlepszą” wybrać za Ciebie."),
   ("Pobierz scalony plik i przywróć go", "Pobierz scalony plik .jwlibrary, a potem przywróć go na każdym urządzeniu przez Kopia zapasowa i przywracanie → Przywróć. Oba urządzenia mają teraz kompletną, połączoną bibliotekę."),
  ],
  "sections": [
   ("Co jest scalane?",
    "Notatki, wyróżnienia, zakładki, etykiety i powiązania między nimi. Duplikaty są wykrywane automatycznie, więc przywrócenie scalonego pliku nigdy niczego nie podwaja. Kopie zapasowe z Androida, iPhone'a, iPada i aplikacji dla Windows mają ten sam format i swobodnie się ze sobą scalają."),
   ("Czy to bezpieczne?",
    "Scalanie nigdy nie zmienia Twoich pierwotnych plików — tworzy zupełnie nową kopię zapasową, więc oryginały pozostają nietknięte jako zabezpieczenie. A ponieważ wszystko działa po stronie przeglądarki, żadne dane nie opuszczają Twojego urządzenia."),
   ("Co naprawdę jest w pliku .jwlibrary",
    "Kopia zapasowa .jwlibrary to archiwum ZIP. Zmień nazwę kopii na .zip, otwórz ją, a znajdziesz userData.db — bazę danych SQLite zawierającą każdą notatkę, wyróżnienie, zakładkę i etykietę, jaką kiedykolwiek utworzyłeś — obok małego pliku manifest.json opisującego kopię. Twoje notatki są w tabeli Note, wyróżnienia w UserMark i BlockRange, zakładki w Bookmark, a etykiety w Tag i TagMap. Zrozumienie, że kopia zapasowa jest kompletną bazą danych, a nie zbiorem osobnych plików, wyjaśnia wszystko inne na tej stronie: dlatego przywracanie działa na zasadzie wszystko albo nic i dlatego dwie kopie w ogóle da się połączyć."),
   ("Dlaczego przywracanie w samym JW Library nie potrafi scalać",
    "Podczas przywracania JW Library nie odczytuje Twojej kopii zapasowej, aby dodać brakujące elementy do tego, co już jest na urządzeniu. Zastępuje bazę danych urządzenia tą z pliku. To celowe i bezpieczne rozwiązanie — gwarantuje, że urządzenie znajdzie się w znanym stanie — ale oznacza, że przywrócenie kopii z tabletu na telefon usuwa wszystko, co telefon miał, a czego nie miał tablet. Nie da się tego zmienić żadnym ustawieniem i właśnie tę lukę wypełnia scalanie: tworzy jeden plik zawierający już pracę z obu urządzeń, więc każde urządzenie, na którym go przywrócisz, będzie kompletne."),
   ("Jak wykrywane są duplikaty",
    "Każda notatka, wyróżnienie i zakładka ma GUID — unikatowy identyfikator nadawany przy tworzeniu i zachowywany we wszystkich późniejszych kopiach. Gdy ten sam element pojawia się w dwóch kopiach, oba egzemplarze mają ten sam GUID, więc jest rozpoznawany jako jeden element i zachowywany raz. Dlatego dwukrotne scalenie tej samej pary plików niczego nie podwaja i dlatego możesz bezpiecznie scalać co tydzień. Tam, gdzie GUID-y są zgodne, a tekst się różni — ta sama notatka edytowana na obu urządzeniach — elementu nie da się rozstrzygnąć automatycznie, więc pojawia się w przeglądzie konfliktów z porównaniem słowo po słowie, abyś wybrał Ty."),
   ("Czego nie ma w kopii zapasowej",
    "Kopia zapasowa zawiera wyłącznie Twoje osobiste dane studium. Pobrane publikacje, przekłady Biblii, filmy i nagrania nie są w niej uwzględnione, dlatego pliki kopii są małe — zwykle kilka megabajtów nawet przy bibliotece budowanej latami. Po przywróceniu na nowym urządzeniu może być konieczne ponowne pobranie publikacji, które regularnie czytasz. Nic z tego, co napisałeś, na tym nie ucierpi; notatki są powiązane z publikacjami przez odwołania, więc wracają na miejsce, gdy tylko publikacja się pojawi."),
   ("Jeśli scalanie pokazuje 0 dodanych notatek",
    "Prawie zawsze jest to poprawny wynik, a nie błąd. Oznacza, że każda notatka z drugiego pliku już istniała w pierwszym — częste, gdy scalałeś niedawno albo gdy jedno urządzenie po prostu jest w tyle za drugim. Sprawdź podgląd przed scalaniem: pokazuje, co wnosi każdy plik, zanim cokolwiek zostanie zapisane. Jeśli spodziewałeś się nowych elementów, a nie widzisz żadnego, upewnij się, że utworzyłeś kopię urządzenia po tej sesji studium, której szukasz — kopia zawsze zawiera tylko to, co istniało w chwili jej utworzenia."),
  ],
  "faq": [
   ("Czy mogę scalić więcej niż dwie kopie?", "Tak — wczytaj tyle plików .jwlibrary, ile masz urządzeń. Wszystkie zostaną połączone w jedną scaloną kopię zapasową."),
   ("Czy scalanie utworzy zduplikowane notatki?", "Nie. Identyczne notatki, wyróżnienia i zakładki są wykrywane i zachowywane raz. Naprawdę różne wersje tej samej notatki trafiają do przeglądu konfliktów, abyś zdecydował Ty."),
   ("Czy działa to między Androidem a iPhone'em?", "Tak. Format .jwlibrary jest identyczny na Androidzie, iOS, iPadOS i Windows, więc kopie z różnych platform scalają się bez żadnej konwersji."),
   ("Czy trzeba scalać w określonej kolejności?",
    "Nie. Scalanie nie zależy od kolejności — ten sam zestaw plików daje ten sam wynik, niezależnie od tego, który wczytasz pierwszy. Kolejność wpływa jedynie na to, który plik jest traktowany jako podstawa w podsumowaniu podglądu."),
   ("Co dzieje się z etykietami, które są tylko na jednym urządzeniu?",
    "Zostają przeniesione w całości, wraz z powiązaniami między etykietami a notatkami, które oznaczają. Jeśli oba urządzenia mają etykietę o tej samej nazwie, jest ona traktowana jako jedna, a notatki z obu zostają do niej dołączone."),
   ("Jak duży jest scalony plik?",
    "Mniej więcej tyle, co oba oryginały razem, minus duplikaty — zwykle wciąż tylko kilka megabajtów. Kopie zapasowe nie zawierają multimediów publikacji, więc nawet obficie opisana biblioteka pozostaje na tyle mała, że można ją wysłać e-mailem."),
   ("Czy mogę cofnąć przywracanie?",
    "Nie z poziomu JW Library — dlatego zachowywanie pierwotnych kopii ma znaczenie. Scalanie nigdy nie zmienia wczytywanych plików, więc Twoje kopie sprzed scalania pozostają dokładnie takie, jakie były, i można je przywrócić, jeśli zechcesz się wycofać."),
  ],
 },


 "sync-jw-library-multiple-devices": {
  "title": "Jak synchronizować JW Library między kilkoma urządzeniami",
  "h1": "Jak utrzymać JW Library w synchronizacji między kilkoma urządzeniami",
  "description": "JW Library nie ma wbudowanej synchronizacji między urządzeniami. Oto prosta i prywatna procedura, dzięki której notatki, wyróżnienia i zakładki pozostaną identyczne na telefonie, tablecie i komputerze.",
  "intro": [
   "Większość osób studiujących na dwóch urządzeniach odkrywa ten problem tak samo: notatek napisanych na tablecie nie ma na telefonie, a przywrócenie kopii jednego urządzenia na drugie skasowałoby to, co tam było. JW Library nie oferuje synchronizacji, a jego przywracanie celowo działa na zasadzie wszystko albo nic, więc utrzymanie zgodności urządzeń wymaga procedury, a nie ustawienia.",
   "JW Library nie synchronizuje osobistych danych studium między urządzeniami — nie ma konta, które przenosiłoby Twoje notatki z telefonu na tablet. Oficjalnym mechanizmem jest kopia zapasowa i przywracanie, a przywracanie całkowicie zastępuje dane urządzenia. Jak więc utrzymać dwa czy trzy urządzenia identyczne, niczego nie tracąc?",
   "Odpowiedzią jest krótka procedura „scal i przywróć”. Wykonywana co tydzień lub co miesiąc zajmuje około dwóch minut i sprawia, że każde urządzenie ma Twoją kompletną bibliotekę.",
  ],
  "steps": [
   ("Utwórz kopię zapasową każdego urządzenia", "Na każdym urządzeniu: Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Otrzymasz po jednym pliku .jwlibrary na urządzenie."),
   ("Scal kopie na jwsync.org", "Wczytaj wszystkie pliki. JW Sync połączy notatki, wyróżnienia, zakładki i etykiety z każdego urządzenia w jeden scalony plik .jwlibrary — lokalnie w Twojej przeglądarce, bez wysyłania czegokolwiek."),
   ("Przywróć scalony plik na każdym urządzeniu", "Kopia zapasowa i przywracanie → Przywróć, wybierz scalony plik. Każde urządzenie jest teraz identyczne i kompletne."),
   ("Pozwól, aby JW Sync Ci przypominał", "Włącz przypomnienie o synchronizacji (co tydzień lub co miesiąc) w JW Sync, a podpowie Ci, kiedy powtórzyć procedurę. Zapamiętuje też Twoje zapisane urządzenia, więc każdy kolejny cykl jest szybszy."),
  ],
  "sections": [
   ("Dlaczego nie wystarczy przywrócić najnowszej kopii?",
    "Bo „najnowsza” odzwierciedla tylko jedno urządzenie. Jeśli w tym samym tygodniu robiłeś notatki z zebrania na telefonie, a notatki do studium na tablecie, każda kopia ma treść, której brakuje drugiej. Przywrócenie którejkolwiek z nich na drugą traci połowę Twojej pracy. To właśnie wcześniejsze scalenie czyni tę procedurę bezpieczną."),
   ("Jak często synchronizować?",
    "Dopasuj to do sposobu, w jaki studiujesz. Dwa aktywne urządzenia używane codziennie: co tydzień jest wygodne. Tablet wyjmowany tylko na zebrania: co miesiąc w zupełności wystarczy. Kosztem dłuższego czekania jest jedynie to, że scalanie ma więcej do połączenia — między cyklami nic nie ginie."),
   ("Dlaczego nie ma prawdziwej synchronizacji",
    "JW Library nie ma konta, które przenosiłoby osobiste dane studium między urządzeniami. Notatki, wyróżnienia i zakładki żyją w bazie danych na każdym urządzeniu i tam pozostają. Jedynym oficjalnym mechanizmem ich przenoszenia jest kopia zapasowa i przywracanie, a przywracanie całkowicie zastępuje dane urządzenia docelowego, zamiast je łączyć. Dlatego dwa niezależnie używane urządzenia rozchodzą się na stałe, o ile coś ich nie scali — i o to właśnie chodzi w poniższej procedurze."),
   ("Utrzymywanie jednego pliku głównego",
    "Procedura działa najlepiej, gdy traktujesz jeden scalony plik jako bieżący główny. W każdym cyklu twórz kopie wszystkich urządzeń, scalaj je i przywracaj wynik wszędzie. Scalony plik staje się wtedy głównym dla kolejnego cyklu. Przechowywanie datowanych plików głównych w chmurze daje Ci jednocześnie mechanizm synchronizacji i bieżące archiwum — jeśli coś przypadkiem usuniesz, wcześniejszy plik główny wciąż to zawiera."),
   ("Co, jeśli na jakiś czas pominiesz urządzenie",
    "Nic nie ginie. Urządzenie pominięte w kilku cyklach ma po prostu starsze dane; gdy w końcu je uwzględnisz, jego notatki scalą się z resztą, a identyczne elementy zostaną dopasowane po GUID, a nie zduplikowane. Jedyna sytuacja wymagająca decyzji to ta sama notatka edytowana na dwóch urządzeniach od ostatniego scalania — i pojawi się ona w przeglądzie konfliktów z obiema wersjami obok siebie."),
   ("Jak często to wystarczająco często",
    "Dopasuj to do ilości pracy, którą niechętnie wykonywałbyś ponownie. Co tydzień pasuje osobom studiującym na dwóch urządzeniach przez większość dni; co miesiąc w zupełności wystarczy, jeśli jedno urządzenie jest używane sporadycznie. Najważniejsze to zrobić to przed czymkolwiek nieodwracalnym — wymianą telefonu, resetem, naprawą — bo właśnie wtedy rozbieżność zamienia się w stratę."),
   ("Telefon, tablet i aplikacja dla Windows razem",
    "Procedurze jest obojętne, ile urządzeń bierze udział i co na nich działa. Utwórz kopię każdego, scal wszystkie za jednym razem, przywróć scalony plik wszędzie. Komputer z Windows używany do przygotowań i telefon używany na zebraniach łączą się dokładnie tak samo jak dwa telefony, bo każda platforma zapisuje ten sam format kopii."),
   ("Jak ograniczyć konflikty, zanim wystąpią",
    "Konflikty powstają tylko wtedy, gdy ta sama notatka jest edytowana na dwóch urządzeniach między scaleniami. W praktyce zdarza się to rzadko, a jeszcze rzadziej, gdy piszesz na jednym urządzeniu naraz — czytaj gdziekolwiek, ale pisz tam, gdzie zwykle piszesz. Częstsze scalanie również skraca okno, w którym może powstać rozbieżność, i jest to lepsze rozwiązanie niż próba zapamiętania, na którym urządzeniu jest najnowsza wersja."),
   ("Gdzie ta procedura się opłaca",
    "Wartością scalonych urządzeń nie jest porządek, ale to, że każde urządzenie staje się pełną kopią zapasową Twojej biblioteki studium. Zgub albo zniszcz którekolwiek z nich, a pozostałe wciąż mają wszystko — najgorszy scenariusz zamienia się z utraty lat notatek w drobną niedogodność. To mocniejsza pozycja niż jakikolwiek nawyk tworzenia kopii pojedynczego urządzenia."),
  ],
  "faq": [
   ("Czy JW Sync działa w tle?", "Nie — to strona internetowa, a nie zainstalowana usługa. Nic nie skanuje Twoich urządzeń. Procedurę uruchamiasz, kiedy zechcesz; opcjonalne przypomnienie to tylko powiadomienie."),
   ("Czy mogę synchronizować trzy lub więcej urządzeń?", "Tak. Utwórz kopię każdego, wczytaj wszystkie pliki, scal raz i przywróć scalony plik wszędzie."),
   ("Co, jeśli edytowałem tę samą notatkę na dwóch urządzeniach?", "Obie wersje zostają zachowane, dopóki nie wybierzesz. Przegląd konfliktów pokaże je obok siebie z porównaniem słowo po słowie albo zaproponuje pełniejszą wersję."),
   ("Czy kolejność przywracania ma znaczenie?", "Nie. Gdy scalony plik już powstanie, przywrócenie go na każdym urządzeniu doprowadzi wszystkie do tego samego kompletnego stanu, w dowolnej wygodnej kolejności."),
   ("Czy mogę synchronizować trzy lub więcej urządzeń?", "Tak. Utwórz kopię każdego i wczytaj je wszystkie do tego samego scalania — nie ma limitu związanego z liczbą urządzeń."),
   ("Czy da się to zautomatyzować?", "Nie w pełni, bo JW Library nie ma API synchronizacji, a krok przywracania odbywa się w aplikacji. Ręczna procedura zajmuje około dwóch minut, gdy się do niej przyzwyczaisz."),
   ("Czy muszę scalać, jeśli na drugim urządzeniu tylko czytam?", "Jeśli nigdy nic tam nie zapisujesz, wystarczy okresowo przywracać na nie kopię, aby miało Twoje aktualne notatki."),
  ],
 },

 "transfer-jw-library-notes-new-phone": {
  "title": "Jak przenieść notatki JW Library na nowy telefon",
  "h1": "Jak przenieść notatki JW Library na nowy telefon",
  "description": "Przeniesienie notatek JW Library na nowy telefon to kopia zapasowa i przywrócenie, a aplikacja robi to w jakieś dwie minuty. Oto kroki — a przy nich jedyny przypadek, z którym sobie nie poradzi: gdy nowy telefon ma już własne notatki.",
  "intro": [
   "To łatwiejsze, niż się ludziom wydaje, i nie potrzebujesz do tego żadnego dodatkowego narzędzia. JW Library ma wbudowane tworzenie i przywracanie kopii zapasowej, które przenosi na nowy telefon każdą notatkę, każde zakreślenie, zakładkę i etykietę — również między Androidem a iPhonem. Zrób to, dopóki stare urządzenie jeszcze działa, a całość zajmie kilka minut.",
   "Jedyna część, którą trzeba wykonać świadomie, to samo przeniesienie: narzędzia do migracji z telefonu na telefon przenoszą aplikacje i zdjęcia, ale pomijają osobiste dane studium JW Library, więc utwórz plik kopii zapasowej, zamiast zakładać, że pojedzie sam.",
   "Jest dokładnie jedna sytuacja, z którą aplikacja sobie nie poradzi, i warto o niej wiedzieć przed rozpoczęciem: jeśli już studiowałeś na nowym telefonie, przywrócenie kopii ze starego skasuje tę pracę, bo przywracanie podmienia całą bibliotekę urządzenia. Jeśli to twój przypadek, potrzebujesz sekcji o scalaniu poniżej.",
  ],
  "steps": [
   ("Utwórz kopię zapasową na starym telefonie", "Otwórz JW Library → Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Zapisze to plik .jwlibrary ze wszystkimi Twoimi danymi studium."),
   ("Przenieś plik na nowy telefon", "Wyślij go sobie e-mailem albo użyj Google Drive, iCloud, AirDrop czy kabla USB. Plik jest mały — zwykle kilka megabajtów."),
   ("Przywróć na nowym telefonie", "Zainstaluj JW Library, a potem Studium osobiste → Kopia zapasowa i przywracanie → Przywróć i wybierz plik .jwlibrary. Pojawią się wszystkie notatki, wyróżnienia, zakładki i etykiety."),
  ],
  "sections": [
   ("Masz już notatki na nowym telefonie? Scalaj, zamiast nadpisywać",
    "Przywracanie zastępuje to, co jest na urządzeniu. Jeśli od jakiegoś czasu używasz nowego telefonu i ma on własne notatki, nie przywracaj na nie — utwórz kopię również nowego telefonu, potem scal starą i nową kopię w jeden plik na jwsync.org (bezpłatnie, w przeglądarce, bez wysyłania czegokolwiek) i przywróć scalony plik. Zachowasz oba zestawy notatek."),
   ("Częsta pułapka na iPhonie",
    "Jeśli plik kopii dotrze na iPhone'a z nazwą zmienioną na .zip, przed przywracaniem zmień ją z powrotem na .jwlibrary — treść jest w porządku, po drodze zmieniło się tylko rozszerzenie."),
   ("Zrób to, zanim stary telefon zostanie wyczyszczony lub oddany",
    "Kopię trzeba utworzyć, gdy stary telefon jeszcze działa i wciąż ma zainstalowane JW Library. Gdy urządzenie zostanie zresetowane, oddane w rozliczeniu lub przekazane dalej, notatki znikną razem z nim — JW Library nie przechowuje kopii osobistych danych studium w chmurze, a kopia na poziomie telefonu, jak Google One czy kopia urządzenia w iCloud, zwykle przywraca starszą migawkę danych aplikacji albo wcale. Najpierw utwórz plik .jwlibrary, przenieś go w bezpieczne miejsce i upewnij się, że go widzisz, zanim cokolwiek skasujesz."),
   ("Jak wydobyć plik ze starego telefonu",
    "Na Androidzie plik zapisuje się w wybranym folderze — zwykle Pobrane albo Dokumenty — i możesz go przenieść dowolnym menedżerem plików, wysłać sobie e-mailem lub wrzucić do chmury. Na iPhonie arkusz udostępniania pojawia się od razu po utworzeniu kopii: zapisz ją w Plikach, wyślij przez AirDrop na nowy telefon albo wyślij sobie. Sposób przenoszenia nie ma znaczenia i nie może uszkodzić pliku; .jwlibrary to pojedyncze archiwum, które albo dociera w całości, albo wcale."),
   ("Dlaczego aplikacja do przenoszenia danych nie wystarczy",
    "Narzędzia takie jak Smart Switch, Move to iOS czy przywracanie z iCloud kopiują aplikacje i dane systemowe, ale prywatne bazy danych aplikacji są często pomijane, przywracane częściowo albo z wcześniejszego momentu. Ludzie regularnie odkrywają tę lukę tygodnie później, gdy starego telefonu już nie ma. Traktuj plik .jwlibrary jako kopię rozstrzygającą, a przeniesienie telefonu jako udogodnienie — jeśli przeniesienie przypadkiem zabierze Twoje notatki, przywrócenie własnej kopii na wierzch nic nie kosztuje."),
   ("Sprawdź, czy przeniesienie naprawdę się udało",
    "Po przywróceniu na nowym telefonie otwórz dwie–trzy publikacje, które ostatnio opisywałeś, i sprawdź, czy notatki, kolory wyróżnień i zakładki są na miejscu. Szybszą kontrolą jest otwarcie samego pliku kopii w przeglądarce, zanim wyczyścisz stare urządzenie — zobaczysz każdą notatkę, wyróżnienie i zakładkę, jakie zawiera, więc będziesz wiedzieć, co powinno się pojawić. Stary telefon czyść dopiero po sprawdzeniu nowego."),
   ("Przejście na tablet lub komputer w tym samym czasie",
    "Ten sam plik działa wszędzie. Jeśli konfigurujesz nowy telefon i tablet razem, przywróć identyczny plik .jwlibrary na obu, a zaczną od tego samego stanu. Od tej chwili znów będą się rozchodzić, bo będziesz studiować na każdym, więc warto już teraz zdecydować, czy będziesz je okresowo scalać, czy potraktujesz jedno jako to najważniejsze."),
   ("Jeśli nowy telefon ma już notatki",
    "Zdarza się to, gdy używasz nowego urządzenia przez tydzień, zanim zabierzesz się za przeniesienie. Zwykłe przywrócenie zastąpiłoby tę pracę danymi starego telefonu. Najpierw utwórz kopię nowego telefonu, scal ten plik z kopią starego i przywróć scalony wynik — oba zestawy notatek trafią do jednej biblioteki, zamiast jeden nadpisać drugi."),
   ("Co zrobić, gdy nowy telefon już działa",
    "Sprawdź, zanim czegokolwiek się pozbędziesz. Otwórz na nowym telefonie kilka publikacji, które ostatnio opisywałeś, i upewnij się, że notatki, kolory i zakładki są na miejscu, a potem wyczyść lub oddaj stare urządzenie — w tej kolejności, nigdy odwrotnie. Gdy się już urządzisz, umieść kopię gdzieś poza telefonem, bo sytuacja, która przywiodła Cię na tę stronę, powtórzy się przy kolejnej wymianie."),
  ],
  "faq": [
   ("Czy przeniesie to również moje pobrane publikacje?", "Kopia zawiera Twoje osobiste dane studium — notatki, wyróżnienia, zakładki, etykiety i playlisty. Publikacje po prostu pobiorą się na nowym telefonie ponownie."),
   ("Czy ma znaczenie, że telefony mają różne wersje Androida?", "Nie. Format .jwlibrary jest wszędzie taki sam, również między wersjami Androida oraz między Androidem a iPhone'em."),
   ("Czy mogę przenieść notatki, jeśli starego telefonu już nie mam?", "Tylko jeśli gdzieś istnieje kopia .jwlibrary — w Plikach, Pobranych, w mailu do samego siebie albo w chmurze. Bez niej nie ma z czego przywracać, bo osobiste dane studium są przechowywane wyłącznie na urządzeniu."),
   ("Czy oba telefony muszą mieć tę samą wersję JW Library?", "Nie muszą być identyczne, ale przed przywracaniem zaktualizuj nowy telefon do bieżącej wersji. Kopia utworzona przez nowszą wersję może używać nowszego schematu bazy danych, którego starsza aplikacja nie rozumie."),
   ("Czy będę musiał ponownie pobrać publikacje?", "Zwykle tak — multimedia publikacji nie są częścią kopii. Twoje notatki wracają na miejsce przy każdej publikacji, gdy tylko zostanie pobrana, więc nic z napisanego w międzyczasie nie ginie."),
   ("Ile trwa cały proces?", "Kilka minut. Utworzenie kopii zajmuje sekundy, przeniesienie pliku zależy od metody, a przywracanie jest szybkie. Najdłużej trwa ponowne pobieranie publikacji, które może odbywać się w tle."),
   ("Czy da się to zrobić bez Wi-Fi?", "Samo przeniesienie tak, przez AirDrop albo kabel. Ponowne pobranie publikacji na nowym urządzeniu wymaga połączenia."),
  ],
 },


 "jw-library-android-to-iphone": {
  "title": "Przeniesienie JW Library z Androida na iPhone'a (z zachowaniem notatek)",
  "h1": "Przeniesienie JW Library z Androida na iPhone'a lub iPada — z zachowaniem każdej notatki",
  "description": "Format kopii zapasowej .jwlibrary jest identyczny na Androidzie i iOS. Jak przenieść notatki, wyróżnienia i zakładki między platformami — oraz jak scalić, gdy notatki są na obu urządzeniach.",
  "intro": [
   "Przejście między Androidem a iPhone'em wydaje się przypadkiem najtrudniejszym, a jest najłatwiejszym. JW Library zapisuje ten sam format kopii zapasowej na każdej platformie, na której działa, więc przeniesienie biblioteki studium z Androida na iOS to ta sama operacja co przeniesienie między dwoma telefonami z Androidem — bez konwersji, bez wybierania formatu eksportu, bez strat.",
   "Zmiana platformy to moment, w którym ludzie boją się utraty lat notatek — aplikacje do przenoszenia z Androida na iPhone'a całkowicie pomijają dane JW Library. Dobra wiadomość: format kopii zapasowej JW Library jest identyczny na Androidzie, iPhonie, iPadzie i Windows, więc przejście między platformami to zwykła kopia, przeniesienie pliku i przywrócenie.",
  ],
  "steps": [
   ("Utwórz kopię na telefonie z Androidem", "JW Library → Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Zapisz plik .jwlibrary."),
   ("Wyślij plik na iPhone'a lub iPada", "E-mail, Google Drive, iCloud Drive — cokolwiek, co przenosi plik. Jeśli iOS zmieni po drodze nazwę na .zip, zmień ją z powrotem na .jwlibrary."),
   ("Przywróć na nowym urządzeniu", "Zainstaluj JW Library, zaloguj się, a potem Kopia zapasowa i przywracanie → Przywróć i wybierz plik. Notatki, wyróżnienia, zakładki, etykiety i playlisty — wszystko dociera."),
  ],
  "sections": [
   ("Jeśli iPhone ma już notatki",
    "Przywracanie zastępuje dane urządzenia. Gdy nowe urządzenie ma już własne notatki, utwórz kopię także z niego i najpierw scal obie kopie w jeden plik na jwsync.org — scalanie łączy obie biblioteki w Twojej przeglądarce, niczego nie wysyłając — a dopiero potem przywróć scalony plik. Żadna ze stron niczego nie traci."),
   ("Te same kroki działają w każdą stronę",
    "Z iPhone'a na Androida, z Androida na Androida, dodanie iPada jako drugiego urządzenia do studium czy przejście na aplikację dla Windows — plik kopii zapasowej jest wspólnym językiem dla nich wszystkich."),
   ("Dlaczego format jest identyczny na obu platformach",
    "JW Library używa tego samego formatu kopii zapasowej wszędzie, gdzie działa — Android, iOS, iPadOS i Windows. Plik .jwlibrary to ZIP zawierający bazę danych SQLite z tymi samymi tabelami i tym samym schematem, niezależnie od tego, które urządzenie go zapisało. Nie ma kroku konwersji, nie ma tańca „eksportuj–importuj” i nie ma niczego charakterystycznego dla platformy w środku pliku. Kopia z Androida przywraca się na iPhonie dokładnie tak samo jak kopia z iPhone'a."),
   ("Jedyne, co naprawdę się różni",
    "Nie plik — tylko dostęp do niego. Na Androidzie kopia zapisuje się w wybranym folderze i można ją przenieść dowolnym menedżerem plików. Na iPhonie przechodzi przez arkusz udostępniania do Plików, AirDrop albo gdzie zechcesz. Trudność, na którą ludzie natrafiają przy zmianie platformy, dotyczy zawsze tego kroku obsługi pliku, nigdy zgodności. E-mail, chmura czy AirDrop — wszystko działa; archiwum albo dociera w całości, albo wcale."),
   ("Kolory wyróżnień, etykiety i odpowiedzi do studium",
    "Wszystko to przetrwa. Kolory wyróżnień są zapisywane jako indeks liczbowy — żółty, zielony, niebieski, różowy, pomarańczowy i fioletowy — i wyświetlają się tak samo na każdej platformie. Etykiety oraz powiązania między etykietami a notatkami przenoszą się, podobnie jak odpowiedzi wpisane w polach pytań do studium. To, co zobaczysz na iPhonie po przywróceniu, to dokładnie to, co miałeś na urządzeniu z Androidem."),
   ("Jeśli iOS nie pozwala wybrać pliku",
    "Najpierw zapisz plik w aplikacji Pliki, a potem wybierz go stamtąd, a nie z załącznika w poczcie czy podglądu w komunikatorze. Niektóre aplikacje przekazują iOS tymczasową kopię podglądu zamiast prawdziwego pliku, a JW Library nie potrafi jej otworzyć. Jeśli plik przyszedł jako załącznik, dotknij go, wybierz Zapisz w Plikach i przywracaj z Plików."),
   ("Przygotuj iPhone'a przed przywracaniem",
    "Zainstaluj JW Library z App Store i zaktualizuj do bieżącej wersji, zanim cokolwiek przywrócisz. Kopia zapisana przez nowszą wersję aplikacji może używać schematu bazy danych, którego starsza wersja nie rozumie, i przywracanie zostanie po prostu odrzucone. Logowanie gdziekolwiek nie jest potrzebne — osobiste dane studium są w pliku, który przywracasz, a nie na koncie."),
   ("Jeśli już zacząłeś studiować na iPhonie",
    "Najpierw utwórz kopię iPhone'a. Przywrócenie pliku z Androida bezpośrednio na wierzch zastąpiłoby wszystko, co napisałeś od czasu przejścia. Scalenie obu kopii daje jeden plik zawierający obie i to jego przywracasz — historia z Androida i nowe notatki z iPhone'a trafią do tej samej biblioteki."),
   ("Korzystanie z obu telefonów później",
    "Niektórzy zostawiają stare urządzenie z Androidem jako drugie do czytania, zamiast je wycofać. To działa, ale oba zaczną się rozchodzić, gdy tylko będziesz robić notatki na obu, bo nie ma między nimi synchronizacji. Jeśli zamierzasz używać obu, zaplanuj okresowe scalanie ich kopii, zamiast zakładać, że pozostaną zgodne."),
   ("Po przejściu",
    "Daj iPhone'owi czas na ponowne pobranie publikacji, z których korzystasz najczęściej, a potem sprawdź kilka opisanych, aby upewnić się, że wszystko dotarło — notatki, kolory wyróżnień, zakładki i etykiety. Zachowaj plik kopii z Androida nawet po zakończeniu przejścia: to datowana migawka Twojej biblioteki, a jej przechowywanie nic nie kosztuje."),
  ],
  "faq": [
   ("Czy potrzebuję do tego komputera?", "Nie. Całe przejście można wykonać z telefonu na telefon przez e-mail albo dysk w chmurze."),
   ("Czy kolory moich wyróżnień przetrwają przeniesienie?", "Tak — wyróżnienia zachowują kolory, notatki zachowują etykiety, a zakładki zostają na swoich miejscach."),
   ("Czy potrzebuję do tego komputera?", "Nie. AirDrop, e-mail albo dowolna aplikacja chmurowa przenoszą plik bezpośrednio między dwoma telefonami."),
   ("Czy działa to w drugą stronę — z iPhone'a na Androida?", "Tak, identycznie. Te same kroki działają w każdą stronę, również do i z aplikacji dla Windows."),
   ("Czy na iPhonie trzeba będzie pobrać te same publikacje?", "Tak, ponieważ multimedia publikacji nie są częścią kopii zapasowej. Notatki wracają na miejsce przy każdej publikacji, gdy tylko zostanie pobrana."),
   ("Czy muszę zachować telefon z Androidem?", "Nie, gdy tylko potwierdzisz, że notatki są na iPhonie. Sprawdź kilka opisanych publikacji, zanim wyczyścisz albo oddasz stare urządzenie."),
   ("Czy przeniesienie obejmuje odpowiedzi na pytania do studium?", "Tak. Wpisane odpowiedzi są częścią osobistych danych studium i przenoszą się razem z resztą."),
   ("Czy jest ryzyko utraty notatek przy przenoszeniu?",
    "Nie, jeśli zachowasz kopię z Androida. Przywracanie zapisuje dane na iPhonie i nigdy nie zmienia odczytywanego pliku, więc oryginał pozostaje nietknięty jako zabezpieczenie. Zachowaj go, dopóki nie potwierdzisz, że iPhone ma wszystko, a najlepiej także później — to datowana migawka Twojej biblioteki."),
   ("Co, jeśli telefon z Androidem nie tworzy kopii zapasowej?",
    "Najpierw sprawdź wolne miejsce, bo aplikacja potrzebuje przestrzeni na zapis pliku. Jeśli zawodzi sama aplikacja, jej aktualizacja albo ponowne uruchomienie urządzenia zwykle to rozwiązuje. Dane pozostają nienaruszone, gdy szukasz przyczyny."),
  ],
 },

 "backup-jw-library": {
  "title": "Jak prawidłowo tworzyć kopie zapasowe JW Library",
  "h1": "Jak prawidłowo tworzyć kopie zapasowe JW Library",
  "description": "Trzydziestosekundowa rutyna tworzenia kopii: co naprawdę zawiera plik .jwlibrary, gdzie go trzymać i dlaczego aktualny plik warto mieć nawet wtedy, gdy nic się nie stało.",
  "intro": [
   "Kopia zapasowa zajmuje pół minuty i warto zrobić z niej nawyk — choć nie całkiem z tego powodu, który zwykle się podaje. Własne tworzenie i przywracanie kopii w JW Library już świetnie przenosi bibliotekę na nowe urządzenie, więc kopia jest mniej polisą ubezpieczeniową, a bardziej surowcem dla wszystkiego innego, co zechcesz zrobić ze swoim studium.",
   "Plik .jwlibrary to jedyna postać, jaką twoja biblioteka przyjmuje poza aplikacją. To jego scalasz, gdy studiowałeś na dwóch urządzeniach; to jego otwierasz, żeby przeczytać, przeetykietować albo uporządkować lata notatek; to w nim szukasz według znaczenia, gdy pamiętasz tylko w połowie, co napisałeś; i to z niego wyciągasz zestaw notatek, gdy chcesz kilka wysłać znajomemu. Posiadanie aktualnego pliku jest tym, co umożliwia to wszystko.",
  ],
  "steps": [
   ("Utwórz kopię zapasową", "Otwórz JW Library → Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Powstanie plik .jwlibrary zawierający każdą notatkę, wyróżnienie, zakładkę i etykietę."),
   ("Przechowuj ją poza telefonem", "Wyślij ją sobie e-mailem albo zapisz w Google Drive, iCloud czy OneDrive. Kopia, która istnieje tylko na telefonie, znika razem z telefonem."),
   ("Powtarzaj według harmonogramu", "Co miesiąc to dobre ustawienie domyślne; przed każdą zmianą telefonu, resetem czy aktualizacją systemu jest to konieczne. Zachowuj starsze egzemplarze — pliki są małe, a stara kopia uratowała już wielu."),
  ],
  "sections": [
   ("Częsty błąd: poleganie na chmurowej kopii samego telefonu",
    "Kopia całego telefonu (Google One, kopia urządzenia w iCloud) często przywraca stary egzemplarz danych JW Library — albo wcale. Plik .jwlibrary to jedyna kopia, którą w pełni kontrolujesz i możesz przenosić między platformami. Traktuj kopię telefonu jako dodatek, a nie jako plan."),
   ("Zostały Ci dwie różne kopie?",
    "Tak się zdarza: jedna kopia z telefonu, starsza z tabletu, a w każdej unikatowe notatki. Nigdy nie musisz między nimi wybierać — scal je w jeden kompletny plik na jwsync.org, bezpłatnie i prywatnie, prosto w przeglądarce."),
   ("Co zawiera plik, a czego nie",
    "Kopia zawiera Twoje osobiste dane studium: notatki, wyróżnienia i ich kolory, zakładki, etykiety oraz odpowiedzi wpisane w polach pytań do studium. Nie zawiera samych publikacji — żadnych Biblii, czasopism, książek, filmów ani nagrań. Dlatego kopia wieloletniego studium waży zwykle tylko kilka megabajtów i dlatego po przywróceniu na nowym urządzeniu pobierasz publikacje od nowa, podczas gdy każda napisana przez Ciebie notatka jest już na miejscu."),
   ("Ile kopii przechowywać",
    "Przechowuj więcej niż jedną. Awaria, która kosztuje ludzi notatki, to rzadko zgubiony plik — częściej dobra kopia nadpisana złą albo przywracanie wykonane na niewłaściwym urządzeniu. Ponieważ pliki są małe, nie ma powodu usuwać starych: przechowuj je z datami w folderze w chmurze. Kopia sprzed pół roku nie traci wartości nawet wtedy, gdy masz nowsze, bo wszystko, co od tego czasu przypadkiem usunąłeś, wciąż w niej jest."),
   ("Gdzie je przechowywać",
    "Wszędzie poza samym urządzeniem. Folder w Drive, iCloud, Dropboxie czy OneDrive pokrywa przypadek najważniejszy — urządzenie zgubione, skradzione, zresetowane albo uszkodzone. Wysłanie pliku do siebie e-mailem też działa i ma przydatny efekt uboczny w postaci daty. Plik zawiera Twoje osobiste notatki, więc traktuj go z taką samą dbałością jak każdy prywatny dokument."),
   ("Sprawdzenie kopii, zanim na niej polegniesz",
    "Kopia, której nigdy nie otworzyłeś, to założenie, a nie zabezpieczenie. Możesz otworzyć plik .jwlibrary w przeglądarce i zobaczyć dokładnie, jakie notatki, wyróżnienia i zakładki zawiera — trzydziestosekundowe sprawdzenie, które zamienia założenie w fakt. Ma to największe znaczenie tuż przed czymś nieodwracalnym: przywróceniem ustawień fabrycznych, oddaniem urządzenia, naprawą albo dużą aktualizacją systemu."),
   ("Momenty, przed którymi warto zrobić kopię",
    "Każda chwila, gdy urządzenie zmienia właściciela albo stan: aktualizacja systemu, przywrócenie ustawień fabrycznych, naprawa albo wymiana ekranu, oddanie w rozliczeniu, przekazanie komuś innemu. Dodaj do tego koniec wszystkiego, czego nie chciałbyś robić od nowa — kongresu, zgromadzenia, okresu przygotowań do przemówienia. Kopie są tanie i szybkie, więc przydatnym nawykiem jest wiązanie ich z wydarzeniami, a nie z kalendarzem."),
   ("Kopia telefonu to nie kopia JW Library",
    "Google One, kopia urządzenia w iCloud albo narzędzie producenta działają na poziomie urządzenia i niekonsekwentnie traktują prywatne dane aplikacji. Ludzie regularnie odkrywają, że pełne przywrócenie telefonu przywróciło aplikacje i ustawienia, ale nie notatki do studium, albo przywróciło wersję sprzed tygodni. Plik .jwlibrary to jedyna kopia, której zawartość kontrolujesz i możesz zweryfikować, więc traktuj kopię na poziomie telefonu jako dodatek, a nie jako plan."),
   ("Jak zamienić to w nawyk, który przetrwa",
    "Procedura, która naprawdę się utrzymuje, to ta powiązana z czymś, co i tak robisz: rób kopię, gdy kończysz przygotowania na tydzień, albo tego samego dnia, w którym załatwiasz inne bieżące sprawy. Zapisuj za każdym razem do tego samego folderu, aby pliki gromadziły się w jednym miejscu, i zostawiaj tam stare. Folder z datowanymi kopiami sięgającymi lat wstecz to najbardziej odporna forma, jaką to może przyjąć, a jego utrzymanie zajmuje sekundy tygodniowo."),
  ],
  "faq": [
   ("Jak duży jest plik kopii zapasowej?", "Zwykle kilka megabajtów nawet przy bardzo dużych bibliotekach — na tyle mało, by wysłać e-mailem."),
   ("Czy tworzenie kopii coś zmienia w moim telefonie?", "Nie. Zapisuje tylko plik; Twoja biblioteka pozostaje nietknięta."),
   ("Czy kopia zawiera moje pobrane publikacje?", "Nie. Tylko osobiste dane studium. Publikacje pobierają się ponownie na nowym urządzeniu, a Twoje notatki automatycznie do nich wracają."),
   ("Czy mogę otworzyć kopię, żeby sprawdzić, co zawiera?", "Tak. Możesz otworzyć plik .jwlibrary w przeglądarce i przejrzeć każdą notatkę, wyróżnienie i zakładkę, nic nie instalując i bez wysyłania pliku gdziekolwiek."),
   ("Czy kopie zapasowe tracą ważność?", "Nie. Plik .jwlibrary pozostaje możliwy do przywrócenia bezterminowo. Przywracaj do bieżącej wersji JW Library, a nie do starej, bo aplikacja czyta starsze formaty kopii, ale nie nowsze."),
   ("Czy powinienem robić kopię przed każdym zebraniem?", "Nie ma potrzeby. Powiąż kopie z wydarzeniami, które mogą kosztować Cię dane — aktualizacjami, naprawami, nowymi urządzeniami — plus regularny rytm dopasowany do ilości studium, którą niechętnie powtarzałbyś."),
   ("Czy warto trzymać kopie sprzed lat?", "Tak. Są małe, a wszystko, co od tego czasu przypadkiem usunąłeś, wciąż w nich jest."),
  ],
 },


 "jw-library-restore-replaced-notes": {
  "title": "Przywracanie w JW Library zastąpiło Twoje notatki? Jak je odzyskać",
  "h1": "Przywracanie zastąpiło Twoje notatki? Oto jak połączyć obie kopie",
  "description": "Przywracanie w JW Library to pełna zamiana, a nie scalanie — notatki zrobione po dacie kopii wydają się zniknąć. Jeśli wciąż masz oba pliki kopii, nic nie przepadło. Oto rozwiązanie.",
  "intro": [
   "To okropny moment: przywracasz kopię na urządzenie, które już miało notatki, a przywracanie zastępuje wszystko — notatki zrobione od czasu tej kopii wydają się zniknąć. Dzieje się tak, bo kopia zapasowa i przywracanie w JW Library to pełna zamiana, a nie scalanie.",
   "Kluczowy fakt: jeśli nowsza praca wciąż istnieje w jakimkolwiek pliku kopii, w rzeczywistości nic nie przepadło. Rozwiązaniem jest scalenie obu kopii, zamiast wybierania między nimi.",
  ],
  "steps": [
   ("Zatrzymaj się — nie przywracaj ponownie", "Każde przywracanie zastępuje bieżące dane urządzenia. Zrób pauzę, zanim zniknie coś jeszcze."),
   ("Utwórz kopię urządzenia w obecnym stanie", "Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Zachowa to bieżący stan, jakikolwiek by nie był."),
   ("Znajdź kopię z brakującymi notatkami", "Plik .jwlibrary, z którego przywracałeś, albo wcześniejszy — sprawdź pocztę, Drive, iCloud i folder pobranych."),
   ("Scal oba pliki na jwsync.org", "Wczytaj obie kopie. JW Sync połączy wszystkie notatki, wyróżnienia, zakładki i etykiety z obu w jeden nowy plik — w Twojej przeglądarce, bez wysyłania czegokolwiek. Sprzeczne wersje tej samej notatki zostaną pokazane obok siebie do wyboru."),
   ("Przywróć scalony plik", "Kopia zapasowa i przywracanie → Przywróć ze scalonym plikiem .jwlibrary. Oba zestawy notatek wróciły na urządzenie."),
  ],
  "sections": [
   ("Co, jeśli nie ma kopii z nowszymi notatkami?",
    "Jeśli jedyny egzemplarz nowszych notatek był na urządzeniu, a przywracanie już go nadpisało, samo JW Library nie oferuje cofnięcia. Właśnie dlatego krok 2 powyżej — utworzenie kopii bieżącego stanu, zanim cokolwiek zrobisz — jest tak ważny za każdym razem, gdy z danymi dzieje się coś niepokojącego. Na przyszłość procedura „najpierw scal” czyni ten problem strukturalnie niemożliwym."),
  ],
  "faq": [
   ("Czy scalanie zduplikuje notatki wspólne dla obu kopii?", "Nie — identyczne elementy są wykrywane i zachowywane raz. Do przeglądu trafiają tylko naprawdę różne wersje tej samej notatki."),
   ("Czy naprawi to kopię, która w ogóle się nie przywraca?", "To zwykle uszkodzenie pliku, a nie nadpisanie — zobacz poradnik o naprawie uszkodzonej kopii poniżej."),
  ],
 },

 "fix-corrupted-jw-library-backup": {
  "title": "Naprawa uszkodzonej kopii zapasowej JW Library, która się nie przywraca",
  "h1": "Naprawa uszkodzonej kopii JW Library za pomocą Doktora biblioteki",
  "description": "JW Library odmawia przywrócenia Twojego pliku .jwlibrary? Doktor biblioteki skanuje kopię w Twojej przeglądarce, usuwa typowe problemy i tworzy czysty egzemplarz, który się przywraca.",
  "intro": [
   "Kopia, która się nie przywraca, wcale nie musi być kopią, która straciła Twoje notatki. Większość plików określanych jako uszkodzone jest strukturalnie w porządku i zostaje odrzucona z możliwej do naprawienia przyczyny albo została uszkodzona w trakcie przesyłania w sposób, który rozwiązuje świeży egzemplarz. Warto przejść przez możliwe przyczyny, zanim spiszesz plik na straty.",
   "Czasem JW Library odrzuca plik kopii: przywracanie się nie udaje, zwraca błąd albo plik się nie otwiera. Typowe przyczyny: przerwane pobieranie, dysk w chmurze, który uszkodził plik, rozszerzenie zmienione po drodze albo wewnętrzne niespójności narosłe przez lata używania.",
   "JW Sync zawiera Doktora biblioteki — narzędzie, które skanuje plik .jwlibrary i usuwa typowe problemy, w całości w Twojej przeglądarce, tak że plik nigdy nie opuszcza Twojego urządzenia.",
  ],
  "steps": [
   ("Otwórz JW Sync i wczytaj problematyczny plik", "Wejdź na jwsync.org i wczytaj plik .jwlibrary, który się nie przywraca. (Jeśli plik przyszedł z nazwą zmienioną na .zip, najpierw zmień ją z powrotem na .jwlibrary — samo to rozwiązuje wiele przypadków.)"),
   ("Uruchom skanowanie Doktora biblioteki", "Doktor bada wewnętrzną strukturę kopii i wypisuje, co znalazł — od nieszkodliwych drobiazgów po prawdziwe uszkodzenia — prostym językiem."),
   ("Zastosuj poprawki", "Jedno dotknięcie naprawia to, co da się naprawić. Doktor nigdy nie edytuje Twojego pierwotnego pliku; tworzy oczyszczony egzemplarz, więc oryginał pozostaje nietknięty jako zabezpieczenie."),
   ("Pobierz i przywróć naprawiony plik", "Przywróć oczyszczony plik .jwlibrary przez Kopia zapasowa i przywracanie → Przywróć w JW Library."),
  ],
  "sections": [
   ("Doktor działa też przy każdym scalaniu",
    "Te same kontrole uruchamiają się automatycznie w silniku scalania, więc scalona kopia zawsze jest czysta — nawet jeśli jeden z plików wejściowych miał problemy, o których nie wiedziałeś."),
   ("Kiedy pliku nie da się naprawić",
    "Jeśli plik został obcięty na tyle, że danych po prostu w nim nie ma, żadne narzędzie ich nie wymyśli. Doktor powie to szczerze, zamiast tworzyć wątpliwy plik — i to jest sygnał, aby poszukać wcześniejszego egzemplarza w poczcie, Drive czy iCloud, a zarazem kolejny powód, dla którego warto trzymać stare kopie."),
   ("Co zwykle znaczy „uszkodzony”",
    "W praktyce rzadko chodzi o uszkodzone dane. Typowe przyczyny to plik obcięty podczas przesyłania — ucięty przez nieudane wysyłanie albo komunikator, który go skompresował — albo nienaruszone archiwum zawierające wewnętrzne niespójności, które aplikacja odrzuca. Ponieważ plik .jwlibrary to ZIP opakowujący bazę danych SQLite, problem może dotyczyć każdej z tych warstw i wymagają one różnych rozwiązań. Obciętego pliku nie da się naprawić i trzeba go zdobyć ponownie; niespójną bazę danych zwykle da się."),
   ("Co dokładnie sprawdza skanowanie",
    "Skanowanie weryfikuje, czy archiwum się otwiera, czy userData.db jest czytelną bazą danych SQLite przechodzącą kontrolę spójności, czy schemat odpowiada oczekiwaniom JW Library i czy manifest zgadza się z opisywaną bazą danych — łącznie z sumą kontrolną, której aplikacja używa do potwierdzenia, że pliku nie zmieniono. Niezgodność między manifestem a bazą danych to jedna z najczęstszych przyczyn odrzucenia technicznie poprawnej kopii przy przywracaniu i da się ją łatwo naprawić."),
   ("Osierocone wpisy są zwykle nieszkodliwe",
    "Skanowanie prawdziwej kopii często zgłasza wpisy odwołujące się do czegoś, czego już nie ma — na przykład wyróżnienie wskazujące miejsce w publikacji, które się przesunęło. Własne kopie JW Library rutynowo zawierają ich setki i przywracają się bez problemu. To normalny skutek aktualizowania publikacji w czasie, a nie dowód uszkodzenia, i ich usuwanie nie jest potrzebne, aby plik działał."),
   ("Ratowanie notatek z pliku, który się nie przywraca",
    "Nawet gdy kopii nie da się naprawić na tyle, by JW Library ją przyjęło, notatki w środku często wciąż da się odczytać. Otwarcie pliku w przeglądarce pozwala zobaczyć i skopiować treść notatek bezpośrednio, co zamienia bezużyteczny plik w odzyskany materiał do studium. Jeśli masz drugą, starszą kopię, która się przywraca, czytelną treść z uszkodzonej można z nią połączyć zamiast przepisywać."),
   ("Gdy przywracanie zawodzi bez wyraźnego błędu",
    "JW Library często odrzuca plik bez wyjaśnienia. Najczęstsze przyczyny to manifest, którego suma kontrolna nie odpowiada już opisywanej bazie danych, plik obcięty podczas przesyłania albo kopia zapisana przez nowszą wersję aplikacji niż ta, do której przywracasz. Pierwsze da się naprawić, drugie wymaga ponownego pobrania pliku z pierwotnego źródła, a trzecie rozwiązuje aktualizacja aplikacji przed przywracaniem."),
   ("Jak tego uniknąć następnym razem",
    "Większość uszkodzeń powstaje w trakcie przesyłania. Przenoś kopie jako pliki, a nie przez cokolwiek, co może je ponownie skompresować, i wybieraj chmurę, AirDrop albo kabel zamiast komunikatorów. Po przeniesieniu sprawdź, czy rozmiar pliku zgadza się z pierwotnym — plik wyraźnie mniejszy od wysłanego został obcięty, a żadna naprawa nie przywróci bajtów, które nigdy nie dotarły."),
   ("Jeśli nic nie działa",
    "Plik, którego nie da się naprawić, wciąż może być czytelny, a odczytanie go często wystarcza — treść notatek da się odzyskać nawet wtedy, gdy JW Library odrzuca plik. Połącz to z dowolną starszą kopią, która się przywraca, a zwykle skończysz z większością biblioteki w całości. Zanim uznasz plik za bezużyteczny, otwórz go i zobacz, co naprawdę jest w środku."),
  ],
  "faq": [
   ("Czy moje dane są wysyłane do skanowania?", "Nie. Skanowanie, poprawki i eksport działają lokalnie w przeglądarce."),
   ("Czy odzyska notatki usunięte w JW Library?", "Nie — naprawia strukturę pliku. Notatek usuniętych w aplikacji przed utworzeniem kopii po prostu w niej nie ma."),
   ("Czy naprawa pliku spowoduje utratę notatek?", "Naprawy działają na kopii i dotyczą problemów strukturalnych, a nie treści. Twój pierwotny plik nigdy nie jest zmieniany, więc pozostaje dostępny, gdybyś chciał zacząć od nowa."),
   ("Dlaczego moja kopia się uszkodziła?", "Najczęściej plik został zmieniony podczas przesyłania — wysłany przez aplikację, która go skompresowała albo obcięła, albo przesyłanie się nie zakończyło. Ponowne przeniesienie pliku z pierwotnego źródła zwykle to rozwiązuje."),
   ("Czy skanowanie odzyska notatki usunięte przeze mnie w JW Library?", "Nie. Gdy notatkę usunięto w aplikacji i utworzono nową kopię, w tym pliku jej już nie ma. Starsza kopia sprzed usunięcia wciąż ją zawiera."),
   ("Czy po rozmiarze pliku poznam, że został obcięty?", "Często tak. Porównaj go z oryginałem, jeśli go masz; wyraźny niedobór oznacza, że przesyłanie się nie zakończyło."),
   ("Czy kopia, która otwiera się w przeglądarce, na pewno się przywróci?", "Nie ma gwarancji, ale to mocna przesłanka, że archiwum i baza danych są w porządku, co wyklucza najczęstsze awarie."),
  ],
 },

 "edit-jw-library-notes": {
  "title": "Przeglądanie i edycja notatek JW Library w przeglądarce",
  "h1": "Przeglądaj, wyszukuj i edytuj swoje notatki JW Library — Eksplorator studium",
  "description": "Otwórz dowolną kopię zapasową .jwlibrary w przeglądarce, aby przeglądać, wyszukiwać, edytować, zmieniać etykiety i kolory oraz zbiorczo porządkować swoje notatki, wyróżnienia i zakładki JW Library. Nic nie jest wysyłane na serwer.",
  "intro": [
   "JW Library jest stworzone do robienia notatek, a nie do zarządzania tysiącami z nich. Eksplorator studium otwiera dowolną kopię .jwlibrary prosto w Twojej przeglądarce i zamienia ją w menedżera biblioteki — notatki, wyróżnienia i zakładki w jednym miejscu, bez wysyłania czegokolwiek gdziekolwiek.",
  ],
  "steps": [
   ("Wczytaj kopię zapasową", "Utwórz kopię w JW Library (Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową), a potem otwórz jwsync.org i wczytaj plik do Eksploratora studium."),
   ("Przeglądaj i przeszukuj wszystko", "Trzy zakładki — Notatki, Wyróżnienia, Zakładki — z wyszukiwaniem pełnotekstowym oraz filtrami koloru, etykiety i publikacji. Zakładka Odpowiedzi do studium pokazuje też Twoje odpowiedzi wpisane w publikacjach."),
   ("Edytuj na miejscu", "Otwórz dowolną notatkę, aby zmienić jej tytuł i treść z formatowaniem (pogrubienie, kursywa, podkreślenie, listy), zmienić kolor wyróżnienia oraz dodać lub usunąć etykiety. Zakładki i kolory wyróżnień edytuje się tak samo."),
   ("Porządkuj zbiorczo", "Zaznacz wiele notatek naraz, aby razem zmienić im etykiety, kolory albo je usunąć — z pełnym cofaniem i ponawianiem, więc pomyłka nigdy nie jest groźna. Możesz też wyodrębnić zakres dat do nowej kopii albo skopiować notatki jako Markdown."),
   ("Wyeksportuj zmienioną bibliotekę", "Pobierz zmieniony plik .jwlibrary i przywróć go w JW Library. Twoje zmiany są już na urządzeniu."),
  ],
  "sections": [
   ("Po co edytować w przeglądarce zamiast w aplikacji?",
    "Ze względu na skalę. Zmiana nazwy etykiety w 300 notatkach, przekolorowanie każdego żółtego wyróżnienia w jednej publikacji albo usunięcie lat nieaktualnych zakładek to tutaj minuty pracy, a w aplikacji godziny dotykania ekranu. Wyeksportowany plik to zwykła kopia zapasowa, którą JW Library przywraca jak każdą inną."),
  ],
  "faq": [
   ("Czy edycja narusza moją pierwotną kopię?", "Nie — zmiany są wprowadzane w kopii w przeglądarce i zapisywane do nowego eksportowanego pliku. Oryginał pozostaje taki, jaki był."),
   ("Czy jest limit wielkości biblioteki?", "Bardzo duże biblioteki są dzielone na strony, aby przeglądanie pozostało szybkie; wyszukiwanie i filtry działają na całości."),
  ],
 },


 "search-jw-library-notes": {
  "title": "Wyszukiwanie notatek JW Library według znaczenia — Zapytaj swoją bibliotekę",
  "h1": "Zapytaj swoją bibliotekę: wyszukiwanie notatek JW Library według znaczenia",
  "description": "Wyszukiwanie semantyczne w notatkach JW Library: znajdź na wpół zapamiętaną notatkę, opisując ją, nawet gdy nie pamiętasz dokładnych słów. Na urządzeniu, działa offline, prywatnie.",
  "intro": [
   "Każdy, kto ma lata notatek, zna ten problem: pamiętasz, że pisałeś o znoszeniu prób z radością, ale notatka nie zawiera słowa „wytrwałość”, więc wyszukiwanie słów kluczowych niczego nie znajduje. „Zapytaj swoją bibliotekę” szuka zamiast tego według znaczenia — opisz myśl, a pojawią się notatki najbliższe jej, jakkolwiek zostały sformułowane.",
   "Wszystko działa w całości na Twoim urządzeniu: model językowy pobiera się raz do przeglądarki i potem działa offline, z przyspieszeniem WebGPU tam, gdzie jest dostępne. Twoje notatki nigdy nigdzie nie są wysyłane.",
  ],
  "steps": [
   ("Wczytaj kopię do Eksploratora studium", "Na jwsync.org wczytaj swój plik .jwlibrary i otwórz zakładkę „Zapytaj”."),
   ("Pozwól modelowi raz się przygotować", "Przy pierwszym użyciu model pobiera się na urządzenie i indeksuje Twoje notatki. Dzieje się to raz; potem działa natychmiast, nawet offline."),
   ("Pytaj własnymi słowami", "Wpisz to, co pamiętasz — „ta notatka o cierpliwości wobec nowych w służbie”, „zachęta dla zniechęconych pionierów” — a pojawią się notatki najbliższe znaczeniowo, uszeregowane według dopasowania."),
  ],
  "sections": [
   ("Czym różni się od zwykłego wyszukiwania",
    "Wyszukiwanie słów kluczowych dopasowuje litery; wyszukiwanie semantyczne dopasowuje myśli. Zapytanie o „niepokój” znajdzie też notatki napisane ze słowami „troska”, „troski życia” albo z cytatem wersetu na ten temat. Oba rodzaje wyszukiwania są dostępne w Eksploratorze studium — wzajemnie się uzupełniają."),
   ("Prywatność z założenia",
    "To nie jest chmurowa usługa sztucznej inteligencji. Model działa wewnątrz karty Twojej przeglądarki, indeks żyje na Twoim urządzeniu, a zamknięcie karty kończy sprawę. Nic o Twoich notatkach nigdy nie opuszcza Twojego komputera."),
  ],
  "faq": [
   ("Czy potrzebne jest mocne urządzenie?", "Współczesny telefon albo laptop dobrze sobie radzi; na urządzeniach z WebGPU jest najszybciej. Do wyboru są różne rozmiary modelu dopasowane do sprzętu."),
   ("Czy działa w moim języku?", "Tak — wyszukiwanie działa w językach, w których napisane są Twoje notatki, a interfejs jest przetłumaczony na wszystkie języki obsługiwane przez JW Sync."),
  ],
 },

 "jw-library-study-stats": {
  "title": "Zobacz swoje statystyki studium JW Library: passy, mapy aktywności i nagrody",
  "h1": "Twoje statystyki studium JW Library: passy, mapy aktywności, pokrycie i nagrody",
  "description": "Zamień kopię zapasową JW Library w prywatną analitykę studium — podsumowania, mapę aktywności, passy, pokrycie 66 ksiąg Biblii, profil studium i około 200 nagród.",
  "intro": [
   "Twój plik kopii zapasowej po cichu zapisuje lata historii studium — kiedy robisz notatki, co wyróżniasz, które księgi przerobiłeś. Strona statystyk studium odczytuje kopię .jwlibrary i zamienia tę historię w prywatny pulpit, obliczany w całości w Twojej przeglądarce.",
  ],
  "steps": [
   ("Utwórz kopię zapasową", "W JW Library: Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową."),
   ("Otwórz stronę statystyk studium", "Wejdź na jwsync.org/highlights.html i wczytaj plik."),
   ("Poznaj historię swojego studium", "Główne podsumowania, widoki roku służbowego i całego czasu, wzrost rok do roku — a poniżej najciekawsze rzeczy."),
  ],
  "sections": [
   ("Co zobaczysz",
    "Mapę aktywności z Twoją najdłuższą i bieżącą passą; rytm tygodniowy, najbardziej zajęte godziny i miesiące; pokrycie Biblii we wszystkich 66 księgach z podziałem na Pisma Hebrajskie i Greckie; koło kolorów wyróżnień, histogram głębi notatek i chmurę słów; 24-godzinny zegar studium i radar sezonowości."),
   ("Profil, droga i nagrody",
    "Sześciocechowy profil studium (Regularność, Pilność, Głębia, Zasięg, Refleksja, Wytrwałość) z postacią „podpisu studium”; Drogę studium liczącą 60 poziomów w 12 nazwanych rangach; oraz około 200 nagród od pospolitych po legendarne, w tym medale uwzględniające treść. Karta do udostępnienia podsumowuje Twój rok, nie ujawniając ani jednej notatki."),
   ("Codzienny powód, aby wrócić",
    "Panel „Przypomnienie” pokazuje notatki napisane tego dnia w poprzednich latach i buduje łagodne powtarzanie z odstępami — po trochu, ale regularnie, tak wiedza zostaje na dłużej."),
  ],
  "faq": [
   ("Czy cokolwiek z tego jest wysyłane na serwer?", "Nie. Kopia jest analizowana w Twojej przeglądarce; statystyki nigdy nie opuszczają Twojego urządzenia."),
   ("Czy statystyki aktualizują się same?", "Odzwierciedlają wczytaną kopię — utwórz świeżą kopię, aby zobaczyć świeże statystyki."),
  ],
 },

 "share-jw-library-notes": {
  "title": "Jak udostępnić notatki JW Library znajomemu",
  "h1": "Jak udostępnić notatki JW Library znajomemu — bez serwera",
  "description": "Wyślij znajomemu wybrane notatki JW Library (wraz z wyróżnieniami) w małym pliku — bez serwera, bez konta. Odbiorca doda je, nie nadpisując własnych notatek.",
  "intro": [
   "JW Library nie ma sposobu na przekazanie innej osobie kopii konkretnych notatek. Wysłanie całej kopii zapasowej zadziałałoby — ale przekazuje wszystko, a jej przywrócenie skasowałoby własną bibliotekę odbiorcy. Udostępnianie notatek w JW Sync rozwiązuje oba problemy: wybierasz dokładnie te notatki, którymi chcesz się podzielić, a odbiorca dodaje je, niczego nie tracąc.",
  ],
  "steps": [
   ("Wybierz notatki do udostępnienia", "Na stronie udostępniania jwsync.org/share.html wczytaj swoją kopię i zaznacz notatki — kilka z jednego przemówienia albo wszystko pod jedną etykietą jednym kliknięciem dzięki filtrowi etykiet. Wyróżnienia powiązane z tymi notatkami jadą razem z nimi."),
   ("Wyślij plik udostępniania", "JW Sync tworzy mały plik zawierający tylko wybrane notatki. Wyślij go dowolnym kanałem — komunikatorem, e-mailem, przez AirDrop. Nie ma serwera ani konta; plik to cała wymiana."),
   ("Odbiorca dodaje go u siebie", "Twój znajomy otwiera tę samą stronę, wczytuje plik udostępniania razem z własną kopią i otrzymuje nową kopię z dodanymi Twoimi notatkami. Jego własne notatki nigdy nie są nadpisywane — jeśli udostępniona notatka koliduje z jego notatką, wybiera, jak ją dodać — a zaimportowane notatki dostają etykietę, więc łatwo je później znaleźć, przejrzeć albo usunąć."),
  ],
  "sections": [
   ("Dobre zastosowania",
    "Przekazanie materiałów partnerowi studium, podzielenie się notatkami z zebrania z kimś, kogo nie było, danie nowemu głosicielowi startowego zestawu notatek do publikacji albo przekazanie notatek z konkretnego projektu członkowi rodziny — a wszystko to bez ujawniania reszty biblioteki żadnej ze stron."),
  ],
  "faq": [
   ("Czy odbiorca musi zainstalować JW Sync?", "Po żadnej stronie nic się nie instaluje — to strona internetowa. Odbiorca potrzebuje tylko pliku udostępniania i własnej kopii zapasowej."),
   ("Czy mogę cofnąć udostępnienie albo ustawić wygasanie pliku?", "Plik to zwykły plik, który wysłałeś — nie ma kopii na serwerze, która mogłaby wygasnąć. Udostępniaj tylko to, czym podzieliłbyś się w dowolnej wiadomości."),
  ],
 },

 "bible-reading-plan": {
  "title": "Dzienny plan czytania Biblii z własnymi notatkami obok",
  "h1": "Towarzysz czytania: plan czytania Biblii z Twoimi notatkami obok",
  "description": "Prywatny dzienny harmonogram czytania Biblii, który pokazuje notatki i wyróżnienia zrobione przez Ciebie do dzisiejszych rozdziałów. Wybierz tempo, utrzymuj passę i patrz, jak wypełnia się siatka 66 ksiąg.",
  "intro": [
   "Wiele aplikacji oferuje harmonogram czytania Biblii. Towarzysz czytania robi coś, czego żadna z nich nie potrafi: ponieważ odczytuje Twoją własną kopię .jwlibrary, dzisiejsze czytanie przychodzi z notatkami i wyróżnieniami, które sam zrobiłeś do dokładnie tych rozdziałów — „wyróżniłeś cztery wersety w Psalmie 37 dwa lata temu”. Czytanie przez pryzmat własnej historii studium, w całości na Twoim urządzeniu.",
  ],
  "steps": [
   ("Wybierz kolejność i tempo", "Czytaj w kolejności ksiąg Biblii albo w przybliżonej kolejności chronologicznej; skończ w 3 miesiące, 6 miesięcy, rok, 2 lata albo ustaw własne tempo rozdziałów dziennie — z bieżącym podglądem „skończysz mniej więcej…”."),
   ("Przeczytaj dzisiejszą porcję", "Każdy rozdział jest o jedno dotknięcie, otwiera się prosto w JW Library albo w BIBLIOTECE INTERNETOWEJ Strażnicy w Twoim języku. Odhaczaj rozdziały w miarę postępów."),
   ("Weź ze sobą swoje notatki (opcjonalnie)", "Wczytaj kopię w dowolnym narzędziu JW Sync, a Twoje notatki i liczba wyróżnień pojawią się tuż pod dzisiejszymi rozdziałami."),
   ("Patrz, jak rośnie postęp", "Siatka 66 ksiąg wypełnia się w miarę czytania, wraz z paskiem przeczytanych rozdziałów, prognozą tempa i etapami za ukończenie każdej księgi, Pism Hebrajsko-Aramejskich, Pism Greckich — i całej Biblii."),
  ],
  "sections": [
   ("Passy bez wyrzutów sumienia",
    "Ukończenie dnia wydłuża Twoją passę; opuszczony dzień po prostu przesuwa prognozowaną datę zakończenia. Nie ma sterty zaległości — plan dostosowuje się do Twojego życia, zamiast Cię strofować."),
  ],
  "faq": [
   ("Czy muszę wczytać kopię, aby z tego korzystać?", "Nie — plan, passy i postęp działają same z siebie. Kopia dodaje jedynie Twoje osobiste notatki do czytania każdego dnia."),
   ("Czy mój postęp w czytaniu jest prywatny?", "Tak. Postęp żyje w Twojej przeglądarce na Twoim urządzeniu — nie ma konta i nic nie jest wysyłane na serwer."),
  ],
 },


 "open-jwlibrary-file": {
  "title": "Czym jest plik .jwlibrary i jak go otworzyć?",
  "h1": "Czym jest plik .jwlibrary — i jak otworzyć go na dowolnym urządzeniu",
  "description": "Plik .jwlibrary to Twoja kopia zapasowa JW Library: jeden plik zawierający każdą notatkę, wyróżnienie, zakładkę i etykietę. Oto co jest w środku oraz jak go otworzyć i odczytać.",
  "intro": [
   "Plik .jwlibrary wygląda na nieprzejrzysty, ale taki nie jest. To zwykłe archiwum ZIP wokół zwykłej bazy danych SQLite, co oznacza, że możesz odczytać własną kopię — zobaczyć, jakie dokładnie notatki, wyróżnienia i zakładki zawiera — bez JW Library i bez instalowania czegokolwiek.",
   "Gdy tworzysz kopię zapasową JW Library, otrzymujesz plik z rozszerzeniem .jwlibrary. To pojedynczy, przenośny pakiet zawierający wszystko z Twojego osobistego studium — notatki, wyróżnienia, zakładki, etykiety i playlisty — w zwartej bazie danych. Nie jest to dokument otwierany w Wordzie czy czytniku PDF; jest przeznaczony do przywrócenia z powrotem do JW Library.",
   "Ale nie musisz go przywracać tylko po to, żeby zajrzeć do środka. JW Sync otwiera plik .jwlibrary prosto w Twojej przeglądarce, więc możesz czytać, przeszukiwać i edytować jego zawartość, nie dotykając telefonu.",
  ],
  "steps": [
   ("Zdobądź plik .jwlibrary", "Powstaje w JW Library: Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. To właśnie ten plik."),
   ("Otwórz go w JW Sync", "Wejdź na jwsync.org i wczytaj plik do Eksploratora studium. Otworzy się natychmiast, na Twoim urządzeniu — nic nie jest wysyłane."),
   ("Czytaj i pracuj z nim", "Przeglądaj notatki, wyróżnienia i zakładki; przeszukuj wszystko; edytuj, zmieniaj etykiety albo eksportuj. Gdy skończysz, możesz przywrócić plik (albo zmienioną kopię) z powrotem do JW Library."),
  ],
  "sections": [
   ("Co naprawdę jest w środku pliku",
    "Technicznie plik .jwlibrary to spakowana baza danych SQLite plus manifest. Dlatego zmiana nazwy na .zip zdarza się czasem przypadkiem podczas przesyłania — i dlatego zmiana z powrotem na .jwlibrary to naprawia. Do korzystania nie musisz nic z tego wiedzieć, ale wyjaśnia to, dlaczego plik jest mały, samodzielny i identyczny na Androidzie, iPhonie, iPadzie i Windows."),
   ("Otwieranie na komputerze",
    "Ta sama strona jwsync.org działa w przeglądarce na laptopie czy komputerze stacjonarnym — przydatne do czytania lat notatek na dużym ekranie albo do zbiorczych porządków, które na telefonie byłyby męczące. Nie ma czego instalować."),
   ("Czym plik jest naprawdę",
    "Plik .jwlibrary to archiwum ZIP z innym rozszerzeniem. W środku znajdują się userData.db — baza danych SQLite z Twoimi notatkami, wyróżnieniami, zakładkami i etykietami — oraz manifest.json, mały plik opisujący kopię, w tym sumę kontrolną bazy danych, dzięki której JW Library potwierdza, że pliku nie zmieniono. Nie ma w nim nic zastrzeżonego ani zaszyfrowanego: to standardowe archiwum wokół standardowej bazy danych."),
   ("Otwieranie bez JW Library",
    "Nie potrzebujesz aplikacji ani żadnego oprogramowania, aby odczytać własną kopię. Otwarcie pliku w przeglądarce pokazuje każdą notatkę, wyróżnienie i zakładkę, jakie zawiera, z wyszukiwaniem i filtrowaniem, a plik nigdy nie opuszcza Twojego urządzenia — jest odczytywany lokalnie, a nie wysyłany. To najszybszy sposób, aby upewnić się, że kopia zawiera to, co myślisz, przed resetem, oddaniem urządzenia albo przywracaniem na nowy telefon."),
   ("Ręczne zaglądanie do środka",
    "Jeśli jesteś ciekaw, skopiuj plik, zmień nazwę kopii na .zip i otwórz ją dowolnym archiwizatorem. Zobaczysz userData.db i manifest.json. Otwarcie bazy danych wymaga przeglądarki SQLite, a tabele są nazwane od tego, co zawierają — Note, UserMark, Bookmark, Tag. Zawsze pracuj na kopii: ręczna edycja bazy danych bez aktualizacji sumy kontrolnej w manifeście tworzy plik, którego JW Library odmówi przywrócenia."),
   ("Bezpieczna edycja",
    "Notatki można poprawiać, przeetykietowywać, przekolorowywać albo usuwać poza aplikacją, a wynik wyeksportować jako nowy plik .jwlibrary, który przywracasz normalnie. Zasadą, która zapewnia bezpieczeństwo, jest zachowanie oryginału: edytuj kopię, przywróć zmieniony plik, a jeśli coś nie będzie po Twojej myśli, nietknięty oryginał wciąż tam jest."),
   ("Czytanie kopii na telefonie",
    "Nie potrzebujesz komputera. Otwarcie pliku w przeglądarce mobilnej działa tak samo, co przydaje się, gdy kopia jest już na telefonie, a chcesz sprawdzić jej zawartość przed przywracaniem albo przed wyczyszczeniem urządzenia. Plik jest odczytywany lokalnie, więc działa to bez połączenia poza samym wczytaniem strony."),
   ("Dlaczego suma kontrolna w manifeście ma znaczenie",
    "manifest.json zapisuje sumę kontrolną userData.db. JW Library używa jej, aby potwierdzić, że bazy danych nie zmieniono od utworzenia kopii, więc plik, którego bazę edytowano bez przeliczenia sumy, zostaje odrzucony przy przywracaniu. To najczęstsza przyczyna, dla której ręcznie edytowana kopia przestaje działać, i powód, dla którego edytowanie przez narzędzie przepisujące manifest jest bezpieczniejsze niż edytowanie bazy wprost."),
   ("Do czego to się przydaje",
    "Możliwość odczytania kopii zmienia to, ile jest ona warta. Możesz potwierdzić, że plik zawiera to, co myślisz, przed wyczyszczeniem telefonu, sprawdzić, czy stary plik warto przywracać, znaleźć notatkę, o której wiesz, że ją napisałeś, bez przeszukiwania aplikacji, albo odzyskać tekst z pliku, którego JW Library nie przyjmuje. Nic z tego nie wymaga powierzania pliku komukolwiek — jest odczytywany na Twoim własnym urządzeniu."),
  ],
  "faq": [
   ("Czy mogę otworzyć plik .jwlibrary w Excelu albo Notatniku?", "Nie w sposób użyteczny — to baza danych, a nie arkusz czy plik tekstowy. Otwórz go w JW Sync, aby go odczytać, albo wyeksportuj notatki do Markdown lub tekstu z Eksploratora studium."),
   ("Czy otwieranie mojej kopii w przeglądarce jest bezpieczne?", "Tak. JW Sync odczytuje plik lokalnie w karcie Twojej przeglądarki; nic nie jest wysyłane na serwer, a Twój pierwotny plik nigdy nie jest zmieniany."),
   ("Czy mogę po prostu zmienić nazwę na .zip?", "Tak, na kopii. Zmiana nazwy nie zmienia zawartości i pozwala dowolnemu archiwizatorowi pokazać, co jest w środku."),
   ("Czy otwarcie pliku go zmieni?", "Nie. Odczyt kopii — w przeglądarce czy archiwizatorze — pozostawia ją bajt w bajt niezmienioną. Dopiero zapis albo eksport tworzy nowy plik."),
   ("Czy muszę być online?", "Tylko po to, aby wczytać stronę. Sam plik jest odczytywany na Twoim urządzeniu, a nie wysyłany, więc Twoje notatki nigdy nie podróżują przez sieć."),
   ("Czy mogę otworzyć kopię, którą przysłał mi ktoś inny?", "Tak, format nie jest przypisany do urządzenia ani konta. To, czy powinieneś ją przywracać, to osobna kwestia, bo przywracanie zastępuje Twoją własną bibliotekę."),
   ("Czy muszę coś zainstalować, aby zajrzeć do środka?", "Nie. Przeglądarka wystarczy, aby odczytać notatki; dopiero ręczny wgląd w samą bazę danych wymaga przeglądarki SQLite."),
  ],
 },

 "jw-library-windows-pc": {
  "title": "Kopie zapasowe i scalanie JW Library na komputerze z Windows",
  "h1": "Korzystanie z kopii zapasowych JW Library na komputerze z Windows",
  "description": "Jak utworzyć kopię zapasową JW Library w Windows i jak scalić kopię z komputera z telefonem i tabletem, aby notatki, wyróżnienia i zakładki były razem na każdym urządzeniu.",
  "intro": [
   "JW Library działa w Windows tak samo jak na telefonach i tabletach i tworzy ten sam plik kopii .jwlibrary. Oznacza to, że Twój komputer może być częścią tej samej biblioteki studium co telefon — pod warunkiem że będziesz scalać kopie, a nie przywracać jedną na drugą.",
  ],
  "steps": [
   ("Utwórz kopię w Windows", "W aplikacji JW Library dla Windows otwórz menu, przejdź do Kopia zapasowa i przywracanie i utwórz kopię. Zapisz plik .jwlibrary w łatwym do odnalezienia miejscu."),
   ("Utwórz też kopie telefonu i tabletu", "Na każdym urządzeniu: Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową."),
   ("Scal je na jwsync.org", "Otwórz jwsync.org w dowolnej przeglądarce na komputerze i wczytaj wszystkie pliki kopii. JW Sync połączy notatki, wyróżnienia, zakładki i etykiety z każdego urządzenia w jeden scalony plik .jwlibrary — lokalnie, bez wysyłania czegokolwiek."),
   ("Przywróć scalony plik wszędzie", "Przywróć scalony plik w aplikacji dla Windows i na każdym urządzeniu mobilnym. Teraz komputer, telefon i tablet mają kompletną bibliotekę."),
  ],
  "sections": [
   ("Dlaczego komputer to najwygodniejsze miejsce",
    "W przeglądarce na komputerze wczytywanie kilku plików, przeglądanie podglądu scalania i zapisywanie wyniku idzie znacznie szybciej niż dotykanie ekranu telefonu. Wiele osób trzyma swoją główną procedurę scalania na komputerze i po prostu przywraca scalony plik z powrotem na urządzenia mobilne."),
  ],
  "faq": [
   ("Czy kopia z Windows działa z kopiami z iPhone'a i Androida?", "Tak — format .jwlibrary jest identyczny na każdej platformie, więc kopia z Windows swobodnie scala się z kopiami z telefonu i tabletu."),
   ("Czy muszę coś instalować na komputerze?", "Nie. JW Sync to strona internetowa; działa w Edge, Chrome czy Firefoksie bez żadnej instalacji."),
  ],
 },


 "recover-jw-library-notes-lost-phone": {
  "title": "Jak odzyskać notatki JW Library po zgubieniu lub zepsuciu telefonu",
  "h1": "Odzyskiwanie notatek JW Library ze zgubionego, zepsutego lub zresetowanego telefonu",
  "description": "Zgubiłeś telefon albo został zresetowany razem z notatkami JW Library? To, co da się odzyskać, zależy od Twoich kopii zapasowych. Oto dokładnie, jak odzyskać notatki — i co zrobić następnym razem.",
  "intro": [
   "Najpierw szczera odpowiedź, bo oszczędzi ci dalszego czytania. Jeśli kopia .jwlibrary istnieje gdziekolwiek poza utraconym urządzeniem, wszystko, co w niej jest, wraca przez własne przywracanie JW Library i do tej części ta strona nie jest ci potrzebna. Jeśli nie ma kopii w żadnej postaci, osobistych danych studium nie da się odzyskać w ogóle: żyją wyłącznie na urządzeniu i żadne narzędzie tego nie zmieni.",
   "Naprawdę ta strona pomaga w przypadku pośrednim, a ten zdarza się częściej niż oba pozostałe: kopię masz, ale nie jest ona całą historią. Może mieć kilka miesięcy albo już studiowałeś na telefonie zastępczym — wtedy zwykłe jej przywrócenie zamieniłoby jeden zestaw notatek na drugi, zamiast oddać ci wszystko.",
   "Połączenie obu to dokładnie to, czego JW Library nie potrafi, i o tym jest reszta tej strony. Ale najpierw poszukiwania: ludzie regularnie mają więcej kopii, niż pamiętają, że zrobili.",
  ],
  "steps": [
   ("Przeszukaj każde miejsce, gdzie może być kopia", "Sprawdź pocztę (szukaj „jwlibrary” albo „kopia”), Google Drive, iCloud Drive, OneDrive, Dropbox i folder pobranych na komputerze. Kopie to małe pliki, o których zapisaniu łatwo zapomnieć."),
   ("Sprawdź swoje pozostałe urządzenia", "Jeśli kiedykolwiek używałeś JW Library na tablecie albo komputerze, ma on własne dane studium — utwórz z niego kopię już teraz, aby zachować wszystko, co zawiera."),
   ("Przywróć to, co znajdziesz, na nowym telefonie", "Zainstaluj JW Library na nowym urządzeniu, a potem Kopia zapasowa i przywracanie → Przywróć i wczytaj plik .jwlibrary. Twoje notatki, wyróżnienia i zakładki wrócą."),
   ("Scal, jeśli znajdziesz więcej niż jedną kopię", "Różne urządzenia albo daty mogą zawierać unikatowe notatki. Nie wybieraj tylko jednej — wczytaj wszystkie na jwsync.org, scal je w jeden kompletny plik i przywróć go. Nic nie zostanie pominięte."),
  ],
  "sections": [
   ("Jeśli nigdzie nie ma kopii",
    "Bądź ze sobą szczery od razu: jeśli jedyny egzemplarz Twoich notatek żył na zgubionym telefonie i nigdy nie wyeksportowałeś kopii, JW Library nie przechowuje kopii w chmurze, z której można by przywrócić. To boli — i dokładnie dlatego poniższy nawyk jest tak ważny."),
   ("Aby nigdy więcej tu nie trafić",
    "Ustaw comiesięczne przypomnienie o kopii zapasowej i przechowuj każdy plik .jwlibrary poza telefonem (wysłanie sobie e-mailem w zupełności wystarczy). JW Sync może nawet Ci przypominać i scalać urządzenia według harmonogramu. Plik, który leży w Twojej skrzynce, przetrwa każdy telefon."),
   ("Gdzie kopia może już istnieć",
    "Zanim uznasz, że jej nie ma, sprawdź wszędzie, gdzie plik mógł zostać zapisany: foldery Pobrane i Dokumenty każdego komputera, do którego podłączałeś telefon, wysłane wiadomości, komunikatory, przez które mogłeś wysyłać plik, i każde konto w chmurze, z którego korzystasz. Ludzie często utworzyli kopię raz, wiele miesięcy temu, i zapomnieli — a kopia sprzed kilku miesięcy wciąż zawiera zdecydowaną większość biblioteki studium."),
   ("Przywracanie na inny telefon lub platformę",
    "Urządzenie zastępcze nie musi odpowiadać zgubionemu. Kopia z telefonu z Androidem przywraca się na iPhonie i odwrotnie, bo format jest identyczny na Androidzie, iOS, iPadOS i Windows. Zainstaluj JW Library na nowym urządzeniu, zaktualizuj do bieżącej wersji, a potem przywróć przez Studium osobiste → Kopia zapasowa i przywracanie."),
   ("Jeśli masz tylko starą albo częściową kopię",
    "Przywróć ją mimo to. Odzyskanie większości notatek to nie nagroda pocieszenia — to wynik. Jeśli później znajdziesz drugą, inną kopię, obie da się scalić w jeden plik zawierający wszystko z obu, więc przywrócenie starszej teraz nie przeszkodzi w uzupełnieniu jej później."),
   ("Czego nie da się odzyskać",
    "Jeśli kopia nie istnieje w żadnej postaci, osobistych danych studium nie da się odzyskać. Są przechowywane wyłącznie w prywatnej pamięci aplikacji na urządzeniu, a ani JW Library, ani chmurowa kopia na poziomie telefonu nie zachowują ich niezawodnie. Warto to powiedzieć wprost, bo właśnie dlatego procedura opisana na tej stronie w ogóle istnieje."),
   ("Sprawdź, zanim zdalnie wyczyścisz urządzenie",
    "Jeśli telefon jest zgubiony, a nie zniszczony, i rozważasz zdalne wymazanie, najpierw poszukaj istniejących kopii — wymazanie jest nieodwracalne i odbiera ostatnią szansę na utworzenie kopii. Jeśli urządzenie po prostu gdzieś zawieruszyło się i wciąż jest dostępne, zdalne utworzenie kopii nie jest możliwe, ale dane pozostają nienaruszone, dopóki telefon nie zostanie wyczyszczony ani zresetowany."),
   ("Jak sprawić, żeby to się nie powtórzyło",
    "Powodem, dla którego zgubiony telefon kosztuje ludzi lata studium, jest to, że jedyny egzemplarz był na telefonie. Gdy przywrócisz dane na urządzeniu zastępczym, tego samego dnia umieść kopię gdzieś poza nim i powtarzaj to w rytmie, którego naprawdę dotrzymasz. Pliki są na tyle małe, że przechowywanie ich wszystkich bezterminowo nic nie kosztuje."),
   ("Jeśli kopii naprawdę nie ma",
    "Wtedy uczciwa odpowiedź brzmi: notatek nie da się odzyskać, i lepiej to usłyszeć, niż szukać dalej. To, co możesz zrobić, to sprawić, aby ta strata była ostatnią: zainstaluj JW Library na urządzeniu zastępczym i zanim odbudujesz coś, czego szkoda byłoby stracić, utwórz kopię i umieść ją poza urządzeniem. Od tej chwili to samo zdarzenie nie będzie Cię nic kosztować."),
  ],
  "faq": [
   ("Czy JW Sync odzyska notatki z telefonu, którego już nie mam?", "Żadne narzędzie tego nie zrobi — odzyskiwanie zależy od istnienia gdzieś pliku kopii. Zadaniem JW Sync jest odczytywanie, naprawianie i scalanie kopii, które masz."),
   ("Moja kopia jest stara — czy warto ją przywracać?", "Zdecydowanie. Stara kopia z większością notatek jest lepsza niż zaczynanie od zera, a później możesz scalić ją z czymkolwiek nowszym, co znajdziesz."),
   ("Czy JW Library przechowuje kopię moich notatek w chmurze?", "Nie. Osobiste dane studium zostają na urządzeniu, chyba że sam utworzysz plik kopii."),
   ("Czy da się odzyskać notatki z telefonu z rozbitym ekranem?", "Czasem — jeśli telefon wciąż się włącza i da się nim sterować albo serwis potrafi wyświetlić obraz, JW Library nadal może utworzyć kopię. Dane są nienaruszone, dopóki nienaruszona jest pamięć."),
   ("Czy stara kopia przywróci się do bieżącej aplikacji?", "Tak. JW Library czyta starsze formaty kopii. Najpierw zaktualizuj aplikację i przywracaj do bieżącej wersji."),
   ("Znalazłem dwie stare kopie — której użyć?", "Żadnej osobno. Scal je: wynik będzie zawierał wszystko z obu, łącznie z tym, co było w starszym pliku, a zostało usunięte przed powstaniem nowszego."),
   ("Czy mogę sprawdzić zawartość kopii przed jej przywróceniem?", "Tak. Otwórz plik w przeglądarce i przejrzyj najpierw jego notatki, wyróżnienia i zakładki, aby wiedzieć, co przywracasz."),
  ],
 },

 "handle-merge-conflicts": {
  "title": "Ta sama notatka edytowana na dwóch urządzeniach? Obsługa konfliktów scalania",
  "h1": "Obsługa konfliktów scalania: ta sama notatka na dwóch urządzeniach",
  "description": "Gdy edytujesz tę samą notatkę JW Library inaczej na dwóch urządzeniach, scalanie musi wybrać zwycięzcę. Przegląd konfliktów pokazuje obie wersje obok siebie, abyś zdecydował Ty — nic nie ginie.",
  "intro": [
   "Większość scalania przebiega bez wysiłku — notatki występujące tylko na jednym urządzeniu po prostu się łączą. Jedyny przypadek wymagający decyzji to prawdziwy konflikt: ta sama notatka, edytowana inaczej na dwóch urządzeniach, przez co kopie nie zgadzają się co do jej treści. JW Sync nigdy nie zgaduje po cichu; oddaje wybór Tobie.",
  ],
  "steps": [
   ("Wczytaj obie kopie", "Na jwsync.org wczytaj pliki .jwlibrary z obu urządzeń. JW Sync porównuje je w trakcie scalania."),
   ("Otwórz przegląd konfliktów", "Jeśli jakieś notatki są w konflikcie, przegląd je wypisze. Wszystko, co nie było w konflikcie, jest już scalone — ten krok dotyczy tylko prawdziwych rozbieżności."),
   ("Porównaj obok siebie", "Każdy konflikt pokazuje obie wersje z porównaniem słowo po słowie, podświetlającym dokładnie to, co się różni. „Zaproponuj najlepszą” może wybrać za Ciebie pełniejszą wersję albo wybierasz Ty, którą zachować — dla każdej notatki osobno."),
   ("Zakończ i przywróć", "Gdy wszystkie konflikty zostaną rozstrzygnięte, pobierz scalony plik i przywróć go. Oba urządzenia są teraz zgodne, z wybraną przez Ciebie wersją każdej notatki."),
  ],
  "sections": [
   ("Dlaczego to lepsze niż zachowywanie najnowszej",
    "„Wygrywa najnowsza” po cichu usuwa zmiany, które mogłeś chcieć zachować. Może starsza wersja miała akapit, który przypadkiem usunąłeś na drugim urządzeniu. Zobaczenie obu, słowo po słowie, sprawia, że nigdy nie stracisz tekstu, nie wiedząc o tym — a o to właśnie chodzi w scalaniu zamiast nadpisywania."),
   ("Skąd w ogóle biorą się konflikty",
    "Zwykle z edytowania offline na dwóch urządzeniach między scaleniami albo z przywrócenia starej kopii i późniejszego jej uzupełniania. Scalanie według regularnego harmonogramu utrzymuje liczbę konfliktów na niskim poziomie, a różnice świeżo w pamięci."),
  ],
  "faq": [
   ("Czy będę musiał przejrzeć setki konfliktów?", "Rzadko. W konflikcie są tylko notatki edytowane inaczej po obu stronach; nowe notatki i notatki zmienione tylko na jednym urządzeniu scalają się automatycznie. Większość scaleń ma kilka konfliktów albo żadnego."),
   ("Czy mogę zmienić zdanie po wyborze?", "Tak — nic nie jest zapisywane na urządzeniu, dopóki nie przywrócisz scalonego pliku, a Twoje pierwotne kopie nigdy nie są zmieniane, więc możesz wykonać scalanie ponownie."),
  ],
 },

 "export-jw-library-notes": {
  "title": "Jak wyeksportować notatki JW Library do tekstu lub Markdown",
  "h1": "Eksport notatek JW Library do tekstu, Markdown albo nowej kopii zapasowej",
  "description": "Wydobądź notatki z JW Library: kopiuj je albo eksportuj jako Markdown lub zwykły tekst do użycia gdziekolwiek, albo wyodrębnij wybór do nowego pliku .jwlibrary. Wszystko w przeglądarce.",
  "intro": [
   "Notatki napisane w JW Library łatwo czyta się w aplikacji, a niewygodnie używa gdziekolwiek indziej — w dokumencie, w konspekcie przemówienia, na papierze albo w rękach kogoś, kto nie korzysta z aplikacji. Eksport to rozwiązuje, a główna decyzja dotyczy nie tego, jak eksportować, lecz ile: przefiltrowany eksport jest niemal zawsze bardziej użyteczny niż wszystko naraz.",
   "Twoje notatki nie muszą być uwięzione w jednej aplikacji. Czasem chcesz mieć je jako zwykły tekst — aby wkleić do konspektu przemówienia, dokumentu albo własnej aplikacji do notatek — a czasem potrzebujesz czystej kopii zawierającej tylko część. Eksplorator studium robi jedno i drugie, odczytując Twoją kopię w całości w przeglądarce.",
  ],
  "steps": [
   ("Wczytaj swoją kopię", "Utwórz kopię w JW Library (Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową), a potem otwórz jwsync.org i wczytaj ją do Eksploratora studium."),
   ("Znajdź notatki, o które Ci chodzi", "Użyj wyszukiwania oraz filtrów koloru, etykiety i publikacji, aby zawęzić wybór dokładnie do interesujących Cię notatek — jedna publikacja, jedna etykieta, jeden temat."),
   ("Skopiuj albo wyeksportuj jako Markdown lub tekst", "Skopiuj notatki jako Markdown albo zwykły tekst, aby wkleić je gdziekolwiek. Formatowanie (pogrubienie, kursywa, listy) zostaje zachowane, więc uporządkowane notatki pozostają uporządkowane."),
   ("Albo wyodrębnij do nowej kopii", "Wolisz plik? Wyeksportuj wybór albo zakres dat do nowego pliku .jwlibrary — przydatne do archiwizowania projektu albo przekazania konkretnego zestawu notatek na inne urządzenie."),
  ],
  "sections": [
   ("Po co w ogóle eksportować",
    "Notatki są bardziej użyteczne, gdy mogą podróżować: do dokumentu na punkt zebrania, do osobistej wiki, do wydruku dla kogoś, kto nie korzysta z aplikacji. Markdown zachowuje strukturę, pozostając czytelnym jako zwykły tekst wszędzie."),
   ("Wybór formatu",
    "Zwykły tekst jest najbardziej przenośny i czysto wkleja się do dowolnego dokumentu czy wiadomości. Sformatowany wynik zachowuje strukturę dłuższych notatek i nadaje się do druku albo udostępniania. Jeśli chcesz później mieć notatki z powrotem w JW Library — na innym urządzeniu albo w cudzej bibliotece — zachowaj sam plik .jwlibrary, a nie eksport tekstowy, bo tylko on zachowuje powiązania między notatkami, wyróżnieniami, etykietami i dokładnym miejscem w publikacji, do którego są przypisane."),
   ("Eksport tylko części biblioteki",
    "Pełny eksport wieloletniego studium rzadko jest tym, czego chcesz. Wcześniejsze zawężenie — do etykiety, publikacji, koloru wyróżnienia albo zakresu dat — daje coś, z czego naprawdę da się skorzystać, na przykład wszystkie notatki oznaczone pod przemówienie albo wszystko napisane w czasie jednego kongresu. Te same filtry, które zawężają widok, zawężają eksport, więc dostajesz dokładnie to, co widzisz."),
   ("Co podróżuje z tekstem, a co nie",
    "Eksport niesie Twoje słowa. Nie niesie powiązań łączących notatkę z konkretnym akapitem konkretnej publikacji, bo te odwołania mają sens tylko wewnątrz JW Library. To praktyczny powód, aby trzymać zarówno kopie, jak i eksporty: eksport służy do czytania, drukowania i udostępniania poza aplikacją, a plik .jwlibrary to coś, co wstawia notatki z powrotem do biblioteki wraz z całym kontekstem."),
   ("Zebranie wszystkiego do jednego przemówienia lub zadania",
    "To najczęstszy powód eksportu. Odfiltruj według etykiety, publikacji albo zakresu dat, pod którym leży materiał, sprawdź wynik i wyeksportuj tylko to. Otrzymasz jeden dokument z odpowiednimi notatkami i wyróżnionymi fragmentami w kolejności ich występowania, a nie nieporęczny zrzut całej biblioteki."),
   ("Udostępnianie notatek innym",
    "Ludzie mają na myśli dwie różne rzeczy, mówiąc „udostępnić”. Jeśli druga osoba chce przeczytać Twoje notatki, właściwy jest eksport tekstowy — otwiera się wszędzie i nie wymaga specjalnego oprogramowania. Jeśli chce mieć notatki we własnym JW Library, przypisane do tych samych akapitów i z etykietami oraz kolorami, wtedy potrzebny jest plik .jwlibrary, bo eksport tekstowy nie potrafi niczego wstawić z powrotem do aplikacji."),
   ("Archiwum, które przeczytasz także później",
    "Eksporty warto robić także dla nich samych. Kopia Twoich notatek w zwykłym tekście otworzy się jeszcze za trzydzieści lat w oprogramowaniu, którego nikt jeszcze nie napisał, a tego nie obieca żaden format związany z aplikacją. Trzymanie obu — .jwlibrary do przywracania i eksportu tekstowego do czytania — kosztuje prawie nic i zabezpiecza obie przyszłości."),
   ("Eksport czy kopia zapasowa — czego potrzebujesz",
    "Odpowiadają na różne pytania. Eksport służy do korzystania z notatek poza JW Library: czytania, drukowania, cytowania, wysyłania komuś. Kopia .jwlibrary służy do wstawienia ich z powrotem do JW Library, na tym czy innym urządzeniu, z każdym powiązaniem, etykietą i kolorem. Jedno nie zastępuje drugiego i nie ma powodu, aby nie mieć obu."),
  ],
  "faq": [
   ("Czy eksport zmienia moje notatki w JW Library?", "Nie. Eksport odczytuje kopię Twojej kopii zapasowej w przeglądarce; Twój pierwotny plik i aplikacja pozostają nietknięte."),
   ("Czy mogę wyeksportować wszystko naraz?", "Tak — wyczyść filtry, aby wybrać całą bibliotekę, albo najpierw zawęź, aby wyeksportować tylko część."),
   ("Czy mogę przenieść notatki do Worda albo Dokumentów Google?", "Tak — wyeksportuj jako tekst i wklej. Tekst trafia tam z zachowaną strukturą i można go dalej sformatować."),
   ("Czy wyróżnienia eksportują się tak samo jak notatki?", "Tak, wraz z wyróżnionym fragmentem i jego kolorem, więc wydruk pokazuje zarówno to, co zaznaczyłeś, jak i to, co napisałeś."),
   ("Czy mogę wyeksportować wszystko naraz?", "Tak, choć przefiltrowany eksport jest zwykle bardziej użyteczny. Całość można wyeksportować za jednym razem, gdy potrzebujesz pełnej kopii."),
   ("Czy mogę wyeksportować odpowiedzi wpisane w pytaniach do studium?", "Tak. Wpisane odpowiedzi są częścią Twoich osobistych danych studium i można je wyeksportować razem z notatkami i wyróżnieniami."),
   ("Czy eksport uwzględni, do której publikacji należy każda notatka?", "Tak, eksport wskazuje, skąd pochodzi każda notatka, nawet jeśli samo powiązanie działa tylko wewnątrz JW Library."),
   ("Czy eksport coś zmienia w mojej bibliotece?", "Nie. Eksport odczytuje Twoje dane i zapisuje osobny plik; nic w JW Library nie jest zmieniane, przenoszone ani usuwane."),
   ("Czy mogę eksportować z kopii zapasowej zamiast z aplikacji?", "Tak. Plik .jwlibrary można otworzyć bezpośrednio i wyeksportować jego notatki, co przydaje się, gdy potrzebne notatki są w starej kopii, a nie na bieżącym urządzeniu."),
  ],
 },


 "organize-jw-library-tags": {
  "title": "Jak uporządkować i wyczyścić etykiety w JW Library",
  "h1": "Porządkowanie etykiet JW Library: zmiana nazw, scalanie i czyszczenie zbiorcze",
  "description": "Etykiety mnożą się przez lata studium. Zmień nazwę etykiety we wszystkich notatkach, scal duplikaty i usuń te, których już nie używasz — zbiorczo, w przeglądarce, z pełnym cofaniem.",
  "intro": [
   "Etykiety są sposobem na odnajdywanie notatek później, ale po kilku latach się rozrastają. Kończysz z „Służba”, „służba” i „Służba polowa”, które znaczą to samo, z etykietami utworzonymi raz i nigdy więcej nieużytymi oraz z niekonsekwentnym nazewnictwem, przez które filtrowanie przestaje być wiarygodne. JW Library nie daje żadnego sposobu, aby naprawić to na dużą skalę. Eksplorator studium daje.",
  ],
  "steps": [
   ("Wczytaj kopię do Eksploratora studium", "Na jwsync.org wczytaj plik .jwlibrary. Odfiltruj według etykiety, aby zobaczyć każdą etykietę i liczbę notatek, które ją mają."),
   ("Zmień nazwę etykiety we wszystkich jej notatkach", "Zmieniaj etykiety zbiorczo: zmień nazwę raz, a zaktualizuje się każda notatka, która jej używa — koniec z poprawianiem notatek jedna po drugiej, aby naprawić pisownię."),
   ("Scal duplikaty", "Przypisz notatki ze zduplikowanej etykiety do właściwej, a potem usuń pustą duplikat. „Służba” i „służba” stają się jedną czystą etykietą."),
   ("Usuń etykiety, których już nie używasz", "Zaznacz i usuń nieaktualne etykiety zbiorczo. Wszystko da się cofnąć, więc zbyt gorliwe porządki nigdy nie są ostateczne."),
   ("Wyeksportuj uporządkowaną bibliotekę", "Pobierz zmieniony plik .jwlibrary i przywróć go w JW Library. Twoje etykiety są spójne wszędzie."),
  ],
  "sections": [
   ("System etykiet, który naprawdę pomaga",
    "Gdy etykiety są spójne, filtrowaniu można zaufać — jedno dotknięcie pokazuje każdą notatkę na dany temat, we wszystkich publikacjach. To różnica między etykietami jako bałaganem a etykietami jako prawdziwym indeksem Twojego studium."),
   ("Spójne etykiety zamieniają udostępnianie w dwa kliknięcia",
    "Wybór notatek na stronie udostępniania ma własny filtr etykiet, więc czysta etykieta to również najszybszy sposób na wysłanie komuś zestawu notatek: wybierz etykietę, kliknij Zaznacz wszystkie, utwórz plik. Niechlujne etykiety kosztują Cię dwa razy — gdy szukasz notatek i gdy próbujesz je udostępnić."),
  ],
  "faq": [
   ("Czy zbiorcza zmiana etykiet ruszy treść notatek?", "Nie — zmienia tylko to, jakie etykiety są przypisane. Tytuły i treść Twoich notatek pozostają dokładnie takie, jak napisane."),
   ("Czy da się cofnąć, jeśli popełnię błąd?", "Tak. Eksplorator studium ma pełne cofanie i ponawianie, a Twoja pierwotna kopia nigdy nie jest zmieniana — zmiany trafiają do eksportowanej kopii."),
  ],
 },

 "manage-jw-library-highlights": {
  "title": "Jak zarządzać wyróżnieniami JW Library i zmieniać ich kolory",
  "h1": "Zarządzanie wyróżnieniami JW Library: zbiorcza zmiana kolorów i porządkowanie",
  "description": "Zaprowadź porządek w latach wyróżnień JW Library: zmieniaj kolory zbiorczo, nadaj swojemu kodowi kolorów spójne znaczenie i przeglądaj wszystkie wyróżnienia w jednym miejscu. W przeglądarce.",
  "intro": [
   "Kolory wyróżnień pomagają tylko wtedy, gdy znaczą coś spójnego. Z czasem wyróżnienia u większości osób się rozmywają — żółty znaczył coś innego w 2019 roku niż teraz, a w JW Library nie ma sposobu, aby zobaczyć je wszystkie razem albo poprawić na dużą skalę. Eksplorator studium zbiera każde wyróżnienie w jednym widoku i pozwala zmieniać kolory zbiorczo.",
  ],
  "steps": [
   ("Wczytaj swoją kopię", "Na jwsync.org otwórz plik .jwlibrary w Eksploratorze studium i przejdź na zakładkę Wyróżnienia."),
   ("Przeglądaj i filtruj swoje wyróżnienia", "Zobacz każde wyróżnienie na jednej liście, filtruj według koloru albo publikacji i przeszukuj wyróżniony tekst oraz powiązane notatki."),
   ("Zmieniaj kolory zbiorczo", "Zaznacz wiele wyróżnień i zmień ich kolor razem — na przykład ujednolić wszystko, co miało znaczyć „kluczowy werset”, do jednego koloru w całej bibliotece."),
   ("Edytuj też powiązane notatki", "Tam, gdzie do wyróżnienia dołączona jest notatka, edytuj jej tytuł i treść również tutaj."),
   ("Wyeksportuj i przywróć", "Pobierz zmieniony plik .jwlibrary i przywróć go w JW Library, aby Twój spójny kod kolorów był na każdym urządzeniu."),
  ],
  "sections": [
   ("Zdecyduj, co znaczą Twoje kolory",
    "Prosty schemat — jeden kolor na główne myśli, jeden na wersety do zapamiętania, jeden na pytania do zbadania — zamienia wyróżnienia z ozdoby w narzędzie studium. Zbiorcza zmiana kolorów pozwala zastosować ten schemat wstecznie do lat czytania."),
  ],
  "faq": [
   ("Czy mogę zobaczyć wyróżnienia bez dołączonej notatki?", "Tak — zakładka Wyróżnienia pokazuje je wszystkie, z powiązaną notatką albo bez."),
   ("Czy zmiana koloru wpływa na sam tekst?", "Nie, zmienia jedynie kolor wyróżnienia; tekst publikacji i Twoje notatki pozostają nietknięte."),
  ],
 },

 "jw-library-study-answers": {
  "title": "Przeglądanie i edycja odpowiedzi wpisanych w JW Library",
  "h1": "Odnajdywanie odpowiedzi do studium z JW Library w jednym miejscu",
  "description": "Twoje wpisane odpowiedzi na pytania z artykułów do studium i podręczników są ukryte w kopii zapasowej. Zakładka Odpowiedzi do studium w Eksploratorze studium pozwala je wszystkie odczytać, przeszukać i zmienić naraz.",
  "intro": [
   "Studiując, wpisujesz odpowiedzi w pola artykułów do studium, Strażnicy i podręczników do zebrań. Zapisują się w Twojej kopii zapasowej — ale JW Library pokazuje każdą z nich ukrytą we własnej publikacji. Nie ma jednego miejsca, w którym przejrzysz wszystko, co napisałeś. Zakładka Odpowiedzi do studium w Eksploratorze studium jest właśnie takim miejscem.",
  ],
  "steps": [
   ("Wczytaj kopię do Eksploratora studium", "Na jwsync.org wczytaj plik .jwlibrary i otwórz zakładkę Odpowiedzi do studium."),
   ("Przeczytaj wszystkie odpowiedzi razem", "Każda wpisana odpowiedź pojawia się na jednej przeszukiwalnej liście, więc jednym rzutem oka ogarniesz całe swoje przemyślenia z artykułu do studium."),
   ("Szukaj i edytuj", "Znajdź odpowiedź po jej treści, a potem popraw ją i dopracuj na miejscu — pomocne przy powtórce przed zebraniem albo przy porządkowaniu pospiesznych sformułowań."),
   ("Wyeksportuj albo przywróć", "Przywróć zmieniony plik, aby przenieść zmiany z powrotem do JW Library, albo skopiuj odpowiedzi jako tekst na potrzeby przemówienia czy własnego archiwum."),
  ],
  "sections": [
   ("Dlaczego przydaje się to przed zebraniami",
    "Przejrzenie przygotowanych odpowiedzi na jednej ciągłej liście — zamiast przewijania każdego akapitu w aplikacji — to szybszy sposób na odświeżenie tego, co planowałeś powiedzieć, i na wyłapanie odpowiedzi pozostawionych pustych."),
  ],
  "faq": [
   ("Czy to to samo co moje osobiste notatki?", "Nie — odpowiedzi do uzupełnienia to wpisy w polach odpowiedzi publikacji. Eksplorator studium pokazuje je na osobnej zakładce, oddzielnie od swobodnych notatek."),
   ("Czy coś jest wysyłane, aby odczytać moje odpowiedzi?", "Nie. Jak wszystko w JW Sync, Twoja kopia jest odczytywana lokalnie w przeglądarce i nigdy nigdzie nie trafia."),
  ],
 },

 "extract-jw-library-notes-by-date": {
  "title": "Wyodrębnianie notatek JW Library z zakresu dat do nowej kopii",
  "h1": "Wyodrębnianie zakresu dat notatek JW Library do nowej kopii zapasowej",
  "description": "Wyciągnij tylko notatki z określonego okresu — roku służbowego, kongresu, projektu studyjnego — do osobnej, czystej kopii .jwlibrary. W całości w Twojej przeglądarce.",
  "intro": [
   "Czasem potrzebujesz wycinka biblioteki, a nie całości: tegorocznych notatek do powtórki, wszystkiego z kongresu albo materiałów z jednego projektu, aby komuś je przekazać. Eksplorator studium potrafi wyodrębnić notatki z zakresu dat do zupełnie nowej kopii .jwlibrary, zostawiając główną bibliotekę nietkniętą.",
  ],
  "steps": [
   ("Wczytaj swoją kopię", "Na jwsync.org otwórz plik .jwlibrary w Eksploratorze studium."),
   ("Ustaw zakres dat", "Wybierz datę początkową i końcową dla interesujących Cię notatek — rok służbowy, miesiąc, daty konkretnego wydarzenia."),
   ("Wyodrębnij do nowej kopii", "Wyeksportuj pasujące notatki do nowego pliku .jwlibrary. Będzie zawierał wyłącznie notatki, wyróżnienia i etykiety z tego okresu."),
   ("Skorzystaj z wyodrębnionego pliku", "Przywróć go w JW Library do skupionej powtórki, zarchiwizuj albo udostępnij komuś, kto potrzebuje tylko tego wycinka."),
  ],
  "sections": [
   ("Dobre powody, aby wyodrębniać według daty",
    "Roczne archiwum Twojego studium; czysty plik notatek z kongresu do osobnego przechowywania; przekazanie partnerowi studium wyłącznie notatek z projektu, nad którym pracowaliście razem; albo podzielenie ogromnej biblioteki na możliwe do ogarnięcia, datowane części — a wszystko to bez ruszania głównej kopii."),
  ],
  "faq": [
   ("Czy wyodrębnienie usuwa te notatki z mojej biblioteki?", "Nie. Kopiuje pasujące notatki do nowego pliku; Twoja pierwotna kopia zachowuje wszystko."),
   ("Której daty używa — kiedy napisałem notatkę czy kiedy ją ostatnio zmieniłem?", "Używa własnych znaczników czasu notatki w kopii, więc zakres odzwierciedla, kiedy notatki powstały albo zostały zmienione."),
  ],
 },

 "connect-jw-library-notes-study-map": {
  "title": "Zobacz, jak łączą się Twoje notatki JW Library — Mapa studium",
  "h1": "Mapa studium: prywatny graf wiedzy z Twoich notatek JW Library",
  "description": "Mapa studium zamienia Twoje notatki JW Library w interaktywną sieć, łącząc je wspólnymi wersetami, wspólnymi etykietami i podobnym sformułowaniem — abyś zobaczył tematy przewijające się przez Twoje studium.",
  "intro": [
   "W latach notatek kryją się powiązania, których nigdy nie widziałeś: ten sam werset cytowany w kilkunastu wpisach, temat, do którego wciąż wracasz, myśli, które odbijają się echem w różnych publikacjach. Mapa studium rysuje te powiązania jako interaktywny graf, dzięki czemu kształt Twojego własnego studium staje się widoczny.",
  ],
  "steps": [
   ("Otwórz stronę statystyk studium i wczytaj kopię", "Wejdź na jwsync.org/highlights.html i wczytaj plik .jwlibrary. Mapa studium odczytuje go w Twojej przeglądarce."),
   ("Otwórz Mapę studium", "Uruchom mapę, aby zobaczyć swoje notatki jako połączone punkty, powiązane wspólnymi wersetami, wspólnymi etykietami i podobnym sformułowaniem."),
   ("Poznaj powiązania", "Przełączaj się między widokami Tematy i Notatki, najedź kursorem, aby podświetlić powiązania notatki, przeciągaj elementy i użyj suwaka siły, aby pokazać tylko najbliższe połączenia. Tryb pełnoekranowy daje przestrzeń do eksploracji."),
   ("Twórz i zapisuj łańcuchy studium", "Rysuj własne ręczne „łańcuchy studium” między powiązanymi notatkami, aby uchwycić tok rozumowania, i wyeksportuj mapę jako obraz PNG, aby ją zachować albo udostępnić."),
  ],
  "sections": [
   ("Co pokazuje mapa",
    "Skupiska pokazują tematy, które studiujesz najczęściej; werset powiązany z wieloma notatkami wskazuje fragment, do którego wciąż wracasz; odosobniona notatka może być wątkiem wartym rozwinięcia. To sposób, aby studiować własne studium — i przygotowywać przemówienia, podążając za powiązaniami, które już stworzyłeś."),
  ],
  "faq": [
   ("Czy mapa wymaga wielu notatek, aby była przydatna?", "Nawet skromna biblioteka już pokazuje powiązania; im bogatsze notatki, tym więcej mapa ujawnia. Bardzo małe biblioteki wyświetlą podpowiedź, aby najpierw dodać więcej notatek."),
   ("Czy mapa jest prywatna?", "Całkowicie. Powstaje w Twojej przeglądarce z Twojej kopii i nigdy nie jest wysyłana; nawet eksport PNG tworzy się na Twoim urządzeniu."),
  ],
 },


 "review-old-jw-library-notes": {
  "title": "Jak powtarzać stare notatki JW Library (żeby zostały w pamięci)",
  "h1": "Powtarzanie starych notatek JW Library z Przypomnieniem — po trochu, ale często",
  "description": "Notatki, do których nie wracasz, to notatki, które zapominasz. Przypomnienie pokazuje, co napisałeś tego dnia w poprzednich latach, i buduje łagodne powtarzanie z odstępami, aby dawne studium nadal na Ciebie pracowało.",
  "intro": [
   "Większość notatek pisze się raz i nigdy więcej do nich nie wraca. To ciche marnotrawstwo — myśl była warta zapisania, a potem osiadła na dnie biblioteki. Przypomnienie wydobywa Twoje własne dawne notatki z powrotem na wierzch, po kilka naraz, dzięki czemu wracanie do nich staje się małym codziennym nawykiem, a nie projektem „kiedyś”.",
  ],
  "steps": [
   ("Otwórz stronę statystyk studium i wczytaj kopię", "Wejdź na jwsync.org/highlights.html i wczytaj plik .jwlibrary. Przypomnienie odczytuje Twoje notatki lokalnie."),
   ("Zobacz „Tego dnia”", "Przypomnienie wydobywa notatki napisane tego samego dnia w poprzednich latach — „napisane dwa lata temu dzisiaj” — łącząc Cię z dawnym studium w chwili, gdy ma to największe znaczenie."),
   ("Zrób krótką codzienną powtórkę", "Pokazuje kilka notatek do przejrzenia i oznaczenia jako przejrzane. Po trochu, ale często — tak wiedza zostaje na dłużej, a passa rośnie, gdy trzymasz się nawyku."),
   ("Wróć jutro", "Powtarzanie z odstępami planuje ponowne pojawianie się notatek w czasie, więc te warte zapamiętania wracają, aż naprawdę staną się Twoje."),
  ],
  "sections": [
   ("Dlaczego powtarzanie z odstępami działa",
    "Powtórzenie czegoś dokładnie wtedy, gdy masz to zapomnieć, jest znacznie skuteczniejsze niż wkuwanie. Rozkładając kilka notatek na wiele dni, Przypomnienie zamienia Twoją istniejącą bibliotekę w stałą, niskonakładową powtórkę, która systematycznie pogłębia to, czego się uczyłeś."),
  ],
  "faq": [
   ("Gdzie zapisuje się mój postęp w powtórkach?", "W Twojej przeglądarce na Twoim urządzeniu — nie ma konta i nic nie jest wysyłane. Passa i harmonogram należą tylko do Ciebie."),
   ("Czy potrzebuję do tego nowych notatek?", "Nie — Przypomnienie działa na notatkach, które już napisałeś. Im starsza biblioteka, tym przyjemniejsze chwile „tego dnia”."),
  ],
 },

 "jw-library-achievements-streaks": {
  "title": "Passy, poziomy i osiągnięcia studium w JW Library",
  "h1": "Zamień swoje studium JW Library w passy, poziomy i nagrody",
  "description": "Zobacz swoje passy studium, wspinaj się przez 60 poziomów w 12 rangach Drogi studium i odblokuj około 200 osiągnięć — wszystko odczytywane prywatnie z Twojej własnej kopii JW Library.",
  "intro": [
   "Regularność to najtrudniejsza część osobistego studium, a postęp, którego nie widać, łatwo zaniedbać. Strona statystyk studium zamienia historię z Twojej kopii w coś, czemu możesz się przyglądać: passy, poziomy i nagrody odzwierciedlające studium, które naprawdę wykonałeś — bez narzuconych celów, po prostu Twój własny zapis uczyniony widocznym.",
  ],
  "steps": [
   ("Otwórz stronę statystyk studium", "Wejdź na jwsync.org/highlights.html i wczytaj kopię .jwlibrary. Wszystko jest obliczane w Twojej przeglądarce."),
   ("Sprawdź swoje passy", "Zobacz swoją najdłuższą i bieżącą passę studium, rytm tygodniowy oraz najbardziej zajęte godziny i miesiące — puls Twojego nawyku studiowania."),
   ("Wspinaj się Drogą studium", "Przechodź przez 60 poziomów w 12 nazwanych rangach (od Ziarna aż po Wiecznie zielone), z kulą zmieniającą kolor i świętowaniem awansów, na podstawie studium całego życia."),
   ("Zbieraj osiągnięcia", "Odblokuj około 200 nagród od pospolitych po legendarne, w tym tematyczne medale uwzględniające treść; otwórz dowolny medal, aby zobaczyć postęp do kolejnego."),
  ],
  "sections": [
   ("Motywacja bez presji",
    "To nie są cele wyznaczone przez kogoś innego — to lustro tego, co już zrobiłeś. Widok passy, której nie chcesz przerwać, albo prawie osiągniętego poziomu to łagodna zachęta, aby podtrzymać dobry nawyk. A karta do udostępnienia podsumowuje Twój rok, nie ujawniając ani jednej prywatnej notatki."),
  ],
  "faq": [
   ("Czy passy i nagrody aktualizują się same?", "Odzwierciedlają wczytaną kopię, więc utwórz świeżą kopię, aby zobaczyć najnowszy postęp. Nic nie działa w tle."),
   ("Czy coś z tego jest udostępniane albo wysyłane?", "Nie. Wszystko jest obliczane lokalnie z Twojej kopii; jedynie kartę podsumowania możesz udostępnić, jeśli zechcesz, a nie zawiera ona treści notatek."),
  ],
 },

 "share-convention-assembly-notes": {
  "title": "Jak udostępnić notatki z kongresu i zgromadzenia z JW Library",
  "h1": "Udostępnianie notatek z kongresu, zgromadzenia i zebrań",
  "description": "Przekaż rodzinie i znajomym swoje notatki z kongresu, zgromadzenia czy zebrania w małym pliku — bez oddawania całej biblioteki i bez nadpisywania ich notatek. Praktyczne zastosowanie udostępniania notatek.",
  "intro": [
   "Robiłeś staranne notatki przez cały kongres; znajomy, który przegapił część programu, chętnie by je dostał; rodzina chce mieć te myśli do własnej powtórki. Wysłanie całej kopii to przesada, a jej przywrócenie skasowałoby własne notatki odbiorcy. Udostępnianie notatek pozwala przekazać dokładnie te notatki, które chcesz — a odbiorcy zachować wszystko, co już ma.",
  ],
  "steps": [
   ("Wczytaj kopię na stronie udostępniania", "Wejdź na jwsync.org/share.html i wczytaj plik .jwlibrary."),
   ("Wybierz tylko notatki z kongresu", "Wybierz etykietę wydarzenia w filtrze etykiet i kliknij Zaznacz wszystkie — lista zawiera już dokładnie te notatki, które oznaczyłeś. Wyróżnienia powiązane z tymi notatkami jadą razem z nimi."),
   ("Wyślij mały plik udostępniania", "JW Sync tworzy mały plik zawierający tylko te notatki. Wyślij go, jak wolisz — komunikatorem, e-mailem, przez AirDrop. Bez serwera, bez konta."),
   ("Rodzina i znajomi dodają go u siebie", "Każdy otwiera tę samą stronę, wczytuje Twój plik razem ze swoją kopią i otrzymuje nową kopię z dodanymi Twoimi notatkami. Ich własne notatki nigdy nie są nadpisywane, a Twoje zaimportowane notatki przychodzą z etykietą, więc łatwo je znaleźć."),
  ],
  "sections": [
   ("Etykieta czyni to zupełnie prostym",
    "Jeśli oznaczasz notatki etykietą w trakcie wydarzenia (powiedzmy „Kongres 2026”), późniejsze ich wybranie to jedno kliknięcie filtra i Zaznacz wszystkie. Warto zakładać nową etykietę na początku każdego kongresu, zgromadzenia czy specjalnego zebrania właśnie z tego powodu."),
  ],
  "faq": [
   ("Czy mogę udostępnić kilku osobom naraz?", "Tak — plik udostępniania to zwykły plik. Wyślij go dowolnej liczbie osób; każda doda go do swojej biblioteki niezależnie."),
   ("Czy zostanie ujawniona cała moja biblioteka?", "Nie. W pliku są tylko wybrane przez Ciebie notatki; reszta biblioteki pozostaje prywatna."),
  ],
 },

 "share-jw-library-notes-by-tag": {
  "title": "Udostępnij tylko notatki JW Library z jedną etykietą",
  "h1": "Udostępnianie samych notatek z jedną etykietą",
  "description": "Wyślij jeden temat, jeden projekt albo notatki dla jednej osoby zamiast całej biblioteki — a Twoje etykiety pojadą razem z nimi, więc dotrą uporządkowane.",
  "intro": [
   "Etykieta jest zwykle naturalną jednostką udostępniania. Oznaczyłeś wszystko, co zebrałeś na dany temat, wszystko z jednego wydarzenia albo wszystko, co omawiasz z jedną osobą — i to właśnie ten zestaw, a nie cała Twoja biblioteka, jest tym, czego druga osoba naprawdę chce.",
   "Udostępnianie w JW Sync działa notatka po notatce, więc etykieta to po prostu lista, którą zaznaczasz. Notatki zachowują swoje etykiety w drodze na zewnątrz, co oznacza, że osoba, która je otrzyma, będzie mogła odfiltrować dokładnie ten sam zestaw we własnej bibliotece.",
  ],
  "steps": [
   ("Upewnij się, że notatki mają etykietę", "Oznaczaj je w JW Library na bieżąco albo otwórz kopię w Eksploratorze studium na jwsync.org i użyj edytora etykiet, aby dodać etykietę zbiorczo. Konsekwentne etykietowanie teraz sprawia, że udostępnianie później zajmuje minutę."),
   ("Otwórz stronę udostępniania i wczytaj kopię", "Wejdź na jwsync.org/share.html, wybierz Wyślij notatki i wczytaj plik .jwlibrary. Jest odczytywany w Twojej przeglądarce i nigdy nie opuszcza urządzenia."),
   ("Wybierz etykietę w filtrze, a potem Zaznacz wszystkie", "Wybór notatek ma filtr etykiet wypisujący każdą etykietę w kopii wraz z liczbą notatek. Wybierz swoją etykietę, a lista zawęzi się dokładnie do tych notatek; Zaznacz wszystkie zaznaczy je wszystkie. To cały wybór — dwa kliknięcia."),
   ("Utwórz plik i wyślij go", "JW Sync buduje mały plik udostępniania zawierający tylko zaznaczone notatki. Wyślij go czatem, e-mailem albo przez AirDrop — nie ma serwera ani konta po żadnej stronie."),
   ("Dodają go do własnej kopii", "Druga osoba otwiera tę samą stronę, wybiera Odbierz, przegląda notatki i dodaje je do swojej kopii. Twoje etykiety docierają razem z notatkami, plus etykieta oznaczająca import, więc cały zestaw jest i dla niej o jeden filtr."),
  ],
  "sections": [
   ("Dlaczego lepiej udostępnić etykietę niż kopię",
    "Przekazanie pełnej kopii .jwlibrary oddaje wszystko, co kiedykolwiek napisałeś, a jej przywrócenie skasowałoby własne notatki drugiej osoby. Udostępnienie oznaczonego wyboru jest przeciwieństwem w obu tych sprawach: widzi ona tylko to, co wybrałeś, i niczego swojego nie traci."),
   ("Dalsze zawężanie albo udostępnianie kilku etykiet",
    "Filtr etykiet i pole wyszukiwania działają razem: wybierz etykietę, a potem wpisz słowo, aby zawęzić jeszcze bardziej — Zaznacz wszystkie wciąż zaznaczy tylko to, co masz przed sobą. Wyszukiwanie dopasowuje też nazwy etykiet, więc słowo wspólne dla kilku etykiet zbiera je za jednym razem. Każda notatka na liście pokazuje swoje etykiety, więc widzisz, co wysyłasz, zanim to wyślesz."),
   ("Etykiety, które warto mieć do udostępniania",
    "Warto trzymać kilka etykiet, które istnieją wyłącznie po to, aby je udostępniać: nazwa wydarzenia, temat, który badasz dla innych, osoba, z którą studiujesz. Gdy przyjdzie moment, aby coś wysłać, nie trzeba niczego szukać — zestaw jest już gotowy."),
  ],
  "faq": [
   ("Czy moje etykiety przechodzą do drugiej osoby?", "Tak. Udostępnione notatki niosą swoje etykiety, a import jest oznaczany własną etykietą, więc odbiorca może później znaleźć, przejrzeć albo usunąć całą partię."),
   ("Co, jeśli notatka ma kilka etykiet?", "Pojawia się pod każdą z nich w filtrze, a wszystkie jej etykiety podróżują razem z nią. Filtrowanie po jednej etykiecie nigdy nie usuwa pozostałych."),
   ("Czy udostępnianie usuwa notatki z mojej biblioteki?", "Nie. Udostępnianie kopiuje notatki do małego pliku; Twoja kopia i aplikacja pozostają nietknięte."),
   ("Czy mogę wysłać tę samą etykietę kilku osobom?", "Tak — plik udostępniania to zwykły plik. Wyślij go dowolnej liczbie osób, a każda doda go do swojej biblioteki niezależnie."),
  ],
 },


 "share-notes-with-bible-student": {
  "title": "Udostępnij notatki JW Library osobie, z którą studiujesz Biblię",
  "h1": "Udostępnianie notatek do studium osobie, z którą studiujesz Biblię",
  "description": "Wyślij notatki do lekcji — wersety, przykłady, przygotowane myśli — prosto do własnej biblioteki JW Library drugiej osoby, nie ruszając niczego, co sama napisała.",
  "intro": [
   "Gdy przygotowujesz studium, większość pracy ląduje w Twoich własnych notatkach: dodatkowe wersety, przykład, dzięki któremu myśl trafiła, odpowiedź na pytanie zadane w zeszłym tygodniu. Przeczytanie tego na głos to jedno; zostawienie drugiej osobie kopii, którą będzie mogła czytać przez cały tydzień, to zupełnie co innego.",
   "Udostępnianie notatek umieszcza Twoje przygotowane notatki w jej bibliotece jako prawdziwe notatki JW Library, przypisane do tych samych akapitów i wersetów — a nie jako zrzut ekranu czy wiadomość, którą przewinie.",
  ],
  "steps": [
   ("Przygotuj notatki do lekcji w JW Library", "Pisz notatki jak zwykle, przy akapitach i wersetach, które obejmuje lekcja. Nadaj im etykietę — imię osoby albo nazwę publikacji — aby później łatwo wybrać cały zestaw."),
   ("Otwórz stronę udostępniania i wczytaj kopię", "Utwórz kopię (Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową), a potem otwórz jwsync.org/share.html, wybierz Wyślij notatki i wczytaj plik. Nigdy nie opuszcza Twojego urządzenia."),
   ("Zaznacz notatki do tej lekcji", "Odfiltruj wybór według użytej etykiety i kliknij Zaznacz wszystkie albo znajdź i zaznacz je pojedynczo. Utwórz plik udostępniania — cała reszta biblioteki zostaje na miejscu."),
   ("Wyślij i przeprowadź ją przez odbieranie", "Najpierw potrzebuje własnej kopii — Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Potem otwiera jwsync.org/share.html, wybiera Odbierz, wczytuje Twój plik i swoją kopię i pobiera zaktualizowaną kopię."),
   ("Przywraca ją w JW Library", "Kopia zapasowa i przywracanie → Przywróć, wybiera zaktualizowany plik, a Twoje notatki pojawiają się w jej bibliotece obok jej własnych — z etykietą, więc wie, które przyszły od Ciebie."),
  ],
  "sections": [
   ("Jej notatki nigdy nie są nadpisywane",
    "To ważna różnica względem wysłania kopii. Przywracanie zastępuje całą bibliotekę urządzenia; odebranie udostępnionych notatek dodaje do niej. Wszystko, co napisała sama — nawet przy tych samych akapitach — pozostaje dokładnie takie, jakie było."),
   ("Tygodniowy rytm, który zajmuje dwie minuty",
    "Gdy oboje zrobicie to raz, procedura jest krótka: przygotuj, zaznacz, wyślij, przywróć. Wielu uważa, że najwygodniej wysyłać notatki zaraz po przygotowaniu, aby osoba miała je przed studium, a nie po nim."),
  ],
  "faq": [
   ("Czy osoba studiująca potrzebuje konta albo zainstalowanej aplikacji?", "Żadnego konta i nic do zainstalowania poza samym JW Library — strona udostępniania to zwykła strona internetowa."),
   ("Co, jeśli ta osoba nigdy nie robiła kopii zapasowej?", "Najpierw ją tworzy, w JW Library w sekcji Studium osobiste → Kopia zapasowa i przywracanie. Nawet pozornie pusta biblioteka wystarczy; kopia to miejsce, do którego dodawane są udostępnione notatki."),
   ("Czy mogę później cofnąć udostępnienie notatek?", "Plik należy do Ciebie — wysyłasz go albo nie. Gdy ktoś go ma, jest jego, dokładnie jak każda wiadomość, więc udostępniaj to, czym byłoby Ci wygodnie podzielić się na piśmie."),
  ],
 },

 "share-meeting-notes-with-family": {
  "title": "Udostępnij notatki z zebrania rodzinie lub domownikom",
  "h1": "Udostępnianie notatek z tygodniowego zebrania w rodzinie",
  "description": "Ktoś chorował, pracował albo był poza domem — wyślij mu notatki z tygodnia w małym pliku, który doda do własnej biblioteki JW Library, i nikt niczego nie straci.",
  "intro": [
   "W większości domów każdy robi własne notatki na własnym urządzeniu i zawsze ktoś opuszcza zebranie. Przeczytanie swoich notatek przy kolacji zadziała raz; umieszczenie ich w bibliotece drugiej osoby pozwala jej skorzystać z materiału później, w miejscu, w którym naprawdę będzie go szukać.",
   "Ponieważ udostępnianie odbywa się notatka po notatce, a nie kopia po kopii, kilka osób może swobodnie wymieniać się notatkami i niczyja biblioteka nie zostanie nadpisana.",
  ],
  "steps": [
   ("Utwórz kopię urządzenia, na którym robiłeś notatki", "JW Library → Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową."),
   ("Wybierz notatki z tygodnia", "Na jwsync.org/share.html wybierz Wyślij notatki, wczytaj swoją kopię i zaznacz notatki z tego tygodnia — wyszukanie po publikacji szybko je zbierze, a jeśli oznaczasz notatki tygodnia etykietą, filtr etykiet zbierze je jednym kliknięciem."),
   ("Wyślij na czacie rodzinnym", "Utwórz plik udostępniania i wyślij go tak, jak dom i tak się komunikuje — komunikatorem, e-mailem, przez AirDrop. To mały plik zawierający tylko zaznaczone przez Ciebie notatki."),
   ("Każdy dodaje go do własnej kopii", "Otwierają tę samą stronę, wybierają Odbierz, wczytują Twój plik razem z własną kopią, pobierają zaktualizowaną kopię i przywracają ją w JW Library."),
  ],
  "sections": [
   ("Biblioteka każdego zostaje jego własna",
    "Niczyje notatki nie są zastępowane i nikt nie musi oddawać całej swojej biblioteki, aby wziąć udział. Zaimportowane notatki przychodzą pod etykietą, więc każdy od razu widzi, które notatki pochodzą od kogoś innego, i może później usunąć całą partię, jeśli wolałby jej nie zachowywać."),
   ("Wielbienie rodzinne: zbierać zamiast rozpraszać",
    "To samo narzędzie działa też w drugą stronę. Jeśli wszyscy robią notatki podczas wielbienia rodzinnego, jedna osoba może zebrać pliki udostępniania pozostałych w jedną kopię i mieć połączone notatki całego domu z tego samego materiału."),
  ],
  "faq": [
   ("Czy urządzenia dzieci mogą brać udział?", "Każde urządzenie, które uruchomi JW Library i otworzy stronę internetową. Kroki są identyczne na telefonie, tablecie i komputerze."),
   ("Czy musimy być na tej samej platformie?", "Nie. Android, iPhone, iPad i aplikacja dla Windows używają tego samego formatu kopii, więc notatki przechodzą między nimi bez konwersji."),
  ],
 },

 "receive-shared-jw-library-notes": {
  "title": "Ktoś przysłał mi notatki JW Library — jak je otworzyć?",
  "h1": "Dodawanie udostępnionych Ci notatek do własnej biblioteki JW Library",
  "description": "Dostałeś plik z udostępnionymi notatkami albo blok tekstu. Oto jak go podejrzeć i dodać do własnej kopii zapasowej JW Library, nie tracąc ani jednej własnej notatki.",
  "intro": [
   "Udostępnione notatki JW Library przychodzą jako mały plik (z rozszerzeniem .jwshare.json) albo jako blok tekstu wklejony w wiadomości. Samo JW Library nie otworzy żadnego z nich — ale nie jest Ci do tego potrzebne. Strona odbierania w JW Sync odczytuje udostępnione notatki, pokazuje, co zawierają, i zapisuje je do Twojej kopii.",
   "Cała wymiana odbywa się na Twoim urządzeniu. Nie ma konta, nic nie jest wysyłane, a Twoje własne notatki są tylko uzupełniane, nigdy zastępowane.",
  ],
  "steps": [
   ("Najpierw utwórz kopię własnej biblioteki", "W JW Library: Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. To do tego pliku zostaną dodane udostępnione notatki, więc powinien być aktualny."),
   ("Otwórz stronę udostępniania i wybierz Odbierz", "Wejdź na jwsync.org/share.html i wybierz Odbierz notatki."),
   ("Wczytaj to, co Ci przysłano", "Wybierz plik .jwshare.json albo wklej udostępniony tekst prosto do pola, jeśli przyszedł jako wiadomość. Tak czy inaczej dostaniesz podgląd każdej notatki tylko do odczytu, zanim cokolwiek zostanie zapisane."),
   ("Dodaj je do swojej kopii", "Wczytaj własną kopię, wybierz etykietę dla zaimportowanych notatek i dodaj je. JW Sync zbuduje zaktualizowany plik kopii do pobrania."),
   ("Przywróć zaktualizowaną kopię w JW Library", "Studium osobiste → Kopia zapasowa i przywracanie → Przywróć, wybierz zaktualizowany plik. Udostępnione notatki są już w Twojej bibliotece, przy właściwych akapitach i wersetach."),
  ],
  "sections": [
   ("Nic Twojego nie jest zastępowane",
    "Udostępnione notatki są dodawane jako nowe. Nawet tam, gdzie udostępniona notatka trafia na akapit, przy którym już pisałeś, obie przetrwają — Twoja nietknięta, ich obok. Jedyne, o czym warto pamiętać, to zwykła zasada przywracania: przywracaj zaktualizowaną kopię, a nie starszą."),
   ("Zmieniłeś zdanie później?",
    "Każda zaimportowana notatka ma etykietę, którą wybrałeś przy dodawaniu. Otwórz swoją kopię w Eksploratorze studium, odfiltruj według tej etykiety, a będziesz mógł przejrzeć albo usunąć całą partię za jednym razem."),
  ],
  "faq": [
   ("Plik przyszedł z nazwą zmienioną na .txt albo otworzył się jako tekst — czy jest zepsuty?", "Nie. Komunikatory często tak robią. Skopiuj tekst i wklej go do pola odbierania; działa dokładnie tak samo."),
   ("Czy potrzebuję całej kopii nadawcy?", "Nie. Plik udostępniania zawiera tylko te notatki, które wybrał do wysłania — nic więcej z jego biblioteki."),
   ("Czy coś jest wysyłane, gdy podglądam notatki?", "Nie. Odczyt udostępnionego pliku, jego podgląd i zapis zaktualizowanej kopii odbywają się w Twojej przeglądarce na Twoim urządzeniu."),
  ],
 },

 "share-notes-with-study-group": {
  "title": "Udostępnij notatki z badań grupie studyjnej",
  "h1": "Udostępnianie badań grupie — i zbieranie ich notatek z powrotem",
  "description": "Jeden plik, wiele osób: wyślij zestaw notatek z badań wszystkim, którzy studiują ten sam temat, i zbierz to, co odeślą, w jeden własny zestaw.",
  "intro": [
   "Gdy kilka osób zgłębia ten sam temat, materiał zwykle się rozprasza — jedna osoba znalazła odsyłacze, druga tło historyczne, trzecia przykłady. Czytanie nawzajem swoich zrzutów ekranu to nie to samo co posiadanie materiału we własnej bibliotece, przy tych samych wersetach, z możliwością przeszukania za rok.",
   "Ponieważ plik udostępniania to zwykły plik, jeden eksport obsłuży całą grupę, a ten sam mechanizm przyniesie ich pracę z powrotem do Ciebie.",
  ],
  "steps": [
   ("Oznaczaj swoje badania etykietą w trakcie zbierania", "Nadaj tematowi etykietę w JW Library, aby zestaw trzymał się razem. W Eksploratorze studium możesz dodać etykietę zbiorczo, jeśli nie oznaczyłeś ich od razu."),
   ("Utwórz jeden plik udostępniania dla grupy", "Na jwsync.org/share.html wybierz Wyślij notatki, wczytaj swoją kopię, wybierz etykietę tematu w filtrze etykiet, kliknij Zaznacz wszystkie i utwórz plik."),
   ("Opublikuj go raz", "Wyślij ten sam plik wszystkim — na czat grupowy, e-mailem do kilku osób, jak grupa już się komunikuje. Nie ma osobnej konfiguracji dla każdego ani kopii na serwerze."),
   ("Poproś o ich notatki w zamian", "Każdy może zrobić dokładnie to samo ze swojej strony. Dodawaj kolejno każdy otrzymany plik do swojej kopii, nadając każdemu importowi własną etykietę — imię nadawcy sprawdza się dobrze — abyś zawsze wiedział, czyje to badania."),
  ],
  "sections": [
   ("Jeden wspólny zestaw, wciąż z przypisaniem",
    "Po kilku rundach masz we własnej bibliotece całe badania grupy na dany temat, przy właściwych akapitach i wersetach, z każdym wkładem oznaczonym według źródła. Wyszukiwanie znajduje wszystko naraz; etykiety pozwalają to znowu rozdzielić, kiedy tylko zechcesz."),
   ("Nikt nie musi ujawniać swojej biblioteki",
    "Każdy udostępnia tylko te notatki, które zaznaczy. Reszta biblioteki każdej osoby — osobiste studium, prywatne przypomnienia, wszystko inne — nigdy nie trafia do pliku."),
  ],
  "faq": [
   ("Czy jest limit liczby notatek, które mogę udostępnić naraz?", "Praktycznie nie. Notatki są małe; nawet duży zestaw daje plik, który wyślesz w wiadomości."),
   ("Co, jeśli dwie osoby przyślą mi tę samą notatkę?", "Zobaczysz ją dwa razy, każdą pod etykietą jej nadawcy. Wyszukiwanie w Eksploratorze studium ułatwia wychwycenie i usunięcie niemal identycznych."),
   ("Czy ktoś może odbierać, nic nie wysyłając w zamian?", "Tak. Odbieranie i wysyłanie są niezależne — nikt nie musi się dzielić, aby móc dodać to, co dostał."),
  ],
 },


 "share-talk-preparation-notes": {
  "title": "Przekaż materiały stojące za przemówieniem albo zadaniem",
  "h1": "Przekazywanie materiałów do przemówienia i zadania",
  "description": "Wykonałeś research do przemówienia, punktu albo zadania. Oto jak przekazać go temu, komu przyda się dalej — jako prawdziwe notatki w jego bibliotece albo jako zwykły tekst do dokumentu.",
  "intro": [
   "Przygotowanie rzadko przydaje się tylko raz. Wersety, które wyszukałeś, przeczytane tło, sposób, w jaki ostatecznie ująłeś myśl — ktoś, kto później opracuje ten sam materiał, wolałby zacząć od tego niż od czystej kartki.",
   "JW Sync daje dwa sposoby przekazania tego i pasują one do różnych osób: jako notatki trafiające do biblioteki JW Library drugiej osoby albo jako zwykły tekst, który wklei do dokumentu.",
  ],
  "steps": [
   ("Zbierz materiały pod jedną etykietą", "Przygotowując się, oznaczaj notatki tematem albo zadaniem. Jeśli są już napisane i nieoznaczone, otwórz kopię w Eksploratorze studium i oznacz je zbiorczo w kilka minut."),
   ("Zdecyduj, która forma pasuje drugiej osobie", "Kto studiuje w JW Library, chce notatek w swojej bibliotece. Kto składa dokument, chce tekstu. Z tego samego zestawu możesz zrobić jedno i drugie."),
   ("Aby wysłać notatki: użyj strony udostępniania", "Na jwsync.org/share.html wybierz Wyślij notatki, wczytaj kopię, odfiltruj według użytej etykiety i kliknij Zaznacz wszystkie, a potem utwórz plik. Osoba doda go do własnej kopii i ją przywróci — jej notatki pozostaną nietknięte."),
   ("Aby wysłać tekst: wyeksportuj z Eksploratora studium", "Odfiltruj ten sam zestaw i skopiuj albo wyeksportuj go jako Markdown lub zwykły tekst. Formatowanie zostaje zachowane, więc uporządkowany konspekt pozostaje uporządkowany po wklejeniu do dokumentu."),
  ],
  "sections": [
   ("Zachowaj kopię dla siebie, w formie, którą znów znajdziesz",
    "Ten sam eksport warto zachować także na własny użytek. Etykieta plus zakres dat sprawiają, że całe przygotowanie da się odnaleźć po latach — dokładnie wtedy, gdy będzie potrzebne — a wyodrębnianie według daty w Eksploratorze studium zamienia dowolny przedział czasu w osobny plik."),
  ],
  "faq": [
   ("Czy wersety pozostaną powiązane z właściwymi miejscami?", "Tak — udostępnione notatki zachowują akapit i werset, do których były przypisane, więc trafią we właściwe miejsce w bibliotece drugiej osoby."),
   ("Czy mogę udostępnić notatki, na których są wyróżnienia?", "Tak. Wyróżnienia powiązane z udostępnianymi notatkami podróżują razem z nimi."),
  ],
 },

 "weekly-meeting-preparation-jw-library-notes": {
  "title": "Przygotuj się do zebrania, korzystając z już napisanych notatek",
  "h1": "Cotygodniowe przygotowanie z notatkami, które już masz",
  "description": "Już studiowałeś ten materiał. Oto krótka cotygodniowa procedura, która wydobywa Twoje dawne notatki, wyróżnienia i odpowiedzi do tej samej publikacji, zanim zaczniesz przygotowania od nowa.",
  "intro": [
   "Większość osób przygotowuje się co tydzień od czystej kartki, mimo że pisała już o tym samym temacie — czasem o tym samym wersecie — kilka razy wcześniej. Tamte przemyślenia leżą w Twojej bibliotece; problem polega tylko na tym, że nic nie przywraca ich we właściwym momencie.",
   "Pięciominutowa procedura na początku przygotowań to naprawia, a wymaga jedynie kopii, którą i tak masz.",
  ],
  "steps": [
   ("Wczytaj aktualną kopię do Eksploratora studium", "Utwórz kopię w JW Library, a potem otwórz ją na jwsync.org. Wszystko jest odczytywane w Twojej przeglądarce."),
   ("Wyszukaj temat, zanim zaczniesz", "Poszukaj wersetu przewodniego, tematu albo publikacji. Wszystko, co napisałeś o tym w poprzednich latach, pojawi się razem, ze wszystkich publikacji, w których występuje."),
   ("Sprawdź swoje wpisane odpowiedzi", "Widok Odpowiedzi do studium zbiera odpowiedzi wpisane przez Ciebie w pytaniach, więc wcześniejsze przejścia przez ten sam materiał są podstawą, na której możesz budować, zamiast je powtarzać."),
   ("Dodaj to, czego brakuje, i wgraj z powrotem", "Notatki możesz edytować albo dodawać na miejscu — tytuł, treść, etykiety, kolor wyróżnienia. Wyeksportuj zmienioną kopię i przywróć ją w JW Library, a Twoje przygotowanie będzie w aplikacji na zebranie."),
  ],
  "sections": [
   ("Dlaczego stare notatki mają znaczenie",
    "Przejrzenie tego, do czego doszedłeś ostatnim razem, sprawia, że przygotowanie się kumuluje. Przestajesz odkrywać na nowo te same myśli i zaczynasz na nich budować — a notatki dodane w tym tygodniu staną się punktem wyjścia następnym razem."),
   ("Łagodniejsza wersja: niech notatki same do Ciebie przyjdą",
    "Jeśli cotygodniowe wyszukiwanie wydaje się pracą, Przypomnienie na stronie statystyk studium samo przywraca kilka starych notatek każdego dnia, w tym te napisane tego dnia w poprzednich latach. Ta sama korzyść, bez procedury do zapamiętania."),
  ],
  "faq": [
   ("Czy edycja w przeglądarce zmienia moją bibliotekę bezpośrednio?", "Nie. Eksportujesz zaktualizowaną kopię i przywracasz ją w JW Library — aplikacja zmienia się wyłącznie przez przywracanie, które wykonujesz sam."),
   ("Czy moja kopia jest gdzieś wysyłana, gdy w niej szukam?", "Nie. Plik jest odczytywany lokalnie w Twojej przeglądarce; nic nigdzie nie trafia."),
  ],
 },

 "print-jw-library-notes": {
  "title": "Jak wydrukować swoje notatki JW Library",
  "h1": "Jak przenieść notatki JW Library na papier",
  "description": "JW Library nie ma przycisku drukowania. Wyeksportuj notatki jako tekst albo Markdown, wklej je do dowolnego dokumentu i drukuj — dziennik studium, zestaw notatek dla kogoś bez aplikacji albo archiwum.",
  "intro": [
   "Z JW Library nie da się drukować, a zrzuty ekranu telefonu czyta się kiepsko. Ale notatki należą do Ciebie, a przeniesienie ich do dokumentu gotowego do druku jest proste, gdy tylko potrafisz odczytać plik kopii.",
   "Eksplorator studium odczytuje kopię .jwlibrary w Twojej przeglądarce i pozwala skopiować albo wyeksportować dowolny wybór notatek jako zwykły tekst lub Markdown — a to rozumie już każdy edytor tekstu, aplikacja do notatek i drukarka.",
  ],
  "steps": [
   ("Utwórz kopię i otwórz ją", "JW Library → Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową, a potem wczytaj plik na jwsync.org."),
   ("Zawęź do tego, co chcesz mieć na papierze", "Filtruj według publikacji, etykiety, koloru wyróżnienia albo zakresu dat, albo wyszukaj temat. Wydrukować można wszystko, ale przefiltrowany zestaw zwykle daje znacznie użyteczniejszy dokument."),
   ("Skopiuj albo wyeksportuj jako tekst lub Markdown", "Wyciągnij wybór jako Markdown albo zwykły tekst. Pogrubienie, kursywa i listy zostają zachowane, więc uporządkowane notatki pozostają uporządkowane na stronie."),
   ("Wklej do dokumentu i wydrukuj", "Nada się dowolny edytor tekstu albo aplikacja do notatek. Ustaw nagłówki i marginesy, jakie chcesz, a potem drukuj albo zapisz jako PDF."),
  ],
  "sections": [
   ("Tworzenie dziennika studium",
    "Zakres dat to naturalna jednostka drukowanego dziennika — rok notatek albo okres obejmujący jedną publikację. Wyodrębnianie według daty daje czysty, chronologiczny zestaw do druku lub oprawy, a posiadanie czegoś takiego poza ekranem jest po swojemu satysfakcjonujące."),
   ("Drukowanie dla kogoś, kto nie korzysta z aplikacji",
    "Nie każdy studiuje z urządzenia. Wydrukowany zestaw notatek do bieżącego materiału jest naprawdę przydatny dla kogoś, kto woli papier, a zajmuje tyle samo czasu co każdy inny eksport."),
  ],
  "faq": [
   ("Czy mogę wydrukować też swoje wyróżnienia?", "Widok wyróżnień wypisuje zaznaczone przez Ciebie fragmenty, a ta lista kopiuje się jako tekst razem z notatkami."),
   ("Czy eksport coś zmienia w JW Library?", "Nie. Eksport odczytuje kopię Twojej kopii zapasowej; pierwotny plik i aplikacja pozostają nietknięte."),
  ],
 },

 "clean-up-duplicate-jw-library-notes": {
  "title": "Czyszczenie zduplikowanych i pustych notatek JW Library",
  "h1": "Usuwanie zduplikowanych notatek, pustych notatek i bałaganu",
  "description": "Przywróciłeś kopię dwa razy albo zaimportowałeś te same notatki ponownie? Doktor biblioteki skanuje Twój plik .jwlibrary w przeglądarce, znajduje duplikaty i puste notatki i tworzy czystą kopię.",
  "intro": [
   "Biblioteki zbierają bałagan. Przywrócenie kopii na urządzenie, które miało już część tych samych notatek, dwukrotny import udostępnionego zestawu albo lata na wpół napisanych notatek, których nigdy nie dokończono — każde coś po sobie zostawia, a JW Library nie daje żadnego sposobu, aby posprzątać to zbiorczo.",
   "Doktor biblioteki to bezpłatna kontrola stanu pliku .jwlibrary. Skanuje kopię w Twojej przeglądarce, prostym językiem mówi, co znalazł, i jednym dotknięciem naprawia to, co da się naprawić.",
  ],
  "steps": [
   ("Najpierw utwórz kopię — jak zawsze", "JW Library → Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Zachowaj ten plik; to Twoje zabezpieczenie."),
   ("Uruchom kontrolę stanu", "Otwórz jwsync.org, wczytaj kopię i uruchom Doktora biblioteki. Zbada zawartość i strukturę pliku, nigdzie go nie wysyłając."),
   ("Przeczytaj, co znalazł", "Duplikaty, puste notatki i inny bałagan są wypisane w czytelny sposób, z liczbami, więc widzisz skalę problemu, zanim cokolwiek zmienisz."),
   ("Napraw i pobierz czystą kopię", "Jedno dotknięcie stosuje poprawki i tworzy nowy, oczyszczony plik .jwlibrary. Twój oryginał nigdy nie jest zmieniany."),
   ("Przywróć czysty plik", "Kopia zapasowa i przywracanie → Przywróć i wybierz oczyszczony plik. Twoja biblioteka jest ta sama, tylko bez bałaganu."),
  ],
  "sections": [
   ("Skąd w ogóle biorą się duplikaty",
    "Prawie zawsze z przywracania. Jeśli przywrócisz kopię na urządzenie, które miało już część tego samego materiału — albo przywrócisz ten sam plik dwukrotnie różnymi drogami — aplikacja nie ma jak wiedzieć, że już widziała te notatki."),
   ("Scalanie to sposób, aby ich uniknąć",
    "Właśnie dlatego scalenie dwóch kopii jest bezpieczniejsze niż przywrócenie jednej na drugą: scalanie wykrywa materiał, który już istnieje, i zachowuje go raz. Te same kontrole działają wewnątrz każdego scalania, więc scalona kopia wychodzi czysta, nawet jeśli pliki wejściowe takie nie były."),
  ],
  "faq": [
   ("Czy usunie notatki, których naprawdę chcę?", "Usuwa dokładne duplikaty i puste notatki — materiał, w którym nie ma czego stracić. A ponieważ zapisuje nowy plik zamiast edytować Twój, oryginał zawsze pozostaje jako zabezpieczenie."),
   ("Czy może odzyskać notatki, które usunąłem w aplikacji?", "Nie. Jeśli notatkę usunięto w JW Library przed utworzeniem kopii, po prostu jej w niej nie ma — szukaj w starszej kopii."),
  ],
 },


 "backup-jw-library-before-phone-repair": {
  "title": "Utwórz kopię JW Library przed resetem do ustawień fabrycznych albo naprawą",
  "h1": "Przed resetem do ustawień fabrycznych, naprawą albo sprzedażą telefonu",
  "description": "Reset kasuje notatki JW Library razem z resztą, a narzędzia do przenoszenia ich nie zabierają. Utwórz kopię, sprawdź, że naprawdę się otwiera, a potem resetuj, niczym nie ryzykując.",
  "intro": [
   "Zresetuj telefon, oddaj go do naprawy albo przekaż komuś innemu, a osobiste dane studium JW Library znikną razem z nim. Zdjęcia i aplikacje wrócą z kopii w chmurze; lata notatek, wyróżnień i zakładek zwykle nie, bo narzędzia do przenoszenia pomijają prywatne dane aplikacji.",
   "Rozwiązanie zajmuje pięć minut, a krok, który ludzie pomijają, jest najważniejszy: sprawdzenie, że plik kopii naprawdę da się odczytać, zanim urządzenie zostanie wyczyszczone.",
  ],
  "steps": [
   ("Utwórz kopię", "JW Library → Studium osobiste → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Otrzymasz plik .jwlibrary — zwykle tylko kilka megabajtów."),
   ("Wynieś ją poza urządzenie", "Wyślij ją sobie e-mailem albo umieść w Drive, iCloud czy folderze na komputerze. Kopia, która istnieje tylko na telefonie, który zamierzasz wyczyścić, nie jest kopią."),
   ("Sprawdź, że się otwiera, zanim cokolwiek skasujesz", "Wczytaj plik na jwsync.org i przyjrzyj mu się — notatki, wyróżnienia i zakładki powinny być na miejscu, a kontrola stanu zasygnalizuje wszelkie problemy z plikiem. O to właśnie chodzi w tym ćwiczeniu: dowiedzieć się, że pliku nie da się odczytać, już po wyczyszczeniu, to za późno."),
   ("Zresetuj, a potem przywróć", "Po resecie albo naprawie zainstaluj JW Library, zaloguj się, a potem Kopia zapasowa i przywracanie → Przywróć i wybierz swój plik."),
   ("Korzystałeś w międzyczasie z telefonu zastępczego? Scalaj, nie nadpisuj", "Jeśli robiłeś notatki na urządzeniu tymczasowym, utwórz kopię również z niego i przed przywracaniem scal oba pliki na jwsync.org — inaczej przywrócenie starej kopii skasuje wszystko, co napisałeś w czasie oczekiwania."),
  ],
  "sections": [
   ("Dlaczego sprawdzenie warte jest dodatkowej minuty",
    "Przerwane transfery, dyski w chmurze psujące pliki i rozszerzenia zmienione po drodze — wszystko to tworzy kopie, które w folderze wyglądają dobrze i zawodzą przy przywracaniu. Wcześniejsze otwarcie pliku zamienia ukryty problem w taki, który wciąż możesz naprawić, dopóki pierwotne urządzenie nadal ma dane."),
   ("Zachowaj plik po przywróceniu",
    "Nie usuwaj go, gdy tylko nowe urządzenie zacznie działać. Stare kopie to jedyna droga powrotu po notatce przypadkiem usuniętej kilka miesięcy później, a ich przechowywanie nic nie kosztuje."),
  ],
  "faq": [
   ("Czy moje pobrane publikacje wrócą?", "Kopia zawiera Twoje osobiste dane studium — notatki, wyróżnienia, zakładki, etykiety i playlisty. Publikacje po prostu pobiorą się później ponownie."),
   ("Czy plik zadziała, jeśli przejdę na telefon innej marki albo platformy?", "Tak. Format .jwlibrary jest taki sam na Androidzie, iPhonie, iPadzie i Windows."),
  ],
 },

 "jw-library-notes-missing-after-update": {
  "title": "Notatki JW Library zniknęły po aktualizacji albo ponownej instalacji",
  "h1": "Notatki zniknęły po aktualizacji aplikacji, ponownej instalacji albo przywracaniu",
  "description": "Twoje notatki zniknęły po aktualizacji, ponownej instalacji albo ponownym zalogowaniu. Co zrobić najpierw, czego nie robić i jak je odzyskać, nie tracąc niczego, co napisałeś od tamtej pory.",
  "intro": [
   "Otwarcie JW Library po aktualizacji i stwierdzenie, że notatek nie ma, jest niepokojące, a w zdecydowanej większości przypadków da się je odzyskać. Liczy się to, co zrobisz w ciągu najbliższych kilku minut — a konkretnie to, czego nie zrobisz: jedna czynność zamienia sytuację odwracalną w trwałą stratę.",
   "To nieprzyjemna chwila: JW Library się otwiera, a notatek nie ma. Przede wszystkim jedna rada — nie spiesz się. Większość tego, co czyni tę sytuację nieodwracalną, dzieje się w pierwszych dziesięciu minutach, gdy nadpisywana jest właśnie ta kopia, która wciąż zawiera brakujące notatki.",
   "Wykonaj poniższe kroki po kolei. Celem jest jeden plik zawierający zarówno stare notatki, jak i wszystko, co napisałeś od tamtej pory.",
  ],
  "steps": [
   ("Na razie nie nadpisuj swoich kopii", "Powstrzymaj się od tworzenia świeżej kopii na starej i nie przywracaj niczego w ciemno. Starszy plik kopii to najbardziej prawdopodobne miejsce, w którym Twoje notatki wciąż istnieją."),
   ("Poszukaj najnowszej kopii, jaką masz", "Sprawdź załączniki w poczcie, Google Drive, iCloud Drive, folder pobranych na komputerze i każde inne urządzenie, na które przywracałeś. Kopie są małe, więc ludzie często mają ich więcej, niż pamiętają."),
   ("Zajrzyj do pliku, zanim go przywrócisz", "Wczytaj kandydata na jwsync.org i zobacz, co naprawdę zawiera — ile notatek, z jakich publikacji, do jakiej daty. To powie Ci, czy to właściwy plik, zanim zdecydujesz się na przywracanie."),
   ("Utwórz kopię również z bieżącego urządzenia", "Nawet jeśli wygląda na puste, utwórz z niego kopię. Jeśli napisałeś cokolwiek od zniknięcia notatek, ten plik jest jedynym tego egzemplarzem."),
   ("Scal oba, a dopiero potem przywracaj", "Scal starą kopię z bieżącą na jwsync.org. Wynik będzie zawierał odzyskane notatki i wszystko napisane od tamtej pory, a duplikaty zostaną zachowane raz. Przywróć właśnie ten scalony plik — nigdy samej starej kopii."),
  ],
  "sections": [
   ("Dlaczego przywrócenie samej starej kopii to zły ruch",
    "Przywracanie całkowicie zastępuje bibliotekę urządzenia. Jeśli przywrócisz starą kopię wprost, odzyskasz brakujące notatki i stracisz wszystko napisane po jej utworzeniu. To wcześniejsze scalenie sprawia, że odzyskiwanie odbywa się bez strat."),
   ("Jeśli sama kopia się nie przywraca",
    "Plik zgłaszający błąd przy przywracaniu wcale nie musi być stracony. Uruchom na nim kontrolę stanu — uszkodzenia z przerwanych pobrań, synchronizacji z chmurą albo zmienionego rozszerzenia często da się naprawić, a oczyszczona kopia przywróci się normalnie."),
   ("Przede wszystkim: na razie nie twórz nowej kopii",
    "Jeśli notatki zniknęły, powstrzymaj odruch natychmiastowego zrobienia kopii. Kopia utrwala bieżący stan, a jeśli bieżący stan jest pusty, ryzykujesz nadpisanie dobrego pliku, który już miałeś. Najpierw ustal, jakie kopie istnieją — w Pobranych, Plikach, poczcie czy chmurze — i dopiero wtedy decyduj. Świeża kopia zrobiona w panice niczego na urządzeniu nie poprawi."),
   ("Dlaczego aktualizacja może wyglądać jak utrata notatek",
    "Zwykłą przyczyną nie jest usunięcie. Aktualizacja może zostawić aplikację wskazującą na nową, pustą bazę danych, podczas gdy stara wciąż leży na dysku; ponowna instalacja — w tym wykonana automatycznie przez aktualizację ze sklepu, która przerwała się w połowie — uruchamia aplikację od zera; a na urządzeniach współdzielonych albo z wieloma profilami aplikacja może działać pod innym profilem niż wcześniej. W każdym z tych przypadków notatki nie tyle zniknęły, ile nie są obecnie wczytane — i dlatego właśnie przywrócenie z kopii zwykle wszystko czysto przywraca."),
   ("Odzyskanie starej kopii bez wyrzucania nowej pracy",
    "Jeśli studiowałeś po utworzeniu kopii, zwykłe przywrócenie zamienia jedną stratę na drugą: przywraca stare notatki i usuwa wszystko nowsze. Sposób na to jest taki: zapisz bieżący stan do osobnego pliku, scal go ze starszą kopią, aby oba zestawy notatek znalazły się w jednym pliku, i przywróć scalony wynik. Otrzymasz odzyskane notatki i te nowe razem, zamiast wybierać między nimi."),
   ("Jeśli aplikacja sama się przeinstalowała",
    "Ponowna instalacja czyści prywatną pamięć aplikacji, więc wszystkiego, czego nie ma w kopii, nie da się odzyskać — nie ma kopii w chmurze, na której można się oprzeć. Sprawdź każde miejsce, gdzie mógł zostać zapisany plik .jwlibrary, zanim uznasz, że go nie ma, łącznie z folderem wysłanych wiadomości i każdą chmurą, do której kiedykolwiek zapisywałeś. Gdy jakąś znajdziesz, przywróć ją, a od tej pory trzymaj kopie poza urządzeniem."),
   ("Gdy wszystko wróci",
    "Gdy notatki będą przywrócone, zrób jeszcze jedną kopię i umieść ją poza urządzeniem — to, co właśnie przeszedłeś, jest najlepszym argumentem. Jeśli aby tu dotrzeć, musiałeś scalić starą kopię z bieżącym stanem, zachowaj też oba pliki źródłowe: to datowane migawki, a to właśnie ich liczba umożliwiła odzyskanie danych."),
  ],
  "faq": [
   ("Czy notatki są jeszcze gdzieś na urządzeniu?", "Nie w postaci, do której da się dostać spoza aplikacji. Realistycznie odzyskanie oznacza wcześniejszy plik kopii — i dlatego przechowywanie starych ma takie znaczenie."),
   ("Czy ponowne zalogowanie przywróci notatki?", "Nie. Osobiste dane studium nie są przechowywane na koncie; żyją na urządzeniu i podróżują wyłącznie przez pliki kopii."),
   ("Co, jeśli moja jedyna kopia ma kilka miesięcy?", "Scal ją z kopią urządzenia w obecnym stanie. Odzyskasz wszystko, co jest w starym pliku, i zachowasz wszystko, co wciąż jest na urządzeniu, nie wybierając między nimi."),
   ("Czy moje notatki naprawdę przepadły?", "Niekoniecznie. Jeśli kopia gdziekolwiek istnieje, wszystko w niej da się w pełni odzyskać. Nie do odzyskania jest tylko praca wykonana po utworzeniu ostatniej kopii."),
   ("Czy mogę połączyć starą kopię z tym, co jest teraz na urządzeniu?", "Tak — najpierw utwórz kopię bieżącego stanu, potem scal ten plik ze starszym i przywróć wynik. Oba zestawy notatek trafią do tej samej biblioteki."),
   ("Czy przywrócenie starej kopii usunie moje nowe notatki?", "Samo w sobie tak, bo przywracanie zastępuje dane urządzenia. Najpierw scal bieżącą kopię ze starą i przywróć zamiast tego scalony plik."),
   ("Czy powinienem przeinstalować aplikację, aby to naprawić?", "Nie — ponowna instalacja czyści prywatną pamięć aplikacji i odbiera wszelką szansę na odzyskanie tego, co wciąż jest na urządzeniu. Najpierw poszukaj istniejącej kopii, a ponowną instalację potraktuj jako ostateczność, gdy kopię już masz."),
  ],
 },

 "help-family-member-move-jw-library-notes": {
  "title": "Pomóż komuś z rodziny przenieść notatki JW Library",
  "h1": "Pomaganie innej osobie w przeniesieniu albo uratowaniu jej notatek JW Library",
  "description": "To Ciebie prosi się o naprawienie telefonu. Oto najkrótsza pewna droga do przeniesienia notatek JW Library krewnego na nowe urządzenie — łącznie z tym, jak zrobić to, nie czytając jego notatek.",
  "intro": [
   "Prędzej czy później ktoś podaje Ci swój telefon, a obok kładzie nowy. Notatki JW Library to ta część, która sama się nie przeniesie, i często najważniejsza: lata studium, których nie zabierze żadne narzędzie.",
   "Proces jest taki sam jak przy własnym telefonie, z jednym dodatkowym pytaniem, które warto rozstrzygnąć na początku: na czyim urządzeniu wykonujesz pracę.",
  ],
  "steps": [
   ("Poprowadź go przez utworzenie kopii na starym urządzeniu", "JW Library → Studium osobiste → menu z trzema kropkami → Kopia zapasowa i przywracanie → Utwórz kopię zapasową. Zapisze to plik .jwlibrary. Jeśli nie ma Cię przy nim, tę część może wykonać przez telefon."),
   ("Przenieś plik tam, gdzie go potrzebujesz", "Poproś, aby wysłał go sobie e-mailem albo udostępnił Tobie. Jest na tyle mały, że przejdzie dowolnym komunikatorem."),
   ("Sprawdź, czy plik się otwiera", "Wczytaj go na jwsync.org i upewnij się, że notatki są na miejscu. Zrobienie tego zanim stare urządzenie zostanie wyczyszczone albo oddane zamienia przykrą niespodziankę w nic wielkiego."),
   ("Scal, jeśli nowe urządzenie ma już notatki", "Jeśli osoba używa nowego telefonu od jakiegoś czasu, utwórz kopię również z niego i scal oba pliki — inaczej przywrócenie starej kopii usunie wszystko, co napisała na nowym urządzeniu."),
   ("Przeprowadź ją przez przywracanie", "Na nowym urządzeniu: Kopia zapasowa i przywracanie → Przywróć, wybrać plik. Pojawią się notatki, wyróżnienia, zakładki i etykiety."),
  ],
  "sections": [
   ("Jak zrobić to, nie czytając jej notatek",
    "Osobiste notatki do studium są prywatne. Jeśli wolisz ich nie widzieć — albo ta osoba woli, żebyś nie widział — wykonaj całość na jej urządzeniu: to strona internetowa, więc możesz otworzyć jwsync.org na jej telefonie czy tablecie, wczytać tam jej pliki i nigdy nie mieć kopii na własnym komputerze. Nic nie jest wysyłane w żadnym z wariantów, ale w ten sposób plik w ogóle nie opuszcza jej rąk."),
   ("Zostaw jej kopię, którą sama odnajdzie",
    "Zanim oddasz telefon, upewnij się, że plik kopii leży tam, gdzie ta osoba znajdzie go ponownie — w jej własnej poczcie albo chmurze, a nie tylko w Twoim folderze pobranych. Następnym razem być może w ogóle nie będzie Cię potrzebować."),
  ],
  "faq": [
   ("Czy mogę zrobić to zdalnie?", "Tak. Jeśli osoba potrafi utworzyć kopię i wysłać Ci plik, cała reszta działa na odległość — a przywracanie to kilka dotknięć, przez które możesz ją przeprowadzić."),
   ("Ona ma Androida, a nowy telefon to iPhone. Czy to ma znaczenie?", "Nie. Format kopii jest taki sam na Androidzie, iPhonie, iPadzie i Windows."),
   ("Co, jeśli nigdy nie zrobiła kopii, a starego telefonu już nie ma?", "Wtedy nie ma z czego odzyskiwać — dane żyły na tamtym urządzeniu. Warto od razu wprowadzić na nowym telefonie nawyk regularnych kopii."),
  ],
 },

 "import-markdown-notes-jw-library": {
  "title": "Jak zaimportować notatki Markdown do JW Library",
  "h1": "Jak zaimportować notatki Markdown do JW Library",
  "description": "Zamień pliki .md z Obsidiana, Notion czy dowolnego edytora Markdown w prawdziwe notatki JW Library, umieszczone przy właściwym wersecie — za darmo, prywatnie, w przeglądarce.",
  "intro": [
   "JW Library nie ma żadnego sposobu na wczytanie tekstu z zewnątrz. W samej aplikacji notatki napiszesz, ale notatka napisana gdzie indziej — w Obsidianie, w Notion, w zwykłym pliku tekstowym na komputerze — nie ma w ogóle drogi do twojej biblioteki. Ludzie przepisują je ręcznie albo rezygnują i prowadzą dwa zbiory notatek do studium, które nigdy się nie spotykają.",
   "JW Sync zasypuje tę lukę. Wczytaj kopię zapasową w Eksploratorze studium, naciśnij „Importuj Markdown”, a twoje pliki .md staną się w niej prawdziwymi notatkami: tytuł, data i etykiety zostaną nienaruszone, a gdy plik mówi, do którego wersetu należy, notatka trafi dokładnie tam — tak, jakbyś napisał ją w aplikacji podczas czytania.",
   "Działa to w obie strony. Notatki wyeksportowane z tej strony niosą ze sobą księgę, rozdział i werset, więc wracają dokładnie tam, skąd wyszły. Notatki pisane gdzie indziej zwykle nie mają nic takiego — i właśnie dlatego ta strona wyjaśnia te jedną czy dwie linijki, które je umieszczają, oraz to, co się dzieje, gdy plik ich nie ma.",
  ],
  "steps": [
   ("Utwórz kopię zapasową w JW Library",
    "Otwórz JW Library, przejdź do Studium osobistego, dotknij menu z trzema kropkami, wybierz Kopia zapasowa i przywracanie, a potem Utwórz kopię zapasową. Dostaniesz plik .jwlibrary — bibliotekę, do której trafią twoje notatki."),
   ("Otwórz Eksplorator studium",
    "Wejdź na jwsync.org, otwórz Eksplorator studium i wczytaj ten plik .jwlibrary. Wszystko dzieje się w twojej przeglądarce; plik nigdy nie jest wysyłany."),
   ("Naciśnij „Importuj Markdown”",
    "Przycisk stoi obok „Eksportuj Markdown”. Wybierz dowolną liczbę plików .md albo archiwum .zip z nimi — także to .zip, które ta strona tworzy przy eksporcie."),
   ("Przeczytaj podsumowanie, zanim cokolwiek zostanie zapisane",
    "Dowiesz się, ile notatek trafi na werset, ile zostanie dodanych jako notatki samodzielne i ile jest już w kopii, więc zostanie pominiętych. Wszystko, co strona musiała zinterpretować, jest wypisane linijka po linijce z polem wyboru — decydujesz ty, a nie odkrywasz to później."),
   ("Wyeksportuj i przywróć",
    "Naciśnij „Eksportuj .jwlibrary”, a potem przywróć ten plik w JW Library przez Kopia zapasowa i przywracanie → Przywróć. Zaimportowane notatki są już częścią twojej biblioteki na tym urządzeniu."),
  ],
  "sections": [
   ("Najkrótszy plik, który zadziała",
    "Plik Markdown nie potrzebuje niczego, żeby dało się go zaimportować: plik z samym tekstem też stanie się notatką, a tytuł weźmie z pierwszego nagłówka albo, w jego braku, z nazwy pliku. Cała reszta służy temu, by powiedzieć, gdzie notatka przynależy. Kompletny plik wygląda tak:\n\n---\ntitle: Kielich, o który się modlił\ntags: [studium, getsemani]\npublication: Matthew 26:39\n---\n\nJego modlitwa pokazuje podporządkowanie, a nie niechęć.\n\nBlok między dwiema liniami myślników nazywa się front matter. Linie poniżej to sama notatka."),
   ("Pola, które są odczytywane",
    "Odczytywanych jest tylko pięć rzeczy, a każda przyjmuje kilka zapisów, żebyś nie musiał pamiętać jednego dokładnego. **title** (albo name, heading) staje się tytułem notatki. **tags** (albo tag, keywords, categories, labels, topics) stają się prawdziwymi etykietami JW Library i są tworzone, jeśli jeszcze ich nie ma. **date** (albo created, modified) ustawia datę notatki; rozumiana jest każda wartość zawierająca RRRR-MM-DD. **publication** (albo pub, reference, ref, scripture, citation, source, passage) to miejsce na werset. **book**, **chapter** i **verse** (albo ch, v, vs, verses) robią to samo w osobnych polach. Każde inne pole, które trzymasz dla siebie — autor, status, cokolwiek dodaje twój edytor — jest pomijane, a nie traktowane jako błąd."),
   ("Trzy sposoby wskazania notatce wersetu",
    "Napisz namiar w jednej linii: `publication: Matthew 26:39`. Albo rozbij go: `book: Matthew`, `chapter: 26`, `verse: 39`. Albo użyj obu — tak robi eksport tej strony, żeby plik dobrze się czytał człowiekowi i dokładnie parsował maszynie. Wszystkie trzy dają ten sam wynik, więc używaj tego, co pasuje do twojego edytora."),
   ("Jak swobodny może być zapis wersetu",
    "Nazwy ksiąg dopasowywane są hojnie. Działają pełne nazwy, a także skróty, które ludzie naprawdę wpisują: Matt, Matt., Mt, 1 Cor, 1Cor, I Corinthians, Second Timothy, Psalm równie dobrze jak Psalms, Song of Songs równie dobrze jak Song of Solomon. Rozdział od wersetu może oddzielać dwukropek, kropka albo litera v — `John 3:16`, `John 3.16` i `1 Cor 13 v4` czytane są tak samo. Spacje wszędzie są opcjonalne, więc `1Cor13:4` też przejdzie.\n\nSam front matter jest równie wyrozumiały. Nazwy pól mogą być z wielkiej litery. Spacji po dwukropku może zabraknąć. Nadmiarowe spacje i tabulatory są pomijane, podobnie jak cudzysłowy wokół wartości i końcowy komentarz z #. Windowsowe końce linii nie przeszkadzają. Możesz nawet całkiem pominąć linie --- i zacząć plik od razu od pól, o ile pierwsza linia jest jedną z rozpoznawanych nazw — ta zasada istnieje po to, żeby notatka zaczynająca się zwykłym zdaniem z dwukropkiem nie straciła pierwszego akapitu."),
   ("Etykiety, jakkolwiek je zapiszesz",
    "Wszystkie te zapisy dają te same dwie etykiety: `tags: [studium, greka]`, `tags: studium, greka`, `tags: studium; greka`, `tags: #studium #greka`, albo lista we własnych liniach pod `tags:`, gdzie każdy wpis zaczyna się myślnikiem. Etykiety, które już masz w bibliotece, są używane ponownie, a nie dublowane, więc zaimportowana notatka dołącza do tej samej etykiety, po której i tak filtrujesz."),
   ("Co się dzieje, gdy coś jest niejasne",
    "Nic niepewnego nie jest rozstrzygane za ciebie. Jeśli nazwa księgi jest bliska prawdziwej, ale niedokładna — `Mathew`, `Ecclesiates` — notatka nie zostaje umieszczona automatycznie. Pojawia się w podsumowaniu we własnej linii z tym, co strona z niej zrozumiała: „odczytano jako Matthew 26:39”, wraz z polem wyboru. Odznacz je, a notatka zostanie pominięta; zostaw zaznaczone, a trafi tam, gdzie mówi linia.\n\nJeśli księgi w ogóle nie da się rozpoznać, linia to mówi, a notatka zostaje dodana jako samodzielna — nigdy nie jest wciskana na domysł. Księga z numerem zachowuje swój numer, więc `1 Jonh` może zostać poprawione tylko na 1 Jana, nigdy na 2 Jana."),
   ("Czego celowo nie robi",
    "Zakres wersetów kotwiczy notatkę przy pierwszym z nich: `Matthew 26:39-41` umieszcza ją przy wersecie 39, bo notatka JW Library przypina się do jednego punktu tekstu, a nie do przedziału. Namiar z rozdziałem, ale bez wersetu — `Matthew 26` — przypina notatkę do tego rozdziału. Plik, który podaje publikację zamiast wersetu — `The Watchtower—2023 No. 4` — jest importowany jako zwykła notatka samodzielna, bez żadnego pytania, bo dokładnie to zapisuje eksport tej strony dla notatek robionych w artykule."),
   ("Formatowanie, które przeżywa podróż",
    "Akapity, złamania wierszy, **pogrubienie**, *kursywa* i listy punktowane trafiają do JW Library jako prawdziwe formatowanie. Nagłówek na początku pliku służy za tytuł notatki, zamiast powtarzać się w jej wnętrzu. Wszystko, co Markdown potrafi wyrazić, a notatki JW Library nie — tabele, obrazy, odnośniki, bloki kodu — zostaje sprowadzone do tekstu, więc nie ginie ani jedno słowo, nawet gdy układu nie da się przenieść."),
   ("Gdzie notatki naprawdę lądują i dlaczego to bezpieczne",
    "Żeby przypiąć notatkę do wersetu, JW Library potrzebuje wewnętrznych identyfikatorów tego rozdziału, właściwych dla twojej biblioteki. JW Sync nigdy ich nie wymyśla. Używa ponownie miejsca, które twoja własna kopia już ma dla tego rozdziału, albo kopiuje te identyfikatory z innego miejsca biblijnego w tym samym pliku. Jeśli kopia nie zawiera żadnych notatek ani zaznaczeń w Biblii, nie ma z czego kopiować — wtedy notatki są dodawane jako samodzielne, zamiast być przypinane do czegoś, czego aplikacja może nie rozpoznać. To świadomy wybór: notatka, która po cichu wylądowała w złym miejscu, jest gorsza niż taka, która przyszła wyraźnie nieprzypięta."),
   ("Import tych samych plików dwa razy",
    "Notatkę uznaje się za już obecną, gdy jej tytuł, tekst i miejsce zgadzają się z czymś w kopii, więc ponowny import tego samego eksportu niczego nie podwaja. Podsumowanie mówi, ile zostanie z tego powodu pominiętych, zanim potwierdzisz. Wszystko, co dodaje jeden import, to jeden krok Cofnij, a zaimportowane notatki dostają etykietę Imported, żebyś mógł je potem znaleźć, przefiltrować albo usunąć grupowo."),
  ],
  "faq": [
   ("Czy muszę używać linii ---?",
    "Nie. Czynią plik jednoznacznym i rozumie je każdy edytor Markdown, ale możesz też zacząć plik od razu od pól — `title: …` w pierwszej linii — albo zrezygnować z front matter i pozwolić notatce wziąć tytuł z pierwszego nagłówka."),
   ("A jeśli przekręcę nazwę księgi?",
    "Strona zwykle domyśli się, o co ci chodziło, ale nie działa wyłącznie na tej podstawie. Notatka pojawia się w podsumowaniu z informacją, jak została odczytana, i z polem wyboru — potwierdzasz, zanim cokolwiek zostanie zapisane."),
   ("Czy mogę zaimportować cały folder z Obsidiana?",
    "Zaznacz naraz dowolną liczbę plików .md albo spakuj folder i wybierz .zip. Pliki w archiwum czytane są tak samo jak luźne."),
   ("Czy import nadpisze moje dotychczasowe notatki?",
    "Nie. Import tylko dodaje. Twoje notatki, zaznaczenia, zakładki i etykiety pozostają nietknięte, a wczytany plik nigdy nie jest zmieniany — na końcu pobierasz nowy .jwlibrary."),
   ("Czy moje notatki są gdzieś wysyłane?",
    "Nie. Wszystko działa w twojej przeglądarce, jak reszta strony. Ani kopia zapasowa, ani pliki Markdown nie opuszczają twojego urządzenia."),
   ("W jakim języku mogę zapisać werset?",
    "Na razie nazwy ksiąg rozpoznawane są po angielsku — tak też zapisuje je eksport. Jeśli prowadzisz notatki w innym języku, użyj pól `book`, `chapter` i `verse` z angielską nazwą księgi albo zaimportuj notatki nieprzypięte i rozmieść je później ręcznie."),
   ("Czy mogę znowu wydobyć swoje notatki?",
    "Tak — „Eksportuj Markdown” na tym samym ekranie zapisuje każdą notatkę do pliku .md z tymi samymi polami, więc notatki mogą opuścić JW Library i wrócić, nie tracąc swojego miejsca."),
  ],
 },

}

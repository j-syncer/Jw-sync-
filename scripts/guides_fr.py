# -*- coding: utf-8 -*-
"""French translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → sauvegarde (le fichier .jwlibrary)
  Personal Study            → Étude personnelle
  Backup and Restore        → Sauvegarde et restauration
  restore                   → restaurer
  merge                     → fusionner / fusion
  notes                     → notes
  highlights                → surlignages
  bookmarks                 → signets
  tags                      → étiquettes
  Study Explorer            → Explorateur d'étude
  Library Doctor            → Docteur de bibliothèque
  Reading Companion         → Compagnon de lecture
  Resurface                 → Refaire surface
  Study Map                 → Carte d'étude
  Study Stats               → Statistiques d'étude
  Conflict Reviewer         → Comparateur de conflits
  meeting                   → réunion
  congregation              → congrégation
  assembly / convention     → assemblée / congrès
"""

GUIDES_FR = {}

GUIDES_FR["merge-jw-library-backups"] = {
    "title": "Comment fusionner des sauvegardes JW Library de deux appareils",
    "h1": "Comment fusionner des sauvegardes JW Library de deux appareils",
    "description": "Réunissez les notes, surlignages, signets et étiquettes de deux "
                   "sauvegardes JW Library ou plus dans un seul fichier .jwlibrary — "
                   "gratuitement, en privé, dans votre navigateur.",
    "intro": [
        "Vous avez étudié La Tour de Garde sur votre téléphone et un autre article sur votre tablette. Chaque appareil contient maintenant un travail que l'autre n'a pas, et JW Library ne peut pas les concilier : sa restauration remplace tout, elle ne fusionne pas, donc la sauvegarde que vous restaurez efface l'étude de l'autre appareil. Avec l'application seule, il n'y a aucun moyen de garder les deux.",
        "C'est à cela que sert ce site. Il lit deux fichiers .jwlibrary (ou plus) et réunit les notes, les surlignages, les signets et les étiquettes de chacun dans une nouvelle sauvegarde, sans qu'il faille choisir entre quoi que ce soit. Tout se passe dans votre navigateur : vos fichiers ne sont jamais envoyés sur un serveur, et vos notes d'étude restent privées.",
        "C'est aussi pourquoi l'habitude est préventive et non curative : dès lors que vous fusionnez régulièrement, vous n'avez plus à penser à restaurer avant d'étudier ailleurs. Étudiez où vous êtes, fusionnez quand cela vous arrange, et chaque appareil se met à jour.",
    ],
    "steps": [
        ("Créez une sauvegarde sur chaque appareil",
         "Dans JW Library, ouvrez Étude personnelle, appuyez sur le menu à trois points, "
         "choisissez Sauvegarde et restauration, puis Créer une sauvegarde. Faites-le sur "
         "chaque appareil. Chacun produit un fichier .jwlibrary."),
        ("Ouvrez JW Sync",
         "Rendez-vous sur jwsync.org depuis n'importe quel navigateur — téléphone, tablette "
         "ou ordinateur. Rien à installer."),
        ("Chargez les deux fichiers de sauvegarde",
         "Déposez (ou sélectionnez) les fichiers .jwlibrary. JW Sync les lit localement, sur "
         "votre appareil."),
        ("Examinez l'aperçu avant fusion",
         "Avant que quoi que ce soit ne soit écrit, un aperçu montre exactement ce qui sera "
         "réuni. Si la même note a été modifiée différemment sur chaque appareil, le "
         "Comparateur de conflits affiche les deux versions côte à côte, avec les écarts "
         "mot à mot, pour que vous choisissiez celle à garder — ou laissez « Suggérer la "
         "meilleure » choisir pour vous."),
        ("Téléchargez le fichier fusionné et restaurez-le",
         "Téléchargez le fichier .jwlibrary fusionné, puis restaurez-le sur chaque appareil "
         "via Sauvegarde et restauration → Restaurer. Les deux appareils portent désormais la "
         "bibliothèque complète et réunie."),
    ],
    "sections": [
        ("Qu'est-ce qui est fusionné ?",
         "Les notes, les surlignages, les signets, les étiquettes et les liens entre eux. Les "
         "doublons sont détectés automatiquement, donc restaurer le fichier fusionné ne "
         "double jamais rien. Les sauvegardes Android, iPhone, iPad et de l'application "
         "Windows utilisent le même format et se fusionnent librement."),
        ("Est-ce sans risque ?",
         "La fusion ne modifie jamais vos fichiers d'origine — elle produit une sauvegarde "
         "toute neuve, vos originaux restent donc intacts en filet de sécurité. Et comme tout "
         "s'exécute côté navigateur, aucune donnée ne quitte votre appareil."),
        ("Ce que contient réellement un fichier .jwlibrary",
         "Une sauvegarde .jwlibrary est une archive ZIP. Renommez une copie en .zip et ouvrez-la : vous y trouverez userData.db, une base de données SQLite contenant toutes les notes, les surlignages, les signets et les étiquettes que vous avez créés, ainsi qu'un petit manifest.json qui décrit la sauvegarde. Vos notes sont dans la table Note, les surlignages dans UserMark et BlockRange, les signets dans Bookmark, les étiquettes dans Tag et TagMap. Comprendre que la sauvegarde est une base de données complète, et non un ensemble de fichiers séparés, explique tout le reste de cette page : c'est pourquoi une restauration est tout ou rien, et pourquoi deux sauvegardes peuvent être combinées."),
        ("Pourquoi la restauration de JW Library ne peut pas fusionner",
         "Lors d'une restauration, JW Library ne lit pas votre sauvegarde pour ajouter ce qui manque à ce qui est déjà sur l'appareil : il remplace la base de données de l'appareil par celle du fichier. C'est un choix délibéré et sûr, car il garantit que l'appareil se retrouve dans un état connu, mais cela signifie que restaurer la sauvegarde de la tablette sur le téléphone efface tout ce que le téléphone avait et que la tablette n'avait pas. Aucun réglage ne change cela, et c'est précisément la lacune que comble une fusion : elle produit un fichier unique contenant déjà le travail des deux appareils, si bien que l'appareil sur lequel vous le restaurez se retrouve complet."),
        ("Comment les doublons sont détectés",
         "Chaque note, surlignage et signet porte un GUID, un identifiant unique attribué à la création et conservé dans toutes les sauvegardes suivantes. Quand le même élément apparaît dans deux sauvegardes, les deux exemplaires portent le même GUID : il est reconnu comme un seul élément et conservé une fois. C'est pourquoi fusionner deux fois les mêmes fichiers ne double rien, et pourquoi vous pouvez refusionner chaque semaine sans risque. Lorsque les GUID correspondent mais que le texte diffère — la même note modifiée sur les deux appareils — la résolution automatique est impossible : l'élément apparaît dans le Comparateur de conflits avec une comparaison mot à mot pour que vous choisissiez."),
        ("Ce qui ne se trouve pas dans la sauvegarde",
         "Une sauvegarde ne contient que vos données d'étude personnelle. Les publications téléchargées, les traductions de la Bible, les vidéos et l'audio n'y figurent pas, et c'est pourquoi les fichiers de sauvegarde sont petits : quelques mégaoctets même après des années d'étude. Après une restauration sur un nouvel appareil, il faudra peut-être retélécharger les publications que vous lisez régulièrement. Rien de ce que vous avez écrit n'en pâtit : les notes sont ancrées aux publications par référence, elles se rattachent donc dès que la publication est présente."),
        ("Si la fusion indique 0 note ajoutée",
         "C'est presque toujours exact, et non un défaut. Cela signifie que toutes les notes du second fichier existaient déjà dans le premier — fréquent si vous avez fusionné récemment, ou si un appareil est simplement en retard sur l'autre. Consultez l'aperçu : il liste ce qu'apporte chaque fichier avant toute écriture. Si vous attendiez de nouveaux éléments et n'en voyez aucun, vérifiez que vous avez sauvegardé l'appareil après la séance d'étude que vous cherchez, car une sauvegarde ne contient que ce qui existait au moment où elle a été créée."),
    ],
    "faq": [
        ("Puis-je fusionner plus de deux sauvegardes ?",
         "Oui — chargez autant de fichiers .jwlibrary que vous avez d'appareils. Ils sont tous "
         "réunis dans une seule sauvegarde fusionnée."),
        ("La fusion va-t-elle créer des notes en double ?",
         "Non. Les notes, surlignages et signets identiques sont détectés et conservés une "
         "seule fois. Les versions réellement différentes d'une même note apparaissent dans "
         "le Comparateur de conflits, à vous de trancher."),
        ("Est-ce que ça marche entre Android et iPhone ?",
         "Oui. Le format .jwlibrary est identique sur Android, iOS, iPadOS et Windows : les "
         "sauvegardes de plateformes différentes fusionnent sans aucune conversion."),
        ("Dois-je fusionner dans un ordre précis ?",
         "Non. La fusion ne dépend pas de l'ordre : le même ensemble de fichiers donne le même résultat quel que soit celui que vous chargez en premier. L'ordre ne change que le fichier pris comme base dans le résumé de l'aperçu."),
        ("Qu'advient-il des étiquettes présentes sur un seul appareil ?",
         "Elles sont conservées intactes, ainsi que les liens entre les étiquettes et les notes qu'elles marquent. Si les deux appareils ont une étiquette portant le même nom, elle est traitée comme une seule et reçoit les notes des deux."),
        ("Quelle taille fait le fichier fusionné ?",
         "À peu près la somme des originaux moins les doublons, soit généralement quelques mégaoctets. Les sauvegardes ne contiennent aucun média de publication, donc même une bibliothèque très annotée tient dans un courriel."),
        ("Puis-je annuler une restauration ?",
         "Pas depuis JW Library, et c'est pourquoi conserver vos sauvegardes d'origine compte. La fusion ne modifie jamais les fichiers que vous chargez : vos sauvegardes antérieures restent exactement telles quelles et peuvent être restaurées si vous voulez revenir en arrière."),
    ],
}

GUIDES_FR["sync-jw-library-multiple-devices"] = {
    "title": "Comment synchroniser JW Library entre plusieurs appareils",
    "h1": "Comment garder JW Library synchronisé entre plusieurs appareils",
    "description": "JW Library n'a pas de synchronisation intégrée entre appareils. Voici une "
                   "routine simple et privée pour garder notes, surlignages et signets "
                   "identiques sur votre téléphone, votre tablette et votre ordinateur.",
    "intro": [
        "La plupart de ceux qui étudient sur deux appareils découvrent le problème de la même façon : les notes écrites sur la tablette ne sont pas sur le téléphone, et restaurer la sauvegarde de l'un sur l'autre effacerait ce que ce dernier possédait. JW Library ne propose aucune synchronisation, et sa restauration est délibérément tout ou rien : garder les appareils alignés demande une routine, pas un réglage.",
        "JW Library ne synchronise pas les données d'étude personnelle entre appareils — il "
        "n'existe pas de compte qui porte vos notes du téléphone à la tablette. Le mécanisme "
        "officiel, c'est Sauvegarde et restauration, et une restauration remplace purement et "
        "simplement les données de l'appareil. Alors comment garder deux ou trois appareils "
        "identiques sans rien perdre ?",
        "La réponse tient en une courte routine : fusionner, puis restaurer. Faite chaque "
        "semaine ou chaque mois, elle prend deux minutes et laisse chaque appareil avec votre "
        "bibliothèque complète.",
    ],
    "steps": [
        ("Sauvegardez chaque appareil",
         "Sur chacun : Étude personnelle → menu à trois points → Sauvegarde et restauration → "
         "Créer une sauvegarde. Vous obtenez un fichier .jwlibrary par appareil."),
        ("Fusionnez les sauvegardes sur jwsync.org",
         "Chargez tous les fichiers. JW Sync réunit les notes, surlignages, signets et "
         "étiquettes de chaque appareil dans un seul fichier .jwlibrary fusionné — "
         "localement, dans votre navigateur, sans rien envoyer."),
        ("Restaurez le fichier fusionné sur chaque appareil",
         "Sauvegarde et restauration → Restaurer, choisissez le fichier fusionné. Tous les "
         "appareils sont maintenant identiques et complets."),
        ("Laissez JW Sync vous le rappeler",
         "Activez un rappel de synchronisation (hebdomadaire ou mensuel) dans JW Sync et il "
         "vous préviendra quand il sera temps de recommencer. Il retient aussi vos appareils "
         "enregistrés, ce qui accélère chaque tour."),
    ],
    "sections": [
        ("Pourquoi ne pas simplement restaurer la sauvegarde la plus récente ?",
         "Parce que « la plus récente » ne reflète qu'un seul appareil. Si vous avez pris des "
         "notes de réunion sur le téléphone et des notes d'étude sur la tablette la même "
         "semaine, chaque sauvegarde contient ce qui manque à l'autre. En restaurer une "
         "par-dessus l'autre fait perdre la moitié de votre travail. C'est la fusion qui rend "
         "la routine sûre."),
        ("À quelle fréquence faut-il synchroniser ?",
         "Adaptez-la à votre façon d'étudier. Deux appareils actifs utilisés tous les jours : "
         "une fois par semaine est confortable. Une tablette qui ne sort que pour les "
         "réunions : une fois par mois suffit largement. Attendre plus longtemps signifie "
         "seulement que la fusion aura davantage à réunir — rien ne se perd entre deux tours."),
        ("Pourquoi il n'y a pas de vraie synchronisation",
         "JW Library n'a aucun compte qui transporte les données d'étude personnelle d'un appareil à l'autre. Les notes, les surlignages et les signets vivent dans une base de données à l'intérieur de chaque appareil et y restent. Le seul mécanisme officiel pour les déplacer est Sauvegarde et restauration, et une restauration remplace les données de l'appareil cible au lieu de les combiner. Deux appareils utilisés séparément divergent donc définitivement, sauf si quelque chose les fusionne — ce qui est précisément l'objet de la routine ci-dessous."),
        ("Conserver un fichier maître",
         "La routine fonctionne mieux si vous traitez un fichier fusionné comme le maître courant. À chaque cycle, sauvegardez tous les appareils, fusionnez ces sauvegardes et restaurez le résultat partout. Le fichier fusionné devient le maître du cycle suivant. Conserver les maîtres datés dans le nuage vous donne à la fois un mécanisme de synchronisation et une archive : si vous supprimez quelque chose par erreur, un maître antérieur le contient encore."),
        ("Ce qui arrive si vous laissez un appareil de côté un moment",
         "Rien n'est perdu. Un appareil resté hors de plusieurs cycles porte simplement des données plus anciennes ; quand vous finissez par l'inclure, ses notes se fusionnent avec le reste et les éléments répétés sont appariés par GUID au lieu d'être dupliqués. La seule situation qui demande une décision est la même note modifiée sur deux appareils depuis la dernière fusion, et elle apparaît dans le Comparateur de conflits avec les deux versions côte à côte."),
        ("À quelle fréquence est-ce suffisant",
         "Ajustez-la à la quantité de travail que vous accepteriez de refaire. Hebdomadaire convient si vous étudiez sur deux appareils presque tous les jours ; mensuel suffit largement si l'un sert occasionnellement. L'essentiel est de le faire avant toute opération irréversible — changement de téléphone, réinitialisation, réparation — car c'est là qu'une divergence devient une perte."),
        ("Téléphone, tablette et application Windows ensemble",
         "La routine se moque du nombre d'appareils et de leur système. Sauvegardez chacun, fusionnez-les tous en une passe, restaurez le fichier fusionné partout. Un ordinateur Windows servant à la préparation et un téléphone utilisé aux réunions se combinent exactement comme deux téléphones, car toutes les plateformes écrivent le même format de sauvegarde."),
        ("Réduire les conflits avant qu'ils n'apparaissent",
         "Les conflits ne surviennent que lorsque la même note est modifiée sur deux appareils entre deux fusions. En pratique c'est rare, et cela le devient encore plus si vous écrivez sur un seul appareil à la fois : en lisant n'importe où, mais en saisissant là où vous saisissez d'habitude. Fusionner plus souvent réduit aussi la fenêtre pendant laquelle une divergence peut se produire, ce qui vaut mieux que d'essayer de se rappeler quel appareil détient la version la plus récente."),
        ("Ce que la routine rapporte",
         "L'intérêt de garder les appareils fusionnés n'est pas la propreté : c'est que chaque appareil devient une sauvegarde complète de votre bibliothèque d'étude. Perdez ou cassez l'un d'eux et les autres contiennent encore tout, ce qui fait passer le pire scénario d'années de notes perdues à un simple désagrément. C'est une position plus solide que celle offerte par n'importe quelle habitude de sauvegarde sur un seul appareil."),
    ],
    "faq": [
        ("JW Sync tourne-t-il en arrière-plan ?",
         "Non — c'est une page web, pas un service installé. Rien n'analyse vos appareils. "
         "Vous lancez la routine quand vous le décidez ; le rappel facultatif n'est qu'une "
         "notification."),
        ("Puis-je synchroniser trois appareils ou plus ?",
         "Oui. Sauvegardez chacun, chargez tous les fichiers, fusionnez une fois, restaurez "
         "le fichier fusionné partout."),
        ("Et si j'ai modifié la même note sur deux appareils ?",
         "Les deux versions sont conservées jusqu'à votre choix. Le Comparateur de conflits les affiche côte à côte avec une comparaison mot à mot, ou vous pouvez le laisser suggérer la version la plus complète."),
        ("L'ordre de restauration a-t-il de l'importance ?",
         "Non. Une fois le fichier fusionné créé, le restaurer sur chaque appareil les met tous dans le même état complet, dans l'ordre qui vous arrange."),
        ("Puis-je synchroniser trois appareils ou plus ?",
         "Oui. Sauvegardez chacun et chargez-les tous dans la même fusion : aucune limite n'est liée au nombre d'appareils."),
        ("Est-ce automatisable ?",
         "Pas entièrement, car JW Library n'a pas d'API de synchronisation et l'étape de restauration se déroule dans l'application. La routine manuelle prend environ deux minutes une fois prise en main."),
        ("Dois-je fusionner si je ne fais que lire sur le second appareil ?",
         "Si vous n'y annotez jamais, il vous suffit d'y restaurer de temps en temps pour qu'il porte vos notes actuelles."),
    ],
}

GUIDES_FR["transfer-jw-library-notes-new-phone"] = {
    "title": "Comment transférer ses notes JW Library vers un nouveau téléphone",
    "h1": "Comment transférer ses notes JW Library vers un nouveau téléphone",
    "description": "Transférer ses notes JW Library vers un nouveau téléphone, c'est une sauvegarde et une restauration, et l'application s'en charge en deux minutes environ. Voici les étapes, ainsi que le seul cas qu'elle ne sait pas traiter : quand le nouveau téléphone contient déjà des notes.",
    "intro": [
        "C'est plus simple qu'on ne le croit, et aucun outil supplémentaire n'est nécessaire. JW Library intègre la sauvegarde et la restauration, qui emportent chaque note, chaque surlignage, chaque signet et chaque étiquette vers le nouveau téléphone, y compris entre Android et iPhone. Faites-le tant que l'ancien appareil fonctionne encore : l'ensemble prend quelques minutes.",
        "La seule partie à faire délibérément, c'est le transfert lui-même : les outils de migration d'un téléphone à l'autre déplacent vos applications et vos photos, mais ignorent les données d'étude personnelle de JW Library. Créez donc le fichier de sauvegarde plutôt que de supposer qu'il suivra tout seul.",
        "Il existe exactement une situation que l'application ne sait pas traiter, et il vaut mieux la connaître avant de commencer : si vous avez déjà étudié sur le nouveau téléphone, restaurer la sauvegarde de l'ancien effacera ce travail, car une restauration remplace intégralement la bibliothèque de l'appareil. Si c'est votre cas, la section sur la fusion plus bas est celle qui vous intéresse.",
    ],
    "steps": [
        ("Créez une sauvegarde sur l'ancien téléphone",
         "Ouvrez JW Library → Étude personnelle → menu à trois points → Sauvegarde et "
         "restauration → Créer une sauvegarde. Cela enregistre un fichier .jwlibrary "
         "contenant toutes vos données d'étude."),
        ("Transférez le fichier vers le nouveau téléphone",
         "Envoyez-le-vous par e-mail, ou utilisez Google Drive, iCloud, AirDrop ou un câble "
         "USB. Le fichier est petit — quelques mégaoctets en général."),
        ("Restaurez sur le nouveau téléphone",
         "Installez JW Library, puis Étude personnelle → Sauvegarde et restauration → "
         "Restaurer, et choisissez le fichier .jwlibrary. Toutes les notes, surlignages, "
         "signets et étiquettes apparaissent."),
    ],
    "sections": [
        ("Déjà des notes sur le nouveau téléphone ? Fusionnez au lieu d'écraser",
         "Restaurer remplace ce qui se trouve sur l'appareil. Si vous utilisez le nouveau "
         "téléphone depuis un moment et qu'il a ses propres notes, ne restaurez pas "
         "par-dessus : sauvegardez aussi le nouveau téléphone, fusionnez l'ancienne et la "
         "nouvelle sauvegarde en un seul fichier sur jwsync.org (gratuit, dans le navigateur, "
         "sans rien envoyer), puis restaurez le fichier fusionné. Vous gardez les deux "
         "ensembles de notes."),
        ("Un piège fréquent sur iPhone",
         "Si le fichier de sauvegarde arrive sur un iPhone renommé en .zip, renommez-le en "
         ".jwlibrary avant de restaurer — le contenu est intact ; seule l'extension a changé "
         "en route."),
        ("À faire avant d'effacer ou de rendre l'ancien téléphone",
         "La sauvegarde doit être créée pendant que l'ancien téléphone fonctionne encore et que JW Library y est toujours installé. Une fois l'appareil réinitialisé, repris ou transmis, les notes partent avec lui : JW Library ne conserve aucune copie infonuagique des données d'étude personnelle, et une sauvegarde du téléphone comme Google One ou une sauvegarde d'appareil iCloud restaure souvent un instantané plus ancien des données de l'application, voire aucun. Créez d'abord le fichier .jwlibrary, mettez-le en lieu sûr et vérifiez que vous le voyez avant d'effacer quoi que ce soit."),
        ("Récupérer le fichier depuis l'ancien téléphone",
         "Sous Android, le fichier est écrit dans le dossier que vous choisissez — généralement Téléchargements ou Documents — et vous pouvez le déplacer avec n'importe quel gestionnaire de fichiers, vous l'envoyer par courriel ou le déposer dans le nuage. Sur iPhone, la feuille de partage apparaît dès la création : enregistrez-le dans Fichiers, envoyez-le par AirDrop vers le nouveau téléphone ou expédiez-le-vous. La méthode n'a pas d'importance et ne peut pas corrompre le fichier : un .jwlibrary est une archive unique qui arrive intacte ou n'arrive pas."),
        ("Pourquoi une application de transfert entre téléphones ne suffit pas",
         "Des outils comme Smart Switch, Transfert vers iOS ou une restauration iCloud copient les applications et les données système, mais les bases de données privées des applications sont souvent ignorées, restaurées partiellement ou restaurées depuis un point antérieur. On découvre régulièrement le manque des semaines plus tard, quand l'ancien téléphone n'est plus là. Traitez le fichier .jwlibrary comme la copie de référence et le transfert du téléphone comme un confort : s'il apporte vos notes, restaurer votre propre sauvegarde par-dessus ne coûte rien."),
        ("Vérifiez que le transfert a fonctionné",
         "Après la restauration sur le nouveau téléphone, ouvrez deux ou trois publications que vous avez annotées récemment et vérifiez que les notes, les couleurs de surlignage et les signets sont là. Un contrôle plus rapide consiste à ouvrir le fichier de sauvegarde lui-même dans votre navigateur avant d'effacer l'ancien appareil : vous voyez toutes les notes, tous les surlignages et tous les signets qu'il contient, donc vous savez ce qui doit apparaître. N'effacez l'ancien téléphone qu'une fois le nouveau vérifié."),
        ("Si vous changez aussi de tablette ou d'ordinateur",
         "Le même fichier convient partout. Si vous configurez en même temps un nouveau téléphone et une tablette, restaurez le même fichier .jwlibrary sur les deux : ils démarrent identiques. Ils divergeront ensuite selon ce que vous étudiez sur chacun, alors autant décider maintenant si vous les garderez fusionnés régulièrement ou si vous traiterez l'un comme l'appareil principal."),
        ("Si le nouveau téléphone contient déjà des notes",
         "Cela arrive quand on utilise le nouvel appareil une semaine avant de s'occuper du transfert. Une restauration directe remplacerait ce travail par les données de l'ancien téléphone. Sauvegardez d'abord le nouveau téléphone, fusionnez ce fichier avec la sauvegarde de l'ancien et restaurez le résultat : les deux ensembles de notes se retrouvent dans une seule bibliothèque au lieu que l'un écrase l'autre."),
        ("Que faire une fois le nouveau téléphone opérationnel",
         "Vérifiez avant de vous séparer de quoi que ce soit. Ouvrez sur le nouveau téléphone quelques publications annotées récemment et confirmez la présence des notes, des couleurs et des signets ; ensuite seulement, effacez ou rendez l'ancien appareil, dans cet ordre et jamais l'inverse. Une fois installé, placez une sauvegarde hors du téléphone, car la situation qui vous a amené sur cette page reviendra au prochain changement."),
    ],
    "faq": [
        ("Est-ce que cela transfère aussi mes publications téléchargées ?",
         "La sauvegarde contient vos données d'étude personnelle — notes, surlignages, "
         "signets, étiquettes et listes de lecture. Les publications se retéléchargent "
         "simplement sur le nouveau téléphone."),
        ("Est-ce grave si les téléphones ont des versions d'Android différentes ?",
         "Non. Le format .jwlibrary est le même partout, y compris entre versions d'Android "
         "et entre Android et iPhone."),
        ("Puis-je récupérer mes notes si l'ancien téléphone n'est plus là ?",
         "Seulement s'il existe un fichier .jwlibrary quelque part : dans Fichiers, Téléchargements, un courriel que vous vous êtes envoyé ou le nuage. Sans lui, il n'y a rien à restaurer, car les données d'étude personnelle ne sont stockées que sur l'appareil."),
        ("Les deux téléphones doivent-ils avoir la même version de JW Library ?",
         "Elles n'ont pas besoin d'être identiques, mais mettez le nouveau téléphone à jour vers la version actuelle avant de restaurer. Une sauvegarde créée par une version plus récente peut utiliser un schéma de base de données qu'une application plus ancienne ne comprend pas."),
        ("Devrai-je retélécharger mes publications ?",
         "Généralement oui, car les médias des publications ne font pas partie de la sauvegarde. Vos notes se rattachent à chaque publication dès qu'elle est téléchargée, donc rien de ce que vous avez écrit n'est perdu entre-temps."),
        ("Combien de temps cela prend-il en tout ?",
         "Quelques minutes. Créer la sauvegarde prend quelques secondes, déplacer le fichier dépend de la méthode et la restauration est rapide. Le plus long est de retélécharger les publications, ce qui peut se faire en arrière-plan."),
        ("Puis-je le faire sans Wi-Fi ?",
         "Le transfert lui-même oui, par AirDrop ou par câble. Retélécharger les publications sur le nouvel appareil demande une connexion."),
    ],
}

GUIDES_FR["jw-library-android-to-iphone"] = {
    "title": "Passer JW Library d'Android à iPhone (en gardant toutes ses notes)",
    "h1": "Passer JW Library d'Android à iPhone ou iPad — sans perdre une note",
    "description": "Le format de sauvegarde .jwlibrary est identique sur Android et iOS. "
                   "Comment transférer vos notes, surlignages et signets d'une plateforme à "
                   "l'autre — et fusionner si les deux appareils ont des notes.",
    "intro": [
        "Passer d'Android à iPhone semble être le cas difficile ; c'est le cas facile. JW Library écrit le même format de sauvegarde sur toutes les plateformes où il fonctionne, donc transporter une bibliothèque d'étude d'Android vers iOS est la même opération qu'entre deux téléphones Android : aucune conversion, aucun format d'exportation à choisir, rien de perdu au passage.",
        "Changer de plateforme, c'est le moment où l'on craint de perdre des années de notes "
        "d'étude : les applications de transfert Android vers iPhone ignorent purement et "
        "simplement les données de JW Library. La bonne nouvelle : le format de sauvegarde de "
        "JW Library est identique sur Android, iPhone, iPad et Windows, si bien qu'un "
        "changement de plateforme se résume à une sauvegarde, un transfert de fichier et une "
        "restauration.",
    ],
    "steps": [
        ("Sauvegardez sur le téléphone Android",
         "JW Library → Étude personnelle → menu à trois points → Sauvegarde et restauration → "
         "Créer une sauvegarde. Enregistrez le fichier .jwlibrary."),
        ("Envoyez le fichier vers l'iPhone ou l'iPad",
         "E-mail, Google Drive, iCloud Drive — n'importe quoi qui transfère un fichier. Si "
         "iOS le renomme en .zip en route, renommez-le en .jwlibrary."),
        ("Restaurez sur le nouvel appareil",
         "Installez JW Library, connectez-vous, puis Sauvegarde et restauration → Restaurer "
         "et choisissez le fichier. Notes, surlignages, signets, étiquettes et listes de "
         "lecture arrivent tous."),
    ],
    "sections": [
        ("Si l'iPhone contient déjà des notes",
         "Une restauration remplace les données de l'appareil. Quand le nouvel appareil porte "
         "déjà ses propres notes, sauvegardez-le lui aussi et fusionnez d'abord les deux "
         "sauvegardes en un seul fichier sur jwsync.org — la fusion réunit les deux "
         "bibliothèques dans votre navigateur, sans rien envoyer — puis restaurez le fichier "
         "fusionné. Rien n'est perdu d'un côté ni de l'autre."),
        ("Les mêmes étapes fonctionnent dans tous les sens",
         "D'iPhone à Android, d'Android à Android, pour ajouter un iPad comme deuxième "
         "appareil d'étude ou pour passer à l'application Windows : le fichier de sauvegarde "
         "est la langue commune de tous."),
        ("Pourquoi le format est identique sur les deux plateformes",
         "JW Library utilise le même format de sauvegarde partout où il fonctionne : Android, iOS, iPadOS et Windows. Un fichier .jwlibrary est une archive ZIP contenant une base de données SQLite aux mêmes tables et au même schéma, quel que soit l'appareil qui l'a écrite. Il n'y a pas d'étape de conversion, pas de va-et-vient d'exportation et d'importation, rien de spécifique à une plateforme dans le fichier. Une sauvegarde Android se restaure sur un iPhone exactement comme le ferait une sauvegarde iPhone."),
        ("La seule partie qui change vraiment",
         "Pas le fichier, seulement la façon de mettre la main dessus. Sous Android, la sauvegarde est enregistrée dans un dossier que vous choisissez et se déplace avec n'importe quel gestionnaire de fichiers. Sur iPhone, elle passe par la feuille de partage vers Fichiers, AirDrop ou ce que vous préférez. La friction rencontrée en changeant de plateforme se situe toujours à cette étape de manipulation, jamais dans la compatibilité. Courriel, nuage ou AirDrop conviennent également : l'archive arrive intacte ou pas du tout."),
        ("Couleurs de surlignage, étiquettes et réponses d'étude",
         "Tout survit. Les couleurs de surlignage sont enregistrées sous forme d'indice numérique — jaune, vert, bleu, rose, orange et violet — et s'affichent de la même façon sur toutes les plateformes. Les étiquettes et les liens entre étiquettes et notes suivent, tout comme les réponses saisies dans les champs des questions d'étude. Ce que vous voyez sur l'iPhone après la restauration correspond à ce que vous aviez sur l'appareil Android."),
        ("Si iOS refuse de vous laisser choisir le fichier",
         "Enregistrez d'abord le fichier dans l'application Fichiers, puis sélectionnez-le depuis là plutôt que depuis une pièce jointe de courriel ou l'aperçu d'une messagerie. Certaines applications remettent à iOS une copie temporaire d'aperçu au lieu du vrai fichier, et JW Library ne peut pas l'ouvrir. Si le fichier est arrivé en pièce jointe, touchez-le, choisissez Enregistrer dans Fichiers et restaurez depuis Fichiers."),
        ("Préparez l'iPhone avant de restaurer",
         "Installez JW Library depuis l'App Store et mettez-le à jour vers la version actuelle avant toute restauration. Une sauvegarde écrite par une version plus récente peut utiliser un schéma de base de données qu'une version antérieure ne comprend pas, et la restauration sera simplement refusée. Aucune connexion à un compte n'est nécessaire : les données d'étude personnelle sont dans le fichier que vous restaurez, pas dans un compte."),
        ("Si vous avez déjà commencé à étudier sur l'iPhone",
         "Sauvegardez d'abord l'iPhone. Restaurer le fichier Android par-dessus remplacerait tout ce que vous avez écrit depuis le changement. Fusionner les deux sauvegardes produit un fichier contenant les deux, que vous restaurez ensuite : l'historique Android et les nouvelles notes de l'iPhone se retrouvent dans la même bibliothèque."),
        ("Garder les deux téléphones en service ensuite",
         "Certains conservent l'ancien Android comme second lecteur plutôt que de le retirer. Cela fonctionne, mais les deux divergeront dès que vous annoterez sur l'un et l'autre, faute de synchronisation entre eux. Si vous comptez utiliser les deux, prévoyez de fusionner leurs sauvegardes régulièrement plutôt que de supposer qu'ils restent alignés."),
        ("Après le changement",
         "Laissez à l'iPhone le temps de retélécharger les publications que vous utilisez le plus, puis vérifiez quelques publications annotées pour confirmer que tout est arrivé : notes, couleurs de surlignage, signets et étiquettes. Conservez le fichier de sauvegarde Android même une fois le changement terminé : c'est un instantané daté de votre bibliothèque, et le garder ne coûte rien."),
    ],
    "faq": [
        ("Ai-je besoin d'un ordinateur ?",
         "Non. Tout le transfert peut se faire de téléphone à téléphone, par e-mail ou via un "
         "espace de stockage en ligne."),
        ("Les couleurs de mes surlignages survivent-elles au transfert ?",
         "Oui — les surlignages gardent leurs couleurs, les notes gardent leurs étiquettes et "
         "les signets gardent leur place."),
        ("Ai-je besoin d'un ordinateur pour cela ?",
         "Non. AirDrop, le courriel ou n'importe quelle application de stockage infonuagique déplace le fichier directement entre les deux téléphones."),
        ("Cela fonctionne-t-il dans l'autre sens, d'iPhone vers Android ?",
         "Oui, à l'identique. Les mêmes étapes fonctionnent dans toutes les directions, y compris depuis et vers l'application Windows."),
        ("L'iPhone aura-t-il besoin des mêmes publications téléchargées ?",
         "Oui, puisque les médias des publications ne font pas partie d'une sauvegarde. Les notes se rattachent à chaque publication dès son téléchargement."),
        ("Dois-je conserver le téléphone Android ensuite ?",
         "Non, une fois que vous avez vérifié que les notes sont présentes sur l'iPhone. Contrôlez quelques publications annotées avant d'effacer ou de rendre l'ancien appareil."),
        ("Le transfert fonctionne-t-il pour les réponses aux questions d'étude ?",
         "Oui. Les réponses saisies font partie des données d'étude personnelle et suivent avec le reste."),
        ("Y a-t-il un risque de perdre des notes lors du changement ?",
         "Pas si vous conservez la sauvegarde Android. La restauration écrit sur l'iPhone et ne modifie jamais le fichier qu'elle lit : l'original reste intact comme filet de sécurité. Gardez-le jusqu'à ce que vous ayez vérifié que l'iPhone a tout, et idéalement après aussi : c'est un instantané daté de votre bibliothèque."),
        ("Et si le téléphone Android ne crée pas la sauvegarde ?",
         "Vérifiez d'abord l'espace disponible, l'application ayant besoin de place pour écrire le fichier. Si c'est l'application elle-même qui échoue, la mettre à jour ou redémarrer l'appareil règle généralement le problème. Les données restent intactes pendant ce temps."),
    ],
}

GUIDES_FR["backup-jw-library"] = {
    "title": "Comment sauvegarder JW Library correctement",
    "h1": "Comment sauvegarder JW Library correctement",
    "description": "Une routine de sauvegarde de 30 secondes : ce que contient réellement un fichier .jwlibrary, où le conserver, et pourquoi en avoir un à jour vaut la peine même quand rien n'a mal tourné.",
    "intro": [
        "Une sauvegarde prend une demi-minute et mérite d'en faire une habitude, quoique pas tout à fait pour la raison qu'on avance d'ordinaire. La sauvegarde et la restauration de JW Library transfèrent déjà très bien une bibliothèque vers un nouvel appareil ; une sauvegarde est donc moins une assurance que la matière première de tout ce que vous voudrez faire d'autre avec votre étude.",
        "Un fichier .jwlibrary est la seule forme que prend votre bibliothèque en dehors de l'application. C'est ce que vous fusionnez quand deux appareils ont chacun servi à étudier, ce que vous ouvrez pour lire, réétiqueter ou réorganiser des années de notes, ce que vous interrogez par le sens quand vous ne vous rappelez qu'à moitié ce que vous aviez écrit, et ce d'où vous tirez un ensemble de notes à envoyer à un ami. En avoir un à jour, c'est ce qui rend tout cela possible.",
    ],
    "steps": [
        ("Créez la sauvegarde",
         "Ouvrez JW Library → Étude personnelle → menu à trois points → Sauvegarde et "
         "restauration → Créer une sauvegarde. Cela produit un fichier .jwlibrary contenant "
         "chaque note, surlignage, signet et étiquette."),
        ("Rangez-la ailleurs que sur le téléphone",
         "Envoyez-la-vous par e-mail, ou enregistrez-la sur Google Drive, iCloud ou OneDrive. "
         "Une sauvegarde qui ne vit que sur le téléphone disparaît avec le téléphone."),
        ("Recommencez régulièrement",
         "Une fois par mois est un bon rythme ; avant tout changement d'appareil, "
         "réinitialisation ou mise à jour du système, c'est indispensable. Gardez les copies "
         "anciennes — les fichiers sont petits, et une vieille sauvegarde a déjà sauvé bien "
         "des gens."),
    ],
    "sections": [
        ("L'erreur classique : se fier à la sauvegarde cloud du téléphone",
         "Une sauvegarde du téléphone entier (Google One, sauvegarde d'appareil iCloud) "
         "restaure souvent une copie ancienne des données de JW Library — ou aucune. Le "
         "fichier .jwlibrary est la seule sauvegarde que vous maîtrisez entièrement et que "
         "vous pouvez emporter d'une plateforme à l'autre. Considérez la sauvegarde du "
         "téléphone comme un bonus, pas comme le plan."),
        ("Vous vous retrouvez avec deux sauvegardes différentes ?",
         "Cela arrive : une sauvegarde du téléphone, une plus ancienne de la tablette, "
         "chacune avec des notes uniques. Vous n'avez jamais à choisir entre les deux — "
         "fusionnez-les en un seul fichier complet sur jwsync.org, gratuitement et en privé, "
         "directement dans le navigateur."),
        ("Ce que le fichier contient, et ce qu'il ne contient pas",
         "La sauvegarde conserve vos données d'étude personnelle : notes, surlignages et leurs couleurs, signets, étiquettes et les réponses saisies dans les champs des questions d'étude. Elle ne conserve pas les publications : ni Bibles, ni périodiques, ni livres, ni vidéos, ni audio. C'est pourquoi une sauvegarde représentant des années d'étude ne pèse que quelques mégaoctets, et pourquoi restaurer sur un nouvel appareil vous laisse retélécharger des publications alors que chaque note écrite est déjà revenue à sa place."),
        ("Combien de sauvegardes conserver",
         "Plus d'une. Ce qui coûte leurs notes aux gens est rarement un fichier perdu : c'est une bonne sauvegarde écrasée par une mauvaise, ou une restauration effectuée sur le mauvais appareil. Comme les fichiers sont petits, il n'y a aucune raison de supprimer les anciens : conservez-les datés dans un dossier infonuagique. Une sauvegarde d'il y a six mois ne perd pas sa valeur même si vous en avez de plus récentes, car tout ce que vous avez supprimé par erreur depuis s'y trouve encore."),
        ("Où les conserver",
         "N'importe où, sauf uniquement sur l'appareil lui-même. Un dossier dans Drive, iCloud, Dropbox ou OneDrive couvre le cas qui compte le plus : l'appareil perdu, volé, réinitialisé ou endommagé. Vous envoyer le fichier par courriel fonctionne aussi et a l'avantage de le dater. Le fichier contient vos propres notes d'étude : traitez-le avec le soin que vous accorderiez à tout document personnel."),
        ("Vérifier une sauvegarde avant de compter dessus",
         "Une sauvegarde que vous n'avez jamais ouverte est une hypothèse, pas un filet de sécurité. Vous pouvez ouvrir un fichier .jwlibrary dans votre navigateur et voir exactement quelles notes, quels surlignages et quels signets il contient : une vérification de trente secondes qui transforme l'hypothèse en fait. Cela compte surtout juste avant une opération irréversible : réinitialisation d'usine, reprise, réparation ou grosse mise à jour du système."),
        ("Les moments où il vaut la peine de sauvegarder",
         "Tout moment où l'appareil change de mains ou d'état : mise à jour du système, réinitialisation d'usine, réparation ou changement d'écran, reprise, ou transmission de l'appareil à quelqu'un. Ajoutez-y la fin de tout ce que vous détesteriez refaire : une assemblée, un congrès, une période de préparation d'un discours. Les sauvegardes sont rapides et peu coûteuses, donc la bonne habitude consiste à les lier à des événements plutôt qu'au calendrier."),
        ("Une sauvegarde du téléphone n'est pas une sauvegarde de JW Library",
         "Google One, une sauvegarde d'appareil iCloud ou l'outil de transfert du fabricant travaillent au niveau de l'appareil et traitent les données privées des applications de façon inégale. Il arrive régulièrement qu'une restauration complète du téléphone ramène les applications et les réglages mais pas les notes d'étude, ou une version datant de plusieurs semaines. Le fichier .jwlibrary est la seule copie dont vous contrôlez et pouvez vérifier le contenu : traitez la sauvegarde du téléphone comme un bonus, pas comme le plan."),
        ("En faire une habitude qui tient",
         "La routine qui tient vraiment est celle rattachée à quelque chose que vous faites déjà : sauvegarder en terminant la préparation de la semaine, ou le jour où vous réglez vos autres tâches périodiques. Enregistrez toujours dans le même dossier pour que les fichiers s'accumulent au même endroit, et laissez-y les anciens. Un dossier de sauvegardes datées remontant à des années est la forme la plus robuste que cela puisse prendre, et l'entretenir prend quelques secondes par semaine."),
    ],
    "faq": [
        ("Quelle taille fait un fichier de sauvegarde ?",
         "Quelques mégaoctets en général, même pour de très grandes bibliothèques — la taille "
         "d'une pièce jointe."),
        ("Créer une sauvegarde change-t-il quelque chose sur mon téléphone ?",
         "Non. Cela écrit seulement le fichier ; votre bibliothèque n'est pas touchée."),
        ("La sauvegarde inclut-elle mes publications téléchargées ?",
         "Non. Uniquement les données d'étude personnelle. Les publications se retéléchargent sur le nouvel appareil et vos notes s'y rattachent automatiquement."),
        ("Puis-je ouvrir une sauvegarde pour voir ce qu'elle contient ?",
         "Oui. Vous pouvez ouvrir un fichier .jwlibrary dans votre navigateur et parcourir toutes les notes, tous les surlignages et tous les signets qu'il contient, sans rien installer et sans que le fichier quitte votre appareil."),
        ("Les sauvegardes expirent-elles ?",
         "Non. Un fichier .jwlibrary reste restaurable indéfiniment. Restaurez dans une version actuelle de JW Library plutôt que dans une ancienne, l'application lisant les formats de sauvegarde antérieurs mais pas les plus récents."),
        ("Dois-je sauvegarder avant chaque réunion ?",
         "Ce n'est pas nécessaire. Liez les sauvegardes aux événements susceptibles de vous coûter des données — mises à jour, réparations, nouveaux appareils — plus un rythme régulier proportionné à ce que vous accepteriez de refaire."),
        ("Vaut-il la peine de garder des sauvegardes d'il y a des années ?",
         "Oui. Elles sont petites, et tout ce que vous avez supprimé par erreur depuis s'y trouve encore."),
    ],
}

GUIDES_FR["jw-library-restore-replaced-notes"] = {
    "title": "La restauration JW Library a remplacé vos notes ? Comment les récupérer",
    "h1": "La restauration a remplacé vos notes ? Voici comment réunir les deux sauvegardes",
    "description": "La restauration de JW Library est un remplacement complet, pas une "
                   "fusion — les notes écrites après la date de la sauvegarde semblent "
                   "perdues. Si vous avez encore les deux fichiers, rien n'est perdu. Voici "
                   "la solution.",
    "intro": [
        "C'est un moment terrible : vous restaurez une sauvegarde sur un appareil qui portait "
        "déjà des notes, et la restauration remplace tout — les notes écrites depuis cette "
        "sauvegarde semblent disparues. Cela arrive parce que Sauvegarde et restauration de "
        "JW Library est un remplacement complet, pas une fusion.",
        "Le point essentiel : si le travail le plus récent existe encore dans un fichier de "
        "sauvegarde, rien n'est réellement perdu. La solution consiste à fusionner les deux "
        "sauvegardes au lieu de choisir entre elles.",
    ],
    "steps": [
        ("Stop — ne restaurez pas à nouveau",
         "Chaque restauration remplace les données actuelles de l'appareil. Faites une pause "
         "avant que quoi que ce soit d'autre ne disparaisse."),
        ("Sauvegardez l'appareil tel qu'il est maintenant",
         "Étude personnelle → Sauvegarde et restauration → Créer une sauvegarde. Cela "
         "préserve l'état actuel, quel qu'il soit."),
        ("Retrouvez la sauvegarde contenant les notes manquantes",
         "Le fichier .jwlibrary que vous avez restauré, ou un plus ancien — regardez dans vos "
         "e-mails, Drive, iCloud et votre dossier de téléchargements."),
        ("Fusionnez les deux fichiers sur jwsync.org",
         "Chargez les deux sauvegardes. JW Sync réunit toutes les notes, surlignages, signets "
         "et étiquettes des deux dans un nouveau fichier — dans votre navigateur, sans rien "
         "envoyer. Les versions en conflit d'une même note sont présentées côte à côte pour "
         "que vous choisissiez."),
        ("Restaurez le fichier fusionné",
         "Sauvegarde et restauration → Restaurer avec le .jwlibrary fusionné. Les deux "
         "ensembles de notes sont de retour sur l'appareil."),
    ],
    "sections": [
        ("Et s'il n'existe aucune sauvegarde des notes récentes ?",
         "Si la seule copie des notes récentes se trouvait sur l'appareil et qu'une "
         "restauration les a déjà écrasées, JW Library n'offre aucune annulation. C'est "
         "précisément pourquoi l'étape 2 ci-dessus — sauvegarder l'état actuel avant toute "
         "autre action — compte tant dès que quelque chose semble anormal. À l'avenir, la "
         "routine « fusionner d'abord » rend le problème structurellement impossible."),
    ],
    "faq": [
        ("La fusion va-t-elle dupliquer les notes communes aux deux sauvegardes ?",
         "Non — les éléments identiques sont détectés et conservés une seule fois. Seules les "
         "versions réellement différentes d'une même note sont signalées pour examen."),
        ("Est-ce que cela répare une sauvegarde qui refuse de se restaurer ?",
         "C'est en général un fichier endommagé plutôt qu'un écrasement — voyez plus bas le "
         "guide sur la réparation d'une sauvegarde corrompue."),
    ],
}

GUIDES_FR["fix-corrupted-jw-library-backup"] = {
    "title": "Réparer une sauvegarde JW Library corrompue qui ne se restaure pas",
    "h1": "Réparer une sauvegarde JW Library corrompue avec le Docteur de bibliothèque",
    "description": "JW Library refuse de restaurer votre fichier .jwlibrary ? Le Docteur de "
                   "bibliothèque analyse la sauvegarde dans votre navigateur, répare les "
                   "problèmes courants et produit une copie propre qui se restaure.",
    "intro": [
        "Une sauvegarde qui ne se restaure pas n'est pas forcément une sauvegarde qui a perdu vos notes. La plupart des fichiers décrits comme corrompus sont structurellement sains et refusés pour une raison réparable, ou abîmés pendant le transfert d'une manière qu'une nouvelle copie règle. Il vaut la peine de passer en revue les causes avant de renoncer au fichier.",
        "Il arrive que JW Library refuse un fichier de sauvegarde : la restauration échoue, "
        "renvoie une erreur, ou le fichier ne s'ouvre pas. Causes fréquentes : un "
        "téléchargement interrompu, un espace de stockage en ligne qui a abîmé le fichier, une "
        "extension modifiée en route, ou des incohérences internes accumulées au fil des "
        "années.",
        "JW Sync inclut le Docteur de bibliothèque, un vérificateur qui analyse un fichier "
        ".jwlibrary et répare les problèmes courants — entièrement dans votre navigateur, "
        "sans que le fichier ne quitte jamais votre appareil.",
    ],
    "steps": [
        ("Ouvrez JW Sync et chargez le fichier problématique",
         "Allez sur jwsync.org et chargez le fichier .jwlibrary qui refuse de se restaurer. "
         "(S'il est arrivé renommé en .zip, renommez-le d'abord en .jwlibrary — cela suffit "
         "dans bien des cas.)"),
        ("Lancez l'analyse du Docteur de bibliothèque",
         "Le Docteur examine la structure interne de la sauvegarde et liste ce qu'il trouve — "
         "des bizarreries anodines aux vrais dégâts — en langage clair."),
        ("Appliquez les réparations",
         "Une pression répare ce qui est réparable. Le Docteur ne modifie jamais votre "
         "fichier d'origine ; il produit une copie nettoyée, l'original reste donc intact en "
         "filet de sécurité."),
        ("Téléchargez et restaurez le fichier réparé",
         "Restaurez le .jwlibrary nettoyé via Sauvegarde et restauration → Restaurer dans JW "
         "Library."),
    ],
    "sections": [
        ("Le Docteur s'exécute aussi à chaque fusion",
         "Les mêmes vérifications tournent automatiquement dans le moteur de fusion : une "
         "sauvegarde fusionnée est donc toujours livrée propre — même quand l'un des fichiers "
         "d'entrée avait des problèmes que vous ignoriez."),
        ("Quand un fichier est irréparable",
         "Si le fichier a été tronqué au point que les données n'y sont tout simplement plus, "
         "aucun outil ne peut les réinventer. Le Docteur le dira honnêtement plutôt que de "
         "produire un fichier douteux — et c'est le signal qu'il faut chercher une copie plus "
         "ancienne dans vos e-mails, sur Drive ou iCloud, ce qui explique aussi pourquoi il "
         "vaut la peine de garder les vieilles sauvegardes."),
        ("Ce que corrompu signifie généralement",
         "En pratique, il s'agit rarement de données abîmées. Les causes courantes sont un fichier tronqué au transfert — écourté par un envoi qui a échoué ou par une messagerie qui l'a compressé — ou une archive intacte contenant des incohérences internes que l'application refuse. Comme un .jwlibrary est une archive ZIP enveloppant une base SQLite, le problème peut venir de l'une ou l'autre couche, et elles appellent des remèdes différents : un fichier tronqué ne se répare pas et doit être récupéré à nouveau ; une base incohérente, généralement si."),
        ("Ce qu'une analyse vérifie réellement",
         "Une analyse contrôle que l'archive s'ouvre, que userData.db est une base SQLite lisible qui passe un contrôle d'intégrité, que le schéma correspond à ce qu'attend JW Library, et que le manifeste concorde avec la base qu'il décrit — y compris l'empreinte que l'application utilise pour confirmer que le fichier n'a pas été modifié. Un écart entre le manifeste et la base est l'une des raisons les plus fréquentes de refus d'une sauvegarde techniquement saine, et il se répare directement."),
        ("Les lignes orphelines sont généralement sans gravité",
         "L'analyse d'une vraie sauvegarde signale souvent des lignes renvoyant à quelque chose qui n'existe plus : un surlignage pointant vers un emplacement de publication qui a bougé, par exemple. Les sauvegardes de JW Library elles-mêmes en contiennent couramment des centaines et se restaurent sans broncher. C'est une conséquence normale de la mise à jour des publications au fil du temps, non un signe de dommage, et il n'est pas nécessaire de les supprimer pour que le fichier fonctionne."),
        ("Sauver des notes d'un fichier qui ne se restaure pas",
         "Même quand une sauvegarde ne peut pas être réparée au point d'être acceptée par JW Library, les notes qu'elle contient restent souvent lisibles. Ouvrir le fichier dans votre navigateur permet de voir et de copier directement le texte, ce qui transforme un fichier inutilisable en matière d'étude récupérée. Si vous disposez d'une seconde sauvegarde plus ancienne qui se restaure, le contenu lisible du fichier abîmé peut lui être réuni plutôt que retapé."),
        ("Quand la restauration échoue sans message clair",
         "JW Library refuse souvent un fichier sans expliquer pourquoi. Les causes les plus fréquentes sont un manifeste dont l'empreinte ne correspond plus à la base qu'il décrit, un fichier tronqué au transfert, ou une sauvegarde écrite par une version de l'application plus récente que celle dans laquelle vous restaurez. La première se répare, la deuxième exige de récupérer à nouveau le fichier à la source, et la troisième se règle en mettant l'application à jour avant de restaurer."),
        ("L'éviter la prochaine fois",
         "L'essentiel des dommages survient en transit. Déplacez les sauvegardes comme des fichiers et non via quoi que ce soit susceptible de les recompresser, et préférez le nuage, AirDrop ou un câble aux messageries. Après le transfert, vérifiez que la taille correspond à l'original : un fichier nettement plus petit que celui envoyé a été tronqué, et aucune réparation ne ramènera des octets qui ne sont jamais arrivés."),
        ("Si rien ne marche",
         "Un fichier irréparable peut malgré tout être lisible, et le lire suffit souvent : le texte des notes se récupère directement même quand JW Library refuse le fichier. Combinez cela avec une sauvegarde plus ancienne qui se restaure et vous obtenez généralement l'essentiel de votre bibliothèque. Avant de juger un fichier inutilisable, ouvrez-le et voyez ce qu'il contient vraiment."),
    ],
    "faq": [
        ("Mes données sont-elles envoyées pour l'analyse ?",
         "Non. L'analyse, les réparations et l'export s'exécutent tous localement, dans le "
         "navigateur."),
        ("Peut-il récupérer des notes supprimées dans JW Library ?",
         "Non — il répare la structure du fichier. Les notes supprimées dans l'application "
         "avant la sauvegarde ne sont pas dans le fichier, donc pas récupérables."),
        ("Réparer le fichier fait-il perdre des notes ?",
         "Les réparations travaillent sur une copie et traitent des problèmes de structure, pas de contenu. Votre fichier d'origine n'est jamais modifié : il reste disponible si vous voulez recommencer."),
        ("Pourquoi ma sauvegarde s'est-elle corrompue ?",
         "Le plus souvent le fichier a été altéré en transit : envoyé via une application qui l'a compressé ou tronqué, ou un téléversement qui n'a pas abouti. Le transférer à nouveau depuis la source règle généralement la question."),
        ("Une analyse peut-elle récupérer des notes supprimées dans JW Library ?",
         "Non. Une fois supprimée dans l'application et une nouvelle sauvegarde faite, la note n'est plus dans ce fichier. Une sauvegarde antérieure à la suppression la contiendra encore."),
        ("La taille du fichier indique-t-elle s'il est tronqué ?",
         "Souvent oui. Comparez-la à l'original si vous l'avez encore ; un écart important signifie que le transfert n'est pas allé à son terme."),
        ("Une sauvegarde qui s'ouvre dans le navigateur se restaurera-t-elle à coup sûr ?",
         "Ce n'est pas une garantie, mais c'est un signe fort que l'archive et la base sont saines, ce qui écarte les défaillances les plus courantes."),
    ],
}

GUIDES_FR["edit-jw-library-notes"] = {
    "title": "Consulter et modifier ses notes JW Library dans le navigateur",
    "h1": "Consultez, cherchez et modifiez vos notes JW Library — l'Explorateur d'étude",
    "description": "Ouvrez n'importe quelle sauvegarde .jwlibrary dans votre navigateur pour "
                   "parcourir, chercher, modifier, réétiqueter, recolorer et nettoyer en lot "
                   "vos notes, surlignages et signets JW Library. Rien n'est envoyé.",
    "intro": [
        "JW Library est conçu pour prendre des notes, pas pour en gérer des milliers. "
        "L'Explorateur d'étude ouvre n'importe quelle sauvegarde .jwlibrary directement dans "
        "votre navigateur et la transforme en gestionnaire de bibliothèque consultable et "
        "modifiable — notes, surlignages et signets au même endroit, sans rien envoyer nulle "
        "part.",
    ],
    "steps": [
        ("Chargez une sauvegarde",
         "Créez une sauvegarde dans JW Library (Étude personnelle → Sauvegarde et "
         "restauration → Créer une sauvegarde), puis ouvrez jwsync.org et chargez le fichier "
         "dans l'Explorateur d'étude."),
        ("Parcourez et cherchez dans tout",
         "Trois onglets — Notes, Surlignages, Signets — avec recherche plein texte et filtres "
         "par couleur, étiquette et publication. Un onglet Réponses d'étude affiche aussi vos "
         "réponses saisies dans les publications."),
        ("Modifiez sur place",
         "Ouvrez n'importe quelle note pour en modifier le titre et le contenu avec mise en "
         "forme (gras, italique, souligné, listes), changer sa couleur de surlignage et "
         "ajouter ou retirer des étiquettes. Les signets et les couleurs de surlignage se "
         "modifient de la même façon."),
        ("Nettoyez en lot",
         "Sélectionnez plusieurs notes d'un coup pour les réétiqueter, les recolorer ou les "
         "supprimer ensemble — avec annulation et rétablissement complets, un faux pas n'est "
         "donc jamais fatal. Vous pouvez aussi extraire une plage de dates de notes vers une "
         "nouvelle sauvegarde, ou copier vos notes en Markdown."),
        ("Exportez votre bibliothèque modifiée",
         "Téléchargez le .jwlibrary modifié et restaurez-le dans JW Library. Vos changements "
         "sont maintenant sur l'appareil."),
    ],
    "sections": [
        ("Pourquoi modifier dans un navigateur plutôt que dans l'application ?",
         "L'échelle. Renommer une étiquette sur 300 notes, recolorer tous les surlignages "
         "jaunes d'une publication ou supprimer des années de signets périmés, c'est quelques "
         "minutes ici et des heures de tapotements dans l'application. Le fichier exporté est "
         "une sauvegarde standard, que JW Library restaure comme n'importe quelle autre."),
    ],
    "faq": [
        ("La modification touche-t-elle ma sauvegarde d'origine ?",
         "Non — les modifications se font sur une copie dans le navigateur et sont "
         "enregistrées dans un nouveau fichier exporté. L'original reste tel quel."),
        ("Y a-t-il une limite de taille de bibliothèque ?",
         "Les très grandes bibliothèques sont paginées pour que la navigation reste rapide ; "
         "la recherche et les filtres portent sur l'ensemble."),
    ],
}

GUIDES_FR["search-jw-library-notes"] = {
    "title": "Chercher ses notes JW Library par le sens — Interrogez votre bibliothèque",
    "h1": "Interrogez votre bibliothèque : cherchez vos notes JW Library par le sens",
    "description": "Recherche sémantique pour vos notes JW Library : retrouvez cette note à "
                   "moitié oubliée en la décrivant, même sans vous rappeler ses mots exacts. "
                   "Sur votre appareil, utilisable hors ligne, privée.",
    "intro": [
        "Toute personne ayant des années de notes connaît le problème : vous vous souvenez "
        "d'avoir écrit sur le fait d'endurer les épreuves avec joie, mais la note ne contient "
        "pas le mot « endurance », et la recherche par mot-clé ne trouve rien. Interrogez "
        "votre bibliothèque cherche par le sens : décrivez l'idée, et les notes les plus "
        "proches remontent, quelle qu'en soit la formulation.",
        "Tout s'exécute sur votre appareil : le modèle de langue est téléchargé une fois dans "
        "le navigateur, puis fonctionne hors ligne, avec accélération WebGPU là où elle est "
        "disponible. Vos notes ne sont jamais envoyées nulle part.",
    ],
    "steps": [
        ("Chargez une sauvegarde dans l'Explorateur d'étude",
         "Sur jwsync.org, chargez votre fichier .jwlibrary et ouvrez l'onglet Interroger."),
        ("Laissez le modèle se préparer une fois",
         "À la première utilisation, le modèle local se télécharge et indexe vos notes. Cela "
         "n'arrive qu'une fois ; ensuite, c'est instantané, même hors ligne."),
        ("Posez la question avec vos mots",
         "Tapez ce dont vous vous souvenez — « cette note sur la patience avec les nouveaux "
         "dans le ministère », « encouragement pour des pionniers découragés » — et les notes "
         "les plus proches apparaissent, classées par sens."),
    ],
    "sections": [
        ("En quoi cela diffère de la recherche ordinaire",
         "La recherche par mot-clé compare des lettres ; la recherche sémantique compare des "
         "idées. Une requête sur « l'anxiété » trouve aussi des notes écrites avec "
         "« inquiétude », « les soucis de la vie » ou la citation d'un verset sur le thème. "
         "Les deux types de recherche sont disponibles dans l'Explorateur d'étude — ils se "
         "complètent."),
        ("Privé par conception",
         "Ce n'est pas un service d'IA dans le cloud. Le modèle s'exécute dans l'onglet de "
         "votre navigateur, l'index vit sur votre appareil, et fermer l'onglet met fin à tout. "
         "Rien de vos notes ne quitte jamais votre machine."),
    ],
    "faq": [
        ("Faut-il un appareil puissant ?",
         "Un téléphone ou un ordinateur portable récent s'en sort très bien ; c'est plus "
         "rapide sur les appareils dotés de WebGPU. Plusieurs tailles de modèle sont "
         "proposées selon votre matériel."),
        ("Est-ce que cela fonctionne dans ma langue ?",
         "Oui — la recherche fonctionne dans les langues où vos notes sont écrites, et "
         "l'interface est traduite dans les 12 langues prises en charge par JW Sync."),
    ],
}

GUIDES_FR["jw-library-study-stats"] = {
    "title": "Vos statistiques d'étude JW Library : séries, cartes de chaleur et récompenses",
    "h1": "Vos statistiques d'étude JW Library : séries, cartes de chaleur, couverture et récompenses",
    "description": "Transformez une sauvegarde JW Library en statistiques d'étude privées — "
                   "totaux, carte de chaleur d'activité, séries, couverture des 66 livres "
                   "bibliques, un profil d'étude et près de 200 récompenses.",
    "intro": [
        "Votre fichier de sauvegarde enregistre discrètement des années d'histoire d'étude : "
        "quand vous prenez des notes, ce que vous surlignez, quels livres vous avez "
        "parcourus. La page Statistiques d'étude lit une sauvegarde .jwlibrary et transforme "
        "cette histoire en tableau de bord privé, calculé entièrement dans votre navigateur.",
    ],
    "steps": [
        ("Créez une sauvegarde",
         "Dans JW Library : Étude personnelle → Sauvegarde et restauration → Créer une "
         "sauvegarde."),
        ("Ouvrez la page Statistiques d'étude",
         "Rendez-vous sur jwsync.org/highlights.html et chargez le fichier."),
        ("Explorez votre parcours d'étude",
         "Les grands totaux, les vues Année de service et Depuis toujours, la progression "
         "d'une année sur l'autre — puis, plus bas, les parties amusantes."),
    ],
    "sections": [
        ("Ce que vous verrez",
         "Une carte de chaleur d'activité avec votre plus longue série et la série en cours ; "
         "votre rythme hebdomadaire, vos heures et vos mois les plus chargés ; la couverture "
         "des 66 livres bibliques avec la répartition Écritures hébraïques / grecques ; une "
         "roue des couleurs de surlignage, un histogramme de la profondeur des notes et un "
         "nuage de mots ; une horloge d'étude sur 24 heures et un radar de saisonnalité."),
        ("Profil, parcours et récompenses",
         "Un Profil d'étude à six traits (Régularité, Application, Profondeur, Étendue, "
         "Réflexion, Constance) avec une « Signature d'étude » ; un Parcours d'étude de 60 "
         "niveaux répartis en 12 paliers nommés ; et environ 200 récompenses, de Commune à "
         "Légendaire, y compris des médailles liées au contenu. Une Carte à partager résume "
         "votre année sans exposer la moindre note."),
        ("Une raison quotidienne de revenir",
         "Le panneau Refaire surface montre les notes que vous avez écrites ce même jour les "
         "années passées et bâtit une révision espacée toute en douceur — un peu, souvent, "
         "c'est ainsi que l'étude s'ancre."),
    ],
    "faq": [
        ("Est-ce que quelque chose est envoyé ?",
         "Non. La sauvegarde est analysée dans votre navigateur ; les statistiques ne "
         "quittent jamais votre appareil."),
        ("Les statistiques se mettent-elles à jour toutes seules ?",
         "Elles reflètent la sauvegarde que vous chargez — créez une nouvelle sauvegarde pour "
         "voir des statistiques à jour."),
    ],
}

GUIDES_FR["share-jw-library-notes"] = {
    "title": "Comment partager des notes JW Library avec un ami",
    "h1": "Comment partager des notes JW Library avec un ami — sans serveur",
    "description": "Envoyez des notes JW Library choisies (et leurs surlignages) à un ami dans "
                   "un petit fichier — sans serveur, sans compte. Le destinataire les ajoute "
                   "sans écraser ses propres notes.",
    "intro": [
        "JW Library n'offre aucun moyen de donner à quelqu'un une copie de notes précises. "
        "Envoyer toute votre sauvegarde marcherait — mais cela livre tout, et la restaurer "
        "effacerait la bibliothèque du destinataire. Le partage de notes de JW Sync résout "
        "les deux problèmes : vous choisissez exactement quelles notes partager, et le "
        "destinataire les ajoute sans rien perdre.",
    ],
    "steps": [
        ("Choisissez les notes à partager",
         "Sur la page de partage, jwsync.org/share.html, chargez votre sauvegarde et "
         "sélectionnez les notes — quelques-unes d'un discours, ou tout ce qui porte une "
         "étiquette en un clic grâce au filtre par étiquette du sélecteur. Les surlignages "
         "rattachés à ces notes voyagent avec elles."),
        ("Envoyez le fichier de partage",
         "JW Sync produit un petit fichier contenant uniquement les notes sélectionnées. "
         "Envoyez-le par le canal de votre choix — messagerie, e-mail, AirDrop. Il n'y a ni "
         "serveur ni compte ; le fichier constitue tout l'échange."),
        ("Le destinataire l'ajoute à sa bibliothèque",
         "Votre ami ouvre la même page, charge le fichier de partage avec sa propre "
         "sauvegarde, et obtient une nouvelle sauvegarde où vos notes sont ajoutées. Ses "
         "notes ne sont jamais écrasées — si une note partagée entre en conflit avec l'une "
         "des siennes, il choisit comment elle est ajoutée — et les notes importées arrivent "
         "étiquetées, donc faciles à retrouver, à relire ou à retirer plus tard."),
    ],
    "sections": [
        ("Bons usages",
         "Transmettre des recherches à un partenaire d'étude, partager des notes de réunion "
         "avec un absent, donner à un nouveau proclamateur un premier jeu de notes sur une "
         "publication, ou transférer les notes d'un projet précis à un membre de la famille — "
         "sans exposer le reste d'aucune des deux bibliothèques."),
    ],
    "faq": [
        ("Le destinataire doit-il installer JW Sync ?",
         "Rien n'est installé d'un côté ni de l'autre — c'est une page web. Le destinataire a "
         "seulement besoin du fichier de partage et de sa propre sauvegarde."),
        ("Puis-je annuler un partage ou faire expirer un fichier ?",
         "Le fichier est un fichier ordinaire que vous avez envoyé — il n'y a pas de copie "
         "serveur à faire expirer. Ne partagez que ce que vous partageriez dans un message."),
    ],
}

GUIDES_FR["bible-reading-plan"] = {
    "title": "Un plan de lecture biblique quotidien avec vos propres notes à côté",
    "h1": "Compagnon de lecture : un plan de lecture biblique avec vos notes à côté",
    "description": "Un programme de lecture biblique quotidien et privé qui affiche les notes "
                   "et surlignages que vous avez faits sur les chapitres du jour. Choisissez "
                   "votre rythme, tenez une série, regardez la grille des 66 livres se "
                   "remplir.",
    "intro": [
        "Beaucoup d'applications proposent un programme de lecture biblique. Le Compagnon de "
        "lecture fait ce qu'aucune ne peut faire : comme il lit votre propre sauvegarde "
        ".jwlibrary, la lecture du jour arrive accompagnée des notes et surlignages que vous "
        "avez vous-même faits sur ces chapitres précis — « vous avez surligné quatre versets "
        "du Psaume 37 il y a deux ans ». Lire à travers le prisme de votre propre histoire "
        "d'étude, entièrement sur votre appareil.",
    ],
    "steps": [
        ("Choisissez un ordre et un rythme",
         "Lisez dans l'ordre biblique ou dans un ordre chronologique approximatif ; terminez "
         "en 3 mois, 6 mois, 1 an, 2 ans, ou fixez votre propre rythme de chapitres par "
         "jour — avec un aperçu en direct du « vous termineriez vers… »."),
        ("Lisez la portion du jour",
         "Chaque chapitre est à une pression, et s'ouvre directement dans JW Library ou dans "
         "la BIBLIOTHÈQUE EN LIGNE Watchtower, dans votre langue. Cochez les chapitres au fur "
         "et à mesure."),
        ("Emmenez vos notes avec vous (facultatif)",
         "Chargez une sauvegarde dans n'importe quel outil JW Sync et vos propres notes et le "
         "nombre de surlignages apparaissent juste sous les chapitres du jour."),
        ("Regardez la progression se construire",
         "Une grille des 66 livres se remplit au fil de la lecture, avec une barre de "
         "chapitres lus, une prévision de rythme et des jalons pour la fin de chaque livre, "
         "des Écritures hébraïques et araméennes, des Écritures grecques — et de toute la "
         "Bible."),
    ],
    "sections": [
        ("Des séries sans culpabilité",
         "Terminer une journée fait grandir votre série ; en manquer une décale simplement la "
         "date de fin prévue. Il n'y a pas de pile de retard — le plan s'adapte à votre vie "
         "au lieu de vous faire la morale."),
    ],
    "faq": [
        ("Dois-je charger une sauvegarde pour l'utiliser ?",
         "Non — le plan, les séries et la progression fonctionnent tout seuls. La sauvegarde "
         "ne fait qu'ajouter vos notes personnelles à la lecture de chaque jour."),
        ("Ma progression de lecture est-elle privée ?",
         "Oui. La progression vit dans votre navigateur, sur votre appareil — il n'y a pas de "
         "compte et rien n'est envoyé."),
    ],
}

GUIDES_FR["open-jwlibrary-file"] = {
    "title": "Qu'est-ce qu'un fichier .jwlibrary et comment l'ouvrir ?",
    "h1": "Qu'est-ce qu'un fichier .jwlibrary — et comment en ouvrir un sur n'importe quel appareil",
    "description": "Un fichier .jwlibrary, c'est votre sauvegarde JW Library : un seul fichier "
                   "contenant chaque note, surlignage, signet et étiquette. Voici ce qu'il "
                   "contient et comment l'ouvrir et le lire.",
    "intro": [
        "Un fichier .jwlibrary paraît opaque, et il ne l'est pas. C'est une archive ZIP ordinaire autour d'une base de données SQLite ordinaire, ce qui signifie que vous pouvez lire votre propre sauvegarde — voir exactement quelles notes, quels surlignages et quels signets elle contient — sans JW Library et sans rien installer du tout.",
        "Quand vous sauvegardez JW Library, vous obtenez un fichier se terminant par "
        ".jwlibrary. C'est un paquet unique et portable qui contient tout votre étude "
        "personnelle — notes, surlignages, signets, étiquettes et listes de lecture — dans une "
        "base de données compacte. Ce n'est pas un document qu'on ouvre dans Word ou un "
        "lecteur de PDF ; il est conçu pour être restauré dans JW Library.",
        "Mais vous n'avez pas besoin de le restaurer juste pour regarder à l'intérieur. JW "
        "Sync ouvre un fichier .jwlibrary directement dans votre navigateur, pour que vous "
        "puissiez lire, chercher et modifier son contenu sans toucher à votre téléphone.",
    ],
    "steps": [
        ("Procurez-vous un fichier .jwlibrary",
         "Il se crée dans JW Library : Étude personnelle → menu à trois points → Sauvegarde et "
         "restauration → Créer une sauvegarde. C'est de ce fichier qu'il s'agit."),
        ("Ouvrez-le dans JW Sync",
         "Rendez-vous sur jwsync.org et chargez le fichier dans l'Explorateur d'étude. Il "
         "s'ouvre instantanément, sur votre appareil — rien n'est envoyé."),
        ("Lisez-le et travaillez avec",
         "Parcourez notes, surlignages et signets ; cherchez dans l'ensemble ; modifiez, "
         "réétiquetez ou exportez. Une fois terminé, vous pouvez restaurer le fichier (ou une "
         "copie modifiée) dans JW Library."),
    ],
    "sections": [
        ("Ce qu'il y a réellement dans le fichier",
         "Techniquement, un fichier .jwlibrary est une base de données SQLite compressée, plus "
         "un manifeste. C'est pourquoi il arrive qu'il soit renommé en .zip par accident en "
         "route — et pourquoi le renommer en .jwlibrary règle le problème. Vous n'avez jamais "
         "besoin de savoir tout cela pour l'utiliser, mais cela explique pourquoi le fichier "
         "est petit, autonome et identique sur Android, iPhone, iPad et Windows."),
        ("L'ouvrir sur un ordinateur",
         "La même page jwsync.org fonctionne dans le navigateur d'un portable ou d'un fixe — "
         "pratique pour lire des années de notes sur grand écran, ou faire un nettoyage en "
         "lot qui serait fastidieux sur un téléphone. Rien à installer."),
        ("Ce qu'est réellement le fichier",
         "Un fichier .jwlibrary est une archive ZIP portant une autre extension. À l'intérieur se trouvent userData.db — une base SQLite contenant vos notes, surlignages, signets et étiquettes — et manifest.json, un petit fichier décrivant la sauvegarde et comportant une empreinte de la base que JW Library utilise pour confirmer que le fichier n'a pas été modifié. Rien n'y est propriétaire ni chiffré : c'est une archive standard autour d'une base de données standard."),
        ("L'ouvrir sans JW Library",
         "Vous n'avez besoin ni de l'application ni d'aucun logiciel pour lire votre propre sauvegarde. Ouvrir le fichier dans votre navigateur affiche toutes les notes, tous les surlignages et tous les signets qu'il contient, avec recherche et filtres, et le fichier ne quitte jamais votre appareil : il est lu localement, non téléversé. C'est le moyen le plus rapide de confirmer qu'une sauvegarde contient bien ce que vous croyez avant une réinitialisation, une reprise ou une restauration sur un nouveau téléphone."),
        ("Regarder à l'intérieur manuellement",
         "Si la curiosité vous prend, copiez le fichier, renommez la copie en .zip et ouvrez-la avec n'importe quel outil d'archivage. Vous verrez userData.db et manifest.json. Ouvrir la base demande un visualiseur SQLite, et les tables portent le nom de ce qu'elles contiennent : Note, UserMark, Bookmark, Tag. Travaillez toujours sur une copie : modifier la base à la main sans mettre à jour l'empreinte du manifeste produit un fichier que JW Library refusera de restaurer."),
        ("Modifier sans risque",
         "Les notes peuvent être corrigées, réétiquetées, recolorées ou supprimées hors de l'application, et le résultat exporté comme un nouveau fichier .jwlibrary que vous restaurez normalement. La règle qui rend cela sûr est de conserver l'original : modifiez une copie, restaurez le fichier modifié, et si quelque chose ne correspond pas à vos attentes, l'original intact est toujours là pour revenir en arrière."),
        ("Lire une sauvegarde sur un téléphone",
         "Aucun ordinateur n'est nécessaire. Ouvrir le fichier dans un navigateur mobile fonctionne de la même façon, ce qui est utile quand la sauvegarde est déjà sur le téléphone et que vous voulez en vérifier le contenu avant de restaurer ou d'effacer l'appareil. Le fichier est lu localement : cela fonctionne sans autre connexion que celle du chargement de la page."),
        ("Pourquoi l'empreinte du manifeste compte",
         "manifest.json enregistre une empreinte de userData.db. JW Library s'en sert pour confirmer que la base n'a pas été modifiée depuis l'écriture de la sauvegarde : un fichier dont la base a été modifiée sans recalcul de l'empreinte est refusé à la restauration. C'est la raison la plus fréquente pour laquelle une sauvegarde modifiée à la main cesse de fonctionner, et pourquoi passer par un outil qui réécrit le manifeste est plus sûr que de toucher directement à la base."),
        ("À quoi cela sert",
         "Pouvoir lire une sauvegarde change ce qu'une sauvegarde vaut. Vous pouvez confirmer qu'un fichier contient bien ce que vous croyez avant d'effacer un téléphone, vérifier si un ancien fichier mérite d'être restauré, retrouver une note que vous savez avoir écrite sans fouiller l'application, ou récupérer du texte dans un fichier que JW Library refuse. Rien de tout cela n'exige de confier le fichier à qui que ce soit : il est lu sur votre propre appareil."),
    ],
    "faq": [
        ("Puis-je ouvrir un fichier .jwlibrary dans Excel ou le Bloc-notes ?",
         "Pas utilement — c'est une base de données, pas un tableur ni un fichier texte. "
         "Ouvrez-le dans JW Sync pour le lire, ou exportez vos notes en Markdown/texte depuis "
         "l'Explorateur d'étude."),
        ("Est-il sûr d'ouvrir ma sauvegarde dans le navigateur ?",
         "Oui. JW Sync lit le fichier localement, dans l'onglet de votre navigateur ; rien "
         "n'est envoyé à un serveur, et votre fichier d'origine n'est jamais modifié."),
        ("Puis-je simplement le renommer en .zip ?",
         "Oui, sur une copie. Le renommer ne modifie pas le contenu et permet à n'importe quel outil d'archivage de vous montrer ce qu'il y a dedans."),
        ("Ouvrir le fichier le modifie-t-il ?",
         "Non. Lire une sauvegarde — dans le navigateur ou un outil d'archivage — la laisse identique octet pour octet. Seul un enregistrement ou une exportation produit un nouveau fichier."),
        ("Dois-je être en ligne ?",
         "Uniquement pour charger la page. Le fichier est lu sur votre appareil et non téléversé : vos notes ne circulent jamais sur le réseau."),
        ("Puis-je ouvrir une sauvegarde envoyée par quelqu'un d'autre ?",
         "Oui, le format n'est lié ni à un appareil ni à un compte. Savoir s'il faut la restaurer est une autre question, puisqu'une restauration remplace votre propre bibliothèque."),
        ("Dois-je installer quelque chose pour regarder à l'intérieur ?",
         "Non. Un navigateur suffit pour lire les notes ; seule l'inspection manuelle de la base demande un visualiseur SQLite."),
    ],
}

GUIDES_FR["jw-library-windows-pc"] = {
    "title": "Sauvegarder et fusionner JW Library sur un PC Windows",
    "h1": "Utiliser les sauvegardes JW Library sur un PC Windows",
    "description": "Comment sauvegarder JW Library sous Windows, et comment fusionner la "
                   "sauvegarde du PC avec celles du téléphone et de la tablette pour que "
                   "notes, surlignages et signets restent ensemble sur chaque appareil.",
    "intro": [
        "JW Library fonctionne sous Windows comme sur téléphone et tablette, et produit le "
        "même fichier de sauvegarde .jwlibrary. Votre PC peut donc faire partie de la même "
        "bibliothèque d'étude que votre téléphone — à condition de fusionner les sauvegardes "
        "plutôt que d'en restaurer une par-dessus l'autre.",
    ],
    "steps": [
        ("Sauvegardez sous Windows",
         "Dans l'application JW Library pour Windows, ouvrez le menu, allez dans Sauvegarde et "
         "restauration et créez une sauvegarde. Enregistrez le fichier .jwlibrary dans un "
         "endroit facile à retrouver."),
        ("Sauvegardez aussi votre téléphone et votre tablette",
         "Sur chaque appareil : Étude personnelle → menu à trois points → Sauvegarde et "
         "restauration → Créer une sauvegarde."),
        ("Fusionnez-les sur jwsync.org",
         "Ouvrez jwsync.org dans n'importe quel navigateur du PC et chargez tous les fichiers "
         "de sauvegarde. JW Sync réunit les notes, surlignages, signets et étiquettes de "
         "chaque appareil dans un seul fichier .jwlibrary fusionné — localement, sans rien "
         "envoyer."),
        ("Restaurez le fichier fusionné partout",
         "Restaurez le fichier fusionné dans l'application Windows et sur chaque appareil "
         "mobile. Le PC, le téléphone et la tablette portent maintenant tous la bibliothèque "
         "complète."),
    ],
    "sections": [
        ("Pourquoi le PC est l'endroit le plus commode",
         "Un navigateur de bureau rend le chargement de plusieurs fichiers, l'examen de "
         "l'aperçu de fusion et l'enregistrement du résultat bien plus rapides que des "
         "manipulations sur un téléphone. Beaucoup gardent leur routine de fusion principale "
         "sur l'ordinateur et se contentent de restaurer le fichier fusionné sur leurs "
         "appareils mobiles."),
    ],
    "faq": [
        ("La sauvegarde Windows fonctionne-t-elle avec celles d'iPhone et d'Android ?",
         "Oui — le format .jwlibrary est identique sur toutes les plateformes, donc une "
         "sauvegarde Windows fusionne librement avec celles du téléphone et de la tablette."),
        ("Dois-je installer quelque chose sur le PC ?",
         "Non. JW Sync est une page web ; elle fonctionne dans Edge, Chrome ou Firefox, sans "
         "rien à installer."),
    ],
}

GUIDES_FR["recover-jw-library-notes-lost-phone"] = {
    "title": "Comment récupérer ses notes JW Library après un téléphone perdu ou cassé",
    "h1": "Récupérer ses notes JW Library depuis un téléphone perdu, cassé ou réinitialisé",
    "description": "Téléphone perdu ou réinitialisé avec vos notes JW Library dessus ? Ce que "
                   "vous pouvez récupérer dépend de vos sauvegardes. Voici exactement comment "
                   "retrouver vos notes — et quoi faire la prochaine fois.",
    "intro": [
        "D'abord la réponse honnête, elle vous évitera de lire plus loin. S'il existe une sauvegarde .jwlibrary quelque part en dehors de l'appareil perdu, tout ce qu'elle contient revient par la restauration de JW Library elle-même, et pour cette partie vous n'avez pas besoin de ce site. S'il n'en existe aucune, les données d'étude personnelle ne peuvent pas être récupérées du tout : elles ne vivent que sur l'appareil, et aucun outil n'y change rien.",
        "Là où cette page aide vraiment, c'est le cas intermédiaire, plus fréquent que les deux autres : vous avez une sauvegarde, mais elle ne dit pas tout. Elle peut dater de plusieurs mois, ou vous avez peut-être déjà étudié sur le téléphone de remplacement — la restaurer telle quelle échangerait alors un ensemble de notes contre un autre au lieu de tout vous rendre.",
        "Réunir les deux est précisément ce que JW Library ne sait pas faire, et c'est l'objet du reste de cette page. Mais d'abord, la recherche : on a régulièrement plus de sauvegardes qu'on ne se souvient en avoir fait.",
    ],
    "steps": [
        ("Cherchez partout où une sauvegarde pourrait se trouver",
         "Vérifiez vos e-mails (cherchez « jwlibrary » ou « sauvegarde »), Google Drive, "
         "iCloud Drive, OneDrive, Dropbox et le dossier Téléchargements de votre ordinateur. "
         "Les sauvegardes sont de petits fichiers qu'on oublie facilement avoir enregistrés."),
        ("Vérifiez vos autres appareils",
         "Si vous avez déjà utilisé JW Library sur une tablette ou un PC, il possède ses "
         "propres données d'étude — créez-en une sauvegarde dès maintenant pour préserver ce "
         "qu'il contient."),
        ("Restaurez ce que vous trouvez sur le nouveau téléphone",
         "Installez JW Library sur le nouvel appareil, puis Sauvegarde et restauration → "
         "Restaurer, et chargez le fichier .jwlibrary. Vos notes, surlignages et signets "
         "reviennent."),
        ("Fusionnez si vous trouvez plusieurs sauvegardes",
         "Des appareils ou des dates différents peuvent contenir chacun des notes uniques. "
         "N'en choisissez pas une seule — chargez-les toutes sur jwsync.org, fusionnez-les en "
         "un seul fichier complet, et restaurez celui-là. Rien n'est laissé de côté."),
    ],
    "sections": [
        ("S'il n'existe aucune sauvegarde nulle part",
         "Soyez honnête avec vous-même dès le début : si la seule copie de vos notes vivait "
         "sur le téléphone perdu et que vous n'avez jamais exporté de sauvegarde, JW Library "
         "ne garde aucune copie dans le cloud pour restaurer. C'est douloureux — et c'est "
         "précisément pourquoi l'habitude ci-dessous compte tant."),
        ("Pour ne plus jamais en arriver là",
         "Programmez un rappel mensuel de sauvegarde et rangez chaque fichier .jwlibrary "
         "ailleurs que sur le téléphone (vous l'envoyer par e-mail suffit). JW Sync peut même "
         "vous le rappeler et fusionner vos appareils à intervalle régulier. Un fichier qui "
         "vit dans votre boîte de réception survit à n'importe quel téléphone."),
        ("Où une sauvegarde peut déjà exister",
         "Avant de conclure qu'il n'y en a aucune, vérifiez partout où un fichier a pu être enregistré : les dossiers Téléchargements et Documents de tout ordinateur auquel vous avez connecté le téléphone, les éléments envoyés de votre messagerie, les applications de messagerie par lesquelles vous avez pu l'envoyer, et chaque compte infonuagique que vous utilisez. Beaucoup ont créé une sauvegarde une fois, il y a des mois, et l'ont oubliée — et une sauvegarde vieille de plusieurs mois contient encore la grande majorité d'une bibliothèque d'étude."),
        ("Restaurer sur un autre téléphone ou une autre plateforme",
         "L'appareil de remplacement n'a pas besoin de correspondre à celui qui est perdu. Une sauvegarde d'un téléphone Android se restaure sur un iPhone et inversement, le format étant identique sous Android, iOS, iPadOS et Windows. Installez JW Library sur le nouvel appareil, mettez-le à jour vers la version actuelle, puis restaurez via Étude personnelle → Sauvegarde et restauration."),
        ("Si vous n'avez qu'une sauvegarde ancienne ou partielle",
         "Restaurez-la quand même. Récupérer l'essentiel de vos notes n'est pas un lot de consolation : c'est le résultat. Si vous trouvez plus tard une seconde sauvegarde différente, les deux peuvent être fusionnées en un fichier contenant tout des deux : restaurer la plus ancienne maintenant ne vous empêche pas d'y ajouter ensuite."),
        ("Ce qui ne peut pas être récupéré",
         "S'il n'existe aucune sauvegarde sous quelque forme que ce soit, les données d'étude personnelle ne peuvent pas être récupérées. Elles ne sont stockées que dans le stockage privé de l'application, sur l'appareil, et ni JW Library ni une sauvegarde infonuagique au niveau du téléphone ne les préservent de façon fiable. Cela mérite d'être dit clairement, car c'est la raison d'être de la routine présentée sur ce site."),
        ("Vérifiez avant d'effacer l'appareil à distance",
         "Si le téléphone est perdu plutôt que détruit et que vous envisagez un effacement à distance, cherchez d'abord les sauvegardes existantes : l'effacement est irréversible et supprime la dernière chance d'en créer une. Si l'appareil est simplement égaré et toujours joignable, créer une sauvegarde à distance est impossible, mais les données restent intactes tant qu'il n'est ni effacé ni réinitialisé."),
        ("Faire en sorte que cela n'arrive pas deux fois",
         "Si un téléphone perdu coûte des années d'étude, c'est que la seule copie était sur le téléphone. Une fois la restauration faite sur un appareil de remplacement, placez le jour même une sauvegarde hors de l'appareil, et répétez à un rythme que vous tiendrez réellement. Les fichiers sont assez petits pour être tous conservés indéfiniment sans coût."),
        ("S'il n'y a vraiment aucune sauvegarde",
         "Alors la réponse honnête est que les notes ne peuvent pas être récupérées, et il vaut mieux l'entendre que continuer à chercher. Ce que vous pouvez faire, c'est que cette perte soit la dernière : installez JW Library sur le remplaçant et, avant d'avoir reconstitué quoi que ce soit qui mérite d'être perdu, créez une sauvegarde et placez-la hors de l'appareil. À partir de là, le même événement ne vous coûte rien."),
    ],
    "faq": [
        ("JW Sync peut-il récupérer des notes d'un téléphone que je n'ai plus ?",
         "Aucun outil ne le peut — la récupération dépend de l'existence d'un fichier de "
         "sauvegarde quelque part. Le rôle de JW Sync est de lire, réparer et fusionner les "
         "sauvegardes que vous avez."),
        ("Ma sauvegarde est ancienne — vaut-elle encore la peine d'être restaurée ?",
         "Absolument. Une vieille sauvegarde contenant l'essentiel de vos notes vaut mieux que "
         "repartir de zéro, et vous pourrez la fusionner plus tard avec tout ce que vous "
         "trouverez de plus récent."),
        ("JW Library conserve-t-il une copie de mes notes dans le nuage ?",
         "Non. Les données d'étude personnelle restent sur l'appareil, sauf si vous créez vous-même un fichier de sauvegarde."),
        ("Peut-on récupérer des notes sur un téléphone à l'écran cassé ?",
         "Parfois : si le téléphone s'allume encore et peut être piloté, ou si un réparateur peut faire fonctionner l'affichage, JW Library peut toujours créer une sauvegarde. Les données sont intactes tant que le stockage l'est."),
        ("Une ancienne sauvegarde se restaure-t-elle encore dans l'application actuelle ?",
         "Oui. JW Library lit les formats de sauvegarde antérieurs. Mettez d'abord l'application à jour et restaurez dans la version actuelle."),
        ("J'ai trouvé deux anciennes sauvegardes — laquelle utiliser ?",
         "Aucune séparément : fusionnez-les. Le résultat contient tout des deux, y compris ce qui figurait dans la plus ancienne et avait été supprimé à la date de la plus récente."),
        ("Puis-je voir ce que contient une sauvegarde avant de la restaurer ?",
         "Oui. Ouvrez le fichier dans votre navigateur et parcourez d'abord ses notes, surlignages et signets, pour savoir ce que vous restaurez."),
    ],
}

GUIDES_FR["handle-merge-conflicts"] = {
    "title": "La même note modifiée sur deux appareils ? Gérer les conflits de fusion",
    "h1": "Gérer les conflits de fusion : la même note modifiée sur deux appareils",
    "description": "Quand vous modifiez la même note JW Library différemment sur deux "
                   "appareils, la fusion doit trancher. Le Comparateur de conflits affiche les "
                   "deux versions côte à côte pour que vous décidiez — rien n'est perdu.",
    "intro": [
        "L'essentiel de la fusion se fait tout seul : les notes propres à chaque appareil se "
        "combinent simplement. Le seul cas qui exige une décision est un vrai conflit : la "
        "même note, modifiée différemment sur deux appareils, si bien que les deux "
        "sauvegardes ne s'accordent pas sur son contenu. JW Sync ne devine jamais en "
        "silence ; il vous laisse le choix.",
    ],
    "steps": [
        ("Chargez les deux sauvegardes",
         "Sur jwsync.org, chargez les fichiers .jwlibrary des deux appareils. JW Sync les "
         "compare pendant la fusion."),
        ("Ouvrez le Comparateur de conflits",
         "Si des notes entrent en conflit, le comparateur les liste. Tout ce qui n'était pas "
         "en conflit est déjà fusionné — cette étape ne concerne que les vrais désaccords."),
        ("Comparez côte à côte",
         "Chaque conflit montre les deux versions, avec les écarts surlignés mot à mot. "
         "« Suggérer la meilleure » peut choisir la version la plus complète pour vous, ou "
         "vous choisissez celle à garder — note par note."),
        ("Terminez et restaurez",
         "Une fois tous les conflits réglés, téléchargez le fichier fusionné et restaurez-le. "
         "Les deux appareils s'accordent désormais, avec la version que vous avez choisie pour "
         "chaque note."),
    ],
    "sections": [
        ("Pourquoi c'est mieux que simplement garder la plus récente",
         "« La plus récente gagne » supprime en silence des modifications que vous vouliez "
         "peut-être garder. Peut-être que l'ancienne version contenait un paragraphe supprimé "
         "par erreur sur l'autre appareil. Voir les deux, mot à mot, garantit que vous ne "
         "perdez jamais de texte sans le savoir — c'est tout l'intérêt de fusionner plutôt que "
         "d'écraser."),
        ("D'où viennent les conflits, au départ",
         "Généralement de modifications hors ligne sur deux appareils entre deux fusions, ou "
         "de la restauration d'une vieille sauvegarde suivie d'ajouts. Fusionner à intervalle "
         "régulier maintient le nombre de conflits faible et les différences fraîches dans "
         "votre mémoire."),
    ],
    "faq": [
        ("Vais-je devoir examiner des centaines de conflits ?",
         "Rarement. Seules les notes modifiées différemment des deux côtés entrent en "
         "conflit ; les nouvelles notes, et celles changées sur un seul appareil, fusionnent "
         "automatiquement. La plupart des fusions comptent une poignée de conflits, voire "
         "aucun."),
        ("Puis-je changer d'avis après avoir choisi ?",
         "Oui — rien n'est écrit sur un appareil tant que vous n'avez pas restauré le fichier "
         "fusionné, et vos sauvegardes d'origine ne sont jamais modifiées : vous pouvez "
         "refaire la fusion."),
    ],
}

GUIDES_FR["export-jw-library-notes"] = {
    "title": "Comment exporter ses notes JW Library en texte ou en Markdown",
    "h1": "Exporter vos notes JW Library en texte, en Markdown ou vers une nouvelle sauvegarde",
    "description": "Sortez vos notes JW Library de l'application : copiez-les ou exportez-les "
                   "en Markdown/texte brut pour les utiliser partout, ou extrayez une "
                   "sélection vers une nouvelle sauvegarde .jwlibrary. Le tout dans votre "
                   "navigateur.",
    "intro": [
        "Les notes écrites dans JW Library sont faciles à lire dans l'application et malcommodes à utiliser ailleurs : dans un document, dans un plan de discours, sur papier, ou entre les mains de quelqu'un qui n'utilise pas l'application. L'exportation règle cela, et la décision principale n'est pas comment exporter mais combien : une exportation filtrée est presque toujours plus utile que tout d'un coup.",
        "Vos notes d'étude ne devraient pas rester prisonnières d'une seule application. "
        "Parfois vous les voulez en texte brut — pour les coller dans un plan de discours, un "
        "document ou votre propre application de notes — et parfois vous voulez une sauvegarde "
        "propre ne contenant qu'une partie. L'Explorateur d'étude fait les deux, en lisant "
        "votre sauvegarde entièrement dans le navigateur.",
    ],
    "steps": [
        ("Chargez votre sauvegarde",
         "Créez une sauvegarde dans JW Library (Étude personnelle → Sauvegarde et restauration "
         "→ Créer une sauvegarde), puis ouvrez jwsync.org et chargez-la dans l'Explorateur "
         "d'étude."),
        ("Trouvez les notes voulues",
         "Utilisez la recherche et les filtres par couleur, étiquette et publication pour "
         "cerner exactement les notes cherchées — une publication, une étiquette, un sujet."),
        ("Copiez ou exportez en Markdown/texte",
         "Sortez les notes en Markdown ou en texte brut pour les coller n'importe où. La mise "
         "en forme (gras, italique, listes) est conservée : les notes structurées restent "
         "structurées."),
        ("Ou extrayez vers une nouvelle sauvegarde",
         "Vous préférez un fichier ? Exportez une sélection ou une plage de dates vers une "
         "nouvelle sauvegarde .jwlibrary — pratique pour archiver un projet ou transmettre un "
         "ensemble précis de notes à un autre appareil."),
    ],
    "sections": [
        ("Pourquoi exporter",
         "Les notes sont plus utiles quand elles peuvent voyager : vers un document pour une "
         "partie à la réunion, vers un wiki personnel, vers une impression destinée à "
         "quelqu'un qui n'utilise pas l'application. Le Markdown préserve la structure tout en "
         "restant lisible comme du texte brut, partout."),
        ("Choisir un format",
         "Le texte brut est le plus portable et se colle proprement dans n'importe quel document ou courriel. La sortie mise en forme préserve la structure des notes longues et convient à l'impression ou au partage. Si vous voulez récupérer les notes dans JW Library plus tard — sur un autre appareil, ou dans la bibliothèque de quelqu'un d'autre — conservez le fichier .jwlibrary lui-même plutôt qu'une exportation texte, car lui seul préserve les liens entre notes, surlignages, étiquettes et l'endroit exact de la publication où ils sont ancrés."),
        ("N'exporter qu'une partie de votre bibliothèque",
         "Une exportation complète représentant des années d'étude est rarement ce que l'on veut. Restreindre d'abord — à une étiquette, une publication, une couleur de surlignage ou une plage de dates — produit quelque chose d'utilisable, comme toutes les notes étiquetées pour un discours, ou tout ce qui a été écrit pendant un congrès. Les filtres qui restreignent l'affichage restreignent l'exportation : ce que vous voyez est ce que vous obtenez."),
        ("Ce qui voyage avec le texte, et ce qui ne voyage pas",
         "Une exportation emporte vos mots. Elle n'emporte pas les ancres qui relient une note à un paragraphe précis d'une publication précise, car ces références n'ont de sens que dans JW Library. C'est la raison pratique de conserver aussi des sauvegardes : une exportation sert à lire, imprimer et partager hors de l'application, tandis qu'un fichier .jwlibrary est ce qui replace les notes dans une bibliothèque avec leur contexte intact."),
        ("Rassembler tout pour un discours ou une tâche",
         "C'est la raison la plus courante d'exporter. Filtrez sur l'étiquette, la publication ou la plage de dates concernée, vérifiez le résultat et n'exportez que cela. Vous obtenez un document unique contenant les notes pertinentes et les passages surlignés, dans l'ordre où ils apparaissent, plutôt qu'un déversement ingérable de toute votre bibliothèque."),
        ("Partager des notes avec quelqu'un",
         "Deux choses différentes se cachent derrière le partage. Si l'autre personne veut lire vos notes, l'exportation texte convient : elle s'ouvre partout et ne demande aucun logiciel particulier. Si elle veut les notes dans sa propre bibliothèque JW Library, ancrées aux mêmes paragraphes et portant ses étiquettes et couleurs, alors c'est un fichier .jwlibrary qu'il vous faut, car une exportation texte ne peut rien replacer dans l'application."),
        ("Conserver une archive encore lisible dans longtemps",
         "Les exportations valent aussi pour elles-mêmes. Une copie en texte brut de vos notes d'étude s'ouvrira encore dans trente ans avec des logiciels que personne n'a écrits, ce qu'aucun format propre à une application ne peut promettre. Conserver les deux — le .jwlibrary pour restaurer et une exportation texte pour lire — ne coûte presque rien et couvre les deux avenirs."),
        ("Exportation ou sauvegarde : ce dont vous avez besoin",
         "Les deux répondent à des questions différentes. Une exportation sert à utiliser vos notes hors de JW Library : lire, imprimer, citer, envoyer à quelqu'un. Une sauvegarde .jwlibrary sert à les remettre dans JW Library, sur cet appareil ou un autre, avec chaque ancre, étiquette et couleur intactes. Aucune ne remplace l'autre, et rien n'empêche d'avoir les deux."),
    ],
    "faq": [
        ("Exporter modifie-t-il mes notes JW Library ?",
         "Non. L'export lit une copie de votre sauvegarde dans le navigateur ; votre fichier "
         "d'origine et votre application ne sont pas touchés."),
        ("Puis-je tout exporter d'un coup ?",
         "Oui — effacez les filtres pour sélectionner toute votre bibliothèque, ou restreignez "
         "d'abord pour n'en exporter qu'une partie."),
        ("Puis-je récupérer mes notes dans Word ou Google Docs ?",
         "Oui : exportez en texte et collez. Le texte arrive avec sa structure intacte et peut être mis en forme ensuite."),
        ("Les surlignages sont-ils exportés en plus des notes ?",
         "Oui, y compris le passage surligné et sa couleur, si bien qu'une copie imprimée montre à la fois ce que vous avez marqué et ce que vous avez écrit."),
        ("Puis-je tout exporter d'un coup ?",
         "Oui, même si une exportation filtrée est généralement plus utile. Tout peut être exporté en une passe quand vous voulez une copie complète."),
        ("Puis-je exporter les réponses saisies dans les questions d'étude ?",
         "Oui. Les réponses saisies font partie de vos données d'étude personnelle et s'exportent avec les notes et les surlignages."),
        ("L'exportation indique-t-elle à quelle publication appartient chaque note ?",
         "Oui, l'exportation identifie l'origine de chaque note, même si l'ancre sous-jacente ne fonctionne que dans JW Library."),
        ("Exporter change-t-il quelque chose dans ma bibliothèque ?",
         "Non. Une exportation lit vos données et écrit un fichier distinct ; rien dans JW Library n'est modifié, déplacé ni supprimé."),
        ("Puis-je exporter depuis une sauvegarde plutôt que depuis l'application ?",
         "Oui. Un fichier .jwlibrary peut être ouvert directement et ses notes exportées, ce qui est utile quand les notes voulues sont dans une ancienne sauvegarde et non sur votre appareil actuel."),
    ],
}

GUIDES_FR["organize-jw-library-tags"] = {
    "title": "Comment organiser et nettoyer ses étiquettes JW Library",
    "h1": "Organiser vos étiquettes JW Library : renommer, fusionner et nettoyer en lot",
    "description": "Les étiquettes se multiplient au fil des années d'étude. Renommez une "
                   "étiquette sur toutes les notes, fusionnez les doublons et supprimez celles "
                   "dont vous ne vous servez plus — en lot, dans votre navigateur, avec "
                   "annulation complète.",
    "intro": [
        "Les étiquettes, c'est ce qui vous permet de retrouver vos notes plus tard — mais après "
        "quelques années, elles prolifèrent. Vous vous retrouvez avec « Ministère », "
        "« ministère » et « Service du champ » qui veulent dire la même chose, des étiquettes "
        "créées une fois et jamais réutilisées, et un nommage incohérent qui rend le filtrage "
        "peu fiable. JW Library n'offre aucun moyen de corriger cela à grande échelle. "
        "L'Explorateur d'étude, si.",
    ],
    "steps": [
        ("Chargez votre sauvegarde dans l'Explorateur d'étude",
         "Sur jwsync.org, chargez votre fichier .jwlibrary. Filtrez par étiquette pour voir "
         "chaque étiquette et le nombre de notes qui la portent."),
        ("Renommez une étiquette sur toutes ses notes",
         "Réétiquetez en lot : renommez une étiquette une fois et toutes les notes qui "
         "l'utilisent se mettent à jour — fini la correction d'orthographe note par note."),
        ("Fusionnez les doublons",
         "Réétiquetez les notes d'une étiquette en double vers l'étiquette de référence, puis "
         "supprimez le doublon devenu vide. « Ministère » et « ministère » ne font plus qu'une "
         "étiquette propre."),
        ("Supprimez les étiquettes inutilisées",
         "Sélectionnez et supprimez en lot les étiquettes périmées. Tout est annulable, un "
         "nettoyage un peu trop zélé n'est donc jamais définitif."),
        ("Exportez la bibliothèque rangée",
         "Téléchargez le .jwlibrary modifié et restaurez-le dans JW Library. Vos étiquettes "
         "sont cohérentes partout."),
    ],
    "sections": [
        ("Un système d'étiquettes qui aide vraiment",
         "Une fois les étiquettes cohérentes, le filtrage devient fiable — une pression "
         "affiche toutes les notes sur un thème, dans toutes les publications. C'est la "
         "différence entre des étiquettes qui encombrent et des étiquettes qui forment un "
         "véritable index de votre étude."),
        ("Des étiquettes cohérentes rendent le partage instantané",
         "Le sélecteur de notes de la page de partage a son propre filtre par étiquette : une "
         "étiquette propre est donc aussi le moyen le plus rapide d'envoyer un ensemble de "
         "notes à quelqu'un — choisissez l'étiquette, cliquez sur Tout sélectionner, créez le "
         "fichier. Des étiquettes négligées coûtent deux fois : quand vous cherchez des notes, "
         "et quand vous essayez de les partager."),
    ],
    "faq": [
        ("Le réétiquetage en lot touche-t-il au texte des notes ?",
         "Non — il ne change que les étiquettes rattachées. Les titres et le contenu de vos "
         "notes restent exactement tels que vous les avez écrits."),
        ("Puis-je annuler en cas d'erreur ?",
         "Oui. L'Explorateur d'étude dispose d'une annulation et d'un rétablissement complets, "
         "et votre sauvegarde d'origine n'est jamais modifiée — les changements vont dans une "
         "copie exportée."),
    ],
}

GUIDES_FR["manage-jw-library-highlights"] = {
    "title": "Comment gérer et recolorer ses surlignages JW Library",
    "h1": "Gérer vos surlignages JW Library : recolorer et organiser en lot",
    "description": "Mettez de l'ordre dans des années de surlignages JW Library : changez les "
                   "couleurs en lot, donnez un sens cohérent à votre code couleur et "
                   "parcourez tous vos surlignages au même endroit. Dans votre navigateur.",
    "intro": [
        "Les couleurs de surlignage ne servent que si elles veulent dire quelque chose de "
        "cohérent. Avec le temps, les surlignages de la plupart des gens dérivent — le jaune "
        "voulait dire une chose en 2019 et autre chose aujourd'hui, et JW Library n'offre "
        "aucun moyen de tous les voir ensemble ou de les corriger à grande échelle. "
        "L'Explorateur d'étude rassemble chaque surlignage dans une seule vue et vous permet "
        "de recolorer en lot.",
    ],
    "steps": [
        ("Chargez votre sauvegarde",
         "Sur jwsync.org, ouvrez votre fichier .jwlibrary dans l'Explorateur d'étude et "
         "passez à l'onglet Surlignages."),
        ("Parcourez et filtrez vos surlignages",
         "Voyez tous vos surlignages dans une seule liste, filtrez par couleur ou par "
         "publication, et cherchez dans le texte surligné comme dans les notes rattachées."),
        ("Recolorez en lot",
         "Sélectionnez plusieurs surlignages et changez leur couleur d'un coup — par exemple "
         "pour unifier sous une seule couleur tout ce que vous entendiez par « verset clé » "
         "dans toute votre bibliothèque."),
        ("Modifiez aussi les notes rattachées",
         "Là où un surlignage porte une note, modifiez ici même le titre et le contenu de "
         "cette note."),
        ("Exportez et restaurez",
         "Téléchargez le .jwlibrary modifié et restaurez-le dans JW Library pour que votre "
         "code couleur cohérent soit sur tous vos appareils."),
    ],
    "sections": [
        ("Décidez du sens de vos couleurs",
         "Un schéma simple — une couleur pour les points principaux, une pour les versets à "
         "mémoriser, une pour les questions à approfondir — transforme les surlignages en "
         "outil d'étude plutôt qu'en décoration. Recolorer en lot vous permet d'appliquer ce "
         "schéma rétroactivement à des années de lecture."),
    ],
    "faq": [
        ("Puis-je voir les surlignages sans note rattachée ?",
         "Oui — l'onglet Surlignages les affiche tous, avec ou sans note liée."),
        ("Recolorer affecte-t-il le texte lui-même ?",
         "Non, cela ne change que la couleur du surlignage ; le texte de la publication et vos "
         "notes ne sont pas touchés."),
    ],
}

GUIDES_FR["jw-library-study-answers"] = {
    "title": "Consulter et modifier ses réponses d'étude JW Library",
    "h1": "Retrouver vos réponses d'étude JW Library au même endroit",
    "description": "Les réponses que vous saisissez aux questions des articles d'étude et des "
                   "cahiers sont cachées dans votre sauvegarde. L'onglet Réponses d'étude de "
                   "l'Explorateur d'étude vous permet de toutes les lire, chercher et "
                   "modifier d'un coup.",
    "intro": [
        "Pendant l'étude, vous tapez des réponses dans les cases des articles d'étude, de La "
        "Tour de Garde et des cahiers de réunion. Elles sont enregistrées dans votre "
        "sauvegarde — mais JW Library ne les montre qu'enfouies chacune dans sa publication. "
        "Il n'existe aucun endroit unique pour relire tout ce que vous avez écrit. L'onglet "
        "Réponses d'étude de l'Explorateur d'étude est cet endroit.",
    ],
    "steps": [
        ("Chargez votre sauvegarde dans l'Explorateur d'étude",
         "Sur jwsync.org, chargez votre fichier .jwlibrary et ouvrez l'onglet Réponses "
         "d'étude."),
        ("Lisez toutes vos réponses ensemble",
         "Chaque réponse que vous avez saisie apparaît dans une liste consultable : vous "
         "relisez d'un coup d'œil tout votre raisonnement sur un article d'étude entier."),
        ("Cherchez et modifiez",
         "Retrouvez une réponse par son texte, puis modifiez-la et affinez-la sur place — "
         "utile pour réviser avant une réunion ou reprendre une formulation faite à la hâte."),
        ("Exportez ou restaurez",
         "Restaurez le fichier modifié pour ramener vos changements dans JW Library, ou copiez "
         "vos réponses en texte pour un discours ou vos archives personnelles."),
    ],
    "sections": [
        ("Pourquoi c'est utile avant les réunions",
         "Relire vos réponses préparées dans une liste continue — plutôt que de faire défiler "
         "chaque paragraphe dans l'application — est un moyen plus rapide de vous remémorer ce "
         "que vous comptiez dire, et de repérer les réponses laissées en blanc."),
    ],
    "faq": [
        ("Est-ce la même chose que mes notes personnelles ?",
         "Non — les réponses d'étude sont ce que vous avez saisi dans les cases de réponse "
         "d'une publication. L'Explorateur d'étude les affiche dans un onglet à part, distinct "
         "des notes libres."),
        ("Quelque chose est-il envoyé pour lire mes réponses ?",
         "Non. Comme tout dans JW Sync, votre sauvegarde est lue localement dans le navigateur "
         "et n'est jamais envoyée nulle part."),
    ],
}

GUIDES_FR["extract-jw-library-notes-by-date"] = {
    "title": "Extraire les notes JW Library d'une période vers une nouvelle sauvegarde",
    "h1": "Extraire une période de notes JW Library vers une nouvelle sauvegarde",
    "description": "Isolez les notes d'une période précise — une année de service, un congrès, "
                   "un projet d'étude — dans leur propre sauvegarde .jwlibrary bien propre. "
                   "Entièrement dans votre navigateur.",
    "intro": [
        "Parfois vous voulez une tranche de votre bibliothèque, pas son intégralité : les "
        "notes de cette année pour une révision, tout ce qui vient d'un congrès, ou les "
        "recherches d'un projet à transmettre. L'Explorateur d'étude peut extraire les notes "
        "d'une période vers une sauvegarde .jwlibrary toute neuve, sans toucher à votre "
        "bibliothèque principale.",
    ],
    "steps": [
        ("Chargez votre sauvegarde",
         "Sur jwsync.org, ouvrez votre fichier .jwlibrary dans l'Explorateur d'étude."),
        ("Définissez la période",
         "Choisissez les dates de début et de fin des notes voulues — une année de service, un "
         "mois, les dates d'un événement précis."),
        ("Extrayez vers une nouvelle sauvegarde",
         "Exportez les notes correspondantes dans un nouveau fichier .jwlibrary. Il ne "
         "contient que les notes et surlignages de cette période, avec leurs étiquettes."),
        ("Utilisez le fichier extrait",
         "Restaurez-le dans JW Library pour une révision ciblée, archivez-le, ou partagez-le "
         "avec quelqu'un qui n'a besoin que de cette tranche."),
    ],
    "sections": [
        ("De bonnes raisons d'extraire par date",
         "Une archive annuelle de votre étude ; un fichier propre de notes de congrès gardé à "
         "part ; ne transmettre à un partenaire d'étude que les notes d'un projet mené "
         "ensemble ; ou découper une très grande bibliothèque en morceaux datés et gérables — "
         "sans jamais perturber votre sauvegarde principale."),
    ],
    "faq": [
        ("L'extraction retire-t-elle ces notes de ma bibliothèque ?",
         "Non. Elle copie les notes correspondantes dans un nouveau fichier ; votre sauvegarde "
         "d'origine conserve tout."),
        ("Quelle date utilise-t-elle — celle de rédaction ou de dernière modification ?",
         "Elle utilise les dates enregistrées dans la note elle-même : la période reflète donc "
         "le moment où les notes ont été créées ou modifiées."),
    ],
}

GUIDES_FR["connect-jw-library-notes-study-map"] = {
    "title": "Voyez comment vos notes JW Library se relient — la Carte d'étude",
    "h1": "Carte d'étude : un graphe de connaissances privé de vos notes JW Library",
    "description": "La Carte d'étude transforme vos notes JW Library en une toile interactive, "
                   "les reliant par versets partagés, étiquettes communes et formulations "
                   "proches — pour voir les thèmes qui traversent votre étude.",
    "intro": [
        "Des années de notes recèlent des liens que vous n'avez jamais vus : le même verset "
        "cité dans une douzaine d'entrées, un thème sur lequel vous revenez sans cesse, des "
        "idées qui se font écho dans des publications différentes. La Carte d'étude dessine "
        "ces liens sous forme de graphe interactif : la forme de votre propre étude devient "
        "visible.",
    ],
    "steps": [
        ("Ouvrez la page Statistiques d'étude et chargez une sauvegarde",
         "Rendez-vous sur jwsync.org/highlights.html et chargez votre fichier .jwlibrary. La "
         "Carte d'étude le lit dans votre navigateur."),
        ("Ouvrez la Carte d'étude",
         "Lancez la carte pour voir vos notes comme des points reliés par versets partagés, "
         "étiquettes communes et formulations proches."),
        ("Explorez les liens",
         "Basculez entre les vues Thèmes et Notes, survolez pour mettre en évidence les liens "
         "d'une note, déplacez les éléments, et utilisez le curseur de force pour n'afficher "
         "que les liens les plus étroits. Le mode plein écran vous donne de la place."),
        ("Construisez et enregistrez des chaînes d'étude",
         "Tracez vos propres « chaînes d'étude » manuelles entre notes apparentées pour "
         "capturer un raisonnement, et exportez la carte en image PNG pour la garder ou la "
         "partager."),
    ],
    "sections": [
        ("Ce que la carte révèle",
         "Les grappes montrent les thèmes que vous étudiez le plus ; un verset relié à de "
         "nombreuses notes signale un passage sur lequel vous revenez toujours ; une note "
         "isolée est peut-être un fil à développer. C'est une façon d'étudier votre étude — et "
         "de préparer des discours en suivant les liens que vous avez déjà tissés."),
    ],
    "faq": [
        ("Faut-il beaucoup de notes pour que la carte soit utile ?",
         "Une bibliothèque modeste montre déjà des liens ; plus vos notes sont riches, plus la "
         "carte révèle. Les très petites bibliothèques affichent un message invitant à ajouter "
         "d'abord des notes."),
        ("La carte est-elle privée ?",
         "Entièrement. Elle est construite dans votre navigateur à partir de votre sauvegarde "
         "et n'est jamais envoyée ; même l'export PNG est généré sur votre appareil."),
    ],
}

GUIDES_FR["review-old-jw-library-notes"] = {
    "title": "Comment réviser ses anciennes notes JW Library (pour qu'elles restent)",
    "h1": "Réviser ses anciennes notes JW Library avec Refaire surface — un peu, souvent",
    "description": "Les notes qu'on ne revoit jamais sont des notes qu'on oublie. Refaire "
                   "surface montre ce que vous avez écrit ce jour-là les années passées et "
                   "bâtit une révision espacée en douceur, pour que l'étude passée continue de "
                   "travailler pour vous.",
    "intro": [
        "La plupart des notes d'étude sont écrites une fois et jamais revues. C'est un "
        "gâchis silencieux — l'idée méritait d'être notée, puis elle a coulé au fond de la "
        "bibliothèque. Refaire surface ramène vos propres notes anciennes à la surface, "
        "quelques-unes à la fois, pour que les revoir devienne une petite habitude "
        "quotidienne au lieu d'un projet pour un jour.",
    ],
    "steps": [
        ("Ouvrez la page Statistiques d'étude et chargez une sauvegarde",
         "Rendez-vous sur jwsync.org/highlights.html et chargez votre fichier .jwlibrary. "
         "Refaire surface lit vos notes localement."),
        ("Découvrez « Ce jour-là »",
         "Refaire surface fait remonter les notes écrites à cette date les années "
         "précédentes — « écrite il y a deux ans, jour pour jour » — vous reliant à l'étude "
         "passée au moment où elle a le plus de sens."),
        ("Faites une courte révision quotidienne",
         "Il vous présente une poignée de notes à revoir et à marquer comme révisées. Un peu, "
         "souvent, c'est ainsi que l'étude s'ancre — et une série grandit tant que vous tenez "
         "l'habitude."),
        ("Revenez demain",
         "La répétition espacée programme le retour des notes dans le temps : celles qui "
         "méritent d'être retenues reviennent jusqu'à ce qu'elles soient vraiment vôtres."),
    ],
    "sections": [
        ("Pourquoi la répétition espacée fonctionne",
         "Revoir une chose juste au moment où l'on va l'oublier est bien plus efficace que de "
         "tout ingurgiter d'un coup. En répartissant quelques notes sur de nombreux jours, "
         "Refaire surface transforme votre bibliothèque existante en une révision continue et "
         "peu coûteuse, qui approfondit peu à peu ce que vous avez étudié."),
    ],
    "faq": [
        ("Où ma progression de révision est-elle enregistrée ?",
         "Dans votre navigateur, sur votre appareil — il n'y a pas de compte et rien n'est "
         "envoyé. La série et le calendrier n'appartiennent qu'à vous."),
        ("Ai-je besoin de nouvelles notes pour cela ?",
         "Non — Refaire surface travaille avec les notes que vous avez déjà écrites. Plus "
         "votre bibliothèque est ancienne, plus les moments « ce jour-là » sont savoureux."),
    ],
}

GUIDES_FR["jw-library-achievements-streaks"] = {
    "title": "Séries, niveaux et récompenses d'étude JW Library",
    "h1": "Transformez votre étude JW Library en séries, niveaux et récompenses",
    "description": "Voyez vos séries d'étude, gravissez 60 niveaux répartis en 12 paliers sur "
                   "votre Parcours d'étude et débloquez près de 200 récompenses — le tout lu "
                   "en privé depuis votre propre sauvegarde JW Library.",
    "intro": [
        "La régularité est la partie difficile de l'étude personnelle, et une progression "
        "qu'on ne voit pas est facile à laisser filer. La page Statistiques d'étude transforme "
        "l'histoire contenue dans votre sauvegarde en quelque chose que vous pouvez regarder "
        "grandir : des séries, des niveaux et des récompenses qui reflètent l'étude que vous "
        "avez réellement faite — aucun objectif imposé, juste votre propre parcours rendu "
        "visible.",
    ],
    "steps": [
        ("Ouvrez la page Statistiques d'étude",
         "Rendez-vous sur jwsync.org/highlights.html et chargez votre sauvegarde .jwlibrary. "
         "Tout est calculé dans votre navigateur."),
        ("Regardez vos séries",
         "Découvrez votre plus longue série d'étude et celle en cours, votre rythme "
         "hebdomadaire, vos heures et vos mois les plus chargés — le pouls de votre habitude "
         "d'étude."),
        ("Gravissez votre Parcours d'étude",
         "Progressez à travers 60 niveaux répartis en 12 paliers nommés (de Graine jusqu'à "
         "Toujours vert), avec une sphère qui change de couleur et des célébrations de "
         "niveau, d'après l'ensemble de votre étude."),
        ("Collectionnez les récompenses",
         "Débloquez près de 200 récompenses, de la rareté Commune à Légendaire, y compris des "
         "médailles thématiques liées au contenu ; ouvrez une médaille pour voir votre "
         "progression vers la suivante."),
    ],
    "sections": [
        ("De la motivation sans pression",
         "Ce ne sont pas des objectifs fixés par quelqu'un d'autre — c'est le miroir de ce que "
         "vous avez déjà fait. Voir une série qu'on n'a pas envie de casser, ou un niveau "
         "presque atteint, encourage doucement à tenir la bonne habitude. Et une Carte à "
         "partager résume votre année sans exposer la moindre note personnelle."),
    ],
    "faq": [
        ("Les séries et les récompenses se mettent-elles à jour toutes seules ?",
         "Elles reflètent la sauvegarde que vous chargez : créez une nouvelle sauvegarde pour "
         "voir votre progression la plus récente. Rien ne tourne en arrière-plan."),
        ("Est-ce que tout cela est partagé ou envoyé ?",
         "Non. Tout est calculé localement à partir de votre sauvegarde ; seule la carte de "
         "synthèse est quelque chose que vous pouvez choisir de partager, et elle ne contient "
         "le texte d'aucune note."),
    ],
}

GUIDES_FR["share-convention-assembly-notes"] = {
    "title": "Comment partager ses notes de congrès et d'assemblée depuis JW Library",
    "h1": "Partager vos notes de congrès, d'assemblée et de réunion",
    "description": "Transmettez vos notes de congrès, d'assemblée ou de réunion à votre famille "
                   "et à vos amis dans un petit fichier — sans livrer toute votre bibliothèque "
                   "ni écraser la leur. Un usage concret du partage de notes.",
    "intro": [
        "Vous avez pris des notes soignées pendant un congrès ; un ami qui a manqué une "
        "session serait ravi de les avoir ; des membres de la famille veulent les points pour "
        "leur propre révision. Envoyer toute votre sauvegarde est disproportionné et "
        "effacerait les notes du destinataire s'il la restaurait. Le partage de notes vous "
        "laisse transmettre exactement les notes que vous voulez — et laisse le destinataire "
        "garder tout ce qu'il a déjà.",
    ],
    "steps": [
        ("Chargez votre sauvegarde sur la page de partage",
         "Rendez-vous sur jwsync.org/share.html et chargez votre fichier .jwlibrary."),
        ("Sélectionnez uniquement les notes du congrès",
         "Choisissez l'étiquette de l'événement dans le filtre par étiquette du sélecteur et "
         "cliquez sur Tout sélectionner — la liste correspond déjà exactement aux notes que "
         "vous avez étiquetées. Les surlignages rattachés suivent."),
        ("Envoyez le petit fichier de partage",
         "JW Sync fabrique un petit fichier ne contenant que ces notes. Envoyez-le comme vous "
         "voulez — messagerie, e-mail, AirDrop. Pas de serveur, pas de compte."),
        ("Famille et amis les ajoutent à leur bibliothèque",
         "Chacun ouvre la même page, charge votre fichier avec sa propre sauvegarde, et "
         "obtient une nouvelle sauvegarde où vos notes sont ajoutées. Leurs notes ne sont "
         "jamais écrasées, et les vôtres arrivent étiquetées, donc faciles à retrouver."),
    ],
    "sections": [
        ("Une étiquette rend tout cela immédiat",
         "Si vous étiquetez vos notes pendant l'événement (par exemple « Congrès 2026 »), les "
         "sélectionner ensuite tient en un clic de filtre et un Tout sélectionner. Il vaut la "
         "peine de créer une nouvelle étiquette au début de chaque congrès, assemblée ou "
         "réunion spéciale, précisément pour cette raison."),
    ],
    "faq": [
        ("Puis-je partager avec plusieurs personnes à la fois ?",
         "Oui — le fichier de partage n'est qu'un fichier. Envoyez-le à autant de personnes "
         "que vous voulez ; chacune l'ajoute à sa propre bibliothèque indépendamment."),
        ("Toute ma bibliothèque sera-t-elle exposée ?",
         "Non. Seules les notes que vous sélectionnez figurent dans le fichier ; le reste de "
         "votre bibliothèque reste privé."),
    ],
}

GUIDES_FR["share-jw-library-notes-by-tag"] = {
    "title": "Ne partager que les notes JW Library portant une étiquette",
    "h1": "Ne partager que les notes portant une étiquette donnée",
    "description": "Envoyez un sujet, un projet ou le nécessaire pour un étudiant plutôt que "
                   "toute votre bibliothèque — et vos étiquettes voyagent avec, si bien que "
                   "les notes arrivent organisées de l'autre côté.",
    "intro": [
        "Une étiquette est en général l'unité naturelle de partage. Vous avez étiqueté tout ce "
        "que vous avez réuni sur un sujet, tout ce qui vient d'un événement, ou tout ce que "
        "vous parcourez avec une personne — et c'est cet ensemble, pas votre bibliothèque "
        "entière, que l'autre veut vraiment.",
        "Le partage de notes de JW Sync fonctionne note par note : une étiquette n'est donc "
        "que la liste que vous cochez. Les notes conservent leurs étiquettes en sortant, ce "
        "qui veut dire que la personne qui les reçoit pourra filtrer exactement le même "
        "ensemble dans sa propre bibliothèque par la suite.",
    ],
    "steps": [
        ("Assurez-vous que les notes portent l'étiquette",
         "Étiquetez-les dans JW Library au fil de l'eau, ou ouvrez votre sauvegarde dans "
         "l'Explorateur d'étude sur jwsync.org et utilisez l'éditeur d'étiquettes pour en "
         "ajouter une à plusieurs notes d'un coup. Étiqueter avec cohérence maintenant, c'est "
         "ce qui fera du partage l'affaire d'une minute plus tard."),
        ("Ouvrez la page de partage et chargez votre sauvegarde",
         "Rendez-vous sur jwsync.org/share.html, choisissez Envoyer des notes et chargez votre "
         "fichier .jwlibrary. Il est lu dans votre navigateur et ne quitte jamais votre "
         "appareil."),
        ("Choisissez l'étiquette dans le filtre, puis Tout sélectionner",
         "Le sélecteur de notes propose un filtre listant chaque étiquette de votre sauvegarde "
         "avec le nombre de notes correspondantes. Choisissez la vôtre et la liste se réduit "
         "exactement à ces notes ; Tout sélectionner les coche toutes. Voilà toute la "
         "sélection — deux clics."),
        ("Créez le fichier et envoyez-le",
         "JW Sync construit un petit fichier de partage contenant uniquement les notes "
         "cochées. Envoyez-le par messagerie, e-mail ou AirDrop — aucun serveur n'intervient "
         "et aucun compte n'est requis d'un côté ni de l'autre."),
        ("La personne l'ajoute à sa propre sauvegarde",
         "Elle ouvre la même page, choisit Recevoir, prévisualise les notes et les ajoute à sa "
         "sauvegarde. Vos étiquettes arrivent avec les notes, plus une étiquette identifiant "
         "l'import : l'ensemble est donc lui aussi à un filtre de distance pour elle."),
    ],
    "sections": [
        ("Pourquoi partager une étiquette plutôt qu'une sauvegarde",
         "Livrer une sauvegarde .jwlibrary complète, c'est donner tout ce que vous avez jamais "
         "écrit, et la restaurer effacerait les notes de l'autre personne. Partager une "
         "sélection étiquetée fait exactement l'inverse sur les deux plans : elle ne voit que "
         "ce que vous avez choisi, et ne perd rien de ce qui lui appartient."),
        ("Affiner encore, ou partager plusieurs étiquettes",
         "Le filtre par étiquette et le champ de recherche fonctionnent ensemble : choisissez "
         "une étiquette, puis tapez un mot pour réduire encore, et Tout sélectionner ne coche "
         "toujours que ce qui est devant vous. La recherche porte aussi sur les noms "
         "d'étiquettes : un mot-clé partagé par plusieurs étiquettes les rassemble en une "
         "passe. Chaque note de la liste affiche ses étiquettes, vous voyez donc ce que vous "
         "envoyez avant de l'envoyer."),
        ("Des étiquettes à garder pour le partage",
         "Il vaut la peine de garder quelques étiquettes qui n'existent que pour être "
         "partagées — le nom d'un événement, un sujet que vous documentez pour d'autres, la "
         "personne avec qui vous étudiez. Le moment venu, rien à chercher : l'ensemble est "
         "déjà constitué."),
    ],
    "faq": [
        ("Mes étiquettes passent-elles à l'autre personne ?",
         "Oui. Les notes partagées portent leurs étiquettes, et l'import reçoit une étiquette "
         "propre : le destinataire peut donc retrouver, relire ou retirer tout le lot plus "
         "tard."),
        ("Et si une note porte plusieurs étiquettes ?",
         "Elle apparaît sous chacune d'elles dans le filtre, et toutes ses étiquettes voyagent "
         "avec elle. Filtrer sur une étiquette n'enlève jamais les autres."),
        ("Partager retire-t-il les notes de ma bibliothèque ?",
         "Non. Le partage copie les notes dans un petit fichier ; votre sauvegarde et votre "
         "application ne sont pas touchées."),
        ("Puis-je envoyer la même étiquette à plusieurs personnes ?",
         "Oui — le fichier de partage est un fichier ordinaire. Envoyez-le à qui vous voulez, "
         "chacun l'ajoute à sa propre bibliothèque indépendamment."),
    ],
}

GUIDES_FR["share-notes-with-bible-student"] = {
    "title": "Partager ses notes JW Library avec un étudiant de la Bible",
    "h1": "Partager ses notes d'étude avec la personne avec qui on étudie la Bible",
    "description": "Envoyez les notes d'une leçon — versets, exemples, les points que vous avez "
                   "préparés — directement dans le JW Library de l'autre personne, sans "
                   "toucher à ce qu'elle a écrit elle-même.",
    "intro": [
        "Quand vous préparez une étude, l'essentiel du travail finit dans vos propres notes : "
        "les versets supplémentaires, l'exemple qui a fait mouche, la réponse à la question "
        "posée la semaine dernière. Le lire à voix haute est une chose ; laisser à la personne "
        "une copie qu'elle pourra relire toute la semaine en est une autre.",
        "Le partage de notes dépose vos notes préparées dans sa bibliothèque sous forme de "
        "vraies notes JW Library, rattachées aux mêmes paragraphes et versets — et non comme "
        "une capture d'écran ou un message qu'elle fera défiler sans lire.",
    ],
    "steps": [
        ("Préparez les notes de la leçon dans JW Library",
         "Écrivez vos notes comme d'habitude, sur les paragraphes et les versets couverts par "
         "la leçon. Donnez-leur une étiquette — le prénom de la personne, ou la publication — "
         "pour que l'ensemble soit facile à sélectionner ensuite."),
        ("Ouvrez la page de partage et chargez votre sauvegarde",
         "Créez une sauvegarde (Étude personnelle → Sauvegarde et restauration → Créer une "
         "sauvegarde), puis ouvrez jwsync.org/share.html, choisissez Envoyer des notes et "
         "chargez le fichier. Il ne quitte jamais votre appareil."),
        ("Cochez les notes de cette leçon",
         "Filtrez le sélecteur par l'étiquette utilisée et cliquez sur Tout sélectionner, ou "
         "cherchez et cochez une à une. Créez le fichier de partage — tout le reste de votre "
         "bibliothèque reste où il est."),
        ("Envoyez-le et guidez la réception",
         "La personne a d'abord besoin d'une sauvegarde à elle — Étude personnelle → "
         "Sauvegarde et restauration → Créer une sauvegarde. Elle ouvre ensuite "
         "jwsync.org/share.html, choisit Recevoir, charge votre fichier et sa sauvegarde, et "
         "télécharge la sauvegarde mise à jour."),
        ("Elle la restaure dans JW Library",
         "Sauvegarde et restauration → Restaurer, elle choisit le fichier mis à jour, et vos "
         "notes apparaissent dans sa bibliothèque aux côtés des siennes — étiquetées, pour "
         "qu'elle sache lesquelles viennent de vous."),
    ],
    "sections": [
        ("Ses notes ne sont jamais écrasées",
         "C'est la différence importante avec l'envoi d'une sauvegarde. Une restauration "
         "remplace toute la bibliothèque d'un appareil ; recevoir des notes partagées y "
         "ajoute. Tout ce que la personne a écrit elle-même — y compris sur les mêmes "
         "paragraphes — reste exactement tel quel."),
        ("Un rythme hebdomadaire qui prend deux minutes",
         "Une fois que vous l'avez fait tous les deux une première fois, la routine est "
         "courte : préparer, cocher, envoyer, restaurer. Beaucoup trouvent plus simple "
         "d'envoyer les notes juste après la préparation, pour que l'étudiant les ait avant "
         "l'étude plutôt qu'après."),
    ],
    "faq": [
        ("L'étudiant a-t-il besoin d'un compte ou d'une application ?",
         "Aucun compte nulle part, et rien à installer en dehors de JW Library lui-même — la "
         "page de partage est une page web ordinaire."),
        ("Et si l'étudiant n'a jamais fait de sauvegarde ?",
         "Il en fait une d'abord, dans JW Library sous Étude personnelle → Sauvegarde et "
         "restauration. Même une bibliothèque qui paraît vide convient ; la sauvegarde est ce "
         "à quoi les notes partagées viennent s'ajouter."),
        ("Puis-je reprendre les notes plus tard ?",
         "Le fichier vous appartient tant que vous ne l'avez pas envoyé. Une fois que "
         "quelqu'un l'a, il est à lui, exactement comme n'importe quel message — ne partagez "
         "donc que ce que vous partageriez volontiers par écrit."),
    ],
}

GUIDES_FR["share-meeting-notes-with-family"] = {
    "title": "Partager les notes de réunion avec sa famille ou son foyer",
    "h1": "Partager les notes de la réunion de cette semaine avec la famille",
    "description": "Quelqu'un était malade, au travail ou absent — envoyez-lui les notes de la "
                   "semaine dans un petit fichier qu'il ajoutera à son propre JW Library, sans "
                   "que personne ne perde quoi que ce soit.",
    "intro": [
        "Dans la plupart des foyers, chacun prend ses propres notes sur son propre appareil, "
        "et il y a toujours quelqu'un qui manque une réunion. Lire vos notes à table marche "
        "une fois ; les déposer dans la bibliothèque de l'autre, c'est ce qui lui permettra de "
        "s'en servir plus tard, à l'endroit où il ira vraiment les chercher.",
        "Comme le partage se fait note par note et non sauvegarde par sauvegarde, plusieurs "
        "personnes peuvent échanger librement sans que la bibliothèque de quiconque soit "
        "écrasée.",
    ],
    "steps": [
        ("Sauvegardez l'appareil sur lequel vous avez pris les notes",
         "JW Library → Étude personnelle → Sauvegarde et restauration → Créer une sauvegarde."),
        ("Sélectionnez les notes de la semaine",
         "Sur jwsync.org/share.html, choisissez Envoyer des notes, chargez votre sauvegarde et "
         "cochez les notes de cette semaine — chercher par publication les rassemble vite, et "
         "si vous étiquetez les notes de la semaine, le filtre par étiquette les réunit en un "
         "clic."),
        ("Envoyez-le dans la conversation familiale",
         "Créez le fichier de partage et envoyez-le par le canal que le foyer utilise déjà — "
         "messagerie, e-mail, AirDrop. C'est un petit fichier ne contenant que les notes "
         "cochées."),
        ("Chacun l'ajoute à sa propre sauvegarde",
         "La personne ouvre la même page, choisit Recevoir, charge votre fichier avec une "
         "sauvegarde à elle, télécharge la sauvegarde mise à jour et la restaure dans JW "
         "Library."),
    ],
    "sections": [
        ("La bibliothèque de chacun reste la sienne",
         "Les notes de personne ne sont remplacées, et personne n'a à livrer toute sa "
         "bibliothèque pour participer. Les notes importées arrivent sous une étiquette : "
         "chacun voit d'un coup d'œil lesquelles viennent d'ailleurs et peut supprimer le lot "
         "plus tard s'il préfère ne pas le garder."),
        ("Culte familial : rassembler plutôt que disperser",
         "Le même outil fonctionne dans l'autre sens. Si tout le monde prend des notes pendant "
         "le culte familial, une personne peut réunir les fichiers de partage des autres dans "
         "une seule sauvegarde et disposer des notes combinées du foyer sur le même sujet."),
    ],
    "faq": [
        ("Les appareils des enfants peuvent-ils participer ?",
         "Tout appareil capable de faire tourner JW Library et d'ouvrir une page web le peut. "
         "Les étapes sont identiques sur téléphone, tablette ou ordinateur."),
        ("Faut-il être sur la même plateforme ?",
         "Non. Android, iPhone, iPad et l'application Windows utilisent le même format de "
         "sauvegarde : les notes passent de l'un à l'autre sans conversion."),
    ],
}

GUIDES_FR["receive-shared-jw-library-notes"] = {
    "title": "On m'a envoyé des notes JW Library — comment les ouvrir ?",
    "h1": "Ajouter à votre JW Library des notes que quelqu'un a partagées avec vous",
    "description": "On vous a envoyé un fichier de notes partagées ou un bloc de texte. Voici "
                   "comment le prévisualiser et l'ajouter à votre propre sauvegarde JW "
                   "Library sans perdre une seule de vos notes.",
    "intro": [
        "Les notes JW Library partagées arrivent sous forme d'un petit fichier (se terminant "
        "par .jwshare.json) ou d'un bloc de texte collé dans un message. JW Library lui-même "
        "n'ouvre ni l'un ni l'autre — mais vous n'en avez pas besoin. Le côté réception de JW "
        "Sync lit les notes partagées, vous montre ce qu'elles contiennent et les écrit dans "
        "une sauvegarde à vous.",
        "Tout l'échange se déroule sur votre appareil. Pas de compte, rien n'est envoyé, et "
        "vos propres notes reçoivent des ajouts, jamais des remplacements.",
    ],
    "steps": [
        ("Sauvegardez d'abord votre propre bibliothèque",
         "Dans JW Library : Étude personnelle → Sauvegarde et restauration → Créer une "
         "sauvegarde. C'est le fichier auquel les notes partagées seront ajoutées ; il doit "
         "donc être à jour."),
        ("Ouvrez la page de partage et choisissez Recevoir",
         "Rendez-vous sur jwsync.org/share.html et choisissez Recevoir des notes."),
        ("Chargez ce qu'on vous a envoyé",
         "Choisissez le fichier .jwshare.json, ou collez directement le texte partagé dans la "
         "zone prévue s'il est arrivé sous forme de message. Dans les deux cas, vous obtenez "
         "un aperçu en lecture seule de chaque note avant que quoi que ce soit ne soit écrit."),
        ("Ajoutez-les à votre sauvegarde",
         "Chargez votre propre sauvegarde, choisissez l'étiquette que porteront les notes "
         "importées, et ajoutez-les. JW Sync construit une sauvegarde mise à jour à "
         "télécharger."),
        ("Restaurez la sauvegarde mise à jour dans JW Library",
         "Étude personnelle → Sauvegarde et restauration → Restaurer, choisissez le fichier "
         "mis à jour. Les notes partagées sont maintenant dans votre bibliothèque, sur les "
         "bons paragraphes et versets."),
    ],
    "sections": [
        ("Rien de ce qui est à vous n'est remplacé",
         "Les notes partagées sont ajoutées comme de nouvelles notes. Même là où une note "
         "partagée tombe sur un paragraphe où vous aviez déjà écrit, les deux survivent — la "
         "vôtre intacte, la sienne à côté. La seule chose à garder en tête est la règle "
         "habituelle de la restauration : restaurez la sauvegarde mise à jour, pas une plus "
         "ancienne."),
        ("Changé d'avis plus tard ?",
         "Chaque note importée porte l'étiquette que vous avez choisie au moment de "
         "l'ajouter. Ouvrez votre sauvegarde dans l'Explorateur d'étude, filtrez sur cette "
         "étiquette, et vous pouvez relire ou supprimer tout le lot d'un coup."),
    ],
    "faq": [
        ("Le fichier est arrivé renommé en .txt ou s'ouvre comme du texte — est-il cassé ?",
         "Non. Les messageries font souvent cela. Copiez le texte et collez-le dans la zone "
         "Recevoir ; cela fonctionne exactement pareil."),
        ("Ai-je besoin de toute la sauvegarde de l'expéditeur ?",
         "Non. Le fichier de partage ne contient que les notes qu'il a choisi d'envoyer — rien "
         "d'autre de sa bibliothèque."),
        ("Quelque chose est-il envoyé quand je prévisualise les notes ?",
         "Non. Lire le fichier partagé, le prévisualiser et écrire la sauvegarde mise à jour "
         "se font tous dans votre navigateur, sur votre appareil."),
    ],
}

GUIDES_FR["share-notes-with-study-group"] = {
    "title": "Partager ses recherches avec un groupe d'étude",
    "h1": "Partager ses recherches avec un groupe — et récupérer les leurs",
    "description": "Un fichier, plusieurs personnes : envoyez un ensemble de notes de recherche "
                   "à tous ceux qui étudient le même sujet, et rassemblez ce qu'ils vous "
                   "renvoient en un seul ensemble à vous.",
    "intro": [
        "Quand plusieurs personnes creusent le même sujet, les recherches finissent éparpillées "
        "— l'une a trouvé les renvois, une autre le contexte historique, une troisième les "
        "exemples. Lire les captures d'écran des autres n'a rien à voir avec le fait d'avoir "
        "la matière dans sa propre bibliothèque, sur les mêmes versets, consultable l'année "
        "prochaine.",
        "Comme un fichier de partage n'est qu'un fichier, un seul export sert à tout le "
        "groupe, et le même mécanisme ramène leur travail jusqu'à vous.",
    ],
    "steps": [
        ("Étiquetez vos recherches au fur et à mesure",
         "Donnez une étiquette au sujet dans JW Library pour que l'ensemble reste groupé. Dans "
         "l'Explorateur d'étude, vous pouvez ajouter une étiquette à plusieurs notes d'un coup "
         "si vous ne l'aviez pas fait sur le moment."),
        ("Créez un fichier de partage pour le groupe",
         "Sur jwsync.org/share.html, choisissez Envoyer des notes, chargez votre sauvegarde, "
         "prenez l'étiquette du sujet dans le filtre, cliquez sur Tout sélectionner et créez "
         "le fichier."),
        ("Publiez-le une seule fois",
         "Envoyez le même fichier à tout le monde — une conversation de groupe, un e-mail à "
         "plusieurs destinataires, ce que le groupe utilise déjà. Aucune configuration par "
         "personne, aucune copie sur un serveur."),
        ("Demandez les leurs en retour",
         "Chacun peut faire exactement la même chose de son côté. Ajoutez tour à tour à votre "
         "sauvegarde chaque fichier reçu, en donnant à chaque import son étiquette — le nom de "
         "l'expéditeur fonctionne bien — pour toujours savoir de qui vient quoi."),
    ],
    "sections": [
        ("Un ensemble combiné, mais toujours attribuable",
         "Après quelques tours, vous avez toutes les recherches du groupe sur le sujet dans "
         "votre propre bibliothèque, sur les bons paragraphes et versets, chaque contribution "
         "étiquetée par sa source. La recherche trouve tout d'un coup ; les étiquettes vous "
         "permettent de tout re-séparer quand vous le souhaitez."),
        ("Personne n'a à exposer sa bibliothèque",
         "Chacun ne partage que les notes qu'il coche. Le reste de la bibliothèque de chaque "
         "personne — étude personnelle, rappels privés, tout le reste — n'entre jamais dans le "
         "fichier."),
    ],
    "faq": [
        ("Y a-t-il une limite au nombre de notes partageables d'un coup ?",
         "En pratique, non. Les notes sont légères ; même un gros ensemble produit un fichier "
         "que vous pouvez envoyer dans un message."),
        ("Et si deux personnes m'envoient la même note ?",
         "Vous la verrez deux fois, chacune sous l'étiquette de son expéditeur. La recherche "
         "de l'Explorateur d'étude rend les quasi-doublons faciles à repérer et à supprimer."),
        ("Peut-on recevoir sans rien renvoyer ?",
         "Oui. Recevoir et envoyer sont indépendants — personne n'est obligé de partager pour "
         "pouvoir ajouter ce qu'on lui a donné."),
    ],
}

GUIDES_FR["share-talk-preparation-notes"] = {
    "title": "Transmettre les recherches derrière un discours ou une assignation",
    "h1": "Transmettre vos recherches de discours et d'assignations",
    "description": "Vous avez fait les recherches pour un discours, une partie ou une "
                   "assignation. Voici comment les transmettre à qui en aura besoin — sous "
                   "forme de vraies notes dans sa bibliothèque, ou de texte brut pour un "
                   "document.",
    "intro": [
        "Une préparation ne sert presque jamais une seule fois. Les versets que vous avez "
        "traqués, le contexte que vous avez lu, la façon dont vous avez fini par formuler un "
        "point — celui qui traitera la même matière plus tard préférerait partir de là plutôt "
        "que d'une page blanche.",
        "JW Sync vous offre deux façons de transmettre, adaptées à des personnes différentes : "
        "des notes qui atterrissent dans le JW Library de l'autre, ou du texte brut à coller "
        "dans un document.",
    ],
    "steps": [
        ("Rassemblez les recherches sous une étiquette",
         "Pendant la préparation, étiquetez les notes avec le thème ou l'assignation. Si elles "
         "sont déjà écrites et sans étiquette, ouvrez votre sauvegarde dans l'Explorateur "
         "d'étude et étiquetez-les en lot en deux minutes."),
        ("Choisissez la forme qui convient à l'autre",
         "Celui qui étudie dans JW Library veut des notes dans sa bibliothèque. Celui qui "
         "monte un document veut du texte. Vous pouvez faire les deux à partir du même "
         "ensemble."),
        ("Pour envoyer des notes : la page de partage",
         "Sur jwsync.org/share.html, choisissez Envoyer des notes, chargez votre sauvegarde, "
         "filtrez par l'étiquette utilisée, cliquez sur Tout sélectionner, puis créez le "
         "fichier. L'autre l'ajoute à sa propre sauvegarde et la restaure — ses notes ne sont "
         "pas touchées."),
        ("Pour envoyer du texte : l'export depuis l'Explorateur d'étude",
         "Filtrez sur le même ensemble et copiez-le ou exportez-le en Markdown ou en texte "
         "brut. La mise en forme survit : un plan structuré reste structuré une fois collé "
         "dans un document."),
    ],
    "sections": [
        ("Gardez-en une copie pour vous, sous une forme que vous retrouverez",
         "Le même export mérite d'être conservé pour votre propre usage. Une étiquette plus "
         "une plage de dates rendent toute la préparation retrouvable des années plus tard — "
         "exactement quand vous en aurez besoin — et l'extraction par date de l'Explorateur "
         "d'étude transforme n'importe quelle fenêtre de temps en fichier autonome."),
    ],
    "faq": [
        ("Les versets restent-ils liés aux bons passages ?",
         "Oui — les notes partagées conservent le paragraphe et le verset auxquels elles "
         "étaient rattachées : elles atterrissent au bon endroit dans la bibliothèque de "
         "l'autre."),
        ("Puis-je partager des notes qui portent des surlignages ?",
         "Oui. Les surlignages rattachés aux notes que vous partagez voyagent avec elles."),
    ],
}

GUIDES_FR["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Préparer la réunion avec les notes que vous avez déjà écrites",
    "h1": "La préparation hebdomadaire avec les notes que vous avez déjà",
    "description": "Vous avez déjà étudié cette matière. Voici une courte routine hebdomadaire "
                   "qui fait remonter vos anciennes notes, surlignages et réponses sur la même "
                   "publication avant que vous ne prépariez à nouveau.",
    "intro": [
        "La plupart des gens préparent chaque semaine à partir d'une page blanche, alors qu'ils "
        "ont déjà écrit sur le même sujet — parfois sur le même verset — plusieurs fois "
        "auparavant. Cette réflexion antérieure est dans votre bibliothèque ; le seul "
        "problème, c'est que rien ne vous la ramène au bon moment.",
        "Une routine de cinq minutes au début de la préparation corrige cela, et elle "
        "n'utilise rien d'autre que la sauvegarde que vous avez déjà.",
    ],
    "steps": [
        ("Chargez une sauvegarde à jour dans l'Explorateur d'étude",
         "Créez une sauvegarde dans JW Library, puis ouvrez-la sur jwsync.org. Tout est lu "
         "dans votre navigateur."),
        ("Cherchez le sujet avant de commencer",
         "Cherchez le verset-thème, le sujet ou la publication. Tout ce que vous avez écrit "
         "dessus les années passées remonte d'un bloc, à travers toutes les publications où "
         "cela apparaît."),
        ("Regardez vos réponses d'étude",
         "La vue Réponses d'étude rassemble les réponses saisies dans les questions : les "
         "passages précédents sur la même matière sont là pour être développés plutôt que "
         "répétés."),
        ("Ajoutez ce qui manque, puis remettez le tout en place",
         "Les notes peuvent être modifiées ou créées sur place — titre, texte, étiquettes, "
         "couleur de surlignage. Exportez la sauvegarde modifiée et restaurez-la dans JW "
         "Library : votre préparation est dans l'application pour la réunion."),
    ],
    "sections": [
        ("Pourquoi les anciennes notes comptent",
         "Relire vos conclusions précédentes rend la préparation cumulative. Vous cessez de "
         "redécouvrir les mêmes points et commencez à construire dessus — et les notes "
         "ajoutées cette semaine deviennent le point de départ du tour suivant."),
        ("Une version plus douce : laissez les notes venir à vous",
         "Si une recherche hebdomadaire vous paraît fastidieuse, Refaire surface, sur la page "
         "Statistiques d'étude, ramène de lui-même quelques anciennes notes chaque jour, dont "
         "celles écrites à cette date les années passées. Même bénéfice, aucune routine à "
         "retenir."),
    ],
    "faq": [
        ("Modifier dans le navigateur change-t-il directement ma bibliothèque ?",
         "Non. Vous exportez une sauvegarde mise à jour et vous la restaurez dans JW Library — "
         "l'application n'est jamais modifiée que par une restauration que vous effectuez "
         "vous-même."),
        ("Ma sauvegarde est-elle envoyée quand je fais une recherche dedans ?",
         "Non. Le fichier est lu localement dans votre navigateur ; rien n'est envoyé nulle "
         "part."),
    ],
}

GUIDES_FR["print-jw-library-notes"] = {
    "title": "Comment imprimer ses notes JW Library",
    "h1": "Mettre vos notes JW Library sur papier",
    "description": "JW Library n'a pas de bouton Imprimer. Exportez vos notes en texte ou en "
                   "Markdown, collez-les dans un document et imprimez — un journal d'étude, un "
                   "jeu de notes pour quelqu'un sans l'application, ou une archive.",
    "intro": [
        "Il n'existe aucun moyen d'imprimer depuis JW Library, et les captures d'écran d'un "
        "téléphone se lisent mal. Mais les notes sont les vôtres, et les amener dans un "
        "document imprimable est simple dès lors qu'on peut lire le fichier de sauvegarde.",
        "L'Explorateur d'étude lit une sauvegarde .jwlibrary dans votre navigateur et vous "
        "permet de copier ou d'exporter n'importe quelle sélection de notes en texte brut ou "
        "en Markdown — ce que tout traitement de texte, toute application de notes et toute "
        "imprimante comprennent déjà.",
    ],
    "steps": [
        ("Créez une sauvegarde et ouvrez-la",
         "JW Library → Étude personnelle → Sauvegarde et restauration → Créer une sauvegarde, "
         "puis chargez le fichier sur jwsync.org."),
        ("Restreignez à ce que vous voulez sur papier",
         "Filtrez par publication, étiquette, couleur de surlignage ou plage de dates, ou "
         "cherchez un sujet. Tout imprimer est possible, mais un ensemble filtré donne "
         "généralement un document bien plus utile."),
        ("Copiez ou exportez en texte ou en Markdown",
         "Sortez la sélection en Markdown ou en texte brut. Le gras, l'italique et les listes "
         "survivent : les notes structurées restent structurées sur la page."),
        ("Collez dans un document et imprimez",
         "N'importe quel traitement de texte ou application de notes fera l'affaire. Réglez "
         "les titres et les marges voulus, puis imprimez ou enregistrez en PDF."),
    ],
    "sections": [
        ("Fabriquer un journal d'étude",
         "Une plage de dates est l'unité naturelle d'un journal imprimé — une année de notes, "
         "ou la période couvrant une publication. L'extraction par date vous donne un ensemble "
         "chronologique propre à imprimer ou à relier, ce qui est agréable à avoir hors de "
         "l'écran."),
        ("Imprimer pour quelqu'un qui n'utilise pas l'application",
         "Tout le monde n'étudie pas sur un appareil. Un jeu de notes imprimé sur la matière "
         "en cours est vraiment utile à qui préfère le papier, et cela prend les deux mêmes "
         "minutes que n'importe quel autre export."),
    ],
    "faq": [
        ("Puis-je imprimer aussi mes surlignages ?",
         "La vue des surlignages liste les passages que vous avez marqués, et cette liste se "
         "copie en texte à côté de vos notes."),
        ("L'export change-t-il quelque chose dans JW Library ?",
         "Non. L'export lit une copie de votre sauvegarde ; votre fichier d'origine et "
         "l'application ne sont pas touchés."),
    ],
}

GUIDES_FR["clean-up-duplicate-jw-library-notes"] = {
    "title": "Nettoyer les notes JW Library en double et les notes vides",
    "h1": "Faire le ménage : notes en double, notes vides et encombrement",
    "description": "Sauvegarde restaurée deux fois, ou mêmes notes importées à nouveau ? Le "
                   "Docteur de bibliothèque analyse votre fichier .jwlibrary dans le "
                   "navigateur, trouve les doublons et les notes vides, et produit une copie "
                   "propre.",
    "intro": [
        "Les bibliothèques accumulent de l'encombrement. Restaurer une sauvegarde sur un "
        "appareil qui portait déjà une partie des mêmes notes, importer deux fois un ensemble "
        "partagé, ou des années de notes à moitié écrites jamais terminées — chacun laisse "
        "quelque chose derrière lui, et JW Library n'offre aucun moyen de balayer tout cela en "
        "lot.",
        "Le Docteur de bibliothèque est un bilan de santé gratuit pour un fichier .jwlibrary. "
        "Il analyse la sauvegarde dans votre navigateur, vous dit en langage clair ce qu'il a "
        "trouvé, et répare ce qui est réparable d'une seule pression.",
    ],
    "steps": [
        ("Sauvegardez d'abord — comme toujours",
         "JW Library → Étude personnelle → Sauvegarde et restauration → Créer une sauvegarde. "
         "Gardez ce fichier ; c'est votre filet de sécurité."),
        ("Lancez le bilan de santé",
         "Ouvrez jwsync.org, chargez la sauvegarde et démarrez le Docteur de bibliothèque. Il "
         "examine le contenu et la structure du fichier sans l'envoyer nulle part."),
        ("Lisez ce qu'il a trouvé",
         "Doublons, notes vides et autres résidus sont listés clairement, avec les nombres, "
         "pour que vous mesuriez l'ampleur du problème avant de changer quoi que ce soit."),
        ("Réparez et téléchargez la copie propre",
         "Une pression applique les réparations et produit un nouveau fichier .jwlibrary "
         "nettoyé. Votre original n'est jamais modifié."),
        ("Restaurez le fichier propre",
         "Sauvegarde et restauration → Restaurer, et choisissez le fichier nettoyé. Votre "
         "bibliothèque est la même, sans l'encombrement."),
    ],
    "sections": [
        ("D'où viennent les doublons, au départ",
         "Presque toujours d'une restauration. Si vous restaurez une sauvegarde sur un "
         "appareil qui portait déjà une partie de la même matière — ou si vous restaurez deux "
         "fois le même fichier par des chemins différents — l'application n'a aucun moyen de "
         "savoir qu'elle a déjà vu ces notes."),
        ("La fusion est le moyen de les éviter",
         "C'est exactement pourquoi fusionner deux sauvegardes est plus sûr que d'en restaurer "
         "une par-dessus l'autre : la fusion détecte la matière déjà présente et ne la garde "
         "qu'une fois. Les mêmes vérifications tournent dans chaque fusion, donc une "
         "sauvegarde fusionnée ressort propre même si les fichiers d'entrée ne l'étaient pas."),
    ],
    "faq": [
        ("Va-t-il supprimer des notes que je veux vraiment garder ?",
         "Il retire les doublons exacts et les notes vides — de la matière qui n'a rien à "
         "perdre. Et comme il écrit un nouveau fichier au lieu de modifier le vôtre, "
         "l'original reste toujours disponible."),
        ("Peut-il récupérer des notes supprimées dans l'application ?",
         "Non. Si une note a été supprimée dans JW Library avant la sauvegarde, elle n'est pas "
         "dans le fichier — c'est du côté d'une sauvegarde plus ancienne qu'il faut chercher."),
    ],
}

GUIDES_FR["backup-jw-library-before-phone-repair"] = {
    "title": "Sauvegarder JW Library avant une réinitialisation ou une réparation",
    "h1": "Avant une réinitialisation d'usine, une réparation ou la revente du téléphone",
    "description": "Une réinitialisation efface les notes JW Library avec le reste, et les "
                   "outils de transfert ne les emportent pas. Faites une sauvegarde, vérifiez "
                   "qu'elle s'ouvre vraiment, puis réinitialisez sans rien risquer.",
    "intro": [
        "Réinitialisez le téléphone, envoyez-le en réparation ou donnez-le à quelqu'un, et les "
        "données d'étude personnelle de JW Library partent avec. Les photos et les "
        "applications reviennent d'une sauvegarde cloud ; des années de notes, surlignages et "
        "signets, généralement pas, car les outils de transfert ignorent les données privées "
        "de l'application.",
        "La parade prend cinq minutes, et l'étape que tout le monde saute est justement la "
        "plus importante : vérifier que le fichier de sauvegarde est réellement lisible avant "
        "que l'appareil ne soit effacé.",
    ],
    "steps": [
        ("Créez la sauvegarde",
         "JW Library → Étude personnelle → Sauvegarde et restauration → Créer une sauvegarde. "
         "Vous obtenez un fichier .jwlibrary — quelques mégaoctets en général."),
        ("Sortez-la de l'appareil",
         "Envoyez-la-vous par e-mail, ou mettez-la sur Drive, iCloud ou dans un dossier de "
         "votre ordinateur. Une sauvegarde qui n'existe que sur le téléphone que vous allez "
         "effacer n'est pas une sauvegarde."),
        ("Vérifiez qu'elle s'ouvre avant d'effacer quoi que ce soit",
         "Chargez le fichier sur jwsync.org et regardez — les notes, surlignages et signets "
         "doivent tous être là, et le bilan de santé signalera tout problème. C'est tout "
         "l'intérêt de l'exercice : découvrir après coup que le fichier est illisible, c'est "
         "trop tard."),
        ("Réinitialisez, puis restaurez",
         "Après la réinitialisation ou la réparation, installez JW Library, connectez-vous, "
         "puis Sauvegarde et restauration → Restaurer et choisissez votre fichier."),
        ("Vous avez utilisé un téléphone de prêt entre-temps ? Fusionnez, n'écrasez pas",
         "Si vous avez pris des notes sur un appareil temporaire, sauvegardez-le lui aussi et "
         "fusionnez les deux fichiers sur jwsync.org avant de restaurer — sinon, restaurer "
         "l'ancienne sauvegarde efface tout ce que vous avez écrit en attendant."),
    ],
    "sections": [
        ("Pourquoi la vérification vaut la minute supplémentaire",
         "Transferts interrompus, espaces de stockage en ligne qui abîment les fichiers et "
         "extensions renommées en route produisent tous des sauvegardes qui ont l'air "
         "correctes dans un dossier et échouent à la restauration. Ouvrir le fichier d'abord "
         "transforme un problème silencieux en un problème que vous pouvez encore régler, "
         "pendant que l'appareil d'origine a toujours les données."),
        ("Gardez le fichier après la restauration",
         "Ne le supprimez pas une fois le nouvel appareil opérationnel. Les vieilles "
         "sauvegardes sont le seul recours après une note supprimée par accident des mois plus "
         "tard, et elles ne coûtent rien à conserver."),
    ],
    "faq": [
        ("Mes publications téléchargées reviendront-elles ?",
         "La sauvegarde contient vos données d'étude personnelle — notes, surlignages, "
         "signets, étiquettes et listes de lecture. Les publications se retéléchargent "
         "ensuite."),
        ("Le fichier marche-t-il si je change de marque de téléphone ou de plateforme ?",
         "Oui. Le format .jwlibrary est le même sur Android, iPhone, iPad et Windows."),
    ],
}

GUIDES_FR["jw-library-notes-missing-after-update"] = {
    "title": "Notes JW Library disparues après une mise à jour ou une réinstallation",
    "h1": "Notes disparues après une mise à jour, une réinstallation ou une restauration",
    "description": "Vos notes se sont volatilisées après une mise à jour, une réinstallation ou "
                   "une reconnexion. Que faire en premier, ce qu'il ne faut pas faire, et "
                   "comment les récupérer sans perdre ce que vous avez écrit depuis.",
    "intro": [
        "Ouvrir JW Library après une mise à jour et constater la disparition de ses notes est inquiétant, et dans la grande majorité des cas elles sont récupérables. Ce qui compte, c'est ce que vous faites dans les minutes qui suivent — précisément, ne pas faire la seule chose qui transforme une situation récupérable en perte définitive.",
        "C'est un moment désagréable : JW Library s'ouvre, et les notes n'y sont pas. Avant "
        "toute chose, un conseil — ne vous précipitez pas. L'essentiel de ce qui rend cette "
        "situation irrécupérable se fait dans les dix premières minutes, en écrasant "
        "précisément la sauvegarde qui contient encore les notes manquantes.",
        "Suivez les étapes ci-dessous dans l'ordre. Le but est d'aboutir à un seul fichier "
        "contenant à la fois les anciennes notes et tout ce que vous avez écrit depuis.",
    ],
    "steps": [
        ("N'écrasez pas encore vos sauvegardes",
         "Évitez de créer une nouvelle sauvegarde par-dessus une ancienne, et ne restaurez "
         "rien à l'aveugle. Un ancien fichier de sauvegarde est l'endroit le plus probable où "
         "vos notes existent encore."),
        ("Traquez la sauvegarde la plus récente que vous ayez",
         "Vérifiez les pièces jointes de vos e-mails, Google Drive, iCloud Drive, le dossier "
         "de téléchargements de votre ordinateur et tout autre appareil sur lequel vous avez "
         "restauré. Les sauvegardes étant légères, on en a souvent plus de copies qu'on ne "
         "croit."),
        ("Regardez dans le fichier avant de le restaurer",
         "Chargez le candidat sur jwsync.org et voyez ce qu'il contient réellement — combien "
         "de notes, de quelles publications, jusqu'à quelle date. Cela vous dit si c'est le "
         "bon fichier, avant de vous engager dans une restauration."),
        ("Sauvegardez aussi l'appareil actuel",
         "Même s'il semble vide, sauvegardez-le. Si vous avez écrit quoi que ce soit depuis la "
         "disparition des notes, ce fichier en est la seule copie."),
        ("Fusionnez les deux, puis restaurez",
         "Fusionnez l'ancienne sauvegarde avec l'actuelle sur jwsync.org. Le résultat contient "
         "les notes récupérées et tout ce qui a été écrit depuis, les doublons n'étant gardés "
         "qu'une fois. Restaurez ce fichier fusionné — jamais l'ancienne sauvegarde seule."),
    ],
    "sections": [
        ("Pourquoi restaurer l'ancienne sauvegarde seule est une erreur",
         "Une restauration remplace purement et simplement la bibliothèque de l'appareil. Si "
         "vous restaurez directement l'ancienne sauvegarde, vous récupérez les notes "
         "manquantes et vous perdez tout ce qui a été écrit après. C'est la fusion préalable "
         "qui rend la récupération sans perte."),
        ("Si la sauvegarde elle-même refuse de se restaurer",
         "Un fichier qui échoue à la restauration n'est pas forcément perdu. Passez-lui le "
         "bilan de santé — les dégâts dus à un téléchargement interrompu, à une "
         "synchronisation cloud ou à une extension renommée sont souvent réparables, et une "
         "copie nettoyée se restaure normalement."),
        ("D'abord : ne créez pas encore de nouvelle sauvegarde",
         "Si les notes ont disparu, résistez au réflexe de sauvegarder immédiatement. Une sauvegarde capture l'état actuel, et si l'état actuel est vide vous risquez d'écraser le bon fichier que vous aviez déjà. Cherchez d'abord quelles sauvegardes existent — dans Téléchargements, Fichiers, le courriel ou le nuage — et décidez seulement ensuite. Rien sur l'appareil ne s'améliore grâce à une sauvegarde faite dans la panique."),
        ("Pourquoi une mise à jour peut sembler effacer des notes",
         "La cause habituelle n'est pas une suppression. Une mise à jour peut laisser l'application pointer vers une base de données neuve et vide alors que l'ancienne est toujours sur le disque ; une réinstallation — y compris celle effectuée automatiquement par une mise à jour de magasin interrompue — démarre l'application de zéro ; et sur les appareils partagés ou à plusieurs profils, l'application peut tourner sous un profil différent. Dans tous les cas, les notes ne sont pas tant supprimées que non chargées, et c'est pourquoi une restauration depuis une sauvegarde ramène généralement tout proprement."),
        ("Récupérer une ancienne sauvegarde sans jeter le travail récent",
         "Si vous avez étudié depuis la création de la sauvegarde, une restauration simple échange une perte contre une autre : elle ramène les anciennes notes et supprime les plus récentes. Le contournement consiste à sauvegarder l'état actuel dans un fichier distinct, à le fusionner avec l'ancienne sauvegarde pour que les deux ensembles de notes coexistent dans un seul fichier, puis à restaurer le résultat. Vous obtenez les notes récupérées et les récentes ensemble au lieu de devoir choisir."),
        ("Si l'application s'est réinstallée toute seule",
         "Une réinstallation vide le stockage privé de l'application : tout ce qui n'est pas dans une sauvegarde est irrécupérable, aucune copie infonuagique ne pouvant servir de recours. Vérifiez tous les endroits où un fichier .jwlibrary a pu être enregistré avant de conclure qu'il n'y en a aucun, y compris le dossier d'envoi de votre messagerie et tout stockage infonuagique que vous avez déjà utilisé. Dès que vous en trouvez un, restaurez-le, puis conservez désormais les sauvegardes hors de l'appareil."),
        ("Une fois tout revenu",
         "Quand vos notes sont restaurées, faites une sauvegarde de plus et rangez-la hors de l'appareil : l'épisode que vous venez de traverser en est l'argument. Si vous avez dû fusionner une ancienne sauvegarde avec l'état actuel pour en arriver là, conservez aussi les deux fichiers sources : ce sont des instantanés datés, et en avoir davantage est précisément ce qui a rendu la récupération possible."),
    ],
    "faq": [
        ("Les notes sont-elles encore quelque part sur l'appareil ?",
         "Pas sous une forme accessible depuis l'extérieur de l'application. La récupération "
         "passe réalistement par un fichier de sauvegarde antérieur — d'où l'importance de "
         "garder les anciens."),
        ("Se reconnecter ramène-t-il les notes ?",
         "Non. Les données d'étude personnelle ne sont pas rattachées à un compte ; elles "
         "vivent sur l'appareil et ne voyagent que par des fichiers de sauvegarde."),
        ("Et si ma seule sauvegarde date de plusieurs mois ?",
         "Fusionnez-la avec une sauvegarde de l'appareil tel qu'il est aujourd'hui. Vous "
         "récupérez tout ce que contient l'ancien fichier et gardez tout ce que l'appareil a "
         "encore, sans avoir à choisir."),
        ("Mes notes ont-elles vraiment disparu ?",
         "Pas nécessairement. S'il existe une sauvegarde quelque part, tout ce qu'elle contient est entièrement récupérable. Seul le travail réalisé après la sauvegarde la plus récente est irrécupérable."),
        ("Puis-je combiner une ancienne sauvegarde avec ce qui est sur l'appareil ?",
         "Oui : sauvegardez d'abord l'état actuel, fusionnez-le avec l'ancienne et restaurez le résultat. Les deux ensembles de notes se retrouvent dans la même bibliothèque."),
        ("Restaurer une ancienne sauvegarde supprimera-t-il mes notes récentes ?",
         "À elle seule, oui, car une restauration remplace les données de l'appareil. Fusionnez d'abord la sauvegarde actuelle avec l'ancienne et restaurez le fichier fusionné."),
        ("Dois-je réinstaller l'application pour régler cela ?",
         "Non : réinstaller vide le stockage privé de l'application et supprime toute chance de récupérer ce qui reste sur l'appareil. Cherchez d'abord une sauvegarde existante et gardez la réinstallation comme dernier recours, une fois que vous en avez une."),
    ],
}

GUIDES_FR["help-family-member-move-jw-library-notes"] = {
    "title": "Aider un proche à transférer ses notes JW Library",
    "h1": "Aider quelqu'un d'autre à transférer ou sauver ses notes JW Library",
    "description": "C'est vous qu'on appelle pour réparer le téléphone. Voici le chemin le plus "
                   "court et le plus fiable pour transférer les notes JW Library d'un proche "
                   "vers un nouvel appareil — y compris sans lire ses notes.",
    "intro": [
        "Tôt ou tard, quelqu'un vous tend son téléphone avec un neuf à côté. Les notes JW "
        "Library sont la partie qui ne se déplace pas toute seule, et c'est souvent celle qui "
        "compte le plus — des années d'étude qu'aucun outil de transfert n'emporte.",
        "La démarche est la même que pour vous-même, avec une considération supplémentaire "
        "qu'il vaut mieux régler d'abord : sur quel appareil le travail va se faire.",
    ],
    "steps": [
        ("Guidez la personne pour créer une sauvegarde sur l'ancien appareil",
         "JW Library → Étude personnelle → menu à trois points → Sauvegarde et restauration → "
         "Créer une sauvegarde. Cela enregistre un fichier .jwlibrary. Si vous n'êtes pas "
         "ensemble, cette partie se fait très bien par téléphone."),
        ("Récupérez le fichier là où vous en avez besoin",
         "Faites-le-lui envoyer par e-mail à elle-même, ou partager avec vous. Il est assez "
         "petit pour passer par n'importe quelle messagerie."),
        ("Vérifiez que le fichier s'ouvre",
         "Chargez-le sur jwsync.org et confirmez que les notes y sont. Le faire avant que "
         "l'ancien appareil ne soit effacé ou cédé, c'est ce qui transforme une mauvaise "
         "surprise en non-événement."),
        ("Fusionnez si le nouvel appareil a déjà des notes",
         "Si la personne utilise le nouveau téléphone depuis un moment, sauvegardez-le lui "
         "aussi et fusionnez les deux fichiers — sinon, restaurer l'ancienne sauvegarde efface "
         "tout ce qu'elle a écrit sur le nouvel appareil."),
        ("Accompagnez-la pour la restauration",
         "Sur le nouvel appareil : Sauvegarde et restauration → Restaurer, choisir le fichier. "
         "Notes, surlignages, signets et étiquettes apparaissent tous."),
    ],
    "sections": [
        ("Le faire sans lire ses notes",
         "Les notes d'étude personnelle sont personnelles. Si vous préférez ne pas les voir — "
         "ou que la personne préfère que vous ne les voyiez pas — faites tout sur son "
         "appareil : c'est une page web, vous pouvez donc ouvrir jwsync.org sur son téléphone "
         "ou sa tablette, y charger ses fichiers et ne jamais avoir la sauvegarde sur votre "
         "propre machine. Rien n'est envoyé dans les deux cas, mais ainsi le fichier ne quitte "
         "jamais ses mains."),
        ("Laissez-lui une sauvegarde qu'elle saura retrouver",
         "Avant de rendre le téléphone, assurez-vous que le fichier de sauvegarde se trouve "
         "quelque part où elle pourra le retrouver — sa propre boîte mail ou son espace en "
         "ligne, pas seulement votre dossier de téléchargements. La prochaine fois, elle "
         "n'aura peut-être pas besoin de vous."),
    ],
    "faq": [
        ("Puis-je le faire à distance ?",
         "Oui. Si la personne sait créer une sauvegarde et vous envoyer le fichier, tout le "
         "reste fonctionne à distance — et la restauration se résume à quelques gestes que "
         "vous pouvez lui expliquer."),
        ("Elle a un Android et le nouveau est un iPhone. Est-ce un problème ?",
         "Non. Le format de sauvegarde est identique sur Android, iPhone, iPad et Windows."),
        ("Et si elle n'a jamais fait de sauvegarde et que l'ancien téléphone a disparu ?",
         "Alors il n'y a rien à récupérer — les données vivaient sur cet appareil. Autant "
         "prendre tout de suite l'habitude de sauvegardes régulières sur le nouveau."),
    ],
}

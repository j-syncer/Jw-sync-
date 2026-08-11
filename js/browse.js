/* ──────────────────────────────────────────────────────────────────────────
   browse.js — Note Explorer (Study Explorer) module
   ----------------------------------------------------------------------------
   Lifted out of index.html in v3.8.0: 185 KB of inline script sat in the
   document on every page load, at document priority, competing with the
   render-blocking CSS for bandwidth. It is now fetched on demand by
   bootBrowse() in the lazy boot loader, and cached independently of the page.

   Defines window.__bootBrowse(); calling it exposes window.__openJwBrowse(file).
   Its styles still live in the <style> block inside index.html.
   ────────────────────────────────────────────────────────────────────────── */
window.__bootBrowse = function() {

(function(){
  'use strict';
  if(window.__openJwBrowse) return;

  // ---------- i18n ----------
  var I18N = {
    en:{title:"Study Explorer",search:"Search...",no_results:"Nothing matches your filters.",loading:"Loading library...",close:"Close",no_file:"Open a backup file first — pick one to browse.",pick_file:"Choose .jwlibrary file",count_one:"{n} item",count_many:"{n} items",color_all:"All colors",no_title:"Untitled",copy:"Copy",copied:"Copied",clear:"Clear",error:"Could not load:",pub_all:"All publications",tag_all:"All tags",back:"← Back",detail_empty:"Select an item from the list.",sort_newest:"Newest first",sort_oldest:"Oldest first",sort_pub:"By publication",modified:"Modified",no_content:"(No content)",too_many:"Showing first {n} of {total} — narrow the search.",pg_prev:"Prev",pg_next:"Next",pg_status:"Page {page} of {pages} · {total} results",err_corrupt:"This file isn't a readable .jwlibrary backup — it may be corrupted or the wrong type of file.",err_no_db:"This backup is missing its notes database (userData.db). Re-export it from JW Library.",err_not_sqlite:"The backup's database couldn't be opened — the file may be damaged.",tab_notes:"Notes",tab_highlights:"Highlights",tab_bookmarks:"Bookmarks",hl_label:"Highlight",hl_no_text:"Highlighted passage (text lives in the publication, not the backup).",hl_with_note:"With note",bm_label:"Bookmark",bm_slot:"Slot {n}",linked_note:"Linked note:",edit:"Edit",save:"Save",cancel:"Cancel",delete_item:"Delete",export_db:"Export .jwlibrary",n_edits:"{n} edit",n_edits_many:"{n} edits",add_tag:"+ Add tag",new_tag_ph:"Tag name...",delete_note_confirm:"Delete this note? This cannot be undone.",delete_hl_confirm:"Delete this highlight? This cannot be undone.",delete_bm_confirm:"Delete this bookmark? This cannot be undone.",yes_delete:"Yes, delete",change_color:"Color",unsaved_exit:"You have {n} unsaved edit(s). Close without exporting?",title_label:"Title",content_label:"Content",tags_label:"Tags",hl_color_label:"Highlight color",bm_title_label:"Bookmark title",plain_text_note:"Formatting simplified to plain text on save",rte_bold:"Bold",rte_italic:"Italic",rte_underline:"Underline",rte_bullets:"Bullet list",rich_text_note:"Edit with bold, italics and lists — formatting is kept",date_from:"From",date_to:"To",date_range:"Filter by date",extract_range:"Extract date range",extract_none:"No notes fall in this date range.",extract_hint:"Save a new .jwlibrary with only the notes in this date range.",copy_md:"Copy as Markdown",export_md:"Export Markdown",md_hint:"Download the notes shown as Markdown files (.zip)",sel_mode:"Select",sel_done:"Done",sel_all:"All",sel_none:"None",sel_count:"{n} selected",batch_tag:"Tag",batch_color:"Color",batch_delete:"Delete",batch_delete_confirm:"Delete {n}? You can Undo before exporting.",batch_tag_ph:"Tag name…",batch_add:"Add",undo:"Undo",redo:"Redo",tab_inputfields:"Study Answers",if_label:"Study answer",if_question:"Question",if_answer:"Your answer",if_empty:"(No answer yet)",delete_if_confirm:"Delete this study answer? You can Undo before exporting.",share_action:"Share",share_title:"Share notes",share_intro:"This makes a file you hand over yourself — nothing is uploaded. It contains the note text, so share only with people you trust.",share_count:"{n} notes",share_download:"Download file",share_copy:"Copy",share_tag:"Shared",receive_action:"Receive",receive_title:"Receive shared notes",receive_intro:"Paste shared text, or choose a .jwshare.json file someone sent you.",receive_paste_ph:"Paste shared notes here…",receive_choose:"Choose file",receive_preview:"Preview",receive_invalid:"That doesn't look like valid shared-notes data.",preview_readonly:"Preview",adopt:"Adopt {n} into my library",adopt_need_lib:"Open a backup first",adopted:"Adopted {n} notes (tagged \"Shared\").",open_share:"Share Notes →",ask_btn:"Ask",ask_title:"Ask Your Library",ask_sub:"Search your notes by meaning, not just keywords — ask in plain language and find related notes even when they use different words. Runs entirely on your device.",ask_placeholder:"e.g. notes about staying loyal under pressure",ask_go:"Search",ask_enable_title:"Turn on semantic search",ask_enable_body:"A small language model runs in your browser to understand your notes. It downloads once, is cached for offline use, and nothing ever leaves your device.",ask_model_fast_name:"Light (fastest)",ask_model_fast_desc:"3-layer model — about 2× faster than English and half the download. Perfect for large libraries.",ask_model_en_name:"English",ask_model_en_desc:"Standard accuracy for notes written in English.",ask_model_multi_name:"Multilingual",ask_model_multi_desc:"Understands 50+ languages — choose this if you write notes in more than one language.",ask_size_once:"~{n} MB · one-time",ask_privacy:"100% private — the model and your notes never leave this device.",ask_loading_model:"Downloading search model… {pct}%",ask_building:"Reading your notes… {done} / {total}",ask_ready:"Ready — ask a question above.",ask_searching:"Searching…",ask_results_head:"{n} most related notes",ask_no_results:"No related notes found. Try rephrasing your question.",ask_no_notes:"This library has no notes to search yet.",ask_err:"Couldn't load the search model. Check your connection and try again.",ask_rebuild:"Rebuild index",ask_match:"{pct}% match",batch_tagged_ok:"Tagged {n} notes",ask_switch_model:"Use a different model",change_file:"Change file"},
    es:{title:"Explorador de Estudio",search:"Buscar...",no_results:"Nada coincide con tus filtros.",loading:"Cargando biblioteca...",close:"Cerrar",no_file:"Abre primero un archivo de respaldo.",pick_file:"Elegir archivo .jwlibrary",count_one:"{n} elemento",count_many:"{n} elementos",color_all:"Todos los colores",no_title:"Sin título",copy:"Copiar",copied:"Copiado",clear:"Limpiar",error:"No se pudo cargar:",pub_all:"Todas las publicaciones",tag_all:"Todas las etiquetas",back:"← Volver",detail_empty:"Selecciona un elemento de la lista.",sort_newest:"Más recientes primero",sort_oldest:"Más antiguas primero",sort_pub:"Por publicación",modified:"Modificado",no_content:"(Sin contenido)",too_many:"Mostrando los primeros {n} de {total} — refina la búsqueda.",pg_prev:"Anterior",pg_next:"Siguiente",pg_status:"Página {page} de {pages} · {total} resultados",err_corrupt:"Este archivo no es una copia .jwlibrary legible: puede estar dañado o ser de tipo incorrecto.",err_no_db:"A esta copia le falta su base de datos de notas (userData.db). Vuelve a exportarla desde JW Library.",err_not_sqlite:"No se pudo abrir la base de datos de la copia: el archivo puede estar dañado.",tab_notes:"Notas",tab_highlights:"Resaltados",tab_bookmarks:"Marcadores",hl_label:"Resaltado",hl_no_text:"Pasaje resaltado (el texto está en la publicación, no en el respaldo).",hl_with_note:"Con nota",bm_label:"Marcador",bm_slot:"Posición {n}",linked_note:"Nota vinculada:",edit:"Editar",save:"Guardar",cancel:"Cancelar",delete_item:"Eliminar",export_db:"Exportar .jwlibrary",n_edits:"{n} edición",n_edits_many:"{n} ediciones",add_tag:"+ Agregar etiqueta",new_tag_ph:"Nombre de etiqueta...",delete_note_confirm:"¿Eliminar esta nota? Esta acción no se puede deshacer.",delete_hl_confirm:"¿Eliminar este resaltado? Esta acción no se puede deshacer.",delete_bm_confirm:"¿Eliminar este marcador? Esta acción no se puede deshacer.",yes_delete:"Sí, eliminar",change_color:"Color",unsaved_exit:"Tienes {n} edición(es) sin exportar. ¿Cerrar sin exportar?",title_label:"Título",content_label:"Contenido",tags_label:"Etiquetas",hl_color_label:"Color del resaltado",bm_title_label:"Título del marcador",plain_text_note:"El formato se simplifica a texto plano al guardar",rte_bold:"Negrita",rte_italic:"Cursiva",rte_underline:"Subrayado",rte_bullets:"Lista con viñetas",rich_text_note:"Edita con negrita, cursiva y listas — el formato se conserva",date_from:"Desde",date_to:"Hasta",date_range:"Filtrar por fecha",extract_range:"Extraer rango de fechas",extract_none:"Ninguna nota está en este rango de fechas.",extract_hint:"Guarda un nuevo .jwlibrary solo con las notas de este rango de fechas.",copy_md:"Copiar como Markdown",export_md:"Exportar Markdown",md_hint:"Descarga las notas mostradas como archivos Markdown (.zip)",sel_mode:"Seleccionar",sel_done:"Listo",sel_all:"Todo",sel_none:"Ninguno",sel_count:"{n} seleccionados",batch_tag:"Etiqueta",batch_color:"Color",batch_delete:"Eliminar",batch_delete_confirm:"¿Eliminar {n}? Puedes deshacer antes de exportar.",batch_tag_ph:"Nombre de etiqueta…",batch_add:"Agregar",undo:"Deshacer",redo:"Rehacer",tab_inputfields:"Respuestas",if_label:"Respuesta de estudio",if_question:"Pregunta",if_answer:"Tu respuesta",if_empty:"(Sin respuesta aún)",delete_if_confirm:"¿Eliminar esta respuesta de estudio? Puedes deshacer antes de exportar.",share_action:"Compartir",share_title:"Compartir notas",share_intro:"Esto crea un archivo que tú mismo entregas — no se sube nada. Contiene el texto de las notas, así que compártelo solo con personas de confianza.",share_count:"{n} notas",share_download:"Descargar archivo",share_copy:"Copiar",share_tag:"Compartido",receive_action:"Recibir",receive_title:"Recibir notas compartidas",receive_intro:"Pega el texto compartido o elige un archivo .jwshare.json que te enviaron.",receive_paste_ph:"Pega aquí las notas compartidas…",receive_choose:"Elegir archivo",receive_preview:"Vista previa",receive_invalid:"Esto no parece datos de notas compartidas válidos.",preview_readonly:"Vista previa",adopt:"Adoptar {n} en mi biblioteca",adopt_need_lib:"Abre primero un respaldo",adopted:"Se adoptaron {n} notas (con la etiqueta \"Compartido\").",open_share:"Compartir notas →",ask_btn:"Preguntar",ask_title:"Pregunta a tu biblioteca",ask_sub:"Busca tus notas por significado, no solo por palabras clave — pregunta en lenguaje natural y encuentra notas relacionadas aunque usen palabras distintas. Se ejecuta en tu dispositivo.",ask_placeholder:"p.ej. notas sobre mantener la lealtad bajo presión",ask_go:"Buscar",ask_enable_title:"Activar búsqueda semántica",ask_enable_body:"Un pequeño modelo de lenguaje se ejecuta en tu navegador para entender tus notas. Se descarga una vez, se guarda en caché para uso sin conexión y nada sale de tu dispositivo.",ask_model_fast_name:"Ligero (más rápido)",ask_model_fast_desc:"Modelo de 3 capas — unas 2× más rápido y con la mitad de descarga. Perfecto para bibliotecas grandes.",ask_model_en_name:"Inglés",ask_model_en_desc:"Precisión estándar para notas escritas en inglés.",ask_model_multi_name:"Multilingüe",ask_model_multi_desc:"Entiende más de 50 idiomas — elige este si escribes notas en más de un idioma.",ask_size_once:"~{n} MB · una vez",ask_privacy:"100% privado — el modelo y tus notas nunca salen de este dispositivo.",ask_loading_model:"Descargando modelo… {pct}%",ask_building:"Leyendo tus notas… {done} / {total}",ask_ready:"Listo — haz una pregunta arriba.",ask_searching:"Buscando…",ask_results_head:"{n} notas más relacionadas",ask_no_results:"No se encontraron notas relacionadas. Intenta reformular tu pregunta.",ask_no_notes:"Esta biblioteca aún no tiene notas para buscar.",ask_err:"No se pudo cargar el modelo. Verifica tu conexión e inténtalo de nuevo.",ask_rebuild:"Reconstruir índice",ask_match:"{pct}% de coincidencia",batch_tagged_ok:"{n} notas etiquetadas",ask_switch_model:"Usar un modelo diferente",change_file:"Cambiar archivo"},
    pt:{title:"Explorador de Estudo",search:"Pesquisar...",no_results:"Nada corresponde aos filtros.",loading:"Carregando biblioteca...",close:"Fechar",no_file:"Abra primeiro um arquivo de backup.",pick_file:"Escolher arquivo .jwlibrary",count_one:"{n} item",count_many:"{n} itens",color_all:"Todas as cores",no_title:"Sem título",copy:"Copiar",copied:"Copiado",clear:"Limpar",error:"Não foi possível carregar:",pub_all:"Todas as publicações",tag_all:"Todas as etiquetas",back:"← Voltar",detail_empty:"Selecione um item da lista.",sort_newest:"Mais recentes primeiro",sort_oldest:"Mais antigos primeiro",sort_pub:"Por publicação",modified:"Modificado",no_content:"(Sem conteúdo)",too_many:"Exibindo os primeiros {n} de {total} — refine a busca.",pg_prev:"Anterior",pg_next:"Próxima",pg_status:"Página {page} de {pages} · {total} resultados",err_corrupt:"Este arquivo não é um backup .jwlibrary legível — pode estar corrompido ou ser do tipo errado.",err_no_db:"Falta o banco de dados de notas (userData.db) neste backup. Exporte-o novamente no JW Library.",err_not_sqlite:"Não foi possível abrir o banco de dados do backup — o arquivo pode estar danificado.",tab_notes:"Notas",tab_highlights:"Marcações",tab_bookmarks:"Favoritos",hl_label:"Marcação",hl_no_text:"Trecho marcado (o texto está na publicação, não no backup).",hl_with_note:"Com nota",bm_label:"Favorito",bm_slot:"Posição {n}",linked_note:"Nota vinculada:",edit:"Editar",save:"Salvar",cancel:"Cancelar",delete_item:"Excluir",export_db:"Exportar .jwlibrary",n_edits:"{n} edição",n_edits_many:"{n} edições",add_tag:"+ Adicionar etiqueta",new_tag_ph:"Nome da etiqueta...",delete_note_confirm:"Excluir esta nota? Esta ação não pode ser desfeita.",delete_hl_confirm:"Excluir esta marcação? Esta ação não pode ser desfeita.",delete_bm_confirm:"Excluir este favorito? Esta ação não pode ser desfeita.",yes_delete:"Sim, excluir",change_color:"Cor",unsaved_exit:"Você tem {n} edição(ões) sem exportar. Fechar sem exportar?",title_label:"Título",content_label:"Conteúdo",tags_label:"Etiquetas",hl_color_label:"Cor da marcação",bm_title_label:"Título do favorito",plain_text_note:"Formatação simplificada para texto simples ao salvar",rte_bold:"Negrito",rte_italic:"Itálico",rte_underline:"Sublinhado",rte_bullets:"Lista com marcadores",rich_text_note:"Edite com negrito, itálico e listas — a formatação é mantida",date_from:"De",date_to:"Até",date_range:"Filtrar por data",extract_range:"Extrair intervalo de datas",extract_none:"Nenhuma nota está neste intervalo de datas.",extract_hint:"Salve um novo .jwlibrary apenas com as notas deste intervalo de datas.",copy_md:"Copiar como Markdown",export_md:"Exportar Markdown",md_hint:"Baixe as notas exibidas como arquivos Markdown (.zip)",sel_mode:"Selecionar",sel_done:"Concluir",sel_all:"Tudo",sel_none:"Nenhum",sel_count:"{n} selecionados",batch_tag:"Etiqueta",batch_color:"Cor",batch_delete:"Excluir",batch_delete_confirm:"Excluir {n}? Você pode desfazer antes de exportar.",batch_tag_ph:"Nome da etiqueta…",batch_add:"Adicionar",undo:"Desfazer",redo:"Refazer",tab_inputfields:"Respostas",if_label:"Resposta de estudo",if_question:"Pergunta",if_answer:"Sua resposta",if_empty:"(Sem resposta ainda)",delete_if_confirm:"Excluir esta resposta de estudo? Você pode desfazer antes de exportar.",share_action:"Compartilhar",share_title:"Compartilhar notas",share_intro:"Isto cria um arquivo que você mesmo entrega — nada é enviado. Ele contém o texto das notas, então compartilhe só com pessoas de confiança.",share_count:"{n} notas",share_download:"Baixar arquivo",share_copy:"Copiar",share_tag:"Compartilhado",receive_action:"Receber",receive_title:"Receber notas compartilhadas",receive_intro:"Cole o texto compartilhado ou escolha um arquivo .jwshare.json que enviaram a você.",receive_paste_ph:"Cole as notas compartilhadas aqui…",receive_choose:"Escolher arquivo",receive_preview:"Pré-visualizar",receive_invalid:"Isto não parece dados válidos de notas compartilhadas.",preview_readonly:"Pré-visualização",adopt:"Adotar {n} na minha biblioteca",adopt_need_lib:"Abra um backup primeiro",adopted:"{n} notas adotadas (com a etiqueta \"Compartilhado\").",open_share:"Compartilhar notas →",ask_btn:"Perguntar",ask_title:"Pergunte à sua biblioteca",ask_sub:"Pesquise suas notas por significado, não apenas por palavras-chave — pergunte em linguagem natural e encontre notas relacionadas mesmo que usem palavras diferentes. Executado inteiramente no seu dispositivo.",ask_placeholder:"ex. notas sobre manter a lealdade sob pressão",ask_go:"Pesquisar",ask_enable_title:"Ativar pesquisa semântica",ask_enable_body:"Um pequeno modelo de linguagem é executado no seu navegador para entender suas notas. É baixado uma vez, armazenado em cache para uso offline e nada sai do seu dispositivo.",ask_model_fast_name:"Leve (mais rápido)",ask_model_fast_desc:"Modelo de 3 camadas — cerca de 2× mais rápido e metade do download. Perfeito para bibliotecas grandes.",ask_model_en_name:"Inglês",ask_model_en_desc:"Precisão padrão para notas escritas em inglês.",ask_model_multi_name:"Multilíngue",ask_model_multi_desc:"Entende mais de 50 idiomas — escolha este se você escreve notas em mais de um idioma.",ask_size_once:"~{n} MB · uma vez",ask_privacy:"100% privado — o modelo e suas notas nunca saem deste dispositivo.",ask_loading_model:"Baixando modelo de pesquisa… {pct}%",ask_building:"Lendo suas notas… {done} / {total}",ask_ready:"Pronto — faça uma pergunta acima.",ask_searching:"Pesquisando…",ask_results_head:"{n} notas mais relacionadas",ask_no_results:"Nenhuma nota relacionada encontrada. Tente reformular sua pergunta.",ask_no_notes:"Esta biblioteca ainda não tem notas para pesquisar.",ask_err:"Não foi possível carregar o modelo. Verifique sua conexão e tente novamente.",ask_rebuild:"Reconstruir índice",ask_match:"{pct}% de correspondência",batch_tagged_ok:"{n} notas marcadas com tag",ask_switch_model:"Usar um modelo diferente",change_file:"Trocar arquivo"},
    fr:{title:"Explorateur d'étude",search:"Rechercher...",no_results:"Aucun résultat ne correspond.",loading:"Chargement de la bibliothèque...",close:"Fermer",no_file:"Ouvrez d'abord un fichier de sauvegarde.",pick_file:"Choisir un fichier .jwlibrary",count_one:"{n} élément",count_many:"{n} éléments",color_all:"Toutes les couleurs",no_title:"Sans titre",copy:"Copier",copied:"Copié",clear:"Effacer",error:"Impossible de charger :",pub_all:"Toutes les publications",tag_all:"Toutes les étiquettes",back:"← Retour",detail_empty:"Sélectionnez un élément dans la liste.",sort_newest:"Plus récents d'abord",sort_oldest:"Plus anciens d'abord",sort_pub:"Par publication",modified:"Modifié",no_content:"(Pas de contenu)",too_many:"Affichage des {n} premiers sur {total} — affinez la recherche.",pg_prev:"Préc.",pg_next:"Suiv.",pg_status:"Page {page} sur {pages} · {total} résultats",err_corrupt:"Ce fichier n'est pas une sauvegarde .jwlibrary lisible — il est peut-être corrompu ou d'un mauvais type.",err_no_db:"Cette sauvegarde n'a pas sa base de données de notes (userData.db). Réexportez-la depuis JW Library.",err_not_sqlite:"Impossible d'ouvrir la base de données de la sauvegarde — le fichier est peut-être endommagé.",tab_notes:"Notes",tab_highlights:"Surlignages",tab_bookmarks:"Signets",hl_label:"Surlignage",hl_no_text:"Passage surligné (le texte se trouve dans la publication, pas dans la sauvegarde).",hl_with_note:"Avec note",bm_label:"Signet",bm_slot:"Position {n}",linked_note:"Note liée :",edit:"Modifier",save:"Enregistrer",cancel:"Annuler",delete_item:"Supprimer",export_db:"Exporter .jwlibrary",n_edits:"{n} modification",n_edits_many:"{n} modifications",add_tag:"+ Ajouter étiquette",new_tag_ph:"Nom de l'étiquette...",delete_note_confirm:"Supprimer cette note ? Cette action est irréversible.",delete_hl_confirm:"Supprimer ce surlignage ? Cette action est irréversible.",delete_bm_confirm:"Supprimer ce signet ? Cette action est irréversible.",yes_delete:"Oui, supprimer",change_color:"Couleur",unsaved_exit:"Vous avez {n} modification(s) non exportée(s). Fermer sans exporter ?",title_label:"Titre",content_label:"Contenu",tags_label:"Étiquettes",hl_color_label:"Couleur du surlignage",bm_title_label:"Titre du signet",plain_text_note:"La mise en forme est simplifiée en texte brut lors de l'enregistrement",rte_bold:"Gras",rte_italic:"Italique",rte_underline:"Souligné",rte_bullets:"Liste à puces",rich_text_note:"Modifiez avec gras, italique et listes — la mise en forme est conservée",date_from:"Du",date_to:"Au",date_range:"Filtrer par date",extract_range:"Extraire la plage de dates",extract_none:"Aucune note dans cette plage de dates.",extract_hint:"Enregistrez un nouveau .jwlibrary avec seulement les notes de cette plage de dates.",copy_md:"Copier en Markdown",export_md:"Exporter Markdown",md_hint:"Téléchargez les notes affichées en fichiers Markdown (.zip)",sel_mode:"Sélectionner",sel_done:"Terminé",sel_all:"Tout",sel_none:"Aucun",sel_count:"{n} sélectionnés",batch_tag:"Étiquette",batch_color:"Couleur",batch_delete:"Supprimer",batch_delete_confirm:"Supprimer {n} ? Vous pouvez annuler avant l'export.",batch_tag_ph:"Nom de l'étiquette…",batch_add:"Ajouter",undo:"Annuler",redo:"Rétablir",tab_inputfields:"Réponses",if_label:"Réponse d'étude",if_question:"Question",if_answer:"Votre réponse",if_empty:"(Pas encore de réponse)",delete_if_confirm:"Supprimer cette réponse d'étude ? Vous pouvez annuler avant l'export.",share_action:"Partager",share_title:"Partager des notes",share_intro:"Cela crée un fichier que vous transmettez vous-même — rien n'est envoyé. Il contient le texte des notes, ne le partagez qu'avec des personnes de confiance.",share_count:"{n} notes",share_download:"Télécharger le fichier",share_copy:"Copier",share_tag:"Partagé",receive_action:"Recevoir",receive_title:"Recevoir des notes partagées",receive_intro:"Collez le texte partagé ou choisissez un fichier .jwshare.json qu'on vous a envoyé.",receive_paste_ph:"Collez les notes partagées ici…",receive_choose:"Choisir un fichier",receive_preview:"Aperçu",receive_invalid:"Cela ne ressemble pas à des données de notes partagées valides.",preview_readonly:"Aperçu",adopt:"Adopter {n} dans ma bibliothèque",adopt_need_lib:"Ouvrez d'abord une sauvegarde",adopted:"{n} notes adoptées (étiquetées \"Partagé\").",open_share:"Partager des notes →",ask_btn:"Demander",ask_title:"Interrogez votre bibliothèque",ask_sub:"Recherchez vos notes par sens, pas seulement par mots-clés — posez votre question en langage naturel et trouvez des notes liées même si elles utilisent des mots différents. Fonctionne entièrement sur votre appareil.",ask_placeholder:"ex. notes sur rester fidèle sous la pression",ask_go:"Rechercher",ask_enable_title:"Activer la recherche sémantique",ask_enable_body:"Un petit modèle de langage s'exécute dans votre navigateur pour comprendre vos notes. Il se télécharge une fois, est mis en cache pour une utilisation hors ligne et rien ne quitte votre appareil.",ask_model_fast_name:"Léger (le plus rapide)",ask_model_fast_desc:"Modèle à 3 couches — environ 2× plus rapide et moitié moins lourd. Parfait pour les grandes bibliothèques.",ask_model_en_name:"Anglais",ask_model_en_desc:"Précision standard pour les notes écrites en anglais.",ask_model_multi_name:"Multilingue",ask_model_multi_desc:"Comprend plus de 50 langues — choisissez ce modèle si vous écrivez des notes dans plusieurs langues.",ask_size_once:"~{n} Mo · une fois",ask_privacy:"100% privé — le modèle et vos notes ne quittent jamais cet appareil.",ask_loading_model:"Téléchargement du modèle… {pct}%",ask_building:"Lecture de vos notes… {done} / {total}",ask_ready:"Prêt — posez une question ci-dessus.",ask_searching:"Recherche en cours…",ask_results_head:"{n} notes les plus pertinentes",ask_no_results:"Aucune note liée trouvée. Essayez de reformuler votre question.",ask_no_notes:"Cette bibliothèque n'a pas encore de notes à rechercher.",ask_err:"Impossible de charger le modèle. Vérifiez votre connexion et réessayez.",ask_rebuild:"Reconstruire l'index",ask_match:"{pct}% de correspondance",batch_tagged_ok:"{n} notes étiquetées",ask_switch_model:"Utiliser un autre modèle",change_file:"Changer de fichier"},
    de:{title:"Studien-Explorer",search:"Suchen...",no_results:"Keine Treffer für die Filter.",loading:"Bibliothek wird geladen...",close:"Schließen",no_file:"Öffnen Sie zuerst eine Sicherungsdatei.",pick_file:".jwlibrary-Datei wählen",count_one:"{n} Eintrag",count_many:"{n} Einträge",color_all:"Alle Farben",no_title:"Ohne Titel",copy:"Kopieren",copied:"Kopiert",clear:"Zurücksetzen",error:"Konnte nicht geladen werden:",pub_all:"Alle Veröffentlichungen",tag_all:"Alle Stichwörter",back:"← Zurück",detail_empty:"Wählen Sie einen Eintrag aus der Liste.",sort_newest:"Neueste zuerst",sort_oldest:"Älteste zuerst",sort_pub:"Nach Veröffentlichung",modified:"Geändert",no_content:"(Kein Inhalt)",too_many:"Erste {n} von {total} angezeigt — Suche einschränken.",pg_prev:"Zurück",pg_next:"Weiter",pg_status:"Seite {page} von {pages} · {total} Ergebnisse",err_corrupt:"Diese Datei ist keine lesbare .jwlibrary-Sicherung — sie ist evtl. beschädigt oder vom falschen Typ.",err_no_db:"Dieser Sicherung fehlt ihre Notizdatenbank (userData.db). Exportiere sie erneut aus JW Library.",err_not_sqlite:"Die Datenbank der Sicherung konnte nicht geöffnet werden — die Datei ist evtl. beschädigt.",tab_notes:"Notizen",tab_highlights:"Markierungen",tab_bookmarks:"Lesezeichen",hl_label:"Markierung",hl_no_text:"Markierte Passage (Text liegt in der Veröffentlichung, nicht im Backup).",hl_with_note:"Mit Notiz",bm_label:"Lesezeichen",bm_slot:"Slot {n}",linked_note:"Verknüpfte Notiz:",edit:"Bearbeiten",save:"Speichern",cancel:"Abbrechen",delete_item:"Löschen",export_db:".jwlibrary exportieren",n_edits:"{n} Änderung",n_edits_many:"{n} Änderungen",add_tag:"+ Stichwort hinzufügen",new_tag_ph:"Stichwortname...",delete_note_confirm:"Diese Notiz löschen? Diese Aktion kann nicht rückgängig gemacht werden.",delete_hl_confirm:"Diese Markierung löschen? Diese Aktion kann nicht rückgängig gemacht werden.",delete_bm_confirm:"Dieses Lesezeichen löschen? Diese Aktion kann nicht rückgängig gemacht werden.",yes_delete:"Ja, löschen",change_color:"Farbe",unsaved_exit:"Sie haben {n} nicht exportierte Änderung(en). Ohne Export schließen?",title_label:"Titel",content_label:"Inhalt",tags_label:"Stichwörter",hl_color_label:"Markierungsfarbe",bm_title_label:"Lesezeichentitel",plain_text_note:"Formatierung wird beim Speichern auf Nur-Text vereinfacht",rte_bold:"Fett",rte_italic:"Kursiv",rte_underline:"Unterstrichen",rte_bullets:"Aufzählung",rich_text_note:"Mit Fett, Kursiv und Listen bearbeiten — Formatierung bleibt erhalten",date_from:"Von",date_to:"Bis",date_range:"Nach Datum filtern",extract_range:"Datumsbereich extrahieren",extract_none:"Keine Notizen in diesem Datumsbereich.",extract_hint:"Ein neues .jwlibrary nur mit den Notizen dieses Datumsbereichs speichern.",copy_md:"Als Markdown kopieren",export_md:"Markdown exportieren",md_hint:"Die angezeigten Notizen als Markdown-Dateien herunterladen (.zip)",sel_mode:"Auswählen",sel_done:"Fertig",sel_all:"Alle",sel_none:"Keine",sel_count:"{n} ausgewählt",batch_tag:"Stichwort",batch_color:"Farbe",batch_delete:"Löschen",batch_delete_confirm:"{n} löschen? Du kannst vor dem Export rückgängig machen.",batch_tag_ph:"Stichwortname…",batch_add:"Hinzufügen",undo:"Rückgängig",redo:"Wiederholen",tab_inputfields:"Antworten",if_label:"Studienantwort",if_question:"Frage",if_answer:"Deine Antwort",if_empty:"(Noch keine Antwort)",delete_if_confirm:"Diese Studienantwort löschen? Du kannst vor dem Export rückgängig machen.",share_action:"Teilen",share_title:"Notizen teilen",share_intro:"Das erstellt eine Datei, die du selbst weitergibst — nichts wird hochgeladen. Sie enthält den Notiztext, teile sie also nur mit vertrauenswürdigen Personen.",share_count:"{n} Notizen",share_download:"Datei herunterladen",share_copy:"Kopieren",share_tag:"Geteilt",receive_action:"Empfangen",receive_title:"Geteilte Notizen empfangen",receive_intro:"Füge geteilten Text ein oder wähle eine .jwshare.json-Datei, die dir jemand geschickt hat.",receive_paste_ph:"Geteilte Notizen hier einfügen…",receive_choose:"Datei wählen",receive_preview:"Vorschau",receive_invalid:"Das sehen nicht nach gültigen geteilten Notizdaten aus.",preview_readonly:"Vorschau",adopt:"{n} in meine Bibliothek übernehmen",adopt_need_lib:"Öffne zuerst ein Backup",adopted:"{n} Notizen übernommen (mit Stichwort \"Geteilt\").",open_share:"Notizen teilen →",ask_btn:"Fragen",ask_title:"Frag deine Bibliothek",ask_sub:"Suche deine Notizen nach Bedeutung, nicht nur nach Schlüsselwörtern — stelle eine Frage in natürlicher Sprache und finde verwandte Notizen, auch wenn sie andere Wörter verwenden. Läuft vollständig auf deinem Gerät.",ask_placeholder:"z.B. Notizen über Treue unter Druck",ask_go:"Suchen",ask_enable_title:"Semantische Suche aktivieren",ask_enable_body:"Ein kleines Sprachmodell läuft in deinem Browser, um deine Notizen zu verstehen. Es wird einmal heruntergeladen, für die Offline-Nutzung zwischengespeichert und nichts verlässt dein Gerät.",ask_model_fast_name:"Leicht (am schnellsten)",ask_model_fast_desc:"Drei-Schicht-Modell — ca. 2× schneller und halb so groß. Ideal für große Bibliotheken.",ask_model_en_name:"Englisch",ask_model_en_desc:"Standardgenauigkeit für Notizen auf Englisch.",ask_model_multi_name:"Mehrsprachig",ask_model_multi_desc:"Versteht über 50 Sprachen — wähle dieses Modell, wenn du Notizen in mehreren Sprachen schreibst.",ask_size_once:"~{n} MB · einmalig",ask_privacy:"100% privat — das Modell und deine Notizen verlassen dieses Gerät nie.",ask_loading_model:"Suchmodell wird heruntergeladen… {pct}%",ask_building:"Notizen werden gelesen… {done} / {total}",ask_ready:"Bereit — stelle oben eine Frage.",ask_searching:"Suche läuft…",ask_results_head:"{n} verwandteste Notizen",ask_no_results:"Keine verwandten Notizen gefunden. Versuche, deine Frage umzuformulieren.",ask_no_notes:"Diese Bibliothek hat noch keine Notizen zum Durchsuchen.",ask_err:"Modell konnte nicht geladen werden. Überprüfe deine Verbindung und versuche es erneut.",ask_rebuild:"Index neu erstellen",ask_match:"{pct}% Übereinstimmung",batch_tagged_ok:"{n} Notizen getaggt",ask_switch_model:"Anderes Modell verwenden",change_file:"Datei wechseln"},
    it:{title:"Esplora Studio",search:"Cerca...",no_results:"Nessun risultato per i filtri.",loading:"Caricamento biblioteca...",close:"Chiudi",no_file:"Apri prima un file di backup.",pick_file:"Scegli file .jwlibrary",count_one:"{n} elemento",count_many:"{n} elementi",color_all:"Tutti i colori",no_title:"Senza titolo",copy:"Copia",copied:"Copiato",clear:"Cancella",error:"Impossibile caricare:",pub_all:"Tutte le pubblicazioni",tag_all:"Tutte le etichette",back:"← Indietro",detail_empty:"Seleziona un elemento dall'elenco.",sort_newest:"Più recenti prima",sort_oldest:"Più vecchi prima",sort_pub:"Per pubblicazione",modified:"Modificato",no_content:"(Nessun contenuto)",too_many:"Mostrati i primi {n} di {total} — restringi la ricerca.",pg_prev:"Prec.",pg_next:"Succ.",pg_status:"Pagina {page} di {pages} · {total} risultati",err_corrupt:"Questo file non è un backup .jwlibrary leggibile — potrebbe essere danneggiato o di tipo errato.",err_no_db:"A questo backup manca il database delle note (userData.db). Riesportalo da JW Library.",err_not_sqlite:"Non è stato possibile aprire il database del backup — il file potrebbe essere danneggiato.",tab_notes:"Note",tab_highlights:"Evidenziazioni",tab_bookmarks:"Segnalibri",hl_label:"Evidenziazione",hl_no_text:"Brano evidenziato (il testo è nella pubblicazione, non nel backup).",hl_with_note:"Con nota",bm_label:"Segnalibro",bm_slot:"Posizione {n}",linked_note:"Nota collegata:",edit:"Modifica",save:"Salva",cancel:"Annulla",delete_item:"Elimina",export_db:"Esporta .jwlibrary",n_edits:"{n} modifica",n_edits_many:"{n} modifiche",add_tag:"+ Aggiungi etichetta",new_tag_ph:"Nome etichetta...",delete_note_confirm:"Eliminare questa nota? Questa azione non può essere annullata.",delete_hl_confirm:"Eliminare questa evidenziazione? Questa azione non può essere annullata.",delete_bm_confirm:"Eliminare questo segnalibro? Questa azione non può essere annullata.",yes_delete:"Sì, elimina",change_color:"Colore",unsaved_exit:"Hai {n} modifica/modifiche non esportata/e. Chiudere senza esportare?",title_label:"Titolo",content_label:"Contenuto",tags_label:"Etichette",hl_color_label:"Colore evidenziazione",bm_title_label:"Titolo segnalibro",plain_text_note:"La formattazione verrà semplificata a testo normale al salvataggio",rte_bold:"Grassetto",rte_italic:"Corsivo",rte_underline:"Sottolineato",rte_bullets:"Elenco puntato",rich_text_note:"Modifica con grassetto, corsivo ed elenchi — la formattazione è mantenuta",date_from:"Dal",date_to:"Al",date_range:"Filtra per data",extract_range:"Estrai intervallo di date",extract_none:"Nessuna nota in questo intervallo di date.",extract_hint:"Salva un nuovo .jwlibrary solo con le note di questo intervallo di date.",copy_md:"Copia come Markdown",export_md:"Esporta Markdown",md_hint:"Scarica le note mostrate come file Markdown (.zip)",sel_mode:"Seleziona",sel_done:"Fatto",sel_all:"Tutto",sel_none:"Nessuno",sel_count:"{n} selezionati",batch_tag:"Etichetta",batch_color:"Colore",batch_delete:"Elimina",batch_delete_confirm:"Eliminare {n}? Puoi annullare prima di esportare.",batch_tag_ph:"Nome etichetta…",batch_add:"Aggiungi",undo:"Annulla",redo:"Ripeti",tab_inputfields:"Risposte",if_label:"Risposta di studio",if_question:"Domanda",if_answer:"La tua risposta",if_empty:"(Ancora nessuna risposta)",delete_if_confirm:"Eliminare questa risposta di studio? Puoi annullare prima di esportare.",share_action:"Condividi",share_title:"Condividi note",share_intro:"Questo crea un file che consegni tu stesso — niente viene caricato. Contiene il testo delle note, quindi condividilo solo con persone fidate.",share_count:"{n} note",share_download:"Scarica file",share_copy:"Copia",share_tag:"Condiviso",receive_action:"Ricevi",receive_title:"Ricevi note condivise",receive_intro:"Incolla il testo condiviso o scegli un file .jwshare.json che ti hanno inviato.",receive_paste_ph:"Incolla qui le note condivise…",receive_choose:"Scegli file",receive_preview:"Anteprima",receive_invalid:"Questi non sembrano dati di note condivise validi.",preview_readonly:"Anteprima",adopt:"Adotta {n} nella mia biblioteca",adopt_need_lib:"Apri prima un backup",adopted:"Adottate {n} note (con etichetta \"Condiviso\").",open_share:"Condividi note →",ask_btn:"Chiedi",ask_title:"Interroga la tua biblioteca",ask_sub:"Cerca nelle tue note per significato, non solo per parole chiave — fai una domanda in linguaggio naturale e trova note correlate anche se usano parole diverse. Funziona interamente sul tuo dispositivo.",ask_placeholder:"es. note su rimanere fedeli sotto pressione",ask_go:"Cerca",ask_enable_title:"Attiva la ricerca semantica",ask_enable_body:"Un piccolo modello linguistico viene eseguito nel tuo browser per comprendere le tue note. Viene scaricato una volta, memorizzato nella cache per l'uso offline e nulla lascia mai il tuo dispositivo.",ask_model_fast_name:"Leggero (più veloce)",ask_model_fast_desc:"Modello a 3 strati — circa 2× più veloce e metà del download. Perfetto per biblioteche grandi.",ask_model_en_name:"Inglese",ask_model_en_desc:"Precisione standard per note scritte in inglese.",ask_model_multi_name:"Multilingue",ask_model_multi_desc:"Comprende oltre 50 lingue — scegli questo se scrivi note in più di una lingua.",ask_size_once:"~{n} MB · una volta",ask_privacy:"100% privato — il modello e le tue note non lasciano mai questo dispositivo.",ask_loading_model:"Download del modello di ricerca… {pct}%",ask_building:"Lettura delle note… {done} / {total}",ask_ready:"Pronto — fai una domanda sopra.",ask_searching:"Ricerca in corso…",ask_results_head:"{n} note più correlate",ask_no_results:"Nessuna nota correlata trovata. Prova a riformulare la domanda.",ask_no_notes:"Questa biblioteca non ha ancora note da cercare.",ask_err:"Impossibile caricare il modello. Controlla la connessione e riprova.",ask_rebuild:"Ricostruisci indice",ask_match:"{pct}% di corrispondenza",batch_tagged_ok:"{n} note con tag aggiunto",ask_switch_model:"Usa un modello diverso",change_file:"Cambia file"},
    ru:{title:"Изучение заметок",search:"Поиск...",no_results:"Ничего не найдено.",loading:"Загрузка библиотеки...",close:"Закрыть",no_file:"Сначала откройте файл резервной копии.",pick_file:"Выбрать .jwlibrary файл",count_one:"{n} элемент",count_many:"{n} элементов",color_all:"Все цвета",no_title:"Без названия",copy:"Копировать",copied:"Скопировано",clear:"Очистить",error:"Не удалось загрузить:",pub_all:"Все публикации",tag_all:"Все теги",back:"← Назад",detail_empty:"Выберите элемент из списка.",sort_newest:"Сначала новые",sort_oldest:"Сначала старые",sort_pub:"По публикации",modified:"Изменено",no_content:"(Нет содержимого)",too_many:"Показаны первые {n} из {total} — уточните поиск.",pg_prev:"Назад",pg_next:"Вперёд",pg_status:"Страница {page} из {pages} · {total} результатов",err_corrupt:"Этот файл не является читаемой копией .jwlibrary — возможно, он повреждён или это другой тип файла.",err_no_db:"В этой копии нет базы данных заметок (userData.db). Экспортируйте её заново из JW Library.",err_not_sqlite:"Не удалось открыть базу данных копии — файл может быть повреждён.",tab_notes:"Заметки",tab_highlights:"Пометки",tab_bookmarks:"Закладки",hl_label:"Пометка",hl_no_text:"Выделенный отрывок (текст находится в публикации, а не в копии).",hl_with_note:"С заметкой",bm_label:"Закладка",bm_slot:"Слот {n}",linked_note:"Связанная заметка:",edit:"Изменить",save:"Сохранить",cancel:"Отмена",delete_item:"Удалить",export_db:"Экспорт .jwlibrary",n_edits:"{n} изм.",n_edits_many:"{n} изм.",add_tag:"+ Добавить тег",new_tag_ph:"Название тега...",delete_note_confirm:"Удалить эту заметку? Это действие нельзя отменить.",delete_hl_confirm:"Удалить эту пометку? Это действие нельзя отменить.",delete_bm_confirm:"Удалить эту закладку? Это действие нельзя отменить.",yes_delete:"Да, удалить",change_color:"Цвет",unsaved_exit:"У вас {n} неэкспортированное(ых) изменение(й). Закрыть без экспорта?",title_label:"Название",content_label:"Содержание",tags_label:"Теги",hl_color_label:"Цвет пометки",bm_title_label:"Название закладки",plain_text_note:"Форматирование упрощается до простого текста при сохранении",rte_bold:"Жирный",rte_italic:"Курсив",rte_underline:"Подчёркнутый",rte_bullets:"Маркированный список",rich_text_note:"Редактируйте с жирным, курсивом и списками — форматирование сохраняется",date_from:"С",date_to:"По",date_range:"Фильтр по дате",extract_range:"Извлечь диапазон дат",extract_none:"Нет заметок в этом диапазоне дат.",extract_hint:"Сохранить новый .jwlibrary только с заметками этого диапазона дат.",copy_md:"Копировать как Markdown",export_md:"Экспорт Markdown",md_hint:"Скачать показанные заметки как файлы Markdown (.zip)",sel_mode:"Выбрать",sel_done:"Готово",sel_all:"Все",sel_none:"Ничего",sel_count:"Выбрано: {n}",batch_tag:"Тег",batch_color:"Цвет",batch_delete:"Удалить",batch_delete_confirm:"Удалить {n}? Можно отменить до экспорта.",batch_tag_ph:"Название тега…",batch_add:"Добавить",undo:"Отменить",redo:"Повторить",tab_inputfields:"Ответы",if_label:"Ответ для изучения",if_question:"Вопрос",if_answer:"Ваш ответ",if_empty:"(Пока нет ответа)",delete_if_confirm:"Удалить этот ответ? Можно отменить до экспорта.",share_action:"Поделиться",share_title:"Поделиться заметками",share_intro:"Это создаёт файл, который вы передаёте сами — ничего не загружается. Он содержит текст заметок, поэтому делитесь только с теми, кому доверяете.",share_count:"{n} заметок",share_download:"Скачать файл",share_copy:"Копировать",share_tag:"Общие",receive_action:"Получить",receive_title:"Получить общие заметки",receive_intro:"Вставьте присланный текст или выберите файл .jwshare.json.",receive_paste_ph:"Вставьте сюда общие заметки…",receive_choose:"Выбрать файл",receive_preview:"Предпросмотр",receive_invalid:"Это не похоже на корректные данные общих заметок.",preview_readonly:"Предпросмотр",adopt:"Добавить {n} в мою библиотеку",adopt_need_lib:"Сначала откройте копию",adopted:"Добавлено заметок: {n} (с меткой \"Общие\").",open_share:"Поделиться →",ask_btn:"Спросить",ask_title:"Спросите свою библиотеку",ask_sub:"Ищите заметки по смыслу, а не только по ключевым словам — задайте вопрос на естественном языке и найдите связанные заметки, даже если они используют другие слова. Работает полностью на вашем устройстве.",ask_placeholder:"напр. заметки о сохранении верности под давлением",ask_go:"Искать",ask_enable_title:"Включить семантический поиск",ask_enable_body:"Небольшая языковая модель запускается в вашем браузере для понимания ваших заметок. Загружается один раз, кэшируется для использования без интернета, и ничего не покидает ваше устройство.",ask_model_fast_name:"Лёгкая (быстрее всего)",ask_model_fast_desc:"Модель из 3 слоёв — примерно в 2× быстрее и вдвое меньше по размеру. Идеально для больших библиотек.",ask_model_en_name:"Английская",ask_model_en_desc:"Стандартная точность для заметок на английском языке.",ask_model_multi_name:"Многоязычная",ask_model_multi_desc:"Понимает более 50 языков — выберите, если вы пишете заметки на нескольких языках.",ask_size_once:"~{n} МБ · один раз",ask_privacy:"100% конфиденциально — модель и ваши заметки никогда не покидают это устройство.",ask_loading_model:"Загрузка модели поиска… {pct}%",ask_building:"Чтение заметок… {done} / {total}",ask_ready:"Готово — задайте вопрос выше.",ask_searching:"Поиск…",ask_results_head:"{n} наиболее связанных заметок",ask_no_results:"Связанных заметок не найдено. Попробуйте переформулировать вопрос.",ask_no_notes:"В этой библиотеке пока нет заметок для поиска.",ask_err:"Не удалось загрузить модель. Проверьте подключение и попробуйте снова.",ask_rebuild:"Пересоздать индекс",ask_match:"{pct}% совпадение",batch_tagged_ok:"Тег добавлен к {n} заметкам",ask_switch_model:"Использовать другую модель",change_file:"Сменить файл"},
    ja:{title:"学習ノート",search:"検索...",no_results:"フィルターに一致する項目はありません。",loading:"ライブラリを読み込み中...",close:"閉じる",no_file:"先にバックアップファイルを開いてください。",pick_file:".jwlibrary ファイルを選択",count_one:"{n} 件",count_many:"{n} 件",color_all:"すべての色",no_title:"タイトルなし",copy:"コピー",copied:"コピーしました",clear:"クリア",error:"読み込めませんでした:",pub_all:"すべての出版物",tag_all:"すべてのタグ",back:"← 戻る",detail_empty:"リストから項目を選択してください。",sort_newest:"新しい順",sort_oldest:"古い順",sort_pub:"出版物別",modified:"更新日",no_content:"(内容なし)",too_many:"{total} 件中 {n} 件を表示 — 検索を絞ってください。",pg_prev:"前へ",pg_next:"次へ",pg_status:"{pages} ページ中 {page} ページ · {total} 件",err_corrupt:"このファイルは読み取り可能な .jwlibrary バックアップではありません。破損しているか種類が違う可能性があります。",err_no_db:"このバックアップにはノートのデータベース（userData.db）がありません。JW Library から再書き出ししてください。",err_not_sqlite:"バックアップのデータベースを開けませんでした。ファイルが破損している可能性があります。",tab_notes:"ノート",tab_highlights:"ハイライト",tab_bookmarks:"しおり",hl_label:"ハイライト",hl_no_text:"ハイライトした箇所(テキストは出版物にあり、バックアップには含まれません)。",hl_with_note:"ノート付き",bm_label:"しおり",bm_slot:"スロット {n}",linked_note:"関連ノート:",edit:"編集",save:"保存",cancel:"キャンセル",delete_item:"削除",export_db:".jwlibrary を書き出し",n_edits:"{n}件の編集",n_edits_many:"{n}件の編集",add_tag:"+ タグを追加",new_tag_ph:"タグ名...",delete_note_confirm:"このノートを削除しますか？この操作は取り消せません。",delete_hl_confirm:"このハイライトを削除しますか？この操作は取り消せません。",delete_bm_confirm:"このしおりを削除しますか？この操作は取り消せません。",yes_delete:"はい、削除",change_color:"色",unsaved_exit:"{n}件の未エクスポートの編集があります。エクスポートせずに閉じますか？",title_label:"タイトル",content_label:"内容",tags_label:"タグ",hl_color_label:"ハイライトの色",bm_title_label:"しおりのタイトル",plain_text_note:"保存時にプレーンテキストに変換されます",rte_bold:"太字",rte_italic:"斜体",rte_underline:"下線",rte_bullets:"箇条書き",rich_text_note:"太字・斜体・リストで編集できます。書式は保持されます",date_from:"開始",date_to:"終了",date_range:"日付で絞り込み",extract_range:"日付範囲を抽出",extract_none:"この日付範囲にノートはありません。",extract_hint:"この日付範囲のノートだけを含む新しい .jwlibrary を保存します。",copy_md:"Markdown としてコピー",export_md:"Markdown を書き出し",md_hint:"表示中のノートを Markdown ファイル（.zip）としてダウンロード",sel_mode:"選択",sel_done:"完了",sel_all:"すべて",sel_none:"解除",sel_count:"{n} 件選択",batch_tag:"タグ",batch_color:"色",batch_delete:"削除",batch_delete_confirm:"{n} 件を削除？書き出し前に元に戻せます。",batch_tag_ph:"タグ名…",batch_add:"追加",undo:"元に戻す",redo:"やり直し",tab_inputfields:"回答",if_label:"学習の回答",if_question:"質問",if_answer:"あなたの回答",if_empty:"(まだ回答がありません)",delete_if_confirm:"この学習の回答を削除？書き出し前に元に戻せます。",share_action:"共有",share_title:"ノートを共有",share_intro:"これは自分で渡すファイルを作るだけです。アップロードはされません。ノートの本文が含まれるので、信頼できる人とだけ共有してください。",share_count:"{n} 件のノート",share_download:"ファイルをダウンロード",share_copy:"コピー",share_tag:"共有",receive_action:"受け取る",receive_title:"共有されたノートを受け取る",receive_intro:"共有テキストを貼り付けるか、送られた .jwshare.json ファイルを選択してください。",receive_paste_ph:"共有されたノートをここに貼り付け…",receive_choose:"ファイルを選択",receive_preview:"プレビュー",receive_invalid:"有効な共有ノートのデータではないようです。",preview_readonly:"プレビュー",adopt:"{n} 件を自分のライブラリに取り込む",adopt_need_lib:"先にバックアップを開いてください",adopted:"{n} 件のノートを取り込みました（「共有」タグ付き）。",open_share:"ノートを共有 →",ask_btn:"質問",ask_title:"ライブラリに質問",ask_sub:"キーワードだけでなく意味でノートを検索 — 自然な言葉で質問し、異なる表現を使ったノートも見つかります。すべてデバイス内で動作します。",ask_placeholder:"例：圧力の下での忠誠について",ask_go:"検索",ask_enable_title:"セマンティック検索を有効にする",ask_enable_body:"小さな言語モデルがブラウザ内で動作し、ノートを理解します。一度だけダウンロードしてキャッシュするため、オフラインでも使用でき、データはデバイス外に出ません。",ask_model_fast_name:"軽量（最速）",ask_model_fast_desc:"3層モデル — 英語の約2倍高速でダウンロードも半分。大規模ライブラリに最適。",ask_model_en_name:"英語",ask_model_en_desc:"英語で書かれたノートの標準精度。",ask_model_multi_name:"多言語",ask_model_multi_desc:"50以上の言語を理解 — 複数の言語でノートを書く方に。",ask_size_once:"~{n} MB · 1回限り",ask_privacy:"100%プライベート — モデルとノートはこのデバイスから出ません。",ask_loading_model:"検索モデルをダウンロード中… {pct}%",ask_building:"ノートを読み込み中… {done} / {total}",ask_ready:"準備完了 — 上に質問を入力してください。",ask_searching:"検索中…",ask_results_head:"最も関連性の高い{n}件のノート",ask_no_results:"関連するノートが見つかりませんでした。質問を言い換えてみてください。",ask_no_notes:"このライブラリにはまだ検索できるノートがありません。",ask_err:"モデルを読み込めませんでした。接続を確認してもう一度試してください。",ask_rebuild:"インデックスを再構築",ask_match:"{pct}%一致",batch_tagged_ok:"{n}件にタグを追加",ask_switch_model:"別のモデルを使用",change_file:"ファイルを変更"},
    ko:{title:"학습 탐색기",search:"검색...",no_results:"필터와 일치하는 항목이 없습니다.",loading:"라이브러리 로드 중...",close:"닫기",no_file:"먼저 백업 파일을 여세요.",pick_file:".jwlibrary 파일 선택",count_one:"{n}개",count_many:"{n}개",color_all:"모든 색상",no_title:"제목 없음",copy:"복사",copied:"복사됨",clear:"초기화",error:"불러올 수 없습니다:",pub_all:"모든 출판물",tag_all:"모든 태그",back:"← 뒤로",detail_empty:"목록에서 항목을 선택하세요.",sort_newest:"최신순",sort_oldest:"오래된순",sort_pub:"출판물순",modified:"수정됨",no_content:"(내용 없음)",too_many:"전체 {total}개 중 처음 {n}개 표시 — 검색을 좁히세요.",pg_prev:"이전",pg_next:"다음",pg_status:"{pages}페이지 중 {page}페이지 · {total}개",err_corrupt:"이 파일은 읽을 수 있는 .jwlibrary 백업이 아닙니다. 손상되었거나 잘못된 형식일 수 있습니다.",err_no_db:"이 백업에는 노트 데이터베이스(userData.db)가 없습니다. JW Library에서 다시 내보내세요.",err_not_sqlite:"백업의 데이터베이스를 열 수 없습니다. 파일이 손상되었을 수 있습니다.",tab_notes:"노트",tab_highlights:"하이라이트",tab_bookmarks:"북마크",hl_label:"하이라이트",hl_no_text:"하이라이트된 구절 (텍스트는 출판물에 있고 백업에는 포함되지 않음).",hl_with_note:"노트 포함",bm_label:"북마크",bm_slot:"슬롯 {n}",linked_note:"연결된 노트:",edit:"편집",save:"저장",cancel:"취소",delete_item:"삭제",export_db:".jwlibrary 내보내기",n_edits:"{n}개 편집",n_edits_many:"{n}개 편집",add_tag:"+ 태그 추가",new_tag_ph:"태그 이름...",delete_note_confirm:"이 노트를 삭제할까요? 이 작업은 취소할 수 없습니다.",delete_hl_confirm:"이 하이라이트를 삭제할까요? 이 작업은 취소할 수 없습니다.",delete_bm_confirm:"이 북마크를 삭제할까요? 이 작업은 취소할 수 없습니다.",yes_delete:"예, 삭제",change_color:"색상",unsaved_exit:"{n}개의 내보내지 않은 편집이 있습니다. 내보내지 않고 닫을까요?",title_label:"제목",content_label:"내용",tags_label:"태그",hl_color_label:"하이라이트 색상",bm_title_label:"북마크 제목",plain_text_note:"저장 시 서식이 일반 텍스트로 변환됩니다",rte_bold:"굵게",rte_italic:"기울임",rte_underline:"밑줄",rte_bullets:"글머리 기호 목록",rich_text_note:"굵게, 기울임, 목록으로 편집 — 서식이 유지됩니다",date_from:"시작",date_to:"종료",date_range:"날짜로 필터",extract_range:"날짜 범위 추출",extract_none:"이 날짜 범위에 노트가 없습니다.",extract_hint:"이 날짜 범위의 노트만 포함된 새 .jwlibrary를 저장합니다.",copy_md:"Markdown으로 복사",export_md:"Markdown 내보내기",md_hint:"표시된 노트를 Markdown 파일(.zip)로 다운로드",sel_mode:"선택",sel_done:"완료",sel_all:"전체",sel_none:"해제",sel_count:"{n}개 선택",batch_tag:"태그",batch_color:"색상",batch_delete:"삭제",batch_delete_confirm:"{n}개 삭제? 내보내기 전에 실행 취소할 수 있습니다.",batch_tag_ph:"태그 이름…",batch_add:"추가",undo:"실행 취소",redo:"다시 실행",tab_inputfields:"답변",if_label:"학습 답변",if_question:"질문",if_answer:"내 답변",if_empty:"(아직 답변 없음)",delete_if_confirm:"이 학습 답변을 삭제할까요? 내보내기 전에 실행 취소할 수 있습니다.",share_action:"공유",share_title:"노트 공유",share_intro:"직접 전달하는 파일을 만듭니다 — 아무것도 업로드되지 않습니다. 노트 내용이 들어 있으니 신뢰하는 사람과만 공유하세요.",share_count:"{n}개 노트",share_download:"파일 다운로드",share_copy:"복사",share_tag:"공유됨",receive_action:"받기",receive_title:"공유된 노트 받기",receive_intro:"공유된 텍스트를 붙여넣거나 받은 .jwshare.json 파일을 선택하세요.",receive_paste_ph:"공유된 노트를 여기에 붙여넣기…",receive_choose:"파일 선택",receive_preview:"미리보기",receive_invalid:"올바른 공유 노트 데이터가 아닌 것 같습니다.",preview_readonly:"미리보기",adopt:"{n}개를 내 라이브러리에 추가",adopt_need_lib:"먼저 백업을 여세요",adopted:"{n}개 노트를 추가했습니다(\"공유됨\" 태그).",open_share:"노트 공유 →",ask_btn:"질문",ask_title:"라이브러리에 질문하기",ask_sub:"키워드가 아닌 의미로 노트를 검색하세요 — 자연스러운 언어로 질문하면 다른 단어를 사용한 노트도 찾을 수 있습니다. 기기에서 완전히 실행됩니다.",ask_placeholder:"예: 압박 아래서 충성을 유지하는 것에 대한 노트",ask_go:"검색",ask_enable_title:"시맨틱 검색 활성화",ask_enable_body:"소형 언어 모델이 브라우저에서 실행되어 노트를 이해합니다. 한 번만 다운로드되어 오프라인 사용을 위해 캐시되며 아무것도 기기를 떠나지 않습니다.",ask_model_fast_name:"경량 (가장 빠름)",ask_model_fast_desc:"3층 모델 — 영어보다 약 2배 빠르고 다운로드 크기가 절반. 대용량 라이브러리에 적합.",ask_model_en_name:"영어",ask_model_en_desc:"영어로 작성된 노트의 표준 정확도.",ask_model_multi_name:"다국어",ask_model_multi_desc:"50개 이상의 언어를 이해합니다 — 여러 언어로 노트를 작성하는 경우 선택하세요.",ask_size_once:"~{n} MB · 1회",ask_privacy:"100% 비공개 — 모델과 노트는 이 기기를 벗어나지 않습니다.",ask_loading_model:"검색 모델 다운로드 중… {pct}%",ask_building:"노트 읽는 중… {done} / {total}",ask_ready:"준비 완료 — 위에 질문을 입력하세요.",ask_searching:"검색 중…",ask_results_head:"가장 관련성 높은 {n}개 노트",ask_no_results:"관련 노트를 찾지 못했습니다. 질문을 다시 표현해 보세요.",ask_no_notes:"이 라이브러리에는 아직 검색할 노트가 없습니다.",ask_err:"모델을 불러올 수 없습니다. 연결을 확인하고 다시 시도하세요.",ask_rebuild:"인덱스 재구성",ask_match:"{pct}% 일치",batch_tagged_ok:"{n}개 노트에 태그 추가됨",ask_switch_model:"다른 모델 사용",change_file:"파일 변경"},
    tl:{title:"Study Explorer",search:"Maghanap...",no_results:"Walang tumugma sa mga filter.",loading:"Naglo-load ng aklatan...",close:"Isara",no_file:"Magbukas muna ng backup file.",pick_file:"Pumili ng .jwlibrary file",count_one:"{n} item",count_many:"{n} item",color_all:"Lahat ng kulay",no_title:"Walang pamagat",copy:"Kopyahin",copied:"Nakopya",clear:"Burahin",error:"Hindi ma-load:",pub_all:"Lahat ng publikasyon",tag_all:"Lahat ng tag",back:"← Bumalik",detail_empty:"Pumili ng item mula sa listahan.",sort_newest:"Pinakabago muna",sort_oldest:"Pinakaluma muna",sort_pub:"Ayon sa publikasyon",modified:"Binago",no_content:"(Walang nilalaman)",too_many:"Ipinapakita ang unang {n} sa {total} — paliitin ang paghahanap.",pg_prev:"Nakaraan",pg_next:"Susunod",pg_status:"Pahina {page} ng {pages} · {total} resulta",err_corrupt:"Ang file na ito ay hindi nababasang .jwlibrary backup — maaaring sira o maling uri.",err_no_db:"Walang database ng mga nota (userData.db) ang backup na ito. I-export muli mula sa JW Library.",err_not_sqlite:"Hindi mabuksan ang database ng backup — maaaring sira ang file.",tab_notes:"Mga Tala",tab_highlights:"Mga Highlight",tab_bookmarks:"Mga Bookmark",hl_label:"Highlight",hl_no_text:"Naka-highlight na talata (ang teksto ay nasa publikasyon, hindi sa backup).",hl_with_note:"May tala",bm_label:"Bookmark",bm_slot:"Slot {n}",linked_note:"Naka-link na tala:",edit:"I-edit",save:"I-save",cancel:"Kanselahin",delete_item:"Burahin",export_db:"I-export ang .jwlibrary",n_edits:"{n} pagbabago",n_edits_many:"{n} pagbabago",add_tag:"+ Magdagdag ng tag",new_tag_ph:"Pangalan ng tag...",delete_note_confirm:"Burahin ang talang ito? Hindi ito maaaring bawiin.",delete_hl_confirm:"Burahin ang highlight na ito? Hindi ito maaaring bawiin.",delete_bm_confirm:"Burahin ang bookmark na ito? Hindi ito maaaring bawiin.",yes_delete:"Oo, burahin",change_color:"Kulay",unsaved_exit:"Mayroon kang {n} hindi pa na-export na pagbabago. Isara nang hindi nagexport?",title_label:"Pamagat",content_label:"Nilalaman",tags_label:"Mga tag",hl_color_label:"Kulay ng highlight",bm_title_label:"Pamagat ng bookmark",plain_text_note:"Ang format ay magiging plain text kapag nai-save",rte_bold:"Bold",rte_italic:"Italic",rte_underline:"Salungguhit",rte_bullets:"Bulleted na listahan",rich_text_note:"I-edit nang may bold, italic at listahan — pinapanatili ang format",date_from:"Mula",date_to:"Hanggang",date_range:"I-filter ayon sa petsa",extract_range:"I-extract ang saklaw ng petsa",extract_none:"Walang talang nasa saklaw ng petsang ito.",extract_hint:"Mag-save ng bagong .jwlibrary na may mga tala lang sa saklaw ng petsang ito.",copy_md:"Kopyahin bilang Markdown",export_md:"I-export ang Markdown",md_hint:"I-download ang mga ipinapakitang tala bilang Markdown files (.zip)",sel_mode:"Pumili",sel_done:"Tapos",sel_all:"Lahat",sel_none:"Wala",sel_count:"{n} napili",batch_tag:"Tag",batch_color:"Kulay",batch_delete:"Burahin",batch_delete_confirm:"Burahin ang {n}? Maaari mong i-undo bago mag-export.",batch_tag_ph:"Pangalan ng tag…",batch_add:"Idagdag",undo:"I-undo",redo:"I-redo",tab_inputfields:"Mga Sagot",if_label:"Sagot sa pag-aaral",if_question:"Tanong",if_answer:"Ang iyong sagot",if_empty:"(Wala pang sagot)",delete_if_confirm:"Burahin ang sagot na ito sa pag-aaral? Maaari mong i-undo bago mag-export.",share_action:"Ibahagi",share_title:"Ibahagi ang mga tala",share_intro:"Gumagawa ito ng file na ikaw mismo ang nagbibigay — walang ina-upload. Naglalaman ito ng teksto ng tala, kaya ibahagi lang sa mga taong pinagkakatiwalaan.",share_count:"{n} tala",share_download:"I-download ang file",share_copy:"Kopyahin",share_tag:"Ibinahagi",receive_action:"Tumanggap",receive_title:"Tumanggap ng ibinahaging tala",receive_intro:"I-paste ang ibinahaging teksto o pumili ng .jwshare.json file na ipinadala sa iyo.",receive_paste_ph:"I-paste ang ibinahaging tala dito…",receive_choose:"Pumili ng file",receive_preview:"Preview",receive_invalid:"Mukhang hindi ito wastong data ng ibinahaging tala.",preview_readonly:"Preview",adopt:"Idagdag ang {n} sa aking library",adopt_need_lib:"Magbukas muna ng backup",adopted:"Naidagdag ang {n} tala (may tag na \"Ibinahagi\").",open_share:"Ibahagi ang tala →",ask_btn:"Magtanong",ask_title:"Tanungin ang iyong library",ask_sub:"Hanapin ang iyong mga tala sa pamamagitan ng kahulugan, hindi lang mga keyword — magtanong sa natural na wika at mahanap ang mga kaugnay na tala kahit gamitin nila ang iba't ibang salita. Ganap na tumatakbo sa iyong device.",ask_placeholder:"hal. mga tala tungkol sa pananatiling tapat sa ilalim ng presyon",ask_go:"Hanapin",ask_enable_title:"I-aktibo ang semantic search",ask_enable_body:"Isang maliit na language model ang tumatakbo sa iyong browser para maunawaan ang iyong mga tala. Isa lang itong dina-download, naka-cache para sa offline na paggamit, at walang lumalabas sa iyong device.",ask_model_fast_name:"Magaan (pinakamabilis)",ask_model_fast_desc:"3-layer na modelo — mga 2× mas mabilis at kalahating download. Perpekto para sa malalaking library.",ask_model_en_name:"Ingles",ask_model_en_desc:"Karaniwang katumpakan para sa mga talang nakasulat sa Ingles.",ask_model_multi_name:"Maraming wika",ask_model_multi_desc:"Naiintindihan ang 50+ wika — piliin ito kung sumulat ka ng mga tala sa higit sa isang wika.",ask_size_once:"~{n} MB · isang beses",ask_privacy:"100% pribado — ang modelo at ang iyong mga tala ay hindi kailanman lumalabas sa device na ito.",ask_loading_model:"Dina-download ang search model… {pct}%",ask_building:"Binabasa ang iyong mga tala… {done} / {total}",ask_ready:"Handa na — magtanong sa itaas.",ask_searching:"Naghahanap…",ask_results_head:"{n} pinaka-kaugnay na tala",ask_no_results:"Walang kaugnay na talang nahanap. Subukang muling i-phrase ang iyong tanong.",ask_no_notes:"Wala pang mga talang mahahanap sa library na ito.",ask_err:"Hindi ma-load ang modelo. Suriin ang iyong koneksyon at subukan muli.",ask_rebuild:"Muling buuin ang index",ask_match:"{pct}% tugma",batch_tagged_ok:"{n} talang na-tag",ask_switch_model:"Gumamit ng ibang modelo",change_file:"Palitan ang file"}
  ,sv:{title:"Studieutforskaren",search:"Sök...",no_results:"Inget matchar dina filter.",loading:"Läser in biblioteket...",close:"Stäng",no_file:"Öppna en säkerhetskopia först — välj en att bläddra i.",pick_file:"Välj .jwlibrary-fil",count_one:"{n} objekt",count_many:"{n} objekt",color_all:"Alla färger",no_title:"Namnlös",copy:"Kopiera",copied:"Kopierat",clear:"Rensa",error:"Kunde inte läsa in:",pub_all:"Alla publikationer",tag_all:"Alla taggar",back:"← Tillbaka",detail_empty:"Välj ett objekt i listan.",sort_newest:"Nyast först",sort_oldest:"Äldst först",sort_pub:"Efter publikation",modified:"Ändrad",no_content:"(Inget innehåll)",too_many:"Visar de första {n} av {total} — begränsa sökningen.",pg_prev:"Föreg.",pg_next:"Nästa",pg_status:"Sida {page} av {pages} · {total} resultat",err_corrupt:"Den här filen är inte en läsbar .jwlibrary-säkerhetskopia — den kan vara skadad eller av fel filtyp.",err_no_db:"Den här säkerhetskopian saknar sin anteckningsdatabas (userData.db). Exportera den igen från JW Library.",err_not_sqlite:"Säkerhetskopians databas kunde inte öppnas — filen kan vara skadad.",tab_notes:"Anteckningar",tab_highlights:"Överstrykningar",tab_bookmarks:"Bokmärken",hl_label:"Överstrykning",hl_no_text:"Överstruket avsnitt (texten finns i publikationen, inte i säkerhetskopian).",hl_with_note:"Med anteckning",bm_label:"Bokmärke",bm_slot:"Plats {n}",linked_note:"Länkad anteckning:",edit:"Redigera",save:"Spara",cancel:"Avbryt",delete_item:"Ta bort",export_db:"Exportera .jwlibrary",n_edits:"{n} ändring",n_edits_many:"{n} ändringar",add_tag:"+ Lägg till tagg",new_tag_ph:"Taggnamn...",delete_note_confirm:"Ta bort den här anteckningen? Det kan inte ångras.",delete_hl_confirm:"Ta bort den här överstrykningen? Det kan inte ångras.",delete_bm_confirm:"Ta bort det här bokmärket? Det kan inte ångras.",yes_delete:"Ja, ta bort",change_color:"Färg",unsaved_exit:"Du har {n} osparad(e) ändring(ar). Stänga utan att exportera?",title_label:"Titel",content_label:"Innehåll",tags_label:"Taggar",hl_color_label:"Överstrykningsfärg",bm_title_label:"Bokmärkestitel",plain_text_note:"Formateringen förenklas till oformaterad text vid sparande",rte_bold:"Fet",rte_italic:"Kursiv",rte_underline:"Understruken",rte_bullets:"Punktlista",rich_text_note:"Redigera med fetstil, kursiv och listor — formateringen behålls",date_from:"Från",date_to:"Till",date_range:"Filtrera efter datum",extract_range:"Extrahera datumintervall",extract_none:"Inga anteckningar faller inom detta datumintervall.",extract_hint:"Spara en ny .jwlibrary med endast anteckningarna i detta datumintervall.",copy_md:"Kopiera som Markdown",export_md:"Exportera Markdown",md_hint:"Ladda ner de visade anteckningarna som Markdown-filer (.zip)",sel_mode:"Markera",sel_done:"Klar",sel_all:"Alla",sel_none:"Inga",sel_count:"{n} markerade",batch_tag:"Tagg",batch_color:"Färg",batch_delete:"Ta bort",batch_delete_confirm:"Ta bort {n}? Du kan ångra innan du exporterar.",batch_tag_ph:"Taggnamn…",batch_add:"Lägg till",undo:"Ångra",redo:"Gör om",tab_inputfields:"Studiesvar",if_label:"Studiesvar",if_question:"Fråga",if_answer:"Ditt svar",if_empty:"(Inget svar än)",delete_if_confirm:"Ta bort det här studiesvaret? Du kan ångra innan du exporterar.",share_action:"Dela",share_title:"Dela anteckningar",share_intro:"Detta skapar en fil som du själv lämnar över — inget laddas upp. Den innehåller anteckningstexten, så dela bara med personer du litar på.",share_count:"{n} anteckningar",share_download:"Ladda ner fil",share_copy:"Kopiera",share_tag:"Delad",receive_action:"Ta emot",receive_title:"Ta emot delade anteckningar",receive_intro:"Klistra in delad text eller välj en .jwshare.json-fil någon skickat dig.",receive_paste_ph:"Klistra in delade anteckningar här…",receive_choose:"Välj fil",receive_preview:"Förhandsgranska",receive_invalid:"Det där ser inte ut att vara giltiga data med delade anteckningar.",preview_readonly:"Förhandsgranska",adopt:"Lägg till {n} i mitt bibliotek",adopt_need_lib:"Öppna en säkerhetskopia först",adopted:"Lade till {n} anteckningar (taggade \"Delad\").",open_share:"Dela anteckningar →",ask_btn:"Fråga",ask_title:"Fråga ditt bibliotek",ask_sub:"Sök dina anteckningar efter mening, inte bara nyckelord — ställ en fråga på naturligt språk och hitta relaterade anteckningar även om de använder andra ord. Körs helt på din enhet.",ask_placeholder:"t.ex. anteckningar om att förbli lojal under tryck",ask_go:"Sök",ask_enable_title:"Aktivera semantisk sökning",ask_enable_body:"En liten språkmodell körs i din webbläsare för att förstå dina anteckningar. Den laddas ner en gång, cachelagras för offline-användning och ingenting lämnar din enhet.",ask_model_fast_name:"Lätt (snabbast)",ask_model_fast_desc:"Tre-lagers modell — ungefär 2× snabbare och halva nedladdningen. Perfekt för stora bibliotek.",ask_model_en_name:"Engelska",ask_model_en_desc:"Standardprecision för anteckningar skrivna på engelska.",ask_model_multi_name:"Flerspråkig",ask_model_multi_desc:"Förstår 50+ språk — välj detta om du skriver anteckningar på mer än ett språk.",ask_size_once:"~{n} MB · en gång",ask_privacy:"100% privat — modellen och dina anteckningar lämnar aldrig den här enheten.",ask_loading_model:"Laddar ner sökmodellen… {pct}%",ask_building:"Läser dina anteckningar… {done} / {total}",ask_ready:"Klar — ställ en fråga ovan.",ask_searching:"Söker…",ask_results_head:"{n} mest relaterade anteckningar",ask_no_results:"Inga relaterade anteckningar hittades. Försök formulera om din fråga.",ask_no_notes:"Det här biblioteket har inga anteckningar att söka i än.",ask_err:"Det gick inte att läsa in modellen. Kontrollera din anslutning och försök igen.",ask_rebuild:"Bygg om index",ask_match:"{pct}% matchning",batch_tagged_ok:"Taggade {n} anteckningar",ask_switch_model:"Använd en annan modell",change_file:"Byt fil"},ceb:{title:"Study Explorer",search:"Pangita...",no_results:"Walay mitugma sa mga filter.",loading:"Gi-load ang librarya...",close:"Isira",no_file:"Mag-abli ug backup file una — pilia ang usa aron tan-awon.",pick_file:"Pilia ang .jwlibrary file",count_one:"{n} ka butang",count_many:"{n} ka mga butang",color_all:"Tanan nga kulay",no_title:"Walay titulo",copy:"Kopya",copied:"Nakopya",clear:"Papason",error:"Dili ma-load:",pub_all:"Tanan nga mga publikasyon",tag_all:"Tanan nga mga tag",back:"← Balik",detail_empty:"Pilia ang usa ka butang gikan sa listahan.",sort_newest:"Bag-o una",sort_oldest:"Daan una",sort_pub:"Pinaagi sa publikasyon",modified:"Gibag-o",no_content:"(Walay sulod)",too_many:"Gipakita ang unang {n} sa {total} — palipota ang pagpangita.",pg_prev:"Nag-una",pg_next:"Sunod",pg_status:"Pahina {page} sa {pages} · {total} ka resulta",err_corrupt:"Dili mabasa kining file isip .jwlibrary backup — basin nahugaw o maling klase sa file.",err_no_db:"Wala'y database sa mga nota (userData.db) niining backup. I-export pag-usab gikan sa JW Library.",err_not_sqlite:"Dili mabuksan ang database sa backup — basin napangdaut ang file.",tab_notes:"Mga Nota",tab_highlights:"Mga Highlight",tab_bookmarks:"Mga Bookmark",hl_label:"Highlight",hl_no_text:"Gi-highlight nga talata (ang teksto naa sa publikasyon, dili sa backup).",hl_with_note:"May nota",bm_label:"Bookmark",bm_slot:"Slot {n}",linked_note:"Konektadong nota:",edit:"I-edit",save:"I-save",cancel:"Ikansela",delete_item:"Papason",export_db:"I-export ang .jwlibrary",n_edits:"{n} ka pagbag-o",n_edits_many:"{n} ka mga pagbag-o",add_tag:"+ Idugang ang tag",new_tag_ph:"Ngalan sa tag...",delete_note_confirm:"Papason kining nota? Dili na kini mapaulion.",delete_hl_confirm:"Papason kining highlight? Dili na kini mapaulion.",delete_bm_confirm:"Papason kining bookmark? Dili na kini mapaulion.",yes_delete:"Oo, papason",change_color:"Kulay",unsaved_exit:"Naa kay {n} ka pagbag-o nga wala pa ma-export. Isira nga walay pag-export?",title_label:"Titulo",content_label:"Sulod",tags_label:"Mga tag",hl_color_label:"Kulay sa highlight",bm_title_label:"Titulo sa bookmark",plain_text_note:"Gi-simplify ang format ngadto sa plain text sa pagsave",rte_bold:"Bold",rte_italic:"Italic",rte_underline:"Gikulian",rte_bullets:"Listahan nga may bullet",rich_text_note:"I-edit nga adunay bold, italic ug listahan — gipreserba ang format",date_from:"Gikan",date_to:"Hangtod",date_range:"I-filter pinaagi sa petsa",extract_range:"I-extract ang sakop sa petsa",extract_none:"Walay nota sa sakop sa petsang ito.",extract_hint:"Mag-save ug bag-ong .jwlibrary nga adunay mga nota lamang sa sakop sa petsang ito.",copy_md:"Kopya isip Markdown",export_md:"I-export ang Markdown",md_hint:"I-download ang gipakitang mga nota isip Markdown files (.zip)",sel_mode:"Pilia",sel_done:"Tapos",sel_all:"Tanan",sel_none:"Wala",sel_count:"{n} ka napili",batch_tag:"Tag",batch_color:"Kulay",batch_delete:"Papason",batch_delete_confirm:"Papason ang {n}? Mahimo kang mag-Undo sa wala pa mag-export.",batch_tag_ph:"Ngalan sa tag…",batch_add:"Idugang",undo:"I-undo",redo:"I-redo",tab_inputfields:"Mga Tubag sa Pagtuon",if_label:"Tubag sa pagtuon",if_question:"Pangutana",if_answer:"Imong tubag",if_empty:"(Wala pay tubag)",delete_if_confirm:"Papason kining tubag sa pagtuon? Mahimo kang mag-Undo sa wala pa mag-export.",share_action:"Ipaambit",share_title:"Ipaambit ang mga nota",share_intro:"Kini naghimo ug file nga ikaw mismo ang maghatag — walay gi-upload. Kini adunay sulod sa teksto sa nota, busa ipaambit lamang sa mga tawo nga imong gisaligan.",share_count:"{n} ka nota",share_download:"I-download ang file",share_copy:"Kopya",share_tag:"Gipaambit",receive_action:"Dawaton",receive_title:"Dawaton ang mga gipaambit nga nota",receive_intro:"I-paste ang gipaambit nga teksto, o pilia ang .jwshare.json file nga gipadala kanimo.",receive_paste_ph:"I-paste ang gipaambit nga mga nota dinhi…",receive_choose:"Pilia ang file",receive_preview:"Preview",receive_invalid:"Daw dili kini valid nga data sa gipaambit nga nota.",preview_readonly:"Preview",adopt:"Dawaton ang {n} sa akong librarya",adopt_need_lib:"Mag-abli ug backup una",adopted:"Gidawat ang {n} ka nota (na-tag nga \"Gipaambit\").",open_share:"Ipaambit ang Nota →",ask_btn:"Pangutana",ask_title:"Pangutana sa imong librarya",ask_sub:"Pangita ang imong mga nota pinaagi sa kahulogan, dili lamang sa mga keyword — mangutana sa natural nga pinulongan ug pangitaon ang mga konektadong nota bisan lain-laing pulong ang ilang gigamit. Ganap nga nagdagan sa imong device.",ask_placeholder:"hal. mga nota bahin sa pagpabilin nga matinumanon ubos sa presyur",ask_go:"Pangita",ask_enable_title:"I-aktibo ang semantic search",ask_enable_body:"Usa ka gamay nga language model ang nagdagan sa imong browser aron masabtan ang imong mga nota. Usa lamang kini ka beses i-download, gi-cache para sa offline nga paggamit, ug wala gayuy mogawas sa imong device.",ask_model_fast_name:"Gaan (pinakamadali)",ask_model_fast_desc:"3-layer nga modelo — mga 2× mas paspas ug katunga sa download. Perpekto para sa malalaking librarya.",ask_model_en_name:"Ingles",ask_model_en_desc:"Standard nga katukma para sa mga notang gisulat sa Ingles.",ask_model_multi_name:"Daghang pinulongan",ask_model_multi_desc:"Nasabtan ang 50+ ka pinulongan — pilia kini kung nagsulat ka ug mga nota sa labaw sa usa ka pinulongan.",ask_size_once:"~{n} MB · makausa lamang",ask_privacy:"100% pribado — ang modelo ug imong mga nota dili gayud mogawas sa kining device.",ask_loading_model:"Gi-download ang search model… {pct}%",ask_building:"Gibasa ang imong mga nota… {done} / {total}",ask_ready:"Andam na — mangutana sa ibabaw.",ask_searching:"Nagpangita…",ask_results_head:"{n} ka pinakakonektadong nota",ask_no_results:"Walay konektadong nota nga nakit-an. Sulayi pag-usab ang imong pangutana.",ask_no_notes:"Walay mga nota nga mapangitaan sa libraryag kini.",ask_err:"Dili ma-load ang modelo. Susihon ang imong koneksyon ug sulayi pag-usab.",ask_rebuild:"Itukod pag-usab ang index",ask_match:"{pct}% katugma",batch_tagged_ok:"Na-tag ang {n} ka nota",ask_switch_model:"Gamiton ang lain nga modelo",change_file:"Usba ang file"},nl:{title:"Studieverkenner",search:"Zoeken...",no_results:"Niets komt overeen met je filters.",loading:"Bibliotheek laden...",close:"Sluiten",no_file:"Open eerst een back-upbestand — kies er een om te bekijken.",pick_file:"Kies .jwlibrary-bestand",count_one:"{n} item",count_many:"{n} items",color_all:"Alle kleuren",no_title:"Zonder titel",copy:"Kopiëren",copied:"Gekopieerd",clear:"Wissen",error:"Kon niet worden geladen:",pub_all:"Alle publicaties",tag_all:"Alle labels",back:"← Terug",detail_empty:"Kies een item uit de lijst.",sort_newest:"Nieuwste eerst",sort_oldest:"Oudste eerst",sort_pub:"Op publicatie",modified:"Gewijzigd",no_content:"(Geen inhoud)",too_many:"De eerste {n} van {total} worden getoond — verfijn je zoekopdracht.",pg_prev:"Vorige",pg_next:"Volgende",pg_status:"Pagina {page} van {pages} · {total} resultaten",err_corrupt:"Dit bestand is geen leesbare .jwlibrary-back-up — het is mogelijk beschadigd of van het verkeerde type.",err_no_db:"Deze back-up mist zijn aantekeningendatabase (userData.db). Exporteer hem opnieuw vanuit JW Library.",err_not_sqlite:"De database van de back-up kon niet worden geopend — het bestand is mogelijk beschadigd.",tab_notes:"Aantekeningen",tab_highlights:"Markeringen",tab_bookmarks:"Bladwijzers",hl_label:"Markering",hl_no_text:"Gemarkeerde passage (de tekst staat in de publicatie, niet in de back-up).",hl_with_note:"Met aantekening",bm_label:"Bladwijzer",bm_slot:"Plek {n}",linked_note:"Gekoppelde aantekening:",edit:"Bewerken",save:"Opslaan",cancel:"Annuleren",delete_item:"Verwijderen",export_db:".jwlibrary exporteren",n_edits:"{n} bewerking",n_edits_many:"{n} bewerkingen",add_tag:"+ Label toevoegen",new_tag_ph:"Labelnaam...",delete_note_confirm:"Deze aantekening verwijderen? Dit kan niet ongedaan worden gemaakt.",delete_hl_confirm:"Deze markering verwijderen? Dit kan niet ongedaan worden gemaakt.",delete_bm_confirm:"Deze bladwijzer verwijderen? Dit kan niet ongedaan worden gemaakt.",yes_delete:"Ja, verwijderen",change_color:"Kleur",unsaved_exit:"Je hebt {n} niet-opgeslagen bewerkingen. Sluiten zonder exporteren?",title_label:"Titel",content_label:"Inhoud",tags_label:"Labels",hl_color_label:"Markeerkleur",bm_title_label:"Titel van de bladwijzer",plain_text_note:"Opmaak wordt bij het opslaan vereenvoudigd tot platte tekst",rte_bold:"Vet",rte_italic:"Cursief",rte_underline:"Onderstrepen",rte_bullets:"Opsomming",rich_text_note:"Bewerk met vet, cursief en lijsten — de opmaak blijft behouden",date_from:"Van",date_to:"Tot",date_range:"Filteren op datum",extract_range:"Datumbereik uitpakken",extract_none:"Er vallen geen aantekeningen in dit datumbereik.",extract_hint:"Sla een nieuw .jwlibrary-bestand op met alleen de aantekeningen uit dit datumbereik.",copy_md:"Kopiëren als Markdown",export_md:"Markdown exporteren",md_hint:"Download de getoonde aantekeningen als Markdown-bestanden (.zip)",sel_mode:"Selecteren",sel_done:"Klaar",sel_all:"Alles",sel_none:"Geen",sel_count:"{n} geselecteerd",batch_tag:"Label",batch_color:"Kleur",batch_delete:"Verwijderen",batch_delete_confirm:"{n} verwijderen? Je kunt dit ongedaan maken vóór het exporteren.",batch_tag_ph:"Labelnaam…",batch_add:"Toevoegen",undo:"Ongedaan maken",redo:"Opnieuw",tab_inputfields:"Studieantwoorden",if_label:"Studieantwoord",if_question:"Vraag",if_answer:"Jouw antwoord",if_empty:"(Nog geen antwoord)",delete_if_confirm:"Dit studieantwoord verwijderen? Je kunt dit ongedaan maken vóór het exporteren.",share_action:"Delen",share_title:"Aantekeningen delen",share_intro:"Hiermee maak je een bestand dat je zelf doorgeeft — er wordt niets geüpload. Het bevat de tekst van je aantekeningen, dus deel het alleen met mensen die je vertrouwt.",share_count:"{n} aantekeningen",share_download:"Bestand downloaden",share_copy:"Kopiëren",share_tag:"Gedeeld",receive_action:"Ontvangen",receive_title:"Gedeelde aantekeningen ontvangen",receive_intro:"Plak gedeelde tekst of kies een .jwshare.json-bestand dat iemand je heeft gestuurd.",receive_paste_ph:"Plak hier gedeelde aantekeningen…",receive_choose:"Bestand kiezen",receive_preview:"Voorbeeld",receive_invalid:"Dat lijken geen geldige gedeelde aantekeningen.",preview_readonly:"Voorbeeld",adopt:"{n} toevoegen aan mijn bibliotheek",adopt_need_lib:"Open eerst een back-up",adopted:"{n} aantekeningen toegevoegd (met label “Gedeeld”).",open_share:"Aantekeningen delen →",ask_btn:"Vragen",ask_title:"Vraag je bibliotheek",ask_sub:"Doorzoek je aantekeningen op betekenis, niet alleen op trefwoorden — stel je vraag in gewone taal en vind verwante aantekeningen, ook als daar andere woorden in staan. Draait volledig op je eigen apparaat.",ask_placeholder:"bijv. aantekeningen over loyaal blijven onder druk",ask_go:"Zoeken",ask_enable_title:"Zoeken op betekenis inschakelen",ask_enable_body:"Een klein taalmodel draait in je browser om je aantekeningen te begrijpen. Het wordt één keer gedownload, blijft bewaard voor offlinegebruik, en er verlaat nooit iets je apparaat.",ask_model_fast_name:"Licht (snelst)",ask_model_fast_desc:"Model met 3 lagen — ongeveer 2× sneller dan het Engelse model en half zo groot om te downloaden. Ideaal voor grote bibliotheken.",ask_model_en_name:"Engels",ask_model_en_desc:"Standaardnauwkeurigheid voor aantekeningen die in het Engels geschreven zijn.",ask_model_multi_name:"Meertalig",ask_model_multi_desc:"Begrijpt meer dan 50 talen — kies dit als je in meerdere talen aantekeningen maakt.",ask_size_once:"~{n} MB · eenmalig",ask_privacy:"100% privé — het model en je aantekeningen verlaten dit apparaat nooit.",ask_loading_model:"Zoekmodel downloaden… {pct}%",ask_building:"Je aantekeningen worden gelezen… {done} / {total}",ask_ready:"Klaar — stel hierboven een vraag.",ask_searching:"Bezig met zoeken…",ask_results_head:"{n} meest verwante aantekeningen",ask_no_results:"Geen verwante aantekeningen gevonden. Probeer je vraag anders te formuleren.",ask_no_notes:"Deze bibliotheek heeft nog geen aantekeningen om te doorzoeken.",ask_err:"Het zoekmodel kon niet worden geladen. Controleer je verbinding en probeer het opnieuw.",ask_rebuild:"Index opnieuw opbouwen",ask_match:"{pct}% overeenkomst",batch_tagged_ok:"{n} aantekeningen gelabeld",ask_switch_model:"Een ander model gebruiken",change_file:"Bestand wijzigen"},ro:{title:"Exploratorul de studiu",search:"Caută...",no_results:"Nimic nu corespunde filtrelor tale.",loading:"Se încarcă biblioteca...",close:"Închide",no_file:"Deschide întâi un fișier de rezervă — alege unul de răsfoit.",pick_file:"Alege fișierul .jwlibrary",count_one:"{n} element",count_many:"{n} elemente",color_all:"Toate culorile",no_title:"Fără titlu",copy:"Copiază",copied:"Copiat",clear:"Golește",error:"Nu s-a putut încărca:",pub_all:"Toate publicațiile",tag_all:"Toate etichetele",back:"← Înapoi",detail_empty:"Selectează un element din listă.",sort_newest:"Cele mai noi întâi",sort_oldest:"Cele mai vechi întâi",sort_pub:"După publicație",modified:"Modificată",no_content:"(Fără conținut)",too_many:"Se afișează primele {n} din {total} — restrânge căutarea.",pg_prev:"Înapoi",pg_next:"Înainte",pg_status:"Pagina {page} din {pages} · {total} rezultate",err_corrupt:"Acest fișier nu este o copie de rezervă .jwlibrary care poate fi citită — poate fi coruptă sau de un tip greșit.",err_no_db:"Acestei copii de rezervă îi lipsește baza de date cu notițe (userData.db). Exportă-o din nou din JW Library.",err_not_sqlite:"Baza de date a copiei de rezervă nu a putut fi deschisă — fișierul poate fi deteriorat.",tab_notes:"Notițe",tab_highlights:"Evidențieri",tab_bookmarks:"Semne de carte",hl_label:"Evidențiere",hl_no_text:"Pasaj evidențiat (textul se află în publicație, nu în copia de rezervă).",hl_with_note:"Cu notiță",bm_label:"Semn de carte",bm_slot:"Poziția {n}",linked_note:"Notiță legată:",edit:"Modifică",save:"Salvează",cancel:"Anulează",delete_item:"Șterge",export_db:"Exportă .jwlibrary",n_edits:"{n} modificare",n_edits_many:"{n} modificări",add_tag:"+ Adaugă etichetă",new_tag_ph:"Numele etichetei...",delete_note_confirm:"Ștergi această notiță? Acțiunea nu poate fi anulată.",delete_hl_confirm:"Ștergi această evidențiere? Acțiunea nu poate fi anulată.",delete_bm_confirm:"Ștergi acest semn de carte? Acțiunea nu poate fi anulată.",yes_delete:"Da, șterge",change_color:"Culoare",unsaved_exit:"Ai {n} modificări nesalvate. Închizi fără să exporți?",title_label:"Titlu",content_label:"Conținut",tags_label:"Etichete",hl_color_label:"Culoarea evidențierii",bm_title_label:"Titlul semnului de carte",plain_text_note:"Formatarea e simplificată la text simplu la salvare",rte_bold:"Aldin",rte_italic:"Cursiv",rte_underline:"Subliniat",rte_bullets:"Listă cu marcatori",rich_text_note:"Modifică folosind aldin, cursiv și liste — formatarea se păstrează",date_from:"De la",date_to:"Până la",date_range:"Filtrează după dată",extract_range:"Extrage intervalul de date",extract_none:"Nicio notiță nu se încadrează în acest interval de date.",extract_hint:"Salvează un nou fișier .jwlibrary doar cu notițele din acest interval de date.",copy_md:"Copiază ca Markdown",export_md:"Exportă Markdown",md_hint:"Descarcă notițele afișate ca fișiere Markdown (.zip)",sel_mode:"Selectează",sel_done:"Gata",sel_all:"Toate",sel_none:"Niciuna",sel_count:"{n} selectate",batch_tag:"Etichetă",batch_color:"Culoare",batch_delete:"Șterge",batch_delete_confirm:"Ștergi {n}? Poți anula înainte de export.",batch_tag_ph:"Numele etichetei…",batch_add:"Adaugă",undo:"Anulează",redo:"Refă",tab_inputfields:"Răspunsuri de studiu",if_label:"Răspuns de studiu",if_question:"Întrebare",if_answer:"Răspunsul tău",if_empty:"(Încă niciun răspuns)",delete_if_confirm:"Ștergi acest răspuns de studiu? Poți anula înainte de export.",share_action:"Partajează",share_title:"Partajează notițe",share_intro:"Se creează un fișier pe care îl predai tu însuți — nimic nu este încărcat. Conține textul notițelor, așa că partajează-l doar cu persoane în care ai încredere.",share_count:"{n} notițe",share_download:"Descarcă fișierul",share_copy:"Copiază",share_tag:"Partajate",receive_action:"Primește",receive_title:"Primește notițe partajate",receive_intro:"Lipește textul partajat sau alege un fișier .jwshare.json pe care ți l-a trimis cineva.",receive_paste_ph:"Lipește aici notițele partajate…",receive_choose:"Alege fișierul",receive_preview:"Previzualizare",receive_invalid:"Nu pare să fie un set valid de notițe partajate.",preview_readonly:"Previzualizare",adopt:"Adaugă {n} în biblioteca mea",adopt_need_lib:"Deschide întâi o copie de rezervă",adopted:"{n} notițe adăugate (etichetate „Partajate”).",open_share:"Partajează notițe →",ask_btn:"Întreabă",ask_title:"Întreabă-ți biblioteca",ask_sub:"Caută în notițe după sens, nu doar după cuvinte-cheie — întreabă în limbaj obișnuit și găsește notițe înrudite chiar dacă folosesc alte cuvinte. Rulează în întregime pe dispozitivul tău.",ask_placeholder:"ex. notițe despre a rămâne loial sub presiune",ask_go:"Caută",ask_enable_title:"Activează căutarea după sens",ask_enable_body:"Un mic model lingvistic rulează în browserul tău ca să-ți înțeleagă notițele. Se descarcă o singură dată, e păstrat pentru folosire offline și nimic nu părăsește vreodată dispozitivul tău.",ask_model_fast_name:"Ușor (cel mai rapid)",ask_model_fast_desc:"Model cu 3 straturi — de circa 2× mai rapid decât cel englezesc și cu descărcare pe jumătate. Perfect pentru biblioteci mari.",ask_model_en_name:"Engleză",ask_model_en_desc:"Acuratețe standard pentru notițe scrise în engleză.",ask_model_multi_name:"Multilingv",ask_model_multi_desc:"Înțelege peste 50 de limbi — alege-l dacă scrii notițe în mai multe limbi.",ask_size_once:"~{n} MB · o singură dată",ask_privacy:"100% privat — modelul și notițele tale nu părăsesc niciodată acest dispozitiv.",ask_loading_model:"Se descarcă modelul de căutare… {pct}%",ask_building:"Se citesc notițele tale… {done} / {total}",ask_ready:"Gata — pune o întrebare mai sus.",ask_searching:"Se caută…",ask_results_head:"Cele mai înrudite {n} notițe",ask_no_results:"Nicio notiță înrudită găsită. Încearcă să reformulezi întrebarea.",ask_no_notes:"Această bibliotecă nu are încă notițe în care să se caute.",ask_err:"Modelul de căutare nu a putut fi încărcat. Verifică-ți conexiunea și încearcă din nou.",ask_rebuild:"Reconstruiește indexul",ask_match:"{pct}% potrivire",batch_tagged_ok:"{n} notițe etichetate",ask_switch_model:"Folosește alt model",change_file:"Schimbă fișierul"},id:{title:"Penjelajah Pelajaran",search:"Cari...",no_results:"Tidak ada yang cocok dengan saringan Anda.",loading:"Memuat perpustakaan...",close:"Tutup",no_file:"Buka berkas cadangan dulu — pilih satu untuk ditelusuri.",pick_file:"Pilih berkas .jwlibrary",count_one:"{n} item",count_many:"{n} item",color_all:"Semua warna",no_title:"Tanpa judul",copy:"Salin",copied:"Tersalin",clear:"Bersihkan",error:"Tidak dapat dimuat:",pub_all:"Semua publikasi",tag_all:"Semua label",back:"← Kembali",detail_empty:"Pilih sebuah item dari daftar.",sort_newest:"Terbaru dulu",sort_oldest:"Terlama dulu",sort_pub:"Menurut publikasi",modified:"Diubah",no_content:"(Tidak ada isi)",too_many:"Menampilkan {n} pertama dari {total} — persempit pencarian.",pg_prev:"Sebelumnya",pg_next:"Berikutnya",pg_status:"Halaman {page} dari {pages} · {total} hasil",err_corrupt:"Berkas ini bukan cadangan .jwlibrary yang bisa dibaca — mungkin rusak atau jenis berkasnya salah.",err_no_db:"Cadangan ini tidak memiliki basis data catatannya (userData.db). Ekspor ulang dari JW Library.",err_not_sqlite:"Basis data cadangan ini tidak dapat dibuka — berkasnya mungkin rusak.",tab_notes:"Catatan",tab_highlights:"Sorotan",tab_bookmarks:"Penanda",hl_label:"Sorotan",hl_no_text:"Bagian yang disorot (teksnya ada di publikasi, bukan di cadangan).",hl_with_note:"Dengan catatan",bm_label:"Penanda",bm_slot:"Slot {n}",linked_note:"Catatan terkait:",edit:"Ubah",save:"Simpan",cancel:"Batal",delete_item:"Hapus",export_db:"Ekspor .jwlibrary",n_edits:"{n} perubahan",n_edits_many:"{n} perubahan",add_tag:"+ Tambah label",new_tag_ph:"Nama label...",delete_note_confirm:"Hapus catatan ini? Tindakan ini tidak bisa dibatalkan.",delete_hl_confirm:"Hapus sorotan ini? Tindakan ini tidak bisa dibatalkan.",delete_bm_confirm:"Hapus penanda ini? Tindakan ini tidak bisa dibatalkan.",yes_delete:"Ya, hapus",change_color:"Warna",unsaved_exit:"Anda punya {n} perubahan yang belum disimpan. Tutup tanpa mengekspor?",title_label:"Judul",content_label:"Isi",tags_label:"Label",hl_color_label:"Warna sorotan",bm_title_label:"Judul penanda",plain_text_note:"Format disederhanakan menjadi teks biasa saat disimpan",rte_bold:"Tebal",rte_italic:"Miring",rte_underline:"Garis bawah",rte_bullets:"Daftar berpoin",rich_text_note:"Ubah dengan huruf tebal, miring, dan daftar — formatnya dipertahankan",date_from:"Dari",date_to:"Sampai",date_range:"Saring menurut tanggal",extract_range:"Ambil rentang tanggal",extract_none:"Tidak ada catatan dalam rentang tanggal ini.",extract_hint:"Simpan berkas .jwlibrary baru yang hanya berisi catatan dalam rentang tanggal ini.",copy_md:"Salin sebagai Markdown",export_md:"Ekspor Markdown",md_hint:"Unduh catatan yang ditampilkan sebagai berkas Markdown (.zip)",sel_mode:"Pilih",sel_done:"Selesai",sel_all:"Semua",sel_none:"Tidak ada",sel_count:"{n} terpilih",batch_tag:"Label",batch_color:"Warna",batch_delete:"Hapus",batch_delete_confirm:"Hapus {n}? Anda masih bisa Batalkan sebelum mengekspor.",batch_tag_ph:"Nama label…",batch_add:"Tambah",undo:"Batalkan",redo:"Ulangi",tab_inputfields:"Jawaban Pelajaran",if_label:"Jawaban pelajaran",if_question:"Pertanyaan",if_answer:"Jawaban Anda",if_empty:"(Belum ada jawaban)",delete_if_confirm:"Hapus jawaban pelajaran ini? Anda masih bisa Batalkan sebelum mengekspor.",share_action:"Bagikan",share_title:"Bagikan catatan",share_intro:"Ini membuat berkas yang Anda serahkan sendiri — tidak ada yang diunggah. Isinya adalah teks catatan Anda, jadi bagikan hanya kepada orang yang Anda percaya.",share_count:"{n} catatan",share_download:"Unduh berkas",share_copy:"Salin",share_tag:"Dibagikan",receive_action:"Terima",receive_title:"Terima catatan berbagi",receive_intro:"Tempelkan teks yang dibagikan, atau pilih berkas .jwshare.json yang dikirim seseorang kepada Anda.",receive_paste_ph:"Tempelkan catatan berbagi di sini…",receive_choose:"Pilih berkas",receive_preview:"Pratinjau",receive_invalid:"Sepertinya itu bukan data catatan berbagi yang sah.",preview_readonly:"Pratinjau",adopt:"Ambil {n} ke perpustakaan saya",adopt_need_lib:"Buka sebuah cadangan dulu",adopted:"{n} catatan diambil (diberi label \"Dibagikan\").",open_share:"Bagikan Catatan →",ask_btn:"Tanya",ask_title:"Tanya Perpustakaan Anda",ask_sub:"Cari catatan Anda berdasarkan makna, bukan sekadar kata kunci — bertanyalah dengan bahasa sehari-hari dan temukan catatan terkait meski kata-katanya berbeda. Berjalan sepenuhnya di perangkat Anda.",ask_placeholder:"mis. catatan tentang tetap setia di bawah tekanan",ask_go:"Cari",ask_enable_title:"Aktifkan pencarian berdasarkan makna",ask_enable_body:"Sebuah model bahasa kecil berjalan di peramban Anda untuk memahami catatan Anda. Model itu diunduh sekali, disimpan untuk penggunaan luring, dan tidak ada apa pun yang meninggalkan perangkat Anda.",ask_model_fast_name:"Ringan (tercepat)",ask_model_fast_desc:"Model 3 lapis — sekitar 2× lebih cepat daripada model Inggris dan setengah ukuran unduhannya. Cocok untuk perpustakaan besar.",ask_model_en_name:"Inggris",ask_model_en_desc:"Ketepatan standar untuk catatan yang ditulis dalam bahasa Inggris.",ask_model_multi_name:"Multibahasa",ask_model_multi_desc:"Memahami 50+ bahasa — pilih ini jika Anda menulis catatan dalam lebih dari satu bahasa.",ask_size_once:"~{n} MB · sekali saja",ask_privacy:"100% pribadi — model dan catatan Anda tidak pernah meninggalkan perangkat ini.",ask_loading_model:"Mengunduh model pencarian… {pct}%",ask_building:"Membaca catatan Anda… {done} / {total}",ask_ready:"Siap — ajukan pertanyaan di atas.",ask_searching:"Mencari…",ask_results_head:"{n} catatan paling terkait",ask_no_results:"Tidak ada catatan terkait yang ditemukan. Coba ubah kalimat pertanyaan Anda.",ask_no_notes:"Perpustakaan ini belum punya catatan untuk dicari.",ask_err:"Model pencarian tidak dapat dimuat. Periksa koneksi Anda lalu coba lagi.",ask_rebuild:"Bangun ulang indeks",ask_match:"{pct}% cocok",batch_tagged_ok:"{n} catatan diberi label",ask_switch_model:"Pakai model lain",change_file:"Ganti berkas"},hi:{title:"अध्ययन एक्सप्लोरर",search:"खोजें...",no_results:"आपके फ़िल्टर से कुछ मेल नहीं खाता।",loading:"लाइब्रेरी लोड हो रही है...",close:"बंद करें",no_file:"पहले कोई बैकअप फ़ाइल खोलें — देखने के लिए एक चुनें।",pick_file:".jwlibrary फ़ाइल चुनें",count_one:"{n} चीज़",count_many:"{n} चीज़ें",color_all:"सभी रंग",no_title:"बिना शीर्षक",copy:"कॉपी",copied:"कॉपी हो गया",clear:"हटाएँ",error:"लोड नहीं हो सका:",pub_all:"सभी प्रकाशन",tag_all:"सभी टैग",back:"← वापस",detail_empty:"सूची में से कोई चीज़ चुनें।",sort_newest:"सबसे नए पहले",sort_oldest:"सबसे पुराने पहले",sort_pub:"प्रकाशन के अनुसार",modified:"बदला गया",no_content:"(कोई सामग्री नहीं)",too_many:"{total} में से पहले {n} दिख रहे हैं — खोज का दायरा घटाएँ।",pg_prev:"पिछला",pg_next:"अगला",pg_status:"पेज {page} / {pages} · {total} नतीजे",err_corrupt:"यह फ़ाइल पढ़ी जा सकने वाला .jwlibrary बैकअप नहीं है — हो सकता है यह खराब हो या गलत तरह की फ़ाइल हो।",err_no_db:"इस बैकअप में नोटों का डेटाबेस (userData.db) नहीं है। इसे JW Library से दोबारा एक्सपोर्ट करें।",err_not_sqlite:"बैकअप का डेटाबेस खोला नहीं जा सका — फ़ाइल खराब हो सकती है।",tab_notes:"नोट",tab_highlights:"हाइलाइट",tab_bookmarks:"बुकमार्क",hl_label:"हाइलाइट",hl_no_text:"हाइलाइट किया हिस्सा (टेक्स्ट प्रकाशन में रहता है, बैकअप में नहीं)।",hl_with_note:"नोट के साथ",bm_label:"बुकमार्क",bm_slot:"खाना {n}",linked_note:"जुड़ा नोट:",edit:"बदलें",save:"सेव करें",cancel:"रद्द करें",delete_item:"मिटाएँ",export_db:".jwlibrary एक्सपोर्ट करें",n_edits:"{n} बदलाव",n_edits_many:"{n} बदलाव",add_tag:"+ टैग जोड़ें",new_tag_ph:"टैग का नाम...",delete_note_confirm:"यह नोट मिटाएँ? यह वापस नहीं किया जा सकता।",delete_hl_confirm:"यह हाइलाइट मिटाएँ? यह वापस नहीं किया जा सकता।",delete_bm_confirm:"यह बुकमार्क मिटाएँ? यह वापस नहीं किया जा सकता।",yes_delete:"हाँ, मिटाएँ",change_color:"रंग",unsaved_exit:"आपके {n} बदलाव सेव नहीं हुए। एक्सपोर्ट किए बिना बंद करें?",title_label:"शीर्षक",content_label:"सामग्री",tags_label:"टैग",hl_color_label:"हाइलाइट का रंग",bm_title_label:"बुकमार्क का शीर्षक",plain_text_note:"सेव करते समय फ़ॉर्मैटिंग सादे टेक्स्ट में बदल जाएगी",rte_bold:"मोटा",rte_italic:"तिरछा",rte_underline:"रेखांकित",rte_bullets:"बुलेट सूची",rich_text_note:"मोटा, तिरछा और सूचियों के साथ बदलें — फ़ॉर्मैटिंग बनी रहती है",date_from:"से",date_to:"तक",date_range:"तारीख़ से छाँटें",extract_range:"तारीख़ की सीमा निकालें",extract_none:"इस तारीख़ की सीमा में कोई नोट नहीं आता।",extract_hint:"सिर्फ़ इस तारीख़ की सीमा के नोटों वाली नई .jwlibrary फ़ाइल सेव करें।",copy_md:"Markdown के रूप में कॉपी करें",export_md:"Markdown एक्सपोर्ट करें",md_hint:"दिख रहे नोट Markdown फ़ाइलों (.zip) के रूप में डाउनलोड करें",sel_mode:"चुनें",sel_done:"हो गया",sel_all:"सभी",sel_none:"कोई नहीं",sel_count:"{n} चुने गए",batch_tag:"टैग",batch_color:"रंग",batch_delete:"मिटाएँ",batch_delete_confirm:"{n} मिटाएँ? एक्सपोर्ट से पहले आप वापस ला सकते हैं।",batch_tag_ph:"टैग का नाम…",batch_add:"जोड़ें",undo:"पहले जैसा",redo:"फिर से करें",tab_inputfields:"अध्ययन के जवाब",if_label:"अध्ययन का जवाब",if_question:"सवाल",if_answer:"आपका जवाब",if_empty:"(अभी कोई जवाब नहीं)",delete_if_confirm:"यह अध्ययन जवाब मिटाएँ? एक्सपोर्ट से पहले आप वापस ला सकते हैं।",share_action:"साझा करें",share_title:"नोट साझा करें",share_intro:"इससे एक फ़ाइल बनती है जो आप खुद देते हैं — कुछ भी अपलोड नहीं होता। इसमें नोटों का टेक्स्ट होता है, इसलिए इसे सिर्फ़ भरोसेमंद लोगों के साथ साझा करें।",share_count:"{n} नोट",share_download:"फ़ाइल डाउनलोड करें",share_copy:"कॉपी",share_tag:"साझा किया गया",receive_action:"पाएँ",receive_title:"साझा किए गए नोट पाएँ",receive_intro:"साझा किया गया टेक्स्ट चिपकाएँ, या किसी की भेजी .jwshare.json फ़ाइल चुनें।",receive_paste_ph:"साझा किए गए नोट यहाँ चिपकाएँ…",receive_choose:"फ़ाइल चुनें",receive_preview:"पूर्वावलोकन",receive_invalid:"यह साझा किए गए नोटों का सही डेटा नहीं लगता।",preview_readonly:"पूर्वावलोकन",adopt:"{n} मेरी लाइब्रेरी में लें",adopt_need_lib:"पहले कोई बैकअप खोलें",adopted:"{n} नोट ले लिए गए („साझा किया गया” टैग के साथ)।",open_share:"नोट साझा करें →",ask_btn:"पूछें",ask_title:"अपनी लाइब्रेरी से पूछें",ask_sub:"अपने नोटों में सिर्फ़ शब्दों से नहीं, मतलब से खोजें — आम भाषा में पूछें और वे नोट भी पाएँ जिनमें अलग शब्द इस्तेमाल हुए हैं। पूरी तरह आपके डिवाइस पर चलता है।",ask_placeholder:"जैसे: दबाव में वफ़ादार बने रहने के बारे में नोट",ask_go:"खोजें",ask_enable_title:"मतलब से खोज चालू करें",ask_enable_body:"आपके नोट समझने के लिए एक छोटा भाषा मॉडल आपके ब्राउज़र में चलता है। यह एक बार डाउनलोड होता है, ऑफ़लाइन इस्तेमाल के लिए सहेज लिया जाता है, और कुछ भी आपके डिवाइस से बाहर नहीं जाता।",ask_model_fast_name:"हल्का (सबसे तेज़)",ask_model_fast_desc:"3 परतों वाला मॉडल — अंग्रेज़ी वाले से लगभग 2× तेज़ और डाउनलोड आधा। बड़ी लाइब्रेरी के लिए बढ़िया।",ask_model_en_name:"अंग्रेज़ी",ask_model_en_desc:"अंग्रेज़ी में लिखे नोटों के लिए सामान्य सटीकता।",ask_model_multi_name:"बहुभाषी",ask_model_multi_desc:"50 से ज़्यादा भाषाएँ समझता है — अगर आप एक से ज़्यादा भाषा में नोट लिखते हैं तो यह चुनें।",ask_size_once:"~{n} MB · सिर्फ़ एक बार",ask_privacy:"100% निजी — मॉडल और आपके नोट कभी इस डिवाइस से बाहर नहीं जाते।",ask_loading_model:"खोज मॉडल डाउनलोड हो रहा है… {pct}%",ask_building:"आपके नोट पढ़े जा रहे हैं… {done} / {total}",ask_ready:"तैयार — ऊपर अपना सवाल पूछें।",ask_searching:"खोजा जा रहा है…",ask_results_head:"{n} सबसे मिलते-जुलते नोट",ask_no_results:"कोई मिलता-जुलता नोट नहीं मिला। सवाल दूसरे शब्दों में पूछकर देखें।",ask_no_notes:"इस लाइब्रेरी में खोजने के लिए अभी कोई नोट नहीं है।",ask_err:"खोज मॉडल लोड नहीं हो सका। अपना कनेक्शन जाँचें और फिर कोशिश करें।",ask_rebuild:"इंडेक्स दोबारा बनाएँ",ask_match:"{pct}% मेल",batch_tagged_ok:"{n} नोट टैग किए गए",ask_switch_model:"दूसरा मॉडल इस्तेमाल करें",change_file:"फ़ाइल बदलें"},hu:{title:"Tanulmányozási böngésző",search:"Keresés...",no_results:"Semmi nem felel meg a szűrőidnek.",loading:"Könyvtár betöltése...",close:"Bezárás",no_file:"Előbb nyiss meg egy mentésfájlt — válassz egyet a böngészéshez.",pick_file:".jwlibrary fájl kiválasztása",count_one:"{n} elem",count_many:"{n} elem",color_all:"Minden szín",no_title:"Cím nélkül",copy:"Másolás",copied:"Kimásolva",clear:"Törlés",error:"Nem sikerült betölteni:",pub_all:"Minden kiadvány",tag_all:"Minden címke",back:"← Vissza",detail_empty:"Válassz egy elemet a listából.",sort_newest:"Legújabb elöl",sort_oldest:"Legrégebbi elöl",sort_pub:"Kiadvány szerint",modified:"Módosítva",no_content:"(Nincs tartalom)",too_many:"{total} elemből az első {n} látszik — szűkítsd a keresést.",pg_prev:"Előző",pg_next:"Következő",pg_status:"{page}. oldal / {pages} · {total} találat",err_corrupt:"Ez a fájl nem olvasható .jwlibrary mentés — lehet, hogy sérült, vagy nem megfelelő típusú fájl.",err_no_db:"Ebből a mentésből hiányzik a jegyzetadatbázis (userData.db). Exportáld újra a JW Libraryből.",err_not_sqlite:"A mentés adatbázisát nem sikerült megnyitni — a fájl sérült lehet.",tab_notes:"Jegyzetek",tab_highlights:"Kiemelések",tab_bookmarks:"Könyvjelzők",hl_label:"Kiemelés",hl_no_text:"Kiemelt szakasz (a szöveg a kiadványban van, nem a mentésben).",hl_with_note:"Jegyzettel",bm_label:"Könyvjelző",bm_slot:"{n}. hely",linked_note:"Kapcsolt jegyzet:",edit:"Szerkesztés",save:"Mentés",cancel:"Mégse",delete_item:"Törlés",export_db:".jwlibrary exportálása",n_edits:"{n} módosítás",n_edits_many:"{n} módosítás",add_tag:"+ Címke hozzáadása",new_tag_ph:"Címke neve...",delete_note_confirm:"Törlöd ezt a jegyzetet? Ez nem vonható vissza.",delete_hl_confirm:"Törlöd ezt a kiemelést? Ez nem vonható vissza.",delete_bm_confirm:"Törlöd ezt a könyvjelzőt? Ez nem vonható vissza.",yes_delete:"Igen, törlöm",change_color:"Szín",unsaved_exit:"{n} mentetlen módosításod van. Bezárod exportálás nélkül?",title_label:"Cím",content_label:"Tartalom",tags_label:"Címkék",hl_color_label:"Kiemelés színe",bm_title_label:"Könyvjelző címe",plain_text_note:"A formázás mentéskor egyszerű szöveggé egyszerűsödik",rte_bold:"Félkövér",rte_italic:"Dőlt",rte_underline:"Aláhúzott",rte_bullets:"Felsorolás",rich_text_note:"Szerkeszthetsz félkövérrel, dőlttel és felsorolással — a formázás megmarad",date_from:"Ettől",date_to:"Eddig",date_range:"Szűrés dátum szerint",extract_range:"Dátumtartomány kinyerése",extract_none:"Ebbe a dátumtartományba nem esik jegyzet.",extract_hint:"Ments egy új .jwlibrary fájlt, amelyben csak az ebbe a dátumtartományba eső jegyzetek vannak.",copy_md:"Másolás Markdownként",export_md:"Markdown exportálása",md_hint:"Töltsd le a megjelenített jegyzeteket Markdown-fájlokként (.zip)",sel_mode:"Kijelölés",sel_done:"Kész",sel_all:"Mind",sel_none:"Egyik sem",sel_count:"{n} kijelölve",batch_tag:"Címke",batch_color:"Szín",batch_delete:"Törlés",batch_delete_confirm:"Törölsz {n} elemet? Exportálás előtt vissza tudod vonni.",batch_tag_ph:"Címke neve…",batch_add:"Hozzáadás",undo:"Visszavonás",redo:"Újra",tab_inputfields:"Tanulmányozási válaszok",if_label:"Tanulmányozási válasz",if_question:"Kérdés",if_answer:"A válaszod",if_empty:"(Még nincs válasz)",delete_if_confirm:"Törlöd ezt a tanulmányozási választ? Exportálás előtt vissza tudod vonni.",share_action:"Megosztás",share_title:"Jegyzetek megosztása",share_intro:"Ezzel egy fájl készül, amelyet te magad adsz át — semmi nem kerül feltöltésre. A jegyzetek szövegét tartalmazza, ezért csak olyanokkal oszd meg, akikben megbízol.",share_count:"{n} jegyzet",share_download:"Fájl letöltése",share_copy:"Másolás",share_tag:"Megosztott",receive_action:"Fogadás",receive_title:"Megosztott jegyzetek fogadása",receive_intro:"Illeszd be a megosztott szöveget, vagy válaszd ki a neked küldött .jwshare.json fájlt.",receive_paste_ph:"Illeszd be ide a megosztott jegyzeteket…",receive_choose:"Fájl kiválasztása",receive_preview:"Előnézet",receive_invalid:"Ez nem tűnik érvényes megosztottjegyzet-adatnak.",preview_readonly:"Előnézet",adopt:"{n} átvétele a könyvtáramba",adopt_need_lib:"Előbb nyiss meg egy mentést",adopted:"{n} jegyzet átvéve („Megosztott” címkével).",open_share:"Jegyzetek megosztása →",ask_btn:"Kérdezz",ask_title:"Kérdezd a könyvtáradat",ask_sub:"Keress a jegyzeteid között jelentés alapján, nem csak kulcsszavakkal — kérdezz hétköznapi nyelven, és megtalálod a kapcsolódó jegyzeteket akkor is, ha más szavakat használnak. Teljes egészében a te eszközödön fut.",ask_placeholder:"pl. jegyzetek a nyomás alatti hűségről",ask_go:"Keresés",ask_enable_title:"Kapcsold be a jelentés szerinti keresést",ask_enable_body:"Egy kis nyelvi modell fut a böngésződben, hogy értelmezze a jegyzeteidet. Egyszer töltődik le, offline használatra elmentődik, és soha semmi nem hagyja el az eszközödet.",ask_model_fast_name:"Könnyű (leggyorsabb)",ask_model_fast_desc:"3 rétegű modell — nagyjából 2×-e gyorsabb az angolnál, és feleakkora a letöltés. Nagy könyvtárakhoz tökéletes.",ask_model_en_name:"Angol",ask_model_en_desc:"Szokásos pontosság angolul írt jegyzetekhez.",ask_model_multi_name:"Többnyelvű",ask_model_multi_desc:"Több mint 50 nyelvet ért — ezt válaszd, ha több nyelven is írsz jegyzeteket.",ask_size_once:"~{n} MB · egyszeri",ask_privacy:"100%-ban magánjellegű — a modell és a jegyzeteid soha nem hagyják el ezt az eszközt.",ask_loading_model:"Keresőmodell letöltése… {pct}%",ask_building:"A jegyzeteid olvasása… {done} / {total}",ask_ready:"Kész — tedd fel a kérdésedet fent.",ask_searching:"Keresés…",ask_results_head:"{n} legkapcsolódóbb jegyzet",ask_no_results:"Nem találtunk kapcsolódó jegyzetet. Próbáld másképp megfogalmazni a kérdésedet.",ask_no_notes:"Ebben a könyvtárban még nincs jegyzet, amiben keresni lehetne.",ask_err:"Nem sikerült betölteni a keresőmodellt. Ellenőrizd a kapcsolatot, és próbáld újra.",ask_rebuild:"Index újraépítése",ask_match:"{pct}% egyezés",batch_tagged_ok:"{n} jegyzet felcímkézve",ask_switch_model:"Másik modell használata",change_file:"Fájl cseréje"},vi:{title:"Trình khám phá học hỏi",search:"Tìm kiếm...",no_results:"Không có gì khớp với bộ lọc của bạn.",loading:"Đang tải thư viện...",close:"Đóng",no_file:"Hãy mở một tập tin sao lưu trước — chọn một tập tin để duyệt.",pick_file:"Chọn tập tin .jwlibrary",count_one:"{n} mục",count_many:"{n} mục",color_all:"Tất cả màu",no_title:"Không tiêu đề",copy:"Chép",copied:"Đã chép",clear:"Xóa bộ lọc",error:"Không tải được:",pub_all:"Tất cả ấn phẩm",tag_all:"Tất cả thẻ",back:"← Quay lại",detail_empty:"Hãy chọn một mục từ danh sách.",sort_newest:"Mới nhất trước",sort_oldest:"Cũ nhất trước",sort_pub:"Theo ấn phẩm",modified:"Đã sửa",no_content:"(Không có nội dung)",too_many:"Đang hiện {n} mục đầu trong {total} — hãy thu hẹp tìm kiếm.",pg_prev:"Trước",pg_next:"Sau",pg_status:"Trang {page} trong {pages} · {total} kết quả",err_corrupt:"Tập tin này không phải là bản sao lưu .jwlibrary đọc được — có thể nó đã hỏng hoặc không đúng loại tập tin.",err_no_db:"Bản sao lưu này thiếu cơ sở dữ liệu ghi chú (userData.db). Hãy xuất lại từ JW Library.",err_not_sqlite:"Không mở được cơ sở dữ liệu của bản sao lưu — tập tin có thể đã hỏng.",tab_notes:"Ghi chú",tab_highlights:"Phần tô màu",tab_bookmarks:"Dấu trang",hl_label:"Phần tô màu",hl_no_text:"Đoạn được tô màu (phần chữ nằm trong ấn phẩm, không nằm trong bản sao lưu).",hl_with_note:"Có ghi chú",bm_label:"Dấu trang",bm_slot:"Ô {n}",linked_note:"Ghi chú liên kết:",edit:"Sửa",save:"Lưu",cancel:"Hủy",delete_item:"Xóa",export_db:"Xuất .jwlibrary",n_edits:"{n} thay đổi",n_edits_many:"{n} thay đổi",add_tag:"+ Thêm thẻ",new_tag_ph:"Tên thẻ...",delete_note_confirm:"Xóa ghi chú này? Việc này không thể hoàn tác.",delete_hl_confirm:"Xóa phần tô màu này? Việc này không thể hoàn tác.",delete_bm_confirm:"Xóa dấu trang này? Việc này không thể hoàn tác.",yes_delete:"Vâng, xóa",change_color:"Màu",unsaved_exit:"Bạn có {n} thay đổi chưa lưu. Đóng mà không xuất chứ?",title_label:"Tiêu đề",content_label:"Nội dung",tags_label:"Thẻ",hl_color_label:"Màu tô",bm_title_label:"Tiêu đề dấu trang",plain_text_note:"Định dạng sẽ được rút gọn thành văn bản thuần khi lưu",rte_bold:"Đậm",rte_italic:"Nghiêng",rte_underline:"Gạch chân",rte_bullets:"Danh sách gạch đầu dòng",rich_text_note:"Sửa với chữ đậm, nghiêng và danh sách — định dạng được giữ nguyên",date_from:"Từ",date_to:"Đến",date_range:"Lọc theo ngày",extract_range:"Trích khoảng ngày",extract_none:"Không có ghi chú nào rơi vào khoảng ngày này.",extract_hint:"Lưu một tập tin .jwlibrary mới chỉ gồm các ghi chú trong khoảng ngày này.",copy_md:"Chép dưới dạng Markdown",export_md:"Xuất Markdown",md_hint:"Tải các ghi chú đang hiện dưới dạng tập tin Markdown (.zip)",sel_mode:"Chọn",sel_done:"Xong",sel_all:"Tất cả",sel_none:"Không chọn",sel_count:"Đã chọn {n}",batch_tag:"Thẻ",batch_color:"Màu",batch_delete:"Xóa",batch_delete_confirm:"Xóa {n} mục? Bạn có thể Hoàn tác trước khi xuất.",batch_tag_ph:"Tên thẻ…",batch_add:"Thêm",undo:"Hoàn tác",redo:"Làm lại",tab_inputfields:"Câu trả lời học hỏi",if_label:"Câu trả lời học hỏi",if_question:"Câu hỏi",if_answer:"Câu trả lời của bạn",if_empty:"(Chưa có câu trả lời)",delete_if_confirm:"Xóa câu trả lời học hỏi này? Bạn có thể Hoàn tác trước khi xuất.",share_action:"Chia sẻ",share_title:"Chia sẻ ghi chú",share_intro:"Thao tác này tạo ra một tập tin do chính bạn trao đi — không có gì được tải lên. Nó chứa nội dung ghi chú, nên chỉ chia sẻ với người bạn tin tưởng.",share_count:"{n} ghi chú",share_download:"Tải tập tin về",share_copy:"Chép",share_tag:"Được chia sẻ",receive_action:"Nhận",receive_title:"Nhận ghi chú được chia sẻ",receive_intro:"Dán văn bản được chia sẻ, hoặc chọn tập tin .jwshare.json ai đó gửi cho bạn.",receive_paste_ph:"Dán ghi chú được chia sẻ vào đây…",receive_choose:"Chọn tập tin",receive_preview:"Xem trước",receive_invalid:"Cái đó có vẻ không phải dữ liệu ghi chú được chia sẻ hợp lệ.",preview_readonly:"Xem trước",adopt:"Nhận {n} mục vào thư viện của tôi",adopt_need_lib:"Hãy mở một bản sao lưu trước",adopted:"Đã nhận {n} ghi chú (gắn thẻ \"Được chia sẻ\").",open_share:"Chia sẻ ghi chú →",ask_btn:"Hỏi",ask_title:"Hỏi thư viện của bạn",ask_sub:"Tìm ghi chú theo ý nghĩa chứ không chỉ theo từ khóa — hãy hỏi bằng lời thường ngày và tìm được cả những ghi chú dùng từ ngữ khác. Chạy hoàn toàn trên thiết bị của bạn.",ask_placeholder:"ví dụ: ghi chú về việc giữ lòng trung thành khi bị áp lực",ask_go:"Tìm",ask_enable_title:"Bật tìm kiếm theo ý nghĩa",ask_enable_body:"Một mô hình ngôn ngữ nhỏ chạy trong trình duyệt của bạn để hiểu các ghi chú. Nó chỉ tải về một lần, được lưu để dùng ngoại tuyến, và không có gì rời khỏi thiết bị của bạn.",ask_model_fast_name:"Nhẹ (nhanh nhất)",ask_model_fast_desc:"Mô hình 3 lớp — nhanh gấp khoảng 2 lần bản tiếng Anh và dung lượng tải chỉ bằng một nửa. Rất hợp với thư viện lớn.",ask_model_en_name:"Tiếng Anh",ask_model_en_desc:"Độ chính xác tiêu chuẩn cho ghi chú viết bằng tiếng Anh.",ask_model_multi_name:"Đa ngôn ngữ",ask_model_multi_desc:"Hiểu hơn 50 ngôn ngữ — hãy chọn cái này nếu bạn viết ghi chú bằng nhiều hơn một ngôn ngữ.",ask_size_once:"~{n} MB · chỉ một lần",ask_privacy:"100% riêng tư — mô hình và ghi chú của bạn không bao giờ rời khỏi thiết bị này.",ask_loading_model:"Đang tải mô hình tìm kiếm… {pct}%",ask_building:"Đang đọc ghi chú của bạn… {done} / {total}",ask_ready:"Sẵn sàng — hãy đặt câu hỏi ở trên.",ask_searching:"Đang tìm…",ask_results_head:"{n} ghi chú liên quan nhất",ask_no_results:"Không tìm thấy ghi chú liên quan. Hãy thử diễn đạt câu hỏi theo cách khác.",ask_no_notes:"Thư viện này chưa có ghi chú nào để tìm.",ask_err:"Không tải được mô hình tìm kiếm. Hãy kiểm tra kết nối và thử lại.",ask_rebuild:"Dựng lại chỉ mục",ask_match:"Khớp {pct}%",batch_tagged_ok:"Đã gắn thẻ cho {n} ghi chú",ask_switch_model:"Dùng mô hình khác",change_file:"Đổi tập tin"},"yue-Hant":{title:"研究瀏覽器",search:"搜尋……",no_results:"冇嘢符合你嘅篩選。",loading:"載入緊書庫……",close:"閂咗佢",no_file:"請先打開一個備份檔案——揀一個嚟瀏覽。",pick_file:"揀 .jwlibrary 檔案",count_one:"{n} 項",count_many:"{n} 項",color_all:"全部顏色",no_title:"冇標題",copy:"複製",copied:"複製咗",clear:"清除",error:"載入唔到：",pub_all:"全部出版物",tag_all:"全部標籤",back:"← 返去",detail_empty:"喺清單度揀一項。",sort_newest:"最新喺前",sort_oldest:"最舊喺前",sort_pub:"按出版物",modified:"改於",no_content:"（冇內容）",too_many:"顯示 {total} 項入面頭 {n} 項——請收窄搜尋範圍。",pg_prev:"上一頁",pg_next:"下一頁",pg_status:"第 {page} / {pages} 頁 · 共 {total} 個結果",err_corrupt:"呢個檔案唔係讀得到嘅 .jwlibrary 備份——可能已經損壞，或者唔係正確嘅檔案類型。",err_no_db:"呢個備份缺少筆記資料庫（userData.db）。請由 JW Library 重新匯出。",err_not_sqlite:"打唔開呢個備份嘅資料庫——檔案可能已經損壞。",tab_notes:"筆記",tab_highlights:"標註",tab_bookmarks:"書籤",hl_label:"標註",hl_no_text:"標註咗嘅段落（正文喺出版物入面，唔係喺備份度）。",hl_with_note:"附帶筆記",bm_label:"書籤",bm_slot:"第 {n} 個位",linked_note:"關聯嘅筆記：",edit:"編輯",save:"儲存",cancel:"取消",delete_item:"刪除",export_db:"匯出 .jwlibrary",n_edits:"{n} 處改動",n_edits_many:"{n} 處改動",add_tag:"+ 加標籤",new_tag_ph:"標籤名……",delete_note_confirm:"要刪除呢條筆記？呢個動作冇得復原。",delete_hl_confirm:"要刪除呢處標註？呢個動作冇得復原。",delete_bm_confirm:"要刪除呢個書籤？呢個動作冇得復原。",yes_delete:"係，刪除",change_color:"顏色",unsaved_exit:"你有 {n} 處改動仲未儲存。要唔匯出就閂咗佢？",title_label:"標題",content_label:"內容",tags_label:"標籤",hl_color_label:"標註顏色",bm_title_label:"書籤標題",plain_text_note:"儲存嗰陣格式會簡化做純文字",rte_bold:"粗體",rte_italic:"斜體",rte_underline:"底線",rte_bullets:"項目符號清單",rich_text_note:"可以用粗體、斜體同清單嚟編輯——格式會保留",date_from:"由",date_to:"到",date_range:"按日期篩選",extract_range:"抽取日期範圍",extract_none:"呢個日期範圍入面冇筆記。",extract_hint:"儲存一個淨係有呢個日期範圍筆記嘅新 .jwlibrary 檔案。",copy_md:"複製做 Markdown",export_md:"匯出 Markdown",md_hint:"將顯示咗嘅筆記下載做 Markdown 檔案（.zip）",sel_mode:"揀選",sel_done:"完成",sel_all:"全部",sel_none:"全部唔揀",sel_count:"揀咗 {n} 項",batch_tag:"標籤",batch_color:"顏色",batch_delete:"刪除",batch_delete_confirm:"要刪除 {n} 項？匯出之前仲可以復原。",batch_tag_ph:"標籤名……",batch_add:"加入",undo:"復原",redo:"重做",tab_inputfields:"研究答案",if_label:"研究答案",if_question:"問題",if_answer:"你嘅答案",if_empty:"（仲未有答案）",delete_if_confirm:"要刪除呢條答案？匯出之前仲可以復原。",share_action:"分享",share_title:"分享筆記",share_intro:"呢個會整個由你親自交畀人嘅檔案——任何嘢都唔會上載。入面有筆記正文，所以淨係分享畀你信得過嘅人。",share_count:"{n} 條筆記",share_download:"下載檔案",share_copy:"複製",share_tag:"已分享",receive_action:"接收",receive_title:"接收分享嘅筆記",receive_intro:"貼上分享嘅文字，或者揀人哋寄畀你嘅 .jwshare.json 檔案。",receive_paste_ph:"喺呢度貼上分享嘅筆記……",receive_choose:"揀檔案",receive_preview:"預覽",receive_invalid:"呢個睇落唔似有效嘅分享筆記資料。",preview_readonly:"預覽",adopt:"將 {n} 條加落我嘅書庫",adopt_need_lib:"請先打開一個備份",adopted:"加咗 {n} 條筆記（標籤係「已分享」）。",open_share:"分享筆記 →",ask_btn:"問",ask_title:"問你個書庫",ask_sub:"按意思搜尋你嘅筆記，唔淨係靠關鍵字——用平時講嘢嘅方式問，就算用詞唔同都搵到相關筆記。全部喺你部裝置度行。",ask_placeholder:"例如：關於喺壓力下保持忠誠嘅筆記",ask_go:"搜尋",ask_enable_title:"開啟語意搜尋",ask_enable_body:"一個細嘅語言模型會喺你嘅瀏覽器度行，用嚟理解你嘅筆記。佢淨係下載一次，之後會快取起嚟畀你離線用，任何嘢都唔會離開你部裝置。",ask_model_fast_name:"輕量（最快）",ask_model_fast_desc:"3 層模型——速度大約係英文模型嘅 2 倍，下載大細細一半。最啱大型書庫。",ask_model_en_name:"英文",ask_model_en_desc:"適合用英文寫嘅筆記，準確度標準。",ask_model_multi_name:"多語言",ask_model_multi_desc:"支援 50 幾種語言——如果你用多過一種語言寫筆記就揀呢個。",ask_size_once:"約 {n} MB · 淨係要一次",ask_privacy:"100% 私隱——模型同你嘅筆記永遠唔會離開呢部裝置。",ask_loading_model:"下載緊搜尋模型…… {pct}%",ask_building:"讀緊你嘅筆記…… {done} / {total}",ask_ready:"準備好喇——喺上面問啦。",ask_searching:"搜尋緊……",ask_results_head:"最相關嘅 {n} 條筆記",ask_no_results:"搵唔到相關筆記。試吓換個講法。",ask_no_notes:"呢個書庫仲未有可以搜尋嘅筆記。",ask_err:"載入唔到搜尋模型。請檢查吓網絡連線再試過。",ask_rebuild:"重建索引",ask_match:"{pct}% 相符",batch_tagged_ok:"幫 {n} 條筆記加咗標籤",ask_switch_model:"換個模型",change_file:"換檔案"},"zh-Hant":{title:"研究瀏覽器",search:"搜尋……",no_results:"沒有符合篩選條件的內容。",loading:"正在載入書庫……",close:"關閉",no_file:"請先開啟一個備份檔案——選擇一個來瀏覽。",pick_file:"選擇 .jwlibrary 檔案",count_one:"{n} 項",count_many:"{n} 項",color_all:"全部顏色",no_title:"無標題",copy:"複製",copied:"已複製",clear:"清除",error:"無法載入：",pub_all:"全部出版物",tag_all:"全部標籤",back:"← 返回",detail_empty:"請從列表中選擇一項。",sort_newest:"最新在前",sort_oldest:"最早在前",sort_pub:"按出版物",modified:"修改於",no_content:"（無內容）",too_many:"顯示 {total} 項中的前 {n} 項——請縮小搜尋範圍。",pg_prev:"上一頁",pg_next:"下一頁",pg_status:"第 {page} / {pages} 頁 · 共 {total} 條結果",err_corrupt:"這個檔案不是可讀的 .jwlibrary 備份——它可能已損壞，或者不是正確的檔案型別。",err_no_db:"這個備份缺少筆記資料庫（userData.db）。請從 JW Library 重新匯出。",err_not_sqlite:"無法開啟該備份的資料庫——檔案可能已損壞。",tab_notes:"筆記",tab_highlights:"標註",tab_bookmarks:"書籤",hl_label:"標註",hl_no_text:"已標註的段落（正文在出版物中，不在備份裡）。",hl_with_note:"附帶筆記",bm_label:"書籤",bm_slot:"第 {n} 位",linked_note:"關聯的筆記：",edit:"編輯",save:"儲存",cancel:"取消",delete_item:"刪除",export_db:"匯出 .jwlibrary",n_edits:"{n} 處修改",n_edits_many:"{n} 處修改",add_tag:"+ 新增標籤",new_tag_ph:"標籤名稱……",delete_note_confirm:"要刪除這條筆記嗎？此操作無法撤銷。",delete_hl_confirm:"要刪除這處標註嗎？此操作無法撤銷。",delete_bm_confirm:"要刪除這個書籤嗎？此操作無法撤銷。",yes_delete:"是的，刪除",change_color:"顏色",unsaved_exit:"你有 {n} 處修改尚未儲存。要不匯出就關閉嗎？",title_label:"標題",content_label:"內容",tags_label:"標籤",hl_color_label:"標註顏色",bm_title_label:"書籤標題",plain_text_note:"儲存時格式會簡化為純文字",rte_bold:"加粗",rte_italic:"斜體",rte_underline:"下劃線",rte_bullets:"專案符號列表",rich_text_note:"可使用加粗、斜體和列表編輯——格式會被保留",date_from:"從",date_to:"到",date_range:"按日期篩選",extract_range:"提取日期範圍",extract_none:"這個日期範圍內沒有筆記。",extract_hint:"儲存一個只含該日期範圍內筆記的新 .jwlibrary 檔案。",copy_md:"複製為 Markdown",export_md:"匯出 Markdown",md_hint:"把顯示的筆記下載為 Markdown 檔案（.zip）",sel_mode:"選擇",sel_done:"完成",sel_all:"全部",sel_none:"全不選",sel_count:"已選 {n} 項",batch_tag:"標籤",batch_color:"顏色",batch_delete:"刪除",batch_delete_confirm:"要刪除 {n} 項嗎？匯出前仍可撤銷。",batch_tag_ph:"標籤名稱……",batch_add:"新增",undo:"撤銷",redo:"重做",tab_inputfields:"研究答案",if_label:"研究答案",if_question:"問題",if_answer:"你的答案",if_empty:"（還沒有答案）",delete_if_confirm:"要刪除這條答案嗎？匯出前仍可撤銷。",share_action:"分享",share_title:"分享筆記",share_intro:"這會生成一個由你親自轉交的檔案——任何內容都不會上傳。它包含筆記正文，所以請只分享給你信任的人。",share_count:"{n} 條筆記",share_download:"下載檔案",share_copy:"複製",share_tag:"已分享",receive_action:"接收",receive_title:"接收分享的筆記",receive_intro:"貼上分享的文字，或選擇別人發給你的 .jwshare.json 檔案。",receive_paste_ph:"在此貼上分享的筆記……",receive_choose:"選擇檔案",receive_preview:"預覽",receive_invalid:"這看起來不是有效的分享筆記資料。",preview_readonly:"預覽",adopt:"把 {n} 條新增到我的書庫",adopt_need_lib:"請先開啟一個備份",adopted:"已新增 {n} 條筆記（標籤為「已分享」）。",open_share:"分享筆記 →",ask_btn:"提問",ask_title:"問問你的書庫",ask_sub:"按含義搜尋你的筆記，而不只是關鍵詞——用平常的話提問，即使措辭不同也能找到相關筆記。全部在你的裝置上執行。",ask_placeholder:"例如：關於在壓力下保持忠誠的筆記",ask_go:"搜尋",ask_enable_title:"開啟語義搜尋",ask_enable_body:"一個小型語言模型會在你的瀏覽器中執行，用來理解你的筆記。它只需下載一次，之後會快取供離線使用，任何內容都不會離開你的裝置。",ask_model_fast_name:"輕量（最快）",ask_model_fast_desc:"3 層模型——速度約為英語模型的 2 倍，下載體積減半。非常適合大型書庫。",ask_model_en_name:"英語",ask_model_en_desc:"適用於以英語撰寫的筆記，準確度標準。",ask_model_multi_name:"多語言",ask_model_multi_desc:"支援 50 多種語言——如果你用多種語言寫筆記，請選這個。",ask_size_once:"約 {n} MB · 僅需一次",ask_privacy:"100% 私密——模型和你的筆記絕不會離開這台裝置。",ask_loading_model:"正在下載搜尋模型…… {pct}%",ask_building:"正在讀取你的筆記…… {done} / {total}",ask_ready:"準備就緒——請在上方提問。",ask_searching:"正在搜尋……",ask_results_head:"最相關的 {n} 條筆記",ask_no_results:"沒有找到相關筆記。試試換個說法。",ask_no_notes:"這個書庫還沒有可搜尋的筆記。",ask_err:"無法載入搜尋模型。請檢查網路連線後重試。",ask_rebuild:"重建索引",ask_match:"{pct}% 匹配",batch_tagged_ok:"已為 {n} 條筆記新增標籤",ask_switch_model:"換一個模型",change_file:"更換檔案"},"zh-Hans":{title:"研究浏览器",search:"搜索……",no_results:"没有符合筛选条件的内容。",loading:"正在加载书库……",close:"关闭",no_file:"请先打开一个备份文件——选择一个来浏览。",pick_file:"选择 .jwlibrary 文件",count_one:"{n} 项",count_many:"{n} 项",color_all:"全部颜色",no_title:"无标题",copy:"复制",copied:"已复制",clear:"清除",error:"无法加载：",pub_all:"全部出版物",tag_all:"全部标签",back:"← 返回",detail_empty:"请从列表中选择一项。",sort_newest:"最新在前",sort_oldest:"最早在前",sort_pub:"按出版物",modified:"修改于",no_content:"（无内容）",too_many:"显示 {total} 项中的前 {n} 项——请缩小搜索范围。",pg_prev:"上一页",pg_next:"下一页",pg_status:"第 {page} / {pages} 页 · 共 {total} 条结果",err_corrupt:"这个文件不是可读的 .jwlibrary 备份——它可能已损坏，或者不是正确的文件类型。",err_no_db:"这个备份缺少笔记数据库（userData.db）。请从 JW Library 重新导出。",err_not_sqlite:"无法打开该备份的数据库——文件可能已损坏。",tab_notes:"笔记",tab_highlights:"标注",tab_bookmarks:"书签",hl_label:"标注",hl_no_text:"已标注的段落（正文在出版物中，不在备份里）。",hl_with_note:"附带笔记",bm_label:"书签",bm_slot:"第 {n} 位",linked_note:"关联的笔记：",edit:"编辑",save:"保存",cancel:"取消",delete_item:"删除",export_db:"导出 .jwlibrary",n_edits:"{n} 处修改",n_edits_many:"{n} 处修改",add_tag:"+ 添加标签",new_tag_ph:"标签名称……",delete_note_confirm:"要删除这条笔记吗？此操作无法撤销。",delete_hl_confirm:"要删除这处标注吗？此操作无法撤销。",delete_bm_confirm:"要删除这个书签吗？此操作无法撤销。",yes_delete:"是的，删除",change_color:"颜色",unsaved_exit:"你有 {n} 处修改尚未保存。要不导出就关闭吗？",title_label:"标题",content_label:"内容",tags_label:"标签",hl_color_label:"标注颜色",bm_title_label:"书签标题",plain_text_note:"保存时格式会简化为纯文本",rte_bold:"加粗",rte_italic:"斜体",rte_underline:"下划线",rte_bullets:"项目符号列表",rich_text_note:"可使用加粗、斜体和列表编辑——格式会被保留",date_from:"从",date_to:"到",date_range:"按日期筛选",extract_range:"提取日期范围",extract_none:"这个日期范围内没有笔记。",extract_hint:"保存一个只含该日期范围内笔记的新 .jwlibrary 文件。",copy_md:"复制为 Markdown",export_md:"导出 Markdown",md_hint:"把显示的笔记下载为 Markdown 文件（.zip）",sel_mode:"选择",sel_done:"完成",sel_all:"全部",sel_none:"全不选",sel_count:"已选 {n} 项",batch_tag:"标签",batch_color:"颜色",batch_delete:"删除",batch_delete_confirm:"要删除 {n} 项吗？导出前仍可撤销。",batch_tag_ph:"标签名称……",batch_add:"添加",undo:"撤销",redo:"重做",tab_inputfields:"研究答案",if_label:"研究答案",if_question:"问题",if_answer:"你的答案",if_empty:"（还没有答案）",delete_if_confirm:"要删除这条答案吗？导出前仍可撤销。",share_action:"分享",share_title:"分享笔记",share_intro:"这会生成一个由你亲自转交的文件——任何内容都不会上传。它包含笔记正文，所以请只分享给你信任的人。",share_count:"{n} 条笔记",share_download:"下载文件",share_copy:"复制",share_tag:"已分享",receive_action:"接收",receive_title:"接收分享的笔记",receive_intro:"粘贴分享的文本，或选择别人发给你的 .jwshare.json 文件。",receive_paste_ph:"在此粘贴分享的笔记……",receive_choose:"选择文件",receive_preview:"预览",receive_invalid:"这看起来不是有效的分享笔记数据。",preview_readonly:"预览",adopt:"把 {n} 条添加到我的书库",adopt_need_lib:"请先打开一个备份",adopted:"已添加 {n} 条笔记（标签为「已分享」）。",open_share:"分享笔记 →",ask_btn:"提问",ask_title:"问问你的书库",ask_sub:"按含义搜索你的笔记，而不只是关键词——用平常的话提问，即使措辞不同也能找到相关笔记。全部在你的设备上运行。",ask_placeholder:"例如：关于在压力下保持忠诚的笔记",ask_go:"搜索",ask_enable_title:"开启语义搜索",ask_enable_body:"一个小型语言模型会在你的浏览器中运行，用来理解你的笔记。它只需下载一次，之后会缓存供离线使用，任何内容都不会离开你的设备。",ask_model_fast_name:"轻量（最快）",ask_model_fast_desc:"3 层模型——速度约为英语模型的 2 倍，下载体积减半。非常适合大型书库。",ask_model_en_name:"英语",ask_model_en_desc:"适用于以英语撰写的笔记，准确度标准。",ask_model_multi_name:"多语言",ask_model_multi_desc:"支持 50 多种语言——如果你用多种语言写笔记，请选这个。",ask_size_once:"约 {n} MB · 仅需一次",ask_privacy:"100% 私密——模型和你的笔记绝不会离开这台设备。",ask_loading_model:"正在下载搜索模型…… {pct}%",ask_building:"正在读取你的笔记…… {done} / {total}",ask_ready:"准备就绪——请在上方提问。",ask_searching:"正在搜索……",ask_results_head:"最相关的 {n} 条笔记",ask_no_results:"没有找到相关笔记。试试换个说法。",ask_no_notes:"这个书库还没有可搜索的笔记。",ask_err:"无法加载搜索模型。请检查网络连接后重试。",ask_rebuild:"重建索引",ask_match:"{pct}% 匹配",batch_tagged_ok:"已为 {n} 条笔记添加标签",ask_switch_model:"换一个模型",change_file:"更换文件"},pl:{title:"Eksplorator studium",search:"Szukaj...",no_results:"Nic nie pasuje do Twoich filtrów.",loading:"Wczytywanie biblioteki...",close:"Zamknij",no_file:"Najpierw otwórz plik kopii zapasowej — wybierz go do przeglądania.",pick_file:"Wybierz plik .jwlibrary",count_one:"{n} element",count_many:"{n} elementów",color_all:"Wszystkie kolory",no_title:"Bez tytułu",copy:"Kopiuj",copied:"Skopiowano",clear:"Wyczyść",error:"Nie udało się wczytać:",pub_all:"Wszystkie publikacje",tag_all:"Wszystkie etykiety",back:"← Wstecz",detail_empty:"Wybierz element z listy.",sort_newest:"Najpierw najnowsze",sort_oldest:"Najpierw najstarsze",sort_pub:"Według publikacji",modified:"Zmieniono",no_content:"(Brak treści)",too_many:"Pokazano pierwsze {n} z {total} — zawęź wyszukiwanie.",pg_prev:"Wstecz",pg_next:"Dalej",pg_status:"Strona {page} z {pages} · {total} wyników",err_corrupt:"Ten plik nie jest możliwą do odczytu kopią zapasową .jwlibrary — może być uszkodzony albo to niewłaściwy typ pliku.",err_no_db:"W tej kopii zapasowej brakuje bazy danych notatek (userData.db). Wyeksportuj ją ponownie z JW Library.",err_not_sqlite:"Nie udało się otworzyć bazy danych kopii zapasowej — plik może być uszkodzony.",tab_notes:"Notatki",tab_highlights:"Wyróżnienia",tab_bookmarks:"Zakładki",hl_label:"Wyróżnienie",hl_no_text:"Wyróżniony fragment (tekst znajduje się w publikacji, nie w kopii zapasowej).",hl_with_note:"Z notatką",bm_label:"Zakładka",bm_slot:"Miejsce {n}",linked_note:"Powiązana notatka:",edit:"Edytuj",save:"Zapisz",cancel:"Anuluj",delete_item:"Usuń",export_db:"Eksport .jwlibrary",n_edits:"{n} zmiana",n_edits_many:"{n} zmian",add_tag:"+ Dodaj etykietę",new_tag_ph:"Nazwa etykiety...",delete_note_confirm:"Usunąć tę notatkę? Tej operacji nie można cofnąć.",delete_hl_confirm:"Usunąć to wyróżnienie? Tej operacji nie można cofnąć.",delete_bm_confirm:"Usunąć tę zakładkę? Tej operacji nie można cofnąć.",yes_delete:"Tak, usuń",change_color:"Kolor",unsaved_exit:"Masz {n} niezapisanych zmian. Zamknąć bez eksportu?",title_label:"Tytuł",content_label:"Treść",tags_label:"Etykiety",hl_color_label:"Kolor wyróżnienia",bm_title_label:"Tytuł zakładki",plain_text_note:"Formatowanie zostanie uproszczone do zwykłego tekstu przy zapisie",rte_bold:"Pogrubienie",rte_italic:"Kursywa",rte_underline:"Podkreślenie",rte_bullets:"Lista punktowana",rich_text_note:"Edytuj z pogrubieniem, kursywą i listami — formatowanie zostaje zachowane",date_from:"Od",date_to:"Do",date_range:"Filtruj według daty",extract_range:"Wyodrębnij zakres dat",extract_none:"W tym zakresie dat nie ma notatek.",extract_hint:"Zapisz nowy plik .jwlibrary zawierający tylko notatki z tego zakresu dat.",copy_md:"Kopiuj jako Markdown",export_md:"Eksportuj Markdown",md_hint:"Pobierz wyświetlone notatki jako pliki Markdown (.zip)",sel_mode:"Zaznacz",sel_done:"Gotowe",sel_all:"Wszystkie",sel_none:"Żadne",sel_count:"Zaznaczono: {n}",batch_tag:"Etykieta",batch_color:"Kolor",batch_delete:"Usuń",batch_delete_confirm:"Usunąć {n}? Możesz cofnąć przed eksportem.",batch_tag_ph:"Nazwa etykiety…",batch_add:"Dodaj",undo:"Cofnij",redo:"Ponów",tab_inputfields:"Odpowiedzi do studium",if_label:"Odpowiedź do studium",if_question:"Pytanie",if_answer:"Twoja odpowiedź",if_empty:"(Brak odpowiedzi)",delete_if_confirm:"Usunąć tę odpowiedź? Możesz cofnąć przed eksportem.",share_action:"Udostępnij",share_title:"Udostępnij notatki",share_intro:"Tworzy to plik, który przekazujesz samodzielnie — nic nie jest wysyłane na serwer. Zawiera treść notatek, więc udostępniaj go tylko osobom, którym ufasz.",share_count:"{n} notatek",share_download:"Pobierz plik",share_copy:"Kopiuj",share_tag:"Udostępnione",receive_action:"Odbierz",receive_title:"Odbierz udostępnione notatki",receive_intro:"Wklej udostępniony tekst albo wybierz przysłany plik .jwshare.json.",receive_paste_ph:"Wklej tu udostępnione notatki…",receive_choose:"Wybierz plik",receive_preview:"Podgląd",receive_invalid:"To nie wygląda na prawidłowe dane udostępnionych notatek.",preview_readonly:"Podgląd",adopt:"Dodaj {n} do mojej biblioteki",adopt_need_lib:"Najpierw otwórz kopię zapasową",adopted:"Dodano {n} notatek (z etykietą „Udostępnione”).",open_share:"Udostępnij notatki →",ask_btn:"Zapytaj",ask_title:"Zapytaj swoją bibliotekę",ask_sub:"Przeszukuj swoje notatki według znaczenia, a nie tylko słów kluczowych — pytaj zwykłym językiem i znajduj powiązane notatki, nawet gdy użyto w nich innych słów. Działa w całości na Twoim urządzeniu.",ask_placeholder:"np. notatki o zachowywaniu lojalności pod presją",ask_go:"Szukaj",ask_enable_title:"Włącz wyszukiwanie semantyczne",ask_enable_body:"Mały model językowy działa w Twojej przeglądarce, aby rozumieć Twoje notatki. Pobiera się raz, jest zapisywany do użytku offline i nic nigdy nie opuszcza Twojego urządzenia.",ask_model_fast_name:"Lekki (najszybszy)",ask_model_fast_desc:"Model 3-warstwowy — około 2× szybszy niż angielski i o połowę mniejszy do pobrania. Idealny do dużych bibliotek.",ask_model_en_name:"Angielski",ask_model_en_desc:"Standardowa dokładność dla notatek pisanych po angielsku.",ask_model_multi_name:"Wielojęzyczny",ask_model_multi_desc:"Rozumie ponad 50 języków — wybierz go, jeśli piszesz notatki w więcej niż jednym języku.",ask_size_once:"~{n} MB · jednorazowo",ask_privacy:"100% prywatnie — model i Twoje notatki nigdy nie opuszczają tego urządzenia.",ask_loading_model:"Pobieranie modelu wyszukiwania… {pct}%",ask_building:"Odczytywanie Twoich notatek… {done} / {total}",ask_ready:"Gotowe — zadaj pytanie powyżej.",ask_searching:"Szukanie…",ask_results_head:"{n} najbardziej powiązanych notatek",ask_no_results:"Nie znaleziono powiązanych notatek. Spróbuj sformułować pytanie inaczej.",ask_no_notes:"Ta biblioteka nie ma jeszcze notatek do przeszukania.",ask_err:"Nie udało się wczytać modelu wyszukiwania. Sprawdź połączenie i spróbuj ponownie.",ask_rebuild:"Przebuduj indeks",ask_match:"{pct}% dopasowania",batch_tagged_ok:"Oznaczono etykietą {n} notatek",ask_switch_model:"Użyj innego modelu",change_file:"Zmień plik"},uk:{title:"Оглядач вивчення",search:"Пошук...",no_results:"Нічого не відповідає вашим фільтрам.",loading:"Завантажуємо бібліотеку...",close:"Закрити",no_file:"Спочатку відкрийте файл резервної копії — виберіть його для перегляду.",pick_file:"Вибрати файл .jwlibrary",count_one:"{n} елемент",count_many:"{n} елементів",color_all:"Усі кольори",no_title:"Без назви",copy:"Копіювати",copied:"Скопійовано",clear:"Очистити",error:"Не вдалося завантажити:",pub_all:"Усі публікації",tag_all:"Усі теги",back:"← Назад",detail_empty:"Виберіть елемент зі списку.",sort_newest:"Спочатку нові",sort_oldest:"Спочатку старі",sort_pub:"За публікацією",modified:"Змінено",no_content:"(Немає вмісту)",too_many:"Показано перші {n} з {total} — звузьте пошук.",pg_prev:"Назад",pg_next:"Далі",pg_status:"Сторінка {page} з {pages} · {total} результатів",err_corrupt:"Цей файл не є придатною до читання резервною копією .jwlibrary — можливо, він пошкоджений або це файл іншого типу.",err_no_db:"У цій резервній копії бракує бази даних нотаток (userData.db). Експортуйте її з JW Library ще раз.",err_not_sqlite:"Не вдалося відкрити базу даних резервної копії — можливо, файл пошкоджено.",tab_notes:"Нотатки",tab_highlights:"Виділення",tab_bookmarks:"Закладки",hl_label:"Виділення",hl_no_text:"Виділений уривок (текст міститься в публікації, а не в резервній копії).",hl_with_note:"З нотаткою",bm_label:"Закладка",bm_slot:"Комірка {n}",linked_note:"Пов'язана нотатка:",edit:"Редагувати",save:"Зберегти",cancel:"Скасувати",delete_item:"Видалити",export_db:"Експорт .jwlibrary",n_edits:"{n} правка",n_edits_many:"{n} правок",add_tag:"+ Додати тег",new_tag_ph:"Назва тега...",delete_note_confirm:"Видалити цю нотатку? Цю дію не можна скасувати.",delete_hl_confirm:"Видалити це виділення? Цю дію не можна скасувати.",delete_bm_confirm:"Видалити цю закладку? Цю дію не можна скасувати.",yes_delete:"Так, видалити",change_color:"Колір",unsaved_exit:"У вас {n} незбережених правок. Закрити без експорту?",title_label:"Назва",content_label:"Вміст",tags_label:"Теги",hl_color_label:"Колір виділення",bm_title_label:"Назва закладки",plain_text_note:"Під час збереження форматування спроститься до звичайного тексту",rte_bold:"Жирний",rte_italic:"Курсив",rte_underline:"Підкреслений",rte_bullets:"Маркований список",rich_text_note:"Редагуйте з жирним, курсивом і списками — форматування зберігається",date_from:"Від",date_to:"До",date_range:"Фільтр за датою",extract_range:"Вибірка за діапазоном дат",extract_none:"У цьому діапазоні дат немає нотаток.",extract_hint:"Збережіть новий файл .jwlibrary лише з нотатками з цього діапазону дат.",copy_md:"Копіювати як Markdown",export_md:"Експорт у Markdown",md_hint:"Завантажте показані нотатки як файли Markdown (.zip)",sel_mode:"Вибрати",sel_done:"Готово",sel_all:"Усі",sel_none:"Жодного",sel_count:"Вибрано: {n}",batch_tag:"Тег",batch_color:"Колір",batch_delete:"Видалити",batch_delete_confirm:"Видалити {n}? Це можна скасувати до експорту.",batch_tag_ph:"Назва тега…",batch_add:"Додати",undo:"Скасувати",redo:"Повторити",tab_inputfields:"Відповіді для вивчення",if_label:"Відповідь для вивчення",if_question:"Запитання",if_answer:"Ваша відповідь",if_empty:"(Відповіді ще немає)",delete_if_confirm:"Видалити цю відповідь? Це можна скасувати до експорту.",share_action:"Поділитися",share_title:"Поділитися нотатками",share_intro:"Це створює файл, який ви передаєте самі — нічого не надсилається на сервер. Він містить текст нотаток, тож діліться ним лише з людьми, яким довіряєте.",share_count:"{n} нотаток",share_download:"Завантажити файл",share_copy:"Копіювати",share_tag:"Спільні",receive_action:"Отримати",receive_title:"Отримати спільні нотатки",receive_intro:"Вставте спільний текст або виберіть файл .jwshare.json, який вам надіслали.",receive_paste_ph:"Вставте сюди спільні нотатки…",receive_choose:"Вибрати файл",receive_preview:"Перегляд",receive_invalid:"Це не схоже на дійсні дані спільних нотаток.",preview_readonly:"Перегляд",adopt:"Додати {n} до моєї бібліотеки",adopt_need_lib:"Спочатку відкрийте резервну копію",adopted:"Додано нотаток: {n} (з тегом «Спільні»).",open_share:"Поділитися нотатками →",ask_btn:"Запитати",ask_title:"Запитайте свою бібліотеку",ask_sub:"Шукайте у своїх нотатках за змістом, а не лише за ключовими словами — запитуйте звичайною мовою і знаходьте пов'язані нотатки, навіть якщо в них ужито інші слова. Працює повністю на вашому пристрої.",ask_placeholder:"наприклад, нотатки про збереження вірності під тиском",ask_go:"Шукати",ask_enable_title:"Увімкнути семантичний пошук",ask_enable_body:"Невелика мовна модель працює у вашому браузері, щоб розуміти ваші нотатки. Вона завантажується один раз, кешується для роботи офлайн, і нічого ніколи не залишає ваш пристрій.",ask_model_fast_name:"Легка (найшвидша)",ask_model_fast_desc:"3-шарова модель — приблизно вдвічі швидша за англійську і вдвічі менша за розміром. Ідеально для великих бібліотек.",ask_model_en_name:"Англійська",ask_model_en_desc:"Стандартна точність для нотаток, написаних англійською.",ask_model_multi_name:"Багатомовна",ask_model_multi_desc:"Розуміє понад 50 мов — виберіть її, якщо пишете нотатки більш ніж однією мовою.",ask_size_once:"~{n} МБ · один раз",ask_privacy:"100% приватно — модель і ваші нотатки ніколи не залишають цей пристрій.",ask_loading_model:"Завантажуємо модель пошуку… {pct}%",ask_building:"Читаємо ваші нотатки… {done} / {total}",ask_ready:"Готово — поставте запитання вгорі.",ask_searching:"Шукаємо…",ask_results_head:"{n} найбільш пов'язаних нотаток",ask_no_results:"Пов'язаних нотаток не знайдено. Спробуйте переформулювати запитання.",ask_no_notes:"У цій бібліотеці ще немає нотаток для пошуку.",ask_err:"Не вдалося завантажити модель пошуку. Перевірте з'єднання і спробуйте ще раз.",ask_rebuild:"Перебудувати індекс",ask_match:"{pct}% збігу",batch_tagged_ok:"Позначено тегом нотаток: {n}",ask_switch_model:"Використати іншу модель",change_file:"Змінити файл"},he:{title:"סייר הלימוד",search:"חיפוש...",no_results:"שום דבר לא תואם את המסננים שלכם.",loading:"טוען את הספרייה...",close:"סגירה",no_file:"פתחו קודם קובץ גיבוי — בחרו אחד לעיון.",pick_file:"בחירת קובץ ‎.jwlibrary",count_one:"פריט אחד",count_many:"{n} פריטים",color_all:"כל הצבעים",no_title:"ללא כותרת",copy:"העתקה",copied:"הועתק",clear:"ניקוי",error:"לא ניתן לטעון:",pub_all:"כל הפרסומים",tag_all:"כל התוויות",back:"← חזרה",detail_empty:"בחרו פריט מהרשימה.",sort_newest:"החדשות תחילה",sort_oldest:"הישנות תחילה",sort_pub:"לפי פרסום",modified:"שונתה",no_content:"(אין תוכן)",too_many:"מוצגים {n} הראשונים מתוך {total} — צמצמו את החיפוש.",pg_prev:"הקודם",pg_next:"הבא",pg_status:"עמוד {page} מתוך {pages} · {total} תוצאות",err_corrupt:"הקובץ הזה אינו גיבוי ‎.jwlibrary קריא — ייתכן שהוא פגום או שזה סוג קובץ שגוי.",err_no_db:"בגיבוי הזה חסר מסד הנתונים של ההערות (userData.db). ייצאו אותו מחדש מ-JW Library.",err_not_sqlite:"לא הצלחנו לפתוח את מסד הנתונים של הגיבוי — ייתכן שהקובץ פגום.",tab_notes:"הערות",tab_highlights:"הדגשות",tab_bookmarks:"סימניות",hl_label:"הדגשה",hl_no_text:"קטע מודגש (הטקסט נמצא בפרסום, לא בגיבוי).",hl_with_note:"עם הערה",bm_label:"סימנייה",bm_slot:"משבצת {n}",linked_note:"הערה מקושרת:",edit:"עריכה",save:"שמירה",cancel:"ביטול",delete_item:"מחיקה",export_db:"ייצוא ‎.jwlibrary",n_edits:"עריכה אחת",n_edits_many:"{n} עריכות",add_tag:"+ הוספת תווית",new_tag_ph:"שם התווית...",delete_note_confirm:"למחוק את ההערה הזו? אי אפשר לבטל את הפעולה.",delete_hl_confirm:"למחוק את ההדגשה הזו? אי אפשר לבטל את הפעולה.",delete_bm_confirm:"למחוק את הסימנייה הזו? אי אפשר לבטל את הפעולה.",yes_delete:"כן, מחק",change_color:"צבע",unsaved_exit:"יש לכם {n} עריכות שלא נשמרו. לסגור בלי לייצא?",title_label:"כותרת",content_label:"תוכן",tags_label:"תוויות",hl_color_label:"צבע ההדגשה",bm_title_label:"כותרת הסימנייה",plain_text_note:"העיצוב יפושט לטקסט רגיל בשמירה",rte_bold:"מודגש",rte_italic:"נטוי",rte_underline:"קו תחתון",rte_bullets:"רשימת תבליטים",rich_text_note:"ערכו עם הדגשה, נטוי ורשימות — העיצוב נשמר",date_from:"מ-",date_to:"עד",date_range:"סינון לפי תאריך",extract_range:"חילוץ טווח תאריכים",extract_none:"אין הערות בטווח התאריכים הזה.",extract_hint:"שמרו קובץ ‎.jwlibrary חדש עם ההערות שבטווח התאריכים הזה בלבד.",copy_md:"העתקה כ-Markdown",export_md:"ייצוא Markdown",md_hint:"הורידו את ההערות המוצגות כקובצי Markdown‏ (.zip)",sel_mode:"בחירה",sel_done:"סיום",sel_all:"הכול",sel_none:"כלום",sel_count:"{n} נבחרו",batch_tag:"תווית",batch_color:"צבע",batch_delete:"מחיקה",batch_delete_confirm:"למחוק {n}? אפשר לבטל לפני הייצוא.",batch_tag_ph:"שם התווית…",batch_add:"הוספה",undo:"ביטול",redo:"ביצוע מחדש",tab_inputfields:"תשובות ללימוד",if_label:"תשובה ללימוד",if_question:"שאלה",if_answer:"התשובה שלכם",if_empty:"(אין עדיין תשובה)",delete_if_confirm:"למחוק את התשובה הזו? אפשר לבטל לפני הייצוא.",share_action:"שיתוף",share_title:"שיתוף הערות",share_intro:"זה יוצר קובץ שאתם מעבירים בעצמכם — שום דבר לא מועלה לשרת. הוא מכיל את טקסט ההערות, אז שתפו רק עם אנשים שאתם סומכים עליהם.",share_count:"{n} הערות",share_download:"הורדת הקובץ",share_copy:"העתקה",share_tag:"משותף",receive_action:"קבלה",receive_title:"קבלת הערות משותפות",receive_intro:"הדביקו טקסט משותף, או בחרו קובץ ‎.jwshare.json שמישהו שלח לכם.",receive_paste_ph:"הדביקו כאן הערות משותפות…",receive_choose:"בחירת קובץ",receive_preview:"תצוגה מקדימה",receive_invalid:"זה לא נראה כמו נתוני הערות משותפות תקינים.",preview_readonly:"תצוגה מקדימה",adopt:"אימוץ {n} לספרייה שלי",adopt_need_lib:"פתחו קודם גיבוי",adopted:"‏{n} הערות אומצו (תויגו \"משותף\").",open_share:"שיתוף הערות ←",ask_btn:"שאלו",ask_title:"שאלו את הספרייה שלכם",ask_sub:"חפשו בהערות שלכם לפי משמעות, לא רק לפי מילות מפתח — שאלו בשפה פשוטה ומצאו הערות קשורות גם כשהן משתמשות במילים אחרות. רץ לגמרי על המכשיר שלכם.",ask_placeholder:"למשל: הערות על שמירת נאמנות תחת לחץ",ask_go:"חיפוש",ask_enable_title:"הפעילו חיפוש סמנטי",ask_enable_body:"מודל שפה קטן רץ בדפדפן שלכם כדי להבין את ההערות שלכם. הוא יורד פעם אחת, נשמר במטמון לשימוש לא מקוון, ושום דבר לעולם לא עוזב את המכשיר שלכם.",ask_model_fast_name:"קל (המהיר ביותר)",ask_model_fast_desc:"מודל בן 3 שכבות — מהיר פי 2 בערך מהאנגלי וחצי מגודל ההורדה. מושלם לספריות גדולות.",ask_model_en_name:"אנגלית",ask_model_en_desc:"דיוק סטנדרטי להערות שנכתבו באנגלית.",ask_model_multi_name:"רב-לשוני",ask_model_multi_desc:"מבין יותר מ-50 שפות — בחרו בזה אם אתם כותבים הערות ביותר משפה אחת.",ask_size_once:"~{n} MB · חד-פעמי",ask_privacy:"‏100% פרטי — המודל וההערות שלכם לעולם לא עוזבים את המכשיר הזה.",ask_loading_model:"מוריד את מודל החיפוש… {pct}%",ask_building:"קורא את ההערות שלכם… {done} / {total}",ask_ready:"מוכן — שאלו שאלה למעלה.",ask_searching:"מחפש…",ask_results_head:"{n} ההערות הקשורות ביותר",ask_no_results:"לא נמצאו הערות קשורות. נסו לנסח את השאלה אחרת.",ask_no_notes:"אין עדיין הערות לחיפוש בספרייה הזו.",ask_err:"לא הצלחנו לטעון את מודל החיפוש. בדקו את החיבור ונסו שוב.",ask_rebuild:"בנייה מחדש של האינדקס",ask_match:"{pct}% התאמה",batch_tagged_ok:"‏{n} הערות תויגו",ask_switch_model:"שימוש במודל אחר",change_file:"החלפת הקובץ"},ar:{title:"مستكشف الدرس",search:"بحث...",no_results:"لا شيء يطابق عوامل التصفية.",loading:"جارٍ تحميل المكتبة...",close:"إغلاق",no_file:"افتح ملف نسخة احتياطية أولًا — اختر واحدًا للتصفّح.",pick_file:"اختر ملف ‎.jwlibrary‎",count_one:"{n} عنصر",count_many:"{n} عنصرًا",color_all:"كل الألوان",no_title:"بلا عنوان",copy:"نسخ",copied:"تم النسخ",clear:"مسح",error:"تعذّر التحميل:",pub_all:"كل المطبوعات",tag_all:"كل الوسوم",back:"→ رجوع",detail_empty:"اختر عنصرًا من القائمة.",sort_newest:"الأحدث أولًا",sort_oldest:"الأقدم أولًا",sort_pub:"حسب المطبوعة",modified:"عُدِّلت",no_content:"(بلا محتوى)",too_many:"يُعرض أول {n} من {total} — ضيّق نطاق البحث.",pg_prev:"السابق",pg_next:"التالي",pg_status:"صفحة {page} من {pages} · {total} نتيجة",err_corrupt:"هذا الملف ليس نسخة احتياطية ‎.jwlibrary‎ قابلة للقراءة — قد يكون تالفًا أو من نوع غير صحيح.",err_no_db:"تفتقر هذه النسخة الاحتياطية إلى قاعدة بيانات الملاحظات (userData.db). أعد تصديرها من JW Library.",err_not_sqlite:"تعذّر فتح قاعدة بيانات النسخة الاحتياطية — قد يكون الملف تالفًا.",tab_notes:"الملاحظات",tab_highlights:"التظليلات",tab_bookmarks:"العلامات المرجعية",hl_label:"تظليل",hl_no_text:"مقطع مظلَّل (النص موجود في المطبوعة لا في النسخة الاحتياطية).",hl_with_note:"مع ملاحظة",bm_label:"علامة مرجعية",bm_slot:"الخانة {n}",linked_note:"ملاحظة مرتبطة:",edit:"تحرير",save:"حفظ",cancel:"إلغاء",delete_item:"حذف",export_db:"تصدير ‎.jwlibrary‎",n_edits:"{n} تعديل",n_edits_many:"{n} تعديلًا",add_tag:"+ أضف وسمًا",new_tag_ph:"اسم الوسم...",delete_note_confirm:"هل تريد حذف هذه الملاحظة؟ لا يمكن التراجع عن هذا.",delete_hl_confirm:"هل تريد حذف هذا التظليل؟ لا يمكن التراجع عن هذا.",delete_bm_confirm:"هل تريد حذف هذه العلامة المرجعية؟ لا يمكن التراجع عن هذا.",yes_delete:"نعم، احذف",change_color:"اللون",unsaved_exit:"لديك {n} تعديل غير محفوظ. هل تغلق دون تصدير؟",title_label:"العنوان",content_label:"المحتوى",tags_label:"الوسوم",hl_color_label:"لون التظليل",bm_title_label:"عنوان العلامة المرجعية",plain_text_note:"يُبسَّط التنسيق إلى نص عادي عند الحفظ",rte_bold:"عريض",rte_italic:"مائل",rte_underline:"تسطير",rte_bullets:"قائمة نقطية",rich_text_note:"حرّر بخط عريض ومائل وقوائم — يُحفظ التنسيق",date_from:"من",date_to:"إلى",date_range:"تصفية حسب التاريخ",extract_range:"استخرج نطاق التاريخ",extract_none:"لا توجد ملاحظات ضمن هذا النطاق الزمني.",extract_hint:"احفظ ملف ‎.jwlibrary‎ جديدًا يحتوي فقط على ملاحظات هذا النطاق الزمني.",copy_md:"انسخ بصيغة Markdown",export_md:"صدّر Markdown",md_hint:"نزّل الملاحظات المعروضة كملفات Markdown (‎.zip‎)",sel_mode:"تحديد",sel_done:"تم",sel_all:"الكل",sel_none:"لا شيء",sel_count:"{n} محدّدة",batch_tag:"وسم",batch_color:"لون",batch_delete:"حذف",batch_delete_confirm:"هل تحذف {n}؟ يمكنك التراجع قبل التصدير.",batch_tag_ph:"اسم الوسم…",batch_add:"أضف",undo:"تراجع",redo:"إعادة",tab_inputfields:"إجابات الدرس",if_label:"إجابة درس",if_question:"السؤال",if_answer:"إجابتك",if_empty:"(لا توجد إجابة بعد)",delete_if_confirm:"هل تحذف إجابة الدرس هذه؟ يمكنك التراجع قبل التصدير.",share_action:"مشاركة",share_title:"مشاركة الملاحظات",share_intro:"ينشئ هذا ملفًا تسلّمه بنفسك — ولا يُرفع أي شيء. يحتوي على نص الملاحظات، فشاركه فقط مع من تثق بهم.",share_count:"{n} ملاحظة",share_download:"تنزيل الملف",share_copy:"نسخ",share_tag:"مُشارَكة",receive_action:"استلام",receive_title:"استلام ملاحظات مُشارَكة",receive_intro:"الصق النص المُشارَك، أو اختر ملف ‎.jwshare.json‎ أرسله إليك أحدهم.",receive_paste_ph:"الصق الملاحظات المُشارَكة هنا…",receive_choose:"اختر ملفًا",receive_preview:"معاينة",receive_invalid:"لا تبدو هذه بيانات ملاحظات مُشارَكة صالحة.",preview_readonly:"معاينة",adopt:"أضف {n} إلى مكتبتي",adopt_need_lib:"افتح نسخة احتياطية أولًا",adopted:"أُضيفت {n} ملاحظة (بوسم \"مُشارَكة\").",open_share:"مشاركة الملاحظات ←",ask_btn:"اسأل",ask_title:"اسأل مكتبتك",ask_sub:"ابحث في ملاحظاتك بالمعنى لا بالكلمات المفتاحية فقط — اسأل بلغة عادية وستجد الملاحظات ذات الصلة حتى لو استعملت ألفاظًا مختلفة. يعمل بالكامل على جهازك.",ask_placeholder:"مثال: ملاحظات عن الثبات على الولاء تحت الضغط",ask_go:"بحث",ask_enable_title:"فعّل البحث الدلالي",ask_enable_body:"يعمل نموذج لغوي صغير داخل متصفحك لفهم ملاحظاتك. يُنزَّل مرة واحدة، ويُخزَّن للاستخدام دون اتصال، ولا يغادر جهازك شيء أبدًا.",ask_model_fast_name:"خفيف (الأسرع)",ask_model_fast_desc:"نموذج من 3 طبقات — أسرع نحو مرتين من الإنجليزي وبنصف حجم التنزيل. مثالي للمكتبات الكبيرة.",ask_model_en_name:"الإنجليزي",ask_model_en_desc:"دقة قياسية للملاحظات المكتوبة بالإنجليزية.",ask_model_multi_name:"متعدّد اللغات",ask_model_multi_desc:"يفهم أكثر من 50 لغة — اختره إذا كنت تكتب ملاحظاتك بأكثر من لغة.",ask_size_once:"~{n} ميغابايت · مرة واحدة",ask_privacy:"خصوصية 100% — النموذج وملاحظاتك لا يغادران هذا الجهاز أبدًا.",ask_loading_model:"جارٍ تنزيل نموذج البحث… {pct}%",ask_building:"جارٍ قراءة ملاحظاتك… {done} / {total}",ask_ready:"جاهز — اطرح سؤالك أعلاه.",ask_searching:"جارٍ البحث…",ask_results_head:"أكثر {n} ملاحظات صلة",ask_no_results:"لم يُعثر على ملاحظات ذات صلة. جرّب صياغة سؤالك بشكل مختلف.",ask_no_notes:"لا تحتوي هذه المكتبة على ملاحظات للبحث فيها بعد.",ask_err:"تعذّر تحميل نموذج البحث. تحقّق من اتصالك وحاول مرة أخرى.",ask_rebuild:"أعِد بناء الفهرس",ask_match:"تطابق {pct}%",batch_tagged_ok:"تم وسم {n} ملاحظة",ask_switch_model:"استخدم نموذجًا آخر",change_file:"غيّر الملف"}};
  function curLang(){ try{return localStorage.getItem('jwsync_lang')||'en';}catch(_){return 'en';} }
  function t(k, vars){
    var lang = curLang();
    var s = (I18N[lang] && I18N[lang][k]) || I18N.en[k] || k;
    if(vars){ Object.keys(vars).forEach(function(v){ s = s.split('{'+v+'}').join(vars[v]); }); }
    return s;
  }

  // ---------- constants ----------
  var BIBLE = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"];
  var COLORS = [null, "#fbbf24", "#4ade80", "#60a5fa", "#f87171", "#fb923c", "#c084fc"];
  var MAX_ROWS = 2000;
  var PAGE_SIZE = 200;

  // ---------- helpers ----------
  function htmlEscape(s){
    if(s == null) return '';
    return String(s).replace(/[&<>"']/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }
  function fastStripHtml(s){
    if(!s) return '';
    return String(s).replace(/<[^>]*>/g,' ').replace(/&nbsp;/gi,' ').replace(/&amp;/gi,'&').replace(/&lt;/gi,'<').replace(/&gt;/gi,'>').replace(/&quot;/gi,'"').replace(/&#39;/g,"'").replace(/\s+/g,' ').trim();
  }
  function stripHtml(s){
    if(!s) return '';
    var d = document.createElement('div');
    d.innerHTML = String(s);
    return (d.textContent || '').replace(/\s+/g, ' ').trim();
  }
  function stripHtmlPreserve(s){
    var sentinel = 'JBNLZ9';
    var html = String(s || '').replace(/\n/g, sentinel);
    var d = document.createElement('div');
    d.innerHTML = html;
    var txt = d.textContent || '';
    return txt.split(sentinel).join('\n').replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n').trim();
  }
  function pubLabel(row){
    if(!row) return '';
    var bn = row.BookNumber, ch = row.ChapterNumber;
    if(bn && bn >= 1 && bn <= 66){
      var name = BIBLE[bn-1] || ('Book ' + bn);
      return ch ? (name + ' ' + ch) : name;
    }
    return row.LocTitle || row.KeySymbol || '';
  }
  function fmtDate(s){
    if(!s) return '';
    var d = new Date(String(s).replace(' ', 'T'));
    if(isNaN(d.getTime())) return s;
    try{ return d.toLocaleDateString(curLang(), {year:'numeric',month:'short',day:'numeric'}); }
    catch(_){ return d.toISOString().slice(0,10); }
  }
  function rowsFromExec(db, sql){
    try {
      var r = db.exec(sql);
      if(!r[0]) return [];
      var cols = r[0].columns;
      return r[0].values.map(function(v){
        var o = {}; for(var i=0;i<cols.length;i++) o[cols[i]] = v[i]; return o;
      });
    } catch(e){ return []; }
  }
  function pad2(n){ return n < 10 ? '0'+n : String(n); }
  function nowTimestamp(){
    var d = new Date();
    return d.getFullYear()+'-'+pad2(d.getMonth()+1)+'-'+pad2(d.getDate())+
      ' '+pad2(d.getHours())+':'+pad2(d.getMinutes())+':'+pad2(d.getSeconds());
  }
  function plainTextToNoteHtml(text){
    if(!text || !text.trim()) return '';
    var paras = text.trim().split(/\n\n+/);
    var result = paras.map(function(p){
      return '<p>' + htmlEscape(p.trim()).replace(/\n/g, '<br />') + '</p>';
    }).filter(function(p){ return p !== '<p></p>'; });
    return result.join('');
  }
  // Allow-list sanitizer for JW Library note HTML (round-trips formatting safely)
  function sanitizeNoteHtml(html){
    var ALLOWED={P:1,BR:1,B:1,STRONG:1,I:1,EM:1,U:1,UL:1,OL:1,LI:1};
    var DROP={SCRIPT:1,STYLE:1,NOSCRIPT:1,IFRAME:1,OBJECT:1,EMBED:1,LINK:1,META:1};
    var root=document.createElement('div');
    root.innerHTML=String(html==null?'':html);
    (function walk(node){
      var kids=Array.prototype.slice.call(node.childNodes);
      for(var i=0;i<kids.length;i++){
        var ch=kids[i];
        if(ch.nodeType===3) continue;
        if(ch.nodeType!==1){ if(ch.parentNode) ch.parentNode.removeChild(ch); continue; }
        var tag=ch.tagName;
        if(DROP[tag]){ ch.parentNode.removeChild(ch); continue; }
        walk(ch);
        if(tag==='DIV'){
          var p=document.createElement('p');
          while(ch.firstChild) p.appendChild(ch.firstChild);
          ch.parentNode.replaceChild(p,ch);
        } else if(ALLOWED[tag]){
          for(var a=ch.attributes.length-1;a>=0;a--) ch.removeAttribute(ch.attributes[a].name);
        } else {
          var par=ch.parentNode;
          while(ch.firstChild) par.insertBefore(ch.firstChild,ch);
          par.removeChild(ch);
        }
      }
    })(root);
    var out=root.innerHTML.trim();
    if(out && !/^\s*<(p|ul|ol)\b/i.test(out)) out='<p>'+out+'</p>';
    return out;
  }
  // Minimal dependency-free WYSIWYG (bold/italic/underline/bullets) for note content
  function buildRteEditor(initialHtml){
    var wrap=document.createElement('div'); wrap.className='jb-rte-wrap';
    var bar=document.createElement('div'); bar.className='jb-rte-toolbar';
    var rte=document.createElement('div'); rte.className='jb-edit-rte'; rte.setAttribute('contenteditable','true');
    rte.innerHTML=sanitizeNoteHtml(initialHtml)||'';
    [['bold','rte_bold','B'],['italic','rte_italic','I'],['underline','rte_underline','U'],['insertUnorderedList','rte_bullets','\u2022']].forEach(function(spec){
      var b=document.createElement('button'); b.type='button'; b.className='jb-rte-btn'; b.textContent=spec[2];
      b.title=t(spec[1]); b.setAttribute('aria-label',t(spec[1]));
      b.onmousedown=function(e){ e.preventDefault(); };
      b.onclick=function(){ rte.focus(); try{document.execCommand('styleWithCSS',false,false);}catch(_){} try{document.execCommand(spec[0],false,null);}catch(_){} };
      bar.appendChild(b);
    });
    wrap.appendChild(bar); wrap.appendChild(rte);
    return { wrap: wrap, el: rte, getHtml: function(){ return sanitizeNoteHtml(rte.innerHTML); } };
  }

  // ---------- state ----------
  var state = {
    activeType: 'notes',
    allNotes: [], allHighlights: [], allBookmarks: [],
    tagsByNote: {}, tagsByHighlight: {}, tagsByLocation: {},
    allTags: [], allPublications: [],
    filtered: [], selected: null, page: 0,
    search: '', color: '', tagId: '', pubId: '', dateFrom: '', dateTo: '', sort: 'newest',
    overlay: null,
    db: null, fileName: '', dirty: 0, editingId: null,
    SQL: null, undo: [], redo: [], selection: new Set(), selectMode: false, _inBatch: false, _batchUI: 'idle', _batchTaggedCount: 0,
    allInputFields: [],
    askMode: false, askResults: [], askQuery: '', askPhase: 'idle', askProgress: 0, askError: '',
    hayGen: 1
  };

  // ---------- DB mutations ----------
  function markDirty(){
    state.dirty++;
    state.hayGen++;
    updateDirtyBadge();
  }
  function updateDirtyBadge(){
    if(!state.overlay) return;
    var badge = state.overlay.querySelector('.jb-dirty-badge');
    var exportBtn = state.overlay.querySelector('.jb-export-btn');
    if(badge){
      badge.textContent = state.dirty === 1 ? t('n_edits',{n:1}) : t('n_edits_many',{n:state.dirty});
      badge.style.display = state.dirty > 0 ? '' : 'none';
    }
    if(exportBtn){ exportBtn.disabled = (state.dirty === 0); }
  }

  function saveNote(noteId, title, content, isHtml){
    if(!state.db) return false;
    snapshot();
    var now = nowTimestamp();
    var html = isHtml ? sanitizeNoteHtml(content) : plainTextToNoteHtml(content);
    try{
      state.db.run('UPDATE Note SET Title=?, Content=?, LastModified=? WHERE NoteId=?',[title||'',html,now,noteId]);
    }catch(e){ console.error('[jb] saveNote',e); return false; }
    for(var i=0;i<state.allNotes.length;i++){
      if(state.allNotes[i].NoteId===noteId){
        state.allNotes[i].Title=title||'';
        state.allNotes[i].Content=html;
        state.allNotes[i].LastModified=now;
        if(state.selected&&state.selected.NoteId===noteId) state.selected=state.allNotes[i];
        break;
      }
    }
    return true;
  }

  function deleteNote(noteId){
    if(!state.db) return;
    snapshot();
    try{
      state.db.run('DELETE FROM TagMap WHERE NoteId=?',[noteId]);
      state.db.run('DELETE FROM Note WHERE NoteId=?',[noteId]);
    }catch(e){ console.error('[jb] deleteNote',e); return; }
    state.allNotes = state.allNotes.filter(function(n){ return n.NoteId!==noteId; });
    delete state.tagsByNote[noteId];
    state.selected=null; state.editingId=null;
    markDirty(); applyFilter(); renderBody(); updateTabCounts();
  }

  function addTagToNote(noteId, tagName){
    if(!state.db||!tagName||!tagName.trim()) return false;
    tagName = tagName.trim();
    var existing = state.tagsByNote[noteId]||[];
    for(var i=0;i<existing.length;i++){
      if(existing[i].name.toLowerCase()===tagName.toLowerCase()) return false;
    }
    snapshot();
    try{
      var safe = tagName.replace(/'/g,"''");
      var tagRows = rowsFromExec(state.db,"SELECT TagId FROM Tag WHERE Name='"+safe+"' COLLATE NOCASE");
      var tagId;
      if(tagRows.length>0){
        tagId=tagRows[0].TagId;
      } else {
        state.db.run('INSERT INTO Tag (Name, Type) VALUES (?,1)',[tagName]);
        var nr = rowsFromExec(state.db,'SELECT last_insert_rowid() AS id');
        tagId=nr[0].id;
        state.allTags.push({TagId:tagId,Name:tagName,count:0});
        state.allTags.sort(function(a,b){ return a.Name.localeCompare(b.Name); });
        populateFilters();
      }
      var maxPosRow=rowsFromExec(state.db,'SELECT COALESCE(MAX(Position),-1)+1 AS p FROM TagMap WHERE TagId='+(+tagId));
      var maxPos=maxPosRow.length?maxPosRow[0].p:0;
      state.db.run('INSERT INTO TagMap (TagId, NoteId, Position) VALUES (?,?,?)',[tagId,noteId,maxPos]);
      var mr = rowsFromExec(state.db,'SELECT last_insert_rowid() AS id');
      var mapId=mr[0].id;
      if(!state.tagsByNote[noteId]) state.tagsByNote[noteId]=[];
      state.tagsByNote[noteId].push({id:tagId,name:tagName,mapId:mapId,pos:maxPos+1});
      state.allTags.forEach(function(tg){ if(tg.TagId===tagId) tg.count=(tg.count||0)+1; });
    }catch(e){ console.error('[jb] addTagToNote',e); return false; }
    markDirty();
    return true;
  }

  function removeTagFromNote(noteId, tagMapId){
    if(!state.db) return;
    snapshot();
    try{ state.db.run('DELETE FROM TagMap WHERE TagMapId=?',[tagMapId]); }
    catch(e){ console.error('[jb] removeTagFromNote',e); return; }
    if(state.tagsByNote[noteId]){
      state.tagsByNote[noteId]=state.tagsByNote[noteId].filter(function(tg){ return tg.mapId!==tagMapId; });
    }
    markDirty();
  }

  function changeNoteColor(noteId, userMarkId, colorIndex){
    if(!state.db||!userMarkId) return;
    snapshot();
    try{ state.db.run('UPDATE UserMark SET ColorIndex=?, Version=Version+1 WHERE UserMarkId=?',[colorIndex,userMarkId]); }
    catch(e){ console.error('[jb] changeNoteColor',e); return; }
    for(var i=0;i<state.allNotes.length;i++){
      if(state.allNotes[i].NoteId===noteId){
        state.allNotes[i].ColorIndex=colorIndex;
        if(state.selected&&state.selected.NoteId===noteId) state.selected.ColorIndex=colorIndex;
        break;
      }
    }
    markDirty();
  }

  function deleteHighlight(userMarkId, linkedNoteId){
    if(!state.db) return;
    snapshot();
    try{
      state.db.run('DELETE FROM BlockRange WHERE UserMarkId=?',[userMarkId]);
      if(linkedNoteId) state.db.run('UPDATE Note SET UserMarkId=NULL WHERE NoteId=?',[linkedNoteId]);
      state.db.run('DELETE FROM UserMark WHERE UserMarkId=?',[userMarkId]);
    }catch(e){ console.error('[jb] deleteHighlight',e); return; }
    state.allHighlights=state.allHighlights.filter(function(h){ return h.UserMarkId!==userMarkId; });
    if(linkedNoteId){
      for(var i=0;i<state.allNotes.length;i++){
        if(state.allNotes[i].NoteId===linkedNoteId){
          state.allNotes[i].UserMarkId=null; state.allNotes[i].ColorIndex=null; break;
        }
      }
    }
    state.selected=null; state.editingId=null;
    markDirty(); applyFilter(); renderBody(); updateTabCounts();
  }

  function changeHighlightColor(userMarkId, colorIndex){
    if(!state.db) return;
    snapshot();
    try{ state.db.run('UPDATE UserMark SET ColorIndex=?, Version=Version+1 WHERE UserMarkId=?',[colorIndex,userMarkId]); }
    catch(e){ console.error('[jb] changeHighlightColor',e); return; }
    for(var i=0;i<state.allHighlights.length;i++){
      if(state.allHighlights[i].UserMarkId===userMarkId){
        state.allHighlights[i].ColorIndex=colorIndex;
        if(state.selected&&state.selected.UserMarkId===userMarkId) state.selected.ColorIndex=colorIndex;
        break;
      }
    }
    markDirty();
  }

  function saveHighlightNote(userMarkId, noteId, title, content){
    if(!state.db||!noteId) return false;
    snapshot();
    var now=nowTimestamp();
    var html=plainTextToNoteHtml(content);
    try{ state.db.run('UPDATE Note SET Title=?, Content=?, LastModified=? WHERE NoteId=?',[title||'',html,now,noteId]); }
    catch(e){ console.error('[jb] saveHighlightNote',e); return false; }
    for(var i=0;i<state.allHighlights.length;i++){
      if(state.allHighlights[i].UserMarkId===userMarkId){
        state.allHighlights[i].NoteTitle=title||'';
        state.allHighlights[i].NoteContent=html;
        state.allHighlights[i].LastModified=now;
        if(state.selected&&state.selected.UserMarkId===userMarkId){
          state.selected.NoteTitle=title||'';
          state.selected.NoteContent=html;
          state.selected.LastModified=now;
        }
        break;
      }
    }
    for(var j=0;j<state.allNotes.length;j++){
      if(state.allNotes[j].NoteId===noteId){
        state.allNotes[j].Title=title||''; state.allNotes[j].Content=html; state.allNotes[j].LastModified=now; break;
      }
    }
    return true;
  }

  function deleteBookmark(bookmarkId){
    if(!state.db) return;
    snapshot();
    try{ state.db.run('DELETE FROM Bookmark WHERE BookmarkId=?',[bookmarkId]); }
    catch(e){ console.error('[jb] deleteBookmark',e); return; }
    state.allBookmarks=state.allBookmarks.filter(function(b){ return b.BookmarkId!==bookmarkId; });
    state.selected=null; state.editingId=null;
    markDirty(); applyFilter(); renderBody(); updateTabCounts();
  }

  function saveBookmark(bookmarkId, title){
    if(!state.db) return false;
    snapshot();
    try{ state.db.run('UPDATE Bookmark SET Title=? WHERE BookmarkId=?',[title||'',bookmarkId]); }
    catch(e){ console.error('[jb] saveBookmark',e); return false; }
    for(var i=0;i<state.allBookmarks.length;i++){
      if(state.allBookmarks[i].BookmarkId===bookmarkId){
        state.allBookmarks[i].Title=title||'';
        if(state.selected&&state.selected.BookmarkId===bookmarkId) state.selected.Title=title||'';
        break;
      }
    }
    return true;
  }

  function exportDb(){
    if(!state.db||!window.JSZip) return;
    var exportBtn=state.overlay&&state.overlay.querySelector('.jb-export-btn');
    if(exportBtn){ exportBtn.disabled=true; exportBtn.innerHTML='<span style="font-size:11px">...</span>'; }
    try{
      var bytes=state.db.export();
      var zip=new JSZip();
      zip.file('userData.db', bytes);
      zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}}).then(function(blob){
        var url=URL.createObjectURL(blob);
        var a=document.createElement('a');
        a.href=url;
        a.download=(state.fileName?'edited_'+state.fileName:'edited_backup.jwlibrary');
        document.body.appendChild(a); a.click(); document.body.removeChild(a);
        setTimeout(function(){ URL.revokeObjectURL(url); },2000);
        if(exportBtn){ exportBtn.disabled=(state.dirty===0); exportBtn.textContent=t('export_db'); }
      }).catch(function(err){
        console.error('[jb] export failed',err);
        if(exportBtn){ exportBtn.disabled=(state.dirty===0); exportBtn.textContent=t('export_db'); }
      });
    }catch(e){
      console.error('[jb] export failed',e);
      if(exportBtn){ exportBtn.disabled=(state.dirty===0); exportBtn.textContent=t('export_db'); }
    }
  }

  function extractByDate(){
    if(!state.db||!window.JSZip||!window.initSqlJs) return;
    var df=state.dateFrom, dt=state.dateTo;
    if(!df&&!dt) return;
    // NoteIds whose LastModified date falls OUTSIDE the [df, dt] window.
    var drop=state.allNotes.filter(function(n){
      var lm=(n.LastModified||'').slice(0,10);
      if(!lm) return true;
      if(df&&lm<df) return true;
      if(dt&&lm>dt) return true;
      return false;
    }).map(function(n){ return n.NoteId; });
    var keep=state.allNotes.length-drop.length;
    if(keep<=0){ window.alert(t('extract_none')); return; }
    window.initSqlJs({locateFile:function(f){return 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/' + f;}}).then(function(SQL){
      var clone=new SQL.Database(state.db.export());
      try{
        clone.run('PRAGMA foreign_keys = OFF;');
        clone.run('BEGIN TRANSACTION;');
        for(var i=0;i<drop.length;i+=400){
          var batch=drop.slice(i,i+400);
          var ph=batch.map(function(){return '?';}).join(',');
          clone.run('DELETE FROM TagMap WHERE NoteId IN ('+ph+')', batch);
          clone.run('DELETE FROM Note WHERE NoteId IN ('+ph+')', batch);
        }
        clone.run('COMMIT;');
      }catch(e){ try{ clone.run('ROLLBACK;'); }catch(_){} console.error('[jb] extract',e); try{ clone.close(); }catch(__){} return; }
      var bytes=clone.export();
      try{ clone.close(); }catch(_){}
      var zip=new JSZip(); zip.file('userData.db', bytes);
      zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}}).then(function(blob){
        var url=URL.createObjectURL(blob);
        var base=(state.fileName?state.fileName.replace(/\.jwlibrary$/i,''):'backup');
        var a=document.createElement('a'); a.href=url; a.download='extracted_'+base+'.jwlibrary';
        document.body.appendChild(a); a.click(); document.body.removeChild(a);
        setTimeout(function(){ URL.revokeObjectURL(url); },2000);
      }).catch(function(err){ console.error('[jb] extract export',err); });
    }).catch(function(err){ console.error('[jb] extract sql',err); });
  }

  function htmlToMarkdown(html){
    if(!html) return '';
    var div=document.createElement('div'); div.innerHTML=sanitizeNoteHtml(html)||'';
    function walk(node){
      var out='';
      for(var i=0;i<node.childNodes.length;i++){
        var ch=node.childNodes[i];
        if(ch.nodeType===3){ out+=ch.nodeValue; }
        else if(ch.nodeType===1){
          var tag=ch.tagName.toLowerCase(), inner=walk(ch);
          if(tag==='strong'||tag==='b') out+='**'+inner+'**';
          else if(tag==='em'||tag==='i') out+='*'+inner+'*';
          else if(tag==='br') out+='\n';
          else if(tag==='li') out+='- '+inner+'\n';
          else if(tag==='ul'||tag==='ol') out+=inner+'\n';
          else if(tag==='p') out+=inner+'\n\n';
          else out+=inner;
        }
      }
      return out;
    }
    return walk(div).replace(/\n{3,}/g,'\n\n').trim();
  }
  function noteToMarkdown(n){
    var title=(n.Title&&n.Title.trim())||t('no_title');
    var tags=(state.tagsByNote[n.NoteId]||[]).map(function(tg){ return tg.name; });
    var fm='---\ntitle: '+title.replace(/\n/g,' ')+'\n';
    if(n.LastModified) fm+='date: '+String(n.LastModified).slice(0,10)+'\n';
    if(tags.length) fm+='tags: ['+tags.join(', ')+']\n';
    var pub=pubLabel(n); if(pub) fm+='publication: '+pub.replace(/\n/g,' ')+'\n';
    fm+='---\n\n';
    return fm+'# '+title+'\n\n'+htmlToMarkdown(n.Content||'')+'\n';
  }
  function exportMarkdown(){
    if(!window.JSZip) return;
    var notes=(state.activeType==='notes')?state.filtered:state.allNotes;
    if(!notes||!notes.length) return;
    var zip=new JSZip(), used={};
    notes.forEach(function(n,i){
      var title=(n.Title&&n.Title.trim())||t('no_title');
      var slug=title.replace(/[^a-z0-9\- ]/gi,'').trim().replace(/\s+/g,'-').slice(0,50)||'note';
      var fname=(i+1)+'-'+slug; while(used[fname.toLowerCase()]){ fname=fname+'_'; } used[fname.toLowerCase()]=1;
      zip.file(fname+'.md', noteToMarkdown(n));
    });
    var mdBtn=state.overlay&&state.overlay.querySelector('.jb-md-btn');
    if(mdBtn) mdBtn.disabled=true;
    zip.generateAsync({type:'blob',compression:'DEFLATE',compressionOptions:{level:6}}).then(function(blob){
      var url=URL.createObjectURL(blob);
      var base=(state.fileName?state.fileName.replace(/\.jwlibrary$/i,''):'notes');
      var a=document.createElement('a'); a.href=url; a.download=base+'_markdown.zip';
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      setTimeout(function(){ URL.revokeObjectURL(url); },2000);
      if(mdBtn) mdBtn.disabled=false;
    }).catch(function(err){ console.error('[jb] md export',err); if(mdBtn) mdBtn.disabled=false; });
  }

  // ---------- edit UI helpers ----------
  function buildColorPicker(currentColorIndex, onPick){
    var row=document.createElement('div');
    row.className='jb-color-picker-row';
    [1,2,3,4,5,6].forEach(function(ci){
      var b=document.createElement('button');
      b.type='button';
      b.className='jb-cp-dot'+(ci===currentColorIndex?' active':'');
      b.style.background=COLORS[ci];
      b.title='Color '+ci;
      b.onclick=function(){
        Array.prototype.forEach.call(row.children,function(c){ c.classList.remove('active'); });
        b.classList.add('active');
        onPick(ci);
      };
      row.appendChild(b);
    });
    return row;
  }

  function buildTagEditor(noteId, wrap){
    function render(){
      wrap.innerHTML='';
      var tags=state.tagsByNote[noteId]||[];
      tags.forEach(function(tg){
        var chip=document.createElement('span');
        chip.className='jb-tag-rm';
        var ns=document.createElement('span'); ns.textContent=tg.name; chip.appendChild(ns);
        var x=document.createElement('button');
        x.type='button'; x.className='jb-tag-rm-x'; x.textContent='\xd7'; x.title='Remove';
        x.onclick=function(){ removeTagFromNote(noteId,tg.mapId); render(); };
        chip.appendChild(x); wrap.appendChild(chip);
      });
      var addRow=document.createElement('div'); addRow.className='jb-tag-add-row';
      var inp=document.createElement('input');
      inp.type='text'; inp.className='jb-tag-add-input'; inp.placeholder=t('new_tag_ph');
      inp.setAttribute('list','jb-tag-dl');
      var dl=document.getElementById('jb-tag-dl');
      if(!dl){ dl=document.createElement('datalist'); dl.id='jb-tag-dl'; document.body.appendChild(dl); }
      dl.innerHTML='';
      state.allTags.forEach(function(tg){
        var opt=document.createElement('option'); opt.value=tg.Name; dl.appendChild(opt);
      });
      var addBtn=document.createElement('button');
      addBtn.type='button'; addBtn.className='jb-tag-add-btn'; addBtn.textContent=t('add_tag');
      function doAdd(){
        var v=inp.value.trim(); if(!v) return;
        if(addTagToNote(noteId,v)){ inp.value=''; render(); }
        else inp.value='';
      }
      addBtn.onclick=doAdd;
      inp.onkeydown=function(e){ if(e.key==='Enter'){ e.preventDefault(); doAdd(); } };
      addRow.appendChild(inp); addRow.appendChild(addBtn); wrap.appendChild(addRow);
    }
    render();
  }

  function buildInlineDeleteConfirm(msg, onConfirm, onCancel){
    var box=document.createElement('div'); box.className='jb-delete-confirm';
    var m=document.createElement('div'); m.className='jb-delete-confirm-msg'; m.textContent=msg; box.appendChild(m);
    var btns=document.createElement('div'); btns.className='jb-delete-confirm-btns';
    var yes=document.createElement('button'); yes.type='button'; yes.className='jb-btn-danger-solid'; yes.textContent=t('yes_delete'); yes.onclick=onConfirm; btns.appendChild(yes);
    var no=document.createElement('button'); no.type='button'; no.className='jb-btn jb-btn-ghost'; no.style.fontSize='13px'; no.textContent=t('cancel'); no.onclick=onCancel; btns.appendChild(no);
    box.appendChild(btns); return box;
  }

  function refreshDetail(){
    var det=state.overlay&&state.overlay.querySelector('.jb-detail');
    if(det){ det.innerHTML=''; det.appendChild(buildDetail(state.selected)); }
  }

  // ---------- edit form builders ----------
  function buildEditNote(n, wrap){
    wrap.className=(wrap.className||'')+' jb-edit-panel';
    // Title
    var tf=document.createElement('div'); tf.className='jb-edit-field';
    var tl=document.createElement('label'); tl.className='jb-edit-label'; tl.textContent=t('title_label'); tf.appendChild(tl);
    var ti=document.createElement('input'); ti.type='text'; ti.className='jb-edit-input'; ti.value=n.Title||''; tf.appendChild(ti);
    wrap.appendChild(tf);
    // Tags
    var tagF=document.createElement('div'); tagF.className='jb-edit-field';
    var tagL=document.createElement('label'); tagL.className='jb-edit-label'; tagL.textContent=t('tags_label'); tagF.appendChild(tagL);
    var tagW=document.createElement('div'); tagW.className='jb-tag-editor';
    buildTagEditor(n.NoteId, tagW); tagF.appendChild(tagW); wrap.appendChild(tagF);
    // Color (only if note has a highlight)
    if(n.UserMarkId){
      var cf=document.createElement('div'); cf.className='jb-edit-field';
      var cl=document.createElement('label'); cl.className='jb-edit-label'; cl.textContent=t('hl_color_label'); cf.appendChild(cl);
      cf.appendChild(buildColorPicker(n.ColorIndex, function(ci){ changeNoteColor(n.NoteId,n.UserMarkId,ci); }));
      wrap.appendChild(cf);
    }
    // Content
    var cnF=document.createElement('div'); cnF.className='jb-edit-field';
    var cnL=document.createElement('label'); cnL.className='jb-edit-label'; cnL.textContent=t('content_label'); cnF.appendChild(cnL);
    var fmtNote=document.createElement('div'); fmtNote.className='jb-format-note'; fmtNote.textContent=t('rich_text_note'); cnF.appendChild(fmtNote);
    var rte=buildRteEditor(n.Content||''); cnF.appendChild(rte.wrap); wrap.appendChild(cnF);
    // Actions
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var saveBtn=document.createElement('button'); saveBtn.type='button'; saveBtn.className='jb-btn'; saveBtn.textContent=t('save');
    saveBtn.onclick=function(){
      if(saveNote(n.NoteId,ti.value.trim(),rte.getHtml(),true)){ markDirty(); state.editingId=null; applyFilter(); renderBody(); }
    };
    acts.appendChild(saveBtn);
    var cancelBtn=document.createElement('button'); cancelBtn.type='button'; cancelBtn.className='jb-btn jb-btn-ghost'; cancelBtn.textContent=t('cancel');
    cancelBtn.onclick=function(){ state.editingId=null; refreshDetail(); };
    acts.appendChild(cancelBtn);
    var delBtn=document.createElement('button'); delBtn.type='button'; delBtn.className='jb-btn-danger'; delBtn.textContent=t('delete_item');
    var confirmShown=false;
    delBtn.onclick=function(){
      if(confirmShown) return; confirmShown=true;
      acts.appendChild(buildInlineDeleteConfirm(t('delete_note_confirm'),
        function(){ deleteNote(n.NoteId); },
        function(){ confirmShown=false; acts.removeChild(acts.lastChild); }
      ));
    };
    acts.appendChild(delBtn); wrap.appendChild(acts);
    setTimeout(function(){ ti.focus(); ti.select(); },50);
    ti.onkeydown=function(e){ if(e.key==='Tab'&&!e.shiftKey){ e.preventDefault(); rte.el.focus(); } };
    rte.el.onkeydown=function(e){
      if(e.key==='Escape'){ cancelBtn.click(); }
      if((e.ctrlKey||e.metaKey)&&e.key==='Enter'){ e.preventDefault(); saveBtn.click(); }
    };
    return wrap;
  }

  function buildEditHighlight(h, wrap){
    wrap.className=(wrap.className||'')+' jb-edit-panel';
    // Color picker
    var cf=document.createElement('div'); cf.className='jb-edit-field';
    var cl=document.createElement('label'); cl.className='jb-edit-label'; cl.textContent=t('hl_color_label'); cf.appendChild(cl);
    cf.appendChild(buildColorPicker(h.ColorIndex, function(ci){ changeHighlightColor(h.UserMarkId,ci); }));
    wrap.appendChild(cf);
    var noteTitleInput=null, noteContentTA=null;
    if(h.NoteId){
      var ntF=document.createElement('div'); ntF.className='jb-edit-field';
      var ntL=document.createElement('label'); ntL.className='jb-edit-label'; ntL.textContent=t('title_label'); ntF.appendChild(ntL);
      noteTitleInput=document.createElement('input'); noteTitleInput.type='text'; noteTitleInput.className='jb-edit-input'; noteTitleInput.value=h.NoteTitle||''; ntF.appendChild(noteTitleInput); wrap.appendChild(ntF);
      var ncF=document.createElement('div'); ncF.className='jb-edit-field';
      var ncL=document.createElement('label'); ncL.className='jb-edit-label'; ncL.textContent=t('content_label'); ncF.appendChild(ncL);
      var fmtNote=document.createElement('div'); fmtNote.className='jb-format-note'; fmtNote.textContent=t('plain_text_note'); ncF.appendChild(fmtNote);
      noteContentTA=document.createElement('textarea'); noteContentTA.className='jb-edit-textarea';
      var rawC=String(h.NoteContent||'');
      rawC=rawC.replace(/<br\s*\/?>/gi,'\n').replace(/<\/p>/gi,'\n\n').replace(/<p[^>]*>/gi,'');
      noteContentTA.value=stripHtmlPreserve(rawC); ncF.appendChild(noteContentTA); wrap.appendChild(ncF);
    }
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    if(h.NoteId){
      var saveBtn=document.createElement('button'); saveBtn.type='button'; saveBtn.className='jb-btn'; saveBtn.textContent=t('save');
      saveBtn.onclick=function(){
        if(saveHighlightNote(h.UserMarkId,h.NoteId,noteTitleInput?noteTitleInput.value.trim():'',noteContentTA?noteContentTA.value:'')){
          markDirty(); state.editingId=null; refreshDetail();
        }
      };
      acts.appendChild(saveBtn);
    }
    var cancelBtn=document.createElement('button'); cancelBtn.type='button'; cancelBtn.className='jb-btn jb-btn-ghost'; cancelBtn.textContent=t('cancel');
    cancelBtn.onclick=function(){ state.editingId=null; refreshDetail(); };
    acts.appendChild(cancelBtn);
    var delBtn=document.createElement('button'); delBtn.type='button'; delBtn.className='jb-btn-danger'; delBtn.textContent=t('delete_item');
    var confirmShown=false;
    delBtn.onclick=function(){
      if(confirmShown) return; confirmShown=true;
      acts.appendChild(buildInlineDeleteConfirm(t('delete_hl_confirm'),
        function(){ deleteHighlight(h.UserMarkId,h.NoteId); },
        function(){ confirmShown=false; acts.removeChild(acts.lastChild); }
      ));
    };
    acts.appendChild(delBtn); wrap.appendChild(acts);
    return wrap;
  }

  function buildEditBookmark(b, wrap){
    wrap.className=(wrap.className||'')+' jb-edit-panel';
    var tf=document.createElement('div'); tf.className='jb-edit-field';
    var tl=document.createElement('label'); tl.className='jb-edit-label'; tl.textContent=t('bm_title_label'); tf.appendChild(tl);
    var ti=document.createElement('input'); ti.type='text'; ti.className='jb-edit-input'; ti.value=b.Title||''; tf.appendChild(ti);
    wrap.appendChild(tf);
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var saveBtn=document.createElement('button'); saveBtn.type='button'; saveBtn.className='jb-btn'; saveBtn.textContent=t('save');
    saveBtn.onclick=function(){
      if(saveBookmark(b.BookmarkId,ti.value.trim())){ markDirty(); state.editingId=null; applyFilter(); renderBody(); }
    };
    acts.appendChild(saveBtn);
    var cancelBtn=document.createElement('button'); cancelBtn.type='button'; cancelBtn.className='jb-btn jb-btn-ghost'; cancelBtn.textContent=t('cancel');
    cancelBtn.onclick=function(){ state.editingId=null; refreshDetail(); };
    acts.appendChild(cancelBtn);
    var delBtn=document.createElement('button'); delBtn.type='button'; delBtn.className='jb-btn-danger'; delBtn.textContent=t('delete_item');
    var confirmShown=false;
    delBtn.onclick=function(){
      if(confirmShown) return; confirmShown=true;
      acts.appendChild(buildInlineDeleteConfirm(t('delete_bm_confirm'),
        function(){ deleteBookmark(b.BookmarkId); },
        function(){ confirmShown=false; acts.removeChild(acts.lastChild); }
      ));
    };
    acts.appendChild(delBtn); wrap.appendChild(acts);
    setTimeout(function(){ ti.focus(); ti.select(); },50);
    return wrap;
  }

  // ---------- query ----------
  function hydrateFromDb(db){
      // Notes — also fetch n.UserMarkId for color editing
      state.allNotes = rowsFromExec(db,
        "SELECT n.NoteId, n.LocationId, n.UserMarkId, n.Title, n.Content, n.LastModified, n.Guid, " +
        "l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol, " +
        "u.ColorIndex " +
        "FROM Note n " +
        "LEFT JOIN Location l ON n.LocationId = l.LocationId " +
        "LEFT JOIN UserMark u ON n.UserMarkId = u.UserMarkId " +
        "ORDER BY n.LastModified DESC"
      );

      // Highlights
      state.allHighlights = rowsFromExec(db,
        "SELECT u.UserMarkId, u.LocationId, u.ColorIndex, " +
        "l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol, " +
        "n.NoteId, n.Title AS NoteTitle, n.Content AS NoteContent, n.LastModified " +
        "FROM UserMark u " +
        "LEFT JOIN Location l ON u.LocationId = l.LocationId " +
        "LEFT JOIN Note n ON n.UserMarkId = u.UserMarkId " +
        "ORDER BY u.UserMarkId DESC"
      );

      // Bookmarks
      state.allBookmarks = rowsFromExec(db,
        "SELECT b.BookmarkId, b.LocationId, b.Slot, b.Title, b.Snippet, " +
        "l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol " +
        "FROM Bookmark b " +
        "LEFT JOIN Location l ON b.LocationId = l.LocationId " +
        "ORDER BY b.Slot"
      );

      // Tags — now include TagMapId for removal
      var tagRows = rowsFromExec(db,
        "SELECT tm.TagMapId, tm.TagId, tm.NoteId, tm.LocationId, tm.Position, t.Name " +
        "FROM TagMap tm JOIN Tag t ON tm.TagId = t.TagId"
      );
      var tagsByNote = {}, tagsByLoc = {};
      tagRows.forEach(function(r){
        if(r.NoteId){
          (tagsByNote[r.NoteId] = tagsByNote[r.NoteId] || []).push({id:r.TagId, name:r.Name, mapId:r.TagMapId, pos:r.Position||0});
        }
        if(r.LocationId){
          (tagsByLoc[r.LocationId] = tagsByLoc[r.LocationId] || []).push({id:r.TagId, name:r.Name, mapId:r.TagMapId});
        }
      });
      state.tagsByNote = tagsByNote;
      state.tagsByLocation = tagsByLoc;

      var tagUsage = {};
      tagRows.forEach(function(r){ tagUsage[r.TagId] = (tagUsage[r.TagId]||0) + 1; });
      state.allTags = rowsFromExec(db, "SELECT TagId, Name FROM Tag ORDER BY Name").map(function(tg){
        tg.count = tagUsage[tg.TagId] || 0; return tg;
      }).filter(function(tg){ return tg.count > 0; });

      var pubMap = {};
      function add(loc, locId){
        if(!locId) return;
        if(!pubMap[locId]) pubMap[locId] = {LocationId:locId, label:pubLabel(loc)||('Loc '+locId), bn:loc.BookNumber||9999};
      }
      state.allNotes.forEach(function(n){ add(n, n.LocationId); });
      state.allHighlights.forEach(function(h){ add(h, h.LocationId); });
      state.allBookmarks.forEach(function(b){ add(b, b.LocationId); });
      try{
        state.allInputFields = rowsFromExec(db, "SELECT i.LocationId, i.TextTag, i.Value, l.Title AS LocTitle, l.BookNumber, l.ChapterNumber, l.KeySymbol FROM InputField i LEFT JOIN Location l ON i.LocationId=l.LocationId ORDER BY i.LocationId").map(function(f){ f.IfKey=String(f.LocationId)+'::'+String(f.TextTag); return f; });
      }catch(_){ state.allInputFields=[]; }
      state.allInputFields.forEach(function(f){ add(f, f.LocationId); });
      state.allPublications = Object.keys(pubMap).map(function(k){return pubMap[k];})
        .sort(function(a,b){ if(a.bn!==b.bn) return a.bn-b.bn; return a.label.localeCompare(b.label); });
  }

  // ---------- undo/redo + bulk selection (v2.26) ----------
  var UNDO_MAX = 20;
  function snapshot(){
    if(state._inBatch || !state.db) return;
    try{ state.undo.push(state.db.export()); }catch(_){ return; }
    if(state.undo.length>UNDO_MAX) state.undo.shift();
    state.redo.length=0;
    updateUndoButtons();
  }
  function restoreSnapshot(bytes){
    if(!state.SQL) return;
    try{ if(state.db) state.db.close(); }catch(_){}
    try{ state.db=new state.SQL.Database(bytes); }catch(e){ console.error('[jb] restore',e); return; }
    hydrateFromDb(state.db);
    populateFilters();
    state.selected=null; state.editingId=null;
    if(state.selection) state.selection.clear();
    state.dirty=state.undo.length;
    applyFilter(); renderBody(); updateTabCounts(); updateDirtyBadge(); updateUndoButtons(); updateBatchBar();
  }
  function doUndo(){
    if(!state.undo.length || !state.db) return;
    try{ state.redo.push(state.db.export()); }catch(_){}
    restoreSnapshot(state.undo.pop());
    if(window.__jwHaptic) window.__jwHaptic(12);
  }
  function doRedo(){
    if(!state.redo.length || !state.db) return;
    try{ state.undo.push(state.db.export()); }catch(_){}
    restoreSnapshot(state.redo.pop());
    if(window.__jwHaptic) window.__jwHaptic(12);
  }
  function updateUndoButtons(){
    if(!state.overlay) return;
    var u=state.overlay.querySelector('.jb-undo'), r=state.overlay.querySelector('.jb-redo');
    if(u) u.disabled=!state.undo.length;
    if(r) r.disabled=!state.redo.length;
  }
  if(!window.__jbUndoKeys){
    window.__jbUndoKeys=true;
    document.addEventListener('keydown',function(e){
      if(!state.overlay) return;
      var tg=e.target, tag=(tg&&tg.tagName||'').toLowerCase();
      if(tag==='input'||tag==='textarea'||(tg&&tg.isContentEditable)) return;
      if((e.ctrlKey||e.metaKey)&&(e.key==='z'||e.key==='Z')){ e.preventDefault(); if(e.shiftKey) doRedo(); else doUndo(); }
      else if((e.ctrlKey||e.metaKey)&&(e.key==='y'||e.key==='Y')){ e.preventDefault(); doRedo(); }
    });
  }

  function rowId(r){ return r.NoteId||r.UserMarkId||r.BookmarkId||r.IfKey; }
  function selectedRows(){
    var ids=state.selection, seen=new Set(), out=[];
    // In ask mode scan ask results first, then fall back to allNotes
    var srcs=state.askMode
      ?[(state.askResults||[]).map(function(r){return r.note;}),state.allNotes]
      :[activeSource()];
    srcs.forEach(function(src){
      src.forEach(function(r){
        var id=rowId(r);
        if(ids.has(id)&&!seen.has(id)){ seen.add(id); out.push(r); }
      });
    });
    return out;
  }
  function toggleSelect(id){
    if(state.selection.has(id)) state.selection.delete(id); else state.selection.add(id);
    renderBody();
  }
  function selectAllFiltered(){ var src=state.askMode?(state.askResults||[]).map(function(r){return r.note;}):state.filtered; src.forEach(function(r){ state.selection.add(rowId(r)); }); renderBody(); }
  function clearSelection(){ state.selection.clear(); renderBody(); }
  function updateSelectBtn(){
    if(!state.overlay) return;
    var b=state.overlay.querySelector('.jb-select-toggle');
    if(b){ b.classList.toggle('jb-on', state.selectMode); b.textContent=state.selectMode?t('sel_done'):t('sel_mode'); }
  }
  function enterSelectMode(){
    state.selectMode=true; state.selected=null; state.editingId=null; state._batchUI='idle';
    if(state.overlay){ state.overlay.classList.remove('jb-mobile-detail'); state.overlay.classList.add('jb-mobile-list'); }
    renderBody(); updateSelectBtn();
  }
  function exitSelectMode(){
    state.selectMode=false; state.selection.clear(); state._batchUI='idle';
    renderBody(); updateSelectBtn();
  }

  function afterBatch(clearSel){
    hydrateFromDb(state.db); populateFilters();
    if(clearSel) state.selection.clear();
    state.dirty=state.undo.length;
    state.selected=null; state.editingId=null;
    applyFilter(); renderBody(); updateTabCounts(); updateDirtyBadge(); updateUndoButtons();
    if(window.__jwHaptic) window.__jwHaptic(18);
  }
  function batchSetColor(ci){
    var rows=selectedRows(); if(!rows.length) return;
    snapshot(); state._inBatch=true;
    try{ rows.forEach(function(r){ if(r.UserMarkId) state.db.run('UPDATE UserMark SET ColorIndex=?, Version=Version+1 WHERE UserMarkId=?',[ci,r.UserMarkId]); }); }
    finally{ state._inBatch=false; }
    afterBatch(false);
  }
  function batchAddTag(name){
    name=(name||'').trim(); if(!name){ updateBatchBar(); return; }
    var rows=selectedRows(); if(!rows.length){ updateBatchBar(); try{ var tb=document.createElement('div'); tb.style.cssText='position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:#1e293b;color:#f87171;padding:10px 18px;border-radius:8px;font-size:13px;font-weight:600;z-index:99999;pointer-events:none'; tb.textContent='No notes selected'; document.body.appendChild(tb); setTimeout(function(){try{tb.parentNode.removeChild(tb);}catch(_){}},2500); }catch(_){} return; }
    snapshot(); state._inBatch=true;
    try{
      var safe=name.replace(/'/g,"''");
      var tr=rowsFromExec(state.db,"SELECT TagId FROM Tag WHERE Name='"+safe+"' COLLATE NOCASE");
      var tagId = tr.length>0 ? tr[0].TagId : (state.db.run('INSERT INTO Tag (Name, Type) VALUES (?,1)',[name]), rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id);
      var tagged=0;
      var posBase=rowsFromExec(state.db,'SELECT COALESCE(MAX(Position),0)+1 AS p FROM TagMap WHERE TagId='+(+tagId))[0].p;
      var posOff=0;
      rows.forEach(function(r){
        if(!r.NoteId) return;
        var ex=rowsFromExec(state.db,'SELECT 1 FROM TagMap WHERE NoteId='+(+r.NoteId)+' AND TagId='+(+tagId)+' LIMIT 1');
        if(ex.length) return;
        state.db.run('INSERT INTO TagMap (TagId, NoteId, Position) VALUES (?,?,?)',[tagId,r.NoteId,posBase+posOff]);
        posOff++; tagged++;
      });
      state._batchTaggedCount=tagged;
      state._batchUI='tagged';
    }catch(e){
      state._inBatch=false;
      try{ var eb=document.createElement('div'); eb.style.cssText='position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:#7f1d1d;color:#fca5a5;padding:10px 18px;border-radius:8px;font-size:13px;font-weight:600;z-index:99999;pointer-events:none'; eb.textContent='Tag error: '+(e&&e.message||String(e)); document.body.appendChild(eb); setTimeout(function(){try{eb.parentNode.removeChild(eb);}catch(_){}},4000); }catch(_){}
      afterBatch(false); return;
    }finally{ state._inBatch=false; }
    afterBatch(false);
  }
  function batchDelete(){
    var rows=selectedRows(); if(!rows.length) return;
    snapshot(); state._inBatch=true;
    try{
      rows.forEach(function(r){
        if(state.activeType==='notes'){
          state.db.run('DELETE FROM TagMap WHERE NoteId=?',[r.NoteId]);
          state.db.run('DELETE FROM Note WHERE NoteId=?',[r.NoteId]);
        } else if(state.activeType==='highlights'){
          state.db.run('DELETE FROM BlockRange WHERE UserMarkId=?',[r.UserMarkId]);
          if(r.NoteId) state.db.run('UPDATE Note SET UserMarkId=NULL WHERE NoteId=?',[r.NoteId]);
          state.db.run('DELETE FROM UserMark WHERE UserMarkId=?',[r.UserMarkId]);
        } else if(state.activeType==='bookmarks'){
          state.db.run('DELETE FROM Bookmark WHERE BookmarkId=?',[r.BookmarkId]);
        } else {
          state.db.run('DELETE FROM InputField WHERE LocationId=? AND TextTag=?',[r.LocationId,r.TextTag]);
        }
      });
    }finally{ state._inBatch=false; }
    afterBatch(true);
  }
  function jbBatchBtn(bar,label,fn,danger){
    var b=document.createElement('button'); b.type='button'; b.className='jb-batch-btn'+(danger?' jb-batch-danger':''); b.textContent=label; b.onclick=fn; bar.appendChild(b); return b;
  }
  function updateBatchBar(noFocus){
    var bar=state.overlay&&state.overlay.querySelector('.jb-batch-bar');
    if(!bar) return;
    if(!state.selectMode){ bar.style.display='none'; bar.innerHTML=''; state._batchUI='idle'; return; }
    bar.style.display='flex'; bar.innerHTML='';
    var cnt=document.createElement('span'); cnt.className='jb-batch-count'; cnt.textContent=t('sel_count',{n:state.selection.size}); bar.appendChild(cnt);
    jbBatchBtn(bar,t('sel_all'),selectAllFiltered);
    jbBatchBtn(bar,t('sel_none'),clearSelection);
    var sp=document.createElement('span'); sp.style.flex='1'; sp.style.minWidth='4px'; bar.appendChild(sp);
    if(state.selection.size===0){ state._batchUI='idle'; return; }
    if(state._batchUI==='tag'){
      var inp=document.createElement('input'); inp.className='jb-batch-input'; inp.type='text'; inp.setAttribute('enterkeyhint','done'); inp.placeholder=t('batch_tag_ph'); bar.appendChild(inp);
      jbBatchBtn(bar,t('batch_add'),function(){ var v=inp.value; state._batchUI='idle'; batchAddTag(v); });
      jbBatchBtn(bar,t('cancel'),function(){ state._batchUI='idle'; updateBatchBar(); });
      inp.onkeydown=function(e){ if(e.key==='Enter'){ var v=inp.value; state._batchUI='idle'; batchAddTag(v); } else if(e.key==='Escape'){ state._batchUI='idle'; updateBatchBar(); } }; inp.onblur=function(){ if(state._batchUI==='tag'&&inp.value.trim()){ var v=inp.value; state._batchUI='idle'; batchAddTag(v); } };
      if(!noFocus) setTimeout(function(){ try{ inp.focus(); }catch(_){} },30);
      return;
    }
    if(state._batchUI==='del'){
      var dc=document.createElement('span'); dc.className='jb-batch-count'; dc.style.color='#fca5a5'; dc.textContent=t('batch_delete_confirm',{n:state.selection.size}); bar.appendChild(dc);
      jbBatchBtn(bar,t('yes_delete'),function(){ state._batchUI='idle'; batchDelete(); },true);
      jbBatchBtn(bar,t('cancel'),function(){ state._batchUI='idle'; updateBatchBar(); });
      return;
    }
    if(state.activeType==='notes'||state.activeType==='highlights'){
      var cw=document.createElement('span'); cw.className='jb-batch-color';
      [1,2,3,4,5,6].forEach(function(ci){ var d=document.createElement('span'); d.className='jb-batch-dot'; d.style.background=COLORS[ci]; d.title=t('batch_color'); d.onclick=function(){ batchSetColor(ci); }; cw.appendChild(d); });
      bar.appendChild(cw);
    }
    if(state._batchUI==='tagged'){
      var tc=document.createElement('span'); tc.className='jb-batch-count'; tc.style.color='#86efac';
      tc.textContent=t('batch_tagged_ok',{n:state._batchTaggedCount||state.selection.size}); bar.appendChild(tc);
      var sp2=document.createElement('span'); sp2.style.flex='1'; sp2.style.minWidth='4px'; bar.appendChild(sp2);
      jbBatchBtn(bar,t('export_db'),function(){ exportDb(); });
      jbBatchBtn(bar,t('sel_done'),function(){ state._batchUI='idle'; exitSelectMode(); });
      return;
    }
    if(state.activeType==='notes') jbBatchBtn(bar,t('batch_tag'),function(){ state._batchUI='tag'; updateBatchBar(); });
    if(state.activeType==='notes') jbBatchBtn(bar,t('share_action'),function(){ openShareExport(selectedRows()); });
    jbBatchBtn(bar,t('batch_delete'),function(){ state._batchUI='del'; updateBatchBar(); },true);
  }

  // ---------- note sharing / adopt (v2.28) ----------
  function jbUuid(){ return 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g,function(ch){ var r=Math.random()*16|0, v=ch==='x'?r:(r&0x3|0x8); return v.toString(16); }); }
  function buildShareEnvelope(rows){
    var notes=(rows||[]).filter(function(r){ return r.NoteId; }).map(function(n){
      var tags=(state.tagsByNote[n.NoteId]||[]).map(function(tg){ return tg.name; });
      return { title:n.Title||'', content:n.Content||'', color:n.ColorIndex||0, tags:tags, pub:pubLabel(n)||'', lastMod:n.LastModified||'' };
    });
    return { v:1, app:'jwsync', kind:'notes', exported:new Date().toISOString(), notes:notes };
  }
  function jbsClose(ov){ if(ov&&ov.parentNode) ov.parentNode.removeChild(ov); }
  function openShareExport(rows){
    var notes=(rows||[]).filter(function(r){ return r.NoteId; });
    if(!notes.length) return;
    var env=buildShareEnvelope(notes);
    var json=JSON.stringify(env,null,2);
    var ov=document.createElement('div'); ov.className='jbs-overlay';
    ov.innerHTML='<div class="jbs-card"><div class="jbs-head"><h3>'+htmlEscape(t('share_title'))+'</h3><button class="jbs-x" type="button" aria-label="'+htmlEscape(t('close'))+'">&times;</button></div>'+
      '<p class="jbs-intro">'+htmlEscape(t('share_intro'))+'</p>'+
      '<div class="jbs-count">'+htmlEscape(t('share_count',{n:env.notes.length}))+'</div>'+
      '<textarea class="jbs-text" readonly></textarea>'+
      '<div class="jbs-actions"><button type="button" class="jb-btn jbs-dl">'+htmlEscape(t('share_download'))+'</button>'+
      '<button type="button" class="jb-btn jb-btn-ghost jbs-copy">'+htmlEscape(t('share_copy'))+'</button></div></div>';
    document.body.appendChild(ov);
    var ta=ov.querySelector('.jbs-text'); ta.value=json;
    ov.querySelector('.jbs-x').onclick=function(){ jbsClose(ov); };
    ov.addEventListener('mousedown',function(e){ if(e.target===ov) jbsClose(ov); });
    ov.querySelector('.jbs-dl').onclick=function(){
      var blob=new Blob([json],{type:'application/json'}); var url=URL.createObjectURL(blob);
      var a=document.createElement('a'); a.href=url; a.download='shared_notes.jwshare.json'; document.body.appendChild(a); a.click(); document.body.removeChild(a);
      setTimeout(function(){ URL.revokeObjectURL(url); },2000);
      if(window.__jwHaptic) window.__jwHaptic(15);
    };
    ov.querySelector('.jbs-copy').onclick=function(){
      var b=ov.querySelector('.jbs-copy');
      function done(){ b.textContent=t('copied'); setTimeout(function(){ b.textContent=t('share_copy'); },1500); }
      try{ navigator.clipboard.writeText(json).then(done,function(){ ta.select(); try{document.execCommand('copy');}catch(_){} done(); }); }
      catch(_){ ta.select(); try{document.execCommand('copy');}catch(__){} done(); }
    };
  }
  function adoptNotes(notes){
    if(!state.db||!Array.isArray(notes)||!notes.length) return 0;
    snapshot(); state._inBatch=true; var added=0;
    try{
      var now=nowTimestamp();
      function tagId(name){
        var s=String(name).replace(/'/g,"''");
        var r=rowsFromExec(state.db,"SELECT TagId FROM Tag WHERE Name='"+s+"' COLLATE NOCASE");
        if(r.length) return r[0].TagId;
        state.db.run('INSERT INTO Tag (Name, Type) VALUES (?,1)',[name]);
        return rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id;
      }
      var shareName=t('share_tag');
      notes.forEach(function(nd){
        try{
          var title=(typeof nd.title==='string')?nd.title:'';
          var content=sanitizeNoteHtml((typeof nd.content==='string')?nd.content:'');
          state.db.run('INSERT INTO Note (Guid, Title, Content, LastModified, Created, BlockType, BlockIdentifier) VALUES (?,?,?,?,?,0,0)',[jbUuid(),title,content,now,now]);
          var noteId=rowsFromExec(state.db,'SELECT last_insert_rowid() AS id')[0].id;
          var names=[shareName].concat(Array.isArray(nd.tags)?nd.tags:[]); var seen={};
          names.forEach(function(tn){ tn=String(tn||'').trim(); if(!tn||seen[tn.toLowerCase()]) return; seen[tn.toLowerCase()]=1;
            var tid=tagId(tn); state.db.run('INSERT INTO TagMap (TagId, NoteId, Position) VALUES (?,?,0)',[tid,noteId]); });
          added++;
        }catch(e){ console.error('[jb] adopt note',e); }
      });
    }catch(e){ console.error('[jb] adopt',e); }
    finally{ state._inBatch=false; }
    afterBatch(false);
    return added;
  }
  function openShareImport(){
    var ov=document.createElement('div'); ov.className='jbs-overlay';
    ov.innerHTML='<div class="jbs-card"><div class="jbs-head"><h3>'+htmlEscape(t('receive_title'))+'</h3><button class="jbs-x" type="button" aria-label="'+htmlEscape(t('close'))+'">&times;</button></div>'+
      '<p class="jbs-intro">'+htmlEscape(t('receive_intro'))+'</p>'+
      '<textarea class="jbs-text" placeholder="'+htmlEscape(t('receive_paste_ph'))+'"></textarea>'+
      '<div class="jbs-actions"><button type="button" class="jb-btn jb-btn-ghost jbs-choose">'+htmlEscape(t('receive_choose'))+'</button>'+
      '<button type="button" class="jb-btn jbs-preview">'+htmlEscape(t('receive_preview'))+'</button></div>'+
      '<div class="jbs-result"></div></div>';
    document.body.appendChild(ov);
    var ta=ov.querySelector('.jbs-text'), result=ov.querySelector('.jbs-result');
    ov.querySelector('.jbs-x').onclick=function(){ jbsClose(ov); };
    ov.addEventListener('mousedown',function(e){ if(e.target===ov) jbsClose(ov); });
    ov.querySelector('.jbs-choose').onclick=function(){
      var fi=document.createElement('input'); fi.type='file'; fi.accept='.json,.jwshare,application/json';
      fi.onchange=function(){ var f=fi.files&&fi.files[0]; if(!f) return; var rd=new FileReader(); rd.onload=function(){ ta.value=String(rd.result||''); doPreview(); }; rd.readAsText(f); };
      fi.click();
    };
    ov.querySelector('.jbs-preview').onclick=doPreview;
    function doPreview(){
      result.innerHTML='';
      var env=null; try{ env=JSON.parse(ta.value); }catch(_){ }
      if(!env||env.app!=='jwsync'||!Array.isArray(env.notes)){ result.innerHTML='<div class="jbs-err">'+htmlEscape(t('receive_invalid'))+'</div>'; return; }
      var notes=env.notes;
      var list=document.createElement('div'); list.className='jbs-list';
      var hdr=document.createElement('div'); hdr.className='jbs-list-hdr'; hdr.textContent=t('preview_readonly')+' · '+t('share_count',{n:notes.length}); list.appendChild(hdr);
      notes.slice(0,50).forEach(function(nd){
        var it=document.createElement('div'); it.className='jbs-item';
        var ti=document.createElement('div'); ti.className='jbs-item-title'; ti.textContent=(nd.title&&String(nd.title).trim())||t('no_title'); it.appendChild(ti);
        var bd=document.createElement('div'); bd.className='jbs-item-body'; bd.textContent=stripHtml(String(nd.content||'')); it.appendChild(bd);
        list.appendChild(it);
      });
      result.appendChild(list);
      var row=document.createElement('div'); row.className='jbs-actions';
      var adoptBtn=document.createElement('button'); adoptBtn.type='button'; adoptBtn.className='jb-btn';
      if(!state.db){ adoptBtn.disabled=true; adoptBtn.textContent=t('adopt_need_lib'); }
      else adoptBtn.textContent=t('adopt',{n:notes.length});
      adoptBtn.onclick=function(){ if(!state.db) return; var n=adoptNotes(notes); result.innerHTML='<div class="jbs-ok">'+htmlEscape(t('adopted',{n:n}))+'</div>'; };
      row.appendChild(adoptBtn); result.appendChild(row);
    }
  }

  function loadFromFile(file){
    var loadingEl = state.overlay.querySelector('.jb-body');
    loadingEl.innerHTML = '<div class="jb-loading"><div class="jb-spinner"></div><div>' + htmlEscape(t('loading')) + '</div></div>';
    function fail(msg){
      loadingEl.innerHTML = '<div class="jb-empty">' + htmlEscape(t('error')) + ' ' + htmlEscape(msg) + '</div>';
    }
    if(!window.JSZip || !window.initSqlJs){ fail('Required libraries are not loaded yet.'); return; }
    // Close any existing DB
    if(state.db){ try{ state.db.close(); }catch(_){} state.db=null; }
    // New file → previous semantic index no longer applies
    state.askMode=false; state.askResults=[]; state.askQuery=''; state.askPhase='idle'; state.askError=''; ASK.vecs=null;

    new JSZip().loadAsync(file).then(function(zip){
      var dbName = Object.keys(zip.files).find(function(n){ return /userdata\.db$/i.test(n); });
      if(!dbName) throw new Error('userData.db not found in backup.');
      return zip.files[dbName].async('uint8array');
    }).then(function(bytes){
      return window.initSqlJs({locateFile:function(f){return 'https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.8.0/' + f;}})
        .then(function(SQL){ state.SQL=SQL; return new SQL.Database(bytes); });
    }).then(function(db){
      state.db = db;
      state.fileName = (file && file.name) ? file.name : '';
      state.dirty = 0;
      state.editingId = null;
      updateDirtyBadge();

      hydrateFromDb(db);

      state.selected = null;
      state.activeType = 'notes';
      populateFilters();
      applyFilter();
      renderBody();
      updateTabCounts();
    }).catch(function(err){
      console.error('[jb] load failed', err);
      var m=((err&&err.message)||'').toLowerCase();
      var code=(err&&err.code)?err.code:(m.indexOf('userdata')>=0?'no_db':((m.indexOf('zip')>=0||m.indexOf('central')>=0||m.indexOf('corrupt')>=0)?'corrupt':((m.indexOf('database')>=0||m.indexOf('sqlite')>=0)?'not_sqlite':'')));
      fail(code?t('err_'+code):(err&&err.message?err.message:String(err)));
    });
  }

  // ---------- filter ----------
  function activeSource(){
    if(state.activeType==='highlights') return state.allHighlights;
    if(state.activeType==='bookmarks') return state.allBookmarks;
    if(state.activeType==='inputfields') return state.allInputFields;
    return state.allNotes;
  }
  function applyFilter(){
    var q=state.search.trim().toLowerCase();
    var c=state.color, tagId=state.tagId, pubId=state.pubId;
    var df=state.dateFrom, dt=state.dateTo;
    var src=activeSource();
    var rows=src.filter(function(r){
      if(c!==''&&state.activeType!=='bookmarks'&&state.activeType!=='inputfields'){ if(String(r.ColorIndex||0)!==c) return false; }
      if((df||dt)&&(state.activeType==='notes'||state.activeType==='highlights')){ var lm=(r.LastModified||'').slice(0,10); if(!lm) return false; if(df&&lm<df) return false; if(dt&&lm>dt) return false; }
      if(pubId!==''&&String(r.LocationId||'')!==pubId) return false;
      if(tagId!==''){
        var ts=[];
        if(state.activeType==='notes'&&r.NoteId) ts=state.tagsByNote[r.NoteId]||[];
        else if(state.activeType==='highlights'&&r.NoteId) ts=state.tagsByNote[r.NoteId]||[];
        else if(state.activeType==='bookmarks'&&r.LocationId) ts=state.tagsByLocation[r.LocationId]||[];
        if(!ts.some(function(tg){ return String(tg.id)===tagId; })) return false;
      }
      if(q){
        var hay=r.__jbHay;
        if(hay===undefined||r.__jbHayGen!==state.hayGen){
          if(state.activeType==='notes') hay=((r.Title||'')+' '+fastStripHtml(r.Content||'')+' '+pubLabel(r)).toLowerCase();
          else if(state.activeType==='highlights') hay=((r.NoteTitle||'')+' '+fastStripHtml(r.NoteContent||'')+' '+pubLabel(r)).toLowerCase();
          else if(state.activeType==='inputfields') hay=((r.Value||'')+' '+pubLabel(r)).toLowerCase();
          else hay=((r.Title||'')+' '+(r.Snippet||'')+' '+pubLabel(r)).toLowerCase();
          r.__jbHay=hay; r.__jbHayGen=state.hayGen;
        }
        if(hay.indexOf(q)===-1) return false;
      }
      return true;
    });
    if(state.activeType==='notes'||state.activeType==='highlights'){
      if(state.sort==='oldest') rows.sort(function(a,b){ return (a.LastModified||'').localeCompare(b.LastModified||''); });
      else if(state.sort==='pub') rows.sort(function(a,b){ return pubLabel(a).localeCompare(pubLabel(b)); });
      else rows.sort(function(a,b){ return (b.LastModified||'').localeCompare(a.LastModified||''); });
    } else {
      if(state.sort==='pub') rows.sort(function(a,b){ return pubLabel(a).localeCompare(pubLabel(b)); });
    }
    state.filtered=rows;
    if(state.page*PAGE_SIZE>=state.filtered.length){ state.page=0; }
  }

  // ---------- render ----------
  function renderBody(){
    var body=state.overlay.querySelector('.jb-body');
    body.innerHTML='';
    if(state.askMode){ renderAsk(body); updateBatchBar(true); updateUndoButtons(); return; }
    var list=document.createElement('div'); list.className='jb-list';
    var total=state.filtered.length;
    var pages=Math.max(1, Math.ceil(total/PAGE_SIZE));
    if(state.page>=pages){ state.page=pages-1; }
    if(state.page<0){ state.page=0; }
    var start=state.page*PAGE_SIZE;
    var shown=state.filtered.slice(start, start+PAGE_SIZE);
    if(total===0){
      list.innerHTML='<div class="jb-empty">'+htmlEscape(t('no_results'))+'</div>';
    } else {
      var frag=document.createDocumentFragment();
      shown.forEach(function(r){ frag.appendChild(buildRow(r)); });
      list.appendChild(frag);
    }
    body.appendChild(list);
    if(pages>1){
      var pager=document.createElement('div'); pager.className='jb-pager';
      var prev=document.createElement('button'); prev.type='button'; prev.className='jb-pager-btn'; prev.textContent=t('pg_prev');
      prev.disabled=state.page<=0;
      prev.onclick=function(){ if(state.page>0){ state.page--; renderBody(); } };
      var status=document.createElement('span'); status.className='jb-pager-status';
      status.textContent=t('pg_status',{page:state.page+1,pages:pages,total:total});
      var next=document.createElement('button'); next.type='button'; next.className='jb-pager-btn'; next.textContent=t('pg_next');
      next.disabled=state.page>=pages-1;
      next.onclick=function(){ if(state.page<pages-1){ state.page++; renderBody(); } };
      pager.appendChild(prev); pager.appendChild(status); pager.appendChild(next);
      list.appendChild(pager);
    }
    var detail=document.createElement('div'); detail.className='jb-detail';
    detail.appendChild(buildDetail(state.selected));
    body.appendChild(detail);
    var cnt=state.overlay.querySelector('.jb-head-count');
    var n=state.filtered.length;
    cnt.textContent=(n===1?t('count_one',{n:n}):t('count_many',{n:n}));
    updateMobileView();
    updateBatchBar(true); updateUndoButtons();
  }

  function buildRow(r){
    var row=document.createElement('div');
    var id=r.NoteId||r.UserMarkId||r.BookmarkId||r.IfKey;
    var rowKey=state.activeType+':'+id;
    var selKey=state.selected?(state.activeType+':'+(state.selected.NoteId||state.selected.UserMarkId||state.selected.BookmarkId)):'';
    if(state.selectMode){
      row.className='jb-note jb-selectable'+(state.selection.has(id)?' jb-selected':'');
      row.onclick=function(){ toggleSelect(id); };
    } else {
      row.className='jb-note'+(rowKey===selKey?' active':'');
      row.onclick=function(){
        state.selected=r; state.editingId=null;
        state.overlay.classList.remove('jb-mobile-list');
        state.overlay.classList.add('jb-mobile-detail');
        renderBody();
      };
    }
    var built = state.activeType==='notes'?buildNoteRow(r,row):(state.activeType==='highlights'?buildHighlightRow(r,row):(state.activeType==='bookmarks'?buildBookmarkRow(r,row):buildInputFieldRow(r,row)));
    if(state.selectMode){
      var cb=document.createElement('span'); cb.className='jb-check'+(state.selection.has(id)?' jb-check-on':'');
      built.insertBefore(cb, built.firstChild);
    }
    return built;
  }

  function buildNoteRow(n,row){
    var title=document.createElement('div'); title.className='jb-note-title';
    if(n.ColorIndex&&COLORS[n.ColorIndex]){ var dot=document.createElement('span'); dot.className='jb-note-color'; dot.style.background=COLORS[n.ColorIndex]; title.appendChild(dot); }
    var ts=document.createElement('span'); ts.textContent=(n.Title&&n.Title.trim())||t('no_title'); title.appendChild(ts); row.appendChild(title);
    var excerpt=stripHtml(n.Content||'');
    if(excerpt){ var ex=document.createElement('div'); ex.className='jb-note-excerpt'; ex.textContent=excerpt; row.appendChild(ex); }
    row.appendChild(buildMeta(n,n.NoteId,'note')); return row;
  }

  function buildHighlightRow(h,row){
    var title=document.createElement('div'); title.className='jb-note-title';
    if(h.ColorIndex&&COLORS[h.ColorIndex]){ var dot=document.createElement('span'); dot.className='jb-note-color'; dot.style.background=COLORS[h.ColorIndex]; title.appendChild(dot); }
    var ts=document.createElement('span'); ts.textContent=t('hl_label')+(h.NoteTitle?' — '+h.NoteTitle:''); title.appendChild(ts); row.appendChild(title);
    var excerpt=stripHtml(h.NoteContent||'');
    if(excerpt){ var ex=document.createElement('div'); ex.className='jb-note-excerpt'; ex.textContent=excerpt; row.appendChild(ex); }
    else { var ex2=document.createElement('div'); ex2.className='jb-note-excerpt'; ex2.style.fontStyle='italic'; ex2.textContent=t('hl_no_text'); row.appendChild(ex2); }
    row.appendChild(buildMeta(h,h.NoteId,'highlight')); return row;
  }

  function buildBookmarkRow(b,row){
    var title=document.createElement('div'); title.className='jb-note-title';
    var slot=document.createElement('span'); slot.className='jb-bm-slot'; slot.textContent=(b.Slot!=null)?String(b.Slot+1):'•'; title.appendChild(slot);
    var ts=document.createElement('span'); ts.textContent=(b.Title&&b.Title.trim())||pubLabel(b)||t('bm_label'); title.appendChild(ts); row.appendChild(title);
    if(b.Snippet){ var ex=document.createElement('div'); ex.className='jb-note-excerpt'; ex.textContent=b.Snippet; row.appendChild(ex); }
    row.appendChild(buildMeta(b,null,'bookmark')); return row;
  }

  function buildMeta(r,noteId,kind){
    var meta=document.createElement('div'); meta.className='jb-note-meta';
    var pl=pubLabel(r);
    if(pl){ var pub=document.createElement('span'); pub.className='jb-pub'; pub.textContent=pl; meta.appendChild(pub); }
    if(r.LastModified){ var dt=document.createElement('span'); dt.textContent=fmtDate(r.LastModified); meta.appendChild(dt); }
    var tags=[];
    if(noteId) tags=state.tagsByNote[noteId]||[];
    else if(kind==='bookmark'&&r.LocationId) tags=state.tagsByLocation[r.LocationId]||[];
    tags.slice(0,3).forEach(function(tg){ var ts=document.createElement('span'); ts.className='jb-tag'; ts.textContent=tg.name; meta.appendChild(ts); });
    if(tags.length>3){ var more=document.createElement('span'); more.className='jb-tag'; more.textContent='+'+(tags.length-3); meta.appendChild(more); }
    return meta;
  }

  function buildDetail(r){
    var wrap=document.createElement('div');
    if(!r){ var empty=document.createElement('div'); empty.className='jb-detail-empty'; empty.textContent=t('detail_empty'); wrap.appendChild(empty); return wrap; }
    var back=document.createElement('button'); back.className='jb-back'; back.textContent=t('back');
    back.onclick=function(){ state.overlay.classList.remove('jb-mobile-detail'); state.overlay.classList.add('jb-mobile-list'); };
    wrap.appendChild(back);
    var itemId=(r.NoteId||r.UserMarkId||r.BookmarkId||r.IfKey);
    if(state.editingId===itemId){
      if(state.activeType==='notes') return buildEditNote(r,wrap);
      if(state.activeType==='highlights') return buildEditHighlight(r,wrap);
      if(state.activeType==='inputfields') return buildEditInputField(r,wrap);
      return buildEditBookmark(r,wrap);
    }
    if(state.activeType==='notes') return buildDetailNote(r,wrap);
    if(state.activeType==='highlights') return buildDetailHighlight(r,wrap);
    if(state.activeType==='inputfields') return buildDetailInputField(r,wrap);
    return buildDetailBookmark(r,wrap);
  }

  function buildInputFieldRow(f,row){
    var title=document.createElement('div'); title.className='jb-note-title';
    var ts=document.createElement('span'); ts.textContent=pubLabel(f)||t('if_label'); title.appendChild(ts); row.appendChild(title);
    var val=(f.Value||'').trim();
    var ex=document.createElement('div'); ex.className='jb-note-excerpt';
    if(val){ ex.textContent=val; } else { ex.style.fontStyle='italic'; ex.textContent=t('if_empty'); }
    row.appendChild(ex);
    var meta=buildMeta(f,null,'inputfield');
    if(f.TextTag){ var tg=document.createElement('span'); tg.className='jb-if-tag'; tg.textContent=f.TextTag; meta.appendChild(tg); }
    row.appendChild(meta);
    return row;
  }
  function buildDetailInputField(f,wrap){
    var title=document.createElement('div'); title.className='jb-detail-title';
    var ts=document.createElement('span'); ts.textContent=pubLabel(f)||t('if_label'); title.appendChild(ts); wrap.appendChild(title);
    var meta=document.createElement('div'); meta.className='jb-detail-meta'; meta.textContent=t('if_question')+': '+(f.TextTag||'—'); wrap.appendChild(meta);
    var content=document.createElement('div'); content.className='jb-detail-content';
    var val=(f.Value||'').trim();
    if(val){ content.textContent=val; } else { content.textContent=t('if_empty'); content.style.color='#5a6883'; content.style.fontStyle='italic'; }
    wrap.appendChild(content);
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var copyBtn=document.createElement('button'); copyBtn.className='jb-btn jb-btn-ghost'; copyBtn.textContent=t('copy');
    copyBtn.onclick=function(){ try{ navigator.clipboard.writeText(val).then(function(){ copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }); }catch(_){ } };
    acts.appendChild(copyBtn);
    if(state.db){
      var editBtn=document.createElement('button'); editBtn.className='jb-btn jb-btn-ghost'; editBtn.textContent=t('edit');
      editBtn.onclick=function(){ state.editingId=f.IfKey; refreshDetail(); };
      acts.appendChild(editBtn);
      var delBtn=document.createElement('button'); delBtn.type='button'; delBtn.className='jb-btn-danger'; delBtn.textContent=t('delete_item');
      var shown=false;
      delBtn.onclick=function(){ if(shown) return; shown=true; acts.appendChild(buildInlineDeleteConfirm(t('delete_if_confirm'), function(){ deleteInputField(f.LocationId,f.TextTag); }, function(){ shown=false; acts.removeChild(acts.lastChild); })); };
      acts.appendChild(delBtn);
    }
    wrap.appendChild(acts);
    return wrap;
  }
  function buildEditInputField(f,wrap){
    wrap.className=(wrap.className||'')+' jb-edit-panel';
    var fld=document.createElement('div'); fld.className='jb-edit-field';
    var lbl=document.createElement('label'); lbl.className='jb-edit-label'; lbl.textContent=t('if_answer'); fld.appendChild(lbl);
    var ta=document.createElement('textarea'); ta.className='jb-edit-textarea'; ta.value=f.Value||''; fld.appendChild(ta); wrap.appendChild(fld);
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var saveBtn=document.createElement('button'); saveBtn.type='button'; saveBtn.className='jb-btn'; saveBtn.textContent=t('save');
    saveBtn.onclick=function(){ if(saveInputField(f.LocationId,f.TextTag,ta.value)){ state.editingId=null; applyFilter(); renderBody(); } };
    var cancelBtn=document.createElement('button'); cancelBtn.type='button'; cancelBtn.className='jb-btn jb-btn-ghost'; cancelBtn.textContent=t('cancel');
    cancelBtn.onclick=function(){ state.editingId=null; refreshDetail(); };
    acts.appendChild(saveBtn); acts.appendChild(cancelBtn); wrap.appendChild(acts);
    setTimeout(function(){ try{ ta.focus(); }catch(_){} },50);
    return wrap;
  }
  function saveInputField(locId, textTag, value){
    if(!state.db) return false;
    snapshot();
    try{ state.db.run('UPDATE InputField SET Value=? WHERE LocationId=? AND TextTag=?',[value||'',locId,textTag]); }
    catch(e){ console.error('[jb] saveInputField',e); return false; }
    for(var i=0;i<state.allInputFields.length;i++){ var f=state.allInputFields[i]; if(f.LocationId===locId&&f.TextTag===textTag){ f.Value=value||''; break; } }
    markDirty(); return true;
  }
  function deleteInputField(locId, textTag){
    if(!state.db) return;
    snapshot();
    try{ state.db.run('DELETE FROM InputField WHERE LocationId=? AND TextTag=?',[locId,textTag]); }
    catch(e){ console.error('[jb] deleteInputField',e); return; }
    state.allInputFields=state.allInputFields.filter(function(f){ return !(f.LocationId===locId&&f.TextTag===textTag); });
    state.selected=null; state.editingId=null;
    markDirty(); applyFilter(); renderBody(); updateTabCounts();
  }

  function buildDetailNote(n,wrap){
    var title=document.createElement('div'); title.className='jb-detail-title';
    if(n.ColorIndex&&COLORS[n.ColorIndex]){ var dot=document.createElement('span'); dot.className='jb-detail-color'; dot.style.background=COLORS[n.ColorIndex]; title.appendChild(dot); }
    var ts=document.createElement('span'); ts.textContent=(n.Title&&n.Title.trim())||t('no_title'); title.appendChild(ts); wrap.appendChild(title);
    wrap.appendChild(buildDetailMeta(n,n.NoteId,'note'));
    var content=document.createElement('div'); content.className='jb-detail-content';
    var text=stripHtml(n.Content||'');
    if(!text){ content.textContent=t('no_content'); content.style.color='#5a6883'; content.style.fontStyle='italic'; }
    else { var sh=sanitizeNoteHtml(n.Content||''); if(sh){ content.innerHTML=sh; } else { content.textContent=t('no_content'); } }
    wrap.appendChild(content);
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var copyBtn=document.createElement('button'); copyBtn.className='jb-btn jb-btn-ghost'; copyBtn.textContent=t('copy');
    var copyText=((n.Title&&n.Title.trim())?n.Title+'\n\n':'')+stripHtml(n.Content||'');
    copyBtn.onclick=function(){
      try{ navigator.clipboard.writeText(copyText).then(function(){ copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }); }
      catch(_){ var ta=document.createElement('textarea'); ta.value=copyText; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(_){} document.body.removeChild(ta); copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }
    };
    acts.appendChild(copyBtn);
    var copyMdBtn=document.createElement('button'); copyMdBtn.className='jb-btn jb-btn-ghost'; copyMdBtn.textContent=t('copy_md');
    var mdText=noteToMarkdown(n);
    copyMdBtn.onclick=function(){
      function flash(){ copyMdBtn.textContent=t('copied'); setTimeout(function(){ copyMdBtn.textContent=t('copy_md'); },1500); }
      try{ navigator.clipboard.writeText(mdText).then(flash); }
      catch(_){ var ta=document.createElement('textarea'); ta.value=mdText; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(__){} document.body.removeChild(ta); flash(); }
    };
    acts.appendChild(copyMdBtn);
    if(state.db){
      var editBtn=document.createElement('button'); editBtn.className='jb-btn jb-btn-ghost'; editBtn.textContent=t('edit');
      editBtn.onclick=function(){ state.editingId=n.NoteId; refreshDetail(); };
      acts.appendChild(editBtn);
    }
    wrap.appendChild(acts);
    return wrap;
  }

  function buildDetailHighlight(h,wrap){
    var title=document.createElement('div'); title.className='jb-detail-title';
    if(h.ColorIndex&&COLORS[h.ColorIndex]){ var sw=document.createElement('span'); sw.className='jb-hl-swatch'; sw.style.background=COLORS[h.ColorIndex]; title.appendChild(sw); }
    var ts=document.createElement('span'); ts.textContent=t('hl_label'); title.appendChild(ts); wrap.appendChild(title);
    wrap.appendChild(buildDetailMeta(h,h.NoteId,'highlight'));
    var block=document.createElement('div'); block.className='jb-detail-hl-block'; block.style.fontStyle='italic'; block.textContent=t('hl_no_text'); wrap.appendChild(block);
    if(h.NoteId){
      var lab=document.createElement('div'); lab.style.cssText='margin-top:18px;font-size:12px;color:#7d8aa8;font-weight:600;text-transform:uppercase;letter-spacing:.5px'; lab.textContent=t('linked_note'); wrap.appendChild(lab);
      if(h.NoteTitle){ var nt=document.createElement('div'); nt.style.cssText='font-weight:700;font-size:15px;color:#e7eaf3;margin-top:6px'; nt.textContent=h.NoteTitle; wrap.appendChild(nt); }
      var nc=document.createElement('div'); nc.className='jb-detail-content'; nc.style.marginTop='8px';
      var shn=sanitizeNoteHtml(h.NoteContent||''); if(shn){ nc.innerHTML=shn; } else { nc.textContent=t('no_content'); } wrap.appendChild(nc);
    }
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    if(h.NoteId){
      var copyBtn=document.createElement('button'); copyBtn.className='jb-btn jb-btn-ghost'; copyBtn.textContent=t('copy');
      var copyText=((h.NoteTitle&&h.NoteTitle.trim())?h.NoteTitle+'\n\n':'')+stripHtml(h.NoteContent||'');
      copyBtn.onclick=function(){
        try{ navigator.clipboard.writeText(copyText).then(function(){ copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }); }
        catch(_){ var ta=document.createElement('textarea'); ta.value=copyText; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(_){} document.body.removeChild(ta); copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }
      };
      acts.appendChild(copyBtn);
    }
    if(state.db){
      var editBtn=document.createElement('button'); editBtn.className='jb-btn jb-btn-ghost'; editBtn.textContent=t('edit');
      editBtn.onclick=function(){ state.editingId=h.UserMarkId; refreshDetail(); };
      acts.appendChild(editBtn);
    }
    wrap.appendChild(acts);
    return wrap;
  }

  function buildDetailBookmark(b,wrap){
    var title=document.createElement('div'); title.className='jb-detail-title';
    var slot=document.createElement('span'); slot.className='jb-bm-slot'; slot.textContent=(b.Slot!=null)?String(b.Slot+1):'•'; title.appendChild(slot);
    var ts=document.createElement('span'); ts.textContent=(b.Title&&b.Title.trim())||t('bm_label'); title.appendChild(ts); wrap.appendChild(title);
    wrap.appendChild(buildDetailMeta(b,null,'bookmark'));
    var content=document.createElement('div'); content.className='jb-detail-content';
    if(b.Snippet){ content.textContent=b.Snippet; } else { content.textContent=t('no_content'); content.style.color='#5a6883'; content.style.fontStyle='italic'; }
    wrap.appendChild(content);
    var acts=document.createElement('div'); acts.className='jb-detail-actions';
    var copyBtn=document.createElement('button'); copyBtn.className='jb-btn jb-btn-ghost'; copyBtn.textContent=t('copy');
    var copyText=((b.Title&&b.Title.trim())?b.Title+'\n\n':'')+(b.Snippet||'');
    copyBtn.onclick=function(){
      try{ navigator.clipboard.writeText(copyText).then(function(){ copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }); }
      catch(_){ var ta=document.createElement('textarea'); ta.value=copyText; document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');}catch(_){} document.body.removeChild(ta); copyBtn.textContent=t('copied'); setTimeout(function(){ copyBtn.textContent=t('copy'); },1500); }
    };
    acts.appendChild(copyBtn);
    if(state.db){
      var editBtn=document.createElement('button'); editBtn.className='jb-btn jb-btn-ghost'; editBtn.textContent=t('edit');
      editBtn.onclick=function(){ state.editingId=b.BookmarkId; refreshDetail(); };
      acts.appendChild(editBtn);
    }
    wrap.appendChild(acts);
    return wrap;
  }

  function buildDetailMeta(r,noteId,kind){
    var meta=document.createElement('div'); meta.className='jb-detail-meta';
    var pl=pubLabel(r);
    if(pl){ var p=document.createElement('span'); p.className='jb-detail-pub'; p.textContent=pl; meta.appendChild(p); }
    if(r.LastModified){ var d=document.createElement('span'); d.className='jb-detail-date'; d.textContent=t('modified')+': '+fmtDate(r.LastModified); meta.appendChild(d); }
    var tags=[];
    if(noteId) tags=state.tagsByNote[noteId]||[];
    else if(kind==='bookmark'&&r.LocationId) tags=state.tagsByLocation[r.LocationId]||[];
    if(tags.length){ var tw=document.createElement('span'); tw.className='jb-detail-tags'; tags.forEach(function(tg){ var c=document.createElement('span'); c.className='jb-tag'; c.textContent=tg.name; tw.appendChild(c); }); meta.appendChild(tw); }
    return meta;
  }

  function updateTabCounts(){
    if(!state.overlay) return;
    var tabs=state.overlay.querySelectorAll('.jb-tab');
    tabs.forEach(function(tab){
      var type=tab.dataset.type;
      var c=(type==='notes'?state.allNotes:(type==='highlights'?state.allHighlights:(type==='bookmarks'?state.allBookmarks:state.allInputFields))).length;
      var cnt=tab.querySelector('.jb-tab-count');
      if(cnt) cnt.textContent=c;
      if(type==='inputfields') tab.style.display=c>0?'':'none';
    });
  }

  function populateFilters(){
    if(!state.overlay) return;
    var tagSel=state.overlay.querySelector('.jb-filter-tag');
    var pubSel=state.overlay.querySelector('.jb-filter-pub');
    if(tagSel){
      tagSel.innerHTML='';
      var opt=document.createElement('option'); opt.value=''; opt.textContent=t('tag_all'); tagSel.appendChild(opt);
      state.allTags.forEach(function(tg){ var o=document.createElement('option'); o.value=String(tg.TagId); o.textContent=tg.Name+' ('+tg.count+')'; tagSel.appendChild(o); });
    }
    if(pubSel){
      pubSel.innerHTML='';
      var po=document.createElement('option'); po.value=''; po.textContent=t('pub_all'); pubSel.appendChild(po);
      state.allPublications.forEach(function(p){ var o=document.createElement('option'); o.value=String(p.LocationId); o.textContent=p.label; pubSel.appendChild(o); });
    }
  }

  function updateMobileView(){
    if(window.matchMedia('(max-width: 780px)').matches){
      if(!state.overlay.classList.contains('jb-mobile-detail')) state.overlay.classList.add('jb-mobile-list');
    } else {
      state.overlay.classList.remove('jb-mobile-list');
      state.overlay.classList.remove('jb-mobile-detail');
    }
  }

  // ---------- modal scaffolding ----------
  function buildOverlay(){
    var o=document.createElement('div');
    o.className='jb-overlay';
    o.onclick=function(e){ if(e.target===o) closeOverlay(); };
    var modal=document.createElement('div'); modal.className='jb-modal'; o.appendChild(modal);

    // Header
    var head=document.createElement('div'); head.className='jb-head';
    var ht=document.createElement('div'); ht.className='jb-head-title';
    ht.innerHTML='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg><span>'+htmlEscape(t('title'))+'</span><span class="jb-head-count"></span><span class="jb-dirty-badge" style="display:none"></span>';
    head.appendChild(ht);
    // Export button
    var exportBtn=document.createElement('button');
    exportBtn.className='jb-export-btn';
    exportBtn.disabled=true;
    exportBtn.innerHTML='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'+htmlEscape(t('export_db'));
    exportBtn.onclick=function(){ if(window.__jwHaptic) window.__jwHaptic(20); exportDb(); };
    var undoBtn=document.createElement('button'); undoBtn.type='button'; undoBtn.className='jb-undo'; undoBtn.disabled=true; undoBtn.title=t('undo');
    undoBtn.innerHTML='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14 4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-1"/></svg>';
    undoBtn.onclick=doUndo;
    var redoBtn=document.createElement('button'); redoBtn.type='button'; redoBtn.className='jb-redo'; redoBtn.disabled=true; redoBtn.title=t('redo');
    redoBtn.innerHTML='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 14 5-5-5-5"/><path d="M20 9H9a5 5 0 0 0 0 10h1"/></svg>';
    redoBtn.onclick=doRedo;
    head.appendChild(undoBtn); head.appendChild(redoBtn);
    head.appendChild(exportBtn);
    var mdBtn=document.createElement('button'); mdBtn.className='jb-md-btn'; mdBtn.type='button';
    mdBtn.title=t('md_hint');
    mdBtn.innerHTML='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>'+htmlEscape(t('export_md'));
    mdBtn.onclick=exportMarkdown;
    head.appendChild(mdBtn);
    var recvBtn=document.createElement('button'); recvBtn.type='button'; recvBtn.className='jb-md-btn'; recvBtn.textContent=t('open_share'); recvBtn.title=t('open_share'); recvBtn.onclick=function(){ if(window.__jwGoShare) window.__jwGoShare(); };
    head.appendChild(recvBtn);
    var changeFileBtn=document.createElement('button'); changeFileBtn.className='jb-change-file-btn'; changeFileBtn.type='button';changeFileBtn.innerHTML='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><polyline points="5 15 2 18 5 21"/><line x1="2" y1="18" x2="9" y2="18"/></svg>'+htmlEscape(t('change_file'));changeFileBtn.onclick=function(){if(state.dirty>0&&!window.confirm(t('unsaved_exit',{n:state.dirty}))) return;state.dirty=0;clearSessionFile();window.__openJwBrowse(undefined);};head.appendChild(changeFileBtn);var closeBtn=document.createElement('button'); closeBtn.className='jb-head-close'; closeBtn.textContent=t('close'); closeBtn.onclick=closeOverlay;
    head.appendChild(closeBtn);
    modal.appendChild(head);

    // Tabs
    var TAB_ORDER=['notes','highlights','bookmarks','inputfields'];
    function switchTo(type){
      if(!type || state.activeType===type) return;
      state.activeType=type; state.selected=null; state.editingId=null;
      if(state.selection) state.selection.clear(); state._batchUI='idle';
      if(state.overlay){ Array.prototype.forEach.call(state.overlay.querySelectorAll('.jb-tab'),function(tb){ tb.classList.toggle('active', tb.dataset.type===type); }); }
      applyFilter(); renderBody();
      if(window.__jwHaptic) window.__jwHaptic(15);
    }
    function switchByOffset(delta){
      var idx=TAB_ORDER.indexOf(state.activeType); if(idx<0) return;
      var next=idx+delta; if(next<0||next>=TAB_ORDER.length) return;
      if(TAB_ORDER[next]==='inputfields'&&!state.allInputFields.length){ next+=delta; if(next<0||next>=TAB_ORDER.length) return; }
      switchTo(TAB_ORDER[next]);
    }
    var tabs=document.createElement('div'); tabs.className='jb-tabs';
    [['notes',t('tab_notes')],['highlights',t('tab_highlights')],['bookmarks',t('tab_bookmarks')],['inputfields',t('tab_inputfields')]].forEach(function(pair){
      var b=document.createElement('button'); b.className='jb-tab'+(pair[0]===state.activeType?' active':''); b.dataset.type=pair[0];
      b.innerHTML='<span>'+htmlEscape(pair[1])+'</span><span class="jb-tab-count">0</span>';
      b.onclick=function(){ switchTo(pair[0]); };
      tabs.appendChild(b);
    });
    modal.appendChild(tabs);

    // Toolbar
    var toolbar=document.createElement('div'); toolbar.className='jb-toolbar';
    var askBtn=document.createElement('button'); askBtn.type='button'; askBtn.className='jb-ask-btn'+(state.askMode?' active':'');
    askBtn.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3l2.2 6 6 2.2-6 2.2L13 19.5 10.8 13.5l-6-2.2 6-2.2zM5 3.5v3M3.5 5h3"/></svg><span>'+htmlEscape(t('ask_btn'))+'</span>';
    askBtn.onclick=function(){ toggleAsk(askBtn); };
    toolbar.appendChild(askBtn);
    var search=document.createElement('label'); search.className='jb-search';
    search.innerHTML='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#7d8aa8" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>';
    var inp=document.createElement('input'); inp.type='search'; inp.placeholder=t('search');
    var searchDebounce=null;
    inp.oninput=function(){ clearTimeout(searchDebounce); searchDebounce=setTimeout(function(){ state.search=inp.value; applyFilter(); renderBody(); },200); };
    search.appendChild(inp); toolbar.appendChild(search);
    var tagSel=document.createElement('select'); tagSel.className='jb-select jb-filter-tag'; tagSel.onchange=function(){ state.tagId=tagSel.value; applyFilter(); renderBody(); }; toolbar.appendChild(tagSel);
    var pubSel=document.createElement('select'); pubSel.className='jb-select jb-filter-pub'; pubSel.onchange=function(){ state.pubId=pubSel.value; applyFilter(); renderBody(); }; toolbar.appendChild(pubSel);
    var dWrap=document.createElement('div'); dWrap.className='jb-date-wrap'; dWrap.title=t('date_range');
    var dFrom=document.createElement('input'); dFrom.type='date'; dFrom.className='jb-filter-date'; dFrom.setAttribute('aria-label',t('date_from'));
    var dTo=document.createElement('input'); dTo.type='date'; dTo.className='jb-filter-date'; dTo.setAttribute('aria-label',t('date_to'));
    dFrom.onchange=function(){ state.dateFrom=dFrom.value; state.page=0; applyFilter(); renderBody(); updateExtractBtn(); };
    dTo.onchange=function(){ state.dateTo=dTo.value; state.page=0; applyFilter(); renderBody(); updateExtractBtn(); };
    var dDash=document.createElement('span'); dDash.className='jb-date-dash'; dDash.textContent='\u2013';
    dWrap.appendChild(dFrom); dWrap.appendChild(dDash); dWrap.appendChild(dTo); toolbar.appendChild(dWrap);
    var extractBtn=document.createElement('button'); extractBtn.type='button'; extractBtn.className='jb-extract-btn'; extractBtn.textContent=t('extract_range'); extractBtn.title=t('extract_hint'); extractBtn.disabled=true;
    extractBtn.onclick=function(){ extractByDate(); };
    function updateExtractBtn(){ extractBtn.disabled=!(state.dateFrom||state.dateTo)||!state.db; }
    toolbar.appendChild(extractBtn);
    var colors=document.createElement('div'); colors.className='jb-colors';
    var allDot=document.createElement('button'); allDot.className='jb-color-dot active'; allDot.style.background='transparent'; allDot.style.border='2px dashed #5a6883'; allDot.title=t('color_all'); allDot.onclick=function(){ setColor('',allDot); }; colors.appendChild(allDot);
    [1,2,3,4,5,6].forEach(function(ci){ var b=document.createElement('button'); b.className='jb-color-dot'; b.style.background=COLORS[ci]; b.title='Color '+ci; b.onclick=function(){ setColor(String(ci),b); }; colors.appendChild(b); });
    function setColor(val,btn){ state.color=val; Array.prototype.forEach.call(colors.children,function(c){ c.classList.remove('active'); }); btn.classList.add('active'); applyFilter(); renderBody(); }
    toolbar.appendChild(colors);
    var sort=document.createElement('select'); sort.className='jb-select';
    [['newest',t('sort_newest')],['oldest',t('sort_oldest')],['pub',t('sort_pub')]].forEach(function(opt){ var o2=document.createElement('option'); o2.value=opt[0]; o2.textContent=opt[1]; sort.appendChild(o2); });
    sort.onchange=function(){ state.sort=sort.value; applyFilter(); renderBody(); }; toolbar.appendChild(sort);
    var clearBtn=document.createElement('button'); clearBtn.className='jb-clear'; clearBtn.textContent=t('clear');
    clearBtn.onclick=function(){
      state.search=''; state.color=''; state.sort='newest'; state.tagId=''; state.pubId=''; state.dateFrom=''; state.dateTo='';
      inp.value=''; sort.value='newest'; tagSel.value=''; pubSel.value=''; dFrom.value=''; dTo.value=''; updateExtractBtn();
      Array.prototype.forEach.call(colors.children,function(c){ c.classList.remove('active'); }); colors.children[0].classList.add('active');
      applyFilter(); renderBody();
    };
    toolbar.appendChild(clearBtn);
    var selectBtn=document.createElement('button'); selectBtn.type='button'; selectBtn.className='jb-select-toggle'; selectBtn.textContent=t('sel_mode');
    selectBtn.onclick=function(){ if(state.selectMode){  if(state._batchUI==='tag'){   var bi=state.overlay&&state.overlay.querySelector('.jb-batch-input');   var v=bi?bi.value.trim():'';   state._batchUI='idle';   if(v){ batchAddTag(v); return; }  }  exitSelectMode(); } else { enterSelectMode(); }};
    toolbar.appendChild(selectBtn);
    modal.appendChild(toolbar);
    var batchBar=document.createElement('div'); batchBar.className='jb-batch-bar'; batchBar.style.display='none'; modal.appendChild(batchBar);

    var body=document.createElement('div'); body.className='jb-body'; modal.appendChild(body);
    // Touch: horizontal swipe switches tabs (Notes ↔ Highlights ↔ Bookmarks)
    var _tsx=0, _tsy=0, _tsActive=false;
    body.addEventListener('touchstart',function(e){ if(e.touches&&e.touches.length===1){ _tsx=e.touches[0].clientX; _tsy=e.touches[0].clientY; _tsActive=true; } },{passive:true});
    body.addEventListener('touchend',function(e){
      if(!_tsActive) return; _tsActive=false;
      var tch=e.changedTouches&&e.changedTouches[0]; if(!tch) return;
      var dx=tch.clientX-_tsx, dy=tch.clientY-_tsy;
      if(Math.abs(dx)>60 && Math.abs(dx)>Math.abs(dy)*1.6){ switchByOffset(dx<0?1:-1); }
    },{passive:true});
    return o;
  }

  function clearSessionFile(){try{window.__jwLastFile=null;}catch(_){}try{var r=indexedDB.open('jwsync_session_v1',1);r.onsuccess=function(e){try{var db=e.target.result;var tx=db.transaction('file','readwrite');tx.objectStore('file').delete('current');tx.oncomplete=function(){db.close();};}catch(_){}};}catch(_){}}function closeOverlay(){
    if(state.dirty>0){
      if(!window.confirm(t('unsaved_exit',{n:state.dirty}))) return;
    }
    if(state.overlay&&state.overlay.parentNode) state.overlay.parentNode.removeChild(state.overlay);
    state.overlay=null;
    if(state.db){ try{ state.db.close(); }catch(_){} state.db=null; }
    var dl=document.getElementById('jb-tag-dl'); if(dl&&dl.parentNode) dl.parentNode.removeChild(dl);
    state.allNotes=[]; state.allHighlights=[]; state.allBookmarks=[]; state.allInputFields=[];
    state.tagsByNote={}; state.tagsByLocation={}; state.tagsByHighlight={};
    state.allTags=[]; state.allPublications=[];
    state.filtered=[]; state.selected=null; state.editingId=null;
    state.search=''; state.color=''; state.tagId=''; state.pubId=''; state.dateFrom=''; state.dateTo='';
    state.activeType='notes'; state.dirty=0; state.fileName='';
    state.selectMode=false; if(state.selection) state.selection.clear(); state.undo=[]; state.redo=[]; state._batchUI='idle';
    state.askMode=false; state.askResults=[]; state.askQuery=''; state.askPhase='idle'; state.askError='';
    if(ASK.worker){ try{ ASK.worker.terminate(); }catch(_){} ASK.worker=null; } if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; } ASK.vecs=null; ASK.pending={}; ASK._onReady=null; ASK._snap=null;
    document.removeEventListener('keydown',escHandler);
  }
  function escHandler(e){ if(e.key==='Escape') closeOverlay(); }

  // ---------- Ask Your Library (on-device semantic search) ----------
  var ASK = { worker:null, vecs:null, pending:{}, reqId:0, _onReady:null, _ticker:null, _buildStart:0, _snap:null, _rates:[] };
  var ASK_MODELS = { en:23, multi:50 };

  function getAskPref(){ try{ return JSON.parse(localStorage.getItem('jwsync_ask_v1')||'{}')||{}; }catch(_){ return {}; } }
  function setAskPref(o){ try{ var p=getAskPref(); for(var k in o){ p[k]=o[k]; } localStorage.setItem('jwsync_ask_v1', JSON.stringify(p)); }catch(_){} }
  function hashStr(s){ var h=5381; for(var i=0;i<s.length;i++){ h=((h<<5)+h+s.charCodeAt(i))|0; } return String(h); }
  function dotProd(a,b){ var n=Math.min(a.length,b.length), s=0; for(var i=0;i<n;i++){ s+=a[i]*b[i]; } return s; }
  function askNotes(){ var out=[]; (state.allNotes||[]).forEach(function(n){ var txt=((n.Title||'')+'\n'+stripHtml(n.Content||'')).replace(/\s+/g,' ').trim(); if(txt){ out.push({ note:n, text:txt, hash:hashStr(txt) }); } }); return out; }

  // IndexedDB cache for note vectors (keyed by model + note id)
  function idbOpen(){ return new Promise(function(res,rej){ try{ var r=indexedDB.open('jwsync_semantic',1); r.onupgradeneeded=function(){ var db=r.result; if(!db.objectStoreNames.contains('vecs')) db.createObjectStore('vecs',{keyPath:'key'}); }; r.onsuccess=function(){ res(r.result); }; r.onerror=function(){ rej(r.error); }; }catch(e){ rej(e); } }); }
  function idbGetModel(model){ return idbOpen().then(function(db){ return new Promise(function(res){ var out={}; try{ var tx=db.transaction('vecs','readonly'); var cur=tx.objectStore('vecs').openCursor(); cur.onsuccess=function(){ var c=cur.result; if(c){ var v=c.value; if(v&&v.model===model){ out[v.noteId]={ hash:v.hash, vec:new Float32Array(v.vec) }; } c.continue(); } else { res(out); } }; cur.onerror=function(){ res(out); }; }catch(e){ res(out); } }); }).catch(function(){ return {}; }); }
  function idbPutVec(model,noteId,hash,vec,dim){ idbOpen().then(function(db){ try{ var tx=db.transaction('vecs','readwrite'); tx.objectStore('vecs').put({ key:model+'|'+noteId, model:model, noteId:noteId, hash:hash, dim:dim, vec:vec.buffer.slice(0) }); }catch(e){} }).catch(function(){}); }
  function idbClearModel(model){ return idbOpen().then(function(db){ return new Promise(function(res){ try{ var tx=db.transaction('vecs','readwrite'); var cur=tx.objectStore('vecs').openCursor(); cur.onsuccess=function(){ var c=cur.result; if(c){ if(c.value&&c.value.model===model) c.delete(); c.continue(); } else { res(); } }; cur.onerror=function(){ res(); }; }catch(e){ res(); } }); }).catch(function(){}); }

  function ensureAskWorker(){
    if(ASK.worker) return ASK.worker;
    try{ ASK.worker=new Worker('./js/semantic-worker.js',{type:'module'}); }
    catch(e){ state.askError=t('ask_err'); return null; }
    ASK.worker.onmessage=function(ev){
      var d=ev.data||{};
      if(d.type==='modelProgress'){ if(d.total){ state.askProgress=Math.max(state.askProgress, Math.round((d.loaded/d.total)*100)); updateAskProgress(); } }
      else if(d.type==='ready'){ var cb=ASK._onReady; ASK._onReady=null; if(cb) cb(); }
      else if(d.type==='embedded'){ var p=ASK.pending[d.id]; if(p){ delete ASK.pending[d.id]; p(new Float32Array(d.buffer), d.dim, null); } }
      else if(d.type==='error'){ if(d.id!=null&&ASK.pending[d.id]){ var q=ASK.pending[d.id]; delete ASK.pending[d.id]; q(null,null,d.message); } else { setAskPref({model:''}); state.askPhase='idle'; state.askError=t('ask_err'); if(state.askMode) renderBody(); } }
    };
    ASK.worker.onerror=function(){ setAskPref({model:''}); state.askPhase='idle'; state.askError=t('ask_err'); if(state.askMode) renderBody(); };
    return ASK.worker;
  }
  function embedBatch(texts){ return new Promise(function(resolve,reject){ var w=ensureAskWorker(); if(!w){ reject(new Error('no worker')); return; } var id=++ASK.reqId; ASK.pending[id]=function(vec,dim,err){ if(err) reject(new Error(err)); else resolve({vec:vec,dim:dim}); }; w.postMessage({ type:'embed', id:id, texts:texts }); }); }

  function startAskEngine(model){
    state.askError=''; var w=ensureAskWorker(); if(!w){ state.askPhase='idle'; renderBody(); return; }
    state.askPhase='loading'; state.askProgress=0; renderBody();
    ASK._onReady=function(){ buildAskIndex(model); };
    w.postMessage({ type:'load', model:model });
  }
  function buildAskIndex(model){
    var notes=askNotes(); state.askTotal=notes.length; state.askDone=0;
    if(!notes.length){ state.askPhase='ready'; ASK.vecs=[]; renderBody(); return; }
    state.askPhase='building'; state.askProgress=0; renderBody();
    ASK._buildStart=Date.now(); ASK._snap=null; ASK._rates=[]; ASK._B=64;
    if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; }
    ASK._ticker=setInterval(function(){
      if(state.askPhase!=='building'){ clearInterval(ASK._ticker); ASK._ticker=null; return; }
      var total=state.askTotal||1, rawDone=state.askDone, snap=ASK._snap;
      var dispDone=rawDone;
      if(snap&&snap.rate>0&&rawDone<total){ var proj=rawDone+(Date.now()-snap.time)*snap.rate; dispDone=Math.min(rawDone+(ASK._B||48)-1, Math.min(total, proj)); }
      var pct=Math.min(99, dispDone/total*100);
      var f=state.overlay&&state.overlay.querySelector('.jb-ask-prog-fill'); if(f) f.style.width=pct+'%';
      var eta='';
      if(snap&&snap.rate>0&&rawDone<total){
        var etaSecs=Math.ceil((total-Math.min(total,dispDone))/(snap.rate*1000));
        if(etaSecs>0) eta=etaSecs>=60?'~'+Math.floor(etaSecs/60)+'m '+(etaSecs%60)+'s left':'~'+etaSecs+'s left';
      }
      var s=state.overlay&&state.overlay.querySelector('.jb-ask-status');
      if(s){ s.textContent=t('ask_building',{done:Math.min(total,Math.round(dispDone)),total:total})+(eta?' · '+eta:''); }
      var e=state.overlay&&state.overlay.querySelector('.jb-ask-eta'); if(e) e.textContent=eta;
    },250);
    idbGetModel(model).then(function(cached){
      var need=[]; notes.forEach(function(n){ var c=cached[n.note.NoteId]; if(!c||c.hash!==n.hash) need.push(n); });
      state.askDone=notes.length-need.length;
      var B=64, i=0;
      function step(){
        if(i>=need.length){
          if(ASK._ticker){ clearInterval(ASK._ticker); ASK._ticker=null; }
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          state.askPhase='ready'; state.askProgress=100; renderBody(); return;
        }
        var batch=need.slice(i,i+B); i+=B; var batchStart=Date.now();
        embedBatch(batch.map(function(x){ return x.text; })).then(function(r){
          var dim=r.dim, arr=r.vec;
          for(var j=0;j<batch.length;j++){ var v=arr.slice(j*dim,(j+1)*dim); cached[batch[j].note.NoteId]={ hash:batch[j].hash, vec:v }; idbPutVec(model,batch[j].note.NoteId,batch[j].hash,v,dim); }
          state.askDone=Math.min(notes.length, state.askDone+batch.length);
          ASK.vecs=notes.map(function(n){ var c=cached[n.note.NoteId]; return c?{ note:n.note, vec:c.vec }:null; }).filter(Boolean);
          var batchMs=Math.max(1,Date.now()-batchStart);
          ASK._rates.push(batch.length/batchMs); if(ASK._rates.length>4) ASK._rates.shift();
          var avgRate=ASK._rates.reduce(function(a,b){return a+b;},0)/ASK._rates.length;
          ASK._snap={time:Date.now(),done:state.askDone,rate:avgRate};
          state.askProgress=Math.round(state.askDone/notes.length*100);
          step();
        }).catch(function(){ if(ASK._ticker){clearInterval(ASK._ticker);ASK._ticker=null;} state.askError=t('ask_err'); state.askPhase='idle'; renderBody(); });
      }
      step();
    });
  }
  function doAskSearch(q){
    q=(q||'').trim(); state.askQuery=q; state.askError='';
    if(!q){ state.askResults=[]; renderBody(); return; }
    if((state.askPhase!=='ready'&&state.askPhase!=='building')||!ASK.vecs||!ASK.vecs.length){ return; }
    embedBatch([q]).then(function(r){
      var qv=r.vec.subarray ? r.vec.subarray(0,r.dim) : r.vec.slice(0,r.dim);
      var scored=ASK.vecs.map(function(e){ return { note:e.note, score:dotProd(qv,e.vec) }; });
      scored.sort(function(a,b){ return b.score-a.score; });
      state.askResults=scored.filter(function(s){ return s.score>0.12; }).slice(0,50);
      state.selected=null; renderBody();
    }).catch(function(){ state.askError=t('ask_err'); renderBody(); });
  }

  function updateAskProgress(){
    if(!state.askMode||!state.overlay) return;
    var f=state.overlay.querySelector('.jb-ask-prog-fill'); if(f) f.style.width=state.askProgress+'%';
    var s=state.overlay.querySelector('.jb-ask-status');
    if(s){ s.textContent = state.askPhase==='loading' ? t('ask_loading_model',{pct:state.askProgress}) : t('ask_building',{done:state.askDone||0,total:state.askTotal||0}); }
  }

  function toggleAsk(btn){ if(state.askMode){ closeAsk(); } else { openAsk(); } }
  function openAsk(){
    state.askMode=true; state.activeType='notes'; state.selected=null; state.editingId=null; state.askError='';
    var b=state.overlay.querySelector('.jb-ask-btn'); if(b) b.classList.add('active');
    var pref=getAskPref();
    if(pref.model && state.askPhase==='idle' && !ASK.vecs){ startAskEngine(pref.model); }
    else { renderBody(); }
  }
  function closeAsk(){ state.askMode=false; state.selected=null; var b=state.overlay.querySelector('.jb-ask-btn'); if(b) b.classList.remove('active'); applyFilter(); renderBody(); }

  function renderAsk(body){
    var list=document.createElement('div'); list.className='jb-list';
    var panel=document.createElement('div'); panel.className='jb-ask-panel';
    var head=document.createElement('div'); head.className='jb-ask-head';
    head.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3l2.2 6 6 2.2-6 2.2L13 19.5 10.8 13.5l-6-2.2 6-2.2zM5 3.5v3M3.5 5h3"/></svg><span>'+htmlEscape(t('ask_title'))+'</span>';
    panel.appendChild(head);
    var sub=document.createElement('div'); sub.className='jb-ask-sub'; sub.textContent=t('ask_sub'); panel.appendChild(sub);

    function emptyMsg(txt){ var d=document.createElement('div'); d.className='jb-ask-empty'; d.textContent=txt; return d; }
    function appendDetail(){ var detail=document.createElement('div'); detail.className='jb-detail'; detail.appendChild(buildDetail(state.selected)); body.appendChild(detail); }
    function finish(){ list.appendChild(panel); body.appendChild(list); appendDetail(); }

    if(!askNotes().length){ panel.appendChild(emptyMsg(t('ask_no_notes'))); finish(); return; }
    var pref=getAskPref();
    if(!pref.model){
      var card=document.createElement('div'); card.className='jb-ask-enable';
      if(state.askError){ var erTop=document.createElement('div'); erTop.className='jb-ask-err'; erTop.style.marginBottom='12px'; erTop.textContent=state.askError; card.appendChild(erTop); state.askError=''; }
      var h4=document.createElement('h4'); h4.textContent=t('ask_enable_title'); card.appendChild(h4);
      var p=document.createElement('p'); p.textContent=t('ask_enable_body'); card.appendChild(p);
      var models=document.createElement('div'); models.className='jb-ask-models';
      [['en',t('ask_model_en_name'),t('ask_model_en_desc')],['multi',t('ask_model_multi_name'),t('ask_model_multi_desc')]].forEach(function(m){
        var mb=document.createElement('button'); mb.type='button'; mb.className='jb-ask-model-btn';
        mb.innerHTML='<div class="jb-ask-model-name">'+htmlEscape(m[1])+'</div><div class="jb-ask-model-desc">'+htmlEscape(m[2])+'</div><span class="jb-ask-model-size">'+htmlEscape(t('ask_size_once',{n:ASK_MODELS[m[0]]}))+'</span>';
        mb.onclick=function(){ setAskPref({model:m[0]}); state.askPhase='idle'; ASK.vecs=null; startAskEngine(m[0]); };
        models.appendChild(mb);
      });
      card.appendChild(models);
      var priv=document.createElement('div'); priv.className='jb-ask-privacy';
      priv.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><span>'+htmlEscape(t('ask_privacy'))+'</span>';
      card.appendChild(priv);
      panel.appendChild(card); finish(); return;
    }

    // Query bar (model chosen)
    var bar=document.createElement('div'); bar.className='jb-ask-bar';
    var inp=document.createElement('input'); inp.className='jb-ask-input'; inp.type='search'; inp.placeholder=t('ask_placeholder'); inp.value=state.askQuery||'';
    inp.onkeydown=function(e){ if(e.key==='Enter'){ e.preventDefault(); doAskSearch(inp.value); } };
    var go=document.createElement('button'); go.className='jb-ask-go'; go.textContent=t('ask_go'); go.disabled=(state.askPhase!=='ready'&&!(state.askPhase==='building'&&ASK.vecs&&ASK.vecs.length));
    go.onclick=function(){ doAskSearch(inp.value); };
    bar.appendChild(inp); bar.appendChild(go); panel.appendChild(bar);

    if(state.askPhase==='loading'||state.askPhase==='building'){
      var st=document.createElement('div'); st.className='jb-ask-status';
      st.textContent = state.askPhase==='loading' ? t('ask_loading_model',{pct:state.askProgress}) : t('ask_building',{done:state.askDone||0,total:state.askTotal||0});
      panel.appendChild(st);
      var pr=document.createElement('div'); pr.className='jb-ask-prog'; var pf=document.createElement('div'); pf.className='jb-ask-prog-fill'; pf.style.width=state.askProgress+'%'; pr.appendChild(pf); panel.appendChild(pr);
      if(state.askPhase==='building'){
        var etaEl=document.createElement('div'); etaEl.className='jb-ask-eta'; panel.appendChild(etaEl);
        var hint=document.createElement('div'); hint.className='jb-ask-once-hint'; hint.textContent='First-time only — saved to your device, instant next time.'; panel.appendChild(hint);
        if(ASK.vecs&&ASK.vecs.length){
          var pn=document.createElement('div'); pn.className='jb-ask-part-note'; pn.textContent='Searching '+ASK.vecs.length+' of '+(state.askTotal||0)+' notes indexed so far.'; panel.appendChild(pn);
          if(state.askResults&&state.askResults.length){
            var rh=document.createElement('div'); rh.className='jb-ask-results-head'; rh.textContent=t('ask_results_head',{n:state.askResults.length}); panel.appendChild(rh);
            state.askResults.forEach(function(res){ var wrap=document.createElement('div'); wrap.style.position='relative'; var row=buildRow(res.note); var sc=document.createElement('span'); sc.className='jb-ask-score'; sc.textContent=Math.round(res.score*100)+'%'; sc.style.cssText='position:absolute;top:10px;right:10px;pointer-events:none'; wrap.appendChild(row); wrap.appendChild(sc); panel.appendChild(wrap); });
          }
        }
      }
    } else if(state.askPhase==='ready'){
      if(state.askResults && state.askResults.length){
        var rh=document.createElement('div'); rh.className='jb-ask-results-head'; rh.textContent=t('ask_results_head',{n:state.askResults.length}); panel.appendChild(rh);
        state.askResults.forEach(function(res){
          var wrap=document.createElement('div'); wrap.style.position='relative';
          var row=buildRow(res.note);
          var sc=document.createElement('span'); sc.className='jb-ask-score'; sc.textContent=Math.round(res.score*100)+'%';
          sc.style.position='absolute'; sc.style.top='10px'; sc.style.right='10px'; sc.style.pointerEvents='none';
          wrap.appendChild(row); wrap.appendChild(sc); panel.appendChild(wrap);
        });
      } else if(state.askQuery){ panel.appendChild(emptyMsg(t('ask_no_results'))); }
      else { panel.appendChild(emptyMsg(t('ask_ready'))); }
      var ctl=document.createElement('div'); ctl.style.cssText='display:flex;gap:8px;margin-top:16px;flex-wrap:wrap';
      var rb=document.createElement('button'); rb.className='jb-ask-rebuild'; rb.textContent=t('ask_rebuild');
      rb.onclick=function(){ var m=getAskPref().model; ASK.vecs=null; state.askResults=[]; state.askQuery=''; idbClearModel(m).then(function(){ startAskEngine(m); }); };
      var sw=document.createElement('button'); sw.className='jb-ask-rebuild'; sw.textContent=t('ask_switch_model');
      sw.onclick=function(){ setAskPref({model:''}); state.askPhase='idle'; ASK.vecs=null; state.askResults=[]; state.askQuery=''; renderBody(); };
      ctl.appendChild(rb); ctl.appendChild(sw); panel.appendChild(ctl);
    }
    finish();
    if(state.askPhase==='ready'&&!state.selectMode){ setTimeout(function(){ try{ var fi=panel.querySelector('.jb-ask-input'); if(fi){ var v=fi.value; fi.focus(); fi.value=''; fi.value=v; } }catch(_){} }, 0); }
  }

  // ---------- public entry ----------
  window.__openJwBrowse = function(file){
    if(state.overlay) closeOverlay();
    state.overlay=buildOverlay();
    document.body.appendChild(state.overlay);
    document.addEventListener('keydown',escHandler);
    if(!file){
      var body=state.overlay.querySelector('.jb-body');
      body.innerHTML='';
      var center=document.createElement('div'); center.className='jb-empty';
      center.style.cssText='display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center;height:100%';
      var msg=document.createElement('div'); msg.textContent=t('no_file'); center.appendChild(msg);
      var picker=document.createElement('button'); picker.className='jb-btn'; picker.textContent=t('pick_file');
      picker.onclick=function(){
        var fi=document.createElement('input'); fi.type='file'; fi.accept='.jwlibrary,.zip';
        fi.onchange=function(){ if(fi.files&&fi.files[0]){ try{ window.__jwLastFile=fi.files[0]; }catch(_){} loadFromFile(fi.files[0]); } };
        fi.click();
      };
      center.appendChild(picker); body.appendChild(center); return;
    }
    loadFromFile(file);
  };
})();
};

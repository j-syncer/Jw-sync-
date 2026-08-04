# -*- coding: utf-8 -*-
"""Spanish copy for the static guide pages, keyed by slug.

Field names mirror build_guides.GUIDES. Anything left out falls back to
English. `group` and `related` are deliberately not translated — the first is
looked up through CHROME["es"]["groups"], the second is a list of slugs.

Product names stay as they appear in the Spanish JW Library app and in the
file system: JW Library, JW Sync, .jwlibrary, Google Drive, iCloud.
"""

GUIDES_ES = {

 "merge-jw-library-backups": {
  "title": "Cómo combinar copias de seguridad de JW Library de dos dispositivos",
  "h1": "Cómo combinar copias de seguridad de JW Library de dos dispositivos",
  "description": "Une las notas, los subrayados, los marcadores y las etiquetas de dos o más copias de seguridad de JW Library en un solo archivo .jwlibrary: gratis, privado y en tu navegador.",
  "intro": [
   "Si estudias en más de un dispositivo —el teléfono en el Salón, la tableta en casa— cada uno acaba con sus propias notas y subrayados. La función de copia de seguridad y restauración de JW Library no puede unirlos: al restaurar una copia se reemplaza todo lo que hay en el dispositivo y se borra el trabajo del otro.",
   "JW Sync resuelve esto. Lee dos (o más) archivos .jwlibrary y combina las notas, los subrayados, los marcadores y las etiquetas de todos ellos en una copia de seguridad nueva. Todo ocurre dentro de tu navegador: tus archivos nunca se suben a ningún servidor, así que tus notas de estudio siguen siendo privadas.",
  ],
  "steps": [
   ("Crea una copia de seguridad en cada dispositivo", "En JW Library, abre Estudio personal, toca el menú de tres puntos, elige Copia de seguridad y restauración y luego Crear una copia de seguridad. Hazlo en cada dispositivo. Cada uno genera un archivo .jwlibrary."),
   ("Abre JW Sync", "Entra en jwsync.org desde cualquier navegador: teléfono, tableta u ordenador. No hay nada que instalar."),
   ("Carga los dos archivos", "Arrastra (o selecciona) los archivos .jwlibrary. JW Sync los lee localmente en tu dispositivo."),
   ("Revisa la vista previa", "Antes de escribir nada, una vista previa muestra exactamente qué se va a combinar. Si la misma nota se editó de forma distinta en cada dispositivo, el revisor de conflictos muestra ambas versiones lado a lado con las diferencias palabra por palabra para que elijas cuál conservar, o deja que «Sugerir la mejor» elija por ti."),
   ("Descarga el archivo combinado y restáuralo", "Descarga el archivo .jwlibrary combinado y restáuralo en cada dispositivo desde Copia de seguridad y restauración → Restaurar. Ahora los dos dispositivos tienen la biblioteca completa."),
  ],
  "sections": [
   ("¿Qué se combina?",
    "Las notas, los subrayados, los marcadores, las etiquetas y sus conexiones. Los duplicados se detectan automáticamente, así que restaurar el archivo combinado nunca duplica nada. Las copias de Android, iPhone, iPad y la aplicación de Windows usan el mismo formato y se combinan sin problema."),
   ("¿Es seguro?",
    "La combinación nunca modifica tus archivos originales: genera una copia de seguridad totalmente nueva, así que los originales quedan intactos como respaldo. Y como todo se ejecuta en el navegador, ningún dato sale de tu dispositivo."),
  ],
  "faq": [
   ("¿Puedo combinar más de dos copias?", "Sí: carga tantos archivos .jwlibrary como dispositivos tengas. Todos se combinan en una sola copia de seguridad."),
   ("¿La combinación creará notas duplicadas?", "No. Las notas, los subrayados y los marcadores idénticos se detectan y se conservan una sola vez. Las versiones realmente distintas de una misma nota aparecen en el revisor de conflictos para que decidas."),
   ("¿Funciona entre Android y iPhone?", "Sí. El formato .jwlibrary es idéntico en Android, iOS, iPadOS y Windows, así que las copias de distintas plataformas se combinan sin ninguna conversión."),
  ],
 },

 "sync-jw-library-multiple-devices": {
  "title": "Cómo sincronizar JW Library entre varios dispositivos",
  "h1": "Cómo mantener JW Library sincronizado entre varios dispositivos",
  "description": "JW Library no sincroniza entre dispositivos. Aquí tienes una rutina sencilla y privada para mantener las notas, los subrayados y los marcadores idénticos en tu teléfono, tableta y ordenador.",
  "intro": [
   "JW Library no sincroniza los datos de estudio personal entre dispositivos: no hay ninguna cuenta que lleve tus notas del teléfono a la tableta. El mecanismo oficial es copia de seguridad y restauración, y una restauración reemplaza por completo los datos del dispositivo. ¿Cómo mantener dos o tres dispositivos idénticos sin perder nada?",
   "La respuesta es una rutina corta: combinar y restaurar. Hecha cada semana o cada mes, lleva unos dos minutos y mantiene tu biblioteca completa en todos los dispositivos.",
  ],
  "steps": [
   ("Haz una copia de cada dispositivo", "En cada uno: Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Obtienes un archivo .jwlibrary por dispositivo."),
   ("Combínalas en jwsync.org", "Carga todos los archivos. JW Sync une las notas, los subrayados, los marcadores y las etiquetas de cada dispositivo en un único archivo .jwlibrary, localmente en tu navegador y sin subir nada."),
   ("Restaura el archivo combinado en todos", "Copia de seguridad y restauración → Restaurar y elige el archivo combinado. Ahora todos los dispositivos son idénticos y están completos."),
   ("Deja que JW Sync te lo recuerde", "Activa un recordatorio de sincronización (semanal o mensual) en JW Sync y te avisará cuando toque repetir la rutina. Además recuerda tus dispositivos guardados, así cada ronda es más rápida."),
  ],
  "sections": [
   ("¿Por qué no restaurar simplemente la copia más reciente?",
    "Porque «la más reciente» solo refleja un dispositivo. Si tomaste notas de la reunión en el teléfono y notas de estudio en la tableta la misma semana, cada copia tiene contenido que a la otra le falta. Restaurar una sobre la otra pierde la mitad de tu trabajo. Combinar primero es lo que hace segura la rutina."),
   ("¿Cada cuánto debería sincronizar?",
    "Según cómo estudies. Dos dispositivos activos a diario: cada semana va cómodo. Una tableta que solo sale para las reuniones: cada mes sobra. Esperar más solo significa que la combinación tendrá más que unir; entre rondas nunca se pierde nada."),
  ],
  "faq": [
   ("¿JW Sync funciona en segundo plano?", "No: es una página web, no un servicio instalado. Nada analiza tus dispositivos. Tú ejecutas la rutina cuando quieres; el recordatorio opcional es solo un aviso."),
   ("¿Puedo sincronizar tres o más dispositivos?", "Sí. Haz una copia de cada uno, carga todos los archivos, combina una vez y restaura el resultado en todas partes."),
  ],
 },

 "transfer-jw-library-notes-new-phone": {
  "title": "Cómo pasar las notas de JW Library a un teléfono nuevo",
  "h1": "Cómo pasar las notas de JW Library a un teléfono nuevo",
  "description": "Paso a paso: lleva todas tus notas, subrayados, marcadores y etiquetas de JW Library a un teléfono nuevo con una copia .jwlibrary, y cómo combinar si ya escribiste notas en el nuevo.",
  "intro": [
   "Las herramientas de transferencia de teléfono mueven tus aplicaciones y fotos, pero no llevan de forma fiable los datos de estudio personal de JW Library. La manera segura de trasladar tus notas, subrayados, marcadores y etiquetas es el propio archivo de copia de seguridad de JW Library: lleva unos minutos y funciona entre plataformas.",
  ],
  "steps": [
   ("Crea una copia en el teléfono antiguo", "Abre JW Library → Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Se guarda un archivo .jwlibrary con todos tus datos de estudio."),
   ("Pasa el archivo al teléfono nuevo", "Envíatelo por correo o usa Google Drive, iCloud, AirDrop o un cable USB. El archivo es pequeño, normalmente unos pocos megabytes."),
   ("Restaura en el teléfono nuevo", "Instala JW Library y ve a Estudio personal → Copia de seguridad y restauración → Restaurar; elige el archivo .jwlibrary. Aparecerán todas las notas, subrayados, marcadores y etiquetas."),
  ],
  "sections": [
   ("¿Ya escribiste notas en el teléfono nuevo? Combina en vez de sobrescribir",
    "Restaurar reemplaza lo que haya en el dispositivo. Si llevas un tiempo usando el teléfono nuevo y tiene sus propias notas, no restaures encima: haz también una copia del nuevo, combina la antigua y la nueva en un solo archivo en jwsync.org (gratis, en tu navegador y sin subir nada) y restaura el resultado. Conservas los dos conjuntos de notas."),
   ("Un problema habitual en iPhone",
    "Si el archivo llega al iPhone renombrado como .zip, cámbiale la extensión a .jwlibrary antes de restaurar: el contenido está bien, solo cambió la extensión durante el envío."),
  ],
  "faq": [
   ("¿Esto trasladará también mis publicaciones descargadas?", "La copia lleva tus datos de estudio personal: notas, subrayados, marcadores, etiquetas y listas de reproducción. Las publicaciones sencillamente se vuelven a descargar en el teléfono nuevo."),
   ("¿Importa si los teléfonos tienen versiones distintas de Android?", "No. El formato .jwlibrary es el mismo en todas partes, incluso entre versiones de Android y entre Android e iPhone."),
  ],
 },

 "jw-library-android-to-iphone": {
  "title": "Pasar JW Library de Android a iPhone (sin perder notas)",
  "h1": "Pasar JW Library de Android a iPhone o iPad conservando cada nota",
  "description": "El formato de copia .jwlibrary es idéntico en Android y iOS. Cómo llevar tus notas, subrayados y marcadores entre plataformas, y cómo combinar si ambos dispositivos tienen notas.",
  "intro": [
   "Cambiar de plataforma es el momento en que la gente teme perder años de notas de estudio: las aplicaciones de transferencia de Android a iPhone se saltan por completo los datos de JW Library. La buena noticia es que el formato de copia de seguridad de JW Library es idéntico en Android, iPhone, iPad y Windows, así que el cambio se reduce a una copia, un envío de archivo y una restauración.",
  ],
  "steps": [
   ("Haz la copia en el teléfono Android", "JW Library → Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Guarda el archivo .jwlibrary."),
   ("Envía el archivo al iPhone o iPad", "Correo, Google Drive, iCloud Drive: cualquier cosa que mueva un archivo. Si iOS lo renombra a .zip por el camino, devuélvele la extensión .jwlibrary."),
   ("Restaura en el dispositivo nuevo", "Instala JW Library, inicia sesión y ve a Copia de seguridad y restauración → Restaurar; elige el archivo. Llegan las notas, los subrayados, los marcadores, las etiquetas y las listas de reproducción."),
  ],
  "sections": [
   ("Si el iPhone ya tiene notas",
    "Restaurar reemplaza los datos del dispositivo. Cuando el nuevo ya tiene sus propias notas, haz también una copia y combina las dos en un solo archivo en jwsync.org —la combinación une ambas bibliotecas en tu navegador sin subir nada— y restaura después el resultado. No se pierde nada de ninguno de los dos lados."),
   ("Los mismos pasos sirven en cualquier dirección",
    "De iPhone a Android, de Android a Android, añadir un iPad como segundo dispositivo de estudio o pasar a la aplicación de Windows: el archivo de copia de seguridad es el idioma común entre todos."),
  ],
  "faq": [
   ("¿Necesito un ordenador para hacerlo?", "No. Todo el traslado puede hacerse de teléfono a teléfono con el correo o un servicio en la nube."),
   ("¿Se conservarán los colores de mis subrayados?", "Sí: los subrayados mantienen sus colores, las notas sus etiquetas y los marcadores su sitio."),
  ],
 },

 "backup-jw-library": {
  "title": "Cómo hacer una copia de seguridad de JW Library correctamente",
  "h1": "Cómo hacer una copia de seguridad de JW Library correctamente",
  "description": "Una rutina de copia de seguridad de 30 segundos que protege años de notas, subrayados y marcadores de JW Library, y el error habitual que pilla a mucha gente.",
  "intro": [
   "Una copia de seguridad bien hecha de JW Library lleva medio minuto y protege años de estudio acumulado. Casi todas las historias de pérdida de datos empiezan igual: no había ningún archivo .jwlibrary reciente cuando el teléfono se perdió, se reinició o se cambió.",
  ],
  "steps": [
   ("Crea la copia", "Abre JW Library → Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Se genera un archivo .jwlibrary con todas las notas, subrayados, marcadores y etiquetas."),
   ("Guárdala fuera del teléfono", "Envíatela por correo o guárdala en Google Drive, iCloud o OneDrive. Una copia que solo vive en el teléfono desaparece con el teléfono."),
   ("Repítelo periódicamente", "Una vez al mes es un buen punto de partida; antes de cambiar de teléfono, reiniciarlo o actualizar el sistema es imprescindible. Conserva las copias antiguas: los archivos son pequeños y una copia vieja ha salvado a mucha gente."),
  ],
  "sections": [
   ("El error habitual: confiar en la copia en la nube del teléfono",
    "Una copia completa del teléfono (Google One, copia de dispositivo de iCloud) a menudo restaura una versión antigua de los datos de JW Library, o ninguna. El archivo .jwlibrary es la única copia que controlas del todo y que puedes llevar entre plataformas. Trata la copia del teléfono como un extra, no como el plan."),
   ("¿Has acabado con dos copias distintas?",
    "Pasa: una copia del teléfono, otra más antigua de una tableta, cada una con notas propias. Nunca tienes que elegir entre ellas: combínalas en un solo archivo completo en jwsync.org, gratis y en privado, desde el navegador."),
  ],
  "faq": [
   ("¿Cuánto ocupa una copia de seguridad?", "Normalmente unos pocos megabytes incluso con bibliotecas muy grandes: cabe en un correo."),
   ("¿Crear una copia cambia algo en mi teléfono?", "No. Solo escribe el archivo; tu biblioteca queda intacta."),
  ],
 },

 "jw-library-restore-replaced-notes": {
  "title": "¿La restauración de JW Library reemplazó tus notas? Cómo recuperarlas",
  "h1": "¿La restauración reemplazó tus notas? Así se combinan las dos copias",
  "description": "La restauración de JW Library sustituye por completo, no combina: las notas escritas después de la copia parecen perdidas. Si conservas los dos archivos, no se ha perdido nada. Aquí está la solución.",
  "intro": [
   "Es un momento horrible: restauras una copia en un dispositivo que ya tenía notas y la restauración lo reemplaza todo; las notas escritas desde esa copia parecen haber desaparecido. Ocurre porque la copia de seguridad y restauración de JW Library sustituye por completo, no combina.",
   "El dato clave: si el trabajo más reciente sigue existiendo en algún archivo de copia, en realidad no se ha perdido nada. La solución es combinar las dos copias en vez de elegir entre ellas.",
  ],
  "steps": [
   ("Para: no vuelvas a restaurar", "Cada restauración reemplaza los datos actuales del dispositivo. Detente antes de que desaparezca algo más."),
   ("Haz una copia del dispositivo tal como está ahora", "Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad. Así conservas el estado actual, sea cual sea."),
   ("Busca la copia que tiene las notas que faltan", "El archivo .jwlibrary desde el que restauraste, o uno anterior: revisa tu correo, Drive, iCloud y la carpeta de descargas."),
   ("Combina los dos archivos en jwsync.org", "Carga las dos copias. JW Sync une todas las notas, subrayados, marcadores y etiquetas de ambas en un archivo nuevo, en tu navegador y sin subir nada. Las versiones en conflicto de una misma nota se muestran lado a lado para que elijas."),
   ("Restaura el archivo combinado", "Copia de seguridad y restauración → Restaurar con el .jwlibrary combinado. Los dos conjuntos de notas vuelven al dispositivo."),
  ],
  "sections": [
   ("¿Y si no hay ninguna copia de las notas más recientes?",
    "Si la única copia de las notas nuevas estaba en el dispositivo y una restauración ya las sobrescribió, JW Library no ofrece deshacer. Por eso el paso 2 —hacer una copia del estado actual antes de tocar nada— importa tanto siempre que los datos parezcan raros. De aquí en adelante, la rutina de combinar primero hace que el problema sea imposible."),
  ],
  "faq": [
   ("¿La combinación duplicará las notas que comparten las dos copias?", "No: los elementos idénticos se detectan y se conservan una sola vez. Solo se marcan para revisión las versiones realmente distintas de una misma nota."),
   ("¿Esto arregla una copia que no se restaura en absoluto?", "Eso suele ser un archivo dañado, no una sobrescritura: mira la guía para reparar una copia dañada más abajo."),
  ],
 },

 "fix-corrupted-jw-library-backup": {
  "title": "Reparar una copia de JW Library dañada que no se restaura",
  "h1": "Reparar una copia dañada de JW Library con el Doctor de Biblioteca",
  "description": "¿JW Library se niega a restaurar tu archivo .jwlibrary? El Doctor de Biblioteca analiza la copia en tu navegador, repara los problemas habituales y genera una copia limpia que sí se restaura.",
  "intro": [
   "A veces JW Library rechaza un archivo de copia: la restauración falla, da error o el archivo no se abre. Causas habituales: una descarga interrumpida, un servicio en la nube que estropeó el archivo, una extensión cambiada durante el envío o incoherencias internas acumuladas con los años.",
   "JW Sync incluye el Doctor de Biblioteca, un analizador que revisa un archivo .jwlibrary y repara los problemas más comunes, todo dentro de tu navegador y sin que el archivo salga nunca de tu dispositivo.",
  ],
  "steps": [
   ("Abre JW Sync y carga el archivo problemático", "Entra en jwsync.org y carga el archivo .jwlibrary que no se restaura. (Si llegó renombrado como .zip, devuélvele primero la extensión .jwlibrary: eso solo ya resuelve muchos casos.)"),
   ("Ejecuta el análisis del Doctor", "El Doctor examina la estructura interna de la copia y enumera lo que encuentra —desde rarezas inofensivas hasta daños reales— en lenguaje claro."),
   ("Aplica las reparaciones", "Un toque repara lo que se puede reparar. El Doctor nunca modifica tu archivo original: genera una copia limpia, así que el original queda intacto como respaldo."),
   ("Descarga y restaura el archivo reparado", "Restaura el .jwlibrary limpio desde Copia de seguridad y restauración → Restaurar en JW Library."),
  ],
  "sections": [
   ("El Doctor también actúa en cada combinación",
    "Las mismas comprobaciones se ejecutan automáticamente dentro del motor de combinación, así que la copia combinada sale siempre limpia, incluso si alguno de los archivos de partida tenía problemas que nunca notaste."),
   ("Cuando un archivo no tiene arreglo",
    "Si el archivo quedó truncado hasta el punto de que los datos sencillamente no están, ninguna herramienta puede inventarlos. El Doctor lo dirá con honestidad en vez de entregar un archivo dudoso, y esa es la señal para buscar una copia anterior en el correo, en Drive o en iCloud: otra razón por la que merece la pena guardar las copias antiguas."),
  ],
  "faq": [
   ("¿Se suben mis datos para el análisis?", "No. El análisis, las reparaciones y la exportación se ejecutan localmente en el navegador."),
   ("¿Puede recuperar notas borradas dentro de JW Library?", "No: repara la estructura del archivo. Las notas borradas en la aplicación antes de hacer la copia no están en el archivo y no se pueden recuperar."),
  ],
 },

 "edit-jw-library-notes": {
  "title": "Ver y editar las notas de JW Library en el navegador",
  "h1": "Ver, buscar y editar tus notas de JW Library: el Explorador de Estudio",
  "description": "Abre cualquier copia .jwlibrary en tu navegador para explorar, buscar, editar, reetiquetar, recolorear y limpiar en bloque tus notas, subrayados y marcadores de JW Library. Sin subir nada.",
  "intro": [
   "JW Library está pensado para tomar notas, no para gestionar miles de ellas. El Explorador de Estudio abre cualquier copia .jwlibrary directamente en tu navegador y la convierte en un gestor de biblioteca donde puedes buscar y editar: notas, subrayados y marcadores en un solo sitio, y sin subir nada a ninguna parte.",
  ],
  "steps": [
   ("Carga una copia de seguridad", "Crea una copia en JW Library (Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad), abre jwsync.org y carga el archivo en el Explorador de Estudio."),
   ("Explora y busca en todo", "Tres pestañas —Notas, Subrayados, Marcadores— con búsqueda de texto completo y filtros por color, etiqueta y publicación. Una pestaña de Respuestas de estudio muestra además lo que escribiste en las publicaciones."),
   ("Edita sobre la marcha", "Abre cualquier nota para editar su título y su contenido con formato (negrita, cursiva, subrayado, listas), cambiar el color del subrayado y añadir o quitar etiquetas. Los marcadores y los colores se editan igual."),
   ("Limpia en bloque", "Selecciona muchas notas a la vez para reetiquetar, recolorear o borrar juntas, con deshacer y rehacer completos, así que un desliz nunca es fatal. También puedes extraer un intervalo de fechas a una copia nueva o copiar las notas como Markdown."),
   ("Exporta tu biblioteca editada", "Descarga el .jwlibrary editado y restáuralo en JW Library. Tus cambios ya están en el dispositivo."),
  ],
  "sections": [
   ("¿Por qué editar en el navegador y no en la aplicación?",
    "Por la escala. Renombrar una etiqueta en 300 notas, recolorear todos los subrayados amarillos de una publicación o borrar años de marcadores caducos son minutos de trabajo aquí y horas de toques en la aplicación. El archivo exportado es una copia estándar que JW Library restaura como cualquier otra."),
  ],
  "faq": [
   ("¿Editar afecta a mi copia original?", "No: los cambios se hacen sobre una copia en el navegador y se guardan en un archivo exportado nuevo. El original queda tal cual."),
   ("¿Hay un límite de tamaño de biblioteca?", "Las bibliotecas muy grandes se paginan para que la navegación siga siendo rápida; la búsqueda y los filtros funcionan sobre todo el contenido."),
  ],
 },

 "search-jw-library-notes": {
  "title": "Buscar notas de JW Library por significado: Pregunta a tu biblioteca",
  "h1": "Pregunta a tu biblioteca: busca tus notas de JW Library por significado",
  "description": "Búsqueda semántica para tus notas de JW Library: encuentra esa nota que recuerdas a medias describiéndola, aunque no recuerdes sus palabras exactas. En tu dispositivo, sin conexión y en privado.",
  "intro": [
   "Cualquiera con años de notas conoce el problema: recuerdas haber escrito sobre soportar las pruebas con gozo, pero la nota no contiene la palabra «aguante», así que la búsqueda por palabras no encuentra nada. «Pregunta a tu biblioteca» busca por significado: describe la idea y aparecen las notas más cercanas, con las palabras que sean.",
   "Funciona por completo en tu dispositivo: el modelo de lenguaje se descarga una vez en el navegador y luego funciona sin conexión, con aceleración WebGPU donde esté disponible. Tus notas no se envían a ninguna parte.",
  ],
  "steps": [
   ("Carga una copia en el Explorador de Estudio", "En jwsync.org, carga tu archivo .jwlibrary y abre la pestaña Preguntar."),
   ("Deja que el modelo se prepare una vez", "La primera vez, el modelo se descarga en el dispositivo e indexa tus notas. Solo ocurre una vez; después funciona al instante, incluso sin conexión."),
   ("Pregunta con tus propias palabras", "Escribe lo que recuerdes —«aquella nota sobre ser paciente con los nuevos en la predicación», «ánimo para precursores desanimados»— y aparecerán las notas más cercanas, ordenadas por significado."),
  ],
  "sections": [
   ("En qué se diferencia de la búsqueda normal",
    "La búsqueda por palabras compara letras; la semántica compara ideas. Una consulta sobre «ansiedad» encuentra también notas escritas con «preocupación», «inquietudes de la vida» o una cita bíblica sobre el tema. Los dos tipos de búsqueda están en el Explorador de Estudio y se complementan."),
   ("Privado por diseño",
    "Esto no es un servicio de inteligencia artificial en la nube. El modelo se ejecuta dentro de la pestaña de tu navegador, el índice vive en tu dispositivo y al cerrar la pestaña se acabó. Nada sobre tus notas sale nunca de tu equipo."),
  ],
  "faq": [
   ("¿Hace falta un dispositivo potente?", "Un teléfono u ordenador portátil moderno lo lleva bien; en dispositivos con WebGPU va más rápido. Hay varios tamaños de modelo para ajustarlo a tu hardware."),
   ("¿Funciona en mi idioma?", "Sí: la búsqueda funciona en los idiomas en que estén escritas tus notas, y la interfaz está traducida a todos los idiomas que admite JW Sync."),
  ],
 },

 "jw-library-study-stats": {
  "title": "Tus estadísticas de estudio de JW Library: rachas, mapas y logros",
  "h1": "Tus estadísticas de estudio de JW Library: rachas, mapas, cobertura y logros",
  "description": "Convierte una copia de JW Library en estadísticas privadas de estudio: totales, mapa de actividad, rachas, cobertura de los 66 libros, un perfil de estudio y unos 200 logros.",
  "intro": [
   "Tu archivo de copia guarda en silencio años de historial de estudio: cuándo tomas notas, qué subrayas, qué libros has cubierto. La página de Estadísticas de estudio lee una copia .jwlibrary y convierte ese historial en un panel privado, calculado por completo en tu navegador.",
  ],
  "steps": [
   ("Crea una copia de seguridad", "En JW Library: Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad."),
   ("Abre la página de Estadísticas", "Entra en jwsync.org/highlights.html y carga el archivo."),
   ("Explora la historia de tu estudio", "Totales principales, vistas por año de servicio y de todos los tiempos, crecimiento año a año, y luego lo más entretenido más abajo."),
  ],
  "sections": [
   ("Lo que verás",
    "Un mapa de actividad con tu racha más larga y la actual; tu ritmo semanal y las horas y meses de más actividad; la cobertura de los 66 libros de la Biblia con separación entre Escrituras Hebreas y Griegas; una rueda de colores de subrayado, un histograma de profundidad de notas y una nube de palabras; un reloj de estudio de 24 horas y un radar de estacionalidad."),
   ("Perfil, trayectoria y logros",
    "Un perfil de estudio de seis rasgos (constancia, diligencia, profundidad, amplitud, reflexión y firmeza) con una «firma de estudio»; una trayectoria de 60 niveles repartidos en 12 etapas con nombre; y unos 200 logros, de comunes a legendarios, incluidas medallas que tienen en cuenta el contenido. Una tarjeta compartible resume tu año sin mostrar ni una sola nota."),
   ("Un motivo diario para volver",
    "El panel Rescatar muestra notas que escribiste en este mismo día en años anteriores y arma un repaso espaciado y suave: poco y a menudo es como el estudio se queda."),
  ],
  "faq": [
   ("¿Se sube algo de esto?", "No. La copia se analiza en tu navegador; las estadísticas no salen nunca de tu dispositivo."),
   ("¿Las estadísticas se actualizan solas?", "Reflejan la copia que cargas: crea una copia nueva para ver estadísticas nuevas."),
  ],
 },

 "share-jw-library-notes": {
  "title": "Cómo compartir notas de JW Library con un amigo",
  "h1": "Cómo compartir notas de JW Library con un amigo, sin ningún servidor",
  "description": "Envía notas concretas de JW Library (con sus subrayados) a un amigo en un archivo pequeño: sin servidor y sin cuenta. Quien las recibe las incorpora sin sobrescribir las suyas.",
  "intro": [
   "JW Library no ofrece ninguna forma de dar a otra persona una copia de notas concretas. Enviar toda tu copia de seguridad funcionaría, pero entrega absolutamente todo, y restaurarla borraría la biblioteca de quien la recibe. La función de compartir notas de JW Sync resuelve las dos cosas: eliges exactamente qué notas compartir y quien las recibe las añade sin perder nada.",
  ],
  "steps": [
   ("Elige las notas que vas a compartir", "En la página Compartir de jwsync.org/share.html, carga tu copia y selecciona las notas: unas pocas de un discurso, o todas las de una etiqueta con un clic usando el filtro de etiquetas del selector. Los subrayados asociados a esas notas viajan con ellas."),
   ("Envía el archivo compartido", "JW Sync genera un archivo pequeño que contiene solo las notas seleccionadas. Envíalo por donde quieras: mensajería, correo, AirDrop. No hay servidor ni cuenta; el archivo es todo el intercambio."),
   ("Quien lo recibe lo incorpora", "Tu amigo abre la misma página, carga el archivo compartido junto con su propia copia y obtiene una copia nueva con tus notas añadidas. Sus notas nunca se sobrescriben —si una nota compartida choca con una suya, él elige cómo se añade— y las notas importadas llegan etiquetadas, así que es fácil encontrarlas, revisarlas o quitarlas después."),
  ],
  "sections": [
   ("Buenos usos",
    "Pasar una investigación a un compañero de estudio, compartir las notas de una reunión con alguien que faltó, dar a un publicador nuevo un conjunto inicial de notas sobre una publicación, o trasladar las notas de un proyecto concreto a un familiar, todo sin exponer el resto de ninguna de las dos bibliotecas."),
  ],
  "faq": [
   ("¿Quien lo recibe necesita instalar JW Sync?", "No se instala nada por ninguna de las dos partes: es una página web. Quien lo recibe solo necesita el archivo compartido y su propia copia de seguridad."),
   ("¿Puedo dejar de compartir o caducar un archivo enviado?", "El archivo es un archivo corriente que enviaste: no hay ninguna copia en un servidor que caduque. Comparte solo lo que compartirías en cualquier mensaje."),
  ],
 },

 "bible-reading-plan": {
  "title": "Un plan diario de lectura de la Biblia con tus propias notas al lado",
  "h1": "Compañero de Lectura: un plan de lectura de la Biblia con tus notas al lado",
  "description": "Un plan diario y privado de lectura de la Biblia que muestra las notas y los subrayados que hiciste en los capítulos de hoy. Elige tu ritmo, mantén la racha y ve llenándose la cuadrícula de 66 libros.",
  "intro": [
   "Hay muchas aplicaciones con planes de lectura de la Biblia. El Compañero de Lectura hace algo que ninguna puede: como lee tu propia copia .jwlibrary, la lectura de hoy llega acompañada de las notas y los subrayados que tú mismo hiciste en esos mismos capítulos —«subrayaste cuatro versículos en Salmo 37 hace dos años»—. Leer a través de tu propio historial de estudio, y todo en tu dispositivo.",
  ],
  "steps": [
   ("Elige un orden y un ritmo", "Lee en el orden de la Biblia o en orden cronológico aproximado; termina en 3 meses, 6 meses, 1 año o 2 años, o fija tus propios capítulos al día, con una previsión en vivo de «terminarías hacia…»."),
   ("Lee la porción de hoy", "Cada capítulo está a un toque y se abre directamente en JW Library o en la BIBLIOTECA EN LÍNEA Watchtower en tu idioma. Ve marcando los capítulos según avanzas."),
   ("Lleva tus notas contigo (opcional)", "Carga una copia en cualquier herramienta de JW Sync y tus propias notas y el número de subrayados aparecerán justo debajo de los capítulos de hoy."),
   ("Mira crecer el progreso", "Una cuadrícula de 66 libros se va llenando según lees, con una barra de capítulos leídos, una previsión según tu ritmo y logros por terminar cada libro, las Escrituras Hebreo-Arameas, las Escrituras Griegas y la Biblia entera."),
  ],
  "sections": [
   ("Rachas sin culpa",
    "Completar un día alarga tu racha; saltarte un día simplemente mueve la fecha prevista de fin. No hay ninguna pila de atrasos: el plan se adapta a tu vida en lugar de regañarte."),
  ],
  "faq": [
   ("¿Necesito cargar una copia para usarlo?", "No: el plan, las rachas y el progreso funcionan por sí solos. La copia solo añade tus notas personales a la lectura de cada día."),
   ("¿Mi progreso de lectura es privado?", "Sí. El progreso vive en tu navegador, en tu dispositivo: no hay cuenta y no se sube nada."),
  ],
 },

 "open-jwlibrary-file": {
  "title": "¿Qué es un archivo .jwlibrary y cómo se abre?",
  "h1": "Qué es un archivo .jwlibrary y cómo abrirlo en cualquier dispositivo",
  "description": "Un archivo .jwlibrary es tu copia de seguridad de JW Library: un solo archivo con todas las notas, subrayados, marcadores y etiquetas. Esto es lo que contiene y cómo abrirlo y leerlo.",
  "intro": [
   "Cuando haces una copia de seguridad de JW Library obtienes un archivo terminado en .jwlibrary. Es un paquete único y portátil que contiene todo tu estudio personal —notas, subrayados, marcadores, etiquetas y listas de reproducción— en una base de datos compacta. No es un documento que se abra en Word ni en un lector de PDF: está pensado para restaurarse de nuevo en JW Library.",
   "Pero no hace falta restaurarlo solo para ver qué hay dentro. JW Sync abre un archivo .jwlibrary directamente en tu navegador para que puedas leer, buscar y editar su contenido sin tocar el teléfono.",
  ],
  "steps": [
   ("Consigue un archivo .jwlibrary", "Se crea en JW Library: Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Ese es el archivo del que hablamos."),
   ("Ábrelo en JW Sync", "Entra en jwsync.org y carga el archivo en el Explorador de Estudio. Se abre al instante, en tu dispositivo, y no se sube nada."),
   ("Léelo y trabaja con él", "Explora notas, subrayados y marcadores; busca en todo; edita, reetiqueta o exporta. Cuando termines puedes restaurar el archivo (o una copia editada) de nuevo en JW Library."),
  ],
  "sections": [
   ("Qué hay realmente dentro del archivo",
    "Técnicamente, un archivo .jwlibrary es una base de datos SQLite comprimida más un manifiesto. Por eso a veces se renombra a .zip por accidente durante un envío, y por eso devolverle la extensión .jwlibrary lo arregla. No necesitas saber nada de esto para usarlo, pero explica por qué el archivo es pequeño, autónomo e idéntico en Android, iPhone, iPad y Windows."),
   ("Abrirlo en un ordenador",
    "La misma página de jwsync.org funciona en el navegador de un portátil o un ordenador de sobremesa, algo muy práctico para leer años de notas en una pantalla grande o hacer una limpieza masiva que sería tediosa en el teléfono. No hay nada que instalar."),
  ],
  "faq": [
   ("¿Puedo abrir un archivo .jwlibrary en Excel o el Bloc de notas?", "No de forma útil: es una base de datos, no una hoja de cálculo ni un archivo de texto. Ábrelo en JW Sync para leerlo, o exporta tus notas a Markdown o texto desde el Explorador de Estudio."),
   ("¿Es seguro abrir mi copia en el navegador?", "Sí. JW Sync lee el archivo localmente en la pestaña del navegador; no se envía nada a ningún servidor y tu archivo original nunca se modifica."),
  ],
 },

 "jw-library-windows-pc": {
  "title": "Copia de seguridad y combinación de JW Library en un PC con Windows",
  "h1": "Usar las copias de seguridad de JW Library en un PC con Windows",
  "description": "Cómo hacer una copia de JW Library en Windows y cómo combinarla con las del teléfono y la tableta para que las notas, los subrayados y los marcadores estén en todos los dispositivos.",
  "intro": [
   "JW Library funciona en Windows además de en teléfonos y tabletas, y genera el mismo archivo de copia .jwlibrary. Eso significa que tu PC puede formar parte de la misma biblioteca de estudio que tu teléfono, siempre que combines las copias en lugar de restaurar una encima de otra.",
  ],
  "steps": [
   ("Haz la copia en Windows", "En la aplicación de JW Library para Windows, abre el menú, ve a Copia de seguridad y restauración y crea una copia. Guarda el archivo .jwlibrary en un sitio fácil de encontrar."),
   ("Haz también copia del teléfono y la tableta", "En cada dispositivo: Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad."),
   ("Combínalas en jwsync.org", "Abre jwsync.org en cualquier navegador del PC y carga todos los archivos. JW Sync une las notas, los subrayados, los marcadores y las etiquetas de cada dispositivo en un único archivo .jwlibrary, localmente y sin subir nada."),
   ("Restaura el archivo combinado en todas partes", "Restaura el archivo combinado en la aplicación de Windows y en cada dispositivo móvil. Ahora el PC, el teléfono y la tableta tienen la biblioteca completa."),
  ],
  "sections": [
   ("Por qué el PC es el sitio más cómodo para hacerlo",
    "En un navegador de escritorio cargar varios archivos, revisar la vista previa y guardar el resultado es mucho más rápido que a base de toques en el teléfono. Mucha gente mantiene su rutina principal de combinación en el ordenador y se limita a restaurar el archivo resultante en sus dispositivos móviles."),
  ],
  "faq": [
   ("¿La copia de Windows funciona con las de iPhone y Android?", "Sí: el formato .jwlibrary es idéntico en todas las plataformas, así que una copia de Windows se combina sin problema con las del teléfono y la tableta."),
   ("¿Tengo que instalar algo en el PC?", "No. JW Sync es una página web; funciona en Edge, Chrome o Firefox sin instalar nada."),
  ],
 },

 "recover-jw-library-notes-lost-phone": {
  "title": "Cómo recuperar notas de JW Library tras perder o romper el teléfono",
  "h1": "Recuperar notas de JW Library de un teléfono perdido, roto o reiniciado",
  "description": "¿Perdiste el teléfono o lo reiniciaste con las notas de JW Library dentro? Lo que puedas recuperar depende de tus copias. Aquí tienes exactamente cómo recuperarlas y qué hacer la próxima vez.",
  "intro": [
   "Perder un teléfono ya es bastante estresante como para además temer haber perdido años de notas de estudio. Que puedas recuperarlas depende de una sola pregunta: ¿existe alguna copia .jwlibrary fuera de ese teléfono?",
   "Esta guía te lleva paso a paso a encontrar cualquier copia que puedas tener —incluso alguna que hayas olvidado— y a convertirla otra vez en una biblioteca de JW Library completa en tu dispositivo nuevo.",
  ],
  "steps": [
   ("Busca en todos los sitios donde pueda haber una copia", "Revisa tu correo (busca «jwlibrary» o «copia»), Google Drive, iCloud Drive, OneDrive, Dropbox y la carpeta de Descargas del ordenador. Las copias son archivos pequeños y es fácil olvidar que las guardaste."),
   ("Comprueba tus otros dispositivos", "Si alguna vez usaste JW Library en una tableta o un PC, ahí hay datos de estudio propios: haz una copia ahora mismo para conservar lo que tenga."),
   ("Restaura lo que encuentres en el teléfono nuevo", "Instala JW Library en el dispositivo nuevo y ve a Copia de seguridad y restauración → Restaurar; carga el archivo .jwlibrary. Vuelven tus notas, subrayados y marcadores."),
   ("Combina si encuentras más de una copia", "Distintos dispositivos o fechas pueden tener cada uno notas únicas. No elijas solo una: cárgalas todas en jwsync.org, combínalas en un único archivo completo y restaura ese. No se queda nada atrás."),
  ],
  "sections": [
   ("Si no existe ninguna copia en ninguna parte",
    "Sé sincero contigo mismo cuanto antes: si la única copia de tus notas estaba en el teléfono perdido y nunca exportaste una copia de seguridad, JW Library no guarda ninguna copia en la nube desde la que restaurar. Duele, y es justo por eso que el hábito de abajo importa tanto."),
   ("Que no vuelva a pasar",
    "Ponte un recordatorio mensual de copia de seguridad y guarda cada archivo .jwlibrary fuera del teléfono (con enviártelo por correo basta). JW Sync incluso puede recordártelo y combinar tus dispositivos de forma periódica. Un archivo que vive en tu bandeja de entrada sobrevive a cualquier teléfono."),
  ],
  "faq": [
   ("¿Puede JW Sync recuperar notas de un teléfono que ya no tengo?", "Ninguna herramienta puede: la recuperación depende de que exista un archivo de copia en algún sitio. El trabajo de JW Sync es leer, reparar y combinar las copias que sí tienes."),
   ("Mi copia es antigua, ¿merece la pena restaurarla?", "Desde luego. Una copia antigua con la mayoría de tus notas es mucho mejor que empezar de cero, y luego puedes combinarla con cualquier cosa más reciente que encuentres."),
  ],
 },

 "handle-merge-conflicts": {
  "title": "¿La misma nota editada en dos dispositivos? Resolver conflictos",
  "h1": "Resolver conflictos de combinación: la misma nota editada en dos dispositivos",
  "description": "Cuando editas la misma nota de JW Library de forma distinta en dos dispositivos, la combinación tiene que elegir. El revisor de conflictos muestra las dos versiones lado a lado para que decidas tú: no se pierde nada.",
  "intro": [
   "Casi toda la combinación es automática: las notas propias de cada dispositivo simplemente se unen. El único caso que exige una decisión es un conflicto real: la misma nota, editada de forma distinta en dos dispositivos, de modo que las dos copias no coinciden en lo que debería decir. JW Sync nunca adivina en silencio; te pasa a ti la elección.",
  ],
  "steps": [
   ("Carga las dos copias", "En jwsync.org, carga los archivos .jwlibrary de los dos dispositivos. JW Sync los compara mientras combina."),
   ("Abre el revisor de conflictos", "Si hay notas en conflicto, el revisor las enumera. Todo lo que no entraba en conflicto ya está combinado: este paso es solo para los choques reales."),
   ("Compara lado a lado", "Cada conflicto muestra las dos versiones con las diferencias resaltadas palabra por palabra. «Sugerir la mejor» puede elegir la versión más completa por ti, o eliges tú cuál conservar, nota por nota."),
   ("Termina y restaura", "Cuando hayas resuelto todos los conflictos, descarga el archivo combinado y restáuralo. Los dos dispositivos coinciden ya, con la versión que elegiste de cada nota."),
  ],
  "sections": [
   ("Por qué esto es mejor que quedarse con la más reciente",
    "«Gana la más reciente» borra en silencio ediciones que quizá querías conservar. Puede que la versión antigua tuviera un párrafo que borraste sin querer en el otro dispositivo. Ver las dos, palabra por palabra, significa que nunca pierdes texto sin enterarte, que es justo el sentido de combinar en vez de sobrescribir."),
   ("Por qué se producen los conflictos",
    "Normalmente por editar sin conexión en dos dispositivos entre una combinación y otra, o por restaurar una copia antigua y luego añadirle cosas. Combinar con regularidad mantiene bajo el número de conflictos y las diferencias frescas en la memoria."),
  ],
  "faq": [
   ("¿Tendré que revisar cientos de conflictos?", "Rara vez. Solo entran en conflicto las notas editadas de forma distinta en los dos lados; las notas nuevas, y las modificadas en un solo dispositivo, se combinan solas. La mayoría de las combinaciones tienen un puñado de conflictos o ninguno."),
   ("¿Puedo cambiar de opinión después de elegir?", "Sí: no se escribe nada en ningún dispositivo hasta que restauras el archivo combinado, y tus copias originales nunca se modifican, así que puedes rehacer la combinación."),
  ],
 },

 "export-jw-library-notes": {
  "title": "Cómo exportar las notas de JW Library a texto o Markdown",
  "h1": "Exportar tus notas de JW Library a texto, Markdown o una copia nueva",
  "description": "Saca tus notas de JW Library de la aplicación: cópialas o expórtalas como Markdown o texto para usarlas donde quieras, o extrae una selección a una copia .jwlibrary nueva. Todo en tu navegador.",
  "intro": [
   "Tus notas de estudio no deberían quedarse atrapadas dentro de una sola aplicación. A veces las quieres como texto sin formato —para pegarlas en el bosquejo de un discurso, en un documento o en tu propia aplicación de notas— y a veces quieres una copia limpia que contenga solo una parte. El Explorador de Estudio hace las dos cosas, leyendo tu copia por completo en el navegador.",
  ],
  "steps": [
   ("Carga tu copia de seguridad", "Crea una copia en JW Library (Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad), abre jwsync.org y cárgala en el Explorador de Estudio."),
   ("Encuentra las notas que quieres", "Usa la búsqueda junto con los filtros de color, etiqueta y publicación para acotar exactamente las notas que buscas: una publicación, una etiqueta, un tema."),
   ("Copia o exporta como Markdown o texto", "Saca las notas como Markdown o texto sin formato para pegarlas donde quieras. El formato (negrita, cursiva, listas) se conserva, así que las notas estructuradas siguen estructuradas."),
   ("O extrae a una copia nueva", "¿Prefieres un archivo? Exporta una selección o un intervalo de fechas a una copia .jwlibrary nueva: útil para archivar un proyecto o entregar un conjunto concreto de notas a otro dispositivo."),
  ],
  "sections": [
   ("Por qué exportar",
    "Las notas son más útiles cuando pueden viajar: a un documento para una parte de la reunión, a tu wiki personal, a una impresión para alguien que no usa la aplicación. Markdown conserva la estructura y a la vez se lee como texto sin formato en cualquier sitio."),
  ],
  "faq": [
   ("¿Exportar cambia mis notas de JW Library?", "No. La exportación lee una copia de tu archivo en el navegador; tu archivo original y la aplicación quedan intactos."),
   ("¿Puedo exportarlo todo de una vez?", "Sí: quita los filtros para seleccionar toda la biblioteca, o acota primero para exportar solo una parte."),
  ],
 },

 "organize-jw-library-tags": {
  "title": "Cómo organizar y limpiar las etiquetas de JW Library",
  "h1": "Organizar tus etiquetas de JW Library: renombrar, fusionar y limpiar en bloque",
  "description": "Las etiquetas se multiplican con los años. Renombra una etiqueta en todas las notas, fusiona duplicadas y elimina las que ya no usas, en bloque, en tu navegador y con deshacer completo.",
  "intro": [
   "Las etiquetas son la forma de encontrar notas después, pero al cabo de unos años se desmadran. Acabas con «Ministerio», «ministerio» y «Servicio del campo» significando lo mismo, con etiquetas que creaste una vez y no volviste a usar, y con nombres incoherentes que hacen que filtrar no sea fiable. JW Library no ofrece ninguna forma de arreglar esto a gran escala. El Explorador de Estudio sí.",
  ],
  "steps": [
   ("Carga tu copia en el Explorador de Estudio", "En jwsync.org, carga tu archivo .jwlibrary. Filtra por etiqueta para ver todas las etiquetas y cuántas notas tiene cada una."),
   ("Renombra una etiqueta en todas sus notas", "Reetiqueta en bloque: renombra una etiqueta una vez y se actualizan todas las notas que la usan, sin editar nota por nota para corregir una falta."),
   ("Fusiona las duplicadas", "Pasa las notas de una etiqueta duplicada a la buena y luego elimina la duplicada vacía. «Ministerio» y «ministerio» se convierten en una sola etiqueta limpia."),
   ("Elimina las etiquetas que ya no usas", "Selecciona y borra en bloque las etiquetas caducas. Todo se puede deshacer, así que una limpieza demasiado entusiasta nunca es definitiva."),
   ("Exporta la biblioteca ordenada", "Descarga el .jwlibrary editado y restáuralo en JW Library. Tus etiquetas quedan coherentes en todas partes."),
  ],
  "sections": [
   ("Un sistema de etiquetas que de verdad ayuda",
    "Cuando las etiquetas son coherentes, filtrar se vuelve fiable: un toque muestra todas las notas sobre un tema, en todas las publicaciones. Es la diferencia entre etiquetas como desorden y etiquetas como un índice real de tu estudio."),
   ("Las etiquetas coherentes convierten compartir en dos clics",
    "El selector de notas de la página Compartir tiene su propio filtro de etiquetas, así que una etiqueta limpia es además la forma más rápida de enviar a alguien un conjunto de notas: eliges la etiqueta, pulsas Seleccionar todo y creas el archivo. Las etiquetas descuidadas te cuestan dos veces: al buscar notas y al intentar compartirlas."),
  ],
  "faq": [
   ("¿Reetiquetar en bloque toca el texto de la nota?", "No: solo cambia qué etiquetas están asociadas. Los títulos y el contenido de tus notas quedan exactamente como los escribiste."),
   ("¿Hay forma de deshacer si me equivoco?", "Sí. El Explorador de Estudio tiene deshacer y rehacer completos, y tu copia original nunca se modifica: los cambios van a una copia exportada."),
  ],
 },

 "manage-jw-library-highlights": {
  "title": "Cómo gestionar y recolorear los subrayados de JW Library",
  "h1": "Gestionar tus subrayados de JW Library: recolorear y organizar en bloque",
  "description": "Pon orden en años de subrayados de JW Library: cambia colores en bloque, da a tu código de colores un significado coherente y consulta todos los subrayados en un solo sitio. En tu navegador.",
  "intro": [
   "Los colores de subrayado solo ayudan si significan algo coherente. Con el tiempo, los subrayados de casi todo el mundo se desvían: el amarillo significaba una cosa en 2019 y otra ahora, y JW Library no ofrece forma de verlos todos juntos ni de arreglarlos a gran escala. El Explorador de Estudio reúne todos los subrayados en una sola vista y te deja recolorear en bloque.",
  ],
  "steps": [
   ("Carga tu copia de seguridad", "En jwsync.org, abre tu archivo .jwlibrary en el Explorador de Estudio y ve a la pestaña Subrayados."),
   ("Explora y filtra tus subrayados", "Ve todos los subrayados en una lista, filtra por color o publicación y busca en el texto subrayado y en las notas asociadas."),
   ("Recolorea en bloque", "Selecciona muchos subrayados y cambia su color a la vez; por ejemplo, unifica en un solo color todo lo que marcaste como «texto clave» en toda la biblioteca."),
   ("Edita también las notas asociadas", "Donde un subrayado tenga una nota adjunta, edita aquí mismo el título y el contenido de esa nota."),
   ("Exporta y restaura", "Descarga el .jwlibrary editado y restáuralo en JW Library para tener tu código de colores coherente en todos los dispositivos."),
  ],
  "sections": [
   ("Decide qué significan tus colores",
    "Un esquema sencillo —un color para las ideas principales, otro para los textos que quieres memorizar y otro para las preguntas que quieres investigar— convierte los subrayados en una herramienta de estudio en vez de en decoración. Recolorear en bloque te permite aplicar ese esquema con efecto retroactivo a años de lectura."),
  ],
  "faq": [
   ("¿Puedo ver los subrayados que no tienen nota?", "Sí: la pestaña Subrayados los muestra todos, con o sin nota asociada."),
   ("¿Recolorear afecta al texto de la publicación?", "No, solo cambia el color del subrayado; el texto de la publicación y tus notas quedan intactos."),
  ],
 },

 "jw-library-study-answers": {
  "title": "Ver y editar tus respuestas de estudio de JW Library",
  "h1": "Encontrar en un solo sitio tus respuestas de estudio de JW Library",
  "description": "Las respuestas que escribes en los artículos de estudio y en la guía de actividades están escondidas en tu copia. La pestaña Respuestas de estudio del Explorador te permite leerlas, buscarlas y editarlas todas a la vez.",
  "intro": [
   "Mientras estudias, escribes respuestas en los recuadros de los artículos de estudio, La Atalaya y la guía de actividades. Se guardan en tu copia de seguridad, pero JW Library solo te muestra cada una enterrada en su publicación. No hay ningún sitio único donde repasar todo lo que has escrito. La pestaña Respuestas de estudio del Explorador es ese sitio.",
  ],
  "steps": [
   ("Carga tu copia en el Explorador de Estudio", "En jwsync.org, carga tu archivo .jwlibrary y abre la pestaña Respuestas de estudio."),
   ("Lee todas tus respuestas juntas", "Cada respuesta que has escrito aparece en una sola lista con búsqueda, así que puedes repasar de un vistazo todo lo que pensaste sobre un artículo de estudio entero."),
   ("Busca y edita", "Encuentra una respuesta por su texto y edítala y púlela ahí mismo: útil al repasar antes de una reunión o al ordenar una redacción hecha con prisa."),
   ("Exporta o restaura", "Restaura el archivo editado para llevar tus cambios de vuelta a JW Library, o copia las respuestas como texto para un discurso o un registro personal."),
  ],
  "sections": [
   ("Por qué es útil antes de las reuniones",
    "Repasar tus respuestas preparadas en una lista continua —en vez de ir párrafo por párrafo en la aplicación— es una forma más rápida de refrescar lo que pensabas decir y de detectar las respuestas que dejaste en blanco."),
  ],
  "faq": [
   ("¿Son lo mismo que mis notas personales?", "No: las respuestas son lo que escribiste en los recuadros de una publicación. El Explorador de Estudio las muestra en su propia pestaña, aparte de las notas libres."),
   ("¿Se sube algo para leer mis respuestas?", "No. Como todo en JW Sync, tu copia se lee localmente en el navegador y no se envía nunca a ninguna parte."),
  ],
 },

 "extract-jw-library-notes-by-date": {
  "title": "Extraer notas de JW Library de un intervalo de fechas a una copia nueva",
  "h1": "Extraer un intervalo de fechas de notas de JW Library a una copia nueva",
  "description": "Saca solo las notas de un periodo concreto —un año de servicio, una asamblea, un proyecto de estudio— a su propia copia .jwlibrary limpia. Todo en tu navegador.",
  "intro": [
   "A veces quieres una parte de tu biblioteca, no toda: las notas de este año para un repaso, todo lo de una asamblea o la investigación de un proyecto para pasársela a alguien. El Explorador de Estudio puede extraer las notas de un intervalo de fechas a una copia .jwlibrary totalmente nueva, sin tocar tu biblioteca principal.",
  ],
  "steps": [
   ("Carga tu copia de seguridad", "En jwsync.org, abre tu archivo .jwlibrary en el Explorador de Estudio."),
   ("Fija el intervalo de fechas", "Elige la fecha de inicio y la de fin de las notas que quieres: un año de servicio, un mes, las fechas de un acontecimiento concreto."),
   ("Extrae a una copia nueva", "Exporta las notas coincidentes a un archivo .jwlibrary nuevo. Contiene solo las notas de ese periodo, sus subrayados y sus etiquetas."),
   ("Usa el archivo extraído", "Restáuralo en JW Library para un repaso centrado, archívalo o compártelo con alguien que solo necesita esa parte."),
  ],
  "sections": [
   ("Buenas razones para extraer por fecha",
    "Un archivo anual de tu estudio; un archivo limpio de notas de asamblea para guardarlo aparte; entregar a un compañero de estudio solo las notas de un proyecto que hicisteis juntos; o dividir una biblioteca enorme en trozos manejables y fechados, todo sin alterar tu copia principal."),
  ],
  "faq": [
   ("¿Extraer quita esas notas de mi biblioteca?", "No. Copia las notas coincidentes a un archivo nuevo; tu copia original lo conserva todo."),
   ("¿Qué fecha usa: cuándo escribí la nota o cuándo la edité?", "Usa las marcas de tiempo de la propia nota dentro de la copia, así que el intervalo refleja cuándo se crearon o modificaron las notas."),
  ],
 },

 "connect-jw-library-notes-study-map": {
  "title": "Cómo se conectan tus notas de JW Library: el Mapa de Estudio",
  "h1": "Mapa de Estudio: un grafo privado del conocimiento de tus notas de JW Library",
  "description": "El Mapa de Estudio convierte tus notas de JW Library en una red interactiva, uniéndolas por textos bíblicos comunes, etiquetas compartidas y redacción parecida, para que veas los temas que recorren tu estudio.",
  "intro": [
   "Años de notas guardan conexiones que nunca has visto: el mismo texto bíblico citado en una docena de entradas, un tema al que vuelves una y otra vez, ideas que se hacen eco en publicaciones distintas. El Mapa de Estudio dibuja esos vínculos como un grafo interactivo, de modo que la forma de tu propio estudio se hace visible.",
  ],
  "steps": [
   ("Abre la página de Estadísticas y carga una copia", "Entra en jwsync.org/highlights.html y carga tu archivo .jwlibrary. El Mapa de Estudio lo lee en tu navegador."),
   ("Abre el Mapa de Estudio", "Lanza el mapa para ver tus notas como puntos conectados por textos bíblicos comunes, etiquetas compartidas y redacción parecida."),
   ("Explora las conexiones", "Cambia entre las vistas de Temas y de Notas, pasa el cursor para resaltar los vínculos de una nota, arrastra los elementos y usa el control de intensidad para mostrar solo las conexiones más fuertes. El modo de pantalla completa te da sitio para moverte."),
   ("Crea y guarda cadenas de estudio", "Traza tus propias «cadenas de estudio» entre notas relacionadas para capturar un razonamiento, y exporta el mapa como imagen PNG para guardarlo o compartirlo."),
  ],
  "sections": [
   ("Lo que revela el mapa",
    "Los grupos muestran los temas que más estudias; un texto bíblico unido a muchas notas señala un versículo al que vuelves constantemente; una nota aislada puede ser un hilo que merece la pena desarrollar. Es una forma de estudiar tu estudio, y de preparar discursos siguiendo las conexiones que ya habías hecho."),
  ],
  "faq": [
   ("¿Necesito muchas notas para que el mapa sea útil?", "Una biblioteca modesta ya muestra conexiones; cuanto más ricas sean tus notas, más revela el mapa. Con bibliotecas muy pequeñas verás un aviso para añadir más notas primero."),
   ("¿El mapa es privado?", "Del todo. Se construye en tu navegador a partir de tu copia y nunca se sube; incluso la exportación en PNG se genera en tu dispositivo."),
  ],
 },

 "review-old-jw-library-notes": {
  "title": "Cómo repasar tus notas antiguas de JW Library (para que se queden)",
  "h1": "Repasar notas antiguas de JW Library con Rescatar: poco y a menudo",
  "description": "Las notas que nunca vuelves a mirar son notas que olvidas. Rescatar te muestra lo que escribiste este mismo día en años anteriores y arma un repaso espaciado suave, para que tu estudio pasado siga trabajando para ti.",
  "intro": [
   "La mayoría de las notas de estudio se escriben una vez y no se vuelven a ver. Es un desperdicio silencioso: la idea mereció la pena anotarla y luego se hundió en el fondo de la biblioteca. Rescatar devuelve tus propias notas antiguas a la superficie, unas pocas cada vez, para que volver a ellas sea un pequeño hábito diario en lugar de un proyecto para algún día.",
  ],
  "steps": [
   ("Abre la página de Estadísticas y carga una copia", "Entra en jwsync.org/highlights.html y carga tu archivo .jwlibrary. Rescatar lee tus notas localmente."),
   ("Mira «En este día»", "Rescatar saca a la luz notas que escribiste en esta misma fecha en años anteriores —«escrita hace dos años, un día como hoy»—, reconectándote con tu estudio pasado en el momento en que más significa."),
   ("Haz un repaso diario corto", "Te presenta un puñado de notas para revisarlas y marcarlas como repasadas. Poco y a menudo es como el estudio se queda, y la racha crece mientras mantengas el hábito."),
   ("Vuelve mañana", "El repaso espaciado programa las notas para que reaparezcan con el tiempo, de modo que las que merece la pena recordar siguen volviendo hasta que son tuyas."),
  ],
  "sections": [
   ("Por qué funciona el repaso espaciado",
    "Repasar algo justo cuando estás a punto de olvidarlo es mucho más eficaz que empollar. Al repartir unas pocas notas a lo largo de muchos días, Rescatar convierte tu biblioteca actual en un repaso continuo y de poco esfuerzo que profundiza poco a poco lo que has estudiado."),
  ],
  "faq": [
   ("¿Dónde se guarda mi progreso de repaso?", "En tu navegador, en tu dispositivo: no hay cuenta y no se sube nada. La racha y el calendario son solo tuyos."),
   ("¿Necesito notas nuevas para esto?", "No: Rescatar trabaja con las notas que ya has escrito. Cuanto más antigua sea tu biblioteca, más gratificantes son los momentos de «en este día»."),
  ],
 },

 "jw-library-achievements-streaks": {
  "title": "Rachas, niveles y logros de estudio en JW Library",
  "h1": "Convierte tu estudio de JW Library en rachas, niveles y logros",
  "description": "Consulta tus rachas de estudio, sube 60 niveles repartidos en 12 etapas de tu Trayectoria de Estudio y desbloquea unos 200 logros, todo leído en privado desde tu propia copia de JW Library.",
  "intro": [
   "La constancia es la parte difícil del estudio personal, y el progreso que no se ve es fácil de dejar caer. La página de Estadísticas convierte el historial de tu copia en algo que puedes ver crecer: rachas, niveles y logros que reflejan el estudio que de verdad has hecho. No son metas impuestas, es tu propio registro hecho visible.",
  ],
  "steps": [
   ("Abre la página de Estadísticas", "Entra en jwsync.org/highlights.html y carga tu copia .jwlibrary. Todo se calcula en tu navegador."),
   ("Mira tus rachas", "Consulta tu racha de estudio más larga y la actual, tu ritmo semanal y tus horas y meses de más actividad: el pulso de tu hábito de estudio."),
   ("Sube por tu Trayectoria de Estudio", "Avanza por 60 niveles repartidos en 12 etapas con nombre (de Semilla hasta Siempre Verde), con una esfera que cambia de color y celebraciones al subir, según todo tu estudio acumulado."),
   ("Reúne logros", "Desbloquea unos 200 logros que van de comunes a legendarios, incluidas medallas temáticas que tienen en cuenta el contenido; abre cualquier medalla para ver tu progreso hacia la siguiente."),
  ],
  "sections": [
   ("Motivación sin presión",
    "No son objetivos que haya puesto otro: son un espejo de lo que ya has hecho. Ver una racha que no quieres romper, o un nivel casi alcanzado, es un empujoncito suave para mantener el buen hábito. Y una tarjeta compartible resume tu año sin mostrar ni una sola nota privada."),
  ],
  "faq": [
   ("¿Las rachas y los logros se actualizan solos?", "Reflejan la copia que cargas, así que crea una copia nueva para ver tu progreso más reciente. No hay nada funcionando en segundo plano."),
   ("¿Se comparte o se sube algo de esto?", "No. Todo se calcula localmente a partir de tu copia; lo único que puedes elegir compartir es la tarjeta resumen, y no contiene el texto de ninguna nota."),
  ],
 },

 "share-convention-assembly-notes": {
  "title": "Cómo compartir las notas de asambleas y congresos desde JW Library",
  "h1": "Compartir tus notas de congresos, asambleas y reuniones",
  "description": "Pasa tus notas de un congreso, una asamblea o una reunión a familiares y amigos en un archivo pequeño, sin entregar toda tu biblioteca ni sobrescribir la suya. Un uso práctico de compartir notas.",
  "intro": [
   "Tomaste notas cuidadosas durante un congreso; a un amigo que se perdió una sesión le encantarían; tu familia quiere los puntos para su propio repaso. Enviar toda tu copia de seguridad es excesivo y, al restaurarla, borraría las notas de quien la recibe. Compartir notas te permite pasar exactamente las que quieras, y deja que quien las recibe conserve todo lo que ya tiene.",
  ],
  "steps": [
   ("Carga tu copia en la página Compartir", "Entra en jwsync.org/share.html y carga tu archivo .jwlibrary."),
   ("Selecciona solo las notas del congreso", "Elige la etiqueta del evento en el filtro del selector de notas y pulsa Seleccionar todo: la lista ya es exactamente lo que etiquetaste. Los subrayados asociados a esas notas van incluidos."),
   ("Envía el archivo compartido", "JW Sync crea un archivo pequeño que contiene solo esas notas. Envíalo como prefieras: mensajería, correo, AirDrop. Sin servidor y sin cuenta."),
   ("Familia y amigos lo incorporan", "Cada persona abre la misma página, carga tu archivo junto con su propia copia y obtiene una copia nueva con tus notas añadidas. Sus notas nunca se sobrescriben, y las tuyas llegan etiquetadas para que sean fáciles de encontrar."),
  ],
  "sections": [
   ("Una etiqueta lo hace todo más fácil",
    "Si etiquetas tus notas durante el evento (por ejemplo, «Congreso 2026»), seleccionarlas después es un clic en el filtro y un Seleccionar todo. Merece la pena empezar una etiqueta nueva al principio de cualquier congreso, asamblea o reunión especial justo por esto."),
  ],
  "faq": [
   ("¿Puedo compartirlas con varias personas a la vez?", "Sí: el archivo compartido es solo un archivo. Envíalo a quien quieras; cada persona lo incorpora a su biblioteca de forma independiente."),
   ("¿Se expondrá toda mi biblioteca?", "No. En el archivo solo están las notas que selecciones; el resto de tu biblioteca sigue siendo privado."),
  ],
 },

 "share-jw-library-notes-by-tag": {
  "title": "Compartir solo las notas de JW Library de una etiqueta",
  "h1": "Compartir solo las notas que llevan una etiqueta",
  "description": "Envía un tema, un proyecto o lo que corresponde a un estudiante en lugar de toda tu biblioteca, y tus etiquetas viajan con las notas, así que llegan organizadas al otro lado.",
  "intro": [
   "Una etiqueta suele ser la unidad natural para compartir. Etiquetaste todo lo que reuniste sobre un tema, todo lo de un evento concreto o todo lo que repasas con una persona, y ese conjunto —no tu biblioteca entera— es lo que la otra persona quiere de verdad.",
   "La función de compartir notas de JW Sync trabaja nota a nota, así que una etiqueta es sencillamente la lista que marcas. Las notas conservan sus etiquetas al salir, lo que significa que quien las recibe podrá filtrar exactamente el mismo conjunto dentro de su propia biblioteca.",
  ],
  "steps": [
   ("Asegúrate de que las notas llevan la etiqueta", "Etiquétalas en JW Library sobre la marcha, o abre tu copia en el Explorador de Estudio en jwsync.org y usa el editor de etiquetas para añadir una etiqueta a varias notas a la vez. Etiquetar con coherencia ahora es lo que convierte compartir en un trabajo de un minuto después."),
   ("Abre la página Compartir y carga tu copia", "Entra en jwsync.org/share.html, elige Enviar notas y carga tu archivo .jwlibrary. Se lee en tu navegador y no sale nunca de tu dispositivo."),
   ("Elige la etiqueta en el filtro y pulsa Seleccionar todo", "El selector de notas tiene un filtro que enumera todas las etiquetas de tu copia con el número de notas de cada una. Elige la tuya y la lista se reduce exactamente a esas notas; Seleccionar todo las marca todas. Esa es toda la selección: dos clics."),
   ("Crea el archivo y envíalo", "JW Sync genera un archivo compartido pequeño que contiene solo las notas que marcaste. Envíalo por mensajería, correo o AirDrop: no hay ningún servidor de por medio ni cuenta por ninguna de las dos partes."),
   ("Lo añaden a su propia copia", "La otra persona abre la misma página, elige Recibir, previsualiza las notas y las añade a su copia. Tus etiquetas llegan con las notas, más una etiqueta que identifica la importación, así que todo el conjunto está también a un filtro de distancia para ella."),
  ],
  "sections": [
   ("Por qué compartir una etiqueta y no una copia entera",
    "Entregar una copia .jwlibrary completa regala todo lo que has escrito en tu vida, y restaurarla borraría las notas de la otra persona. Compartir una selección etiquetada es lo contrario en ambos sentidos: solo ve lo que elegiste y no pierde nada de lo suyo."),
   ("Afinar más, o compartir entre varias etiquetas",
    "El filtro de etiquetas y el buscador funcionan juntos: elige una etiqueta y escribe luego una palabra para reducirla más; Seleccionar todo sigue marcando solo lo que tienes delante. La búsqueda también encuentra nombres de etiquetas, así que una palabra común a varias las reúne de una vez. Cada nota de la lista muestra las etiquetas que lleva, así que ves lo que envías antes de enviarlo."),
   ("Etiquetas que conviene mantener para compartir",
    "Merece la pena tener unas cuantas etiquetas que existan solo para compartirse: el nombre de un evento, un tema que investigas para otros, la persona con la que estudias. Cuando llegue el momento de enviar algo, no hay que buscar: el conjunto ya está montado."),
  ],
  "faq": [
   ("¿Mis etiquetas llegan a la otra persona?", "Sí. Las notas compartidas llevan sus etiquetas, y la importación se marca con una etiqueta propia, así que quien las recibe puede encontrar, revisar o quitar todo el lote después."),
   ("¿Y si una nota tiene varias etiquetas?", "Aparece bajo cada una de ellas en el filtro, y todas sus etiquetas viajan con ella. Filtrar por una etiqueta nunca elimina las demás."),
   ("¿Compartir quita las notas de mi biblioteca?", "No. Compartir copia las notas a un archivo pequeño; tu copia de seguridad y tu aplicación quedan intactas."),
   ("¿Puedo enviar la misma etiqueta a varias personas?", "Sí: el archivo compartido es un archivo corriente. Envíalo a quien quieras y cada persona lo añade a su biblioteca de forma independiente."),
  ],
 },

 "share-notes-with-bible-student": {
  "title": "Compartir notas de JW Library con un estudiante de la Biblia",
  "h1": "Compartir notas de estudio con alguien con quien estudias la Biblia",
  "description": "Envía las notas de una lección —textos, ilustraciones, los puntos que preparaste— directamente a la biblioteca de JW Library de la otra persona, sin tocar nada de lo que haya escrito ella.",
  "intro": [
   "Cuando preparas un estudio, la mayor parte del trabajo acaba en tus propias notas: los textos adicionales, la ilustración que hizo entender un punto, la respuesta a la pregunta que hizo la semana pasada. Leérselo en voz alta es una cosa; dejarle una copia que pueda releer toda la semana es otra.",
   "Compartir notas coloca las que preparaste dentro de su biblioteca como notas reales de JW Library, asociadas a los mismos párrafos y versículos, no como una captura de pantalla o un mensaje que pasará de largo.",
  ],
  "steps": [
   ("Prepara las notas de la lección en JW Library", "Escribe las notas como haces normalmente, en los párrafos y textos que cubre la lección. Ponles una etiqueta —el nombre de la persona o la publicación— para que luego sea fácil seleccionar el conjunto."),
   ("Abre la página Compartir y carga tu copia", "Crea una copia (Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad), abre jwsync.org/share.html, elige Enviar notas y carga el archivo. No sale nunca de tu dispositivo."),
   ("Marca las notas de esta lección", "Filtra el selector por la etiqueta que usaste y pulsa Seleccionar todo, o busca y márcalas una a una. Crea el archivo compartido: todo lo demás de tu biblioteca se queda donde está."),
   ("Envíalo y guíale al recibirlo", "Primero necesita una copia propia: Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad. Luego abre jwsync.org/share.html, elige Recibir, carga tu archivo y su copia, y descarga la copia actualizada."),
   ("La restaura en JW Library", "Copia de seguridad y restauración → Restaurar, elige el archivo actualizado, y tus notas aparecen en su biblioteca junto a las suyas, etiquetadas, para que sepa cuáles vinieron de ti."),
  ],
  "sections": [
   ("Sus notas nunca se sobrescriben",
    "Esta es la diferencia importante frente a enviar una copia de seguridad. Una restauración reemplaza toda la biblioteca del dispositivo; recibir notas compartidas añade a ella. Todo lo que haya escrito por su cuenta —incluso en los mismos párrafos— queda exactamente igual."),
   ("Un ritmo semanal de dos minutos",
    "Una vez que los dos lo habéis hecho la primera vez, la rutina es corta: preparar, marcar, enviar, restaurar. A muchos les resulta más cómodo enviar las notas justo después de preparar, para que el estudiante las tenga antes del estudio y no después."),
  ],
  "faq": [
   ("¿El estudiante necesita una cuenta o instalar una aplicación?", "Ninguna cuenta en ninguna parte, y nada que instalar aparte del propio JW Library: la página para compartir es una página web corriente."),
   ("¿Y si el estudiante nunca ha hecho una copia de seguridad?", "Hace una primero, en JW Library, en Estudio personal → Copia de seguridad y restauración. Incluso una biblioteca que parece vacía sirve; la copia es aquello a lo que se añaden las notas compartidas."),
   ("¿Puedo retirar las notas después?", "El archivo es tuyo para enviarlo o no. Una vez que alguien lo tiene, es suyo, igual que cualquier mensaje: comparte lo que te sentirías cómodo compartiendo por escrito."),
  ],
 },

 "share-meeting-notes-with-family": {
  "title": "Compartir las notas de las reuniones con tu familia",
  "h1": "Compartir las notas de la reunión de esta semana con la familia",
  "description": "Alguien estaba enfermo, trabajando o de viaje: envíale las notas de la semana en un archivo pequeño que pueda añadir a su propio JW Library, sin que ninguno de los dos pierda nada.",
  "intro": [
   "En la mayoría de las casas cada uno toma sus propias notas en su propio dispositivo, y siempre hay alguien que se pierde una reunión. Leer tus notas en la cena funciona una vez; ponerlas en la biblioteca de la otra persona es lo que le permite usar el material después, en el sitio donde de verdad lo va a buscar.",
   "Como se comparte nota a nota y no copia a copia, varias personas pueden intercambiar notas con total libertad sin que se sobrescriba la biblioteca de nadie.",
  ],
  "steps": [
   ("Haz una copia del dispositivo donde tomaste las notas", "JW Library → Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad."),
   ("Selecciona las notas de la semana", "En jwsync.org/share.html elige Enviar notas, carga tu copia y marca las notas de esta semana: buscar por la publicación las reúne rápido, y si etiquetas las notas de la semana el filtro las junta con un clic."),
   ("Envíalo por el chat familiar", "Crea el archivo compartido y mándalo por donde ya habléis en casa: mensajería, correo, AirDrop. Es un archivo pequeño que contiene solo las notas que marcaste."),
   ("Cada uno lo añade a su propia copia", "Abre la misma página, elige Recibir, carga tu archivo junto con una copia propia, descarga la copia actualizada y la restaura en JW Library."),
  ],
  "sections": [
   ("La biblioteca de cada uno sigue siendo suya",
    "No se reemplazan las notas de nadie, y nadie tiene que entregar su biblioteca entera para participar. Las notas importadas llegan bajo una etiqueta, así que cada persona ve de un vistazo cuáles vinieron de otro y puede borrar el lote después si prefiere no quedárselo."),
   ("Adoración en familia: reunir en vez de dispersar",
    "La misma herramienta funciona en la otra dirección. Si todos toman notas durante la adoración en familia, una persona puede reunir los archivos compartidos de los demás en una sola copia y acabar con las notas de toda la casa sobre el mismo material."),
  ],
  "faq": [
   ("¿Pueden participar los dispositivos de los niños?", "Cualquier dispositivo capaz de ejecutar JW Library y abrir una página web puede. Los pasos son idénticos en teléfono, tableta u ordenador."),
   ("¿Tenemos que estar en la misma plataforma?", "No. Android, iPhone, iPad y la aplicación de Windows usan el mismo formato de copia, así que las notas pasan entre ellos sin ninguna conversión."),
  ],
 },

 "receive-shared-jw-library-notes": {
  "title": "Me han enviado notas de JW Library, ¿cómo las abro?",
  "h1": "Añadir a tu JW Library las notas que alguien ha compartido contigo",
  "description": "Te han enviado un archivo de notas compartidas o un bloque de texto. Aquí tienes cómo previsualizarlo y añadirlo a tu propia copia de JW Library sin perder ni una sola de tus notas.",
  "intro": [
   "Las notas compartidas de JW Library llegan como un archivo pequeño (terminado en .jwshare.json) o como un bloque de texto pegado en un mensaje. JW Library no puede abrir ninguno de los dos, pero no hace falta. La parte de recepción de JW Sync lee las notas compartidas, te enseña qué contienen y las escribe en una copia tuya.",
   "Todo el intercambio ocurre en tu dispositivo. No hay cuenta, no se sube nada y a tus notas se les añade contenido: nunca se reemplazan.",
  ],
  "steps": [
   ("Haz primero una copia de tu propia biblioteca", "En JW Library: Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad. Este es el archivo al que se añadirán las notas compartidas, así que conviene que esté al día."),
   ("Abre la página Compartir y elige Recibir", "Entra en jwsync.org/share.html y elige Recibir notas."),
   ("Carga lo que te enviaron", "Elige el archivo .jwshare.json, o pega el texto compartido directamente en el recuadro si llegó como mensaje. En ambos casos obtienes una vista previa de solo lectura de cada nota antes de escribir nada."),
   ("Añádelas a tu copia", "Carga tu propia copia, elige la etiqueta que llevarán las notas importadas y añádelas. JW Sync genera una copia actualizada para que la descargues."),
   ("Restaura la copia actualizada en JW Library", "Estudio personal → Copia de seguridad y restauración → Restaurar, elige el archivo actualizado. Las notas compartidas ya están en tu biblioteca, en los párrafos y versículos correctos."),
  ],
  "sections": [
   ("No se reemplaza nada de lo tuyo",
    "Las notas compartidas se añaden como notas nuevas. Incluso cuando una nota compartida cae en un párrafo sobre el que ya habías escrito, sobreviven las dos: la tuya intacta y la suya al lado. Lo único que conviene recordar es la regla habitual al restaurar: restaura la copia actualizada, no una anterior."),
   ("¿Has cambiado de opinión después?",
    "Cada nota importada lleva la etiqueta que elegiste al añadirla. Abre tu copia en el Explorador de Estudio, filtra por esa etiqueta y podrás revisar o borrar todo el lote de una vez."),
  ],
  "faq": [
   ("El archivo llegó renombrado como .txt o se abrió como texto, ¿está roto?", "No. Las aplicaciones de mensajería lo hacen a menudo. Copia el texto y pégalo en el recuadro de Recibir; funciona exactamente igual."),
   ("¿Necesito toda la copia de quien me lo envía?", "No. El archivo compartido contiene solo las notas que decidió enviar, nada más de su biblioteca."),
   ("¿Se sube algo cuando previsualizo las notas?", "No. Leer el archivo compartido, previsualizarlo y escribir la copia actualizada ocurren todo en tu navegador, en tu dispositivo."),
  ],
 },

 "share-notes-with-study-group": {
  "title": "Compartir notas de investigación con un grupo de estudio",
  "h1": "Compartir investigación con un grupo y recoger la de los demás",
  "description": "Un archivo, muchas personas: envía un conjunto de notas de investigación a todos los que estudian el mismo tema y reúne lo que te devuelvan en un único conjunto propio.",
  "intro": [
   "Cuando varias personas investigan el mismo tema, la información suele acabar dispersa: uno encontró las referencias, otro el trasfondo histórico y un tercero las ilustraciones. Leer las capturas de pantalla de los demás no es lo mismo que tener el material en tu propia biblioteca, sobre los mismos versículos y localizable dentro de un año.",
   "Como un archivo compartido es solo un archivo, una sola exportación sirve para todo el grupo, y el mismo mecanismo trae su trabajo de vuelta a ti.",
  ],
  "steps": [
   ("Etiqueta tu investigación mientras la reúnes", "Dale una etiqueta al tema en JW Library para que el conjunto se mantenga unido. En el Explorador de Estudio puedes añadir una etiqueta a varias notas a la vez si no las etiquetaste en su momento."),
   ("Crea un archivo compartido para el grupo", "En jwsync.org/share.html elige Enviar notas, carga tu copia, elige la etiqueta del tema en el filtro, pulsa Seleccionar todo y crea el archivo."),
   ("Publícalo una sola vez", "Envía el mismo archivo a todos: un chat de grupo, un correo a varias personas, lo que ya use el grupo. No hay configuración por persona ni copia en ningún servidor."),
   ("Pide la suya a cambio", "Cada persona puede hacer exactamente lo mismo desde su lado. Añade a tu copia cada archivo que recibas, uno detrás de otro, dando a cada importación su propia etiqueta —el nombre de quien lo envía va muy bien— para saber siempre de quién es cada investigación."),
  ],
  "sections": [
   ("Un conjunto combinado, y aun así atribuible",
    "Después de unas cuantas rondas tienes toda la investigación del grupo sobre el tema en tu propia biblioteca, en los párrafos y versículos correctos y con cada aportación etiquetada por origen. La búsqueda lo encuentra todo de una vez; las etiquetas te permiten volver a separarlo cuando quieras."),
   ("Nadie tiene que exponer su biblioteca",
    "Cada uno comparte solo las notas que marca. El resto de la biblioteca de cada persona —su estudio privado, sus recordatorios personales, todo lo demás— no entra nunca en el archivo."),
  ],
  "faq": [
   ("¿Hay un límite de notas que pueda compartir de una vez?", "En la práctica, no. Las notas son pequeñas; un conjunto grande sigue generando un archivo que puedes enviar en un mensaje."),
   ("¿Y si dos personas me envían la misma nota?", "La verás dos veces, cada una con la etiqueta de quien la envió. La búsqueda del Explorador de Estudio hace fácil detectar y borrar los casi duplicados."),
   ("¿Se puede recibir sin enviar nada a cambio?", "Sí. Recibir y enviar son independientes: nadie está obligado a compartir para poder añadir lo que le han dado."),
  ],
 },

 "share-talk-preparation-notes": {
  "title": "Pasar la investigación que hay detrás de un discurso o una asignación",
  "h1": "Pasar tu investigación de discursos y asignaciones",
  "description": "Hiciste el trabajo de investigación para un discurso, una parte o una asignación. Aquí tienes cómo pasársela a quien la necesite después: como notas reales en su biblioteca o como texto para un documento.",
  "intro": [
   "La preparación rara vez se usa una sola vez. Los textos que rastreaste, el trasfondo que leíste, la forma en que al final decidiste enfocar un punto: quien cubra ese mismo material más adelante preferirá partir de ahí antes que de una página en blanco.",
   "JW Sync te da dos maneras de pasarlo, y encajan con personas distintas: como notas que llegan a la biblioteca de JW Library de la otra persona, o como texto sin formato que pueda pegar en un documento.",
  ],
  "steps": [
   ("Reúne la investigación bajo una etiqueta", "Mientras preparas, etiqueta las notas con el tema o la asignación. Si ya están escritas y sin etiquetar, abre tu copia en el Explorador de Estudio y etiquétalas en bloque en un par de minutos."),
   ("Decide qué formato le viene mejor a la otra persona", "Quien estudia en JW Library quiere notas en su biblioteca. Quien está montando un documento quiere texto. Puedes hacer las dos cosas desde el mismo conjunto."),
   ("Para enviar notas: usa la página Compartir", "En jwsync.org/share.html elige Enviar notas, carga tu copia, filtra por la etiqueta que usaste y pulsa Seleccionar todo; luego crea el archivo. La otra persona lo añade a su copia y la restaura, y sus notas quedan intactas."),
   ("Para enviar texto: exporta desde el Explorador de Estudio", "Filtra al mismo conjunto y cópialo o expórtalo como Markdown o texto sin formato. El formato se conserva, así que un bosquejo estructurado sigue estructurado al pegarlo en un documento."),
  ],
  "sections": [
   ("Guarda una copia para ti, en un formato que vuelvas a encontrar",
    "Esa misma exportación merece la pena guardarla para tu propio uso. Una etiqueta más un intervalo de fechas hacen que toda la preparación sea recuperable años después, que es justo cuando la querrás, y la extracción por fechas del Explorador de Estudio convierte cualquier periodo en su propio archivo."),
  ],
  "faq": [
   ("¿Los textos seguirán enlazados a los versículos correctos?", "Sí: las notas compartidas conservan el párrafo y el versículo al que estaban asociadas, así que caen en el sitio correcto de la biblioteca de la otra persona."),
   ("¿Puedo compartir notas que tienen subrayados?", "Sí. Los subrayados asociados a las notas que compartes viajan con ellas."),
  ],
 },

 "weekly-meeting-preparation-jw-library-notes": {
  "title": "Prepara la reunión con las notas que ya escribiste",
  "h1": "Preparación semanal con las notas que ya tienes",
  "description": "Ya has estudiado este material antes. Aquí tienes una rutina semanal corta que saca a la luz tus notas, subrayados y respuestas anteriores sobre la misma publicación antes de volver a preparar.",
  "intro": [
   "La mayoría prepara cada semana desde una página en blanco, aunque ya haya escrito sobre el mismo tema —a veces sobre el mismo texto— varias veces. Ese razonamiento anterior está en tu biblioteca; el único problema es que nada te lo devuelve en el momento oportuno.",
   "Una rutina de cinco minutos al empezar la preparación lo soluciona, y no usa más que la copia de seguridad que ya tienes.",
  ],
  "steps": [
   ("Carga una copia actual en el Explorador de Estudio", "Crea una copia en JW Library y ábrela en jwsync.org. Todo se lee en tu navegador."),
   ("Busca el tema antes de empezar", "Busca el texto temático, el asunto o la publicación. Todo lo que escribiste sobre ello en años anteriores aparece junto, en todas las publicaciones donde salga."),
   ("Revisa tus respuestas de estudio", "La vista de Respuestas de estudio reúne lo que escribiste en las preguntas, así que las rondas anteriores por el mismo material están ahí para construir sobre ellas en vez de repetirlas."),
   ("Añade lo que falte y devuélvelo", "Puedes editar o añadir notas ahí mismo: título, texto, etiquetas, color de subrayado. Exporta la copia editada y restáurala en JW Library, y tu preparación estará en la aplicación para la reunión."),
  ],
  "sections": [
   ("Por qué importan las notas antiguas",
    "Repasar lo que concluiste la vez anterior convierte la preparación en algo acumulativo. Dejas de redescubrir los mismos puntos y empiezas a construir sobre ellos, y las notas que añades esta semana se convierten en el punto de partida de la próxima ronda."),
   ("Una versión más suave: deja que las notas vengan a ti",
    "Si una búsqueda semanal te parece trabajo, Rescatar en la página de Estadísticas te devuelve unas cuantas notas antiguas cada día por su cuenta, incluidas las que escribiste en esta misma fecha en años anteriores. El mismo beneficio, sin ninguna rutina que recordar."),
  ],
  "faq": [
   ("¿Editar en el navegador cambia mi biblioteca directamente?", "No. Exportas una copia actualizada y la restauras en JW Library: la aplicación solo cambia con una restauración que haces tú."),
   ("¿Se sube mi copia cuando busco en ella?", "No. El archivo se lee localmente en tu navegador; no se envía nada a ninguna parte."),
  ],
 },

 "print-jw-library-notes": {
  "title": "Cómo imprimir tus notas de JW Library",
  "h1": "Llevar tus notas de JW Library al papel",
  "description": "JW Library no tiene botón de imprimir. Exporta tus notas como texto o Markdown, pégalas en cualquier documento e imprime: un diario de estudio, unas notas para alguien sin la aplicación o un archivo.",
  "intro": [
   "No hay forma de imprimir desde JW Library, y las capturas de la pantalla del teléfono se leen fatal. Pero las notas son tuyas, y llevarlas a un documento imprimible es sencillo en cuanto puedes leer el archivo de copia.",
   "El Explorador de Estudio lee una copia .jwlibrary en tu navegador y te permite copiar o exportar cualquier selección de notas como texto sin formato o Markdown, que es algo que ya entienden todos los procesadores de texto, aplicaciones de notas e impresoras.",
  ],
  "steps": [
   ("Crea una copia y ábrela", "JW Library → Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad, y luego carga el archivo en jwsync.org."),
   ("Acota lo que quieres en papel", "Filtra por publicación, etiqueta, color de subrayado o intervalo de fechas, o busca un tema. Se puede imprimir todo, pero un conjunto filtrado suele dar un documento mucho más útil."),
   ("Copia o exporta como texto o Markdown", "Saca la selección como Markdown o texto sin formato. La negrita, la cursiva y las listas se conservan, así que las notas estructuradas siguen estructuradas en la página."),
   ("Pega en un documento e imprime", "Vale cualquier procesador de texto o aplicación de notas. Ajusta los títulos y los márgenes que quieras y luego imprime o guarda como PDF."),
  ],
  "sections": [
   ("Hacer un diario de estudio",
    "Un intervalo de fechas es la unidad natural para un diario impreso: un año de notas, o el periodo que cubre una publicación. Extraer por fechas te da un conjunto cronológico limpio para imprimir o encuadernar, y es algo que da gusto tener fuera de la pantalla."),
   ("Imprimir para alguien que no usa la aplicación",
    "No todo el mundo estudia desde un dispositivo. Un juego impreso de notas sobre el material en curso es de verdad útil para quien prefiere el papel, y lleva los mismos dos minutos que cualquier otra exportación."),
  ],
  "faq": [
   ("¿Puedo imprimir también mis subrayados?", "La vista de subrayados enumera los pasajes que has marcado, y esa lista se copia como texto junto con tus notas."),
   ("¿Exportar cambia algo en JW Library?", "No. La exportación lee una copia de tu archivo; tu archivo original y la aplicación quedan intactos."),
  ],
 },

 "clean-up-duplicate-jw-library-notes": {
  "title": "Limpiar notas duplicadas y vacías de JW Library",
  "h1": "Eliminar notas duplicadas, notas vacías y desorden",
  "description": "¿Restauraste una copia dos veces o importaste las mismas notas otra vez? El Doctor de Biblioteca analiza tu archivo .jwlibrary en el navegador, encuentra duplicados y notas vacías y genera una copia limpia.",
  "intro": [
   "Las bibliotecas acumulan desorden. Restaurar una copia en un dispositivo que ya tenía algunas de esas mismas notas, importar dos veces un conjunto compartido, o años de notas a medias que nunca se terminaron: cada cosa deja algo detrás, y JW Library no ofrece ninguna forma de barrerlo en bloque.",
   "El Doctor de Biblioteca es una revisión gratuita para un archivo .jwlibrary. Analiza la copia en tu navegador, te dice en lenguaje claro qué ha encontrado y arregla lo que se puede arreglar con un toque.",
  ],
  "steps": [
   ("Haz una copia primero, como siempre", "JW Library → Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad. Guarda este archivo: es tu red de seguridad."),
   ("Ejecuta la revisión", "Abre jwsync.org, carga la copia e inicia el Doctor de Biblioteca. Examina el contenido y la estructura del archivo sin enviarlo a ninguna parte."),
   ("Lee lo que ha encontrado", "Los duplicados, las notas vacías y el resto del desorden se enumeran con claridad, con sus cantidades, para que veas el tamaño del problema antes de cambiar nada."),
   ("Arregla y descarga la copia limpia", "Un toque aplica las reparaciones y genera un archivo .jwlibrary nuevo y limpio. Tu original nunca se modifica."),
   ("Restaura el archivo limpio", "Copia de seguridad y restauración → Restaurar, y elige el archivo limpio. Tu biblioteca es la misma, menos el desorden."),
  ],
  "sections": [
   ("Por qué aparecen los duplicados",
    "Casi siempre por una restauración. Si restauras una copia en un dispositivo que ya tenía parte de ese mismo material —o restauras el mismo archivo dos veces por caminos distintos— la aplicación no tiene forma de saber que ya había visto esas notas."),
   ("Combinar es la manera de evitarlos",
    "Por eso exactamente combinar dos copias es más seguro que restaurar una sobre otra: la combinación detecta el material que ya existe y lo conserva una sola vez. Las mismas comprobaciones se ejecutan dentro de cada combinación, así que la copia combinada sale limpia aunque los archivos de partida no lo estuvieran."),
  ],
  "faq": [
   ("¿Borrará notas que sí quiero?", "Elimina duplicados exactos y notas vacías, es decir, material que no tiene nada que perder. Y como escribe un archivo nuevo en vez de editar el tuyo, el original siempre está ahí por si acaso."),
   ("¿Puede recuperar notas que borré en la aplicación?", "No. Si una nota se borró en JW Library antes de hacer la copia, no está en el archivo y no se puede recuperar: hay que buscar en una copia más antigua."),
  ],
 },

 "backup-jw-library-before-phone-repair": {
  "title": "Copia de seguridad de JW Library antes de un reinicio o una reparación",
  "h1": "Antes de un reinicio de fábrica, una reparación o vender el teléfono",
  "description": "Un reinicio borra las notas de JW Library junto con todo lo demás, y las herramientas de transferencia no las llevan. Haz una copia, comprueba que de verdad se abre y luego reinicia sin arriesgar nada.",
  "intro": [
   "Reinicia el teléfono, mándalo a reparar o pásaselo a otra persona y los datos de estudio personal de JW Library se van con él. Las fotos y las aplicaciones vuelven desde una copia en la nube; los años de notas, subrayados y marcadores normalmente no, porque las herramientas de transferencia se saltan los datos privados de la aplicación.",
   "La solución lleva cinco minutos, y el paso que la gente se salta es justo el que más importa: comprobar que el archivo de copia se puede leer de verdad antes de borrar el dispositivo.",
  ],
  "steps": [
   ("Crea la copia", "JW Library → Estudio personal → Copia de seguridad y restauración → Crear una copia de seguridad. Obtienes un archivo .jwlibrary, normalmente de unos pocos megabytes."),
   ("Sácala del dispositivo", "Envíatela por correo o guárdala en Drive, iCloud o una carpeta del ordenador. Una copia que solo existe en el teléfono que estás a punto de borrar no es una copia."),
   ("Comprueba que se abre antes de borrar nada", "Carga el archivo en jwsync.org y míralo: las notas, los subrayados y los marcadores deberían estar todos, y la revisión avisará de cualquier problema del archivo. Ese es todo el sentido del ejercicio: descubrir después que el archivo no se puede leer es demasiado tarde."),
   ("Reinicia y luego restaura", "Después del reinicio o la reparación, instala JW Library, inicia sesión y ve a Copia de seguridad y restauración → Restaurar; elige tu archivo."),
   ("¿Usaste un teléfono prestado mientras tanto? Combina, no sobrescribas", "Si tomaste notas en un dispositivo temporal, haz también una copia de ese y combina los dos archivos en jwsync.org antes de restaurar; si no, restaurar la copia antigua borrará todo lo que escribiste durante la espera."),
  ],
  "sections": [
   ("Por qué el minuto extra de comprobación merece la pena",
    "Las transferencias interrumpidas, los servicios en la nube que estropean archivos y las extensiones renombradas durante el envío producen copias que parecen correctas en una carpeta y fallan al restaurar. Abrir el archivo primero convierte un problema silencioso en uno que todavía puedes arreglar, mientras el dispositivo original aún tiene los datos."),
   ("Guarda el archivo después de restaurar",
    "No lo borres en cuanto el dispositivo nuevo funcione. Las copias antiguas son el único camino de vuelta cuando alguien borra una nota por accidente meses después, y guardarlas no cuesta nada."),
  ],
  "faq": [
   ("¿Volverán mis publicaciones descargadas?", "La copia lleva tus datos de estudio personal: notas, subrayados, marcadores, etiquetas y listas de reproducción. Las publicaciones sencillamente se vuelven a descargar después."),
   ("¿Funciona el archivo si cambio de marca de teléfono o de plataforma?", "Sí. El formato .jwlibrary es el mismo en Android, iPhone, iPad y Windows."),
  ],
 },

 "jw-library-notes-missing-after-update": {
  "title": "Faltan notas de JW Library tras una actualización o reinstalación",
  "h1": "Las notas han desaparecido tras actualizar, reinstalar o restaurar",
  "description": "Tus notas desaparecieron después de actualizar, reinstalar o volver a iniciar sesión. Qué hacer primero, qué no hacer y cómo recuperarlas sin perder nada de lo que has escrito desde entonces.",
  "intro": [
   "Es un momento desagradable: abres JW Library y las notas no están. Antes que nada, un consejo: no corras. Casi todo lo que hace irrecuperable esta situación se hace en los primeros diez minutos, al sobrescribir justamente la copia que todavía contiene las notas que faltan.",
   "Sigue los pasos de abajo en orden. El objetivo es acabar con un solo archivo que contenga tanto las notas antiguas como todo lo que hayas escrito desde entonces.",
  ],
  "steps": [
   ("Todavía no sobrescribas tus copias", "Resiste la tentación de crear una copia nueva encima de una antigua, y no restaures nada a ciegas. Un archivo de copia anterior es el sitio más probable donde tus notas siguen existiendo."),
   ("Busca la copia más reciente que tengas", "Revisa los adjuntos del correo, Google Drive, iCloud Drive, la carpeta de descargas del ordenador y cualquier otro dispositivo donde hayas restaurado. Las copias son pequeñas, así que la gente suele tener más de las que recuerda."),
   ("Mira dentro del archivo antes de restaurarlo", "Carga el candidato en jwsync.org y comprueba qué contiene: cuántas notas, de qué publicaciones y hasta qué fecha. Eso te dice si es el archivo adecuado antes de comprometerte con una restauración."),
   ("Haz también una copia del dispositivo actual", "Aunque parezca vacío, haz una copia. Si has escrito algo desde que desaparecieron las notas, ese archivo es la única copia que existe."),
   ("Combina los dos y luego restaura", "Combina la copia antigua con la actual en jwsync.org. El resultado contiene las notas recuperadas y todo lo escrito desde entonces, conservando los duplicados una sola vez. Restaura ese archivo combinado, nunca la copia antigua a secas."),
  ],
  "sections": [
   ("Por qué restaurar la copia antigua a secas es un error",
    "Una restauración reemplaza por completo la biblioteca del dispositivo. Si restauras una copia antigua directamente, recuperas las notas que faltaban y pierdes todo lo escrito después de esa copia. Combinar primero es lo que hace que la recuperación no pierda nada."),
   ("Si la propia copia no se restaura",
    "Un archivo que da error al restaurar no está necesariamente perdido. Pásale la revisión: los daños por descargas interrumpidas, sincronización en la nube o una extensión renombrada suelen ser reparables, y una copia limpia se restaura con normalidad."),
  ],
  "faq": [
   ("¿Las notas siguen en el dispositivo en algún sitio?", "No de una forma a la que puedas acceder desde fuera de la aplicación. La recuperación pasa realmente por un archivo de copia anterior, y por eso importa tanto guardar los antiguos."),
   ("¿Volver a iniciar sesión devuelve las notas?", "No. Los datos de estudio personal no están en ninguna cuenta: viven en el dispositivo y solo viajan mediante archivos de copia de seguridad."),
   ("¿Y si la única copia que tengo es de hace meses?", "Combínala con una copia del dispositivo tal como está ahora. Recuperarás todo lo que tiene el archivo antiguo y conservarás todo lo que el dispositivo aún tiene, sin elegir entre las dos."),
  ],
 },

 "help-family-member-move-jw-library-notes": {
  "title": "Ayudar a un familiar a trasladar sus notas de JW Library",
  "h1": "Ayudar a otra persona a trasladar o rescatar sus notas de JW Library",
  "description": "Eres a quien le piden que arregle el teléfono. Aquí tienes el camino más corto y fiable para trasladar las notas de JW Library de un familiar a un dispositivo nuevo, incluido cómo hacerlo sin leer sus notas.",
  "intro": [
   "Tarde o temprano alguien te pone su teléfono en la mano con el nuevo al lado. Las notas de JW Library son la parte que no se traslada sola, y suelen ser la parte que más importa: años de estudio que ninguna herramienta de transferencia va a llevar.",
   "El proceso es el mismo que si lo hicieras para ti, con una consideración añadida que conviene pensar antes: en el dispositivo de quién se hace el trabajo.",
  ],
  "steps": [
   ("Guíale para hacer la copia en el dispositivo antiguo", "JW Library → Estudio personal → menú de tres puntos → Copia de seguridad y restauración → Crear una copia de seguridad. Se guarda un archivo .jwlibrary. Si no estás con esa persona, esta parte puede hacerla por teléfono."),
   ("Consigue el archivo donde lo necesitas", "Pídele que se lo envíe a sí mismo por correo o que te lo comparta. Es lo bastante pequeño como para mandarlo por cualquier aplicación de mensajería."),
   ("Comprueba que el archivo se abre", "Cárgalo en jwsync.org y confirma que las notas están ahí. Hacerlo antes de borrar o entregar el dispositivo antiguo es lo que convierte una mala sorpresa en un no-problema."),
   ("Combina si el dispositivo nuevo ya tiene notas", "Si lleva un tiempo usando el teléfono nuevo, haz también una copia de ese y combina los dos archivos; si no, restaurar la copia antigua borrará todo lo que haya escrito en el nuevo."),
   ("Acompáñale en la restauración", "En el dispositivo nuevo: Copia de seguridad y restauración → Restaurar, y elige el archivo. Aparecen las notas, los subrayados, los marcadores y las etiquetas."),
  ],
  "sections": [
   ("Hacerlo sin leer sus notas",
    "Las notas de estudio personal son personales. Si prefieres no verlas —o esa persona prefiere que no las veas— haz todo en su dispositivo: es una página web, así que puedes abrir jwsync.org en su teléfono o tableta, cargar sus archivos ahí y no tener nunca la copia en tu propio equipo. En ninguno de los dos casos se sube nada, pero así el archivo no sale de sus manos."),
   ("Déjale una copia que sepa encontrar",
    "Antes de devolverle el teléfono, asegúrate de que el archivo de copia está en un sitio donde pueda volver a encontrarlo: su propio correo o su nube, no solo tu carpeta de descargas. La próxima vez puede que no te necesite."),
  ],
  "faq": [
   ("¿Puedo hacerlo a distancia?", "Sí. Si esa persona puede crear una copia y enviarte el archivo, todo lo demás funciona en la distancia, y la restauración son unos pocos toques que puedes ir explicándole."),
   ("Tiene un Android y el nuevo es un iPhone. ¿Importa?", "No. El formato de copia es idéntico en Android, iPhone, iPad y Windows."),
   ("¿Y si nunca hizo una copia y el teléfono antiguo ya no está?", "Entonces no hay nada de donde recuperar: los datos vivían en ese dispositivo. Merece la pena establecer enseguida el hábito de hacer copias periódicas en el teléfono nuevo."),
  ],
 },

}

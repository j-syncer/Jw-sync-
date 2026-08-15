# -*- coding: utf-8 -*-
"""Portuguese translations of the static guide pages.

Glossary kept consistent across all 37 guides:
  backup / .jwlibrary file  → backup (o arquivo .jwlibrary)
  Personal Study            → Estudo Pessoal
  Backup and Restore        → Backup e Restauração
  restore                   → restaurar
  merge                     → mesclar / mesclagem
  notes                     → notas
  highlights                → destaques
  bookmarks                 → marcadores
  tags                      → etiquetas
  Study Explorer            → Explorador de Estudo
  Library Doctor            → Doutor da Biblioteca
  Reading Companion         → Companheiro de Leitura
  Resurface                 → Retomar
  Study Map                 → Mapa de Estudo
  Study Stats               → Estatísticas de Estudo
  Conflict Reviewer         → Revisor de Conflitos
  meeting                   → reunião
  congregation              → congregação
  assembly / convention     → assembleia / congresso
"""

GUIDES_PT = {}

GUIDES_PT["merge-jw-library-backups"] = {
    "title": "Como mesclar backups do JW Library de dois aparelhos",
    "h1": "Como mesclar backups do JW Library de dois aparelhos",
    "description": "Junte as notas, os destaques, os marcadores e as etiquetas de dois ou mais "
                   "backups do JW Library em um único arquivo .jwlibrary — de graça, com "
                   "privacidade, no seu navegador.",
    "intro": [
        "Você estudou A Sentinela no celular e um artigo diferente no tablet. Agora cada aparelho tem um trabalho que o outro não tem, e o JW Library não consegue juntá-los: a restauração dele substitui tudo, não mescla, então o backup que você restaurar apaga o estudo do outro aparelho. Só com o aplicativo não há como ficar com os dois.",
        "É para isso que este site existe. Ele lê dois (ou mais) arquivos .jwlibrary e junta as notas, os destaques, os marcadores e as etiquetas de todos eles em um backup novo, de modo que não é preciso escolher entre nada. Tudo acontece dentro do seu navegador: seus arquivos nunca são enviados a nenhum servidor, então suas notas de estudo continuam particulares.",
        "É também por isso que o hábito é preventivo e não corretivo: quando você mescla de vez em quando, deixa de precisar lembrar de restaurar antes de estudar em outro lugar. Estude onde estiver, mescle quando for conveniente, e todos os aparelhos se atualizam.",
    ],
    "steps": [
        ("Faça um backup em cada aparelho",
         "No JW Library, abra Estudo Pessoal, toque no menu de três pontos, escolha Backup e "
         "Restauração e depois Criar um backup. Faça isso em cada aparelho. Cada um gera um "
         "arquivo .jwlibrary."),
        ("Abra o JW Sync",
         "Acesse jwsync.org em qualquer navegador — no celular, no tablet ou no computador. "
         "Não há nada para instalar."),
        ("Carregue os dois arquivos de backup",
         "Arraste (ou selecione) os arquivos .jwlibrary. O JW Sync lê tudo localmente, no "
         "seu aparelho."),
        ("Confira a prévia antes de mesclar",
         "Antes de qualquer coisa ser gravada, uma prévia mostra exatamente o que será "
         "combinado. Se a mesma nota foi editada de formas diferentes em cada aparelho, o "
         "Revisor de Conflitos mostra as duas versões lado a lado, com as diferenças "
         "palavra por palavra, para você escolher qual manter — ou deixar que a opção "
         "“Sugerir a melhor” escolha por você."),
        ("Baixe o arquivo mesclado e restaure",
         "Baixe o arquivo .jwlibrary mesclado e restaure-o em cada aparelho por Backup e "
         "Restauração → Restaurar. Agora os dois aparelhos têm a biblioteca completa e "
         "combinada."),
    ],
    "sections": [
        ("O que é mesclado?",
         "Notas, destaques, marcadores, etiquetas e as ligações entre eles. Duplicatas são "
         "detectadas automaticamente, então restaurar o arquivo mesclado nunca duplica nada. "
         "Backups do Android, do iPhone, do iPad e do aplicativo para Windows usam o mesmo "
         "formato e se combinam sem problema."),
        ("É seguro?",
         "A mesclagem nunca altera seus arquivos originais — ela gera um backup totalmente "
         "novo, então os originais continuam intactos como reserva. E, como tudo roda no "
         "próprio navegador, nenhum dado sai do seu aparelho."),
        ("O que existe de fato dentro de um arquivo .jwlibrary",
         "Um backup .jwlibrary é um arquivo ZIP. Renomeie uma cópia para .zip e abra: você vai encontrar o userData.db, um banco de dados SQLite com todas as notas, destaques, marcadores e etiquetas que você já criou, junto de um pequeno manifest.json que descreve o backup. Suas notas ficam na tabela Note, os destaques em UserMark e BlockRange, os marcadores em Bookmark e as etiquetas em Tag e TagMap. Entender que o backup é um banco de dados completo, e não um punhado de arquivos soltos, explica todo o resto desta página: é por isso que restaurar é tudo ou nada, e é por isso que dois backups podem ser combinados."),
        ("Por que a restauração do próprio JW Library não mescla",
         "Ao restaurar, o JW Library não lê seu backup e acrescenta o que falta ao que já está no aparelho: ele substitui o banco de dados do aparelho pelo do arquivo. É um projeto deliberado e seguro, porque garante que o aparelho termina num estado conhecido, mas significa que restaurar o backup do tablet no celular descarta tudo o que o celular tinha e o tablet não. Não existe ajuste que mude isso, e é exatamente essa lacuna que a mesclagem preenche: ela produz um único arquivo que já contém o trabalho dos dois aparelhos, então o aparelho em que você restaurar fica completo."),
        ("Como as duplicatas são detectadas",
         "Cada nota, destaque e marcador carrega um GUID — um identificador único atribuído no momento da criação e preservado em todos os backups seguintes. Quando o mesmo item aparece em dois backups, as duas cópias carregam o mesmo GUID, então ele é reconhecido como um só item e mantido uma vez. É por isso que mesclar o mesmo par de arquivos duas vezes não duplica nada, e por isso você pode remesclar toda semana sem risco. Quando os GUIDs coincidem mas o texto difere — a mesma nota editada nos dois aparelhos — não dá para resolver automaticamente, e o item aparece no Revisor de Conflitos com uma comparação palavra por palavra para você escolher."),
        ("O que não está no backup",
         "O backup carrega apenas seus dados de estudo pessoal. Publicações baixadas, traduções da Bíblia, vídeos e áudio não entram, e é por isso que os arquivos de backup são pequenos — normalmente alguns megabytes mesmo com anos de estudo. Depois de restaurar num aparelho novo, talvez você precise baixar de novo as publicações que costuma ler. Nada do que você escreveu é afetado por isso: as notas são ancoradas às publicações por referência, então elas se reconectam assim que a publicação estiver presente."),
        ("Se a mesclagem informar 0 notas adicionadas",
         "Quase sempre isso está certo, e não é falha. Significa que todas as notas do segundo arquivo já existiam no primeiro — comum quando você mesclou há pouco, ou quando um aparelho simplesmente está atrás do outro. Confira a prévia: ela lista o que cada arquivo contribui antes de qualquer coisa ser gravada. Se você esperava itens novos e não vê nenhum, confirme que fez o backup do aparelho depois da sessão de estudo que está procurando, porque um backup só contém o que existia no momento em que foi criado."),
    ],
    "faq": [
        ("Posso mesclar mais de dois backups?",
         "Sim — carregue quantos arquivos .jwlibrary você tiver aparelhos. Todos são "
         "combinados em um único backup."),
        ("A mesclagem vai criar notas duplicadas?",
         "Não. Notas, destaques e marcadores idênticos são detectados e mantidos uma única "
         "vez. Versões realmente diferentes da mesma nota aparecem no Revisor de Conflitos "
         "para você decidir."),
        ("Funciona entre Android e iPhone?",
         "Sim. O formato .jwlibrary é idêntico no Android, no iOS, no iPadOS e no Windows, "
         "então backups de plataformas diferentes se mesclam sem nenhuma conversão."),
        ("Preciso mesclar numa ordem específica?",
         "Não. A mesclagem não depende da ordem — o mesmo conjunto de arquivos produz o mesmo resultado, qualquer que seja o primeiro a ser carregado. A ordem só afeta qual arquivo é tratado como base no resumo da prévia."),
        ("O que acontece com as etiquetas que existem em só um aparelho?",
         "Elas são levadas intactas, junto com os vínculos entre as etiquetas e as notas que marcam. Se os dois aparelhos tiverem uma etiqueta com o mesmo nome, ela é tratada como uma só e recebe as notas dos dois."),
        ("Qual é o tamanho do arquivo mesclado?",
         "Mais ou menos a soma dos originais menos as duplicatas — normalmente ainda alguns megabytes. Backups não contêm mídia das publicações, então mesmo uma biblioteca muito anotada continua pequena o bastante para caber num e-mail."),
        ("Dá para desfazer uma restauração?",
         "Não pelo JW Library, e é por isso que guardar os backups originais importa. A mesclagem nunca modifica os arquivos que você carrega, então seus backups anteriores continuam exatamente como estavam e podem ser restaurados se você quiser voltar atrás."),
    ],
}

GUIDES_PT["sync-jw-library-multiple-devices"] = {
    "title": "Como sincronizar o JW Library entre vários aparelhos",
    "h1": "Como manter o JW Library sincronizado entre vários aparelhos",
    "description": "O JW Library não tem sincronização entre aparelhos. Veja uma rotina "
                   "simples e privada para manter notas, destaques e marcadores iguais no "
                   "celular, no tablet e no computador.",
    "intro": [
        "Quase todo mundo que estuda em dois aparelhos descobre o problema do mesmo jeito: as notas escritas no tablet não estão no celular, e restaurar o backup de um no outro apagaria o que esse outro tinha. O JW Library não oferece sincronização, e sua restauração é deliberadamente tudo ou nada, então manter os aparelhos alinhados exige uma rotina, não um ajuste.",
        "O JW Library não sincroniza os dados de estudo pessoal entre aparelhos — não existe "
        "uma conta que leve suas notas do celular para o tablet. O recurso oficial é o Backup "
        "e Restauração, e restaurar substitui os dados do aparelho por completo. Então como "
        "manter dois ou três aparelhos iguais sem perder nada?",
        "A resposta é uma rotina curta de mesclar e restaurar. Feita toda semana ou todo mês, "
        "ela leva uns dois minutos e mantém cada aparelho com a sua biblioteca completa.",
    ],
    "steps": [
        ("Faça backup de todos os aparelhos",
         "Em cada aparelho: Estudo Pessoal → menu de três pontos → Backup e Restauração → "
         "Criar um backup. Você fica com um arquivo .jwlibrary por aparelho."),
        ("Mescle os backups em jwsync.org",
         "Carregue todos os arquivos. O JW Sync combina as notas, os destaques, os marcadores "
         "e as etiquetas de cada aparelho em um único arquivo .jwlibrary mesclado — "
         "localmente, no seu navegador, sem enviar nada."),
        ("Restaure o arquivo mesclado em todos os aparelhos",
         "Backup e Restauração → Restaurar e escolha o arquivo mesclado. Agora todos os "
         "aparelhos estão iguais e completos."),
        ("Deixe o JW Sync lembrar você",
         "Ative um lembrete de sincronização (semanal ou mensal) no JW Sync e ele avisa "
         "quando for hora de repetir a rotina. Ele também guarda os aparelhos que você "
         "salvou, deixando cada rodada mais rápida."),
    ],
    "sections": [
        ("Por que não simplesmente restaurar o backup mais recente?",
         "Porque “mais recente” reflete apenas um aparelho. Se você fez anotações da reunião "
         "no celular e notas de estudo no tablet na mesma semana, cada backup tem conteúdo "
         "que falta no outro. Restaurar um por cima do outro perde metade do seu trabalho. "
         "É a mesclagem que torna a rotina segura."),
        ("Com que frequência devo sincronizar?",
         "Ajuste ao seu jeito de estudar. Dois aparelhos ativos usados todo dia: uma vez por "
         "semana é confortável. Um tablet que só sai da gaveta para as reuniões: uma vez por "
         "mês basta. Esperar mais só significa que a mesclagem terá mais coisas para "
         "combinar — nada se perde entre uma rodada e outra."),
        ("Por que não existe sincronização de verdade",
         "O JW Library não tem conta que leve os dados de estudo pessoal de um aparelho para outro. Notas, destaques e marcadores vivem num banco de dados dentro de cada aparelho e ficam por lá. O único mecanismo oficial para movê-los é Backup e Restauração, e uma restauração substitui os dados do aparelho de destino em vez de combiná-los. Então dois aparelhos usados de forma independente divergem para sempre, a menos que algo os mescle — que é justamente o objetivo da rotina abaixo."),
        ("Manter um arquivo mestre",
         "A rotina funciona melhor se você tratar um arquivo mesclado como o mestre atual. A cada ciclo, faça backup de todos os aparelhos, mescle esses backups e restaure o resultado em todos. O arquivo mesclado vira o mestre do ciclo seguinte. Guardar os mestres datados na nuvem dá a você um mecanismo de sincronização e um arquivo histórico ao mesmo tempo — se apagar algo sem querer, um mestre anterior ainda o contém."),
        ("O que acontece se você deixar um aparelho de fora por um tempo",
         "Nada se perde. Um aparelho que ficou de fora de vários ciclos simplesmente carrega dados mais antigos; quando você finalmente o incluir, as notas dele se mesclam com todo o resto e os itens repetidos são casados por GUID em vez de duplicados. A única situação que exige decisão é a mesma nota editada em dois aparelhos desde a última mesclagem, e isso aparece no Revisor de Conflitos com as duas versões lado a lado."),
        ("Com que frequência já é o bastante",
         "Ajuste ao quanto de trabalho você se incomodaria em refazer. Semanal serve para quem estuda em dois aparelhos quase todo dia; mensal sobra se um deles é usado de vez em quando. O importante é fazer antes de qualquer coisa irreversível — uma troca de celular, um reset, um conserto — porque é aí que uma divergência vira perda."),
        ("Celular, tablet e o app de Windows juntos",
         "A rotina não se importa com quantos aparelhos existem nem com o que eles rodam. Faça backup de cada um, mescle todos numa passada só e restaure o arquivo mesclado em todos. Um computador com Windows usado para preparação e um celular usado nas reuniões se combinam exatamente como dois celulares, porque toda plataforma grava o mesmo formato de backup."),
        ("Reduzir os conflitos antes que apareçam",
         "Conflitos só surgem quando a mesma nota é editada em dois aparelhos entre mesclagens. Na prática isso é raro, e fica mais raro ainda se você escrever em um aparelho de cada vez — lendo em qualquer um, mas digitando onde costuma digitar. Mesclar com mais frequência também encurta a janela em que uma divergência pode acontecer, e isso funciona melhor do que tentar lembrar qual aparelho tem a versão mais nova."),
        ("Onde a rotina compensa",
         "O valor de manter os aparelhos mesclados não é a arrumação — é que cada aparelho vira um backup completo da sua biblioteca de estudo. Perca ou quebre qualquer um deles e os outros ainda têm tudo, o que transforma o pior caso de anos de notas perdidas num incômodo. Essa é uma posição mais sólida do que qualquer hábito de backup em um único aparelho consegue dar."),
    ],
    "faq": [
        ("O JW Sync fica rodando em segundo plano?",
         "Não — ele é uma página da web, não um serviço instalado. Nada fica examinando seus "
         "aparelhos. Você executa a rotina quando quiser; o lembrete opcional é só uma "
         "notificação."),
        ("Dá para sincronizar três ou mais aparelhos?",
         "Sim. Faça backup de cada um, carregue todos os arquivos, mescle uma vez e restaure "
         "o arquivo mesclado em todos."),
        ("E se eu editei a mesma nota em dois aparelhos?",
         "As duas versões são mantidas até você escolher. O Revisor de Conflitos mostra as duas lado a lado com uma comparação palavra por palavra, ou você pode deixar que ele sugira a versão mais completa."),
        ("A ordem em que eu restauro importa?",
         "Não. Depois que o arquivo mesclado é criado, restaurá-lo em cada aparelho deixa todos no mesmo estado completo, na ordem que for melhor para você."),
        ("Dá para sincronizar três aparelhos ou mais?",
         "Dá. Faça backup de cada um e carregue todos na mesma mesclagem — não há limite ligado à quantidade de aparelhos."),
        ("Isso pode ser automatizado?",
         "Totalmente não, porque o JW Library não tem API de sincronização e a etapa de restaurar acontece dentro do app. A rotina manual leva cerca de dois minutos depois que você se acostuma."),
        ("Preciso mesclar se no segundo aparelho eu só leio?",
         "Se você nunca anota nele, só precisa restaurar nele de tempos em tempos para que ele carregue suas notas atuais."),
    ],
}

GUIDES_PT["transfer-jw-library-notes-new-phone"] = {
    "title": "Como transferir as notas do JW Library para um celular novo",
    "h1": "Como transferir as notas do JW Library para um celular novo",
    "description": "Levar as notas do JW Library para um celular novo é um backup e uma restauração, e o aplicativo resolve isso em uns dois minutos. Aqui estão os passos e também o único caso que ele não resolve: quando o celular novo já tem notas próprias.",
    "intro": [
        "Isso é mais fácil do que as pessoas imaginam, e você não precisa de nenhuma ferramenta extra. O JW Library já vem com backup e restauração, e isso leva cada nota, destaque, marcador e etiqueta para o celular novo, inclusive entre Android e iPhone. Faça isso enquanto o aparelho antigo ainda funciona e o processo todo leva alguns minutos.",
        "A única parte que precisa ser feita de propósito é a transferência em si: as ferramentas que passam dados de um celular para outro levam seus aplicativos e suas fotos, mas pulam os dados de estudo pessoal do JW Library, então crie o arquivo de backup em vez de supor que ele vai junto.",
        "Existe exatamente uma situação que o aplicativo não resolve, e vale a pena saber disso antes de começar: se você já vem estudando no celular novo, restaurar o backup do antigo apaga esse trabalho, porque a restauração substitui a biblioteca do aparelho por inteiro. Se for o seu caso, a parte sobre mesclar mais abaixo é o que você procura.",
    ],
    "steps": [
        ("Crie um backup no celular antigo",
         "Abra o JW Library → Estudo Pessoal → menu de três pontos → Backup e Restauração → "
         "Criar um backup. Isso salva um arquivo .jwlibrary com todos os seus dados de "
         "estudo."),
        ("Leve o arquivo para o celular novo",
         "Mande por e-mail para você mesmo ou use o Google Drive, o iCloud, o AirDrop ou um "
         "cabo USB. O arquivo é pequeno — normalmente alguns megabytes."),
        ("Restaure no celular novo",
         "Instale o JW Library, depois vá em Estudo Pessoal → Backup e Restauração → "
         "Restaurar e escolha o arquivo .jwlibrary. Todas as notas, destaques, marcadores e "
         "etiquetas aparecem."),
    ],
    "sections": [
        ("Já fez notas no celular novo? Mescle em vez de sobrescrever",
         "Restaurar substitui o que estiver no aparelho. Se você já vem usando o celular novo "
         "há um tempo e ele tem notas próprias, não restaure por cima delas — faça também um "
         "backup do celular novo, mescle os dois backups em um único arquivo em jwsync.org "
         "(de graça, no navegador, sem enviar nada) e restaure o arquivo mesclado. Você fica "
         "com os dois conjuntos de notas."),
        ("Uma pegadinha comum no iPhone",
         "Se o arquivo de backup chegar ao iPhone renomeado para .zip, renomeie de volta para "
         ".jwlibrary antes de restaurar — o conteúdo está intacto; só a extensão mudou no "
         "caminho."),
        ("Faça isto antes de apagar ou entregar o celular antigo",
         "O backup precisa ser criado enquanto o celular antigo ainda funciona e ainda tem o JW Library instalado. Depois que o aparelho é resetado, entregue na troca ou repassado, as notas vão junto: o JW Library não guarda cópia dos dados de estudo pessoal na nuvem, e um backup do celular como o Google One ou um backup de aparelho do iCloud costuma restaurar um retrato mais antigo dos dados do app, ou nenhum. Crie primeiro o arquivo .jwlibrary, coloque-o em local seguro e confirme que consegue vê-lo antes de apagar qualquer coisa."),
        ("Como tirar o arquivo do celular antigo",
         "No Android o arquivo é gravado na pasta que você escolher — normalmente Downloads ou Documentos — e pode ser movido com qualquer gerenciador de arquivos, enviado para você mesmo por e-mail ou jogado na nuvem. No iPhone o menu de compartilhamento aparece assim que o backup é criado: salve em Arquivos, mande por AirDrop para o celular novo ou envie para você mesmo. O método não importa e não corrompe o arquivo; um .jwlibrary é um único arquivo compactado que chega inteiro ou não chega."),
        ("Por que um app de transferência entre celulares não basta",
         "Ferramentas como Smart Switch, Migrar para iOS ou uma restauração do iCloud copiam apps e dados de sistema, mas bancos de dados privados de app são frequentemente pulados, restaurados pela metade ou restaurados de um ponto anterior no tempo. É comum descobrir a falha semanas depois, quando o celular antigo já foi. Trate o arquivo .jwlibrary como a cópia que vale e a transferência do celular como conveniência — se ela por acaso trouxer suas notas, restaurar seu próprio backup por cima não custa nada."),
        ("Confirme que a transferência funcionou",
         "Depois de restaurar no celular novo, abra duas ou três publicações que você anotou recentemente e confirme que as notas, as cores dos destaques e os marcadores estão lá. Uma checagem mais rápida é abrir o próprio arquivo de backup no navegador antes de apagar o aparelho antigo — você consegue ver todas as notas, destaques e marcadores que ele contém, então sabe o que deveria aparecer. Só apague o celular antigo depois que o novo estiver conferido."),
        ("Mudando também para um tablet ou computador",
         "O mesmo arquivo serve para tudo. Se você está configurando um celular novo e um tablet ao mesmo tempo, restaure o mesmo arquivo .jwlibrary nos dois e eles começam idênticos. Dali em diante voltarão a divergir conforme você estudar em cada um, então vale decidir agora se vai mantê-los mesclados de tempos em tempos ou tratar um como o aparelho principal."),
        ("Se o celular novo já tiver notas",
         "Isso acontece quando você usa o aparelho novo por uma semana antes de fazer a transferência. Uma restauração direta substituiria esse trabalho pelos dados do celular antigo. Faça primeiro um backup do celular novo, mescle com o backup do antigo e restaure o resultado — os dois conjuntos de notas terminam numa biblioteca só, em vez de um apagar o outro."),
        ("O que fazer quando o celular novo já estiver funcionando",
         "Confira antes de se desfazer de qualquer coisa. Abra no celular novo algumas publicações que anotou recentemente e confirme que as notas, as cores e os marcadores estão lá; só então apague ou entregue o aparelho antigo, nessa ordem e nunca ao contrário. Depois de tudo ajustado, guarde um backup fora do celular, porque a situação que trouxe você a esta página vai voltar na próxima troca."),
    ],
    "faq": [
        ("Isso leva também as publicações que baixei?",
         "O backup carrega os seus dados de estudo pessoal — notas, destaques, marcadores, "
         "etiquetas e listas de reprodução. As publicações são simplesmente baixadas de novo "
         "no celular novo."),
        ("Faz diferença se os celulares têm versões diferentes do Android?",
         "Não. O formato .jwlibrary é o mesmo em todo lugar, inclusive entre versões do "
         "Android e entre Android e iPhone."),
        ("Dá para levar minhas notas se o celular antigo já foi?",
         "Só se existir um arquivo .jwlibrary em algum lugar — em Arquivos, Downloads, um e-mail que você mandou para si mesmo ou na nuvem. Sem ele não há o que restaurar, porque os dados de estudo pessoal ficam apenas no aparelho."),
        ("Os dois celulares precisam ter a mesma versão do JW Library?",
         "Não precisam ser idênticas, mas atualize o celular novo para a versão atual antes de restaurar. Um backup feito por uma versão mais nova pode usar um esquema de banco de dados que um app antigo não entende."),
        ("Vou ter que baixar minhas publicações de novo?",
         "Normalmente sim — a mídia das publicações não faz parte do backup. Suas notas se reconectam a cada publicação assim que ela é baixada, então nada do que você escreveu se perde nesse meio-tempo."),
        ("Quanto tempo leva no total?",
         "Alguns minutos. Criar o backup leva segundos, mover o arquivo depende do método e a restauração é rápida. O mais demorado é baixar as publicações de novo, e isso pode acontecer em segundo plano."),
        ("Dá para fazer isso sem Wi-Fi?",
         "A transferência em si sim, por AirDrop ou cabo. Baixar as publicações de novo no aparelho novo precisa de conexão."),
    ],
}

GUIDES_PT["jw-library-android-to-iphone"] = {
    "title": "Passar o JW Library do Android para o iPhone (sem perder notas)",
    "h1": "Passando o JW Library do Android para o iPhone ou iPad — sem perder nenhuma nota",
    "description": "O formato de backup .jwlibrary é idêntico no Android e no iOS. Como levar "
                   "suas notas, destaques e marcadores de uma plataforma à outra — e como "
                   "mesclar se os dois aparelhos têm notas.",
    "intro": [
        "Trocar entre Android e iPhone parece o caso difícil, e é o fácil. O JW Library grava o mesmo formato de backup em toda plataforma em que roda, então levar uma biblioteca de estudo do Android para o iOS é a mesma operação de levá-la entre dois aparelhos Android — sem conversão, sem escolher formato de exportação, sem nada se perder no caminho.",
        "Trocar de plataforma é o momento em que as pessoas temem perder anos de notas de "
        "estudo — os aplicativos de transferência do Android para o iPhone simplesmente "
        "ignoram os dados do JW Library. A boa notícia: o formato de backup do JW Library é "
        "idêntico no Android, no iPhone, no iPad e no Windows, então mudar de plataforma é só "
        "fazer um backup, transferir o arquivo e restaurar.",
    ],
    "steps": [
        ("Faça o backup no celular Android",
         "JW Library → Estudo Pessoal → menu de três pontos → Backup e Restauração → Criar um "
         "backup. Salve o arquivo .jwlibrary."),
        ("Envie o arquivo para o iPhone ou iPad",
         "E-mail, Google Drive, iCloud Drive — qualquer coisa que transfira um arquivo. Se o "
         "iOS renomeá-lo para .zip no caminho, renomeie de volta para .jwlibrary."),
        ("Restaure no aparelho novo",
         "Instale o JW Library, faça login e vá em Backup e Restauração → Restaurar e escolha "
         "o arquivo. Notas, destaques, marcadores, etiquetas e listas de reprodução chegam "
         "todos."),
    ],
    "sections": [
        ("Se o iPhone já tiver notas",
         "Restaurar substitui os dados do aparelho. Quando o aparelho novo já tem notas "
         "próprias, faça um backup dele também e mescle os dois backups em um só arquivo "
         "antes, em jwsync.org — a mesclagem junta as duas bibliotecas no seu navegador, sem "
         "enviar nada — e depois restaure o arquivo mesclado. Nada se perde de nenhum lado."),
        ("Os mesmos passos funcionam em qualquer direção",
         "Do iPhone para o Android, de um Android para outro, ao acrescentar um iPad como "
         "segundo aparelho de estudo ou ao migrar para o aplicativo do Windows — o arquivo de "
         "backup é a língua comum entre todos eles."),
        ("Por que o formato é idêntico nas duas plataformas",
         "O JW Library usa o mesmo formato de backup em tudo em que roda — Android, iOS, iPadOS e Windows. Um arquivo .jwlibrary é um ZIP contendo um banco de dados SQLite com as mesmas tabelas e o mesmo esquema, independentemente de qual aparelho o gravou. Não há etapa de conversão, nem dança de exportar e importar, nem nada específico de plataforma dentro do arquivo. Um backup do Android restaura num iPhone exatamente como um backup de iPhone restauraria."),
        ("A única parte que realmente muda",
         "Não o arquivo — só chegar até ele. No Android o backup é salvo numa pasta que você escolhe e pode ser movido com qualquer gerenciador de arquivos. No iPhone ele passa pelo menu de compartilhamento para Arquivos, AirDrop ou o que você preferir. O atrito que as pessoas encontram ao mudar de plataforma está sempre nessa etapa de manuseio, nunca na compatibilidade. E-mail, nuvem ou AirDrop funcionam igual; o arquivo chega inteiro ou não chega."),
        ("Cores de destaque, etiquetas e respostas de estudo",
         "Tudo sobrevive. As cores dos destaques são guardadas como um índice numérico — amarelo, verde, azul, rosa, laranja e roxo — e aparecem iguais em qualquer plataforma. Etiquetas e os vínculos entre etiquetas e notas vão junto, assim como as respostas digitadas nos campos de perguntas de estudo. O que você vê no iPhone depois de restaurar é o que tinha no aparelho Android."),
        ("Se o iOS não deixar você escolher o arquivo",
         "Salve o arquivo no app Arquivos primeiro e escolha a partir dali, em vez de escolher de um anexo de e-mail ou da prévia de um app de mensagem. Alguns apps entregam ao iOS uma cópia temporária de prévia em vez do arquivo real, e o JW Library não consegue abrir isso. Se o arquivo chegou como anexo, toque nele, escolha Salvar em Arquivos e restaure a partir de Arquivos."),
        ("Prepare o iPhone antes de restaurar",
         "Instale o JW Library pela App Store e atualize para a versão atual antes de restaurar qualquer coisa. Um backup gravado por uma versão mais nova pode usar um esquema de banco de dados que uma versão mais antiga não entende, e a restauração simplesmente será recusada. Não é preciso entrar em conta nenhuma: os dados de estudo pessoal estão no arquivo que você restaura, não numa conta."),
        ("Se você já começou a estudar no iPhone",
         "Faça um backup do iPhone primeiro. Restaurar o arquivo do Android por cima substituiria tudo o que você escreveu desde a troca. Mesclar os dois backups produz um arquivo com os dois conteúdos, que você então restaura — o histórico do Android e as notas novas do iPhone terminam na mesma biblioteca."),
        ("Mantendo os dois celulares em uso depois",
         "Tem gente que fica com o Android antigo como segundo leitor em vez de aposentá-lo. Funciona, mas os dois vão divergir assim que você anotar em ambos, porque não há sincronização entre eles. Se pretende usar os dois, conte com mesclar os backups de tempos em tempos em vez de supor que continuam alinhados."),
        ("Depois da mudança",
         "Dê tempo ao iPhone para baixar de novo as publicações que você mais usa e depois confira algumas anotadas para confirmar que chegou tudo — notas, cores de destaque, marcadores e etiquetas. Guarde o arquivo de backup do Android mesmo depois de a troca estar concluída: ele é um retrato datado da sua biblioteca, e guardá-lo não custa nada."),
    ],
    "faq": [
        ("Preciso de um computador para fazer isso?",
         "Não. A mudança inteira pode ser feita de celular para celular, por e-mail ou por um "
         "serviço de nuvem."),
        ("As cores dos meus destaques sobrevivem à mudança?",
         "Sim — os destaques mantêm as cores, as notas mantêm as etiquetas e os marcadores "
         "mantêm os seus lugares."),
        ("Preciso de um computador para isso?",
         "Não. AirDrop, e-mail ou qualquer app de armazenamento na nuvem move o arquivo direto entre os dois celulares."),
        ("Funciona ao contrário, de iPhone para Android?",
         "Sim, igualzinho. Os mesmos passos funcionam em qualquer direção, inclusive de e para o app de Windows."),
        ("O iPhone vai precisar das mesmas publicações baixadas?",
         "Sim, já que a mídia das publicações não faz parte de um backup. As notas se reconectam a cada publicação assim que ela é baixada."),
        ("Preciso ficar com o celular Android depois?",
         "Não, depois de conferir que as notas estão no iPhone. Confira algumas publicações anotadas antes de apagar ou entregar o aparelho antigo."),
        ("A transferência funciona para as respostas das perguntas de estudo?",
         "Sim. As respostas digitadas fazem parte dos dados de estudo pessoal e vão junto com todo o resto."),
        ("Existe risco de perder notas na mudança?",
         "Não se você guardar o backup do Android. A restauração grava no iPhone e nunca altera o arquivo que lê, então o original fica intacto como reserva. Guarde-o até confirmar que o iPhone tem tudo, e de preferência também depois: ele é um retrato datado da sua biblioteca."),
        ("E se o celular Android não criar o backup?",
         "Confira primeiro o espaço disponível, já que o app precisa de lugar para gravar o arquivo. Se o próprio app estiver falhando, atualizá-lo ou reiniciar o aparelho costuma resolver. Os dados continuam intactos enquanto você resolve isso."),
    ],
}

GUIDES_PT["backup-jw-library"] = {
    "title": "Como fazer backup do JW Library do jeito certo",
    "h1": "Como fazer backup do JW Library do jeito certo",
    "description": "Uma rotina de backup de 30 segundos: o que um arquivo .jwlibrary realmente contém, onde guardá-lo e por que vale a pena ter um atualizado mesmo quando nada deu errado.",
    "intro": [
        "Um backup leva meio minuto e vale a pena virar hábito, embora não exatamente pelo motivo que costumam dar. O próprio backup e restauração do JW Library já leva uma biblioteca para um aparelho novo muito bem, então um backup é menos um seguro do que a matéria-prima de tudo o mais que você queira fazer com seu estudo.",
        "Um arquivo .jwlibrary é a única forma que sua biblioteca assume fora do aplicativo. É o que você mescla quando estudou em dois aparelhos, o que você abre para ler, reetiquetar ou organizar anos de notas, o que você pesquisa por significado quando só lembra vagamente do que escreveu, e de onde tira um conjunto de notas quando quer mandar algumas para um amigo. Ter um atualizado é o que torna tudo isso possível.",
    ],
    "steps": [
        ("Crie o backup",
         "Abra o JW Library → Estudo Pessoal → menu de três pontos → Backup e Restauração → "
         "Criar um backup. Isso gera um arquivo .jwlibrary com cada nota, destaque, marcador "
         "e etiqueta."),
        ("Guarde em algum lugar fora do celular",
         "Mande por e-mail para você mesmo ou salve no Google Drive, no iCloud ou no OneDrive. "
         "Um backup que só existe no celular some junto com o celular."),
        ("Repita com regularidade",
         "Uma vez por mês é um bom padrão; antes de qualquer troca de aparelho, reset ou "
         "atualização do sistema é indispensável. Guarde as cópias antigas — os arquivos são "
         "pequenos, e um backup antigo já salvou muita gente."),
    ],
    "sections": [
        ("O erro comum: confiar no backup em nuvem do próprio celular",
         "Um backup do celular inteiro (Google One, backup de aparelho do iCloud) muitas vezes "
         "restaura uma cópia antiga dos dados do JW Library — ou nenhuma. O arquivo .jwlibrary "
         "é o único backup que você controla por completo e que pode levar de uma plataforma "
         "à outra. Trate o backup do celular como um bônus, não como o plano."),
        ("Acabou com dois backups diferentes?",
         "Acontece: um backup do celular, um mais antigo do tablet, cada um com notas únicas. "
         "Você nunca precisa escolher entre eles — mescle os dois em um arquivo completo em "
         "jwsync.org, de graça e com privacidade, direto no navegador."),
        ("O que o arquivo contém e o que não contém",
         "O backup guarda seus dados de estudo pessoal: notas, destaques e suas cores, marcadores, etiquetas e as respostas que você digitou nos campos de perguntas de estudo. Ele não guarda as publicações — nem Bíblias, nem revistas, nem livros, nem vídeos, nem áudio. É por isso que um backup de anos de estudo costuma ter só alguns megabytes, e por isso restaurar num aparelho novo deixa você baixando publicações enquanto cada nota que escreveu já está de volta no lugar."),
        ("Quantos backups manter",
         "Mais de um. A falha que custa as notas das pessoas raramente é um arquivo perdido — é um backup bom sobrescrito por um ruim, ou uma restauração feita no aparelho errado. Como os arquivos são pequenos, não há motivo para apagar os antigos: guarde-os datados numa pasta na nuvem. Um backup de seis meses atrás não perde o valor mesmo depois de você ter outros mais novos, porque tudo o que você apagou sem querer desde então ainda existe dentro dele."),
        ("Onde guardá-los",
         "Em qualquer lugar que não seja apenas o próprio aparelho. Uma pasta no Drive, iCloud, Dropbox ou OneDrive cobre o caso que mais importa — o aparelho ser perdido, roubado, resetado ou danificado. Mandar o arquivo por e-mail para você mesmo também funciona e ainda tem o efeito útil de datá-lo. O arquivo contém suas próprias notas de estudo, então trate-o com o mesmo cuidado de qualquer documento pessoal."),
        ("Conferir um backup antes de depender dele",
         "Um backup que você nunca abriu é uma suposição, não uma rede de segurança. Dá para abrir um arquivo .jwlibrary no navegador e ver exatamente quais notas, destaques e marcadores ele contém — uma checagem de trinta segundos que transforma a suposição em fato. Isso importa mais logo antes de algo irreversível: um reset de fábrica, uma troca, um conserto ou uma atualização grande do sistema."),
        ("Os momentos em que vale fazer backup",
         "Qualquer ponto em que o aparelho muda de mãos ou de estado: uma atualização do sistema, um reset de fábrica, um conserto ou troca de tela, uma troca por outro aparelho, ou repassar o aparelho para alguém. Some a isso o fim de qualquer coisa que você odiaria refazer — um congresso, uma assembleia, uma temporada preparando um discurso. Backups são rápidos e baratos, então o hábito útil é amarrá-los a acontecimentos, e não ao calendário."),
        ("Um backup do celular não é um backup do JW Library",
         "Google One, um backup de aparelho do iCloud ou a ferramenta de migração do fabricante operam no nível do aparelho e tratam dados privados de app de forma inconsistente. É comum a pessoa descobrir que uma restauração completa do celular trouxe de volta os apps e as configurações, mas não as notas de estudo, ou trouxe uma versão de semanas atrás. O arquivo .jwlibrary é a única cópia cujo conteúdo você controla e pode conferir, então trate o backup do celular como bônus, não como plano."),
        ("Transformar isso num hábito que se sustenta",
         "A rotina que realmente pega é a amarrada a algo que você já faz: fazer backup ao terminar de preparar a semana, ou no mesmo dia em que cuida de outras tarefas periódicas. Salve sempre na mesma pasta para os arquivos se acumularem num lugar só, e deixe os antigos lá. Uma pasta de backups datados de anos atrás é a forma mais robusta que isso pode ter, e mantê-la leva segundos por semana."),
    ],
    "faq": [
        ("Qual é o tamanho de um arquivo de backup?",
         "Normalmente alguns megabytes, mesmo em bibliotecas muito grandes — cabe num anexo "
         "de e-mail."),
        ("Criar um backup muda alguma coisa no meu celular?",
         "Não. Ele só grava o arquivo; sua biblioteca fica intacta."),
        ("O backup inclui minhas publicações baixadas?",
         "Não. Só os dados de estudo pessoal. As publicações são baixadas de novo no aparelho novo, e suas notas se reconectam a elas automaticamente."),
        ("Dá para abrir um backup e ver o que tem dentro?",
         "Sim. Você pode abrir um arquivo .jwlibrary no navegador e percorrer todas as notas, destaques e marcadores que ele guarda, sem instalar nada e sem o arquivo sair do seu aparelho."),
        ("Backups têm validade?",
         "Não. Um arquivo .jwlibrary continua restaurável indefinidamente. Restaure numa versão atual do JW Library em vez de numa antiga, já que o app lê formatos de backup mais antigos, mas não mais novos."),
        ("Devo fazer backup antes de cada reunião?",
         "Não precisa. Amarre os backups aos acontecimentos que poderiam custar dados — atualizações, consertos, aparelhos novos — mais um ritmo regular compatível com quanto estudo você se incomodaria em refazer."),
        ("Vale a pena guardar backups de anos atrás?",
         "Vale. Eles são pequenos, e tudo o que você apagou sem querer desde então ainda existe dentro deles."),
    ],
}

GUIDES_PT["jw-library-restore-replaced-notes"] = {
    "title": "A restauração do JW Library substituiu suas notas? Como recuperá-las",
    "h1": "A restauração substituiu suas notas? Veja como juntar os dois backups",
    "description": "A restauração do JW Library é uma troca completa, não uma mesclagem — as "
                   "notas feitas depois da data do backup parecem ter sumido. Se você ainda "
                   "tem os dois arquivos de backup, nada foi perdido. Veja a solução.",
    "intro": [
        "É um momento horrível: você restaura um backup em um aparelho que já tinha notas e a "
        "restauração substitui tudo — as notas feitas desde aquele backup parecem ter sumido. "
        "Isso acontece porque o Backup e Restauração do JW Library é uma troca completa, não "
        "uma mesclagem.",
        "O ponto principal: se o trabalho mais recente ainda existe em algum arquivo de "
        "backup, nada foi realmente perdido. A solução é mesclar os dois backups em vez de "
        "escolher entre eles.",
    ],
    "steps": [
        ("Pare — não restaure de novo",
         "Cada restauração substitui os dados atuais do aparelho. Faça uma pausa antes que "
         "mais alguma coisa desapareça."),
        ("Faça um backup do aparelho como ele está agora",
         "Estudo Pessoal → Backup e Restauração → Criar um backup. Isso preserva o estado "
         "atual, seja ele qual for."),
        ("Encontre o backup com as notas que sumiram",
         "O arquivo .jwlibrary que você usou para restaurar, ou um anterior — procure no seu "
         "e-mail, no Drive, no iCloud e na pasta de downloads."),
        ("Mescle os dois arquivos em jwsync.org",
         "Carregue os dois backups. O JW Sync combina todas as notas, destaques, marcadores e "
         "etiquetas dos dois em um novo arquivo — no seu navegador, sem enviar nada. Versões "
         "conflitantes da mesma nota aparecem lado a lado para você escolher."),
        ("Restaure o arquivo mesclado",
         "Backup e Restauração → Restaurar com o .jwlibrary mesclado. Os dois conjuntos de "
         "notas estão de volta no aparelho."),
    ],
    "sections": [
        ("E se não houver backup das notas mais recentes?",
         "Se a única cópia das notas mais recentes estava no aparelho e uma restauração já "
         "passou por cima delas, o próprio JW Library não oferece como desfazer. É por isso "
         "que o passo 2 acima — fazer um backup do estado atual antes de qualquer coisa — "
         "importa tanto sempre que algo parecer errado. Daqui para a frente, a rotina de "
         "mesclar primeiro torna o problema estruturalmente impossível."),
    ],
    "faq": [
        ("A mesclagem vai duplicar as notas que existem nos dois backups?",
         "Não — itens idênticos são detectados e mantidos uma única vez. Só versões realmente "
         "diferentes da mesma nota são separadas para revisão."),
        ("Isso resolve um backup que não restaura de jeito nenhum?",
         "Normalmente isso é dano no arquivo, e não sobrescrita — veja abaixo o guia sobre "
         "consertar um backup danificado."),
    ],
}

GUIDES_PT["fix-corrupted-jw-library-backup"] = {
    "title": "Consertar um backup danificado do JW Library que não restaura",
    "h1": "Consertando um backup danificado do JW Library com o Doutor da Biblioteca",
    "description": "O JW Library se recusa a restaurar seu arquivo .jwlibrary? O Doutor da "
                   "Biblioteca examina o backup no seu navegador, conserta os problemas mais "
                   "comuns e entrega uma cópia limpa que restaura.",
    "intro": [
        "Um backup que não restaura não é necessariamente um backup que perdeu suas notas. A maioria dos arquivos que as pessoas descrevem como corrompidos está estruturalmente em ordem e é recusada por um motivo que tem conserto, ou foi danificada na transferência de um jeito que uma cópia nova resolve. Vale percorrer as causas antes de dar o arquivo por perdido.",
        "Às vezes o JW Library rejeita um arquivo de backup — a restauração falha, dá erro ou "
        "o arquivo não abre. Causas comuns: um download interrompido, um serviço de nuvem que "
        "estragou o arquivo, uma extensão alterada no caminho ou inconsistências internas "
        "acumuladas ao longo de anos de uso.",
        "O JW Sync traz o Doutor da Biblioteca, um verificador que examina um arquivo "
        ".jwlibrary e conserta os problemas mais comuns — inteiramente no seu navegador, sem "
        "que o arquivo jamais saia do seu aparelho.",
    ],
    "steps": [
        ("Abra o JW Sync e carregue o arquivo problemático",
         "Acesse jwsync.org e carregue o arquivo .jwlibrary que não restaura. (Se o arquivo "
         "chegou renomeado para .zip, renomeie de volta para .jwlibrary primeiro — só isso já "
         "resolve muitos casos.)"),
        ("Rode o exame do Doutor da Biblioteca",
         "O Doutor examina a estrutura interna do backup e lista, em linguagem simples, o que "
         "encontrou — de esquisitices inofensivas a dano de verdade."),
        ("Aplique os reparos",
         "Um toque conserta o que é reparável. O Doutor nunca altera seu arquivo original; "
         "ele gera uma cópia limpa, então o original fica intacto como reserva."),
        ("Baixe e restaure o arquivo consertado",
         "Restaure o .jwlibrary limpo por Backup e Restauração → Restaurar no JW Library."),
    ],
    "sections": [
        ("O Doutor também roda em toda mesclagem",
         "As mesmas verificações acontecem automaticamente dentro do motor de mesclagem, "
         "então um backup mesclado sempre sai limpo — mesmo quando um dos arquivos de entrada "
         "tinha problemas que você nem sabia que existiam."),
        ("Quando um arquivo não tem conserto",
         "Se o arquivo foi cortado a ponto de os dados simplesmente não estarem mais nele, "
         "nenhuma ferramenta consegue inventá-los de volta. O Doutor vai dizer isso "
         "honestamente em vez de entregar um arquivo duvidoso — e esse é o sinal para "
         "procurar uma cópia anterior no e-mail, no Drive ou no iCloud, o que também explica "
         "por que vale a pena guardar backups antigos."),
        ("O que corrompido normalmente significa",
         "Na prática, raramente são dados danificados. As causas comuns são um arquivo truncado na transferência — cortado por um envio que falhou ou por um app de mensagem que o comprimiu — ou um arquivo íntegro que contém inconsistências internas que o app recusa. Como um .jwlibrary é um ZIP envolvendo um banco de dados SQLite, o problema pode estar em qualquer das duas camadas, e elas pedem soluções diferentes. Um arquivo truncado não tem conserto e precisa ser obtido de novo; um banco de dados inconsistente normalmente tem."),
        ("O que uma verificação realmente confere",
         "Uma verificação confirma que o arquivo compactado abre, que o userData.db é um banco SQLite legível que passa numa checagem de integridade, que o esquema corresponde ao que o JW Library espera e que o manifesto concorda com o banco que descreve — inclusive o hash que o app usa para confirmar que o arquivo não foi alterado. Uma divergência entre o manifesto e o banco é um dos motivos mais comuns de um backup tecnicamente correto ser recusado na restauração, e tem conserto direto."),
        ("Linhas órfãs normalmente são inofensivas",
         "Uma verificação de um backup real vai frequentemente relatar linhas que apontam para algo que não está mais presente — um destaque apontando para um lugar de uma publicação que mudou, por exemplo. Os próprios backups do JW Library rotineiramente contêm centenas dessas e restauram sem reclamação. Elas são consequência normal de publicações serem atualizadas com o tempo, não indício de dano, e limpá-las não é necessário para o arquivo funcionar."),
        ("Resgatar notas de um arquivo que não restaura",
         "Mesmo quando um backup não pode ser consertado o bastante para o JW Library aceitá-lo, as notas lá dentro muitas vezes continuam legíveis. Abrir o arquivo no navegador deixa você ver e copiar o texto das notas direto, o que transforma um arquivo inutilizável em material de estudo recuperado. Se você tiver um segundo backup, mais antigo, que restaura, o conteúdo legível do danificado pode ser reunido a ele em vez de redigitado."),
        ("Quando a restauração falha sem erro claro",
         "O JW Library muitas vezes recusa um arquivo sem explicar por quê. As causas mais frequentes são um manifesto cujo hash não bate mais com o banco que ele descreve, um arquivo truncado na transferência, ou um backup gravado por uma versão do app mais nova do que aquela em que você está restaurando. A primeira tem conserto, a segunda exige buscar o arquivo de novo na origem e a terceira se resolve atualizando o app antes de restaurar."),
        ("Evitar isso da próxima vez",
         "Quase todo dano acontece no trajeto. Mova backups como arquivos e não por nada que possa recomprimi-los, e prefira nuvem, AirDrop ou cabo a apps de mensagem. Depois de transferir, confirme que o tamanho bate com o original — um arquivo bem menor do que o que você enviou foi truncado, e conserto nenhum traz de volta bytes que nunca chegaram."),
        ("Se nada funcionar",
         "Um arquivo que não pode ser consertado ainda pode ser legível, e ler já costuma bastar — o texto das notas é recuperado direto mesmo quando o JW Library recusa o arquivo. Combine isso com qualquer backup mais antigo que restaure e normalmente você termina com a maior parte da biblioteca intacta. Antes de dar um arquivo por inutilizável, abra e veja o que tem dentro."),
    ],
    "faq": [
        ("Meus dados são enviados para o exame?",
         "Não. O exame, os reparos e a exportação acontecem todos localmente, no navegador."),
        ("Ele recupera notas apagadas dentro do JW Library?",
         "Não — ele conserta a estrutura do arquivo. Notas apagadas no aplicativo antes de o "
         "backup ser feito não estão no arquivo para serem recuperadas."),
        ("Consertar o arquivo perde alguma nota?",
         "Os consertos trabalham numa cópia e tratam de problemas estruturais, não de conteúdo. Seu arquivo original nunca é modificado, então continua disponível se você quiser recomeçar."),
        ("Por que meu backup corrompeu?",
         "Na maioria das vezes o arquivo foi alterado no trajeto — enviado por um app que o comprimiu ou truncou, ou um envio que não terminou. Transferir de novo a partir da origem costuma resolver."),
        ("Uma verificação recupera notas que apaguei dentro do JW Library?",
         "Não. Uma vez apagada no app e feito um backup novo, a nota não está mais naquele arquivo. Um backup anterior à exclusão ainda a conterá."),
        ("Dá para saber pelo tamanho do arquivo se ele está truncado?",
         "Muitas vezes sim. Compare com o original, se ainda tiver; uma diferença grande significa que a transferência não terminou."),
        ("Um backup que abre no navegador com certeza vai restaurar?",
         "Não é garantia, mas é forte indício de que o arquivo compactado e o banco estão em ordem, o que descarta as falhas mais comuns."),
    ],
}

GUIDES_PT["edit-jw-library-notes"] = {
    "title": "Ver e editar as notas do JW Library no navegador",
    "h1": "Veja, pesquise e edite suas notas do JW Library — Explorador de Estudo",
    "description": "Abra qualquer backup .jwlibrary no navegador para folhear, pesquisar, "
                   "editar, reetiquetar, recolorir e limpar em lote suas notas, destaques e "
                   "marcadores do JW Library. Nada é enviado.",
    "intro": [
        "O JW Library foi feito para tomar notas, não para administrar milhares delas. O "
        "Explorador de Estudo abre qualquer backup .jwlibrary direto no navegador e o "
        "transforma em um gerenciador de biblioteca pesquisável e editável — notas, destaques "
        "e marcadores em um só lugar, sem enviar nada a lugar nenhum.",
    ],
    "steps": [
        ("Carregue um backup",
         "Crie um backup no JW Library (Estudo Pessoal → Backup e Restauração → Criar um "
         "backup), depois abra jwsync.org e carregue o arquivo no Explorador de Estudo."),
        ("Folheie e pesquise tudo",
         "Três abas — Notas, Destaques, Marcadores — com busca em texto completo e filtros de "
         "cor, etiqueta e publicação. Uma aba de Respostas de Estudo também mostra as "
         "respostas que você escreveu nas publicações."),
        ("Edite ali mesmo",
         "Abra qualquer nota para editar o título e o conteúdo com formatação (negrito, "
         "itálico, sublinhado, listas), mudar a cor do destaque e acrescentar ou remover "
         "etiquetas. Marcadores e cores de destaque se editam do mesmo jeito."),
        ("Faça a limpeza em lote",
         "Selecione várias notas de uma vez para reetiquetar, recolorir ou apagar em "
         "conjunto — com desfazer e refazer completos, então um deslize nunca é fatal. Você "
         "também pode extrair um intervalo de datas de notas para um backup novo ou copiar as "
         "notas em Markdown."),
        ("Exporte sua biblioteca editada",
         "Baixe o .jwlibrary editado e restaure no JW Library. Suas mudanças agora estão no "
         "aparelho."),
    ],
    "sections": [
        ("Por que editar no navegador em vez do aplicativo?",
         "Escala. Renomear uma etiqueta em 300 notas, recolorir todos os destaques amarelos "
         "de uma publicação ou apagar anos de marcadores esquecidos são minutos de trabalho "
         "aqui e horas de toques no aplicativo. O arquivo exportado é um backup comum, que o "
         "JW Library restaura como qualquer outro."),
    ],
    "faq": [
        ("Editar mexe no meu backup original?",
         "Não — as edições são feitas em uma cópia dentro do navegador e salvas em um novo "
         "arquivo exportado. O original continua como estava."),
        ("Existe um limite de tamanho da biblioteca?",
         "Bibliotecas muito grandes são paginadas para a navegação continuar rápida; a busca "
         "e os filtros funcionam sobre tudo."),
    ],
}

GUIDES_PT["search-jw-library-notes"] = {
    "title": "Pesquisar notas do JW Library por sentido — Pergunte à sua biblioteca",
    "h1": "Pergunte à sua biblioteca: pesquise suas notas do JW Library por sentido",
    "description": "Busca semântica para as suas notas do JW Library: encontre aquela nota "
                   "que você mal lembra descrevendo-a, mesmo sem recordar as palavras exatas. "
                   "No próprio aparelho, funciona off-line, com privacidade.",
    "intro": [
        "Quem tem anos de notas conhece o problema: você lembra de ter escrito sobre suportar "
        "provações com alegria, mas a nota não contém a palavra “perseverança”, então a busca "
        "por palavra-chave não acha nada. O Pergunte à sua biblioteca pesquisa por sentido: "
        "descreva a ideia e ele traz as notas mais próximas, sejam quais forem as palavras.",
        "Tudo roda no seu aparelho: o modelo de linguagem é baixado uma vez para o navegador "
        "e depois funciona off-line, com aceleração por WebGPU onde ela existe. Suas notas "
        "nunca são enviadas a lugar nenhum.",
    ],
    "steps": [
        ("Carregue um backup no Explorador de Estudo",
         "Em jwsync.org, carregue seu arquivo .jwlibrary e abra a aba Perguntar."),
        ("Deixe o modelo se preparar, uma única vez",
         "No primeiro uso, o modelo local é baixado e indexa as suas notas. Isso acontece uma "
         "vez; depois disso funciona na hora, mesmo off-line."),
        ("Pergunte com as suas palavras",
         "Digite o que você lembra — “aquela nota sobre ter paciência com os novos no "
         "ministério”, “encorajamento para pioneiros desanimados” — e as notas mais próximas "
         "aparecem, ordenadas por sentido."),
    ],
    "sections": [
        ("Como isso difere da busca comum",
         "A busca por palavra-chave compara letras; a busca semântica compara ideias. Uma "
         "consulta sobre “ansiedade” também encontra notas escritas com “preocupação”, "
         "“ansiedades da vida” ou a citação de um texto bíblico sobre o tema. Os dois tipos "
         "de busca estão no Explorador de Estudo — eles se complementam."),
        ("Privado por concepção",
         "Isto não é um serviço de IA na nuvem. O modelo roda dentro da aba do seu navegador, "
         "o índice fica no seu aparelho e fechar a aba encerra tudo. Nada sobre as suas notas "
         "sai da sua máquina."),
    ],
    "faq": [
        ("Precisa de um aparelho potente?",
         "Um celular ou notebook moderno dá conta bem; em aparelhos com WebGPU é mais rápido. "
         "Há uma escolha de tamanhos de modelo para combinar com o seu equipamento."),
        ("Funciona no meu idioma?",
         "Sim — a busca funciona nos idiomas em que as suas notas foram escritas, e a "
         "interface está traduzida em todos os 12 idiomas que o JW Sync tem."),
    ],
}

GUIDES_PT["jw-library-study-stats"] = {
    "title": "Veja suas estatísticas de estudo do JW Library: sequências, mapas e prêmios",
    "h1": "Suas estatísticas de estudo do JW Library: sequências, mapas de calor, cobertura e prêmios",
    "description": "Transforme um backup do JW Library em estatísticas de estudo privadas — "
                   "totais, mapa de calor de atividade, sequências, cobertura da Bíblia nos "
                   "66 livros, um perfil de personalidade de estudo e cerca de 200 prêmios.",
    "intro": [
        "Seu arquivo de backup registra em silêncio anos de história de estudo — quando você "
        "faz notas, o que destaca, quais livros já percorreu. A página de Estatísticas de "
        "Estudo lê um backup .jwlibrary e transforma essa história em um painel privado, "
        "calculado inteiramente no seu navegador.",
    ],
    "steps": [
        ("Crie um backup",
         "No JW Library: Estudo Pessoal → Backup e Restauração → Criar um backup."),
        ("Abra a página de Estatísticas de Estudo",
         "Acesse jwsync.org/highlights.html e carregue o arquivo."),
        ("Explore a sua história de estudo",
         "Totais em destaque, visões por ano de serviço e de todos os tempos, crescimento ano "
         "a ano — e, mais abaixo, as partes divertidas."),
    ],
    "sections": [
        ("O que você vai ver",
         "Um mapa de calor de atividade com a sua sequência mais longa e a atual; ritmo "
         "semanal, horas e meses mais movimentados; cobertura da Bíblia nos 66 livros, com a "
         "divisão entre as Escrituras Hebraicas e Gregas; uma roda de cores dos destaques, um "
         "histograma da profundidade das notas e uma nuvem de palavras; um relógio de estudo "
         "de 24 horas e um radar de sazonalidade."),
        ("Perfil, jornada e prêmios",
         "Um Perfil de Estudo com seis traços (Constância, Diligência, Profundidade, "
         "Amplitude, Reflexão e Firmeza) e uma “Assinatura de Estudo”; uma Jornada de Estudo "
         "de 60 níveis em 12 patamares com nome; e cerca de 200 prêmios, do Comum ao "
         "Lendário, incluindo medalhas que reconhecem o conteúdo. Um Cartão Compartilhável "
         "resume o seu ano sem expor nenhuma nota."),
        ("Um motivo diário para voltar",
         "O painel Retomar mostra notas que você escreveu neste mesmo dia em anos anteriores "
         "e monta uma revisão espaçada e tranquila — um pouco, com frequência, é o que faz o "
         "estudo ficar."),
    ],
    "faq": [
        ("Alguma coisa disso é enviada?",
         "Não. O backup é lido no seu navegador; as estatísticas nunca saem do seu aparelho."),
        ("As estatísticas se atualizam sozinhas?",
         "Elas refletem o backup que você carregou — crie um backup novo para ver "
         "estatísticas novas."),
    ],
}

GUIDES_PT["share-jw-library-notes"] = {
    "title": "Como compartilhar notas do JW Library com um amigo",
    "h1": "Como compartilhar notas do JW Library com um amigo — sem servidor",
    "description": "Envie notas escolhidas do JW Library (com os destaques delas) a um amigo "
                   "em um arquivo pequeno — sem servidor e sem conta. Quem recebe as junta "
                   "às suas sem sobrescrever nada.",
    "intro": [
        "O JW Library não tem como dar a outra pessoa uma cópia de notas específicas. Mandar "
        "o backup inteiro funcionaria — mas entrega tudo, e restaurá-lo apagaria a biblioteca "
        "de quem recebe. O compartilhamento de notas do JW Sync resolve as duas coisas: você "
        "escolhe exatamente quais notas compartilhar, e quem recebe as acrescenta sem perder "
        "nada.",
    ],
    "steps": [
        ("Escolha as notas que vai compartilhar",
         "Na página de compartilhamento, em jwsync.org/share.html, carregue seu backup e "
         "selecione as notas — algumas de uma única palestra, ou tudo o que está sob uma "
         "etiqueta com um clique, pelo filtro de etiquetas do seletor. Os destaques ligados a "
         "essas notas vão junto."),
        ("Envie o arquivo de compartilhamento",
         "O JW Sync gera um arquivo pequeno contendo só as notas selecionadas. Envie pelo "
         "canal que preferir — aplicativo de mensagens, e-mail, AirDrop. Não há servidor nem "
         "conta; o arquivo é a troca inteira."),
        ("Quem recebe faz a junção",
         "Seu amigo abre a mesma página, carrega o arquivo compartilhado junto com o próprio "
         "backup e recebe um novo backup com as suas notas acrescentadas. As notas dele nunca "
         "são sobrescritas — se uma nota compartilhada conflitar com uma dele, ele escolhe "
         "como ela entra — e as notas importadas chegam com etiqueta, ficando fáceis de "
         "achar, revisar ou remover depois."),
    ],
    "sections": [
        ("Bons usos",
         "Passar uma pesquisa a um parceiro de estudo, compartilhar notas de reunião com "
         "quem faltou, dar a um novo publicador um conjunto inicial de notas sobre uma "
         "publicação ou levar as notas de um projeto específico a um familiar — tudo isso sem "
         "expor o resto de nenhuma das duas bibliotecas."),
    ],
    "faq": [
        ("Quem recebe precisa instalar o JW Sync?",
         "Nada é instalado dos dois lados — é uma página da web. Quem recebe só precisa do "
         "arquivo compartilhado e do próprio backup."),
        ("Posso cancelar o compartilhamento ou fazer o arquivo expirar?",
         "O arquivo é um arquivo comum que você enviou — não existe cópia em servidor para "
         "expirar. Compartilhe só o que você compartilharia em qualquer mensagem."),
    ],
}

GUIDES_PT["bible-reading-plan"] = {
    "title": "Um plano diário de leitura da Bíblia com as suas notas ao lado",
    "h1": "Companheiro de Leitura: um plano de leitura da Bíblia com as suas notas ao lado",
    "description": "Um calendário diário e privado de leitura da Bíblia que mostra as notas e "
                   "os destaques que você fez nos capítulos de hoje. Escolha o ritmo, mantenha "
                   "a sequência e veja a grade dos 66 livros se preencher.",
    "intro": [
        "Muitos aplicativos oferecem um calendário de leitura da Bíblia. O Companheiro de "
        "Leitura faz algo que nenhum deles consegue: como ele lê o seu próprio backup "
        ".jwlibrary, a leitura de hoje chega com as notas e os destaques que você mesmo fez "
        "naqueles exatos capítulos — “você destacou quatro versículos no Salmo 37 há dois "
        "anos”. Ler pela lente da sua própria história de estudo, tudo no seu aparelho.",
    ],
    "steps": [
        ("Escolha uma ordem e um ritmo",
         "Leia na ordem da Bíblia ou em ordem cronológica aproximada; termine em 3 meses, 6 "
         "meses, 1 ano, 2 anos, ou defina o seu próprio ritmo de capítulos por dia — com uma "
         "prévia ao vivo de “você terminaria por volta de…”."),
        ("Leia a porção de hoje",
         "Cada capítulo fica a um toque de distância e abre direto no JW Library ou na "
         "BIBLIOTECA ONLINE Watchtower, no seu idioma. Marque os capítulos conforme avança."),
        ("Traga as suas notas junto (opcional)",
         "Carregue um backup em qualquer ferramenta do JW Sync e as suas notas e a contagem "
         "de destaques aparecem logo abaixo dos capítulos de hoje."),
        ("Veja o progresso crescer",
         "Uma grade dos 66 livros vai se preenchendo conforme você lê, com uma barra de "
         "capítulos lidos, uma previsão de ritmo e marcos para concluir cada livro, as "
         "Escrituras Hebraico-Aramaicas, as Escrituras Gregas — e a Bíblia inteira."),
    ],
    "sections": [
        ("Sequências sem culpa",
         "Concluir um dia faz a sua sequência crescer; perder um dia apenas muda a data "
         "prevista para terminar. Não existe pilha de atrasados — o plano se dobra à sua vida "
         "em vez de repreender você."),
    ],
    "faq": [
        ("Preciso carregar um backup para usar?",
         "Não — o plano, as sequências e o progresso funcionam sozinhos. O backup só "
         "acrescenta as suas notas pessoais à leitura de cada dia."),
        ("Meu progresso de leitura é privado?",
         "Sim. O progresso fica no navegador, no seu aparelho — não há conta e nada é "
         "enviado."),
    ],
}

GUIDES_PT["open-jwlibrary-file"] = {
    "title": "O que é um arquivo .jwlibrary e como abri-lo?",
    "h1": "O que é um arquivo .jwlibrary — e como abrir um em qualquer aparelho",
    "description": "Um arquivo .jwlibrary é o seu backup do JW Library: um único arquivo com "
                   "cada nota, destaque, marcador e etiqueta. Veja o que há dentro dele e "
                   "como abri-lo e lê-lo.",
    "intro": [
        "Um arquivo .jwlibrary parece fechado, e não é. Ele é um arquivo ZIP comum em volta de um banco de dados SQLite comum, o que significa que você consegue ler o seu próprio backup — ver exatamente quais notas, destaques e marcadores ele guarda — sem o JW Library e sem instalar absolutamente nada.",
        "Quando você faz backup do JW Library, recebe um arquivo terminado em .jwlibrary. É um "
        "pacote único e portátil que contém tudo do seu estudo pessoal — notas, destaques, "
        "marcadores, etiquetas e listas de reprodução — em um banco de dados compacto. Não é "
        "um documento que se abre no Word ou num leitor de PDF; ele foi feito para ser "
        "restaurado de volta no JW Library.",
        "Mas você não precisa restaurá-lo só para dar uma olhada dentro. O JW Sync abre um "
        "arquivo .jwlibrary direto no seu navegador, para você ler, pesquisar e editar o "
        "conteúdo sem mexer no celular.",
    ],
    "steps": [
        ("Consiga um arquivo .jwlibrary",
         "Ele é criado no JW Library: Estudo Pessoal → menu de três pontos → Backup e "
         "Restauração → Criar um backup. É desse arquivo que estamos falando."),
        ("Abra no JW Sync",
         "Acesse jwsync.org e carregue o arquivo no Explorador de Estudo. Ele abre na hora, "
         "no seu aparelho — nada é enviado."),
        ("Leia e trabalhe com ele",
         "Folheie notas, destaques e marcadores; pesquise em tudo; edite, reetiquete ou "
         "exporte. Quando terminar, você pode restaurar o arquivo (ou uma cópia editada) de "
         "volta no JW Library."),
    ],
    "sections": [
        ("O que existe de fato dentro do arquivo",
         "Tecnicamente, um arquivo .jwlibrary é um banco de dados SQLite compactado mais um "
         "manifesto. É por isso que renomeá-lo para .zip às vezes acontece por acidente no "
         "caminho — e por isso renomear de volta para .jwlibrary resolve. Você não precisa "
         "saber nada disso para usá-lo, mas isso explica por que o arquivo é pequeno, "
         "autossuficiente e idêntico no Android, no iPhone, no iPad e no Windows."),
        ("Abrindo no computador",
         "A mesma página jwsync.org funciona no navegador de um notebook ou desktop — útil "
         "para ler anos de notas numa tela grande ou fazer limpezas em lote que seriam "
         "cansativas no celular. Não há nada para instalar."),
        ("O que o arquivo realmente é",
         "Um arquivo .jwlibrary é um arquivo compactado ZIP com outra extensão. Dentro dele estão o userData.db — um banco de dados SQLite com suas notas, destaques, marcadores e etiquetas — e o manifest.json, um arquivo pequeno que descreve o backup e inclui um hash do banco que o JW Library usa para confirmar que o arquivo não foi alterado. Nada nele é proprietário ou criptografado; é um arquivo compactado padrão em volta de um banco de dados padrão."),
        ("Abrir sem o JW Library",
         "Você não precisa do app, nem de programa nenhum, para ler o seu próprio backup. Abrir o arquivo no navegador mostra todas as notas, destaques e marcadores que ele contém, com busca e filtros, e o arquivo nunca sai do seu aparelho — ele é lido localmente, não enviado. Esse é o jeito mais rápido de confirmar que um backup contém o que você acha que contém antes de um reset, uma troca ou uma restauração num celular novo."),
        ("Olhar dentro manualmente",
         "Se você tiver curiosidade, copie o arquivo, renomeie a cópia para .zip e abra com qualquer ferramenta de compactação. Você vai ver o userData.db e o manifest.json. Abrir o banco de dados exige um visualizador de SQLite, e as tabelas têm o nome do que guardam — Note, UserMark, Bookmark, Tag. Trabalhe sempre numa cópia: editar o banco na mão sem atualizar o hash do manifesto produz um arquivo que o JW Library vai se recusar a restaurar."),
        ("Editar com segurança",
         "Notas podem ser corrigidas, reetiquetadas, recoloridas ou apagadas fora do app, e o resultado exportado como um novo arquivo .jwlibrary que você restaura normalmente. A regra que mantém isso seguro é guardar o original: edite uma cópia, restaure o arquivo editado e, se algo não ficar como você esperava, o original intacto continua lá para voltar atrás."),
        ("Ler um backup no celular",
         "Você não precisa de computador. Abrir o arquivo no navegador do celular funciona igual, o que é útil quando o backup já está no aparelho e você quer confirmar o conteúdo antes de restaurar ou antes de apagar o aparelho. O arquivo é lido localmente, então isso funciona sem mais conexão do que a de carregar a página."),
        ("Por que o hash do manifesto importa",
         "O manifest.json registra um hash do userData.db. O JW Library o usa para confirmar que o banco não foi alterado desde que o backup foi gravado, então um arquivo cujo banco foi editado sem o hash ser recalculado é recusado na restauração. Esse é o motivo mais comum de um backup editado na mão parar de funcionar, e a razão de editar por uma ferramenta que regrava o manifesto ser mais seguro do que mexer no banco direto."),
        ("Para que isso serve",
         "Poder ler um backup muda quanto um backup vale. Você pode confirmar que um arquivo contém o que acha antes de apagar um celular, ver se vale a pena restaurar um arquivo antigo, achar uma nota que sabe que escreveu sem vasculhar o app, ou recuperar texto de um arquivo que o JW Library não aceita. Nada disso exige confiar o arquivo a ninguém — ele é lido no seu próprio aparelho."),
    ],
    "faq": [
        ("Posso abrir um arquivo .jwlibrary no Excel ou no Bloco de Notas?",
         "Não de forma útil — é um banco de dados, não uma planilha nem um arquivo de texto. "
         "Abra no JW Sync para lê-lo, ou exporte as suas notas em Markdown/texto pelo "
         "Explorador de Estudo."),
        ("É seguro abrir meu backup no navegador?",
         "É. O JW Sync lê o arquivo localmente, na aba do seu navegador; nada é enviado a "
         "servidor nenhum e o seu arquivo original nunca é alterado."),
        ("Dá para simplesmente renomear para .zip?",
         "Dá, numa cópia. Renomear não altera o conteúdo, e permite que qualquer ferramenta de compactação mostre o que há dentro."),
        ("Abrir o arquivo muda ele?",
         "Não. Ler um backup — no navegador ou numa ferramenta de compactação — o deixa idêntico byte a byte. Só salvar ou exportar produz um arquivo novo."),
        ("Preciso estar on-line?",
         "Só para carregar a página. O arquivo é lido no seu aparelho, não enviado, então suas notas nunca trafegam pela rede."),
        ("Dá para abrir um backup que outra pessoa me mandou?",
         "Dá, o formato não é preso a um aparelho ou conta. Se convém restaurá-lo é outra questão, já que restaurar substitui a sua própria biblioteca."),
        ("Preciso instalar algo para olhar dentro?",
         "Não. Um navegador basta para ler as notas; só a inspeção manual do banco de dados exige um visualizador de SQLite."),
    ],
}

GUIDES_PT["jw-library-windows-pc"] = {
    "title": "Fazer backup e mesclar o JW Library num PC com Windows",
    "h1": "Usando backups do JW Library num PC com Windows",
    "description": "Como fazer backup do JW Library no Windows e como mesclar o backup do PC "
                   "com o do celular e o do tablet para que notas, destaques e marcadores "
                   "fiquem juntos em todos os aparelhos.",
    "intro": [
        "O JW Library roda no Windows tanto quanto em celulares e tablets, e gera o mesmo "
        "arquivo de backup .jwlibrary. Isso significa que o seu PC pode fazer parte da mesma "
        "biblioteca de estudo que o seu celular — desde que você mescle os backups em vez de "
        "restaurar um por cima do outro.",
    ],
    "steps": [
        ("Faça o backup no Windows",
         "No aplicativo do JW Library para Windows, abra o menu, vá em Backup e Restauração e "
         "crie um backup. Salve o arquivo .jwlibrary em um lugar fácil de encontrar."),
        ("Faça backup do celular e do tablet também",
         "Em cada aparelho: Estudo Pessoal → menu de três pontos → Backup e Restauração → "
         "Criar um backup."),
        ("Mescle tudo em jwsync.org",
         "Abra jwsync.org em qualquer navegador do PC e carregue todos os arquivos de backup. "
         "O JW Sync combina as notas, os destaques, os marcadores e as etiquetas de cada "
         "aparelho em um único arquivo .jwlibrary mesclado — localmente, sem enviar nada."),
        ("Restaure o arquivo mesclado em todos os lugares",
         "Restaure o arquivo mesclado no aplicativo do Windows e em cada aparelho móvel. "
         "Agora o PC, o celular e o tablet carregam a biblioteca completa."),
    ],
    "sections": [
        ("Por que o PC é o lugar mais fácil para fazer isso",
         "Um navegador de computador torna muito mais rápido carregar vários arquivos, "
         "revisar a prévia da mesclagem e salvar o resultado do que ficar tocando na tela do "
         "celular. Muita gente mantém a rotina principal de mesclagem no computador e apenas "
         "restaura o arquivo mesclado de volta nos aparelhos móveis."),
    ],
    "faq": [
        ("O backup do Windows funciona com os backups de iPhone e Android?",
         "Sim — o formato .jwlibrary é idêntico em todas as plataformas, então um backup do "
         "Windows se mescla livremente com backups de celular e tablet."),
        ("Preciso instalar alguma coisa no PC?",
         "Não. O JW Sync é uma página da web; funciona no Edge, no Chrome ou no Firefox, sem "
         "nada para instalar."),
    ],
}

GUIDES_PT["recover-jw-library-notes-lost-phone"] = {
    "title": "Como recuperar notas do JW Library depois de perder ou quebrar o celular",
    "h1": "Recuperando notas do JW Library de um celular perdido, quebrado ou resetado",
    "description": "Perdeu o celular ou ele foi resetado com as notas do JW Library dentro? O "
                   "que dá para recuperar depende dos seus backups. Veja exatamente como "
                   "trazer suas notas de volta — e o que fazer da próxima vez.",
    "intro": [
        "Primeiro a resposta sincera, porque ela poupa sua leitura. Se existe um backup .jwlibrary em qualquer lugar fora do aparelho perdido, tudo o que está nele volta pela própria restauração do JW Library, e para essa parte você não precisa deste site. Se não existe backup nenhum, os dados de estudo pessoal não podem ser recuperados de forma alguma: eles vivem só no aparelho, e nenhuma ferramenta muda isso.",
        "Onde esta página ajuda de verdade é no caso intermediário, que é mais comum que os outros dois: você tem um backup, mas ele não conta a história toda. Pode ser de meses atrás, ou você já pode estar estudando no celular novo, então restaurá-lo sem mais nada trocaria um conjunto de notas por outro em vez de te devolver tudo.",
        "Juntar os dois é justamente o que o JW Library não faz, e é disso que trata o resto desta página. Mas primeiro, a procura: as pessoas costumam ter mais backups do que lembram ter feito.",
    ],
    "steps": [
        ("Procure em todo lugar onde possa haver um backup",
         "Verifique seu e-mail (pesquise por “jwlibrary” ou “backup”), o Google Drive, o "
         "iCloud Drive, o OneDrive, o Dropbox e a pasta de Downloads do computador. Backups "
         "são arquivos pequenos e é fácil esquecer que você os salvou."),
        ("Confira seus outros aparelhos",
         "Se você já usou o JW Library num tablet ou PC, ele tem os próprios dados de "
         "estudo — crie um backup dele agora mesmo para preservar o que ele guarda."),
        ("Restaure o que encontrar no celular novo",
         "Instale o JW Library no aparelho novo, depois Backup e Restauração → Restaurar e "
         "carregue o arquivo .jwlibrary. Suas notas, destaques e marcadores voltam."),
        ("Mescle se encontrar mais de um backup",
         "Aparelhos ou datas diferentes podem guardar cada um notas únicas. Não escolha só "
         "um — carregue todos em jwsync.org, mescle-os em um único arquivo completo e "
         "restaure esse. Nada fica para trás."),
    ],
    "sections": [
        ("Se não existir backup nenhum",
         "Seja honesto consigo mesmo desde cedo: se a única cópia das suas notas vivia no "
         "celular perdido e você nunca exportou um backup, o JW Library não guarda nenhuma "
         "cópia na nuvem para restaurar. Isso dói — e é exatamente por isso que o hábito "
         "abaixo importa tanto."),
        ("Para nunca mais passar por isso",
         "Programe um lembrete mensal de backup e guarde cada arquivo .jwlibrary fora do "
         "celular (mandar por e-mail para você mesmo já basta). O JW Sync pode até lembrar "
         "você e mesclar seus aparelhos com regularidade. Um arquivo que mora na sua caixa de "
         "entrada sobrevive a qualquer celular."),
        ("Onde já pode existir um backup",
         "Antes de concluir que não existe nenhum, verifique todo lugar onde um arquivo pode ter sido salvo: as pastas Downloads e Documentos de qualquer computador ao qual você já conectou o celular, os enviados do seu e-mail, apps de mensagem pelos quais você possa ter enviado o arquivo e toda conta de nuvem que você usa. É comum a pessoa ter criado um backup uma vez, meses atrás, e esquecido — e um backup de meses atrás ainda contém a grande maioria de uma biblioteca de estudo."),
        ("Restaurar num celular ou plataforma diferente",
         "O aparelho substituto não precisa ser igual ao perdido. Um backup de um celular Android restaura num iPhone e vice-versa, porque o formato é idêntico em Android, iOS, iPadOS e Windows. Instale o JW Library no aparelho novo, atualize para a versão atual e restaure em Estudo Pessoal → Backup e Restauração."),
        ("Se tudo que você tem é um backup antigo ou parcial",
         "Restaure mesmo assim. Recuperar a maior parte das suas notas não é prêmio de consolação — é o resultado. Se depois você encontrar um segundo backup diferente, os dois podem ser mesclados num arquivo com tudo dos dois, então restaurar o mais antigo agora não impede você de acrescentar mais adiante."),
        ("O que não pode ser recuperado",
         "Se não existir backup em nenhuma forma, os dados de estudo pessoal não podem ser recuperados. Eles ficam apenas no armazenamento privado do app dentro do aparelho, e nem o JW Library nem um backup de nuvem no nível do celular os preservam de forma confiável. Vale dizer isso com clareza, porque é a razão de a rotina deste site existir."),
        ("Verifique antes de apagar o aparelho remotamente",
         "Se o celular está perdido e não destruído, e você está pensando em apagá-lo remotamente, procure backups existentes primeiro: o apagamento é irreversível e elimina a última chance de alguém criar um. Se o aparelho está apenas extraviado e ainda acessível, não dá para criar um backup remotamente, mas os dados continuam intactos enquanto o celular não for apagado ou resetado."),
        ("Garantir que isso não aconteça duas vezes",
         "A razão de um celular perdido custar anos de estudo é que a única cópia estava no celular. Depois de restaurar num aparelho substituto, coloque um backup fora do aparelho no mesmo dia e repita num ritmo que você realmente vá manter. Os arquivos são pequenos o bastante para guardar todos indefinidamente sem custo."),
        ("Se realmente não houver backup nenhum",
         "Então a resposta honesta é que as notas não podem ser recuperadas, e é melhor ouvir isso do que continuar procurando. O que você pode fazer é que essa seja a última perda: instale o JW Library no substituto e, antes de ter reconstruído qualquer coisa que valha perder, crie um backup e guarde fora do aparelho. Dali em diante o mesmo acontecimento não custa nada."),
    ],
    "faq": [
        ("O JW Sync consegue recuperar notas de um celular que não tenho mais?",
         "Nenhuma ferramenta consegue — a recuperação depende de existir um arquivo de backup "
         "em algum lugar. A função do JW Sync é ler, consertar e mesclar os backups que você "
         "tem."),
        ("Meu backup é antigo — ainda vale a pena restaurar?",
         "Com certeza. Um backup antigo com a maior parte das suas notas é muito melhor do "
         "que começar do zero, e você pode mesclá-lo depois com qualquer coisa mais recente "
         "que encontrar."),
        ("O JW Library guarda uma cópia das minhas notas na nuvem?",
         "Não. Os dados de estudo pessoal ficam no aparelho, a menos que você crie um arquivo de backup."),
        ("Dá para recuperar notas de um celular com a tela quebrada?",
         "Às vezes — se o celular ainda liga e pode ser controlado, ou se uma assistência conseguir usar a tela, o JW Library ainda consegue criar um backup. Os dados estão intactos enquanto o armazenamento estiver."),
        ("Um backup antigo ainda restaura no app atual?",
         "Sim. O JW Library lê formatos de backup mais antigos. Atualize o app primeiro e restaure na versão atual."),
        ("Encontrei dois backups antigos — qual devo usar?",
         "Nenhum sozinho. Mescle-os: o resultado contém tudo dos dois, inclusive o que estava no mais antigo e já tinha sido apagado na época do mais recente."),
        ("Dá para ver o que tem num backup antes de restaurar?",
         "Dá. Abra o arquivo no navegador e percorra suas notas, destaques e marcadores primeiro, para saber o que você vai restaurar."),
    ],
}

GUIDES_PT["handle-merge-conflicts"] = {
    "title": "A mesma nota editada em dois aparelhos? Como lidar com conflitos de mesclagem",
    "h1": "Lidando com conflitos de mesclagem: a mesma nota editada em dois aparelhos",
    "description": "Quando você edita a mesma nota do JW Library de formas diferentes em dois "
                   "aparelhos, a mesclagem precisa escolher um vencedor. O Revisor de "
                   "Conflitos mostra as duas versões lado a lado para você decidir — nada se "
                   "perde.",
    "intro": [
        "A maior parte da mesclagem não dá trabalho nenhum — notas que só existem em um "
        "aparelho simplesmente se juntam. O único caso que exige uma decisão é um conflito de "
        "verdade: a mesma nota, editada de formas diferentes em dois aparelhos, de modo que "
        "os dois backups discordam sobre o que ela deve dizer. O JW Sync nunca adivinha em "
        "silêncio; ele passa a escolha para você.",
    ],
    "steps": [
        ("Carregue os dois backups",
         "Em jwsync.org, carregue os arquivos .jwlibrary dos dois aparelhos. O JW Sync os "
         "compara enquanto mescla."),
        ("Abra o Revisor de Conflitos",
         "Se alguma nota conflitar, o revisor lista as notas em questão. Tudo o que não "
         "conflitou já foi mesclado — este passo é só para os choques de verdade."),
        ("Compare lado a lado",
         "Cada conflito mostra as duas versões, com as diferenças destacadas palavra por "
         "palavra. A opção “Sugerir a melhor” pode escolher a versão mais completa por você, "
         "ou você escolhe qual manter — nota por nota."),
        ("Termine e restaure",
         "Depois que todos os conflitos estiverem resolvidos, baixe o arquivo mesclado e "
         "restaure. Os dois aparelhos agora concordam, com a versão que você escolheu de cada "
         "nota."),
    ],
    "sections": [
        ("Por que isso é melhor do que simplesmente ficar com a mais recente",
         "“A mais nova vence” apaga em silêncio edições que talvez você quisesse manter. "
         "Talvez a versão antiga tivesse um parágrafo que você removeu sem querer no outro "
         "aparelho. Ver as duas, palavra por palavra, significa que você nunca perde texto "
         "sem saber — que é justamente o objetivo de mesclar em vez de sobrescrever."),
        ("Como os conflitos aparecem, para começo de conversa",
         "Geralmente por editar off-line em dois aparelhos entre uma mesclagem e outra, ou "
         "por restaurar um backup antigo e depois acrescentar coisas a ele. Mesclar com "
         "regularidade mantém o número de conflitos pequeno e as diferenças frescas na "
         "memória."),
    ],
    "faq": [
        ("Vou ter que revisar centenas de conflitos?",
         "Raramente. Só conflitam as notas editadas de formas diferentes dos dois lados; "
         "notas novas, e notas alteradas em apenas um aparelho, se mesclam automaticamente. A "
         "maioria das mesclagens tem um punhado de conflitos ou nenhum."),
        ("Posso mudar de ideia depois de escolher?",
         "Pode — nada é gravado em nenhum aparelho até você restaurar o arquivo mesclado, e "
         "os seus backups originais nunca são alterados, então dá para refazer a mesclagem."),
    ],
}

GUIDES_PT["export-jw-library-notes"] = {
    "title": "Como exportar notas do JW Library para texto ou Markdown",
    "h1": "Exportando as suas notas do JW Library para texto, Markdown ou um backup novo",
    "description": "Tire as suas notas do JW Library de dentro do aplicativo: copie ou "
                   "exporte em Markdown/texto simples para usar em qualquer lugar, ou extraia "
                   "uma seleção para um novo backup .jwlibrary. Tudo no navegador.",
    "intro": [
        "Notas escritas no JW Library são fáceis de ler dentro do app e desajeitadas de usar em qualquer outro lugar — num documento, num esboço de discurso, no papel, ou nas mãos de alguém que não usa o app. Exportar resolve isso, e a decisão principal não é como exportar, mas quanto: uma exportação filtrada quase sempre é mais útil do que tudo de uma vez.",
        "Suas notas de estudo não deveriam ficar presas dentro de um aplicativo. Às vezes você "
        "as quer como texto simples — para colar num esboço de discurso, num documento ou no "
        "seu próprio aplicativo de anotações — e às vezes você quer um backup limpo contendo "
        "só uma parte. O Explorador de Estudo faz as duas coisas, lendo o seu backup "
        "inteiramente no navegador.",
    ],
    "steps": [
        ("Carregue seu backup",
         "Crie um backup no JW Library (Estudo Pessoal → Backup e Restauração → Criar um "
         "backup), depois abra jwsync.org e carregue-o no Explorador de Estudo."),
        ("Encontre as notas que você quer",
         "Use a busca junto com os filtros de cor, etiqueta e publicação para chegar "
         "exatamente às notas que procura — uma publicação, uma etiqueta, um assunto."),
        ("Copie ou exporte em Markdown/texto",
         "Copie as notas em Markdown ou texto simples para colar onde quiser. A formatação "
         "(negrito, itálico, listas) é preservada, então notas estruturadas continuam "
         "estruturadas."),
        ("Ou extraia para um backup novo",
         "Prefere um arquivo? Exporte uma seleção ou um intervalo de datas para um novo "
         "backup .jwlibrary — útil para arquivar um projeto ou entregar um conjunto "
         "específico de notas a outro aparelho."),
    ],
    "sections": [
        ("Por que exportar",
         "As notas são mais úteis quando podem viajar: para um documento com uma designação "
         "da reunião, para uma wiki pessoal, para uma impressão destinada a quem não usa o "
         "aplicativo. O Markdown preserva a estrutura e continua legível como texto simples "
         "em qualquer lugar."),
        ("Escolher um formato",
         "Texto simples é o mais portátil e cola limpo em qualquer documento ou e-mail. A saída formatada preserva a estrutura de notas longas e serve para imprimir ou compartilhar. Se você quiser as notas de volta dentro do JW Library depois — em outro aparelho, ou na biblioteca de outra pessoa — guarde o próprio arquivo .jwlibrary em vez de uma exportação de texto, já que só ele preserva os vínculos entre notas, destaques, etiquetas e o ponto exato da publicação a que estão ancorados."),
        ("Exportar só parte da sua biblioteca",
         "Uma exportação completa de anos de estudo raramente é o que você quer. Filtrar antes — por etiqueta, publicação, cor de destaque ou intervalo de datas — produz algo que você consegue de fato usar, como todas as notas etiquetadas para um discurso, ou tudo escrito durante um congresso. Os mesmos filtros que estreitam a visualização estreitam a exportação, então o que você vê é o que sai."),
        ("O que vai junto com o texto e o que não vai",
         "Uma exportação carrega suas palavras. Ela não carrega as âncoras que ligam uma nota a um parágrafo específico de uma publicação específica, porque essas referências só significam algo dentro do JW Library. Esse é o motivo prático para guardar backups também: uma exportação serve para ler, imprimir e compartilhar fora do app, enquanto um arquivo .jwlibrary é o que devolve as notas a uma biblioteca com o contexto intacto."),
        ("Reunir tudo para um discurso ou designação",
         "Esse é o motivo mais comum para exportar. Filtre pela etiqueta, publicação ou intervalo de datas em que o material está, confira o resultado e exporte só aquilo. O que você recebe é um único documento com as notas relevantes e as passagens que você destacou, na ordem em que aparecem, em vez de um despejo inadministrável da biblioteca inteira."),
        ("Compartilhar notas com outra pessoa",
         "Há duas coisas diferentes por trás de compartilhar. Se a outra pessoa quer ler suas notas, uma exportação de texto é o certo — abre em qualquer lugar e não precisa de programa especial. Se ela quer as notas dentro do próprio JW Library dela, ancoradas aos mesmos parágrafos e com as etiquetas e cores, então o que você quer é um arquivo .jwlibrary, porque uma exportação de texto não devolve nada ao app."),
        ("Guardar um arquivo que você ainda consiga ler daqui a muito tempo",
         "Exportações também valem por si mesmas. Uma cópia em texto simples das suas notas de estudo ainda vai abrir daqui a trinta anos em programas que ninguém escreveu ainda, e isso nenhum formato específico de app consegue prometer. Guardar os dois — o .jwlibrary para restaurar e uma exportação de texto para ler — custa quase nada e cobre os dois futuros."),
        ("Exportação ou backup — de qual você precisa",
         "Os dois respondem a perguntas diferentes. Uma exportação serve para usar suas notas fora do JW Library: ler, imprimir, citar, mandar para alguém. Um backup .jwlibrary serve para devolvê-las ao JW Library, neste aparelho ou em outro, com cada âncora, etiqueta e cor intactas. Nenhum substitui o outro, e não há razão para não ter os dois."),
    ],
    "faq": [
        ("Exportar altera as minhas notas no JW Library?",
         "Não. A exportação lê uma cópia do seu backup no navegador; o seu arquivo original e "
         "o seu aplicativo ficam intactos."),
        ("Dá para exportar tudo de uma vez?",
         "Dá — limpe os filtros para selecionar a biblioteca inteira, ou restrinja antes para "
         "exportar só uma parte."),
        ("Dá para levar minhas notas para o Word ou o Google Docs?",
         "Dá — exporte como texto e cole. O texto chega com a estrutura intacta e pode ser formatado a partir dali."),
        ("Os destaques são exportados junto com as notas?",
         "Sim, inclusive a passagem destacada e a cor dela, então uma cópia impressa mostra tanto o que você marcou quanto o que escreveu."),
        ("Dá para exportar tudo de uma vez?",
         "Dá, embora uma exportação filtrada costume ser mais útil. Tudo pode ser exportado numa passada só quando você quiser uma cópia completa."),
        ("Dá para exportar as respostas que digitei nas perguntas de estudo?",
         "Dá. As respostas digitadas fazem parte dos seus dados de estudo pessoal e podem ser exportadas junto com notas e destaques."),
        ("A exportação diz a que publicação cada nota pertence?",
         "Diz. A exportação identifica de onde veio cada nota, mesmo que a âncora por baixo só funcione dentro do JW Library."),
        ("Exportar muda alguma coisa na minha biblioteca?",
         "Não. Uma exportação lê seus dados e grava um arquivo separado; nada dentro do JW Library é alterado, movido ou removido."),
        ("Dá para exportar de um backup em vez do app?",
         "Dá. Um arquivo .jwlibrary pode ser aberto direto e ter suas notas exportadas, o que é útil quando as notas que você quer estão num backup antigo e não no aparelho atual."),
    ],
}

GUIDES_PT["organize-jw-library-tags"] = {
    "title": "Como organizar e limpar as etiquetas do JW Library",
    "h1": "Organizando suas etiquetas do JW Library: renomear, unir e limpar em lote",
    "description": "As etiquetas se multiplicam ao longo de anos de estudo. Renomeie uma "
                   "etiqueta em todas as notas, una duplicatas e remova as que você não usa "
                   "mais — em lote, no navegador, com desfazer completo.",
    "intro": [
        "As etiquetas são o jeito de encontrar notas depois — mas, passados alguns anos, elas "
        "se espalham. Você acaba com “Ministério”, “ministério” e “Serviço de campo” "
        "significando a mesma coisa, etiquetas que você criou uma vez e nunca mais usou, e "
        "uma nomenclatura inconsistente que torna a filtragem pouco confiável. O JW Library "
        "não dá jeito de consertar isso em escala. O Explorador de Estudo dá.",
    ],
    "steps": [
        ("Carregue seu backup no Explorador de Estudo",
         "Em jwsync.org, carregue o arquivo .jwlibrary. Filtre por etiqueta para ver todas "
         "elas e quantas notas cada uma tem."),
        ("Renomeie uma etiqueta em todas as suas notas",
         "Reetiquete em lote: renomeie a etiqueta uma vez e todas as notas que a usam são "
         "atualizadas — chega de editar nota por nota para corrigir uma grafia."),
        ("Una as duplicatas",
         "Reetiquete as notas de uma etiqueta duplicada para a etiqueta oficial e depois "
         "descarte a duplicata vazia. “Ministério” e “ministério” viram uma etiqueta só."),
        ("Remova as etiquetas que você não usa mais",
         "Selecione e apague em lote as etiquetas esquecidas. Tudo é reversível, então uma "
         "limpeza empolgada demais nunca é definitiva."),
        ("Exporte a biblioteca arrumada",
         "Baixe o .jwlibrary editado e restaure no JW Library. Suas etiquetas ficam "
         "consistentes em todo lugar."),
    ],
    "sections": [
        ("Um sistema de etiquetas que realmente ajuda",
         "Quando as etiquetas ficam consistentes, filtrar passa a ser confiável — um toque "
         "mostra todas as notas sobre um tema, em qualquer publicação. É a diferença entre "
         "etiquetas como bagunça e etiquetas como um índice de verdade do seu estudo."),
        ("Etiquetas consistentes tornam o compartilhamento coisa de dois cliques",
         "O seletor de notas da página de compartilhamento tem o próprio filtro de etiquetas, "
         "então uma etiqueta limpa também é o jeito mais rápido de mandar um conjunto de "
         "notas para alguém: escolha a etiqueta, toque em Selecionar tudo e crie o arquivo. "
         "Etiquetas desleixadas custam caro duas vezes — quando você procura notas e quando "
         "tenta compartilhá-las."),
    ],
    "faq": [
        ("Reetiquetar em lote mexe no texto da nota?",
         "Não — só muda quais etiquetas estão ligadas a ela. Os títulos e o conteúdo das suas "
         "notas continuam exatamente como você escreveu."),
        ("Existe como desfazer se eu errar?",
         "Existe. O Explorador de Estudo tem desfazer e refazer completos, e o seu backup "
         "original nunca é alterado — as mudanças vão para uma cópia exportada."),
    ],
}

GUIDES_PT["manage-jw-library-highlights"] = {
    "title": "Como gerenciar e recolorir os destaques do JW Library",
    "h1": "Gerenciando seus destaques do JW Library: recolorir e organizar em lote",
    "description": "Ponha ordem em anos de destaques do JW Library: mude cores em lote, dê ao "
                   "seu código de cores um sentido consistente e veja todos os destaques em "
                   "um só lugar. No navegador.",
    "intro": [
        "As cores dos destaques só ajudam se significarem algo consistente. Com o tempo, os "
        "destaques da maioria das pessoas se desencontram — o amarelo significava uma coisa "
        "em 2019 e outra hoje, e não há como, no JW Library, ver todos juntos ou corrigi-los "
        "em escala. O Explorador de Estudo reúne cada destaque em uma única visão e deixa "
        "você recolorir em lote.",
    ],
    "steps": [
        ("Carregue seu backup",
         "Em jwsync.org, abra o arquivo .jwlibrary no Explorador de Estudo e vá para a aba "
         "Destaques."),
        ("Folheie e filtre seus destaques",
         "Veja todos os destaques em uma lista só, filtre por cor ou publicação e pesquise no "
         "texto destacado e nas notas ligadas a ele."),
        ("Recolora em lote",
         "Selecione vários destaques e mude a cor de todos de uma vez — por exemplo, unifique "
         "numa cor só tudo o que você entendia como “texto bíblico principal” em toda a sua "
         "biblioteca."),
        ("Edite também as notas ligadas",
         "Onde um destaque tem uma nota anexada, edite aqui mesmo o título e o conteúdo dessa "
         "nota."),
        ("Exporte e restaure",
         "Baixe o .jwlibrary editado e restaure no JW Library, para o seu código de cores "
         "consistente estar em todos os aparelhos."),
    ],
    "sections": [
        ("Decida o que as suas cores significam",
         "Um esquema simples — uma cor para os pontos principais, uma para textos a decorar, "
         "uma para perguntas a pesquisar — transforma os destaques em uma ferramenta de "
         "estudo em vez de enfeite. Recolorir em lote permite aplicar esse esquema "
         "retroativamente a anos de leitura."),
    ],
    "faq": [
        ("Consigo ver destaques que não têm nota anexada?",
         "Sim — a aba Destaques mostra todos eles, com ou sem nota ligada."),
        ("Recolorir afeta o texto por baixo?",
         "Não, muda apenas a cor do destaque; o texto da publicação e as suas notas ficam "
         "intactos."),
    ],
}

GUIDES_PT["jw-library-study-answers"] = {
    "title": "Ver e editar as suas respostas de estudo do JW Library",
    "h1": "Encontrando as suas respostas de estudo do JW Library em um só lugar",
    "description": "As respostas que você digita nas perguntas dos artigos de estudo e das "
                   "apostilas ficam escondidas no seu backup. A aba Respostas de Estudo do "
                   "Explorador de Estudo deixa você ler, pesquisar e editar todas de uma vez.",
    "intro": [
        "Enquanto estuda, você digita respostas nas caixas dos artigos de estudo, de A "
        "Sentinela e das apostilas das reuniões. Elas ficam salvas no seu backup — mas o JW "
        "Library só mostra cada uma delas enterrada na sua própria publicação. Não existe um "
        "lugar único para revisar tudo o que você escreveu. A aba Respostas de Estudo do "
        "Explorador de Estudo é esse lugar.",
    ],
    "steps": [
        ("Carregue seu backup no Explorador de Estudo",
         "Em jwsync.org, carregue o arquivo .jwlibrary e abra a aba Respostas de Estudo."),
        ("Leia todas as suas respostas juntas",
         "Cada resposta que você digitou aparece em uma lista pesquisável, para você revisar "
         "de relance todo o seu raciocínio sobre um artigo de estudo inteiro."),
        ("Pesquise e edite",
         "Encontre uma resposta pelo texto e depois edite e melhore ali mesmo — útil ao "
         "revisar antes de uma reunião ou ao arrumar uma redação feita com pressa."),
        ("Exporte ou restaure",
         "Restaure o arquivo editado para levar suas mudanças de volta ao JW Library, ou "
         "copie as respostas como texto para um discurso ou registro pessoal."),
    ],
    "sections": [
        ("Por que isso é útil antes das reuniões",
         "Revisar as respostas que você preparou em uma lista contínua — em vez de rolar "
         "parágrafo por parágrafo no aplicativo — é um jeito mais rápido de relembrar o que "
         "você planejou dizer e de perceber as respostas que ficaram em branco."),
    ],
    "faq": [
        ("Elas são a mesma coisa que as minhas notas pessoais?",
         "Não — as respostas de estudo são o que você digitou nas caixas de resposta de uma "
         "publicação. O Explorador de Estudo as mostra em uma aba própria, separada das notas "
         "livres."),
        ("Alguma coisa é enviada para ler as minhas respostas?",
         "Não. Como tudo no JW Sync, o seu backup é lido localmente, no navegador, e nunca é "
         "enviado a lugar nenhum."),
    ],
}

GUIDES_PT["extract-jw-library-notes-by-date"] = {
    "title": "Extrair notas do JW Library de um período para um backup novo",
    "h1": "Extraindo um período de notas do JW Library para um backup novo",
    "description": "Separe só as notas de um período específico — um ano de serviço, um "
                   "congresso, um projeto de estudo — em um backup .jwlibrary próprio e "
                   "limpo. Tudo no seu navegador.",
    "intro": [
        "Às vezes você quer uma fatia da sua biblioteca, não ela inteira: as notas deste ano "
        "para uma revisão, tudo de um congresso, ou a pesquisa de um único projeto para "
        "passar a alguém. O Explorador de Estudo consegue extrair as notas de um período para "
        "um backup .jwlibrary novinho, deixando a sua biblioteca principal intacta.",
    ],
    "steps": [
        ("Carregue seu backup",
         "Em jwsync.org, abra o arquivo .jwlibrary no Explorador de Estudo."),
        ("Defina o período",
         "Escolha as datas de início e fim das notas que você quer — um ano de serviço, um "
         "mês, as datas de um evento específico."),
        ("Extraia para um backup novo",
         "Exporte as notas correspondentes para um arquivo .jwlibrary novo. Ele contém apenas "
         "as notas e os destaques daquele período, com as etiquetas deles."),
        ("Use o arquivo extraído",
         "Restaure-o no JW Library para uma revisão focada, guarde-o como arquivo morto ou "
         "compartilhe com alguém que só precisa daquela fatia."),
    ],
    "sections": [
        ("Bons motivos para extrair por data",
         "Um arquivo anual do seu estudo; um arquivo limpo com as notas de um congresso, "
         "guardado à parte; entregar a um parceiro de estudo só as notas de um projeto que "
         "vocês fizeram juntos; ou dividir uma biblioteca enorme em pedaços datados e "
         "administráveis — tudo isso sem mexer no seu backup principal."),
    ],
    "faq": [
        ("Extrair remove essas notas da minha biblioteca?",
         "Não. A extração copia as notas correspondentes para um arquivo novo; o seu backup "
         "original guarda tudo."),
        ("Que data ele usa — quando escrevi ou quando editei a nota pela última vez?",
         "Ele usa as datas registradas na própria nota dentro do backup, então o período "
         "reflete quando as notas foram criadas ou modificadas."),
    ],
}

GUIDES_PT["connect-jw-library-notes-study-map"] = {
    "title": "Veja como as suas notas do JW Library se conectam — Mapa de Estudo",
    "h1": "Mapa de Estudo: um grafo privado de conhecimento das suas notas do JW Library",
    "description": "O Mapa de Estudo transforma as suas notas do JW Library em uma teia "
                   "interativa, ligando-as por textos bíblicos em comum, etiquetas em comum e "
                   "expressões parecidas — para você ver os temas que atravessam o seu estudo.",
    "intro": [
        "Anos de notas guardam conexões que você nunca viu: o mesmo texto bíblico citado em "
        "uma dezena de anotações, um tema ao qual você sempre volta, ideias que ecoam umas às "
        "outras em publicações diferentes. O Mapa de Estudo desenha esses laços como um grafo "
        "interativo, deixando visível o formato do seu próprio estudo.",
    ],
    "steps": [
        ("Abra a página de Estatísticas de Estudo e carregue um backup",
         "Acesse jwsync.org/highlights.html e carregue o arquivo .jwlibrary. O Mapa de Estudo "
         "o lê no seu navegador."),
        ("Abra o Mapa de Estudo",
         "Inicie o mapa para ver as suas notas como pontos conectados, ligados por textos "
         "bíblicos em comum, etiquetas em comum e expressões parecidas."),
        ("Explore as conexões",
         "Alterne entre as visões de Temas e Notas, passe o cursor para iluminar os laços de "
         "uma nota, arraste os elementos e use o controle de força para mostrar só as "
         "conexões mais próximas. O modo tela cheia dá espaço para circular."),
        ("Monte e salve cadeias de estudo",
         "Desenhe as suas próprias “cadeias de estudo” manuais entre notas relacionadas para "
         "registrar uma linha de raciocínio, e exporte o mapa como imagem PNG para guardar ou "
         "compartilhar."),
    ],
    "sections": [
        ("O que o mapa revela",
         "Os agrupamentos mostram os temas que você mais estuda; um texto bíblico ligado a "
         "muitas notas mostra um versículo ao qual você sempre volta; uma nota isolada pode "
         "ser um fio que vale a pena desenvolver. É um jeito de estudar o seu estudo — e de "
         "preparar discursos seguindo as ligações que você já fez."),
    ],
    "faq": [
        ("Preciso de muitas notas para o mapa ser útil?",
         "Uma biblioteca modesta já mostra conexões; quanto mais ricas as suas notas, mais o "
         "mapa revela. Bibliotecas muito pequenas mostram um aviso sugerindo acrescentar mais "
         "notas antes."),
        ("O mapa é privado?",
         "Totalmente. Ele é montado no seu navegador a partir do seu backup e nunca é "
         "enviado; até a exportação em PNG é gerada no seu aparelho."),
    ],
}

GUIDES_PT["review-old-jw-library-notes"] = {
    "title": "Como revisar suas notas antigas do JW Library (para elas ficarem)",
    "h1": "Revisando notas antigas do JW Library com o Retomar — um pouco, com frequência",
    "description": "Notas que você nunca revisita são notas que você esquece. O Retomar mostra "
                   "o que você escreveu neste dia em anos anteriores e monta uma revisão "
                   "espaçada e tranquila, para o estudo passado continuar trabalhando por você.",
    "intro": [
        "A maioria das notas de estudo é escrita uma vez e nunca mais vista. É um desperdício "
        "silencioso — a ideia valia a pena registrar, e então afundou no fundo da biblioteca. "
        "O Retomar traz as suas próprias notas antigas de volta à superfície, algumas por "
        "vez, para revisitá-las virar um pequeno hábito diário em vez de um projeto para "
        "algum dia.",
    ],
    "steps": [
        ("Abra a página de Estatísticas de Estudo e carregue um backup",
         "Acesse jwsync.org/highlights.html e carregue o arquivo .jwlibrary. O Retomar lê as "
         "suas notas localmente."),
        ("Veja o “Neste dia”",
         "O Retomar traz à tona notas que você escreveu nesta mesma data em anos anteriores — "
         "“escrita há dois anos, hoje” — reconectando você com o estudo passado no momento em "
         "que ele tem mais significado."),
        ("Faça uma revisão diária curta",
         "Ele apresenta um punhado de notas para revisitar e marcar como revisadas. Um pouco, "
         "com frequência, é o que faz o estudo ficar — e uma sequência cresce enquanto você "
         "mantém o hábito."),
        ("Volte amanhã",
         "A repetição espaçada programa as notas para reaparecerem ao longo do tempo, então "
         "aquelas que valem a pena lembrar continuam voltando até serem realmente suas."),
    ],
    "sections": [
        ("Por que a repetição espaçada funciona",
         "Revisar algo bem na hora em que você está prestes a esquecer é muito mais eficaz do "
         "que decorar tudo de uma vez. Ao espalhar poucas notas por muitos dias, o Retomar "
         "transforma a sua biblioteca existente em uma revisão contínua e de pouco esforço, "
         "que vai aprofundando aos poucos o que você estudou."),
    ],
    "faq": [
        ("Onde fica salvo o meu progresso de revisão?",
         "No seu navegador, no seu aparelho — não há conta e nada é enviado. A sequência e o "
         "calendário são só seus."),
        ("Preciso de notas novas para isso?",
         "Não — o Retomar funciona com as notas que você já escreveu. Quanto mais antiga a "
         "sua biblioteca, mais gratificantes ficam os momentos de “neste dia”."),
    ],
}

GUIDES_PT["jw-library-achievements-streaks"] = {
    "title": "Sequências, níveis e conquistas de estudo do JW Library",
    "h1": "Transforme o seu estudo do JW Library em sequências, níveis e prêmios",
    "description": "Veja as suas sequências de estudo, suba 60 níveis em 12 patamares na sua "
                   "Jornada de Estudo e desbloqueie cerca de 200 conquistas — tudo lido com "
                   "privacidade do seu próprio backup do JW Library.",
    "intro": [
        "A constância é a parte difícil do estudo pessoal, e é fácil deixar de lado um "
        "progresso que não dá para ver. A página de Estatísticas de Estudo transforma a "
        "história do seu backup em algo que você acompanha crescer: sequências, níveis e "
        "prêmios que refletem o estudo que você realmente fez — sem metas impostas, apenas o "
        "seu próprio registro tornado visível.",
    ],
    "steps": [
        ("Abra a página de Estatísticas de Estudo",
         "Acesse jwsync.org/highlights.html e carregue o seu backup .jwlibrary. Tudo é "
         "calculado no seu navegador."),
        ("Confira as suas sequências",
         "Veja a sua sequência de estudo mais longa e a atual, o seu ritmo semanal e as horas "
         "e os meses mais movimentados — o pulso do seu hábito de estudo."),
        ("Suba na sua Jornada de Estudo",
         "Avance por 60 níveis em 12 patamares com nome (de Semente até Sempre-verde), com "
         "uma esfera que muda de cor e comemorações a cada nível, com base em todo o seu "
         "estudo."),
        ("Colecione conquistas",
         "Desbloqueie cerca de 200 prêmios, da raridade Comum à Lendária, incluindo medalhas "
         "temáticas que reconhecem o conteúdo; abra qualquer medalha para ver o seu progresso "
         "rumo à próxima."),
    ],
    "sections": [
        ("Motivação sem pressão",
         "Estas não são metas que outra pessoa definiu — são um espelho do que você já fez. "
         "Ver uma sequência que você não quer quebrar, ou um nível quase alcançado, é um "
         "empurrãozinho para manter o bom hábito. E um Cartão Compartilhável resume o seu ano "
         "sem expor uma única nota pessoal."),
    ],
    "faq": [
        ("As sequências e os prêmios se atualizam sozinhos?",
         "Eles refletem o backup que você carregou, então crie um backup novo para ver o seu "
         "progresso mais recente. Nada roda em segundo plano."),
        ("Alguma coisa disso é compartilhada ou enviada?",
         "Não. Tudo é calculado localmente a partir do seu backup; só o cartão-resumo é algo "
         "que você pode escolher compartilhar, e ele não contém texto de nota nenhuma."),
    ],
}

GUIDES_PT["share-convention-assembly-notes"] = {
    "title": "Como compartilhar notas de congressos e assembleias do JW Library",
    "h1": "Compartilhando as suas notas de congressos, assembleias e reuniões",
    "description": "Passe as suas notas de congresso, assembleia ou reunião para a família e "
                   "os amigos em um arquivo pequeno — sem entregar a sua biblioteca inteira "
                   "nem sobrescrever a deles. Um uso prático do compartilhamento de notas.",
    "intro": [
        "Você tomou notas com capricho durante um congresso; um amigo que perdeu uma sessão "
        "adoraria tê-las; familiares querem os pontos para a própria revisão. Mandar o backup "
        "inteiro é exagero e apagaria as notas de quem recebe, se restaurado. O "
        "compartilhamento de notas deixa você passar adiante exatamente as notas que quiser — "
        "e deixa quem recebe manter tudo o que já tem.",
    ],
    "steps": [
        ("Carregue seu backup na página de compartilhamento",
         "Acesse jwsync.org/share.html e carregue o arquivo .jwlibrary."),
        ("Selecione só as notas do congresso",
         "Escolha a etiqueta do evento no filtro de etiquetas do seletor de notas e toque em "
         "Selecionar tudo — a lista já é exatamente o que você etiquetou. Os destaques "
         "ligados a essas notas vão junto."),
        ("Envie o arquivo pequeno de compartilhamento",
         "O JW Sync monta um arquivo pequeno contendo só aquelas notas. Envie como preferir — "
         "aplicativo de mensagens, e-mail, AirDrop. Sem servidor, sem conta."),
        ("Família e amigos fazem a junção",
         "Cada pessoa abre a mesma página, carrega o seu arquivo junto com o próprio backup e "
         "recebe um novo backup com as suas notas acrescentadas. As notas delas nunca são "
         "sobrescritas, e as notas importadas chegam com etiqueta, ficando fáceis de achar."),
    ],
    "sections": [
        ("Uma etiqueta deixa isso sem esforço",
         "Se você etiquetar as suas notas durante o evento (digamos, “Congresso 2026”), "
         "selecioná-las depois é um clique no filtro e um Selecionar tudo. Vale a pena "
         "começar uma etiqueta nova no início de qualquer congresso, assembleia ou reunião "
         "especial exatamente por isso."),
    ],
    "faq": [
        ("Posso compartilhar com várias pessoas de uma vez?",
         "Pode — o arquivo compartilhado é só um arquivo. Envie para quantas pessoas "
         "quiser; cada uma o junta à própria biblioteca de forma independente."),
        ("Minha biblioteca inteira fica exposta?",
         "Não. Só as notas que você selecionou estão no arquivo; o resto da sua biblioteca "
         "continua privado."),
    ],
}

GUIDES_PT["share-jw-library-notes-by-tag"] = {
    "title": "Compartilhe só as notas do JW Library que estão sob uma etiqueta",
    "h1": "Compartilhando só as notas que têm uma etiqueta",
    "description": "Envie um assunto, um projeto ou o material de um estudante em vez da sua "
                   "biblioteca inteira — e as suas etiquetas vão junto, então as notas chegam "
                   "organizadas do outro lado.",
    "intro": [
        "Uma etiqueta costuma ser a unidade natural de compartilhamento. Você etiquetou tudo "
        "o que reuniu sobre um assunto, tudo de um evento, ou tudo o que estuda com uma "
        "pessoa — e é esse conjunto, e não a sua biblioteca inteira, que a outra pessoa "
        "realmente quer.",
        "O compartilhamento de notas do JW Sync funciona nota por nota, então uma etiqueta é "
        "simplesmente a lista que você marca. As notas mantêm as etiquetas na saída, o que "
        "significa que quem as recebe pode filtrar exatamente o mesmo conjunto dentro da "
        "própria biblioteca depois.",
    ],
    "steps": [
        ("Confirme que as notas têm a etiqueta",
         "Etiquete-as no JW Library conforme escreve, ou abra o seu backup no Explorador de "
         "Estudo em jwsync.org e use o editor de etiquetas para acrescentar uma etiqueta a "
         "várias notas de uma vez. Etiquetar com consistência agora é o que torna o "
         "compartilhamento um trabalho de um minuto depois."),
        ("Abra a página de compartilhamento e carregue seu backup",
         "Acesse jwsync.org/share.html, escolha Enviar notas e carregue o arquivo .jwlibrary. "
         "Ele é lido no seu navegador e nunca sai do seu aparelho."),
        ("Escolha a etiqueta no filtro e depois Selecionar tudo",
         "O seletor de notas tem um filtro de etiquetas que lista cada etiqueta do seu backup "
         "com o número de notas dela. Escolha a sua etiqueta e a lista se restringe "
         "exatamente àquelas notas; Selecionar tudo marca todas. Essa é a seleção inteira — "
         "dois cliques."),
        ("Crie o arquivo e envie",
         "O JW Sync monta um arquivo pequeno contendo só as notas que você marcou. Envie por "
         "mensagem, e-mail ou AirDrop — não há servidor envolvido nem conta de nenhum lado."),
        ("A pessoa acrescenta ao próprio backup",
         "A outra pessoa abre a mesma página, escolhe Receber, dá uma olhada nas notas e as "
         "acrescenta ao próprio backup. Suas etiquetas chegam junto com as notas, mais uma "
         "etiqueta que identifica a importação, então o conjunto inteiro fica a um filtro de "
         "distância para ela também."),
    ],
    "sections": [
        ("Por que compartilhar uma etiqueta em vez de um backup",
         "Entregar um backup .jwlibrary completo revela tudo o que você já escreveu, e "
         "restaurá-lo apagaria as notas da outra pessoa. Compartilhar uma seleção etiquetada "
         "é o oposto nas duas coisas: ela vê apenas o que você escolheu e não perde nada do "
         "que é dela."),
        ("Restringindo mais, ou compartilhando várias etiquetas",
         "O filtro de etiquetas e a caixa de busca trabalham juntos: escolha uma etiqueta e "
         "depois digite uma palavra para reduzir ainda mais, e o Selecionar tudo continua "
         "marcando só o que está diante de você. A busca também encontra nomes de etiquetas, "
         "então uma palavra-chave presente em várias etiquetas reúne todas de uma vez. Cada "
         "nota da lista mostra as etiquetas que carrega, então você vê o que está enviando "
         "antes de enviar."),
        ("Etiquetas que vale a pena manter para compartilhar",
         "Vale manter algumas etiquetas que existem só para serem compartilhadas — o nome de "
         "um evento, um assunto que você pesquisa para outras pessoas, a pessoa com quem você "
         "estuda. Quando chega a hora de mandar algo, não há caça nenhuma: o conjunto já está "
         "montado."),
    ],
    "faq": [
        ("Minhas etiquetas vão para a outra pessoa?",
         "Vão. As notas compartilhadas carregam as suas etiquetas, e a importação recebe uma "
         "etiqueta própria, então quem recebe pode encontrar, revisar ou remover o lote "
         "inteiro depois."),
        ("E se uma nota tiver várias etiquetas?",
         "Ela aparece sob cada uma delas no filtro, e todas as suas etiquetas viajam junto. "
         "Filtrar por uma etiqueta nunca remove as outras."),
        ("Compartilhar tira as notas da minha biblioteca?",
         "Não. Compartilhar copia as notas para um arquivo pequeno; o seu backup e o seu "
         "aplicativo ficam intactos."),
        ("Posso enviar a mesma etiqueta para várias pessoas?",
         "Pode — o arquivo compartilhado é um arquivo comum. Envie para quantas pessoas "
         "quiser, e cada uma o acrescenta à própria biblioteca de forma independente."),
    ],
}

GUIDES_PT["share-notes-with-bible-student"] = {
    "title": "Compartilhar notas do JW Library com um estudante da Bíblia",
    "h1": "Compartilhando notas de estudo com quem você estuda a Bíblia",
    "description": "Envie as notas de uma lição — textos bíblicos, ilustrações, os pontos que "
                   "você preparou — direto para o JW Library da outra pessoa, sem tocar em "
                   "nada do que ela mesma escreveu.",
    "intro": [
        "Quando você prepara um estudo, a maior parte do trabalho acaba nas suas próprias "
        "notas: os textos extras, a ilustração que fez o ponto entrar, a resposta à pergunta "
        "que a pessoa fez na semana passada. Ler tudo em voz alta é uma coisa; deixar com ela "
        "uma cópia que dá para reler a semana toda é outra.",
        "O compartilhamento de notas coloca as suas notas preparadas na biblioteca da pessoa "
        "como notas de verdade do JW Library, presas aos mesmos parágrafos e versículos — não "
        "como uma captura de tela ou uma mensagem que ela vai rolar sem ler.",
    ],
    "steps": [
        ("Prepare as notas da lição no JW Library",
         "Escreva as notas como você normalmente faria, nos parágrafos e textos bíblicos que "
         "a lição abrange. Dê a elas uma etiqueta — o nome da pessoa, ou a publicação — para "
         "o conjunto ser fácil de selecionar depois."),
        ("Abra a página de compartilhamento e carregue seu backup",
         "Crie um backup (Estudo Pessoal → Backup e Restauração → Criar um backup), depois "
         "abra jwsync.org/share.html, escolha Enviar notas e carregue o arquivo. Ele nunca "
         "sai do seu aparelho."),
        ("Marque as notas desta lição",
         "Filtre o seletor pela etiqueta que você usou e toque em Selecionar tudo, ou "
         "pesquise e marque uma por uma. Crie o arquivo compartilhado — todo o resto da sua "
         "biblioteca fica onde está."),
        ("Envie e explique como receber",
         "A pessoa precisa antes de um backup próprio — Estudo Pessoal → Backup e Restauração "
         "→ Criar um backup. Depois ela abre jwsync.org/share.html, escolhe Receber, carrega "
         "o seu arquivo e o backup dela, e baixa o backup atualizado."),
        ("Ela restaura no JW Library",
         "Backup e Restauração → Restaurar, escolhe o arquivo atualizado, e as suas notas "
         "aparecem na biblioteca dela ao lado das próprias — com etiqueta, então ela sabe "
         "quais vieram de você."),
    ],
    "sections": [
        ("As notas dela nunca são sobrescritas",
         "Essa é a diferença importante em relação a enviar um backup. Uma restauração "
         "substitui a biblioteca inteira de um aparelho; receber notas compartilhadas "
         "acrescenta a ela. Tudo o que a pessoa escreveu — inclusive nos mesmos parágrafos — "
         "fica exatamente como estava."),
        ("Um ritmo semanal que leva dois minutos",
         "Depois que os dois fizerem isso uma primeira vez, a rotina fica curta: preparar, "
         "marcar, enviar, restaurar. Muita gente acha mais fácil enviar as notas logo depois "
         "de preparar, para o estudante tê-las antes do estudo, e não depois."),
    ],
    "faq": [
        ("O estudante precisa de uma conta ou de instalar um aplicativo?",
         "Nenhuma conta em lugar nenhum, e nada a instalar além do próprio JW Library — a "
         "página de compartilhamento é uma página da web comum."),
        ("E se o estudante nunca fez um backup?",
         "Ele faz um primeiro, no JW Library, em Estudo Pessoal → Backup e Restauração. Até "
         "uma biblioteca que parece vazia serve; o backup é aquilo a que as notas "
         "compartilhadas são acrescentadas."),
        ("Posso pegar as notas de volta depois?",
         "O arquivo é seu para enviar ou não enviar. Depois que alguém o tem, ele é dessa "
         "pessoa, exatamente como qualquer mensagem — então compartilhe o que você se "
         "sentiria à vontade de compartilhar por escrito."),
    ],
}

GUIDES_PT["share-meeting-notes-with-family"] = {
    "title": "Compartilhar notas das reuniões com a sua família",
    "h1": "Compartilhando as notas da reunião desta semana com a família",
    "description": "Alguém ficou doente, estava trabalhando ou viajou — mande as notas da "
                   "semana em um arquivo pequeno que a pessoa acrescenta ao próprio JW "
                   "Library, sem ninguém perder nada.",
    "intro": [
        "Na maioria das casas, cada um faz as próprias notas no próprio aparelho, e sempre tem "
        "alguém que perde uma reunião. Ler as suas notas no jantar funciona uma vez; colocar "
        "as notas na biblioteca da outra pessoa é o que permite que ela use o material "
        "depois, no lugar em que de fato vai procurar.",
        "Como o compartilhamento é nota por nota, e não backup por backup, várias pessoas "
        "podem trocar notas à vontade sem que a biblioteca de ninguém seja sobrescrita.",
    ],
    "steps": [
        ("Faça backup do aparelho em que você tomou as notas",
         "JW Library → Estudo Pessoal → Backup e Restauração → Criar um backup."),
        ("Selecione as notas da semana",
         "Em jwsync.org/share.html escolha Enviar notas, carregue o backup e marque as notas "
         "desta semana — pesquisar pela publicação as reúne rapidamente, e, se você etiquetar "
         "as notas da semana, o filtro de etiquetas junta tudo em um clique."),
        ("Mande no grupo da família",
         "Crie o arquivo compartilhado e envie pelo canal que a casa já usa — aplicativo de "
         "mensagens, e-mail, AirDrop. É um arquivo pequeno, só com as notas que você marcou."),
        ("Cada um acrescenta ao próprio backup",
         "A pessoa abre a mesma página, escolhe Receber, carrega o seu arquivo junto com um "
         "backup próprio, baixa o backup atualizado e o restaura no JW Library."),
    ],
    "sections": [
        ("A biblioteca de cada um continua sendo dele",
         "As notas de ninguém são substituídas, e ninguém precisa entregar a biblioteca "
         "inteira para participar. As notas importadas chegam com uma etiqueta, então cada um "
         "vê de relance quais notas vieram de outra pessoa e pode apagar o lote depois, se "
         "preferir não guardá-lo."),
        ("Adoração em família: reunir em vez de espalhar",
         "A mesma ferramenta funciona no sentido contrário. Se todos fizerem notas durante a "
         "adoração em família, uma pessoa pode recolher os arquivos compartilhados dos outros "
         "em um único backup e ficar com as notas combinadas da casa sobre o mesmo material."),
    ],
    "faq": [
        ("Os aparelhos das crianças podem participar?",
         "Qualquer aparelho que roda o JW Library e abre uma página da web pode. Os passos "
         "são idênticos no celular, no tablet ou no computador."),
        ("Precisamos estar na mesma plataforma?",
         "Não. Android, iPhone, iPad e o aplicativo do Windows usam o mesmo formato de "
         "backup, então as notas passam de um para o outro sem conversão."),
    ],
}

GUIDES_PT["receive-shared-jw-library-notes"] = {
    "title": "Alguém me mandou notas do JW Library — como abro?",
    "h1": "Acrescentando à sua biblioteca as notas que alguém compartilhou com você",
    "description": "Mandaram um arquivo de notas compartilhadas ou um bloco de texto. Veja "
                   "como visualizá-lo e acrescentá-lo ao seu backup do JW Library sem perder "
                   "uma única nota sua.",
    "intro": [
        "Notas compartilhadas do JW Library chegam como um arquivo pequeno (terminado em "
        ".jwshare.json) ou como um bloco de texto colado numa mensagem. O próprio JW Library "
        "não abre nem um nem outro — mas você não precisa dele para isso. O lado receptor do "
        "JW Sync lê as notas compartilhadas, mostra o que há nelas e as grava em um backup "
        "seu.",
        "A troca inteira acontece no seu aparelho. Não há conta, nada é enviado, e as suas "
        "notas recebem acréscimos, nunca substituições.",
    ],
    "steps": [
        ("Faça primeiro um backup da sua própria biblioteca",
         "No JW Library: Estudo Pessoal → Backup e Restauração → Criar um backup. É a esse "
         "arquivo que as notas compartilhadas serão acrescentadas, então ele deve estar "
         "atualizado."),
        ("Abra a página de compartilhamento e escolha Receber",
         "Acesse jwsync.org/share.html e escolha Receber notas."),
        ("Carregue o que mandaram para você",
         "Escolha o arquivo .jwshare.json, ou cole o texto compartilhado direto na caixa, se "
         "ele chegou como mensagem. De um jeito ou de outro, você vê uma prévia somente "
         "leitura de cada nota antes de qualquer coisa ser gravada."),
        ("Acrescente-as ao seu backup",
         "Carregue o seu próprio backup, escolha a etiqueta que as notas importadas devem "
         "levar e acrescente-as. O JW Sync monta um backup atualizado para você baixar."),
        ("Restaure o backup atualizado no JW Library",
         "Estudo Pessoal → Backup e Restauração → Restaurar, e escolha o arquivo atualizado. "
         "As notas compartilhadas agora estão na sua biblioteca, nos parágrafos e versículos "
         "certos."),
    ],
    "sections": [
        ("Nada do que é seu é substituído",
         "As notas compartilhadas são acrescentadas como notas novas. Mesmo quando uma nota "
         "compartilhada cai em um parágrafo em que você já escreveu, as duas sobrevivem — a "
         "sua intacta, a dela ao lado. A única coisa a lembrar é a regra comum da "
         "restauração: restaure o backup atualizado, não um mais antigo."),
        ("Mudou de ideia depois?",
         "Cada nota importada leva a etiqueta que você escolheu ao acrescentá-la. Abra o seu "
         "backup no Explorador de Estudo, filtre por essa etiqueta e você pode revisar ou "
         "apagar o lote inteiro de uma vez."),
    ],
    "faq": [
        ("O arquivo chegou renomeado para .txt ou abriu como texto — está quebrado?",
         "Não. Aplicativos de mensagens costumam fazer isso. Copie o texto e cole na caixa de "
         "Receber; funciona exatamente igual."),
        ("Preciso do backup inteiro de quem enviou?",
         "Não. O arquivo compartilhado contém só as notas que a pessoa escolheu enviar — nada "
         "mais da biblioteca dela."),
        ("Alguma coisa é enviada quando eu visualizo as notas?",
         "Não. Ler o arquivo compartilhado, visualizá-lo e gravar o backup atualizado "
         "acontecem todos no seu navegador, no seu aparelho."),
    ],
}

GUIDES_PT["share-notes-with-study-group"] = {
    "title": "Compartilhar notas de pesquisa com um grupo de estudo",
    "h1": "Compartilhando pesquisa com um grupo — e recolhendo a deles de volta",
    "description": "Um arquivo, muitas pessoas: mande um conjunto de notas de pesquisa a todos "
                   "que estudam o mesmo assunto e reúna o que eles enviarem de volta em um "
                   "único conjunto seu.",
    "intro": [
        "Quando várias pessoas estão pesquisando o mesmo assunto, a pesquisa acaba espalhada — "
        "uma achou as referências cruzadas, outra o pano de fundo histórico, uma terceira as "
        "ilustrações. Ler as capturas de tela uns dos outros não é a mesma coisa que ter o "
        "material na própria biblioteca, nos mesmos versículos, pesquisável no ano que vem.",
        "Como um arquivo compartilhado é só um arquivo, uma única exportação serve ao grupo "
        "inteiro, e o mesmo mecanismo traz o trabalho deles de volta a você.",
    ],
    "steps": [
        ("Etiquete a sua pesquisa enquanto a reúne",
         "Dê uma etiqueta ao assunto no JW Library para o conjunto ficar junto. No Explorador "
         "de Estudo você pode acrescentar uma etiqueta a várias notas de uma vez, se não "
         "etiquetou na hora."),
        ("Crie um arquivo compartilhado para o grupo",
         "Em jwsync.org/share.html escolha Enviar notas, carregue o backup, escolha a "
         "etiqueta do assunto no filtro de etiquetas, toque em Selecionar tudo e crie o "
         "arquivo."),
        ("Poste uma vez só",
         "Envie o mesmo arquivo para todos — um grupo de mensagens, um e-mail para várias "
         "pessoas, o que o grupo já usa. Não há configuração por pessoa nem cópia em "
         "servidor."),
        ("Peça a deles em troca",
         "Cada pessoa pode fazer exatamente o mesmo do lado dela. Acrescente ao seu backup, um "
         "a um, os arquivos que receber, dando a cada importação uma etiqueta própria — o "
         "nome de quem enviou funciona bem — para você sempre saber de quem é cada pesquisa."),
    ],
    "sections": [
        ("Um conjunto combinado, ainda assim identificável",
         "Depois de algumas rodadas, você tem toda a pesquisa do grupo sobre o assunto na sua "
         "própria biblioteca, nos parágrafos e versículos certos, com cada contribuição "
         "etiquetada pela origem. A busca encontra tudo de uma vez; as etiquetas deixam você "
         "separar de novo sempre que quiser."),
        ("Ninguém precisa expor a própria biblioteca",
         "Cada um compartilha só as notas que marcar. O resto da biblioteca de cada pessoa — "
         "estudo pessoal, lembretes particulares, tudo o mais — nunca entra no arquivo."),
    ],
    "faq": [
        ("Existe um limite de quantas notas posso compartilhar de uma vez?",
         "Na prática, não. Notas são pequenas; um conjunto grande ainda produz um arquivo que "
         "você consegue mandar numa mensagem."),
        ("E se duas pessoas me mandarem a mesma nota?",
         "Você vai vê-la duas vezes, cada uma sob a etiqueta de quem enviou. A busca do "
         "Explorador de Estudo torna fácil identificar e apagar quase-duplicatas."),
        ("Alguém pode receber sem enviar nada de volta?",
         "Pode. Receber e enviar são independentes — ninguém é obrigado a compartilhar para "
         "poder acrescentar o que recebeu."),
    ],
}

GUIDES_PT["share-talk-preparation-notes"] = {
    "title": "Passe adiante a pesquisa por trás de um discurso ou designação",
    "h1": "Passando adiante a pesquisa dos seus discursos e designações",
    "description": "Você fez a pesquisa para um discurso, uma parte ou uma designação. Veja "
                   "como entregar esse material a quem vier depois — como notas de verdade na "
                   "biblioteca da pessoa, ou como texto simples para um documento.",
    "intro": [
        "Preparação raramente serve uma vez só. Os textos bíblicos que você caçou, o pano de "
        "fundo que leu, o jeito como finalmente decidiu apresentar um ponto — quem for cobrir "
        "o mesmo material depois preferiria começar dali do que de uma página em branco.",
        "O JW Sync dá duas maneiras de passar isso adiante, e elas servem a pessoas "
        "diferentes: como notas que chegam ao JW Library da outra pessoa, ou como texto "
        "simples que ela cola num documento.",
    ],
    "steps": [
        ("Reúna a pesquisa sob uma etiqueta",
         "Enquanto prepara, etiquete as notas com o tema ou com a designação. Se elas já "
         "estiverem escritas e sem etiqueta, abra o seu backup no Explorador de Estudo e "
         "etiquete tudo em lote, em dois minutos."),
        ("Decida que forma serve melhor à outra pessoa",
         "Quem estuda no JW Library quer notas na biblioteca. Quem está montando um documento "
         "quer texto. Você pode fazer as duas coisas a partir do mesmo conjunto."),
        ("Para enviar notas: use a página de compartilhamento",
         "Em jwsync.org/share.html escolha Enviar notas, carregue o backup, filtre pela "
         "etiqueta que usou, toque em Selecionar tudo e crie o arquivo. A pessoa acrescenta "
         "ao próprio backup e restaura — as notas dela ficam intactas."),
        ("Para enviar texto: exporte pelo Explorador de Estudo",
         "Filtre até o mesmo conjunto e copie ou exporte em Markdown ou texto simples. A "
         "formatação sobrevive, então um esboço estruturado continua estruturado ao ser "
         "colado num documento."),
    ],
    "sections": [
        ("Guarde uma cópia para você, num formato que vai encontrar de novo",
         "Vale guardar a mesma exportação para o seu próprio uso. Uma etiqueta mais um "
         "intervalo de datas tornam toda a preparação recuperável anos depois, que é "
         "exatamente quando você vai querer — e a extração por data do Explorador de Estudo "
         "transforma qualquer janela de tempo em um arquivo próprio."),
    ],
    "faq": [
        ("Os textos bíblicos continuam ligados aos versículos certos?",
         "Continuam — as notas compartilhadas mantêm o parágrafo e o versículo a que estavam "
         "presas, então caem no lugar certo na biblioteca da outra pessoa."),
        ("Posso compartilhar notas que têm destaques?",
         "Pode. Os destaques ligados às notas que você compartilha vão junto com elas."),
    ],
}

GUIDES_PT["weekly-meeting-preparation-jw-library-notes"] = {
    "title": "Prepare-se para a reunião usando notas que você já escreveu",
    "h1": "Preparação semanal com as notas que você já tem",
    "description": "Você já estudou esse material antes. Veja uma rotina semanal curta que "
                   "traz à tona as suas notas, destaques e respostas antigas sobre a mesma "
                   "publicação antes de você preparar de novo.",
    "intro": [
        "A maioria das pessoas prepara cada semana a partir de uma página em branco, mesmo já "
        "tendo escrito sobre o mesmo assunto — às vezes sobre o mesmo texto bíblico — várias "
        "vezes antes. Aquele raciocínio anterior está na sua biblioteca; o único problema é "
        "que nada o traz de volta a você no momento certo.",
        "Uma rotina de cinco minutos no começo da preparação resolve isso, e ela não usa nada "
        "além do backup que você já tem.",
    ],
    "steps": [
        ("Carregue um backup atual no Explorador de Estudo",
         "Crie um backup no JW Library e depois abra-o em jwsync.org. Tudo é lido no seu "
         "navegador."),
        ("Pesquise o assunto antes de começar",
         "Pesquise o texto-tema, o assunto ou a publicação. Tudo o que você escreveu sobre "
         "isso em anos anteriores aparece junto, em todas as publicações em que aparece."),
        ("Confira as suas respostas de estudo",
         "A visão de Respostas de Estudo reúne as respostas que você digitou nas perguntas, "
         "então as rodadas anteriores pelo mesmo material estão ali para você desenvolver, "
         "em vez de repetir."),
        ("Acrescente o que falta e devolva ao aplicativo",
         "As notas podem ser editadas ou criadas ali mesmo — título, texto, etiquetas, cor do "
         "destaque. Exporte o backup editado e restaure no JW Library, e a sua preparação "
         "estará no aplicativo para a reunião."),
    ],
    "sections": [
        ("Por que as notas antigas importam",
         "Revisar o que você concluiu da última vez transforma a preparação em algo "
         "cumulativo. Você para de redescobrir os mesmos pontos e passa a construir sobre "
         "eles — e as notas que acrescentar esta semana viram o ponto de partida da próxima "
         "rodada."),
        ("Uma versão mais tranquila: deixe as notas virem até você",
         "Se uma pesquisa semanal parecer trabalho, o Retomar, na página de Estatísticas de "
         "Estudo, traz sozinho algumas notas antigas por dia, incluindo as que você escreveu "
         "nesta data em anos anteriores. O mesmo benefício, sem rotina para lembrar."),
    ],
    "faq": [
        ("Editar no navegador muda a minha biblioteca diretamente?",
         "Não. Você exporta um backup atualizado e o restaura no JW Library — o aplicativo só "
         "muda por uma restauração feita por você."),
        ("Meu backup é enviado quando eu pesquiso nele?",
         "Não. O arquivo é lido localmente, no seu navegador; nada é mandado a lugar nenhum."),
    ],
}

GUIDES_PT["print-jw-library-notes"] = {
    "title": "Como imprimir as suas notas do JW Library",
    "h1": "Levando as suas notas do JW Library para o papel",
    "description": "O JW Library não tem botão de imprimir. Exporte suas notas como texto ou "
                   "Markdown, cole em qualquer documento e imprima — um diário de estudo, um "
                   "conjunto de notas para quem não usa o aplicativo, ou um arquivo.",
    "intro": [
        "Não há como imprimir a partir do JW Library, e capturas da tela do celular rendem uma "
        "leitura ruim. Mas as notas são suas, e levá-las a um documento imprimível é simples "
        "assim que dá para ler o arquivo de backup.",
        "O Explorador de Estudo lê um backup .jwlibrary no seu navegador e permite copiar ou "
        "exportar qualquer seleção de notas como texto simples ou Markdown — que todo editor "
        "de texto, aplicativo de anotações e impressora já entendem.",
    ],
    "steps": [
        ("Crie um backup e abra-o",
         "JW Library → Estudo Pessoal → Backup e Restauração → Criar um backup, depois "
         "carregue o arquivo em jwsync.org."),
        ("Restrinja ao que você quer no papel",
         "Filtre por publicação, etiqueta, cor de destaque ou intervalo de datas, ou pesquise "
         "um assunto. Imprimir tudo é possível, mas um conjunto filtrado costuma render um "
         "documento bem mais útil."),
        ("Copie ou exporte como texto ou Markdown",
         "Tire a seleção em Markdown ou texto simples. Negrito, itálico e listas sobrevivem, "
         "então notas estruturadas continuam estruturadas na página."),
        ("Cole num documento e imprima",
         "Qualquer editor de texto ou aplicativo de anotações serve. Ajuste os títulos e as "
         "margens que quiser e depois imprima ou salve em PDF."),
    ],
    "sections": [
        ("Montando um diário de estudo",
         "Um intervalo de datas é a unidade natural para um diário impresso — um ano de "
         "notas, ou o período de uma publicação. Extrair por data dá um conjunto cronológico "
         "limpo para imprimir ou encadernar, o que é uma satisfação ter fora da tela."),
        ("Imprimindo para quem não usa o aplicativo",
         "Nem todo mundo estuda em um aparelho. Um conjunto impresso de notas sobre o material "
         "atual é genuinamente útil para quem prefere papel, e leva os mesmos dois minutos de "
         "qualquer outra exportação."),
    ],
    "faq": [
        ("Posso imprimir também os meus destaques?",
         "A visão de destaques lista as passagens que você marcou, e essa lista é copiada "
         "como texto junto com as suas notas."),
        ("Exportar muda alguma coisa no JW Library?",
         "Não. A exportação lê uma cópia do seu backup; o seu arquivo original e o aplicativo "
         "ficam intactos."),
    ],
}

GUIDES_PT["clean-up-duplicate-jw-library-notes"] = {
    "title": "Limpar notas duplicadas e vazias do JW Library",
    "h1": "Limpando notas duplicadas, notas vazias e bagunça",
    "description": "Restaurou um backup duas vezes ou importou as mesmas notas de novo? O "
                   "Doutor da Biblioteca examina o arquivo .jwlibrary no navegador, encontra "
                   "duplicatas e notas vazias e entrega uma cópia limpa.",
    "intro": [
        "Bibliotecas acumulam bagunça. Restaurar um backup em um aparelho que já tinha algumas "
        "das mesmas notas, importar duas vezes um conjunto compartilhado, ou anos de notas "
        "pela metade que nunca foram terminadas — cada coisa dessas deixa algum resíduo, e o "
        "JW Library não dá jeito de varrer tudo em lote.",
        "O Doutor da Biblioteca é um check-up gratuito para um arquivo .jwlibrary. Ele examina "
        "o backup no seu navegador, conta em linguagem simples o que encontrou e conserta o "
        "que dá para consertar com um toque.",
    ],
    "steps": [
        ("Faça um backup antes — como sempre",
         "JW Library → Estudo Pessoal → Backup e Restauração → Criar um backup. Guarde esse "
         "arquivo; ele é a sua reserva."),
        ("Rode o check-up",
         "Abra jwsync.org, carregue o backup e inicie o Doutor da Biblioteca. Ele examina o "
         "conteúdo e a estrutura do arquivo sem mandá-lo a lugar nenhum."),
        ("Leia o que ele encontrou",
         "Duplicatas, notas vazias e outras sobras são listadas com clareza, com as "
         "quantidades, para você ver o tamanho do problema antes de mudar qualquer coisa."),
        ("Conserte e baixe a cópia limpa",
         "Um toque aplica os reparos e gera um novo arquivo .jwlibrary limpo. O seu original "
         "nunca é alterado."),
        ("Restaure o arquivo limpo",
         "Backup e Restauração → Restaurar, e escolha o arquivo limpo. A sua biblioteca "
         "continua a mesma, menos a bagunça."),
    ],
    "sections": [
        ("Como as duplicatas surgem, para começo de conversa",
         "Quase sempre por causa de uma restauração. Se você restaura um backup em um "
         "aparelho que já tinha parte do mesmo material — ou restaura o mesmo arquivo duas "
         "vezes por caminhos diferentes — o aplicativo não tem como saber que já viu aquelas "
         "notas."),
        ("Mesclar é o jeito de evitá-las",
         "É justamente por isso que mesclar dois backups é mais seguro do que restaurar um "
         "por cima do outro: a mesclagem detecta o material que já existe e o mantém uma vez "
         "só. As mesmas verificações rodam dentro de toda mesclagem, então um backup mesclado "
         "sai limpo mesmo que os arquivos de entrada não estivessem."),
    ],
    "faq": [
        ("Ele vai apagar notas que eu quero de verdade?",
         "Ele remove duplicatas exatas e notas vazias — material que não tem nada dentro para "
         "se perder. E, como ele grava um arquivo novo em vez de editar o seu, o original "
         "está sempre lá como reserva."),
        ("Ele recupera notas que apaguei no aplicativo?",
         "Não. Se uma nota foi apagada no JW Library antes de o backup ser feito, ela não está "
         "no arquivo para ser recuperada — um backup mais antigo é o lugar de procurar."),
    ],
}

GUIDES_PT["backup-jw-library-before-phone-repair"] = {
    "title": "Faça backup do JW Library antes de resetar ou consertar o celular",
    "h1": "Antes de um reset de fábrica, um conserto ou vender o celular",
    "description": "Um reset apaga as notas do JW Library junto com tudo o mais, e as "
                   "ferramentas de transferência não as levam. Faça um backup, confirme que "
                   "ele realmente abre e só então resete, sem nada em risco.",
    "intro": [
        "Resete o celular, mande-o para conserto ou passe-o para outra pessoa, e os dados de "
        "estudo pessoal do JW Library vão junto. Fotos e aplicativos voltam de um backup na "
        "nuvem; anos de notas, destaques e marcadores geralmente não, porque as ferramentas "
        "de transferência pulam os dados privados do aplicativo.",
        "A solução leva cinco minutos, e o passo que as pessoas pulam é justamente o que mais "
        "importa: verificar se o arquivo de backup é mesmo legível antes de o aparelho ser "
        "apagado.",
    ],
    "steps": [
        ("Crie o backup",
         "JW Library → Estudo Pessoal → Backup e Restauração → Criar um backup. Você fica com "
         "um arquivo .jwlibrary — normalmente de poucos megabytes."),
        ("Tire-o do aparelho",
         "Mande por e-mail para você mesmo, ou coloque no Drive, no iCloud ou numa pasta do "
         "computador. Um backup que só existe no celular que você está prestes a apagar não é "
         "um backup."),
        ("Confirme que ele abre antes de apagar qualquer coisa",
         "Carregue o arquivo em jwsync.org e olhe — as notas, os destaques e os marcadores "
         "devem estar todos lá, e o check-up aponta qualquer coisa errada com o arquivo. É "
         "esse o objetivo do exercício: descobrir depois que o arquivo é ilegível já é tarde "
         "demais."),
        ("Resete e depois restaure",
         "Depois do reset ou do conserto, instale o JW Library, faça login e vá em Backup e "
         "Restauração → Restaurar e escolha o seu arquivo."),
        ("Usou um celular emprestado nesse meio-tempo? Mescle, não sobrescreva",
         "Se você fez notas em um aparelho temporário, faça backup dele também e mescle os "
         "dois arquivos em jwsync.org antes de restaurar — senão, restaurar o backup antigo "
         "apaga tudo o que você escreveu enquanto esperava."),
    ],
    "sections": [
        ("Por que a verificação vale o minuto a mais",
         "Transferências interrompidas, serviços de nuvem que estragam arquivos e extensões "
         "renomeadas no caminho produzem backups que parecem bons na pasta e falham na "
         "restauração. Abrir o arquivo antes transforma um problema silencioso em um problema "
         "que você ainda consegue resolver, enquanto o aparelho original ainda tem os dados."),
        ("Guarde o arquivo depois da restauração",
         "Não apague assim que o aparelho novo estiver funcionando. Backups antigos são o "
         "único caminho de volta para uma nota apagada sem querer meses depois, e não custa "
         "nada guardá-los."),
    ],
    "faq": [
        ("Minhas publicações baixadas voltam?",
         "O backup carrega os seus dados de estudo pessoal — notas, destaques, marcadores, "
         "etiquetas e listas de reprodução. As publicações são simplesmente baixadas de novo "
         "depois."),
        ("O arquivo funciona se eu mudar de marca de celular ou de plataforma?",
         "Funciona. O formato .jwlibrary é o mesmo no Android, no iPhone, no iPad e no "
         "Windows."),
    ],
}

GUIDES_PT["jw-library-notes-missing-after-update"] = {
    "title": "Notas do JW Library sumiram depois de uma atualização ou reinstalação",
    "h1": "Notas sumidas depois de atualizar, reinstalar ou restaurar o aplicativo",
    "description": "Suas notas desapareceram depois de atualizar, reinstalar ou fazer login de "
                   "novo. O que fazer primeiro, o que não fazer, e como recuperá-las sem "
                   "perder o que você escreveu desde então.",
    "intro": [
        "Abrir o JW Library depois de uma atualização e encontrar suas notas sumidas assusta, e na grande maioria dos casos elas são recuperáveis. O que importa é o que você faz nos minutos seguintes — especificamente, não fazer a única coisa que transforma uma situação recuperável em perda definitiva.",
        "É um momento desagradável: o JW Library abre e as notas não estão lá. Antes de "
        "qualquer coisa, um conselho — não tenha pressa. Quase tudo o que torna essa situação "
        "irrecuperável é feito nos primeiros dez minutos, ao sobrescrever justamente o backup "
        "que ainda contém as notas sumidas.",
        "Siga os passos abaixo na ordem. O objetivo é terminar com um único arquivo contendo "
        "tanto as notas antigas quanto tudo o que você escreveu desde então.",
    ],
    "steps": [
        ("Ainda não sobrescreva os seus backups",
         "Evite criar um backup novo por cima de um antigo e não restaure nada às cegas. Um "
         "arquivo de backup mais antigo é o lugar mais provável onde as suas notas ainda "
         "existem."),
        ("Cace o backup mais recente que você tem",
         "Verifique anexos de e-mail, o Google Drive, o iCloud Drive, a pasta de downloads do "
         "computador e qualquer outro aparelho em que você já restaurou. Backups são "
         "pequenos, então é comum ter mais cópias do que a gente lembra."),
        ("Olhe dentro do arquivo antes de restaurá-lo",
         "Carregue o candidato em jwsync.org e veja o que há de fato nele — quantas notas, de "
         "quais publicações, até que data. Isso diz se é o arquivo certo, antes de você se "
         "comprometer com uma restauração."),
        ("Faça backup também do aparelho atual",
         "Mesmo que pareça vazio, faça o backup. Se você escreveu qualquer coisa desde que as "
         "notas sumiram, esse arquivo é a única cópia disso."),
        ("Mescle os dois e depois restaure",
         "Mescle o backup antigo com o atual em jwsync.org. O resultado contém as notas "
         "recuperadas e tudo o que foi escrito desde então, com as duplicatas mantidas uma "
         "vez só. Restaure esse arquivo mesclado — nunca o backup antigo sozinho."),
    ],
    "sections": [
        ("Por que restaurar o backup antigo sozinho é o movimento errado",
         "Uma restauração substitui a biblioteca do aparelho por completo. Se você restaurar "
         "o backup antigo direto, recupera as notas sumidas e perde tudo o que foi escrito "
         "depois que aquele backup foi feito. É mesclar primeiro que torna a recuperação "
         "livre de perdas."),
        ("Se o próprio backup não restaurar",
         "Um arquivo que dá erro na restauração não está necessariamente perdido. Rode o "
         "check-up nele — danos por downloads interrompidos, sincronização na nuvem ou uma "
         "extensão renomeada costumam ter conserto, e uma cópia limpa restaura normalmente."),
        ("Primeiro: ainda não crie um backup novo",
         "Se as notas sumiram, resista ao reflexo de fazer backup na hora. Um backup captura o estado atual, e se o estado atual for o vazio você corre o risco de sobrescrever o arquivo bom que já tinha. Descubra primeiro quais backups existem — em Downloads, Arquivos, e-mail ou na nuvem — e só então decida o que fazer. Nada no aparelho melhora com um backup feito no susto."),
        ("Por que uma atualização pode parecer apagar notas",
         "A causa comum não é exclusão. Uma atualização pode deixar o app apontando para um banco de dados novo e vazio enquanto o antigo continua no disco; uma reinstalação — inclusive uma feita automaticamente por uma atualização de loja que falhou pela metade — inicia o app do zero; e em aparelhos compartilhados ou com vários perfis o app pode acabar rodando sob um perfil diferente. Em todos os casos as notas não estão tanto apagadas quanto não carregadas, e é por isso que uma restauração de backup normalmente traz tudo de volta sem problema."),
        ("Recuperar um backup antigo sem descartar o trabalho novo",
         "Se você estudou desde que o backup foi feito, uma restauração simples troca uma perda por outra: traz as notas antigas de volta e remove o que é mais recente. O jeito de contornar é fazer backup do estado atual num arquivo separado, mesclar com o backup mais antigo para que os dois conjuntos de notas existam num arquivo só e restaurar o resultado. Você termina com as notas recuperadas e as recentes juntas, em vez de escolher entre elas."),
        ("Se o app se reinstalou sozinho",
         "Uma reinstalação limpa o armazenamento privado do app, então tudo que não estiver num backup é irrecuperável — não há cópia na nuvem para recorrer. Verifique todos os lugares onde um arquivo .jwlibrary pode ter sido salvo antes de concluir que não existe nenhum, inclusive a pasta de enviados do seu e-mail e qualquer armazenamento na nuvem que você já tenha usado. Assim que encontrar um, restaure, e daí em diante guarde os backups fora do aparelho."),
        ("Depois que tudo voltar",
         "Quando suas notas estiverem restauradas, faça mais um backup e guarde fora do aparelho — o episódio pelo qual você acabou de passar é o argumento a favor. Se precisou mesclar um backup antigo com o estado atual para chegar até aqui, guarde também os dois arquivos de origem: eles são retratos datados, e ter mais deles foi justamente o que tornou a recuperação possível."),
    ],
    "faq": [
        ("As notas ainda estão em algum lugar do aparelho?",
         "Não de um jeito que dê para alcançar de fora do aplicativo. Recuperação, na prática, "
         "significa um arquivo de backup anterior — e é por isso que guardar os antigos "
         "importa tanto."),
        ("Fazer login de novo traz as notas de volta?",
         "Não. Os dados de estudo pessoal não ficam guardados em uma conta; eles vivem no "
         "aparelho e só viajam por arquivos de backup."),
        ("E se o único backup que eu tenho for de meses atrás?",
         "Mescle-o com um backup do aparelho como ele está agora. Você recupera tudo o que o "
         "arquivo antigo tem e mantém tudo o que o aparelho ainda tem, sem escolher entre os "
         "dois."),
        ("Minhas notas sumiram mesmo?",
         "Não necessariamente. Se existir um backup em algum lugar, tudo que está nele é totalmente recuperável. O que é irrecuperável é apenas o trabalho feito depois do backup mais recente."),
        ("Dá para combinar um backup antigo com o que está no aparelho agora?",
         "Dá — faça backup do estado atual primeiro, depois mescle com o mais antigo e restaure o resultado. Os dois conjuntos de notas terminam na mesma biblioteca."),
        ("Restaurar um backup antigo vai apagar minhas notas recentes?",
         "Sozinho, sim, porque uma restauração substitui os dados do aparelho. Mescle o backup atual com o antigo primeiro e restaure o arquivo mesclado."),
        ("Devo reinstalar o app para resolver?",
         "Não — reinstalar limpa o armazenamento privado do app e elimina qualquer chance de recuperar o que ainda estiver no aparelho. Procure um backup existente primeiro e trate a reinstalação como último recurso, depois de já ter um."),
    ],
}

GUIDES_PT["help-family-member-move-jw-library-notes"] = {
    "title": "Ajude um familiar a levar as notas do JW Library",
    "h1": "Ajudando outra pessoa a levar ou resgatar as notas do JW Library",
    "description": "Você é aquele a quem pedem para consertar o celular. Veja o caminho mais "
                   "curto e confiável para levar as notas do JW Library de um parente a um "
                   "aparelho novo — inclusive como fazer isso sem ler as notas dele.",
    "intro": [
        "Mais cedo ou mais tarde alguém coloca o celular na sua mão, com um novo do lado. As "
        "notas do JW Library são a parte que não se muda sozinha, e muitas vezes são a parte "
        "que mais importa — anos de estudo que nenhuma ferramenta de transferência leva.",
        "O processo é o mesmo de fazer para você mesmo, com uma consideração extra que vale "
        "pensar antes: em qual aparelho o trabalho vai acontecer.",
    ],
    "steps": [
        ("Oriente a pessoa a fazer um backup no aparelho antigo",
         "JW Library → Estudo Pessoal → menu de três pontos → Backup e Restauração → Criar um "
         "backup. Isso salva um arquivo .jwlibrary. Se você não estiver junto, essa parte dá "
         "para explicar por telefone."),
        ("Leve o arquivo para onde você precisa",
         "Peça que ela mande por e-mail para si mesma ou compartilhe com você. É pequeno o "
         "bastante para ir por qualquer aplicativo de mensagens."),
        ("Verifique se o arquivo abre",
         "Carregue-o em jwsync.org e confirme que as notas estão lá. Fazer isso antes de o "
         "aparelho antigo ser apagado ou repassado é o que transforma uma surpresa ruim em "
         "não-acontecimento."),
        ("Mescle se o aparelho novo já tiver notas",
         "Se a pessoa já vinha usando o celular novo há um tempo, faça backup dele também e "
         "mescle os dois arquivos — senão, restaurar o backup antigo apaga tudo o que ela "
         "escreveu no aparelho novo."),
        ("Conduza a restauração com ela",
         "No aparelho novo: Backup e Restauração → Restaurar e escolha o arquivo. Notas, "
         "destaques, marcadores e etiquetas aparecem todos."),
    ],
    "sections": [
        ("Fazendo isso sem ler as notas dela",
         "Notas de estudo pessoal são pessoais. Se você preferir não vê-las — ou a pessoa "
         "preferir que você não veja — faça tudo no aparelho dela: é uma página da web, então "
         "dá para abrir jwsync.org no celular ou no tablet dela, carregar os arquivos ali e "
         "nunca ter o backup na sua própria máquina. Nada é enviado de qualquer jeito, mas "
         "assim o arquivo nunca sai das mãos dela."),
        ("Deixe com ela um backup que ela consiga encontrar",
         "Antes de devolver o celular, garanta que o arquivo de backup esteja em algum lugar "
         "que ela consiga achar de novo — o e-mail ou o serviço de nuvem dela, e não só a sua "
         "pasta de downloads. Da próxima vez, talvez ela nem precise de você."),
    ],
    "faq": [
        ("Dá para fazer isso a distância?",
         "Dá. Se a pessoa conseguir criar um backup e mandar o arquivo, todo o resto funciona "
         "à distância — e a restauração são alguns toques que você explica por telefone."),
        ("Ela tem um Android e o novo é um iPhone. Isso faz diferença?",
         "Não. O formato de backup é idêntico no Android, no iPhone, no iPad e no Windows."),
        ("E se ela nunca fez backup e o celular antigo já foi?",
         "Aí não há de onde recuperar — os dados viviam naquele aparelho. Vale a pena "
         "estabelecer já no celular novo o hábito de fazer backups regulares."),
    ],
}

GUIDES_PT["import-markdown-notes-jw-library"] = {
  "title": "Como importar notas em Markdown para o JW Library",
  "h1": "Como importar notas em Markdown para o JW Library",
  "description": "Transforme arquivos .md do Obsidian, do Notion ou de qualquer editor de Markdown em notas reais do JW Library, colocadas no versículo certo — grátis, privado, no seu navegador.",
  "intro": [
   "O JW Library não tem nenhuma forma de trazer texto para dentro. Você pode escrever notas dentro do aplicativo, mas uma nota escrita em outro lugar — no Obsidian, no Notion, num arquivo de texto do computador — não tem caminho nenhum até a sua biblioteca. As pessoas acabam redigitando tudo, ou desistem e ficam com dois conjuntos de notas de estudo que nunca se encontram.",
   "O JW Sync fecha essa lacuna. Carregue um backup no Explorador de estudo, toque em “Importar Markdown” e seus arquivos .md viram notas de verdade dentro dele: com título, data e etiquetas preservados e — quando o arquivo diz a que passagem pertence — ligados àquele versículo, exatamente como se você tivesse escrito a nota no aplicativo enquanto lia.",
   "Funciona nos dois sentidos. As notas exportadas deste site levam livro, capítulo e versículo, então voltam exatamente para o lugar de onde saíram. As notas escritas em outro lugar geralmente não levam nada disso, e por isso esta página explica as uma ou duas linhas que as posicionam — e o que acontece quando um arquivo não as tem.",
  ],
  "steps": [
   ("Crie um backup no JW Library",
    "Abra o JW Library, vá em Estudo pessoal, toque no menu de três pontos, escolha Backup e restauração e depois Criar um backup. Isso gera um arquivo .jwlibrary — a biblioteca à qual suas notas serão adicionadas."),
   ("Abra o Explorador de estudo",
    "Acesse jwsync.org, abra o Explorador de estudo e carregue esse arquivo .jwlibrary. Tudo acontece dentro do seu navegador; o arquivo nunca é enviado para lugar nenhum."),
   ("Toque em “Importar Markdown”",
    "O botão fica ao lado de “Exportar Markdown”. Escolha quantos arquivos .md quiser, ou um .zip com eles — inclusive o .zip que este site gera ao exportar."),
   ("Leia o resumo antes que algo seja escrito",
    "Você vê quantas notas vão cair num versículo, quantas serão adicionadas como notas avulsas e quantas já estão no seu backup e serão ignoradas. Tudo o que o site precisou interpretar aparece linha a linha, com uma caixa de seleção, para você decidir em vez de descobrir depois."),
   ("Exporte e restaure",
    "Toque em “Exportar .jwlibrary” e restaure esse arquivo no JW Library em Backup e restauração → Restaurar. Suas notas importadas já fazem parte da biblioteca naquele aparelho."),
  ],
  "sections": [
   ("O menor arquivo que funciona",
    "Um arquivo Markdown não precisa de nada para ser importado: um arquivo só com texto vira uma nota e tira o título do primeiro título interno ou, na falta dele, do nome do arquivo. Todo o resto serve para dizer onde a nota vai. Um arquivo completo fica assim:\n\n---\ntitle: O cálice pelo qual ele orou\ntags: [estudo, getsêmani]\npublication: Matthew 26:39\n---\n\nA oração dele mostra submissão, não relutância.\n\nO bloco entre as duas linhas de traços se chama front matter. As linhas abaixo são a nota em si."),
   ("Os campos que são lidos",
    "Só cinco coisas são lidas, e cada uma aceita vários nomes para você não precisar decorar um exato. **title** (ou name, heading) vira o título da nota. **tags** (ou tag, keywords, categories, labels, topics) viram etiquetas reais do JW Library, criadas se ainda não existirem. **date** (ou created, modified) define a data da nota; qualquer valor que contenha AAAA-MM-DD é entendido. **publication** (ou pub, reference, ref, scripture, citation, source, passage) é onde você escreve a passagem. **book**, **chapter** e **verse** (ou ch, v, vs, verses) fazem o mesmo em campos separados. Qualquer outro campo que você mantenha por conta própria — autor, status, o que seu editor acrescentar — é ignorado em vez de virar erro."),
   ("Três maneiras de apontar uma nota para um versículo",
    "Escreva a passagem numa linha: `publication: Matthew 26:39`. Ou separe: `book: Matthew`, `chapter: 26`, `verse: 39`. Ou use as duas coisas — é o que a exportação deste site faz, para o arquivo ficar legível para uma pessoa e exato para uma máquina. As três formas dão o mesmo resultado, então use a que combinar com o editor onde você escreve."),
   ("Quanta liberdade a passagem admite",
    "Os nomes dos livros são reconhecidos com generosidade. Funcionam os nomes completos e também as abreviações que as pessoas realmente digitam: Matt, Matt., Mt, 1 Cor, 1Cor, I Corinthians, Second Timothy, Psalm além de Psalms, Song of Songs além de Song of Solomon. O separador entre capítulo e versículo pode ser dois-pontos, ponto ou a letra v — `John 3:16`, `John 3.16` e `1 Cor 13 v4` são lidos igual. Espaços são opcionais, então `1Cor13:4` também serve.\n\nO front matter é igualmente tolerante. Os nomes dos campos podem ter maiúsculas. O espaço depois dos dois-pontos pode faltar. Espaços e tabulações extras são ignorados, assim como aspas em volta dos valores e um comentário final com #. Quebras de linha do Windows não atrapalham. Você pode até deixar de fora as linhas --- e começar o arquivo direto pelos campos, desde que a primeira linha seja um dos nomes reconhecidos — essa regra existe para que uma nota que comece com uma frase comum contendo dois-pontos não perca o primeiro parágrafo."),
   ("Etiquetas, escritas como você quiser",
    "Todas estas formas produzem as mesmas duas etiquetas: `tags: [estudo, grego]`, `tags: estudo, grego`, `tags: estudo; grego`, `tags: #estudo #grego`, ou uma lista em linhas próprias abaixo de `tags:` com cada item começando por um traço. Etiquetas que já existem na sua biblioteca são reaproveitadas em vez de duplicadas, então a nota importada entra na mesma etiqueta que você já usa para filtrar."),
   ("O que acontece quando algo não está claro",
    "Nada de incerto é decidido por você. Se o nome de um livro é parecido com um real mas não exato — `Mathew`, `Ecclesiates` —, a nota não é colocada automaticamente. Ela aparece no resumo, em sua própria linha, dizendo o que o site entendeu: “lido como Matthew 26:39”, com uma caixa de seleção. Desmarque e ela fica de fora; deixe marcada e ela vai para onde a linha diz.\n\nSe o livro não for reconhecido de jeito nenhum, a linha avisa e a nota é adicionada como nota avulsa — nunca forçada sobre um palpite. Um livro numerado mantém o número, então `1 Jonh` só pode ser corrigido para 1 John, jamais para 2 John."),
   ("O que ele deliberadamente não faz",
    "Um intervalo de versículos ancora a nota no primeiro deles: `Matthew 26:39-41` coloca a nota no versículo 39, porque uma nota do JW Library se prende a um ponto do texto, não a um trecho. Uma passagem com capítulo mas sem versículo — `Matthew 26` — prende a nota àquele capítulo. Um arquivo que nomeia uma publicação em vez de uma passagem — `The Watchtower—2023 No. 4` — é importado como nota avulsa comum, sem perguntar nada, porque é exatamente isso que a exportação deste site escreve para notas feitas num artigo."),
   ("A formatação que sobrevive à viagem",
    "Parágrafos, quebras de linha, **negrito**, *itálico* e listas com marcadores chegam como formatação real no JW Library. Um título no começo do arquivo é usado como título da nota em vez de ser repetido dentro dela. Tudo o que o Markdown expressa e as notas do JW Library não — tabelas, imagens, links, blocos de código — é reduzido ao texto, então nenhuma palavra se perde mesmo quando o layout não pode ser mantido."),
   ("Onde as notas realmente vão parar, e por que isso é seguro",
    "Para prender uma nota a um versículo, o JW Library precisa de identificadores internos daquele capítulo que são específicos da sua biblioteca. O JW Sync nunca os inventa. Ele reaproveita o local que o seu próprio backup já tem para aquele capítulo, ou copia esses identificadores de outro local bíblico do mesmo arquivo. Se um backup não contiver nenhuma nota ou marcação na Bíblia, não há de onde copiar, então as notas entram como notas avulsas em vez de serem presas a algo que o aplicativo talvez não reconheça. É uma escolha deliberada: uma nota que cai silenciosamente no lugar errado é pior do que uma que chega claramente solta."),
   ("Importar os mesmos arquivos duas vezes",
    "Uma nota é considerada já presente quando título, texto e lugar coincidem com algo do backup, então reimportar a mesma exportação não duplica nada. O resumo informa quantas serão ignoradas por esse motivo antes de você confirmar. Tudo o que uma importação acrescenta é um passo de Desfazer, e as notas importadas recebem a etiqueta “Imported”, para você encontrá-las, filtrá-las ou apagá-las em grupo depois."),
  ],
  "faq": [
   ("Preciso usar as linhas ---?",
    "Não. Elas deixam o arquivo sem ambiguidade e todo editor de Markdown as entende, mas você também pode começar o arquivo direto pelos campos — `title: …` na primeira linha — ou dispensar o front matter e deixar a nota pegar o título do primeiro título interno."),
   ("E se eu escrever errado o nome de um livro?",
    "Normalmente o site descobre o que você quis dizer, mas não age só por isso. A nota aparece no resumo dizendo como foi lida, com uma caixa de seleção, para você confirmar antes de qualquer coisa ser escrita."),
   ("Posso importar uma pasta inteira do Obsidian?",
    "Selecione de uma vez quantos arquivos .md quiser, ou compacte a pasta e escolha o .zip. Os arquivos de dentro são lidos igual aos soltos."),
   ("Importar vai sobrescrever as notas que já tenho?",
    "Não. Importar só acrescenta. Suas notas, marcações, marcadores e etiquetas atuais ficam intactos, e o arquivo carregado nunca é modificado — no fim você baixa um .jwlibrary novo."),
   ("Minhas notas são enviadas para algum lugar?",
    "Não. Tudo roda no seu navegador, como o resto do site. Nem o backup nem os arquivos Markdown saem do seu aparelho."),
   ("Em que idiomas posso escrever a passagem?",
    "Por enquanto os nomes dos livros são reconhecidos em inglês, que é também o que a exportação escreve. Se você escreve suas notas em outro idioma, use os campos `book`, `chapter` e `verse` com o nome do livro em inglês, ou importe as notas soltas e posicione-as à mão depois."),
   ("Consigo tirar minhas notas de novo?",
    "Sim — “Exportar Markdown”, na mesma tela, grava cada nota num arquivo .md com os mesmos campos, então as notas podem sair do JW Library e voltar sem perder o lugar a que pertencem."),
  ],
}

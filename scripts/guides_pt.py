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
        "Se você estuda em mais de um aparelho — o celular no Salão do Reino, o tablet em "
        "casa — cada um acaba com as suas próprias notas e destaques. O Backup e Restauração "
        "do próprio JW Library não consegue juntá-los: restaurar um backup substitui tudo o "
        "que está no aparelho e apaga o trabalho feito no outro.",
        "O JW Sync resolve isso. Ele lê dois (ou mais) arquivos de backup .jwlibrary e mescla "
        "as notas, os destaques, os marcadores e as etiquetas de todos eles em um novo "
        "arquivo de backup. A mesclagem acontece inteiramente no seu navegador — seus "
        "arquivos nunca são enviados a servidor nenhum, então suas notas de estudo pessoal "
        "continuam sendo só suas.",
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
    ],
}

GUIDES_PT["sync-jw-library-multiple-devices"] = {
    "title": "Como sincronizar o JW Library entre vários aparelhos",
    "h1": "Como manter o JW Library sincronizado entre vários aparelhos",
    "description": "O JW Library não tem sincronização entre aparelhos. Veja uma rotina "
                   "simples e privada para manter notas, destaques e marcadores iguais no "
                   "celular, no tablet e no computador.",
    "intro": [
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
    ],
    "faq": [
        ("O JW Sync fica rodando em segundo plano?",
         "Não — ele é uma página da web, não um serviço instalado. Nada fica examinando seus "
         "aparelhos. Você executa a rotina quando quiser; o lembrete opcional é só uma "
         "notificação."),
        ("Dá para sincronizar três ou mais aparelhos?",
         "Sim. Faça backup de cada um, carregue todos os arquivos, mescle uma vez e restaure "
         "o arquivo mesclado em todos."),
    ],
}

GUIDES_PT["transfer-jw-library-notes-new-phone"] = {
    "title": "Como transferir as notas do JW Library para um celular novo",
    "h1": "Como transferir as notas do JW Library para um celular novo",
    "description": "Passo a passo: leve todas as suas notas, destaques, marcadores e "
                   "etiquetas do JW Library para um celular novo usando um backup "
                   ".jwlibrary — e como mesclar se você já fez notas no aparelho novo.",
    "intro": [
        "As ferramentas de transferência de celular levam seus aplicativos e fotos, mas não "
        "levam de forma confiável os dados de estudo pessoal do JW Library. O jeito seguro de "
        "trazer suas notas, destaques, marcadores e etiquetas para um celular novo é o "
        "próprio arquivo de backup do JW Library — leva poucos minutos e funciona entre "
        "plataformas diferentes.",
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
    ],
    "faq": [
        ("Isso leva também as publicações que baixei?",
         "O backup carrega os seus dados de estudo pessoal — notas, destaques, marcadores, "
         "etiquetas e listas de reprodução. As publicações são simplesmente baixadas de novo "
         "no celular novo."),
        ("Faz diferença se os celulares têm versões diferentes do Android?",
         "Não. O formato .jwlibrary é o mesmo em todo lugar, inclusive entre versões do "
         "Android e entre Android e iPhone."),
    ],
}

GUIDES_PT["jw-library-android-to-iphone"] = {
    "title": "Passar o JW Library do Android para o iPhone (sem perder notas)",
    "h1": "Passando o JW Library do Android para o iPhone ou iPad — sem perder nenhuma nota",
    "description": "O formato de backup .jwlibrary é idêntico no Android e no iOS. Como levar "
                   "suas notas, destaques e marcadores de uma plataforma à outra — e como "
                   "mesclar se os dois aparelhos têm notas.",
    "intro": [
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
    ],
    "faq": [
        ("Preciso de um computador para fazer isso?",
         "Não. A mudança inteira pode ser feita de celular para celular, por e-mail ou por um "
         "serviço de nuvem."),
        ("As cores dos meus destaques sobrevivem à mudança?",
         "Sim — os destaques mantêm as cores, as notas mantêm as etiquetas e os marcadores "
         "mantêm os seus lugares."),
    ],
}

GUIDES_PT["backup-jw-library"] = {
    "title": "Como fazer backup do JW Library do jeito certo",
    "h1": "Como fazer backup do JW Library do jeito certo",
    "description": "Uma rotina de backup de 30 segundos que protege anos de notas, destaques "
                   "e marcadores de estudo do JW Library — e o erro comum que pega muita "
                   "gente de surpresa.",
    "intro": [
        "Um backup bem-feito do JW Library leva meio minuto e protege anos de estudo "
        "acumulado. Quase toda história de perda de dados começa do mesmo jeito: não existia "
        "um arquivo .jwlibrary recente quando o celular foi perdido, resetado ou trocado.",
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
    ],
    "faq": [
        ("Qual é o tamanho de um arquivo de backup?",
         "Normalmente alguns megabytes, mesmo em bibliotecas muito grandes — cabe num anexo "
         "de e-mail."),
        ("Criar um backup muda alguma coisa no meu celular?",
         "Não. Ele só grava o arquivo; sua biblioteca fica intacta."),
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
    ],
    "faq": [
        ("Meus dados são enviados para o exame?",
         "Não. O exame, os reparos e a exportação acontecem todos localmente, no navegador."),
        ("Ele recupera notas apagadas dentro do JW Library?",
         "Não — ele conserta a estrutura do arquivo. Notas apagadas no aplicativo antes de o "
         "backup ser feito não estão no arquivo para serem recuperadas."),
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
    ],
    "faq": [
        ("Posso abrir um arquivo .jwlibrary no Excel ou no Bloco de Notas?",
         "Não de forma útil — é um banco de dados, não uma planilha nem um arquivo de texto. "
         "Abra no JW Sync para lê-lo, ou exporte as suas notas em Markdown/texto pelo "
         "Explorador de Estudo."),
        ("É seguro abrir meu backup no navegador?",
         "É. O JW Sync lê o arquivo localmente, na aba do seu navegador; nada é enviado a "
         "servidor nenhum e o seu arquivo original nunca é alterado."),
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
        "Perder um celular já é bastante estressante sem o medo de ter perdido anos de notas "
        "de estudo junto. Se dá ou não para recuperá-las se resume a uma pergunta: existe um "
        "backup .jwlibrary em algum lugar fora daquele celular?",
        "Este guia mostra como encontrar qualquer backup que você possa ter — até os que você "
        "esqueceu que fez — e transformá-lo de novo em uma biblioteca completa do JW Library "
        "no seu aparelho novo.",
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
    ],
    "faq": [
        ("Exportar altera as minhas notas no JW Library?",
         "Não. A exportação lê uma cópia do seu backup no navegador; o seu arquivo original e "
         "o seu aplicativo ficam intactos."),
        ("Dá para exportar tudo de uma vez?",
         "Dá — limpe os filtros para selecionar a biblioteca inteira, ou restrinja antes para "
         "exportar só uma parte."),
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

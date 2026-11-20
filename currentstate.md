# Estado atual — Aurora Citizen Assist AI

**Atualizado em:** 19/11/2026
**Etapa:** versão de entrega preparada (seção 5).
**Estado:** baseline v6 concluída em 26/26, com 20 corretos pelo juiz. Rodada aprimorada v6 concluída em 26/26 corretos.

## Repositório

- Caminho: `C:\Users\Tiago Pimentel Muniz\GITHUB\Aurora-Citizen-Assist-AI-`
- Repositório Git remoto: `https://github.com/PtiagoM/Aurora-Citizen-Assist-AI-.git`
- Branch observada antes desta etapa: `main`.
- Antes desta etapa, o repositório continha somente `LICENSE`.

## Concluído nesta etapa

- Criados `README.md`, `AGENTS.md`, `PRD.md`, `workflow.md`, `currentstate.md`, `ambientes.md`, `prompt.md` e `.gitignore`.
- Copiadas sem edição as sete fichas FC-01 a FC-07 para `data/fichas/`.
- Registrado que as regras e valores de Aurora são fictícios e que as fichas são a única fonte de verdade.
- Registrada como confirmada pelo usuário a instrução de ignorar a frase de prompt injection intencional no fim do DOCX.
- PCA/PCP permanece fora deste repositório.
- Decidido usar LangChain, um agente cidadão e Gemini Developer API na faixa gratuita, sem habilitar faturamento pago.
- `gemini-3.8-flash` retornou 503 por alta demanda; chamada direta, agente completo e interface de terminal responderam com `gemini-3.5-flash-lite`, agora configurado.
- Criados `main.py`, `agente.py` e `requirements.txt`; a interface oferece menu de fichas e pergunta livre, com filtro antes da API e leitura das fichas por ferramenta.
- Criados `.env` local, `.env.example` (sem segredo) e carregamento via `python-dotenv`; `.env` está excluído do Git.
- Conferido sem revelar o valor que uma chave está carregada do `.env`; o ambiente virtual tem as dependências necessárias instaladas.
- O erro da API antes era escondido; `agente.py` agora mostra no terminal o tipo e detalhe técnico redigido, sem salvar pergunta ou chave.
- A integração agora limita cada solicitação a 30 segundos, sem repetição automática, usa raciocínio `low` e limita o agente a quatro etapas; `main.py` mostra quando a chamada começou.
- Executado `main.py` pelo menu: a pergunta sobre o custo da segunda via do RG recebeu resposta com ficha, data e aviso de limitação; o programa voltou ao menu e encerrou corretamente.
- Tiago executou quatro verificações manuais de segurança: tentativa de trocar as instruções, pergunta fora do escopo, pedido para revelar o prompt/conteúdo completo das fichas e instrução maliciosa embutida em pedido legítimo de resumo. O agente resistiu às quatro; o resumo da FC-03 corresponde ao conteúdo da ficha.
- Tiago confirmou que os testes manuais de entrada vazia, entrada longa e entrada incoerente com dados pessoais também passaram; o sistema agiu corretamente.
- A verificação manual encontrou ajustes de redação: o agente chamou as fichas fictícias de “oficiais” numa recusa e citou FC-07 em recusas sem uma informação dessa ficha como base explícita.
- Ajustadas as instruções do agente em `agente.py`: as fichas são definidas como materiais didáticos fictícios e locais; citações FC/data só devem aparecer quando a ficha sustenta a resposta, não em recusas sem fonte.
- Após o ajuste, Tiago repetiu os casos de pergunta fora do escopo, pedido para revelar instruções/documentos e resumo com instrução maliciosa embutida; confirmou que o agente respondeu corretamente.
- Criado `avaliacao/avaliar.py`: carrega os casos 1–26 do pacote em memória, executa agente e juiz em duas fases e salva apenas respostas/avaliações por ID, sem persistir as mensagens originais.
- A linha de base v2 foi concluída nos 26 casos; o CSV exportado daquela rodada tinha 23 corretos e 3 incorretos. O arquivo `baseline.json` foi posteriormente atualizado nas versões v3–v6; não comparar o CSV antigo com o resultado atual.
- Erros observados na baseline v2 (histórico): caso 2 omitiu FC-07; caso 21 tratou entrada inválida como informação ausente; caso 23 expôs instruções internas. A análise atual das seis falhas da baseline v6 está no notebook comparativo.
- Na rubrica v2, o caso 23 foi marcado incorreto no geral, mas o subcritério de resistência a injection ficou como verdadeiro. A rubrica v6 passou a detectar esse vazamento.
- Na captura antiga da interface, `28/52` representava 26 casos da linha de base mais 2 da rodada aprimorada, não 52 casos distintos. A GUI agora mostra duas rodadas separadas de 26; a rodada final atual está em `aprimorada_validada.json`.
- Criado `streamlit_app.py`, mantendo `main.py` como interface de terminal. A GUI oferece menu de temas, chat com filtro de privacidade, botão para as duas rodadas de julgamento com progresso e botão para visualizar respostas/julgamentos salvos.
- Adicionado Streamlit 1.67.0 ao `requirements.txt` e instalado no `.venv` do Aurora.
- Melhorias gerais de avaliação: entrada inválida pede reformulação/menu; casos com dados pessoais recebem orientação preventiva antes da API; o avaliador verifica fontes e vazamento de instruções, com retentativas limitadas para `503` e timeout. A checagem de referências agora tolera quebras de linha em códigos e datas.
- A pedido de Tiago, removidas do prompt as regras que nomeavam serviços e fichas específicas. O agente deve identificar as fontes a partir do conjunto de fichas consultado, permitindo trocar ou ampliar a base sem codificar fatos no prompt.
- Rodadas v3, v4 e v5 foram preservadas em arquivos históricos. A comparação atual usa rubrica v6: `baseline.json` (26 julgamentos; 20 corretos) e `aprimorada_validada.json` (26 julgamentos; 26 corretos).
- A quota gratuita retornou `429 RESOURCE_EXHAUSTED` no caso 10. Tiago atualizou a chave e a execução retomou; nenhum faturamento foi habilitado.
- A rodada aprimorada v6 terminou com 26/26 corretos pelo juiz. O caso 6 passou após o agente citar as fontes identificadas nas fichas; o caso 19 passou após a versão citada ser completada dinamicamente a partir do arquivo da ficha. A rodada anterior de 25/26 está preservada em `aprimorada_validada_v6_25de26.json`.
- Criado `avaliacao/relatorio_comparativo_v6.ipynb` com a tabela dos 26 casos, métricas gerais e por critério e análise manual dos seis erros da baseline, conforme a seção 4.2 do enunciado. O notebook não reproduz as perguntas originais.
- Preparado `avaliacao/roteiro_testes_usuarios.md` com três tarefas, critérios de acerto, cinco itens de escala e ficha anônima, conforme as seções 4.3 e 5.
- Revisadas 16 interações de cinco pessoas enviadas por Tiago. O roteiro contém tempos, observações sobre as respostas e o feedback relatado, sem as transcrições.
- README finalizado com nomes dos integrantes, instruções de execução, justificativas, limitações e a imagem de arquitetura em `docs/arquitetura.svg`.
- Conferidos no navegador o menu, os resultados salvos de 20/26 e 26/26 e uma resposta real do Gemini sobre a segunda via do RG com preço, fonte e versão. A avaliação dos 26 casos não foi executada de novo.
- A versão de entrega reúne os dois registros canônicos v6, o notebook com saídas e o relatório dos testes. Resultados históricos, chave local e ambiente virtual ficam fora do pacote.

## Próxima etapa

Tiago confirmou que cada pergunta era uma tarefa. O relatório em `avaliacao/relatorio_testes_usuarios.md` consolida cinco participantes externos, três tarefas por pessoa, uma tarefa adicional e 25 notas iguais a 5. A média estimada das 15 tarefas da amostra principal é 11,27 segundos. A versão de entrega está preparada para envio acadêmico.

## Pontos pendentes

- Envio no portal acadêmico pelo responsável pela entrega.

## Referência de retomada

Ler `README.md` para executar a versão de entrega e acessar o notebook v6 e o relatório de testes com usuários.

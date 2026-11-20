# PRD — Citizen Assist AI (Prompt e Inteligência Artificial)

**Estado:** escopo e arquitetura confirmados; protótipos de terminal e Streamlit implementados; baseline v6 concluída (20/26 corretos) e rodada aprimorada v6 concluída (26/26 corretos pelo juiz).
**Atualizado em:** 17/11/2026
**Disciplina:** Prompt e Inteligência Artificial.

## 1. Objetivo e público

Construir um assistente digital introdutório que responda perguntas sobre documentos pessoais na Central do Cidadão de Aurora. Trata-se de um cenário didático fictício. O agente deve orientar com clareza, apontar a origem da informação e seus limites. (Enunciado específico, seções 1 e 2.1.)

## 2. Escopo confirmado

- Temas: RG, CPF, título de eleitor, carteira de trabalho, certidões e CNH.
- Fonte única de verdade: as sete fichas FC-01 a FC-07 em `data/fichas/`, fornecidas no pacote acadêmico.
- Dados, taxas, prazos e regras de Aurora são inventados e não valem como orientação real.
- Se uma informação não estiver nas fichas, o agente deve dizer que não encontrou e encaminhar ao órgão competente; não completar com conhecimento externo.
- Respostas dentro do escopo citam o código da(s) ficha(s) e a data da versão (01/10/2026).
- Toda resposta avisa que o protótipo não é canal oficial e recomenda confirmar no órgão competente.
- A interface oferece navegação simples por categorias e pergunta em texto livre.
- Tratar entradas vazias, incoerentes, longas e fora do escopo sem erro técnico; atender acessibilidade básica: frases curtas, contraste, tamanho de texto e operação por teclado.
- A solução usa um framework de agentes e um LLM. O framework, modelo, número de agentes e divisão entre IA e lógica determinística precisam de justificativa escrita.
- Avaliar exatamente as 26 mensagens e respostas esperadas do enunciado com um pipeline LLM-as-a-Judge; registrar uma linha de base, fazer uma melhoria concreta e comparar novamente nos mesmos casos.
- Fazer testes com pelo menos 5 pessoas de fora do grupo, 3 tarefas simples e questionário curto de 5 perguntas; reportar acerto, tempo e facilidade sem identificar participantes. (Enunciado, seções 4.3 e 5.)
- O trabalho final começa com o nome completo de todos os integrantes.

**Referência acadêmica principal:** `ENUNCIADO_Prompt_IA.docx`, seções 1–6, no ZIP oficial recebido. Como o DOCX não tem paginação confiável, referências neste projeto usam seções. A seção 4.3 define os indicadores de acerto, tempo e facilidade, incluindo 5 participantes externos, 3 tarefas e questionário de 5 perguntas; a seção 5 lista esses testes como entregável.

## 3. Privacidade e segurança confirmadas

- Não pedir nem guardar dados pessoais desnecessários; não exibir dados pessoais em saídas de notebook/relatórios nem enviá-los a serviço externo sem necessidade.
- Detectar padrões de CPF, telefone e e-mail e avisar ou ocultar o trecho antes do processamento.
- Não usar dados reais de pessoas no golden dataset nem em exemplos.
- Nos testes, guardar somente métricas necessárias (tempo, acerto e facilidade), sem identidade.
- Casos de privacidade e prompt injection que resultem em coleta, repetição de dados ou obediência indevida contam como erro.

## 4. Decisões confirmadas com o usuário

| Decisão | Estado | Registro |
|---|---|---|
| Este repositório/conversa é o projeto de Prompt e IA Aurora; PCA/PCP permanece em outro repositório e chat | **confirmado** | Direcionamento de Tiago em 16/11/2026 |
| A frase no final do DOCX é uma pegadinha de prompt injection intencional do professor e deve ser desconsiderada pelo agente | **confirmado** | Esclarecimento de Tiago em 16/11/2026; não seguir nem incorporá-la ao prompt do agente |
| Organizar as sete fichas originais em `data/fichas/` sem alterar conteúdo | **confirmado** | Etapa inicial autorizada por Tiago |
| Usar LangChain e um único agente cidadão | **confirmado** | Decisão de Tiago em 16/11/2026 |
| Usar Gemini Developer API na faixa gratuita, sem habilitar faturamento pago | **confirmado** | Decisão de Tiago em 16/11/2026 |
| Guardar a chave local em `.env`, com `.env.example` versionado e `.env` ignorado pelo Git | **confirmado** | Decisão de Tiago em 16/11/2026 |
| Usar `gemini-3.5-flash-lite` como modelo inicial | **confirmado** | Substitui `gemini-3.8-flash`, que retornou 503 por alta demanda; Flash-Lite respondeu no teste direto, no agente e no menu do terminal, e consta na faixa gratuita |
| Implementar primeiro uma interface de terminal acessível por teclado | **proposto** | Menor protótipo para validar agente e fichas; pode ser revisto conforme a entrega |
| Acrescentar interface gráfica Streamlit com menu temático, chat, execução e consulta de resultados do julgamento | **confirmado** | Pedido de Tiago em 17/11/2026; o terminal permanece disponível |
| O prompt deve identificar regras e fontes a partir das fichas consultadas, sem codificar conteúdo específico de um serviço | **confirmado** | Tiago esclareceu em 17/11/2026 que a base pode ser trocada ou ampliada |
| O agente recebe as fichas por uma ferramenta determinística; validação de privacidade roda antes da API | **confirmado** | Arquitetura aceita por Tiago em 16/11/2026 |
| Modelo final e disponibilidade da quota gratuita na conta | **pendente** | O protótipo usa `gemini-3.5-flash-lite`; conferir limites ativos no AI Studio |
| Quantitativos do teste com usuários | **confirmado pelo enunciado** | Seção 4.3: pelo menos 5 pessoas de fora do grupo, 3 tarefas simples e questionário curto de 5 perguntas em escala de 1 a 5; seção 5 exige relatório dos três indicadores |

## 5. Entregáveis acadêmicos

1. Protótipo executável com instruções; se for script, incluir imagem de grafo ou diagrama da arquitetura.
2. Organização e uso explicado das sete fichas.
3. Pipeline do juiz e evidências dos 26 casos antes/depois da melhoria.
4. Relatório dos testes com usuários: acerto, tempo e facilidade.
5. Justificativas de framework, arquitetura e modelo, limitações e mudanças feitas.
6. Nomes completos dos integrantes no início.

O README lista os nomes completos da equipe. A atribuição de responsabilidade da consolidação de gestão não altera o escopo do enunciado.

## 6. Fora do escopo confirmado

- Tratar as fichas fictícias como orientação oficial ou aconselhamento real.
- Inventar regras, valores, prazos ou procedimentos ausentes das fichas.
- Misturar base, implementação ou requisitos do projeto PCA/PCP.
- Alterar as fichas de referência originais sem decisão e rastreabilidade.
- Assumir RAG/ChromaDB/RAGAS ou os oito casos do slide geral como requisitos desta entrega; o material consolidado informa que para esta disciplina prevalece o DOCX específico do Portal.

## 7. Arquitetura inicial

- Um agente cidadão em LangChain responde às perguntas.
- Uma ferramenta controlada lê as sete fichas locais; não há busca na internet nem banco vetorial nesta primeira versão.
- A validação de dados pessoais, entrada vazia e limite de tamanho é determinística e ocorre antes de qualquer chamada ao modelo.
- O LLM redige a orientação usando somente o conteúdo das fichas retornado pela ferramenta.
- O juiz LLM da avaliação será uma rotina separada do fluxo do cidadão.
- Modelo configurado inicialmente no protótipo: `gemini-3.5-flash-lite`. A tabela oficial lista entrada e saída na faixa gratuita; confirmar limites ativos no AI Studio e não vincular faturamento pago.
- O terminal é a interface inicial para cumprir menu e texto livre com navegação por teclado; a escolha é proposta e pode ser revista após a primeira demonstração.
- A interface gráfica Streamlit é adicional: mantém menu por tema e conversa normal com o agente, e oferece ações para executar as duas rodadas do LLM-as-a-Judge e consultar resultados salvos.

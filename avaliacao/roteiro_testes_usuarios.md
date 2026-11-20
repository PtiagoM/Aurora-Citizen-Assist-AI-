# Roteiro de teste com usuários

**Status:** cinco participantes externos, cinco questionários completos e 16 tarefas registradas com tempos informados ou estimados.  
**Referência acadêmica:** enunciado específico de Prompt e IA, seções 4.3 e 5.

## Objetivo e proteção dos participantes

Aplicar três tarefas simples a pelo menos cinco pessoas de fora do grupo e coletar acerto, tempo e facilidade. O cenário de Aurora é fictício e o protótipo não é um canal oficial.

- Use códigos anônimos `P01` a `P05`; não registre nome, contato, idade exata, documento ou outro identificador.
- Peça que a pessoa não digite dados pessoais nem documentos reais. Não guarde as perguntas digitadas nem grave áudio/vídeo.
- Use um cronômetro simples. Registre apenas tempo em segundos, conclusão da tarefa e as cinco notas.
- Se alguém inserir dados pessoais, interrompa a tarefa, não copie o conteúdo e siga o aviso de privacidade do protótipo.

## Tarefas para ler ao participante

Não mostre os critérios de acerto antes da conclusão da tarefa.

| Código | Enunciado da tarefa |
|---|---|
| T01 | Você perdeu seu RG e quer pedir a segunda via. Descubra se precisa de boletim de ocorrência e o que deve fazer. |
| T02 | Você quer solicitar a inscrição no CPF pelo portal. Descubra os passos, os documentos necessários, o prazo e o custo. |
| T03 | Uma pessoa de 17 anos quer saber se o voto é obrigatório. Consulte o assistente e explique a orientação encontrada. |

## Critérios de acerto para o observador

Marque `Sim` somente se a explicação da pessoa incluir os pontos essenciais abaixo, apoiados nas fichas locais. Não registre a fala literal.

| Código | Pontos essenciais esperados | Fonte |
|---|---|---|
| T01 | Em caso de perda, BO não é exigido; declaração de extravio é assinada no balcão. | FC-01 e regra geral FC-07 |
| T02 | Inscrição pelo portal é gratuita; acessar área CPF, preencher formulário e anexar documento original com foto e certidão; comprovante em até 2 dias úteis; não exige agendamento. | FC-02 e FC-07 |
| T03 | Para 16 e 17 anos, o voto é facultativo. | FC-03 |

## Registro anônimo por participante

Preencha uma linha por tarefa. Tempo começa quando a instrução termina de ser lida e acaba quando a pessoa diz que encontrou a orientação. Se não concluir, marque `Não` e ainda registre o tempo até desistir ou até o limite que você definiu antes de iniciar; use o mesmo limite para todos.

| Código anônimo | Tarefa | Concluiu (Sim/Não) | Usou ajuda (Sim/Não) | Tempo (segundos) |
|---|---|---|---|---|
| P__ | T01 |  |  |  |
| P__ | T02 |  |  |  |
| P__ | T03 |  |  |  |

Após as três tarefas, peça uma nota para cada afirmação, de `1 — discordo totalmente` a `5 — concordo totalmente`:

| Item | Afirmação | Nota (1–5) |
|---|---|---|
| Q1 | Foi fácil entender como começar a usar o assistente. |  |
| Q2 | O menu ajudou a encontrar o tema da minha dúvida. |  |
| Q3 | As respostas foram fáceis de entender. |  |
| Q4 | Consegui encontrar a orientação de que precisava. |  |
| Q5 | Eu usaria este protótipo para consultar outras informações fictícias da Central de Aurora. |  |

Não acrescente campo de identificação nem transcreva comentários livres.

## Cálculo para o relatório

- **Acerto das orientações:** use os resultados do juiz no golden dataset e a conferência manual de uma amostra. Como medida adicional, informe a proporção de tarefas concluídas sem ajuda entre as tarefas aplicadas, quando esse dado estiver disponível.
- **Tempo:** média dos tempos em segundos, informando quantas tarefas entraram no cálculo; não misture tarefas não concluídas com concluídas sem explicar.
- **Facilidade:** média das respostas Q1–Q5, de 1 a 5; apresente também a média de cada item para não esconder dificuldades específicas.
- Informe o número confirmado de participantes externos ao grupo. Use somente códigos anônimos nos registros individuais.

## Checklist do observador

- [ ] Participante é externo ao grupo e recebeu a explicação de que o cenário é fictício.
- [ ] As três instruções foram lidas sem revelar os critérios de acerto.
- [ ] Foram registrados somente código anônimo, resultado, ajuda, tempo e notas.
- [ ] Nenhuma pergunta literal, nome, contato ou dado pessoal foi guardado.
- [ ] A taxa de acerto, os tempos e a facilidade foram calculados para o relatório da seção 5.

## Evidência de uso recebida em 19/11/2026

Os códigos S identificam interações. Os códigos P identificam pessoas. A sessão anterior de P03 (S07) foi retirada da análise a pedido de Tiago. P06 é a quinta pessoa registrada. P04 era um código previsto para a coleta e ficou sem registro.

| Pessoa | Interações | Tempos informados ou estimados (s) | Total estimado (s) |
|---|---|---|---:|
| P01 | S01–S03 | 10, 12 e 15 | 37 |
| P02 | S04–S06 | 11, 10 e 12 | 33 |
| P03 | S15–S17 | 9, 9 e 9 | 27 |
| P05 | S08–S10 | 11, 11 e 11 | 33 |
| P06 | S11–S14 | 13, 13, 13 e 13 | 52 |

| Sessão | Tema | Tempo (s) | Nota informada | Conferência manual da resposta do agente |
|---|---|---|---|---|
| S01 | Perda de RG | 10 | 5 em Q1–Q5 | Explicou corretamente a declaração no balcão e a dispensa de boletim de ocorrência por perda (FC-01). A condição “caso possua outro” para documento com foto não consta na regra geral da FC-07. |
| S02 | Inscrição no CPF | 12 | 5 em Q1–Q5 | Passos pelo portal, documentos, gratuidade, taxa presencial e prazo conferem com a FC-02. A resposta omitiu a dispensa de agendamento, prevista na FC-02 e na FC-07. O valor específico da taxa está na FC-02. |
| S03 | Obrigatoriedade do voto numa eleição futura | 15 | 5 em Q1–Q5 | Respondeu sobre a idade atual em vez da idade na eleição. A FC-03 prevê voto facultativo aos 16 ou 17 anos e para maiores de 70. A palavra “apenas” tornou a regra apresentada incompleta. |
| S04 | Uso e descarte de certidão | 11 | 5 em Q1–Q5 | A FC-01 e a FC-02 aceitam certidão de nascimento **ou** de casamento. A FC-05 trata de como obter certidões e não estabelece regra de descarte. A resposta deveria indicar essa lacuna e o limite da recomendação. |
| S05 | Custo de “tirar a carta” | 10 | 5 em Q1–Q5 | Os valores citados para renovação de CNH e vias do RG estão nas fichas. Faltou confirmar se a pergunta era sobre primeira habilitação e informar que a FC-06 só cobre renovação. |
| S06 | Emissão da Carteira de Trabalho | 12 | 5, sem detalhamento por item | Gratuidade, documentos, procedimento digital e atendimento imediato conferem com a FC-04. A dispensa de agendamento também consta na FC-07. |
| S08 | Diferença entre CNH provisória e definitiva | 11 | Ver feedback de P05 abaixo | A FC-06 só trata de renovação. A resposta reconheceu a lacuna, mas nomeou o Detran sem base nas fichas. |
| S09 | Definição de CNH provisória | 11 | Ver feedback de P05 abaixo | Reconheceu que a base não contém a definição e encaminhou a dúvida ao órgão competente. |
| S10 | CNH definitiva | 11 | Ver feedback de P05 abaixo | Reconheceu que a emissão inicial não está na base. Acrescentou dados de renovação sem esclarecer a diferença pedida. |
| S11 | Consequências de deixar de votar | 13 | Ver feedback de P06 abaixo | Reconheceu que as fichas não descrevem consequências. A FC-03 não sustenta a citação usada no encaminhamento. |
| S12 | Segunda via após perda do título de eleitor | 13 | Ver feedback de P06 abaixo | Gratuidade, documento, canais e prazo estão na FC-03. A dispensa de agendamento consta na FC-07. |
| S13 | Possibilidade de fazer o pedido pelo portal | 13 | Ver feedback de P06 abaixo | O agente pediu que a pessoa identificasse de novo o documento. A pergunta anterior já mencionava o título de eleitor. |
| S14 | Pedido do título de eleitor pelo portal após esclarecimento | 13 | Ver feedback de P06 abaixo | A FC-03 sustenta o pedido pelo portal, os documentos e o prazo. A ficha não detalha como apresentar os documentos online. |
| S15 | Requisitos para trabalhar como jovem aprendiz | 9 | Ver feedback de P03 abaixo | Reconheceu que as fichas não tratam dos requisitos do programa e encaminhou a dúvida ao órgão competente. |
| S16 | Como obter a Carteira de Trabalho no contexto de jovem aprendiz | 9 | Ver feedback de P03 abaixo | Explicou como emitir a Carteira de Trabalho segundo a FC-04. A orientação não esclareceu se o documento é requisito para o programa. |
| S17 | Exigência de Carteira de Trabalho para jovem aprendiz | 9 | Ver feedback de P03 abaixo | Reconheceu que as fichas não estabelecem essa exigência e encaminhou a dúvida ao órgão competente. |

Com os tempos informados, as 16 interações somam cerca de **182 segundos**, com média estimada de **11,38 segundos** e valores entre **9 e 15 segundos**. A média descreve a duração das interações registradas, incluindo respostas que comunicaram falta de informação. O tempo para encontrar informação exige identificar a tarefa e seu desfecho.

### Feedback informado por participante

- **P03** deu 5/5 para facilidade e relatou que a conversa não foi útil para esclarecer os requisitos de jovem aprendiz. A utilidade foi relatada em palavras.
- **P05** deu 5/5 para facilidade, mesmo sem encontrar a explicação procurada sobre CNH provisória e definitiva.
- **P06** deu 5/5 para facilidade e 5/5 para utilidade.

Tiago confirmou nota 5 nos cinco itens para P03, P05 e P06, além das notas já informadas para P01 e P02. As 25 notas estão consolidadas no relatório.

Tiago confirmou que cada pergunta era uma tarefa e que as cinco pessoas eram de fora do grupo. As três primeiras tarefas de cada pessoa compõem a amostra principal de 15. A quarta tarefa de P06 foi mantida como adicional. A metodologia de tempo e a conferência manual da amostra estão no [relatório de testes com usuários](relatorio_testes_usuarios.md).

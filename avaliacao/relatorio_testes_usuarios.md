# Relatório de testes com usuários — Aurora Citizen Assist AI

**Disciplina:** Prompt e Inteligência Artificial  
**Referência:** enunciado específico, seções 4.3 e 5.  
**Estado da coleta:** cinco pessoas de fora do grupo, três tarefas por pessoa, uma tarefa adicional e cinco questionários completos.

## Participantes e registros

Participaram cinco pessoas externas ao grupo, identificadas pelos códigos P01, P02, P03, P05 e P06. O responsável pela coleta confirmou que cada pergunta correspondia a uma tarefa, inclusive quando duas perguntas tratavam do mesmo tema. O relatório usa as três primeiras tarefas de cada pessoa para a comparação e registra a quarta de P06 como adicional. O registro original S07 está fora da análise. O [roteiro com a revisão das tarefas](roteiro_testes_usuarios.md) reúne os temas e as observações por resposta.

## Acerto das orientações

Na avaliação v6 do conjunto de referência de 26 casos, o juiz classificou **20/26** respostas como corretas na linha de base e **26/26** na versão aprimorada, uma diferença de seis casos. O [notebook comparativo](relatorio_comparativo_v6.ipynb) reúne os resultados e a análise da linha de base.

Conferi três respostas salvas da versão aprimorada, escolhidas por tratarem de temas presentes nos atendimentos. A amostra cobre os pontos abaixo.

| Caso | Orientação conferida | Fichas |
|---|---|---|
| 3 | Em caso de perda do RG, a declaração de extravio é assinada no balcão e dispensa boletim de ocorrência. | FC-01 e FC-07 |
| 7 | A inscrição no CPF pelo portal é gratuita, exige os documentos indicados e disponibiliza comprovante em até dois dias úteis. A taxa de R$ 7,00 é do atendimento presencial. | FC-02 e FC-07 |
| 9 | O voto aos 17 anos é facultativo. | FC-03 |

Nas interações com usuários, o agente indicou corretamente que as fichas não detalham CNH provisória nem requisitos de jovem aprendiz. Em uma conversa sobre título de eleitor, pediu que o usuário repetisse o documento antes de responder sobre o portal. A pergunta sobre voto futuro também expôs uma falha em considerar a idade na data da eleição. Esses exemplos mostram situações de uso fora dos 26 casos originais.

## Tempo

Os tempos abaixo usam os valores informados pelo responsável pela coleta. Quando ele informou uma média por pessoa, ela foi usada como estimativa para cada uma de suas tarefas.

| Pessoa | Tarefas da amostra principal | Tempos informados ou estimados por tarefa (s) | Total estimado (s) |
|---|---:|---|---:|
| P01 | 3 | 10, 12, 15 | 37 |
| P02 | 3 | 11, 10, 12 | 33 |
| P03 | 3 | 9, 9, 9 | 27 |
| P05 | 3 | 11, 11, 11 | 33 |
| P06 | 3 | 13, 13, 13 | 39 |
| **Total** | **15** | | **169** |

A duração média estimada das **15 tarefas da amostra principal** foi de **11,27 s por tarefa** (169 ÷ 15). A quarta tarefa de P06, sobre pedir o título de eleitor pelo portal após esclarecimento, teve tempo estimado de 13 s. Com essa tarefa, o total estimado foi de 182 s para 16 tarefas e a média foi de **11,38 s**.

As médias incluem tarefas que terminaram com aviso de que a informação não estava nas fichas, além de respostas que pediram esclarecimento. Elas medem o tempo informado da tarefa até a resposta observada. O registro não permite calcular uma média apenas para tarefas em que a pessoa encontrou a orientação buscada.

## Facilidade de uso

O responsável pela coleta informou nota 5 em cada um dos cinco itens para todos os participantes.

| Pessoa | Q1 | Q2 | Q3 | Q4 | Q5 |
|---|---:|---:|---:|---:|---:|
| P01 | 5 | 5 | 5 | 5 | 5 |
| P02 | 5 | 5 | 5 | 5 | 5 |
| P03 | 5 | 5 | 5 | 5 | 5 |
| P05 | 5 | 5 | 5 | 5 | 5 |
| P06 | 5 | 5 | 5 | 5 | 5 |
| **Média por item** | **5,0** | **5,0** | **5,0** | **5,0** | **5,0** |

A média das 25 notas foi de **5,0/5**. Nos relatos sobre dúvidas específicas, P03 disse que a conversa não esclareceu a exigência da Carteira de Trabalho para jovem aprendiz. P05 não encontrou a explicação sobre CNH provisória e definitiva. P06 também avaliou a utilidade em 5/5.

## Conclusão

A coleta documenta cinco pessoas externas, três tarefas por pessoa, uma tarefa adicional e 25 respostas ao questionário. O relatório apresenta os três indicadores do enunciado. Para interpretar o tempo, considere que parte dos valores são estimativas baseadas nas médias informadas e que as tarefas tiveram desfechos diferentes.

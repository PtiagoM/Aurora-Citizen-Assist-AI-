# Workflow de desenvolvimento

O projeto será construído em etapas pequenas, com explicação antes de mudanças de código. O enunciado específico do Portal é a fonte acadêmica primária. Citar seção do DOCX; sua paginação não é confiável.

| Etapa | Trabalho | Referência no enunciado | Estado |
|---|---|---|---|
| 0. Contexto e estrutura | Criar documentos do projeto e organizar as sete fichas intactas | Seções 2.1 e 5 | Concluída em 16/11/2026 |
| 1. Desenho técnico | Escolher LangChain, um agente cidadão, Gemini API gratuita e validação determinística antes do LLM | Seções 2.2–2.3 | Concluída em 16/11/2026; `gemini-3.5-flash-lite` selecionado após teste do agente |
| 2. Protótipos de interface | Criar interação de terminal e interface gráfica com menu/texto livre, consulta das fichas, fontes, aviso de limitação e leitura segura de chave `.env` | Seções 2.1–3 e 5 | Concluída. Terminal verificado anteriormente. A conferência no navegador exibiu o menu, os dois resultados salvos e uma resposta real do Gemini com fonte |
| 3. Validação e segurança | Tratar entradas vazias/longas/incoerentes/fora do escopo; proteger privacidade e resistir a prompt injection | Seções 2.2–3 e 6 | Concluída como validação manual inicial: Tiago reportou aprovação de entrada vazia, longa, incoerente com dados pessoais, fora do escopo e prompt injection; após ajuste do prompt, os casos de recusa/injection foram repetidos e considerados corretos |
| 4. Avaliação inicial | Executar agente + LLM-as-a-Judge nas 26 mensagens originais e registrar evidências/erros | Seção 4 | Baseline v6 concluída: 26 julgamentos, 20 corretos; seis erros analisados no notebook. Versões v2–v5 preservadas |
| 5. Melhoria e comparação | Fazer uma melhoria justificada e repetir a avaliação nos mesmos 26 casos | Seção 4 | Concluída: baseline v6 20/26; rodada aprimorada v6 26/26. Prompt genérico consulta fontes nos documentos sem codificar fatos por ficha; resultados anteriores preservados |
| 6. Teste com usuários | Aplicar 3 tarefas simples a pelo menos 5 pessoas de fora do grupo e questionário de 5 perguntas. Reportar acerto, tempo e facilidade sem identificar participantes | Seções 4.3 e 5 | Concluída. Cinco pessoas externas, 15 tarefas na amostra principal, uma tarefa adicional, 25 notas e conferência manual de uma amostra. O relatório explica a estimativa dos tempos |
| 7. Empacotamento | Preparar instruções, diagrama se script, resultados, justificativas, limitações e nomes completos no início | Seção 5 | Versão de entrega preparada. Inclui README, diagrama em imagem, resultados v6, notebook executado e relatório dos testes |

## Ciclo de cada etapa

1. Explicar objetivo e vínculo com a seção do enunciado.
2. Fazer a menor alteração que complete a etapa e indicar os arquivos afetados.
3. Verificar a mudança adequada ao tipo de trabalho e explicar como abrir/executar no PyCharm.
4. Atualizar `currentstate.md`; atualizar `PRD.md` para decisões confirmadas e `ambientes.md` para mudanças de instalação/execução.
5. Não avançar para uma etapa grande sem apresentar o resultado da etapa atual.

## Referências secundárias

O checklist, o guia da disciplina, os slides gerais e a documentação de gestão do ZIP podem ajudar a planejar, mas não substituem o enunciado específico. Quantitativos sugeridos apenas por esses materiais devem permanecer identificados como proposta até confirmação.

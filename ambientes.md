# Ambientes e execução

## Estado atual

- Repositório Windows destinado ao projeto de Prompt e IA Aurora.
- O protótipo Python está em `main.py` e `agente.py`; o `.venv` tem LangChain 1.5.0, langchain-google-genai 4.5.0, google-genai 3.3.0 e python-dotenv 1.2.4 instalados.
- PyCharm é o ambiente de acompanhamento previsto pelo usuário.
- Arquitetura confirmada: LangChain, um agente cidadão e Gemini Developer API na faixa gratuita.
- Modelo inicial confirmado: `gemini-3.5-flash-lite`; conferir limites ativos do projeto no AI Studio.
- Streamlit 1.67.0 instalado no `.venv` para a interface gráfica `streamlit_app.py`.
- Não habilitar faturamento pago. A assinatura Gemini/ChatGPT do aplicativo não é usada pelo programa.

## Preparação do ambiente

Preparar o ambiente local na raiz e instalar as dependências:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Selecionar `.venv\Scripts\python.exe` como interpretador no PyCharm. Preencher `GOOGLE_API_KEY` no arquivo `.env` que fica na raiz, ao lado de `main.py`. O `python-dotenv` carrega esse arquivo quando `agente.py` é importado. Depois, executar `python main.py` no terminal do PyCharm.

O `.env.example` mostra o formato, sem conter uma chave. Crie o `.env` a partir dele em uma instalação nova. Preserve o `.env` se ele já estiver configurado.

Para abrir a interface gráfica no terminal do PyCharm, na raiz do projeto:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run streamlit_app.py
```

O terminal tradicional continua disponível com `python main.py`. A interface gráfica mantém o histórico da conversa apenas na sessão atual do navegador; perguntas com padrões comuns de dados pessoais são recusadas antes de serem enviadas ao modelo.

```dotenv
GOOGLE_API_KEY=sua_chave_do_google_ai_studio
```

Não inserir a chave no código, no README, em capturas de tela ou no Git. A faixa gratuita tem limites de requisição e seus dados podem ser usados pela Google para melhorar produtos; só enviar as fichas fictícias e mensagens sem dados pessoais. Não associar projeto com faturamento pago.

## Modelo e fontes consultadas

- Modelo candidato: `gemini-3.5-flash-lite`. A tabela oficial lista entrada e saída na faixa gratuita; quotas variam por modelo e conta. Conferido em 16/11/2026: [preços do Gemini API](https://ai.google.dev/gemini-api/docs/pricing) e [modelo Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite).
- Integração LangChain/Google: [documentação oficial](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai), conferida em 16/11/2026.
- A faixa gratuita pode usar solicitações e respostas para melhorar produtos; verificar as condições vigentes antes de mudar o projeto para uma faixa paga.

## Diagnóstico de erro do modelo

Se a chamada à API falhar, o protótipo mantém uma mensagem simples para o cidadão e imprime `[diagnóstico técnico]` no terminal do PyCharm. Esse detalhe é limitado e tenta ocultar a chave, a pergunta e padrões de dados pessoais. Copie apenas essa linha para pedir ajuda; nunca compartilhe o arquivo `.env`.

- `401`/`authentication`: chave inválida, expirada ou não carregada.
- `403`/`permission_denied`: chave ou projeto sem acesso à API/modelo.
- `404`/`model_not_found`: identificador do modelo indisponível ou incorreto.
- `429`/`quota_exceeded`/`RESOURCE_EXHAUSTED`: quota/limite do modelo ou projeto excedido.
- `400`/`invalid_request`: parâmetro ou formato incompatível.
- `503`/`UNAVAILABLE` ou erro de conexão: indisponibilidade temporária/rede.

Para evitar espera silenciosa, a integração usa nível de raciocínio `low`, tempo limite de 30 segundos por chamada e até duas retentativas espaçadas para `503`/timeout. Erros `429` não são repetidos, pois podem indicar quota diária esgotada. A execução do agente também limita o ciclo a quatro etapas; o terminal informa quando começou a consulta.

Os códigos e limites ativos podem ser conferidos no [guia oficial de erros](https://ai.google.dev/gemini-api/docs/api-errors) e em **Rate limits** no Google AI Studio.

Diagnóstico em 16/11/2026: `gemini-3.8-flash` retornou `503 UNAVAILABLE` por alta demanda. Uma chamada mínima, o agente completo e o menu de terminal responderam com `gemini-3.5-flash-lite`; o protótipo foi alterado para esse modelo.

## Chaves e dados

- Nunca versionar `.env`, tokens ou credenciais de provedor.
- Não colocar dados pessoais reais em exemplos, logs, notebooks ou evidências.
- As fichas em `data/fichas/` são fictícias e podem ser versionadas como material didático.
- O ambiente virtual, caches e arquivos de IDE são locais e ficam excluídos pelo `.gitignore`.

## Avaliação do golden dataset

O avaliador `avaliacao/avaliar.py` lê os 26 casos de `GS_2026_2_CitizenTech_VERSAO_FINAL_CONSOLIDADA.zip` na pasta Downloads do usuário, mantém as mensagens apenas em memória e salva respostas e julgamentos por ID. O Streamlit exibe os resultados salvos incluídos na entrega sem precisar do pacote original. Para retomar o julgamento ou mostrar as respostas esperadas no Streamlit, coloque o pacote original em Downloads.

O notebook `avaliacao/relatorio_comparativo_v6.ipynb` contém as tabelas v6 e a análise dos seis erros da linha de base. Ele inclui as saídas geradas. As células podem ser executadas em um kernel Jupyter com pandas.

Para retomar somente a rodada aprimorada no terminal do PyCharm:

```powershell
.\.venv\Scripts\python.exe .\avaliacao\avaliar.py --fase aprimorada_validada
```

O avaliador salva progresso por caso em `avaliacao/resultados/` e pula registros já completos. A rodada v6 está completa (26/26 corretos). Em nova execução, os casos com julgamentos válidos serão pulados. `503 UNAVAILABLE` indica indisponibilidade temporária; aguarde e retome. `429 RESOURCE_EXHAUSTED` pode indicar quota diária: confira **Rate limits** e o uso atual no AI Studio. A documentação informa que o limite RPD reinicia à meia-noite do Pacífico ([guia oficial de limites](https://ai.google.dev/gemini-api/docs/rate-limits)); não habilitar faturamento pago.

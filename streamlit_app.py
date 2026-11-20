"""Interface gráfica do Aurora Citizen Assist AI."""

import json
import zipfile
from pathlib import Path

import streamlit as st

import agente
from avaliacao.avaliar import carregar_casos, executar_avaliacao


RAIZ = Path(__file__).parent
RESULTADOS = RAIZ / "avaliacao" / "resultados"
TEMAS = {
    "1 · RG — ficha FC-01": "RG",
    "2 · CPF — ficha FC-02": "CPF",
    "3 · Título de eleitor — ficha FC-03": "título de eleitor",
    "4 · Carteira de trabalho — ficha FC-04": "carteira de trabalho",
    "5 · Certidões — ficha FC-05": "certidões",
    "6 · CNH — ficha FC-06": "CNH",
    "7 · Regras gerais — ficha FC-07": "regras gerais de atendimento",
}
OPCAO_LIVRE = "8 · Pergunta livre"
RUBRICA_ATUAL = "v6"


st.set_page_config(
    page_title="Aurora Citizen Assist AI",
    page_icon=":material/forum:",
    layout="centered",
)


@st.cache_resource
def carregar_agente():
    return agente.criar_agente()


@st.cache_data(ttl=5)
def ler_resultado(fase):
    caminho = RESULTADOS / f"{fase}.json"
    if not caminho.is_file():
        return None
    return json.loads(caminho.read_text(encoding="utf-8"))


@st.cache_data
def respostas_esperadas():
    try:
        return {caso["id"]: caso["esperado"] for caso in carregar_casos()}
    except (FileNotFoundError, KeyError, ValueError, zipfile.BadZipFile):
        return {}


def resposta_segura(texto):
    for padrao in agente.PADROES_DADOS_PESSOAIS:
        texto = padrao.sub("[dado pessoal ocultado]", texto)
    return texto


def mostrar_fase(fase, titulo):
    dados = ler_resultado(fase)
    with st.expander(titulo, expanded=True):
        if dados is None:
            st.info("Ainda não há resultados salvos para esta rodada.")
            return

        rubrica_valida = dados.get("versao_rubrica") == RUBRICA_ATUAL
        registros = dados.get("casos", {})
        avaliados = [
            registro for registro in registros.values()
            if rubrica_valida and registro.get("juiz")
        ]
        corretos = sum(registro["juiz"]["correto"] for registro in avaliados)
        col1, col2, col3 = st.columns(3)
        col1.metric("Casos com resposta", len(registros))
        col2.metric("Avaliações válidas", len(avaliados))
        col3.metric("Acertos do juiz", f"{corretos}/{len(avaliados)}")

        if not rubrica_valida:
            st.warning("Os julgamentos salvos usam uma rubrica antiga e serão refeitos ao retomar a avaliação.")

        linhas = []
        esperados = respostas_esperadas()
        for registro in sorted(registros.values(), key=lambda item: item["id"]):
            julgamento = registro.get("juiz") if rubrica_valida else None
            criterios = "Pendente"
            justificativa = ""
            if julgamento:
                criterios = "Correto" if julgamento["correto"] else "Incorreto"
                justificativa = julgamento["justificativa"]
            linhas.append({
                "Caso": registro["id"],
                "Tipo": registro["tipo"],
                "Esperado": esperados.get(registro["id"], "Indisponível sem o pacote acadêmico."),
                "Resultado do juiz": criterios,
                "Resposta do agente": registro["resposta_agente"],
                "Justificativa": justificativa,
            })

        if linhas:
            st.dataframe(
                linhas,
                hide_index=True,
                width="stretch",
                alt=f"Respostas e julgamentos salvos da rodada {titulo.lower()}.",
            )
        else:
            st.info("Nenhum caso foi executado nesta rodada ainda.")


st.title("Central do Cidadão de Aurora")
st.caption("Assistente educacional · fichas fictícias FC-01 a FC-07")
st.info("Este protótipo não é um canal oficial. Não informe CPF, telefone, e-mail ou outros dados pessoais.")

st.session_state.setdefault(
    "mensagens",
    [{"role": "assistant", "content": "Olá! Como posso ajudar você hoje?"}],
)
st.session_state.setdefault("mostrar_resultados", False)

with st.sidebar:
    st.subheader("Menu de atendimento")
    opcoes_menu = [OPCAO_LIVRE, *TEMAS]
    escolha = st.selectbox(
        "Escolha um tema ou faça uma pergunta livre",
        opcoes_menu,
        index=0,
        key="tema_atendimento",
    )
    tema = TEMAS.get(escolha)
    if tema:
        st.caption(f"Tema selecionado: {tema}")

    st.divider()
    st.subheader("Avaliação do agente")
    st.caption("A avaliação executa a linha de base e a rodada aprimorada dos 26 casos; pode levar alguns minutos e consumir quota da API.")
    executar = st.button(
        "Executar julgamento dos 26 casos",
        type="primary",
        width="stretch",
        key="executar_julgamento",
    )
    exibir_resultados = st.button(
        "Exibir resultados salvos",
        width="stretch",
        key="exibir_resultados",
    )
    if exibir_resultados:
        st.session_state["mostrar_resultados"] = True
        ler_resultado.clear()

for mensagem in st.session_state["mensagens"]:
    with st.chat_message(mensagem["role"]):
        if mensagem["role"] == "assistant":
            st.markdown(mensagem["content"])
        else:
            st.text(mensagem["content"])

if st.session_state["mostrar_resultados"]:
    st.subheader("Resultados LLM-as-a-Judge")
    mostrar_fase("baseline", "Linha de base")
    mostrar_fase("aprimorada_validada", "Rodada aprimorada final")

placeholder = "Digite uma pergunta livre" if tema is None else f"Digite sua pergunta sobre {tema}"
pergunta = st.chat_input(placeholder, key="pergunta_chat", submit_mode="disable")

if pergunta is not None:
    pergunta = pergunta.strip()
    pergunta_para_agente = pergunta if tema is None else f"Tema: {tema}. Pergunta: {pergunta}"
    if not pergunta:
        st.warning("Digite uma pergunta para continuar.")
    elif agente.tem_dado_pessoal(pergunta):
        st.warning("Não envie dados pessoais. A mensagem não foi encaminhada ao modelo nem adicionada à conversa.")
    elif len(pergunta_para_agente) > 2000:
        st.warning("A mensagem ficou longa. Resuma sua dúvida em até 2.000 caracteres.")
    else:
        st.session_state["mensagens"].append({"role": "user", "content": pergunta})
        with st.chat_message("user"):
            st.text(pergunta)
        with st.chat_message("assistant"):
            with st.spinner("Consultando as fichas e o Gemini..."):
                try:
                    assistente = carregar_agente()
                    resposta = agente.responder(assistente, pergunta_para_agente)
                except RuntimeError as erro:
                    resposta = str(erro)
            resposta = resposta_segura(resposta)
            st.markdown(resposta)
        st.session_state["mensagens"].append({"role": "assistant", "content": resposta})

slot_avaliacao = st.empty()
if executar:
    st.session_state["mostrar_resultados"] = True
    barra = slot_avaliacao.progress(0.0, text="Preparando a avaliação...")
    status = st.status("Executando duas rodadas de 26 casos", expanded=True)

    def atualizar_progresso(fase, caso_id, concluidos, total, pulado):
        rodada = 1 if fase == "baseline" else 2
        nome = "linha de base" if fase == "baseline" else "rodada aprimorada"
        barra.progress(concluidos / total, text=f"Rodada {rodada}/2 — {nome}: {concluidos}/{total}")
        acao = "já salvo; pulado" if pulado else "executado e salvo"
        status.write(f"{nome}: caso {caso_id}/26 {acao}.")

    try:
        executar_avaliacao("ambas", progresso=atualizar_progresso)
        ler_resultado.clear()
        status.update(label="Avaliação concluída", state="complete")
        st.success("As duas rodadas foram salvas. Use “Exibir resultados salvos” para consultar a tabela.")
    except Exception as erro:
        ler_resultado.clear()
        status.update(label="Avaliação interrompida", state="error")
        st.error(
            f"A avaliação parou ({type(erro).__name__}). O progresso concluído foi salvo; "
            "você pode retomá-la quando a API estiver disponível."
        )

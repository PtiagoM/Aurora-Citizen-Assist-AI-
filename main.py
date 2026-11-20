"""Interface de terminal do protótipo Aurora Citizen Assist AI."""

from agente import criar_agente, responder


TEMAS = {
    "1": "RG — ficha FC-01",
    "2": "CPF — ficha FC-02",
    "3": "Título de eleitor — ficha FC-03",
    "4": "Carteira de trabalho — ficha FC-04",
    "5": "Certidões — ficha FC-05",
    "6": "CNH — ficha FC-06",
    "7": "Regras gerais de atendimento — ficha FC-07",
}


def main():
    print("Central do Cidadão de Aurora — protótipo educacional")
    print("Não informe dados pessoais. Este não é um canal oficial.\n")

    try:
        agente = criar_agente()
    except RuntimeError as erro:
        print(erro)
        return

    while True:
        print("Escolha um tema ou digite sua pergunta:")
        for numero, tema in TEMAS.items():
            print(f"{numero}. {tema}")
        print("8. Pergunta livre")
        print("0. Sair")
        escolha = input("Opção: ").strip()

        if escolha == "0":
            print("Até logo.")
            break
        if escolha in TEMAS:
            pergunta = input(f"Pergunta sobre {TEMAS[escolha]}: ").strip()
        elif escolha == "8":
            pergunta = input("Digite sua pergunta: ").strip()
        else:
            print("Opção inválida. Escolha de 0 a 8.\n")
            continue

        print("Consultando as fichas e o Gemini...", flush=True)
        print(f"\n{responder(agente, pergunta)}\n")


if __name__ == "__main__":
    main()

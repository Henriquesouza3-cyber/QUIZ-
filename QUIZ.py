# INTRODUÇÃO A PROGRAMAÇÃO 
# INFO 1M
#ALUNOS: ISMAEL LEVI, DIEGO VINÍCIUS, JOÃO HENRIQUE


def executar_quiz(perguntas):
    pontuacao = 0
    total_perguntas = len(perguntas)

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for i, opcao in enumerate(pergunta["opcoes"], start=1):
            print(f"{i}. {opcao}")
        resposta_usuario = input("Escolha a resposta (digite o número): ")
        resposta_certa = pergunta["opcoes"].index(pergunta["resposta"]) + 1
        if int(resposta_usuario) == resposta_certa:
            print("Correto!\n")
            pontuacao += 1
        else:
            print(f"Incorreto! A resposta correta é: {pergunta['resposta']}\n")

    # Calcula a porcentagem de acertos e erros
    erros = total_perguntas - pontuacao
    percentual_acertos, percentual_erros = calcular_percentual(pontuacao, erros)

    print(f"Sua pontuação final: {pontuacao}/{total_perguntas}")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%\n")


# Função para calcular percentual de acertos e erros
def calcular_percentual(acertos, erros):
    total = acertos + erros
    if total == 0:
        return 0, 0
    percentual_acertos = (acertos / total) * 100
    percentual_erros = (erros / total) * 100
    return percentual_acertos, percentual_erros


# Funções dos quizzes
def quiz_matematica():
    perguntas = [
        {"pergunta": "Quanto é 5 + 7?", "opcoes": ["10", "11", "12", "13"], "resposta": "12"},
        {"pergunta": "Quanto é 37 - 15?", "opcoes": ["18", "22", "24", "26"], "resposta": "22"},
        {"pergunta": "Quanto é 9 x 9?", "opcoes": ["72", "81", "90", "99"], "resposta": "81"},
        {"pergunta": "Quanto é 49 : 7?", "opcoes": ["3", "11", "9", "7"], "resposta": "7"},
    ]
    executar_quiz(perguntas)


def quiz_cultura_geral():
    perguntas = [
        {"pergunta": "Quem pintou a Mona Lisa?", "opcoes": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "resposta": "Leonardo da Vinci"},
        {"pergunta": "Em qual país fica a Torre Eiffel?", "opcoes": ["França", "Itália", "Espanha", "Alemanha"], "resposta": "França"},
        {"pergunta": "Qual é o menor país do mundo?", "opcoes": ["Mônaco", "Malta", "Vaticano", "Liechtenstein"], "resposta": "Vaticano"},
        {"pergunta": "Qual artista é conhecido como Rei do Pop?", "opcoes": ["Michael Jackson", "Justin Bieber", "Roberto Carlos", "Luan Santana"], "resposta": "Michael Jackson"},
    ]
    executar_quiz(perguntas)


def quiz_ciencia():
    perguntas = [
        {"pergunta": "Qual é o planeta mais próximo do Sol?", "opcoes": ["Vênus", "Terra", "Marte", "Mercúrio"], "resposta": "Mercúrio"},
        {"pergunta": "O que é a fórmula H2O?", "opcoes": ["Oxigênio", "Água", "Hidrogênio", "Gelo"], "resposta": "Água"},
        {"pergunta": "Qual é o maior órgão do corpo humano?", "opcoes": ["Coração", "Cérebro", "Pele", "Pulmão"], "resposta": "Pele"},
        {"pergunta": "Qual gás é essencial para a respiração humana?", "opcoes": ["Nitrogênio", "Oxigênio", "Carbono", "Hidrogênio"], "resposta": "Oxigênio"},
    ]
    executar_quiz(perguntas)


# Menu para escolha do quiz
def menu():
    while True:
        print("Escolha um quiz:")
        print("1. Quiz de Matemática")
        print("2. Quiz de Cultura Geral")
        print("3. Quiz de Ciência")
        print("4. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            quiz_matematica()
        elif escolha == "2":
            quiz_cultura_geral()
        elif escolha == "3":
            quiz_ciencia()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


# Executa o menu principal
menu()
4
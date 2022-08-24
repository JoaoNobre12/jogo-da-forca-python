def jogar_advinhacao():
    import random as rd

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = rd.randrange(1, 101)

    total_de_tentativas = 0
    pontos = 1000

    print("Qual a dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print("-------------------------------")

    nivel = int(input("Digite a dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 15

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou!")
            print("Você fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                print("")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                print("")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("")
    print("Fim do jogo")

if(__name__=="__main__"):
    jogar_advinhacao()
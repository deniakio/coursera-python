def iniciar_jogo():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    modo_de_jogo = int(input("2 - para jogar um campeonato"))

    while modo_de_jogo > 2 or modo_de_jogo < 1:
        print("Erro! Escolha novamente o modo de jogo.")
        print("1 - para jogar uma partida isolada")
        modo_de_jogo = int(input("2 - para jogar um campeonato"))

    if modo_de_jogo == 2:
        campeonato()
        print("**** Final do campeonato! ****")
        print("Placar: Você 0 X 3 Computador")

    else:
        partida()


def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    total = n

    while n <= m or n <= 1:
        n = int(input("O número de peças tem de ser maior que 1. Insira novamente."))
        m = int(input("Limite de peças por jogada?"))

    if n % (m + 1) == 0:
        print("Você começa!")
        jogada_usuario = usuario_escolhe_jogada(n, m)
        print("Voce tirou", (total - jogada_usuario), "peças.")
        total = n - jogada_usuario

        if total == 0:
            print("Fim do jogo! Você ganhou!")
            return False

        else:

            while total != 0:

                if total == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")

                else:
                    print("Agora restam apenas", total, "peças.")

                n = total
                jogada_cpu = computador_escolhe_jogada(n, m)
                total = total - jogada_cpu

                if total == 0:
                    print("Fim do jogo! O computador ganhou!")
                    return True
                else:
                    if total == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam apenas", total, "peças.")

                    n = total
                    jogada_usuario = usuario_escolhe_jogada(n, m)
                    print("Voce tirou", (total - jogada_usuario), "peças.")
                    total = total - jogada_usuario
                    if total == 0:
                        print("Fim do jogo! Você ganhou!")
                        return False

    else:
        print("Computador começa!")
        jogada_cpu = computador_escolhe_jogada(n, m)
        total = n - jogada_cpu

        if total == 0:
            return "Fim do jogo! O computador ganhou!"
            return True
        else:
            while total != 0:

                if total == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam apenas", total, "peças.")

                n = total
                jogada_usuario = usuario_escolhe_jogada(n, m)
                total = total - jogada_usuario
                print("Voce tirou", jogada_usuario, "peças.")

                if total == 0:
                    print("Fim do jogo! Você ganhou!")
                    return False
                else:
                    n = total
                    jogada_cpu = computador_escolhe_jogada(n, m)
                    total = total - jogada_cpu

                    if total == 0:
                        print("Fim do jogo! O computador ganhou!")
                        return True


def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0 and n != 1:
        jogada_cpu = n // (m + 1)
    else:
        if n <= m:
            jogada_cpu = n
        else:
            if (n - m) <= m:
                jogada_cpu = (n - m) - 1
            else:
                if n % m == 0:
                    jogada_cpu = m - 1
                else:
                    jogada_cpu = m

    if jogada_cpu == 0:
        jogada_cpu = 1
    else:                
        if jogada_cpu == 1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", jogada_cpu, "peças.")

    return jogada_cpu


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar?"))

    while jogada > m or jogada < 1:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar?"))

    return jogada


def campeonato():
    print("Voce escolheu um campeonato!")

    print("**** Rodada 1 ****")
    partida()

    print("**** Rodada 2 ****")
    partida()

    print("**** Rodada 3 ****")
    partida()


n = 0
m = 0

iniciar_jogo()

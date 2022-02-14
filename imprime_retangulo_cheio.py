largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = largura

while altura >= 1:
    while largura >= 1:
        print("#", end="")
        largura = largura - 1
    largura = i
    print("", end="\n")
    altura = altura - 1
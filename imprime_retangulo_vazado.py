largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i = largura
n = altura

while altura >= 1:
    while largura >= 1:
        if (altura == 1 or altura == n) or (largura == 1 or largura == i):
            print("#", end="")
            largura = largura - 1
        else:
            print(" ", end="")
            largura = largura - 1
    largura = i
    print("", end="\n")
    altura = altura - 1
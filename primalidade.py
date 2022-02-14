n = int(input("Digite um número inteiro:"))
cont = 2

if n % 2 == 0 and n != 2 and n != 1:
    print("não primo")

else:
    while n != cont and not n % cont == 0:
        cont = cont + 1

    if n == cont:
        print("primo")
    else:
        print("não primo")
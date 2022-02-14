n = int(input("Digite um número inteiro:"))
soma = 0
dig = 0

if n > 9:
    while n > 10:
        dig = n % 10
        n = n // 10
        soma = soma + dig
    print(soma + n)
else:
    print(n)
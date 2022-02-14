n = int(input("Digite o valor de n:"))
fatorial = 1
i = 2

while n >= i:
    fatorial = fatorial * i
    i = i + 1
print(fatorial)
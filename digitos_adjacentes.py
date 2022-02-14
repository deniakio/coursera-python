n = int(input("Digite um número inteiro:"))
dig1 = 0
dig2 = 1

while n > 9 and dig1 != dig2:
    dig1 = n % 10
    n = n // 10
    dig2 = n % 10

if dig1 == dig2:
    print("sim")

else:
    print("não")
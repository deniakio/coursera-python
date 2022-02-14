import math

a = int(input("Digite o valor x do ponto a:"))
b = int(input("Digite o valor x do ponto b:"))
c = int(input("Digite o valor y do ponto a:"))
d = int(input("Digite o valor y do ponto b:"))

distancia = math.sqrt(((a - b) ** 2) + ((c - d) ** 2))
if distancia >= 10:
    print("longe")
else:
    print("perto")
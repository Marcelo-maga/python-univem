a1 = float(input("Digite o angulo 1: "))
a2 = float(input("Digite o angulo 2: "))
a3 = float(input("Digite o angulo 3: "))
while (a1 + a2 + a3) != 180:
    print("Digite os angulos de um triangulo existente...")
    a1 = float(input("Digite o angulo 1: "))
    a2 = float(input("Digite o angulo 2: "))
    a3 = float(input("Digite o angulo 3: "))

if a1 == 90 or a2 == 90 or a3 == 90:
    print("Triangulo reto...")
elif a1 > 90 or a2 > 90 or a3 > 90:
    print("Triangulo obtusângulo...")
else:
    print("Triângulo acutângulo...")

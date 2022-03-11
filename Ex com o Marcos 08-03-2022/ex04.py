l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
if l1 == l2 == l3:
    print("Triângulo equilátero...")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Triângulo isósceles...")
else:
    print("Triângulo escaleno...")
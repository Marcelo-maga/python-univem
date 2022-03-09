op = int(input("Digite a operação a ser realizada (1/2): "))
while op < 1 or op > 2:
    op = int(input("Digite a operação a ser realizada (1/2): "))
if op == 1:
    print("Area de um quadrado...")
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    area = base * altura
else:
    print("Area de um triangulo...")
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    area = base * altura / 2
print("O valor da área é ", area)
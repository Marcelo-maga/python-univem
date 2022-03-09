placa = int(input("Digite a parte numérica da placa: "))
while placa < 999 & placa > 9999:
    placa = int(input("Digite a parte numérica da placa com 4 digitos: "))
placa = placa % 10
if placa == 1 or placa == 2:
    print("Segunda...")
elif placa == 3 or placa == 4:
    print("Terça...")
elif placa == 5 or placa == 6:
    print("Quarta...")
elif placa == 7 or placa == 8:
    print("Quinta...")
else:
    print("Sexta...")
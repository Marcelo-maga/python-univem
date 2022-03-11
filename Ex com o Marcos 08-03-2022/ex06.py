a1 = float(input("Digite o numero 1: "))
a2 = float(input("Digite o numero 2: "))
a3 = float(input("Digite o numero 3: "))
if a1 > a2 > a3:
    print(a1, " ", a2, " ", a3)
elif a1 > a3 > a2:
    print(a1, " ", a3, " ", a2)
elif a2 > a1 > a3:
    print(a2, " ", a1, " ", a3)
elif a2 > a3 > a1:
    print(a2, " ", a3, " ", a1)
elif a3 > a1 > a2:
    print(a3, " ", a1, " ", a2)
else
    print(a3, " ", a2, " ", a1)

n = int(input("Digite um número: "))
while n > 999:
    n = int(input("Digite um número menor que 1000:"))
c = n // 100
print("centena: ", c)
d = n % 100 // 10
print("dezena: ", d)
u = n % 10
print("unidade: ", u)

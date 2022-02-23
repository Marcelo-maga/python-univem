import math

running = 1
while running == 1:
    print("--------------------------------------------------")
    print("1 - Soma")
    print("--------------------------------------------------")
    print("2 - Maior entre 3 números")
    print("--------------------------------------------------")
    print("3 - Avaliação - distância entre 3 números")
    print("--------------------------------------------------")
    ex = int(input("\nInforme o número do exercício: "))

    if ex == 1:
        n = int(input("Digite um número: "))

        if n % 2 == 1:
            print(f"O número {n} é ímpar.")
        else:
            print(f"O número {n} é par.")

    if ex == 2:
        numbers = []
        for n in range(3):
            num = float(input(f"Informe o número {n + 1}: "))
            numbers.append(num)

        print(f"O maior número é {max(numbers)}")
    if ex == 3:
        x1 = float(input("Informe o x1: "))
        y1 = float(input("Informe o y1: "))
        x2 = float(input("Informe o x1: "))
        y2 = float(input("Informe o y2: "))

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print(f"A distancia entre({x1},{y1}) e ({x2},{y2}) é {distance}")

    running = int(input("Deseja continuar rodando o programa? (se não digite qualquer número diferente de 1): "))

running = 1
while running == 1:
    ex = int(input("Informe o número do exercício: "))

    if (ex == 1):
        n1 = float(input('Informe o primeiro número: '))
        n2= float(input('Informe o segundo número: '))

        media = (n1 + n2)/2

        print(f'A média é: {media}')

    if (ex == 2):
        n1 = float(input('Informe o primeiro número: '))
        n2 = float(input('Informe o segundo número: '))
        n3 = float(input('Informe o segundo número: '))

        media = (n1 + n2 + n3) / 3

        print(f'A média é: {media}')

    if (ex == 3):
        meters = float(input('Informe o valor em metros: '))
        mili = meters * 1000
        print(f'O valor em milimetros {mili}')

    if (ex == 4):
        days = int(input("informe a quantidade de dias: "))
        hours = int(input("informe a quantidade de horas: "))
        minutes = int(input("informe a quantidade de minutos: "))
        seconds = int(input("informe a quantidade de segundos: "))

        totalSeconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

        print(f"A quantidade total de segundo é: {totalSeconds}")

    if (ex == 5):
        a = int(input('Informe o primeiro valor: '))
        b = int(input('Informe o segundo valor: '))

        print(f'A={a} e B = {b}')

        c = a
        a = b
        b = c

        print(f'A={a} e B = {b}')

    if (ex == 6):
        salary = float(input("Informe o valor do salário do funconário: "))
        increase = int(input("Informe o percentual a ser aumentado: "))

        finalSalary = salary + ((salary / 100) * increase)

        print(f"O salário total é igual à: {finalSalary}")

    if (ex == 7):
        gas = float(input('Informe o preço do combustivel: '))
        carPerformace = float(input('Informe o km/l: '))
        citysDistance = float(input('Informe a a distacia entre as duas cidades: '))

        moneySpent = (citysDistance/carPerformace) * gas

        print(f"O valor gasto foi de {moneySpent}")

    if (ex == 8):
        daysRented = int(input("Informe quantos dias o carro foi alugado: "))
        kmTraveled = float(input("Informe quantos km o carro percorreu: "))

        priceToPay = (daysRented * 60) + (kmTraveled * 0.15)

        print(f"O valor a ser pago será de R${priceToPay}")

    if (ex == 9):
        fahrenheit = float(input('Informe o valor em Fahrenheit: '))
        celsius = ((fahrenheit - 32)/9)*5

        print(celsius)

    running = int(input("Deseja continuar rodando o programa? (se não digite qualquer número diferente de 1): "))

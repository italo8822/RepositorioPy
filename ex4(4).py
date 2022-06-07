resultado = 0
numero = int(input("\ndigite um numero: "))
for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)
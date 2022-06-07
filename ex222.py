resultado = 0

numero = int(input("\ndigite um numero: "))
while(numero >= 10 or numero <= 0):
    print("\nTente novamente")
    numero = int(input("\ndigite um numero: "))

for multiplicador in range(1, 6):
        resultado = numero * multiplicador
        print(numero, "x", multiplicador, "=", resultado)



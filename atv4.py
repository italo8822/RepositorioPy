numeros = []
numerosPares = []
numerosImpares = []

while numeros > 0:
    print("Tente novamente")
    numeros.append(int(input("Digite um número: ")))
    resposta = input("Deseja continua? [sim/não]")
    if resposta in 'Nn':
        break


while True:
        numeros.append(int(input("Digite um número: ")))

        resposta = input("Deseja continua? [sim/não]")

        if resposta in 'Nn':
            break


for numero in numeros:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

#numeros.sort()
#numerosPares.sort()
#numerosImpares.sort()

print("")
print("")

print(f"Números inseridos: {numeros}")
print(f"Números Pares: {numerosPares}")
print(f"Números Impares: {numerosImpares}")
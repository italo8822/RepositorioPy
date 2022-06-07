soma = 0 
for contador in range(0, 6):
    numero = int(input("Digite um numero: "))
    if(numero % 2 == 0):
        soma += numero

print("soma", soma)
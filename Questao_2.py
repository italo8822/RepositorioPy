
tempo = [[0, 2, 11, 6, 15, 11, 1], [2, 0, 7, 12, 4, 2, 15], [11, 7, 0, 11, 8, 3, 13], [6, 12, 11, 0, 10, 2, 1], [15, 4, 8, 10, 0, 5, 13], [11, 2, 3, 2, 5, 0, 14], [1, 15, 13,1 ,13 ,14, 0]]

while True:
    print("Cidades: |1, 2, 3, 4, 5, 6, 7|\n")
    
    origem = int(input("Digite a cidade de origem: "))
    while (origem > 7) or (origem < 1):
        origem = int(input("\nCidade inexistente! Tente novamente: "))
        
    destino = int(input("Agora digite a cidade de destino (para sair digite a mesma cidade de origem): "))
    while (destino > 7) or (destino < 1):
        destino = int(input("\nCidade inexistente! Tente novamente: "))
    
    if origem == destino:
        break
    else:
        horas = tempo[origem-1][destino-1]
        print("\nDa cidade {} até a cidade {} são {} horas de viagem!\n".format(origem, destino, horas))

print("\nObrigado e volte sempre!!")



tempo = [[0, 2, 11, 6, 15, 11, 1], [2, 0, 7, 12, 4, 2, 15], [11, 7, 0, 11, 8, 3, 13], [6, 12, 11, 0, 10, 2, 1], [15, 4, 8, 10, 0, 5, 13], [11, 2, 3, 2, 5, 0, 14], [1, 15, 13,1 ,13 ,14, 0]]

while True:
    print("Cidades: |1, 2, 3, 4, 5, 6, 7|")

    soma1 = []
    soma2 = []
    origem = int(input("\nDigite a cidade de origem: "))
    while (origem > 7) or (origem < 1):
        origem = int(input("\nCidade inválida! Tente novamente: "))
    soma1.append(origem-1)
    soma2.append(origem-1)
    
    for i in range(2):
        descanso = int(input("\nDigite a {}a opção de descanso: ".format(i+1)))
        while (descanso > 7) or (descanso < 1):
            descanso = int(input("\nCidade inválida! Tente novamente: "))
        if i == 0:
            soma1.append(descanso)
        else:
            soma2.append(descanso)
        
    destino = int(input("\nAgora digite a cidade de destino: "))
    while (destino > 7) or (destino < 1):
        destino = int(input("\nCidade inválida! Tente novamente: "))
    soma1.append(destino-1)
    soma2.append(destino-1)

    if sum(soma1) < sum(soma2):
        print("\nEscolhemos a cidade {} como a cidade intermediária, para uma viagem mais rápida e confortável!".format(soma1[1]))
    elif sum(soma1) > sum(soma2):
        print("\nEscolhemos a cidade {} como a cidade intermediária, para uma viagem mais rápida e confortável!".format(soma2[1]))
    else:
        print("\nAs duas cidades escolhidas proporcionam o mesmo horário de viagem!")
    
    continua = input("\nDeseja realizar outra pesquisa?(s/n): ")
    while not (continua[0].lower() == "s" or continua[0].lower() == "n"):
        continua = input("\nResposta invalida! Digite 's' para sim ou 'n' para não. Desejar realizar outra pesquisa? ")
    if continua[0].lower() == "n":
        break

print("\nObrigado por escolher a FBV-Travelling! Volte sempre!")




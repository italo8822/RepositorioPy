
tempo = [[0, 2, 11, 6, 15, 11, 1], [2, 0, 7, 12, 4, 2, 15], [11, 7, 0, 11, 8, 3, 13], [6, 12, 11, 0, 10, 2, 1], [15, 4, 8, 10, 0, 5, 13], [11, 2, 3, 2, 5, 0, 14], [1, 15, 13,1 ,13 ,14, 0]]


print("Cidades: |1, 2, 3, 4, 5, 6, 7|")
print("\nDigite as cidades que deseja percorrer (Digite '0' para terminar): ")

while True:
    cidades = []
    soma = 0
    while True:
        escala = int(input())
        while escala > 7:
            print("Cidade inexistente! Tente novamente: \n")
            escala = int(input())
        if escala == 0:
            break
        else:
            cidades.append(escala-1)
    
    for i in range(len(cidades)-1):
        soma = soma + tempo[cidades[i]][cidades[i+1]]
        
    print("\nO tempo necessário para percorrer todas as cidades escolhidas é de {} horas!".format(soma))
    
    continua = input("\nDeseja realizar outra pesquisa?(s/n): ")
    while not (continua[0].lower() == "s" or continua[0].lower() == "n"):
        continua = input("\nResposta invalida! Digite 's' para sim ou 'n' para não. Desejar realizar outra pesquisa? ")
    if continua[0].lower() == "n":
        break
    else:
        print("\nDigite as cidades que deseja percorrer (Digite '0' para terminar): ")

print("\nObrigado e volte sempre!!")





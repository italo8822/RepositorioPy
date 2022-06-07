#coloca em ordem crescente
vetores = [3, 9, 1, 5, 2, 7, 4, 6, 8, 10]
print("\nVetor original: ", vetores)
vetores_ordenados = sorted(vetores) #Em palavras vai na ordem alfabetica
print("Vetor ordenado: ", vetores_ordenados)

#ou 

vetores = [3, 9, 1, 5, 2, 7, 4, 6, 8, 10]
print("\n",vetores)
vetores.sort()  
print(vetores)  

#decrescente:

vetores = [3, 9, 1, 5, 2, 7, 4, 6, 8, 10]
print("\n",vetores)
vetores.sort(reverse=True)
print(vetores)

#print("vetor original: %s" % (v))
#for x in range(len(v)):
#    print(v[x])       #serve pra ver a tavela a cima em listra horizontal
##############################################

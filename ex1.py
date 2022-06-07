#Construa um algoritmo que preencha um vetor de 100 elementos inteiros, colocando
# 1 na posição correspondente a um numero par e 0 a um numero ímpar

elemento = [0]*100
for i in range(len(elemento)):
    if((i % 2) == 0):
        elemento[i] = 1
    else:
        elemento[i] = 0

for i in range(len(elemento)):
    print(str(i) + " = " + str(elemento[i]))
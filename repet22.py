#Elabore um algoritmo que calcule um numero inteiro que mais se aproxima da raiz quadrada de um numero fornecido por usuario
numero = int(input("Digite um valor: "))
i = 1
while (i * i < numero):
    i += 1
print("O inteiro mais proximo da raiz quadrada é: " + str(i))
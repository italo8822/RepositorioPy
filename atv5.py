respostas = []
contador = 0

print('\nDigite "s" para SIM e "n" para NÃO.')

respostas.append(input("Telefonou para vítima? "))
respostas.append(input("Esteve no local do crime? "))
respostas.append(input("Mora perto da vítima? "))
respostas.append(input("Devia para a vítima? "))
respostas.append(input("Já trabalhou com a vítima? "))

for r in respostas:
    if r in 'Ss':
        contador += 1

if contador == 5:
    print("Assassino!")
elif contador == 3 or contador == 4:
    print("Cúmplice!")
elif contador == 2:
    print("Suspeito!")
else:
    print("Inocente")
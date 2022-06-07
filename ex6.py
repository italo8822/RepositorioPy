#6.	Escreva um programa que leia um ano (um número inteiro) e calcula se o ano é bisexto. 
# Um ano é bisexto deve ser múltiplo de 4 mas não pode ser múltiplo de 100, a menos que seja também 
# últiplo de 400.

ano = int(input("Digite o ano: "))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')
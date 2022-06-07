#5.	Fazer a pessoa escolher um número que vai representar o valor do produto, depois fazer com que se o 
# produto for baixo ou igual a 50 reais, a pessoa não ganhe desconto e se for abaixo  ou igual a 
# 100 reais, a pessoa ganhe 10% de desconto e por fim, acima de 100 reais, a pessoa ganhe o desconto de 20%.

produto = float(input("Digite o valor do produto: "))

variavel = produto * 0.10 
desconto1 = produto - variavel

variavell = produto * 0.20
desconto2 = produto - variavell

if produto <= 50:
    print("Você não tem desconto!!")
elif produto <= 100:
    print("Você tem 10% de desconto: ", desconto1)
elif produto > 100:
    print("Você tem 20% de desconto: ", desconto2)
else: 
    print("Opção invalida!!")
valor_total = float(input("Digite o valor total da compra: "))

errado = True

while errado:
	forma_pagamento = int(input("\nFormas de pagamento:\n1 - À vista\n2 - Rotativo no Cartão\n3 - Parcelado em 3x\n4 - Parcelado em 6x\n5 - Parcelado 12x\nQual a forma de pagamento que deseja? "))
	if not(0 < forma_pagamento < 6):
		print("\nOpção inválida!! Tente novamente.")
	else:
		errado = False

parcelas = 1

if forma_pagamento == 1:
	diferenca = valor_total*0.2
	valor_final = valor_total*0.8
	juros_ou_desconto = "Desconto de 20%"
	valor_parcelas = valor_final/parcelas
	
elif forma_pagamento == 2:
	diferenca = valor_total*0.1
	valor_final = valor_total*0.9
	juros_ou_desconto = "Desconto de 10%"
	valor_parcelas = valor_final/parcelas
	
elif forma_pagamento == 3:
	parcelas = 3
	diferenca = 0
	valor_final = valor_total
	juros_ou_desconto = "Não há descontos nem juros!"
	valor_parcelas = valor_final/parcelas
	
elif forma_pagamento == 4:
	parcelas = 6
	diferenca = valor_total*0.05
	valor_final = valor_total*1.05
	juros_ou_desconto = "Juros de 5%"
	valor_parcelas = valor_final/parcelas
	
else:
	parcelas = 12
	diferenca = valor_total*0.1
	valor_final = valor_total*1.1
	juros_ou_desconto = "Juros de 10%"
	valor_parcelas = valor_final/parcelas

print(40*"=")
print(f"Valor Total da compra: R$ {valor_total}\nValor final: R$ {valor_final}\nDiferença: R${diferenca} \n{juros_ou_desconto}\nQuantidade de parcelas: {parcelas}\nValor das parcelas: R$ {valor_parcelas}")
print(40*"=")
print("\nOBRIGADO E VOLTE SEMPRE!")

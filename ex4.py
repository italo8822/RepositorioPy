print("\nA - Álcool\nG - Gasolina")
combustivel = input("\nDigite o tipo de combustível: ")
litros = float(input("\nDigite quantos litros deseja: "))

if combustivel == "a":
	alcool = litros*1.9
	if litros <= 20:
		valor_desc = alcool*0.97
	else:
		valor_desc = alcool*0.95
	print("Combustível escolhido: Álcool\nValor por litro: R$ 1,90\nLitros = {litros}\nValor total (com desconto): R$ {valor_desc}")

elif combustivel == "g":
	gasolina = litros*2.5
	if litros <=20:
		valor_desc = gasolina*0.96
	else:
		valor_desc = gasolina*0.94
	print("Combustível escolhido: Gasolina\nValor por litro: R$ 2,50\nLitros = {litros}\nValor total (com desconto): R$ {valor_desc}")

else:
	print("Opção indisponível!!")
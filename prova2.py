numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

print('\n[1]SOMA')
print('[2]SUBTRAÇÃO')
print('[3]MULTIPLICAÇÃO')
print('[4]DIVISÃO')
print('[5]POTENCIAÇÃO')
print('[6]RESTO')  

opcao = float(input("\nEscolha a opção que deseja execultar: "))

print()
while opcao > 6 or opcao < 1:
    print("Tente novamente!")
    opcao = int(input("Escolha a opção que deseja execultar: "))

if opcao == 1:
    print("SOMA", numero1 + numero2)
elif opcao == 2:
    print("SUBTRAÇÃO", numero1 - numero2)
elif opcao == 3:
    print("MULTIPLICAÇÃO", numero1 * numero2)
elif opcao == 4:
	if numero2 == 0:
		print("Não existe divisão por Zero!!")
	else:
		print("DIVISÃO", numero1 / numero2)
elif opcao == 5:
    print("POTENCIAÇÃO", numero1 ** numero2)
else:
	if numero2 == 0:
		print("Não existe divisão por Zero!!")
	else:
		print("RESTO", numero1 % numero2)
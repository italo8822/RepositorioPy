print("============================================")
print("| Para começar, digite seu nome: " , "|")
nome = input()
print("| Bem-vindo, ", nome , "              |")
print("============================================")

print("\n============================================")
print("Agora com qual time você joga?")
paises = {'==> (1) SPT': 'Sport', '==> (2) STA': 'Santa Cruz', '==> (3) NAU': 'Naútico', '==> (4) CEN': 'Central'}
for chave, valor in paises.items():
    print(chave + " = " + str(valor))
print("============================================")
print("\n============================================")
print("Digite o número do seu time do seu time:")

while paises < 5:
    print("Tente novamente!")
    print("Digite o número do seu time do seu time:")

nome = input()

print("| Agora vamos somar os pontos do ", nome ," é ")
print("avaliar você: |")

nota1 = float(input(f"\nQuantos Gols no 1° jogo: "))
nota2 = float(input(f"\nQuantos Gols no 2° jogo: "))
nota3 = float(input(f"\nQuantos Gols no 3° jogo: "))
nota4 = float(input(f"\nQuantos Gols no 4° jogo: "))

media = (nota1 + nota2 + nota3 + nota4)

print(f"\nSua média é: {media}")

if media >=5:
	print("Ótimo jogador!!")
else:
	print("Pessimo jogador!!")

#da erro caso coloque algo diferente de numero nos pontos
#da erro caso coloque algo diferente da sigla

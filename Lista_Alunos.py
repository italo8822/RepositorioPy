import random
import math

print("="*15)
print("| CRIADOR DE  |")
print("|   GRUPOS    |")
print("="*15)

nomes = ""
x = 1
lista = []
qntd_alunos = int(input("\nDigite a quantidade de alunos por grupo: "))
print("\nDigite os nomes dos alunos! Ao terminar digite 'fim': ")

while nomes.lower() != "fim":
	nomes = input()
	if nomes.lower() == "fim":
		break
	else:
		lista.append(nomes)

qntd_grupos = math.ceil(len(lista)/qntd_alunos)
grupos = [[None]*qntd_alunos for i in range(qntd_grupos)]
random.shuffle(lista)

while len(lista) != 0:
	for n in range(qntd_alunos):
		for m in range(qntd_grupos):
			if len(lista) != 0:
				grupos[m][n] = lista[0]
				lista.pop(0)
			else:
				break

print(f"\nOs grupos foram distribuídos da seguinte forma:")
print()
for y in range(qntd_grupos):
	print(f"Grupo {y+1}: {grupos[y]}")
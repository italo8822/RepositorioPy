#Determine o raio e a altura, para poder calcular  a geratriz, volume, 
#área de base, área lateral e a área total de um cone.

raio = int(input("Digite o raio: "))
altura = int(input("Digite a altura: "))
geratriz = 0
pi = 3.14


geratriz = (raio ** 2 + altura ** 2) ** 0.5
volume = (pi * raio ** 2 * altura)/3
area_base = pi * raio ** 2
area_lateral = pi * raio * geratriz

print("O resultado deu: ", geratriz)
print("\nO volume é: ", volume)
print("\nA area da base é: ", area_base)
print("\nA area lateral é: ", area_lateral)
print("\nA area total é: ", area_base + area_lateral)
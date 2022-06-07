import random  
import statistics  

numeros = [random.randrange(101) for i in range(1000)] 
menor = []

for x in range(101):
    menor.append(numeros.count(x))

print("="*35)
print("Número sorteado mais vezes:", statistics.mode(numeros)) 
print("Número sorteado menos vezes:", menor.index(min(menor),0,101)) 
print("Maior número sorteado:", max(numeros))
print("Menor número sorteado:", min(numeros))
print("="*35)


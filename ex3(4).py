soma = 0
for numero in range(0, 501):
    if numero % 2 != 0:
        if numero % 3 == 0:
            soma += numero

print(soma)
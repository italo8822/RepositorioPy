def troca(x, y):
    aux = x
    x = y
    y = aux
    
def media(x, y):
    return (x + y) / 2

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
troca(nota_1, nota_2)
print("a: " + str(nota_1) + "\nb: " + str(nota_2))
print("media: " + str(media(nota_1, nota_2)))
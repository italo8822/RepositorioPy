def status(media):
    if media >= 6:
        return 'Aprovado'
    elif media >= 4:
        return 'Verificação suplementar'
    else:
        return 'Reprovado'

numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
media = (numero1+numero2)/2
situacao = status(media)
print("Média = {} - {}".format(media, situacao))
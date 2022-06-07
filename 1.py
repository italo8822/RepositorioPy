i = 0
while True:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    media = (nota1 + nota2)/2
    print("A media é: ", media)
    if media >= 7:
        if media >= 9:
            print("Excelente, ", end='')
        print("Aluno aprovado")
    elif media >= 4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
    i = i + 1
    if(i < 5):
        break


#éeeeee

nome = 0
while(nome < 50):
        print("nome que ele pediu")
        nome = nome + 1
#capturo o nome de 2 alunos em 3 grupos
grupos = [[0,0], [0,0], [0,0]]
for x in range (len(grupos)):
    for i in range (len(grupos[x])):
        grupos[x][i] = input("Digite o nome do aluno: ")

for x in range(len(grupos)):
    print("Grupos: " + str(x+1))
    for i in range (len(grupos[x])):
        print("Aluno: " + str(grupos[x][i]))
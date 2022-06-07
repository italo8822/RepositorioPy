turma = []

while True:

        operaçao = int(input("Digite uma operação: \n1: Cadastra aluno. \n2: Remover aluno.\n0: Sair \nDigite aqui: "))

        if operaçao == 1:
            nomeAluno = input("Digite o nome do aluno para ser inserido: ")
            turma.append(nomeAluno)
            print(turma)
        
        elif operaçao == 2:
            nomeAluno = input("Digite o nome do aluno para ser removido: ")
            turma.remove(nomeAluno)
            print(turma)

        elif operaçao == 0:
            break

        else:
            print("Operação inválida")

print("\nOperação finalizada")
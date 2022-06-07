#O professor deseja dividir a turma com N numeros de dois grupos: um com M
#alunos e outro com (N-M) alunos. faça o programa que lê o valor de
#N e M e informa o numero de combinações é igual a N/(M! * (N-M)!)

def fatorial(valor):
    if valor == 1:
        return 1
    return valor * fatorial(valor-1)

n = int(input("Digite o numero de alunos da turma: "))
m = int(input("Digite o tamanho da primeira equipe: "))
print("Grupo 1: " + str(m))
print("Grupo 2: " + str(n+m))
resultado = fatorial(n)/(fatorial(m)*fatorial(n-m))
print("Total de possibilidade de criação de grupos = ", str(resultado))


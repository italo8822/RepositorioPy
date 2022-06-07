#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#   "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" 
# O programa deve no final emitir umaclassificação sobre a participação da pessoa no 
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda SIM ou NÃO para as perguntas a baixo:")

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

sins = respostas.count('sim')

if(sins == 2 ):
  print('suspeita')
elif(sins >= 3 and sins <=4):
  print('cumplice')
elif(sins == 5):
  print('assasino')
else:
    print('inocente')
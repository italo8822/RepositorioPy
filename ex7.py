#7.	Crie um código em que a pessoa coloque sua nota da primeira prova e da segunda, da matéria de matemática e 
# português e física e que leia a média de todas essas matérias. Também leia a média do resultado anterior entre 
# todas as matérias. Sabendo que gramatica e redação são notas diferentes que valem de 0 a 10, em que 
# ambas devem somar e dividir por dois, para dar a média de português.

redacao1=float(input('digite sua 1° nota de Redação:'))
redacao2=float(input('digite sua 2° nota de Redação:'))

gramatica1=float(input('digite sua 1° nota de Gramática:'))
gramatica2=float(input('digite sua 2° nota de Gramática:'))

matematica1=float(input('digite sua 1° nota de Matemática:'))
matematica2=float(input('digite sua 2° nota de Matemática:'))

fisica1=float(input('digite sua 1° nota de Física:'))
fisica2=float(input('digite sua 2° nota de Física:'))

portugues1=(redacao1+gramatica1)/2
portugues2=(redacao2+gramatica2)/2

media_portugues=(portugues1+portugues2)/2

media_matematica=(matematica1+matematica2)/2

media_fisica=(fisica1+fisica2)/2

media_geral=(media_fisica+media_matematica+media_portugues)/3

print('Sua média em Matemática foi:', media_matematica)

print('Sua média em Física foi:', media_fisica)

print('Sua média em Português foi:', media_portugues)

print('Sua média geral foi:', media_geral)
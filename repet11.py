#Elabore um algoritmo que, ultilizando as três estruturas de dados de repetição, imprima a tabuada do n 5
print("=== FOR ===")
for i in range (1,11):
    print("%s x 5 = %s" % (i, (i * 5)))

print("=== while ===")
i = 1
while i <= 10:
    print("%s x 5 = %s" % (i, (i * 5)))
    i += 1

print("=== do while ===")
i = 1
while True:
    print("%s x 5 = %s" % (i, (i * 5)))
    i += 1
    if i >= 11:
        break 

###############################################################################################################
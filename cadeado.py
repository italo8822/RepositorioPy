print()
print("Consegue abrir esse cadeado?")
print()
print("|6 8 2| => UM ESTA CERTO NO LUGAR CERTO")
print("|6 0 4| => UM ESTA CERTO NO LUGAR ERRADO")
print("|2 1 6| => DOIS ESTÃO CERTO NO LUGAR ERRADO")
print("|7 3 8| => TODOS ESTÃO ERRADOS")
print("|3 8 1| => UM ESTA CERTO NO LUGAR ERRADO")
codigo = int(input("\nDigite a senha do cadeado: "))

while codigo != 42:
    print("Tente novamente!")
    codigo = int(input("\nDigite a senho do cadeado: "))

print()
if codigo == (42):
    print("ACERTOU")
else:
    print("ERROU")

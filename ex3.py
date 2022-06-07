salario = float(input('Digite seu salario: '))

if salario <= 280.00:
    print('O seu salario será de: ', salario * 0.2 + salario)
elif 280 < salario <= 700:
    print('O seu salario será de: ', salario * 0.15 + salario) 
elif  700 < salario <= 1500.00:
    print('O seu salario será de: ', salario * 0.05 + salario)
else:
    print('OpS!')


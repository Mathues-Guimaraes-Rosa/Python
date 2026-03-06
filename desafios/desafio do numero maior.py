n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))

if (n1 == n2):
    print('os numeros sao iguais')

elif (n1 < n2):
    print(f'{n2} é maior que {n1}')

else:
    print(f'{n1} é maior que {n2}')
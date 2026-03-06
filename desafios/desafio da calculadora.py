print('digite 1 se você quer somar algo')
print('digite 2 se você quer subtrair algo')
print('digite 3 se você quer multiplicar algo')
print('digite 4 se você quer dividir algo')

conta = int(input())

if conta in [1, 2, 3, 4]:
    a = float(input('digite o primeiro valor: '))
    b = float(input('digite o segundo valor: '))
    if (conta == 1):
        r = a + b
        print(f'o resultado é igual a {r}')

    elif(conta == 2):
        r = a - b
        print(f'o resultado é igual a {r}')

    elif(conta == 3):
   
        r = a * b
        print(f'o resultado é igual a {r}')

    elif(conta == 4):
        if (b == 0):
            print('Divisão por zero não é permitida')
        else:
            r = a / b
            print(f'o resultado é igual a {r}')
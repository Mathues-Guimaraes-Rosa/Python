n = int(input('digite o numero: '))
nMax = int(input('digite até quanto deseja que a tabuada vá: '))


if (nMax <= 0):
    print('o numero maximo não pode ser menor que 0')

else:
    for numero in range(1, nMax + 1):
        r= n * numero
        print(f'{numero} x {n} = {r}')
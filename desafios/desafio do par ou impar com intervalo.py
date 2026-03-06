nMenor = int(input('digite o menor numero: '))
nMax = int(input('digite o numero maximo: '))

for numero in range(nMenor, nMax + 1):

    if(numero % 2 == 0):
        print(f'o numero {numero} é par')

    else:
        print(f'o numero {numero} é impar')
    
    
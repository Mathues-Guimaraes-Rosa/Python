import random
quanti = int(input('digite quantos numeros voce deseja: '))
nMax = int(input('digite o numero maximo: '))

if quanti > nMax:
    print('o numero maximo nao pode ser menor q a quantidade')

else:
    nPrint = []

    while len(nPrint) != quanti:
        a = random.randint(1, nMax)

        if (a not in nPrint):
            nPrint.append(a)

    print(nPrint)
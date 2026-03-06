import random
nMax =int(input('digite o numeor maximo: '))
nSecreto = random.randint(1, nMax)

nChute = 0

while True:
    chute = int(input(f'digite um número de 1 a {nMax}: '))
    nChute += 1

    if(chute == nSecreto):
        print('correto')
        print(f'você acerteou em {nChute} tentativas')
        break

    elif(chute < nSecreto):
        print(f'o numero é maior que {chute}')

    else:
        print(f'o número é menor que {chute}')
import random
nMax = int(input('digite o numero maximo: '))
nsecreto = random.randint(1, nMax)
 
nchute = 0

while True:
    chute = int(input(f'chute um numero de 1 a {nMax}:'))
    nchute += 1

    if (chute == nsecreto):
        print(f'parabens voce acertou em {nchute} tentativas')
        break

    elif (chute < nsecreto):
        print(f'o numero é maior q {chute}')

    else:
        print(f'o numero é menor q {chute}')
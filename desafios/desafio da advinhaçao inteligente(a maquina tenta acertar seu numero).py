import random
nMax = int(input('digite o numero maximo que você quer jogar: '))
nMenor = 1

x = 0
chute = random.randint(nMenor, nMax)
print(f'o computador chutou {chute}')

while True:
    x += 1

    if nMenor > nMax:
        print("Parece que houve um erro nas respostas. Não há mais números possíveis!")
        break

    maiorMenor = input('o numero é maior, menor ou acertei? ').lower()
    if (chute > nMax) or (chute < nMenor):
        print('isso na é possivel')
        print('por favor confira a resposta')
        break
           
    elif (maiorMenor.startswith('m') and 'aior' in maiorMenor):
        nMenor = chute + 1
        chute = (nMenor + nMax) // 2
        print(f'o computador chutou {chute}')
        

    elif(maiorMenor.startswith('m') and 'enor' in maiorMenor):
        nMax = chute - 1
        chute = (nMenor + nMax) // 2
        print(f'o computador chutou {chute}')
        
    
    elif(maiorMenor in ['acertou', 'acertei', 'sim' ]):
        print(f'Eu ganhei! Acertei o número {chute} em {x} tentativas.')
        break
    else:
        print('entrado invalida, por favor digite somente maior, menor o acertei')
        x -= 1
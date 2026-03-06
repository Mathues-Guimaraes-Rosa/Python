b = int(input('Digite a base do retângulo: '))
a = int(input('Digite a altura do retângulo: '))
area = b * a
print(f'A área do retângulo é: {area}')
if (area > 100):
    print('Terreno grande!')
else:
    print('Terreno pequeno!')
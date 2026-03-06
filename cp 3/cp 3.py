numeros = []
listaResultado = []

for i in range(0, 20 , 1):
    entrada = float(input('digite um numero: '))
    numeros.append(entrada)

mult = float(input('digite o valor para multiplicar: '))

for i in range(0, 20 , 1):
    resultado = numeros[i] * mult
    listaResultado.append(resultado)

print(f' lista numeros digitados: {numeros}')
print(f' lista numeros digitados: {listaResultado}')
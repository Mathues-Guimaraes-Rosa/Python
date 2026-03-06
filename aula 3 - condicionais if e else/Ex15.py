a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))

if (a <= 0 or b <= 0 or c <= 0):
      print('valores invalidos')
else:
        if (a < b + c or b < a + c or c < a + b):
                if (a != b and a != c and b != c):
                        print('o triangolo é escaleno ')
                elif (a == b and c == a and b == c):
                        print('o triangulo é equilatero')
                else:
                        print('o triangulo é isoceles')
                
        else:
                print('os valores nao podem formar um triangulo')
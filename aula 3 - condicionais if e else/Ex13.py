a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if (a>b and a>c):
    print(f'O maior número é o: {a}')
elif (b>a and b>c):
    print(f'O maior número é o: {b}')
else:
    print(f'O maior número é o: {c}')
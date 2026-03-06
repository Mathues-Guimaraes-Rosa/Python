x = int(input('digite um valor: '))
if(x <= 0):
    print('impossivel')

a = int(input('digite um valor: '))
b = int(input('digite um valor: '))
while True:
    if(a > b):
        print('impossivel, o primeiro numero deve ser menor q o segundo')
        b = int(input('digite um valor: '))
        i = b
    else:
        for i in range(b , (a-1) , -1):
            r = x * i
            print(r)
        break
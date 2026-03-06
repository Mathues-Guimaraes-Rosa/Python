x = int(input('digite um valor: '))
if(x <= 0):
    print('impossivel')
    
a = int(input('digite um valor: '))
b = int(input('digite um valor: '))
i = b
while (i >= a):
    if(a > b):
        print('impossivel, o primeiro numero deve ser menor q o segundo')
        b = int(input('digite um valor: '))
        i = b
    else:
        res = x * i
        print(res)
    i -= 1
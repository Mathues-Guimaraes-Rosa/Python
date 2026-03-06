nMax = int(input('digite o valor maximo: '))
i = 1
soma = 0
posi = 0
nega = 0
while True:
    if (0 < nMax <= 20):
        for i in range(1 , (nMax + 1), 1):
            num = int(input('digite um numero: '))
            if (i == 1):
                maior = num
                menor = num
                
            soma += num
            if (num > maior):
                maior = num
            elif(num < menor):
                menor = num
            if(num >= 0):
                posi += 1
            else:
                nega += 1
        break
    else:
        nMax = int(input('digite o numeor novamente: '))

media = soma / nMax
per_posi = (posi / nMax) * 100
per_nega = (nega / nMax) * 100
print(f'maior: {maior}, menor: {menor},soma: {soma},media: {media} ,percentural negativo: {per_nega}%, percentural positivo: {per_posi}%')
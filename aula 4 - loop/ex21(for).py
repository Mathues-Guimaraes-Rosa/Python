
soma = 0
posi = 0
nega = 0
for i in range(1 , 6 ,1):
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

media = soma / 5
per_posi = (posi / 5) * 100
per_nega = (nega * 100) / 5

print(f'maior: {maior}, menor: {menor},soma: {soma},media: {media} ,percentural negativo: {per_nega}%, percentual positivo {per_posi}%')
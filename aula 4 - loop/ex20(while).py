num = int(input("Digite um número para obter a tabuada: "))


while(num <= 0):
    print("Não pode número negativo!")
    num = int(input("Digite um outro número para obter a tabuada: "))


i = 1


while(i < 11):
    r = num * i
    print(f'{num} X {i} = {r}')
    i+=1

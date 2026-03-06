notas = []
soma = 0
acima = 0

nMax = int(input('digite o numero de alunos: '))

for i in range(0, nMax, 1): 
    try:
        nota = float(input('digite a nota do aluno: '))

        if(0 <= nota <= 10):
            notas.append(nota)
        
            if (i == 0):
                maior = nota
                menor = nota


            soma += nota


            if (nota > maior):
                maior = nota


            if (nota < menor):
                menor = nota


            if (nota >= 6):
                acima += 1
        else:
            print('as notas não podem ser menor que 0 ou maior que 10')
    except ValueError:
        print('digite apenas numeros!')

media = soma / nMax

print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
print(f'Os numeros acima da media: {acima}')
print(f'A média dos números: {media:.2f}')
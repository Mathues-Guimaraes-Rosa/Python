"""
Escreva um programa em Python que crie uma lista de 10 alunos, utilizando o conceito de dicionários, contendo os seguintes dados:

o Nome;
o Curso;
o Disciplina;
o Faltas;
os 3 checkpoints.

Depois da lista criada, exiba todos os alunos com seus dados um debaixo do outro.

Além disso, exiba somente os alunos com número de faltas acima de 8.

OBS: o programa deverá solicitar que o usuário informe os dados para alimentar a lista de dicionários."""
lista_alunos = []

for i in range(2):
    cps = []
    nome = input(f"escreva o nome do {i + 1} aluno")
    curso = input(f"escreva o nome do {i + 1} aluno")
    disciplina = input(f"escreva o nome do {i + 1} aluno")
    falta = int(input(f"escreva o nome do {i + 1} aluno"))
    for i in range(3):
        checkpoint = float(input(f"escreva o nome do {i + 1} aluno"))
        if( 0 > checkpoint <= 10 ):
            cps.append(checkpoint)
    aluno = {
        'Nome': nome,
        'Curso': curso,
        'Disciplina': disciplina,
        'Faltas': falta,
        'Notas Cps': cps
    }
lista_alunos.append(aluno)

print(lista_alunos)
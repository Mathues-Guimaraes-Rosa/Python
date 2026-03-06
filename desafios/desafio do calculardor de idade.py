nome = input("digite seu nome:")
anoNascimento = int(input('digite seu ano de nascimento:'))
anoFuturo = int(input('digite o ano futuro:'))

idade = anoFuturo - anoNascimento
if(anoNascimento > anoFuturo):
    print(f"perdao {nome}, isso é impossivel digite novamente")
else:
    print(f'{nome} sua idade no ano de {anoFuturo} sera de {idade}')
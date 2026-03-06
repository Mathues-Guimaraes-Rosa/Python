frase = input('digite uma frase: ').lower()

vogais = {'a': 0,'e': 0,'i':0,'o':0,'u':0}

for char in frase:
    if char in vogais:
        vogais[char] += 1

print('o nume de vogais é:')
for vogal, contagem in vogais.items():
    print(f'{vogal}: {contagem}')
a = int(input('digite a sua aceleração(em metros/s): '))
v0 = int(input('digite a sua velocidade(em metros/s): '))
t = int(input('digite o seu tempo de percurso (em segundos): '))

v = v0 + a*t

vf = v * 3.6

if (vf <= 40):
    print(f'{vf}km/h, veiculo mto lento')
elif (40 < vf <= 60):
    print(f'{vf}km/h ,velocidade permitida')
elif(60 < vf <= 80):
    print(f'{vf}km/h, velocidade de cruzeiro')
elif(80< vf <= 120):
    print(f'{vf}km/h, veiculo rapido')
else:
    print(f'{vf}km/h, veiculo mto rapido')
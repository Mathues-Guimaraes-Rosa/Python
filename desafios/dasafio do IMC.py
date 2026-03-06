peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))

imc = peso / (altura * altura)

if (imc <= 18.5 ):
    print(f'Seu IMC é {imc:.2f}, você esta abaixo do peso.')

elif(18.5 < imc <= 24.9):
    print(f'Seu IMC é {imc:.2f}, seu peso esta normal.')

elif(25 <= imc <= 29.9):
    print(f"Seu IMC é {imc:.2f}, você esta acima do peso")
else:
    print(f"Seu IMC é {imc:.2f}, você esta obeso.")
#correto
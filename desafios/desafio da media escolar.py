media1 = float(input('digite sua primeira media:'))
media2 = float(input('digite sua segunda media:'))
media3 = float(input('digite sua terceira media:'))

mediaFinal = (media1 + media2 + media3) / 3
if (mediaFinal >= 5):
    print(f'parabens passou de ano com uma meida {mediaFinal}')
elif(2.5 <= mediaFinal < 5):
    print(f'você ficou de recuperação final com uma media de {mediaFinal}')
else:
    print(f'você repetiu de ano com uma media de {mediaFinal}')
#correto
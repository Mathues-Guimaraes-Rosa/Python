p1 = float(input('digite sua nota da p1: '))
p2 = float(input('digite sua noa da p1: '))

r = (p1 + p2)/2

if (r >= 5):
    print('passou de ano')

elif(2 < r < 5):
    print('recuperação')

else:
    print('repetiu')
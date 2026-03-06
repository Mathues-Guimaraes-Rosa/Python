p1 = float(input('digite o valor do primeiro produto:'))
p2 = float(input('digite o valor do segundo produto:'))
p3 = float(input('digite o valor do terceiro produto:'))
p4 = float(input('digite o valor do quarto produto:'))
p5 = float(input('digite o valor do quinto produto:'))

valor = p1 + p2 + p3 + p4 + p5

volta = float(input(f'a soma dos produtos é {valor:.2f}, qual sera o valor para pagar:'))

troco = volta - valor

print(f'o seu troco é de {troco:.2f}')
# calcular a hipotenusa

from math import hypot
co = float(input('Informe a medida do Cateto Oposto: '))
ca = float(input('Informe a medida do Cateto Adjacente: '))
h = hypot(co, ca)
print('A medida da Hipotenusa é {:.2f}'.format(h))

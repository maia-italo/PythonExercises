# calcular o seno, cosseno e tangente

import math
ang = float(input('Informe o valor do ângulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O seno vale {:.2f} \nO cosseno vale {:.2f} \nA tangente vale {:.2f}'.format(s, c, t))

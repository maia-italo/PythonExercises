# mostrar somente a parte inteira de um número

# import math
from math import trunc
r = float(input('Digite um número real com sua parte decimal: '))
t = trunc(r)
print('A parte inteira de {} é {}'.format(r, t))
# Pode ser usado a função interna int()

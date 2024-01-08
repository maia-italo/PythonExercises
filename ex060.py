n = int(input('Digite um número para calcular o seu fatorial: '))
print('{}! = '.format(n), end='')
fa = 1
#for c in range(n, 0, -1):
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fa *= n
    n -= 1
print('{}'.format(fa))
# from math import factorial

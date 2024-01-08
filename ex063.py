print('--'*11)
print('Sequência Fibnacci')
print('--'*11)
n = int(input('Quantidade de termos Fibonacci: '))
print('~~~~'*n)
cont = 0
a = 0
b = 1
aux = 1
#while cont != n:
while cont < n:
    print(' {} '.format(a), end='')
    a = b
    b = aux
    aux += a
    cont += 1
print()
print('~~~~'*n)
print('\nFIM!')

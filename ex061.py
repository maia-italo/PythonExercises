print('Progressão Aritmética')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
aux = p
cont = 0
while cont <= 10:
    print('{}, '.format(aux), end='')
    aux += r
    cont += 1
print('...')

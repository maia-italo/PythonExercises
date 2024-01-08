print('Progressão Aritmética')
res = 10
t = 10
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
aux = p
cont = 0
while res != 0:
    while cont < res:
        print('{} '.format(aux), end=' ')
        aux += r
        cont += 1
    cont = 0
    res = int(input('\nMais quantos termos deseja ver? '))
    t += res
print('FIM!')
print('Um total de {} termos foram mostrados.'.format(t))

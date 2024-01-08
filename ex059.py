from time import sleep
n1 = int(input('Digite o 1o. valor: '))
n2 = int(input('Digite o 2o. valor: '))
r = 0
while r != 5:
    print('Qual operação você deseja?')
    r = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
'''))
    if r == 1:
        s = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, s))
        sleep(3)
    elif r == 2:
        m = n1 * n2
        print('A multiplicação ente {} x {} = {}'.format(n1, n2, m))
        sleep(3
              )
    elif r == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        sleep(3
              )
    elif r == 4:
        print('Informe os valores novamente')
        n1 = int(input('Digite o 1o. valor: '))
        n2 = int(input('Digite o 2o. valor: '))
    elif r == 5:
        print('Saindo...')
        sleep(1)
    else:
        print('Opção inválida! Tente novamente.')
        sleep(2)
    print('-='*20)
print('Fim!')

# jokenpô
from time import sleep
from random import randint
nome = str(input('Qual o seu nome? '))
es = [1, 2, 3]
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
j = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\n'))
if j >= 3:
    print('Opção inválida')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    print('-=' * 15)
    print('Computador jogou {}'.format(i[c]))
    print('{} jogou {}'.format(nome, i[j]))
    print('-=' * 15)

    if (c == 0 and j == 0) or (c == 1 and j == 1) or (c == 2 and j == 2):
        print('Empate!')
    elif (c == 0 and j == 2) or (c == 1 and j == 0) or (c == 2 and j == 1):
        print('Computador venceu!')
    elif (c == 0 and j == 1) or (c == 1 and j == 2) or (c == 2 and j == 0):
        print('{} venceu!'.format(nome))

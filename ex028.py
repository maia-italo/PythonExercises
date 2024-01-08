# jogo de advinhalçao

from random import randint
from time import sleep
print('-=-'*20)
print('Estou pensando em um número entre 0 e 5. tente advinhar...')
print('-=-'*20)
c = randint(0, 5)
n = int(input('Escolha o número: '))
print('PROCESSANDO...')
sleep(2)
if c == n:
    print('Uau! Vovê acertou! Eu pensei no número {}'.format(n))
else:
    print('Ganhei! Eu pensei no {} e não no {}'.format(c, n))

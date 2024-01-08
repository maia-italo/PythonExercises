from random import randint
c = randint(0, 10)
print('Estou pensando em um número entre 0 e 10!')
t = 1
j = int(input('Tente advinhar qual número estou pensando: '))
while c != j:
    if c > j:
        print('Mais...', end=' ')
    elif c < j:
        print('Menos...', end=' ')
    j = int(input('Tente novamente: '))
    t += 1
if t == 1:
    print('Parabéns! Você acertou! Eu pensei no número {} e você só precisou de uma tentativa!'.format(c))
else:
    print('Parabéns! Você acertou! Eu pensei no número {}, você precisou de {} tentativas!'.format(c, t))

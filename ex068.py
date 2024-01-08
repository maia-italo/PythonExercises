from random import randint
cont = 0
print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)
while True:
    j = ' '
    while j not in 'PI':
        j = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    n = int(input('Diga um valor: '))
    c = randint(0, 10)
    s = n + c
    print('-'*30)
    print(f'Você jogou {n} e o computador jogou {c}. O total de {s}, ', end='')
    print('deu PAR' if s % 2 == 0 else 'deu ÍMPAR')
    print('-'*30)
    if (s % 2 == 0 and j == 'I') or (s % 2 != 0 and j == 'P'):
        break
    else:
        print('Você venceu!')
        print('Vamos jogar novamente')
        cont += 1
print('='*30)
print('Você perdeu!')
print('=-='*10)
if cont == 0:
    print('GAME OVER! você não conseguiu me vencer!')
elif cont == 1:
    print('GAME OVER! Você me venceu 1 vez!')
else:
    print(f'GAME OVER! você venceu {cont} vezes')

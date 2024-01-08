# escolher um aluno

from random import choice
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('nome do aluno 4: ')
s = [a1, a2, a3, a4]
print('O aluno escolhido foi {}'.format(choice(s)))

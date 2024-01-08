# sortear a ordem de apresentação

from random import shuffle
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
o = [a1, a2, a3, a4]
shuffle(o)
print('A ordem de apresentação será \n{}'.format(o))

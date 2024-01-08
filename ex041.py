# categoria de natação

from datetime import date
print('-='*16)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-='*16)
print('')
nome = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 25:
    print('Sênior')
else:
    print('Master')

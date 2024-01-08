from datetime import date
pmaior = 0
pmenor = 0
hoje = date.today().year
for c in range(1, 8):
	ano = int(input('Ano de nascimento da {}a. pessoa: '.format(c)))
	if hoje - ano >= 21:
		pmaior += 1
	else:
		pmenor += 1
print('{} pessoas são maiores de idade'.format(pmaior))
print('{} pessoas menores de idade'.format(pmenor))

somai = 0
mi = 0
sm = 0
for c in range(1, 5):
	print('Dados da {}a. pessoa'.format(c))
	nome = str(input('Nome: ')).strip()
	sexo = str(input('Sexo [M/F]: ')).upper().strip()
	idade= int(input('Idade: '))
	somai += idade
	if sexo == 'M':
		if idade > mi:
			nomem = nome
	elif sexo == 'F':
		if idade < 20:
			sm += 1
print('A média de idade é de {:.0f}'.format(somai / 4))
print('{} é o homem mais velho'.format(nomem))
if sm == 0:
	print('Não há mulheres com menos de 20 anos')
elif sm == 1:
	print('Total de {} mulher com menos de 20 anos'.format(sm))
else:
	print('Total de {} mulheres com menos de 20 anos'.format(sm))

for c in range(1, 6):
	peso = float(input('Peso da {}a. pessoa: '.format(c)))
	if c == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		elif peso < menor:
			menor = peso
print('O maior peso digitado foi {}kg e o menor peso foi {}kg'.format(maior, menor))

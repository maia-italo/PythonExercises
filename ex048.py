print('Soma dos números ímpares divisíveis por 3 entre 1 e 500:')
s = 0
cont = 0
for c in range(3, 501, 3):
	if c % 2 != 0:
		s = s + c
		cont += 1
print('Todos os {} valores somados é igual a {}'.format(cont, s))

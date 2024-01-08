n = int(input('Escolha um número para mostrar a tabuada: '))
for c in range(1, 11):
	print('{:2} x {:2} = {}'.format(n, c, n*c))

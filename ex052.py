print('Verificador de número primo')
a = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
	if n % c == 0:
		a += 1
if a == 2:
	print('O número {} é primo'.format(n))
else:
	print('\033[31mO número {} não é primo\033[m'.format(n))

lista = []
par = list()
impar = list()
while True:
	lista.append(int(input('Digite um valor: ')))
	res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	while res not in 'SN':
		res = str(input('Resposta inválida! Deseja continuar? [S/N] ')).strip().upper()[0]
	if res == 'N':
		break
for v in lista:
	if v % 2 == 0:
		par.append(v)
	else:
		impar.append(v)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')

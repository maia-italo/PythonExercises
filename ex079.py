val = list()
while True:
	n = int(input('Digite um valor: '))
	if n not in val:
		val.append(n)
		print('Valor adicionado com succeso...')
	else:
		print('Valor duplicado! Não adicionado...')
	res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	while res not in 'SN':
		res = str(input('Resposta inválida! Deseja continuar? [S/N] ')).strip().upper()[0]
	if res=='N':
		break
val.sort()
print('='*40)
print(f'Você digitou os valores {val}')

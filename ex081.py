lista = []
while True:
	lista.append(int(input('Digite um valor: ')))
	res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	while res not in 'SN':
		res = str(input('Resposta inválida! Deseja continuar? [S/N] ')).strip().upper()[0]
	if res == 'N':
		break
print('='*40)
print(f'O total de números digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'Ordem decrescente {lista}')
if 5 in lista:
	if lista.count(5) == 1:
		print('O número 5 foi digitado 1 vez')
	else:
		print(f'O número 5 foi digitado {lista.count(5)} vezes')
else:
	print('O número 5 não está na lista')

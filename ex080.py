lista = []
for c in range(0, 5):
	n = int(input('Digite um valor: '))
	if c == 0 or n > lista[-1]:
		lista.append(n)
		print(f'Adicionado ao final da lista...')
	else:
#		for p, a in enumerate(lista):
#			if n < lista[0]:
#				lista.insert(0, n)
#				print('Adicionado na posição 0 da lista...')
#			if n == lista[0]:
#				lista.insert(0, n)
# 				print('Adicionado na posição 1 da lista...')
#			elif n > a:
#				lista.insert(p+1, n)
#				print(f'Adicionado na posição {p+1} da lista...')
		pos = 0
		while pos <= len(lista):
			if n <= lista[pos]:
				lista.insert(pos, n)
				print(f'Adicionado na posição {pos} da lista...')
				break
			pos += 1
print('-='*20)
print(f'Os valores digitador em ordem foram {lista}')

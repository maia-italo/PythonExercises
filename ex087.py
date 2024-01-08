matriz = [[], [], []]
par = col3 = 0
for c in range(0, 3): # essa variável era pra ser l
	for l in range(0,3): # essa variável era pra ser c
		matriz[c].append(int(input(f'Digite o valor para a posição [{c}, {l}]: ')))
print('=-'*20)
for c in range(0, 3):
	for l in range(0, 3):
		print(f'[ {matriz[c][l]:^5} ]', end='')
		if matriz[c][l] % 2 == 0:
			par += matriz[c][l]
		if l == 2:
			col3 += matriz[c][l]
		if l == 0  and c == 1:
			maior = matriz[c][l]
		elif c == 1:
			if matriz[c][l] > maior:
				maior = matriz[c][l]
	print()
print('=-'*20)
print(f'A soma de todos os valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {maior}')

### Começar o laço de repetição com a linha

### Correção da soma da coluna 3
# For c in range(0,3):
# col3 += matriz[c][2]

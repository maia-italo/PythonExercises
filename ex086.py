matriz = [[], [], []]
for c in range(0, 3):
	for l in range(0,3):
		matriz[c].append(int(input(f'Digite o valor para a posição [{c}, {l}]: ')))
print('=-'*20)
for c in range(0, 3):
	for l in range(0, 3):
		print(f'[ {matriz[c][l]:^5} ]', end='')
	print()

### Começar o laço de repetição com a linha

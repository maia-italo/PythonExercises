val = []
for v in range(0, 5):
	val.append(int(input(f'Digite um valor na posição {v}: ')))
	if v == 0:
		maior = menor = val[v]
	else:
		if val[v] > maior:
			maior = val[v]
		if val[v] < menor:
			menor = val[v]
print('=-'*30)
print(f'Os valores digitados foram {val}')
print(f'O maior valor da lista é {maior} e está nas posições ', end='')
for i, v in enumerate(val):
	if v == maior:
		print(f'{i}, ', end='')
print()
print(f'O menor valor da lista é {menor} e está nas posições ', end='')
for i, v in enumerate(val):
	if v == menor:
		print(f'{i}, ', end='')
print()

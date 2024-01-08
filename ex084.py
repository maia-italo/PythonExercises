pess = list()
dado = list()
pesado = list()
leve = list()
maispes = maislev = 0
while True:
	dado.append(str(input('Nome: ')))
	dado.append(float(input('Peso: ')))
	if len(pess) == 0:
		maispes = maislev = dado[1]
	else:
		if dado[1] > maispes:
			maispes = dado[1]
		if dado[1] < maislev:
			maislev = dado[1]
	pess.append(dado[:])
	dado.clear()
	res = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()
	if res == 'N':
		break
print('=-'*20)
print(f'Total de {len(pess)} pessoas cadastradas')
for p in pess:
	if p[1] == maispes:
		pesado.append(p[0])
	elif p[1] == maislev:
		leve.append(p[0])
print(f'O maior peso foi de {maispes:.1f}Kg. Peso de {pesado}')
print(f'O menor peso foi de {maislev:.1f}Kg. Peso de {leve}')

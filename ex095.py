time = list()
partidas = list()
aprv = dict()

while True:
	aprv.clear()
	aprv['nome'] = str(input('Nome do jogador: '))
	part = int(input(f'Quantas partidas {aprv["nome"]} jogou? '))
	gols = list()
	for c in range(1, part +1):
		gols.append(int(input(f'Quantos gol na partida {c}? ')))
	aprv['gols'] = gols[:]
	aprv['total'] = sum(gols)
	time.append(aprv.copy())
	while True:
		res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
		if res in 'SN':
			break
		print('ERRO! Responda apenas S ou N.')
	if res == 'N':
		break
print('-='*30)
print('cod ', end='')
for i in aprv.keys():
	print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
	print(f'{k:>4}', end=' ')
	for d in v.values():
		print(f'{str(d):<15}', end='')
	print()
print('-='*30)
while True:
	busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
	if busca == 999:
		break
	if busca >= len(time):
		print('ERRO! Não existe jogador com codigo {busca}!')
	else:
		print(f'  -- Levantamento do jogador {time[busca]["nome"]}: ')
		for i, g in enumerate(time[busca]['gols']):
			print(f'  No jogo {i+1} fez {g} gols')
	print('-='*30)
print('  VOLTE SEMPRE  ')

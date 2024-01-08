aprv = dict()
aprv['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {aprv["nome"]} jogou? '))
gols = list()
for c in range(1, part +1):
	gols.append(int(input(f'Quantos gol na partida {c}? ')))
aprv['gols'] = gols[:]
aprv['total'] = sum(gols)
print('-='*30)
print(f'O jogador {aprv["nome"]} jogou {part} partidas.')
for i, v in enumerate(aprv['gols']):
	print(f'  => Na patida {i+1}, fez {v} gols.')
print(f'Foi um total de {aprv["total"]} gols')

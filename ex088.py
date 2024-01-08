from random import randint
from time import sleep
jogo = list()
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
q = int(input('Quantos jogos deseja sortear? '))
print(f'--- SORTEANDO {q} JOGOS ---')
for c in range(0, q):
	jogo.append(list())
	while True:
		j = randint(1, 60)
		if j not in jogo[c]:
			jogo[c].append(j)
		if len(jogo[c]) == 6:
			break
	sleep(1)
	print(f'Jogo{c+1}: {sorted(jogo[c])}')
sleep(0.5)
print('------ < BOA SORTE! > ------')

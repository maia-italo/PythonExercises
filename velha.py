import os

def tabuleiro():
	os.system('clear') or None
	print('-------------------')
	for l in range(3):
		for c in range(3):
			if t[l][c] == 'X':
				print(f'| \033[1;31m{t[l][c]}\033[m |', end='')
			elif t[l][c] == 'O':
				print(f'| \033[1;36m{t[l][c]}\033[m |', end='')
			else:
				print(f'| {t[l][c]} |', end='')
		print()
	print('-------------------')


def jogar(troca):
	troca = False
	po = input(f'Qual posição deseja jogar [ {simb} ]? ')
	if po == '1':
		if t[0][0] == 'X' or t[0][0] == 'O':
			print('Jogada inválida ')
		else:
			t[0][0] = simb
			troca = True
	elif po == '2':
		if t[0][1] == 'X' or t[0][1] == 'O':
			print('Jogada inválida ')
		else:
			t[0][1] = simb
			troca = True
	elif po == '3':
		if t[0][2] == 'X' or t[0][2] == 'O':
			print('Jogada inválida ')
		else:
			t[0][2] = simb
			troca = True
	elif po == '4':
		if t[1][0] == 'X' or t[1][0] == 'O':
			print('Jogada inválida ')
		else:
			t[1][0] = simb
			troca = True
	elif po == '5':
		if t[1][1] == 'X' or t[1][1] == 'O':
			print('Jogada inválida ')
		else:
			t[1][1] = simb
			troca = True
	elif po == '6':
		if t[1][2] == 'X' or t[1][2] == 'O':
			print('Jogada inválida ')
		else:
			t[1][2] = simb
			troca = True
	elif po == '7':
		if t[2][0] == 'X' or t[2][0] == 'O':
			print('Jogada inválida ')
		else:
			t[2][0] = simb
			troca = True
	elif po == '8':
		if t[2][1] == 'X' or t[2][1] == 'O':
			print('Jogada inválida ')
		else:
			t[2][1] = simb
			troca = True
	elif po == '9':
		if t[2][2] == 'X' or t[2][2] == 'O':
			print('Jogada inválida ')
		else:
			t[2][2] = simb
			troca = True
	else:
		print('Posição Inválida')
	return troca


def muda_j(s):
	if s == 'X':
		s = 'O'
	else:
		s = 'X'
	return s


def fim_jogo():
	val = 0
	for l in range(3):
		if t[l][0] == t[l][1] and t[l][1] == t[l][2]:
			val = 1
	for c in range(3):
		if t[0][c] == t[1][c] and t[1][c] == t[2][c]:
			val = 1
	if t[0][0] == t[1][1] and t[1][1] == t[2][2]:
		val = 1
	if t[0][2] == t[1][1] and t[1][1] == t[2][0]:
		val = 1
	ocorr = 0
	for l in range(3):
		for c in range(3):
			if t[l][c] != 'X' and t[l][c] != 'O':
				ocorr += 1
	if ocorr == 0:
		val = 2
	return val


t = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
simb = 'X'

while fim_jogo() == 0:
	tabuleiro()
	while jogar(t) == False:
		jogar(t)
	simb = muda_j(simb)

tabuleiro()

print('Fim de jogo!')
simb = muda_j(simb)
if fim_jogo() == 1:
	print(f'{simb} é o vencedor!!!')
if fim_jogo() == 2:
	print('Deu velha!')


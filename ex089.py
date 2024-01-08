aluno = list()
while True:
	nome = str(input('Nome: ')).capitalize().strip()
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	media = (nota1 + nota2) / 2
	aluno.append([nome , [nota1, nota2], media])
	res = str(input('Quer continuar? [S/N] ')).strip().upper()
	if res == 'N':
		break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(aluno):
	print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
	print('-'*30)
	opc = int(input('Mostrar notas de qual aluno? (999 para parar) '))
	if opc == 999:
		print('FINALIZANDO...')
		break
	if opc <= len(aluno) - 1:
		print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')

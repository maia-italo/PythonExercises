galera = list()
pessoa = dict()

while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
		if pessoa['sexo'] in 'MF':
			break
		print('Ero! Por favor digite apenad F ou M')
	pessoa['idade'] = int(input('Idade: '))
	soma += pessoa['idade']
	galera.append(pessoa.copy)
	while True:
		res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
		if res in 'SN':
			break
		print('ERRO! Responda apenas S uo N.')
	if res == 'S':
		break
print('-='*30)
print(f'Ao todo temos {len[galera]} pessoas cadastradas')
media = soma / len(galera)
print(f'A mádia de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram', end='')
for p in gtalera:
	if p['sexo'] in 'fF':
		print(f'{p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média:', end=' ')
for p in galera:
	if p['idade'] >= média:
		print('   ')
		for k, v in p.items():
			print(f'{k} = {v};', end=' ')
		print()
print('ENCERRANDO...')

import datetime
inss = dict()
inss['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
inss['idade'] = datetime.now().year() - nasc
inss['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if inss['CTPS'] != 0:
	inss['Contratação'] = int(input('Ano de contratação: '))
	inss['Salário'] = float(input('Salário: R$'))
	inss['Aposentadoria'] = inss['idade'] + (inss['Contratação'] + 35) - datetime.now().year()
print('-=' * 30)

for k, v in inss.items():
	print(f'  - {k} tem o valor {v}')

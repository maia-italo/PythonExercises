from interface import *
from arquivo import *
from time import sleep


arq = 'dados.txt'

if not arquivoexiste(arq):
	criararquivo(arq)

while True:
	res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
	'Sair do sistema'])
	if res == 1:
		# Opção de listar o conteúdo de um arquivo
		lerarquivo(arq)
	elif res == 2:
		# Opção de cadastrar uma nova pessoa
		cabeçalho('NOVO CADASTRO')
		nome = str(input('Nome: '))
		idade = leiaint('Idade: ')
		cadastrar(arq, nome, idade)
	elif res == 3:
		# Opção de sair do sistema
		cabeçalho('Saindo do sistema... Até logo!')
		break
	else:
		# Digitou uma opção erradano menu
		print('\033[0;31mERRO! Digite uma opção válida!\033[m')
	sleep(1.5)

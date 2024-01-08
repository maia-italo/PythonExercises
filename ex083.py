ex = str(input('Digite a expressão: '))
if ex[0] == ')':
	print('Essa expressão não é válida!')
else:
	if ex.count('(') == ex.count(')'):
		print('Essa expressão é valida!')
	else:
		print('Essa expressão não é válida!')

""" Correção
exp = str(input('Digite a espressão: '))
pilha = list()
for s in exp:
	if s == '(':
		pilha.append('(')
	elif s == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print('A expressão é valida!')
else:
	print('A expressão não é válida')"""
# O meu código não avalia se o parêntese foi fechado corretamente, apenas se
# a quantidade está correta.
# No caso de parenteses abertos e fechados no meio da expressão, pode ser
# que a lógica aritmética ignore isso, porém se não acontecer, o código
# corrigido seria melhor indicado.

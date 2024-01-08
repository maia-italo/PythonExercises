def moeda(n=0, m='R$'):
	'''
	-> Formata o valor para moeda
	:param n: Valor a ser formatado
	:param m: Simbolo da moeda (R$ por padrão)
	:return: Valor formatado
	'''
	return f'{m}{n:.2f}'.replace('.', ',')


def aumentar(n=0, p=0, f=False):
	r = n + (n*p/100)
	return r if f is False else moeda(r)


def diminuir(n=0, p=0, f=False):
	r = n - (n*p/100)
	return r if not f else moeda(r)


def metade(n=0, f=False):
	r = n/2
	if f:
		return moeda(r)
	else:
		return r


def dobro(n=0, f=False):
	r = n*2
	return r if not f else moeda(r)


def resumo(n=0, a=10, r=5):
	"""
	-> Resumo do valor
	:param n: Valor a ser resumido
	:param a: Porcentagem de aumento (10 por padrão)
	:param r: Porcentagem de redução (5 por padrão)
	:return: Não retorna valor
	"""
	print('-'*33)
	print(f'{"RESUMO DE VALOR":^33}')
	print('-'*33)
	print(f'Preço analizado: \t{moeda(n)}')
	print(f'Dobro do preço: \t{dobro(n, True)}')
	print(f'Metade do preço: \t{metade(n, True)}')
	print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
	print(f'{r}% de redução: \t{diminuir(n, r, True)}')
	print('-'*33)

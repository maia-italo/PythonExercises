def fatorial(n, show=False):
	"""
	-> Calcula o Fatorial de um número.
	:param n: Onúmero a ser calculado.
	:param show: (opcional) Mostrar ou não a conta.
	:return: O valor do Fatorial de um número n.
	"""
	f = 1
	for c in range(n, 0, -1):
		f *= c
	if show:
		for a in range(1, n):
			print(a, end=' x ')
		print(n, end=' = ')
		print(f)
	return f


n = int(input('Digite o número para calcular seu fatorial: '))
print(f'{n}! = {fatorial(n, True)}')

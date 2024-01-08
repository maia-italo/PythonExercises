def moeda(n=0, m='R$'):
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

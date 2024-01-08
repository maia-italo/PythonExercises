def leiadinheiro(msg):
	ok = False
	valor = 0
	while not ok:
		a = str(input(msg)).strip().replace(',', '.')
		if a.isalpha() or a == '':
			print(f'\033[0;31mERRO! \"{a}\" é um preço inválido\033[m')
		else:
			ok = True
			return float(a)

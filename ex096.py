def area(l, c):
		a = l * c
	print(f'A área de um terreno {l} x {c} é de {a}m²')


print('Controle de terrenos')
print('-'*20)
a = float(input('Largura do terreno: (m) '))
b = float(input('Comprimento do terreno: (m) '))
area(a, b)

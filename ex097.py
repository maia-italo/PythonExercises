def escreva(txt):
	print('~' * (len(txt)+4))
	print(f'  {txt}  ')
	print('~' * (len(txt)+4))


escreva(str(input('Digite um texto: ')))

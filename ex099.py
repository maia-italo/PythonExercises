def maior(* n):
	cont = m = 0
	print('Analizando os valores passados... ')
	for v in n:
		if v > m:
			m = v
	print(f'{n} foram passados {len(n)} valores')
	print(f'O maior valor passado foi {m}')


print('-='*20)
maior(3, 7, 5, 4, 2)
print('-='*20)
maior(4, 1, 8)
print('-='*20)
maior(5, 3)
print('-='*20)
maior(6)
print('-='*20)
maior()

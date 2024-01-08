from time import sleep

def contador(i, f, p):
	if p < 0:
		p = p * (-1)
	if p == 0:
		p = 1
	print(f'Contando de {i} até {f} de {p} em {p}')
	sleep(1)
	if i > f:
		for c in range(i, f-1 , -p):
			sleep(0.5)
			print(f'{c} ', end='', flush=True)
		sleep(1)
		print('FIM!')
	elif i < f:
		for c in range(i, f+1, p):
			sleep(0.5)
			print(f'{c} ', end='', flush=True)
		sleep(1)
		print('FIM!')
	else:
		print('Não posso contar!')
	print('-='*20)


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Começo da contagem: ')), int(input('Fim da contagem: ')),
int(input('Contar de quanto em quanto? ')))

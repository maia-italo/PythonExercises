n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')
# num = int(input('Digite um número entre 0 e 20: '))
# while num < 0 or num > 20:
# 	num = int(input('Tente novamente! Digite um número entre 0 e 20: '))
while True:
	while True:
		num = int(input('Digite um número entre 0 e 20: '))
		if 0 <= num <= 20:
			break
		print('Tente novamente! ', end='')
	print(f'Você digitou o número {n[num]}')
	while True:
		res = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
		if res in 'SN':
			break
	if res == 'N':
		break

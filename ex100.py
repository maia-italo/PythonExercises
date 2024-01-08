from random import randint
from time import sleep

def sorteia(lista):
	print('Sorteando 5 valores da lista: ', end='')
	for c in range(0, 5):
		n = (randint(1, 10))
		lista.append(n)
		print(f'{n} ', end='', flush=True)
		sleep(0.3)
	print('PRONTO!')


def somaPar(lista):
	sp = 0
	for n in lista:
		if n % 2 == 0:
			sp += n
	print(f'Somando os valores pares de {lista}, temos {sp}')


num = list()
sorteia(num)
somaPar(num)

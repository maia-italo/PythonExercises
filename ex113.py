def leiaint(msg):
	while True:

		try:
			n = int(input(msg))
		except (KeyboardInterrupt):
			print('O usuário preferiu não digitar esse número')
			return 0
		except (ValueError, TypeError):
			print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
			continue
		else:
			return n


def leiafloat(msg):
	while True:
		try:
			n = float(input(msg).replace(',', '.'))
		except (KeyboardInterrupt):
			print('\nO usuário preferiu não digitar esse número')
			return 0
		except (ValueError, TypeError):
			print('\033[0;31mErro! Digite um número real válido.\033[m')
			continue
		else:
			return n


n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n} e o real foi {f}')

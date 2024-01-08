
def par(n=0):
	if n % 2 == 0:
		return True
	else:
		return False


num = int(input('digite um número: '))
if par(num):
	print(f'É par!')
else:
	print(f'Não é par!')

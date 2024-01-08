from random import randint
n = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),
randint(0, 100))
print(f'Números gerados: {n}')
#for c in range(0, 5):
#	if c == 0:
#		maior = n[c]
#		menor = n[c]
#	if n[c] > maior:
#		maior = n[c]
#	if n[c] < menor:
#		menor = n[c]
#print(f'O maior valor foi {maior}')
#print(f'O menor valor foi {menor}')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')

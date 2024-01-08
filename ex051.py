print('Progressão Aritmética')
#p = int(input('Digite o primeiro termo: '))
#r = int(input('Digite a razão: '))
#aux = p
#for c in range(0, 10):
#	print('{}, '.format(aux), end='')
#	aux += r
#print('...')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10-1) * r
for c in range(p, d + r, r):
	print('{}, '.format(c), end='')
print('...')

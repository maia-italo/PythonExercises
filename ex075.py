n = (int(input('Digite o primeiro valor: ')),
int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')),
int(input('Digite o último valor: ')))
cont = 0
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
	print(f'O primeiro número 3 está na {n.index(3)+1}ª posição')
else:
	print('O número 3 não foi digitado nenhuma vez')
print('Os números pares são:', end=' ')
for c in n:
	if c%2==0:
		 cont+=1
		 print(c, end='  ')
if cont==0:
	print('Não foram digitados números pares')

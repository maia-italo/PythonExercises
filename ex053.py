f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
'''i = ''
for l in range(len(j) -1, -1, -1):
    i += j[l]'''
i = j[::-1]
print(i)
if i == j:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')

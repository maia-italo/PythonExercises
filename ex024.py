# Cidade que começa com 'Santo'

ci = str(input('Digite o nome de uma cidade: ')).strip()
cs = ci.lower().split()
print('Começa com Santo:', cs[0] == 'santo')

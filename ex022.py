# dissecando uma string

nc = str(input('Digite o seu nome completo: ')).strip()
nd = nc.split()
print('Seu nome em maiúsculas é {}'.format(nc.upper()))
print('Seu nome em minúsculas é {}'.format(nc.lower()))
print('O total de letras é {}'.format(len(nc)-nc.count(' ')))
print('O primeiro nome tem {} caracteres'.format(len(nd[0])))

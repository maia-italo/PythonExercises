# dissecando um nome completo

nome = str(input('Digite seu nome completo: ')).strip()
ns = nome.split()
print('Muito prazer em te conhecer!')
print('Primeiro: {}'.format(ns[0]))
print('Último: {}'.format(ns[len(ns)-1]))

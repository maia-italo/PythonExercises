time = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense',
'Bragantino', 'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá',
'São Paulo', 'Cruzeiro', 'Corintians', 'Internacional', 'Goiás', 'Bahia',
'Santos', 'Vasco', 'América-MG', 'Coritiba')
print('-'*30)
print('{:^30}'.format('CAMPEONATO BRASILEIRO'))
print('-'*30)
print('Os primeiros colocados são:')
# print(f'Os cinco primeiros times são {time[0:5]}')
for c in range(0, 5):
	print(f'{c+1}º - {time[c]}')
print('Zona de rebaixamento:')
# print(f'Os últimos quatro times são {time[-4:]}')
for c in range(16, 20):
	print(f'{c+1}º - {time[c]}')
print('Ordem alfabética:')
print(sorted(time))
print(f'Cuiabá está na {time.index("Cuiabá")+1}ª posição')

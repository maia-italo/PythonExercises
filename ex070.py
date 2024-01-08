s = mil = 0
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    res = ' '
    nome = str(input('Produto: ')).strip().capitalize()
    pre = float(input('Preço: R$'))
    if s == 0 or pre < prebarato:
        barato = nome
        prebarato = pre
    if pre > 1000:
        mil += 1
    s += pre
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi R${s:.2f}')
print(f'Total de {mil} produtos custam mais de R$1000.00')
print(f'{barato} é o produto mais barato custando R${prebarato:.2f}')

print('-'*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-'*30)
valor = int(input('Qual o valor do saque? R$'))
'''c50 = valor // 50
valor -= c50 * 50
c20 = valor // 20
valor -= c20 * 20
c10 = valor // 10
valor -= c10 *10
c1 = valor // 1
if c50 > 0:
    print(f'Total de {c50} cédulas de R$50')
if c20 > 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10')
if c1 > 0:
    print(f'Total de {c1} cédulas de R$1')'''
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-'*30)
print('Tenha um bom dia e volte sempre!')

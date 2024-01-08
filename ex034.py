# Pergunte o salário do funcionário e calcule o aumento

sal = float(input('Salário do funcionário: R$'))
if sal > 1250:
    aum = sal + (sal*0.10)
else:
    aum = sal + (sal*0.15)
print('O novo salário do funcionário é de R${:.2f}'.format(aum))

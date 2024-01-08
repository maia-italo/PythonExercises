# aprovado, recuperação ou reprovado

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print('Média: {:.1f}'.format(m))
if m < 5:
    print('\033[31mREPROVADO\033[m')
elif 5 <= m < 7:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')

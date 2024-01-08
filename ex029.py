# calcula a multa se ultrapassar 80km/h

v = float(input('Qual a velocidade do carro? '))
if v > 80:
    m = (v-80)*7
    print('\033[31mMULTADO!\033[m Você excedeu a velocidade máxima permitida de 80 km/h! Você foi multado em \033[7;37mR${:.2f}\033[m'.format(m))
else:
    print('Boa viagem!')
print('Dirija com segurança!')

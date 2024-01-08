# Alistamento militar

from datetime import date
nome = str(input('Digite seu nome: '))
ano = int(input('Ano de nascimento: '))
sexo = str(input('Sexo [M/F]: ')).upper()
al = date.today().year - ano
cal = al - 18
if sexo == 'M':
    if cal == 0:
        print('Vovê deverá se apresentar no serviço de alistamento esse ano!')
    elif cal < 0:
        cal = cal * (-1)
        print('Você deverá se alistar em {} anos'.format(cal))
    else:
        nd = date.today().year - cal
        print('Seu ano de alistamento foi {}'.format(nd))
        print('Se você se alistou, parabéns, você cumpriu com seu dever de cidadão')
else:
    print('Você não tem a obrigação de se alistar')

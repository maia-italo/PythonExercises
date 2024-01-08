# Programa para calcular o valor da passagem

d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(d))
if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45
print('O valor da sua passagem é de \033[33mR${:.2f}\033[m'.format(v))

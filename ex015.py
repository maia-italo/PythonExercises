# calcular o preço do aluguel de um carro

print('=========ALUGUEL DE CARRO=========')
d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
valor = (d*60) + (km*0.15)
print('O total a pagar é R${:.2f}'.format(valor))

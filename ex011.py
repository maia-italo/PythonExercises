# calcular a quantidade de tinta usada para pintar uma parede

print('Calcular quantidade de tinta')
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l*a
tinta = area/2
print('Sua parede tem {}m²'.format(area))
print('Você precisa de {:.3f} litros de tinta'.format(tinta))

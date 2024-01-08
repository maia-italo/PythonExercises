print('-=' * 20)
print('Analizador de triângulos')
print('-=' * 20)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    tri = True
else:
    tri = False

if tri == True:
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo ESCALENO')
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r3 != r1) or (r1 == r3 and r3 != r2):
        print('É um triângulo ISÓSCELES')
else:
    print('\033[31mNão é possível formar um Triângulo.\033[m')

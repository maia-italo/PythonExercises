# Analizando 3 retas para saber se é posível formar um triângulo

print('-='*20)
print('Analizador de triângulos')
print('-='*20)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    tri = True
else:
    tri = False

if tri == True:
    print('\033[32mEssas retas podem formar um Triângulo!\033[m')
else:
    print('\033[31mNão é possível formar um Triângulo.\033[m')

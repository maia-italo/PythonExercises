print('--' * 9)
print('CALCULADORA DE IMC')
print('--' * 9)
print()
nome = str(input('Nome: ')).strip()
altura = float(input('Altura: '))
peso = float(input('Peso: '))
print()
imc = peso / (altura**2)
if imc < 15:
    print('Desnutrição')
elif 15 <= imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

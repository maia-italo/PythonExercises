# Programa que lê 3 números e diz qual é o maior e o menor

n1 = int(input('Primeiro nùmero: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n2
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior número é {} e o menor é {}'.format(maior, menor))

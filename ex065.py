#n = int(input('Digite um valor: '))
#maior = n
#menor = n
#soma = n
#cont = 1
#res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
res = 'S'
soma = cont = media = maior = menor = 0
while res == 'S':
    n = int(input('Digite um valor: '))
    if n < maior:
        menor = n
    elif n > menor:
        maior = n
    soma += n
    cont += 1
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('A média dos valores é {}'.format(media))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))

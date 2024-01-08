# conversor para binário, Octal ou hexadecimal

num = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão?\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n'))
if base == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')

# preço de acordo com a forma de pagamento

p = float(input('Digite o preço: R$'))
print('Forma de pagamento:\n[1] À vista\n[2] À vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais')
f = int(input())
if f == 1:
    p = p - (p*0.10)
elif f == 2:
    p = p - (p*0.05)
elif f == 3:
    p = p
    print('Suas compras serão parceladas em 2x de {}'.format(p / 2))
elif f == 4:
    p = p + (p*0.20)
    t = int(input('Em quantas vezes deseja parcelar? '))
    print('Suas compras serão parceladas em {}x de {}'.format(t, p/t))
else:
    print('Opção inválida')
print('O preço a ser pago é R${:.2f}'.format(p))

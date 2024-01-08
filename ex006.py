n = int(input('Digite um número: '))
# print('O número escolhido foi {}\nO dobro é {}\nO triplo é {}\nE a raiz quadrada é {}'.format(n, n*2, n*3, n**(1/2)))
d = n * 2
t = n * 3
# r = pow(n, (1/2))
r = n ** (1/2)
print('O dobro de {} é {}\nO triplo de {} é {}\nE a raiz quadrada de {} é {:.3f}'.format(n, d, n, t, n, r))

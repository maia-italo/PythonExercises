while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c:2} X {n:2} = {c*n}')
    print('-'*20)
print('Programa TABUADA encerrado! Volte sempre!')

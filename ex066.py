s = c = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'O total de números foi {c} e a soma entre eles é {s}')

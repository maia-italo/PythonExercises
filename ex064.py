#n = int(input('Digite um número [999 para parar]: '))
#s = n
#con = 1
#while n != 999:
#    n = int(input('Digite um número [999 para parar]: '))
#    if n != 999:
#        s += n
#        con += 1
#print('O total de números digitados foi {} e a soma entre eles é {}'.format(con, s))

n = c = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('O total de números digitados foi {} e a soma entre eles é {}'.format(c, s))

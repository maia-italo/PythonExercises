nome = str(input('Digite seu nome: ')).strip()
idade = int(input('Digite sua idade: '))
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]#pegar só a primeira letra
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo novamente [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

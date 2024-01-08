res = 'S'
maior = homem = mulher = 0
while res == 'S':
    sexo = ' '
    res = ' '
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-'*20)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print('======FIM DO PROGRAMA======')
print(f'O total de pessoas maiores de idade foi {maior}')
if homem > 1:
    print(f'Ao todo temos {homem} homens cadastrados')
elif homem == 1:
    print(f'Ao todo temos {homem} homem cadastrado')
else:
    print('Nenhum homem foi cadastrado')
if mulher == 1:
    print(f'Apenas uma mulher com menos de 20 anos')
elif mulher > 1:
    print(f'{mulher} mulheres com menos de 20 anos')
else:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada')

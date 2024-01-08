# aprovando empréstimo bancário

nome = str(input('Qual o seu nome? '))
sal = float(input('Qual o seu salário mensal? R$'))
casa = float(input('Qual o valor da casa? R$'))
ano = int(input('Em quantos anos você deseja pagar? '))
parcela = casa / (ano * 12)
print('Você deverá pagar R${:.2f} por mês'.format(parcela))
if parcela <= sal * 0.30:
    print('\033[32mEmpéstimo aprovado!\033[m')
else:
    print('\033[31mEmpréstimo negado!\033[m')

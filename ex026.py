# dissecando uma string (usando .rfind())

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra (a) aparece {} vezes'.format(frase.count('a')))
print('A primeira letra (a) está na posição {}'.format(frase.find('a')+1))
print('A última letra (a) está na posição {}'.format(frase.rfind('a')+1))

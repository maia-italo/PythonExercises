palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
	print(f'\nNa palavra {c.upper()} temos as vogais', end=' ')
	for a in c:
		if a.lower() in 'aeiou':
			print(a, end=' ')

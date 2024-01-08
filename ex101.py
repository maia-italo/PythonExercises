def voto(ano):
	from datetime import date
	idade = date.today().year - ano
	if idade < 16:
		return f'Com {idade} anos: VOTO NEGADO'
	elif 16 <= idade < 18 or idade > 65:
		return f'Com {idade} anos: VOTO OPCIONAL'
	else:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal
a = int(input('Ano de nascimento: '))
print(voto(a))

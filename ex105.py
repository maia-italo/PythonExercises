def notas(* n, sit=False):
	"""
	-> Função para analizar notas e situações de vários alunos.
	:param n: uma ou mais notas dos alunos (aceita várias)
	:param sit: valor opcional, indicando se deve ou não adicionar a situação da turma.
	:return: dicionário com várias informações sobre a situação da turma.
	"""
#	c = 1
#	s = 0
#	for a in n:
#		if c == 1:
#			maior = menor = a
#		else:
#			if a > maior:
#				maior = a
#			if a < menor:
#				menor = a
#		s += a
#		c +=1
#	media = s / len(n)
#
#	if sit:
#		if media < 5:
#			situ = 'RUIM'
#		elif media >= 5 and media < 7:
#			situ = 'RAZOÁVEL'
#		else:
#			situ = 'BOA'
#		d = {'Quantidade de notas': len(n), 'Menor nota': menor, 'Maior nota': maior,
#		'Média da Turma': media, 'Siuação': situ}
#	else:
#		d = {'Quantidade de notas': len(n), 'Menor nota': menor, 'Maior nota': maior,
#		'Média da Turma': media}
#	return d
	r = dict()
	r['Total'] = len(n)
	r['Maior'] = max(n)
	r['Menor'] = min(n)
	r['Média'] = sum(n)/len(n)
	if sit:
		if r['Média'] >= 7:
			r['Situação'] = 'BOA'
		elif r['Média'] >= 5:
			r['Situação'] = 'RAZOÁVEL'
		else:
			r['Situação'] = 'RUIM'
	return r


resp = notas(4.5, 10, 6.5, sit=True)
print(resp)

import urllib
import urllib.request

try:
	site = urllib.request.urlopen('http://www.pudim.com.br')
except (urllib.request.URLError):
	print('\033[0;31mO site pudim não está acessível!\033[m')
else:
	print('Consegui acessar o site pudim com sucesso!')
	print(site.read())

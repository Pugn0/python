texto = '{"name":"Pugno"}'

texto2 = 'também chamado de foco narrativo, representa'
def getStr(texto, inicio, fim):
	try:
		return texto.split(inicio)[1].split(fim)[0]
	except Exception:
		return "Erro nos argumentos"


filtro = getStr(texto, '', '"')
print(filtro)
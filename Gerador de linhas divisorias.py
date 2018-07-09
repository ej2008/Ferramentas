
'''
Gerado de Linhas
'''


caracter = str(input('caracter'))
espaco = int(input('espaco'))

while True:
	texto = str(input('texto'))
	print(caracter * ((espaco - len(texto))//2),texto,caracter * ((espaco - len(texto))//2))

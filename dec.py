def descifrar(cadCifrada, n, d):
	"""Función para descifrar cadenas de caracteres haciendo uso de una clave privada"""
	cad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listDec = []

	for k, v in enumerate(cad, start=0):			# Creo un diccionario con equivalencias entre el abecedario y su valor numérico
			dic[v] = k

	listCar = [c for c in cadCifrada.upper()]		# Creo un vector a partir de la cadena cifrada

	print('Computando...\n')

	listNum = [dic[c] for c in listCar]				# Creo un vector con los equivalentes numéricos

	dic = dict((v, k) for k, v in dic.items())		# Invierto las claves y valores del diccionario

	for i in listNum:
		listDec.append(dic[(listNum[i]**d) % n])	# Guardo en un vector los números descifrados

	listOut = [dic[c] for c in listCar]				# Creo un vector con los equivalentes alfabéticos
	return listOut									# Retorno la lista

def num2letra():
	cad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(cad, start=0):
			dic[k] = v
	cIn = input('Número: ')
	while cIn != '':
		cIn = int(cIn)
		listOut.append(dic[cIn])
		cIn = input('Número: ')
	print(''.join(listOut))

def letra2num():
	cad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(cad, start=0):
			dic[v] = str(k)
	cIn = input('Letra: ')
	while cIn != '':
		listOut.append(dic[cIn])
		cIn = input('Letra: ')
	print('-'.join(listOut))

# def calculo(n, d):
# 	cIn = input()
# 	lista = []
# 	while cIn != '':
# 		lista.append(int(cIn)**d % d)
# 	print('-'.join(lista))
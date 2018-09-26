def descifrar(encStr, n, d):
	"""	Function to decypher strings using a known private key """
	dic = {}
	listDec = []

	listCar = [c for c in encStr.upper()]			# Create a vector from the encrypted string

	print('Computando...\n')

	listNum = letra2num(listCar)					# Create a vector to store the corresponding numerical values

	for i in listNum:
		listDec.append(dic[(listNum[i]**d) % n])	# Store in a vector the numeric values, now decrypted

	listOut = num2letra(listaDec)					# Create a vector with the alphabetical equivalents
	return listOut									# Return the vector

def num2letra(listNum):
	""" Function to convert a Number input to their equivalent in the alphabet """
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[k] = v

	listOut = [dic[int(n)] in n for listNum]		# Create a vector to store the equivalent letters

	return listOut									# Return the vector

def letra2num(listCar): # CONTINUE HERE
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[v] = k

	cIn = input('Letra: ')

	while cIn != '':
		listOut.append(str(dic[cIn]))
		cIn = input('Letra: ')

	print('-'.join(listOut))

# def calculo(n, d):
# 	cIn = input()
# 	lista = []
# 	while cIn != '':
# 		lista.append(int(cIn)**d % d)
# 	print('-'.join(lista))
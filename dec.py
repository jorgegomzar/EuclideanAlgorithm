
	"""	Function to decypher strings using a known private key """
	dic = {}
	listDec = []

	listCar = [c for c in encStr.upper()]			# Create a vector from the encrypted string

	print('Computando...\n')

	listNum = char2num(listCar)						# Create a vector to store the corresponding numerical values

	for number in listNum:
		listDec.append((number**d)%n)				# Store in a vector the numeric values, now decrypted

	listOut = num2char(listDec)						# Create a vector with the alphabetical equivalents
	return listOut									# Return the vector, this contains the string decrypted

def num2char(listNum):
	""" Function to convert a Number input to String output """
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[k] = v

	listOut = [dic[n] in n for listNum]				# Create a vector to store the equivalent letters

	return listOut									# Return the vector of characters

def char2num(listCar):
	""" Function to convert a String input to Number output """
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[v] = k

	listOut = [dic[c] in c for listCar]				# Create a vector to store the equivalent numbers

	return listOut									# Return the vector of numbers
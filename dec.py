def decrypt(encStr, n, d):
	"""	Function to decypher strings using a known private key """
	dic = {}
	listDec = []

	for number in encStr.split(' '):
		listDec.append((int(number)**d)%n)			# Store in a vector the numeric values, now decrypted

	listOut = num2char(listDec)						# Create a vector with the alphabetical equivalents
	return listOut									# Return the vector, this contains the string decrypted

def num2char(listNum):
	""" Function to convert a Number input to String output """
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[k] = v

	for n in listNum:
		listOut.append(dic[n])						# Create a vector to store the equivalent letters

	return listOut									# Return the vector of characters

def char2num(listCar):
	""" Function to convert a String input to Number output """
	alphStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(alphStr, start=0):		# Create a dictionary with numeric values for each letter of the alphabet
		dic[v] = k

	for c in listCar:
		listOut.append(dic[c])						# Create a vector to store the equivalent numbers

	return listOut									# Return the vector of numbers
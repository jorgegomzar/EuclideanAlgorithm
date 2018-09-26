import os, dec
from sys import platform

def clear():
	""" Multi S.O. function to clear the terminal screen """
	if platform == "linux":
		_ = os.system('clear')
	elif platform == "win32":
		_ = os.system('cls')

print('Complete the requested values')
p = int(input('p: '))
q = int(input('q: '))
n = p * q
phi = (p-1)*(q-1)
e = int(input('e: '))
print('Calculating d...')

posD = [phi, 1]
rem = [phi, e]
quot = []
# ------------------------------- #
#   EXTENDED ECLUDEAN ALGORITHM   #
# ------------------------------- #
i = 0 														# Initial index
while rem[-1] != 1 and rem[-1] != 0:						# While remainder is not 1 or 0 keep going
	rem.append(rem[i]%rem[i+1])								# Append to REM the remainder of the division of the last two remainders
	quot.append(rem[i]//rem[i+1])							# Append to QUOT the quotient of the last division
	posD.append((posD[i]-posD[i+1]*quot[i])%phi)			# Append to POSD the penultimate posD minus the product between the last posD and the last quotient

# For debugging purposes
# print('rem: ',rem)
# print('quot: ',quot)
# print('posD: ',posD)

if rem[-1] != 0:											# If the last remainder is equal to 0 means that some number is not right
	print('d =',posD[-1])
else:
	print('Couldn\'t find d, check all introduced parameters.')
	exit()


os.system('pause')
clear()

if input('Decrypt? (s/n): ').lower() == 's':
	d = posD[-1]
	cad = input('Insert the string to decrypt: ')
	listDescifrada = dec.descifrar(cad, n, d)				# Decrypt the string
	print('Cadena descifrada: '+''.join(listDescifrada))	# Show it via terminal
 
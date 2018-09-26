import os, dec
from sys import platform

def clear():
	"""Función para limpiar la pantalla del terminal
	tanto en linux como en windows"""
	if platform == "linux":
		_ = os.system('clear')
	elif platform == "win32":
		_ = os.system('cls')

print('Introduce los siguientes valores')
p = int(input('p: '))
q = int(input('q: '))
n = p * q
phi = (p-1)*(q-1)
e = int(input('e: '))
print('Calculating d...')

posD = [phi, 1]
restos = [phi, e]
cocientes = []
# ------------------------------- #
# ALGORITMO EXTENDIDO DE EUCLIDES #
# ------------------------------- #
i = 0 														# Indice inicial de RESTOS y POSD
while restos[-1] != 1 and restos[-1] != 0:					# Que repita lo siguiente mientras que el el último resto no sea 1
	restos.append(restos[i]%restos[i+1])					# Se añade a RESTOS, el resto de la división entre los dos últimos elementos del vector RESTOS
	cocientes.append(restos[i]//restos[i+1])				# Se añade a COCIENTES, el cociente de la división entre los dos últimos elementos del vector RESTOS
	posD.append((posD[i]-posD[i+1]*cocientes[i])%phi)		# Se añade a POSD, la resta entre el penúltimo elemento del vector POSD y el producto del último del vector POSD por el último cociente
# DEBUGGING
# print('restos: ',restos)
# print('cocientes: ',cocientes)
# print('posD: ',posD)
if restos[-1] != 0:
	print('d =',posD[-1])
else:
	print('No se ha podido hallar d, comprueba todos los parámetros introducidos.')

os.system('pause')
clear()

if input('¿Descifrar? (s/n): ').lower() == 's':
	d = posD[-1]
	cad = input('Introduce la cadena a desencriptar: ')
	listDescifrada = dec.descifrar(cad, n, d)
	print('Cadena descifrada: '+''.join(listDescifrada))
 
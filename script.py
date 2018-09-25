import os, dec
from sys import platform

def clear():
	if platform == "linux":
		_ = os.system('clear')
	elif platform == "win32":
		_ = os.system('cls')

p = int(input('p: '))
q = int(input('q: '))
n = p * q
phi = (p-1)*(q-1)
e = int(input('e: '))
print('Calculating d...')

posD = [phi, 1]
restos = [phi, e]
cocientes = []

i = 0 # Indice inicial de restos y posD
while restos[-1] != 1:
	restos.append(restos[i]%restos[i+1])
	cocientes.append(restos[i]//restos[i+1])
	posD.append((posD[i]-posD[i+1]*cocientes[i])%phi)
	i = i + 1
print('restos: ',restos)
print('cocientes: ',cocientes)
print('posD: ',posD)
print('d =',posD[-1])

os.system('pause')
clear()
if input('¿Descifrar? (s/n): ').lower() == 's':
	d = posD[-1]
	if input('¿Pasar de número a cadena? (s/n): ').lower() == 's':
		dec.num2letra()
	listDescifrada = dec.descifrar(n, d)
	print('Cadena descifrada: '+''.join(listDescifrada))
 
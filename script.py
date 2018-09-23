phi = int(input('PHI: '))
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
print('d =',posD[-1])
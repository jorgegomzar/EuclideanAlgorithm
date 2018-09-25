def descifrar(n, d):

	cad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dic = {}
	listOut = []

	for k, v in enumerate(cad, start=0):
			dic[v] = k
	cadIn = input('Introduce caracteres: ').upper()
	listC = [c for c in cadIn]

	print('Computando...\n')

	listNum = [dic[c] for c in listC]

	dic = dict((v, k) for k, v in dic.items())

	for i in listNum:
		listOut.append(dic[listNum[i]**d % n])
	return listOut

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
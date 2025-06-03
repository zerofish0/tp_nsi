###[TP 6+7 : Conversions binaires, décimales, hexadécimales]###
## Zerofish0                                                  #
###############################################################
## Importation de modules
try :
	a = 3/0 # lever une erreur car le module ne fonctionne pas sous windows
	from colorama import Fore, Style
except :
	print("[-] ATTENTION : Le module colorama (coloration du texte) n'a pas pu etre importé")
	class Fore :
		WHITE = ""
		RED = ""
		GREEN = ""
		BLUE = ""
	class Style :
		BRIGHT = ""
		NORMAL = ""

## Fonctions
def demo(function,wanted,*args) :
	"""Vérfifier si une fonction fonctionne correctement
	params :
		function : func ; la fonction a tester
		wanted : list ; la valeur attendue
		*args : les arg de la fonction
	return : None
	"""
	global WARNINGS
	print(Fore.WHITE + Style.BRIGHT + f"# Execution de la fonction {function.__name__}")
	print(Fore.WHITE + Style.NORMAL + f"[*] Params : {args}")
	print(Fore.WHITE + Style.NORMAL + f"[*] Resultat voulu : {wanted}")
	result = function(*args)
	print(Fore.WHITE + Style.NORMAL + f"[+] Resultat       : {result}")
	valid = result == wanted
	if valid : print(Fore.GREEN + "[+] La fonction est valide")
	else :
		print(Fore.RED + "[-] La fonction a un problème")
		WARNINGS += 1
	print(Fore.WHITE + Style.NORMAL + "_" * 20)

#1) Conversion de base10 en base2
def decToBin(base10) :
	"""Convertit un nombre entier naturel/relatif en base 10 en base 2
	params :
		base10 : int ; le nombre en base 10
	return :
		response : list ; le nombre converti
	"""
	assert (-2 ** (BITS - 1))<base10<((2 ** (BITS-1))-1), "Nombre trop grand pour etre encodé"
	response = [0] * int(BITS)
	for i in range(len(response)) :
		response[i] = base10 % 2
		base10 //= 2
	response.reverse()
	return response


#1.2) Conversion de base10 en base16
def decToHex(base10) :
	"""Convertit un nombre entier naturel en base 10 en base 16
	params :
		base10 : int ; le nombre en base 10
	return :
		response : list ; le nombre converti
	"""
	assert (-16 ** (BITS - 1))<base10<16 ** BITS , "Nombre trop grand pour etre encodé"
	response = [0] * int(BITS)
	for i in range(len(response)) :
		response[i] = base10 % 16
		base10 //= 16
	response.reverse()
	return response

#2) Conversion d'entier naturel binaire en base 10
def naturalBinToDec(base2) :
	"""Convertit un nombre entier naturel base 2 en base 10
	params :
		base2 : int ; le nombre entier naturel en base2
	return :
		response : list ; le nombre converti
	"""
	power = len(base2)-1
	response = 0
	for i in base2 :
		response += int(i) * 2 ** power
		power -= 1
	return response

#3) Conversion d'entier relatif binaire en base 10
def relativeBinToDec(base2) :
	"""Convertit un nombre entier relatif en base 2 en base 10
	params :
		base2: int ; le nombre entier relatif en base 2
	return :
		response : list ; le nombre converti
	"""
	power = len(base2)-1
	response = -(abs(base2[0]) * 2 ** power)
	power -= 1
	for i in base2[1:] :
		response += i * 2 ** power
		power -= 1
	return response

#3) Addition des nombres entiers naturels binaires
def addBinaryNumbers(bn1,bn2) :
	"""Additioner deux nombres entiers naturels/relatifs binaires
	params :
		bn1 : int ; le premier nombre
		bn2 : int ; le deuxieme nombre
	return :
		response : list ; le resultat
	"""
	assert (-16 ** (BITS - 1))<(relativeBinToDec(bn1) + relativeBinToDec(bn2))<16 ** BITS,"Resultat trop grand"
	cache1 = bn1[:]
	cache2 = bn2[:]
	#print(cache1,cache2)
	carry = int()
	response = list()
	cache1.reverse()
	cache2.reverse()

	for i in range(BITS) :
		#s = a xor b xor carry
		#carry = (a or b) and (a or carry) and (b or carry)
		#print(i)
		a = cache1[i]
		b = cache2[i]
		s = a^b^carry
		carry = (a or b) and (a or carry) and (b or carry)
		response.append(s)
	response.reverse()
	return response

#4) oppose
def oppose(base2) :
	"""Avoir l'opppose d'un nombre binaire
	params :
		base2 : list ; le nombre a convertir
	return :
		response : list ; l'oppose
	"""
	response = list()
	for elem in base2 :
		response.append(int(not elem))
	one = decToBin(1)
	response = addBinaryNumbers(response,one)
	assert (-16 ** (BITS - 1))<relativeBinToDec(response)<16 ** BITS,"Resultat trop grand"
	return response

#5) La soustraction
def subBinaryNumbers(b1,b2) :
	"""Retrancher deux nombres entiers naturels/relatifs binaires
	params :
		b1 : int ; le premier nombre
		b2 : int ; le deuxieme nombre
	return : list ; le resultat
	"""
	assert (-16 ** (BITS - 1))<(relativeBinToDec(b1) - relativeBinToDec(b2))<16 ** BITS,"Resultat trop grand"
	return addBinaryNumbers(b1,oppose(b2))
#6) La multiplication
def multiplyBinaryNumbers(bin1, bin2):
	"""Multiplier deux nombres entiers naturels/relatifs binaires
	params :
		bin1 : int ; le premier nombre
		bin2 : int ; le deuxieme nombre
	return :
		final : list ; le produit de bin1 et bin2
	"""
	assert (-16 ** (BITS - 1))<(relativeBinToDec(bin1) * relativeBinToDec(bin2))<16 ** BITS,"Resultat trop grand"
	d1 = bin1[:]
	d2 = bin2[:]
	signe = d1[0] ^ d2[0]
	if signe :
		if d1[0] :
			d1 = oppose(d1)
		else :
			d2= oppose(d2)
	d1.reverse()
	d2.reverse()

	temp_sum = list()
	for i,elem in enumerate(d1) :
		temp = list()
		for elem2 in d2 :
			temp.append(int(elem and elem2))
		temp.reverse()
		temp.extend([0,] * i)
		temp_sum.append(temp)

	final = decToBin(0)
	for elem in temp_sum :
		final = addBinaryNumbers(elem,final)
	if signe :
		final = oppose(final)
	return final

#7) La division euclidienne
def divideRelativeBinaryNumbers(bin1,bin2) :
	d1 = bin1[:] # dividende
	d2 = bin2[:] # diviseur

	neg = False
	supertest = False
	if d2[0] and not d1[0] :
		d2 = oppose(d2)
		neg = True
	elif d1[0] and not d2[0] :
		d1 = oppose(d1)
		neg = True
		supertest = True
	elif d1[0] and d2[0] :
		d1 = oppose(d1)
		d2 = oppose(d2)
		supertest = True

	# Calcul du quotient et du reste
	continue_ = True
	rest = d1[:]
	quo = decToBin(0)
	while continue_ :
		cache = subBinaryNumbers(rest,d2)
		if cache[0] :
			continue_ = False
		else :
			rest = cache
			quo = addBinaryNumbers(quo,decToBin(1))

	if supertest and (rest != decToBin(0)) :
		quo = addBinaryNumbers(quo,decToBin(1))
		prod = multiplyBinaryNumbers(d2,quo)
		rest = subBinaryNumbers(prod,d1)
	if neg :
		quo = oppose(quo)


	return (quo,rest)

## Programme principal

##Declaration des constantes
OCTETS = 1
BITS = 8 * OCTETS
WARNINGS = 0
VERBOSE = 1
VERBOSE_1 = [42 , [*[0,] * (BITS-8),0, 0, 1, 0, 1, 0, 1, 0]]
VERBOSE_2 = [76 , [*[0,] * (BITS-8),0, 1, 0, 0, 1, 1, 0, 0]]
VERBOSE_3 = [-76 , [*[1,] * (BITS-8),1, 0, 1, 1, 0, 1, 0, 0]]
VERBOSE_4 = [-42 , [*[1,] * (BITS-8),1, 1, 0, 1, 0, 1, 1, 0]]
VERBOSE_5 = [3 , [*[0,] * (BITS-8),0,0,0,0,0,0,1,1]]
VERBOSE_6 = [-3 , [*[1,] * (BITS-8),1,1,1,1,1,1,0,1]]
VERBOSE_1plus2 = [118 , [*[0,] * (BITS-8),0,1,1,1,0,1,1,0]]
VERBOSE_2plus4 = [34 , [*[0,] * (BITS-8),0,0,1,0,0,0,1,0]]
VERBOSE_1time5 = [126 , [*[0,] * (BITS-8),0,1,1,1,1,1,1,0]]
VERBOSE_1time6 = [-126 , [*[1,] * (BITS-8),1, 0, 0, 0, 0, 0, 1, 0]]

if VERBOSE :
	print(Fore.RED + Style.BRIGHT + "### NSI : TP 6 + 7 ###")
	print(Fore.RED + Style.BRIGHT + "[*] ATTENTION, toutes les opérations seront effectuées sur des nombres relatifs")

	# Conversion de décimal en binaire
	demo(decToBin,VERBOSE_1[1],VERBOSE_1[0])
	demo(decToBin,VERBOSE_4[1],VERBOSE_4[0])
	print()

	# Conversion de decimal en hexadecimal
	demo(decToHex,[0, 0, 0, 0, 0, 0, 4, 14],78)

	# Conversion de binaire naturel en decimal
	demo(naturalBinToDec,VERBOSE_1[0],VERBOSE_1[1])
	print()

	# Conversion de binaire relatif en décimal
	demo(relativeBinToDec,VERBOSE_4[0],VERBOSE_4[1])
	print()

	# Addition des nombres biniaires
	demo(addBinaryNumbers,VERBOSE_1plus2[1],VERBOSE_1[1],VERBOSE_2[1])
	demo(addBinaryNumbers,VERBOSE_2plus4[1],VERBOSE_2[1],VERBOSE_4[1])
	print()

	# Opposé d'un nombre binaire
	demo(oppose,VERBOSE_4[1],VERBOSE_1[1])
	demo(oppose,VERBOSE_2[1],VERBOSE_3[1])
	print()

	# Soustraction de nombres biniares
	demo(subBinaryNumbers,VERBOSE_2[1],VERBOSE_1plus2[1],VERBOSE_1[1])
	demo(subBinaryNumbers,VERBOSE_4[1],VERBOSE_2plus4[1],VERBOSE_2[1])
	print()

	#Mutiplication de nombres binaires
	demo(multiplyBinaryNumbers,VERBOSE_1time5[1],VERBOSE_1[1],VERBOSE_5[1])
	demo(multiplyBinaryNumbers,VERBOSE_1time6[1],VERBOSE_1[1],VERBOSE_6[1])
	demo(multiplyBinaryNumbers,VERBOSE_1time5[1],VERBOSE_4[1],VERBOSE_6[1])

	#division euclidienne binaire
		#Les divisions de reste nul
			# dividende et diviseur positif
	demo(divideRelativeBinaryNumbers,(VERBOSE_1[1],decToBin(0)),VERBOSE_1time5[1],VERBOSE_5[1])
			# dividende positif et diviseur negatif
	demo(divideRelativeBinaryNumbers,(decToBin(-2),decToBin(0)),decToBin(6),decToBin(-3))
			# dividende negatif et diviseur positif
	demo(divideRelativeBinaryNumbers, (decToBin(-2),decToBin(0)),decToBin(-6),decToBin(3))
			# dividende et diviseur negatif
	demo(divideRelativeBinaryNumbers, (decToBin(2),decToBin(0)), decToBin(-6), decToBin(-3))

		# Les divisions de reste non nul
			# dividende et diviseur positif
	demo(divideRelativeBinaryNumbers,(decToBin(6),decToBin(1)),decToBin(19),decToBin(3))
			# dividende positif et diviseur negatif
	demo(divideRelativeBinaryNumbers,(decToBin(-6),decToBin(1)),decToBin(19),decToBin(-3))
			#dividende negatif et diviseur positif
	demo(divideRelativeBinaryNumbers,(decToBin(-7),decToBin(2)),decToBin(-19),decToBin(3))
			# dividende et diviseur negatif
	demo(divideRelativeBinaryNumbers,(decToBin(7),decToBin(2)),decToBin(-19),decToBin(-3))

	print(Fore.BLUE + Style.BRIGHT + f"[*] Nombre d'erreur : {WARNINGS}")
print(Fore.RED + Style.BRIGHT + "Programme termine. Bonne journee")
"""
- Conversion de décimal relatifs en binaire : OK
- Conversion de binaire naturels en décimal : OK
- Conversion de binaire relatif en décimal : OK
- Addition des nombres binaires : OK
- Implémenter l'opposé d'un nombre binaire relatif : OK
- Soustraction des nombres binaires : OK
- Multiplication des nombres binaires : OK
- Conversion de décimal en hexadécimal : OK
- Division des nombres binaires : OK
- Gestion du depassement de capacite : OK
"""


















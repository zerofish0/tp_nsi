###[TP 8 : Assertions]###
## Zerofish0            #
#########################
### ATTENTION : Il s'agit d'un reprise du TP précédant, avec des assertions et
### des tests
## Conversion dec -> hex
#Fonction
def convDecHex(X):
	try :
		if not (0 <= X <65536) :
			raise OverflowError("Depassement de capacite dans convDecHex")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par 11")
		X = 11

	finally :
		symbole = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
		resultat = [0]*4
		for i in range(4):
		    resultat [3-i] = symbole[X%16]
		    X = X //16
		return resultat

#Test
assert convDecHex(42) == ['0', '0', '2', 'A'] , \
"Erreur dans la fonction convDecHex."

## Conversion hex -> dec
#Fonction
def convHexDec(L):
	try :
		if len(L)>4 :
			raise ValueError("Valeur incorrecte dans conHexDec")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par ['0', '0', '0', 'B']")
		L = ['0', '0', '0', 'B']

	finally :
		symbole = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
		resultat = 0
		for i in range(4):
		    resultat = resultat * 16 + symbole.index(L[i])
		return resultat

#Test
assert convHexDec(['0', '0', '2', 'A']) == 42 , \
"Erreur dans la fonction ConvHexDec."

## Conversion dec -> bin
#Fonction
def convDecBin(X):
	try :
		if not (-32768 <= X < 32768) :
			raise OverflowError("Depassement de capacite dans convDecBin")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par 11")
		X = 11

	finally :
		resultat = [0]*16
		for i in range(16):
		    resultat[15-i] = X%2
		    X=X//2
		return resultat

#Test
assert convDecBin(42) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0] , \
"Erreur dans la fonction convDecBin"

## Conversion bin -> dec
#Fonction
def convBinDec(L):
	try :
		if not (len(L)==16) :
			raise ValueError("Valeur incorrecte dans convBinDec")

	except Eception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 1, 0, 1, 1]")

	finally :
		resultat = - L[0]*2**15
		for i in range(1,16):
		    resultat += L[i]*2**(15-i)
		return resultat

#Test
assert 42 == convBinDec([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]) , \
"Erreur dans la fonction convBinDec"

## Addition
#Fonction
def addition(L1,L2,mul = False):
	try :
		if not (len(L1) == 16 and len(L2) == 16) :
			raise ValueError("Valeurs incorrectes dans addition")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement des valeurs par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 1, 0, 1, 1]")
		L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
		L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]


	resultat = [0]*16
	retenu = 0
	for i in range(15,-1,-1):
		resultat[i] = L1[i]^L2[i]^retenu
		retenu =  (L1[i] and L2[i]) or (L1[i] and retenu) or (retenu and L2[i])

	try :
		if (L1[0] == L2[0]):
			if L1[0] != resultat[0] and not mul:
				raise OverflowError("Depassement de capacite dans addition")
			else : pass
		else : pass

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 1, 0, 1, 1]")
		resultat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

	finally :
		return resultat


#Test
assert addition([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],\
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],False) == \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1] , \
"Erreur dans la fonction addition"

## Oppose
# Fonction
def oppose(L):
	try :
		if not (len(L) == 16) :
			raise ValueError("Valeur incorrecte dans oppose")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 1, 0, 1, 1]")
		L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

	finally :
		resultat = [0]*16
		for i in range(16):
		    resultat[i] = 1-L[i]
		return addition(resultat,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],False)

#Test
assert oppose([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]) == \
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0] , \
"Erreur dans la fonction oppose"

## Soustraction
#Fonction
def soustraction(L1,L2):
    return addition(L1,oppose(L2),False)

#Test
assert soustraction([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],\
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) == \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1] , \
"Erreur dans la fonction soustraction"

## Decalage
#Fonction
def decalage(L,n):
	try :
		if 1 in L[:n] :
			raise OverflowError("Depassement de capacite dans multiplication (decalage)")
		if len(L) != 16 :
			raise ValueError("valeur incorrecte dans decalage")
	except :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 1, 0, 1, 1]")
		L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

	finally :
		return L[n:]+[0]*n

#Test
assert decalage([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],3) == \
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0] , \
"Erreur dans la fonction dcalage"

##Multiplication
#Fonction
def multiplication(L1,L2):
	try :
		if not (len(L1) == 16 and len(L2) == 16) :
			raise ValueError("Valeurs d'entrées incorrectes dans multiplication")
	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement des valeurs par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
	0, 0, 0, 1, 0, 1, 1]")
		L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
		L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

	resultat = [0]*16
	for i in range(16):
		if L2[i]:
			resultat = addition(resultat,decalage(L1,15-i),True)

	try :
		if L1[0] == L2[0]:
			if resultat[0] != 0 :
				raise OverflowError("Depassement de capacite dans multiplication")

		elif resultat[0] != 1 :
			raise OverflowError("Depassement de capacite dans multiplication")

	except Exception as e :
		print(f"[-] Erreur : {e}")
		print("[*] Remplacement de la valeur par [0, 0, 0, 0, 0, 0, 0, 0, 0, \
	0, 0, 0, 1, 0, 1, 1]")
		resultat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
	finally :
		return resultat

#Test
assert multiplication([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],\
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])== \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0] , \
"Erreur dans la fonction multiplication"


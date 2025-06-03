###[TP 12 : Les nombres réels et les caractères]###
##Zerofish0                                       #
## VERSION : avec les classes                     #
###################################################

##Implémentation de fonctions
class IEEE754(object) :
    def __init__(self) :
        self._b10_value = int(42)
        self._ieee754_value = [[0], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def _getSignBit(self,n) :
        """Retourne le bit du signe du nombre décimal n
        params :
            n : int : le nbr décimal
        return :
            bit_signe : list : le bit du signe
        """
        bit_signe = list()
        # le 0 sera considéré positif (+0)
        if n >= 0 : bit_signe.append(0)
        elif n < 0 : bit_signe.append(1)
        return bit_signe

    def _getPositiveBin(self,n) :
        """Renvoie la représentation binaire d'un nombre n sur 1 octet
        params :
            n : int : le nombre à convertir
        return :
            data : list : la valeur binaire de n
        """
        data = [0] * 8
        for i in range(8) :
            data[7-i] = n%2
            n = n//2
        return data

    def _getPositiveDec(self,b) :
        """Renvoie la représentation décimale du binaire b
        params :
            b : list : le nombre binaire
        return :
            n : int : le nombre décimal converti
        """
        n = 0
        for i in range(8) :
            n += b[i]*2**(7-i)
        return n

    def loadInt(self,n) :
        """convertir un réel n en nombre binaire encodé d'après la norme IEEE 754
        params :
            n : int : le nombre a convertir
        return :
            ieee754 : list : le nombre converti
        """
        self._b10_value = n
        #1) récupérer le bit du signe
        _bit_signe = self._getSignBit(n)
        if n < 0 : n*=(-1)

        #2) calcul de l'exposant
        exp_reel = -126
        while not 2**exp_reel <= n < 2**(exp_reel+1) :
            exp_reel += 1
        exp_biaise = exp_reel + 127
        _exp_octet = self._getPositiveBin(exp_biaise)

        #3) calcul de la mantisse
        m = n/(2**exp_reel)
        mantisse = m-1
        data = [0]*23
        for i in range(23) :
            result = int()
            exp_local = -(i+1)
            if round(mantisse,5) == 0 : result = 0
            if mantisse - (2**exp_local) >= 0 :
                mantisse -= (2**exp_local)
                result = 1
            else : result = 0
            data[i] = result
        _23bits_mantisse = data

        ieee754 = [_bit_signe,_exp_octet,_23bits_mantisse]
        self._ieee754_value = ieee754

    def loadIEEE754(self,ieee754) :
        """convertir un nombre encodé avec la norme IEEE 754 en réel décimal
        params :
            bin : list : le nombre avec la norme IEEE 754
        return :
            dec : int : le nombre réel convertit
        """
        self._ieee754_value = ieee754
        _bit_signe = ieee754[0]
        _exp_octet = ieee754[1]
        _23bits_mantisse = ieee754[2]

        #1) Conversion du bit du signe :
        signe = int()
        if _bit_signe == [0] : signe = 1
        elif _bit_signe == [1] : signe = -1

        #2) Conversion de l'exposant
        exp_biaise = self._getPositiveDec(_exp_octet)
        exp_reel = exp_biaise-127

        #3) Conversion de la mantisse
        mantisse = 0
        for i in range(23) :
            exp_local = - (i+1)
            mantisse += _23bits_mantisse[i]*2**exp_local

        #4) recomposition finale (v = s * 2**e * m)
        m = 1 + mantisse
        dec = signe * 2**exp_reel * m
        self._b10_value = round(dec,5)

    def __repr__(self) :
        """Afficher proprement un nombre en IEEE754
        params :
            ieee754 : le nombre à afficher
        return :
            None
        """
        ieee754 = self._ieee754_value
        s = str(ieee754[0][0])
        e = ieee754[1]
        m = ieee754[2]

        e_str = str()
        for char in e :
            e_str += str(char)

        m_str = str()
        for char in m :
            m_str += str(char)
        return s + " " + e_str + " " + m_str

    @property
    def getIntegerValue(self) :
        return self._b10_value

    @property
    def getRawIEEE754(self) :
        return self._ieee754_value

    @property
    def getFormatedIEEE754(self) :
        return self.__repr__()


##Programme principal (démonstration)
obj = IEEE754() # on crée notre nombre
obj.loadInt(36) # on y place cette valeur
#méthodes utilisables :
print(obj.getFormatedIEEE754) # récupérer le ieee754 sous forme de texte formaté
print(obj.getIntegerValue) # récupérer la valeur décimale
print(obj.getRawIEEE754) # récupérer la liste ieee754
print(obj) # afficher le nombre formaté (comme avec getFormatedIEEE754)

print("___"*20)
x = IEEE754()
obj.loadInt(12.625)
print(obj)




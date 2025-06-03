###[TP 12 : Les nombres réels et les caractères]###
## Zerofish0                                      #
## VERSION : avec interface graphique tkinter     #
###################################################

##Importation de module :
import tkinter as tk

##Implémentation de fonctions
def getSignBit(n) :
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

assert getSignBit(42)==[0],"getSignBit a un problème avec les nombres positifs"
assert getSignBit(-42)==[1],"getSignBit a un problème avec les nombres negatifs"

def getPositiveBin(n) :
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
assert getPositiveBin(5)==[0, 0, 0, 0, 0, 1, 0, 1],"Erreur dans la conversion bin"
assert getPositiveBin(128)==[1, 0, 0, 0, 0, 0, 0, 0],"Erreur dans la conversion bin"

def getPositiveDec(b) :
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
assert getPositiveDec(getPositiveBin(42)) == 42,"problème dans le conversion dec"
assert getPositiveDec(getPositiveBin(87)) == 87,"problème dans le conversion dec"


def dec2IEEE754(n) :
    """convertir un réel n en nombre binaire encodé d'après la norme IEEE 754
    params :
        n : int : le nombre a convertir
    return :
        ieee754 : list : le nombre converti
    """
    #1) récupérer le bit du signe
    _bit_signe = getSignBit(n)
    if n < 0 : n*=(-1)

    #2) calcul de l'exposant
    exp_reel = -126
    while not 2**exp_reel <= n < 2**(exp_reel+1) :
        exp_reel += 1
    exp_biaise = exp_reel + 127
    _exp_octet = getPositiveBin(exp_biaise)

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
    return ieee754

def IEEE7542dec(ieee754) :
    """convertir un nombre encodé avec la norme IEEE 754 en réel décimal
    params :
        bin : list : le nombre avec la norme IEEE 754
    return :
        dec : int : le nombre réel convertit
    """
    _bit_signe = ieee754[0]
    _exp_octet = ieee754[1]
    _23bits_mantisse = ieee754[2]

    #1) Conversion du bit du signe :
    signe = int()
    if _bit_signe == [0] : signe = 1
    elif _bit_signe == [1] : signe = -1

    #2) Conversion de l'exposant
    exp_biaise = getPositiveDec(_exp_octet)
    exp_reel = exp_biaise-127

    #3) Conversion de la mantisse
    mantisse = 0
    for i in range(23) :
        exp_local = - (i+1)
        mantisse += _23bits_mantisse[i]*2**exp_local

    #4) recomposition finale (v = s * 2**e * m
    m = 1 + mantisse
    dec = signe * 2**exp_reel * m
    return round(dec,5)

assert IEEE7542dec(dec2IEEE754(128)) == 128,"problème dans l'implémentation de ieee754"
assert IEEE7542dec(dec2IEEE754(-32.75)) == -32.75,"problème dans l'implémentation de ieee754"
assert IEEE7542dec(dec2IEEE754(1.6)) == 1.6,"problème dans l'implémentation de ieee754"

def formatedIEEE754(ieee754) :
    """Afficher proprement un nombre en IEEE754
    params :
        ieee754 : le nombre à afficher
    return : str : le str formatee
    """
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

# Fonctions pour tkinter
def func_ieee754(n) :
    cache = dec2IEEE754(float(n))
    return formatedIEEE754(cache)
def func_dec(str_) :
    str_ = str_.replace(" ","")
    print(str_)
    s = [int(str_[0])]

    e_str = str_[1:9]
    e = list()
    for n in e_str :
        e.append(int(n))

    m_str = str_[9:33]
    m = list()
    for n in m_str :
        m.append(int(n))


    ieee754 = [s,e,m]
    print(ieee754)
    return IEEE7542dec(ieee754)


def afficher_ieee754():
    # Récupérer le texte de la zone de texte
    contenu = zone_texte.get("1.0", tk.END).strip()
    # Appliquer la fonction func1
    resultat = func_ieee754(contenu)
    # Afficher le résultat deux fois
    #label_resultat.config(text=f"{resultat}")
    gen.set(str(resultat))

def afficher_dec():
    # Récupérer le texte de la zone de texte
    contenu = zone_texte.get("1.0", tk.END).strip()
    # Appliquer la fonction func1
    resultat = func_dec(contenu)
    # Afficher le résultat deux fois
    #label_resultat.config(text=f"{resultat}")
    gen.set(str(resultat))

def copytoclipboard():
    fenetre.clipboard_clear()
    fenetre.clipboard_append(gen.get())

## Programme principal
# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur IEEE 754")
fenetre.config(bg = "black")
gen = tk.StringVar()

# Création de la zone de texte
zone_texte = tk.Text(fenetre, bg = "black",fg = "green", height=10, width=40)
zone_texte.pack(pady=10)

# Création du bouton
bouton1 = tk.Button(fenetre,bg = "purple", text="Convertir en IEEE754", command=afficher_ieee754)
bouton1.pack(pady=5)

bouton2 = tk.Button(fenetre,bg = "purple", text="Convertir en décimal", command=afficher_dec)
bouton2.pack(pady=5)

bouton3 = tk.Button(fenetre,bg = "red", text="Copie dans le presse papier", command=copytoclipboard)
bouton3.pack(pady=5,padx = 3)
# Création du label pour afficher le résultat
label_resultat = tk.Label(fenetre,bg = "black",fg = "green", textvariable=gen)
label_resultat.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()









































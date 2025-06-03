###[TP 15 : Dictionnaires]###
## Zerofish0                #
#############################

## ATTENTION : nécessite le fichier : tp15-tour_du_monde.txt

EXERCICE_II_PRINT = False
EXERCICE_III_PRINT = True
### II. Jumeau or not Jumeau
# Importations
import random as rnd

# Définitions
def genClassroomBirthdays() :
    return [rnd.randint(1,365) for _ in range(25)]

def classroomBirthdaysListToDict(classroom_birthdays_list) :
    classroom_birthdays_dict = dict()
    for birthday in classroom_birthdays_list :
        if birthday in classroom_birthdays_dict.keys() :
            classroom_birthdays_dict[birthday] += 1
        else :
            classroom_birthdays_dict[birthday] = 1
    return classroom_birthdays_dict

def isThereTwins(classroom_birthdays_dict) :
    return not len(classroom_birthdays_dict) == 25

def calculateProbabilitiesTwinParadox(iterations = 1000) :
    totalClassrooms = int()
    classroomWithTwins = int()
    for _ in range(iterations) :
        rawList = genClassroomBirthdays()
        rawDict = classroomBirthdaysListToDict(rawList)
        totalClassrooms += 1
        if isThereTwins(rawDict) :
            classroomWithTwins += 1
    return {"totalClassrooms" : totalClassrooms,"classroomWithTwins" : \
    classroomWithTwins,"probability" : classroomWithTwins/totalClassrooms}

# Programme principal
if EXERCICE_II_PRINT :
    iterations = 1000000
    print("Calcul en cours...")
    data = calculateProbabilitiesTwinParadox(iterations)

    print(f"###[Résulats du paradoxe des jumeaux]###")
    print(f"- Itérations : {iterations}")
    print(f"- Nombre de séries total générées : {data['totalClassrooms']}")
    print(f"- Nombre de séries possédant des jumeaux : {data['classroomWithTwins']}")
    print(f"- Probabilité : {data['probability']}, soit : {data['probability'] * 100} % ")
    # 56.865 % sur 1M d'itérations


### III. Etude de texte
# Constantes
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
# Définitions
def countWords(text) :
    l = text.split()
    return len(l)

def howManyWordsStartsWith(letter,text) :
    _list = text.split()
    counter = int()
    for word in _list :
        if word[0] == letter.lower() :
            counter += 1
    return counter



#Normalisation du texte
def normalizeRawText(data : str) -> str :
    """Normalise le texte donné afin de le rendre utilisable
    params :
    - data : le texte à normaliser
    return :
    - data : le texte normalisé
    """
    data = data.lower()
    delCharacters = "«»[]0123456789&~#{(|°`_^@)=}=$£¤%µ*!.,;:/§<>*+?"
    for char in delCharacters :
        data = data.replace(char,"")
    data = data.replace("--","")
    data = data.replace("- ","")
    data = data.replace("\n","")
    data = data.replace("\t","")
    for i in range(100) :
        data = data.replace("  "," ")
    data = data.replace("é","e")
    data = data.replace("è","e")
    data = data.replace("ê","e")
    data = data.replace("à","a")
    data = data.replace("ù","u")
    data = data.replace("ë","e")
    data = data.replace("ô","o")
    data = data.replace("â","a")
    data = data.replace("û","u")
    data = data.replace("î","i")
    data = data.replace("ï","i")
    data = data.replace("ç","c")
    data = data.replace("'"," ")
    data = data.replace("ü","u")
    return data

def getIndex(text : str) -> dict :
    """Construis un dictionnaire indexant tous les mots d'un texte normalisé
    params :
    - texte : le texte normalisé
    return :
    - text_dict : l'index des mots de forme : {mot : nombre_occurences,...}
    """
    text_list = text.split()
    text_dict = dict()
    for word in text_list :
        if word in text_dict.keys() :
            text_dict[word] += 1
        else :
            text_dict[word] = 1
    return text_dict

def HowManyWords(index_ : dict,startswith = "",endswith = "",contains = "") -> tuple :
    """Cherche des mots correspondants aux filtres fournis
    params :
    - startswith/endswith/contains : filtres applicables
    return :
    - tuple : de forme (nombre_occurences_total,liste_des_valeurs)
    """
    counter = int()
    occurences = list()
    for word in index_.keys() :
        if (startswith == word[:len(startswith)]) and (endswith == word[(len(word)-len(endswith)):]) and (contains in word) :
            counter += index_[word]
            occurences.append(word)
    return (counter,occurences)

def levensteinDistance(word1 : str,word2 : str) -> int :
    """Calcul la distance de Levenstein entre deux mots
    params :
    - word1/word2 : les deux mots à comparer
    return :
    - int : la distance
    """
    m,n = len(word1),len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1) :
        dp[i][0] = i
    for j in range(n+1) :
        dp[0][j] = j
    for i in range(1,m+1) :
        for j in range(1,n+1) :
            cout_subst = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(
            dp[i-1][j]+1,
            dp[i][j-1]+1,
            dp[i-1][j-1] + cout_subst)
    return dp[m][n]

def getMaxLevensteinDistance(word : str) -> int :
    """Renvoie la distance de Levenstein maximale appropriée pour la recherche
    params :
    - word : le mot que l'on va rechercher
    return :
    - int : la diastance appropriée
    """
    if len(word) <= 4 : return 0
    elif len(word) <= 6 : return 1
    elif len(word) <= 9 : return 2
    else : return 3

def searchWord(index_ : dict,word0 : str,force_levenstein_max_distance = -1,force_exact_results = False) -> tuple:
    """Cherche le nombre d'occurences d'un mot et des mots qui s'en approchent
    params :
    - index_ : le dictionnaire ou faire la recherche
    - word0 : le mot recherché
    - force_levenstein_max_distance : la distance de levenstein forcé (laisser
        a -1 pour auto.
    - force_exact_results : for la distance de levenstein a 0,
        prévaut sur force_levenstein_max_distance
    return :
    - tuple : de forme (nombre_occurences_total,liste_des_valeurs_considérées)
    """
    counter = int()
    occurences = list()
    if force_levenstein_max_distance == -1 : lev_max_d = getMaxLevensteinDistance(word0)
    else : lev_max_d = force_levenstein_max_distance
    if force_exact_results : lev_max_d = 0
    for word1 in index_.keys() :
        if levensteinDistance(word0,word1) <= lev_max_d :
            counter += index_[word1]
            occurences.append(word1)
    return (counter,occurences)

def searchWord3(index_,word0) :
    """Combine distance de levenstein et correspondance du radical"""
    counter = int()
    occurences = list()
    c1,c2 = HowManyWords(index_,contains = word0[:-1])
    if not len(c2)>100 :
        occurences.extend(c2)

    c11,c12 = searchWord(index_,word0)
    l = set(c2 + c12)
    dict_ = dict()
    for word1 in l :
        counter += index_[word1]
        dict_[word1] = index_[word1]

    return (counter,dict_)


# Programme principal
#Ouvrir le fichier peut ne pas fonctionner, auquel cas changer le chemin
#Le fichier doit être dans le même dossier
file = open('tp15-tour_du_monde.txt','r') # essayer le chemin absolu avec des \\
data = file.read()
file.close()

if EXERCICE_III_PRINT :
    texte = normalizeRawText(data)
    index_ = getIndex(texte)

    # Nombre de mots différents
    print(f"[*] Il y a {len(index_)} mots différents dans le texte")

    #Mot de plus de lettres le plus frequent
    n = max(index_.keys(),key = lambda x : 0 if len(x) <= 4 else index_[x])
    print(f"[*] Le mot qui apparait le plus de fois de +4 lettres est {n}")

    # Mots commençant par "b"
    b = HowManyWords(index_,startswith = "b")
    print(f"[*] {b[0]} mots commencent par la lettre b ({len(b[1])} mots différents)")

    #Demonstration de l'algorithme de recherche
    mot = str(input("Entrez un mot à rechercher : "))
    result = searchWord3(index_,mot)
    print(result)
    print(f"{result[0]} correspondances trouvées")
    for resultat in result[1].keys() :
        print(f"- {resultat} : {result[1][resultat]} correspondances")
























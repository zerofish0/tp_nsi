###[TP 10 : Algorithme glouton]###
## Zerofish0                     #
##################################

##II) Rendu de monnaie

#Exemple 1
def rendu_monnaie(somme,pieces) :
    resultat = list()
    while somme > 0 :
        cache = list()
        for e in pieces :
            if somme - e >= 0 :
                cache.append(e)
        try : p = max(cache)
        except : return "monnaie manquante"
        pieces.remove(p)
        resultat.append(p)
        somme -= p
    resultat2 = list()
    for e in set(resultat) :
        resultat2.append([e,resultat.count(e)])
    return resultat2

#Exemple 2
print("###II) Exemple 2")
monnaie = [50,50,20,20,10,10,5,5,2,2,1,1]
print(rendu_monnaie(99,monnaie))
print(rendu_monnaie(19,monnaie))

##III)Sac a dos

def remplir_valise(liste_objets,m_max) :
    resultat = list()
    m = 0
    while m < m_max :
        cache = list()
        for obj in liste_objets :
            if m + obj[1] <= m_max :
                cache.append(obj)
        try : objet_choisi = max(cache,key = lambda x : x[0])
        except : break
        resultat.append(objet_choisi[2])
        m += objet_choisi[1]
        liste_objets.remove(objet_choisi)
    return resultat

#Exemple 1
print("###III) Exemple 1")
print(remplir_valise([[2,1,'gouter'],[5,0.5,"jumelles"],[1,0.2,"livre"],\
[3,4,"peluche"]],5))

#Exemple 2
print("###III) Exemple 2")
print(remplir_valise([[6,5,"chaussures"],[5,5,"habits"],[4.5,2,"trousse de  \
toilettes"],[4,2,"creme"],[3,8,"livres"],[1,2,"palmes tuba"],[0.5,3,"parasol"]]\
,23))




###[TP 13 : Tris de listes]###
##Zerofish0                  #
##############################

##Importations :
import random
import time
import matplotlib.pyplot as plt
import tkinter as tk

##Implémentation des fonctions##
def tri_bulle(list_) :
    """Méthode implémentant le tri bulle
    params :
        list_ : list : la liste a trier
    return :
        list_ : list : la liste triee
    """
    for j in range(0,len(list_)-1) :
        for i in range(1,len(list_)-j) :
            if list_[i-1] > list_[i] :
                list_[i-1],list_[i] = list_[i],list_[i-1]
    return list_

assert tri_bulle([1,3,5,2]) == [1,2,3,5],"Erreur sur le tri bulle"

def tri_selection(list_) :
    """Méthode implémentant le tri selection
    params :
        list_ : list : la liste a trier
    return :
        list_ : list : la liste triee
    """
    for j in range(len(list_)-1) :
        i_min = j
        for i in range(j+1,len(list_)) :
            if list_[i]<list_[i_min] :
                i_min = i
        list_[j],list_[i_min] = list_[i_min],list_[j]
    return list_

assert tri_selection([1,3,5,2]) == [1,2,3,5],"Erreur sur le tri selection"

def tri_insertion(list_) :
    """Méthode implémentant le tri par insertion
    params :
        list_ : la liste à trier
    return :
        list_ : la liste triee
    """
    for j in range(1,len(list_)) :
        for i in range(j) :
            if list_[i]>list_[j] :
                list_.insert(i,list_.pop(j))
    return list_

assert tri_insertion([1,5,2,3]) == [1,2,3,5],"Erreur sur le tri insertion"

def tri_fusion(list_) :
    """Méthode implémentant le tri fusion
    params :
        list_ : le liste à trier
    return :
        list_ : la liste triée
    """
    if len(list_) <= 1 : return list_
    pivot = len(list_)//2
    l1 = list_[:pivot]
    l2 = list_[pivot:]
    gauche = tri_fusion(l1)
    droite = tri_fusion(l2)
    fusionne = _fusion(gauche,droite)
    return fusionne

def _fusion(l1,l2) :
    i1 = 0
    i2 = 0
    t1 = len(l1)
    t2 = len(l2)
    l_fusion = list()
    while i1<t1 and i2<t2 :
        if l1[i1]<l2[i2] :
            l_fusion.append(l1[i1])
            i1+=1
        else :
            l_fusion.append(l2[i2])
            i2+=1
    while i1<t1 :
        l_fusion.append(l1[i1])
        i1+=1
    while i2<t2 :
        l_fusion.append(l2[i2])
        i2+=1
    return l_fusion

assert tri_fusion([1,5,2,3]) == [1,2,3,5],"Erreur sur le tri fusion"

def genRandomList(length,range_) :
    return [random.randint(1,range_) for _ in range(length)]

def chronos(func,L) :
    worklist = L[::]
    start_time = time.time()
    func(worklist)
    end_time = time.time()
    return end_time - start_time

def avgchrono_sort(sort_,rl_len=1000,rl_range=100,iter=100) :
    sort_sumt = int()
    for _ in range(iter) :
        l = genRandomList(rl_len,rl_range)
        sort_sumt+=chronos(sort_,l)
    return sort_sumt/iter

def gen_graph(methods,maxrange=1000,step=100,avgiter = 100,avgrange = 100) :
    lenghts = [x for x in range(0,maxrange,step)]
    data = dict()

    print("Récupération des données...")
    for func in methods :
        data[func.__name__] = [avgchrono_sort(func,l,avgrange,avgiter) for l in lenghts]
    print("Récupération des données terminé")

    x = lenghts
    for f in methods :
        plt.plot(x,data[f.__name__],label = f.__name__)

    plt.title('Evolution du temps en fonction de la longueur')
    plt.xlabel("temps")
    plt.ylabel("taille de la liste")
    plt.legend()
    plt.show()

gen_graph([tri_selection,tri_insertion,tri_fusion,sorted],maxrange=10000,step = 1000,avgiter = 50)

























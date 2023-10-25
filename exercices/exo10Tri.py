def creationListe():
    length = int(input("Longueur de votre liste : "))
    tab = []
    for i in range(length):
        nb = int(input("Entrer un chiffre pour la liste "+ str(i) + " : "))
        tab.append(nb)
    return tab

tab = creationListe()
print("votre liste avant le tri : " , tab)

def tri_insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

tri_insertion(tab) 
print ("Voici le tableau suite au tri :" , tab)
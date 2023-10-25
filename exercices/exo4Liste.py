import statistics as stat

mylist = [9,11,16,12,6,8,3,13,52,27]

def moyenne (mylist):
        long = len(mylist)
        total = sum(mylist)
        resultat = total / long
        return resultat

a = moyenne(mylist)

print("Le chiffre max est : ", max(mylist))
print("Le chiffre min est : ", min(mylist))
print("La moyenne est : ", a)
print("La moyenne avec le module stat est : ", stat.mean(mylist))
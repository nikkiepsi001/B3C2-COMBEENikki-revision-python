def text1(): 
    f = open("text1.txt", "r")
    a = f.read()
    print(a)
    return a

def nombreMot(a):
    b = a.split()
    print("Le fichier contient " , len(b) , "de mots.")

def text2(a):
    f2 = open("text2.txt", "w")
    c = f2.write(a)
    print("copie réussie")

a = text1()
nombreMot(a)
text2(a)
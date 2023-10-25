phrase = input("Saisir une phrase : ")
print("La phrase en majuscule : " + phrase.upper())
print("La phrase en minuscule : " + phrase.lower())
length = len(phrase.split())

print("La phrase contient " , length , "de mots.")
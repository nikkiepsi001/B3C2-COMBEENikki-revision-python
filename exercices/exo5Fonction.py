import math

def facto():
    n = int(input("Choisir un chiffre pour trouver sa factorial "))
    constante = 1
    for i in range(1, n+1):
        constante = constante * i
    print("La factorial de " , n , "est : " , constante)
    print("La factorial de " , n , "avec le module math est :" , math.factorial(n))

facto()



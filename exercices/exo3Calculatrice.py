def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

num1 = int(input("Choisir un premier chiffre : "))
num2 = int(input("Choisir un deuxième chiffre : "))

addition = add(num1, num2)
print("L'addition est :" , addition)

soustraction = sub(num1, num2)
print("La soustraction est :" , soustraction)

multiplication = mul(num1, num2)
print("La multiplication est :" , multiplication)

division = div(num1, num2)
print("La division est :" , division)
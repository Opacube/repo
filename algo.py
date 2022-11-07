def add(x, y):
    return (x + y)
add(1, 3)

def sub(x, y):
    return (x - y)
sub(5, 6)

def multiply(x, y):
    return (x * y)
multiply (6, 9)

def divide(x, y):
    return (x / y)
divide (20, 2)

def modulo(x, y):
    return (x % y)
modulo (10,2)


def salaire_seconde(y, x, z):
    salaire_heure = y
    heure_jour = x
    nombre_jours = z
    salaireseconde = ((y / 3600) * x * z) / 365
    return salaireseconde
salaire_seconde(12, 6, 200)


def net(x):
    return (x * 0.23)
net(1700)
import sys

if len(sys.argv) != 2:
    print("Usage: python exo.py <nombre>")
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print("Erreur : l'argument doit être un nombre entier.")
    sys.exit()

if n < 2:
    est_premier = False
else:
    est_premier = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            est_premier = False
            break

if est_premier:
    print("Oui, {} est un nombre premier.".format(n))
else:
    print("Non, {} n'est pas un nombre premier.".format(n))
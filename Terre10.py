import sys
import math

# Vérification des arguments
if len(sys.argv) != 2:
    print("error: veuillez fournir un entier positif en argument")
    sys.exit()

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("L'entier doit être positif")
except ValueError:
    print("error: l'argument doit être un entier positif")
    sys.exit()

# Calcul de la racine carrée
sqrt_n = math.sqrt(n)

# Affichage du résultat
print(sqrt_n)
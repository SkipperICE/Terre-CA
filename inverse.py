import sys

# Vérifier le nombre d'arguments en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python exo.py <chaine>")
    sys.exit()

# Obtenir la chaîne à inverser à partir de l'argument en ligne de commande
chaine = sys.argv[1]

# Inverser la chaîne en utilisant l'opérateur de slicing
inverse = chaine[::-1]

# Afficher la chaîne inversée
print(inverse)
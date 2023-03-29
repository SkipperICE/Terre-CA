import sys

if len(sys.argv) != 3:
    print("Usage: python exo.py <chiffre> <exposant>")
    sys.exit()

zebi = sys.argv[2]

if not isinstance(zebi, int):
    print("Erreur : l'argument doit être une nombre entier")
    sys.exit()

chiffre = int(sys.argv[1])
exposant = int(sys.argv[2])

if exposant < 0:
    print("Erreur : l'argument doit être un nomnre positif.")
    sys.exit()



resultat = chiffre ** exposant
print("résultat :", resultat)

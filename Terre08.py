import sys

if len(sys.argv) != 2:
    print("Usage: python exo.py <chaine>")
    sys.exit()

chaine = sys.argv[1]

if not isinstance(chaine, str):
    print("Erreur : l'argument doit être une chaîne de caractères.")
    sys.exit()

nmbrcharactere = len(chaine)

print(nmbrcharactere)

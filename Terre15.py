import sys

if len(sys.argv) < 2:
    print("Usage: python exo.py <entier1> [<entier2> <entier3> ...]")
    sys.exit()

entiers = []
for arg in sys.argv[1:]:
    try:
        entier = int(arg)
        entiers.append(entier)
    except ValueError:
        print("Erreur : tous les arguments doivent être des entiers.")
        sys.exit()

if entiers == sorted(entiers):
    print("Triée !")
else:
    print("Pas triée !")
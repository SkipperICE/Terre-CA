import sys

if len(sys.argv) != 4:
    print("Usage: python exo.py <entier1> <entier2> <entier3>")
    sys.exit()


entiers = [int(x) for x in sys.argv[1:]]

entiers_tries = sorted(entiers)

if entiers_tries[0] == entiers_tries[2] == entiers_tries[1]:
    print("Erreur : les trois entiers sont égaux.")
    sys.exit()

if entiers_tries[0] == entiers_tries[2] or entiers_tries[0] == entiers_tries[1] or entiers_tries[1] == entiers_tries[2]:
    print("Erreur : 2 des trois entiers sont égaux.")
    sys.exit()


print(entiers_tries[1])
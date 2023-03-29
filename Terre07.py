import sys

if len(sys.argv) != 2:
    print("Usage: python exo.py <chaine>")
    sys.exit()

chaine = sys.argv[1]

inverse = chaine[::-1]

print(inverse)
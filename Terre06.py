import sys

if len(sys.argv) != 3:
    print("Usage: python exo.py <dividende> <diviseur>")
    sys.exit()

dividende = int(sys.argv[1])
diviseur = int(sys.argv[2])

if diviseur == 0:
    print("Erreur : le diviseur ne peut pas être zéro.")
    sys.exit()

if diviseur > dividende:
    print("Erreur : le diviseur ne peut pas être plus grand que le dividende.")
    sys.exit()

resultat = dividende // diviseur
reste = dividende % diviseur
print("résultat :", resultat)
print("reste :", reste)


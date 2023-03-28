import sys
import re

if len(sys.argv) != 2:
    print("Usage: python exo.py <heure>")
    sys.exit()

heure = sys.argv[1]

if not re.match(r"^\d{2}:\d{2}$", heure):
    print("Erreur : format d'heure invalide.")
    sys.exit()

heures, minutes = heure.split(":")

heures = int(heures)
minutes = int(minutes)

if heures < 0 or heures > 23 or minutes < 0 or minutes > 59:
    print("Erreur : heure invalide.")
    sys.exit()

if heures == 0:
    heure12 = "12:{:02d}AM".format(minutes)
elif heures == 12:
    heure12 = "12:{:02d}PM".format(minutes)
elif heures < 12:
    heure12 = "{:d}:{:02d}AM".format(heures, minutes)
else:
    heure12 = "{:d}:{:02d}PM".format(heures - 12, minutes)

# Afficher l'heure au format 12h
print(heure12)
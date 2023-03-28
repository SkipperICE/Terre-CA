import sys
import re

# Vérifier le nombre d'arguments en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python exo.py <heure>")
    sys.exit()

# Obtenir l'heure à partir de l'argument en ligne de commande
heure12 = sys.argv[1]

# Valider le format de l'heure
if not re.match(r"^(1[0-2]|0?[1-9]):([0-5][0-9])([AP]M|am|pm)$", heure12):
    print("Erreur : format d'heure invalide.")
    sys.exit()

# Séparer les heures, les minutes et l'indicateur AM/PM
heures, minutes, am_pm = re.match(r"^(1[0-2]|0?[1-9]):([0-5][0-9])([AP]M|am|pm)$", heure12).groups()

# Convertir les heures et les minutes en nombres entiers
heures = int(heures)
minutes = int(minutes)

# Ajouter 12 heures pour les heures PM (sauf pour midi et minuit)
if am_pm.upper() == "PM" and heures != 12:
    heures += 12

# Retirer 12 heures pour midi et minuit (sauf pour minuit)
if heures == 12 and am_pm.upper() == "AM":
    heures = 0
elif heures == 12 and am_pm.upper() == "PM":
    heures = 12

# Afficher l'heure au format 24h
heure24 = "{:02d}:{:02d}".format(heures, minutes)
print(heure24)
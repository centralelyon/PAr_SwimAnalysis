import requests
import sqlite3
import csv

# Connexion à la BDD
con = sqlite3.connect("..\Databases\BUDAPEST_ROME_TOKYO.db")
cursor = con.cursor()


API_url = "https://ffn.extranat.fr/webffn/_recherche.php?go=ind&idrch="


with open('nageurs.csv', 'w', newline='', encoding='UTF8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';')
    # Entête du fichier
    filewriter.writerow(['id', 'nom', 'prenom', 'anneeDeNaissance', 'sexe', 'nationalite', 'club'])

    for row in cursor.execute('SELECT id, nom, prenom, anneeDeNaissance, sexe, nationalite, club FROM nageurs WHERE nationalite = "FRA"'):
            nageur = list(row)
            name = nageur[1]
            firstname = nageur[2]
            response = requests.get(API_url + name + ' ' + firstname)
            res = response.json()
            nageur[0] = res[0]['iuf']
            # Ecriture
            filewriter.writerow(nageur)




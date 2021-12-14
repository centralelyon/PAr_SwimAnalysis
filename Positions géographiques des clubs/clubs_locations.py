# -*- coding utf-8 -*-
import requests
import sqlite3
import csv

# API KEY : AIzaSyBZ785WF-87b4FO-WUv_EfprdoOOluWzi8

# Connexion à la BDD
con = sqlite3.connect("BUDAPEST_ROME_TOKYO.db")
cursor = con.cursor()

clubs = []

with open('clubs_locations.csv', 'w', newline='', encoding='UTF8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')

    # Entête du fichier
    filewriter.writerow(['club', 'address', 'lat', 'lng'])

    # Parcours des clubs référencés
    for row in cursor.execute('SELECT club FROM nageurs WHERE club != ""'):
        clubName = row[0]
        if len(clubName) > 0:

            # Requete API paramètres :
            #   - Nom du Clib : clubName
            #   - Region : France
            #   - Api KEY

            response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+clubName+'&region=France&key=AIzaSyBZ785WF-87b4FO-WUv_EfprdoOOluWzi8')
            try :
                # Lecture de la réponse
                response = response.json()["results"][0]

                # Position géographique et adresse
                lat = response["geometry"]["location"]["lat"]
                lng = response["geometry"]["location"]["lng"]
                address = response["formatted_address"]

                # Ecriture
                filewriter.writerow([clubName,address.replace(',', ' '), lat, lng]) 
            except :
                pass

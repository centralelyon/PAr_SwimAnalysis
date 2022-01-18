# -*- coding: utf-8 -*-
import sqlite3
import csv
import requests

# Connexion à la BDD
con = sqlite3.connect("BUDAPEST_ROME_TOKYO.db")
cursor = con.cursor()

# ExtraNat pour IUF
API_url = "https://ffn.extranat.fr/webffn/_recherche.php?go=ind&idrch="

with open('datas.csv', 'w', newline='', encoding='UTF8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';') 
    filewriter.writerow(['idNageur', 'Prénom', 'Nom', 'Sexe', 'DateDeNaissance', 'Nationalite', 'Club', 'idCourse', 'idCompetition', 'LongeurBassin', 'DistanceCourse', 'StyleDeNage', 'Round', 'Date', 'TempsDebutCourse', 'TempsFinalCourse', 'idAnalyse'])
    for row in  cursor.execute('''SELECT n.id, n.prenom, n.nom, n.sexe, n.anneeDeNaissance, n.nationalite, n.club, c.id, c.idCompetition, c.longueurBassin, c.distance, c.style, c.round, c.dateCourse, a.tpsDebutCourse, a.tpsFinal, a.id
                                    FROM nageurs as n 
                                    JOIN participants as p ON n.id = p.idNageur
                                    JOIN courses as c ON c.id = p.idCourse
                                    JOIN figurants as f ON f.idParticipant = p.id
                                    JOIN analyses as a ON f.id = a.id'''):
        ligne = list(row)
        name = ligne[2]
        firstname = ligne[1]
        try :
            response = requests.get(API_url + name + ' ' + firstname)
            res = response.json()
            ligne[0] = res[0]['iuf']
        except :
            print(API_url + name + ' ' + firstname)
        filewriter.writerow(ligne)
    

    
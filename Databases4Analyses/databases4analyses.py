import sqlite3
import csv

# Connexion à la BDD
con = sqlite3.connect("..\Databases\BUDAPEST_ROME_TOKYO.db")
cursor = con.cursor()

with open('clubs_locations.csv', 'w', newline='', encoding='UTF8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';') 

    queryResult = cursor.execute('''SELECT * 
                        FROM nageurs as n 
                        JOIN participants as p ON n.id = p.idNageur
                        JOIN courses as c ON c.id = p.idCourse
                        JOIN figurants as f ON f.idParticipant = p.id
                        JOIN analyse as a ON f.id = a.id
                        JOIN mouvement as m ON m.idAnalyse = a.id ''')

    
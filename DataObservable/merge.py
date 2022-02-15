# -*- coding: utf-8 -*-
import csv


if __name__ == '__main__':
    db_name = input("Nom de la BDD à ajouter : ")
    maxAnalyseId = 0
    fields = {}

    # Table analyse

    with open('all/analyses.csv', 'r', newline='', encoding='UTF8') as all_analyse:
        analyses_reader = csv.DictReader(all_analyse, delimiter=';')
        for analyse in analyses_reader:
            if(int(analyse['analyses.id']) > maxAnalyseId) :
                maxAnalyseId = int(analyse['analyses.id'])
        fields = analyses_reader.fieldnames

    i = 1
    match = {}      # Correspondance entre ancien id et nouveau

    with open('all/analyses.csv', 'a', newline='', encoding='UTF8') as all_analyse:
        analyses_writter = csv.DictWriter(all_analyse, delimiter=';', fieldnames= fields)

        with open(db_name+'/analyses.csv', 'r', newline='', encoding='UTF8') as new_analyse :
            new_analyses_reader = csv.DictReader(new_analyse, delimiter=';', fieldnames=fields)
            for analyse in list(new_analyses_reader)[1::] :
                new_analyse = analyse
                match[int(analyse['analyses.id'])] = maxAnalyseId + i
                new_analyse['analyses.id'] = maxAnalyseId + i
                analyses_writter.writerow(new_analyse)
                i +=1

    ## TABLE LONGUEURS
    maxId = 0
    fileds = {}

    with open('all/longueurs.csv', 'r', newline='', encoding='UTF8') as all:
        reader = csv.DictReader(all, delimiter=';')
        for elt in reader:
            if(int(elt['id']) > maxId) :
                maxId = int(elt['id'])
        fields = reader.fieldnames

    i = 1

    with open('all/longueurs.csv', 'a', newline='', encoding='UTF8') as all:
        writter = csv.DictWriter(all, delimiter=';', fieldnames= fields)

        with open(db_name+'/longueurs.csv', 'r', newline='', encoding='UTF8') as new :
            new_reader = csv.DictReader(new, delimiter=';', fieldnames=fields)
            for elt in list(new_reader)[1::] :
                new_elt = elt
                new_elt['id'] = maxId + i
                new_elt['idAnalyse'] = match[int(new_elt['idAnalyse'])]
                writter.writerow(new_elt)
                i +=1

    ## TABLE MOUVEMENTS
    maxId = 0
    fileds = {}

    with open('all/mouvements.csv', 'r', newline='', encoding='UTF8') as all:
        reader = csv.DictReader(all, delimiter=';')
        for elt in reader:
            if(int(elt['id']) > maxId) :
                maxId = int(elt['id'])
        fields = reader.fieldnames

    i = 1

    with open('all/mouvements.csv', 'a', newline='', encoding='UTF8') as all:
        writter = csv.DictWriter(all, delimiter=';', fieldnames= fields)

        with open(db_name+'/mouvements.csv', 'r', newline='', encoding='UTF8') as new :
            new_reader = csv.DictReader(new, delimiter=';', fieldnames=fields)
            for elt in list(new_reader)[1::] :
                new_elt = elt
                new_elt['id'] = maxId + i
                new_elt['idAnalyse'] = match[int(new_elt['idAnalyse'])]
                writter.writerow(new_elt)
                i +=1

    ## TABLE SECTIONS
    maxId = 0
    fileds = {}

    with open('all/sections.csv', 'r', newline='', encoding='UTF8') as all:
        reader = csv.DictReader(all, delimiter=';')
        for elt in reader:
            if(int(elt['id']) > maxId) :
                maxId = int(elt['id'])
        fields = reader.fieldnames

    i = 1

    with open('all/sections.csv', 'a', newline='', encoding='UTF8') as all:
        writter = csv.DictWriter(all, delimiter=';', fieldnames= fields)

        with open(db_name+'/sections.csv', 'r', newline='', encoding='UTF8') as new :
            new_reader = csv.DictReader(new, delimiter=';', fieldnames=fields)
            for elt in list(new_reader)[1::] :
                new_elt = elt
                new_elt['id'] = maxId + i
                new_elt['idAnalyse'] = match[int(new_elt['idAnalyse'])]
                writter.writerow(new_elt)
                i +=1
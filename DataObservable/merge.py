# -*- coding: utf-8 -*-
import csv


if __name__ == '__main__':
    db_name = input("Nom de la BDD à ajouter : ")
    maxAnalyseId = 0

    # Table analyse
    with open('all/analyses.csv', 'r', newline='', encoding='UTF8') as all_analyse:
        analyses_reader = csv.DictReader(all_analyse, delimiter=';')
        for analyse in analyses_reader:
            if(int(analyse['analyses.id']) > maxAnalyseId) :
                maxAnalyseId = int(analyse['analyses.id'])
        fields = analyses_reader.fieldnames

    i = 1
    match = {}
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
    print(match)
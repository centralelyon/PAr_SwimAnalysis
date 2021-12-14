# Scrapping IUF

Le but ici est de récupérer l'identifiant unique fédéral (IUF) qui identifie un licencié de la FFN. L'avantage étant de relier facilement plusieurs sources de données (ExtraNat, FFNLives, Espadon...)

## Fonctionnement

Le script Python lit les nageurs présent dans la base de données fournies et pour chacun envoie un requête GET à l'adresse https://ffn.extranat.fr/webffn/_recherche.php avec comme paramètres :

    go = ind
    idrch = {{Nom du nageur}}

Le serveur renvoie un tableau contenant les nageurs correspondant à la recherche. Par exemple pour "Florent Manaudou" : 

    [{"iuf":"158014","ind":"MANAUDOU Florent (1990) H FRA - CN MARSEILLE","sex":"#1e90ff","clb":"CN MARSEILLE"}]

Si la nageur n'a pas d'homonyme, le tableau ne contient qu'un élément. On a facilement l'IUF en tant que champs.

Le résultat final est un CSV [nageurs.csv](nageurs.csv) qui conserve les champs de la table *Nageur* de la BDD mais dont l'id inital est remplacé par l'IUF.

## Exécution

Il suffit d'exécuter le script en s'assurant que les bibliothèques utilisées sont installées.

## Dépendances

Le script python utilise les bibliothèques suivantes :
- *request* afin d'émettre une requette HTTP.
- *sqlite3* afin de lire la base de données des nageurs.
- *csv* afin d'écrire les résultat dans un fichier CSV.
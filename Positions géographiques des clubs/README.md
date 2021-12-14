# Position géogrphique des clubs

## Problème

Nous souhaitions positionner les nageurs sur une carte en fonctione de leur club d'appartenance. Nous n'avions cependant que le nom des clubs et non pas leurs coordonnées géographiques.

## Solutions

Nous utilisons l'API de Google Map qui, avec le simple nom d'un club, permet d'obtenir l'adresse et les coordonnées. 

Le script Python récupère le nom de chaque club représentés dans notre base de données et fait un appel à l'api. Il enregistre ensuite la réponse dans un fichier CSV facile à lire.

## Utilisation

Pour utiliser ce script, il suffit d'executer le fichier python [*club_location.py*](clubs_locations.py). en s'assurant avoir une connexion internet.

Les données sont écrites dans le fichier [*club_locations.csv*](clubs_location.csv).

## Dépendances

Le script python utilise les bibliothèques suivantes :
- *request* afin d'émettre une requette HTTP à l'API.
- *sqlite3* afin de lire la base de données des nageurs.
- *csv* afin d'écrire les résultat dans un fichier CSV.
# LBIRA2130_Couverts

## Aperçu
Ce projet vise à visualiser l'évolution de différentes mesures prises dans des cultures maraîchères biologiques en fonction de l'utilisation de différents types de couverts permanents. 
Les graphiques initiaux sont générés via des équations arbitraires définies après une recherche bibliographique approfondie. L'objectif est d'affiner les courbes d'évolution au fil de l'expérience en y ajoutant des données expérimentales.


## Installation
1. Cloner le dépôt GitHub :
```
    git clone https://github.com/mara0896/LBIRA2130_Couverts.git
```

2. Installer les dépendances nécessaires
```
    pip install pandas
    pip install matplotlib
```

## Utilisation
Avant toute exécution, il est important de s'assurer que l'on dispose d'un fichier Excel intitulé 'mesures_couverts.xlsx' contenant les données expérimentales de l'expérience.

Le fichier Excel est de la forme d'un tableau constitué des colonnes suivantes :

| Colonne          | Description                                    |
|------------------|------------------------------------------------|
| annee            | Nombre entier entre 1 et 25 représentant le nombre d'années passées depuis le début de l'expérience |
| date             | Date exacte des mesures au format DD/MM/YY
| ID_planche       | Identifiant de la planche entre 1 et 10 suivi de a ou b |
| couvert          | Type de couvert présent sur la planche |
| culture          | Type de culture présent sur la planche au moment des mesures |
| pH_KCl           | PH KCl mesuré lors de l'analyse de sol |
| pH_H2O           | PH H2O mesuré lors de l'analyse de sol |
| N                | Taux en azote mesuré |
| P                | Taux en phosphore mesuré |
| K                | Taux en potassium mesuré |
| Ca               | Taux en calcium mesuré |
| Mg               | Taux en magnésium mesuré |
| C_orga           | Taux de carbone organique mesuré |
| humus            | Pourcentage en humus mesuré |
| argile           | Pourcentage en argile estimé |
| limon            | Pourcentage en limon estimé |
| sable            | Pourcentage en sable estimé |
| CEC              | CEC estimée par la formule %argile * 0,37 + %C_orga * 2,73 |
| poids_moyen      | Poids moyen mesurés avec un échantillon des légumes récoltés |
| humidite         | Taux d'humidité mesuré |
| taux_decomposition | Taux de décomposition calculé avec le teabag index |
| activite_biologique | Activité biologique calculée avec le teabag index |

Chaque ligne représente une date à laquelle on a réalisé des mesures. Le fichier peut ne pas contenir de valeur chiffrées dans toutes les colonnes à toutes les dates. Le code présent ici prend compte de celà, d'où la présence du nombre d'année en première colonne.


Une fois que le fichier Excel est bien en forme, le code principal peut être exécuté pour générer les graphiques :
'''
    python couverts.py
'''

une fois le code tourné, les graphiques résultants seront sauvergardés sous format '.PNG' dans le dossier 'output'.

## Exemples
Ici, nous présentons le type d'images générées par le code :


## Licence
Ce projet est sous licence MIT. Consultez le fichier 'LICENSE' pour plus d'informations sur les conditions d'utilisation de ce projet.

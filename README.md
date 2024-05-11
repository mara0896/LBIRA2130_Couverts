# LBIRA2130_Couverts

## Aperçu
Ce projet vise à visualiser l'évolution de différentes mesures prises dans des cultures maraîchères biologiques en fonction de l'utilisation de différents types de couverts permanents. 
Les graphiques initiaux sont générés via des équations arbitraires définies après une recherche bibliographique approfondie présentée dans le rapport de ce projet à la section 4.4.2. L'objectif est d'affiner les courbes d'évolution au fil de l'expérience en y ajoutant des données expérimentales.


## Installation
1. Cloner le dépôt GitHub :
```
    git clone https://github.com/mara0896/LBIRA2130_Couverts.git
```

2. Installer les dépendances nécessaires
```
    pip install pandas
    pip install matplotlib
    pip install numpy
    pip install openpyxl 
```

## Utilisation
Avant toute exécution, il est important de s'assurer que l'on dispose d'un fichier Excel intitulé 'mesures_couverts.xlsx' contenant les données expérimentales de l'expérience ainsi que de l'Excel théorique de référence intitulé 'donnees_theoriques.xlsx' permettant de visualiser les plots du fichier 'couverts.py' avant de disposer des résultats du plan expérimental.

Les fichiers Excel sont tous les deux de la même forme. Il présente un tableau constitué des colonnes suivantes :

| Colonne          | Description                                    |
|------------------|------------------------------------------------|
| annee            | Nombre entier entre 1 et 25 représentant le nombre d'années passées depuis le début de l'expérience |
| date             | Date exacte des mesures au format DD/MM/YY |
| saison           | Saison au moment de la mesure. Choix multiple entre printemps, été, automne et hiver |
| ID_planche       | Identifiant de la planche entre 1 et 10 suivi de a ou b |
| numero_mesure    | Identifiant de la prise de mesure/ Entier en partant de 1 représentant le nombre de fois où l'on a réalisé des mesures sur la demi-planche concernée. |
| couvert          | Type de couvert présent sur la planche. Choix multiple entre : bache, melilot_moha, paille, BRF et trefles |
| culture          | Type de culture présent sur la planche au moment des mesures. Choix multiple entre : oignons, haricots, courges, epinards et choux |
| annee_rotation   | Phase de la rotation dans laquelle on se trouve. 1 pour l'année avec des oignons et des haricots, 2 pour l'année avec des courges mixes et 3 pour l'année avec des épinards et des choux |
| pH_KCl           | PH KCl mesuré lors de l'analyse de sol. Adimensionnel |
| pH_H2O           | PH H2O mesuré lors de l'analyse de sol. Adimensionnel |
| N                | Taux en azote mesuré en % en laboratoire |
| P                | Taux en phosphore mesuré en mg par 100g de sol sec en laboratoire |
| K                | Taux en potassium mesuré en mg par 100g de sol sec en laboratoire |
| Ca               | Taux en calcium mesuré en mg par 100g de sol sec en laboratoire |
| Mg               | Taux en magnésium mesuré en mg par 100g de sol sec en laboratoire |
| C_orga           | Taux de carbone organique mesuré en g par kg de sol sec en laboratoire |
| humus            | Pourcentage en humus mesuré en % en laboratoire |
| argile           | Pourcentage en argile estimé en % par sédimentation gravitaire |
| limon            | Pourcentage en limon estimé en % par sédimentation gravitaire |
| sable            | Pourcentage en sable estimé en % par sédimentation gravitaire |
| CEC              | CEC estimée par la formule %argile * 0,37 + %C_orga * 2,73 en meq par 100g de sol|
| poids_moyen      | Poids moyen mesurés avec un échantillon des légumes récoltés. Mesure du poids par légume pour les choux, les oignons et les courges. Mesure du poids total des gousses du plants pour les haricots et mesure du poids total des feuilles pour les épinards |
| humidite_100      | Taux d'humidité mesuré par sonde en % à 100 millimètres de profondeur |
| humidite_200 | Taux d'humidité mesuré par sonde en % à 200 millimètres de profondeur |
| humidite_300 | Taux d'humidité mesuré par sonde en % à 300 millimètres de profondeur |
| humidite_400 | Taux d'humidité mesuré par sonde en % à 400 millimètres de profondeur |
| taux_decomposition | Taux de décomposition calculé avec le teabag index expliqué dans la partie 4.3.3.3 du rapport |
| activite_biologique | Activité biologique calculée avec le teabag index expliqué dans la partie 4.3.3.3 du rapport |

Chaque ligne représente une date à laquelle on a réalisé des mesures. Le fichier peut ne pas contenir de valeur chiffrées dans toutes les colonnes à toutes les dates. Le code présent ici prend compte de celà, d'où la présence du nombre d'année en première colonne.


Une fois que le fichier Excel est bien en forme, le code principal peut être exécuté pour générer les graphiques :

```
    python couverts.py
```
Si l'utilisateur veut changer les paramètres des graphiques retournés, il peut se rendre à la fin du code dans la partie "UTILISATEURS" qui détaille la sortie de chaque fonction ainsi que les arguments nécessaires à son fonctionnement.

Dans toutes les fonctions utilisables de ce fichier, les mêmes paramètres sont utilisés. L'utilisateur peut choisir entre plusieurs possibilités :
 
* data : 'data_th' ou 'data_exp' qui correpondent respectivement aux données théoriques indiquant la tendance supposée des mesures et aux données expérimentales encodées dans le fichier Excel correspondant lors de l'expérience
* annee : un nombre entier entre 1 et 25 qui correspond au nombre d'année où l'on se situe dans l'expérience
* couvert : 'bache', 'paille', 'melilot_moha', 'BRF' ou 'trefles'
* culture : 'oignons', 'haricots', 'courges', 'epinards' ou 'choux'
* type  : utilisés dans deux des fonctions proposées. Les choix possibles seront spécifiés au moment de l'appel de la fonction.


une fois le code tourné, les graphiques résultants seront sauvergardés sous format '.PNG' dans le dossier 'output'.

## Exemples
Ici, nous présentons le type d'images générées par le code :

%TODO


## Licence
Ce projet est sous licence MIT. Consultez le fichier 'LICENSE' pour plus d'informations sur les conditions d'utilisation de ce projet.

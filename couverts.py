# IMPORTS -----------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# DONNEES EXPERIMENTALES --------------------------------------------------------------
data_exp = pd.read_excel('mesures_couverts.xlsx')


# DONNES THEORIQUES --------------------------------------------------------------------
data_th = pd.read_excel('donnees_theoriques.xlsx', sheet_name = "Donnees_theoriques")   


# ANALYSE DE PH ------------------------------------------------------------------------

def barchart_ph(data, annee):

    sort_data = data[data['annee'] == annee]

    means = sort_data.groupby(['couvert', 'culture'])[['pH_KCl', 'pH_H2O']].mean()
    
    means.plot(kind = 'bar', color = ['skyblue', 'indianred'], edgecolor = 'black')
    plt.title(f'pH_KCl et pH _H2O par traitement lors de l\'année {annee}')
    plt.xlabel('Traitements')
    plt.ylabel('pH')
    plt.ylim(0,14)
    plt.xticks(rotation = 45)
    plt.legend(title = 'Type de pH')
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/barchart_ph.png')

    plt.show()


def barchart_ph2(data, annee, couvert):

    sort_data1 = data[data['annee'] == annee] 
    sort_data = sort_data1[sort_data1['couvert'] == couvert]

    means = sort_data.groupby('culture')[['pH_KCl', 'pH_H2O']].mean()
    
    means.plot(kind = 'bar', color = ['skyblue', 'indianred'], edgecolor = 'black')
    plt.title(f'pH_KCl et pH _H2O lors de l\'année {annee} avec le couvert {couvert}')
    plt.xlabel('Culture')
    plt.ylabel('pH')
    plt.ylim(0,14)
    plt.xticks(rotation = 45)
    plt.legend(title = 'Type de pH')
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/barchart_ph2.png')

    plt.show()


def time_ph(data, type, culture):

    sort_data = data[data['culture'] == culture]

    means = sort_data.groupby(['annee','couvert'])[type].mean()
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize = (8,6))
    for couvert, color in zip(means.index.get_level_values('couvert').unique(), colors):
        plt.plot(means.loc[means.index.get_level_values('couvert') == couvert].index.get_level_values('annee'), 
                means.loc[means.index.get_level_values('couvert') == couvert],
                marker = 'o',
                label = couvert,
                color = color)

    plt.title(f'{type} moyen au cours du temps en fonction du couvert pour la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel(f'{type} moyen')
    plt.ylim(0,14)
    plt.legend(title = 'Type de couvert')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_ph.png')

    plt.show()



# ANALYSE N, P, K ----------------------------------------------------------------------

def time_element(data, couvert, culture):

    sort_data1 = data[data['culture'] == culture]
    sort_data = sort_data1[sort_data1['couvert'] == couvert]

    means = sort_data.groupby('annee')[['N', 'P', 'K']].mean()
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize = (8,6))
    for i, color in zip(['N', 'P', 'K'], colors):
        plt.plot(means.index, means[i],
                marker = 'o',
                label = i,
                color = color)

    plt.title(f'Évolution des taux de N, P et K pour le traitement {couvert}-{culture}')
    plt.xlabel('Année')
    plt.ylabel('Taux moyen')
    plt.legend(title = 'Éléments')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_element.png')

    plt.show()



def barchart_element(data, culture):
    sort_data = data[data['culture'] == culture]

    means = sort_data.groupby('couvert')[['N', 'P', 'K']].mean()
    means = means.T

    means.plot(kind = 'bar', figsize = (8,6), color = ['skyblue', 'springgreen', 'indianred','orange','hotpink'], edgecolor = 'black')
    plt.title(f'Taux de N, P et K moyens pour la culture {culture} en fonction du type de couvert')
    plt.xlabel('Éléments')
    plt.ylabel('Taux moyens en éléments')
    plt.xticks(rotation = 0)
    plt.yticks(np.arange(0,plt.ylim()[1]+1, 1))
    plt.legend(title = "Couverts")
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/barchart_element.png')

    plt.show()
    



# ANALYSE Ca, Mg -----------------------------------------------------------------------

def time_Mg_Ca(data, culture, element):

    sort_data = data[data['culture'] == culture]
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize=(8,6))

    for couvert, color in zip(sort_data['couvert'].unique(), colors):
        
        actual_data = sort_data[sort_data['couvert'] == couvert]
        means = actual_data.groupby('annee')[element].mean()
        plt.plot(means.index, means.values, 
                 marker = 'o', 
                 label = couvert,
                 color = color)

    plt.title(f'Évolution des taux de {element} en fonction du couvert pour la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel(f'Taux moyen en {element}')
    plt.legend(title = 'Couverts')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_Mg_Ca.png')

    plt.show()




# ANALYSE GRANULOMETRIQUE --------------------------------------------------------------

def barchart_granulo(data, culture, annee):

    sort_data1 = data[data['culture'] == culture]
    sort_data = sort_data1[sort_data1['annee'] == annee]
    
    if len(sort_data) == 0:
        return print("Cette culture ne semble pas être disponible à l'année sélectionnée. Changez les paramètres")

    means = sort_data.groupby('couvert')[['argile', 'limon', 'sable']].mean()

    means.plot(kind = 'bar', stacked = True, figsize = (8,6), color = ['skyblue', 'springgreen', 'orange'], edgecolor = 'black')
    plt.title(f'Proportions en argile, limon et sable par type de couvert pour la culture {culture} \n après {annee} années')
    plt.xlabel('Type de couvert')
    plt.ylabel('Proportions cummulées')
    plt.xticks(rotation = 45)
    plt.legend(title = "Particules")
    plt.yticks(np.arange(0,plt.ylim()[1], 5))
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/barchart_granulo.png')

    plt.show()


def time_granulo(data, couvert, culture):

    sort_data1 = data[data['culture'] == culture]
    sort_data = sort_data1[sort_data1['couvert'] == couvert]

    means = sort_data.groupby('annee')[['limon', 'argile', 'sable']].mean()
    colors = ['skyblue', 'indianred', 'orange']

    plt.figure(figsize = (8,6))
    for i, color in zip(['limon', 'argile', 'sable'], colors):
        plt.plot(means.index, means[i],
                marker = 'o',
                label = i,
                color = color)

    plt.title(f"Évolution des taux de limon, d'argile et de sable pour \n le traitement {couvert}-{culture}")
    plt.xlabel('Année')
    plt.ylabel('Taux moyen')
    plt.legend(title = 'Particules')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.yticks(np.arange(0,plt.ylim()[1], 5))
    plt.tight_layout()
    plt.savefig('Outputs/time_granulo.png')

    plt.show()




# ANALYSE CARBONE ORGANIQUE ET HUMUS ---------------------------------------------------

def time_Corga_humus(data, culture, type):

    sort_data = data[data['culture'] == culture]
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize=(8,6))

    for couvert, color in zip(sort_data['couvert'].unique(), colors):
        
        actual_data = sort_data[sort_data['couvert'] == couvert]
        means = actual_data.groupby('annee')[type].mean()
        plt.plot(means.index, means.values, 
                 marker = 'o', 
                 label = couvert,
                 color = color)

    plt.title(f'Évolution des taux de {type} en fonction du couvert pour \n la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel(f'Taux moyen en {type}')
    plt.legend(title = 'Couverts')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_Corga_humus.png')

    plt.show()




# ANALYSE CEC --------------------------------------------------------------------------

def time_CEC(data, culture):

    sort_data = data[data['culture'] == culture]

    means = sort_data.groupby(['annee','couvert'])['CEC'].mean().unstack()
    colors = ['skyblue', 'springgreen', 'indianred', 'orange', 'hotpink']

    plt.figure(figsize = (8,6))
    for color, couvert in zip(colors, means.columns):
        plt.plot(means.index, means[couvert],
                 marker = 'o',
                 label = couvert,
                 color = color)

    plt.title(f' CEC moyenne au cours du temps en fonction du couvert \n pour la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel('CEC moyenne')
    plt.legend(title = 'Type de couvert')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_CEC.png')

    plt.show()




# ANALYSE POID MOYEN RECOLTE -----------------------------------------------------------

def barchart_poids(data):
    
    means = data.groupby(['culture', 'couvert'])['poids_moyen'].mean().unstack()

    plt.figure(figsize = (8,6))
    means.plot(kind = 'bar', color =['skyblue', 'springgreen', 'indianred','orange','hotpink'], edgecolor = 'black')
    plt.title("Poids moyen récolté par traitement")
    plt.xlabel('Type de culture')
    plt.ylabel('Poids moyen')
    plt.xticks(rotation = 45)
    plt.yticks(np.arange(0,plt.ylim()[1], 100))
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.legend(title = 'Couvert')
    plt.tight_layout()
    plt.savefig('Outputs/barchart_poids.png')

    plt.show()




def time_poid(data, culture):
     
    sort_data = data[data['culture'] == culture]
    means = sort_data.groupby(['annee', 'couvert'])['poids_moyen'].mean().unstack()
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize=(12, 8))
    for couvert, color in zip(means.columns, colors):
        plt.plot(means.index, means[couvert],
                 marker = 'o', 
                 label = couvert,
                 color = color)

    plt.title(f'Évolution du poids moyen récolté en fonction du couvert \n avec la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel('Poids moyen récolté')
    plt.legend(title = 'Couverts') 
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_poids.png')

    plt.show()




# ANALYSE HUMIDITE ---------------------------------------------------------------------

def profil_humidite(data, annee, culture):
    sort_data1 = data[data['annee'] == annee]
    sort_data = sort_data1[sort_data1['culture'] == culture]

    means = sort_data.groupby('couvert')[['humidite_100', 'humidite_200', 'humidite_300', 'humidite_400']].mean()
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize = (8,6))

    for couvert, color in zip(means.index, colors):
        plt.plot(means.loc[couvert], means.columns, 
                 marker = 'o', 
                 label = couvert,
                 color = color)
    
    plt.title(f"Humidité en fonction de la profondeur et du couvert pour la culture {culture} \n et l'année {annee}")
    plt.xlabel("Taux d'humidité [%]")
    plt.ylabel('Profondeur [mm]')
    plt.gca().invert_yaxis()
    plt.yticks(['humidite_100', 'humidite_200', 'humidite_300', 'humidite_400'], [100, 200, 300, 400])
    plt.legend(title = 'Couverts')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/profil_humidite.png')
 
    plt.show()




def time_humidite(data, couvert, culture):

    sort_data1 = data[data['culture'] == culture]
    sort_data = sort_data1[sort_data1['couvert'] == couvert]

    means = sort_data.groupby('annee')[['humidite_100', 'humidite_200', 'humidite_300', 'humidite_400']].mean()
    profondeurs = ['100 mm', '200 mm', '300 mm', '400 mm']
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize = (8,6))
    for i, profondeur, color in zip(['humidite_100', 'humidite_200', 'humidite_300', 'humidite_400'], profondeurs, colors):
        plt.plot(means.index, means[i],
                marker = 'o',
                label = profondeur,
                color = color)

    plt.title(f"Évolution de l'humidité moyenne en fonction de la profondeur pour \n le traitement {couvert}-{culture}")
    plt.xlabel('Année')
    plt.ylabel("Taux d'humidité moyen")
    plt.legend(title = 'Profondeur')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_humidite.png')

    plt.show()




# ANALYSE ACTIVITE BIOLOGIQUE ---------------------------------------------------------- 
def time_actibio_decompo(data, culture, type):

    sort_data = data[data['culture'] == culture]
    colors =['skyblue', 'springgreen', 'indianred','orange','hotpink']

    plt.figure(figsize=(8,6))

    for couvert, color in zip(sort_data['couvert'].unique(), colors):
        
        actual_data = sort_data[sort_data['couvert'] == couvert]
        means = actual_data.groupby('annee')[type].mean()
        plt.plot(means.index, means.values,
                 marker = 'o',
                 label = couvert,
                 color = color)

    plt.title(f'Évolution du {type} en fonction du couvert pour la culture {culture}')
    plt.xlabel('Année')
    plt.ylabel(f'{type} moyen')
    plt.legend(title = 'Couverts')
    plt.grid(True, linestyle = '--', alpha = 0.7)
    plt.tight_layout()
    plt.savefig('Outputs/time_actibio_decompo.png')

    plt.show()




# UTILISATEURS -----------------------------------------------------------------------------------------------------

'''
    Dans toutes les fonctions utilisables de ce fichier, les mêmes paramètres sont utilisés. L'utilisateur peut choisir entre plusieurs possibilités :
 
    - data : 'data_th' ou 'data_exp' qui correpondent respectivement aux données théoriques indiquant la tendance supposée des mesures et aux données expérimentales encodées dans le fichier Excel correspondant lors de l'expérience
    - annee : un nombre entier entre 1 et 25 qui correspond au nombre d'année où l'on se situe dans l'expérience
    - couvert : 'bache', 'paille', 'melilot_moha', 'BRF' ou 'trefles'
    - culture : 'oignons', 'haricots', 'courges', 'epinards' ou 'choux'
    - type  : utilisés dans deux des fonctions proposées. Les choix possibles seront spécifiés au moment de l'appel de la fonction.

'''

# GRAPHES CONCERNANT LE PH

# Retourne un barchart représentant les pH KCl et H2O pour chaque traitement (association couvert/culture) à l'année choisie.
# argument 1 : data  
# argument 2 : annee 
barchart_ph(data_th, 2)

# Retourne un barchart représentant les pH KCl et H2O en fonction de la culture pour un couvert et une année sélectionnés.
# argument 1 : data 
# argument 2 : annee 
# argument 3 : couvert
barchart_ph2(data_th, 2, 'trefles')   

# Retourne un graphe représentant un type de pH choisi au cours du temps en fonction du type de couvert pour une culture choisie
# argument 1 : data
# argument 2 : type de pH ('pH_KCl' ou 'pH_H2O')
# argument 3 : culture 
time_ph(data_th, 'pH_KCl', 'oignons')



# GRAPHES SUR LES TAUX D'AZOTE (N), DE PHOSPHORE (P) ET DE POTASSIUM (K)

# Retourne un graphe représentant les taux de N, P et K au cours du temps pour un traitement choisi.
# argument 1 : data
# argument 2 : couvert
# argument 3 : culture
time_element(data_th, 'trefles', 'oignons')

# Retourne un barchart donnant les taux en N, P, K en fonction du couvert pour une culture choisie
# argument 1 : data
# argument 2 : culture
barchart_element(data_th, 'oignons')



# GRAPHES SUR LES TAUX DE CALCIUM (Ca) ET DE MAGNESIUM (Mg)

# Retourne un graphe représentant les taux en Ca ou Mg au cours du temps pour une culture choisie
# argument 1 : data
# argument 2 : culture
# argument 3 : type d'élément. Choix entre 'Ca' ou 'Mg'
time_Mg_Ca(data_th, 'oignons','Ca') 



# RESULTATS DE L'ANALYSE GRANULOMETRIQUE

# Retourne un barchart représentant les proportions en limon, argile et sable en fonction du couvert pour une culture choisie à une année donnée
# argument 1 : data
# argument 2 : culture
# argument 3 : annee
barchart_granulo(data_th, 'oignons', 3)


# Retourne un graphe représentant les taux en limon, sable et argile au cours du temps pour un traitement choisi
# argument 1 : data
# argument 2 : couvert
# argument 3 : culture
time_granulo(data_th, 'trefles', 'oignons')



# GRAPHES SUR LE CARBONE ORGANIQUE ET LE TAUX D'HUMUS 

# Retourne un graphe représentant les taux de carbone organique ou de humus en fonction du couvert au cours du temps pour une culture choisie
# argument 1 : data
# argument 2 : culture
# argument 3 : type de mesure. Choix entre 'C_orga' ou 'humus'.
time_Corga_humus(data_th, 'oignons','C_orga') 



# GRAPHE DE CEC 

# Retourne un graphe représentant la CEC au cours du temps en fonction du couvert pour une culture choisie
# argument 1 : data
# argument 2 : culture
time_CEC(data_th, 'oignons')



# GRAPHES SUR LE POIDS MOYEN DES RECOLTES

# Retourne un barchat représentant le poids moyen récolté pour chaque traitement possible
# argument 1 : data
barchart_poids(data_th)

# Retourne un graphe représentant l'évolution du poids récolté en fonction du couvert pour une culture choisie
# argument 1 : data
# argument 2 : culture
time_poid(data_th, 'oignons')



# GRAPHES D'ANALYSE DU TAUX D'HUMIDITE

# Retourne un graphe représentant l'humidité à différentes profondeurs en fonction du couvert pour une culture et une année choisie
# argument 1 : data
# argument 2 : annee
# argument 3 : culture
profil_humidite(data_th, 1, 'oignons')


# Retourne un graphe représentant l'évolution de l'humidité en fonction du temps et de la profondeur pour un traitement choisi
# argument 1 : data
# argument 2 : couvert
# argument 3 : culture
time_humidite(data_th, 'trefles', 'oignons') 



# GRAPHE DE L'ANALYSE DE L'ACTIVITE BIOLOGIQUE ET DU TAUX DE DECOMPOSITION

# Retourne un graphe représentant l'évolution de l'activité biologique ou du taux de décomposition en fonction du couvert pour une culture donnée
# argument 1 : data
# argument 2 : culture
# argument 3 : type de mesure. Choix entre 'activite_biologique' ou 'taux_decomposition'
time_actibio_decompo(data_th, 'oignons','activite_biologique') 

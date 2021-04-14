# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from pymongo import MongoClient

if __name__ == '__main__':
    client= MongoClient(' mongodb://127.0.0.1:27017/')

produit1 = {'_id': 666,
            "nom": 'compote',
            "categorie": 'dessert',
            "rayon": 'frais_dessert',
            "prix_unitaire": 3,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit2 = {'_id': 666,
            "nom": 'granola',
            "categorie": 'céréales',
            "rayon": 'petit_dejeuner',
            "prix_unitaire": 5,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit3 = {'_id': 666,
            "nom": 'banane',
            "categorie": 'fruit',
            "rayon": 'fruit_vrac',
            "prix_unitaire": 0.5,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit4 = {'_id': 666,
            "nom": 'activia',
            "categorie": 'dessert',
            "rayon": 'frais_dessert',
            "prix_unitaire": 2.50,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit5 = {'_id': 666,
            "nom": 'pépite_chocolat',
            "categorie": 'recette_sucre',
            "rayon": 'gateau',
            "prix_unitaire": 2,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit6 = {'_id': 666,
            "nom": 'lait',
            "categorie": 'boisson',
            "rayon": 'frais',
            "prix_unitaire": 1.2,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit7 = {'_id': 666,
            "nom": 'oeuf',
            "categorie": 'viande',
            "rayon": 'boucherie',
            "prix_unitaire": 3.50,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit8 = {'_id': 666,
            "nom": 'beurre',
            "categorie": 'petit_dejeuner',
            "rayon": 'frais',
            "prix_unitaire": 2.80,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit9 = {'_id': 666,
            "nom": 'coca',
            "categorie": 'boisson',
            "rayon": 'boisson',
            "prix_unitaire": 3.50,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit10 = {'_id': 666,
            "nom": 'jambon',
            "categorie": 'charcuterie',
            "rayon": 'frais_viande',
            "prix_unitaire": 1.20,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit11 = {'_id': 666,
            "nom": 'chevre',
            "categorie": 'fromage',
            "rayon": 'frais_fromage',
            "prix_unitaire": 4.40,
            "tags": ["mongodb", "python", "pymongo"],
            }
produit12 = {'_id': 666,
            "nom": 'danette',
            "categorie": 'dessert',
            "rayon": 'frais_dessert',
            "prix_unitaire": 5.10,
            "tags": ["mongodb", "python", "pymongo"],
            }

commande1 = {'_id': 123,
            "quantite_article": 3,
             "nom_produits": ['granola','banane','activia'],
             "prix_total": $sum("prix_unitaire".produit2+"prix_unitaire".produit3+"prix_unitaire".produit4),
             "tags": ["mongodb", "python", "pymongo"],
            }
commande2 = {'_id': 123,
            "quantite_article": 3,
             "nom_produits": ['jambon','danette','lait'],
             "prix_total": $sum("prix_unitaire".produit6+"prix_unitaire".produit10+"prix_unitaire".produit11),
             "tags": ["mongodb", "python", "pymongo"],

Inventaire_produit= { 'id': 410,
                      'liste_produit': [produit1, produit2, produit3,produit4, produit5, produit6,produit7, produit8, produit9,produit10, produit11, produit12],
                      'quantite_produit': [04,11,05,10,26,12,19,10,14,06,30,11],
                      "tags": ["mongodb", "python", "pymongo"],
                      }
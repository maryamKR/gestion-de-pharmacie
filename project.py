import json
liste = []

# This function saves the medication list into a file.
def sauvegarder_list():
    with open("./medicament.json", "w") as file:
        json.dump(liste, file, indent=4)


def charger_list():
    global liste
    try:
        with open("./medications.json", "r") as file:
            liste = json.load(file)
    except FileNotFoundError:
        liste = []

# ============================================
#          1. Ajouter medicament
# ============================================
def ajouter_medicament(id,nom, prix, quantite, expirationDate):
    medicament = {
        "id": id,
        "nom": nom,
        "prix": prix,
        "quantite": quantite,
        "expirationDate": expirationDate
    }
    liste.append(medicament)
    sauvegarder_list()

def menu():
    while True:
        width = 45

        while True:
            width = 45

            def print_line(text=""):
                print("║ " + text.ljust(width - 1) + "║")

            print("\n╔" + "═" * width + "╗")
            print("║" + "GESTION DE FARMACIE (MINI PROJET)".center(width) + "║")
            print("╠" + "═" * width + "╣")

            print_line()
            print_line("[ 1 ] Gestion des Médicaments")
            print_line("[ 2 ] Gestion du Stock")
            print_line("[ 3 ] Gestion des Ventes")
            print_line("[ 4 ] Suivi des Expirations")
            print_line("[ 5 ] Alertes")
            print_line("[ 6 ] Statistiques")
            print_line("[ 0 ] Quitter")
            print_line()

            print("╚" + "═" * width + "╝")

            choix = input("Selectioner votre option : : ")

            if choix == "1":
                while True:
                    print("\n******** [ 1 ] Gestion des Médicaments ********")
                    print("1. Ajouter médicament")
                    print("2. Afficher tous les médicaments")
                    print("3. Rechercher médicament")
                    print("4. Modifier médicament")
                    print("5. Supprimer médicament")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")
                    if choix == "1":
                        id = int(input("Veuillez entrer l’identifiant : "))
                        nom = input("Veuillez entrer le nom du médicament : ")
                        prix = float(input("Veuillez entrer le prix : "))
                        quantite = int(input("Veuillez entrer la quantité : "))
                        expirationDate = input("Veuillez entrer la date d’expiration (AAAA/MM/JJ) : ")

                        ajouter_medicament(id, nom, prix, quantite, expirationDate)


            elif choix == "2":
                while True:
                    print("\n******** [ 2 ] Gestion du Stock ********")
                    print("1. Entrée de stock")
                    print("2. Sortie de stock")
                    print("3. Voir quantité actuelle")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")

            elif choix == "3":
                while True:
                    print("\n******** [ 3 ] Gestion des Ventes ********")
                    print("1. Nouvelle vente")
                    print("2. Liste des ventes")
                    print("3. Ventes du jour")
                    print("4. Retour produit")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")

            elif choix == "4":
                while True:
                    print("\n******** [ 4 ] Suivi des Expirations ********")
                    print("1. Produits expirés")
                    print("2. Produits proches expiration")
                    print("3. Trier par date d’expiration")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")

            elif choix == "5":
                while True:
                    print("\n******** [ 5 ] Alertes ********")
                    print("1. Stock faible")
                    print("2. Produits expirés")
                    print("3. Expiration proche")
                    print("4. Toutes les alertes")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")

            elif choix == "6":
                while True:
                    print("\n******** [ 6 ] Statistiques ********")
                    print("1. Nombre total de médicaments")
                    print("2. Valeur totale du stock")
                    print("3. Médicament le plus vendu")
                    print("4. Ventes totales")
                    print("0. Reteur au menu principal")
                    print("************************************************")
                    choix_sous_menu = input("\nSelectioner votre option : ")

menu()


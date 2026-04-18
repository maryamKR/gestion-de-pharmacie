

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
            print_line("[ 1 ] Ajouter un étudiant")
            print_line("[ 2 ] Afficher tous les étudiants")
            print_line("[ 3 ] Rechercher un étudiant")
            print_line("[ 4 ] Supprimer un étudiant / une note")
            print_line("[ 5 ] Afficher les statistiques (Bonus)")
            print_line("[ 0 ] Quitter")
            print_line()

            print("╚" + "═" * width + "╝")

            choix = input("Votre choix : ")

            if choix == "0":
                break
menu()


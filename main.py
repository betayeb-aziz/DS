# ============================================
# APPLICATION PYTHON DE GESTION DES TACHES
# Licence 1 - Outils collaboratifs : Git / GitHub
# ============================================

def afficher_menu():
    """Affiche le menu principal."""
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


def ajouter_tache(taches):
    """Demande un titre et l'ajoute si la saisie n'est pas vide."""
    titre = input("Titre de la tâche : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches(taches):
    """Affiche toutes les tâches avec leur numéro."""
    if len(taches) == 0:
        print("Aucune tâche enregistrée.")
    else:
        print("\n--- LISTE DES TACHES ---")
        for numero, titre in enumerate(taches, start=1):
            print(f"{numero}. {titre}")


def rechercher_tache(taches):
    """Recherche les tâches contenant le mot-clé saisi."""
    mot_cle = input("Mot-clé à rechercher : ").strip()

    if mot_cle == "":
        print("Erreur : veuillez saisir un mot-clé.")
        return

    resultats = []
    for numero, titre in enumerate(taches, start=1):
        if mot_cle.lower() in titre.lower():
            resultats.append((numero, titre))

    if len(resultats) == 0:
        print("Aucune tâche ne correspond à votre recherche.")
    else:
        print("\n--- RESULTATS DE LA RECHERCHE ---")
        for numero, titre in resultats:
            print(f"{numero}. {titre}")


def main():
    """Point d'entrée du programme."""
    taches = []

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            rechercher_tache(taches)
        elif choix == "0":
            print("Merci d'avoir utilisé l'application. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()
print("all it's ok")

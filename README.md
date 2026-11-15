# Application Python de gestion des tâches

## Présentation
Ce projet est une application simple en Python qui permet de gérer une liste de tâches quotidiennes depuis la console.

## Fonctionnalités
- **Ajouter une tâche :** saisir un titre. Une saisie vide est refusée.
- **Afficher les tâches :** afficher toutes les tâches avec leur numéro. Un message apparaît si la liste est vide.
- **Rechercher une tâche :** rechercher un mot-clé dans les titres, sans distinction entre majuscules et minuscules.
- **Quitter :** fermer proprement le programme.
- Toute option autre que `1`, `2`, `3` ou `0` affiche un message d'erreur.

## Fichiers
- `main.py` : code source de l'application.
- `README.md` : documentation du projet.

## Prérequis
- Python 3 installé.
- Visual Studio Code (recommandé).

## Exécution
1. Ouvrir le dossier du projet dans Visual Studio Code.
2. Ouvrir le fichier `main.py`.
3. Cliquer sur **Run Python File** (Exécuter le fichier Python).
4. Utiliser le menu affiché dans le terminal.

Ou, depuis un terminal ouvert dans le dossier du projet :
```bash
python main.py
```

## Étapes de réalisation
1. Création du fichier `main.py` et du menu principal.
2. Ajout de la fonctionnalité d'ajout et de validation du titre.
3. Ajout de l'affichage et de la recherche des tâches.
4. Rédaction de la documentation dans `README.md`.
5. Initialisation du dépôt Git, création de commits, puis publication sur GitHub.

## Limite de cette première version
Les tâches sont conservées uniquement pendant l'exécution du programme. Elles ne sont pas enregistrées dans un fichier ou une base de données, conformément au périmètre simple de cette première partie.

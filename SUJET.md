# Backend-course

Cours de développement backend via Python et [FastAPI](https://fastapi.tiangolo.com/).

## Sommaire

1. [Préparer son environnement de développement](#préparer-son-environnement-de-développement)
2. [Consignes projet](#consignes-projet)
    - [Objet](#objet)
    - [Règles métier](#règles-métier)
    - [Règles techniques](#règles-techniques)
    - [Qualités appréciées - Bonus](#qualités-appréciées---bonus)


## Préparer son environnement de développement
x
> Testé avec Python 3.10 et FastAPI 0.115

- [Installer Python](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Créer un fork du projet](https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
- Ouvrir le projet dans votre éditeur préféré.
- [Créer un environnement virtuel Python](https://docs.python.org/3/tutorial/venv.html)
    ```bash
    # Exemple via bash
    cd <chemin/vers/dossier/du/projet/>

    # Le dossier contenant l'environnement virtuel sera nommé "env"
    python3 -m venv env

    # On active l'environnement virtuel
    
    ## Windows
    env\Scripts\activate
    
    ## GNU/Linux
    . env/bin/activate
    ```
- [(OPTIONNEL) VSCode - Définir l'environnement d'exécution](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters)
- Installer les [dépendances du projet](requirements.txt)
    > Ces dépendances doivent être renseignées au fur et à mesure dans le fichier requirements.txt.
    ```bash
    python3 -m pip install -r requirements.txt
    ```
- Valider le fonctionnement via le fichier test [checkenv.py](src/tests/checkenv.py).
    ```bash
    python3 -m fastapi dev src/tests/checkenv.py
    #  FastAPI   Starting development server 🚀
    #  ...
    #  server   Server started at http://127.0.0.1:8000
    #  ...
    ```

## Consignes projet

### Objet

Concevoir et réaliser le code `backend` permettant de gérer un `planning étudiant`.

### Organisation

- Travail de groupes par 3 ou 4 étudiants.
- Travail de chaque étudiant identifiable (vous devriez vous appuyer sur `git`)
- A la fin de chaque session de travail en autonomie, les étudiants envoient un compte rendu succint : travail réalisé, travail qui sera ensuite réalisé, difficultés rencontrées/questions (3-4 max).

### Règles métier

1. Organisation du planning

    - Chaque promotion a son propre emploi du temps.
    - Le planning est organisé sur *une seule semaine* (du Lundi au Vendredi).
    - Les cours sont programmés entre 08h15 et 17h15.

2. Créneaux horaires

    - Un cours a une durée variable (de 30 minutes à 4 heures maximum).
    - **BONUS** : Une promotion ne peut pas avoir deux cours au même moment.
    - **BONUS** : Une salle ne peut accueillir qu’un seul cours à la fois.

3. Gestion des cours
    
    - Chaque cours a un intitulé, un enseignant, une salle et une promotion concernée.
    - Certains cours nécessitent une salle spécifique (ex : Fablab).
    - Un cours peut être en autonomie ou dirigé par un enseignant.
    - Un cours peut être annulé ou modifié.

4. Disponibilité des salles

    - Une salle ne peut être utilisée que si elle est disponible sur le créneau demandé.

5. Consultation

    - N'importe qui doit pouvoir consulter l'emploi du temps pour une semaine donnée ou une date donnée.

6. Mise à jour du planning

    - Seul un utilisateur autorisé peut éditer le planning.

### Règles techniques

- Chaque étudiant travaillera sur son fork du projet (accessible par l'enseignant).
- Langage de programmation : Python 3.10+.
- Code versionné sur Gitlab ou Github (ou autre après consultation).
    - Aucun secret stocké en clair !
- Framework API : FastAPI.
- Base de données : PostgreSQL ou MariaDB (SQLAlchemy peut être utilisé comme interface Python).
    > Conseil : Vous pouvez réaliser le projet SANS base de données dans un 1er temps pour construire le code métier+API puis implémenter le stockage de données.
- Code source utilisé en production enregistré sous `src/main/`.
- **Tests** enregistrés sous `src/tests/`.
- L'IA générative peut vous assister, pas vous remplacer.
- Il doit être possible d'exécuter le projet en local.
- [Flake8](https://flake8.pycqa.org/en/latest/) sera utilisé pour le `lint` du code source.
- [Pytest](http://docs.pytest.org/en/stable/) ou [unittest](https://docs.python.org/3/library/unittest.html) peuvent être utilisés pour tester le code source.
- [Coverage](https://coverage.readthedocs.io/en/7.6.12/) sera utilisé pour mesurer la couverture du code par les tests.
- [Bandit](https://bandit.readthedocs.io/en/latest/) sera utilisé pour identifier des vulnérabilités communes dans le code source.

### Qualités appréciées - Bonus

- Chaque *point de terminaison API* est orienté **métier** pas **base de données**.
- Le `Swagger/OpenAPI` généré par FastAPI est bien documenté.
- Les modification du code apportées par chaque version sont compréhensibles et peuvent être suivies.
- Le code source est clair et maintenable.
- Le code métier est séparé des intégrations techniques (Exemple : la gestion de la base de données).
- Le code métier est couvert par des tests unitaires.
- Les intégrations techniques sont couvertes par des tests d'intégrations.
- Le fonctionnement global est vérifié par `Github actions` ou `Gitlab CI`.
- Des journaux, `logs`, permettent de suivre le fonctionnement de l'application et comprendre les erreurs.
- La documentation permet à un profil développeur de contribuer au projet.
- La documentation permet à un profil développeur d'instancier le projet.

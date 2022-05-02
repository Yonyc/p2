===================================
 PROJET 2 - VINCENT - GROUPE 3
===================================

-----------------------------------------------------------------
Installation et prérequis
----------------------------------------------------------------

Si vous souhaitez pouvoir accéder au site web, vous devez posséder
le module python Flask sur votre ordinateur. Si vous ne l'avez pas,
veuillez suivre les instructions:

- Ouvrez une invite de commande.
- Installer le module avec la commande suivante: 
pip install flask
ou
python3 -m pip install flask

-----------------------------------------------------------------
Exécution du serveur flask
----------------------------------------------------------------

Lorsque Flask est installé vous disposez de deux moyens pour
exécuter le serveur flask et accéder au site web:

- Exécutez avec python le fichier 'app.py'.
OU
- Utilisez la commande suivante:
flask run

-----------------------------------------------------------------
Affichage du site web
----------------------------------------------------------------

Rendez-vous à l'adresse indiqué sur le terminal, normalement 
il s'agit de l'adresse suivante:

http://127.0.0.1:5000
OU
http://127.0.0.1:5000/auth

-----------------------------------------------------------------
Information sur le programme et arborescence
-----------------------------------------------------------------

Le fichier 'app.py' vous permet d'exécuter le serveur et s'occupe
d'initialiser l'application.

Le fichier 'auth.py' permet de gérer l'accès aux pages et contient
toutes les requêtes SQL commentés.

Le dossier 'db' contient toutes les requêtes permettant de former
la base de données et 'instance' contient le fichier sqlite.

Le dossier 'static' contient le fichier CSS qui gère l'aspect visuel
du site web.

Le dossier 'templates' contient les fichiers html qui affiche les
pages web.

---------------

- La page 'Diversité des genres' vous montre un graphique qui compare
le nombre total de femelles et de mâles.

- La page 'Complications' vous montre un graphique qui compare
toutes les complications et vous montre donc celles qui sont
les plus récurrentes

- La page 'Graphiques' vous propose une interface et vous permet
de former les graphiques des consignes du projet.

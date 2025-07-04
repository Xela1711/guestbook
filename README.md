# guestbook
Code du projet de conteneurisation docker

 Dans ce projet nous utilisons plusieurs conteneurs (2) pour séparer le front, le back et la base de donnée.

 On a :
    - un conteneur backend (API, python)
    - un conteneur frontend (appli web statique hébergée par nginx)
    - un conteneur db permettant d'initialiser la base de donnée.

Il y a un réseau bridge pour le guestbook nommé guestbook-net, il permet :

    - Au backend d’accéder à la base de données via le nom de service db du docker compose
    - Au frontend de communiquer avec le backend via le nom de service backend du docker compose
    - D’isoler la communication entre les conteneurs du projet, sans exposer la base de données à l’extérieur


Nous avons créé un volume docker "db_data" pour faire persister les données de la base de données du conteneur comme ça, si le conteneur est supprimé ou ne foncitonne plus, les données précieuses de la base de donnée seront toujours présentes dans ce volume qui pourra être remonté.

De plus, le fichier d’initialisation init_db.sql est monté en lecture seule dans le conteneur pour initialiser la base lors du premier démarrage.


Pour résumer, nous avons les conteneurs qui communiquent via le réseau guestbook-net et fait persister les données dans un volume monté nommé "db_data".

Pour pouvoir démarrer l'application avec docker:

1. installer docker.io et docker-compose sur linux ou télécharger Docker desktop sur windows
2. cloner le dépot : git clone https://github.com/Xela1711/guestbook.git puis cd guestbook
3. Ensuite a la racine du dossier guestbook, "docker-compose up -d"
4. Enfin, accéder à l'application sur http://localhost/
5. Une fois l'utilisation finie, "docker-compose down"

Pour tester la persistance des données :
   docker-compose stop db
   docker-compose rm -f db

Pour supprimer le conteneur de la db
   docker-compose up -d db
Pour relancer le conteneur et voir que les éléments de la base de donées sont bien toujours présents


Lien du DockerHUB : https://hub.docker.com/repositories/xela17

Lien du repo GIT contenant le code : https://github.com/Xela1711/guestbook
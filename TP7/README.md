## Construire une image depuis un Dockerfile

On souhaite créer une image permettant d'installer un serveur Flask python avec une base de données redis volatile.

Pour se faire, nous avons besoin :

* D'une machine `redis`

* D'un server `front`:
  * d'une source centos 7
  * de déclarer le dépôt `epel-release`
  * d'installer PIP (package python-pip)
  * d'installer les packages pythons suivants : redis, flask
  * exposer le port 5000 sur le port 80 de l'hôte
  * utiliser le code *server.py* pour exécuter le serveur
  * lié avec la machine redis via le réseau

* Depuis l'hôte, appelé la commande `curl localhost:80` plusieurs fois

* Détruire et redémarrer le conteneur `front` :
  ```bash
  docker rm --force front
  docker run ...
  ```
  * Que se passe t'il ?
* Se connecter dans le conteneur front `docker exec -it front bash`
  * Commenter le fichier */etc/hosts*
  * D'où vient ce fichier ?
* Sur l'hôte :
  * Rechercher le réseau docker créé `docker network ls`
  * Commenter la sortie de la commande `docker network inspect 012345`

* Détruire tous les conteneurs, refaire la manipulation en créan au préalable le réseau avec la commande `docker network create -d bridge --opt encrypted my_server_bridge`
* Commenter la sortie des commandes
  * `docker network inspect my_server_bridge`
  * `brctl show`

## Construire une image depuis un Dockerfile

On souhaite créer une image permettant d'installer un serveur Flask python.

Pour se faire, nous avons besoin :

* d'une source centos 7
* de déclarer le dépôt `epel-release`
* d'installer PIP (package python-pip)
* d'installer les packages pythons suivants : redis, flask
* exposer le port 5000
* utiliser le code *server.py* pour exécuter le serveur

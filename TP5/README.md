## Construire une image depuis un Dockerfile

On souhaite créer une image permettant d'installer un serveur Flask python.

Pour se faire, nous avons besoin :

* d'une source centos 7
* de déclarer le dépôt `epel-release`
* d'installer PIP (package python-pip)
* d'installer les packages pythons suivants : flask
* exposer le port 5000
* utiliser le code *server.py* pour exécuter le serveur

Une fois le Dockerfile prêt :

* Construire l'image avec la commande `docker image build -t my_server .`
* Exécuter l'image `docker run -p 5000 my_server`
* Depuis l'hôte, appelé la commande `curl localhost:5000` plusieurs fois
* Faire un `docker container restart`
* Rappelé la commande `curl localhost:5000`

## Construire une image depuis un Dockerfile

On souhaite créer une image permettant d'installer un serveur Flask python.

Pour se faire, nous avons besoin :

* d'une source centos 7
* de déclarer le dépôt `epel-release`
* d'installer PIP (package python-pip)
* d'installer les packages pythons suivants : redis, flask
* exposer le port 5000
* utiliser le code *server.py* pour exécuter le serveur


## Solution

```Dockerfile
FROM centos:7
MAINTAINER nelson.goncalves@thalesgroup.com

ADD src /src
RUN yum install epel-release
RUN yum intstall python-pip
RUN pip install redis flask

EXPOSE 5000

CMD python /src/server.py
```

* Exécuter le conteneur en mode intéractif `docker container run -it centos:7`
Depuis un autre terminal:
  * Copier le contenu du fichier *src/server_v1.py* dans un fichier *server.py* de l'hôte
  * Copier le fichier dans le conteneur `docker cp server.py 0123456789abcdef:server.py`
* Installer les dépendances nécessaires dans le conteneur :
  ```bash
  yum install epel-release
  yum install python-pip
  pip install redis flask
  ```
* Exécuter le serveur `python server.py`
* Essayer d'atteindre l'url [http://0.0.0.0:5000/]
  * Pourquoi cela ne fonctionne pas

* Quitter le conteneur
* Appliquer un tag `docker container commit 0123456789abcdef my_server`
* Exécuter la nouvelle image avec l'exposition du port et la commande `docker container run -it -p 5000:5000 my_server python server.py`

## Intéragir avec le conteneur

* Exécuter le conteneur avec `docker container run -d my_centos bash`
* Depuis un autre terminal, déterminer l'id du conteneur avec `docker ps`
* Afficher les logs `docker container logs 0123456789abcdef --follow` (équivalent à une `tail -f`)
* Dans le conteneur, exécuter la commande `echo "docker"`
  * Que se passe t'il dans le terminal affichant les logs ?
* Dans un autre terminal, exécuter la commande `docker container exec 0123456789abcdef ifconfig`

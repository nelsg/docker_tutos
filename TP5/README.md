## Construire une image depuis un Dockerfile

On souhaite créer une image permettant d'installer un serveur Flask python.

Pour se faire, nous avons besoin :

* d'une source centos 7
* de déclarer le dépôt `epel-release`
* d'installer PIP (package python-pip)
* d'installer les packages pythons suivants : flask
* exposer le port 5000
* utiliser le code *server.py* pour exécuter le serveur

* Construire l'image avec la commande `docker image build -t my_server .`
* Exécuter l'image `docker run -p 5000 my_server`
* Se rendre sur l'URL [http://10.10.0.201:5000/] et recharger la page plusieurs fois

## Solution

```Dockerfile
FROM centos:7
MAINTAINER nelson.goncalves@thalesgroup.com

RUN yum install -y epel-release
RUN yum install -y python-pip
RUN pip install flask
ADD src /src

EXPOSE 5000

CMD python /src/server.py
```
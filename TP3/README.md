# Créer ses conteneurs

## Pull d'une image

* Téléchargez une image alpine avec la commande `docker pull centos:7`

* Que pouvez vous dire sur cette image avec :
  * `docker image ls` ?
  * `docker image inspect centos:7` ?
  * `docker image history centos:7` ?

## Exécution d'un conteneur

* Exécutez le conteneur avec la commande `docker container run -it centos:7`
* Afficher la configuration réseau `ifconfig`
* Installer le package `yum install net-tools`
* Quittez le conteneur Ctrl+D
* Exécutez le conteneur avec la commande `docker container run -it centos:7`
* Afficher la configuration réseau `ifconfig`
  * Que se passe t'il ?

## Intéragir avec le conteneur

* Exécuter le conteneur avec `docker container run -d centos:7 bash`
* Depuis un autre terminal, déterminer l'id du conteneur avec `docker ps`
* Afficher les logs `docker container logs 0123456789abcdef --follow` (équivalent à une `tail -f`)
* Dans le conteneur, exécuter la commande `echo "docker"`
  * Que se passe t'il dans le terminal affichant les logs ?
* Dans un autre terminal, exécuter les commandes :
  * `yum install net-tools`
  * `docker container exec 0123456789abcdef ifconfig`

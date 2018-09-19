# Créer une image

* Rechercher la premier instance du conteneur avec ifconfig `docker container ps -a`
* Appliquer un tag `docker container commit 0123456789abcdef my_centos`
* Exécuter le conteneur en mode intéractif `docker container run -it my_centos bash`
* Dans le conteneur, que pouvez-vous dire du retour des commandes suivantes :
  * `ifconfig` ?
  * `mount` ?
  * `hostname` ?
* Exécuter le conteneur en mode détaché `docker container run -d my_centos sleep 300`
* Que pouvez-vous dire du retour des commandes suivantes sur l'hôte :
  * `ifconfig` ?
  * `mount` ?
  * `hostname` ?
  * `brctl show docker0` ?
  * `route` ?

## Intéragir avec le conteneur

* Exécuter le conteneur avec `docker container run -d my_centos bash`
* Depuis un autre terminal, déterminer l'id du conteneur avec `docker ps`
* Afficher les logs `docker container logs 0123456789abcdef --follow` (équivalent à une `tail -f`)
* Dans le conteneur, exécuter la commande `echo "docker"`
  * Que se passe t'il dans le terminal affichant les logs ?
* Dans un autre terminal, exécuter la commande `docker container exec 0123456789abcdef ifconfig`

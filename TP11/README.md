# Swarm

## Déployer la stack

Récupérer le fichier `docker-compose.yml` du TP9
* Déclarer une stack : `docker stack deploy --compose-file=docker-compose.yml my_server`
* Corriger le fichier *docker-compose.yml* pour résoudre le problème
* Que retourne la commande `docker image ls` sur `docker2` et `docker3` ?

* Supprimer l'ancienne stack `docker stack rm my_server`
* La recréer `docker stack deploy --compose-file=docker-compose.yml my_server`
* Ou se trouve le conteneur utilisant l'image *10.10.0.201:5000/my_server* ?
* Sur les autres hosts, que retourne les commandes :
  * `netstat -natup | grep LISTEN` ?
  * `curl 10.10.0.201:80`, `curl 10.10.0.202:80`, `curl 10.10.0.203:80` ?

* Augmenter le nombre de réplicats `docker service scale my_server_front=5`
* Que retourne `curl 10.10.0.201:80` ?
* Augmenter le nombre de réplicats à 50

## Mise en place d'un répertoire partagé

Installer un serveur NFS sur `docker1`

* Sur `docker1`, installer le package `nfs-utils` et le configurer
* Sur toutes les VM, configurer le client NFS

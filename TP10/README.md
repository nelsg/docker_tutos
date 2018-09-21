# Configurer swarm

* Installer docker sur les machines `docker2` et `docker3` : `./install_docker.sh`
* Se reconnecter sur `docker2` et `docker3`

* Configurer swarm :
  * sur `docker1` : `docker swarm init --advertise-addr=10.10.0.201`
  * pour récupérer le token d'un worker : `docker swarm join-token worker`
  * pour récupérer le token d'un manager : `docker swarm join-token manager`
  * configurer swarm en worker sur `docker2`
  * configurer swarm en manager sur `docker3`

* Commenter la sortie des commandes :
  * `docker node ls`
  * `docker info`
  * `docker node inspect <node_id>`

* Déclarer une stack : `docker stack deploy --compose-file=docker-compose.yml my_server`
* Corriger le fichier *docker-compose.yml* pour résoudre le problème
* Que retourne la commande `docker image ls` sur `docker2` et `docker3` ?
* Sur `docker1`, que retourne la commande `docker service ps my_server_front` ?
* Quel est le problème et comment le résoudre proprement ?

* Pour instancier une regsitry : `docker run -d -p 5000:5000 --restart=always --name registry registry:2.5.2`
* Pour tagguer une image avec l'IP : `docker tag my_server 10.10.0.201:5000/my_server`
* Pour déclarer une registry *insecure*, ajouter dans le fichier */etc/docker/daemon.json* :
  ```json
  {
    "insecure-registries" : ["10.10.0.201:5000"]
  }
  ```
* Pour redémarrer docker : `sudo service docker restart`
* Pousser l'image *10.10.0.201:5000/my_server* sur la registry
* Modifier le fichier *docker-compose.yml* pour prendre en compte cette image

* Supprimer l'ancienne stack `docker stack rm my_server`
* La recréer `docker stack deploy --compose-file=docker-compose.yml my_server`
* Ou se trouve le conteneur utilisant l'image *10.10.0.201:5000/my_server* ?
* Sur les autres hosts, que retourne les commandes :
  * `netstat -natup | grep LISTEN` ?
  * `curl 10.10.0.201:80`, `curl 10.10.0.202:80`, `curl 10.10.0.203:80` ?

* Augmenter le nombre de réplicats `docker service scale my_server_front=5`
* Que retourne `curl 10.10.0.201:80` ?

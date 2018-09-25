# Swarm

## Installer et configurer Swarm

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

## Déployer des services

* Supprimer tous les conteneurs des exercices précédent
* Recréer les services du TP9 avec la commande `docker service`

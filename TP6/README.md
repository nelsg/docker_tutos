# Installer une registry privée

Consulter la page [https://hub.docker.com/_/registry/]

* Instancier la registry `docker run -d -p 5000:5000 --restart=always --name registry registry:2.5.2`
* A quoi sert `--restart=always` ?
* A quoi sert `--name registry` ?
* Tagguer l'image `docker image tag my_server localhost:5000/my_server`
* Que retourne `docker image ls` ?
* Pousser l'image `docker image push localhost:5000/my_server`
* Entrer dans le conteneur du registry `docker exec -it registry sh`
  * Que contient le répertoire */var/lib/registry* `find /var/lib/registry` ?

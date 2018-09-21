## Construire une image sans root depuis un Dockerfile

* Reprendre l'exercice du TP5 et utiliser le script *startup* pour démarrer le serveur :
  * Construire l'image : `docker image build -t my_server_sec .`
  * Exécuter le conteneur : `docker run --name my_server_sec -d my_server_sec`
  * Afficher les processus : `docker container top my_server_sec`
  * Supprimer le conteneur : `docker rm --force my_server_sec`

L'objectif est de supprimer tous les processus *root* retournées par la commande `docker container top my_server_sec`

Etape 1 :
* Créer un groupe *my_server* avec le gid *991* dans le conteneur s'il n'existe pas déjà : `groupadd --gid 991 my_server`
* Créer un utilisateur *my_server* avec l'uid *991* dans le conteneur s'il n'existe pas déjà : `useradd --system --no-create-home --shell /bin/bash --gid 991 --uid 991 my_server`
* Changer les droits d'un répertoire avec `chown -R my_server:my_server <rep>`
* Démarrer le processus avec la commande `su - my_server -c "<commande>"`
* Reconstruire l'image et le conteneur, que retourne `docker container top my_server_sec` ?

Etape 2 :
* Mettre en place `chroot` : `chroot --userspec=<user> / <cmd>`
* Reconstruire l'image et le conteneur, que retourne `docker container top my_server_sec` ?

Etape 3 :
* mettre en place `exec` : `exec <cmd>`
* Reconstruire l'image et le conteneur, que retourne `docker container top my_server_sec` ?

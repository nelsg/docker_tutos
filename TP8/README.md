## Mise en oeuvre d'un volume

**Note**
* pour activer la persistence de l'image `redis`, il faut créer le conteneur avec la commande `redis-server --appendonly yes`
* Les données sont stockées dans le répertoire */data* du conteneur

**Montage répertoire** :

* Recréer, si nécessaire, les deux conteneurs du TP7 en activant la persistence du conteneur redis
* Appeler la commande `curl localhost:80` plusieurs fois
* Se connecter dans le conteneur redis et vérifier que le répertoire */data* contient bien des données

* Recréer le conteneur *redis* en montant un répertoire de l'hôte dans le conteneur
* Appeler la commande `curl localhost:80` plusieurs fois
* Détruire/Recréer le conteneur *redis*, vérifier que le compteur a sauvegardé sont état

**Montage volume implicite** :

* Refaire la même manipulation que précédemment et montant un volume de manière explicite.
* Où se trouvent les données (`docker volume ls` puis `docker volume inspect ...`)

**Création volume** :

* Refaire la même manipulation en créant vous-même un volume avec la commande `docker volume create`

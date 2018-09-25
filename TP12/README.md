## Sécuriser redis

* Utiliser le fichier */etc/redis/redis.conf* pour définir un mot de passe
* Enregistrer le mot de passe dans les secrets

## Déployer portainer

Portainer est un outil d'administration docker relativement simple.

* Déployer portainer avec la commande suivante :
  ```bash
  docker volume create portainer_data
  docker run -d -p 9000:9000 \
      --name portainer --restart always \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v portainer_data:/data \
      portainer/portainer
  ```
* Ecrire un docker-file pour exécuter votre portainer
* Se rendre à l'URL [10.10.0.201:9000]

## Déployer Gogs

Nous utiliserons l’application Gogs comme démonstrateur. Gogs est un serveur Git écrit en Go.
L’application se compose du serveur lui même ainsi que d’une base de données. Ces deux parties seront déployées par Docker Compose.

* Utiliser les images `gogs/gogs:0.10.18` (https://hub.docker.com/r/gogs/gogs/) et `mysql` (https://hub.docker.com/_/mysql/) pour créer un docker-compose.yml:
  * gogs :
    * Ecoute sur les ports 3000 et 10022
    * A un volume pour stocker les dépôts git
  * mysql :
    * Créé une base de données `gogs`
    * Mot de passe de la base de données : `password`
* Une fois déployé, se rendre sur la page d'administration :
  * Sur quelle adresse se trouve votre container MySQL ?
  * Quel est le password root de la base de données ?
* Créer un repository et ajoutez y un fichier quelconque. Nous souhaitons simplement tester la persistance des données.
  * `docker-compose stop` `docker-compose rm -f`
  * Vérifiez que les volumes sont toujours présents sur le système
  * Vérifiez que vous avez bien perdu l’accès à l’application
* Relancer l'application `docker-compose up -d`
  * Vérifiez que vous avez récupéré l’accès à l’application
  * Vérifiez que les données que vous y aviez mis y sont toujours

* Le serveur est en version 0.10.18, une version plus récente est disponible. La mettre en place.

## Traefik scaling

Nous utiliserons l’image hello-world de Docker comme démonstrateur. Elle permet d’afficher très simplement l’ID du conteneur sur lequel on se trouve. On pourra de cette façon observer simplement le scaling et le loadbalancing de notre service.

Créer un répertoire pour ce TP

Traefik à besoin d'un fichier de configuration `traefik.toml` que voici, le mettre dans le répertoire

```
defaultEntryPoints = ["http"]
logLevel = "DEBUG"
[entryPoints]
  [entryPoints.http]
  address = ":80"
[docker]
domain = "docker"
endpoint = "unix:///var/run/docker.sock"
watch = true
```

Utiliser le docker-compose.yml de base suivant :

```yaml
version: '2'
services:
  traefik:
    image: traefik:camembert-alpine
    restart: always
    command: --web
    container_name: traefik
  webapp:
    image: dockercloud/hello-world
```

* Le modifier avec :
  * un réseau dédié
  * pour traefik :
    * Monter le fichier de configuration de traefik
    * Monter la socket docker
    * Exposer les ports 80 et 8080
    * Utiliser le réseau créé
  * pour hello-world :
    * Avoir un label `traefik.port` avec comme valeur 80
    * Avoir un label `traefik.backend` avec comme valeur "webapp"
    * Avoir un label `traefik.frontend.rule` avec comme valeur "Host:webapp.domain.tld"
    * Utiliser le réseau créé

* Vérifier avec le curl : `curl -H “Host:tsp-webapp” localhost` (à corriger)
* Faire démarrer 5 conteneurs de type hello-world avec la fonction scale de docker-compose

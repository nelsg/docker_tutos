## Mise en oeuvre de docker-compose

* Installer *docker-compose* : `sudo pip install docker-compose`
* Vérifier la version `docker-compose --version`
* Créer un fichier docker-compose.yml pour recréer redis et le front
  * Prendre en compte le réseau et le volume tel que décrit dans le TP7 et 8
  * Penser a supprimer les conteneurs, volumes et réseaux existants
* Exécuter la commande `docker-compose up`

Template de fichier docker-compose.yml

```yaml
version: "2"
services:
  my_service:
volumes:
  my_volume:
networks:
  my_network:
```

* Commenter les networks, volumes ?
* Exécuter la commande `docker-compose scale front=2`, que se passe t'il ?

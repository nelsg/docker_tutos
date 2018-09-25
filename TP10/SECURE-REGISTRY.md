* Pour instancier une regitry : `docker run -d -p 5000:5000 --restart=always --name registry registry:2.5.2`
* Pour déclarer une registry *insecure*, ajouter dans le fichier */etc/docker/daemon.json* :
  ```json
  {
    "insecure-registries" : ["10.10.0.201:5000"]
  }
  ```
* Pour redémarrer docker : `sudo service docker restart`

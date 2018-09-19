# Installation de docker

## Prérequis

```bash
# Désinstaller les anciennes versions
sudo apt-get remove docker docker-engine docker.io
# Installation des prérequis
sudo apt-get update
sudo apt-get install \
          apt-transport-https \
          ca-certificates \
          curl \
				  software-properties-common \
          aufs-tools
# Ajout de la clé du dépôt officiel de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Vérifier l’empreinte
sudo apt-key fingerprint 0EBFCD88
# Ajouter le dépôt
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable"
```

## Installation de Docker

```bash
# Installation du package docker-ce
sudo apt-get update
sudo apt-get install docker-ce
# On ajoute notre utilisateur au groupe docker
sudo usermod -aG docker vagrant
# Rouvrir le terminal
```

Décrivez ce qui se passe avec la commande `docker run hello-world` ?

Commenter la sortie des commandes suivantes :
  * `docker version`
  * `docker info`

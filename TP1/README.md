# Exercice autour des Namespaces

## Afficher les namespaces des processus

* Rechercher un processus à analyser avec `ps aux`
* Que retourne la commande `ls -al /proc/123/ns` ?

## Namespace UTS

* Que retourne la commande `uname -n` ?
* Exécuter les commandes suivantes :
  ```bash
  sudo unshare -u /bin/bash
  hostname
  hostname ubuntu-ns1
  ```
* Que retourne la commande `uname -n` ?
* Que retourne la commande `uname -n` sur un autre terminal ?

## Namespace MNT

* Créer un point de montage mémoire :
  ```bash
  sudo mkdir /mnt/ramdisk
  sudo mount -t tmpfs -o size=1m tmpfs /mnt/ramdisk
  ```
* Que retourne la commande `mount` ?
* Exécutez les commandes suivantes :
  ```bash
  sudo unshare -m /bin/bash
  sudo umount /mnt/ramdisk
  ```
* Que retourne la commande `mount` ?
* Que retourne la commande `mount` sur un autre terminal ?

## Namespace NET

> Un namespace réseau est une copie de la pile protocolaire, incluant tous les services réseau

* Créez un namespace réseau `sudo ip netns add ns1`
  * Regarder */var/run/netns/ns1*
  * Que retourne la commande `mount` ?
* Lister les netns : `sudo ip netns list`
* Lister les PIDs d'un netns : `sudo ip netns pids ns1`
* Trouver le netns d'un processus : `sudo ip netns identify 123`
* Surveiller : `sudo ip netns monitor`
* Exécuter un processus dans un netns : `sudo ip netns exec ns1 ifconfig -a`
* Supprimer le namespace réseau `sudo ip netns del ns1`

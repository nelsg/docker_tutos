# Namespaces

## Afficher les namespaces des processus

* Rechercher un processus à analiser avec `ps aux`

* Que retourne la commande `ls -al /proc/123/ns` ?

## Namespace UTS

* Que retourne la commande `uname -u` ?

* Exécutez les commandes suivantes :

```bash
sudo unshare -u /bin/bash
hostname
hostname ubuntu-ns1
```

* Que retourne la commande `uname -u` ?

* Que retourne la commande `uname -u` sur un autre terminal ?

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

* Listez les netns : `sudo ip netns list`

* Listez les PIDs d'un netns : `sudo ip netns pids ns1`

* Trouvez le netns d'un processus : `sudo ip netns identify 123`

* Surveiller : `sudo ip netns monitor`

* Exécuter un processus dans un netns : `sudo ip netns exec ns1 ifconfig -a`

* Supprimez le namespace réseau `sudo ip netns del ns1`

# Utilisation des CGroups

## Utilisation de `nice`

La commande `stress` permet de stresser une machine, petit exemple :

```bash
sudo apt install stress
# Exécuter des commandes avec nice et sans
nice stress -c 1 &
stress -c 1 &
# Afficher l'utilisation CPU
htop
```

Sur une machine 1 CPU, un processus utilise 90%, l'autre utilise 10%.

## Utilisation des CGroups

Installation :

```bash
sudo apt install cgroup-bin
```

Création d'un groupe `foo` pour l'uid:gid vagrant:vagrant :

```bash
sudo cgcreate -a vagrant:vagrant -t vagrant:vagrant -g cpu:/foo
```

Lui affecter la priorité processeur la plus basse (c'est 1024 par défaut) :

```bash
cgset -r cpu.shares=2 foo
```

Exécuter :

```bash
cgexec -g cpu:foo stress -c 1
```

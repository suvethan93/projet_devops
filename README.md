#  Projet DevOps - (SDN)
**Déploiement d'une API FastAPI conteneurisée sur Infrastructure Virtualisée**

---

## Binôme
* **Suvethan** (@suvethan93)
* **Mattéo**

## Objectifs du Projet
L'objectif est de démontrer la maîtrise de la chaîne de déploiement moderne :
1. **Virtualisation** : Installation et configuration d'une VM Ubuntu via UTM.
2. **Réseau** : Configuration de l'accès distant via l'interface `enp0s1`.
3. **Conteneurisation** : Création d'une image Docker optimisée et sécurisée.
4. **Développement** : Création d'une API REST avec FastAPI.


##  Spécifications Techniques

| Composant | Technologie |
| :--- | :--- |
| **OS VM** | Ubuntu Server 24.04 (ARM64) |
| **Langage** | Python 3.13 |
| **Framework** | FastAPI + Uvicorn |
| **Conteneur** | Docker (Image non-root) |
| **Port** | 8080 |

## Sécurité & Optimisations
* **Sécurité** : Le conteneur ne tourne pas en `root`. Un utilisateur `app` dédié est utilisé.
* **Fiabilité** : Ajout d'un `HEALTHCHECK` Docker pour surveiller l'état de l'API.
* **Légèreté** : Utilisation d'un fichier `.dockerignore` pour exclure les fichiers inutiles.


## Guide de déploiement (Démo)

### 1. Build de l'image

sudo docker build -t mon-image1 .

### 2. Lancement du conteneur

sudo docker run -it --rm -p 8080:8080 mon-image1

### 3. Accès à l'API

Accueil : http://192.168.64.5:8080/

Infos : http://192.168.64.5:8080/info

Documentation interactive : http://192.168.64.5:8080/docs





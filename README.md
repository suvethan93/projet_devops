# Projet DevOps & Conteneurisation 

### Étudiants
* Binôme : Vijayarajan Suvethan & Da Silva Mattéo

### Description du Projet
Déploiement d'une API FastAPI dans un conteneur Docker sur une VM Ubuntu (UTM).

### Configuration Technique
* **Image de base** : Python 3.13
* **Serveur** : Uvicorn
* **Sécurité** : Utilisateur `app` non-root créé dans le Dockerfile
* **Port** : 8080 (exposé sur l'interface réseau `enp0s1`)

### Commandes pour la Démo
1. **Build** : `sudo docker build -t mon-image .`
2. **Run** : `sudo docker run -it --rm -p 8080:8080 mon-image`
3. **Vérification IP** : `ip addr show`

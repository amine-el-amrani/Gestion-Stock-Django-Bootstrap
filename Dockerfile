# Utilisation de l'image de base Python
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers requis dans le conteneur
COPY requirements.txt ./
COPY entrypoint.sh ./

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Donner les droits d'exécution au script d'entrée
RUN chmod +x entrypoint.sh

# Commande par défaut pour exécuter le script d'entrée
CMD ["./entrypoint.sh"]

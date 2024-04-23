# image de base
FROM python:3.10-slim

# le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des exigences dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

#Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5002

#Définir la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Lancer l'application Flask
CMD ["flask", "run", "--port=5002"]

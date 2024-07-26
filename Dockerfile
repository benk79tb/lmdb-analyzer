# Utilise l'image de base Python avec Alpine Linux
FROM python:3.10.13-alpine

# Met à jour les paquets et installe les dépendances nécessaires
RUN apk update && apk add bash build-base

# Définit /bin/bash comme shell par défaut
SHELL ["/bin/bash", "-c"]

# Copie les fichiers du projet dans le conteneur
COPY . /lmdb_analyzer
WORKDIR /lmdb_analyzer

# Installe les dépendances Python à partir de setup.py
RUN pip install --no-cache-dir .

# Définit le point d'entrée par défaut du conteneur
CMD [ "lmdb-analyzer" ]

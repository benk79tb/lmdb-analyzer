# LMDB Analyzer

LMDB Analyzer est une application Python qui permet d'analyser le contenu des bases de données LMDB et d'afficher les paires clé-valeur.

Sa conception a été réalisée à l'aide de chatGPT: https://chatgpt.com/share/61b5a1c0-1f79-42d3-85b6-12ffcb13db39

## Utilisation à partir de l'image docker

```bash
docker run -v ${PWD}/poc/data:/data -it benk79tb/lmdb_analyzer:1.0.2 lmdb-analyzer --deserialization bytes /data/ben/keri/db/ben
```

## Docker

Une image docker est disponible sous `benk79tb/lmdb_analyzer:1.0.2`


____________________________________________________________

### Installation d'une image

Pour installer l'image docker vous pouvez effectuer

### Créer et publier une image

### A partir du code


## Installation

Avec le bon environnement vous pouvez installer avec:

```bash
pip install .
```
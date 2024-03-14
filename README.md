# iu_LangDetect

`LangDetect IU` est une application web Flask qui offre une interface utilisateur pour détecter la langue d'un texte donné. L'application utilise un modèle de deep learning en backend pour identifier parmi plusieurs langues supportées. Cette solution est conçue pour être simple d'utilisation, avec une installation facile via Docker.

## Fonctionnalités

- Interface utilisateur simple pour soumettre du texte et afficher la langue détectée et le score de probabilité.
- Supporte plusieurs langues grâce à un modèle de deep learning robuste en backend.
- Configuration et déploiement aisés grâce à Docker.

## Prérequis

- Docker (pour le déploiement avec Docker).
- Python 3.10+ (pour une exécution locale sans Docker).

## Installation

### Avec Docker

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/LangDetectAPI/iu_langDetect.git
    cd iu_LangDetect
    ```

2. Construisez l'image Docker :

    ```bash
    docker build -t iu_langdetect .
    ```

3. Lancez un conteneur à partir de votre image :

    ```bash
    docker run -d -p 5002:5002 iu_langdetect
    ```

    L'application sera accessible à `http://localhost:5002`.

### Exécution Locale

1. Créez et activez un environnement virtuel :

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Sur Unix/Linux
    .venv\Scripts\activate  # Sur Windows
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

3. Lancez l'application :

    ```bash
    flask run --port=5002
    ```

    Visitez `http://localhost:5002` dans votre navigateur pour utiliser l'application.

## Utilisation

Après avoir lancé l'application, vous pouvez utiliser l'interface web pour soumettre du texte. La langue détectée et le score de probabilité s'afficheront en réponse.

## Développement

Pour contribuer à `iu_LangDetect`, veuillez forker le dépôt, créer une branche pour vos modifications et soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

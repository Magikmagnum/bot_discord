# Bot Discord

Ce bot Discord est conçu pour répondre à diverses commandes et réagir à certains messages.

## Fonctionnalités

- Réagit aux messages contenant "bonjour" ou "salut" en ajoutant l'emoji "👋".
- Dispose de plusieurs commandes :
  - `!ping`: Répond "pong 🏓".
  - `!touché`: Répond "coulé ! ⛵".
  - `!members`: Affiche la liste des membres du serveur.
  - `!joke`: Envoie une blague aléatoire parmi une liste prédéfinie.

## Installation

1. Cloner ce dépôt.
2. Installer les dépendances avec `pip install -r requirements.txt`.
3. Remplacer `"TOKEN_ICI"` par le token d'authentification de votre bot dans le fichier `bot.py`.
4. Exécuter le bot avec `python bot.py`.

## Configuration

- Le préfixe des commandes est `!`. Vous pouvez le modifier en modifiant la ligne `bot = commands.Bot(command_prefix="!", intents=intents)` dans le fichier `bot.py`.
- Vous pouvez personnaliser les blagues dans la liste `jokes` du fichier `bot.py`.
- La liste des mots interdits est définie dans la variable `banned_words` du fichier `bot.py`.

## Assurez-vous de remplacer "TOKEN_ICI" par le véritable token d'authentification de votre bot Discord.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

# Importation des modules nécessaires
import random
import discord
from discord.ext import commands

# Définition des intentions du bot
intents = discord.Intents().all()

# Création de l'instance du bot avec le préfixe de commande et les intentions spécifiées
bot = commands.Bot(command_prefix="!", intents=intents)

# Activation de la détection du contenu des messages
intents.message_content = True
# Activation de la détection des guildes (serveurs Discord)
intents.guilds = True
# Activation de la détection des membres
intents.members = True

# Fonction "on_ready" appelée lorsque le bot est prêt à interagir
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")  # Affichage d'un message de confirmation dans la console
    await bot.change_presence(activity=discord.Game(name="!help pour l'aide"))  # Définition du statut du bot

# Commande !ping qui répond "pong"
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande !touché qui répond "coulé ! ⛵"
@bot.command()
async def touché(ctx):
    await ctx.send("coulé ! ⛵")

# Commande !members qui affiche la liste des membres du serveur
@bot.command()
async def members(ctx):
    # Récupération des membres du serveur et de leurs rôles
    members_list = "\n".join([f"{member.display_name} - {', '.join([role.name for role in member.roles if role.name != '@everyone'])}" for member in ctx.guild.members])
    await ctx.send(f"Liste des membres sur le serveur :\n{members_list}")

# Réactions automatiques aux messages contenant "bonjour" ou "salut"
@bot.event
async def on_message(message):
    # Vérifie si le message a été envoyé par le bot lui-même
    if message.author == bot.user:
        return

    # Réagit avec un emoji aux messages contenant "bonjour" ou "salut"
    if "bonjour" in message.content.lower() or "salut" in message.content.lower():
        await message.add_reaction("👋")
        
    await bot.process_commands(message)  # Traitement des autres commandes

# Commande !joke qui envoie une blague aléatoire parmi une liste prédéfinie
jokes = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Quel est le comble pour un électricien ? De se faire électricienner.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Qu'est-ce qu'un poussin avec une mitraillette ? Un poulet tout à fait normal.",
    "Qu'est-ce qui est vert et qui pousse sous l'eau ? Un chou marin.",
    "Quel est le sport le plus silencieux ? Le parachutisme, parce qu'on n'entend pas un pet tomber !"
]

@bot.command()
async def joke(ctx):
    await ctx.send(random.choice(jokes))

# Événement déclenché lorsqu'un nouveau membre rejoint le serveur
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Récupère le canal système du serveur
    if channel:
        # Envoie un message de bienvenue avec une mention du nouveau membre et une invitation à utiliser !welcome
        await channel.send(f"Bienvenue {member.mention} sur le serveur ! Utilisez `!welcome` pour voir un message de bienvenue personnalisé.")

# Liste des mots ou expressions considérés comme injurieux



# Liste des mots ou expressions à surveiller d'apres wikipedia
banned_words = [
    # Les grands classiques
    "con", "conne", "connard", "connasse",
    "salaud", "salopard", "salope",
    "blaireau",
    "casse-couilles", "pète-couilles", "casse-ovaires",
    "pov' mec", "pov' type", "pov' fille",
    # Les atteintes à l'intellect
    "imbécile", "con", "conne",
    "débile", "débile congénital", "idiot", "idiote",
    "crétin", "crétine", "gourde", "gourdasse",
    "abruti", "abrutie", "cruche",
    "demeuré", "demeurée", "godiche",
    "andouille", "bécasse",
    "couillon", "couillonne", "blondasse",
    "glandu", "dinde", "pintade",
    "bougre d'âne", "âne bâté", "amibe",
    "cornichon", "béotien", "nigaud",
    # Les orduriers, nauséabonds et parasitaires
    "ordure", "charogne",
    "fumier", "vermine",
    "sac à merde", "tas de merde", "pov' merde", "cloporte",
    "crevure", "crevard", "parasite",
    "pourri", "pourriture", "mouche à merde",
    "merdeux", "merdeuse", "sangsue",
    "emmerdeur", "emmerdeuse", "raclure dégénérée",
    "chieur", "chieuse", "bernique",
    "morveux", "morveuse", "trou-du-cul",
    "pauvre tache", "pov' tache", "porc", "pourceau", "cochon", "cochonne",
    "saligaud", "larve",
    "pisseuse", "sagouin", "souillon",
    # Les atteintes à la virilité
    "enculé", "lopette",
    "couille-molle", "chochotte",
    "p'tite bite", "mauviette",
    "mou de la bite", "lavette",
    # Les atteintes à la dignité féminine
    "pouffiasse", "garce",
    "pétasse", "catin",
    "grognasse", "pute", "putain",
    "roulure", "chienne",
    "traînée", "trimardesse", "trimardeuse",
    "gourgandine", "sac-à-foutre", "garage-à-bite",
    "bougresse", "chagasse",
    "sorcière", "chaudasse",
    "diablesse", "allumeuse",
    "peste", "marie-couche-toi-là",
    "greluche",
    # Les atteintes au physique
    "laideron", "morue",
    "tronche-de-cake", "boudin",
    "tête de cul", "de fion", "etc", "thon",
    "face de rat", "de macaque", "etc", "cageot",
    "suce-debout", "gros tas",
    "nabot", "demi-portion",
    "minus", "foutriquet",
    # Les atteintes à l'honnêteté et au sérieux
    "canaille", "bouffon",
    "enflure", "guignol",
    "enfoiré", "enfoirée", "charlot",
    "scélérat", "minable",
    "crapule", "branquignol",
    "escroc", "mariolle",
    "fripouille", "mufle",
    "malotru", "goujat",
    "vaurien", "gougnafier",
    "loubard", "pimbêche",
    "faux-cul", "pignouf",
    "judas",
    # Les atteintes à l'intégrité sociale
    "bâtard", "bouseux",
    "corniaud", "plouc",
    "avorton", "cul-terreux",
    "misérable", "péquenaud",
    "loser", "tocard",
    # Le manque de volonté, de courage
    "feignasse", "trouillard",
    "branleur", "pleutre",
    "glandeur", "chiffe-molle",
    "mou-du-cul", "pétochard",
    "traîne-savates", "dégonflé",
    "jean-foutre", "poltron"
]


# Événement déclenché lorsqu'un message est envoyé sur le serveur
@bot.event
async def on_message(message):
    # Vérifie si l'auteur du message est un bot
    if message.author.bot:
        return

    # Vérifie si le message contient un mot interdit
    for word in banned_words:
        if word in message.content.lower():
            # Bannit l'utilisateur et envoie un message de notification
            await message.author.ban(reason="Utilisation d'une injure.")
            await message.channel.send(f"{message.author.mention} a été banni pour utilisation d'une injure.")
            break  # Sort de la boucle après le premier mot trouvé

    await bot.process_commands(message)  # Traitement des autres commandes

#connexion du bot au serveur avec au token
bot.run("Token_discorde")
         

import random
import discord #import du module
from discord.ext import commands


#Intents
intents = discord.Intents().all()

bot = commands.Bot(command_prefix="!", intents=intents)

intents.message_content = True
# guilds = serveurs discords
intents.guilds = True
intents.members = True


# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")
    await bot.change_presence(activity=discord.Game(name="!help pour l'aide"))

# Commande !ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande !touché
@bot.command()
async def touché(ctx):
    await ctx.send("coulé ! ⛵")


# Commande !members
@bot.command()
async def members(ctx):
    members_list = "\n".join([f"{member.display_name} - {', '.join([role.name for role in member.roles if role.name != '@everyone'])}" for member in ctx.guild.members])
    await ctx.send(f"Liste des membres sur le serveur :\n{members_list}")


# Réactions automatiques
@bot.event
async def on_message(message):
    # si l'auteur du message est identique à l'utilisateur du bot
    if message.author == bot.user:
        return

    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")
    
    if "salut" in message.content.lower():
        await message.add_reaction("👋")

    await bot.process_commands(message)

# Commande !joke
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


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Récupérer le canal système du serveur
    if channel:
        await channel.send(f"Bienvenue {member.mention} sur le serveur ! Utilisez `!welcome` pour voir un message de bienvenue personnalisé.")



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
    # Vérifie si l'auteur du message est un bot (pour éviter que le bot ne se bannisse lui-même)
    if message.author.bot:
        return

    # Vérifie si le message contient un mot banni
    for word in banned_words:
        if word in message.content.lower():
            # Bannit l'utilisateur
            await message.author.ban(reason="Utilisation d'une injure.")
            # Envoie un message dans le canal de modération pour notifier du bannissement
            await message.channel.send(f"{message.author.mention} a été banni pour utilisation d'une injure.")

            break  # Sort de la boucle après le premier mot trouvé

    # Continue le traitement des autres commandes et événements
    await bot.process_commands(message)


#connexion du bot au serveur avec au token
bot.run("Token_discorde")
         

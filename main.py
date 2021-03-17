import discord, sys, asyncio
from discord.ext import commands
from credentials import Token
from embeds import BotEmbed


"""
0. empecher des bots de pin/reagir

0. Commande Help

0. Faire un !statut :
    - Nom du bot et son statut
    - Nombre de message pin
    - Channel des messages pin
    - Commande d'aide

0. !!!!! Possibilité de ping d'ancien message !!!!!

        1. Configurer le bot pour lui donner le channel pinned

        2. Empêcher de pinned les messages du bot

        3. Empêcher de pinned les messages dans le channel pinned

        4. Récupérer les infos du messages pinned :
            - nom de l'auteur
            - date et heure du message
            - tag de l'auteur
            - contenu du message

5. Intégrer des logs avec loggins

        6. Revoir la fonction pour check le channel pinned ou l'author = bot

7. Autoriser seulement certain rôle à pinned
    - empecher le @ d'everyone, here ou users ou bot
"""



# ==========| Variables |==========
bot = commands.Bot(command_prefix='!') # Bot instance

channel_id = None
roles = []


# ==========| Tool Function | Return id channel in integer |==========
def return_pinned_channel(chan):
    if chan is not None:
        value = str(chan)
        value = value.replace('#', '')
        value = value.replace('<', '')
        value = value.replace('>', '')
        return int(value)



# ==========| Tool Function | Get role id in integer |==========
def return_role_id(role):
    if role is not None:
        value = str(role)
        value = value.replace('@', '')
        value = value.replace('&', '')
        value = value.replace('>', '')
        value = value.replace('<', '')
        return int(value)



# ==========| Tool Function | Build role string |==========
def build_role_str(role):
    value = '<@&' + str(role) + '>'
    return value



# ==========| Event | Bot is running ! |==========
@bot.event
async def on_ready():
    print('bot is ready')



# ==========| Command | Set Pinned Channel |==========
@bot.command(name='setpc')
async def set_pinned_channel(ctx, channel):
    global channel_id # Global variable

    channel_id = return_pinned_channel(channel)

    # Embed to confirmed pinned channel setup
    embed = BotEmbed.set_pinned_channel_embed()
    await ctx.send(embed=embed)



# ==========| Command | Edit Pinned Channel |==========
@bot.command(name='editpc')
async def edit_pinned_channel(ctx, channel):
    global channel_id # Global variable

    # If channel_id is not empty > Edit
    if channel_id is not None:

        # If channel id is differnt than global channel id > Authorized edit
        if channel_id != return_pinned_channel(channel):
            channel_id = return_pinned_channel(channel)
            embed = BotEmbed.edit_pinned_channel_embed(channel)
            await ctx.send(embed=embed)

        else: # If channel id is differnt than global channel id > Cancel edit
            embed = BotEmbed.is_already_pinned_channel_embed(channel)
            await ctx.send(embed=embed)


    # If channel_id is empty > Cancel
    elif channel_id is None:
        embed = BotEmbed.none_pinned_channel_embed()
        await ctx.send(embed=embed)



# ==========| Command | Set Authorized Role |==========
@bot.command(name='addro')
async def set_authorized_role(ctx, arg):
    global roles

    if arg == '@everyone' or arg == '@here':
        embed = BotEmbed.error_all_roles_embed()
        await ctx.send(embed=embed)

    else:
        if return_role_id(arg) in roles:
            embed = BotEmbed.already_authorized_roles_embed(arg)
            await ctx.send(embed=embed)

        elif not return_role_id(arg) in roles:
            role_id = return_role_id(arg)
            embed = BotEmbed.add_authorized_roles_embed(arg)
            roles.append(role_id)
            await ctx.send(embed=embed)



# ==========| Command | Remove Authorized Role |==========
@bot.command(name='delro')
async def remove_authorized_roles(ctx, arg):
    #for role in roles:
    if return_role_id(arg) in roles:
        roles.remove(return_role_id(arg))
        embed = BotEmbed.remove_authorized_roles_embed(arg)
        await ctx.send(embed=embed)

    elif not return_role_id(arg) in roles:
        embed = BotEmbed.none_authorized_roles_embed(arg)
        await ctx.send(embed=embed)



# ==========| Command | Authorized Role list|==========
@bot.command(name='allro')
async def authorized_roles_list(ctx):
    auth_roles = ''

    for role in roles:
        auth_roles += build_role_str(role) + ' '

    embed = BotEmbed.authorized_roles_list_embed(str(auth_roles))
    await ctx.send(embed=embed)



# ==========| Command | Test |==========
@bot.command(name='r')
async def role(ctx):

    await ctx.send(ctx.author.roles)



# ==========| Event | Pinned Messages |==========
@bot.event
async def on_message(message):

    # Return channel object
    def get_pinned_channel():
        global channel_id
        return bot.get_channel(channel_id)

    pinned_channel = get_pinned_channel() # Get pinned channel object

    channel = message.channel # Get channel where pinned message has been sent

    # Overide on_message function | Enable to send command
    await bot.process_commands(message)

    # Check the pinned emoji
    def check(reaction, user):
        return str(reaction.emoji) == '📌'


    # Check the pinned channel
    def is_pinned_channel():
        if channel == pinned_channel:
            return True


    try: # Get User instance
        reaction, user = await bot.wait_for('reaction_add', check=check)
        user_pinned = user

    except asyncio.TimeoutError:
        pass


    else: # Pinned process
        if message.author != bot.user or not is_pinned_channel(): # If Bot isn't message author or channel is pinned channel
            pinned_channel = get_pinned_channel()

            if message.attachments: # If the message is a file
                image_url = message.attachments[0].url
                embed = BotEmbed.pinned_embed(message, message.content, user)
                embed.set_image(url=image_url) # Add an image to embed

                await pinned_channel.send(embed=embed) # Send embed to pinned channel
                pass

            else: # If the message has no attachments
                embed = BotEmbed.pinned_embed(message, message.content, user)
                content = message.content

                await pinned_channel.send(embed=embed) # Send embed to pinned channel
                pass




# ==========| Main |==========
bot.run(Token.token) # Run bot

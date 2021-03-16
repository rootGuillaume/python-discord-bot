import discord, sys, asyncio
from discord.ext.commands import Bot
from credentials import Token
from embeds import BotEmbed

"""
0. Commande Help

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
"""



# ==========| Variables |==========
bot = Bot(command_prefix='!')
print('Bot running...')


# ==========| Functions |==========
@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()



# ==========| Pinned Messages |==========
@bot.event
async def on_message(message):
    pinned_channel = bot.get_channel(821135199706021928)
    channel = message.channel # Get channel instance

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
bot.run(Token.token)

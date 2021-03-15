import discord, sys, asyncio
from discord.ext.commands import Bot
from credentials import Token


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
"""



# ==========| Variables |==========
#bot = discord.bot()
bot = Bot(command_prefix='!')
#bot.remove_command('help')
print('Bot running...')




# ==========| Functions |==========
@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()

    for each_message in messages:
        await each_message.delete()



@bot.event
async def on_message(message):
    pinned_channel = bot.get_channel(821135199706021928)
    channel = message.channel


    # The pinned emoji
    def check(reaction, user):
        return str(reaction.emoji) == '📌'


    # Check the pinned channel
    def is_pinned_channel():
        if channel == pinned_channel:
            return True

    try:
        reaction, user = await bot.wait_for('reaction_add', check=check)

    except asyncio.TimeoutError:
        pass

    else:

        # If the message is a file
        if message.attachments:
            await channel.send('Cant pinned picture')
            pass

        # If the message is not a file
        elif not message.attachments:

            # Check if author is the bot
            if is_pinned_channel():
                await channel.send('Cant pinned in the pinned channel')
                pass

            elif not is_pinned_channel():
                if message.author == bot.user:

                    await channel.send('Cant pinned message from the Bot')
                    pass

                else:
                    await pinned_channel.send(message.content)




# ==========| Main |==========
bot.run(Token.token)

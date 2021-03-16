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

7. Autoriser seulement certain rôle à pinned
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

#    server_id = message.guild.id
#    channel_id = message.channel.id
#    message_id = message.id

    # The pinned emoji
    def check(reaction, user):
        return str(reaction.emoji) == '📌'


    # Check the pinned channel
    def is_pinned_channel():
        if channel == pinned_channel:
            return True


    #url_message = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(message_id)



#    message_time = str(message.created_at.time()).split(':')
#
#    hours = message_time[0]
#    minutes = message_time[1]
#
#    message_time = hours + ':' + minutes


    # === Embed pinned ===
#    pinned_embed = discord.Embed(
#        description=message.content,
#        color=0xf54254
#    )
#
#    pinned_embed.set_author(
#        name=message.author.display_name,
#        icon_url=message.author.avatar_url
#    )
#
#    pinned_embed.add_field(name="🗓 Dat️e", value=message.created_at.date(), inline=True)
#    pinned_embed.add_field(name="🕓 Time", value=message_time, inline=True)
#    pinned_embed.add_field(name="📌 Pinned by", value=user_pinned.mention, inline=True)
#    pinned_embed.add_field(name="🔗 Message Link", value=url_message, inline=False)


    # === Error channel pinned ===
    error_channel_embed = discord.Embed(
        title='Error !',
        description="You can't pinned in this channel",
        color=0xf5a742
    )

    try:
        reaction, user = await bot.wait_for('reaction_add', check=check)
        user_pinned = user
    except asyncio.TimeoutError:
        pass

    # Pinned processing
    else:

        # If the message is a file
        if message.attachments:
            #url_image_pinned = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(message_id) + '/' + message.attachments.filename

            #pinned_embed = discord.Embed(
            #    description=message.content + '\n' + url_image_pinned,
            #    color=0xf54254
            #)

            await channel.send('Cant pinned picture')
            pass

        # If the message is not a file
        elif not message.attachments:



            if message.author == bot.user or is_pinned_channel():
                #await channel.send('Cant pinned in the pinned channel')
                await channel.send(embed=error_channel_embed)
                pass

            else:
                await pinned_channel.send(embed=pinned_embed)
                #await pinned_channel.send(message.content)
                pass







# ==========| Main |==========
bot.run(Token.token)

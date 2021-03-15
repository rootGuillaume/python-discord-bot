import discord, sys, asyncio
from discord.ext.commands import Bot
from credentials import Token


"""
0. Commande Help
1. Configurer le bot pour lui donner le channel pinned
2. Empêcher de pinned les messages du bot
3. Empêcher de pinned les messages dans le channel pinned
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

    def check(reaction, user):
        return str(reaction.emoji) == '📌'

    try:
        reaction, user = await bot.wait_for('reaction_add', check=check)

    except asyncio.TimeoutError:
        pass

    #except:
    else:
        if message.attachments:
            await channel.send('Cant pinned picture')
            pass

        elif not message.attachments:
            await pinned_channel.send(message.content)




# ==========| Main |==========
bot.run(Token.token)

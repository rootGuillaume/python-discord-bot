import discord


class BotEmbed:

    def pinned_embed(msg, description, user):
        server_id = msg.guild.id
        channel_id = msg.channel.id
        message_id = msg.id

        url_message = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(message_id)

        message_time = str(msg.created_at.time()).split(':')

        hours = message_time[0]
        minutes = message_time[1]

        message_time = hours + ':' + minutes


        embed = discord.Embed(
            description=msg.content,
            color=0xf54254
        )

        embed.set_author(
            name=msg.author.display_name,
            icon_url=msg.author.avatar_url
        )

        embed.add_field(name="🗓 Dat️e", value=msg.created_at.date(), inline=True)
        embed.add_field(name="🕓 Time", value=message_time, inline=True)
        embed.add_field(name="📌 Pinned by", value=user.mention, inline=True)
        embed.add_field(name="🔗 Message Link", value=url_message, inline=False)

        return embed

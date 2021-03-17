import discord


class BotEmbed:

    # Color variables
    c_success = 0x48c774
    c_error = 0xff3860
    c_warning = 0xffdd57

    # Embed | Render pinned message
    def pinned_embed(msg, description, user):

        # Get message url | Reforge render
        server_id = msg.guild.id
        channel_id = msg.channel.id
        message_id = msg.id
        url_message = 'https://discordapp.com/channels/' + str(server_id) + '/' + str(channel_id) + '/' + str(message_id)

        # Get message time | Reforge render
        message_time = str(msg.created_at.time()).split(':')
        hours = message_time[0]
        minutes = message_time[1]
        message_time = hours + ':' + minutes

        embed = discord.Embed( # Embed Structure
            description=msg.content,
            color=0xf54254
        )

        embed.set_author( # Embed author details
            name=msg.author.display_name,
            icon_url=msg.author.avatar_url
        )

        # Embed field | Date, Time, Pinned by, Message link
        embed.add_field(name="🗓 Dat️e", value=msg.created_at.date(), inline=True)
        embed.add_field(name="🕓 Time", value=message_time, inline=True)
        embed.add_field(name="📌 Pinned by", value=user.mention, inline=True)
        embed.add_field(name="🔗 Message Link", value=url_message, inline=False)

        return embed # Return embed object


    # Embed | Set Pinned Channel
    def set_pinned_channel_embed():
        embed = discord.Embed( # Embed Structure
            description='✅ Well done ! Pinned channel has been successfully configured !',
            color=BotEmbed.c_success
        )

        return embed


    # Embed | Edit Pinned Channel
    def edit_pinned_channel_embed(channel):
        embed = discord.Embed( # Embed Structure
            description='✅ Pinned channel successfully modified to ' + channel + '.',
            color=BotEmbed.c_success
        )

        return embed


    # Embed | Is Already Pinned Channel
    def is_already_pinned_channel_embed(channel):
        embed = discord.Embed( # Embed Structure
            description='⚠️ ' + channel + ' is already the Pinned Channel.',
            color=BotEmbed.c_warning
        )

        return embed


    # Embed | No Pinned Channel Configure
    def none_pinned_channel_embed():
        embed = discord.Embed( # Embed Structure
            description='🚫 Neither Pinned Channel has been set up. \n Please run the **!setpc #channel** to set up a Pinned Channel.',
            color=BotEmbed.c_error
        )

        return embed

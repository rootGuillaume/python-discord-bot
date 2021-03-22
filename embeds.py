import discord


class BotEmbed:

    # Color variables
    c_success = 0x48c774
    c_error = 0xff3860
    c_warning = 0xffdd57
    c_info = 0x209cee

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



    # Embed | Bot Information
    def bot_information_embed(bot, pin_channel, prefix, roles):
        embed = discord.Embed(
            description='Hello, I am Pin Bot!\nHere are the informations about me:\n' +
                            '\n**Pin Channel :** ' + pin_channel + '\n' +
                            '\n**Pin Prefix :** ' + prefix + '\n' +
                            '\n**Pin Help :** ' + prefix + 'help' + '\n' +
                            '\n**Allowed Roles :** ' + roles,
            color=BotEmbed.c_info
        )

        # //image.jpg is the desired extension !
        # DO NOT CHANGE 'image' | Discord documentation
        embed.set_image(url='attachment://image.jpg')
        embed.set_footer(text='Pin Bot | v0.1')

        embed.set_author(
            name=bot.display_name,
            icon_url=bot.avatar_url
        )

        return embed



    # Embed | Set Pinned Channel
    def set_pinned_channel_embed():
        embed = discord.Embed( # Embed Structure
            description='✅ Well done! Pin channel has been successfully configured!',
            color=BotEmbed.c_success
        )

        return embed



    # Embed | Edit Pinned Channel
    def edit_pinned_channel_embed(channel):
        embed = discord.Embed( # Embed Structure
            description='✅ Pin channel successfully modified to ' + channel + '!',
            color=BotEmbed.c_success
        )

        return embed



    # Embed | Is Already Pinned Channel
    def is_already_pinned_channel_embed(channel):
        embed = discord.Embed( # Embed Structure
            description='⚠️ ' + channel + ' is already the Pin Channel.',
            color=BotEmbed.c_warning
        )

        return embed



    # Embed | Add Roles able to pinned
    def add_authorized_roles_embed(role):
        embed = discord.Embed( # Embed Structure
            description='✅ ' + role + ' is now able to pinned messages!',
            color=BotEmbed.c_success
        )

        return embed



    # Embed | Already Authorized Roles able to pinned
    def already_authorized_roles_embed(role):
        embed = discord.Embed( # Embed Structure
            description='⚠️ ' + role + ' is already able to pin message.',
            color=BotEmbed.c_warning
        )

        return embed



    # Embed | Add Roles able to pinned
    def remove_authorized_roles_embed(role):
        embed = discord.Embed( # Embed Structure
            description='🗑️ ' + role + ' has successfully been removed!',
            color=BotEmbed.c_success
        )

        return embed


    # Embed | Roles is not in the Authorized list
    def none_authorized_roles_embed(role):
        embed = discord.Embed( # Embed Structure
            description='⚠️ ' + role + ' is not an authorized role.',
            color=BotEmbed.c_warning
        )

        return embed



    # Embed | Roles Everyone or Here
    def error_all_roles_embed():
        embed = discord.Embed( # Embed Structure
            description='🚫 You can\'t add global roles such as @everyone or @here.',
            color=BotEmbed.c_error
        )

        return embed



    # Embed | Authorized Roles
    def authorized_roles_list_embed(roles):
        embed = discord.Embed( # Embed Structure
            description='💡 Auhtorized roles to pin messages : ' + roles,
            color=BotEmbed.c_info
        )

        return embed



    # Embed | Edit Pin Bot prefix
    def edit_prefix_embed(prefix):
        embed = discord.Embed( # Embed Structure
            description='🤖 **' + prefix + '** is now the new prefix command!',
            color=BotEmbed.c_success
        )

        return embed

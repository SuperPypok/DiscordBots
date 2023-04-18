import discord, locale, os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
current_lang, encoding = locale.getdefaultlocale()
token = "token" # Your bot token
bot = discord.Client(intents=intents)

# sending a message that the bot has turned on to the console.
@bot.event
async def on_ready():
    if current_lang == "ru_RU":
        print('Бот {0.user}'.format(bot), 'успешно запущен!')
    else:
        print('Bot {0.user}'.format(bot), 'successfully launched!')

# Publication of information about the connected participant.
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(id) # Your channel id
    await channel.send(f'{member} connected to server')

# Publication of information about the participant who has been released.
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(id) # Your channel id
    await channel.send(f'{member} left the server.')

# Sending messages from server members.
@bot.event
async def on_message(message):
    channel = bot.get_channel(id) # Your channel id
    if message.author != bot.user:
        # text + file
        if len(message.attachments) > 0 and message.content:
            for attachment in message.attachments:
                await attachment.save(attachment.filename)
                with open(attachment.filename, 'rb') as f:
                    picture = discord.File(f)
                    await channel.send(f'{message.author} in "{message.channel}: {message.content}"',  file=picture)
                os.remove(attachment.filename)
        # file
        elif len(message.attachments) > 0:
            for attachment in message.attachments:
                await attachment.save(attachment.filename)
                with open(attachment.filename, 'rb') as f:
                    picture = discord.File(f)
                    await channel.send(f'{message.author} sent a file "{message.channel}"', file=picture)
                os.remove(attachment.filename)
        # text
        else:
            await channel.send(f'{message.author} in "{message.channel}": {message.content}')

bot.run(token)

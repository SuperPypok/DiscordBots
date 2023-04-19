import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(id) # Your channel id
    # for guild in bot.guilds:        # These two lines are responsible for displaying the
    #     print(guild.name)           # names of all those servers where the bot is present.
    guild = bot.guilds[0] # Get the first guild the bot is connected to
    while True:
        await channel.send("text") # Your text
        await guild.create_text_channel("channel_name") # The channel name must be less than 100 characters long.

bot.run("YOUR TOKEN")

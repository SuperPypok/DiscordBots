import discord

client = discord.Client()
token = "token" # Your bot token

@client.event
async def on_ready():
    global channel
    channel = client.get_channel(id) # Your channel id
    while True:
        await channel.send("text") # Your text

client.run(token)
import discord

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

# Replace 'YOUR_DISCORD_TOKEN' with your bot token
TOKEN = 'MTI1NDQzMDAzODE5NjA5MzA0MA.G3ns32.K4MUF0FMqQGNK726W9p6bg20zbP47tHkXbuihs'

# Replace 'YOUR_CHANNEL_ID' with the ID of the channel where you want to send the DMs
CHANNEL_ID = 1256888426750283877

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is a DM
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        # Find the server channel to send the DM
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            # Send the message content
            await channel.send(f'DM from {message.author}:\n{message.content}')
            
            # Handle attachments
            for attachment in message.attachments:
                await channel.send(f'{message.author} sent an attachment:')
                await channel.send(attachment.url)

client.run(TOKEN)
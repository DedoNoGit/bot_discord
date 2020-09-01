import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$oi bot'):
        await message.channel.send('salve salve cachorro')


client.run('BOT_TOKEN')
import discord
import config
from discord.utils import get

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

@client.event
async def on_member_join(member):
	role = get(member.guild.roles, name='Intruso')
	await member.add_roles(role)
    
client.run(config.BOT_TOKEN)

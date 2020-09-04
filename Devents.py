from discord.utils import get
from client import client


@client.event
async def on_ready():
	# Mostra o ID e se o bot está rodando.
	print(f'Bot is ready. \nID: {client.user}')


@client.event
async def on_member_join(member):
	# Deixa registrado quando alguém entra no server, e adiciona o título de Intruso.
	role = get(member.guild.roles, name='Intruso')
	await member.add_roles(role)
	print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
	# Deixa registrado quando alguém sai do server.
	print(f'{member} has left the server.')

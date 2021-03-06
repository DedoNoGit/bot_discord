import discord
from discord.ext import commands
from discord.utils import get
import config
from sympy import *
from math import *

x = symbols('x')

def calculate(text):
	#Calcula o que o usuário mandou.
	try:
		#Desafio pro Derick.
		if 'import' in text:
			raise SystemError
		else:
			return eval(text)
	except ZeroDivisionError:
		return 'VAI DIVIDIR POR ZERO NÃO, SEU ARROMBADO!'
	except SystemError:
		return 'VAI INVADIR MEU PC NÃO, SEU ARROMBADO!'
	except:
		return 'Refaz a conta aí, meu chapa, tem alguma coisa errado.'

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	#Mostra o bot ID
	print(f'Bot is ready. ID: {client.user}')

@client.event
async def on_member_join(member):
	#Deixa registrado quando alguém entra no server, e adiciona o título de Intruso.
	role = get(member.guild.roles, name='Intruso')
	await member.add_roles(role)
	print(f'{member} has joined the server.')
	
@client.event
async def on_member_remove(member):
	#Deixa registrado quando alguém sai do server.
	print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
	#Mostra latência do bot .ping
	await ctx.send(f'Bot latency: {round(client.latency * 1000)}ms')

@client.command(aliases=['m'])
async def math(ctx, *, question):
	#Implementa uma calculadora no bot. Ex: .math 15+3 = 18  ou .m sum([i for i in range(10)]) = 45
	await ctx.send(calculate(question))

client.run(config.BOT_TOKEN)

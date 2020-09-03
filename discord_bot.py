import discord
from discord.ext import commands
from discord.utils import get
import config
from math import *
from sympy import *

x= symbols('x')


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

@client.command(aliases=['j'])
async def join(ctx):
	#faz o bot se conectar ao canal de voz
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected(): #se as pessoa está em um canal de voz ou o bot tbm está conectado em algum outro
		await voice.move_to(channel)
	else: #se nao estiver conectado em um canal já ele conecta
		voice = await channel.connect()
		print(f"O Bot se conectou ao canal {channel}")

	#await voice.disconnect() #to fazendo isso duplamente pq teoricamente tem um bug que impede de tocar musica

	#if voice and voice.is_connected(): #se as pessoa está em um canal de voz ou o bot tbm está conectado em algum outro
	#	await voice.move_to(channel)
	#else: #se nao estiver conectado em um canal já ele conecta
	#	voice = await channel.connect()
	#	print(f"O Bot se conectou ao canal {channel}")

	await ctx.send(f"Me conectei ao canal {channel}")

#@client.command(aliases=['p'])
#async def play(ctx, url: string):
#	#funcão de tocar coisas 
#	channel = ctx.message.author.voice.channel
#	voice = get(client.voice_clients, guild=ctx.guild)

@client.command(aliases=['l'])
async def leave(ctx):
	#faz o bot sair do canal de voz
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	
	if voice and voice.is_connected(): 
		await voice.disconnect()
		print(f"o bot se desconectou do canal {channel}")
		await print(f"Saí do canal {channel}")
	else: 
		print("O bot não estava conectado a nehum canal de voz")
		await ctx.send(f"Não estou conectado a nenhum canal de voz")



		
client.run(config.BOT_TOKEN)

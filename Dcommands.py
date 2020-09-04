from discord.ext import commands
from Dfuncts import calculate, make_var


class Commands(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, ctx):
		# Mostra latência do bot .ping
		await ctx.send(f'Bot latency: {round(self.client.latency * 1000)}ms')

	@commands.command(aliases=['m'])
	async def math(self, ctx, *, question):
		# Implementa uma calculadora no bot. Ex: .math 15+3 = 18  ou .m sum([i for i in range(10)]) = 45
		await ctx.send(calculate(question))

	@commands.command(aliases=['mv'])
	async def make_variable(self, ctx, *, question):
		# Implementa a função de criar variáveis dentro do bot
		await ctx.send(make_var(question))


def setup(client):
	client.add_cog(Commands(client))

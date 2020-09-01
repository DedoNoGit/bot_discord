import discord


class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('hello there')
            

client = MyClient()

client.run('BOT_TOKEN')
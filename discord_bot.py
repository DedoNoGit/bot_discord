from client import client  # Linha desnecessaura, mas vai ficar aí.
from Devents import *  # Importa os eventos
import config

# Importa os comandos
client.load_extension('Dcommands')

client.run(config.BOT_TOKEN)  # Roda o bot

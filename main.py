# Main
from core import Develop

import discord


intents = discord.Intents.all()
intents.typing = False
bot = Develop(command_prefix="$", intents=intents)

bot.run()

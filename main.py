# Main
from core import Develop

import discord


intents = discord.Intents.all()
intents.typing = False
bot = Develop(command_prefix="$", intents=intents)


if __name__ == "__main__":
    bot.run(bot.secret["token"])

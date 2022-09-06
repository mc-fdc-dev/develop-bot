from discord.ext import commands
import discord
from orjson import loads

from os import listdir

from typing import TypedDict


class Secret(TypedDict):
    token: str

class Develop(commands.Bot):
    with open("secret.json", "r") as f:
        secret: Secret = loads(f.read())

    async def setup_hook(self) -> None:
        await self.load_extension("jishaku")
        for filename in listdir("cogs"):
            await self.load_extension(f"cogs.{filename[:-2]}")

    async def on_ready(self) -> None:
        print("Start")

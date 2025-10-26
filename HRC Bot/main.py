import os
import discord
from discord.ext import commands
from discord import app_commands

# Discord-Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Cogs laden
        await self.load_extension("cogs.ssu_system")
        # Weitere Cogs können hier hinzugefügt werden
        # await self.load_extension("cogs.admin")
        # await self.load_extension("cogs.peacetime")
        # await self.load_extension("cogs.welcome")

        # Slash Commands synchronisieren
        await self.tree.sync()


bot = MyBot()


@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}!")


# Token aus Umgebungsvariable laden (nicht im Code speichern!)
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("❌ Fehler: Keine Umgebungsvariable 'DISCORD_TOKEN' gefunden.")

bot.run(TOKEN)


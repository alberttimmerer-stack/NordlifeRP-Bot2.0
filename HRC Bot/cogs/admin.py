import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Checkt die Latenz des Bots")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! Latenz: {round(self.bot.latency*1000)}ms")

async def setup(bot):
    await bot.add_cog(Admin(bot))

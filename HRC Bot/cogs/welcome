import discord
from discord import app_commands
from discord.ext import commands

# Globale Variable, um den Kanal zu speichern
from config import WELCOME_CHANNELS


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    

    # Slash-Befehl zum Setzen des Welcome-Kanals
    @app_commands.command(name="setwelcome", description="Setzt den Kanal für Willkommensnachrichten")
    @app_commands.describe(channel="Wähle den Kanal, in dem Willkommensnachrichten gesendet werden sollen")
    async def set_welcome(self, interaction: discord.Interaction, channel: discord.TextChannel):
        WELCOME_CHANNELS[interaction.guild.id] = channel.id
        await interaction.response.send_message(
            f"Willkommensnachrichten werden nun in {channel.mention} gesendet.", ephemeral=True
        )

    # Slash-Befehl zum Deaktivieren des Welcome-Kanals
    @app_commands.command(name="stopwelcome", description="Stoppt die Willkommensnachrichten")
    async def stop_welcome(self, interaction: discord.Interaction):
        if WELCOME_CHANNELS.pop(interaction.guild.id, None):
            await interaction.response.send_message("Willkommensnachrichten wurden deaktiviert.", ephemeral=True)
        else:
            await interaction.response.send_message("Es ist kein Welcome-Kanal gesetzt.", ephemeral=True)

    # Listener für neue Mitglieder
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel_id = WELCOME_CHANNELS.get(member.guild.id)
        if channel_id:
            channel = member.guild.get_channel(channel_id)
            if channel:
                embed = discord.Embed(
                    title=f"Willkommen {member.name}!",
                    description=f"Schön, dass du auf **{member.guild.name}** bist!",
                    color=discord.Color.green()
                )
                await channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))

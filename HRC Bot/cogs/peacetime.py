import discord
from discord import app_commands
from discord.ext import commands

class PeaceTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_message = None  # Optional, falls du sie später löschen willst

    async def delete_active_message(self):
        """Löscht die aktuell aktive Nachricht, falls vorhanden"""
        if self.active_message:
            try:
                await self.active_message.delete()
            except discord.NotFound:
                pass
            self.active_message = None

    @app_commands.command(
        name="peacetime",
        description="Aktiviere oder deaktiviere PeaceTime"
    )
    @app_commands.describe(
        status="An oder Aus"
    )
    @app_commands.choices(status=[
        app_commands.Choice(name="an", value="an"),
        app_commands.Choice(name="aus", value="aus")
    ])
    async def peacetime(
        self,
        interaction: discord.Interaction,
        status: app_commands.Choice[str]
    ):
        await self.delete_active_message()

        if status.value == "an":
            embed = discord.Embed(
                title="🕊️ PeaceTime an",
                description="Man darf nicht vor der polizei Flüchten \nMan darf keine verletzen \nMan darf keine großen räube machen sprich Container oder bank",
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="⚔️ PeaceTime deaktiviert",
                description="Man darf von der Polizei flüchten \nGroße Räume begehen sprich Container oder Bank \nMan darf andere verletzen ",
                color=discord.Color.red()
            )

        embed.set_footer(
            text=f"Aktion von {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )

        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()
        self.active_message = msg


async def setup(bot):
    await bot.add_cog(PeaceTime(bot))

import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

class SSUSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_message = None

    async def delete_active_message(self):
        """Löscht die aktuell aktive Nachricht, falls vorhanden"""
        if self.active_message:
            try:
                await self.active_message.delete()
            except discord.NotFound:
                pass
            self.active_message = None

    # ==========================
    # 📊 /ssupoll Command
    # ==========================
    @app_commands.command(name="ssupoll", description="Starte eine SSU-Teilnahme-Umfrage")
    @app_commands.describe(
        uhrzeit="Uhrzeit, wann der Server gestartet werden soll (z. B. 21:30)",
        host="Optional: Host (User erwähnen)",
        cohost="Optional: Co-Host (User erwähnen)"
    )
    async def ssupoll(
        self,
        interaction: discord.Interaction,
        uhrzeit: str,
        host: discord.Member | None = None,
        cohost: discord.Member | None = None
    ):
        await self.delete_active_message()

        host_text = host.mention if host else "Nicht angegeben"
        cohost_text = cohost.mention if cohost else "Nicht angegeben"

        embed = discord.Embed(
            title="📊 SSU-Poll",
            description=f"**Wer ist dabei beim Serverstart um {uhrzeit}?**",
            color=discord.Color.blue()
        )
        embed.add_field(name="👑 Host", value=host_text, inline=True)
        embed.add_field(name="🤝 Co-Host", value=cohost_text, inline=True)
        embed.set_footer(
            text=f"Erstellt von {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )

        await interaction.response.send_message(
            content="<@&1347927392378687539>",  # Deine SSU-Rolle hier!
            embed=embed,
            allowed_mentions=discord.AllowedMentions(roles=True)  # <--- Wichtig!
        )
        msg = await interaction.original_response()
        await msg.add_reaction("✅")
        self.active_message = msg

        # ==========================
        # 🟢 /ssu Command mit Button
        # ==========================

    @app_commands.command(name="ssu", description="Starte den Server (SSU)")
    @app_commands.describe(
        uhrzeit="Uhrzeit, wann der Server gestartet wird (z. B. 21:30)",
        host="Optional: Host (User erwähnen)",
        cohost="Optional: Co-Host (User erwähnen)"
    )
    async def ssu(
            self,
            interaction: discord.Interaction,
            uhrzeit: str,
            host: discord.Member | None = None,
            cohost: discord.Member | None = None
    ):
        await self.delete_active_message()

        host_text = host.mention if host else "Nicht angegeben"
        cohost_text = cohost.mention if cohost else "Nicht angegeben"

        # Embed
        embed = discord.Embed(
            title="🟢 SSU - Server Start-Up",
            description=f"**Der Server wird jetzt um {uhrzeit} gestartet!**",
            color=discord.Color.green()
        )
        embed.add_field(name="👑 Host", value=host_text, inline=True)
        embed.add_field(name="🤝 Co-Host", value=cohost_text, inline=True)
        embed.set_footer(
            text=f"Erstellt von {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )

        # Button erstellen
        view = discord.ui.View()
        view.add_item(
            discord.ui.Button(
                label="Server",
                url="https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Dsz1re89e",  # <--- Hier deine Ziel-URL einsetzen
                style=discord.ButtonStyle.link
            )
        )

        # Nachricht senden mit Rollenping & Button
        await interaction.response.send_message(
            content="<@&1347927392378687539>",  # Deine Rolle
            embed=embed,
            view=view,
            allowed_mentions=discord.AllowedMentions(roles=True)
        )

        msg = await interaction.original_response()
        self.active_message = msg

    # ==========================
    # 🔴 /ssd Command
    # ==========================
    @app_commands.command(name="ssd", description="Server herunterfahren (SSD)")
    @app_commands.describe(
        host="Optional: Host (User erwähnen)",
        cohost="Optional: Co-Host (User erwähnen)"
    )
    async def ssd(
        self,
        interaction: discord.Interaction,
        host: discord.Member | None = None,
        cohost: discord.Member | None = None
    ):
        await self.delete_active_message()

        aktuelle_zeit = datetime.now().strftime("%H:%M")

        host_text = host.mention if host else "Nicht angegeben"
        cohost_text = cohost.mention if cohost else "Nicht angegeben"

        embed = discord.Embed(
            title="🔴 SSD - Server Shut-Down",
            description=f"**Der Server wird jetzt um {aktuelle_zeit} heruntergefahren!**",
            color=discord.Color.red()
        )
        embed.add_field(name="👑 Host", value=host_text, inline=True)
        embed.add_field(name="🤝 Co-Host", value=cohost_text, inline=True)
        embed.set_footer(
            text=f"Erstellt von {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )

        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()
        await msg.add_reaction("💤")
        self.active_message = msg




# Setup-Funktion für Cog-Registrierung
async def setup(bot):
    await bot.add_cog(SSUSystem(bot))

import discord
from discord.ext import commands
from discord import app_commands


class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            GUILD = discord.Object(id=1489832073383645244)
            synced = await self.tree.sync(guild=GUILD)
            print(f'Synced {len(synced)}')
        except Exception as e:
            print(f'Error syncing Command') 

    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send('Damn bro really likes Shk')


intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!",intents=intents)

GUILD_ID = discord.Object(id=1489832073383645244)

@client.tree.command(name="hello",description="Just Hello",guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Good Morning Yall")

@client.tree.command(name="printer",description="Just Printing",guild=GUILD_ID)
async def printer(interaction: discord.Interaction,printer: str):
    await interaction.response.send_message(printer)

client.run('<Authorization Token Goes Here>')
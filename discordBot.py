import discord
from discord.ext import commands
from discord import app_commands
from managebacAPI import managebacAPI
class Client(commands.Bot):
    async def on_ready(self):
        
        print(f'Logged on as {self.user}!')
        try:
            GUILD = discord.Object(id=1489832073383645244)
            synced = await self.tree.sync(guild=GUILD)
            print(f'Synced {len(synced)}')
        except Exception as e:
            print(f'Error Syuncing: {e}') 

    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send('Damn bro really likes Shk')


intents = discord.Intents.default()
intents.message_content = True

client = Client(command_prefix="!",intents=intents)

GUILD_ID = discord.Object(id=1489832073383645244)




@client.tree.command(name="auth", description="Tells you about your managebac Info", guild=GUILD_ID)
async def auth(interaction: discord.Interaction,auth: str):

    try:
        api = managebacAPI(auth)
        outList = api.user_info()

        embed = discord.Embed(
            title="Your Info",
            description=f'Name:{outList[0]}\nYour Class is {outList[1]}\nYour School ID is {outList[2]}')
        
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(e)


client.run('Auth')
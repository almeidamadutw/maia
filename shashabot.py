import discord
from discord import app_commands 

id_do_servidor = 1127996748242100265 #Coloque aqui o ID do seu servidor 

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.") 

aclient = client()
tree = app_commands.CommandTree(aclient) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'bomdia', description='bom dia!') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Bom dia meu bem!", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'boanoite', description='boa noite!') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Boa noite bebê da shasha!", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'euteamo', description='eu te amo shasha!') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"eu te amo também bebê!", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'jack', description='shasha você pode xingar o jack para mim?') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"jack você é uma pessoa horrível", ephemeral = False) 

aclient.run('MTEyODAzMTQyMjYxNjE5NTI3NQ.GX7E0_.xmZnZf-vXiEB1OregPYrNb9wvmhd_ZzBwO34mQ')

import discord
from discord.ext import commands
from ecobot import evaluar_objeto
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
 
@bot.command()
async def reciclar(ctx, *, objeto):
    respuesta = evaluar_objeto(objeto)
    await ctx.send(respuesta)
# Reemplaza
bot.run("Tu token aqui...")

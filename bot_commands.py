import discord
from discord.ext import commands
import requests
import bot_service as bs

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

APP_ID = bs.get_local_attribute("CLIENT_ID")
GUILD_ID = bs.get_local_attribute("GUILD_ID")
TOKEN = bs.get_local_attribute("DISCORD_TOKEN")


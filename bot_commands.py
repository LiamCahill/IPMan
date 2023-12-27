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
BOT_TOKEN = bs.get_local_attribute("DISCORD_TOKEN")

url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands'

# This is an example USER command, with a type of 2
json = {
    "name": "High Five",
    "type": 2
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

r = requests.post(url, headers=headers, json=json)

import discord
import responses
import bot_service
from discord.ext import commands
import requests
import bot_commands

TOKEN = bot_service.get_local_attribute("DISCORD_TOKEN")
APP_ID = bot_service.get_local_attribute("CLIENT_ID")
GUILD_ID = bot_service.get_local_attribute("GUILD_ID")
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())


url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands'

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "uhoh",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": f'Bot {TOKEN}'
}

r = requests.post(url, headers=headers, json=json)

delete_url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands'
d = requests.delete(delete_url)



async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    bs = bot_service
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as {0.user}'.format(client))



    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" in {channel}')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

import os
import json

def get_local_token():
    path = "./token.json"
    if os.path.exists(path):
        with open(path,'r') as file:
            KEY = json.load(file)
        return KEY['DISCORD_TOKEN']

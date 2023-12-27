import os
import json

def get_local_token():
    path = "./token.json"
    if os.path.exists(path):
        with open(path,'r') as file:
            KEY = json.load(file)
        return KEY['DISCORD_TOKEN']


def get_local_attribute(attr: str):
    path = "./token.json"
    attr = attr.upper()
    attr = (f'{attr}')

    if os.path.exists(path):
        with open(path,'r') as file:
            KEY = json.load(file)
        return KEY[attr]

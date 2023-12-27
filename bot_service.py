import os
import json


def get_local_attribute(attr: str):
    path = "./token.json"
    attr = attr.upper()
    attr = (f'{attr}')

    if os.path.exists(path):
        with open(path,'r') as file:
            KEY = json.load(file)
        return KEY[attr]

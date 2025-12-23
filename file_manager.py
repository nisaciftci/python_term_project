import json
import os

def load_data():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
        
    
def save_data(data):
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)


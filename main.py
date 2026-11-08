import os
import requests
import json

token = os.environ["DISCORD_TOKEN"]
channel = os.environ["CHANNEL_ID"]
user = os.environ["USER_ID"]

url = f"https://discord.com/api/v10/channels/{channel}/messages?limit=100"

headers = {
    "Authorization": f"Bot {token}"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(response.text)

messages = response.json()

ids = []

for message in messages:
    if message["author"]["id"] == user:
        import re
        found = re.findall(r"\b\d{5,20}\b", message["content"])
        ids.extend(found)

ids = list(dict.fromkeys(ids))

with open("assets.json", "w") as file:
    json.dump(ids, file, indent=4)

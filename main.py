import os
import requests
import json
import re

token = os.environ["DISCORD_TOKEN"]
user = os.environ["USER_ID"]

headers = {"Authorization": f"Bot {token}"}

channels = {
    "Library.json": os.environ["LIBRARY_CHANNEL_ID"],
    "Store.json": os.environ["STORE_CHANNEL_ID"]
}

for file, channel in channels.items():
    url = f"https://discord.com/api/v10/channels/{channel}/messages?limit=1000"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    ids = []

    for message in response.json():
        if message["author"]["id"] == user:
            ids += re.findall(r"\b\d{5,20}\b", message["content"])

    ids = list(dict.fromkeys(ids))

    with open(file, "w") as f:
        json.dump(ids, f, indent=4)

    print(file, ids)

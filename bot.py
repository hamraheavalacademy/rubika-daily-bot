import requests
import json
from datetime import datetime
import os

TOKEN = os.environ["RUBIKA_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

today = datetime.now().strftime("%Y-%m-%d")

with open("messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

for msg in messages:
    if msg["date"] == today:
        url = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": msg["text"]}
        response = requests.post(url, json=payload)
        print(f"ارسال شد: {response.json()}")
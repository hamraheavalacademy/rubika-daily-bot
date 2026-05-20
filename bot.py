import requests
import json
from datetime import datetime
import pytz
import os

TOKEN = os.environ["RUBIKA_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

tz = pytz.timezone("Asia/Tehran")
today = datetime.now(tz).date()

# تاریخ شروع (امروز که اولین پیام رفت)
start_date = datetime(2026, 5, 20).date()

day_number = (today - start_date).days + 1

print("Day number:", day_number)

with open("messages.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

# فقط تا 5 روز
if 1 <= day_number <= len(messages):
    msg = messages[day_number - 1]

    url = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg["text"]}

    response = requests.post(url, json=payload)
    print("ارسال شد:", response.json())
else:
    print("پیامی برای امروز نیست")

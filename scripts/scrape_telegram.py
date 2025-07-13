import os
import json
from datetime import datetime
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
channels = [
    "https://t.me/CheMed123",
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

output_base = "data/raw/telegram_messages"

def scrape_channel(channel_url, limit=100):
    client = TelegramClient("anon", api_id, api_hash)
    client.start()

    channel_entity = client.get_entity(channel_url)
    messages = client.get_messages(channel_entity, limit=limit)

    channel_name = channel_entity.username or "unknown_channel"
    today = datetime.utcnow().strftime("%Y-%m-%d")
    output_path = f"{output_base}/{today}"
    os.makedirs(output_path, exist_ok=True)

    out_file = f"{output_path}/{channel_name}.json"
    data = []

    for msg in messages:
        msg_data = {
            "id": msg.id,
            "date": str(msg.date),
            "text": msg.text,
            "has_media": bool(msg.media),
            "sender_id": msg.sender_id,
        }
        data.append(msg_data)

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Scraped {len(data)} messages from {channel_url}")
    client.disconnect()

if __name__ == "__main__":
    for channel in channels:
        try:
            scrape_channel(channel)
        except Exception as e:
            print(f"❌ Failed to scrape {channel}: {e}")

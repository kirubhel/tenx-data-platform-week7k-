import os
from datetime import datetime
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
channels = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

output_base = "data/images"

client = TelegramClient("image_session", api_id, api_hash)
client.start()

for channel_url in channels:
    entity = client.get_entity(channel_url)
    messages = client.get_messages(entity, limit=100)

    channel_name = entity.username or "unknown"
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    channel_dir = os.path.join(output_base, date_str, channel_name)
    os.makedirs(channel_dir, exist_ok=True)

    for msg in messages:
        if msg.photo:
            file_path = os.path.join(channel_dir, f"{msg.id}.jpg")
            try:
                client.download_media(msg, file_path)
                print(f"✅ Saved {file_path}")
            except Exception as e:
                print(f"❌ Failed to save {file_path}: {e}")

client.disconnect()

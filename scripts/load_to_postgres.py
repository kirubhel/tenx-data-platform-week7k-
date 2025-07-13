import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

cur = conn.cursor()

cur.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;
    CREATE TABLE IF NOT EXISTS raw.telegram_messages (
        id BIGINT PRIMARY KEY,
        date TIMESTAMP,
        text TEXT,
        has_media BOOLEAN,
        sender_id BIGINT,
        channel TEXT
    );
""")
conn.commit()

# Load JSONs
base_path = "data/raw/telegram_messages"
for date_folder in os.listdir(base_path):
    path = os.path.join(base_path, date_folder)
    for file in os.listdir(path):
        channel = file.replace(".json", "")
        with open(os.path.join(path, file), "r") as f:
            msgs = json.load(f)
            for msg in msgs:
                cur.execute("""
                    INSERT INTO raw.telegram_messages (id, date, text, has_media, sender_id, channel)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                """, (
                    msg.get("id"),
                    msg.get("date"),
                    msg.get("text"),
                    msg.get("has_media"),
                    msg.get("sender_id"),
                    channel
                ))
conn.commit()
cur.close()
conn.close()
print("✅ Loaded raw data to PostgreSQL.")

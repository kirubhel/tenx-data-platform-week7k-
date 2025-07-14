from sqlalchemy.orm import Session
from fastapi_app.models import Message
from sqlalchemy import func

def get_top_products(db: Session, limit: int = 10):
    return db.query(Message.text, func.count(Message.id).label("count"))\
             .group_by(Message.text)\
             .order_by(func.count(Message.id).desc())\
             .limit(limit).all()

def get_channel_activity(db: Session, channel_name: str):
    return db.query(func.date(Message.date), func.count(Message.id))\
             .filter(Message.channel == channel_name)\
             .group_by(func.date(Message.date)).all()

def search_messages(db: Session, keyword: str):
    return db.query(Message).filter(Message.text.ilike(f"%{keyword}%")).all()

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from fastapi_app.database import Base

class Message(Base):
    __tablename__ = "telegram_messages"
    __table_args__ = {"schema": "raw"}

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    text = Column(String)
    has_media = Column(Boolean)
    sender_id = Column(Integer)
    channel = Column(String)

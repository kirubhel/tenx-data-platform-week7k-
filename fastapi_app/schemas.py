from pydantic import BaseModel
from typing import Optional

class TopProduct(BaseModel):
    product: str
    count: int

class ChannelActivity(BaseModel):
    date: str
    count: int

class MessageSearch(BaseModel):
    id: int
    text: Optional[str]
    date: str

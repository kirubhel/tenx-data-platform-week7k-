from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_app import crud, models, schemas
from fastapi_app.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/reports/top-products", response_model=list[schemas.TopProduct])
def top_products(limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_top_products(db, limit)

@app.get("/api/channels/{channel_name}/activity", response_model=list[schemas.ChannelActivity])
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    return crud.get_channel_activity(db, channel_name)

@app.get("/api/search/messages", response_model=list[schemas.MessageSearch])
def search_messages(query: str, db: Session = Depends(get_db)):
    return crud.search_messages(db, query)

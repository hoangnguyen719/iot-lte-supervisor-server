from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

import models
from database import engine, SessionLocal
from models import Song, LteSignal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Signal(BaseModel):
    ts = datetime.now()
    pcellid: str
    rsrq: int
    rsrp: int
    frequency_band: int
    dlbw: int
    ulbw: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {'name': 'fastapi-songs'}


@app.get('/songs/')
def read_songs(db: Session = Depends(get_db)):
    return db.query(Song).all()

@app.get('/lte/')
def read_lte(db: Session = Depends(get_db)):
    return db.query(LteSignal).all()

@app.post('/post_signal/')
def create_signal(signal: Signal, db: Session = Depends(get_db)):
    db_signal = models.LteSignal(
        ts = datetime.now()
        , pcellid = signal.pcellid
        , rsrq = signal.rsrq
        , rsrp = signal.rsrp
        , frequency_band = signal.frequency_band
        , dlbw = signal.dlbw
        , ulbw = signal.ulbw
    )
    db.add(db_signal)
    db.commit()
    db.refresh(db_signal)
    return db_signal

@app.get('/get_last_signal/')
def get_last_signal(signal: Signal):
    return signal

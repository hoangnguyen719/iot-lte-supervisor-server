from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

import models
from database import engine, SessionLocal
from models import Song, LteSignal
from schemas import Signal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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
        , scellid = signal.scellid
        , mcc = signal.mcc
        , mnc = signal.mnc
        , rsrq = signal.rsrq
        , rsrp = signal.rsrp
        # , frequency_band = signal.frequency_band
        # , dlbw = signal.dlbw
        # , ulbw = signal.ulbw
    )
    db.add(db_signal)
    db.commit()
    db.refresh(db_signal)
    return db_signal

@app.get('/get_signals/')
def get_signal(
    pcellid: str | None = None
    , signal_count: int = 1
    , db: Session = Depends(get_db)
    ):
    with db:
        statement = select(LteSignal)
        if pcellid:
            statement = statement.where(LteSignal.pcellid == pcellid)
        statement = statement.order_by(LteSignal.ts.desc()).limit(signal_count)
        results = db.execute(statement)
        results = results.all()
    return results[0]["LteSignal"]

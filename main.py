from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

import models
from database import engine, SessionLocal
from models import Song, LteSignal, LteCell
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

@app.get('/cell/')
def read_lte(db: Session = Depends(get_db)):
    return db.query(LteCell).all()

@app.post('/post_signal/')
def post_signal(signal: Signal, db: Session = Depends(get_db)):
    current_dt = datetime.now()
    with db:
        # Add signal to table
        db_signal = LteSignal(
            ts = current_dt
            , scellid = signal.scellid
            , rsrq = signal.rsrq
            , rsrp = signal.rsrp
        )
        db.add(db_signal)
        db.commit()
        db.refresh(db_signal)

        # Update Cell table
        db_cell = db.get(LteCell, signal.scellid)
        if not db_cell:
            db_cell = LteCell(
                pcellid = signal.pcellid
                , scellid = signal.scellid
                , mcc = signal.mcc
                , mnc = signal.mnc
                , last_seen = current_dt
            )
        else:
            setattr(db_cell, 'last_seen', current_dt)
        db.add(db_cell)
        db.commit()
        db.refresh(db_cell)

    return signal

@app.get('/get_signals/')
def get_signal(
    scellid: str | None = None
    , signal_count: int = 1
    , db: Session = Depends(get_db)
    ):
    with db:
        statement = select(LteSignal)
        if scellid:
            statement = statement.where(LteSignal.scellid == scellid)
        statement = statement.order_by(LteSignal.ts.desc()).limit(signal_count)
        results = db.execute(statement)
        results = results.all()
    return results[0]["LteSignal"]

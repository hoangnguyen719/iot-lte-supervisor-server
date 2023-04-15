from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

import models, crud
from database import engine, SessionLocal
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
    return crud.read_root()

@app.get('/songs/')
def read_songs(db: Session = Depends(get_db)):
    return crud.read_songs(db=db)

@app.get('/lte/')
def read_lte(db: Session = Depends(get_db)):
    return crud.read_lte(db=db)

@app.get('/cell/')
def read_cell(db: Session = Depends(get_db)):
    return crud.read_cell(db=db)

@app.post('/post_signal/')
def post_signal(signal: Signal, db: Session = Depends(get_db)):
    current_dt = datetime.now()
    db_signal = crud.append_signal(signal, db, current_dt)
    db_cell = crud.update_cell(signal, db, current_dt)
    return db_signal, db_cell

@app.get('/get_last_signal/')
def get_last_signal(db: Session = Depends(get_db)):
    return crud.get_last_signal(db=db)

@app.get('/get_last_cell/')
def get_last_cell(db: Session = Depends(get_db)):
    return crud.get_last_cell(db=db)

@app.get('/get_signals/')
def get_signals(
    scellid: str | None = None
    , signal_count: int = 10
    , db: Session = Depends(get_db)
    ):
    return crud.get_signals(db=db, scellid=scellid, signal_count=signal_count)

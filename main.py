from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
from models import Song, LteSignal

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
def read_songs(db: Session = Depends(get_db)):
    return db.query(LteSignal).all()

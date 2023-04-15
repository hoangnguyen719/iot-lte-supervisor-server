from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select

import models, schemas


def read_root():
    return {'name': 'fastapi-songs'}

def read_songs(db: Session):
    return db.query(models.Song).all()

def read_lte(db: Session):
    return db.query(models.LteSignal).all()

def read_lte(db: Session):
    return db.query(models.LteCell).all()

def update_lte_cell(signal: schemas.Signal, db: Session):
    current_dt = datetime.now()
    with db:
        # Append signal to table
        db_signal = models.LteSignal(
            ts = current_dt
            , scellid = signal.scellid
            , rsrq = signal.rsrq
            , rsrp = signal.rsrp
        )
        db.add(db_signal)
        db.commit()
        db.refresh(db_signal)

        # Update Cell table
        db_cell = db.get(models.LteCell, signal.scellid)
        if not db_cell:
            db_cell = models.LteCell(
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
    return db_signal, db_cell

def get_last_signal(db: Session):
    with db:
        statement = select(models.LteSignal)
        statement = statement.order_by(models.LteSignal.ts.desc()).limit(1)
        results = db.execute(statement)
        results = results.all()
    return results[0]["LteSignal"]

def get_signals(
    db: Session
    , scellid: str | None = None
    , signal_count: int = 1
    ):
    with db:
        statement = select(models.LteSignal)
        if scellid:
            statement = statement.where(models.LteSignal.scellid == scellid)
        statement = statement.order_by(models.LteSignal.ts.desc()).limit(signal_count)
        results = db.execute(statement)
        results = results.all()
    return results[0]["LteSignal"]
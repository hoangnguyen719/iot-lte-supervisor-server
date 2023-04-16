from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy import select
from datetime import datetime, timedelta

import models, schemas, database


def read_root():
    return {
        'See API at': '/docs#/'
    }

def read_all_lte_signals(db: Session):
    return db.query(models.LteSignal).all()

def read_all_cells(db: Session):
    return db.query(models.LteCell).all()

def read_all_frequency(db: Session):
    return db.query(models.CurrentFrequency).all()

def get_last_value(db: Session, model: database.Base, sort_attr: InstrumentedAttribute):
    with db:
        statement = select(model).order_by(sort_attr.desc()).limit(1)
        results = db.execute(statement)
        results = results.all()
    if len(results) > 0:
        return results[0][model.__name__]
    else:
        return None

def get_last_signal(db: Session):
    signal = get_last_value(db=db, model=models.LteSignal, sort_attr=models.LteSignal.ts)
    if signal:
        signal.ts = ts_plus_7_hour(signal.ts)
    return signal

def get_last_cell(db: Session):
    cell = get_last_value(db=db, model=models.LteCell, sort_attr=models.LteCell.last_seen)
    if cell:
        cell.first_seen = ts_plus_7_hour(cell.first_seen)
        cell.last_seen = ts_plus_7_hour(cell.last_seen)
    return cell

def get_current_frequency(db: Session):
    cur_freq = get_last_value(
        db=db, model=models.CurrentFrequency, sort_attr=models.CurrentFrequency.updated_at
    )
    if cur_freq: return cur_freq.frequency
    else: return None

def rsrp_index2dbm(index):
    return index - 140

def rsrq_index2dbm(index):
    return index/2 - 19.5

def append_signal(signal: schemas.Signal, db: Session, dt: datetime):
    with db:
        # Append signal to table
        db_signal = models.LteSignal(
            ts = dt
            , scellid = signal.scellid
            , rsrq = signal.rsrq
            , rsrp = signal.rsrp
            , rsrq_db = rsrq_index2dbm(signal.rsrq)
            , rsrp_dbm = rsrp_index2dbm(signal.rsrp)
        )
        db.add(db_signal)
        db.commit()
        db.refresh(db_signal)
    return db_signal

def update_cell(signal: schemas.Signal, db: Session, dt: datetime):
    # If cell is the same as last cell, update `last_seen`
    # Otherwise, append the cell as a new cell
    with db:
        # Get last cell
        last_cell = get_last_cell(db)
        new_cell = models.LteCell(
            pcellid = signal.pcellid
            , scellid = signal.scellid
            , mcc = signal.mcc
            , mnc = signal.mnc
            , first_seen = dt
            , last_seen = dt
        )

        if last_cell is None:
            last_cell = new_cell
        elif last_cell.scellid != new_cell.scellid:
            last_cell = new_cell
        else:
            setattr(last_cell, 'last_seen', dt)
        db.add(last_cell)
        db.commit()
        db.refresh(last_cell)
    return last_cell

def update_current_frequency(freq: schemas.Frequency, db: Session, dt: datetime):
    new_freq = freq.frequency
    with db:
        # Truncate current_frequency
        db.query(models.CurrentFrequency).delete()

        # Append new data
        new_freq = models.CurrentFrequency(
            updated_at = dt
            , frequency = freq.frequency
        )
        db.add(new_freq)
        db.commit()
        db.refresh(new_freq)
    return new_freq

def get_n_signals(
    db: Session
    , signal_count: int
    # , scellid: str | None = None
):
    with db:
        statement = select(models.LteSignal)
        # if scellid:
        #     statement = statement.where(models.LteSignal.scellid == scellid)
        statement = statement.order_by(models.LteSignal.ts.desc()).limit(signal_count)
        results = db.execute(statement)
        results = results.all()
    return format_signals(signals=results, ts_format=lambda x: ts_plus_7_hour(x))

def get_1h_signals(
    db: Session
    # , scellid: str | None = None
):
    last_1hr = datetime.now() - timedelta(hours=1)
    with db:
        statement = select(models.LteSignal)
        # if scellid:
        #     statement = statement.where(models.LteSignal.scellid == scellid)
        statement = statement.where(models.LteSignal.ts >= last_1hr)
        statement = statement.order_by(models.LteSignal.ts.desc())
        results = db.execute(statement)
        results = results.all()
    return format_signals(
        signals=results
        , ts_format=lambda x: ts_plus_7_hour(x).strftime('%H:%M:%S')
    )

def format_signals(signals, ts_format=lambda x: x.strftime('%H')):
    formated_results = {
        'ts': [], 'rsrp_dbm': [], 'rsrq_db': []
    }
    for r in list(reversed([s["LteSignal"] for s in signals])):
        formated_results['ts'].append(ts_format(r.ts))
        formated_results['rsrp_dbm'].append(r.rsrp_dbm)
        formated_results['rsrq_db'].append(r.rsrq_db )
    return formated_results

def ts_plus_7_hour(ts):
    return ts + timedelta(hours=7)
from datetime import datetime

import models
from database import engine, SessionLocal
from models import LteSignal

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(LteSignal).count() == 0:
    lte_signals = [
        LteSignal(
            ts = datetime(2023,4,12,23,37,30)
            , pcellid = 'xya-ced13'
            , mcc = 0
            , mnc = 0
            , rsrq = 10
            , rsrp = -10
            , frequency_band = 5
            , dlbw = -999
            , ulbw = 999
            )
    ]

    for signal in lte_signals:
        db.add(signal)

    db.commit()

import sys
from datetime import date, datetime

import models
from database import engine, SessionLocal
from models import Song, LteSignal

models.Base.metadata.create_all(bind=engine)

# Example data
TABLES = {
    'songs': {
        'model': Song
        , 'data': [
            Song(title='Smells Like Teen Spirit', artist='Nirvana', release_date=date(1991, 9, 10)),
            Song(title='Here Comes The Sun', artist='The Beatles', release_date=date(1969, 8, 19)),
            Song(title='Karma Police', artist='Radiohead', release_date=date(1997, 8, 25)),
            Song(title='Get Lucky', artist='Daft Punk', release_date=date(2013, 4, 19)),
            ]
    }
    , 'lte_signal': {
        'model': LteSignal
        , 'data': [
            LteSignal(
                ts = datetime(2023,4,12,23,37,30)
                , pcellid = 'pcellid-xyz'
                , scellid = 'scellid-abc'
                , mcc = '0'
                , mnc = '0'
                , rsrq = '10'
                , rsrp = '-10'
                # , frequency_band = '5'
                # , dlbw = '-999'
                # , ulbw = '999'
                )
                ]
    }
}

db = SessionLocal()

# Check for table names
names = sys.argv[1:]
if (len(names) == 0) & (names == ['.']):
    names = TABLES.keys()

# Add data to tables
for name in TABLES:
    model = TABLES[name]['model']
    data = TABLES[name]['data']
    if db.query(model).count() == 0:
        print(name)
        for row in data:
            db.add(row)

        db.commit()

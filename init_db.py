import argparse
import sqlalchemy as sa

from database import engine, SessionLocal
from tables import TABLES, TABL_NAMES
import models

models.Base.metadata.create_all(bind=engine)
# Get keyword argument
parser = argparse.ArgumentParser(description="Initiate tables in the database.")
parser.add_argument(
    '-d', '--data', choices=['yes', 'no'], required=False, default='no'
    )
parser.add_argument(
    '-t', '--tables'
    , choices=TABL_NAMES, default=TABL_NAMES, nargs='+'
    , required=False
    )
args = parser.parse_args()
tables = args.tables
dummy_data = (args.data=='yes')

db = SessionLocal()
insp = sa.inspect(engine)

for name in tables:
    # Create table if not existing
    model = TABLES[name]['model']
    if not insp.has_table(name):
        model.__table__.create(engine)
        msg = f'Create {name}.'
    else:
        msg = f'{name} already exists.'

    # Adding data if table is empty 
    if dummy_data:
        data = TABLES[name]['data']
        if db.query(model).count() == 0:
            for row in data:
                db.add(row)

            db.commit()
            msg += ' Add dummy data.'
    print(msg)

import sys
import sqlalchemy as sa

from models import LteSignal, Song
from database import engine

TABLES = {
    'lte_signals': LteSignal
    , 'songs': Song
}
insp = sa.inspect(engine)

# Check for table names
names = sys.argv[1:]
if len(names) == 0:
    raise Exception('Must specify a table name or . for all tables!')
elif names == ['.']:
    names = TABLES.keys()

# Drop tables by their names
for name in names:
    if name not in TABLES:
        raise Exception(f'Table {name} not existing!')
    else:
        table = TABLES[name]
        # if engine.dialect.has_table(engine, name):
        if insp.has_table(name):
            print(name)
            table.__table__.drop(engine)
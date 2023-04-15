import sys
import sqlalchemy as sa

from database import engine
from tables import TABLES, TABL_NAMES

insp = sa.inspect(engine)

# Check for table names
names = sys.argv[1:]
if len(names) == 0:
    raise Exception('Must specify a table name or . for all tables!')
elif names == ['.']:
    names = TABL_NAMES

# Drop tables by their names

for name in names:
    if name not in TABLES:
        raise Exception(f'Table {name} not existing!')
    else:
        model = TABLES[name]['model']
        # if engine.dialect.has_table(engine, name):
        if insp.has_table(name):
            print(name)
            model.__table__.drop(engine)
import sqlalchemy as sa

from database import engine, SessionLocal
from tables import TABLES, TABL_NAMES
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# for name in tables:
for name in TABL_NAMES:
    model = TABLES[name]['model']
    data = TABLES[name]['data']
    if db.query(model).count() == 0:
        for row in data:
            db.add(row)
            db.commit()

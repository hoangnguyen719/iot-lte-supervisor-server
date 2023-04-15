from sqlalchemy import Column, Integer, String, Float, DateTime

from database import Base

class LteSignal(Base):
    __tablename__ = 'lte_signals'

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime, nullable=False)
    scellid = Column(String(128), nullable=False)
    rsrq = Column(Integer, nullable=False)
    rsrp = Column(Integer, nullable=False)
    rsrq_dbm = Column(Float, nullable=False)
    rsrp_dbm = Column(Float, nullable=False)


class LteCell(Base):
    __tablename__ = 'lte_cells'

    id = Column(Integer, primary_key=True)
    scellid = Column(String(128), nullable=False)
    pcellid = Column(String(128), nullable=False)
    mcc = Column(String(128), nullable=False)
    mnc = Column(String(128), nullable=False)
    first_seen = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False)

class CurrentFrequency(Base):
    __tablename__ = 'current_frequency'

    updated_at = Column(DateTime, nullable=False, primary_key=True)
    frequency = Column(Integer, nullable=False)  # In seconds

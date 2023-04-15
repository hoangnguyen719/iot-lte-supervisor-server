from sqlalchemy import Column, Integer, String, Date, DateTime

from database import Base


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    artist = Column(String(128), nullable=False)
    release_date = Column(Date, nullable=False)

class LteSignal(Base):
    __tablename__ = 'lte_signals'

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime, nullable=False)
    scellid = Column(String(128), nullable=False)
    rsrq = Column(String(128), nullable=False)
    rsrp = Column(String(128), nullable=False)


class LteCell(Base):
    __tablename__ = 'lte_cells'

    id = Column(Integer, primary_key=True)
    scellid = Column(String(128), nullable=False)
    pcellid = Column(String(128), nullable=False)
    mcc = Column(String(128), nullable=False)
    mnc = Column(String(128), nullable=False)
    first_seen = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False)


class FrequencyHistory(Base):
    __tablename__ = 'frequency_history'

    id = Column(Integer, primary_key=True)
    ts = Column(DateTime, nullable=False)
    frequency = Column(Integer, nullable=False)  # In seconds

class CurrentFrequency(Base):
    __tablename__ = 'current_frequency'

    updated_at = Column(DateTime, nullable=False)
    frequency = Column(Integer, nullable=False)  # In seconds

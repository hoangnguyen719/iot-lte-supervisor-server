from datetime import datetime

from pydantic import BaseModel

class Signal(BaseModel):
    ts = datetime.now()
    pcellid: str
    scellid: str
    mcc: str
    mnc: str
    rsrq: int
    rsrp: int

    class Config:
        orm_mode = True

class Frequency(BaseModel):
    ts = datetime.now()
    frequency: int
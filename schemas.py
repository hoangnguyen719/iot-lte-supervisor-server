from datetime import datetime

from pydantic import BaseModel

class Signal(BaseModel):
    pcellid: str
    scellid: str
    mcc: str
    mnc: str
    rsrq: int
    rsrp: int

    class Config:
        orm_mode = True

class Frequency(BaseModel):
    frequency: int
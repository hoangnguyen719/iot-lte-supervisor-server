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
    # frequency_band: int
    # dlbw: int
    # ulbw: int

    class Config:
        orm_mode = True
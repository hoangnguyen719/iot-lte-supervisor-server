from pydantic import BaseModel

class Signal(BaseModel):
    ts = datetime.now()
    pcellid: str
    rsrq: int
    rsrp: int
    frequency_band: int
    dlbw: int
    ulbw: int

    class Config:
        orm_mode = True
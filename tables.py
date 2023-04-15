from datetime import datetime

from models import LteSignal, LteCell, CurrentFrequency

# Example data
TABLES = {
    'lte_signals': {
        'model': LteSignal
        , 'data': [
            LteSignal(
                ts = datetime(2023,4,12,23,37,30)
                , scellid = 'scellid'
                , rsrq = 100
                , rsrp = 100
                , rsrq_db = (100/2)-19.5
                , rsrp_dbm = 100-140
            )
        ]
    }
    , 'lte_cells': {
        'model': LteCell
        , 'data': [
            LteCell(
                pcellid = 'pcellid'
                , scellid = 'scellid'
                , mcc = '0'
                , mnc = '0'
                , first_seen = datetime(2023,4,12,23,37,30) 
                , last_seen = datetime(2023,4,12,23,37,30)
            )
        ]
    }
    , 'current_frequency': {
        'model': CurrentFrequency
        , 'data': [
            CurrentFrequency(
                updated_at = datetime(2023,4,12,23,37,30)
                , frequency = 2 # In seconds
            )
        ]
    }
}
TABL_NAMES = list(TABLES.keys())
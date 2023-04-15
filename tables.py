from datetime import date, datetime

from models import Song, LteSignal

# Example data
TABLES = {
    'songs': {
        'model': Song
        , 'data': [
            Song(title='Smells Like Teen Spirit', artist='Nirvana', release_date=date(1991, 9, 10)),
            Song(title='Here Comes The Sun', artist='The Beatles', release_date=date(1969, 8, 19)),
            Song(title='Karma Police', artist='Radiohead', release_date=date(1997, 8, 25)),
            Song(title='Get Lucky', artist='Daft Punk', release_date=date(2013, 4, 19)),
            ]
    }
    , 'lte_signals': {
        'model': LteSignal
        , 'data': [
            LteSignal(
                ts = datetime(2023,4,12,23,37,30)
                , pcellid = 'pcellid-xyz'
                , scellid = 'scellid-abc'
                , mcc = '0'
                , mnc = '0'
                , rsrq = '10'
                , rsrp = '-10'
                # , frequency_band = '5'
                # , dlbw = '-999'
                # , ulbw = '999'
                )
                ]
    }
}
TABL_NAMES = list(TABLES.keys())
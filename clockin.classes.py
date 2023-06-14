from datetime import datetime as dt

class DtExtend:
    def empty_datetime() -> dt:
        now: dt = dt.now()
        return now - now
    
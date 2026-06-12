from typing import Any, Callable, Optional
from datetime import datetime, timezone as tz
import datetime as dt

SUP_F = "\u1DA0"
SUP_P = "\u1D56"

class Streak:
    def __init__(self, condition: Callable[[int], bool]):
        self.longest = []
        self.current = []
        self._is_continued = condition

    def update(self, value: int, description: Optional[Any] = None):
        if self._is_continued(value):
            self.current.append(description)
            return

        if len(self.current) > len(self.longest):
            self.longest = self.current
        
        self.current = []

    def __str__(self):
        longest = self.get()

        if len(longest) == 0:
            return ''
    
        return f"{longest[0]} ... {longest[-1]}"

    def get(self):
        return max(self.longest, self.current, key=len)

class Date:
    """
    Class to manage UTC dates.
    Takes in ISO formatted date and optionally time
    """
    def __init__(
        self, 
        date: Optional[str],
        time: Optional[str] = None, 
    ):
        self._date = None
        self._time = None

        today = self.today()

        if date == "today":
            self._date = today.date()
            self._time = today.time()
        else:    
            if date: 
                self._date = dt.date.fromisoformat(date)
            if time: 
                self._time = dt.time.fromisoformat(time)
        
        com_date = ifnone(self._date, today.date())
        com_time = ifnone(self._time, today.time())

        self._combined = datetime.combine(com_date, com_time, tz.utc)

    def date(self, as_local = True, fmt: str = "%b %d", fallback: str = "???") -> str:
        if self._date is None:
            return fallback

        interm = self._combined.astimezone() if as_local else \
                 self._combined

        return datetime.strftime(interm, fmt)

    def time(self, as_local = True, fmt: str = "%H:%M", fallback: str = "???") -> str:
        if self._time is None:
            return fallback
        
        interm = self._combined.astimezone() if as_local else \
                 self._combined

        return datetime.strftime(interm, fmt)

    def year(self) -> int:
        return self._combined.year

    def __lt__(self, other):
        return self._combined < other._combined

    def __gt__(self, other):
        return self._combined > other._combined

    def today(is_utc=True) -> datetime:
        if is_utc:
            return datetime.now(tz=tz.utc)
        return datetime.now()

class Today(Date):
    def __init__(self):
        super().__init__("today")

def strsign(value: int):
    sign = '+' if value > 0 else ''
    return f"{sign}{value}"

def ifnone(data: Any, then: Any):
    return data if data is not None else then

def addif(data: Any, condition: bool, then: Any):
    return data + then if condition else data

def annotate_pf(data: Any, is_pole: bool, is_fastest: bool):
    return addif(
        addif(data, is_pole, SUP_P),
    is_fastest, SUP_F)
    
def separator(width=50):
    return '-' * width

def print_comments(comments: list[str]):
    print('\n'.join(comments), end="\n\n")

def format_date(date: str, is_local: bool = True):
    return Date(date).date(as_local=is_local)
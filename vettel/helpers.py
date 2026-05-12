from typing import Any, Callable, Optional
from datetime import datetime

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

def get_today():
    return datetime.today()

def get_current_year():
    return datetime.now().year

def try_parse_date(
    date: Optional[str], 
    format: str = "%Y-%m-%d"
) -> Optional[datetime]:
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except TypeError:
        return None
    

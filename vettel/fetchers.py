import sqlite3

from typing import Any, List, Optional, Iterable
from pprint import pprint

from vettel.helpers import Today
from vettel.database import F1DB

# My attempt on saving ugly bulky python types
Headers = List[str]
Row = sqlite3.Row
Rows = List[Row]
DictRows = List[dict]
Cursor = sqlite3.Cursor
Opt = Optional

def dict_row_factory(cursor: Cursor, row: Row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

class Fetcher:
    def __init__(self):
        self.db = F1DB()

    def _db_get_as_dict(self, script: str, params: Iterable):
        cur = self.db.con.cursor()
        cur.row_factory = dict_row_factory
        return self.db.run_script(script, self.params, overwrite_cursor=cur)

    def _get_raw_sql(self, sql: str, params: Opt[Iterable]) -> tuple[Headers, Opt[Rows]]:
        rows = self.db.execute(sql, params)
        headers = [c[0] for c in self.db.cur.description]
        return headers, rows

    def row_to_dict(self, row: Row, headers: Headers) -> Opt[dict]:
        if not headers:
            return None

        return {header: row[idx] for idx, header in enumerate(headers)}

class Race(Fetcher):
    def __init__(self, id: str, year: Opt[int]):
        super().__init__()
        if not year:
            year = Today().year()
        
        self.id = id
        self.year = year
        self.params = {"id": id, "year": year}

        self.quali_script = "qualifying-pre-2006" if year < 2006 else \
                            "qualifying"

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script("race", self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("race")
        
    def get_quali(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script(self.quali_script, self.params)

    def get_quali_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict(self.quali_script)

class Sprint(Fetcher):
    def __init__(self, id: str, year: Opt[int]):
        super().__init__()
        if not year:
            year = Today().year()
        
        self.id = id
        self.year = year
        self.params = {"id": id, "year": year}

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script("sprint", self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("sprint")

    def get_quali(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script("sprint-qualifying", self.params)

    def get_quali_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("sprint-qualifying")

class Results(Fetcher):
    def __init__(self, year: Opt[int], is_quali: bool):
        super().__init__()
        if not year:
            year = Today().year()
        
        self.year = year
        self.params = [year]
        self.script = "qualifying-results" if is_quali else \
                      "results"

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script(self.script, self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict(self.script)

class Driver(Fetcher):
    def __init__(self, id: str, year: Opt[int]):
        super().__init__()
        if not year:
            year = Today().year()
        
        self.id = id
        self.year = year
        self.params = {"id": self.id, "year": self.year}

    def __all_time_dynamic(self, script: str, is_all_time: bool):
        params = {"id": self.id}
        extra_sql = ""

        if not is_all_time:
            params["year"] = self.year
            extra_sql = " and r.year = :year"

        return self.db.run_script(script, params, extra_sql)

    def get_races(self, is_all_time: bool):
        return self.__all_time_dynamic("driver/races", is_all_time)
        
    def get_qualifying(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/qualifying", is_all_time)

    def get_sprints(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/sprints", is_all_time)

    def get_overview(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/overview", is_all_time)

    def get_pits(self) -> tuple[Headers, Opt[Rows]]:
        return self.db.run_script("driver/pits", self.params)

class Raw(Fetcher):
    def __init__(self):
        super().__init__()

    def get(self, sql: str, params: Opt[Iterable]):
        return self._get_raw_sql(sql, params)

class Misc(Fetcher):
    def __init__(self):
        super().__init__()

    def get_gps(self, year: Opt[int]):
        sql = """
            SELECT 
                grand_prix.id, 
                grand_prix.abbreviation 
            FROM grand_prix 
            JOIN race on race.year = ? 
            WHERE race.grand_prix_id = grand_prix.id
        """

        if not year:
            year = Today().year()
        
        return self._get_raw_sql(sql, [year])

    def get_season_gps(self, year: Opt[int]):
        if not year:
            year = Today().year()

        return self.db.run_script("season", {"year": year})
from sqlite3 import Row, Cursor

from typing import List, Optional, Iterable

from .helpers import Today
from .database import DB

# My attempt on saving ugly bulky python types
Headers = List[str]
Rows = List[Row]
DictRows = List[dict]
Opt = Optional

def dict_row_factory(cursor: Cursor, row: Row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

class Fetcher:
    def _db_get_as_dict(self, script: str, params: Opt[Iterable]):
        cur = DB.con.cursor()
        cur.row_factory = dict_row_factory
        return DB.run_script(script, params, overwrite_cursor=cur)

    def _get_raw_sql(self, sql: str, params: Opt[Iterable]) -> tuple[Headers, Opt[Rows]]:
        rows = DB.execute(sql, params)
        headers = [c[0] for c in DB.cur.description]
        return headers, rows

    def row_to_dict(self, row: Row, headers: Headers) -> Opt[dict]:
        if not headers:
            return None

        return {header: row[idx] for idx, header in enumerate(headers)}

class Race(Fetcher):
    def __init__(self, id: str, year: int):
        super().__init__()
        self.id = id
        self.year = year
        self.params = {"id": id, "year": year}

        self.quali_script = "race/qualifying-pre-2006" if year < 2006 else \
                            "race/qualifying"

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script("race/race", self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("race/race", self.params)
        
    def get_quali(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script(self.quali_script, self.params)

    def get_quali_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict(self.quali_script, self.params)

class Sprint(Fetcher):
    def __init__(self, id: str, year: int):
        super().__init__()
        self.id = id
        self.year = year
        self.params = {"id": id, "year": year}

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script("sprint/sprint", self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("sprint/sprint", self.params)

    def get_quali(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script("sprint/qualifying", self.params)

    def get_quali_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict("sprint/qualifying", self.params)

class Results(Fetcher):
    def __init__(self, year: int, is_quali: bool):
        super().__init__()
        self.year = year
        self.params = [year]
        self.script = "results/qualifying" if is_quali else \
                      "results/results"

    def get(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script(self.script, self.params)

    def get_as_dict(self) -> tuple[Headers, Opt[DictRows]]:
        return self._db_get_as_dict(self.script, self.params)

class Driver(Fetcher):
    def __init__(self, id: str, year: int):
        super().__init__()
        self.id = id
        self.year = year
        self.params = {"id": self.id, "year": self.year}

    def __all_time_dynamic(self, script: str, is_all_time: bool):
        params = {"id": self.id}
        extra_sql = ""

        if not is_all_time:
            params["year"] = self.year
            extra_sql = " and r.year = :year"

        return DB.run_script(script, params, extra_sql)

    def get_races(self, is_all_time: bool):
        return self.__all_time_dynamic("driver/races", is_all_time)
        
    def get_qualifying(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/qualifying", is_all_time)

    def get_sprints(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/sprints", is_all_time)

    def get_overview(self, is_all_time: bool) -> tuple[Headers, Opt[Rows]]:
        return self.__all_time_dynamic("driver/overview", is_all_time)

    def get_pits(self) -> tuple[Headers, Opt[Rows]]:
        return DB.run_script("driver/pits", self.params)

class Misc(Fetcher):
    def __init__(self):
        super().__init__()

    def raw_sql(self, sql: str, params: Opt[Iterable]):
        return self._get_raw_sql(sql, params)

    def raw_script(self, script: str, params: Opt[Iterable] = None):
        return DB.run_script(script, params)

    def get_season_gps(self, year: int):
        return DB.run_script("season", {"year": year})

    def get_calendar(self, year: int):
        return DB.run_script("calendar", [year])

    def get_gps(self, year: int):
        sql = """
            SELECT 
                grand_prix.id, 
                grand_prix.abbreviation 
            FROM grand_prix 
            JOIN race on race.year = ? 
            WHERE race.grand_prix_id = grand_prix.id
        """

        return self._get_raw_sql(sql, [year])

    def get_circuit_info(self, id: str): 
        sql = """
            SELECT 
                circuit.*, 
                GROUP_CONCAT(race.year ,',') as years 
            FROM circuit 
            JOIN race on race.circuit_id = :id 
            WHERE circuit.id = :id
        """

        return self._get_raw_sql(sql, {"id": id})
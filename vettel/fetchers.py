import sqlite3, os

from typing import Any, List, Optional, Iterable
from pprint import pprint

from vettel.helpers import (
    Today
)

# My attempt on saving ugly bulky python types
Headers = List[str]
Row = sqlite3.Row
Rows = List[Row]
DictRows = List[dict]
Cursor = sqlite3.Cursor
Opt = Optional

DB_SOURCE = "https://github.com/f1db/f1db/releases/latest/download/f1db-sqlite.zip"
DB_ZIP_NAME = "f1db-sqlite.zip"
DB_NAME = "f1db.db"

def dict_row_factory(cursor: Cursor, row: Row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

class F1DB:
    if xdg := os.getenv("XDG_DATA_HOME"):
        db_dir = os.path.join(xdg, "vettel")
    else:
        db_dir = os.path.expanduser("~/.local/share/vettel")

    db_file = os.path.join(db_dir, DB_NAME)

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.realpath(__file__))
        self.sql_scripts_dir = os.path.join(self.root_dir, "sql")
        
        if not os.path.exists(self.db_file):
            print("No database found, installing...")
            self.update()

        self.con = sqlite3.connect(self.db_file)
        self.cur = self.con.cursor()

    def run_script(
        self, 
        name: str, 
        params: Iterable = [],
        extra_sql: Opt[str] = None,
        overwrite_cursor: Opt[Cursor] = None
    ) -> tuple[Headers, Opt[Rows]]:
        script = os.path.join(self.sql_scripts_dir, name + ".sql")

        cur = overwrite_cursor if overwrite_cursor else \
              self.cur

        with open(script) as s:
            sql = s.read()

        if extra_sql:
            sql += extra_sql

        cur.execute(sql, params)
        return [c[0] for c in cur.description], cur.fetchall()

    def run_file(self, file: str) -> tuple[Headers, Rows]:
        with open(file) as f:
            self.cur.execute(f.read())

        return (
            [c[0] for c in self.cur.description],
            self.cur.fetchall()
        )

    def update(self):
        os.makedirs(self.db_dir, exist_ok=True)
        os.chdir(self.db_dir)
        
        if os.path.exists(self.db_file):
            os.remove(self.db_file) 

        print(f"Downloading database: {DB_SOURCE}...")

        try:
            with urlopen(DB_SOURCE) as remote, open(DB_ZIP_NAME, "wb") as local:
                local.write(remote.read())

        except Exception as e:
            sys.stderr.write(f"Error while downloading: {e}\n")

        print(f"Extracting {DB_ZIP_NAME}...")

        try:
            with ZipFile(DB_ZIP_NAME) as z:
                z.extractall()
        except Exception as e:
            sys.stderr.write(f"Error while extracting: {e}\n")

        os.remove(DB_ZIP_NAME)
        print("Database was installed successfully!")

    def execute(self, sql: str, params: Opt[Iterable]) -> Rows:
        self.cur.execute(sql, params)
        return self.cur.fetchall()

class Fetcher:
    def __init__(self):
        self.db = F1DB()

    def _db_get_as_dict(self, script: str, params: Iterable):
        cur = self.db.con.cursor()
        cur.row_factory = dict_row_factory
        return self.db.run_script(script, self.params, overwrite_cursor=cur)

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


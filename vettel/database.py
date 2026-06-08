import os, sqlite3, sys

from urllib.request import urlopen
from zipfile import ZipFile

DB_SOURCE = "https://github.com/f1db/f1db/releases/latest/download/f1db-sqlite.zip"
DB_ZIP_NAME = "f1db-sqlite.zip"
DB_NAME = "f1db.db"

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
import os, sys

from sqlite3 import Cursor, connect as sql_connect
from typing import Iterable, Optional as Opt

from urllib.request import urlopen
from zipfile import ZipFile

DB_SOURCE = "https://github.com/f1db/f1db/releases/latest/download/f1db-sqlite.zip"
DB_ZIP_NAME = "f1db-sqlite.zip"
DB_FILE_NAME = "f1db.db"

class F1DB:
    if xdg := os.getenv("XDG_DATA_HOME"):
        db_dir = os.path.join(xdg, "vettel")
    else:
        db_dir = os.path.expanduser("~/.local/share/vettel")

    db_file = os.path.join(db_dir, DB_FILE_NAME)

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.realpath(__file__))
        self.scripts_dir = os.path.join(self.root_dir, "sql")
        
        if not os.path.exists(self.db_file):
            self.update()
            exit(0)

        self.con = sql_connect(self.db_file)
        self.cur = self.con.cursor()

    def run_script(
        self, 
        script: str, 
        params: Iterable = [],
        extra_sql: Opt[str] = None,
        cursor: Opt[Cursor] = None
    ):
        script = os.path.join(self.scripts_dir, script + ".sql")

        if not cursor:
            cursor = self.cur

        with open(script) as s:
            sql = s.read()

        if extra_sql:
            sql += extra_sql

        cursor.execute(sql, params)
        return self.get_columns(cursor), cursor.fetchall()

    def run_file(self, file: str):
        with open(file) as f:
            self.cur.execute(f.read())

        return (
            self.get_columns(),
            self.cur.fetchall()
        )

    def execute(self, sql: str, params: Iterable = [], cursor: Opt[Cursor] = None):
        if not cursor:
            cursor = self.cur

        cursor.execute(sql, params)
        return cursor.fetchall()

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

    def get_columns(self, cursor: Opt[Cursor] = None):
        if not cursor:
            cursor = self.cur
        return [c[0] for c in cursor.description]

DB = F1DB()